#!/usr/bin/env python3
"""
Fetch news from various sources.
"""

import requests
import re
from datetime import datetime
from xml.etree import ElementTree as ET


def fetch_url_content(url: str, timeout: int = 10) -> str:
    """Basic URL content fetch with text extraction."""
    if not url or not url.startswith('http'):
        return ""

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; NewsBot/1.0)'
        }
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()

        # Basic text extraction
        text = response.text

        # Remove HTML tags
        text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL|re.IGNORECASE)
        text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL|re.IGNORECASE)
        text = re.sub(r'<[^>]+>', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()

        return text[:5000] if text else ""

    except Exception as e:
        print(f"Fetch failed: {e}", file=__import__('sys').stderr)
        return ""


def fetch_hackernews(limit: int = 5, keyword: str = "") -> list:
    """Fetch AI-related stories from Hacker News."""

    # Get top stories
    api_url = "https://hacker-news.firebaseio.com/v0/topstories.json"

    try:
        response = requests.get(api_url, timeout=10)
        story_ids = response.json()[:100]  # Check top 100

        articles = []
        keywords = keyword.split(',') if keyword else ['AI']

        for story_id in story_ids:
            if len(articles) >= limit:
                break

            story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
            story_resp = requests.get(story_url, timeout=10)
            story = story_resp.json()

            if not story or not story.get('title'):
                continue

            title = story.get('title', '')
            url = story.get('url', '')
            score = story.get('score', 0)
            time_ts = story.get('time', 0)

            # Filter by keyword
            if not any(kw.lower() in title.lower() for kw in keywords):
                continue

            # Use HN discussion page if no URL
            if not url:
                url = f"https://news.ycombinator.com/item?id={story_id}"

            time_str = datetime.fromtimestamp(time_ts).strftime('%Y-%m-%d') if time_ts else "Unknown"

            articles.append({
                'source': 'HackerNews',
                'title': title,
                'url': url,
                'time': time_str,
                'heat': str(score),
                'hn_url': f"https://news.ycombinator.com/item?id={story_id}",
                'content': ''
            })

        print(f"Found {len(articles)} from HackerNews", file=__import__('sys').stderr)
        return articles

    except Exception as e:
        print(f"HackerNews fetch failed: {e}", file=__import__('sys').stderr)
        return []


def fetch_ai_newsletters(limit: int = 5, keyword: str = "") -> list:
    """Fetch from AI newsletter RSS feeds."""

    rss_feeds = [
        "https://newsletter.physna.com/feed",
        "https://artificialintelligence-news.com/feed",
        "https://www.artificialintelligence-news.com/feed/",
    ]

    articles = []
    keywords = keyword.split(',') if keyword else ['AI']

    for feed_url in rss_feeds:
        if len(articles) >= limit * 2:
            break

        try:
            response = requests.get(feed_url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
            root = ET.fromstring(response.content)

            items = root.findall('.//item') or root.findall('.//{http://www.w3.org/2005/Atom}entry')

            for item in items:
                if len(articles) >= limit * 2:
                    break

                # Extract fields (RSS 2.0 format)
                title_elem = item.find('title')
                link_elem = item.find('link')
                desc_elem = item.find('description')

                if title_elem is None:
                    continue

                title = title_elem.text or ''
                url = link_elem.text if link_elem else ''

                # Filter by keyword
                if not any(kw.lower() in title.lower() for kw in keywords):
                    continue

                articles.append({
                    'source': 'AI Newsletter',
                    'title': title,
                    'url': url,
                    'time': datetime.now().strftime('%Y-%m-%d'),
                    'heat': '',
                    'content': ''
                })

        except Exception as e:
            print(f"Feed {feed_url} failed: {e}", file=__import__('sys').stderr)
            continue

    # Deduplicate by title
    seen = set()
    unique = []
    for a in articles:
        if a['title'] not in seen:
            seen.add(a['title'])
            unique.append(a)

    print(f"Found {len(unique[:limit])} from AI Newsletters", file=__import__('sys').stderr)
    return unique[:limit]


if __name__ == "__main__":
    # Test
    print("Testing HackerNews...")
    hn = fetch_hackernews(3, "AI")
    for a in hn:
        print(f"  - {a['title']}")

    print("\nTesting AI Newsletters...")
    nl = fetch_ai_newsletters(3, "AI")
    for a in nl:
        print(f"  - {a['title']}")