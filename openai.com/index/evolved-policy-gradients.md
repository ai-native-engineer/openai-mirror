<!-- source: https://openai.com/index/evolved-policy-gradients/ -->

April 18, 2018

[Milestone](/research/index/milestone/)

# Evolved Policy Gradients

[Read paper(opens in a new window)](https://arxiv.org/abs/1802.04821)[View code(opens in a new window)](https://github.com/openai/EPG)

![Evolved Policy Gradients](https://images.ctfassets.net/kftzwdyauwt9/d915bb1d-d402-4648-35baa0a0a809/63757b5fc87fe396d4b0bb87a560d833/image_148.png?w=3840&q=90&fm=webp)

We’re releasing an experimental metalearning approach called Evolved Policy Gradients, a method that evolves the loss function of learning agents, which can enable fast training on novel tasks. Agents trained with EPG can succeed at basic tasks at test time that were outside their training regime, like learning to navigate to an object on a different side of the room from where it was placed during training.

EPG trains agents to have a prior notion of what constitutes making progress on a novel task. Rather than encoding prior knowledge through a learned policy network, EPG encodes it as a learned [loss⁠(opens in a new window)](https://en.wikipedia.org/wiki/Loss_function) [function⁠(opens in a new window)](https://arxiv.org/abs/1506.05254). Agents are then able to use this loss function, defined as a temporal-convolutional neural network, to learn quickly on a novel task. We’ve shown that EPG can generalize to *out of distribution* test time tasks, exhibiting behavior qualitatively different from other popular metalearning algorithms. In tests, we’ve also found that EPG can train agents faster than [PPO⁠(opens in a new window)](https://blog.openai.com/openai-baselines-ppo/), an off-the-shelf policy gradient method. EPG is related to previous work on [evolving⁠(opens in a new window)](http://www2.hawaii.edu/~nreed/ics606/papers/Ackley91learningEvolution.pdf) [reward⁠(opens in a new window)](http://www.ece.uvic.ca/~bctill/papers/ememcog/Niekum_etal_2010.pdf) [functions⁠(opens in a new window)](https://web.eecs.umich.edu/~baveja/Papers/IJCAIGSLL2016.pdf) [for⁠(opens in a new window)](https://papers.nips.cc/paper/4146-reward-design-via-online-gradient-ascent.pdf) RL agents, but generalizes this idea to evolving a complete loss function, which means that the loss function has to effectively learn an RL algorithm internally.

Loading...

The intuition behind EPG comes from something we are all familiar with: trying to pick up a new skill and experiencing the alternating frustration and joy involved in that process. Suppose you are just starting out learning to play the violin. Even without instruction, you will immediately have a feel for what to try, and, listening to the sounds you produce, you will have a sense of whether or not you are making progress – that’s because you effectively have access to very well shaped [internal reward functions⁠(opens in a new window)](http://www-anw.cs.umass.edu/legacy/pubs/2009/singh_l_b_09.pdf), derived from prior experience on other motor tasks, and through the course of biological evolution. In contrast, most reinforcement learning (RL) agents approach each new task without using prior knowledge. Instead they rely entirely on external reward signals to guide their initial behavior. Coming from such a blank slate, it is no surprise that current RL agents take [far longer⁠(opens in a new window)](https://arxiv.org/abs/1604.00289) than humans to learn simple skills. EPG takes a step toward agents that are not blank slates but instead know what it means to make progress on a new task, by having experienced making progress on similar tasks in the past.

![Flow diagram](https://images.ctfassets.net/kftzwdyauwt9/f8efe739-e20d-4f16-7e0f83f857bc/062b0c09ee365c23ba5f111969f36221/fig1_4.gif?w=3840&q=90&fm=webp)

EPG consists of two optimization loops. In the inner loop, an agent learns, from scratch, to solve a particular task sampled from a family of tasks. The family of tasks might be “move gripper to target location [x, y]” and one particular task in this family could be “move gripper to position [50, 100]”. The inner loop uses [stochastic gradient descent⁠(opens in a new window)](https://en.wikipedia.org/wiki/Stochastic_gradient_descent) (SGD) to optimize the agent’s policy against a loss function proposed by the outer loop. The outer loop evaluates the returns achieved after inner-loop learning and adjusts the parameters of the loss function, using [Evolution Strategies⁠(opens in a new window)](https://blog.openai.com/evolution-strategies/) (ES), to propose a new loss that will lead to higher returns.

Having a learned loss offers several advantages compared to current RL methods: using ES to evolve the loss function allows us to optimize the true objective (final trained policy performance) rather than short-term returns, and EPG improves on standard RL algorithms by allowing the loss function to be adaptive to the environment and agent history.

Loading...

There has been a flurry of recent [work⁠(opens in a new window)](https://arxiv.org/abs/1611.02779) [on⁠(opens in a new window)](https://arxiv.org/abs/1611.05763) [metalearning⁠(opens in a new window)](https://arxiv.org/abs/1707.03141) [policies⁠(opens in a new window)](https://arxiv.org/abs/1703.03400), and it’s worth asking why learn a loss function as opposed to directly learning a policy? Learning recurrent policies tends to overfit the task at hand, while learning policy initializations has limited expressivity when it comes to exploration. Our motivation is that we expect loss functions to be the kind of object that may generalize very well across substantially different tasks. This is certainly true of hand-engineered loss functions: a well-designed RL loss function, such as that in [PPO⁠(opens in a new window)](https://blog.openai.com/openai-baselines-ppo/), can be very generically applicable, finding use in problems ranging from playing Atari games to controlling robots.

To test the generalization ability of EPG, we conducted a simple experiment. We evolved the EPG loss to be effective at getting “ants” to walk to randomly located targets on the right half of an arena. Then, we froze the loss, and gave the ants a new target, this time on the *left* half of the arena. Surprisingly, the ants learned to walk to the left! Here is how their learning curves looked (red lines on graphs):

![Learning curves](https://images.ctfassets.net/kftzwdyauwt9/d9b72ebc-866a-4a1a-0d94145c6d3f/f465c0c3819478c75e0548cf8c424869/fig2_4.png?w=3840&q=90&fm=webp)

This result is exciting to us because it demonstrates generalization to a task *outside the training distribution*. This kind of generalization can be quite hard to achieve. We compared EPG to an alternative metalearning algorithm, called [RL2⁠(opens in a new window)](https://arxiv.org/abs/1611.02779), which tries to directly learn a policy that can adapt to novel tasks. In our experiment, RL2 was indeed successful at getting agents to walk to targets on the right half of the screen. However, when given a test time target on the left half of the screen, it qualitatively failed, and just kept walking to the right. In a sense, it “overfit” to the set of tasks on which it was trained (i.e. walking to the right).

Loading...

As do all metalearning approaches, our method still has many limitations. Right now, we can train an EPG loss to be effective for one small family of tasks at a time, e.g., getting an ant to walk left and right. However, the EPG loss for this family of tasks is unlikely to be at all effective on a wildly different kind of task, like playing Space Invaders. In contrast, standard RL losses *do* have this level of generality—the same loss function can be used to learn a huge variety of skills. EPG gains on performance by losing on generality. There is a long road ahead toward metalearning methods that both outperform standard RL methods *and* have the same level of generality.

* [Learning Paradigms](/research/index/?tags=learning-paradigms)

## Authors

Rein Houthooft, Richard Chen, Phillip Isola, Bradly Stadie, Filip Wolski, Jonathan Ho, Pieter Abbeel

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
