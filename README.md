# 📱 Santhosh's Android Apps

[![APK Signature Check](https://github.com/mskian/vibe-coded-apps/actions/workflows/verify-apks.yml/badge.svg)](https://github.com/mskian/vibe-coded-apps/actions/workflows/verify-apks.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Apps](https://img.shields.io/badge/APKs-6-blue.svg)](#-available-apps)

A collection of Android apps built with curiosity, open-source tools, and a little help from AI. During recovery from an accident and a fracture in my right arm, ChatGPT helped me keep learning and vibe-coding these apps. 🩹💻

## 📥 Available apps

All APKs are signed. Download links point directly to the APK files in the `apks/` folder. GitHub Actions verifies each APK, extracts its app version and signer SHA-256 fingerprint, and automatically updates this table.

<!-- APK-LIST-START -->
## Android apps

### 👟 Fitsteps — v1.0.0

Analyze your step count and activity data from the past 7 days using Health Connect. Track your daily progress and stay motivated to maintain an active lifestyle.

- [Download APK](apks/Fitsteps-release-signed.apk)
- **Signing certificate SHA-256:** `DD6FD9AD1630A597207CBC970E0ED8A9A08EAFEDE05BDF97723F3E148F8CDAB6`
- **APK SHA-256:** `7E8EDBAD57BA36F689F2D1B441B637E12AA1014EE6B151B732706784343F7591`

### 📚 Random Words — v1.0.0

Discover random English words with their definitions and pronunciations. Expand your vocabulary and improve your language skills.

- [Download APK](apks/RandomWords-release-signed.apk)
- **Signing certificate SHA-256:** `DD6FD9AD1630A597207CBC970E0ED8A9A08EAFEDE05BDF97723F3E148F8CDAB6`
- **APK SHA-256:** `596A38581CE470BB0E1B1E340F46074A36FF235E5E01CFEC89375F1A0E8018F2`

### ❤️ SanFit — v1.0.0

A heart-rate analytics app designed specifically for Fitbit Air. Monitor your heart-rate data and explore detailed analytics.

- [Download APK](apks/SanFit-release-signed.apk)
- **Signing certificate SHA-256:** `DD6FD9AD1630A597207CBC970E0ED8A9A08EAFEDE05BDF97723F3E148F8CDAB6`
- **APK SHA-256:** `CACE35659F96CBFA0E0D81FDFD867A315DA37B54C666F2F7813452DB2E1B5F11`

### 💓 FitHR — v1.0.0

A heart-rate companion for monitoring and reviewing heart-rate data.

- [Download APK](apks/fithr-release-signed.apk)
- **Signing certificate SHA-256:** `DD6FD9AD1630A597207CBC970E0ED8A9A08EAFEDE05BDF97723F3E148F8CDAB6`
- **APK SHA-256:** `DD85308A110BCEBB548518C7A00A88F6000C2574C5A649F721ABFD55909C2371`

### 🎨 SanCraft — v1.0.0

Create and customize quote and Tamil kavithai images.

- [Download APK](apks/sancraft-release-signed.apk)
- **Signing certificate SHA-256:** `DD6FD9AD1630A597207CBC970E0ED8A9A08EAFEDE05BDF97723F3E148F8CDAB6`
- **APK SHA-256:** `075973E24A9E7563DD51E0527B138E234D0F82843AD5FA30F260A7554020016C`

### 💬 Tamil SMS — v1.0.0

Discover Tamil words and find inspiration for messages.

- [Download APK](apks/tamilsms-release-signed.apk)
- **Signing certificate SHA-256:** `DD6FD9AD1630A597207CBC970E0ED8A9A08EAFEDE05BDF97723F3E148F8CDAB6`
- **APK SHA-256:** `FE9F812F4F4F9FE11937FB4B9A0C418C29B2B49AE239E8CFCAD57325D81B0498`

<!-- APK-LIST-END -->

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


