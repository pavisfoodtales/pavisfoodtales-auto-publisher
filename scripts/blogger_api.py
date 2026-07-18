import os
import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Read secrets from GitHub Actions
BLOG_ID = os.environ.get("BLOG_ID")
REFRESH_TOKEN = os.environ.get("REFRESH_TOKEN")
CLIENT_SECRET_JSON = os.environ.get("GOOGLE_CLIENT_SECRET_JSON")

if not BLOG_ID:
    raise Exception("BLOG_ID secret not found.")

if not REFRESH_TOKEN:
    raise Exception("REFRESH_TOKEN secret not found.")

if not CLIENT_SECRET_JSON:
    raise Exception("GOOGLE_CLIENT_SECRET_JSON secret not found.")

# Load OAuth client credentials
client = json.loads(CLIENT_SECRET_JSON)

creds = Credentials(
    token=None,
    refresh_token=REFRESH_TOKEN,
    token_uri="https://oauth2.googleapis.com/token",
    client_id=client["installed"]["client_id"],
    client_secret=client["installed"]["client_secret"],
)

# Connect to Blogger API
service = build("blogger", "v3", credentials=creds)

# Get latest posts
posts = (
    service.posts()
    .list(blogId=BLOG_ID, maxResults=5)
    .execute()
)

print("=" * 60)
print("✅ Connected to Blogger API")
print("=" * 60)

for post in posts.get("items", []):
    print(f"Title     : {post['title']}")
    print(f"Published : {post['published']}")
    print(f"URL       : {post['url']}")
    print("-" * 60)
