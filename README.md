# xotaDown

![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python) ![License: MIT](https://img.shields.io/badge/license-MIT-green) ![CI](https://github.com/shubhyagami/xotaDown/actions/workflows/ci.yml/badge.svg) ![PyPI - Downloads](https://img.shields.io/pypi/dm/xotadown?label=pypi+downloads)

**xotaDown** is a lightweight command‑line tool for downloading individual tweets, media, and entire threads from X (formerly Twitter).  
Public content can be fetched without authentication; API keys are only required for protected accounts or to avoid stricter rate limits.

---

## Quick start

```bash
# Install from PyPI (Python 3.8+ required)
pip install xotadown
```

```bash
# Download a single tweet
xotadown "https://x.com/elonmusk/status/1523456789"

# Download the whole thread
xotadown "https://x.com/elonmusk/status/1523456789" --thread
```

Run `xotadown --help` for a full list of options.

---

## Features

- Download the **text** of a tweet or the **full thread** it belongs to.  
- Preserve the original reply order when rebuilding threads.  
- Auto‑download **images, videos, PDFs** and attach them to the tweet text.  
- Simple local cache to avoid re‑downloading the same media.  
- Exponential back‑off to gracefully handle X rate limits.  
- Verbose mode (`-v`) displays progress and debugging information.

---

## Installation

### From PyPI (recommended)

```bash
pip install xotadown
```

This installs a `xotadown` script in your system’s `PATH`.

### From source

```bash
git clone https://github.com/shubhyagami/xotaDown.git
cd xotaDown
pip install -e .
```

---

## Usage

```bash
xotadown "<tweet_url>" [options]
```

| Option      | Aliases | Description |
|-------------|--------|--------------|
| `--thread` | `-t`   | Download the entire thread containing the tweet |
| `--output`  | `-o`   | Destination directory (defaults to the current working directory) |
| `--verbose` | `-v`   | Show detailed progress and status messages |
| `--help`    | `-h`   | Show help information |

### Examples

```bash
# Single‑tweet download
xotadown "https://x.com/elonmusk/status/1523456789"

# Thread download
xotadown "https://x.com/elonmusk/status/1523456789" --thread

# Custom output folder
xotadown "https://x.com/user/status/1234567890" -o ./archives
```

---

## Contributing

1. Fork the repository and create a branch off `main`.  
2. Follow the existing style guidelines: PEP 8, type hints, and tests.  
3. Add tests for any new functionality.  
4. Update `CHANGELOG.md` with a brief summary of your changes.  
5. Open a pull request and request a review.

Please create an issue first for large changes or significant feature requests.

---

## Getting help

- **Discussions** – <https://github.com/shubhyagami/xotaDown/discussions>  
- **Issues** – <https://github.com/shubhyagami/xotaDown/issues>

---

## Changelog

### 0.2.0 – 2026‑08‑12
- Refined README layout  
- Improved thread fetching for long threads  
- Optimized cache to reduce redundant downloads  

### 0.1.0 – 2026‑07‑15
- Initial release: single‑tweet and thread download, basic media extraction

For a complete history, see the [CHANGELOG.md](CHANGELOG.md) file.

---

## License

MIT – see the [LICENSE](LICENSE) file.
