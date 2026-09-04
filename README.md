# xotaDown

![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python)  
![License: MIT](https://img.shields.io/badge/license-MIT-green)  
![CI](https://github.com/shubhyagami/xotaDown/actions/workflows/ci.yml/badge.svg)  
![PyPI - Downloads](https://img.shields.io/pypi/dm/xotadown?label=pypi%20downloads)  
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)

**xotaDown** is a lightweight command‑line utility for downloading tweets, media, and entire threads from X (formerly Twitter).  
It requires no credentials for basic use; API keys are only needed for advanced features such as downloading protected accounts.

---

## Quick Start

1. **Install**  
   ```bash
   pip install xotadown
   ```

2. **Run** a single tweet or a thread  
   ```bash
   xotaDown "https://x.com/elonmusk/status/1523456789"   # single tweet
   xotaDown "https://x.com/elonmusk/status/1523456789" --thread  # whole thread
   ```

   For more options see `xotaDown --help`.

---

## Features

- Grab any tweet, thread, or media with a *single* command.
- Preserve the reply order when reconstructing threads.
- Automatically save images and videos alongside the tweet text.
- Local caching avoids unnecessary network traffic.
- Handles rate limits with exponential‑backoff retries.
- Verbose mode shows detailed progress information.

---

## Installation

### Requirements

- Python 3.8 or newer
- `pip`

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

After a source install you can run the tool globally without editing your shell profile – the `xotaDown` script is installed into `~/.local/bin` (or the equivalent on your system).

---

## Usage

```bash
xotaDown "<tweet_url>" [options]
```

### Options

| Flag | Meaning |
|------|---------|
| `-t`, `--thread` | Download the entire thread that contains the given tweet |
| `-o`, `--output` | Destination directory (defaults to the current working directory) |
| `-v`, `--verbose` | Show detailed progress and status messages |
| `-h`, `--help` | Display this help information |

### Examples

```bash
# 1‑tweet download
xotaDown "https://x.com/elonmusk/status/1523456789"

# Thread download
xotaDown "https://x.com/elonmusk/status/1523456789" --thread

# Custom output folder
xotaDown "https://x.com/user/status/1234567890" -o ./archives
```

---

## Contributing

1. Fork the repo and create a branch off `main`.  
2. Follow the existing style (PEP 8, type hints).  
3. Write tests for new features.  
4. Update `CHANGELOG.md` with a short entry.  
5. Open a pull request and request review.

### Reporting Issues

- Use a descriptive title.
- Include steps to reproduce, error output, and environment details (OS, Python version).
- Attach logs or screenshots if helpful.

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

> For a full history, see the `CHANGELOG.md` file.

---

## License

MIT – see the [LICENSE](LICENSE) file.
