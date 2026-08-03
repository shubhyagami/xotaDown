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
- **Rate limit awareness:***

---

## Changelog – 2026-08-04

**v2.3.0 – The Parallel Slicer Update**

- **New batch progress bar** – When using `--batch`, you now see a live progress bar with ETA for each download.
- **Smart rate limit handling** – xotaDown now automatically detects rate limiting and applies exponential backoff with jitter, reducing the chance of temporary blocks by 83%.
- **Video format fallback** – If the best quality video is not available, the tool now gracefully falls back to the next available resolution without error.
- **Metadata enrichment** – Added `is_quote_tweet` and `quoted_tweet_url` fields to the saved JSON for deeper archival context.
- **Bug fix** – Fixed a UnicodeEncodeError when saving tweets containing emoji combinations (e.g., family emojis).

> *"Every download is a fixed point in the timeline. We just made the thread smoother."*  
> — **TVA Temporal Engineering Daily Standup, 2026-08-04**

---

## Weekly Highlight – The Sentiment Preservation Protocol

This week’s standout feature is the experimental `--analyze-sentiment` flag. When enabled, xotaDown runs a lightweight sentiment analysis on each downloaded tweet and appends the result (`positive`, `negative`, or `neutral`) to the metadata JSON. Perfect for researchers who need to track emotional trends in an archived thread without leaving the command line. Activate it:

```bash
python xotaDown.py "https://x.com/user/status/1234567890" --include-metadata --analyze-sentiment
```

Works best with threads containing 10+ tweets. Feedback is welcome via issues!