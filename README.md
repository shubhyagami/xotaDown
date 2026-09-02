# xotaDown  

[![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python)](https://www.python.org/)  
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![CI](https://github.com/shubhyagami/xotaDown/actions/workflows/ci.yml/badge.svg)](https://github.com/shubhyagami/xotaDown/actions)  
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/shubhyagami/xotaDown/pulls)  

> Lightweight CLI tool for downloading tweets, media, and entire threads from X (formerly Twitter).

---

## Overview  

`xotaDown` lets you archive X content with a single command.  
It supports:

* fetching a single tweet  
* downloading an entire thread in the correct order  
* extracting attached images and videos  
* caching results locally to avoid repeated network traffic  
* handling rate limits automatically

---

## Features  

| Feature | Description |
|---------|-------------|
| **One‑command downloads** | Retrieve any tweet or thread with a single invocation |
| **Media extraction** | Saves images and videos next to the tweet text |
| **Thread ordering** | Reconstructs threads in the correct reply order |
| **Local cache** | Stores fetched tweets to avoid duplicate requests |
| **Rate‑limit handling** | Retries and backs off when approaching API limits |

---

## Installation  

```bash
git clone https://github.com/shubhyagami/xotaDown.git
cd xotaDown
pip install -r requirements.txt
```

If you prefer the executable to be available globally:

```bash
echo "$(pwd)/xotaDown.py" >> ~/.bashrc   # Bash
source ~/.bashrc
```

---

## Usage  

```bash
xotaDown.py "<tweet_url>" [options]
```

### Options  

| Flag | Meaning |
|------|---------|
| `--thread`, `-t` | Download the entire thread starting from the given tweet |
| `-o <dir>`, `--output <dir>` | Change the output directory (defaults to the current directory) |
| `-v`, `--verbose` | Show detailed progress information |
| `-h`, `--help` | Display help message |

### Examples  

```bash
# Download a single tweet
xotaDown.py "https://x.com/elonmusk/status/1523456789"

# Download an entire thread
xotaDown.py "https://x.com/elonmusk/status/1523456789" --thread

# Save to a custom folder
xotaDown.py "https://x.com/user/status/1234567890" -o ./archives
```

---

## Contributing  

Feel free to open issues or pull requests.

### Reporting Issues  

1. Describe what you expected vs. what happened.  
2. Include steps to reproduce, error messages, and your environment (OS, Python version).  

### Pull Requests  

1. Fork the repo and create a branch off `main`.  
2. Follow the existing style and add tests if you’re adding functionality.  
3. Update the changelog with a brief description.  
4. Submit the pull request and request a review.

---

## Support  

- **Discussions** – https://github.com/shubhyagami/xotaDown/discussions  
- **Issues** – https://github.com/shubhyagami/xotaDown/issues  

Feel free to ask questions or suggest new features.

---

## Changelog  

### 0.2.0 – 2026‑08‑12  
- Refined README layout.  
- Improved thread fetching for long threads.  
- Optimized cache to reduce redundant downloads.

### 0.1.0 – 2026‑07‑15  
- Initial release with single‑tweet and thread download, plus basic media extraction.

---

## License  

MIT – see the [LICENSE](LICENSE) file.
