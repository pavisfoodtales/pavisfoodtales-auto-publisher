import feedparser

RSS_URL = "https://exploringcookingfood.blogspot.com/feeds/posts/default?alt=rss"

feed = feedparser.parse(RSS_URL)

print(f"Blog Title: {feed.feed.title}")
print(f"Total Posts Found: {len(feed.entries)}")

if feed.entries:
    latest = feed.entries[0]
    print("\nLatest Post")
    print("Title:", latest.title)
    print("Link :", latest.link)
