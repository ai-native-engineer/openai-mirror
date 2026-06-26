<!-- source: https://openai.com/index/gpt-5-system-card/ -->

August 7, 2025

[Publication](/research/index/publication/)[Safety](/news/safety-alignment/)

# GPT‑5 System Card

[Read the System Card(opens in a new window)](https://arxiv.org/abs/2601.03267)[Dive into the data(opens in a new window)](https://deploymentsafety.openai.com/gpt-5)

GPT‑5 is a unified system with a smart and fast model that answers most questions, a deeper reasoning model for harder problems, and a real-time router that quickly decides which model to use based on conversation type, complexity, tool needs, and explicit intent (for example, if you say “think hard about this” in the prompt). The router is continuously trained on real signals, including when users switch models, preference rates for responses, and measured correctness, improving over time. Once usage limits are reached, a mini version of each model handles remaining queries. In the near future, we plan to integrate these capabilities into a single model.

In this system card, we label the fast, high-throughput models as gpt-5-main and gpt-5-main-mini, and the thinking models as gpt-5-thinking and gpt-5-thinking-mini. In the API, we provide direct access to the thinking model, its mini version, and an even smaller and faster nano version of the thinking model, made for developers (gpt-5-thinking-nano). In ChatGPT, we also provide access to gpt-5-thinking using a setting that makes use of parallel test time compute; we refer to this as gpt-5-thinking-pro.

It can be helpful to think of the GPT‑5 models as successors to previous models:

|  |  |
| --- | --- |
| **Previous model** | **GPT‑5 model** |
| GPT‑4o | gpt-5-main |
| GPT‑4o‑mini | gpt-5-main-mini |
| OpenAI o3 | gpt-5-thinking |
| OpenAI o4-mini | gpt-5-thinking-mini |
| GPT‑4.1‑nano | gpt-5-thinking-nano |
| OpenAI o3 Pro | gpt-5-thinking-pro |

This system card focuses primarily on gpt-5-thinking and gpt-5-main, while evaluations for other models are available in the appendix. The GPT‑5 system not only outperforms previous models on benchmarks and answers questions more quickly, but—more importantly—is more useful for real-world queries. We’ve made significant advances in reducing hallucinations, improving instruction following, and minimizing sycophancy, and have leveled up GPT‑5’s performance in three of ChatGPT’s most common uses: writing, coding, and health. All of the GPT‑5 models additionally feature safe-completions, our latest approach to safety training to prevent disallowed content.

Similarly to ChatGPT agent, we have decided to treat gpt-5-thinking as High capability in the Biological and Chemical domain under our [Preparedness Framework](/index/updating-our-preparedness-framework/), activating the associated safeguards. While we do not have definitive evidence that this model could meaningfully help a novice to create severe biological harm—our [defined threshold⁠(opens in a new window)](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf) for High capability—we have chosen to take a precautionary approach.

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
