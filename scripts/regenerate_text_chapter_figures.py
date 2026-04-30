from pathlib import Path
import textwrap

import pandas as pd
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
TEXT = ROOT / "data" / "cleaned" / "text" / "text_cleaned.csv"
OUTS = [
    ROOT / "outputs" / "figures" / "part1_data_collection" / "02_text_segments_per_chapter.png",
    ROOT / "outputs" / "figures" / "part1_data_processing" / "02_cleaned_text_segments_per_chapter.png",
]


def font(size=24, bold=False):
    candidates = [
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/calibrib.ttf" if bold else "C:/Windows/Fonts/calibri.ttf",
    ]
    for p in candidates:
        if Path(p).exists():
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def clean_title(title):
    title = str(title)
    # Keep the visible chapter number and title even when the source has mojibake around the dash.
    title = title.replace("鈥?", "-").replace("—", "-").replace("–", "-")
    title = " ".join(title.split())
    return title


def draw_chart(counts, out_path, title):
    W, H = 1800, 1050
    margin_l, margin_r = 140, 70
    margin_t, margin_b = 120, 260
    plot_w = W - margin_l - margin_r
    plot_h = H - margin_t - margin_b

    img = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(img)
    title_f = font(42, True)
    label_f = font(24)
    small_f = font(20)
    tick_f = font(18)

    d.text((W // 2, 42), title, anchor="mm", fill=(20, 20, 20), font=title_f)

    max_v = max(counts.values())
    y_max = ((max_v + 9) // 10) * 10
    if y_max < 10:
        y_max = 10

    # Axes
    x0, y0 = margin_l, H - margin_b
    d.line((x0, margin_t, x0, y0), fill=(60, 60, 60), width=3)
    d.line((x0, y0, W - margin_r, y0), fill=(60, 60, 60), width=3)

    # Grid / y ticks
    for i in range(0, 6):
        val = round(y_max * i / 5)
        y = y0 - (val / y_max) * plot_h
        d.line((x0, y, W - margin_r, y), fill=(225, 225, 225), width=1)
        d.text((x0 - 18, y), str(val), anchor="rm", fill=(60, 60, 60), font=tick_f)

    chapters = list(counts.keys())
    n = len(chapters)
    gap = 18
    bar_w = (plot_w - gap * (n - 1)) / n
    blue = (48, 117, 183)

    for i, ch in enumerate(chapters):
        v = counts[ch]
        x = x0 + i * (bar_w + gap)
        h = (v / y_max) * plot_h
        y = y0 - h
        d.rounded_rectangle((x, y, x + bar_w, y0), radius=4, fill=blue)
        d.text((x + bar_w / 2, y - 12), str(v), anchor="mb", fill=(20, 20, 20), font=small_f)

        short = ch
        if " - " in short:
            parts = short.split(" - ", 1)
            short = parts[0].replace("CHAPTER ", "Ch. ") + "\n" + parts[1]
        short = short.replace("CHAPTER ", "Ch. ")
        lines = []
        for line in short.split("\n"):
            lines.extend(textwrap.wrap(line, width=15) or [""])
        yy = y0 + 18
        for line in lines[:4]:
            d.text((x + bar_w / 2, yy), line, anchor="mt", fill=(30, 30, 30), font=tick_f)
            yy += 22

    # Axis labels
    d.text((W // 2, H - 48), "Chapter", anchor="mm", fill=(20, 20, 20), font=label_f)
    # Rotated y label
    y_label = Image.new("RGBA", (300, 40), (255, 255, 255, 0))
    yd = ImageDraw.Draw(y_label)
    yd.text((150, 20), "Number of text segments", anchor="mm", fill=(20, 20, 20), font=label_f)
    y_label = y_label.rotate(90, expand=True)
    img.paste(y_label, (30, margin_t + plot_h // 2 - y_label.height // 2), y_label)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(out_path)


def main():
    df = pd.read_csv(TEXT)
    df["chapter_title_fixed"] = df["chapter_title"].map(clean_title)
    ordered = (
        df.sort_values(["chapter_index", "text_id"])
        .groupby(["chapter_index", "chapter_title_fixed"], sort=True)
        .size()
    )
    counts = {title: int(v) for (_, title), v in ordered.items()}
    for out in OUTS:
        label = "Raw Text Segments per Chapter" if "part1_data_collection" in str(out) else "Cleaned Text Segments per Chapter"
        draw_chart(counts, out, label)
        print(out)


if __name__ == "__main__":
    main()
