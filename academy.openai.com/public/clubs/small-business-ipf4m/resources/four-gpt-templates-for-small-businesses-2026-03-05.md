<!-- source: https://academy.openai.com/public/clubs/small-business-ipf4m/resources/four-gpt-templates-for-small-businesses-2026-03-05 -->

[Small Business](/en/public/clubs/small-business-ipf4m/overview)

[navigation.content](/en/public/clubs/small-business-ipf4m/content)

Article

March 5, 2026 · Last updated on May 29, 2026

# Four GPT templates for small businesses

![Four GPT templates for small businesses](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/Academy-content-covers-12--66a2b814-1c8c-4651-95e8-253c4003614c-1772741399534.jpeg?fit=scale-down&width=1200)

# Workplace & Business

# Advanced & Builder Skills

## Build practical GPTs step by step—for marketing, customer feedback, customer communications, and operations.

![Four GPT templates for small businesses](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/Academy-content-covers-12--66a2b814-1c8c-4651-95e8-253c4003614c-1772741399534.jpeg?fit=scale-down&width=1200)

#### **Small businesses run on time, clarity, and consistency.**

This guide is designed to help you build practical GPTs for real work. Each template walks through a common business need step by step so you can move from idea to a working first version without needing to start from scratch. The goal is to create something useful: a GPT that helps with a repeatable task, works with real context, and is worth coming back to again next week.

|  |
| --- |
| **How to use this guide** * **Pick a template.** If you are torn between two, choose the one you would most likely use next week.  * **Bring one real example input.** A GPT becomes much better when you test it on something real.  * **Use the starter instructions as a first draft, not a final answer.** Swap in your business details and tighten the output format.  * **Run the test set.** If the GPT fails a test, improve it before you call it done.  * **If you get stuck, narrow the scope:** one user, one job, one output format. |

**﻿**

### **Pick a GPT template**

|  |  |
| --- | --- |
| **Local marketing & customer comms kit**  Turn a promotion, event, or announcement into ready-to-use messaging.  **Best for:** promos, launches, reminders | **Customer feedback to action plan**  Turn reviews and simple data into themes, fixes, and replies.  **Best for:** reviews, surveys, weekly ops |
| **Customer comms copilot**  Draft calm, clear customer messages that match your policies.  **Best for:** email, SMS, DM, service replies | **Ops checklist coach**  Turn routines into checklists, SOPs, and training FAQs.  **Best for:** opening/closing, onboarding, handoffs |

**﻿**

### **Know when a GPT is the right format**

|  |  |
| --- | --- |
| Use a GPT when… | The task is repeatable, the knowledge is fairly stable, the output can follow a clear format, and you want the same guardrails or tone every time. |
| Use a Project instead when… | You are still exploring the workflow, doing several related tasks, or working with context that changes a lot from day to day. |

**﻿**

### **Core steps to build a GPT**

