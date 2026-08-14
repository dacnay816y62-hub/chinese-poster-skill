---
name: chinese-style-poster-skill
description: Create refined contemporary Chinese-style / Oriental aesthetic posters and poster-generation prompts from themes, titles, event information, brand copy, products, photos, architecture, intangible cultural heritage, cities, exhibitions, seasonal festivals, tea, incense, craft, museum, commercial brands, fashion, urban culture, editorial campaigns, or experimental cultural subjects. Use when the user asks for 中式海报, 东方美学海报, 国风海报, Chinese style poster, Oriental poster design, cultural poster direction, poster prompt generation, broader direction exploration, or multiple style/layout tests for this visual system.
---

# Chinese Style Poster Skill

Use this skill to translate a user-provided subject, copy, image, cultural object, place, event, or brand idea into a refined 3:4 contemporary Chinese / Oriental poster direction or image-generation prompt.

## Host And Image Backend

This skill is host-agnostic. It can be used in Codex, ChatGPT, API workflows, or another host that supports image generation.

- In Codex, use the built-in Imagen v2 image capability directly. No separate API key or external image service is required.
- In ChatGPT or another image-capable host, use that host's native image workflow.
- The Python batch scripts in this repository are optional utilities for JSONL jobs, contact sheets, and custom external backends. Their backend credentials are not a requirement of this skill.

Default output:

- Use a 3:4 vertical poster unless the user specifies another ratio.
- Produce one poster by default.
- Use Chinese as the primary text language and English only as secondary visual annotation.
- Aim for high-end cultural poster / exhibition poster quality.
- Avoid template-like "beige paper + brush calligraphy + red seal" shortcuts.
- When creating generated files, place images, exports, drafts, and temporary assets under the corresponding subdirectories of `CODEX_OUTPUT_ROOT`. If it is not set, use a local `outputs/` directory.

## Core Principle

Do not equate "Oriental" with stacked traditional motifs. Avoid mechanical use of ink mountains, red seals, brush text, auspicious clouds, bamboo, old architecture, and rice paper.

Instead, extract structure, material, cultural imagery, rhythm, and spatial logic from the subject, then translate them into contemporary graphic design.

Examples:

- 景德镇: porcelain silhouette, kiln fire, cobalt pattern, glaze flow, circular vessel mouth.
- 苗族服饰: silver arcs, pleated skirt rhythm, batik, embroidery geometry.
- 故宫: central axis, red walls, eaves, platform base, ceremonial order.
- 古琴: strings, wood grain, resonance curves, mountain-water atmosphere.
- 竹编: warp and weft, bamboo strips, grid shadows, circular weaving.
- 香道: smoke, incense burner, ash trace, circle form.
- 苏州园林: moon gate, lattice window, borrowed view, water surface, Taihu stone.

## Direction Expansion Matrix

When the user asks to broaden, randomize, test, or extend directions, vary both the **subject domain** and the **visual archetype**. Do not let all outputs collapse into quiet museum paper posters.

### Subject Domains

Sample across these domains:

- **Archaeology / museum**: bronzes, jade, pottery shards, oracle bones, Han tiles, Buddhist grotto fragments, archive labels.
- **Architecture / spatial order**: city gates, alleys, courtyards, pavilions, watchtowers, tea rooms, hotels, theaters, contemporary cultural spaces.
- **Craft / material process**: lacquer, bamboo, porcelain, paper, textile, indigo dye, woodblock, metalwork, stone carving, restoration, kiln firing.
- **Performance / movement**: Kunqu, shadow puppetry, dragon boat, martial arts, lion dance, folk ritual, festival procession, contemporary dance.
- **Lifestyle / sensory culture**: tea, incense, food, medicine, gardens, seasonal terms, flowers, rain, snow, night markets, travel memory.
- **Literature / philosophy**: poetry, old books, letter paper, bookbinding, mountain-water thought, time, silence, ritual, wandering.
- **City / route / commerce**: canals, harbors, railway towns, old shops, urban renewal, brand campaigns, cultural retail, pop-ups.
- **Contemporary / youth / experimental**: design festivals, fashion, music, street culture, new heritage, digital Oriental, abstract identity systems.

