#!/usr/bin/env python3
import sys
from pathlib import Path


def extract_pdf_text(pdf_path: Path) -> str:
    try:
        from pypdf import PdfReader
    except Exception as e:
        print("ERROR: pypdf is not installed. Install with: pip install pypdf", file=sys.stderr)
        raise

    reader = PdfReader(str(pdf_path))
    texts = []
    for page in reader.pages:
        try:
            texts.append(page.extract_text() or "")
        except Exception:
            texts.append("")
    return "\n\n".join(texts)


def main():
    if len(sys.argv) < 3:
        print("Usage: extract_pdf_text.py <input.pdf> <output.txt>")
        sys.exit(1)

    in_path = Path(sys.argv[1]).expanduser()
    out_path = Path(sys.argv[2]).expanduser()

    if not in_path.exists():
        print(f"ERROR: Input file not found: {in_path}", file=sys.stderr)
        sys.exit(2)

    text = extract_pdf_text(in_path)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")
    print(f"Wrote text to {out_path}")


if __name__ == "__main__":
    main()
