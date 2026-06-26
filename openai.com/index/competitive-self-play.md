<!-- source: https://openai.com/index/competitive-self-play/ -->

October 11, 2017

[Milestone](/research/index/milestone/)

# Competitive self-play

[View code(opens in a new window)](https://github.com/openai/multiagent-competition)[Read paper(opens in a new window)](https://arxiv.org/abs/1710.03748)

![Competitive Self Play](https://images.ctfassets.net/kftzwdyauwt9/b280dd57-ff0c-4f1a-746042cb93a9/4600fb9bd871e443f99cb3c78704a4bd/competitive-self-play.jpg?w=3840&q=90&fm=webp)

Illustration: Ben Barry

We’ve found that self-play allows simulated AIs to discover physical skills like tackling, ducking, faking, kicking, catching, and diving for the ball, without explicitly designing an environment with these skills in mind. Self-play ensures that the environment is always the right difficulty for an AI to improve. Taken alongside our Dota 2 self-play results, we have increasing confidence that self-play will be a core part of powerful AI systems in the future.

We set up competitions between multiple simulated 3D robots on a range of basic games, trained each agent with simple goals (push the opponent out of the sumo ring, reach the other side of the ring while preventing the other agent from doing the same, kick the ball into the net or prevent the other agent from doing so, and so on), then analyzed the different strategies that emerged.

Agents initially receive dense rewards for behaviours that aid exploration like standing and moving forward, which are eventually annealed to zero in favor of being rewarded for just winning and losing. Despite the simple rewards, the agents learn subtle behaviors like tackling, ducking, faking, kicking and catching, and diving for the ball. Each agent’s neural network policy is independently trained with [Proximal Policy Optimization⁠(opens in a new window)](https://arxiv.org/abs/1707.06347).

Loading...

To understand how complex behaviors can emerge through a combination of simple goals and competitive pressure, let’s analyze the sumo wrestling task. Here we took the dense reward defined in [previous work⁠(opens in a new window)](https://arxiv.org/abs/1506.02438) for training a humanoid to walk, removed the term for velocity, added the negative L2 distance from the center of the ring and took this as a dense exploration reward for our sumo agents. The agents were allowed to use this reward for exploration in the ring initially, then we slowly annealed it to zero so the agents would learn to optimize for the competition reward — pushing the other player out of the ring — for the remaining training iterations.

Loading...

Though it is possible to design tasks and environments that require each of these skills, this requires effort and ingenuity on the part of human designers, and the agents’ behaviors will be bounded in complexity by the problems that the human designer can pose for them. By developing agents through thousands of iterations of matches against successively better versions of themselves, we can create AI systems that successively bootstrap their own performance; we saw a similar phenomenon in our [Dota 2 project⁠](/index/more-on-dota-2/), where self-play let us create an RL agent that could beat top human players at a solo version of the e-sport.

## Transfer Learning

Loading...

These agents also exhibit transfer learning, applying skills learned in one setting to succeed in another never-before-seen one. In one case, we took the agent trained on the self-play sumo wrestling task and faced it with the task of standing while being perturbed by “wind” forces. The agent managed to stay upright despite never seeing the windy environment or observing wind forces, while agents trained to walk using classical reinforcement learning would fall over immediately.

Loading...

## Overfitting

Our agents were overfitting by co-learning policies that were precisely tailored to counter specific opponents, but would fail when facing new ones with different characteristics. We dealt with this by pitting each agent against several different opponents rather than just one. These possible opponents come from an ensemble of policies that were trained in parallel as well as policies from earlier in the training process. Given this diversity of opponents, agents needed to learn general strategies and not just ones targeted to a specific opponent.

Additionally, we’re [releasing⁠(opens in a new window)](https://github.com/openai/multiagent-competition) the MuJoCo environments and trained policies used in this work so that others can experiment with these systems. If you’d like to work on self-play systems, we’re [hiring⁠](/careers/)!

* [Simulated Environments](/research/index/?tags=simulated-environments)
* [Exploration & Games](/research/index/?tags=exploration-game)
* [Transformers](/research/index/?tags=transformers)
* [Multi-agent](/research/index/?tags=multi-agent)

## Authors

Trapit Bansal, Igor Mordatch, Jakub Pachocki, Ilya Sutskever, Szymon Sidor

## Related articles

![Scaling Laws For Reward Model Overoptimization](https://images.ctfassets.net/kftzwdyauwt9/a8801fe6-8892-472b-f746d1d9fb2d/547c46ed9a8a71e89efbb7a7963a8932/image-6.webp?w=3840&q=90&fm=webp)

[Scaling laws for reward model overoptimization

PublicationOct 19, 2022](/index/scaling-laws-for-reward-model-overoptimization/)

![Screenshot of a scene from Minecraft](https://images.ctfassets.net/kftzwdyauwt9/ef9fc360-1a5a-4ca3-5c25b83b3564/50c07940455cc86ef84d91526d9cf3e0/vpt.jpg?w=3840&q=90&fm=webp)

[Learning to play Minecraft with Video PreTraining

ConclusionJun 23, 2022](/index/vpt/)

![CLIP](https://images.ctfassets.net/kftzwdyauwt9/5e490f66-703f-4228-221ca64049ed/8ed4358ba4b9f8779e07a2b15d7256e1/image_125.png?w=3840&q=90&fm=webp)

[CLIP: Connecting text and images

MilestoneJan 5, 2021](/index/clip/)
