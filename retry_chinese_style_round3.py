from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path


SKILL_SCRIPT = Path(os.getenv("MALIANG_IMAGE_SCRIPT", "generate_image.py"))
OUTPUT_ROOT = Path(os.getenv("CODEX_OUTPUT_ROOT", "outputs"))
OUT_DIR = OUTPUT_ROOT / "images" / "chinese-style-poster-tests-round3-20260813"
TEMP_DIR = OUTPUT_ROOT / "temp" / "chinese-style-poster-round3-20260813"
JOBS = Path("chinese_style_poster_image2_jobs_round3.jsonl")
LOCAL_MANIFEST = Path("chinese_style_poster_image2_manifest_round3.json")
REMOTE_MANIFEST = OUT_DIR / "manifest-image2-round3.json"
RUN_LOG = TEMP_DIR / "retry-run-log.jsonl"


def looks_like_png(path: Path) -> bool:
    if not path.exists() or path.stat().st_size < 1024:
        return False
    with path.open("rb") as f:
        return f.read(8) == b"\x89PNG\r\n\x1a\n"


def write_log(record: dict) -> None:
    TEMP_DIR.mkdir(parents=True, exist_ok=True)
    with RUN_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    TEMP_DIR.mkdir(parents=True, exist_ok=True)

    if LOCAL_MANIFEST.exists():
        REMOTE_MANIFEST.write_text(LOCAL_MANIFEST.read_text(encoding="utf-8"), encoding="utf-8")

    jobs = [json.loads(line) for line in JOBS.read_text(encoding="utf-8").splitlines() if line.strip()]
    failed: list[str] = []

    for index, job in enumerate(jobs, start=1):
        out = OUT_DIR / job["out"]
        meta = out.with_suffix(".json")
        if looks_like_png(out):
            print(f"SKIP {index:02d}/{len(jobs)} {out.name}", flush=True)
            write_log({"index": index, "out": str(out), "status": "skipped"})
            continue

        print(f"START {index:02d}/{len(jobs)} {out.name}", flush=True)
        cmd = [
            sys.executable,
            str(SKILL_SCRIPT),
            "-m",
            "gpt-image-2",
            job["prompt"],
            "-o",
            str(out),
            "--json-out",
            str(meta),
            "--meta",
            "--timeout",
            "300",
        ]

        proc = subprocess.run(cmd, text=True, capture_output=True)
        record = {
            "index": index,
            "out": str(out),
            "meta": str(meta),
            "returncode": proc.returncode,
            "stdout": proc.stdout[-4000:],
            "stderr": proc.stderr[-4000:],
        }

        if proc.returncode == 0 and looks_like_png(out):
            record["status"] = "done"
            record["bytes"] = out.stat().st_size
            print(f"DONE {index:02d}/{len(jobs)} {out.name} bytes={record['bytes']}", flush=True)
        else:
            record["status"] = "failed"
            failed.append(out.name)
            print(f"FAIL {index:02d}/{len(jobs)} {out.name}", flush=True)
            if proc.stderr:
                print(proc.stderr[-1200:], flush=True)

        write_log(record)

    if failed:
        print("FAILED " + ", ".join(failed), flush=True)
        print(f"LOG {RUN_LOG}", flush=True)
        return 1

    print(f"ALL_DONE {OUT_DIR}", flush=True)
    print(f"LOG {RUN_LOG}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
