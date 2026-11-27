#!/usr/bin/env python3
"""Draw the 27 November 2026 world-news front page.

Run from the entry directory:
    python3 tools/generate_image.py
Writes entry.png (1024x1024, deterministic) next to main.py.
This script is only for local reproduction; the grader runs main.py,
which copies the PNG it produces here.
"""
from PIL import Image, ImageDraw, ImageFont

SIZE = 1024
PAPER = (247, 242, 231)
INK = (17, 17, 17)
RED = (185, 28, 28)
NAVY = (30, 58, 95)
GREY = (90, 86, 78)
CREAM = (233, 226, 210)
WHITE = (255, 255, 255)
GOLD = (255, 214, 64)

SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def load(path, size):
    return ImageFont.truetype(path, size)


def wrap_text(draw, text, font, max_width):
    words = text.split()
    lines, current = [], ""
    for word in words:
        trial = (current + " " + word).strip()
        if draw.textlength(trial, font=font) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_para(draw, x, y, text, font, max_width, fill=INK, gap=4):
    for line in wrap_text(draw, text, font, max_width):
        draw.text((x, y), line, font=font, fill=fill)
        y += font.size + gap
    return y


def pictogram(draw, cx, cy, kind, colour):
    """Flat white pictogram on a coloured disc, radius 34."""
    draw.ellipse([cx - 34, cy - 34, cx + 34, cy + 34], fill=colour)
    w = WHITE
    if kind == "drone":
        draw.rectangle([cx - 10, cy - 6, cx + 10, cy + 6], fill=w)
        draw.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=colour)
        for sx, sy in ((-20, -16), (20, -16), (-20, 16), (20, 16)):
            draw.line([cx, cy, cx + sx, cy + sy], fill=w, width=3)
            draw.ellipse([cx + sx - 7, cy + sy - 3, cx + sx + 7, cy + sy + 3],
                         fill=w)
    elif kind == "flame":
        draw.polygon([(cx, cy - 22), (cx + 14, cy + 2), (cx + 6, cy + 16),
                      (cx - 6, cy + 16), (cx - 14, cy + 2)], fill=w)
        draw.ellipse([cx - 6, cy + 6, cx + 6, cy + 18], fill=colour)
    elif kind == "ship":
        draw.polygon([(cx - 20, cy + 2), (cx + 20, cy + 2), (cx + 14, cy + 16),
                      (cx - 14, cy + 16)], fill=w)
        draw.rectangle([cx - 4, cy - 16, cx + 4, cy + 2], fill=w)
        draw.rectangle([cx - 12, cy - 12, cx + 12, cy - 8], fill=w)
    elif kind == "storm":
        draw.ellipse([cx - 20, cy - 12, cx - 2, cy + 4], fill=w)
        draw.ellipse([cx - 8, cy - 18, cx + 14, cy + 2], fill=w)
        draw.ellipse([cx + 4, cy - 10, cx + 22, cy + 4], fill=w)
        draw.polygon([(cx - 2, cy + 4), (cx + 6, cy + 4), (cx - 2, cy + 14),
                      (cx + 6, cy + 14), (cx - 4, cy + 24), (cx + 2, cy + 12)],
                     fill=GOLD)
    elif kind == "flags":
        draw.rectangle([cx - 18, cy - 18, cx - 2, cy - 2], fill=w)
        draw.rectangle([cx + 2, cy - 18, cx + 18, cy - 2], outline=w, width=3)
        draw.line([cx - 18, cy - 18, cx - 18, cy + 18], fill=w, width=3)
        draw.line([cx + 18, cy - 18, cx + 18, cy + 18], fill=w, width=3)
    elif kind == "eu":
        for i in range(8):
            import math
            a = math.pi * i / 4.0
            x = cx + int(20 * math.cos(a))
            y = cy + int(20 * math.sin(a))
            draw.ellipse([x - 3, y - 3, x + 3, y + 3], fill=GOLD)
        draw.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=w)
    elif kind == "chart":
        draw.line([cx - 20, cy + 18, cx + 20, cy + 18], fill=w, width=3)
        draw.line([cx - 20, cy - 18, cx - 20, cy + 18], fill=w, width=3)
        draw.line([cx - 16, cy - 12, cx - 4, cy - 2, cx + 6, cy - 8,
                   cx + 18, cy + 10], fill=w, width=4)
        draw.polygon([(cx + 18, cy + 10), (cx + 10, cy + 8), (cx + 14, cy + 16)],
                     fill=w)
    elif kind == "chess":
        draw.ellipse([cx - 7, cy - 20, cx + 7, cy - 6], fill=w)
        draw.polygon([(cx - 6, cy - 8), (cx + 8, cy - 14), (cx + 10, cy + 4),
                      (cx - 10, cy + 4)], fill=w)
        draw.rectangle([cx - 14, cy + 6, cx + 14, cy + 12], fill=w)
        draw.rectangle([cx - 18, cy + 14, cx + 18, cy + 20], fill=w)


