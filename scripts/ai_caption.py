from blog_data import get_latest_blog


def generate_caption():
    blog = get_latest_blog()

    if not blog:
        return None

    caption = f"""
🍽️ {blog['title']}

{blog['summary'][:250]}...

👉 Read the full recipe:
{blog['link']}

#Food #Recipe #Cooking #PavisFoodTales
"""

    return caption.strip()


if __name__ == "__main__":
    caption = generate_caption()

    if caption:
        print("=" * 60)
        print("AI Caption")
        print("=" * 60)
        print(caption)