### Visual Archetypes

Choose one primary archetype before selecting font and layout:

- **D01 Museum Archive**: specimen blocks, labels, catalog numbers, rubbed textures, quiet curatorial order.
- **D02 Architectural System**: axes, section lines, elevation rhythm, windows, gates, structural grids.
- **D03 Material Macro**: close crop of glaze, fiber, lacquer, stone, metal, textile, ash, paper, or water.
- **D04 Typography Campaign**: title as campaign image, bold crop, strong type-to-graphic tension.
- **D05 Commercial Cultural Ad**: product or brand-like hero composition, polished campaign finish, restrained copy.
- **D06 Festival Kinetic**: movement, speed, sound, flags, water, drums, diagonal force, but still refined.
- **D07 Dark Contemporary Oriental**: black, mineral, night, shadow, lacquer, neon accent, high contrast.
- **D08 Philosophical Minimal**: very few elements, strong silence, tiny text, object-as-thought.
- **D09 Color-Field Editorial**: large modern color planes from subject materials, minimal illustration.
- **D10 Route / Map / Data**: paths, coordinates, waterlines, trade routes, grids, diagram-like cultural geography.
- **D11 Workshop Process**: tools, marks, unfinished edges, steps, fragments, material transformation.
- **D12 Textile / Pattern System**: repeat, weave, embroidery, pleat, batik, modular ornaments with discipline.
- **D13 Urban Night / Street Culture**: alley light, signage rhythm, brick, concrete, rain, contemporary city mood.
- **D14 Stage / Performance Motion**: sleeves, shadow, strings, sound waves, body trajectory, theater light.
- **D15 Botanical / Naturalist**: herbarium, seasonal plants, dew, seeds, branches, scientific quietness.
- **D16 Book / Object Cover**: book-cover-like typography, object silhouette, restrained publishing language.
- **D17 Digital Neo-Oriental**: scan lines, interface grids, generative marks, neon mineral colors, cultural abstraction.
- **D18 Public Event System**: poster as signage, ticket, schedule, exhibition identity, modular information.

For a 15-image exploration, use at least 10 subject domains or subdomains, at least 8 visual archetypes, at least 8 title presets/layout combinations, at least 6 palettes, and at least 3 outputs that are not pale paper-led.

## Visual Direction Compile

Before writing a final image prompt or producing an image, form a short internal visual brief. Do not paste this entire skill into the generation prompt.

Determine:

1. Theme and user-provided copy.
2. Core visual anchor.
3. Subject domain and visual archetype.
4. Calligraphy / title style preset.
5. Layout structure.
6. Abstract graphic translation.
7. Main color, secondary color, and accent color.
8. Text hierarchy.
9. The main visual contrast of this poster.

Only include the details needed for the current poster in the final prompt.

## Calligraphy And Title Presets

Choose the title style according to subject temperament, era, material quality, event type, and user preference. Do not use the same preset repeatedly in multi-poster tests.

### F01: 魏碑 · 雄浑

Square, heavy, carved, structural, stone-inscription feeling; suitable for 长城, 故宫, history, architecture, ruins, intangible heritage, museums.

### F02: 汉隶 · 古拙

Wide horizontal structure, ancient and stable tablet feeling; suitable for tea, vessels, Chinese medicine, seasonal festivals, cultural brands, folk subjects.

### F03: 楷书 · 端正

Clear skeleton, restrained, formal, readable; suitable for formal exhibitions, museums, opera, cultural events, high-end brands.

### F04: 行楷 · 文人

Readable regular-script structure with flowing literati rhythm; suitable for Suzhou gardens, tea, Jiangnan, lifestyle, hotels, incense culture, humanities photography.

