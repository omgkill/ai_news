#!/usr/bin/env python3
"""
AI News Archive - Daily Article Archiver

Fetches AI articles with clean paragraph formatting, saves as Markdown.
"""

import os
import sys
import subprocess
import re
from datetime import datetime
from pathlib import Path
import requests
from xml.etree import ElementTree as ET

# Add news-aggregator-skill to path
NEWS_SKILL_PATH = os.path.expanduser("~/.openclaw/skills/news-aggregator-skill/scripts")
sys.path.insert(0, NEWS_SKILL_PATH)
import fetch_news

# Try to import newspaper3k
try:
    from newspaper import Article
    HAS_NEWSPAPER = True
except ImportError:
    HAS_NEWSPAPER = False
    print("Warning: newspaper3k not installed", file=sys.stderr)

CONFIG = {
    "sources": ["ai_newsletters", "hackernews"],
    "keywords": "AI,LLM,GPT,Claude,Agent,RAG,DeepSeek",
    "limit_per_source": 5,
    "repo_path": os.path.expanduser("~/ai_news"),
    "auto_push": True,
    "max_content_length": 5000,
}

# Patterns to remove from content (subscription buttons, etc.)
REMOVE_PATTERNS = [
    r'^Subscribe\s*$',
    r'^Sign in\s*$',
    r'^Sign up\s*$',
    r'^Login\s*$',
    r'^Subscribe here.*$',
    r'^Please please subscribe.*$',
    r'^\s*Share\s*$',
    r'^\d+\s*$',  # Standalone numbers (like view counts)
    r'^\d+\s+\d+\s+\d+$',  # Numbers like "70 15 12"
    r'^Greetings from.*$',
    r'^…As always.*$',
]


def clean_content(content: str) -> str:
    """Remove subscription UI elements and format paragraphs."""
    if not content:
        return ""
    
    # Split into paragraphs
    paragraphs = content.split('\n')
    
    # Clean each paragraph
    cleaned = []
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        
        # Skip if matches remove pattern
        should_remove = False
        for pattern in REMOVE_PATTERNS:
            if re.match(pattern, p, re.IGNORECASE):
                should_remove = True
                break
        
        if not should_remove and len(p) > 10:  # Skip very short fragments
            cleaned.append(p)
    
    # Rejoin with proper spacing
    return '\n\n'.join(cleaned)[:CONFIG["max_content_length"]]


def fetch_arxiv_papers(limit: int = 5) -> list:
    """Fetch recent AI papers from arXiv API."""
    query = "cat:cs.AI+OR+cat:cs.LG+OR+cat:cs.CL"
    api_url = f"http://export.arxiv.org/api/query?search_query={query}&sortBy=submittedDate&sortOrder=descending&max_results={limit*2}"
    
    print("Fetching from arXiv API...", file=sys.stderr)
    
    try:
        response = requests.get(api_url, timeout=15)
        root = ET.fromstring(response.content)
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        entries = root.findall('atom:entry', ns)
        
        articles = []
        for entry in entries:
            title_elem = entry.find('atom:title', ns)
            summary_elem = entry.find('atom:summary', ns)
            link_elem = entry.find('atom:link[@rel="alternate"]', ns)
            author_elems = entry.findall('atom:author', ns)
            published_elem = entry.find('atom:published', ns)
            
            if title_elem is None or summary_elem is None or link_elem is None:
                continue
            
            title = title_elem.text.strip()
            summary = summary_elem.text.strip()
            url = link_elem.get('href', '')
            
            # Filter by AI keywords
            ai_keywords = ["AI", "LLM", "machine learning", "deep learning", "neural network", "transformer", "GPT", "language model"]
            if not any(kw.lower() in title.lower() or kw.lower() in summary.lower() for kw in ai_keywords):
                continue
            
            # Format authors
            authors = [a.find('atom:name', ns).text for a in author_elems[:5] if a.find('atom:name', ns) is not None]
            author_str = ', '.join(authors)
            if len(author_elems) > 5:
                author_str += f" et al."
            
            # Format date
            time_str = "Unknown"
            if published_elem is not None:
                try:
                    pub_date = datetime.fromisoformat(published_elem.text.replace('Z', '+00:00'))
                    time_str = pub_date.strftime('%Y-%m-%d')
                except:
                    pass
            
            # Format abstract with proper paragraphs
            content = f"**Authors**: {author_str}\n\n## Abstract\n\n{summary.strip()}"
            
            articles.append({
                "source": "arXiv",
                "title": title,
                "url": url,
                "time": time_str,
                "heat": "",
                "content": content
            })
            
            if len(articles) >= limit:
                break
        
        print(f"  Found {len(articles)} papers from arXiv", file=sys.stderr)
        return articles
        
    except Exception as e:
        print(f"  arXiv fetch failed: {e}", file=sys.stderr)
        return []


def fetch_content_newspaper(url: str) -> str:
    """Fetch content using newspaper3k with proper paragraph formatting."""
    if not url or not url.startswith('http'):
        return ""
    
    if HAS_NEWSPAPER:
        try:
            a = Article(url)
            a.download()
            a.parse()
            return clean_content(a.text)
        except Exception as e:
            print(f"    newspaper3k failed: {e}", file=sys.stderr)
    
    # Fallback to trafilatura or basic extraction
    try:
        import trafilatura
        downloaded = trafilatura.fetch_url(url, timeout=10)
        if downloaded:
            content = trafilatura.extract(downloaded, include_comments=False, favor_precision=True)
            if content:
                return clean_content(content)
    except:
        pass
    
    # Final fallback
    return fetch_news.fetch_url_content(url)[:CONFIG["max_content_length"]]