1. Open [chatgpt.com/gpts/editor](https://chatgpt.com/gpts/editor), or go to chatgpt.com/gpts and click “+ Create.”

2. Choose how you want to build. The **Create** tab lets you chat with the GPT Builder; the **Configure** tab lets you set everything directly. For jam build time, Configure is usually faster.

3. In Configure, add the name, description, instructions, conversation starters, and any knowledge files.

4. Turn on only the capabilities you need. The most useful ones for today are Image Generation and Code Interpreter & Data Analysis.

5. Test the GPT in Preview before you save it.

6. Save or publish it and choose the right visibility for your use case.

|  |
| --- |
| **Useful product notes** * GPT creation is available on eligible paid and workspace plans. Creating and editing GPTs is currently web-only.  * Knowledge supports up to 20 files. Simple, single-column documents work best.  * For charts, data work, or downloadable files, enable Code Interpreter & Data Analysis.  * Use Apps or custom actions only if you already know you need them. They are not necessary for this jam. |

**﻿**

### **Build recipe**

Use these five questions to design your GPT clearly before you build, so it does one useful job well and is easier to test, trust, and improve.

1. **What job should this GPT do?** Write it as one repeatable job, not a whole department.

2. **What context should it use?** Decide what is stable enough to upload as Knowledge and what should be provided each time in the chat.

3. **What should the output look like?** Be explicit about structure, length, tone, and what must be included.

4. **What should it never do?** Add guardrails such as “ask before guessing,” “do not include sensitive personal data,” or “flag anything that needs manager approval.”

5. **How will you test it?** Use 3 normal cases, 1 edge case, and 1 missing-info case.

**﻿**

### **A simple instruction formula**

Use this simple structure to draft your instructions in plain language, so your GPT knows what to do, how to do it, and what kind of result to return.

|  |
| --- |
| You are [GPT name], a practical assistant for [business type]. Your job is to help the user do [one repeatable job]. Use uploaded knowledge for stable facts. If key information is missing, ask concise clarifying questions before drafting. Return outputs in [desired format]. Never guess about prices, policies, deadlines, or sensitive details. End with a short human-check list. |

**﻿**

### **Reliability, privacy, and quality**

* Use **Knowledge** for stable references like hours, policies, menus, FAQs, and tone examples. Put fresh inputs into the chat when you use the GPT.

* Do not upload sensitive personal data unless you have a clear reason and permission to do so. In most small-business cases, you do not need it.

* If the answer depends on current facts, ask the GPT to use Web Search or verify the facts manually before sending anything out.

* Add an “ask before guessing” rule. This is one of the highest-leverage ways to improve reliability.

* A good v1 ends with a human check: what you still need to verify before using the output with customers or staff.

# **Template 1 — Local marketing & customer comms kit**

*Turn one offer, event, or announcement into customer-ready messaging you can actually use.*

|  |  |
| --- | --- |
| Best for | Seasonal promos, slow-day offers, launches, local events, reminder campaigns, and “what do I post this week?” moments. |
| Main outputs | Core message, headline options, social caption, short email, SMS or DM, and a simple sign or image brief. |
| Turn on | Image Generation on. Web Search optional. Data Analysis usually off. |
| Upload as Knowledge | Brand voice examples, service or menu list, hours/location, recurring offers, do-not-say rules, FAQ, style examples. |
| Bring into the chat each time | The live offer, dates, price, channel, audience, and any last-minute constraints for this week. |

**﻿**

### **What to gather before you build**

* A short description of your business and who your customers are.

* One real offer or announcement: what it is, when it runs, any limits, and what action you want customers to take.

* 1-3 examples of your brand voice (past email, caption, flyer, website copy).

* Stable facts such as hours, location, ordering link, policies, and approved claims.

* A short list of channels you actually use: Instagram, SMS, email, in-store sign, Google Business Profile, etc.

**﻿**

### **Build it step by step**

1. Open the GPT Builder. For jam speed, go straight to Configure.

2. Name it something clear, such as “Local Marketing Kit — [Business Name].”

3. Write a short description that says exactly what it helps with.

4. Paste the starter instructions below into Instructions and replace the bracketed business details.

5. Add 3-5 conversation starters for your most common marketing jobs.

6. Upload stable knowledge files: brand voice, service/menu details, FAQ, hours, and policy notes.

7. Turn on Image Generation. Only turn on Web Search if you expect the GPT to pull in current facts, public events, or fresh market context.

8. In Preview, test it with one real offer from this week. Fix anything generic, unclear, or off-brand before saving.

### **Starter instructions to paste into Configure**

|  |
| --- |
| **Copy this, then replace the bracketed parts.** You are “Local Marketing & Customer Comms Kit,” a practical marketing assistant for [Business Name], a [business type]. Your job is to turn one offer, event, or announcement into clear customer-facing assets a small business owner can use today. Always start by confirming the audience, offer details, dates, channels, and tone if anything important is missing. Use uploaded knowledge for stable facts such as hours, location, menu or service details, approved claims, and brand voice. Draft outputs in this order unless the user asks otherwise: 1) core message, 2) 3 headline options, 3) social caption, 4) short email, 5) one short SMS or DM, 6) simple sign text or image brief. Keep the tone warm, specific, and realistic for a local business. Avoid hype, filler, or generic marketing language. If a request depends on facts that are missing or time-sensitive, ask before guessing. End every answer with a short human-check list: dates, prices, hours, links, approvals, and tone. |

**﻿**

### **Suggested conversation starters**

* Build a mini-campaign for this week’s offer.

* Turn this event into an Instagram caption, short email, SMS, and sign.

* Give me 3 image ideas for this promotion, then write the image prompt for the best one.

* Rewrite this promo in a warmer, more neighborhood-friendly tone.

**﻿**

