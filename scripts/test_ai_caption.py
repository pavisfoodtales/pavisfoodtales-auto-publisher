from ai_caption import generate_caption

try:
    caption = generate_caption()

    if caption:
        print("=" * 60)
        print("AI Caption")
        print("=" * 60)
        print(caption)
    else:
        print("Caption generation failed.")

except Exception as e:
    print(f"AI Error: {e}")
