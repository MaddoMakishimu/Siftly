import os
from dotenv import load_dotenv
from pathlib import Path
import praw
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Print current path for verification
env_path = Path(__file__).resolve().parent / '.env'
print("CURRENT PATH:", Path(__file__).resolve().parent)
print("LOOKING FOR .env AT:", env_path)

# Load .env file
load_dotenv(dotenv_path=env_path)

# Debug print ALL values loaded
print("DEBUG: ENABLE_REDDIT =", os.getenv("ENABLE_REDDIT"))
print("DEBUG: CLIENT_ID =", os.getenv("REDDIT_CLIENT_ID"))
print("DEBUG: CLIENT_SECRET =", os.getenv("REDDIT_CLIENT_SECRET"))
print("DEBUG: USER_AGENT =", os.getenv("REDDIT_USER_AGENT"))

REDDIT_ENABLED = os.getenv("ENABLE_REDDIT", "false").lower() == "true"

if not REDDIT_ENABLED:
    print("Reddit source disabled. Exiting.")
    exit()

# Initialize Reddit client using env vars
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
)

# Sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

def search_and_score(keyword, subreddit=None, limit=25):
    query = f"{keyword}"
    results = reddit.subreddit(subreddit).search(query, limit=limit) if subreddit else reddit.subreddit("all").search(query, limit=limit)

    scored_posts = []

    for post in results:
        text = post.title + " " + post.selftext
        sentiment = analyzer.polarity_scores(text)
        scored_posts.append({
            "title": post.title,
            "url": f"https://reddit.com{post.permalink}",
            "score": post.score,
            "created_utc": post.created_utc,
            "sentiment": sentiment,
            "subreddit": post.subreddit.display_name
        })

    return scored_posts

if __name__ == "__main__":
    keyword = input("Enter a keyword to search: ")
    use_sub = input("Search specific subreddit? (y/n): ").lower()
    sub = input("Enter subreddit name: ") if use_sub == "y" else None

    posts = search_and_score(keyword, subreddit=sub)

    print("\nTop results:")
    for p in posts:
        print(f"\n[{p['subreddit']}] {p['title']}")
        print(f"Sentiment: {p['sentiment']}")
        print(f"Score: {p['score']} | URL: {p['url']}")
