import os
import requests

from blog_data import get_latest_blog

ACCESS_TOKEN = os.getenv("FACEBOOK_ACCESS_TOKEN")

PAGE_ID = "122244514670045482"


def publish():
    blog = get_latest_blog()

    if not blog:
        print("No blog found.")
        return

    message = f"""{blog['title']}

{blog['summary']}

Read more:
{blog['link']}
"""

    url = f"https://graph.facebook.com/v25.0/{PAGE_ID}/feed"

    response = requests.post(
        url,
        data={
            "message": message,
            "access_token": ACCESS_TOKEN
        }
    )

    print(response.json())


if __name__ == "__main__":
    publish()
