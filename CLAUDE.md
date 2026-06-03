# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

AI News Archive - A daily AI news aggregation system that fetches articles from multiple sources (arXiv, AI Newsletters, Hacker News), extracts full content, saves as Markdown files organized by date, and auto-pushes to GitHub.

## Commands

```bash
# Run the daily archive process (fetch, save, push)
python3 skill/scripts/archive_daily.py

# Run minimal test (titles only, no deep content fetch)
python3 skill/scripts/test_minimal.py

# Sync skill files from OpenClaw to this repo
./skill/scripts/sync_skill.sh
```

## Architecture

### Core Script: `archive_daily.py`

1. **Fetch Phase**: Pulls articles from:
   - arXiv API (cs.AI, cs.LG, cs.CL categories, filtered by AI keywords)
   - AI Newsletters (via `news-aggregator-skill`)
   - Hacker News (via `news-aggregator-skill`)

2. **Enrichment Phase**: Extracts full article content using:
   - newspaper3k (primary)
   - trafilatura (fallback)
   - Basic URL fetch (final fallback)

3. **Output Phase**: Creates Markdown files in date directories (`YYYY-MM-DD/`)

4. **Publish Phase**: Git commits and pushes to remote

### Configuration

Key settings in `archive_daily.py` CONFIG dict:
- `sources`: List of source identifiers to fetch
- `keywords`: Comma-separated filter terms
- `limit_per_source`: Max articles per source
- `repo_path`: Local repository path (default: `~/ai_news`)
- `auto_push`: Whether to auto-commit and push

### Output Format

Each article saved as `NN_Title_Slug.md` with front matter:
```markdown
# Title

- **Source**: arXiv | HackerNews | etc
- **URL**: https://...
- **Time**: YYYY-MM-DD
- **Heat**: (engagement metrics if available)

## Summary
{title}

## Content
{full extracted content}

## Links
- [Discussion]({hn_url})
```

## Dependencies

- Python 3.8+
- `newspaper3k` - Full content extraction
- `trafilatura` - Fallback content extraction
- `requests` - HTTP requests
- External: `~/.openclaw/skills/news-aggregator-skill/scripts/fetch_news.py`

## External Integration

This repo syncs with OpenClaw skill system:
- **Working directory**: `~/.openclaw/skills/ai-news-archive/`
- **Git backup**: `~/ai_news/skill/` (this repo)
- Uses `news-aggregator-skill` for base fetching functionality