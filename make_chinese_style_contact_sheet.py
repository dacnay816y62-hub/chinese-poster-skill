from __future__ import annotations

import json
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT_DIR = Path(r"D:\Codex_Outputs\images\chinese-style-poster-tests-20260813")
LOCAL_MANIFEST = Path("chinese_style_poster_image2_manifest.json")
REMOTE_MANIFEST = OUT_DIR / "manifest-image2.json"
CONTACT = OUT_DIR / "contact-sheet.png"


def main() -> int:
    if LOCAL_MANIFEST.exists():
        shutil.copyfile(LOCAL_MANIFEST, REMOTE_MANIFEST)

    items = json.loads(LOCAL_MANIFEST.read_text(encoding="utf-8"))
    thumb_w, thumb_h = 256, 384
    label_h = 64
    cols = 5
    rows = 3
    margin = 24
    gap = 18
    sheet_w = margin * 2 + cols * thumb_w + (cols - 1) * gap
    sheet_h = margin * 2 + rows * (thumb_h + label_h) + (rows - 1) * gap
    sheet = Image.new("RGB", (sheet_w, sheet_h), (242, 240, 234))
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()

    for idx, item in enumerate(items):
        col = idx % cols
        row = idx // cols
        x = margin + col * (thumb_w + gap)
        y = margin + row * (thumb_h + label_h + gap)
        img = Image.open(item["output"]).convert("RGB")
        img.thumbnail((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        tile = Image.new("RGB", (thumb_w, thumb_h), (255, 255, 255))
        ox = (thumb_w - img.width) // 2
        oy = (thumb_h - img.height) // 2
        tile.paste(img, (ox, oy))
        sheet.paste(tile, (x, y))
        label = f"{item['id']} {item['title']} | {item['theme']}"
        draw.text((x, y + thumb_h + 8), label, fill=(22, 22, 22), font=font)
        draw.text((x, y + thumb_h + 28), f"{item['preset']} / {item['layout']}", fill=(72, 72, 72), font=font)

    sheet.save(CONTACT)
    print(CONTACT)
    print(REMOTE_MANIFEST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
