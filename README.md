# MediaShift — Open-Source Windows Utility

Offline Windows audio and video converter GUI using your separately installed FFmpeg.

[![Automated tests](https://github.com/amirhoseinteras/mediashift-desktop/actions/workflows/tests.yml/badge.svg)](https://github.com/amirhoseinteras/mediashift-desktop/actions/workflows/tests.yml)
[Download latest](https://github.com/amirhoseinteras/mediashift-desktop/releases/latest) · [Source code](https://github.com/amirhoseinteras/mediashift-desktop) · [Issues](https://github.com/amirhoseinteras/mediashift-desktop/issues)

**Version:** 1.0.0 · **Platform:** Windows · **License:** MIT

## Features
- Convert local media using FFmpeg through an easy graphical interface.
- Export to MP4, MP3, WAV and WebM.
- Runs offline without uploading your private recordings.
- Installer and portable versions available for Windows.

## Download for Windows

| Package | Download | Usage |
| --- | --- | --- |
| Installer | [MediaShift-Setup.exe](https://github.com/amirhoseinteras/mediashift-desktop/releases/latest/download/MediaShift-Setup.exe) | Install with Start Menu shortcut and uninstaller for the current user |
| Portable | [MediaShift-Portable.zip](https://github.com/amirhoseinteras/mediashift-desktop/releases/latest/download/MediaShift-Portable.zip) | Unzip and launch MediaShift.exe; no installation |
| Checksums | [SHA256SUMS.txt](https://github.com/amirhoseinteras/mediashift-desktop/releases/latest/download/SHA256SUMS.txt) | Verify the downloaded files |

**Important:** Release files are unsigned; Windows SmartScreen may display a warning. Check the source and published hashes before trusting an executable. Do not disable your security software to bypass warnings.

### Check download integrity

~~~powershell
Get-FileHash .\MediaShift-Setup.exe -Algorithm SHA256
~~~
Compare the output with the corresponding line of SHA256SUMS.txt from the same release.

## Requirements & limitations

FFmpeg is a separate requirement and is not included. Install it from the official project; exact codec availability depends on your FFmpeg build.

## Run from source

Windows and Python 3.10+ with Tkinter are required.

~~~powershell
python -m pip install -r requirements.txt
python mediashift.py
python -m unittest discover -s tests -v
~~~

The source tree includes build_windows.py and packaging/installer.py for reproducible Windows packaging.

## Support and development

- [Security](SECURITY.md) · [License](LICENSE) · [Changelog](CHANGELOG.md) · [Contributing](CONTRIBUTING.md)
- [Report bugs or request features](https://github.com/amirhoseinteras/mediashift-desktop/issues). Provide the OS version, steps, and expected/actual results.
- No telemetry or account is needed for these offline tools. The source code provides the authoritative feature specification.

## فارسی — راهنمای دانلود

**MediaShift** برنامه‌ای متن‌باز و رایگان برای ویندوز است. فایل Setup برای نصب و نسخه Portable ZIP برای اجرا بدون نصب ارائه شده است.
نسخه‌های اجرایی امضای دیجیتال ندارند. مقدار SHA-256 هر فایل را با فایل SHA256SUMS.txt داخل همان انتشار مقایسه کنید.

---
**Repository:** https://github.com/amirhoseinteras/mediashift-desktop · **Releases:** https://github.com/amirhoseinteras/mediashift-desktop/releases