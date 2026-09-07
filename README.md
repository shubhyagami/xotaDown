# xotaDown

![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python)  
![License: MIT](https://img.shields.io/badge/license-MIT-green)  
![CI](https://github.com/shubhyagami/xotaDown/actions/workflows/ci.yml/badge.svg)  
![PyPI - Downloads](https://img.shields.io/pypi/dm/xotadown?label=pypi%20downloads)

**xotaDown** is a lightweight command‑line tool that lets you download tweets, media, and entire threads from X (formerly Twitter).  
Public content can be fetched without authentication; API keys are only required for protected accounts or to avoid stricter rate limits.

---

## Getting Started

```bash
# Install the package
pip install xotadown
```

```bash
# Download a single tweet
xotadown "https://x.com/elonmusk/status/1523456789"

# Download the whole thread
xotadown "https://x.com/elonmusk/status/1523456789" --thread
```

Run `xotadown --help` to see all available options.

---

## Features

- Download the **text** of a tweet or the **whole thread** it belongs to.
- Keep the original reply order when rebuilding threads.
- Automatically fetch **images, videos, PDFs** and embed them into the tweet text.
- Local cache to avoid re‑downloading the same media.
- Exponential back‑off to handle X rate limits gracefully.
- Verbose mode (`-v`) shows progress and debugging output.

---

## Usage

```bash
xotadown "<tweet_url>" [options]
```

| Option      | Alias | Description |
|------------|-------|-------------|
| `--thread` | `-t`  | Download the entire thread that contains the tweet. |
| `--output` | `-o`  | Destination directory (defaults to the current working directory). |
| `--verbose`| `-v`  | Show detailed progress and status messages. |
| `--help`   | `-h`  | Display this help text. |

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

## Installation

### From PyPI (recommended)

```bash
pip install xotadown
```

A `xotadown` executable will be installed on your system’s `PATH`.

### From source

```bash
git clone https://github.com/shubhyagami/xotaDown.git
cd xotaDown
pip install -e .
```

---

## Contributing

1. Fork the repository and create a branch off `main`.  
2. Follow the coding style: PEP 8, type hints, and existing tests.  
3. Add tests for new features.  
4. Update `CHANGELOG.md` with a short summary of your changes.  
5. Open a pull request and request a review.

For large changes or major feature requests, open an issue first.

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

- Initial release: single‑tweet and thread download, basic media extraction.

For a complete history, see the [CHANGELOG.md](CHANGELOG.md) file.

---

## License

MIT – see the [LICENSE](LICENSE) file.
