<!-- source: https://openai.com/index/warp/ -->

May 27, 2026

Startup

# Warp’s big bet on building open source with GPT‑5.5

Warp uses GPT‑5.5 to orchestrate agents across local, cloud, and open-source workflows.

[Start building with OpenAI(opens in a new window)](/startups)

![Warp customer story art card.](https://images.ctfassets.net/kftzwdyauwt9/3DK9g0hpubvAEz7lDs0nUf/713989b24b9d377312714303868b9126/oai_Warp_1x1.png?w=3840&q=90&fm=webp)

Company size: Startup

Region: North America

Industry: Technology

Products: API

30%

Fewer tokens per task with GPT-5.5

90%

Of internal pull requests created with agents

[Warp⁠(opens in a new window)](https://warp.dev) started as a modern terminal, earning early love from developers for its speed, collaboration features, command workflows, and AI-native interface. As coding agents moved from experiments to everyday engineering workflows, Warp saw the terminal becoming a natural place for developers to work with agents: where commands, context, collaboration, and review already meet.

When Warp [open-sourced⁠(opens in a new window)](https://www.warp.dev/blog/warp-is-now-open-source) its terminal client this year, with OpenAI as the founding sponsor of the repo, the company also introduced Open Agentic Development: a model for building software in the open. Humans define objectives and supervise outcomes, while agents plan work, write code, test changes, and open pull requests.

Recent improvements in frontier AI models helped make that kind of agent orchestration practical at scale. For Warp’s open-source workflows, GPT‑5.5 helps agents reason across larger problem spaces and prepare work for human review. In internal benchmarks, GPT‑5.5 used 30% fewer tokens per agentic coding task than GPT‑5.4, helping Warp improve efficiency as it scales long-running agent workflows.

Today, Warp has nearly 1 million developers and is used by more than 56% of the Fortune 500. In Warp’s own engineering organization, agents now co-create around 90% of the company’s pull requests, giving the team a firsthand view into what long-running agent workflows need to scale: observability, coordination, memory, and human review.

> “We think we can ship a better Warp, more quickly, by working with our community to supervise a fleet of agents. OpenAI models help make that sustainable for the long-horizon coding work these systems require.”

—Zach Lloyd, CEO

## The next generation of collaborative software development

Open Agentic Development is Warp’s bet on where software development is heading. Agents will write code, and developers will specify intent, verify the outputs, and decide what ultimately ships. Those choices become reusable context for future agents, allowing the system to improve over time.

If the orchestration is good enough, Warp believes agents can produce more consistent code than a loosely coordinated group of humans. Open source then becomes less about humans contributing implementation work directly, and more about contributing the product judgment and shared vision that only humans can provide.

![Diagram showing Warp's Open Agentic Development workflow.](https://images.ctfassets.net/kftzwdyauwt9/LIctfUsXv5q5lTqMM85fe/2d781c7e5f82dd5d140635f7e2783bd0/WarpWorkflow_Light.jpg?w=3840&q=90&fm=webp)

Persistent, parallelized agents need components like shared memory, reproducible environments, evaluation systems, permissions, and ways to coordinate work. Warp built Oz, its cloud orchestration platform, to manage agents across local and cloud environments.

For Open Agentic Development workflows, Warp uses GPT‑5.5 for agents that help manage open-source contributions, according to the company. OpenAI models have also performed strongly in Warp’s internal evaluations for long-horizon engineering tasks involving reasoning, planning, code generation, and code review.

## Agentic orchestration with Oz

[Oz⁠(opens in a new window)](https://www.warp.dev/oz) acts as a control plane for deploying and coordinating agents across local and cloud environments. Developers can launch agents through a web interface, select predefined skills and environments, choose the model and hosting configurations, and monitor long-running workflows centrally as they execute.

![Screenshot of an agent run in Warp's Oz interface.](https://images.ctfassets.net/kftzwdyauwt9/4vqc0BRhd712yZ0Jpdoygo/8011aa2f4228fed7c9a7868b51c65206/Warp_AgentRun.png?w=3840&q=90&fm=webp)

![Screenshot of an agent session in Warp's Oz interface.](https://images.ctfassets.net/kftzwdyauwt9/4zVWgbG3zCL5Rj0kGy2PjW/ab0310bfddba5ae56ad41e54a56f0718/Warp_AgentSession.png?w=3840&q=90&fm=webp)

![Screenshot of the new agent setup flow in Warp's Oz interface.](https://images.ctfassets.net/kftzwdyauwt9/3DkAOEIgUAXsyqUPE6zq91/98e69ddbf00765b3b2fdd87111981eb3/Warp_NewAgent.png?w=3840&q=90&fm=webp)

Once launched, agents can continue running remotely while developers inspect live sessions, monitor execution state, review generated artifacts, and hand workflows back and forth between cloud and local environments without losing context. Oz also supports recurring workflows, allowing agents to operate like scheduled cron jobs.

As agents accumulate more state over time, maintaining focus and preserving important decisions becomes increasingly difficult. Oz uses techniques like context compaction, persistent memory, and dedicated subagents for tasks like code search and file analysis to help agents stay reliable across extended workflows.

OpenAI models play several roles inside Oz. For the Warp agent, tasks are classified by type and difficulty, with more complex coding and reasoning work routed to stronger model configurations. GPT‑5.5 is part of the OpenAI model mix Warp uses for demanding agentic coding workflows. Warp also uses OpenAI models as LLM-as-a-judge systems inside its evaluation pipelines.

> “We’ve found that OpenAI models regularly provide frontier-level intelligence while taking fewer tokens and turns to complete the same tasks. The models are especially strong for coding tasks that require reasoning across large problem spaces.”

—Zach Lloyd, CEO

## Building the infrastructure for agentic development

For Warp, Open Agentic Development and the Oz orchestration platform are ultimately part of the same long-term bet: that software development is evolving from individual interactions with coding assistants into systems for coordinating large numbers of persistent agents over time.

So far, that bet seems to be paying off. Warp’s ARR grew 35x last year, with enterprise revenue up more than 500% since Q4 2025. The company says much of that growth is coming from organizations looking for more flexible ways to scale agent workflows.

The underlying workflows around agentic development are still early and highly experimental. By open sourcing its terminal client and building in public with Open Agentic Development workflows, Warp hopes developers can help shape how orchestration, supervision, and verification systems evolve as agents become more autonomous over time.

“No one knows exactly what the future of agentic development will look like,” Lloyd says. “We think the community ought to be able to participate in shaping it.”

## OpenAI <3 startups

[Join the community](/leads/startup/)[Start building(opens in a new window)](/startups)

## Keep reading

![Parloa > Card](https://images.ctfassets.net/kftzwdyauwt9/79CIP6zYxNAKgc3cJfSimj/cd0b9187ba78aeca8088ba6c11ce8b7e/oai_Parloa_1x1.png?w=3840&q=90&fm=webp)

[Parloa builds service agents customers want to talk to

StartupMay 7, 2026](/index/parloa/)

![oai GradientLabs 1x1](https://images.ctfassets.net/kftzwdyauwt9/5KZQBYyY2LBtllikqf9aul/6143158d9c259eed5aafb47cdac9bcdd/oai_GradientLabs_1x1.png?w=3840&q=90&fm=webp)

[Gradient Labs gives every bank customer an AI account manager

StartupApr 1, 2026](/index/gradient-labs/)

![Descript > 1x1 Card](https://images.ctfassets.net/kftzwdyauwt9/7wL94yXvqYUEQRfOpp68V8/4f6d4a21db6e98ddb2352cbc52ac3b77/oai_descript_1x1.png?w=3840&q=90&fm=webp)

[How Descript engineers multilingual video dubbing at scale

StartupMar 6, 2026](/index/descript/)
