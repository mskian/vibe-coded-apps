# 📱 Santhosh's Android Apps

[![APK Signature Check](https://github.com/mskian/vibe-coded-apps/actions/workflows/verify-apks.yml/badge.svg)](https://github.com/mskian/vibe-coded-apps/actions/workflows/verify-apks.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Apps](https://img.shields.io/badge/APKs-6-blue.svg)](#-available-apps)

A collection of Android apps built with curiosity, open-source tools, and a little help from AI. During recovery from an accident and a fracture in my right arm, ChatGPT helped me keep learning and vibe-coding these apps. 🩹💻

## 📥 Available apps

All APKs are signed. Download links point directly to the APK files in the `apks/` folder. GitHub Actions verifies each APK, extracts its app version and signer SHA-256 fingerprint, and automatically updates this table.

<!-- APK-TABLE-START -->
<div class="apk-grid">

<div class="apk-card">
  <h3>FitSteps</h3>
  <p>Android application.</p>
  <p><strong>Version:</strong> 1.0.0</p>
  <p>
    <a href="https://github.com/mskian/vibe-coded-apps/raw/main/apks/Fitsteps-release-signed.apk">⬇️ Download APK</a>
  </p>
  <details>
    <summary>Signature details</summary>
    <p><code>dd6fd9ad1630a597207cbc970e0ed8a9a08eafede05bdf97723f3e148f8cdab6</code></p>
  </details>
</div>

<div class="apk-card">
  <h3>Random Words</h3>
  <p>Android application.</p>
  <p><strong>Version:</strong> 1.0.0</p>
  <p>
    <a href="https://github.com/mskian/vibe-coded-apps/raw/main/apks/RandomWords-release-signed.apk">⬇️ Download APK</a>
  </p>
  <details>
    <summary>Signature details</summary>
    <p><code>dd6fd9ad1630a597207cbc970e0ed8a9a08eafede05bdf97723f3e148f8cdab6</code></p>
  </details>
</div>

<div class="apk-card">
  <h3>SanFit</h3>
  <p>Android application.</p>
  <p><strong>Version:</strong> 1.0.0</p>
  <p>
    <a href="https://github.com/mskian/vibe-coded-apps/raw/main/apks/SanFit-release-signed.apk">⬇️ Download APK</a>
  </p>
  <details>
    <summary>Signature details</summary>
    <p><code>dd6fd9ad1630a597207cbc970e0ed8a9a08eafede05bdf97723f3e148f8cdab6</code></p>
  </details>
</div>

<div class="apk-card">
  <h3>fithr</h3>
  <p>Heart-rate companion and monitoring tools.</p>
  <p><strong>Version:</strong> 1.0.0</p>
  <p>
    <a href="https://github.com/mskian/vibe-coded-apps/raw/main/apks/fithr-release-signed.apk">⬇️ Download APK</a>
  </p>
  <details>
    <summary>Signature details</summary>
    <p><code>dd6fd9ad1630a597207cbc970e0ed8a9a08eafede05bdf97723f3e148f8cdab6</code></p>
  </details>
</div>

<div class="apk-card">
  <h3>SanCraft</h3>
  <p>Create and customize quote and kavithai images.</p>
  <p><strong>Version:</strong> 1.0.0</p>
  <p>
    <a href="https://github.com/mskian/vibe-coded-apps/raw/main/apks/sancraft-release-signed.apk">⬇️ Download APK</a>
  </p>
  <details>
    <summary>Signature details</summary>
    <p><code>dd6fd9ad1630a597207cbc970e0ed8a9a08eafede05bdf97723f3e148f8cdab6</code></p>
  </details>
</div>

<div class="apk-card">
  <h3>Tamil SMS</h3>
  <p>Tamil words and message inspiration.</p>
  <p><strong>Version:</strong> 1.0.0</p>
  <p>
    <a href="https://github.com/mskian/vibe-coded-apps/raw/main/apks/tamilsms-release-signed.apk">⬇️ Download APK</a>
  </p>
  <details>
    <summary>Signature details</summary>
    <p><code>dd6fd9ad1630a597207cbc970e0ed8a9a08eafede05bdf97723f3e148f8cdab6</code></p>
  </details>
</div>
</div>
<!-- APK-TABLE-END -->

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
