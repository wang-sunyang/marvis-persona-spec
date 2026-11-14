---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: ba89e2f233ef3708dee31ea6faa51e09_d3b154e9dfef11f18c5752540024e231
    ReservedCode1: KgtQbJjKuXeBJltvwDLP6at+UNi9FJxMNidBIfoDQn4VL2ZjnGnIh6LAgFeYREvRhBEFv1oNwOvEM6hs4Yjkn/eYy5WxwEGSxSC4ePatJ4OJDGzu+vDHkA7Q41aIwR1gwhCYpjP058T421+mctErZWclEt7F/vkFw5ewmmoEQw50od64+spaAyLL6QQ=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: ba89e2f233ef3708dee31ea6faa51e09_d3b154e9dfef11f18c5752540024e231
    ReservedCode2: KgtQbJjKuXeBJltvwDLP6at+UNi9FJxMNidBIfoDQn4VL2ZjnGnIh6LAgFeYREvRhBEFv1oNwOvEM6hs4Yjkn/eYy5WxwEGSxSC4ePatJ4OJDGzu+vDHkA7Q41aIwR1gwhCYpjP058T421+mctErZWclEt7F/vkFw5ewmmoEQw50od64+spaAyLL6QQ=
---

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

## 五、豁免

行尾加注释即可：

```kotlin
// marvis-lint: ignore  这是给用户看的错误日志模板，故意保留原文
val tpl = "操作失败，请重试"
```

**防线**：只支持行级豁免，不支持整文件豁免。有豁免就必须有理由写在后面——这句话本身就是给 review 的人看的。

不建议在测试文件里批量豁免，那等于把检查器关掉。

---

## 六、Android 项目特别注意

好消息：`res/values/strings.xml` 里的 UI 文案**会被扫到**，这正是价值所在——`strings.xml` 是最容易出现"抱歉给您带来不便"的地方。

要注意的三点：

1. `values-en/` 等英文资源不会命中中文正则，正常跳过
2. 若你把 AS 的默认模板文案（如 "Operation failed, please try again"）直接翻译进了中文资源，第一轮会**大量命中**，属于预期
3. 第一次跑建议只扫 `app/src/main`，全仓扫会包含 build 产物（已在默认排除表里，但自定义目录需要 `--exclude`）

```bash
python tools/marvis_lint.py --path app/src/main
```

---

## 七、本地预检（可选）

想在自己的提交前就拦住：

```bash
cp MARVIS_09_pre-commit .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
```

跳过单次检查：`git commit --no-verify`

---

## 八、如果不用 GitHub Actions

任何 CI 都能接，只需要一行：

```bash
python tools/marvis_lint.py --path .        # 有命中则退出码 1
python tools/marvis_lint.py --path . --warn-only   # 恒定退出码 0
```

`--json` 输出结构化结果，`--summary` 输出 Markdown 摘要（在 GitHub 环境里会自动写进 Job Summary，不在则打印到终端）。

---

*检查器只能拦住已经被写下来的句子。真正要练的是那 30 格。*
*（内容由AI生成，仅供参考）*
