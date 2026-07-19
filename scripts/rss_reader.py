import feedparser
import os

RSS_URL = "https://exploringcookingfood.blogspot.com/feeds/posts/default?alt=rss"
LAST_POST_FILE = "data/last_post.txt"

feed = feedparser.parse(RSS_URL)

if not feed.entries:
    print("No posts found.")
    exit()

# Get the latest post
latest_post = feed.entries[0]

title = latest_post.title
link = latest_post.link

print("=" * 60)
print("Latest Blog Post")
print("=" * 60)
print(f"Title : {title}")
print(f"Link  : {link}")
print("=" * 60)

# Read previously processed post
last_link = ""

if os.path.exists(LAST_POST_FILE):
    with open(LAST_POST_FILE, "r", encoding="utf-8") as f:
        last_link = f.read().strip()

# Compare
if last_link == link:
    print("No new blog post found.")
else:
    print("New blog post detected!")

    with open(LAST_POST_FILE, "w", encoding="utf-8") as f:
        f.write(link)

    print("last_post.txt updated successfully.")
