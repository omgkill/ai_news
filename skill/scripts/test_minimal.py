#!/usr/bin/env python3
"""Minimal test - just fetch titles and basic info, no deep content."""

import sys
import os
from datetime import datetime
from pathlib import Path

# Local module
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
import fetch_news

# Test fetching
print("Fetching from HackerNews (AI keywords)...", file=sys.stderr)
articles = fetch_news.fetch_hackernews(limit=5, keyword="AI")
print(f"Found {len(articles)} articles", file=sys.stderr)

for i, a in enumerate(articles, 1):
    print(f"{i}. {a['title'][:60]}")

# Test save to markdown
today = datetime.now().strftime("%Y-%m-%d")
repo_path = Path(os.path.expanduser("~/ai_news"))
day_dir = repo_path / today
day_dir.mkdir(parents=True, exist_ok=True)

for idx, article in enumerate(articles, 1):
    title = article.get("title", "Untitled")
    safe_name = "".join(c for c in title if c.isalnum() or c in " -_").strip().replace(" ", "_")[:80]
    filename = f"{idx:02d}_{safe_name}.md"
    filepath = day_dir / filename
    
    md = f"""# {title}

- **Source**: {article.get("source")}
- **URL**: {article.get("url")}
- **Time**: {article.get("time")}
- **Heat**: {article.get("heat")}

## Summary

{title}

## Content

*Content to be fetched separately*

## Links

"""
    if article.get("hn_url"):
        md += f"- [Discussion]({article['hn_url']})\n"
    
    with open(filepath, "w") as f:
        f.write(md)
    
    print(f"Saved: {filename}", file=sys.stderr)

print(f"\nDone! Files in {day_dir}", file=sys.stderr)