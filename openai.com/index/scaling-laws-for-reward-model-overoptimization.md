<!-- source: https://openai.com/index/scaling-laws-for-reward-model-overoptimization/ -->

October 19, 2022

[Publication](/research/index/publication/)

# Scaling laws for reward model overoptimization

[Read paper(opens in a new window)](https://arxiv.org/abs/2210.10760)

![Scaling Laws For Reward Model Overoptimization](https://images.ctfassets.net/kftzwdyauwt9/a8801fe6-8892-472b-f746d1d9fb2d/547c46ed9a8a71e89efbb7a7963a8932/image-6.webp?w=3840&q=90&fm=webp)

## Abstract

In reinforcement learning from human feedback, it is common to optimize against a reward model trained to predict human preferences. Because the reward model is an imperfect proxy, optimizing its value too much can hinder ground truth performance, in accordance with Goodhart's law. This effect has been frequently observed, but not carefully measured due to the expense of collecting human preference data. In this work, we use a synthetic setup in which a fixed "gold-standard" reward model plays the role of humans, providing labels used to train a proxy reward model. We study how the gold reward model score changes as we optimize against the proxy reward model using either reinforcement learning or best-of-n sampling. We find that this relationship follows a different functional form depending on the method of optimization, and that in both cases its coefficients scale smoothly with the number of reward model parameters. We also study the effect on this relationship of the size of the reward model dataset, the number of reward model and policy parameters, and the coefficient of the KL penalty added to the reward in the reinforcement learning setup. We explore the implications of these empirical results for theoretical considerations in AI alignment.

* [Learning Paradigms](/research/index/?tags=learning-paradigms)

## Authors

Leo Gao, John Schulman, Jacob Hilton

## Related articles

![Screenshot of a scene from Minecraft](https://images.ctfassets.net/kftzwdyauwt9/ef9fc360-1a5a-4ca3-5c25b83b3564/50c07940455cc86ef84d91526d9cf3e0/vpt.jpg?w=3840&q=90&fm=webp)

[Learning to play Minecraft with Video PreTraining

ConclusionJun 23, 2022](/index/vpt/)

![Ai Written Critiques Help Humans Notice Flaws](https://images.ctfassets.net/kftzwdyauwt9/533e7e34-5b5d-4f0b-c175293c0363/1e96f2bf24cec03d982566ac4125beb1/image-8.webp?w=3840&q=90&fm=webp)

[AI-written critiques help humans notice flaws

PublicationJun 13, 2022](/index/critiques/)

![Aligning Language Models To Follow Instructions](https://images.ctfassets.net/kftzwdyauwt9/5b1e6906-9f64-42b7-b5d87c29543b/25be46c3552b7af3af0a1c5a70381626/image-13.webp?w=3840&q=90&fm=webp)

[Aligning language models to follow instructions

PublicationJan 27, 2022](/index/instruction-following/)
