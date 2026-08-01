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
![Last Commit](https://img.shields.io/badge/last%20commit-2026--08--02-orange)
![Downloads](https://img.shields.io/badge/downloads-2.8k%2B-yellow)
![Temporal Anomalies Pruned](https://img.shields.io/badge/TVA%20anomalies%20pruned-42-red)
![Cache Hit Rate](https://img.shields.io/badge/cache%20hit%20rate-98.4%25-success)

> **Save tweets, videos, and threads from X/Twitter with a single command.**

> *"In the vast temporal expanse of the internet, tweets vanish like variants diverging from the Sacred Timeline. xotaDown is your temporal anchor—preserving the moment before it is pruned from existence."*  
> — **TVA Temporal Engineering Manual, Vol. 7**

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

## Featured Use Case: The Archivist Initiative

Imagine you're a digital archivist tasked with preserving a historic X/Twitter thread documenting a major world event. The thread spans 47 interconnected tweets, contains video evidence, and the author has a history of deleting content without notice.

**Before xotaDown:** You'd manually screenshot each tweet, miss video content entirely, and lose sleep over the integrity of your archive.

**With xotaDown:**

```bash
# Grab the entire thread at maximum quality with metadata
python xotaDown.py "https://x.com/historian/status/1234567890" \
  --thread \
  --quality best \
  --include-metadata \
  --output ./archive/historic_thread_2026/
```

Result: A complete, timestamped, folder-organized archive with videos, images, and JSON metadata for every tweet—all preserved in one deterministic command. Timeline secured.

---

## Pro Tips

- **Threads?** Pass a tweet URL from the thread and use the `--thread` flag to download the entire conversation.
- **High quality videos:** Add `--quality best` to grab the highest resolution available.
- **Batch downloads:** Save a list of URLs (one per line) and use `--batch urls.txt`.
- **Keep it tidy:** Output is organized in folders by username and date by default.
- **Metadata matters:** Use `--include-metadata` to save tweet JSON alongside media for complete archival integrity.
- **Rate limit awareness:** xotaDown auto-throttles requests. For huge batch jobs, add `--delay 2` to add a 2-second pause between downloads.

---

## Weekly Highlight – 2026-08-02

🌐 **Local-First Metadata Export** – Your downloaded tweets now come with a full JSON metadata companion file. Tags, timestamps, view counts, and full text are preserved locally in structured format, making xotaDown not just a media downloader but a true temporal archiving tool. Pair it with your favorite data analysis pipeline and start mining the Sacred Timeline.

---

## Changelog

### 2026-08-02
- 🆕 **Local-First Metadata Export** – Added `--include-metadata` flag to save JSON companion files for every downloaded tweet.
- ✨ Added `--delay` flag for custom rate-limiting between batch downloads.
- 📦 Reduced memory footprint by 30% when processing large threads.

### 2026-07-30
- 🆕 **Smart Resume** – Added `--resume` flag to skip already-downloaded media and avoid re-downloads.
- 🐛 Fixed crash when tweet contains multi-byte unicode characters in user bio.

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
   `[TVA-PR] Brief description of temporal fix or enhancement`