### **Make it reliable: test set**

Now that you've built a draft, check whether your GPT works across typical tasks, tricky situations, and missing information before you rely on it in real work.

1. Normal case: “Create a mini-campaign for our Wednesday pastry special. Audience: morning commuters. Tone: warm and simple.”

2. Normal case: “Turn our salon spring package into IG, email, and front-desk sign copy.”

3. Missing-info case: give only “Write marketing for my business” and confirm the GPT asks clarifying questions before drafting.

4. Tone case: ask for the same offer in two tones, such as “more playful” and “more premium,” and check whether both still sound like your business.

5. Fact-check case: include a price, hours, and an ordering link and confirm the human-check list reminds you to verify all three before publishing.

### **Potential variations**

* Holiday promo builder

* Local event launch kit

* Customer win-back message pack

* New product or service announcement kit

* Weekly social planning assistant

### **Watch-outs**

* If current facts matter, either enable Web Search or verify them yourself before sending.

* If outputs sound generic, upload one strong example of your real tone and tighten the output format.

# **Template 2 — Customer feedback to action plan**

*Turn reviews, comments, and simple business data into themes, fixes, replies, and a weekly action plan.*

|  |  |
| --- | --- |
| Best for | Google reviews, survey comments, inbox feedback, refund reasons, service complaints, and weekly “what should we fix first?” questions. |
| Main outputs | Themes with evidence, top fixes for this week, draft replies, a staff checklist, and sometimes a simple chart or trend summary. |
| Turn on | Code Interpreter & Data Analysis on. Web Search optional. Image Generation off. |
| Upload as Knowledge | Reply tone examples, customer service policies, refund rules, service standards, escalation rules, product or service FAQ. |
| Bring into the chat each time | Fresh CSVs, review exports, survey comments, refund logs, and any notes about what changed this week. |

### **What to gather before you build**

* One recent data file or review export. Sample data is fine if you do not want to use live data.

* Any policy notes that should shape the output: refund policy, late-arrival policy, service guarantees, escalation paths.

* A short note about what question you are trying to answer, such as “Why are ratings down?” or “What should we fix this week?”

* One example of a response that sounds like your business.

### **Build it step by step**

1. Name the GPT something practical, such as “Feedback to Action — [Business Name].”

2. Add a description that explains the GPT turns customer feedback and simple data into clear next steps.

3. Paste the starter instructions below into Instructions.

4. Turn on Code Interpreter & Data Analysis so the GPT can work with files, tables, charts, and downloadable outputs.

5. Upload only stable knowledge files, such as policy docs and tone examples. Do not upload changing weekly review exports as Knowledge; upload those in the chat when you use the GPT.

6. Add conversation starters that match your weekly review or ops rhythm.

7. Preview with one sample file and make sure the GPT first describes the dataset, flags quality issues, and only then moves to conclusions.

8. Save once it produces a clear table, a useful weekly action list, and a safe human-check step.

**﻿**

### **Starter instructions to paste into Configure**

|  |
| --- |
| **Copy this, then replace the bracketed parts.** You are “Customer Feedback to Action Plan,” a practical analysis assistant for [Business Name]. Your job is to turn customer reviews, comments, and simple business data into clear operational actions a small business owner can take this week. When a user uploads a file, first tell them what is in the file and flag any obvious quality issues, missing values, odd categories, duplicates, or small-sample limitations. Use uploaded knowledge for stable policies, service standards, and approved reply tone. Then produce outputs in this order unless the user asks otherwise: 1) top themes with evidence or example quotes, 2) top 3 fixes for this week, 3) draft replies for 2–3 customer issues in a calm and helpful tone, 4) a short weekly staff checklist. If a conclusion is uncertain, say so. Do not expose sensitive personal data in the output. If the user asks for a chart, make it simple and explain what it shows. End with a short human-check list: sample size, policy review, edge cases, and anything to verify before sending or acting. |

### **Suggested conversation starters**

* Analyze these reviews and tell me the top themes, top 3 fixes, 2 reply drafts, and a weekly checklist.

* Upload my weekly sales snapshot and explain what changed in plain English.

* Turn these survey comments into a short action plan for the team meeting.

* Help me draft calm, policy-aligned replies to these negative reviews.

### **Make it reliable: test set**

Now that you've built a draft, check whether your GPT works across typical tasks, tricky situations, and missing information before you rely on it in real work.

