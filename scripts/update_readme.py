#!/usr/bin/env python3
"""Verify APKs in apks/ and update the APK list section in README.md."""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import quote

APKS_DIR = Path("apks")
README_PATH = Path("README.md")
DESCRIPTIONS_PATH = Path("app-descriptions.json")

START_MARKER = "<!-- APK-LIST-START -->"
END_MARKER = "<!-- APK-LIST-END -->"


def get_build_tool(tool_name: str) -> str:
    env_key = tool_name.upper()
    if env_key in os.environ and os.environ[env_key]:
        return os.environ[env_key]

    android_home = os.environ.get("ANDROID_HOME") or os.environ.get("ANDROID_SDK_ROOT")
    build_tools_version = os.environ.get("BUILD_TOOLS_VERSION", "35.0.0")
    if android_home:
        candidate = Path(android_home) / "build-tools" / build_tools_version / tool_name
        if candidate.exists():
            return str(candidate)

    return tool_name


def run_cmd(cmd: list[str]) -> str:
    result = subprocess.run(cmd, capture_output=True, text=True)
    combined = f"{result.stdout}\n{result.stderr}".strip()
    if result.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(cmd)}\n{combined}")
    return combined


def extract_apk_metadata(aapt2: str, apk_path: Path) -> tuple[str, str]:
    output = run_cmd([aapt2, "dump", "badging", str(apk_path)])

    label_match = (
        re.search(r"^application-label:'([^']+)'", output, re.MULTILINE)
        or re.search(r"^application-label-[a-zA-Z0-9_-]+:'([^']+)'", output, re.MULTILINE)
        or re.search(r"application:\s+label='([^']+)'", output)
    )
    app_name = label_match.group(1).strip() if label_match else apk_path.stem

    version_match = re.search(r"versionName='([^']*)'", output)
    if not version_match or not version_match.group(1).strip():
        raise RuntimeError(f"Could not read versionName from {apk_path.name}")

    return app_name, version_match.group(1).strip()


def verify_and_get_cert_sha256(
    apksigner: str, apk_path: Path, expected_cert: str | None
) -> str:
    output = run_cmd([apksigner, "verify", "--verbose", "--print-certs", str(apk_path)])

    cert_match = re.search(
        r"Signer #1 certificate SHA-256 digest:\s*([0-9a-fA-F]+)", output
    )
    if not cert_match:
        raise RuntimeError(f"Could not read signing certificate SHA-256 for {apk_path.name}")

    cert_sha256 = cert_match.group(1).upper()

    if expected_cert:
        normalized_expected = re.sub(r"[:\s]", "", expected_cert).upper()
        if cert_sha256 != normalized_expected:
            raise RuntimeError(
                f"Signing certificate mismatch for {apk_path.name}\n"
                f"Expected: {normalized_expected}\n"
                f"Found:    {cert_sha256}"
            )

    return cert_sha256


def compute_file_sha256(file_path: Path) -> str:
    digest = hashlib.sha256()
    with file_path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def load_descriptions() -> dict[str, dict[str, str]]:
    """Load optional app-descriptions.json keyed by app name (case-insensitive)."""
    if not DESCRIPTIONS_PATH.exists():
        return {}

    raw = json.loads(DESCRIPTIONS_PATH.read_text(encoding="utf-8"))
    parsed: dict[str, dict[str, str]] = {}

    for key, value in raw.items():
        norm_key = key.strip().lower()
        if isinstance(value, str):
            parsed[norm_key] = {"description": value.strip(), "emoji": ""}
        elif isinstance(value, dict):
            parsed[norm_key] = {
                "description": str(value.get("description", "")).strip(),
                "emoji": str(value.get("emoji", "")).strip(),
            }

    return parsed


def build_readme_section(records: list[dict[str, str]]) -> str:
    lines = [
        START_MARKER,
        "## Android apps",
        "",
    ]

    for rec in records:
        title = f"{rec['emoji']} {rec['name']}".strip()
        lines.append(f"### {title} — v{rec['version']}")
        lines.append("")

        if rec["description"]:
            lines.append(rec["description"])
            lines.append("")

        encoded_file = quote(rec["file"])
        lines.extend([
            f"- [Download APK](apks/{encoded_file})",
            f"- **Signing certificate SHA-256:** `{rec['cert_sha256']}`",
            f"- **APK SHA-256:** `{rec['apk_sha256']}`",
            "",
        ])

    lines.append(END_MARKER)
    return "\n".join(lines)


def update_readme(section: str) -> None:
    readme = README_PATH.read_text(encoding="utf-8") if README_PATH.exists() else ""

    if START_MARKER in readme and END_MARKER in readme:
        before, remainder = readme.split(START_MARKER, 1)
        _, after = remainder.split(END_MARKER, 1)
        updated = before + section + after
    else:
        updated = readme.rstrip() + "\n\n" + section + "\n"

    README_PATH.write_text(updated, encoding="utf-8")


def main() -> int:
    if not APKS_DIR.is_dir():
        print("::error::The apks/ directory does not exist.", file=sys.stderr)
        return 1

    apk_files = sorted(APKS_DIR.glob("*.apk"), key=lambda p: p.name.lower())
    if not apk_files:
        print("::error::No APK files found in apks/.", file=sys.stderr)
        return 1

    aapt2 = get_build_tool("aapt2")
    apksigner = get_build_tool("apksigner")
    expected_cert = os.environ.get("EXPECTED_CERT_SHA256", "").strip() or None
    descriptions = load_descriptions()

    records: list[dict[str, str]] = []

    for apk_path in apk_files:
        print(f"Verifying: {apk_path.name}")
        app_name, version = extract_apk_metadata(aapt2, apk_path)
        cert_sha256 = verify_and_get_cert_sha256(apksigner, apk_path, expected_cert)
        apk_sha256 = compute_file_sha256(apk_path)

        meta = descriptions.get(app_name.lower(), {"description": "", "emoji": ""})

        records.append({
            "file": apk_path.name,
            "name": app_name,
            "emoji": meta["emoji"],
            "description": meta["description"],
            "version": version,
            "cert_sha256": cert_sha256,
            "apk_sha256": apk_sha256,
        })
        print(f"  OK: {app_name} v{version}")

    records.sort(key=lambda r: r["name"].lower())
    section = build_readme_section(records)
    update_readme(section)

    print(f"Updated {README_PATH} with {len(records)} verified APKs.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print(f"::error::{exc}", file=sys.stderr)
        sys.exit(1)
