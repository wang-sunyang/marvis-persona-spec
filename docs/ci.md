<!-- marvis-lint: ignore-file 含 lint 输出示例，必须保留原句 -->


# CI 接入说明 · persona-lint

配套：`MARVIS_08_marvis_lint.py`（检查器）、`MARVIS_09_ci_persona-lint.yml`（工作流）

---

## 一、两个文件放哪

```
你的仓库/
├── tools/
│   └── marvis_lint.py          ← 拷 MARVIS_08_marvis_lint.py，重命名
└── .github/
    └── workflows/
        └── persona-lint.yml    ← 拷 MARVIS_09_ci_persona-lint.yml
```

不需要装任何依赖，纯标准库。

---

## 二、接入四步

1. 拷上面两个文件，路径别改（workflow 里写死了 `tools/marvis_lint.py`）
2. 本地先跑一次，看存量底数：
   ```bash
   python tools/marvis_lint.py --path .
   ```
3. 提交并开一个 PR，去 PR 页面看 **Job Summary**，报告会直接渲染成表格
4. 确认能跑通后，把 `env.PERSONA_LINT_BLOCKING` 保持 `"false"` 不动，进入灰阶期

---

## 三、两阶段设计

| 阶段 | 开关 | 行为 | 目的 |
|---|---|---|---|
| 灰阶观测 | `"false"` | 出报告、传 JSON，**永不挂 CI** | 摸清存量，不打断任何人 |
| 硬门禁 | `"true"` | 命中即 exit 1，PR 阻塞 | 防止新禁句流入 |

**为什么必须分两段**：如果现在存量就有几十上百处，直接开阻塞等于当天全员罢工，团队第一反应是关掉这个检查——那就永久失效了。

灰阶期的真实任务不是"等两周"，是**把存量清到零**。

---

## 四、两周内看什么

每次运行都会上传 `persona-lint.json`（保留 30 天），三个指标：

1. **命中数曲线** —— 是否单调下降
2. **分组占比** —— 讨好型占比高说明在写客服话术；免责型高说明在推责任
3. **热点文件** —— 集中在哪个文件，往往就是还没有人格的那块

**开阻塞的判据**：

- 存量清到 0，且连续两周新增命中 < 5 条 → 改 `"true"`
- 存量清不干净，或每周新增仍然 > 30 → 不要开，先改文案

---

## 五、扫描范围：不止代码

默认扩展名包含 `.md` / `.mdx`，**文档和代码一起过关卡**。

原因很直接：禁句最高发的地方不是代码，是公告、发布说明、README、运营文案——恰好全是 Markdown。只扫代码，等于把最容易脏的那半块放过。

代价是：讲规则的文档必须写出禁句原文才讲得清。所以下一节专门留了口子。真正该被盯的，是新写的发布公告、用户协议、引导页文案、错误提示。

---

## 六、豁免

**行级（首选）**：注释放同一行行尾，只跳过这一行。

```kotlin
// marvis-lint: ignore  这是给用户看的错误日志模板，故意保留原文
val tpl = "操作失败，请重试"
```

**文件级（只给定义源与元文档）**：必须写在文件**前 5 行**内，且必须带理由。

```markdown
<!-- marvis-lint: ignore-file 本文件是禁句表本体，示例即条款 -->
```

```python
# marvis-lint: ignore-file 禁句库定义源，原文即数据
```

本仓库自己用掉的 5 个豁免，全是"不写禁句就干不了活"的文件：

| 文件 | 原因 |
|---|---|
| `docs/persona-spec-v3.md` | 20 条禁句的定义表 |
| `tools/marvis_lint.py` | 禁句正则库本体 |
| `README.md` | 门面文档，要放反面示例 |
| `docs/ci.md` | 本文，要贴检查器输出样例 |
| `docs/research/04-ip-next-step.md` | 研究报告，禁句是分析对象 |

**为什么必须留文件级**：禁句的定义源不可能通过自己的检查，这是所有 linter 的共同处境（ESLint 也得对配置豁免自身规则）。硬要全豁免掉，只能把禁句拆字或转码，那比豁免更坏。

**成本约束**：文件级豁免必须写理由，且每次运行的 Job Summary 都会列出豁免清单。想悄悄关掉某个文件的检查，会在 PR 里显形。

**不该用的场合**：业务代码、UI 文案、测试断言里整文件豁免。那不是豁免，是把检查器关掉。

---

## 七、Android 项目特别注意

好消息：`res/values/strings.xml` 里的 UI 文案**会被扫到**，这正是价值所在——`strings.xml` 是最容易出现"抱歉给您带来不便"的地方。

要注意的三点：

1. `values-en/` 等英文资源不会命中中文正则，正常跳过
2. 若你把 AS 的默认模板文案（如 "Operation failed, please try again"）直接翻译进了中文资源，第一轮会**大量命中**，属于预期
3. 第一次跑建议只扫 `app/src/main`，全仓扫会包含 build 产物（已在默认排除表里，但自定义目录需要 `--exclude`）

```bash
python tools/marvis_lint.py --path app/src/main
```

---

## 八、本地预检（可选）

想在自己的提交前就拦住：

```bash
cp MARVIS_09_pre-commit .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
```

跳过单次检查：`git commit --no-verify`

---

## 九、如果不用 GitHub Actions

任何 CI 都能接，只需要一行：

```bash
python tools/marvis_lint.py --path .        # 有命中则退出码 1
python tools/marvis_lint.py --path . --warn-only   # 恒定退出码 0
```

`--json` 输出结构化结果，`--summary` 输出 Markdown 摘要（在 GitHub 环境里会自动写进 Job Summary，不在则打印到终端）。

---

*检查器只能拦住已经被写下来的句子。真正要练的是那 30 格。*