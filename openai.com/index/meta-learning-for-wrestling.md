<!-- source: https://openai.com/index/meta-learning-for-wrestling/ -->

October 11, 2017

[Publication](/research/index/publication/)

# Meta-learning for wrestling

[View code(opens in a new window)](https://github.com/openai/robosumo)[Read paper(opens in a new window)](https://arxiv.org/abs/1710.03641)

![Two spidery 3D renders wrestling on a stage](https://images.ctfassets.net/kftzwdyauwt9/cbb687d8-0398-4000-1f8b2b36c1bf/03017ab02a40880350fd43acb965abbe/meta-learning-for-wrestling.jpg?w=3840&q=90&fm=webp)

We show that for the task of simulated robot wrestling, a meta-learning agent can learn to quickly defeat a stronger non-meta-learning agent, and also show that the meta-learning agent can adapt to physical malfunction.

Loading...

We’ve extended the [Model-Agnostic Meta-Learning (MAML)⁠(opens in a new window)](https://arxiv.org/abs/1703.03400) algorithm by basing its objective function on optimizing against pairs of environments, rather than single ones as in stock MAML. MAML initializes the policies of our agents so that after only a small number of parameter updates during execution on a new environment (or task) the agents learn to do better in that environment. The policy parameter updates at execution are done via gradient ascent steps on the reward collected during the few episodes of initial interaction with a new environment. By training on pairs we’re able to create policies that quickly adapt to previously unseen environments, as long as the environment doesn’t diverge too wildly from previous ones.

Loading...

To test our continuous adaptation approach we designed 3 types of agents—Ant (4-leg), Bug (6-leg), and Spider (8-leg)—and set up a multi-round game where each agent played several matches against the same opponent and adapted its policy parameters between the rounds to better counter the opponent’s policy. In tests, we found that agents that could adapt their tactics are much better competitors than agents that have fixed policies. After training over a hundred agents, some of which learned fixed policies and others learned to adapt, we evaluated the fitness of each agent.

Learning on the fly can also let agents deal with unusual changes in their own bodies as well, like adapting to some of their own limbs losing functionality over time. This suggests we can use techniques like this to develop agents that can handle both changes in their external environment and also changes in their own bodies or internal states.

Loading...

We’re exploring meta-learning as part of our work on large-scale multi-agent research. Additionally, we’re [releasing the MuJoCo environments and trained policies⁠(opens in a new window)](https://github.com/openai/robosumo) used in this work so that others can experiment with these systems.

* [Learning Paradigms](/research/index/?tags=learning-paradigms)
* [Multi-agent](/research/index/?tags=multi-agent)
* [Exploration & Games](/research/index/?tags=exploration-game)
* [Simulated Environments](/research/index/?tags=simulated-environments)

## Authors

Maruan Al-Shedivat, Trapit Bansal, Ilya Sutskever, Yura Burda, Igor Mordatch, Pieter Abbeel

## Related articles

![Group of people posing behind a panel](https://images.ctfassets.net/kftzwdyauwt9/e7b99f23-347e-4bc9-9e110180fdae/7ae5d14a2436edfbb925876fccae36ca/dota-2-with-large-scale-deep-reinforcement-learning.jpg?w=3840&q=90&fm=webp)

[Dota 2 with large scale deep reinforcement learning

PublicationDec 13, 2019](/index/dota-2-with-large-scale-deep-reinforcement-learning/)

![Outstretched robot arm solving a Rubik's cube in its palm in front of a cloudy purple background](https://images.ctfassets.net/kftzwdyauwt9/9267c72e-6cc1-42f6-d23abb5fa261/3bb199192cd8749d8adc83a71751833c/solving-rubiks-cube.jpg?w=3840&q=90&fm=webp)

[Solving Rubik’s Cube with a robot hand

MilestoneOct 15, 2019](/index/solving-rubiks-cube/)

![OpenAI Five competitive event in a large, dim venue with bright spotlights and a large audience](https://images.ctfassets.net/kftzwdyauwt9/12b8cb5b-dbf2-4e54-54ed702c36f5/692053b6fc20292d8868af782748fa4a/openai-five-defeats-dota-2-world-champions.jpg?w=3840&q=90&fm=webp)

[OpenAI Five defeats Dota 2 world champions

MilestoneApr 15, 2019](/index/openai-five-defeats-dota-2-world-champions/)