1. Normal case: upload a review export and ask for themes, fixes, replies, and a checklist.

2. Normal case: upload a CSV and ask for a simple chart plus a plain-English summary of what matters.

3. Missing-info case: ask for a reply without providing the relevant policy and confirm the GPT asks for the policy or flags the assumption.

4. Edge case: upload a tiny or messy sample and check that the GPT mentions limits instead of overclaiming.

5. Privacy case: include names, email addresses, or phone numbers in the source and confirm the GPT does not repeat unnecessary personal details in the output.

### **Potential variations**

* Weekly review digest

* Refund-reason analyzer

* Service quality retro for managers

* Customer churn clue finder

* Reputation response coach

### **Watch-outs**

* Do not treat one noisy week as a complete truth; ask the GPT to note confidence and evidence.

* Use stable policy files as Knowledge; bring fresh operational data into the chat when needed.

* If you want files, charts, or exports, keep Data Analysis on.

# **Template 3 — Customer comms copilot**

*Draft calm, clear, policy-aware customer messages for email, SMS, DM, confirmations, and issue resolution.*

|  |  |
| --- | --- |
| Best for | Booking confirmations, reschedules, shipping updates, refund questions, complaint replies, waitlist messages, and everyday customer service drafts. |
| Main outputs | A ready-to-send reply, a shorter version for SMS or DM, optional tone variations, and a quick check before sending. |
| Turn on | No capability required to start. Web Search optional. Image Generation off. Data Analysis off. |
| Upload as Knowledge | Hours, booking rules, service promises, refund or return policy, response tone examples, FAQs, escalation rules. |
| Bring into the chat each time | The actual customer situation, the channel, the desired outcome, and any notes that are specific to today. |

### **What to gather before you build**

* 2-3 examples of customer messages that sound like your business.

* Stable policy notes: refunds, returns, booking windows, lateness, reschedules, shipping windows, service guarantees.

* A short list of channels you use, such as email, SMS, Instagram DM, or web chat.

* A few real scenarios you deal with often, such as late pickup, wrong item, reschedule request, or unhappy customer.

### **Build it step by step**

1. Create a GPT named something like “Customer Comms Copilot — [Business Name].”

2. Write a one-line description that explains it drafts customer responses that are clear, warm, and policy-aware.

3. Paste the starter instructions below.

4. Upload stable knowledge files: hours, policies, FAQs, and tone examples.

5. Add conversation starters for the 3–5 situations you see most often.

6. Keep capabilities off unless you truly need them. For most service replies, the GPT does not need extra tools.

7. Preview with one easy scenario and one difficult scenario. Check whether it asks before promising something your business has not approved.

8. Save once it consistently produces messages you would be comfortable editing and sending.

**﻿**

### **Starter instructions to paste into Configure**

|  |
| --- |
| **Copy this, then replace the bracketed parts.**  You are “Customer Comms Copilot,” a response assistant for [Business Name]. Your job is to help the user draft customer-facing messages that are clear, calm, warm, and aligned with the business’s policies. Use uploaded knowledge for stable facts like hours, booking rules, refund policy, shipping windows, service details, and tone examples. If the user does not provide enough context, ask concise questions about the channel, the situation, the desired outcome, and any policy constraints before drafting. Unless the user asks otherwise, return: 1) one strong draft reply, 2) a shorter version for SMS or DM if relevant, 3) an optional warmer or firmer variation, 4) a short human-check list. Never promise refunds, discounts, deadlines, or exceptions unless the user or the uploaded knowledge explicitly supports them. For sensitive or escalated situations, suggest a human handoff or approval step. Keep language plain, respectful, and specific; no hype and no robotic tone. |

### **Suggested conversation starters**

* Draft a calm reply to a customer who says we were late.

* Write a booking confirmation email and a 1-line SMS version.

* Help me reply to this DM about our return policy.

* Turn this rough note into a warm but clear customer update.

### **Make it reliable: test set**

Now that you've built a draft, check whether your GPT works across typical tasks, tricky situations, and missing information before you rely on it in real work.

1. Normal case: ask for a booking confirmation email and SMS using your actual policy.

2. Normal case: give a complaint scenario and see whether the GPT stays calm and clear.

3. Missing-info case: ask for a refund reply without giving the refund policy; confirm the GPT asks for it or flags the uncertainty.