def fetch_articles():
    """Fetch articles from all sources."""
    all_articles = []
    
    # ArXiv papers (content pre-populated)
    arxiv_articles = fetch_arxiv_papers(CONFIG["limit_per_source"])
    all_articles.extend(arxiv_articles)
    
    # Other sources
    fetcher_map = {
        "ai_newsletters": fetch_news.fetch_ai_newsletters,
        "hackernews": fetch_news.fetch_hackernews,
    }
    
    for source in CONFIG["sources"]:
        print(f"Fetching from {source}...", file=sys.stderr)
        try:
            fetcher = fetcher_map.get(source)
            if fetcher:
                articles = fetcher(limit=CONFIG["limit_per_source"], keyword=CONFIG["keywords"])
                all_articles.extend(articles)
                print(f"  Found {len(articles)} from {source}", file=sys.stderr)
        except Exception as e:
            print(f"  Error: {e}", file=sys.stderr)
    
    return all_articles


def enrich_articles(articles):
    """Fetch full content for articles."""
    print(f"\nEnriching content...", file=sys.stderr)
    
    for i, article in enumerate(articles, 1):
        if article.get("content"):  # Skip if already has content (arXiv)
            continue
        
        url = article.get("url", "")
        title = article.get("title", "Unknown")[:50]
        print(f"  [{i}/{len(articles)}] {title}...", file=sys.stderr)
        
        content = fetch_content_newspaper(url)
        article["content"] = content if content else "*Content unavailable*"
    
    return articles


def sanitize_filename(title: str) -> str:
    """Create safe filename."""
    # Remove CDATA prefix if present
    title = title.replace('<![CDATA[', '').replace(']]>', '')
    safe = "".join(c for c in title if c.isalnum() or c in " -_")
    safe = safe.strip().replace(" ", "_")[:80]
    return safe


def create_markdown(article: dict, index: int) -> str:
    """Create markdown content."""
    title = article.get("title", "Untitled")
    # Remove CDATA from title
    title = title.replace('<![CDATA[', '').replace(']]>', '')
    
    source = article.get("source", "Unknown")
    url = article.get("url", "")
    time_str = article.get("time", "Unknown")
    heat = article.get("heat", "")
    content = article.get("content", "*Content unavailable*")
    hn_url = article.get("hn_url", "")
    
    md = f"""# {title}

- **Source**: {source}
- **URL**: {url}
- **Time**: {time_str}
- **Heat**: {heat}

## Summary

{title}

## Content

{content}

## Links

"""
    if hn_url:
        md += f"- [Discussion]({hn_url})\n"
    
    return md


def save_articles(articles):
    """Save to markdown files."""
    today = datetime.now().strftime("%Y-%m-%d")
    repo_path = Path(CONFIG["repo_path"])
    day_dir = repo_path / today
    day_dir.mkdir(parents=True, exist_ok=True)
    
    saved = 0
    for idx, article in enumerate(articles, 1):
        title = article.get("title", "Untitled")
        filename = f"{idx:02d}_{sanitize_filename(title)}.md"
        filepath = day_dir / filename
        
        md_content = create_markdown(article, idx)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(md_content)
        
        print(f"Saved: {filename}", file=sys.stderr)
        saved += 1
    
    return saved, day_dir


def git_commit_and_push():
    """Commit and push to GitHub."""
    repo_path = Path(CONFIG["repo_path"])
    today = datetime.now().strftime("%Y-%m-%d")
    
    result = subprocess.run(["git", "status", "--porcelain"], cwd=repo_path, capture_output=True, text=True)
    
    if not result.stdout.strip():
        print("No changes to commit.", file=sys.stderr)
        return
    
    subprocess.run(["git", "add", "."], cwd=repo_path, check=True)
    subprocess.run(["git", "commit", "-m", f"AI News - {today}"], cwd=repo_path, check=True)
    
    print("Pushing to GitHub...", file=sys.stderr)
    result = subprocess.run(["git", "push"], cwd=repo_path, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"Successfully pushed to GitHub.", file=sys.stderr)
    else:
        print(f"Push failed: {result.stderr}", file=sys.stderr)


def main():
    print("=" * 50, file=sys.stderr)
    print("AI News Archive", file=sys.stderr)
    print(f"Time: {datetime.now().isoformat()}", file=sys.stderr)
    print("=" * 50, file=sys.stderr)
    
    # Fetch
    articles = fetch_articles()
    print(f"\nTotal: {len(articles)} articles", file=sys.stderr)
    
    if not articles:
        print("No articles found.", file=sys.stderr)
        return
    
    # Enrich content
    articles = enrich_articles(articles)
    
    # Save
    saved, day_dir = save_articles(articles)
    print(f"\nSaved {saved} files to {day_dir}", file=sys.stderr)
    
    # Push
    if CONFIG["auto_push"]:
        try:
            git_commit_and_push()
        except Exception as e:
            print(f"Git failed: {e}", file=sys.stderr)
    
    print("\nDone.", file=sys.stderr)


if __name__ == "__main__":
    main()