def build():
    img = Image.new("RGB", (SIZE, SIZE), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([8, 8, SIZE - 9, SIZE - 9], outline=INK, width=4)

    # Masthead
    d.rectangle([8, 8, SIZE - 9, 112], fill=INK)
    d.text((28, 18), "THE WORLD IN ONE DAY",
           font=load(SERIF_BOLD, 54), fill=WHITE)
    d.text((28, 76), "FRIDAY  27  NOVEMBER  2026",
           font=load(SANS_BOLD, 22), fill=GOLD)
    d.text((830, 76), "EIGHT STORIES", font=load(SANS_BOLD, 18), fill=WHITE)

    y = 124
    # Lead: Kuwait drone strike
    d.rectangle([28, y, 996, y + 138], fill=WHITE, outline=INK, width=2)
    d.rectangle([28, y, 40, y + 138], fill=RED)
    d.text((58, y + 8), "MIDDLE EAST  \u2022  KUWAIT  \u2014  LEAD STORY",
           font=load(SANS_BOLD, 19), fill=RED)
    d.text((58, y + 32), "DRONE STRIKE IN KUWAIT KILLS 2",
           font=load(SERIF_BOLD, 40), fill=INK)
    draw_para(d, 58, y + 86,
              "Two Italian technicians were killed at a Kuwait air-defence site "
              "in a drone attack Italy and Kuwait blamed on Iran. "
              "Tehran denied any role.",
              load(SANS_REG, 20), 800)
    pictogram(d, 928, y + 69, "drone", RED)

    # Second: Trump tells Putin to pull back
    y += 150
    d.rectangle([28, y, 996, y + 122], fill=CREAM, outline=INK, width=2)
    d.text((58, y + 8), "DIPLOMACY  \u2022  UNITED STATES",
           font=load(SANS_BOLD, 19), fill=NAVY)
    d.text((58, y + 32), "TRUMP TELLS PUTIN: PULL BACK",
           font=load(SERIF_BOLD, 30), fill=INK)
    draw_para(d, 58, y + 74,
              "Trump said he told Putin in China last week to pull back all "
              "military aggression in Europe, hoping for a quick deal to end "
              "the war in Ukraine.",
              load(SANS_REG, 19), 800)
    pictogram(d, 928, y + 61, "flags", NAVY)

    # Grid: six stories, 2 columns x 3 rows
    y += 134
    grid = [
        ("ASIA  \u2022  THAILAND", "BANGKOK OIL BLAST INJURES 7",
         "An explosion at the Bangchak oil depot in Bangkok injured seven "
         "people, four critically, and forced evacuations nearby.",
         "flame", (176, 92, 0)),
        ("EUROPE  \u2022  SPAIN", "TANKER CAPSIZES OFF IBIZA, 1 DEAD",
         "The Malta-flagged tanker Med Emre capsized off Ibiza with up to "
         "7,000 tonnes of diesel aboard. One crew member died.",
         "ship", (0, 90, 120)),
        ("WEATHER  \u2022  UNITED STATES", "THANKSGIVING STORM CUTS POWER TO 800,000",
         "A powerful storm cut power to more than 800,000 homes on the US "
         "East Coast and forced New York to postpone the Macy's parade.",
         "storm", (90, 90, 90)),
        ("EUROPE  \u2022  EUROPEAN UNION", "EU SPLIT OVER $49BN UKRAINE LOAN",
         "After more than 12 hours of talks in Brussels, EU leaders failed "
         "to agree on the budget or a $49 billion loan for Ukraine.",
         "eu", NAVY),
        ("EUROPE  \u2022  UNITED KINGDOM", "UK NET MIGRATION FALLS TO 77,000",
         "Net migration fell to 77,000 in the year to June, the lowest since "
         "1997 outside the pandemic, official figures showed.",
         "chart", (120, 20, 20)),
        ("SPORT  \u2022  CHESS", "CHESS: GUKESH, SINDAROV DRAW GAME 3",
         "Gukesh and Sindarov drew a 60-move Game 3 in Geneva. The World "
         "Championship match stands level at 1.5-1.5.",
         "chess", (0, 120, 60)),
    ]
    cw, ch, gap = 474, 164, 12
    for i, (tag, head, body, kind, col) in enumerate(grid):
        x = 28 + (i % 2) * (cw + gap)
        yy = y + (i // 2) * (ch + gap)
        d.rectangle([x, yy, x + cw, yy + ch], fill=WHITE, outline=INK, width=2)
        d.text((x + 16, yy + 8), tag, font=load(SANS_BOLD, 16), fill=col)
        hy = draw_para(d, x + 16, yy + 30, head, load(SERIF_BOLD, 23), cw - 104)
        draw_para(d, x + 16, max(hy + 4, yy + 94), body, load(SANS_REG, 17), cw - 32)
        pictogram(d, x + cw - 48, yy + 46, kind, col)

    # Ticker + footer
    y += 3 * ch + 2 * gap + 12
    d.rectangle([28, y, 996, y + 44], fill=INK)
    d.text((40, y + 11),
           "ALSO TODAY:  De Cos to lead ECB  \u2022  Hamas weighs reply as 10 die in Gaza  \u2022  Nepal: 213 presumed dead",
           font=load(SANS_BOLD, 15), fill=WHITE)
    d.text((28, y + 54),
           "Reported Friday 27 November 2026  \u2022  Sources in the repository README",
           font=load(SANS_REG, 15), fill=GREY)

    img.save("entry.png", format="PNG", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    build()
