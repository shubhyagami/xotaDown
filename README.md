# xotaDown

![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python)  
![License: MIT](https://img.shields.io/badge/license-MIT-green)  
![CI](https://github.com/shubhyagami/xotaDown/actions/workflows/ci.yml/badge.svg)  
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)

**xotaDown** – a lightweight CLI tool for downloading tweets, media, and entire threads from X (formerly Twitter).

---

## Table of Contents

- [Getting Started](#getting-started)
- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Clone & Install](#clone--install)
  - [Running from Anywhere](#running-from-anywhere)
- [Usage](#usage)
  - [Command‑Line Options](#command-line-options)
  - [Examples](#examples)
- [Contributing](#contributing)
- [Support](#support)
- [Changelog](#changelog)
- [License](#license)

---

## Getting Started

```bash
git clone https://github.com/shubhyagami/xotaDown.git
cd xotaDown
pip install -r requirements.txt
```

Run `xotaDown.py --help` to see the available options.

---

## Features

| Feature | Description |
|---------|-------------|
| One‑command downloads | Retrieve any tweet or thread with a single execution |
| Media extraction | Images and videos are saved alongside the tweet text |
| Thread ordering | Threads are reconstructed in the correct reply sequence |
| Local caching | Fetched tweets are stored locally to reduce network traffic |
| Rate‑limit handling | Retries and backs off when approaching API limits |

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

### Running from Anywhere (optional)

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
| `-t`, `--thread` | Download the entire thread starting from the given tweet |
| `-o <dir>`, `--output <dir>` | Output directory (default: current directory) |
| `-v`, `--verbose` | Show detailed progress |
| `-h`, `--help` | Display help message |

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

## Contributing

Feel free to open issues or pull requests.

### Reporting Issues

1. Describe the expected behavior versus what actually happened.  
2. Provide reproducible steps, error messages, and your environment (OS, Python version).

### Pull Requests

1. Fork the repository and create a branch off `main`.  
2. Follow the code style and add tests if you add new features.  
3. Update the changelog with a short entry.  
4. Submit the pull request and request a review.

---

## Support

- **Discussions** – https://github.com/shubhyagami/xotaDown/discussions  
- **Issues** – https://github.com/shubhyagami/xotaDown/issues  

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
