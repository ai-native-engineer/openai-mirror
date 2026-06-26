<!-- source: https://openai.com/index/basis/ -->

August 12, 2025

# Basis scales accounting by turning OpenAI model progress into trusted agents

Built with OpenAI o3, o3‑Pro, GPT‑4.1, and GPT‑5, Basis’ AI agents help accounting firms save up to 30% of their time and expand capacity for advisory and growth.

![A digital background of glowing blue fiber-optic strands with the white Basis logo centered in the frame.](https://images.ctfassets.net/kftzwdyauwt9/6mE2ATm4KI9DK75aUWDwA9/87edfa8e4f12177c8734ff8930accbcb/oai_basis_1.1.png?w=3840&q=90&fm=webp)

Some startups use AI to solve a point-in-time problem. Others build systems that get better as AI improves. [Basis⁠(opens in a new window)](https://www.getbasis.ai/) is the latter.

Founded in 2023, Basis builds AI agents used by top accounting firms—designed to take on structured accounting work with the reliability and depth those tasks require. The team uses OpenAI o3, o3‑Pro, GPT‑4.1, and GPT‑5 to power AI agents that help accounting firms automate repetitive tasks like reconciliations, journal entries, and financial summaries while giving accountants full visibility into how decisions are made and control over the process. The result is up to 30% time savings and increased capacity for high-leverage work, like advising clients and taking on new business.

As OpenAI’s models evolve, Basis compounds those improvements. Each new release expands what agents can handle, boosting reasoning quality, speeding up reviews, and unlocking more sophisticated workflows.

“We’ve worked with OpenAI from day one,” says Mitchell Troyanovsky, co-founder of Basis. “Each model improvement broadens what our agents can take on. As reasoning improves, we unlock more complex, longer-running workflows and grant our agents greater autonomy.”

## Routing accounting tasks to the right OpenAI model

Basis treats accounting as a system of workflows, each with its own context and complexity. To support that, the team built a multi-agent architecture that assigns the best-fit OpenAI model to the right job.

Each task begins with a supervising agent, originally built on OpenAI o3 and now migrated to GPT‑5, which coordinates the full process—routing steps to specialized sub-agents based on task, complexity, latency needs, and input type. GPT‑5 is the strongest model Basis has evaluated to date in reasoning, consistency, and explainability, making it well-suited to guide agents across high-context workflows with minimal oversight.

Sub-agents are powered by a range of models, selected by an internal benchmark suite that scores each model on key capabilities and traits. For speed-critical interactions, like clarifying questions mid-review or surfacing quick feedback, Basis relies on GPT‑4.1.

In more complex scenarios, such as interpreting unusual transaction patterns, resolving ambiguous classifications, or managing multi-step processes like month-end close, Basis agents again rely on GPT‑5 for its deep reasoning capabilities.

This orchestration allows Basis to continuously improve task coverage and accuracy as model capabilities grow.

![A flowchart diagram of an accounting multi-agent system showing multiple AI agents performing tasks such as invoice processing, transaction categorization, reconciliation, and report generation. Arrows indicate the sequential flow of data between modules.](https://images.ctfassets.net/kftzwdyauwt9/4gcRtmjxyYAoFu6Nj8L7wn/329f15bcfc65c209920416cf2680a5a1/Accounting_Multi-Agent_System_Flow_Chart_Light_Mode.svg?w=3840&q=90)

## Validating agent output with OpenAI reasoning

In accounting, automation is most useful if it's reviewable. Basis agents act independently but share context through a central layer, surfacing assumptions, data sources, and the logic behind each decision. Basis originally relied on OpenAI o3‑Pro to scale reasoning across workflows, and later migrated to GPT‑5 upon its release for its ability to reason through structured processes and explain how outcomes were reached.

Take a journal entry, for example. The supervising agent reviews supporting materials, retrieves data, references shared context and best practices, and coordinates sub-agents to prepare its work. The accountant sees the entry along with a clear explanation of what data was used, why it was mapped that way, and how confident the system is in its recommendation.

“Everything we do depends on reasoning,” notes Troyanovsky. “That’s why OpenAI’s models, especially GPT‑5, are so critical. By scaling test-time compute well beyond what earlier models could support, while still exposing the model’s reasoning, we can surface explanations that give customers visibility into and control over what is happening.”

This reasoning also powers the supervising agent’s ability to route tasks with context and precision. As the system matured, Basis moved beyond task automation into real workflow delegation. Function calling pushed that forward, enabling agents to complete multi-step processes like reconciliations and journal entries, not just propose them, in ways that mirror how accountants actually think and approach their work.

## Driving model benchmarking with reasoning and reviewability

With each new model release, the Basis team runs detailed benchmarks on real-world accounting workflows, evaluating not just accuracy, but how clearly the model can explain its reasoning. This helps the team decide both which models to rely on for various tasks and when agents can safely take on new workflows. GPT‑5 is the strongest model in Basis’ stack to date and a strong fit for workflows that require depth and precision, thanks to its performance in parallel tool calling and advanced reasoning.

One area where GPT‑5’s performance stands out is parallel tool calling—a critical capability that enables Basis’ agents to coordinate multiple structured actions within a single workflow. On Basis’ tool-calling benchmark, which tested the model’s ability to use multiple tools in parallel with both code interpreter and web search enabled, GPT‑5 achieved a perfect 100% success rate while also leading all other models across reasoning benchmarks.

GPT‑5 delivers the performance they need at scale, thanks in part to close collaboration with the OpenAI team. Throughout development, Basis shared real-world examples and edge cases and contributed feedback that helped shape model behavior in production.

“OpenAI’s models have consistently led the way in both performance and speed of deployment,” says Troyanovsky. “That combination of reasoning power and accessibility is what makes our architecture possible. And that kind of progress is what makes OpenAI such a valuable partner. We’re not just reacting to model improvements, we’re helping drive them.”

## Scaling trust, not just tasks, with OpenAI

Today, Basis supports a significant share of large accounting firms across the U.S. Firms using Basis report 30% time savings on average, and continue expanding agent responsibilities as trust grows. More importantly, they’re reclaiming capacity to serve clients, explore new practice areas, and deepen advisory relationships.

“OpenAI has been instrumental to that shift,” says Troyanovsky. “Their models don’t just perform, they’ve helped shape how and what we build. As the models evolve, so does the scope of what our agents can do, and therefore what accountants can do.”

## Interested in learning more about ChatGPT for business?

[Talk with our team](/contact-sales/)

## Keep reading

![Intercom cover image](https://images.ctfassets.net/kftzwdyauwt9/32rIG6b83UB8GU0atjwCLp/2859930e037889e03ffc8ca685d00d5a/oai_Intercom_1x1.png?w=3840&q=90&fm=webp)

[Three lessons for creating a sustainable AI advantage

Jul 30, 2025](/index/intercom/)

![oai Outtake 1x1](https://images.ctfassets.net/kftzwdyauwt9/6ndUQXibUAMFP9MDEq2a3Z/c36faa5a2a1c9e7294820ae74035c31f/oai_Outtake_1x1.png?w=3840&q=90&fm=webp)

[Resolving digital threats 100x faster with OpenAI

Jul 24, 2025](/index/outtake/)

![Invideo > Cover Image](https://images.ctfassets.net/kftzwdyauwt9/3ENpuoD5KB8oejWnO6md1b/52f63a73ffd0928cc87b5e072205221c/oai_invideo_1x1.png?w=3840&q=90&fm=webp)

[Invideo AI uses OpenAI models to create videos 10x faster

Jul 17, 2025](/index/invideo-ai/)
