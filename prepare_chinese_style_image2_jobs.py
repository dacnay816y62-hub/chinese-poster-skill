from __future__ import annotations

import json
import os
from pathlib import Path

from batch_generate_chinese_style_posters import TESTS


OUTPUT_ROOT = Path(os.getenv("CODEX_OUTPUT_ROOT", "outputs"))
OUT_DIR = OUTPUT_ROOT / "images" / "chinese-style-poster-tests-20260813"
JOBS = Path("chinese_style_poster_image2_jobs.jsonl")
MANIFEST = Path("chinese_style_poster_image2_manifest.json")


def main() -> int:
    jobs = []
    manifest = []
    for item in TESTS:
        filename = f"chinese-style-poster-test-{item['id']}.png"
        jobs.append(
            {
                "prompt": item["prompt"],
                "out": filename,
                "size": "1024x1536",
                "quality": "high",
            }
        )
        manifest.append(
            {
                "id": item["id"],
                "theme": item["theme"],
                "title": item["title"],
                "preset": item["preset"],
                "layout": item["layout"],
                "palette": item["palette"],
                "output": str(OUT_DIR / filename),
                "prompt": item["prompt"],
            }
        )

    JOBS.write_text(
        "\n".join(json.dumps(job, ensure_ascii=False) for job in jobs) + "\n",
        encoding="utf-8",
    )
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"jobs={JOBS.resolve()}")
    print(f"manifest={MANIFEST.resolve()}")
    print(f"out_dir={OUT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