### F05: 行书 · 洒脱

Flowing, breathable, energetic but controlled; suitable for Huangshan, travel, mountain-water, cities, humanities, nature, Oriental art.

### F06: 草书 · 狂放

Flying white, ink motion, strong dynamic strokes where the character becomes the main visual; suitable for dragon boat, music festivals, martial arts, avant-garde art, young culture.

### F07: 枯笔 · 苍劲

Dry brush, broken ink, fiber edge, weathered stone and time; suitable for guqin, mountains, ruins, handcraft, stone carving, old architecture, historical subjects.

### F08: 篆意 · 古朴

Rounded, pictographic, ancient-script feeling, mysterious and graphic; suitable for seals, relics, ancient civilization, museum, old books, Shan Hai Jing.

### F09: 瘦劲 · 清雅

Thin, elongated, quiet, elegant, sparse, modern Oriental; suitable for incense, high-end hotels, tea spaces, fragrance, lifestyle, aesthetic brands.

### F10: 当代手写 · 实验

Free hand-written structure, stretched strokes, local distortion, asymmetry, designer lettering; suitable for bamboo weaving, contemporary heritage, youth brands, design events, experimental cultural posters.

## Font Selection Hints

- 故宫: 魏碑 / 楷书 / 隶书.
- 景德镇: 行楷 / 枯笔 / 瘦劲.
- 苗族服饰: 行书 / 枯笔 / 当代手写.
- 长城: 魏碑 / 枯笔.
- 茶: 隶书 / 行楷 / 瘦劲.
- 古琴: 枯笔 / 行楷.
- 昆曲: 楷书 / 瘦劲 / 行楷.
- 黄山: 行书 / 草书.
- 龙舟: 草书 / 行书.
- 篆刻: 篆意 / 魏碑.
- 香道: 瘦劲 / 行楷.
- 竹编: 当代手写 / 行楷.
- 山海经: 篆意 / 枯笔 / 草书.
- 高端酒店: 瘦劲 / 行楷.

## Layout Presets

Avoid long-term repetition of "large calligraphy on the right + small text on the left + illustration at the bottom." Select a structure that belongs to the current subject.

### L01: 纵向题字型

Vertical large title, main visual to one side, information on the other, strong negative space. Suitable for landscape, architecture, museums, intangible heritage.

### L02: 横向题字型

Horizontal title across top or upper-middle, main visual below, information on both sides. Suitable for tea, brands, lifestyle, exhibitions.

### L03: 中心圆相型

Large central circle such as vessel mouth, moon gate, smoke ring, tea stove, or Zen circle. Suitable for tea, incense, pottery, blessing themes.

### L04: 窗格 / 园林框景型

Window, gate, lattice, or screen creates a framed architectural structure. Suitable for Suzhou gardens, Jiangnan, architecture, Oriental spaces.

### L05: 现代分栏型

Two to four vertical or horizontal columns, modern editorial structure, optional dark information block. Suitable for seal carving, intangible heritage, contemporary exhibitions, design festivals.

### L06: 拼贴档案型

Image, texture, stamp, and text blocks arranged like an archive or specimen book. Suitable for relics, seal carving, museums, handcraft, cultural research.

### L07: 满版书法型

Calligraphy occupies 35% to 65% of the poster and becomes the graphic itself. Suitable for dragon boat, martial arts, music festivals, mountains, strong motion themes.

### L08: 下沉景观型

Large upper negative space, suspended title, visual elements concentrated in the lower half. Suitable for Dunhuang, mountains, ruins, cities, architecture.

### L09: 左右对景型

Text on one side and visual on the other, with central breathing space and album-page feeling. Suitable for vessels, tea, handwork, humanities.

### L10: 非对称实验型

Off-center title, cropped type, graphic elements entering text area, light misalignment, bold proportion contrast. Suitable for young brands, contemporary Oriental fashion, design events, new heritage.

### L11: 超大标题 + 微型信息型

