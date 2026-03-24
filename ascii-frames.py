from PIL import Image, ImageDraw, ImageFont
import os

ASCII_CHARS = ["Ñ", "@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".", " . ", " "]

def resize_image(image, new_width=250):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    return image.resize((new_width, new_height))

def pixels_to_ascii(image, new_width=250):
    resized = resize_image(image, new_width)
    pixels = resized.convert("L").getdata()
    characters = ""
    for pixel in pixels:
        if pixel == 255:
            characters += " "
        else:
            characters += ASCII_CHARS[pixel // 25]
    pixel_count = len(characters)
    lines = [characters[i:i + new_width] for i in range(0, pixel_count, new_width)]
    return "\n".join(lines)

def ascii_to_image(ascii_text, font_path=None, font_size=14, bg=(0, 0, 0), fg=(255, 255, 255)):
    try:
        font = ImageFont.truetype(font_path or "/System/Library/Fonts/Menlo.ttc", font_size)
    except:
        font = ImageFont.load_default()

    lines = ascii_text.split("\n")

    dummy = Image.new("RGB", (1, 1))
    draw = ImageDraw.Draw(dummy)
    bbox = draw.textbbox((0, 0), "A", font=font)
    char_w = bbox[2] - bbox[0]
    char_h = bbox[3] - bbox[1]

    img_w = char_w * max(len(line) for line in lines)
    img_h = char_h * len(lines)

    img = Image.new("RGB", (img_w, img_h), color=bg)
    draw = ImageDraw.Draw(img)

    for i, line in enumerate(lines):
        draw.text((0, i * char_h), line, font=font, fill=fg)

    return img

def process_frames(input_dir=".", new_width=250, output_gif="output.gif", fps=10):
    frames = []
    jpg_files = sorted([f for f in os.listdir(input_dir) if f.endswith(".jpg")])

    for filename in jpg_files:
        with Image.open(os.path.join(input_dir, filename)) as image:
            ascii_text = pixels_to_ascii(image, new_width)
            frame_img = ascii_to_image(ascii_text)
            frames.append(frame_img)
            print(f"Rendered {filename}")

    if frames:
        frames[0].save(
            output_gif,
            save_all=True,
            append_images=frames[1:],
            loop=0,
            duration=int(1000 / fps)
        )
        print(f"Saved GIF: {output_gif}")

process_frames()