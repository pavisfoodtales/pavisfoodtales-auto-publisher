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

    try:
        print("Using OpenRouter Free Models Router...")

        response = client.chat.completions.create(
            model="openrouter/free",
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
            extra_headers={
                "HTTP-Referer": "https://github.com/pavisfoodtales/pavisfoodtales-auto-publisher",
                "X-Title": "Pavi's Food Tales Auto Publisher"
            }
        )

        print("Caption generated successfully!")
        return response.choices[0].message.content.strip()

    except Exception as e:
        print("AI Error:")
        print(e)
        return None


if __name__ == "__main__":
    caption = generate_caption()

    if caption:
        print("=" * 60)
        print("AI Caption")
        print("=" * 60)
        print(caption)
    else:
        print("Caption generation failed.")
