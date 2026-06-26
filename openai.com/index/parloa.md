<!-- source: https://openai.com/index/parloa/ -->

May 7, 2026

Startup

# Parloa builds service agents customers want to talk to

Parloa uses OpenAI models to simulate, evaluate, and run voice-driven customer service systems for the enterprise.

[Start building](/startups/)

![Parloa](https://images.ctfassets.net/kftzwdyauwt9/79CIP6zYxNAKgc3cJfSimj/cd0b9187ba78aeca8088ba6c11ce8b7e/oai_Parloa_1x1.png?w=3840&q=90&fm=webp)

Company size: Startup

Region: Europe & UK, Global

Industry: Technology

Products: API

In Parloa’s early days, Co-founder Stefan Ostwald spent a day inside an insurance call center, where his team had been building early voice experiences. Sitting alongside agents, he listened to the same conversations play out again and again: password resets, policy questions, routine changes. He realized much of that work could be automated.

After that experience, Berlin-based [Parloa⁠(opens in a new window)](https://www.parloa.com/) began building rule-based voice agents to automate high-volume customer interactions.

With the emergence of ChatGPT, the company evolved to build what is now its AI Agent Management Platform (AMP), built on a new generation of models including GPT‑5.4.

AMP gives enterprises a way to design, deploy, and manage customer service interactions at scale. Instead of mapping out rigid intents and flows, teams define behavior in natural language, connect to internal systems, and iterate quickly using built-in simulations and evaluations.

Parloa runs these interactions end to end, handling everything from simple routing to complex, multi-step requests. The focus is on consistency in production, where performance, latency, and edge cases all matter. To get there, Parloa continuously tests models against real customer scenarios before deploying them.

> “The models only matter if they work in production. We work closely with OpenAI on how to make the models fast and reliable enough for real-time conversations.”

—Ciaran O’Reilly Ibañez, Engineering Manager at Parloa

## Designing AMP for enterprise builders

Parloa’s Agent Management Platform (AMP) is designed for business users and subject matter experts to be able to build AI agents without writing code.

“With AMP, we can have subject matter experts from different business units actually build the agents and connect the APIs in a much leaner and simpler way,” says O’Reilly.

At a high level, AMP allows brands to manage the entire AI agent lifecycle. It does that by giving non-technical teams a simpler way to define how an agent should behave before it ever goes live. Instead of writing code or mapping rigid intent trees, subject matter experts set the agent’s role, instructions, tools, and boundaries in natural language. That configuration becomes the basis for how the model is prompted and how the system behaves in production.

Once defined, the agent is tested before deployment. Parloa simulates customer conversations using models like GPT‑5.4, with one model acting as the caller and another running the configured agent. Teams can inspect these interactions directly, test changes against realistic scenarios, and iterate before going live.

The same models are then used to evaluate those conversations using a mix of deterministic checks and LLM-as-a-judge scoring. This shows whether the agent followed instructions, used tools correctly, and completed the task as expected.

![Parloa visuals](https://images.ctfassets.net/kftzwdyauwt9/6CQuobCnvBvFo7b9dlizf4/9938977cc953baed91f9980e0dfaeffd/Studio.png?w=3840&q=90&fm=webp)

![Parloa interface showing an assistant adjusting a new agent from uploaded files.](https://images.ctfassets.net/kftzwdyauwt9/66RbDyQvbXfQAvJmZlJBnt/16d77a9c4ab9f918b7950b54687e1032/parloa-amp-assist.png?w=3840&q=90&fm=webp)

![Parloa interface for creating an AI judge evaluation rule.](https://images.ctfassets.net/kftzwdyauwt9/4Rz7K5eCKrCqXBklORtGOS/db2e3c6df1ee1f71ba85a41c231920d6/parloa-evaluations.png?w=3840&q=90&fm=webp)

![Parloa interface showing simulated customer conversations for testing an AI agent.](https://images.ctfassets.net/kftzwdyauwt9/WxltRqbLPm53mpH53tPtq/45f5137163060d8c2ea185daacd19f6c/Simulations.png?w=3840&q=90&fm=webp)

During a live conversation, AMP’s orchestration layer prompts an OpenAI model with the agent configuration and conversation context to generate a response, retrieve information through RAG, or trigger tools to interact with customer backends. Parloa continuously updates this layer with the latest generation of models as they demonstrate clear gains in real world performance.

After the conversation, separate OpenAI-powered workflows summarize the interaction, classify customer intent, and evaluate performance against defined rules.

As agents became more complex, maintaining a single, monolithic prompt became harder. Small changes could introduce unintended side effects. To address this, Parloa introduced a modular approach. Tasks like authentication, booking changes, or account updates can be separated into distinct sub-agents, improving instruction-following and making systems easier to evolve over time.

At the same time, the platform incorporates deterministic controls where reliability matters most. Enterprises can define structured API chains and event-based logic to ensure critical steps happen in the right order, balancing conversational flexibility with predictable execution.

Parloa uses models like GPT‑4.1, GPT‑5‑mini, and others to simulate realistic customer interactions before an agent ever goes live, then evaluates those interactions using a combination of LLM-as-a-judge and deterministic rules. This allows teams to test edge cases, iterate quickly, and validate performance before exposing customers to failure.

## An evaluation-first approach

Parloa works primarily with large enterprises, where consistency matters as much as capability.

“When a new model comes out, we run our benchmarking suite against it,” says Matthäus Deutsch, Senior Applied Scientist. “It’s very important for us that things do not only work in theoretical benchmarks but in actual real use cases.”

Instead of relying on abstract benchmarks, Parloa mirrors real production agents and runs them through simulation and evaluation pipelines. These tests measure instruction-following reliability, API-calling consistency, latency, and overall performance under realistic conditions.

These evaluations determine which models are ready for production. Only models that perform reliably across real customer scenarios are deployed.

“Enterprise customers face a real migration cost,” says Deutsch. “Once a system is working in production, they keep it stable and only switch when the benefits are clear.”

As a result, systems behave predictably in production, even at scale. Across millions of customer interactions, most conversations are resolved without friction. Even when calls are routed to human agents, escalation is rarely driven by failure. In one deployment, a global travel company reduced requests for a human agent by 80%.

This evaluation-first mindset has become a core differentiator, allowing Parloa to move quickly without sacrificing reliability in production.

## Building for voice at global scale

Voice introduces a different set of constraints than text-based chat. Every interaction runs through a low-latency pipeline: speech-to-text, model reasoning, and text-to-speech.

This pipeline makes latency critical. Even small delays in the model layer compound into noticeable pauses for the caller, shaping how models are selected and optimized.

Parloa works closely with OpenAI to optimize performance for real-time use cases, focusing on latency, response quality, and instruction following. The team continuously evaluates and stress-tests new model iterations in production-like environments before rolling them out to live customer interactions.

Parloa evaluates each component of the voice stack independently:

* **Speech-to-text** systems are tested for word error rate, especially for sensitive inputs like policy numbers or account identifiers.
* **Text-to-speech** models are evaluated through blind listening tests to assess how natural the voice sounds to real users. Those results are then checked against real customer interactions to ensure consistent performance in production environments.
* **Speech-to-speech** models are currently being evaluated for production readiness, with a focus on latency, accuracy, and cost.

From the beginning, these systems have been built for global deployment. Benchmarks span multiple languages, with customers operating across regions worldwide. This multilingual rigor reflects both Parloa’s European roots and the expectations of enterprise customers, who require consistent performance across markets, not just in a single language or region.

Today, Parloa’s agents handle millions of conversations across industries including retail, travel, and insurance, supporting use cases that range from support automation to revenue-generating flows such as teleshopping.

## Changing tech for changing customer journeys

Parloa sees customer service evolving into a fully multimodal experience.

A conversation might start on the phone, continue in chat, and include links or interactive elements along the way. Instead of treating each step as a separate flow, AMP is designed to handle it as a single interaction. Over time, AI agents may become as central to customer journeys as websites and mobile apps.

As enterprises move toward automating a growing share of customer interactions, Parloa is focused on making AI agents reliable enough, flexible enough, and trusted enough to operate at global scale.

## OpenAI <3 startups

[Join the community](/leads/startup/)[Start building(opens in a new window)](/startups)

## Keep reading

![Warp customer story 1x1 hero art card](https://images.ctfassets.net/kftzwdyauwt9/3DK9g0hpubvAEz7lDs0nUf/713989b24b9d377312714303868b9126/oai_Warp_1x1.png?w=3840&q=90&fm=webp)

[Warp’s big bet on building open source with GPT-5.5

StartupMay 27, 2026](/index/warp/)

![oai GradientLabs 1x1](https://images.ctfassets.net/kftzwdyauwt9/5KZQBYyY2LBtllikqf9aul/6143158d9c259eed5aafb47cdac9bcdd/oai_GradientLabs_1x1.png?w=3840&q=90&fm=webp)

[Gradient Labs gives every bank customer an AI account manager

StartupApr 1, 2026](/index/gradient-labs/)

![Descript > 1x1 Card](https://images.ctfassets.net/kftzwdyauwt9/7wL94yXvqYUEQRfOpp68V8/4f6d4a21db6e98ddb2352cbc52ac3b77/oai_descript_1x1.png?w=3840&q=90&fm=webp)

[How Descript engineers multilingual video dubbing at scale

StartupMar 6, 2026](/index/descript/)
