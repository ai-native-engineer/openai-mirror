<!-- source: https://openai.com/index/practical-guide-building-gpt-6/ -->

October 2, 2026

[Product](/news/product-releases/)Guides

# A model guide for the GPT‑6 family

Practical tips for getting the best results from GPT‑6 models while managing time and cost

GPT‑6 is [our most advanced suite of models yet⁠](/index/introducing-gpt-6-1-sol/), and offers you a choice of models for different kinds of work.

Whether you’re turning an idea into a working prototype, building and testing a feature, or orchestrating multi-step workflows across code repositories, databases, and external APIs, this guide explains how to choose a GPT‑6 model, give it effective instructions, manage long-running work, and prepare for production.

* ### GPT-6Astra

  Our most intelligent model for the
  best results.

  input
  :   $10.00

  output
  :   $50.00

  cached input
  :   $1.00
* ### GPT-6.1Sol

  Near-Astra intelligence for a fifth of the price.

  input
  :   $2.00

  output
  :   $10.00

  cached input
  :   $0.10
* ### GPT-6Luna

  Fast and efficient everyday work
  at scale.

  input
  :   $0.10

  output
  :   $0.50

  cached input
  :   $0.01

## TL;DR

* **Run effectively in production.** Use [caching⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/prompt-caching) and [compaction⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/compaction) to manage context and cost. Measure task success and latency, and plan for monitoring and data controls.
* **Match the model to your workload.** Balance capability, cost, and latency by choosing the model, [reasoning effort⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/reasoning), and speed that fit the task.
* **Adjust your prompts and skills.** Keep prompts, skills, and repository instructions consistent about what the model should deliver, what it can do independently, and what counts as done.
* **Keep long-running work on track.** Use [steering⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/steering), [async tools⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/async-tool-calling), and [delegation⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/responses-multi-agent#overview) to handle updates and independent work. Set clear boundaries for when the model should ask for input.

## 1. Run effectively in production

### Prepare your workflow for production

Before deploying, there are several checks and best practices you’ll want to put into place.

* Keep efficiency in mind. [Cut context the task doesn’t need⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/cost-optimization#cost-and-latency) while keeping the evidence it does. Where your application supports it, [run independent tasks together⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/latency-optimization#parallelize) so one slow step doesn’t hold up unrelated work.
* Reuse shared context through [prompt caching⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/prompt-caching) for recurring work. Cached input tokens cost up to [95% less⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/prompt-caching#why-prompt-caching-matters) than uncached input tokens, depending on the model. Put stable instructions and reference material before changing task details, and keep tool definitions consistent. The [caching dashboard⁠(opens in a new window)](https://platform.openai.com/usage?usage_section=prompt-caching) and [diagnostics guide⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/prompt-caching/diagnostics) help you see where that reuse breaks down. Include cache writes and any long-context rates when estimating the cost of a complete workflow.
* For longer conversations, [compaction⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/compaction) reduces context size while preserving the state needed to continue.
* Decide how you’ll [monitor behavior⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/safety-checks/misalignment-monitoring) and review the [data controls⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/your-data) for your application.
* Test before deploying: Run representative tasks and measure task success, latency, and cost per successful task. Check out our [API deployment checklist⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/deployment-checklist#choose-a-model-for-the-workload).

### Match the model to the workload

Think of the model choice and reasoning level as an intelligence/price tradeoff.

* **Model:**

  + [GPT‑6 Astra⁠(opens in a new window)](https://developers.openai.com/api/docs/models/gpt-6-astra) for the hardest reasoning work where maximum intelligence is needed.
  + [GPT‑6.1 Sol⁠(opens in a new window)](https://developers.openai.com/api/docs/models/gpt-6.1-sol) for complex coding, research, and computer use.
  + [GPT‑6 Luna⁠(opens in a new window)](https://developers.openai.com/api/docs/models/gpt-6-luna) for focused tasks at scale and everyday, repeated work with a clear goal, such as extracting invoice fields, classifying requests, or producing structured summaries.

When evaluating the best model for the task, [compare pricing⁠(opens in a new window)](https://developers.openai.com/api/docs/models/compare) for each model.

* **Reasoning level:** In the API, choose how much effort the model spends on the task.

  + Low: Routine tasks, such as extracting facts or making small edits.
  + Medium: Work requiring judgment, such as planning a feature or comparing options.
  + High: Difficult debugging, deeper analysis, or careful review.
  + Extra high / Max: Test where supported when High falls short, and keep only if the improvement justifies the added time and cost.

In the API, you can [change reasoning effort mid-conversation⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/reasoning#change-reasoning-mid-conversation) without breaking cache.

In Codex, start with the default reasoning level for that model, then lower it for simpler tasks or increase it for deeper analysis.

* **Speed:**

  + In the API, use [Fast mode⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/fast-mode) when response time matters, such as in chat apps or coding tools. It provides faster, more consistent response times at a higher per-token cost than Standard processing.
  + In Codex and the API, use [Ultrafast⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/ultrafast-mode) when faster responses are worth the premium, such as rapid coding iterations. It speeds up token generation independently of reasoning effort. [Available for GPT‑6 Astra⁠(opens in a new window)](https://x.com/OpenAIDevs/status/2104996045482778973).

![Paul Solt describes building apps and fixing iPad compatibility with Ultrafast and live steering.](https://images.ctfassets.net/kftzwdyauwt9/6nQdXeHQXmiZChoipK4uRH/36e1a5934003392045ae4cdfa58d5957/paul-solt-tweet-textured-light.png?w=3840&q=90&fm=webp)

## 2. Adjust your prompts and skills

### Give the model a clear assignment

[*“Models have gotten much better at understanding nuance and ambiguity, so overly specific guidance can now hinder results where it previously helped.”*⁠(opens in a new window)](https://x.com/pvncher/status/2095991462416490862)

—Eric Provencher, Developer Experience at OpenAI

Start with a clear assignment: the result you want, who it’s for, the relevant context and constraints, and what counts as done. Then review these four areas, summarized from [*Rethinking skills and prompts for GPT‑6 Astra*⁠(opens in a new window)](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra#better-skills), for a deeper dive into updating your instructions:

* **Create better skills:** Keep descriptions short and explicit about when each skill should run, load supporting details only when needed, and replace rigid recipes with guidance suited to the models your team uses.
* **Update your AGENTS.md:** Explain when particular documents and tests are relevant, and explicitly authorize safe routine workflows, such as running local tests with disposable data and no production access.
* **Set decision boundaries:** State which actions can proceed independently and which require approval, replacing blanket “always ask” rules with clear boundaries.
* **Be prescriptive about persistence:** Define what “done” includes—implementing the change, running it, inspecting the result, and fixing failures—and identify any decisions that require your review.

For additional guidance, see [reasoning best practices⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/reasoning-best-practices#how-to-prompt-reasoning-models-effectively).

### Define the output you need

Whether you’re working in Codex or building with the API, specify which decisions the model can make, when it should ask for input, and what a useful response looks like.

Give the model enough direction to keep work moving without guessing at decisions that matter. [Tell it which choices it can make and when to ask for your input⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/latest-model#initiative-and-follow-through), for example, it can choose how to organize a summary, but should check with you before changing the project’s scope. [Describe what a useful response looks like⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/latest-model#personality-and-writing-style), for example plain language, technical detail suited to your audience, and a short handoff covering what changed, what was checked, and what still needs attention.

## 3. Optimize long-running tasks

### Keep complex work moving

With the GPT‑6 family of models, you can now take on tasks that span hours or days. Use the following features to better manage agents on long-running tasks.

#### API

In the API, use steering, asynchronous tools, and parallel work to keep long-running tasks moving.

* **Update instructions during a run:** [Mid-turn steering⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/steering#send-a-steering-message) lets you send a correction through the [Responses WebSocket API⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/websocket-mode) while the model works. Updates are queued; they don’t cancel running tools or undo completed actions.
* **Keep working while a tool runs:** [Asynchronous tool calling⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/async-tool-calling#how-async-tools-work) lets the model continue independent work while your app runs a slower task, such as tests. Your app returns the result when it’s ready. Wait for that result before starting work that depends on it.
* **Delegate independent subtasks:** GPT‑6.1 Sol supports [multi-agent workflows in the Responses API⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/responses-multi-agent#overview). It can assign independent work to subagents (such as investigating different parts of a codebase) and combine their findings into a final response. Multi-agent is currently in beta.

#### Codex

Long-running tasks can uncover decisions you wouldn’t necessarily anticipate in the initial prompt. Use clarification and steering to keep the work on course.

* **Answer questions as work progresses:** With GPT‑6 Astra, Codex can [ask for clarification while it works⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/latest-model#initiative-and-follow-through). Resolve questions that affect the next step, and specify which independent work can continue while you decide. If you’ll be away, tell Codex which tasks can continue and when it should pause for your answer.
* **Redirect work when requirements change:** [Steer the active task⁠(opens in a new window)](https://developers.openai.com/blog/mastering-codex-remote-for-engineering#2-learn-the-difference-between-queue-and-steer) with new information, explaining what should change and what should stay the same. This helps avoid spending more time on an approach that no longer meets your needs.

![Peter Steinberger describes using Astra for a long-running refactor to asynchronous workers.](https://images.ctfassets.net/kftzwdyauwt9/2OX0vajCJwQiYaxHP7gP6k/98f40c01020b65b1c6f999fd21616d8c/peter-steinberger-tweet-textured-light.png?w=3840&q=90&fm=webp)

### Leverage computer use to do more of the job

[**Computer use**⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/tools-computer-use) lets GPT‑6 Astra, GPT‑6.1 Sol, and GPT‑6 Luna interact directly with websites and desktop apps, even applications without an API. For example, you can ask the model to investigate a bug, fix the code, and open your product in a browser to check that the fix works.

Choose the simplest reliable way to do each step:

* Use an API or connected tool when it can do the job directly.
* Use computer use when the model needs to read a screen, click buttons, or fill in a form for you.

If you’re building computer use into your own app, give the model a tool that can run code to control a browser or desktop. [Playwright works with browsers⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/tools-computer-use#code-execution-harness-examples); PyAutoGUI works with desktop apps.

![Higgsfield AI demonstrates GPT-6.1 Sol multitasking and computer use in ChatGPT.](https://images.ctfassets.net/kftzwdyauwt9/4hpVcAhs91d4pc8IFCucvF/e22b669e9d4de0ff54464d997d39d0d7/higgsfield-tweet-textured-light.png?w=3840&q=90&fm=webp)

### From testing to production: How teams are building with GPT‑6 Astra

1 of 4

> [**Harvey: more context, more useful drafts.**⁠](https://openai.com/index/harvey-from-context-to-confidence-with-astra/) Harvey combines court information, case law, firm documents, and a lawyer’s preferences to tailor its drafts. “We can give more context to the model and produce better and better structured outputs,” says cofounder Gabe Pereyra.

> [**Cognition: test results engineers can review.**⁠](https://openai.com/index/cognition-devin-testing-with-astra/) Cognition uses GPT‑6 Astra inside Devin to test software and return evidence. In an iPhone-game example, Devin produced a simulator recording and a report separating checks that passed from areas left untested, making the remaining work easier to see.

> [**Hex: from a business question to an interactive dashboard.**⁠](https://openai.com/index/hex-gpt-6-astra/) Hex uses GPT‑6 Astra to turn questions about sales-channel performance into written findings and interactive dashboards, including geographic breakdowns. It also asks the model to examine whether the numbers make sense and whether the analysis answers the business question.

> [**Invideo: more control over the final edit.**⁠](https://openai.com/index/invideo-builds-with-gpt-6-astra/) Invideo uses GPT‑6 Astra to plan timeline edits and create custom effects that editors can refine. The company reports roughly three times the success rate on color-grading and correction tasks. A few editors also created about 50 effects in one day.

* Harvey
* Cognition
* Hex
* Invideo

* [ChatGPT](/news/?tags=chatgpt)
* [2026](/news/?tags=2026)

## Author

[View all](/news/)

![GPT-6 Cyber — Cover](https://images.ctfassets.net/kftzwdyauwt9/1AiFc9sQFyo6YguQtfjHHN/3ac0a37435e1dfd2b532eaefe26b18bb/gpt-6-cyber-cover.png?w=3840&q=90&fm=webp)

[GPT‑6 Cyber: Advancing the frontier of aligned cybersecurity agents

ProductNov 5, 2026](/index/introducing-gpt-6-cyber/)

![Daybreak Red is now available in AWS GovCloud (US-East) — Cover](https://images.ctfassets.net/kftzwdyauwt9/3NOPzjiEJ3CYIUuWfexkd5/c16ef9c6350003e5f2f161245be1f78c/daybreak-red-aws-govcloud-cover.png?w=3840&q=90&fm=webp)

[Daybreak Red is now available in AWS GovCloud (US-East)

ProductNov 4, 2026](/index/daybreak-red-aws-govcloud/)

![GPT-Image 2.6 — listing art card](https://images.ctfassets.net/kftzwdyauwt9/2E8ts1o0xQpNfGigwDDkUx/f144a75f6a59d0307eba199c518e5a83/gpt-image-2-6-card.png?w=3840&q=90&fm=webp)

[Introducing Images 2.6

ProductNov 4, 2026](/index/introducing-images-2-6/)
