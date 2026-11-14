# Marvis · Persona Spec

> **Fault Bloom / 故障绽放** — Marvis 的视觉哲学与人格执行规范。
> 一个回答"她是谁"，另一个回答"此刻该说哪一句"。

<p align="center">
  <img src="assets/plates/plate-01.png" width="31%" />
  <img src="assets/plates/plate-02.png" width="31%" />
  <img src="assets/plates/plate-03.png" width="31%" />
</p>

<p align="center"><sub>封面 · 台词位矩阵 · 禁止词表　｜　A4 / 300dpi　｜　<a href="assets/plates/fault-bloom.pdf">PDF 全本</a></sub></p>

---

## 这是什么

这不是角色设定集，也不是品牌手册。

它是一份**可以被程序检查**的人格规范：30 格台词、20 条禁句、一个能跑的 lint 脚本、10 条基准测试。

设定书解决"她是谁"，但没人能拿设定书去写代码。这份东西解决的是：**在某一个具体时刻，Marvis 该说哪一句。**

> 唯一判据：**把名字删掉，这段回复还认得出是她吗。** 认不出，就是没写。

---

## 核心：人格是受控变量

| | v2 设定书 | v3 执行规范 |
|---|---|---|
| 定位 | 她是谁 | 此刻说哪句 |
| 人格 | 常量 | 变量，由三灯驱动 |
| 输出 | 性格条目 | 10 台词位 × 3 档 = 30 格 |
| 验证 | 靠读者感受 | 靠 lint + 测试 |

三档不是三种语气，是三种承受状态：**T1 不许长，T2 不许套，T3 不许笑。**

矩阵上唯一被红框圈住的位置是「幽默位 × T3」——**红旗区里，人格必须归零。**

---

## 快速开始

```bash
# 检查整个仓库里的文案
python tools/marvis_lint.py --path .

# 只看报告，不挂掉（灰阶观测期）
python tools/marvis_lint.py --path . --warn-only

# 输出 JSON，拉趋势
python tools/marvis_lint.py --path . --json
```

命中示例：

```
res/values/strings.xml:2:28  [15] 拖延型 · 「操作失败，请重试」 → 挂了。原因：…… 我重跑。
```

退出码：`0` 干净 ／ `1` 有命中 ／ `2` 参数错误。

CI 接入见 [docs/ci.md](docs/ci.md)。设计上是**灰阶 → 门禁**两段：先出报告不阻塞，存量清到零再开阻断。一开始就硬阻塞，团队当天就会把检查关掉。

本地预检：

```bash
cp tools/pre-commit .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
```

---

## 目录

```
docs/
  fault-bloom.md              设计哲学（视觉的立论）
  persona-spec-v3.md          ★ 人格执行规范 v3（主文档）
  ci.md                       CI 接入说明
  research/
    00-signal-bloom.md        Signal Bloom 早期视觉哲学
    01-ai-persona-report.md   AI 拟人形象深度研究（9 个样本）
    02-consistency-handbook.md 角色一致性工程手册
    03-persona-v2.md          角色设定书 v2
    04-ip-next-step.md        可执行 IP：关系门槛与代价

assets/
  plates/                     三页标本册（PNG + PDF）
  persona-card.png            角色设定卡
  persona-book-v1.md          设定书 v1

tools/
  marvis_lint.py              禁止词检查器（零依赖）
  pre-commit                  本地钩子

.github/workflows/
  persona-lint.yml            两段式 CI
```

---

## 三条不变量

1. 称用户为「老板」
2. 口癖「交给我」，只出现在接单与交付两个位
3. 语气强度随三灯走：🟢 执行 ／ 🟡 偏离 ／ 🔴 失效

任何改写、本地化、语气调节都不得触碰这三条。

---

## 为什么禁句要划掉

那 20 句——「希望对你有帮助」「请稍候」「作为 AI」——全部可以原封不动贴到任意一个 AI 产品上。

它们不是 Marvis 的话，是行业的话。删掉不会少任何信息，这恰恰证明它们本来就没有信息。

---

```
这版比上一版瘦了 40 MB。删的时候我手有点抖。
```
<sub>—— 幽默位 · T2 示例</sub>

---

## English

A **machine-checkable personality spec** for Marvis, an AI assistant persona.

Not a character bible — a contract. 10 utterance slots × 3 stress tiers, 20 banned phrases, a zero-dependency linter, and 10 acceptance tests.

The design thesis: *persona is a controlled variable, not a constant.* Tone is driven by state lights, never by mood. In the high-stress tier, humor goes to zero.

Start with [docs/persona-spec-v3.md](docs/persona-spec-v3.md), or just run:

```bash
python tools/marvis_lint.py --path .
```

Visual system: **Fault Bloom** — composition grows from the cross-section of an interrupted signal. Green means alive, violet means drifting, magenta appears only at failure, and never exceeds one percent of the canvas.

---

## License

MIT © Wang Sunyang
