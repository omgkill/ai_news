---
name: ai-news-archive
description: "AI新闻存档技能：每日拉取AI文章全文，保存为Markdown文件并自动推送到GitHub仓库。触发词：AI新闻存档、ai news archive、存档AI文章。"
---

# AI News Archive Skill

每日拉取AI领域文章，保存完整英文内容到本地Markdown文件，自动推送到GitHub仓库。

---

## 工作流程

### 1. 拉取文章
```bash
python3 scripts/archive_daily.py
```

### 2. 自动执行
- 拉取 AI 信源（HuggingFace Papers, AI Newsletters, Hacker News AI）
- 深度抓取每篇文章完整内容
- 生成日期目录和Markdown文件
- 自动 Git commit 和 push

---

## 配置

| 配置项 | 值 |
|---|---|
| 信源 | arXiv Papers, AI Newsletters, Hacker News |
| 关键词 | AI,LLM,GPT,Claude,Agent,RAG,DeepSeek |
| 每信源文章数 | 5 篇 |
| 仓库地址 | https://github.com/omgkill/ai_news |
| 本地路径 | ~/ai_news |
| 自动推送 | 是 |

---

## 文件位置

| 位置 | 路径 | 作用 |
|---|---|---|
| 工作目录 | `~/.openclaw/skills/ai-news-archive/` | OpenClaw 实际执行 |
| Git备份 | `~/ai_news/skill/` | GitHub 持久化 |

**同步脚本**: `scripts/sync_skill.sh`

---

## 目录结构

```
~/ai_news/
├── 2026-06-03/
│   ├── 01_hf_paper-transformers-optimization.md
│   ├── 02_hn_gpt5-rumors.md
│   └── ...
├── 2026-06-04/
│   └── ...
└── README.md
```

---

## Markdown模板

```markdown
# {title}

- **Source**: {source}
- **URL**: {url}
- **Time**: {time}
- **Heat**: {heat}

## Summary

{中文摘要}

## Content

{英文原文内容}

## Links

- [Discussion]({hn_url})
- [GitHub]({github})
```

---

## 定时任务

如需配置定时任务，编辑 OpenClaw cron：

```bash
# 每天早上 8:00 执行
0 8 * * * ai-news-archive
```

---

## 触发方式

**定时任务**: 每天 08:00 自动运行

**手动触发**: 说 "运行AI新闻存档任务" 或 "AI新闻存档"

**直接运行脚本**:
```bash
python3 ~/.openclaw/skills/ai-news-archive/scripts/archive_daily.py
```

---

## 依赖

- Python 3.8+
- 复用 news-aggregator-skill 的依赖
- Git 已配置 push 权限