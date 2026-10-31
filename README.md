# 📱 Santhosh's Android Apps

[![APK Signature Check](https://github.com/mskian/vibe-coded-apps/actions/workflows/verify-apks.yml/badge.svg)](https://github.com/mskian/vibe-coded-apps/actions/workflows/verify-apks.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Apps](https://img.shields.io/badge/APKs-6-blue.svg)](#-available-apps)
[![Downloads](https://img.shields.io/github/downloads/mskian/vibe-coded-apps/total?label=release%20downloads)](https://github.com/mskian/vibe-coded-apps/releases)

A collection of Android apps built with curiosity, open-source tools, and a little help from AI. During recovery from an accident and a fracture in my right arm, ChatGPT helped me keep learning and vibe-coding these apps. 🩹💻

## 📥 Available apps

All APKs are signed. Download links point directly to the APK files in the `apks/` folder. GitHub Actions extracts each app version and signer SHA-256 fingerprint and publishes them in its workflow summary. The download badge counts GitHub Release asset downloads; GitHub does not expose per-file raw repository download counts.

| App | Description | Version | Signing certificate SHA-256 | Download |
|---|---|---:|---|---|
| FitHR | Heart-rate companion and monitoring tools. | Extracted by Actions | Published by Actions | [⬇️ Download](https://github.com/mskian/vibe-coded-apps/raw/refs/heads/main/apks/fithr-release-signed.apk) |
| SanCraft | Create and customize quote/kavithai images. | Extracted by Actions | Published by Actions | [⬇️ Download](https://github.com/mskian/vibe-coded-apps/raw/refs/heads/main/apks/sancraft-release-signed.apk) |
| Random Words | Discover a random word and its meaning. | Extracted by Actions | Published by Actions | [⬇️ Download](https://github.com/mskian/vibe-coded-apps/raw/refs/heads/main/apks/RandomWords-release-signed.apk) |
| Tamil SMS | Tamil words and message inspiration. | Extracted by Actions | Published by Actions | [⬇️ Download](https://github.com/mskian/vibe-coded-apps/raw/refs/heads/main/apks/tamilsms-release-signed.apk) |
| Fitsteps | Step tracking and activity tools. | Extracted by Actions | Published by Actions | [⬇️ Download](https://github.com/mskian/vibe-coded-apps/raw/refs/heads/main/apks/Fitsteps-release-signed.apk) |
| SanFit | Fitness and activity companion. | Extracted by Actions | Published by Actions | [⬇️ Download](https://github.com/mskian/vibe-coded-apps/raw/refs/heads/main/apks/SanFit-release-signed.apk) |

### 🔑 Verify the signing key

The workflow verifies that every APK has a valid Android signature and reports its signer certificate SHA-256 fingerprint. For a trusted-key comparison, configure the repository variable `EXPECTED_CERT_SHA256` with the SHA-256 fingerprint of your known signing certificate (hex characters, optionally colon-separated). The workflow fails if any APK's signer differs. **Never upload your private keystore or its password to this repository.**

## 🔐 Privacy, safety & cost

These apps are personally used by me, and I aim to keep them simple, private, and free:

- **100% free to use** — no paid features or subscriptions.
- **Zero ads and zero third-party tracking SDKs** in the apps.
- **No app cloud account or third-party analytics/tracking service is used** by these apps.
- The apps are intended to process their features locally on your device. Any network access needed for a specific feature should be explained in that app's listing or privacy information.

I build and use these apps myself, but please still review Android's permission prompt and the app-specific privacy details before installing. A valid APK signature confirms the signer and helps detect tampering; it is not a guarantee that software is vulnerability-free or independently audited. Install only releases you trust, and verify the signing fingerprint when possible.

## 📜 License

This repository's documentation and release tooling are licensed under the [MIT License](LICENSE). App source code and third-party dependencies may have separate licenses; see their respective projects and notices.

## 🙏 Credits

Created by **Santhosh** with help from ChatGPT, Android tooling, and the open-source community. Thanks to everyone who builds and shares free software.
