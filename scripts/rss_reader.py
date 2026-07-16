import feedparser

RSS_URL = "https://exploringcookingfood.blogspot.com/feeds/posts/default?alt=rss"

feed = feedparser.parse(RSS_URL)

print("=" * 60)
print(f"Blog Title : {feed.feed.title}")
print(f"Total Posts Found : {len(feed.entries)}")
print("=" * 60)

for index, post in enumerate(feed.entries, start=1):
    print(f"\nPost #{index}")
    print(f"Title      : {post.title}")
    print(f"Published  : {post.published}")
    print(f"Link       : {post.link}")

    if "summary" in post:
        summary = post.summary.replace("\n", " ").strip()
        print(f"Summary    : {summary[:150]}...")
