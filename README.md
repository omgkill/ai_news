# AI News Archive

自动抓取 AI 领域每日热点文章，保存完整内容到 Markdown 文件，并推送到 GitHub 仓库。

## 功能概述

- **多源聚合**：从 arXiv、AI Newsletters、Hacker News 等来源抓取 AI 相关文章
- **全文提取**：自动提取文章完整内容，支持 newspaper3k 和 trafilatura
- **智能过滤**：基于关键词（AI, LLM, GPT, Claude, Agent, RAG, DeepSeek）筛选相关内容
- **自动归档**：按日期组织 Markdown 文件，便于查阅
- **自动同步**：每日自动 commit 和 push 到 GitHub

## 目录结构

```
ai_news/
├── skill/
│   ├── SKILL.md              # Skill 配置说明
│   └── scripts/
│       ├── archive_daily.py  # 主脚本
│       ├── test_minimal.py   # 测试脚本
│       └── sync_skill.sh     # 同步脚本
├── 2026-06-03/               # 按日期归档的文章
│   ├── 01_xxx.md
│   ├── 02_xxx.md
│   └── ...
└── README.md
```

## 快速开始

### 运行每日归档

```bash
python3 skill/scripts/archive_daily.py
```

### 测试模式（仅抓取标题）

```bash
python3 skill/scripts/test_minimal.py
```

### 同步 Skill 文件

```bash
./skill/scripts/sync_skill.sh
```

## 文章来源

| 来源 | 说明 |
|------|------|
| arXiv | cs.AI、cs.LG、cs.CL 分类下的最新论文 |
| AI Newsletters | AI 领域热门通讯 |
| Hacker News | AI 相关热门讨论 |

## 输出格式

每篇文章保存为独立的 Markdown 文件：

```markdown
# 文章标题

- **Source**: arXiv
- **URL**: https://arxiv.org/abs/xxx
- **Time**: 2026-06-03
- **Heat**: 热度指标

## Summary

文章摘要

## Content

文章完整内容...

## Links

- [Discussion](讨论链接)
```

## 依赖

- Python 3.8+
- newspaper3k（内容提取，可选）
- trafilatura（备用提取，可选）
- requests

> 注：所有依赖代码已内置，无需外部 skill 依赖

## 配置

编辑 `archive_daily.py` 中的 `CONFIG` 字典：

```python
CONFIG = {
    "sources": ["ai_newsletters", "hackernews"],
    "keywords": "AI,LLM,GPT,Claude,Agent,RAG,DeepSeek",
    "limit_per_source": 5,          # 每个来源的文章数
    "repo_path": "~/ai_news",       # 本地仓库路径
    "auto_push": True,              # 自动推送到 GitHub
}
```

## 定时任务

可配置 cron 每日自动执行：

```bash
# 每天早上 8:00 执行
0 8 * * * python3 ~/ai_news/skill/scripts/archive_daily.py
```

## 抓取策略

项目针对不同来源使用不同的抓取方式，以应对网站限制：

### 1. arXiv 论文

**方式**：官方 API（无限制）

```
http://export.arxiv.org/api/query?search_query=cat:cs.AI+OR+cat:cs.LG+OR+cat:cs.CL
```

- 使用官方 Atom API，无需担心反爬
- 直接获取标题、摘要、作者、链接
- 无需二次访问网页

### 2. Hacker News

**方式**：官方 API（无限制）

- Hacker News 提供开放的 REST API
- 获取热门文章列表和讨论链接
- 内容需访问原始链接提取

### 3. AI Newsletters / 其他网站

**方式**：多层内容提取

| 层级 | 工具 | 特点 |
|------|------|------|
| 优先 | newspaper3k | 模拟浏览器行为，解析 HTML |
| 备用 | trafilatura | 专注正文提取，忽略广告/导航 |
| 最终 | 基础 HTTP | 直接 requests.get |

### 应对反爬策略

```
1. newspaper3k 内置 User-Agent 模拟
2. trafilatura 使用简洁请求头
3. 设置 timeout 防止超时阻塞
4. 多层 fallback 确保容错
5. 失败时记录 "*Content unavailable*"
```

### 已移除的内容干扰项

自动过滤以下 UI 元素：
- Subscribe / Sign in / Sign up / Login
- Share 按钮、订阅提示
- 单独数字（如阅读量）
- "Greetings from..." 等问候语

## 相关链接

- 仓库地址：https://github.com/omgill/ai_news
- Skill 文档：[skill/SKILL.md](skill/SKILL.md)