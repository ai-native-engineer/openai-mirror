<!-- source: https://openai.com/index/gradient-labs/ -->

April 1, 2026

Startup

# Gradient Labs gives every bank customer an AI account manager

Gradient Labs uses GPT‑4.1 and GPT‑5.4 mini and nano to run complex financial support workflows with high accuracy and low latency.

[Start building](/startups/)

![Soft flowing gradient background in warm orange and yellow blending into teal with a white geometric cube icon beside the text "Gradient Labs" centered across the image.](https://images.ctfassets.net/kftzwdyauwt9/5KZQBYyY2LBtllikqf9aul/6143158d9c259eed5aafb47cdac9bcdd/oai_GradientLabs_1x1.png?w=3840&q=90&fm=webp)

Company size: Startup

Region: Europe & UK

Industry: Technology, Finance

Products: API

Results

10x

Revenue growth

Results

98%

Customer satisfaction with AI agent experience

Results

+11%

Higher accuracy with GPT-4.1 vs. next-best provider

In banking, resolving a customer issue is rarely simple. Cases like fraud or blocked payments require strict adherence to complex procedures across multiple teams. When systems fall short, customers are passed between teams, wait in queues, and face delays at moments when the stakes are highest.

[Gradient Labs⁠(opens in a new window)](https://gradient-labs.ai) is built to handle this complexity. The London-based company is building AI agents that give every bank customer the experience of a dedicated account manager. Founded by a team that previously led AI and data efforts at Monzo, the company’s platform is built on OpenAI models and is now shifting production traffic onto GPT‑5.4 mini and nano.

“We’re seeing 500-millisecond latency with GPT‑5.4 mini and nano, which is exactly what we need for natural voice conversations,” says Danai Antoniou, Co-Founder and Chief Scientist at Gradient Labs. “We’re moving a significant portion of our workload over.”

> “We needed three things simultaneously: accuracy at instruction-following, low hallucination rates, and function-calling reliability, all under voice latency constraints. OpenAI was the only provider that passed on all three.”

Danai Antoniou, Co-Founder and Chief Scientist at Gradient Labs

## Moving from SOPs to real-time systems

In banking, customer interactions are governed by standard operating procedures (SOPs) that define what should happen at each step.

A typical customer interaction might look like this:

1. A customer calls to report a stolen card.
2. The system verifies their identity, handling corrections and interruptions in real time.
3. Once verified, it freezes the card and initiates a replacement.
4. It answers follow-up questions, such as delivery timing, and suggests next steps.

Each step follows a defined procedure, with decisions made in real time based on user input, context, running guardrails, and both customer and agent responses to ensure compliance.

“The model needs to maintain procedure state across interruptions, backchannels, and topic switches while keeping response generation fast,” says Antoniou. “Most providers couldn't even attempt it.”

Gradient Labs benchmarks providers on their most challenging procedures and evaluates them on what they call *trajectory accuracy*: whether the system follows the correct path from start to finish.

In one of their initial evals, GPT‑4.1 was the only model to hit 97% trajectory accuracy and consistency. The next closest provider was 88%.

“In financial services, that’s the difference between resolving a call and creating a compliance incident,” Antoniou says.

This result shaped how Gradient Labs designed its system. The team built a hybrid architecture that uses OpenAI models for reasoning-intensive steps and smaller models for faster, deterministic tasks, with routing that adapts based on complexity and latency constraints.

Internally, the system is composed of specialized skills orchestrated by a central reasoning agent, allowing complex cases to move across workflows without losing context.

For every interaction, 15+ guardrail systems run in parallel to ensure conversations stay within defined procedures and compliance boundaries, including financial advice detection, vulnerability signals, complaints, and attempts to bypass verification or access sensitive data.

## Proving reliability in high-risk environments

Financial institutions don’t deploy systems like this on faith. They need to see, step-by-step, that it behaves correctly under real-world conditions.

“You have to architect from the ground up for no hallucinations,” says Antoniou. “That needs to be the guiding principle as you’re building.”

To evaluate both new and existing models, the team replays real customer conversations and compares the system’s behavior against the expected procedure. They also generate synthetic conversations to test edge cases and rare scenarios before anything is deployed.

Gradient Labs also gives teams control over how the system is introduced. They analyze historical support data to map out the types of customer issues a bank handles and how often they occur. Teams can then choose which categories the AI should handle, starting with lower-risk workflows and expanding over time.

![Dashboard interface for a banking support tool showing a procedure titled Fraud impersonation callback with step by step instructions for verifying suspicious payments. A live call transcript appears on the right with messages between an AI agent and a customer confirming identity and sending a verification code to secure the account.](https://images.ctfassets.net/kftzwdyauwt9/qj3MJpS5LrlNkd5xLnKCH/a6caf281ac2c14e3da0b749609afd5f0/oai_Gradient_UI_16x9.png?w=3840&q=90&fm=webp)

Before going live, customers can simulate conversations to review how the system responds across different scenarios, building confidence that it behaves as expected.

Deployment typically begins with a small percentage of traffic, with continuous monitoring and automated checks flagging conversations that may require human review. Over time, coverage expands as the system demonstrates consistent performance.

## Showing impact on day one, and the path ahead

Gradient Labs’ customers report CSAT scores as high as 98%, in some cases outperforming their best human agents. Most deployments start with over 50% resolution rates on day one, even for complex workflows like disputes, account verification, and fraud.

That impact is reflected in the company’s growth. Gradient Labs has increased revenue more than 10x over the past year, expanding from inbound support into outbound and back-office processes.

Looking ahead, Gradient Labs is focused on systems that can carry context across interactions: understanding a customer’s history, tracking ongoing issues, and picking up where previous conversations left off. This direction is closely aligned with how Gradient Labs thinks about its long-term partnership with OpenAI.

> “We’re not just choosing a model for today. We’re building on a platform where we see the trajectory of reasoning models going in the same direction as our product.”

Danai Antoniou, Co-Founder and Chief Scientist at Gradient Labs

As models continue to improve, the range of procedures that can be safely automated expands. For Gradient Labs, that means moving closer to a system where every customer interaction is handled with the same consistency, judgment, and continuity as a top-tier human agent.

## OpenAI <3 startups

[Join the community](/leads/startup/)[Start building(opens in a new window)](/startups)

## Keep reading

![Warp customer story 1x1 hero art card](https://images.ctfassets.net/kftzwdyauwt9/3DK9g0hpubvAEz7lDs0nUf/713989b24b9d377312714303868b9126/oai_Warp_1x1.png?w=3840&q=90&fm=webp)

[Warp’s big bet on building open source with GPT-5.5

StartupMay 27, 2026](/index/warp/)

![Parloa > Card](https://images.ctfassets.net/kftzwdyauwt9/79CIP6zYxNAKgc3cJfSimj/cd0b9187ba78aeca8088ba6c11ce8b7e/oai_Parloa_1x1.png?w=3840&q=90&fm=webp)

[Parloa builds service agents customers want to talk to

StartupMay 7, 2026](/index/parloa/)

![Descript > 1x1 Card](https://images.ctfassets.net/kftzwdyauwt9/7wL94yXvqYUEQRfOpp68V8/4f6d4a21db6e98ddb2352cbc52ac3b77/oai_descript_1x1.png?w=3840&q=90&fm=webp)

[How Descript engineers multilingual video dubbing at scale

StartupMar 6, 2026](/index/descript/)
