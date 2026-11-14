#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
marvis_lint — Marvis 人格执行规范 v3 · 禁止词检查器

用法:
    python marvis_lint.py --path ./app/src
    python marvis_lint.py --path . --include .ts .py --exclude build node_modules
    python marvis_lint.py --text "希望对你有帮助"

退出码:
    0  干净
    1  命中禁句
    2  参数或路径错误
"""
import argparse
import json
import os
import re
import sys

# ---------------------------------------------------------------- 禁句库
# (编号, 分组, 正则, 原句, 改写建议)
BANNED = [
    ("01", "讨好型", r"希望(对你|对您)有(所)?帮助", "希望对你有帮助", "（直接删）"),
    ("02", "讨好型", r"如有(其他|其它)问题.{0,6}(随时)?(告诉我|联系我)", "如有其他问题请随时告诉我", "还有别的就说。"),
    ("03", "讨好型", r"感谢(您的|你的)?(理解(与|和))?(支持|配合)", "感谢您的理解与支持", "不用谢，这是该做的。"),
    ("04", "讨好型", r"感谢(您的|你的)?反馈", "感谢您的反馈", "记下了，下次改。"),
    ("05", "讨好型", r"温馨提示", "温馨提示", "（直接删，正文里说）"),
    ("06", "讨好型", r"继续努力(为您|为你)?服务", "我会继续努力为您服务", "（删，用下一次交付证明）"),
    ("07", "免责型", r"(作为|身为)(一个)?\s*AI", "作为 AI 语言模型", "（删。她从不自称 AI）"),
    ("08", "免责型", r"我(无法|不能)完成(此|该|这个)?(操作|请求)", "我无法完成此操作", "这个不做。理由：……"),
    ("09", "免责型", r"(很|非常)?抱歉[，,]?\s*我(不明白|不理解)(您的|你的)?意思", "很抱歉，我不明白您的意思", "这句我理解成 A 还是 B？"),
    ("10", "免责型", r"为了(提供|给)(更好|更优质)的(服务|体验)", "为了提供更好的服务", "（删。这是授权话术）"),
    ("11", "免责型", r"我会?尽力(而为|做到)", "我会尽力而为", "我做 A，做不成给你 B。"),
    ("12", "拖延型", r"请稍(候|等)[，,]?\s*(正在)?(努力)?(处理|加载|生成)中?", "请稍候，正在努力处理中", "在跑，约 40 秒。"),
    ("13", "拖延型", r"正在(为您|为你)?(查询|处理)[，,]?\s*请?(耐心)?等待", "正在为您查询，请耐心等待", "查着呢，两个口径，先给你一个。"),
    ("14", "拖延型", r"(您的|你的)需求(我已|已)收到", "您的需求我已收到", "明白，分两步。"),
    ("15", "拖延型", r"(操作|执行)(失败|异常)[，,]?\s*请(重试|稍后重试)", "操作失败，请重试", "挂了。原因：…… 我重跑。"),
    ("16", "拖延型", r"您可以?(尝试|试试)(以下|下面)(的)?(方法|方式)", "您可以尝试以下方法", "试试这个：……"),
    ("17", "空道歉", r"抱歉[给为]?(您|你)?带(来)?(不便|麻烦)", "抱歉给您带来不便", "我的问题。错在……"),
    ("18", "空道歉", r"(非常|十分)?抱歉[，,]?\s*我?(深表|十分)?歉意", "非常抱歉，我深表歉意", "是我搞错了，已回滚。"),
    ("19", "空道歉", r"请问(还)?有(什么|其他|其它)(可以|能)?(帮|为)(您|你)", "请问还有什么可以帮您", "还有吗。"),
    ("20", "空夸赞", r"这(是)?(一个)?(很好的|好)问题", "这是一个很好的问题", "（删，直接回答）"),
]

COMPILED = [(n, g, re.compile(p), raw, hint) for n, g, p, raw, hint in BANNED]

DEFAULT_EXT = [".py", ".ts", ".tsx", ".js", ".jsx", ".kt", ".java",
               ".swift", ".dart", ".json", ".yaml", ".yml", ".xml",
               ".vue", ".rs", ".go"]
DEFAULT_EXCLUDE = ["node_modules", ".git", "build", "dist", ".gradle",
                   "__pycache__", "venv", ".venv", "vendor"]
IGNORE_TOKEN = "marvis-lint: ignore"


def check_text(text):
    """返回 [(行号, 列号, 编号, 分组, 原句, 建议)]"""
    hits = []
    for lineno, line in enumerate(text.splitlines(), 1):
        if IGNORE_TOKEN in line:
            continue
        for num, group, rx, raw, hint in COMPILED:
            for m in rx.finditer(line):
                hits.append((lineno, m.start() + 1, num, group, raw, hint))
    return hits


def iter_files(root, include, exclude):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in exclude and not d.startswith(".")]
        for fn in filenames:
            if os.path.splitext(fn)[1].lower() in include:
                yield os.path.join(dirpath, fn)


def to_records(raw_hits, rel_path):
    out = []
    for lineno, col, num, group, raw, hint in raw_hits:
        out.append({"file": rel_path, "line": lineno, "col": col,
                    "id": num, "group": group, "hit": raw, "suggest": hint})
    return out


def emit_summary(records, scanned, root):
    """写入 GitHub Step Summary（若在 Actions 环境中）"""
    groups = {}
    files = {}
    for r in records:
        groups[r["group"]] = groups.get(r["group"], 0) + 1
        files[r["file"]] = files.get(r["file"], 0) + 1

    lines = ["## 人格 lint · 禁止词报告", ""]
    if not records:
        lines += ["**PASS** — 扫描 `%s`，%d 个文件，零命中。" % (root, scanned), ""]
    else:
        lines += ["**命中 %d 处**，涉及 %d 个文件（扫描 %d 个文件）。" % (len(records), len(files), scanned), ""]
        lines += ["| 分组 | 命中 |", "|---|---|"]
        for g, c in sorted(groups.items(), key=lambda x: -x[1]):
            lines.append(f"| {g} | {c} |")
        lines += ["", "| 文件 | 命中 |", "|---|---|"]
        for f, c in sorted(files.items(), key=lambda x: -x[1])[:10]:
            lines.append(f"| `{f}` | {c} |")
        lines += ["", "<details><summary>明细（最多 50 条）</summary>", "", "| 位置 | 编号 | 禁句 | 改成 |", "|---|---|---|---|"]
        for r in records[:50]:
            lines.append(f"| `{r['file']}:{r['line']}` | {r['id']} | {r['hit']} | {r['suggest']} |")
        lines += ["", "</details>", ""]

    md = "\n".join(lines)
    target = os.environ.get("GITHUB_STEP_SUMMARY")
    if target:
        try:
            with open(target, "a", encoding="utf-8") as f:
                f.write(md + "\n")
            return
        except OSError:
            pass
    print(md)


def main():
    ap = argparse.ArgumentParser(description="Marvis 人格规范 v3 · 禁止词检查器")
    ap.add_argument("--path", default=".", help="扫描根目录（默认当前目录）")
    ap.add_argument("--include", nargs="*", default=None, help="扫描的扩展名，如 .ts .py")
    ap.add_argument("--exclude", nargs="*", default=None, help="跳过的目录名")
    ap.add_argument("--text", default=None, help="只检查一段文本，不扫文件")
    ap.add_argument("--warn-only", action="store_true", help="只报告，恒定返回 0（灰阶观测期用）")
    ap.add_argument("--json", dest="as_json", action="store_true", help="以 JSON 数组输出（供 CI 解析）")
    ap.add_argument("--summary", action="store_true", help="输出 Markdown 摘要到 GITHUB_STEP_SUMMARY")
    args = ap.parse_args()

    if args.text is not None:
        hits = check_text(args.text)
        recs = to_records(hits, "<text>")
        if args.as_json:
            print(json.dumps(recs, ensure_ascii=False, indent=2))
        else:
            for r in recs:
                print(f"[{r['id']}] {r['group']} · 命中「{r['hit']}」 → {r['suggest']}")
            print(f"\n共 {len(recs)} 处命中。")
        if args.warn_only:
            return 0
        return 1 if recs else 0

    if not os.path.isdir(args.path):
        print(f"路径不存在或不是目录: {args.path}", file=sys.stderr)
        return 2

    include = [e if e.startswith(".") else "." + e for e in args.include] if args.include else DEFAULT_EXT
    exclude = set(args.exclude) if args.exclude else set(DEFAULT_EXCLUDE)

    records, scanned = [], 0
    for fp in iter_files(args.path, include, exclude):
        scanned += 1
        try:
            with open(fp, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
        except OSError:
            continue
        hits = check_text(content)
        if hits:
            records.extend(to_records(hits, os.path.relpath(fp, args.path)))

    if args.as_json:
        print(json.dumps(records, ensure_ascii=False, indent=2))
    elif args.summary:
        emit_summary(records, scanned, args.path)
    else:
        for r in records:
            print(f"{r['file']}:{r['line']}:{r['col']}  [{r['id']}] {r['group']} · 「{r['hit']}」 → {r['suggest']}")
        print()
        if records:
            print(f"FAIL — {len(set(r['file'] for r in records))} 个文件，{len(records)} 处禁句。请按箭头改写。")
        else:
            print(f"PASS — 扫描 {args.path}（{scanned} 个文件），零命中。")

    if records and not args.warn_only:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
