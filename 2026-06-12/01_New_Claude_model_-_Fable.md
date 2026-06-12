# New Claude model - Fable

- **Source**: Ben's Bites
- **URL**: https://www.bensbites.com/p/new-claude-model-fable
- **Time**: Thu, 11 Jun 2026 13:03:20 GMT
- **Heat**: 

## Summary

New Claude model - Fable

## Content

Like a lot of others, I’m trying Fable. But I don’t think I’ve given it really hard tasks for me to feel the big step change people are claiming. Although as I’m working on visual, interactive essays for my reference manual, I’ve been testing one-shot generations on all sorts of topics to play with my kids; how to play the piano, how tetris works, how a volcano works. They’re loving bashing away at my keyboard to see the components come alive.

It’s less chatty than Opus. I use agents as a back-and-forth, so I need some chattiness, GPT models are very to the point, Claude models are usually more verbose. So I think Fable’s a bit of a sweet spot for me, because as of now I still prefer the ‘vibe’ of how Claude models think with me.

It’s slow. Speed is a huge thing for me because I can’t actively run many agents at once, my ADHD context switching is already bad enough. But I need the speed. So then I look to change from High or XHigh reasoning to lower levels but it feels wrong to pick less intelligence. Even though I know it’s probably wasting tokens.

Composer 2.5 Fast from Cursor is the fastest model I’ve tried and I really enjoyed using it in Pi, and it’s shattered the glass for me, GPT 5.5 has too to be honest. They’re quick so I can chew through a bunch of work quickly.

Ever a game of toss-up between price, speed and vibe.

I’m sure GPT 5.6 or 6 is just around the corner, and I imagine OpenAI are really trying to make sure the vibe is on par with Claude models if they want to keep the Codex hype going.

Ben’s Bites is brought to you by Plaid

Over half of Americans used AI to manage their finances in the past 12 months. And their expectations for financial products have never been higher. Plaid's latest report, The State of Intelligent Finance, breaks down what consumers expect from AI and what that means for your team. Get the report.

Claude Code can have nested subagents now - each subagent can spawn even more subagents. Currently up to a depth of 5 layers.

The model selector in ChatGPT has been updated to a) show all GPT-5 generation models and b) thinking levels are simplified to Instant, Medium, High, Extra High and Pro - just like how it is in Codex.

Missions are now available on Factory Desktop.

Skribe - Local first markdown writing app with an AI review partner.

Little python harness to run evals on your skills - is the skill improving or hurting the model’s performance?

pr.video by Mainframe - turn any GitHub PR into a narrated video walkthrough to review changes (without needing the code diff).

New essay from Dario Amodei on policymaking to keep up with the pace of AI development. It’s a good read but has “trust me bro” vibes at many places.

Supermemory is now available locally to host yourself.

DiffusionGemma - new open-weights model from Google that uses a different architecture (diffusion instead of transformers) to gain a 3-5x speedup with roughly similar performance.

Agents can now sign up on Firecrawl.

- by Keshav

I’m building a speech-to-text app that’s entirely local (kinda like Wispr flow, Monologue, Superwhisper, etc.) but no data gets sent to their servers. Part of it stemmed from wanting to play with local models, and part of it was guilt of paying for a similar tool that I don’t use much.

I’m calling the app “Option AFK”, and here’s how I built it in 3-4 days spread out over the past few weeks:

Asked Opus 4.7 to write a simple Python script to get Nvidia’s Parakeet 0.6B working on my M3 Air. I tested it in the browser, and the accuracy/speed were better than what I expected. Used Codex’s Computer Use to do a screen-by-screen audit of the tool I was paying for and document all the features that it has with screenshots. I was able to do this on the $20 plan in a single session (hitting the 5-hour limit only once). Then started building the MacOS app with Opus 4.8 (using the audit as a reference). While building this, Opus 4.8 selected an SDK I had no idea existed to wire up things like splitting long voice notes into chunks and speeding the model processing.

Here’s that SDK:

fluidaudio - run transcription and TTS models on MacOS locally.

I got a working version of the app yesterday with Fable 5, and I’m using it on my device already. Here’s how it looks:

It also supports uploading voice notes (even the longer ones) as a file and getting them transcribed at no additional cost.

I’m planning to release this app once I get the Apple Developer Program sign-up done. Would you want to use it?

Share Ben's Bites

Find me on X, Linkedin, or YouTube

Read about me and Ben’s Bites

📷 thumbnail via @_nicolealonso

## Links

