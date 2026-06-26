<!-- source: https://openai.com/index/learning-to-model-other-minds/ -->

September 14, 2017

[Publication](/research/index/publication/)

# Learning to model other minds

[Read paper(opens in a new window)](https://arxiv.org/abs/1709.04326)[(opens in a new window)](https://github.com/alshedivat/lola)

![Learning To Model Other Minds](https://images.ctfassets.net/kftzwdyauwt9/3c4a6e91-7857-4f36-90b7f5c7c83f/38710fef7095393478f9184908d8124c/image-64.webp?w=3840&q=90&fm=webp)

We’re releasing an algorithm which accounts for the fact that other agents are learning too, and discovers self-interested yet collaborative strategies like tit-for-tat in the iterated prisoner’s dilemma. This algorithm, Learning with Opponent-Learning Awareness (LOLA), is a small step towards agents that model other minds.

LOLA, a collaboration by researchers at OpenAI and the University of Oxford, lets a reinforcement learning (RL) agent take account of the learning of others when updating its own strategy. Each LOLA agent adjusts its policy in order to shape the learning of the other agents in a way that is advantageous. This is possible since the learning of the other agents depends on the rewards and observations occurring in the environment, which in turn can be influenced by the agent.

This means that the LOLA agent, “Alice,” models how the parameter updates of the other agent, “Bob,” depend on its own policy and how Bob’s parameter update impacts its own future expected reward. Alice then updates its own policy in order to make the learning step of the other agents, like Bob, more beneficial to its own goals.

LOLA agents can discover effective, reciprocative strategies, in games like the iterated [*prisoner’s dilemma*⁠(opens in a new window)](http://www.econlib.org/library/Enc/PrisonersDilemma.html), or the [coin game⁠(opens in a new window)](https://arxiv.org/abs/1707.01068). In contrast, state-of-the-art deep reinforcement learning methods, like Independent PPO, fail to learn such strategies in these domains. These agents typically learn to take selfish actions that ignore the objectives of other agents. LOLA solves this by letting agents act out of a self-interest that incorporates the goals of others. It also works without requiring hand-crafted rules, or environments set up to encourage cooperation.

The inspiration for LOLA comes from how people collaborate with one another: Humans are great at reasoning about how their actions can affect the future behavior of other humans, and frequently invent ways to collaborate with others that leads to a win–win. One of the reasons humans are good at collaborating with each other is that they have a sense of a “theory of mind” about other humans, letting them come up with strategies that lead to benefits for their collaborators. So far, this sort of “theory of mind” representation has been absent from deep multi-agent reinforcement learning. To a state of the art deep-RL agent there is no inherent difference between another learning agent and a part of the environment, say a tree.

The key to LOLA’S performance is the inclusion of term:

(∂V1(θi1,θi2)∂θi2)T∂2V2(θi1,θi2)∂θi1∂θi2⋅δη,\left( \frac{\partial V^1 (\theta^1\_i,\theta^2\_i) }{\partial \theta^2\_i} \right)^T \frac{\partial^2 V^2 (\theta^1\_i,\theta^2\_i)}{\partial \theta^1\_i \partial \theta^2\_i} \cdot \delta \eta,(∂θi2​∂V1(θi1​,θi2​)​)T∂θi1​∂θi2​∂2V2(θi1​,θi2​)​⋅δη,

Here the left hand side captures how Alice’s return depends on the change in Bob’s policy. The right hand side, describes how Bob’s learning step depends on Alice’s policy. Multiplying those two components essentially measures how Alice can change Bob’s learning step such that it leads to an increase in Alice’s rewards.

This means that when we train our agents they try to optimize their return after one anticipated learning step of the opponent. By differentiating through this anticipated learning step the agent can actively shape the parameter update of the opponent in a way that increases their own return.

While the formula above assume access to the true gradient and hessian of the two value functions, we can also estimate all relevant terms using samples. In particular the second order term can be estimated by applying the policy gradient theorem, which makes LOLA suitable for any deep reinforcement learning setting.

LOLA can handle this by including a step of opponent modeling where we fit a model of the opponent to the observed trajectories—predicting the parameters of other agents based on their actions. In the future we would like to extend this by also inferring architectures and rewards from the observed learning.

![LOLA results](https://images.ctfassets.net/kftzwdyauwt9/8231dafe-99fb-4407-a97ab42e3916/28839b21e3eb21e82a8f10e367a67313/Screenshot-2017-09-13-10.44.04.png?w=3840&q=90&fm=webp)

LOLA works in situations where we can access the policy of the other agents (LOLA), as well as ones where we can only estimate the state of other agents from traces (LOLA-OM). Both approaches pick up a larger number of coins (left) and score a far greater number of points (right) than other approaches.

## Results

Loading...

LOLA lets us train agents that succeed at the [coin game⁠(opens in a new window)](https://arxiv.org/abs/1707.01068), in which two agents, red and blue, compete with one another to pick up red and blue colored coins. Each agent gets a point for picking up any coin, but if they pick up a coin which isn’t their color then the other agent will receive a –2 penalty. Thus, if both agents greedily pick up both coins, everyone gets zero points on average. LOLA agents learn to predominantly pick up coins of their own color, leading to high scores (shown above).

## Drawbacks

LOLA works best when using large batch-sizes and full roll-outs for variance reduction. This means that the method is both memory and compute intensive. Furthermore, under opponent modeling LOLA can exhibit instability which we hope to address with future improvements.

* [Learning Paradigms](/research/index/?tags=learning-paradigms)
* [Multi-agent](/research/index/?tags=multi-agent)
* [Simulated Environments](/research/index/?tags=simulated-environments)

## Authors

Jakob Foerster, Richard Chen, Pieter Abbeel, Igor Mordatch, Shimon Whiteson, Maruan Al-Shedivat

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
