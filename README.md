# xotadown

![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python&style=flat)  
![License: MIT](https://img.shields.io/badge/license-MIT-green?style=flat)  
![CI](https://github.com/shubhyagami/xotaDown/actions/workflows/ci.yml/badge.svg?style=flat)  
![PyPI - Downloads](https://img.shields.io/pypi/dm/xotadown?label=pypi%20downloads&style=flat)

**xotadown** is a lightweight command‑line tool that downloads tweets, media attachments, and complete conversation threads from X (formerly Twitter).  
Public tweets can be fetched without authentication; only an API key is needed for protected accounts or to increase the rate‑limit.

---

## 📦 Installation

```bash
# From PyPI (recommended)
pip install xotadown
```

The `xotadown` executable is added to your system’s `PATH`.  
If you prefer the source, clone the repo and install in editable mode:

```bash
git clone https://github.com/shubhyagami/xotaDown.git
cd xotaDown
pip install -e .
```

### Dependencies

- Python 3.8+
- Optional: A valid X API key for protected content.  
  Put the key in `~/.config/xotadown/api_key` or export `XOTADOWN_API_KEY`.

---

## 🚀 Quick start

```bash
# Download a single tweet
xotadown "https://x.com/elonmusk/status/1523456789"

# Download the entire thread that contains the tweet
xotadown "https://x.com/elonmusk/status/1523456789" --thread

# Save to a custom folder
xotadown "https://x.com/user/status/1234567890" -o ./archives
```

Run `xotadown --help` to view all options.

---

## ⚙️ Features

- Retrieve the raw tweet text or reconstruct full conversation threads.
- Preserve original reply order when exporting threads.
- Extract images, videos, PDFs, and other media and embed links into the output.
- Cache media locally to avoid redundant downloads.
- Exponential back‑off and rate‑limit handling compliant with X API policies.
- Verbose mode (`-v`) shows progress, debugging information, and potential errors.

---

## 📘 Usage

```bash
xotadown "<tweet_url>" [options]
```

| Option      | Alias | Description |
|-------------|-------|-------------|
| `--thread`  | `-t`  | Include all tweets in the thread that contains the supplied tweet. |
| `--output`  | `-o`  | Destination directory (default: current working directory). |
| `--verbose` | `-v`  | Show detailed progress and status messages. |
| `--help`    | `-h`  | Display this help message. |

For more advanced usage, consult the command‑line help:

```bash
xotadown --help
```

---

## 🤝 Contributing

1. Fork the repo and create a feature branch from `main`.  
2. Follow the existing style (PEP 8, type hints, tests).  
3. Add tests for new code paths.  
4. Update `CHANGELOG.md` with a short summary of your changes.  
5. Open a pull request and request a review.

Large changes or new feature ideas? Open an issue first.

---

## ❓ Support

- **Discussions** – <https://github.com/shubhyagami/xotaDown/discussions>  
- **Issues** – <https://github.com/shubhyagami/xotaDown/issues>

---

## 📜 Changelog

### 0.2.0 – 2026‑08‑12

- Refined README layout.
- Improved thread fetching for long threads.
- Optimized media cache to reduce duplicate downloads.

### 0.1.0 – 2026‑07‑15

- Initial release: single‑tweet and thread download, basic media extraction.

See the full history in the [CHANGELOG.md](CHANGELOG.md).

---

## 📄 License

MIT – see the [LICENSE](LICENSE) file.
