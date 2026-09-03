# xotaDown

![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python)  
![License: MIT](https://img.shields.io/badge/license-MIT-green)  
![CI](https://github.com/shubhyagami/xotaDown/actions/workflows/ci.yml/badge.svg)  
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)

**xotaDown** is a lightweight command‑line utility that downloads tweets, media, and full threads from X (formerly Twitter).  
It works purely from a tweet URL – no credentials are required unless you enable advanced API usage.

---

## Quick Start

```bash
# Install from PyPI (recommended)
pip install xotadown

# Or install directly from source
git clone https://github.com/shubhyagami/xotaDown.git
cd xotaDown
pip install -e .
```

Run the tool:

```bash
xotaDown "https://x.com/elonmusk/status/1523456789" --thread
```

See `xotaDown --help` for a full list of options.

---

## Features

| Feature | What it does |
|----------|--------------|
| **Single‑command downloads** | Grab any tweet, thread, or media with one line of code |
| **Thread reconstruction** | Maintains the correct reply order for multi‑tweet threads |
| **Media support** | Images & videos are saved automatically alongside the text |
| **Local cache** | Stores fetched tweets to avoid redundant network requests |
| **Rate‑limit awareness** | Retries with exponential back‑off when approaching API limits |
| **Progress output** | Verbose mode shows detailed status messages |

---

## Installation

### Prerequisites

- Python 3.8 or newer
- `pip`

### From PyPI

```bash
pip install xotadown
```

### From source

```bash
git clone https://github.com/shubhyagami/xotaDown.git
cd xotaDown
pip install -e .
```

> *Tip:* After a source install, you can run the tool from anywhere without modifying your shell profile – the `xotaDown` script is installed into `~/.local/bin` (or the equivalent on your system).

---

## Usage

```bash
xotaDown "<tweet_url>" [options]
```

### Options

| Flag | Meaning |
|------|---------|
| `-t`, `--thread` | Download the entire thread starting from the given tweet |
| `-o`, `--output` | Output directory (defaults to the current working directory) |
| `-v`, `--verbose` | Show detailed progress information |
| `-h`, `--help`    | Display this help message |

### Examples

```bash
# Download a single tweet
xotaDown "https://x.com/elonmusk/status/1523456789"

# Download an entire thread
xotaDown "https://x.com/elonmusk/status/1523456789" --thread

# Save to a custom folder
xotaDown "https://x.com/user/status/1234567890" -o ./archives
```

---

## Contributing

1. **Fork** the repository and create a feature branch from `main`.  
2. Follow the existing coding style (PEP 8, type annotations where appropriate).  
3. Add tests for new functionality.  
4. Update `CHANGELOG.md` with a short entry.  
5. Open a pull request and ask for review.

### Reporting Issues

- Provide a clear title and description.  
- Include reproducible steps, error messages, and your environment (OS, Python version).  
- Attach any relevant logs or screenshots.

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

> *For a full history, view the `CHANGELOG.md` file.*

---

## License

MIT – see the [LICENSE](LICENSE) file.
