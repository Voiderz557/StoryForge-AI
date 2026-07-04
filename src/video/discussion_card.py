from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import textwrap


FONT_DIR = "C:/Windows/Fonts"


def _font(name: str, size: int):
    return ImageFont.truetype(f"{FONT_DIR}/{name}", size)


def create_discussion_card(title: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    width, height = 850, 320
    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    title_font = _font("arialbd.ttf", 38)
    small_font = _font("arial.ttf", 21)
    tiny_font = _font("arial.ttf", 17)

    # Shadow
    draw.rounded_rectangle(
        (22, 26, width - 18, height - 12),
        radius=38,
        fill=(0, 0, 0, 65),
    )

    # Card
    draw.rounded_rectangle(
        (0, 0, width - 45, height - 45),
        radius=38,
        fill=(255, 255, 255, 250),
    )

    # Avatar
    draw.ellipse((40, 35, 92, 87), fill=(255, 188, 66))
    draw.ellipse((52, 47, 80, 75), fill=(255, 222, 128))

    draw.text((110, 35), "StoryForge", font=small_font, fill=(25, 25, 25))
    draw.text((110, 62), "original story • family safe", font=tiny_font, fill=(115, 115, 115))

    wrapped = textwrap.wrap(title, width=28)
    y = 110
    for line in wrapped[:3]:
        draw.text((40, y), line, font=title_font, fill=(10, 10, 10))
        y += 45

    draw.text((42, height - 88), "♡ 99+", font=small_font, fill=(115, 115, 115))
    draw.text((170, height - 88), "💬 99+", font=small_font, fill=(115, 115, 115))
    draw.text((665, height - 88), "↗ Share", font=small_font, fill=(135, 135, 135))

    image.save(output_path)
    return output_path