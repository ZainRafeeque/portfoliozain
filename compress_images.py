"""Compress all portfolio images to WebP @ <= 1600px wide.

Run from repo root:
    python compress_images.py
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).parent
MAX_WIDTH = 1600
QUALITY = 82  # 80-85 is the sweet spot for WebP

# Files to convert (skip already-tiny ones and the CV)
SKIP = {"compress_images.py", "Zain-Rafeeque-CV-2026.pdf", "index.html", "README.md"}


def compress_one(src: Path) -> tuple[Path, int, int]:
    """Compress a single image. Returns (output_path, before_bytes, after_bytes)."""
    before = src.stat().st_size
    img = Image.open(src)
    # Drop alpha for JPGs/WebPs targeted at JPEG-style backgrounds
    if img.mode in ("RGBA", "LA"):
        # Composite onto a dark background to match the portfolio
        bg = Image.new("RGB", img.size, (10, 10, 10))
        bg.paste(img, mask=img.split()[-1])
        img = bg
    elif img.mode != "RGB":
        img = img.convert("RGB")

    if img.width > MAX_WIDTH:
        new_h = int(img.height * MAX_WIDTH / img.width)
        img = img.resize((MAX_WIDTH, new_h), Image.LANCZOS)

    out = src.with_suffix(".webp")
    img.save(out, "WEBP", quality=QUALITY, method=6)
    after = out.stat().st_size
    return out, before, after


def main() -> None:
    candidates = [
        p for p in ROOT.iterdir()
        if p.is_file()
        and p.suffix.lower() in {".png", ".jpg", ".jpeg"}
        and p.name not in SKIP
    ]
    candidates.sort()

    total_before = 0
    total_after = 0
    print(f"{'file':<55} {'before':>10} {'after':>10} {'savings':>8}")
    print("-" * 90)
    for src in candidates:
        out, before, after = compress_one(src)
        total_before += before
        total_after += after
        pct = 100 * (1 - after / before)
        print(f"{src.name:<55} {before/1024:>9.1f}K {after/1024:>9.1f}K {pct:>7.1f}%")
    print("-" * 90)
    print(f"{'TOTAL':<55} {total_before/1024:>9.1f}K {total_after/1024:>9.1f}K "
          f"{100*(1-total_after/total_before):>7.1f}%")
    print(f"\nWrote .webp files alongside originals. Update index.html to use the new names,")
    print(f"then you can delete the original .png/.jpg files.")


if __name__ == "__main__":
    main()
