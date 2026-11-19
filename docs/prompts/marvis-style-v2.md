<!--
MARVIS Style Prompt Pack v2
Author: 王孙阳 (Wang Sunyang) / Nightglean Studio
Repo: https://github.com/wang-sunyang/marvis-persona-spec
License: CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/
You may share and adapt this prompt pack for any purpose, including commercially,
provided you give appropriate credit to the author and the repository above.
-->

> **License: CC BY 4.0** — 转载、改编、商用均可，请署名「王孙阳 / Nightglean Studio」并附仓库链接。

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

# MARVIS 多风格生成提示词 v2

英文提示词集，用于让主流图像模型把同一个 MARVIS 角色套进各大 AI 的视觉语言。
用法：**块 A（身份锁定）+ 任一风格块**，两段连起来发。只换画风不换人。

修订要点（相对 v1）：
1. `chevron` → `flat downward-V slash / flat angular tab`，防模型画成箭头图标。
2. 名字改为「内部代号，禁止渲染成文字」，消除水印式 MARVIS 字样。
3. 每个风格块自带 render 模式，平涂与 3D 拆开写，避免半平半 3D。
4. 块 A 增加数量硬约束（两臂两腿、五趾、单角色）。

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
*（内容由AI生成，仅供参考）*
