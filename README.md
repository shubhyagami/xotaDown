# xotaDown

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue?logo=python)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)

A command‑line tool for saving tweets, videos, and threads from X (Twitter) with a single command.

---

## Overview

xotaDown simplifies the process of downloading tweets, media, and full threads from X (formerly Twitter). With one command you can fetch a tweet’s text, images, and videos, and the tool automatically preserves entire thread contexts. It’s ideal for archiving, research, journalism, or personal reference.

---

## Key Features

- **Single‑Command Downloads** – Pull individual tweets, videos, or complete threads instantly.  
- **Media Extraction** – Saves attached images and videos alongside the tweet text.  
- **Thread Preservation** – Retrieves and orders all replies in chronological sequence.  
- **Local Caching** – Caches downloads to avoid redundant network requests.  
- **Rate‑Limit Management** – Handles X/Twitter API limits gracefully and retries failed fetches.

---

## Getting Started

1. **Clone the repository**  
   ```bash
   git clone https://github.com/shubhyagami/xotaDown.git
   cd xotaDown
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the tool**  
   ```bash
   python xotaDown.py "https://x.com/user/status/1234567890"
   ```

*Tip:* Add `xotaDown` to your `PATH` or create an alias for quick access.

---

## Use Cases

- **Digital archivists** – Preserve social media content for historical or research purposes.  
- **Journalists** – Collect and verify information from Twitter threads for reporting.  
- **Social media enthusiasts** – Save tweets, videos, and threads for personal reference or sharing.

---

## Contributing

Contributions keep the project vibrant. Follow these steps to get involved:

### Reporting Bugs
- Provide a concise description of the issue (expected vs. actual behavior).  
- List steps to reproduce and any relevant error logs or stack traces.  
- Include environment details (OS, Python version, etc.).

### Pull Requests
1. Fork the repo and branch from `main`.  
2. Adhere to the existing code style and structure.  
3. Add or update tests covering your changes.  
4. Write a clear changelog entry describing the modification and its reason.  
5. Submit a pull request and request a review.

---

## Contact

For questions, suggestions, or support, join the discussion:

- **GitHub Discussions**: https://github.com/shubhyagami/xotaDown/discussions  
- **Open issues**: https://github.com/shubhyagami/xotaDown/issues

---

## Changelog

### 0.2.0 – 2026‑08‑12  
- Refined README layout and overall documentation.  
- Strengthened thread‑fetching reliability for long threads.  
- Optimized local cache handling to minimise redundant downloads.

### 0.1.0 – 2026‑07‑15  
- Initial release.  
- Core functionality for single‑tweet and thread downloads.  
- Basic media extraction for images and videos.
