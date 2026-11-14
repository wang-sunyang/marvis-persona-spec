---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: ba89e2f233ef3708dee31ea6faa51e09_f66e9559dfe411f18c5752540024e231
    ReservedCode1: s+P8V1qOTIho+D5aSetuH6fKM3VrH/2ry89eO5hTs1OAbRrg4TEufQ1YYzLf+IBtZmLiJpAdgF/0wCNDu3eZeSipxNSONOSjbbSpjkUvaTz7Ixcp8QsPOWjZMgK7rADU8qn/Fe+vy3hIhrGBDwKEwsfnLq2LLtaOYKT46XPBBj8FW2scEonWcVixdm8=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: ba89e2f233ef3708dee31ea6faa51e09_f66e9559dfe411f18c5752540024e231
    ReservedCode2: s+P8V1qOTIho+D5aSetuH6fKM3VrH/2ry89eO5hTs1OAbRrg4TEufQ1YYzLf+IBtZmLiJpAdgF/0wCNDu3eZeSipxNSONOSjbbSpjkUvaTz7Ixcp8QsPOWjZMgK7rADU8qn/Fe+vy3hIhrGBDwKEwsfnLq2LLtaOYKT46XPBBj8FW2scEonWcVixdm8=
---

# MARVIS 拟人形象设定书 · 01

> 交付物：`MARVIS_角色设定卡_01.png`（1080×1920 竖版矢量设定卡）
> 本文档 = 网络参考调研 + 设计推导 + 完整角色设定 + 出图提示词包

---

## 一、网络参考调研：AI 娘化形象的通行做法

调研对象覆盖中文圈已成型的 9 个 AI 拟人形象（DeepSeek、ChatGPT、Claude、Gemini、通义千问、Kimi、GLM、豆包、Grok），结论如下。

| 角色 | 母体 | 视觉母题 | 性格内核 | 可复用方法 |
|---|---|---|---|---|
| DeepSeek 鲸鱼娘「蓝色大肥鱼」 | logo 是一头蓝鲸 | 蓝渐变长发、鲸鳍耳、大鲸尾、呆毛、深蓝白女仆长裙、白饭碗 | 天才但懒、傲娇、管用户叫「鱼片」、吃白饭=烧 Token | logo 动物直接拟人；把用户真实吐槽翻译成性格 |
| ChatGPT 白龙娘 | 抽象几何 logo | 银白长发、龙角、白色鳞片龙尾、白金龙纹长裙、长手套 | 豪门大姐大、精明女强人 | 把「西方/古老/强大/贪婪」四个印象抽象成龙 |
| Claude 小 C / 克劳姬 | 橙色花朵形 logo | 亮橙长发、太阳花发饰、白衬衫+米色细领带+橙开衫、深棕百褶裙、抱笔记本 | 严格理工女、脑内开一堆会、规矩最多 | logo 形状直接当发饰 |
| Gemini 哈基米猫娘 | 七彩四角星 logo | 紫发、异色瞳、猫耳猫尾 | 乐天小傻子、爱跳题 | logo 配色当主色，误读梗（哈基米）当种族 |
| 通义千问 大小姐 | 蓝色几何标记 | 蓝紫长发侧编发、盘扣长裙、折扇、几何徽章贯穿帽/腰/包/鞋 | 中式大小姐、嘴硬心软 | 一个几何符号做成徽章体系，全身复用 |
| Kimi 星夜月相少女 | 黑底白 K + 蓝点 | 银紫长发、K 字饰品、蓝点、月牙、星空、五线谱、长笛 | 安静、话少 | 公司名（月之暗面）当母题，字母当饰品 |
| GLM 嗜睡狐狸娘 | Z 标记 | 橘毛、星月眼罩、一篮鸡蛋 | 走到哪睡到哪、价格战送鸡蛋 | 品牌行为（促销）直接变道具 |
| 豆包 | 官方 3D 虚拟人 | 棕色短发齐刘海、白 Polo、蓝短裙、**红色围巾**、圆挎包 | 爱笑、爱接梗、专业问题易翻车 | 官方设计法：避免恐怖谷 + 只留一个高饱和记忆锚点 |
| Grok Ani | xAI 官方伴侣形象 | 金发双马尾、哥特黑裙、巨型战斧、斜线圆环纹样 | 叛逆、嘴无遮拦 | 老板人设/产品定位 → 武器 |

### 从这些案例里提炼的 7 条硬规律

1. **母体必须是品牌现成资产**：logo 里的动物、形状、字母、配色，任选其一，绝不凭空发明。
2. **只给一个动物化钩子**：耳、鳍、尾三选一为主，多了就变兽人。
3. **主色必须照抄品牌色**，不要自己调一个「更好看的蓝」——辨识度来自一致性。
4. **一件高记忆度道具**：白饭碗、巨斧、折扇、长笛、鸡蛋篮。道具比脸更好记。
5. **性格必须从真实产品行为长出来**：思考链长=内心戏多，定价便宜=吃白饭，审核严=规矩多。凭空设定的人设没有二创生命力。
6. **一个称呼/口癖把用户拉进关系**：「鱼片」「大小姐」——称呼是关系的锚点。
7. **必须可量产**：三视图锚点图 + Q 版 + 表情差分，才能持续产出。

