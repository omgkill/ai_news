# AI Can now control your desktop

- **Source**: Hacker News
- **URL**: https://clawdcursor.com
- **Time**: Today
- **Heat**: 2 points

## Summary

AI Can now control your desktop

## Content

v1.0.1 — latest stable v1.0.1 — latest stable A cursor and a keyboard

for any AI agent Any model. Any app. One MCP entry. Local-only. 6 compact tools, single safety chokepoint, no telemetry. Cheap paths first — accessibility before pixels, vision only as a last resort. View on GitHub — Quick Start

6 Toolbox — compound tools (recommended) 94 Tools — granular (compat / debug) 3 Operating Systems

Two ways to use it Run it yourself, or hand it to your agent. Test from the CLI Plain English in, actions out. clawdcursor doctor clawdcursor agent Wire it into your agent One MCP entry, desktop control appears as native tools. Claude Code Cursor Windsurf OpenClaw Zed

Pick a mode How will your AI talk to it? Same tools, three entry shapes. Pick once during install. clawdcursor mcp — recommended AI lives in your editor (Claude Code, Cursor, Windsurf, Zed). Editor spawns clawdcursor on demand over stdio. No daemon, no port. { "mcpServers": { "clawdcursor": { "command": "clawdcursor", "args": ["mcp", "--compact"] } } } 6 / 94 Compact / Granular tools stdio Transport clawdcursor agent — autonomous daemon clawdcursor brings its own LLM brain (configured via doctor ). For unattended runs, scheduled tasks, multi-process orchestration. Run clawdcursor doctor · pick a provider Run clawdcursor agent POST tasks to 127.0.0.1:3847/mcp :3847 HTTP MCP 13+ Providers clawdcursor agent --no-llm — BYO brain Your agent already has a brain — you just want HTTP tools. Same daemon, no built-in agent loop. Run clawdcursor agent --no-llm 94 tools on :3847/mcp Stateless — no session init needed 94 Granular tools (compat) any HTTP client

How it works Cheap paths first. A11y tree before pixels. Vision only when needed. 1 Accessibility Zero pixels Read the a11y tree, act on element names. No screenshot, no vision LLM. → 2 Escalate as needed Cheapest rung that works OCR when the tree is sparse, screenshot when you need pixels, vision only for canvas UIs. → 3 Safety Single chokepoint Every tool call gates through one safety layer. Destructive actions need confirmation. 🎯 Toolbox — 6 compound tools The recommended surface — computer , accessibility , window , system , browser , task . ~12× smaller catalog than the granular Tools surface. 🧩 One adapter per OS Windows, macOS, Linux behind a single interface. Linux covers X11 and Wayland.

Features Any OS. Any model. 🍎 macOS TCC-safe. clawdcursor grant handles Accessibility + Screen Recording. 🪟 Windows Native UIA + Windows.Media.Ocr. x64 and ARM64. 🐧 Linux X11 and Wayland. AT-SPI for a11y, Tesseract for OCR. 🖱️ Smart tools Click by name, type by label, read screen. A11y first, OCR as fallback. ⌨️ Shortcuts engine Platform-aware key combos — Cmd on macOS, Ctrl elsewhere. No LLM cost. 📦 batch — one round-trip Collapse N deterministic tool calls into a single guarded, safety-gated batch. N calls → 1.

CLI Every command › The CLI is for humans diagnosing an install. Agents connect via MCP. # Install & setup clawdcursor consent # one-time desktop-control authorization clawdcursor grant # macOS Accessibility + Screen Recording prompts clawdcursor doctor # verify permissions, configure AI provider clawdcursor status # readiness check (consent, permissions, AI config) # Run clawdcursor mcp # stdio MCP server for editor hosts clawdcursor mcp --compact # same, with 6 compound tools (recommended) clawdcursor agent # HTTP MCP daemon at :3847/mcp, optional built-in LLM clawdcursor agent --no-llm # tool surface only — your agent brings its own brain clawdcursor stop # stop every running mode clawdcursor uninstall # remove all clawdcursor config and data

## Links

- [Discussion](https://news.ycombinator.com/item?id=48430028)
