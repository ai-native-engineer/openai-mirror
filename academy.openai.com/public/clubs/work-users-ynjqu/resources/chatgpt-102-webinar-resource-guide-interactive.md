<!-- source: https://academy.openai.com/public/clubs/work-users-ynjqu/resources/chatgpt-102-webinar-resource-guide-interactive -->

[Work Users](/en/public/clubs/work-users-ynjqu/overview)

[navigation.content](/en/public/clubs/work-users-ynjqu/content)

Webinar

February 25, 2026 · Last updated on May 29, 2026

# ChatGPT 102: Webinar Resource Guide

![ChatGPT 102: Webinar Resource Guide](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/102resourceguide-0f104dc6-1b3f-4ab3-9501-f65f0a258126-1772061282894.jpeg?fit=scale-down&width=1200)

# Workplace & Business

# Use Cases

## Follow along with our webinar ChatGPT 102: Leveraging AI to do your best work

![Juliann Igo](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/1722019004102-4c419576-e710-4bb4-91fb-7208ae0552b0-1746650892941.jpeg?fit=scale-down&width=60)

Juliann Igo

![ChatGPT 102: Webinar Resource Guide](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/102resourceguide-0f104dc6-1b3f-4ab3-9501-f65f0a258126-1772061282894.jpeg?fit=scale-down&width=1200)

Use this guide to follow along with the **ChatGPT 102 Webinar: Leveraging AI to do your best work**. Please note that some prompts require a file upload - you can find all the sample files on this page. *If you’re viewing on-demand, you can use any file you have access to to practice the exercise.*

**Other resources to bookmark**

