import os
import json

BLOG_ID = os.environ.get("BLOG_ID")

def get_blog_id():
    if not BLOG_ID:
        raise Exception("BLOG_ID secret not found.")
    return BLOG_ID

if __name__ == "__main__":
    print("=" * 60)
    print(f"Blog ID : {get_blog_id()}")
    print("=" * 60)
