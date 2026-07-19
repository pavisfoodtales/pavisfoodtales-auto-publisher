import feedparser

RSS_URL = "https://exploringcookingfood.blogspot.com/feeds/posts/default?alt=rss"


def get_latest_blog():
    feed = feedparser.parse(RSS_URL)

    if not feed.entries:
        return None

    post = feed.entries[0]

    return {
        "title": post.title,
        "link": post.link,
        "published": post.published,
        "summary": post.summary if "summary" in post else "",
        "image": post.media_content[0]["url"] if "media_content" in post else None,
    }


if __name__ == "__main__":
    blog = get_latest_blog()

    if blog:
        print(blog)
    else:
        print("No blog found.")
