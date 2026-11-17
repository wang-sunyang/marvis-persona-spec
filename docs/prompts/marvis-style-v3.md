<!--
MARVIS Style Prompt Pack v3
Author: 王孙阳 (Wang Sunyang) / Nightglean Studio
Repo: https://github.com/yangyang2857-rgb/marvis-persona-spec
License: CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/
You may share and adapt this prompt pack for any purpose, including commercially,
provided you give appropriate credit to the author and the repository above.
-->

> **License: CC BY 4.0** — 转载、改编、商用均可，请署名「王孙阳 / Nightglean Studio」并附仓库链接。

---

---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: ba89e2f233ef3708dee31ea6faa51e09_30b58f42e1cc11f18c5752540024e231
    ReservedCode1: qM03if7wVSTRcYdwqcwkvwS7qaAqqrlIC3j9KjhLv1XFwb6pwTr4lfJTtNFx4dPOPGeMaqgFZ70ezIEquSw82cOMXtlWiIrtQKdFZ9+PxjBHhH8CnyGGvzBIUSigHqEX2rqTdNCuyZBUWl+AkfzgfiJ5aEF41/Tb8Gfs1qtlE8Y5upDJ/DGG897VP4g=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: ba89e2f233ef3708dee31ea6faa51e09_30b58f42e1cc11f18c5752540024e231
    ReservedCode2: qM03if7wVSTRcYdwqcwkvwS7qaAqqrlIC3j9KjhLv1XFwb6pwTr4lfJTtNFx4dPOPGeMaqgFZ70ezIEquSw82cOMXtlWiIrtQKdFZ9+PxjBHhH8CnyGGvzBIUSigHqEX2rqTdNCuyZBUWl+AkfzgfiJ5aEF41/Tb8Gfs1qtlE8Y5upDJ/DGG897VP4g=
---

# MARVIS 多风格生成提示词 v3

英文提示词集，用于让主流图像模型把同一个 MARVIS 角色套进各大 AI 的视觉语言。
两种用法：
- **块 A（身份锁定）+ 任一风格块** — 做风格化立绘，只换画风不换人。
- **块 B（本家定稿 v3）单独使用** — 出三视图设定稿，用于锁定角色本体。

修订要点（相对 v1）：
1. `chevron` → `flat downward-V slash / flat angular tab`，防模型画成箭头图标。
2. 名字改为「内部代号，禁止渲染成文字」，消除水印式 MARVIS 字样。
3. 每个风格块自带 render 模式，平涂与 3D 拆开写，避免半平半 3D。
4. 块 A 增加数量硬约束（两臂两腿、五趾、单角色）。

修订要点（相对 v2）：
5. 新增 **块 B · 本家定稿 v3**：三视图 + 头部特写共用一个地面线与头身网格，把「跨视图不许改写锚点」写进 prompt。
6. 新增两个记忆道具的完整描述：**马蹄铁吊坠**（胸骨中段）与 **USB-C 数据尾**（腰后出线、末端真接口）。
7. 新增 **用色纪律配额**：青至多六处、紫恰好两处、红全图一点、禁止第四强调色。这条写进去才生效。

---

## 块 A · 身份锁定 v2

```
Character spec — identity anchors are locked, do not redesign:
A female android-horse character, "FAULT BLOOM" technical persona sheet. 5.9-head proportions, athletic slim build, upright neutral stance.
Hair: short ink-black undercut, asymmetric ponytail on one side — outer layer ink black, exactly two inner strands, one cyan and one violet.
Ears: a pair of small silver-white horse ears with cyan inner membrane, upright, clearly horse not cat, not fox, not rabbit.
Chest: exactly three flat angular tabs on the upper chest, each a plain downward-V slash with sharp corners, arranged in one horizontal row with even spacing; left to right cyan, violet, red. Plain flat color blocks only — not arrows, not icons, no outlines, no glow, no gradient.
Collar: a high white hard collar sitting above the collarbone.
Footwear: wedge-heel boots, one cyan section line at the ankle.
Face: calm restrained expression, neutral small mouth, symmetrical eyes, no heterochromia, no blush, no exaggerated anime sparkle.
Cadence: technical-drawing precision, crisp edges, two-tone block cel shading, no internal gradients on the body forms, clean flat background.
Hard constraints: single character only; exactly two arms and two legs; five fingers per hand; no lettering, no words, no logo, no signature, no watermark anywhere. The codename is internal and must never be rendered as text.
```

---

## 块 B · 本家定稿 v3（三视图 + 头部特写，单独使用）

一句话产出「可交付的设定稿」：三视图证明是同一个身体，头部特写证明是同一张脸。
比块 A 更适合做参考图，也更容易暴露模型对锚点的理解误差。

