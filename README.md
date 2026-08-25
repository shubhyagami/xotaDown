# xotaDown

[xotaDown Logo]

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue?logo=python)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)

A command-line tool for saving tweets, videos, and threads from X (Twitter) with a single command.

## Overview

xotaDown is a powerful tool designed to simplify the process of saving tweets, videos, and threads from Twitter. It allows users to effortlessly download and archive content with a single command, making it an ideal solution for digital archivists, journalists, and social media enthusiasts.

## Key Features

*   **Single Command Download**: Quickly download individual tweets, videos, or entire threads with a single command.
*   **Media Extraction**: Automatically downloads attached images and video content alongside the text.
*   **Thread Preservation**: Fetches and organizes interconnected tweets chronologically.
*   **Local Caching**: Reduces redundant network requests with an efficient local cache.
*   **Rate-Limit Handling**: Safely manages X/Twitter API limits and automatically retries failed downloads.

## Getting Started

To get started with xotaDown, follow these simple steps:

1.  Clone the repository using `git clone https://github.com/shubhyagami/xotaDown.git`
2.  Install the required dependencies by running `pip install -r requirements.txt` in the project directory
3.  Run the tool using `python xotaDown.py "https://x.com/user/status/1234567890"`

## Use Case: Digital Archiving

xotaDown is a valuable tool for digital archivists and journalists who need to preserve and analyze social media content. By using xotaDown, you can ensure that your records are accurate, reliable, and easily accessible.

## Contributing

Contributions are what make the open-source community such a fantastic place to learn, inspire, and create. If you'd like to contribute to xotaDown, please follow these guidelines:

### Reporting Bugs

When reporting a bug, please include:

*   A clear description of the problem (expected vs. actual behavior)
*   Steps to reproduce the issue
*   Your environment details (OS, Python version, etc.)
*   Relevant error logs or stack traces

### Submitting a Pull Request

1.  Fork the repository and create a branch from `main`
2.  Follow the existing code style and structure
3.  Add or update tests to cover your changes
4.  Write a clear changelog entry describing what you changed and why
5.  Open a pull request and request a review

## Contact

If you have any questions, suggestions, or need support, please reach out to us via [GitHub Discussions](https://github.com/shubhyagami/xotaDown/discussions) or open an issue.

## Changelog

### [0.2.0] - 2026-08-12
-   Improved README layout and documentation
-   Enhanced thread-fetching reliability for long threads
-   Improved local cache management to reduce redundant network requests

### [0.1.0] - 2026-07-15
-   Initial release
-   Implemented core downloading for single tweets and threads
-   Added basic media extraction for images and videos
