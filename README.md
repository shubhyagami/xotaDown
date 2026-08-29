# xotaDown  

[![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python)](https://python.org)  
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![Status](https://img.shields.io/badge/status-active-brightgreen)](https://github.com/shubhyagami/xotaDown)  
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/shubhyagami/xotaDown/pulls)  

A lightweight command‑line tool for saving tweets, media, and full threads from X (formerly Twitter) with a single command.

---

## Overview  

xotaDown streamlines archiving of X content.  
- Pull individual tweets, videos, or complete threads instantly.  
- Retrieve attached images, videos, and tweets text in one go.  
- Maintain chronological order of thread replies.  
- Cache downloads locally to avoid redundant network requests and gracefully handle rate‑limit throttling.  

Ideal for personal reference, research, journalism, or any workflow that needs reliable social‑media snapshots.

---

## Key Features  

- **One‑command downloads** – Fetch a tweet, a video, or an entire thread with a single CLI call.  
- **Media extraction** – Saves images and videos alongside the tweet text.  
- **Thread preservation** – Retrieves and orders all replies correctly.  
- **Local caching** – Stores previously fetched content to speed up subsequent runs.  
- **Rate‑limit handling** – Manages API limits and retries failed requests automatically.  

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

   *Optional:* Add `xotaDown` to your `PATH` or create an alias for quick access.

---

## Use Cases  

- **Digital archivists** – Capture and preserve social‑media artifacts for research or historical records.  
- **Journalists** – Verify and collect Twitter threads for reporting.  
- **Enthusiasts** – Save tweets, videos, or threads for later reading or sharing.

---

## Contributing  

Contributions are welcome.  

### Reporting Issues  
- Describe the expected behavior and what actually happens.  
- Include steps to reproduce, error messages, and environment details (OS, Python version, etc.).  

### Pull Requests  
1. Fork the repo and create a branch from `main`.  
2. Follow the existing code style and structure.  
3. Add or update tests for new functionality.  
4. Update the changelog with a brief entry describing the change and its purpose.  
5. Open a pull request and request a review.

---

## Contact  

- **Discussions:** https://github.com/shubhyagami/xotaDown/discussions  
- **Issues:** https://github.com/shubhyagami/xotaDown/issues  

Feel free to open a discussion for questions, feature suggestions, or general support.

---

## Changelog  

### 0.2.0 – 2026‑08‑12  
- Refined README layout and overall documentation.  
- Improved thread‑fetching reliability for long threads.  
- Optimized cache handling to reduce redundant downloads.  

### 0.1.0 – 2026‑07‑15  
- Initial release.  
- Core single‑tweet and thread download functionality.  
- Basic media extraction for images and videos.
