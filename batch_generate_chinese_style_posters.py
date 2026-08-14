from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


SKILL_SCRIPT = Path(r"D:\Codex_Moved_From_C\.codex\skills\ML-img\scripts\generate_image.py")
OUT_DIR = Path(r"D:\Codex_Outputs\images\chinese-style-poster-tests-20260813")
MANIFEST = OUT_DIR / "manifest.json"


TESTS = [
    {
        "id": "01",
        "theme": "故宫中轴",
        "title": "中轴",
        "preset": "F01 魏碑 · 雄浑",
        "layout": "L11 超大标题 + 微型信息型",
        "palette": "palace-wall red, dark gray, muted gold, quiet ivory",
        "prompt": "Create a refined 3:4 contemporary Chinese / Oriental poster. Theme: Forbidden City central axis / 故宫中轴. Main title: \"中轴\". Calligraphy preset: F01 Wei tablet, square heavy carved strokes, structural and monumental. Layout preset: L11 oversized title plus micro information, title occupies more than 40 percent of the field, tiny museum annotations. Translate the subject into abstract graphic elements: a vertical ceremonial axis, large palace-wall red rectangular fields, thin eave-like horizontal black-gray lines, courtyard negative space, one muted gold alignment mark. Use generous negative space, clear visual hierarchy, refined Chinese typography, tiny English annotation \"IMPERIAL AXIS\", restrained small seal, premium clean paper texture, contemporary editorial composition. Palette: palace-wall red, dark gray, muted gold, quiet ivory. Avoid tourist postcard architecture, generic Chinese decoration, excessive gold, excessive red seals, ink mountains, and template-like layout.",
    },
    {
        "id": "02",
        "theme": "景德镇瓷器",
        "title": "瓷光",
        "preset": "F04 行楷 · 文人",
        "layout": "L03 中心圆相型",
        "palette": "porcelain white, cobalt blue, kiln-earth yellow, soft warm gray",
        "prompt": "Create a refined 3:4 contemporary Chinese / Oriental poster. Theme: Jingdezhen porcelain / 景德镇瓷器. Main title: \"瓷光\". Calligraphy preset: F04 literati semi-cursive, readable, elegant, lightly flowing. Layout preset: L03 central circular form, a vessel-mouth circle as the poster anchor. Translate the subject into abstract graphic elements: translucent porcelain contour, cobalt blue floral fragments, vertical glaze-flow lines, a small kiln-fire earth-yellow accent. Use generous negative space, clear visual hierarchy, refined Chinese typography, small English annotations \"PORCELAIN LIGHT\" and \"JINGDEZHEN\", restrained seal marks, premium paper and porcelain-smooth texture, contemporary editorial composition. Palette: porcelain white, cobalt blue, kiln-earth yellow, soft warm gray. Avoid generic vases, tourist souvenir feeling, excessive blue pattern clutter, template-like layouts, and ink landscape.",
    },
    {
        "id": "03",
        "theme": "苗族银饰服饰",
        "title": "银脉",
        "preset": "F10 当代手写 · 实验",
        "layout": "L12 图形主导型",
        "palette": "indigo, silver gray, dark brown, faint wax white",
        "prompt": "Create a refined 3:4 contemporary Chinese / Oriental poster. Theme: Miao silver jewelry and traditional clothing / 苗族银饰服饰. Main title: \"银脉\". Calligraphy preset: F10 contemporary handwritten experimental, stretched strokes, asymmetric designer lettering, not childish. Layout preset: L12 graphic-led composition where abstract patterns dominate and title is secondary. Translate the subject into abstract graphic elements: silver arcs and rings, pleated skirt radial lines, indigo batik blocks, embroidery geometry, one dark-brown textile grounding strip. Use generous negative space, clear visual hierarchy, refined Chinese typography, small English annotation \"SILVER THREADS\", restrained seal, premium textile-paper texture, contemporary editorial composition. Palette: indigo, silver gray, dark brown, faint wax white. Avoid costume illustration, folk-tourism poster style, excessive ornament, unrelated clouds or mountains.",
    },
    {
        "id": "04",
        "theme": "敦煌壁画",
        "title": "沙色飞天",
        "preset": "F08 篆意 · 古朴",
        "layout": "L08 下沉景观型",
        "palette": "stone green, ocher, sand yellow, cinnabar, warm off-white",
        "prompt": "Create a refined 3:4 contemporary Chinese / Oriental poster. Theme: Dunhuang mural fragments / 敦煌壁画. Main title: \"沙色飞天\". Calligraphy preset: F08 seal-inspired ancient rounded pictographic feeling, graphic and mysterious. Layout preset: L08 sinking landscape, large empty upper field, visual fragments concentrated in the lower half. Translate the subject into abstract graphic elements: linear flying ribbons, mural color fragments, geometric cave openings, sand-yellow granular texture, a restrained cinnabar accent. Use generous negative space, clear visual hierarchy, refined Chinese typography, small English annotation \"DUNHUANG FRAGMENTS\", one small abstract seal, premium mineral-pigment paper texture, contemporary editorial composition. Palette: stone green, ocher, sand yellow, cinnabar, warm off-white. Avoid religious overstatement, fake antique dirt, tourist mural copy, excessive decoration.",
    },
    {
        "id": "05",
        "theme": "龙舟竞渡",
        "title": "竞渡",
        "preset": "F06 草书 · 狂放",
        "layout": "L07 满版书法型",
        "palette": "river blue-gray, cinnabar, black ink, foam white",
        "prompt": "Create a refined 3:4 contemporary Chinese / Oriental poster. Theme: dragon boat race / 龙舟竞渡. Main title: \"竞渡\". Calligraphy preset: F06 wild cursive with flying-white strokes and strong motion; the characters become the main graphic. Layout preset: L07 full-page calligraphy occupying about 55 percent of the poster. Translate the subject into abstract graphic elements: river-current blue-gray bands, oar rhythm as diagonal strokes, cinnabar race signal, compressed black-ink speed marks. Use generous negative space where possible, clear visual hierarchy, refined Chinese typography, tiny English annotation \"RIVER RACE\", restrained seal, premium printmaking texture, contemporary editorial composition. Palette: river blue-gray, cinnabar, black ink, foam white. Avoid cartoon dragon boats, festival kitsch, chaotic unreadable typography, excessive red.",
    },
    {
        "id": "06",
        "theme": "苏州园林",
        "title": "借景",
        "preset": "F04 行楷 · 文人",
        "layout": "L04 窗格 / 园林框景型",
        "palette": "mist white, ink gray, moss green, Taihu stone gray",
        "prompt": "Create a refined 3:4 contemporary Chinese / Oriental poster. Theme: Suzhou garden borrowed view / 苏州园林. Main title: \"借景\". Calligraphy preset: F04 literati semi-cursive, relaxed, refined, readable. Layout preset: L04 window and garden framed-view composition using lattice and moon-gate geometry. Translate the subject into abstract graphic elements: moon gate opening, lattice window divisions, water-surface horizontal calm, Taihu stone porous silhouette, moss-green quiet accent. Use generous negative space, clear visual hierarchy, refined Chinese typography, small English annotation \"BORROWED VIEW\", restrained seal, premium clean xuan paper texture, contemporary editorial composition. Palette: mist white, ink gray, moss green, Taihu stone gray. Avoid generic bamboo, tourist garden illustration, over-aged paper, repeated right-title layout.",
    },
    {
        "id": "07",
        "theme": "昆曲水袖",
        "title": "水袖",
        "preset": "F03 楷书 · 端正",
        "layout": "L09 左右对景型",
        "palette": "moon white, rouge pink, ink black, pale jade",
        "prompt": "Create a refined 3:4 contemporary Chinese / Oriental poster. Theme: Kunqu opera water sleeves / 昆曲水袖. Main title: \"水袖\". Calligraphy preset: F03 formal regular script, clear skeleton, restrained and elegant. Layout preset: L09 left-right facing composition, one side typography and one side abstract sleeve movement, with breathing space between. Translate the subject into abstract graphic elements: long sleeve ribbon curves, stage shadow, subtle rouge accent, pale jade breath line, delicate vertical information. Use generous negative space, clear visual hierarchy, refined Chinese typography, small English annotation \"KUNQU OPERA\", restrained seal, premium silk-paper texture, contemporary editorial composition. Palette: moon white, rouge pink, ink black, pale jade. Avoid theatrical clutter, literal actor portrait, heavy red stage curtain, decorative overload.",
    },
    {
        "id": "08",
        "theme": "围炉煮茶",
        "title": "围炉",
        "preset": "F02 汉隶 · 古拙",
        "layout": "L03 中心圆相型",
        "palette": "tea brown, ash gray, rice white, ember orange",
        "prompt": "Create a refined 3:4 contemporary Chinese / Oriental poster. Theme: winter tea around a small stove / 围炉煮茶. Main title: \"围炉\". Calligraphy preset: F02 Han clerical script, wide horizontal ancient stability, quiet tablet feeling. Layout preset: L03 central circular form, stove and teacup circle as anchor. Translate the subject into abstract graphic elements: circular tea stove, ash-gray ring, rising steam line, tiny ember-orange heat point, tea-brown ceramic surface. Use generous negative space, clear visual hierarchy, refined Chinese typography, small English annotation \"WARM TEA\", restrained seal, premium fibrous paper texture, contemporary editorial composition. Palette: tea brown, ash gray, rice white, ember orange. Avoid cozy cartoon scene, excessive beige, generic bamboo, overdecorated tea props.",
    },
    {
        "id": "09",
        "theme": "香道",
        "title": "一缕",
        "preset": "F09 瘦劲 · 清雅",
        "layout": "L02 横向题字型",
        "palette": "incense ash, rice white, gray-brown, muted smoke blue",
        "prompt": "Create a refined 3:4 contemporary Chinese / Oriental poster. Theme: incense ceremony / 香道. Main title: \"一缕\". Calligraphy preset: F09 thin elegant elongated strokes, sparse and modern Oriental. Layout preset: L02 horizontal title across the upper field, visual smoke form below. Translate the subject into abstract graphic elements: one vertical thread of smoke, ash trace, small burner shadow, pale circular breath, gray-brown quiet base. Use generous negative space, clear visual hierarchy, refined Chinese typography, small English annotation \"INCENSE TRACE\", restrained seal, premium clean rice-paper texture, contemporary editorial composition. Palette: incense ash, rice white, gray-brown, muted smoke blue. Avoid religious symbols, cluttered altar objects, dirty vintage paper, red-gold decoration.",
    },
    {
        "id": "10",
        "theme": "竹编工艺",
        "title": "经纬",
        "preset": "F10 当代手写 · 实验",
        "layout": "L05 现代分栏型",
        "palette": "bamboo yellow, moss green, gray-brown, quiet white",
        "prompt": "Create a refined 3:4 contemporary Chinese / Oriental poster. Theme: bamboo weaving craft / 竹编工艺. Main title: \"经纬\". Calligraphy preset: F10 contemporary handwritten experimental, stretched strokes and slight misalignment. Layout preset: L05 modern column layout with three narrow vertical panels and one calm information zone. Translate the subject into abstract graphic elements: woven warp-weft grids, bamboo-strip shadows, circular rim fragment, moss-green tiny accent, gray-brown material lines. Use generous negative space, clear visual hierarchy, refined Chinese typography, small English annotation \"BAMBOO WEAVE\", restrained seal, premium hand-print paper texture, contemporary editorial composition. Palette: bamboo yellow, moss green, gray-brown, quiet white. Avoid rustic craft fair look, excessive basket illustration, fixed template, over-aged background.",
    },
    {
        "id": "11",
        "theme": "篆刻印谱",
        "title": "刀痕",
        "preset": "F08 篆意 · 古朴",
        "layout": "L06 拼贴档案型",
        "palette": "seal red, stone gray, bone white, black ink",
        "prompt": "Create a refined 3:4 contemporary Chinese / Oriental poster. Theme: seal carving archive / 篆刻印谱. Main title: \"刀痕\". Calligraphy preset: F08 seal-inspired ancient pictographic title, round and graphic. Layout preset: L06 collage archive, specimen blocks, small numbering, texture samples, restrained seal impressions. Translate the subject into abstract graphic elements: carved stone edge, square seal negative space, knife-cut grooves, small red seal sample, archival labels. Use generous negative space, clear visual hierarchy, refined Chinese typography, small English annotation \"SEAL ARCHIVE\", premium old-book but clean paper texture, contemporary editorial composition. Palette: seal red, stone gray, bone white, black ink. Avoid red seal overload, antique shop clutter, illegible dense text, direct copying of seal charts.",
    },
    {
        "id": "12",
        "theme": "黄山云海",
        "title": "云骨",
        "preset": "F05 行书 · 洒脱",
        "layout": "L08 下沉景观型",
        "palette": "mist gray, pine green, rock black, pale sky",
        "prompt": "Create a refined 3:4 contemporary Chinese / Oriental poster. Theme: Huangshan sea of clouds / 黄山云海. Main title: \"云骨\". Calligraphy preset: F05 flowing running script, breathable and controlled, not chaotic. Layout preset: L08 sinking landscape, very large upper negative space with abstract landscape concentrated below. Translate the subject into abstract graphic elements: cloud bands as soft horizontal fields, pine-green vertical needles, black-rock angular forms, title floating in clean air. Use generous negative space, clear visual hierarchy, refined Chinese typography, small English annotation \"CLOUD BONE\", restrained seal, premium mineral paper texture, contemporary editorial composition. Palette: mist gray, pine green, rock black, pale sky. Avoid generic ink mountain painting, travel brochure style, overdone mist, repeated right-title layout.",
    },
    {
        "id": "13",
        "theme": "城市胡同夜色",
        "title": "巷光",
        "preset": "F05 行书 · 洒脱",
        "layout": "L10 非对称实验型",
        "palette": "night blue, warm lantern amber, brick gray, off-white",
        "prompt": "Create a refined 3:4 contemporary Chinese / Oriental poster. Theme: old Beijing hutong at night / 城市胡同夜色. Main title: \"巷光\". Calligraphy preset: F05 flowing running script, city-humanities rhythm, energetic but controlled. Layout preset: L10 asymmetric experimental composition with cropped title and slight offset. Translate the subject into abstract graphic elements: narrow alley perspective as compressed vertical trapezoids, warm lantern amber dots, brick-gray texture blocks, night-blue field, tiny street-number annotation. Use generous negative space, clear visual hierarchy, refined Chinese typography, small English annotation \"ALLEY LIGHT\", restrained seal, premium matte paper texture, contemporary editorial composition. Palette: night blue, warm lantern amber, brick gray, off-white. Avoid nostalgic tourist postcard, literal street photo collage, excessive red lanterns, messy typography.",
    },
    {
        "id": "14",
        "theme": "山海经异兽",
        "title": "异形",
        "preset": "F08 篆意 · 古朴",
        "layout": "L10 非对称实验型",
        "palette": "mineral black, malachite green, bone white, cinnabar dot",
        "prompt": "Create a refined 3:4 contemporary Chinese / Oriental poster. Theme: Shan Hai Jing mythical creature as abstract cultural graphic / 山海经异兽. Main title: \"异形\". Calligraphy preset: F08 seal-inspired ancient pictographic feeling, mysterious and graphic. Layout preset: L10 asymmetric experimental composition with cropped type and abstract creature silhouette entering the text area. Translate the subject into abstract graphic elements: nonliteral hybrid silhouette fragments, archaic curved lines, mineral-black field, malachite-green contour, one cinnabar dot as eye-like accent. Use generous negative space, clear visual hierarchy, refined Chinese typography, small English annotation \"CLASSIC OF MOUNTAINS AND SEAS\", restrained seal, premium mineral paper texture, contemporary editorial composition. Palette: mineral black, malachite green, bone white, cinnabar dot. Avoid fantasy game illustration, monster literalism, religious symbols, excessive ornament.",
    },
    {
        "id": "15",
        "theme": "当代新非遗设计节",
        "title": "新作",
        "preset": "F10 当代手写 · 实验",
        "layout": "L05 现代分栏型",
        "palette": "warm white, graphite black, electric teal, muted cinnabar",
        "prompt": "Create a refined 3:4 contemporary Chinese / Oriental poster. Theme: contemporary new intangible heritage design festival / 当代新非遗设计节. Main title: \"新作\". Calligraphy preset: F10 contemporary handwritten experimental, free structure, stretched strokes, designer title feeling. Layout preset: L05 modern editorial columns with bold grid, one dark information band, and abstract craft samples. Translate the subject into abstract graphic elements: material swatches, modular craft marks, cut-paper edge, woven line sample, electric teal contemporary accent, muted cinnabar micro seal. Use generous negative space, clear visual hierarchy, refined Chinese typography, small English annotation \"NEW HERITAGE DESIGN\", premium clean paper texture, contemporary editorial composition. Palette: warm white, graphite black, electric teal, muted cinnabar. Avoid old-fashioned heritage poster, decorative overload, excessive gold or red, template-like layout.",
    },
]


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    results = []
    for item in TESTS:
        out = OUT_DIR / f"chinese-style-poster-test-{item['id']}.png"
        meta = OUT_DIR / f"chinese-style-poster-test-{item['id']}.json"
        cmd = [
            sys.executable,
            str(SKILL_SCRIPT),
            "-m",
            "gpt-image-2",
            item["prompt"],
            "-o",
            str(out),
            "--json-out",
            str(meta),
            "--meta",
            "--timeout",
            "240",
        ]
        print(f"START {item['id']} {item['theme']} -> {out}", flush=True)
        proc = subprocess.run(cmd, text=True, capture_output=True)
        record = {
            "id": item["id"],
            "theme": item["theme"],
            "title": item["title"],
            "preset": item["preset"],
            "layout": item["layout"],
            "palette": item["palette"],
            "output": str(out),
            "api_json": str(meta),
            "returncode": proc.returncode,
            "stdout": proc.stdout[-4000:],
            "stderr": proc.stderr[-4000:],
            "prompt": item["prompt"],
        }
        results.append(record)
        MANIFEST.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
        if proc.returncode != 0:
            print(f"FAIL {item['id']}: {proc.stderr}", flush=True)
            return proc.returncode
        print(f"DONE {item['id']}", flush=True)
    print(f"MANIFEST {MANIFEST}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
