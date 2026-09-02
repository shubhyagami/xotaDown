# xotaDown

[![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python)](https://www.python.org/)  
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![CI](https://github.com/shubhyagami/xotaDown/actions/workflows/ci.yml/badge.svg)](https://github.com/shubhyagami/xotaDown/actions)  
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/shubhyagami/xotaDown/pulls)

**xotaDown** – a lightweight CLI tool for downloading tweets, media, and entire threads from X (formerly Twitter).

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Clone & Install](#clone--install)
  - [Add to PATH (optional)](#add-to-path-optional)
- [Usage](#usage)
  - [Command‑Line Options](#command-line-options)
  - [Examples](#examples)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [Support](#support)
- [Changelog](#changelog)
- [License](#license)

---

## Overview

`xotaDown` fetches and stores content from X with a single command.  
It supports:

- Downloading a single tweet.
- Downloading an entire thread in the correct reply order.
- Extracting attached images and videos.
- Caching results locally to avoid duplicate network calls.
- Automatic handling of rate limits.

---

## Features

| Feature | Description |
|---------|-------------|
| **One‑command downloads** | Retrieve any tweet or thread with a single execution. |
| **Media extraction** | Images and videos are saved alongside the tweet text. |
| **Thread ordering** | Threads are reconstructed in the correct reply sequence. |
| **Local caching** | Fetched tweets are stored locally to reduce network traffic. |
| **Rate‑limit handling** | Retries and backs off when approaching API limits. |

---

## Installation

### Prerequisites

- Python 3.8 or newer
- `git`

### Clone & Install

```bash
git clone https://github.com/shubhyagami/xotaDown.git
cd xotaDown
pip install -r requirements.txt
```

### Add to PATH (optional)

If you want to run `xotaDown` from anywhere:

```bash
echo "$(pwd)/xotaDown.py" >> ~/.bashrc   # Bash
source ~/.bashrc
```

---

## Usage

```bash
xotaDown.py "<tweet_url>" [options]
```

### Command‑Line Options

| Flag | Meaning |
|------|---------|
| `--thread`, `-t` | Download the entire thread starting from the given tweet. |
| `-o <dir>`, `--output <dir>` | Output directory (default: current directory). |
| `-v`, `--verbose` | Display detailed progress information. |
| `-h`, `--help` | Show help message. |

### Examples

```bash
# Download a single tweet
xotaDown.py "https://x.com/elonmusk/status/1523456789"

# Download an entire thread
xotaDown.py "https://x.com/elonmusk/status/1523456789" --thread

# Save to a custom folder
xotaDown.py "https://x.com/user/status/1234567890" -o ./archives
```

---

## Getting Started

1. Clone the repository and install dependencies (see *Installation*).  
2. Run `xotaDown.py --help` to view available options.  
3. Perform your first download and check the created `*.txt` and media files.

---

## Contributing

Feel free to open issues or pull requests.

### Reporting Issues

1. Describe the expected behavior vs. what happened.  
2. Provide steps to reproduce, error messages, and your environment (OS, Python version).  

### Pull Requests

1. Fork the repo and create a branch off `main`.  
2. Follow the existing style and add tests if you introduce new functionality.  
3. Update the changelog with a brief description.  
4. Submit the pull request and request a review.

---

## Support

- **Discussions** – https://github.com/shubhyagami/xotaDown/discussions  
- **Issues** – https://github.com/shubhyagami/xotaDown/issues  

Feel free to ask questions or suggest new features.

---

## Changelog

### 0.2.0 – 2026‑08‑12
- Refined README layout.  
- Improved thread fetching for long threads.  
- Optimized cache to reduce redundant downloads.

### 0.1.0 – 2026‑07‑15
- Initial release with single‑tweet and thread download, plus basic media extraction.

---

## License

MIT – see the [LICENSE](LICENSE) file.
