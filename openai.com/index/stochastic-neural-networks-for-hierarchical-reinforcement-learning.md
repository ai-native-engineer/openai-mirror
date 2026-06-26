<!-- source: https://openai.com/index/stochastic-neural-networks-for-hierarchical-reinforcement-learning/ -->

April 10, 2017

[Publication](/research/index/publication/)

# Stochastic Neural Networks for hierarchical reinforcement learning

[Read paper(opens in a new window)](https://arxiv.org/abs/1704.03012)

![Stochastic Neural Networks For Hierarchical Reinforcement Learning](https://images.ctfassets.net/kftzwdyauwt9/eaa0f45c-1d46-48b3-e6dcab9f7e47/5a18d43299f25b6ba17603ef88e67eae/image_141.png?w=3840&q=90&fm=webp)

## Abstract

Deep reinforcement learning has achieved many impressive results in recent years. However, tasks with sparse rewards or long horizons continue to pose significant challenges. To tackle these important problems, we propose a general framework that first learns useful skills in a pre-training environment, and then leverages the acquired skills for learning faster in downstream tasks. Our approach brings together some of the strengths of intrinsic motivation and hierarchical methods: the learning of useful skill is guided by a single proxy reward, the design of which requires very minimal domain knowledge about the downstream tasks. Then a high-level policy is trained on top of these skills, providing a significant improvement of the exploration and allowing to tackle sparse rewards in the downstream tasks. To efficiently pre-train a large span of skills, we use Stochastic Neural Networks combined with an information-theoretic regularizer. Our experiments show that this combination is effective in learning a wide span of interpretable skills in a sample-efficient way, and can significantly boost the learning performance uniformly across a wide range of downstream tasks.

* [Learning Paradigms](/research/index/?tags=learning-paradigms)

## Authors

Carlos Florensa, Yan Duan, Pieter Abbeel

## Related articles

![Scaling Laws For Reward Model Overoptimization](https://images.ctfassets.net/kftzwdyauwt9/a8801fe6-8892-472b-f746d1d9fb2d/547c46ed9a8a71e89efbb7a7963a8932/image-6.webp?w=3840&q=90&fm=webp)

[Scaling laws for reward model overoptimization

PublicationOct 19, 2022](/index/scaling-laws-for-reward-model-overoptimization/)

![Screenshot of a scene from Minecraft](https://images.ctfassets.net/kftzwdyauwt9/ef9fc360-1a5a-4ca3-5c25b83b3564/50c07940455cc86ef84d91526d9cf3e0/vpt.jpg?w=3840&q=90&fm=webp)

[Learning to play Minecraft with Video PreTraining

ConclusionJun 23, 2022](/index/vpt/)

![Group of people posing behind a panel](https://images.ctfassets.net/kftzwdyauwt9/e7b99f23-347e-4bc9-9e110180fdae/7ae5d14a2436edfbb925876fccae36ca/dota-2-with-large-scale-deep-reinforcement-learning.jpg?w=3840&q=90&fm=webp)

[Dota 2 with large scale deep reinforcement learning

PublicationDec 13, 2019](/index/dota-2-with-large-scale-deep-reinforcement-learning/)
