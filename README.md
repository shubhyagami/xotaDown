# xotaDown

![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python)
![License: MIT](https://img.shields.io/badge/license-MIT-green)
![CI](https://github.com/shubhyagami/xotaDown/actions/workflows/ci.yml/badge.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/xotadown?label=pypi%20downloads)

**xotaDown** is a lightweight command‑line tool for downloading tweets, media, and entire threads from X (formerly Twitter).  
No credentials are required for public content; API keys are needed only for protected accounts or to avoid stricter rate limits.

---

## Getting Started

```bash
# Install from PyPI
pip install xotadown
```

```bash
# Download a single tweet
xotadown "https://x.com/elonmusk/status/1523456789"

# Download an entire thread
xotadown "https://x.com/elonmusk/status/1523456789" --thread
```

Run `xotadown --help` for a full list of options.

---

## Features

- **Single tweet** or entire thread in one command
- **Original reply order** preserved when rebuilding threads
- Automatic download of **images, videos, and PDFs** alongside the tweet text
- Local cache prevents duplicate downloads
- Exponential back‑off handles X rate limits gracefully
- **Verbose mode** (`-v`) shows progress and debugging information

---

## Installation

### From PyPI (recommended)

```bash
pip install xotadown
```

### From source

```bash
git clone https://github.com/shubhyagami/xotaDown.git
cd xotaDown
pip install -e .
```

The `xotadown` script is installed in your user‑local `bin` directory (e.g., `~/.local/bin`), so you can run it from any location.

---

## Usage

```bash
xotadown "<tweet_url>" [options]
```

| Option | Aliases | Description |
|-------|---------|-------------|
| `--thread`      | `-t` | Download the entire thread that contains the tweet |
| `--output`      | `-o` | Destination directory (defaults to the current working directory) |
| `--verbose`     | `-v` | Show detailed progress and status messages |
| `--help`        | `-h` | Show help information |

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

1. Fork the repository and create a new branch off `main`.  
2. Follow the existing style guidelines (PEP 8, type hints, tests).  
3. Write tests for new features.  
4. Update `CHANGELOG.md` with a brief summary.  
5. Open a pull request and request a review.

If you find a bug or would like to suggest an improvement, open an issue. Provide a clear title, steps to reproduce, and any relevant logs.

---

## Support

- **Discussions** – <https://github.com/shubhyagami/xotaDown/discussions>  
- **Issues** – <https://github.com/shubhyagami/xotaDown/issues>

---

## Changelog

### 0.2.0 – 2026‑08‑12
- Refined README layout  
- Improved thread fetching for long threads  
- Optimized cache to reduce redundant downloads  

### 0.1.0 – 2026‑07‑15
- Initial release: single‑tweet and thread download, basic media extraction

> For a complete history, see the [CHANGELOG.md](CHANGELOG.md) file.

---

## License

MIT – see the [LICENSE](LICENSE) file.
