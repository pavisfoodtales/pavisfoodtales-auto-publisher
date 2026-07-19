import feedparser
import re

RSS_URL = "https://exploringcookingfood.blogspot.com/feeds/posts/default?alt=rss"


def get_latest_blog():
    feed = feedparser.parse(RSS_URL)

    if not feed.entries:
        return None

    post = feed.entries[0]

    summary = post.summary if "summary" in post else ""

    image_match = re.search(r'<img[^>]+src="([^"]+)"', summary)
    image = image_match.group(1) if image_match else None

    return {
        "title": post.title,
        "link": post.link,
        "published": post.published,
        "summary": summary,
        "image": image,
    }


if __name__ == "__main__":
    blog = get_latest_blog()

    if blog:
        print(blog)
    else:
        print("No blog found.")