4. Length case: request an SMS under a specific character or line limit and confirm the output fits.

5. Escalation case: present a high-friction issue and check whether the GPT suggests manager review instead of overpromising.

### **Potential variations**

* Booking and reminder copilot

* Returns and refunds assistant

* After-service follow-up writer

* Membership or subscription support GPT

* B2B quote and follow-up assistant

### **Watch-outs**

* Do not upload full inbox exports with unnecessary personal data.

* This GPT should sound human, but it should never invent policy exceptions.

* If the replies sound too generic, upload 2–3 real examples of your tone and tighten the instructions.

# **Template 4 — Ops checklist coach**

*Turn routines, notes, and team knowledge into opening and closing checklists, SOP drafts, training FAQs, and handoff notes.*

|  |  |
| --- | --- |
| Best for | Opening and closing routines, shift handoffs, new-hire training, recurring quality checks, cleaning and prep, and “what should this process look like?” moments. |
| Main outputs | Checklists, SOP drafts, training FAQs, role-based task lists, and a clear manager review step. |
| Turn on | No capability required to start. Data Analysis optional if you also want to use logs or inspection data. |
| Upload as Knowledge | Existing SOPs, role descriptions, safety rules, quality standards, equipment notes, service flow, FAQ, training materials. |
| Bring into the chat each time | Today’s role, location, shift, staffing level, special event notes, and anything unusual for the day or week. |

### **What to gather before you build**

* Existing notes, SOPs, or rough bullet points for the process you want to improve.

* Role details: who does the work, when it happens, and what good looks like.

* Safety or policy requirements that must never be skipped.

* One real example of where the process breaks down today.

### **Build it step by step**

1. Create a GPT with a clear name such as “Ops Checklist Coach — [Business Name].”

2. Describe it as a tool that turns routines into checklists, SOPs, and training guidance.

3. Paste the starter instructions below into Instructions.

4. Upload stable SOPs, safety notes, role guides, and FAQs as Knowledge.

5. Add conversation starters that match the routines you care about most, such as opening, closing, setup, cleaning, or shift handoff.

6. Keep the first version narrow: one role, one routine, one output format.

7. Preview with one real routine and confirm the output is easy to scan, easy to print, or easy to copy into a team doc.

8. Save once the GPT gives you a checklist or SOP you could realistically use next week.

### **Starter instructions to paste into Configure**

|  |
| --- |
| **Copy this, then replace the bracketed parts.** You are “Ops Checklist Coach,” an operations assistant for [Business Name]. Your job is to turn recurring routines into clear, usable checklists, SOP drafts, training FAQs, and handoff notes. Use uploaded knowledge for stable process information, safety rules, role responsibilities, and standard answers. When the request is missing key details, ask concise questions about the role, timing, location, tools, frequency, and what “done” looks like. Unless the user asks otherwise, structure outputs so they are easy to scan and use on the job: grouped steps, short wording, clear owners when relevant, and check-box friendly formatting. Always separate must-do safety or compliance steps from nice-to-have improvements. If a step is unclear or safety-critical, tell the user to confirm it with a manager or policy owner rather than guessing. End with a short human-check list: policy review, safety review, and any local details to confirm before rollout. |

### **Suggested conversation starters**

* Build an opening checklist for my shop.

* Turn these rough notes into a one-page SOP.

* Create a new-hire FAQ for front-desk staff.

* Make a shift handoff checklist for busy days.

### **Make it reliable: test set**

Now that you've built a draft, check whether your GPT works across typical tasks, tricky situations, and missing information before you rely on it in real work.

1. Normal case: ask for an opening checklist for one role at one location.

2. Normal case: paste rough notes and ask for a cleaner SOP.

3. Missing-info case: ask for a checklist without giving the role or shift and confirm the GPT asks clarifying questions.

4. Safety case: include a safety-sensitive step and check that the GPT flags it for manager or policy review.

5. Usability case: ask for a version that could be printed or copied into a staff doc and confirm the format is simple and scannable.

### **Potential variations**

* New-hire onboarding coach

* Shift handoff assistant

* Cleaning and prep checklist builder

* Event-day runbook coach

* Manager weekly audit checklist

### **Watch-outs**

* A GPT can organize a process, but it should not replace safety judgment or official policy.

