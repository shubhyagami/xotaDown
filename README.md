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
- 🐛 Fixed crash when tweet contains multi-byte unicode characters in user b

---

## Contributing to the Sacred Timeline

Welcome, Temporal Agent! The Time Variance Authority (TVA) appreciates your interest in preserving the **Sacred Timeline of tweet archives**. Every contribution helps us prune temporal anomalies (read: broken downloaders) and ensure xotaDown remains a perfectly deterministic tool.

### How to File a Variant Report (Bug Report)

Found a nexus event? Open an [Issue](https://github.com/shubhyagami/xotaDown/issues) with:
- A clear description of the **deviation** (expected vs. actual behaviour).
- Steps to **reset the timeline** (reproduction steps).
- Your **TVA ID** (Python version, OS, and any error logs).
- **Attachment of the offending tweet URL** (redacted if necessary – we don’t judge).

### Submitting a Prune (Pull Request)

1. **Fork** the repository – consider this your own branched timeline.
2. **Create a feature branch** from `main` (the “Prime” timeline).
3. **Commit your changes** with a clear message. Use the format:  
   `[TVA-###] Short description of the reset`
4. **Push** and open a Pull Request.  
   - In the description, explain **what nexus event** your PR addresses.
   - If your change fixes an issue, link it using `Closes #123`.
5. A **TVA Analyst** (maintainer) will review your case. Expect questions – they’re just verifying the timeline hasn’t been tampered with.

### Code of Conduct

All agents must adhere to the **TVA Code of Order**:
- Be **courteous** – no one likes a rogue variant.
- Respect **temporal ordering** – keep your code clean and PEP 8 compliant.
- **No self‑pruning** – do not delete or modify your own PRs without a valid reason.
- **No interference** with other agents’ work without prior coordination.

### Development Setup

To set up your own TVA workstation:

```bash
git clone https://github.com/shubhyagami/xotaDown.git
cd xotaDown
python -m venv .tva_venv
source .tva_venv/bin/activate   # or .tva_venv\Scripts\activate on Windows
pip install -r requirements-dev.txt   # includes testing & linting tools
```

Run the tests to ensure the timeline remains intact:

```bash
pytest tests/
```

Lint your code with:

```bash
flake8 xotaDown.py
```

### Need Help?

Contact the **TVA Help Desk** by opening a [Discussion](https://github.com/shubhyagami/xotaDown/discussions). We’ll get a Variant Locator on the case ASAP.

---

*Thank you for helping maintain the one true timeline of tweet downloads. Long live the Sacred Timeline!*