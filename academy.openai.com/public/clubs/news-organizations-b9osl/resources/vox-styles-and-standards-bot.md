<!-- source: https://academy.openai.com/public/clubs/news-organizations-b9osl/resources/vox-styles-and-standards-bot -->

[News Organizations](/en/public/clubs/news-organizations-b9osl/overview)

[navigation.content](/en/public/clubs/news-organizations-b9osl/content)

Article

July 15, 2026 · Last updated on July 13, 2026

# Vox gives every journalist a first stop for style and standards questions

![Vox gives every journalist a first stop for style and standards questions](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/Screenshot-2026-07-13-at-3-16-33-PM-3cdd2001-8aa4-4a31-a980-c19ebf3ff0b0-1783970340386.jpeg?fit=scale-down&width=1200)

# News

# News Organizations

# Use Cases

## Vox Style & Standards Bot

![Vox gives every journalist a first stop for style and standards questions](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/Screenshot-2026-07-13-at-3-16-33-PM-3cdd2001-8aa4-4a31-a980-c19ebf3ff0b0-1783970340386.jpeg?fit=scale-down&width=1200)

In a newsroom, style questions rarely arrive when everyone has time to spare. A reporter may be filing on deadline. An editor may be checking a headline. A producer may need to know whether a term is acceptable, whether a date should be abbreviated, or how to handle sensitive language in a story that is still moving.

At Vox, those answers live in detailed guidance built by the style and standards team: the Vox Style Guide, the Vox Standards Guide, topic-specific guidance for coverage areas such as elections, and violence, workflow and corrections documentation, and AP style as a fallback when Vox does not have its own rule.

The guidance is comprehensive by design. It also means the answer to a simple question can sit across long documents, Slack threads, and institutional memory. Before Vox built its Style & Standards Bot, reporters and editors often asked individual copy editors for help rather than searching every source themselves. For a small style and standards team responsible for copy editing and fact-checking across the newsroom, those repeat questions added up.

So the team built a first stop: a Custom GPT in ChatGPT Enterprise that helps newsroom staff ask style and standards questions conversationally and get direct, source-aware answers in the flow of work.

![](https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/some-file-2cde72ab-f1d3-4292-b09e-25ba813d7af9-1783970236412.png)

﻿

﻿

The bot is not designed to replace copy editors, fact-checkers, or editorial judgment. Stories still go through Vox's normal copy editing and fact-checking processes. Instead, the bot gives reporters, editors, producers, copy editors, fact-checkers, and audience team members a faster way to navigate existing guidance before they need to ask a human in Slack.

﻿

## How the bot works

Vox's Style & Standards Bot is a searchable, conversational version of the newsroom's internal guidance. Staff can ask about grammar, punctuation, headline and dek formatting, sensitive language, corrections workflows, fact-checking process, or the difference between Vox style and AP style.

![](https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/some-file-e35408c7-2a84-47ba-9cad-1b4a011f1454-1783970236487.png)

﻿

﻿

The bot's instructions are intentionally specific. It prioritizes Vox's internal documentation first. If Vox guidance does not address the question, it can fall back to AP style. When it gives an answer, it should make clear whether the guidance comes from Vox, AP, or another approved source. And when the answer is not in the source material, it should say so rather than invent a rule.

That boundary is central to the use case. The bot is meant to draw only from existing available guidance, not improvise new standards. If a question requires more nuance, or if the bot cannot find a clear answer, it directs the user back to the style and standards team.

Vox also set clear limits around what the bot should not do. It does not copy-edit or fact-check full stories. If someone pastes in a long passage or asks for a full edit, the bot points them back to the style and standards team and offers to answer a narrower style question instead. The result is a tool that can be helpful without pulling people away from the newsroom's existing checks and balances.

![](https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/some-file-5d4677c1-63d7-4012-9286-6cc0e1ef7b8d-1783970236445.png)

﻿

﻿

## Why it fits the newsroom

The project started from a practical newsroom need, not a product roadmap. During an AI working group, a reporter suggested creating a GPT for the style guide. The style and standards editor, who leads the team responsible for maintaining Vox's guidance and overseeing copy editing and fact-checking, built the bot herself in ChatGPT Enterprise.

That mattered. Because the bot was created by the team closest to the guidance, it could be shaped around the way Vox actually makes editorial decisions. It also did not require product resources or compete with other newsroom priorities. The team could start with the documentation it already trusted, test the bot against common questions, and refine the instructions as copy editors and fact-checkers found places where the bot needed tighter boundaries.

Before launch, Vox introduced the bot to the style and standards team for testing. Copy editors and fact-checkers gave feedback, which led to adjustments to the backend instructions. Once the team was ready, the bot was introduced to the broader newsroom in an all-hands meeting with a demonstration of practical use cases.

The rollout message was deliberately clear: use the bot for questions, not full edits. The Style Guide itself encourages people to try the bot, while emphasizing that it "doesn't replace judgment" and that writers should still consult editors when needed.

## What changed

Today, the bot is used across the newsroom by reporters, editors, copy editors, producers, and audience team members.

