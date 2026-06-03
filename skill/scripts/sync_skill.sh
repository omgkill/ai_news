#!/bin/bash
# Sync skill files to Git repo backup

SKILL_DIR=~/.openclaw/skills/ai-news-archive
REPO_DIR=~/ai_news/skill

# Copy skill files
cp -r "$SKILL_DIR"/* "$REPO_DIR"/ 2>/dev/null

# Git commit if changes
cd ~/ai_news
git add skill/
git diff-index --quiet HEAD -- skill/ || git commit -m "Sync skill files"
git push

echo "Skill synced to repo"