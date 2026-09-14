# xotaDown

![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python&style=flat)  
![License: MIT](https://img.shields.io/badge/license-MIT-green?style=flat)  
![CI](https://github.com/shubhyagami/xotaDown/actions/workflows/ci.yml/badge.svg?style=flat)  
![PyPI - Downloads](https://img.shields.io/pypi/dm/xotadown?label=pypi%20downloads&style=flat)

xotaDown is a lightweight command‑line utility that downloads tweets, their attached media, and complete threads from X (formerly Twitter).  
Public content is accessible without authentication; an API key is required only for protected accounts or to raise the rate‑limit allowance.

---

## 📦 Installation

```bash
# From PyPI (recommended)
pip install xotadown
```

A `xotadown` executable will be added to your system’s `PATH`.

```bash
# From source
git clone https://github.com/shubhyagami/xotaDown.git
cd xotaDown
pip install -e .
```

---

## 🚀 Quick start

```bash
# Download a single tweet
xotadown "https://x.com/elonmusk/status/1523456789"

# Download the entire thread that contains the tweet
xotadown "https://x.com/elonmusk/status/1523456789" --thread

# Specify an output folder
xotadown "https://x.com/user/status/1234567890" -o ./archives
```

Run `xotadown --help` to see all options.

---

## ⚙️ Features

- Download tweet text or an entire conversation thread
- Preserve the original reply order when rebuilding threads
- Extract and embed images, videos, PDFs, and other media into the tweet text
- Local caching of media to prevent duplicate downloads
- Exponential back‑off to respect X rate limits
- Verbose mode (`-v`) shows progress and debugging information

---

## 🛠️ Usage

```bash
xotadown "<tweet_url>" [options]
```

| Option      | Alias | Description |
|------------|-------|-------------|
| `--thread` | `-t`  | Include all tweets in the thread that contains the supplied tweet |
| `--output` | `-o`  | Destination directory (default: current working directory) |
| `--verbose`| `-v` | Show detailed progress and status messages |
| `--help`   | `-h` | Show this help text |

For advanced usage, consult the command‑line help:

```bash
xotadown --help
```

---

## 🤝 Contributing

1. Fork the repository and create a branch from `main`.  
2. Follow the existing coding style (PEP 8, type hints, and tests).  
3. Write tests for any new functionality.  
4. Update `CHANGELOG.md` with a short summary of your changes.  
5. Submit a pull request and request a review.

For large changes or feature requests, open an issue first.

---

## ❓ Support

- **Discussions** – <https://github.com/shubhyagami/xotaDown/discussions>  
- **Issues** – <https://github.com/shubhyagami/xotaDown/issues>

---

## 📜 Changelog

### 0.2.0 – 2026‑08‑12

- Refined README layout.  
- Improved thread fetching for long threads.  
- Optimized media cache to reduce redundant downloads.

### 0.1.0 – 2026‑07‑15

- Initial release with single‑tweet and thread download, basic media extraction.

For a complete history, see the [CHANGELOG.md](CHANGELOG.md) file.

---

## 📄 License

MIT – see the [LICENSE](LICENSE) file.
