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

Instructions:
- Write in natural, friendly English.
- Make readers curious to click.
- Use suitable food emojis.
- Keep it under 180 words.
- Do NOT mention AI.
- Do NOT invent ingredients.
- End with a strong Call-to-Action.
- Add 8-10 relevant hashtags.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
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