Title occupies more than 40% of the visual field, tiny information, strong negative space, book-cover feeling. Suitable for art exhibitions, architecture, philosophy, minimal brands.

### L12: 图形主导型

Abstract graphic dominates while calligraphy moves to a secondary level. Suitable for Miao clothing, bamboo weaving, Jingdezhen, textile, heritage patterns, product culture.

## Copy And Text Hierarchy

When the user provides title, subtitle, time, location, brand name, event details, or tagline, preserve the original wording unless asked to rewrite.

When the user only provides a subject, generate 3 to 5 short supporting lines about material, history, space, craft, mood, philosophy, action, or regional culture.

Use four text levels:

- T1 main title: 15% to 45% of the visual field; calligraphy, handwriting, seal-inspired, Wei tablet, running script, or cursive.
- T2 subtitle: 3% to 8%; Song / Ming-style serif, thin serif, modern sans, or small vertical setting.
- T3 explanatory copy: 1% to 4%; time, place, material, history, craft, or mood.
- T4 English annotation: secondary only, such as `ORIENTAL POSTER`, `CULTURAL POSTER`, `EXHIBITION`, `MATERIAL / CRAFT NAME`.

## Abstract Translation

Prefer abstract translation over direct scenic illustration.

Path:

`Theme -> cultural keywords -> physical structure -> visual shape -> graphic composition`

Examples:

- 故宫: red wall as large rectangular color field, central axis as vertical order, eaves as horizontal linear silhouette, courtyard as negative space.
- 景德镇: porcelain as translucent contour, blue-and-white as local cobalt pattern, kiln fire as warm red or earth tone, vessel mouth as circle, glaze flow as vertical texture.
- 苗族服饰: silver jewelry as silver arcs and rings, pleated skirt as radial lines, embroidery as geometry, batik as indigo field.
- 敦煌: flying apsaras as linear ribbons, murals as fragmented color blocks, grottoes as geometric openings, desert as ocher texture.

## Color System

Do not default to only beige, black, and red. Extract one theme color from the subject.

Recommended balance:

- 70% to 85% neutral color.
- 10% to 20% subject color.
- 1% to 5% accent color.

Subject palettes:

- 故宫: palace-wall red, dark gray, muted gold.
- 景德镇: cobalt blue, porcelain white, earth yellow.
- 苗族: indigo, silver gray, dark brown.
- 敦煌: stone green, ocher, sand yellow, cinnabar.
- 香道: gray-brown, rice white, incense ash.
- 竹编: bamboo yellow, moss green, gray-brown.
- 龙舟: river blue-gray, cinnabar, black ink.

Expansion palettes:

- Dark contemporary: lacquer black, mineral green, bone white, one neon teal or cinnabar accent.
- Commercial cultural: warm white, graphite, product-derived accent, one confident color field.
- Urban night: deep blue, brick gray, lantern amber, rain reflection.
- Material macro: subject material color at high scale, with one quiet neutral and one process accent.
- Festival kinetic: controlled high contrast with one active color; avoid folk-color pile-up.
- Botanical naturalist: herb green, seed brown, paper white, soft scientific gray.

## Seals, Paper, And Materials

Use seals only as accents:

- Use 1 to 3 small seals.
- Do not stamp every corner.
- Allow round, square, rectangular, or abstract seals.
- Do not require readable real seal text.
- Keep seals secondary.

Paper and material direction:

- Use clean xuan paper, hemp paper, rice paper, old-book paper, slight fibers, micro grain, subtle fading, printmaking texture, or hand-print feeling.
- Avoid excessive aging, large dirty stains, heavy cracks, fake antique texture, muddy dark areas, and newspaper-yellow paper.
- Aim for clean, restrained, tactile material quality.

## Handling User Images

When the user provides an image, do not simply place it into the poster. Decide its role first:

- Main visual.
- Local crop.
- Background texture.
- Silhouette.
- Black-and-white image.
- Monochrome treatment.
- Halftone.
- Translucent overlay.
- Local abstraction.
- Contour extraction.
- Color-block extraction.
- Pattern extraction.

