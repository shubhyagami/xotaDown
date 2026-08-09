# xotaDown

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

> **Save tweets, videos, and threads from X/Twitter with a single command.**

---

## Features

- **Single Command Download:** Grab individual tweets, videos, or entire threads effortlessly.
- **Media Extraction:** Automatically downloads attached images and video content alongside the text.
- **Thread Preservation:** Fetches and organizes interconnected tweets chronologically.
- **Local Caching:** Reduces redundant network requests with an efficient local cache.
- **Rate-Limit Handling:** Safely manages X/Twitter API limits and automatically retries failed downloads.

---

## Getting Started

To get started, you only need Python 3.8 or newer and `pip`.

### Quick Start

```bash
# Clone the repository
git clone https://github.com/shubhyagami/xotaDown.git
cd xotaDown

# Install dependencies
pip install -r requirements.txt

# Download a tweet or thread by URL
python xotaDown.py "https://x.com/user/status/1234567890"
```

---

## Use Case: Digital Archiving

If you are a digital archivist or journalist tasked with preserving historic threads, xotaDown simplifies the extraction process. 

Rather than manually screenshotting interconnected tweets—which often breaks context and misses video content—you can pass the root URL of a thread to the tool. xotaDown systematically fetches the entire thread, downloads all associated media, and saves the text locally. This ensures you have a reliable, offline record of the content before it is edited or deleted.

---

## Contributing

Contributions are what make the open-source community such a fantastic place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

### Reporting Bugs

Found a bug? Open an issue and include:

- A clear description of the problem (expected vs. actual behavior).
- Steps to reproduce the issue.
- Your environment details (OS, Python version, etc.).
- Relevant error logs or stack traces.

### Submitting a Pull Request

1. Fork the repository and create a branch from `main`.
2. Follow the existing code style and structure.
3. Add or update tests to cover your changes.
4. Write a clear changelog entry describing what you changed and why.
5. Open a pull request and request a review.

### Coding Standards

- **Python 3.8+**: Ensure your code is compatible with Python 3.8 and above.
- **Type Hints**: Required for all new functions and methods.
- **Docstrings**: Must follow the Google style format.
- **Dependencies**: Avoid adding unnecessary packages. Any new dependency must be clearly justified.
- **Commit Messages**: Use clear, concise messages, e.g., *"fix: corrected retry logic for download timeouts"*.

All accepted contributions earn you a place in the `CONTRIBUTORS.md` file.

---

## Contact

For questions, suggestions, or support, please reach out via [GitHub Discussions](https://github.com/shubhyagami/xotaDown/discussions) or open an issue.

---

## Changelog

### [0.2.0] - 2026-08-09
- Cleaned up README layout and documentation.
- Improved thread-fetching reliability for long threads.
- Added better local cache management to reduce redundant network requests.
