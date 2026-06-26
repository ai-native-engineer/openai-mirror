<!-- source: https://openai.com/index/mle-bench/ -->

October 10, 2024

[Publication](/research/index/publication/)

# MLE-bench

Evaluating Machine Learning Agents on Machine Learning Engineering

[Read paper(opens in a new window)](https://arxiv.org/abs/2410.07095)

We introduce MLE-bench, a benchmark for measuring how well AI agents perform at machine learning engineering. To this end, we curate 75 ML engineering-related competitions from Kaggle, creating a diverse set of challenging tasks that test real-world ML engineering skills such as training models, preparing datasets, and running experiments. We establish human baselines for each competition using Kaggle's publicly available leaderboards. We use open-source agent scaffolds to evaluate several frontier language models on our benchmark, finding that the best-performing setup — OpenAI's o1‑preview with AIDE scaffolding — achieves at least the level of a Kaggle bronze medal in 16.9% of competitions. In addition to our main results, we investigate various forms of resource-scaling for AI agents and the impact of contamination from pre-training. We [open-source our benchmark code⁠(opens in a new window)](https://github.com/openai/mle-bench/) to facilitate future research in understanding the ML engineering capabilities of AI agents.

* [o1](/research/index/?tags=o1)
* [Software & Engineering](/research/index/?tags=software-engineering)
* [Learning Paradigms](/research/index/?tags=learning-paradigms)
* [Reasonings & Policy](/research/index/?tags=reasoning-policy)

## Authors

Chan Jun Shern, Neil Chowdhury, Oliver Jaffe, James Aung, Dane Sherburn, Evan Mays, Giulio Starace, Kevin Liu, Leon Maksin, Tejal Patwardhan, Lilian Weng, Aleksander Madry
