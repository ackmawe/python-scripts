<!-- MANPAGE: BEGIN EXCLUDED SECTION -->
<div align="center">

[![YT-DLP](https://raw.githubusercontent.com/yt-dlp/yt-dlp/master/.github/banner.svg)](#readme)

[![Release version](https://img.shields.io/github/v/release/yt-dlp/yt-dlp?color=brightgreen&label=Download&style=for-the-badge)](#installation "Installation")
[![PyPI](https://img.shields.io/badge/-PyPI-blue.svg?logo=pypi&labelColor=555555&style=for-the-badge)](https://pypi.org/project/yt-dlp "PyPI")
[![Donate](https://img.shields.io/badge/_-Donate-red.svg?logo=githubsponsors&labelColor=555555&style=for-the-badge)](Collaborators.md#collaborators "Donate")
[![Matrix](https://img.shields.io/matrix/yt-dlp:matrix.org?color=brightgreen&labelColor=555555&label=&logo=element&style=for-the-badge)](https://matrix.to/#/#yt-dlp:matrix.org "Matrix")
[![Discord](https://img.shields.io/discord/807245652072857610?color=blue&labelColor=555555&label=&logo=discord&style=for-the-badge)](https://discord.gg/H5MNcFW63r "Discord")
[![Supported Sites](https://img.shields.io/badge/-Supported_Sites-brightgreen.svg?style=for-the-badge)](supportedsites.md "Supported Sites")
[![License: Unlicense](https://img.shields.io/badge/-Unlicense-blue.svg?style=for-the-badge)](LICENSE "License")
[![CI Status](https://img.shields.io/github/actions/workflow/status/yt-dlp/yt-dlp/core.yml?branch=master&label=Tests&style=for-the-badge)](https://github.com/yt-dlp/yt-dlp/actions "CI Status")
[![Commits](https://img.shields.io/github/commit-activity/m/yt-dlp/yt-dlp?label=commits&style=for-the-badge)](https://github.com/yt-dlp/yt-dlp/commits "Commit History")
[![Last Commit](https://img.shields.io/github/last-commit/yt-dlp/yt-dlp/master?label=&style=for-the-badge&display_timestamp=committer)](https://github.com/yt-dlp/yt-dlp/pulse/monthly "Last activity")

</div>
<!-- MANPAGE: END EXCLUDED SECTION -->

# Video Downloader

A Python script that downloads videos from various platforms using [yt-dlp](https://github.com/yt-dlp/yt-dlp), with built-in network stability checks and format selection.

## Description

This script allows users to download videos by providing a video URL. It checks for network stability before starting the download and allows users to select from available video formats.

## Features

- Checks network stability by pinging a reliable server.
- Fetches available video formats for the provided URL.
- Allows users to select a specific format for download.
- Implements retry logic for downloads in case of network issues.
- Saves downloaded videos in a specified directory.

## Requirements

- Python 3.x
- `yt-dlp` library
- `requests` library
- ffmpeg

You can install the required libraries using pip:

```bash
pip install yt-dlp requests
```
## Usage

- Run the script:

  ```bash
  python video-downloader.py
```
- Enter the video URL when prompted.
- Specify the directory to save the video (leave blank to use the current directory).
- Select the desired video format from the available options.
- The script will check network stability and start the download.

# Network Stability
- The script checks the network stability by pinging Google. If the network is unstable, it will wait for 2 minutes before checking again.

# Author
- Ack-Mawé 🐥