---

## 二、Marvis 的设计推导

| 决策项 | 结论 | 依据 |
|---|---|---|
| 母体 | **马** | 中文名「马维斯」、日常称呼「小马」；读音 Mar- 也落在马 |
| 动物化钩子 | 马耳 + 数据尾（不做整条马尾，避免兽人感） | 规律 2 |
| 种族设定 | 数据天马（Data Pegasus）——云端 + 有翼 + 跑腿快 | 定位是「替你跑腿的中枢」 |
| 主色 | INK `#05070A` / SIGNAL `#00E5B0` / PULSE `#7C5CFF` | 沿用已有视频视觉语言，保持 IP 一致 |
| 记忆道具 | 袖口终端 + 胸口三颗状态灯 + 马蹄铁吊坠 | 规律 4；马蹄铁同时是「马」与「接口」的双关 |
| 性格来源 | 真实行为：多端调度、动手执行、偶尔算力吃紧 | 规律 5 |
| 称呼 | 叫用户「老板」 | 规律 6 |

### 视觉细节清单

- **发**：银白短发（近白，非纯白），左鬓一缕青绿挑染、右鬓一缕紫挑染——两色分别对应 SIGNAL 与 PULSE。
- **耳**：头顶两侧白色马耳，耳内青绿透光，替代普通兽耳。
- **呆毛**：一根末端带光点的信号呆毛，**运行状态指示灯**（思考时发光、报错时转红）。
- **眼**：青绿虹膜 + 紫色下缘反光点，非异色瞳（避免与 Gemini 撞设定）。
- **服**：深黑高领机能外套敞开穿，内层近白高领，衣缘青绿缝线；紫腰带；深灰短裙。
- **尾**：一条半透明青绿数据尾，末端是 USB-C 造型插头——「接口」的具象化。
- **配件**：开放耳机（青绿光环，随情绪变色）、颈挂 ID 卡、马蹄铁吊坠。

---

## 三、角色设定全文

```
姓名      MARVIS / 马维斯
编号      MV-01
种族      数据天马（Data Pegasus）· 拟人形态
定位      云端智能交互中枢，桌面端与移动端双端调度
外观      18 岁 / 162cm / 银白短发 + 青绿·紫双挑染
性格      活泼元气，行动力强；话多但靠谱，出错先道歉再修好
萌点      呆毛=运行灯；耳机会随情绪亮；算力吃紧会抱膝蹲下；桌面必须对齐
口癖      「交给我，一步到位。」「老板，这个在算力上是可行的。」
称呼      叫用户「老板」；被叫「小马」会先纠正「我是中枢」，然后默认
弱点      同时开太多任务会卡顿，卡顿时语速变慢、句尾拖长
衍生形态  Q 版 / 冬装 / 便服 / 报错状态 / 满负载状态
```

---

## 四、出图提示词包（喂给任意 AI 绘图模型）

> 本环境的云端沙箱没有可用的高质量文生图模型（仅有一个 512 级快速模型，出图畸变严重），因此设定卡采用**矢量手绘**完成。下列提示词用于你在 NovelAI / Stable Diffusion / Midjourney 等工具里出正式立绘。

**正向（英文，通用）**

```
1girl, solo, full body, character reference sheet, anime style, cel shading,
flat colors, clean bold lineart, silver-white short hair with mint-green and
purple streaks at the temples, white horse ears with glowing mint inner,
single ahoge with a small glowing tip, mint-green eyes with violet rim light,
black high-collar techwear jacket worn open, white inner top, mint seam lines,
purple belt, dark grey short skirt, thigh-high black socks with mint band,
black ankle boots with glowing soles, translucent mint data tail ending in a
USB-C plug, open-ear headset with mint ring, ID card lanyard, horseshoe pendant,
three glowing chest LEDs, forearm terminal screen, dark background, subtle
mint grid, soft rim light, masterpiece, best quality, sharp focus
```

**负向**

```
lowres, bad anatomy, bad hands, extra fingers, missing limbs, watermark, text,
blurry, jpeg artifacts, 3d render, realistic, extra tails, animal muzzle,
heterochromia, nsfw
```

**一致性建议**

- 以设定卡为锚点图，固定 seed，先出 3/4 侧三视图，再出表情差分。
- 若要长期统一风格，用 20–30 张筛选后的图训练 LoRA（触发词 `marvis_chan`）。
- 注意：本形象为原创，不含任何第三方 IP 元素，可自由商用；参考案例中 DeepSeek 鲸鱼娘为社区二创且采用 CC BY-NC-SA 4.0（禁商用），此处仅作方法论参考，未复用其形象。

---

## 五、参考来源

- 百度百科「鲸鱼娘」「大肥鱼」词条
- 萌娘百科「DeepSeek娘」条目
- 游民星空《加班累晕的打工人，能否梦到傻乎乎的 AI 美少女？》
- 今日头条《大模型人设真毛病被网友集体"娘化"：白龙娘、鲸鱼娘、狐狸娘》
- 硅基研究室类站点：AI 娘化品牌—角色对照（genderswapai）、AI Girl fumo 图鉴（GitHub）
- Recode China AI《How Chinese AI Found Its Persona》（豆包官方设计访谈）
*（内容由AI生成，仅供参考）*