Common questions are the everyday ones that slow people down in the middle of real work: Is this term okay? How should this headline be formatted? What is the rule for dates? What does Vox prefer for language around identity, violence, or misinformation? What happens when a story needs to be fact-checked?

Those questions still matter. They are part of how a newsroom protects accuracy, consistency, clarity, and reader trust. The difference is that ChatGPT helps make the first step faster. Instead of spending time searching through documentation, staff can start with the bot, see the relevant guidance, and escalate to the style and standards team when judgment or nuance is needed. It saves time for copy editors who might be answering the same style questions repeatedly, and saves time for journalists who can find answers quickly without needing to wade through various documents.

For the style and standards team, that means less time spent fielding repeated questions and more time for the higher-value work only humans can do: editing stories, checking facts, maintaining standards, and making judgment calls on sensitive coverage.

## Lessons for other publishers

Vox's main lesson is simple: be specific about both the job and the limits.

A useful internal GPT needs clear source boundaries. It should know which documents to prioritize, when to use fallback guidance, and how to attribute the answer. It also needs clear refusal behavior when the answer is not documented or when the user is asking it to do something outside its role.

The team also recommends checking the bot regularly. The style and standards team tests common questions to make sure the answers remain accurate, and corrects mistakes quickly when they appear.

For other publishers, the pattern is a practical one. Start with a recurring question set. Use source material your newsroom already trusts. Build the bot around an existing workflow. Make the handoff to humans explicit. Then keep improving the instructions as people use it.

In Vox's case, the Style & Standards Bot works because it solves a specific problem in a specific workflow. It does not ask the newsroom to change how editorial judgment works. It helps people find the guidance that supports that judgment faster.

## Popular

[49:00](/en/public/clubs/news-organizations-b9osl/videos/ai-essentials-for-journalists-2025-12-12)

Video

[AI Essentials for Journalists](/en/public/clubs/news-organizations-b9osl/videos/ai-essentials-for-journalists-2025-12-12)

[35:00](/en/public/clubs/news-organizations-b9osl/videos/on-the-air-with-ai-behind-the-scenes-at-tbpn-2026-05-22)

Video

[On the air with AI: Behind the scenes at TBPN](/en/public/clubs/news-organizations-b9osl/videos/on-the-air-with-ai-behind-the-scenes-at-tbpn-2026-05-22)

By Evan Hirsch

Resource

[How VG Built an AI “Buddy” for Journalists](/en/public/clubs/news-organizations-b9osl/resources/how-vg-built-an-ai-buddy-for-journalists)

Dive in

## Related

[48:00](/en/public/clubs/news-organizations-b9osl/videos/using-chatgpt-for-prospecting-and-donor-research)

Video

[Using ChatGPT for prospecting and donor research](/en/public/clubs/news-organizations-b9osl/videos/using-chatgpt-for-prospecting-and-donor-research)

Dec 15th, 2025 • Views 279

[3:40](/en/public/clubs/news-organizations-b9osl/videos/upskill-with-skills-2026-07-07)

Video

[Upskill With Skills](/en/public/clubs/news-organizations-b9osl/videos/upskill-with-skills-2026-07-07)

By Evan Hirsch • Jul 10th, 2026 • Views 167

[2:40](/en/public/clubs/news-organizations-b9osl/videos/spot-the-fake-2026-07-14)

Video

[Spot The Fake](/en/public/clubs/news-organizations-b9osl/videos/spot-the-fake-2026-07-14)

By Evan Hirsch • Jul 15th, 2026 • Views 76

[4:20](/en/public/clubs/news-organizations-b9osl/videos/skills-vs-agents-2026-07-13)

Video

[Skills vs. Agents](/en/public/clubs/news-organizations-b9osl/videos/skills-vs-agents-2026-07-13)

By Evan Hirsch • Jul 13th, 2026 • Views 213

[48:00](/en/public/clubs/news-organizations-b9osl/videos/using-chatgpt-for-prospecting-and-donor-research)

Video

[Using ChatGPT for prospecting and donor research](/en/public/clubs/news-organizations-b9osl/videos/using-chatgpt-for-prospecting-and-donor-research)

Dec 15th, 2025 • Views 279

[2:40](/en/public/clubs/news-organizations-b9osl/videos/spot-the-fake-2026-07-14)

Video

[Spot The Fake](/en/public/clubs/news-organizations-b9osl/videos/spot-the-fake-2026-07-14)

By Evan Hirsch • Jul 15th, 2026 • Views 76

[4:20](/en/public/clubs/news-organizations-b9osl/videos/skills-vs-agents-2026-07-13)

Video

[Skills vs. Agents](/en/public/clubs/news-organizations-b9osl/videos/skills-vs-agents-2026-07-13)

By Evan Hirsch • Jul 13th, 2026 • Views 213

[3:40](/en/public/clubs/news-organizations-b9osl/videos/upskill-with-skills-2026-07-07)

Video

[Upskill With Skills](/en/public/clubs/news-organizations-b9osl/videos/upskill-with-skills-2026-07-07)

By Evan Hirsch • Jul 10th, 2026 • Views 167