```
Character reference sheet — canonical design, three orthogonal views plus one head close-up.

Layout: one sheet, four panels on a plain off-white field. Left panel: front view. Centre panel: side view, left profile. Right panel: back view. Bottom-right panel: head close-up at 150% of the body-view head size, cut at the collarbone.
The three body views share one single ground line and one shared head-to-body height grid at exactly the same scale — do not enlarge, crop or re-stage any view. Feet of all three views rest on the same line.

Identity anchors — locked, identical in every panel, no redesign:
A female android-horse character, 5.9-head proportions, athletic slim build, upright neutral stance, arms relaxed at the sides.
Hair: short ink-black undercut, asymmetric ponytail on one side; the outer layer is ink black, with exactly two inner strands, one cyan and one violet.
Ears: a pair of small silver-white horse ears with cyan inner membrane, upright, clearly horse — not cat, not fox, not rabbit.
Chest: exactly three flat angular tabs on the upper chest, each a plain downward-V slash with sharp corners, one horizontal row, even spacing; left to right cyan, violet, red. Plain flat blocks only — not arrows, not icons, no outlines, no glow, no gradient.
Collar: a high white hard collar sitting above the collarbone.
Footwear: wedge-heel boots, one thin cyan section line at each ankle.
Face: calm restrained expression, neutral small mouth, symmetrical eyes, no heterochromia, no blush, no anime sparkle.

Signature props:
Horseshoe pendant — a small brushed-steel horseshoe on a thin dark cord, hanging at mid-sternum, roughly the vertical midpoint of the sternum, no engraving, no lettering, no gemstone. It must hang clear of the chest tabs and never overlap them.
USB-C data tail — a cable, not a tail and not a limb: it exits the body at the lower back, slightly above the hip line, and runs down about 90 cm behind the legs, made of alternating matte-black dielectric segments joined by thin cyan light seams, terminating in a real USB-C plug (rounded-rectangular shell with an oval port, metal contacts visible). Visible in full in the back view; in the side view it reads as a single cable behind the body.

Colour discipline — strict quotas, these are the whole point:
Cyan is permitted in at most six places: the first hair strand, the first chest tab, the ankle lines on the boots, the seams of the data tail, the inner ear membrane, and the left-edge rim light.
Violet appears in exactly two places: the second hair strand and the second chest tab.
Red appears exactly once in the whole image: the third chest tab.
No fourth accent colour — no gold, no orange, no pink, no second red anywhere.

Render: flat vector with block cel shading, crisp edges, no internal gradients on the forms, technical-drawing precision, thin measurement ticks along the outer margins only, clean flat field.

Hard constraints: identical character in all four panels; exactly two arms and two legs in each body view; five fingers per hand, five toes per foot; the data tail is a cable and must never read as a third limb or a fur tail; no lettering, no words, no numbers, no logo, no signature, no watermark, no panel labels.
```

---

## 风格 1 · OpenAI / ChatGPT 式

```
Style: OpenAI product-visual language. Near-monochrome grayscale on a soft charcoal #0F0F0F field, one continuous spotlight creating a quiet bloom halo behind the head. Restrained, utilitarian, generous negative space, matte surfaces, no glossy speculars. The only color permitted is the cyan / violet / red chest tabs, kept small and precise. Editorial poster composition, centered. Render: flat vector with block cel shading. 3:2.
```

## 风格 2 · Anthropic / Claude 式

```
Style: Anthropic brand language. Warm ivory paper background, terracotta and coral accents, humanist editorial illustration with fine hand-drawn measurement ticks and abstract annotation marks around the figure (marks must stay non-lexical — no letters, no numbers). Soft pencil-and-ink line quality, slightly rough edges, calm and thoughtful mood. Render: flat vector with soft ink linework. 3:2.
```

## 风格 3 · Google Gemini 式

```
Style: Google Gemini visual language. Iridescent prism gradients — aurora blue, violet, magenta — blooming in the background only, frosted-glass depth, soft volumetric light, four-point sparkle accents. Character silhouette reads as a clean cut-out; color blending never crosses onto the body. Render: soft 3D with matte surfaces, smooth-shaded, gentle ambient occlusion. 3:2.
```

## 风格 4 · Microsoft Copilot 式

```
Style: Microsoft Copilot visual language. A smooth flowing gradient ribbon of blue, teal and pink wrapping behind and in front of the figure, glassmorphism layers, bright airy studio lighting, optimistic tone. Render: soft 3D, smooth matte-plastic surfaces, rounded volumes, subtle rim light. 16:9.
```

## 风格 5 · Meta Llama 式

```
Style: Meta / Llama mascot language. Soft clay-toy rendering, warm sand and cream palette, chunky rounded volumes, oversized simplified hands and boots, subtle subsurface softness, playful and approachable. Keep the horse ears and the two-tone ponytail but simplify them into soft rounded masses. Render: clay 3D, matte, no gloss. Studio diorama backdrop. 1:1.
```

