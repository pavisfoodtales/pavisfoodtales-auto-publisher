import os
from google import genai

from blog_data import get_latest_blog


def generate_caption():
    blog = get_latest_blog()

    if not blog:
        return None

    client = genai.Client(
        api_key=os.environ["GEMINI_API_KEY"]
    )

    prompt = f"""
You are a professional food blogger and social media marketing expert.

Create a highly engaging Facebook post for the recipe below.

Recipe Title:
{blog['title']}

Recipe Summary:
{blog['summary']}

Recipe Link:
{blog['link']}

Requirements:
- Friendly and natural English
- Maximum 180 words
- Use suitable food emojis
- Create curiosity
- End with a strong Call-to-Action
- Add 8-10 relevant hashtags
- Do NOT mention AI
- Do NOT invent ingredients
"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )

    return response.text.strip()


if __name__ == "__main__":
    caption = generate_caption()

    if caption:
        print("=" * 60)
        print("AI Caption")
        print("=" * 60)
        print(caption)
    else:
        print("Caption generation failed.")
