<!-- source: https://openai.com/index/advancing-computer-use-with-ironclad/ -->

October 6, 2026

[Publication](/research/index/publication/)

# Advancing computer use with Ironclad

How a research collaboration in contracting is helping us train and evaluate AI agents on complex professional work.

When we introduced [GPT‑6 Astra](/index/gpt-6-astra/), we demonstrated how far our models have come in using computers for professional work, from preparing documents to testing websites. Our next goal is to make agents more capable and efficient at using specialized software to solve complex business problems. We’re exploring how to train models to understand a company’s business rules, execute multi-step workflows, and verify that their work meets the original requirements.

To accelerate this research, we’re partnering directly with a small number of software companies that understand these workflows best. Together, we’re identifying challenging, high-value tasks and turning them into research problems for training and evaluating our models, ultimately making our models more capable and useful in real-world business applications.

Our first partner is Ironclad, a leader in AI contracting. Working closely with Ironclad’s team, we’ve developed tasks that require agents to configure agreements, approvals, and reusable legal terms, and demonstrated progress on these complex workflows. Ironclad’s expertise has been instrumental in defining what success looks like and bringing real customer needs directly into frontier model development. We’re grateful for their partnership and excited to share what we’ve accomplished together.

GPT‑6 Astra is our first frontier model trained on Ironclad tasks. On our research evaluation, its average score was 32% higher than GPT‑5.6 Sol’s, while estimated time per attempt was 48% lower.[1](#citation-bottom-1)

## Turning contracting workflows into training tasks

Consider a legal operations team setting up a process for buying software. Finance may need to approve purchases above a certain amount, Security may need to review certain requests, and Legal may need to review nonstandard terms. The person setting up the process has to turn that short list into an intake form, document templates, approval rules, and a record of the final agreement.

An AI agent doing the same work has to keep those requirements in view as it moves through the software. For example, it must configure Finance approval above the spending threshold and check that requests above and below it follow the right paths. Getting individual steps right is not enough: the finished process must work across the situations it was designed to handle.

Ironclad employees and people who use Ironclad at OpenAI helped our researchers identify 11 tasks across legal, commercial, and procurement work. These included tasks like setting up nondisclosure agreements, creating procurement approval processes, and updating a reusable legal clause so that it reflects the jurisdiction a requester selects. We estimate that this work would take an experienced user about 30 to 40 minutes per task, on average.

We evaluated each task against 8 to 50 criteria, depending on its complexity. This let us see which parts a model got right and where it fell short. Ironclad also provided hosted software environments of their product where the models could practice these tasks. Our researchers developed synthetic training tasks[2](#citation-bottom-2) around representative workflows and used reinforcement learning to help the models improve through practice and feedback. This combination—tasks selected with people who know the work, detailed criteria, and a place for models to practice—ensures we are improving on real-world tasks that are most important to our customers.

## How Astra performed

We compared Astra and GPT‑5.6 Sol using Max reasoning for Astra and High reasoning for Sol, the settings where each model scored highest. Across the 11 research tasks, Astra’s average score was 55.0%, compared with 41.6% for GPT‑5.6 Sol, while estimated average time per attempt fell from 37.0 minutes for Sol to 19.2 minutes for Astra.[3](#citation-bottom-3) An internal model used in the development of Astra achieved an even stronger 63.7% on these tasks, and we aim to bring these further gains to future models.

|  |  |  |
| --- | --- | --- |
| **Metric** | **GPT‑5.6 Sol** High reasoning | **GPT‑6 Astra** Max reasoning |
| Mean rubric score | 41.6% | 55.0% |
| Estimated average time per attempt | 37.0 minutes | 19.2 minutes |

Astra met more of the task requirements with less simulated time per attempt. The two clips below show how the models handled the same research task. Astra (first) met about 94% of the task criteria in an estimated 20 minutes; GPT‑5.6 Sol (second) met about 85% in an estimated 32 minutes.

**GPT‑6 Astra** met about 94% of the task criteria in an estimated 20 minutes.

**GPT‑5.6 Sol** met about 85% of the task criteria in an estimated 32 minutes.

## What this collaboration means for Ironclad

Ironclad’s role in this work reflects a challenge its customers know well: a contracting process must handle exceptions while preserving the rules a business depends on. If an agent loses track of one of those rules halfway through a task, that limits what a software company can confidently ask it to do. This underscores why human oversight still matters as agents get better at complex contracting tasks, and why a full contracting platform remains essential. Working with our researchers gives Ironclad a way to bring these problems into the development of the underlying model, where we can study them together.

As models become more capable, Ironclad has an opportunity to use them in more of its own products. For legal and business teams, that could mean AI taking on more of the effort involved in complex contracting while preserving the controls those teams rely on.

> “For AI to be genuinely useful in complex areas of contracting, it has to do more than complete individual actions. Agents need to understand the full contracting lifecycle, including how business workflows connect while preserving the controls teams rely on. Our collaboration with OpenAI brings these real-world challenges into the research process and helps move the technology forward.”

—Sunita Verma, Chief Technology Officer, Ironclad

## Work with us to advance AI for complex professional work

We’re inviting a small number of software companies to work directly with our research and engineering teams on important professional tasks that today’s agents still can’t reliably complete. If your team has one, we’d like to see a concrete example: what you’re asking the agent to do, evidence of where it fails, and how you would judge a successful result. Partners should also be able to bring people who know the work deeply, a secure environment for testing, and data that can be safely used for research. This gives us a starting point for investigating the failure and measuring whether the model improves.

If that describes your team,[**apply to explore a research collaboration**](/form/computer-use-research-collaboration/).

* [2026](/research/index/?tags=2026)

## Author

## Footnotes

1. 1

   These results cover the 11 research tasks, not all Ironclad workflows. The times are simulated estimates based on assumed model processing and generation speeds, not measured customer time savings.
2. 2

   We created simulated tasks from contracts publicly available in the SEC’s EDGAR database after applying filters designed to remove personal information. We did not use OpenAI customer data, OpenAI’s internal contracts, or nonpublic Ironclad customer data or contracts for training or evaluation.
3. 3

   See the research-evaluation footnote above.

[View all](/news/)

![BioBasicsBench — Cover](https://images.ctfassets.net/kftzwdyauwt9/jNZJCNxCnXJEalE02MRYi/9c7ad4cdb35bae08e5e49eb6a2f65622/biobasicsbench-cover.png?w=3840&q=90&fm=webp)

[Measuring how AI agents handle everyday wet-lab science

PublicationNov 6, 2026](/index/measuring-how-ai-agents-handle-wet-lab-science/)

![A thousand fewer paths to root — Cover](https://images.ctfassets.net/kftzwdyauwt9/6xmxSENf49pAUFzVokN3KG/3206934563d5b072f5a75139d6b26497/a-thousand-fewer-paths-to-root-cover.png?w=3840&q=90&fm=webp)

[A thousand fewer paths to root

SecurityNov 4, 2026](/index/a-thousand-fewer-paths-to-root/)

![Accelerating engineering for the physical world — card](https://images.ctfassets.net/kftzwdyauwt9/57kuzOPUZjrDUJwHE8nub0/30011dcc7969dfca81d5ac9e06aa31e5/accelerating-engineering-physical-world-card.png?w=3840&q=90&fm=webp)

[Accelerating engineering for the physical world

ResearchNov 3, 2026](/index/accelerating-engineering-for-the-physical-world/)