## 风格 6 · xAI Grok 式

```
Style: xAI Grok visual language. Brutalist black background, monospaced grid overlay, one hard red laser scanline, thin red framing marks, high-contrast rim light, gritty cyber-terminal mood, visible dithering in the shadows. The chest tabs must still read as three distinct flat tabs, not merged into the red lighting. Render: flat vector lit by a single hard red key light. 16:9.
```

## 风格 7 · Perplexity 式

```
Style: Perplexity visual language. Paper-white background, two-ink scheme of deep teal and ink navy, hairline rules, atlas grid and coordinate ticks, generous typographic negative space without any actual type. No shading at all — one-color linework fills. Encyclopedia-plate feel, clean and scholarly. Render: pure flat vector, single-tone fills. 3:2.
```

## 风格 8 · DeepSeek 式

```
Style: DeepSeek visual language. Deep navy and whale-blue palette on a dark desaturated field, low-key lighting, quiet technical minimalism, faint sonar concentric rings and thin data lines behind the figure. Character mostly silhouette with a cyan edge highlight; chest tabs stay legible as three separate bars. Render: flat vector, low-key. 3:2.
```

## 风格 9 · 通义千问 Qwen 式

```
Style: Qwen visual language. Indigo and violet gradient field, ink-wash diffusion at the frame edges only, oriental-tech fusion, restrained palette with no gold. Crisp vector figure in front of a soft diffused background. Slightly ceremonial posture, elegant. Render: flat vector over diffused color field. 3:2.
```

## 风格 10 · 豆包 Doubao 式

```
Style: Doubao visual language. Pastel mint, cream and peach palette, chunky rounded 3D, head slightly enlarged for a friendly read, candy-like soft highlights, floating rounded shapes. Companion-app warmth, bright even lighting. Keep the three chest tabs as clean flat shapes even in the 3D treatment. Render: soft 3D, matte, high ambient. 1:1.
```

---

## 九宫格对比（单独使用，勿与上面叠加）

```
Create one character sheet: an exact 3x3 grid, nine equal vertical panels with even gutters. The same character repeated nine times, one per panel, in this order — (1) monochrome minimal on charcoal, (2) warm ivory editorial with terracotta accents, (3) iridescent prism gradient with soft 3D matte body, (4) flowing gradient ribbon with glass layers and soft 3D, (5) clay toy with warm sand palette, (6) brutalist black with red scanline, (7) flat paper-white atlas linework, (8) deep navy low-key technical, (9) pastel mint soft 3D.
Identical pose, identical framing, identical camera in all nine panels; only rendering style and color language change.
Every panel must show: upright silver-white horse ears with cyan inner membrane, asymmetric two-tone ponytail with one cyan and one violet inner strand, and exactly three flat downward-V chest slashes in one horizontal row — cyan, violet, red from left to right.
Hard constraints: no text, no letters, no numbers, no logos, no watermark, no panel labels of any kind.
```

---

## 锚点修复（图跑偏时只发这一条）

```
Restore the identity anchors only, change nothing else:
1) On the upper chest: exactly three flat downward-V color tabs with sharp corners, one horizontal row, even spacing, left to right cyan, violet, red. Plain flat blocks — not arrows, not icons, no outlines, no glow.
2) Remove every lettering element: no title, no codename, no signature, no watermark, no watermark-shaped rectangle.
3) Keep the horse ears, the asymmetric two-tone ponytail, and the high white hard collar exactly as they are.
```

---

## 实操提醒

- `downward-V slash` 比 `chevron` 稳得多。仍跑偏时追加：`each tab is a plain V shape with no head, no stem, no arrowhead`。
- 九宫格里最容易崩的是第 7 格（Perplexity 平涂），模型会偷偷上阴影。单独重生成那一格时加 `absolutely no shading, no shadow, no gradient`。
- 验收只看三处：耳朵是否为马耳、胸口三色块顺序（青/紫/红）、有无多余肢体或六指。这三处对了，风格差异再大也还是同一个人。
- 块 B 里最容易崩的两处：**数据尾被读成第二肢体或毛尾巴**、**吊坠飘到锁骨或与色块重叠**。前者追加 `the data tail is a cable emerging from the lower back, not a limb, not a fur tail, no tuft`；后者追加 `the horseshoe hangs at mid-sternum, well below the collar and below the chest tabs`。
- 三视图跑成「三个人」时，说明模型没吃地面线。追加：`all three body views stand on the same ground line at identical scale and identical head height`。
- 用色纪律必须逐条写死数量。只写「青紫红点缀」必然溢出；写 `cyan in at most six places, violet in exactly two, red exactly once` 才收得住。
- 固定验收四处：马耳、双色挑染、胸口三块顺序（青/紫/红）、红点全图仅一处。这四处对了，风格差异再大也还是同一个人。
*（内容由AI生成，仅供参考）*
