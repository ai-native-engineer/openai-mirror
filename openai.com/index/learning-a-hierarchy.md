<!-- source: https://openai.com/index/learning-a-hierarchy/ -->

October 26, 2017

[Publication](/research/index/publication/)

# Learning a hierarchy

[Read paper(opens in a new window)](https://arxiv.org/abs/1710.09767)[(opens in a new window)](https://github.com/openai/mlsh)

![Learning A Hierarchy](https://images.ctfassets.net/kftzwdyauwt9/475d0757-5e75-4a28-5e2a95fd71c4/800335a93a66f94c429f05bfaae4334d/image-19.webp?w=3840&q=90&fm=webp)

We’ve developed a hierarchical reinforcement learning algorithm that learns high-level actions useful for solving a range of tasks, allowing fast solving of tasks requiring thousands of timesteps. Our algorithm, when applied to a set of navigation problems, discovers a set of high-level actions for walking and crawling in different directions, which enables the agent to master new navigation tasks quickly.

Humans solve complicated challenges by breaking them up into small, manageable components. Grilling pancakes consists of a series of high-level actions, such as measuring flour, whisking eggs, transferring the mixture to the pan, turning the stove on, and so on. Humans are able to learn new tasks rapidly by sequencing together these learned components, even though the task might take millions of low-level actions, i.e., individual muscle contractions.

On the other hand, today’s reinforcement learning methods operate through brute force search over low-level actions, requiring an enormous number of attempts to solve a new task. These methods become very inefficient at solving tasks that take a large number of timesteps.

Our solution is based on the idea of hierarchical reinforcement learning, where agents represent complicated behaviors as a short sequence of high-level actions. This lets our agents solve much harder tasks: while the solution might require 2000 low-level actions, the hierarchical policy turns this into a sequence of 10 high-level actions, and it’s much more efficient to search over the 10-step sequence than the 2000-step sequence.

## Meta-learning shared hierarchies

![Flow diagram of observations undergoing policy and converting to action](https://images.ctfassets.net/kftzwdyauwt9/16c8cb5b-efed-4d35-4c864147f91e/204673a0d5d446dcb88be8b68ff4adc1/MLSH.gif?w=3840&q=90&fm=webp)

Our algorithm, *meta-learning shared hierarchies* (MLSH), learns a hierarchical policy where a master policy switches between a set of sub-policies. The master selects an action every every N timesteps, where we might take N=200. A sub-policy executed for N timesteps constitutes a high-level action, and for our navigation tasks, sub-policies correspond to walking or crawling in different directions.

In most prior work, hierarchical policies have been explicitly hand-engineered. Instead, we aim to discover this hierarchical structure automatically through interaction with the environment. Taking a meta-learning perspective, we define a good hierarchy as one that quickly reaches high reward quickly when training on unseen tasks. Hence, the MLSH algorithm aims to learn sub-policies that enable fast learning on previously unseen tasks.

We train on a distribution over tasks, sharing the sub-policies while learning a new master policy on each sampled task. By repeatedly training new master policies, this process automatically finds sub-policies that accommodate the master policy’s learning dynamics.

## Experiments

Loading...

In our AntMaze environment, a Mujoco Ant robot is placed into a distribution of 9 different mazes and must navigate from the starting position to the goal. Our algorithm is successfully able to find a diverse set of sub-policies that can be sequenced together to solve the maze tasks, solely through interaction with the environment. This set of sub-policies can then be used to master a larger task than the ones they were trained on (see video at beginning at post).

Loading...

## Code

We’re releasing the [code⁠(opens in a new window)](https://github.com/openai/mlsh) for training the MLSH agents, as well as the MuJoCo environments we built to evaluate these algorithms.

* [Simulated Environments](/research/index/?tags=simulated-environments)
* [Exploration & Games](/research/index/?tags=exploration-game)
* [Learning Paradigms](/research/index/?tags=learning-paradigms)

## Authors

Kevin Frans, Jonathan Ho, Peter Chen, Pieter Abbeel

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
