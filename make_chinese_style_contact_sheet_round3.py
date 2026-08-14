from __future__ import annotations

import json
import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUTPUT_ROOT = Path(os.getenv("CODEX_OUTPUT_ROOT", "outputs"))
OUT_DIR = OUTPUT_ROOT / "images" / "chinese-style-poster-tests-round3-20260813"
LOCAL_MANIFEST = Path("chinese_style_poster_image2_manifest_round3.json")
REMOTE_MANIFEST = OUT_DIR / "manifest-image2-round3.json"
CONTACT = OUT_DIR / "contact-sheet-round3.png"


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    REMOTE_MANIFEST.write_text(LOCAL_MANIFEST.read_text(encoding="utf-8"), encoding="utf-8")

    items = json.loads(LOCAL_MANIFEST.read_text(encoding="utf-8"))
    thumb_w, thumb_h = 256, 384
    label_h = 64
    cols = 5
    rows = (len(items) + cols - 1) // cols
    margin = 24
    gap = 18
    sheet_w = margin * 2 + cols * thumb_w + (cols - 1) * gap
    sheet_h = margin * 2 + rows * (thumb_h + label_h) + (rows - 1) * gap
    sheet = Image.new("RGB", (sheet_w, sheet_h), (242, 240, 234))
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()

    for idx, item in enumerate(items):
        path = Path(item["output"])
        if not path.exists():
            raise FileNotFoundError(path)
        col = idx % cols
        row = idx // cols
        x = margin + col * (thumb_w + gap)
        y = margin + row * (thumb_h + label_h + gap)
        img = Image.open(path).convert("RGB")
        img.thumbnail((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        tile = Image.new("RGB", (thumb_w, thumb_h), (255, 255, 255))
        tile.paste(img, ((thumb_w - img.width) // 2, (thumb_h - img.height) // 2))
        sheet.paste(tile, (x, y))
        draw.text((x, y + thumb_h + 8), f"{item['id']} {item['title']} | {item['theme']}", fill=(22, 22, 22), font=font)
        draw.text((x, y + thumb_h + 28), f"{item['preset']} / {item['layout']}", fill=(72, 72, 72), font=font)

    sheet.save(CONTACT)
    print(CONTACT)
    print(REMOTE_MANIFEST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
