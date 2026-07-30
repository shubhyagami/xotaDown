# xotaDown
---

```
  ██╗  ██╗ ██████╗ ████████╗ █████╗ ██████╗  ██████╗ ██╗    ██╗███╗   ██╗
  ╚██╗██╔╝██╔═══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔═══██╗██║    ██║████╗  ██║
   ╚███╔╝ ██║   ██║   ██║   ███████║██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║
   ██╔██╗ ██║   ██║   ██║   ██╔══██║██║  ██║██║   ██║██║███╗██║██║╚██╗██║
  ██╔╝ ██╗╚██████╔╝   ██║   ██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║
  ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝
```

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue?logo=python)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![Last Commit](https://img.shields.io/badge/last%20commit-2026--07--30-orange)
![Downloads](https://img.shields.io/badge/downloads-2.8k%2B-yellow)

> **Save tweets, videos, and threads from X/Twitter with a single command.**

---

## Quick Start

```bash
# Clone the repo
git clone https://github.com/shubhyagami/xotaDown.git
cd xotaDown

# Install dependencies
pip install -r requirements.txt

# Download a tweet by URL
python xotaDown.py "https://x.com/user/status/1234567890"
```

---

## Pro Tips

- **Threads?** Pass a tweet URL from the thread and use the `--thread` flag to download the entire conversation.
- **High quality videos:** Add `--quality best` to grab the highest resolution available.
- **Batch downloads:** Save a list of URLs (one per line) and use `--batch urls.txt`.
- **Keep it tidy:** Output is organized in folders by username and date by default.

---

## Weekly Highlight – 2026-07-30

🔍 **Smart Resume** – Interrupted downloads now pick up where they left off. Use `--resume` to skip already-downloaded files and avoid duplicates. Perfect for unstable connections or large batch jobs.

---

## Changelog

### 2026-07-30
- 🆕 **Smart Resume** – Added `--resume` flag to skip already-downloaded media and avoid re-downloads.
- 🐛 Fixed crash when tweet contains multi-byte unicode characters in user bio.

---

## Contributing – TVA Temporal Engineer Edition

Welcome, variant! You have been selected to help maintain the Sacred Timeline of xotaDown. Before you submit a pull request, please align your actions with the following TVA directives:

### 🔧 How to Contribute

1. **Prune a Branch** – Fork the repository and create a feature branch from `main`. Name it something descriptive, e.g., `fix/unicode-gremlin` or `feat/gif-support`.
2. **Reset the Timeline** – Ensure your code passes existing tests. Run `pytest` or `python -m unittest discover` before committing.
3. **Submit an Evidence File** – Open a pull request with a clear description of what you changed and why. Include screenshots or logs if you fixed a timeline anomaly (a.k.a. a bug).
4. **Await Judgment** – A Time-Keeper (maintainer) will review your PR. We may ask for changes to keep the timeline stable.

### 📜 Code of Conduct

- All variants are welcome, regardless of timeline origin.
- No nexus events (breaking changes without discussion).
- Use clear, temporal-proof commit messages: `fix: resolve crash when tweet contains emoji` or `feat: add video transcoding`.
- Respect the pruning order – keep your changes focused and atomic.

### 🧪 Testing Your Changes

- Run `python xotaDown.py --test` (if available) or manually test with a known tweet URL.
- For new features, add tests in the `tests/` folder. If you don’t, the TVA may send a Minuteman to your timeline.

### 🕰️ Submitting a PR

We accept contributions that:
- Fix bugs (temporal paradoxes)
- Add new output formats (e.g., `--format json`)
- Improve download speed (accelerate the timeline)
- Expand platform support (other social media? maybe…)

Remember: *For all time. Always.* And if you break the timeline, we’ll send a Reset Charge your way. Happy coding, agent!

--- 
*End of transmission. TVA File #xotaDown-2026-07-31.*