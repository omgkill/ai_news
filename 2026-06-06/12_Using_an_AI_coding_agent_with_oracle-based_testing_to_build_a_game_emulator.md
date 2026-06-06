# Using an AI coding agent with oracle-based testing to build a game emulator

- **Source**: Hacker News
- **URL**: https://keanw.com/2026/03/a-diary-of-an-agentic-retro-gamer-part-1.html
- **Time**: Today
- **Heat**: 1 points

## Summary

Using an AI coding agent with oracle-based testing to build a game emulator

## Content

This is the first part of a guest series by Patrick Nadeau, a member of the Research Engineering team based in Canada. I mentioned it in this recent post. Patrick is a great writer and a very experienced developer who gives a personal, nuanced perspective on his explorations of using agentic coding tools to solve a really interesting programming challenge.

When I was a kid, there were only two computing devices in the house: the Intellivision game console and my Apple II computer. Decades later, when I wrote code with a coding agent for the first time, those were the machines I kept coming back to.

The first time I saw the insides of the Intellivision was the time my sister dropped her bracelet through one of the vent holes and my dad had to open it up to get it working again. I opened up my Apple II too, tracing the lines from the CPU to the RAM and ROMs. Halfway between toy and tool, those machines loomed large in my imagination, and before long I'd graduated from BASIC to assembly and spent long hours poring over programming manuals.

A friend of my dad's, who ran an electronics shop, once asked me to design a Greek character set for the Apple II. I traced the letters on graph paper, encoded them into a binary file, and brought it downtown to his shop. We burned the character set onto a ROM and popped the new chip into the machine. I still remember him typing the letters in one by one, and laughing in delight as each character appeared on the screen.

I still have the graph paper designs, but most of my earliest work is gone. Recently, I had the chance to capture another first: the first time a computer and I wrote a program together. Feeling that something was coming full circle, I kept careful notes.

I still like to play those old Intellivision games around the holidays. Not on the console — that was thrown out years ago — but on an emulator. The problem was that the emulator broke on every OS update, requiring ugly hacks to get it working again.

Like any programmer, I decided to solve this minor inconvenience with a huge programming digression: I would code my own emulator from scratch. I gave myself until next Christmas.

I started with the CPU, writing the instruction decoder and core by hand. To validate the new code, I extracted the CPU implementation from the emulator I'd been using, jzintv. This allowed my unit tests to compare each instruction's effects—on registers, flags, RAM, and cycle counts—against the old but tried-and-true version.

This is called a "test oracle": a trusted reference you can compare your new work against. Building it took a lot of effort, but it turned out to be the most important design decision in the whole project.

By mid-March, working by myself, I had a mostly working CP-1610 CPU core, but no real machine around it yet: no bus, no video, no sound. It would be a long time before I could play a game on it.

Around the same time, work was encouraging us to start using coding agents. I was skeptical — openly reluctant. I asked the AI to write its own version of a parser I had written. Without guidance it produced workaday code with two major flaws.

When I showed the AI my version, it had to admit that mine was "better in every dimension that matters for this use case." I wrote gloating Slack posts about it: the AI had missed my imaginative leaps! Still, I wanted a working emulator, and I had a solid test oracle, so I tried again, this time guiding the AI as it worked.

By hour 5, I had the first pixels on screen, and saw those familiar colour test bars. By hour 10, the rendering pipeline was in place. At hour 21, the first cartridge ROM booted. By hour 28, all 204 ROMs in my collection were booting. By hour 32, we had movement on screen. We were almost there. By hour 36, we had a complete Intellivision system up and running, and I was playing through a controller with sound.

Over the next few days, we added features that would have been practically impossible with the old emulator.

I took a second leap: what if we added a debugger port to the emulator, a way for the AI to peer into the running machine, inspect its internal state, and control it during live play?

I watched, delighted, as the AI controlled the game from the inside. I even called my wife over and typed, "Move the ship left," and it did.

I asked the AI to find the spot in the code where the ship gets hit, and we added code to make the controller buzz when you get killed. Totally bonkers.

By the end, I was exhausted. Five days of watching over the AI's shoulder, making sure to keep it on track, left me almost as tired as if I'd written it myself.

And once the exhilaration wore off, my discomfort returned. It bugs me that coding agents can do this only because they've captured — some would say appropriated — the work of millions of programmers who learned the hard way, and then shared their code freely for others to learn from.

But my emulator would not have been possible without the years of work Joe Zbciak put into developing jzintv. Wasn't the test oracle also an automated way to extract his hard-won knowledge?

What surprised me was how familiar the process still felt. Sure, the AI wrote most of the code, but when we got lost, it felt exactly the same: the answer still had to come from me, and I still had to want it badly enough.

I suppose I finally got inside those chips I saw when my dad cracked open that console back then. I still can't help feeling that I reclaimed something and lost something at the same time.

I hope you enjoyed reading this as much as I did. In upcoming posts we'll dig more deeply into Patrick's journey.

## Links

- [Discussion](https://news.ycombinator.com/item?id=48419824)
