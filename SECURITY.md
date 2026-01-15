# Security Policy

## Supported Versions

- Security fixes target the latest `master` branch. Please re-run scrapers with the current dependency set before opening reports.
- Older sample scripts or pinned Chromedriver builds are not updated once superseded.

## Ecosystem & Compatibility

| Component / Library      | Version(s) / Tooling                     | Notes |
| ------------------------ | ---------------------------------------- | ----- |
| OS baseline              | WSL (Ubuntu 24.04.3 LTS)                 | Matches README instructions. |
| Python runtime           | CPython 3.14.2 (`.python-version`)       | Install dependencies via pip. |
| Core Python packages     | `pandas`, `Pillow`, `selenium`, `urllib3` | See `requirements.txt`. |
| Browser automation       | Google Chrome Stable + matching Chromedriver for installed Chrome (e.g., 131.x; keep in sync with Chrome releases) | Follow README steps to install binaries and export `PATH_TO_WEBDRIVER`. |

## Backward Compatibility

- Scrapers are tested with the Chrome/Chromedriver pairing listed above. We aim to stay compatible with newer Chrome patch releases; older major versions are unsupported.
- Selenium scripts rely on Python 3.14.x semantics. Running them on older Python versions may break and is outside our support window.

## Reporting a Vulnerability

Disclose vulnerabilities privately via GitHub’s **Security → Report a
vulnerability** workflow with:

- Target URL(s) and scraper script name
- Dependency versions (`pip freeze`, Chromedriver build)
- Steps to reproduce and observed impact

We acknowledge within **3 business days** and share updates at least every **7 business days** while triaging.
