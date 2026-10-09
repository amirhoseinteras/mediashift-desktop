# MediaShift for Windows

Convert local video/audio files into MP4, MP3, WAV and WebM with FFmpeg.

**Version:** 1.0.0. Works fully offline, with no accounts or analytics.

## Download / دانلود

Use GitHub Releases: **MediaShift-Setup.exe** to install (Start Menu, desktop shortcut, uninstall) or **MediaShift-Portable.zip** to run without installing. Both builds are unsigned. Windows SmartScreen can warn about unsigned programs.

## Run from source

Requires Windows and Python 3.10+ with Tkinter. Run: python mediashift.py

## Important

FFmpeg is not included; install it separately from https://ffmpeg.org/download.html. Conversion time depends on hardware.

## License / مشارکت

MIT for original source code. Bug reports, translations and genuine contributions are welcome. Do not submit fake stars, downloads, or meaningless pull requests.

## Reproducible Windows builds

Install Python 3.10+, run 'python -m pip install -r requirements.txt pyinstaller' then 'python build_windows.py'. Outputs are under dist/. The installer provides per-user installation and uninstall; it never requires administrator access.
