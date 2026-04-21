from pathlib import Path
import re
import pandas as pd


def split_alice_text(txt_path: Path) -> pd.DataFrame:
    text = txt_path.read_text(encoding="utf-8", errors="ignore")

    # 尝试去掉 Gutenberg 头尾，如果没有也没关系
    start_marker = "*** START OF THE PROJECT GUTENBERG EBOOK"
    end_marker = "*** END OF THE PROJECT GUTENBERG EBOOK"

    start_idx = text.find(start_marker)
    end_idx = text.find(end_marker)

    if start_idx != -1 and end_idx != -1:
        text = text[start_idx:end_idx]




    # 按章节切分
    chapters = re.split(r"\bCHAPTER\s+[IVXLC]+\b\.?", text)
    chapters = [c.strip() for c in chapters if c.strip()]

    rows = []

    for chapter_idx, chapter_text in enumerate(chapters, start=1):
        paragraphs = re.split(r"\n\s*\n", chapter_text)
        paragraphs = [p.strip() for p in paragraphs if len(p.strip()) > 80]

        for para_idx, para in enumerate(paragraphs, start=1):
            rows.append({
                "id": f"alice_ch{chapter_idx:02d}_p{para_idx:03d}",
                "source": "local_txt",
                "text_type": "novel_paragraph",
                "chapter": chapter_idx,
                "paragraph": para_idx,
                "text": para,
                "source_file": str(txt_path)
            })

    return pd.DataFrame(rows)


def main():
    base_dir = Path(__file__).resolve().parent.parent
    txt_path = base_dir / "data" / "raw" / "text" / "alice_original.txt"
    output_path = base_dir / "data" / "raw" / "text" / "alice_text_raw.csv"

    if not txt_path.exists():
        raise FileNotFoundError(f"File not found: {txt_path}")

    df = split_alice_text(txt_path)
    df.to_csv(output_path, index=False, encoding="utf-8-sig")

    print(f"Saved: {output_path}")
    print(f"Rows: {len(df)}")
    print(df.head())


if __name__ == "__main__":
    main()