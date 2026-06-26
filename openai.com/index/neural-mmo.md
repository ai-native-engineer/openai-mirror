<!-- source: https://openai.com/index/neural-mmo/ -->

March 4, 2019

[Milestone](/research/index/milestone/)

# Neural MMO: A massively multiagent game environment

[Read paper(opens in a new window)](http://arxiv.org/abs/1903.00784)[View code(opens in a new window)](https://github.com/openai/neural-mmo)[3D client(opens in a new window)](https://github.com/jsuarez5341/neural-mmo-client)

![Aerial view of a 3D terrain with boulders and figures on green grass](https://images.ctfassets.net/kftzwdyauwt9/260e0a3f-c0ad-4f1a-872a3b988dd5/0108cb3658e4c62d1f102f00c3ed631b/neural-mmo.jpg?w=3840&q=90&fm=webp)

We’re releasing a Neural [MMO⁠(opens in a new window)](https://en.wikipedia.org/wiki/Massively_multiplayer_online_game), a massively multiagent game environment for reinforcement learning agents. Our platform supports a large, variable number of agents within a persistent and open-ended task. The inclusion of many agents and species leads to better exploration, divergent niche formation, and greater overall competence.

In recent years, multiagent settings have become an effective [platform⁠(opens in a new window)](https://www.pommerman.com/) [for⁠(opens in a new window)](https://arxiv.org/abs/1902.00506) [deep⁠(opens in a new window)](https://arxiv.org/abs/1207.4708) [reinforcement⁠(opens in a new window)](https://blog.openai.com/openai-five/) [learning⁠(opens in a new window)](https://www.nature.com/articles/nature24270) [research⁠(opens in a new window)](https://deepmind.com/blog/capture-the-flag/). Despite this progress, there are still two main challenges for multiagent reinforcement learning. We need to create open-ended tasks with a high complexity ceiling: current environments are either complex but [too⁠](/five/) [narrow⁠(opens in a new window)](https://deepmind.com/blog/alphastar-mastering-real-time-strategy-game-starcraft-ii/) or open-ended but [too⁠(opens in a new window)](https://arxiv.org/abs/1712.00600) [simple⁠(opens in a new window)](https://arxiv.org/abs/1709.04511). Properties such as persistence and large population scale are key, but we also need more **benchmark environments** to quantify learning progress in the presence of large population scales and persistence. The game genre of Massively Multiplayer Online Games (MMOs) simulates a large ecosystem of a variable number of players competing in persistent and extensive environments.

To address these challenges, we built our Neural MMO to meet the following criteria:

* **Persistence**: Agents learn concurrently in the presence of other learning agents with no environment resets. Strategies must consider long time horizons and adapt to potentially rapid changes in the behaviors of other agents.
* **Scale**: The environment supports a large and variable number of entities. Our experiments consider up to 100M lifetimes of 128 concurrent agents in each of 100 concurrent servers.
* **Efficiency**: The computational barrier to entry is low. We can train effective policies on a single desktop CPU.
* **Expansion**: Similarily [to⁠(opens in a new window)](https://oldschool.runescape.com/) [existing⁠(opens in a new window)](https://worldofwarcraft.com/en-us/) [MMOs⁠(opens in a new window)](https://en.wikipedia.org/wiki/Massively_multiplayer_online_game), our Neural MMO is designed to update with new content. Current core features include procedural generation of tile-based terrain, a food and water foraging system, and a strategic combat system. There is an opportunity for open-source driven expansion in the future.

## The environment

**Players** *(agents)* may join any available **server** *(environment)*, each containing an automatically generated tile-based game map of configurable size. Some tiles, such as food-bearing forest tiles and grass tiles, are traversable. Others, such as water and solid stone, are not. Agents spawn at a random location along the edges of the environment. They must obtain food and water, and avoid combat damage from other agents, in order to sustain their health. Stepping on a forest tile or next to a water tile refills a portion of the agent’s food or water supply, respectively. However, forest tiles have a limited supply of food, which regenerates slowly over time. This means that agents must compete for food tiles while periodically refilling their water supply from infinite water tiles. Players engage in combat using three combat styles, denoted *Melee, Range,* and *Mage* for flavor.

**Input**: Agents observe a square crop of tiles centered on their current position. This includes tile terrain types and the select properties (health, food, water, and position) of occupying agents.

**Output**: Agents output action choices for the next game **tick** *(timestep)*. Actions consist of one movement and one attack.

![Grouped visualizations of the game creation process](https://images.ctfassets.net/kftzwdyauwt9/9a823d25-9eed-4951-9f9b167afa65/7d639250b4925ff7641055d1c349d54a/Screen-Shot-2019-02-21-at-10.48.37-AM.png?w=3840&q=90&fm=webp)

## The model

As a simple baseline, we train a small, fully connected architecture using [vanilla policy gradients⁠(opens in a new window)](https://spinningup.openai.com/en/latest/algorithms/vpg.html), with a value function baseline and reward discounting as the only enhancements. Instead of rewarding agents for achieving particular objectives, agents optimize only for their **lifetime** *(trajectory length)*: they receive reward 1 for each tick of their lifetime. We convert variable length observations, such as the list of surrounding players, into a single length vector by computing the maximum across all players ([OpenAI Five⁠](/five/) also utilized this trick). The source release includes our full distributed training implementation, which is based on [PyTorch⁠(opens in a new window)](https://pytorch.org/) and [Ray⁠(opens in a new window)](https://ray.readthedocs.io/en/latest/#).

## Evaluation results

![Four line graphs compare lifetime in tournament across different opponent population sizes at train time, showing that agents trained with larger opponent populations generally perform better across tournament sizes.](https://images.ctfassets.net/kftzwdyauwt9/1579637b-01b6-4144-e05fcf9c80cb/b162d918031a4bdb52d70c655859b5cf/Screen-Shot-2019-02-21-at-3.56.31-PM.png?w=3840&q=90&fm=webp)

Agents’ policies are sampled uniformly from a number of populations—agents in different populations share architectures, but only agents in the same population share weights. Initial experiments show that agent competence scales with increasing multiagent interaction. Increasing the maximum number of concurrent players magnifies exploration; increasing the number of populations magnifies niche formation—that is, the tendency of populations to spread out and forage within different parts of the map.

### Server merge tournaments: Multiagent magnifies competence

There is no standard procedure among MMOs for evaluating relative player competence across multiple servers. However, MMO servers sometimes undergo merges where the player bases from multiple servers are placed within a single server. We implement “tournament” style evaluation by merging the player bases trained in different servers. This allows us to directly compare the policies learned in different experiment settings. We vary test time scale and find that agents trained in larger settings consistently outperform agents trained in smaller settings.

### Increased population size magnifies exploration

Loading...

In the natural world, competition among animals can incentivize them to spread out to avoid conflict. We observe that map coverage increases as the number of concurrent agents increases. Agents learn to explore only because the presence of other agents provides a natural incentive for doing so.

### Increased species count magnifies niche formation

![Three panels compare agent movement patterns on a game map, showing that training with 8 species leads to broader and more diverse visitation across the environment than training with a single species.](https://images.ctfassets.net/kftzwdyauwt9/a40d2564-7360-461b-d9748a069305/7f33e2df5eb4a1ca1fdfb3ba48d11758/Screen-Shot-2019-02-21-at-1.13.45-PM.png?w=3840&q=90&fm=webp)

Given a sufficiently large and resource-rich environment, we found different populations of agents separated across the map to avoid competing with others as the populations increased. As entities cannot out-compete other agents of their own population (i.e., agents with whom they share weights), they tend to seek areas of the map that contain enough resources to sustain their population. Similar effects were also independently observed in [concurrent multiagent research by DeepMind⁠(opens in a new window)](https://arxiv.org/abs/1812.07019).

## Additional insights

![Heatmaps visualize spatial value distributions around agents.](https://images.ctfassets.net/kftzwdyauwt9/fd8119d1-2ce7-42f5-79ce36f587b7/bb6102a08069b40336899010df8384ee/Screen-Shot-2019-03-04-at-8.24.55-AM.png?w=3840&q=90&fm=webp)

We visualize agent-agent dependencies by fixing an agent at the center of a hypothetical map crop. For each position visible to that agent, we show what the value function would be if there were a second agent at that position. We find that agents learn policies dependent on those of other agents, in both the foraging and combat environments. Agents learn “bull’s eye” avoidance maps to begin foraging more effectively after only a few minutes of training. As agents learn the combat mechanics of the environment, they begin to appropriately value effective engagement ranges and angles of approach.

## Next steps

Our Neural MMO resolves two key limitations of previous game-based environments, but there are still many left unsolved. This Neural MMO strikes a middle ground between [environment⁠](/five/) [complexity⁠(opens in a new window)](https://deepmind.com/blog/alphastar-mastering-real-time-strategy-game-starcraft-ii/) and [population⁠(opens in a new window)](https://arxiv.org/abs/1712.00600) [scale⁠(opens in a new window)](https://arxiv.org/abs/1709.04511). We’ve designed this environment with open-source expansion in mind and for the research community to build upon.

If you are excited about conducting research on multiagent systems, consider [joining⁠](/careers/) OpenAI.

* [OpenAI Five](/research/index/?tags=openai-five)
* [Exploration & Games](/research/index/?tags=exploration-game)
* [Learning Paradigms](/research/index/?tags=learning-paradigms)
* [Multi-agent](/research/index/?tags=multi-agent)
* [Simulated Environments](/research/index/?tags=simulated-environments)
* [Robotics](/research/index/?tags=robotics)

## Authors

Joseph Suarez, Yilun Du, Phillip Isola, Igor Mordatch

## Acknowledgments

Thanks to Clare Zhu for her substantial work on the 3D client.

We also thank the following for feedback on drafts of this post: Greg Brockman, Ilya Sutskever, Jack Clark, Ashley Pilipiszyn, Ryan Lowe, Julian Togelius, Joel Liebo, Cinjon Resnick.

## Related articles

![Whisper](https://images.ctfassets.net/kftzwdyauwt9/13c810cb-0592-442d-190ab7378bef/a7cb2299d034abe93023f662f8d32263/Speech_Rec_16_9.png?w=3840&q=90&fm=webp)

[Introducing Whisper

ReleaseSep 21, 2022](/index/whisper/)

![Screenshot of a scene from Minecraft](https://images.ctfassets.net/kftzwdyauwt9/ef9fc360-1a5a-4ca3-5c25b83b3564/50c07940455cc86ef84d91526d9cf3e0/vpt.jpg?w=3840&q=90&fm=webp)

[Learning to play Minecraft with Video PreTraining

ConclusionJun 23, 2022](/index/vpt/)

![Techniques For Training Large Neural Networks](https://images.ctfassets.net/kftzwdyauwt9/62793de4-0f01-42fc-539325d9af36/bc1ac82499fc1dc43f59accdd31d0195/image-9.webp?w=3840&q=90&fm=webp)

[Techniques for training large neural networks

PublicationJun 9, 2022](/index/techniques-for-training-large-neural-networks/)