* ﻿[OpenAI Help Center](https://help.openai.com/en): Technical documentation for how ChatGPT works

* ﻿[OpenAI Academy for Work](https://academy.openai.com/home/clubs/work-users-ynjqu/overview?linkMenu=Users) **:** Resources to learn how to use ChatGPT most effectively for your role.

* ﻿[Use Cases for Work GPT:](https://chatgpt.com/g/g-h5aUtVu0G-chatgpt-use-cases-for-work?model=gpt-4o) GPT built by the OpenAI team to help you brainstorm use cases for your role.

* ﻿[cookbook.openai.com](http://cookbook.openai.com): Developer-focused resources

# Follow along with the webinar:

## **Learn:** ChatGPT 101 recap + customization options (1:07-4:42)

### **Key ideas**

* The key parts of the interface to explore now are the tools menu (the + on your chat window) and the left sidebar with your chat history

* You have some personalization options by clicking on your name at the bottom of your chat window, and clicking **Personalization**

* You can add facts to your ChatGPT memory within a chat and manage your memories from your personal settings

**Go deeper →** [**Customizing ChatGPT**](https://academy.openai.com/home/clubs/work-users-ynjqu/resources/customizing-chatgpt)﻿

## **Demo:** Deep research (4:42-7:20)

### **Key ideas**

* Deep research is an agentic search capability designed for longer, multi-step research on the internet

* You’ll notice that ChatGPT will ask for more clarification to help guide its research most effectively. Remember that the more guidelines, context, and constraints you give it, the more relevant its output will be.

* Deep research is great for more comprehensive research, while web search is great for quick, specific up-to-date information

**Go deeper →** [**Deep research**](https://academy.openai.com/home/clubs/work-users-ynjqu/resources/deep-research)﻿

### **Follow along**

*Click deep research on your tools menu and add the following prompt:*

```
What is the current state of the microbiome therapeutics market, and which approaches show credible paths to commercialization?
```

*ChatGPT will then respond with additional questions. Answer these appropriately, and allow deep research to start. Come back in 5-15 minutes to see the results!*

## **Demo:** Apps (7:20-11:12)

### **Key ideas**

* Apps allow you to connect to third-party tools that you already have access to, and to bring those apps directly into your ChatGPT experience. Some apps will bring in information from your connected systems, and some will bring up a more interactive interface

* Your workspace administrators control which apps are available to you.  Check out your [enabled apps](https://chatgpt.com/#settings/Connectors) in your settings and all apps available to you in <https://chatgpt.com/apps>﻿

* You’ll authenticate to your apps during setup, and then they’ll be available in chat to you via your tools menu or by @ mentioning the specific app

**Go deeper →** [**Apps**](https://academy.openai.com/home/clubs/work-users-ynjqu/resources/connectors)﻿

## **Demo:** Projects (11:12-13:53)

### **Key ideas**

* Projects allow you to organize your chats, as well as add files and instructions that can apply to all chats that start

* You can drag existing chats into a project on the sidebar

* You can share projects with others in your workspace, provided that your workspace settings allow it

* You can also turn on project-only memory so that chats will have memory independent from your general ChatGPT memory – but this setting needs to be enabled at project creation.

**Go deeper →** [**Projects**](https://academy.openai.com/home/clubs/work-users-ynjqu/resources/projects)﻿

## **Demo:** Custom GPTs (13:53-21:32)

### **Key ideas**

* Custom GPTs allow you to hard-code instructions so you can complete repeatable tasks

* If you workspace allows it, you can share custom GPTs with your team

* Custom GPTs and projects have many similar capabilities, but slightly different use cases. Projects are best for longer-term, ongoing work – while GPTs are best for repeated workflows.

**Go deeper →** [**Custom GPTs**](https://academy.openai.com/home/clubs/work-users-ynjqu/resources/custom-gpts)﻿

### **Follow along**

﻿[*Create a custom GPT*](https://chatgpt.com/gpts/editor) *and paste in the following instructions in the Configure tab in the corresponding sections:*

***Name:***

```
Meeting notes summarizer
```

***Description:***

```
Summarizes meeting notes into my preferred format.
```

***Instructions:***

```
Role & Purpose

You are a professional meeting notes summarization assistant. Your purpose is to transform raw meeting notes, transcripts, or bullet points into a clear, concise, and consistently structured meeting summary suitable for sharing with stakeholders.

You do not invent information, infer decisions that were not explicitly stated, or add commentary beyond what is supported by the notes.

Input Expectations

The user will provide one or more of the following:

* Raw meeting notes (bullet points or free text)

* A meeting transcript

* Chat logs or action-item lists

* Partial or unstructured notes

If the input is incomplete or unclear, summarize only what is present and flag gaps explicitly.

Output Format (Always Use This Exact Structure)

Use this format every time, in the order shown below. Use clear headings and concise bullet points.

Meeting Summary

* One short paragraph (2–4 sentences) describing the overall purpose of the meeting and the main outcomes.

Key Discussion Topics

* Topic 1: brief summary

* Topic 2: brief summary

* Topic 3: brief summary (Only include topics actually discussed.)

Decisions Made

* Decision 1

* Decision 2 (If no decisions were made, write: “No decisions were finalized.”)

Action Items

* Owner – Action item description – Due date (if mentioned)

* Owner – Action item description – Due date (if mentioned) (If no owner or date is specified, write “Owner: TBD” or “Due date: Not specified.”)

Open Questions / Risks

* Question, concern, or unresolved issue (If none, write: “No open questions or risks were identified.”)

Next Meeting

* Date/time if mentioned (If not mentioned, write: “Next meeting not scheduled.”)

Style Guidelines

* Be concise, neutral, and professional

* Use plain language suitable for cross-functional teams

* Prefer bullets over long paragraphs

* Do not use emojis, slang, or filler language

* Do not repeat the same information across sections

Accuracy & Guardrails

* Do not assume intent, decisions, or priorities

* Do not merge similar ideas unless the notes clearly indicate they are the same

* If information is ambiguous, reflect that ambiguity explicitly

* Never add recommendations or opinions

Quality Check Before Responding

Before finalizing the output, ensure:

1. All sections are present

2. The format exactly matches the required structure

3. No information was added beyond the source notes

4. Missing information is clearly labeled (e.g., “Not specified”)
```

***Conversation starters:***

```
Summarize the notes below
```

*Hit update, and now paste in the following raw notes into the GPT to test out the instructions:*

```
Marketing Campaign Kickoff – RadiancePro Global Skincare Line (internal) Date: Sept 12 Time: 9–10:30am (ran over) Attendees Maya (Global Marketing Lead / campaign owner) Luca (PMM – RadiancePro) Aisha (Sales Director – Enterprise) Tom (Sales – EMEA) Priya (Sales – APAC) Carla (LATAM Partnerships) Jonas (Paid / Performance) Ingrid (Brand & Creative) Leo (Web/CX) Nina (CS Lead) Victor (Finance) Samir (Ops / Supply Chain) Jess (Reg / Compliance) Alex (RevOps/CRM) joined halfway “plus a couple of juniors” (Maya’s note) 1. Why are we doing this / what’s the thing again? RadiancePro = new “global B2B skincare manufacturing platform” → for brands, not end customers. Maya: “We have a Ferrari-level product and a Craigslist listing.” Current site copy is generic “high quality manufacturing since forever” 🙃 Goal-ish: Launch campaign that actually tells a story about RadiancePro to brand leaders (founders, VP Product, Innovation, etc.). Drive qualified form fills on new landing page (formulation consult / discovery call). Q4: prove this can beat our old “generic manufacturing” campaigns on lead quality + CPL. Aisha: “Sales is getting more inbound but it’s random – we want fewer tire kickers, more real brands that can scale.” 2. Who are we talking to? (chaotic but useful convo) Titles floating around: Founder / Co-founder (indie + niche brands). VP Product / Head of Innovation. Brand Director, sometimes Marketing leads (esp. smaller brands). Procurement / Sourcing for the big global groups. Region nuance (debate): NA: DTC-heavy, lots of people coming from Sephora/Ulta/e-comm backgrounds. More open to “bold” language, less formal. EMEA: conservative, compliance-heavy, hates fluffy claims. Tom: “If we say ‘clinical’ we have to be ready to back it up in a dossier.” APAC: super fast cycles, very trend + texture driven (K-beauty vibes). Priya: “They’ll ask about textures first, margins second.” LATAM: more price-sensitive, obsess over MOQs and payment terms. Carla: “If we can’t speak to MOQs and logistics clearly, they’ll ghost.” Aisha: “Biggest pattern: brands that outgrew their boutique lab partner but don’t want a faceless megafactory.” 3. Product / offer brain dump (Luca talking fast) RadiancePro line: Pre-built, clinically-inspired base formulations: serums, moisturizers, cleansers, eye creams. Focus areas: sensitive skin / barrier, brightening, anti-aging, “derm-inspired”. Ingredient story: niacinamide, peptides, ceramides, etc. (exact INCI list in the 1-pager – Luca to send). Value prop (rough): Use our “platforms” → customize to brand → 8–10 weeks from alignment to first run (vs 12–18 months full custom). Can scale from startup-friendly MOQs → big enterprise volumes. In-house formulation + regulatory support included (within reason). Samir: MOQs are lower than legacy but not “tiny.” Don’t oversell “small batches.” Messaging TBD but we can say “designed for growing brands, not just giants.” Jess: “Please don’t promise ‘clinically proven’ everywhere. We have supporting studies, but language must be controlled.” 4. Pain points (from Sales + CS – kind of all over the place) From CS calls (Nina – reading from notes): “We know what we want the line to feel like but don’t have R&D to get there.” “Our last manufacturer kept pushing generic formulas; we want something ownable.” “We can’t wait 18 months to launch, trends move too fast.” Sales patterns (Aisha): Enterprise brands: want co-innovation, concepting, and help with global rollouts. Indie brands: want someone who “gets” their story but can scale with them. Everyone agrees: Time to market, MOQs, regulatory / claims support, and transparent ingredient stories are the hot buttons. 5. Channels / structure (this part got messy) Paid (Jonas): Meta: awareness + remarketing. Audiences = interests (beauty/skincare/business), lookalikes from site traffic + CRM. LinkedIn: target job titles (Head of Product, Innovation, Brand Director, etc.). Maybe separate ABM stream for Top 50 accounts. Google: Brand search: “RadiancePro” / “[company] skincare manufacturing”. Generic: “private label skincare manufacturer”, “wholesale skincare formulations”, etc. PMax: Jonas: “We should at least test – global inventory, see where demand pops up.” Owned: New RadiancePro landing page (one hero page, maybe 1–2 supporting detail pages later). Email to existing pipeline (filtered by segment + region; Alex to build lists). Internal: Sales deck updates, one-page PDF for reps to send post-call. Timing: Soft content readiness mid-October. Paid flight: 8 weeks to start, then re-evaluate. Need site live BEFORE we turn on the full spend (Leo very clear on this). 6. Early messaging (lots of fragments) Phrases people tossed around (not final): “From concept to shelf in a quarter, not a year.” (everyone nodded) “Clinical-grade skincare without clinical-level complexity.” (Jess skeptical of “clinical-grade”) “The innovation partner behind your next skincare line.” “Flexible MOQs built for bold ideas.” “Science-backed platforms you can make your own.” Regional tweaks (random notes): EMEA: tone down the hype; emphasize compliance, documentation, stability testing. APAC: emphasize textures, speed, trend-forward formats. Maybe show specific product types. LATAM: highlight MOQs, reliability, logistics, less about fancy clinical language. Ingrid: Visual direction = “modern lab” + macro texture shots, packaging, light neutrals. “No influencers, no ‘get your glow’ Instagram captions. They’re buyers and brand leads, not consumers.” 7. Metrics (Victor trying to pin numbers, not fully resolved) Victor wants: CPL target lower than last generic manufacturing campaign by X%. Pipeline influenced: $$ TBD but should be trackable via UTM → CRM. Target # of qualified leads vs “noise leads.” Needs definition. Jonas: wants to tag everything by: Channel (Meta, LI, Google, PMax). Audience (founders vs enterprise, region, remarketing vs prospecting). Creative theme (ingredient, speed, scale, regulatory). Alex (RevOps): Need consistent campaign naming in CRM. Current state = chaos. Will create a RadiancePro parent campaign with sub-campaigns for each channel / region. 8. Risks / dependencies Ops capacity (Samir): “Please do not run a ‘no MOQ’ angle.” Capacity is finite. Need a clear expectation on how many net-new RadiancePro clients we can onboard per quarter. Compliance (Jess): Needs to review all claims. Promised a claims matrix: what we can say globally vs region-specific. Target: Friday. Web (Leo): Needs about 2 weeks for a decent landing page template once copy is final-ish. “Please stop sending me text in screenshots. Use a doc.” Budget (Victor): There is budget for an 8-week “real” test (not pennies). After that, we must move spend to what’s working. Wants commit from Marketing to kill underperformers, not “let’s just see one more week.” 10. Open questions / parking lot How aggressively do we push “clinical” language? (Jess + Luca to sync.) Do we offer any intro package or pilot program for indie brands? (Nina + Victor to explore feasibility.) Are we targeting retailers (Sephora, etc.) at all or strictly brands? Consensus: brands first – retailers maybe later. Do we localize landing page copy immediately (FR/PT/DE) or start with EN only? Priya + Carla want localization soon; Leo says phased approach. 11. To-dos (scribbled, partial) Maya Draft v1 campaign brief (goal, audience, positioning, metrics). Align with Sales leadership on what “qualified lead” specifically means for this campaign. Luca Send updated RadiancePro 1-pager (benefits, features, proof, compliant language). Work with Jess on claims matrix + “safe phrases.” Ingrid & Creative Moodboard for visual direction. 3 headline options per core narrative (speed / science / scale). Jonas Draft channel + audience testing plan. Propose initial budget split and rules for shifting spend based on performance. Leo Sketch wireframe for LP. Confirm CMS constraints (forms, regions, tracking, etc.). Alex Clean campaign naming standards + CRM setup for RadiancePro. Nina Pull 5–10 anonymized quotes from CS calls re: manufacturing pain points. Samir Confirm MOQs + lead time ranges we can publicly state. Victor Share historical CPL / lead quality benchmarks for comparison. Jess Draft claims & compliance one-pager by EOW.
```

## **Demo:** Research and creative brainstorming (22:22-28:03)

### Follow along

*- Create a project titled “****Q2 2026 - South America Expansion****”*

*- Within that project, create a chat using* ***deep research*** *with the following prompt:*

```
Analyze how the productivity and collaboration software market in South America has evolved over the last 5 years, including adoption drivers, customer behavior shifts, competitive dynamics, and country-level differences. Clearly separate observed trends from inferred implications, label assumptions, and focus on strategic insights rather than exact statistics.
```

*- Answer any follow-up questions that ChatGPT asks, and let that run while you’re doing the rest of the exercise.*

*- Next, r**eturn to your projects and click on* ***Edit instructions*** *on the top right.*

![](https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/some-file-dab9f253-a377-493b-b125-c3019b43e96e-1772061955823.png)

*- Paste in the following instructions:*

```
This project is a space to organize context about our potential South American expansion next year. The files uploaded give more context on the market opportunity, as well as a product spec and roadmap for the Lumio Flow product. Ensure your answers are strategic and appropriately push back on assumptions we may make based on our work in other regions that might not apply to South America.
```

*- Upload the file* ***“Product Specifications and 18-month roadmap.pdf”*** *(*[*download here*](https://docsend.com/view/rvra3ugezvz6q6ns)*) into the project so any chats within the project can reference that file. You can also upload the PDF from your deep research query as a file for the project chats to reference.*

*- Start a new chat in the project and upload the CSV “****Lumio\_Top\_500\_Customers.csv****” (*[*download here*](https://docsend.com/view/v6mdytfd33yy6qqn)*) to a chat within your project. Use the following prompt:*

```
Analyze the data from our top 500 customers. Highlight any trends you see that would indicate issues when entering the South American market.
```

## **Demo:** Writing a project plan (28:03-30:05)

### Follow along

*Start a new chat in the same project and paste the following prompt:*

```
Create an example market entry strategy for Lumio entering the South American market.

Treat this as a hypothetical strategy, not official Lumio guidance. Focus on 2–3 priority countries and briefly explain why they were selected.

Structure the response as follows:

Executive Summary

Market Opportunity Overview

Priority Countries & Rationale

Target Customers & Value Proposition

Go-to-Market Strategy (partnerships, sales model, pricing/financing)

Key Risks & Mitigations

Success Metrics

Use a professional, clear tone suitable for a business audience. Keep insights concise and practical, avoiding unnecessary jargon. Keep it to under 500 words.
```

## **Demo:** Preparing for the presentation (30:05-30:23)

### Follow along

*Start a new chat in the same project and paste the following prompt:*

```
Create an image for my slide deck that is an abstract conceptual visualization of productivity in South America. Make it dramatic and inspiring.
```

## **Demo:** Organize your to-do list (30:23-32:20)

### Follow along

*Start a new chat (outside of the project) and upload the file* ***To-Dos.png.*** *Paste the following prompts:*

```
Summarize this to-do list and help me think through priorities.

Summarize in a quick message to my manager, Ronnie.
```

## **Demo:** Draft internal updates (32:20-33:37)

If you have apps connected, @ mention an app and ask it a question!

## **Demo:** Prepare for an internal meeting (33:37-36:07)

### Follow along

*You can create a GPT with the following instructions to prepare for your next career chat with your manager:*

```
You are Career Conversation Co-Pilot, a voice-first career planning assistant. Your job is to help the user prepare for a monthly career conversation with their manager. Use the attached documents to understand the role and expectations.. Each month you will:

1. Interview the user using short, single questions suitable for voice mode.

2. Identify themes, progress, blockers, impact, skills growth, and next steps.

3. Produce an updated career plan in a consistent format named “Monthly Career Plan (YYYY-MM)”.

Operating principles:

* Be direct, concrete, and specific. Avoid generic advice.

* Ask one question at a time. Keep questions short. Wait for the user’s answer before continuing.

* Use light coaching: clarify, reflect back, and probe for specifics (metrics, examples, outcomes, scope).

* If the user is uncertain, propose 2–3 plausible options and ask them to pick.

* Take reasonable liberties for demo purposes: you may suggest polished phrasing, plausible metrics, and coherent narratives, but clearly label anything you “drafted” vs. what the user explicitly stated.

* Maintain continuity: start each new month by briefly recalling last month’s goals and checking progress. If prior months aren’t available, ask a quick baseline set of questions and proceed.

Conversation phases (do in order):

A) Context check (role, priorities, manager expectations, month timeframe)

B) Wins & impact (3–5 items, each with outcome + evidence)

C) Challenges & learnings (blockers, what changed, what you’d do differently)

D) Skills & growth (skills practiced, skills to build, feedback received)

E) Career direction (role aspiration, scope, level signals, strengths)

F) Next month plan (3 priorities, risks, stakeholder map)

G) Ask-for list (support needed from manager, opportunities, visibility)

H) Draft review (read back summary bullets; confirm; then finalize)

Output requirements:

* Always end with a consistent artifact titled exactly: “Monthly Career Plan (YYYY-MM)”.

* Use the format defined in “Monthly Career Plan Format” below.

* Keep the manager-facing sections crisp and ready to paste into a doc.

Monthly Career Plan Format:

1. One-line headline (theme of the month)

2. Role & scope snapshot (2–3 bullets)

3. Progress since last check-in (bullets; include numbers when possible)

4. Top wins (3–5 bullets; each has: Action → Outcome → Evidence)

5. Key learnings & challenges (2–4 bullets)

6. Feedback & signals (what I heard; what I inferred; open questions)

7. Current strengths to leverage (2–3 bullets)

8. Skills to build next (2–3 bullets + how I’ll practice them)

9. Next month priorities (3 items; each has: deliverable, success metric, stakeholders)

10. Risks & mitigations (2–3)

11. Support I want from my manager (3–5 asks; specific)

12. Longer-term career plan (6–12 months)

* Target direction (role/level/scope)

* 2 capability pillars to prove

* 1–2 “signature projects” to pursue

* Visibility & sponsorship plan

13. Appendix (optional)

* Private notes (only if user requests)

* Drafted language vs. user-supplied notes

Style:

* Manager-facing language is concise, positive, and evidence-based.

* Avoid oversharing; keep tone constructive and accountable.

* Prefer bullets over paragraphs.

When the user says “start this month,” begin Phase A immediately.

When the user says “finalize,” produce the artifact immediately using the latest info.

When the user says “same format,” reuse the exact format above without changes.

---

## Suggested “Conversation Starters” (in the GPT builder)

* “Start this month’s career conversation prep (voice interview).”

* “Turn my rough notes into this month’s Monthly Career Plan.”

* “Help me craft my asks for my manager this month.”

* “What are the strongest impact bullets from my month?”

---

## Optional: quick “Memory” fields (for continuity)

If you want the GPT to feel consistent month-to-month, have it capture (and re-confirm) these in the first session:

* Current role + core responsibilities

* Manager’s top priorities for you this quarter

* Promotion/role aspiration (6–12 months)

* 2–3 skill themes you’re focusing on

* Your “impact metrics” (what counts as success)

(For your demo, you can pretend these are “already known” after the first run.)

```

## **Learn:** Becoming a ChatGPT Champion (36:07-37:37)

Learn more → [**OpenAI Academy: Champion Resources**](https://academy.openai.com/home/clubs/champions-ecqup/overview?linkMenu=Champions)﻿

6

Table Of Contents

[44:20](/en/public/clubs/work-users-ynjqu/videos/chatgpt-101-a-guide-to-your-ai-superassistant-recording)

Video

[ChatGPT 101: A Guide to Your AI Superassistant [Recording]](/en/public/clubs/work-users-ynjqu/videos/chatgpt-101-a-guide-to-your-ai-superassistant-recording)

[40:09](/en/public/clubs/work-users-ynjqu/videos/chatgpt-102-leveraging-ai-to-do-your-best-work-recording)

Video

[ChatGPT 102: Leveraging AI to Do Your Best Work [Recording]](/en/public/clubs/work-users-ynjqu/videos/chatgpt-102-leveraging-ai-to-do-your-best-work-recording)

[How finance teams use Codex: Webinar resource guide](/en/public/clubs/work-users-ynjqu/resources/how-finance-teams-use-codex-webinar-resource-guide-2026-05-19)

[ChatGPT 102 Webinar Resource Guide](/en/public/clubs/work-users-ynjqu/resources/chatgpt-102-webinar-resource-guide)

Aug 5th, 2025 • Views 16K

[Codex for everyday work: Webinar resource guide](/en/public/clubs/work-users-ynjqu/resources/codex-for-everyday-work-webinar-resource-guide-2026-05-05)

By Diana Stegall • May 6th, 2026 • Views 7.4K

[ChatGPT 101: Webinar Resource Guide](/en/public/clubs/work-users-ynjqu/resources/chatgpt-101-webinar-resource-guide-interactive)

By Juliann Igo • Feb 19th, 2026 • Views 14.1K

[ChatGPT 101 Webinar Resource Guide](/en/public/clubs/work-users-ynjqu/resources/chatgpt-101-webinar-resource-guide)

Aug 6th, 2025 • Views 53.5K

[ChatGPT 102 Webinar Resource Guide](/en/public/clubs/work-users-ynjqu/resources/chatgpt-102-webinar-resource-guide)

Aug 5th, 2025 • Views 16K

[ChatGPT 101: Webinar Resource Guide](/en/public/clubs/work-users-ynjqu/resources/chatgpt-101-webinar-resource-guide-interactive)

By Juliann Igo • Feb 19th, 2026 • Views 14.1K

[ChatGPT 101 Webinar Resource Guide](/en/public/clubs/work-users-ynjqu/resources/chatgpt-101-webinar-resource-guide)

Aug 6th, 2025 • Views 53.5K

[Codex for everyday work: Webinar resource guide](/en/public/clubs/work-users-ynjqu/resources/codex-for-everyday-work-webinar-resource-guide-2026-05-05)

By Diana Stegall • May 6th, 2026 • Views 7.4K
