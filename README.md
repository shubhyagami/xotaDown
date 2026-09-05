# xotaDown

![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python)
![License: MIT](https://img.shields.io/badge/license-MIT-green)
![CI](https://github.com/shubhyagami/xotaDown/actions/workflows/ci.yml/badge.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/xotadown?label=pypi%20downloads)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)

**xotaDown** is a lightweight command‑line tool for downloading tweets, media, and entire threads from X (formerly Twitter).  
No credentials are required for public content; API keys are only needed for protected accounts or to avoid stricter rate limits.

---

## Getting Started

```bash
# Install from PyPI
pip install xotadown
```

```bash
# Download a single tweet
xotaDown "https://x.com/elonmusk/status/1523456789"

# Download an entire thread
xotaDown "https://x.com/elonmusk/status/1523456789" --thread
```

For a full list of options, run `xotaDown --help`.

---

## Features

- Fetch a single tweet, its media, or an entire thread with a single command.
- Preserve the original order of replies when reconstructing threads.
- Save images, videos, and PDFs automatically alongside the tweet text.
- Local cache prevents duplicate downloads.
- Handles X rate limits with exponential back‑off.
- Verbose mode (`-v`) shows progress and debugging information.

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

The `xotaDown` script is installed in your user‐local `bin` directory (e.g., `~/.local/bin`), so you can run it from any directory.

---

## Usage

```bash
xotaDown "<tweet_url>" [options]
```

| Option | Aliases | Description |
|--------|---------|-------------|
| `-t`, `--thread` | – | Download the entire thread that contains the tweet |
| `-o`, `--output` | – | Destination directory (defaults to the current working directory) |
| `-v`, `--verbose` | – | Show detailed progress and status messages |
| `-h`, `--help` | – | Show help information |

**Examples**

```bash
# Single‑tweet download
xotaDown "https://x.com/elonmusk/status/1523456789"

# Thread download
xotaDown "https://x.com/elonmusk/status/1523456789" --thread

# Custom output folder
xotaDown "https://x.com/user/status/1234567890" -o ./archives
```

---

## Contributing

1. Fork the repository and create a branch off `main`.  
2. Follow the existing style guidelines (PEP 8, type hints, tests).  
3. Write tests for new features.  
4. Update `CHANGELOG.md` with a brief description.  
5. Open a pull request and request a review.

If you find a bug or want to suggest an improvement, open an issue. Include a clear title, steps to reproduce, and any relevant logs.

---

## Support

- **Discussions** – <https://github.com/shubhyagami/xotaDown/discussions>
- **Issues** – <https://github.com/shubhyagami/xotaDown/issues>

---

## Changelog

### 0.2.0 – 2026‑08‑12
- Refined README layout.
- Improved thread fetching for long threads.
- Optimized cache to reduce redundant downloads.

### 0.1.0 – 2026‑07‑15
- Initial release with single‑tweet and thread download, plus basic media extraction.

> For a complete history, see the [CHANGELOG.md](CHANGELOG.md) file.

---

## License

MIT – see the [LICENSE](LICENSE) file.
