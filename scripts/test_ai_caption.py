from ai_caption import generate_caption

caption = generate_caption()

if caption:
    print(caption)
else:
    print("Caption generation failed.")
