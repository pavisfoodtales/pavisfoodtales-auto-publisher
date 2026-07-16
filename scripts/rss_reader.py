import feedparser

RSS_URL = "https://exploringcookingfood.blogspot.com/feeds/posts/default?alt=rss"

feed = feedparser.parse(RSS_URL)

if not feed.entries:
    print("No posts found.")
    exit()

latest = feed.entries[0]

print("Latest Post")
print("------------")
print("Title:", latest.title)
print("Link:", latest.link)
print("Published:", latest.published)

if "summary" in latest:
    print("Summary:", latest.summary[:300])
