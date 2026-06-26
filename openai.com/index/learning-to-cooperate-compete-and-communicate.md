<!-- source: https://openai.com/index/learning-to-cooperate-compete-and-communicate/ -->

June 8, 2017

[Publication](/research/index/publication/)

# Learning to cooperate, compete, and communicate

[View code(opens in a new window)](https://github.com/openai/multiagent-particle-envs)[Read paper(opens in a new window)](https://arxiv.org/abs/1706.02275)

![Learning To Cooperate Compete And Communicate](https://images.ctfassets.net/kftzwdyauwt9/a3167a62-8b16-4837-a885b1647794/348739c5737599b1bb35d48041de5300/image-71.webp?w=3840&q=90&fm=webp)

Multiagent environments where agents compete for resources are stepping stones on the path to AGI. Multiagent environments have two useful properties: first, there is a natural curriculum—the difficulty of the environment is determined by the skill of your competitors (and if you’re competing against clones of yourself, the environment exactly matches your skill level). Second, a multiagent environment has no stable equilibrium: no matter how smart an agent is, there’s always pressure to get smarter. These environments have a very different feel from traditional environments, and it’ll take a lot more research before we become good at them.

We’ve developed a new algorithm, [MADDPG⁠(opens in a new window)](https://arxiv.org/abs/1706.02275), for centralized learning and decentralized execution in multiagent environments, allowing agents to learn to collaborate and compete with each other.

![Chase Gif Final](https://images.ctfassets.net/kftzwdyauwt9/1b2613b7-91d6-41cb-8605df59a017/51cecbd204417f3730b69d3af64f989c/chase_gif_final.gif?w=3840&q=90&fm=webp)

MADDPG used to train four red agents to chase two green agents. The red agents have learned to team up with one another to chase a single green agent, gaining higher reward. The green agents, meanwhile, learned to split up, and while one is being chased the other tries to approach the water (blue circle) while avoiding the red agents.

MADDPG extends a reinforcement learning algorithm called [DDPG⁠(opens in a new window)](https://arxiv.org/abs/1509.02971), taking inspiration from [actor-critic reinforcement learning⁠(opens in a new window)](http://webber.physik.uni-freiburg.de/~hon/vorlss02/Literatur/sutton/6/node7.html) techniques; other groups are [exploring⁠(opens in a new window)](https://arxiv.org/abs/1605.07736) [variations⁠(opens in a new window)](https://arxiv.org/abs/1605.06676) and [parallel implementations⁠(opens in a new window)](https://arxiv.org/abs/1705.08926) of these ideas.

We treat each agent in our simulation as an “actor”, and each actor gets advice from a “critic” that helps the actor decide what actions to reinforce during training. Traditionally, the critic tries to predict the *value* (i.e. the reward we expect to get in the future) of an action in a particular state, which is used by the agent—*the actor*—to update its policy. This is more stable than directly using the reward, which can vary considerably. To make it feasible to train multiple agents that can act in a globally-coordinated way, we enhance our critics so they can access the observations and actions of all the agents, as the following diagram shows.

![Nipsdiagram 2](https://images.ctfassets.net/kftzwdyauwt9/764afdf0-e3f5-4164-baec774d815d/1a474a9eb8b652ee3e73c2e5c74e26cc/nipsdiagram_2.gif?w=3840&q=90&fm=webp)

Our agents don’t need to access the central critic at test time; they act based on their observations in combination with their predictions of other agents behaviors’. Since a centralized critic is learned independently for each agent, our approach can also be used to model arbitrary reward structures between agents, including adversarial cases where the rewards are opposing.

Loading...

We tested our approach on a variety of tasks and it performed better than DDPG on all of them. In the above animations you can see, from left to right: two AI agents trying to go to a specific location and learning to split up to hide their intended location from the opposing agent; one agent communicating the name of a [landmark to another agent⁠(opens in a new window)](https://blog.openai.com/learning-to-communicate/); and three agents coordinating to travel to landmarks without bumping into each other.

Loading...

## Where traditional RL struggles

Traditional decentralized RL approaches—DDPG, actor-critic learning, deep Q-learning, and so on—struggle to learn in multiagent environments, as at every time step each agent will be trying to learn to predict the actions of other agents while also taking its own actions. This is especially true in competitive situations. MADDPG employs a centralized critic to supply agents with information about their peers’ observations and potential actions, transforming an unpredictable environment into a predictable one.

Using policy gradient methods presents further challenges: because these exhibit high variance learning the right policy is difficult to do when the reward is inconsistent. We also found that adding in a critic, while improving stability, still failed to solve several of our environments such as cooperative communication. It seems that considering the actions of others during training is important for learning collaborative strategies.

## Initial research

Before we developed MADDPG, when using decentralized techniques, we noticed that listener agents would often learn to ignore the speaker if it sent inconsistent messages about where to go to. The agent would then set all the weights associated with the speaker’s message to 0, effectively deafening itself. Once this happens, it’s hard for training to recover, since the speaker will never know if it says the right thing due to the absence of any feedback. To fix this, we looked at a technique outlined in [a recent hierarchical reinforcement project⁠(opens in a new window)](https://arxiv.org/abs/1703.01161), which lets us force the listener to incorporate the utterances of the speaker in its decision-making process. This fix didn’t work, because though it forces the listener to pay attention to the speaker, it doesn’t help the speaker figure out what to say that is relevant. Our centralized critic method helps deal with these challenges, by helping the speaker to learn which utterances might be relevant to the actions of other agents. For more of our results, you can watch the following video:

## Next steps

Agent modeling has a [rich history⁠(opens in a new window)](https://link.springer.com/article/10.1007/s10458-005-2631-2) within artificial intelligence research and many of these scenarios have been studied before. Lots of [previous research⁠(opens in a new window)](http://ieeexplore.ieee.org/document/4445757/) considered games with only a small number of time steps with a small state space. Deep learning lets us deal with complex visual inputs and RL gives us tools to learn behaviors over long time periods. Now that we can use these capabilities to train multiple-agents at once without them needing to know the dynamics of the environment (how the environment changes at each time-step), we can tackle a wider range of problems involving communication and language while learning from environments’ high-dimensional information. If you’re interesting in exploring different approaches to evolving agents then consider [joining OpenAI⁠](/careers/).

* [Learning Paradigms](/research/index/?tags=learning-paradigms)
* [Multi-agent](/research/index/?tags=multi-agent)
* [Simulated Environments](/research/index/?tags=simulated-environments)
* [Exploration & Games](/research/index/?tags=exploration-game)

## Authors

Ryan Lowe, Igor Mordatch, Pieter Abbeel, Yi Wu, Aviv Tamar, Jean Harb

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
