# Siftly

**Siftly** is a lightweight insights engine that helps product teams, developers, and founders understand real user feedback from Reddit and other public sources.

It uses Reddit’s public API to:

- 🔍 Search for user posts related to any product, feature, or topic
- 💬 Analyse sentiment using open-source NLP models (VADER)
- 📊 Score and organise pain points, feature requests, and common complaints

Siftly is designed to help early teams catch recurring user issues without needing a full customer support system or expensive analytics stack.

---

### 🧠 How It Works

1. Enter a keyword or phrase (e.g. “login broken”, “refund policy”)
2. Siftly searches Reddit’s public content using the official API
3. Each post is analysed for **positive, negative, or mixed sentiment **
4. Results are displayed with:
   - Title
   - Subreddit
   - Sentiment scores
   - Reddit URL

---

### 🚧 Project Status

Siftly is in early development. The current version includes:

- ✅ Reddit keyword search + sentiment scoring
- ✅ Command line interface for testing
- ⚙️ Plans to support:
  - YouTube, Hacker News, and Discourse
  - Web dashboard with login
  - CSV export + API access
  - Zapier + Gmail integrations
  - Chrome extension

---

### 🔐 Disclaimer

This tool uses only **public content** accessed through the [Reddit Data API](https://www.redditinc.com/policies/data-api-terms) and is built to comply with all usage guidelines. It does not collect personal data or scrape private content.

---

> Created with ❤️ for teams who want signal, not noise.