It is acceptable to use only part of the source image.

## Generation Workflow

1. Read the input: identify theme, user text, image content, cultural context, and use case.
2. Determine the visual direction: subject domain, visual archetype, title preset, layout preset, visual anchor, abstract translation, color, and text hierarchy.
3. Build copy structure: if copy is incomplete, supplement 3 to 5 concise support lines.
4. Compose layout: determine title position, visual weight, negative space, information distribution, and graphic entry method.
5. Generate the main visual or prompt: require complete composition, clear graphic relationships, no element pile-up, no tourist-poster look, no fake antique style.
6. Check title style difference: ensure the title style matches the theme and is not too similar to the last generated poster.
7. Check layout difference: avoid repeated right-title / left-copy layout; consider horizontal title, circular form, framed view, collage, columns, or asymmetry.

## Multi-Poster Test Rules

When the user asks for random tests, multiple tests, applicability tests, different themes, font tests, or layout tests:

- Randomize theme, font preset, layout preset, subject color, and abstract translation method while preserving logic.
- For 10 tests, cover at least architecture, landscape, intangible heritage, vessels, opera, tea, folk culture, city, handcraft, and contemporary culture.
- For 10 tests, use at least 7 title presets, 5 layout presets, and 5 subject colors.
- For 15 tests, include at least 8 visual archetypes from the Direction Expansion Matrix.
- For 15 tests, include at least 3 contemporary / commercial / urban directions and at least 3 material / macro / process directions.
- Include dark, saturated, structural, and kinetic posters where the subject supports them; do not force every output into pale paper, museum archive, or literati quietness.
- Do not make every poster beige.
- Do not make every title vertical.

## Strong Avoidance List

Avoid:

- Every poster looking the same.
- The same brush lettering every time.
- Always placing the large title on the right.
- Always placing four small copy blocks on the left.
- Always placing an ink landscape at the bottom.
- Drawing mountains for every cultural subject.
- Scattering red seals everywhere.
- Fake antique style.
- Tourist souvenir poster aesthetics.
- Chaotic AI-looking calligraphy.
- Excessive text density.
- Traditional motifs unrelated to the subject.
- Direct copying of reference posters.
- Fixed templates.
- Dirty backgrounds.
- Excessive nostalgia.
- Excessive religious symbols.
- Excessive Chinese red.
- Excessive gold.
- Excessive decoration.

## Quality Checklist

A qualified poster should satisfy:

- Content: the theme is immediately recognizable, information is clear, copy is not empty.
- Title style: the main title has personality, matches the subject, and differs from other test images.
- Graphic language: visual elements come from the subject and have abstract translation.
- Layout: structure is clear, negative space is meaningful, and the result does not feel templated.
- Color: restrained, subject-specific, and not monotonous.
- Temperament: Oriental, contemporary, refined, quiet, cultural, and not vulgar.

## Prompt Template

Compress the final image prompt to the current direction:

```text
Create a refined 3:4 contemporary Chinese / Oriental poster.
Theme: [theme].
Direction archetype: [D-code and archetype].
Main title: "[title]".
Calligraphy preset: [selected title style and its traits].
Layout preset: [selected layout].
Translate the subject into abstract graphic elements: [elements].
Use generous negative space, clear visual hierarchy, refined Chinese typography, small English annotations, restrained seal marks, premium paper texture, and a contemporary editorial composition.
Palette: [colors].
Avoid generic Chinese decoration, template-like layouts, tourist-poster aesthetics, excessive red, excessive ink mountains, and repeated composition patterns.
```

Core declaration:

> Do not apply a Chinese-style template.
> Do not treat "calligraphy + xuan paper + red seal" as Oriental design.
> Let the theme choose the title style.
> Let the content choose the layout.
> Let cultural elements re-enter contemporary graphic design through abstraction.
