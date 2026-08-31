# xotaDown  

[![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python)](https://python.org)  
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![Status](https://img.shields.io/badge/status-active-brightgreen)](https://github.com/shubhyagami/xotaDown)  
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/shubhyagami/xotaDown/pulls)  

A lightweight command‑line tool for saving tweets, media, and full threads from X (formerly Twitter) with a single command.

---  

## Overview  

`xotaDown` simplifies archiving X content. With one CLI call you can:

* download a single tweet,
* fetch an entire thread, or
* pull attached images and videos.

The tool preserves the original order of replies, caches downloads locally, and handles rate‑limit throttling gracefully.

---  

## Key Features  

- **One‑command downloads** – Retrieve a tweet, video, or entire thread with a single invocation.  
- **Media extraction** – Saves images and videos alongside the tweet text.  
- **Thread preservation** – Retrieves and orders all replies correctly.  
- **Local caching** – Stores previously fetched content to avoid redundant network requests.  
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

3. **(Optional) Add to your PATH**  
   ```bash
   echo "$(pwd)/xotaDown" >> ~/.bashrc   # Bash
   source ~/.bashrc
   ```

4. **Run the tool**  
   ```bash
   xotaDown.py "https://x.com/user/status/1234567890"
   ```

   For help, use `xotaDown.py -h`.

---  

## Usage Examples  

- **Download a single tweet**  
  ```bash
  xotaDown.py "https://x.com/elonmusk/status/1523456789"
  ```

- **Download an entire thread**  
  ```bash
  xotaDown.py "https://x.com/elonmusk/status/1523456789" --thread
  ```

- **Specify an output directory**  
  ```bash
  xotaDown.py "https://x.com/user/status/1234567890" -o ./archives
  ```

---  

## Contributing  

Contributions are welcome.

### Reporting Issues  
- Describe expected behavior and what actually happens.  
- Include steps to reproduce, error messages, and environment details (OS, Python version, etc.).  

### Pull Requests  
1. Fork the repository and create a branch from `main`.  
2. Follow the existing code style and structure.  
3. Add or update tests for new functionality.  
4. Update the changelog with a brief entry describing the change.  
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

---  

## License  

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