* If the routine changes every day, you may be better off with a Project plus a few reusable prompts.

* If the output feels too long, ask for a one-page checklist version and a separate detailed SOP version.

# **Troubleshooting and “done” checklist**

|  |  |
| --- | --- |
| **Problem** | **Solution** |
| The GPT is too generic | Add one strong example, more business context, tighter output format, and real constraints. |
| The GPT gets facts wrong | Upload stable references, tell it to use knowledge first, and add an ask-before-guessing rule. |
| The GPT works once but not twice | Add a 5-test set and fix the failure modes one by one. |
| The GPT cannot make charts or files | Turn on Code Interpreter & Data Analysis. |
| The task still feels too broad | Shrink it to one user, one job, and one output format. |

### **A strong version is done when…**

* It runs end-to-end with one real input.

* It is saved and easy to find tomorrow.

* The output is easy to reuse, copy, or export.

* It includes a short human-check step.

* It passes a small test set.

* You know exactly when you will use it next.

#### A useful GPT should feel less like a demo and more like a tool you would genuinely return to. If what you built helps you communicate more clearly, spot issues faster, or make everyday operations more consistent, that is real progress. Start small, keep what works, and improve the rest over time. Share what you built in the comments so others can see what’s possible and build on your ideas.

Table Of Contents

[Small Business Prompt Pack](/en/public/clubs/small-business-ipf4m/resources/run-your-small-business-with-chatgpt-2025-11-18)

[How DoorDash merchants can use ChatGPT to run a more efficient business](/en/public/clubs/small-business-ipf4m/resources/how-doordash-merchants-can-use-chatgpt-to-run-a-more-efficient-business-2025-12-15)

[8:05](/en/public/clubs/small-business-ipf4m/videos/chatgpt-workflow-creating-a-customer-response-plan-2025-11-18)

Video

[ChatGPT Workflow: Creating a customer response plan](/en/public/clubs/small-business-ipf4m/videos/chatgpt-workflow-creating-a-customer-response-plan-2025-11-18)

[22:14](/en/public/clubs/small-business-ipf4m/videos/chatgpt-102-for-small-businesses)

Video

[ChatGPT 102 for Small Businesses](/en/public/clubs/small-business-ipf4m/videos/chatgpt-102-for-small-businesses)

By Juliann Igo • Nov 18th, 2025 • Views 9.6K

[Bellevue Small Business Jam](/en/public/clubs/small-business-ipf4m/resources/bellevue-small-business-jam-2026-03-02)

Mar 2nd, 2026 • Views 1.2K

[34:34](/en/public/clubs/small-business-ipf4m/videos/chatgpt-101-introduction-to-chatgpt-for-small-businesses)

Video

[ChatGPT 101: Introduction to ChatGPT for Small Businesses](/en/public/clubs/small-business-ipf4m/videos/chatgpt-101-introduction-to-chatgpt-for-small-businesses)

By Juliann Igo • Nov 18th, 2025 • Views 24.8K

[ChatGPT Use Cases for Work GPT](/en/public/clubs/small-business-ipf4m/resources/chatgpt-use-cases-for-work-gpt-2025-12-05)

Dec 5th, 2025 • Views 5.6K

[22:14](/en/public/clubs/small-business-ipf4m/videos/chatgpt-102-for-small-businesses)

Video

[ChatGPT 102 for Small Businesses](/en/public/clubs/small-business-ipf4m/videos/chatgpt-102-for-small-businesses)

By Juliann Igo • Nov 18th, 2025 • Views 9.6K

[34:34](/en/public/clubs/small-business-ipf4m/videos/chatgpt-101-introduction-to-chatgpt-for-small-businesses)

Video

[ChatGPT 101: Introduction to ChatGPT for Small Businesses](/en/public/clubs/small-business-ipf4m/videos/chatgpt-101-introduction-to-chatgpt-for-small-businesses)

By Juliann Igo • Nov 18th, 2025 • Views 24.8K

[ChatGPT Use Cases for Work GPT](/en/public/clubs/small-business-ipf4m/resources/chatgpt-use-cases-for-work-gpt-2025-12-05)

Dec 5th, 2025 • Views 5.6K

[Bellevue Small Business Jam](/en/public/clubs/small-business-ipf4m/resources/bellevue-small-business-jam-2026-03-02)

Mar 2nd, 2026 • Views 1.2K
