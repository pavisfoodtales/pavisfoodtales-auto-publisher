import os
from openai import OpenAI

from blog_data import get_latest_blog


def generate_caption():
    blog = get_latest_blog()

    if not blog:
        return None

    client = OpenAI(
        api_key=os.environ["OPENROUTER_API_KEY"],
        base_url="https://openrouter.ai/api/v1",
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
- Friendly and natural English.
- Maximum 180 words.
- Use suitable food emojis.
- Create curiosity.
- End with a strong Call-to-Action.
- Add 8-10 relevant hashtags.
- Do NOT mention AI.
- Do NOT invent ingredients.
"""

    response = client.chat.completions.create(
        model="deepseek/deepseek-chat-v3-0324:free",
        messages=[
            {
                "role": "system",
                "content": "You are an expert food blogger and social media marketer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.8,
        max_tokens=300,
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    caption = generate_caption()

    if caption:
        print("=" * 60)
        print("AI Caption")
        print("=" * 60)
        print(caption)
    else:
        print("Caption generation failed.")
