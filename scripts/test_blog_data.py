from blog_data import get_latest_blog

blog = get_latest_blog()

if blog:
    print("=" * 50)
    print("Latest Blog Data")
    print("=" * 50)
    print(f"Title     : {blog['title']}")
    print(f"Link      : {blog['link']}")
    print(f"Published : {blog['published']}")
    print(f"Summary   : {blog['summary'][:150]}...")
    print(f"Image     : {blog['image']}")
else:
    print("No blog found.")
