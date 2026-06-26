<!-- source: https://openai.com/index/gpt-5-1-codex-max-system-card/ -->

November 19, 2025

[Publication](/research/index/publication/)[Safety](/news/safety-alignment/)

# GPT‑5.1‑Codex‑Max System Card

[Read the System Card(opens in a new window)](https://deploymentsafety.openai.com/gpt-5-1-codex-max)

## Introduction

GPT‑5.1‑Codex‑Max is our new frontier agentic coding model. It is built on an update to our foundational reasoning model trained on agentic tasks across software engineering, math, research, medicine, computer use and more. It is our first model natively trained to operate across multiple context windows through a process called compaction, coherently working over millions of tokens in a single task. Like its predecessors, GPT‑5.1‑Codex‑Max was trained on real-world software engineering tasks like PR creation, code review, frontend coding and Q&A.

This system card outlines the comprehensive safety measures implemented for GPT‑5.1-Codex-Max. It details both model-level mitigations, such as specialized safety training for harmful tasks and prompt injections, and product-level mitigations like agent sandboxing and configurable network access.

GPT‑5.1‑Codex‑Max was evaluated under our Preparedness Framework. It is very capable in the cybersecurity domain but does not reach High capability on cybersecurity. We expect current trends of rapidly increasing capability to continue, and for models to cross the High cybersecurity threshold in the near future. Like other recent models, it is being treated as High capability on biology, and is being deployed with the corresponding suite of safeguards we use for GPT‑5. It does not reach High capability on AI self-improvement.

* [2025](/research/index/?tags=2025)
* [System Cards](/research/index/?tags=system-cards)

## Author

## Keep reading

![A near-autonomous AI chemist improves a challenging reaction](https://images.ctfassets.net/kftzwdyauwt9/QgPPg4etNE5C4Ao0G94sk/e5f2a50e5de4619d0e0fe8483698718b/molecule-one-art-card.png?w=3840&q=90&fm=webp)

[A near-autonomous AI chemist improves a challenging reaction in medicinal chemistry

ResearchJun 17, 2026](/index/ai-chemist-improves-reaction/)

![LifeSciBench 1x1](https://images.ctfassets.net/kftzwdyauwt9/1iV0eZRf28MZRvIxYY4eLf/4379e20807f5ff44efccf518a97e480a/LifeSciBench_1x1.png?w=3840&q=90&fm=webp)

[Introducing LifeSciBench

ResearchJun 17, 2026](/index/introducing-life-sci-bench/)

![oai 1x1](https://images.ctfassets.net/kftzwdyauwt9/7eONRWq61MKUix4tK4t88Y/170085acc9b241a0bdfba429bd217907/oai_1x1.png?w=3840&q=90&fm=webp)

[Advancing youth safety and opportunity through global leadership

Global AffairsJun 2, 2026](/index/advancing-youth-safety-and-opportunity-through-global-leadership/)
