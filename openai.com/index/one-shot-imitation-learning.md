<!-- source: https://openai.com/index/one-shot-imitation-learning/ -->

March 21, 2017

[Publication](/research/index/publication/)

# One-shot imitation learning

[Read paper(opens in a new window)](https://arxiv.org/abs/1703.07326)

![One Shot Imitation Learning](https://images.ctfassets.net/kftzwdyauwt9/883a4349-9568-4db3-13fa2eb1c8b7/d8ad21a28ff2921bee0e64275eec4ead/image-80.webp?w=3840&q=90&fm=webp)

## Abstract

Imitation learning has been commonly applied to solve different tasks in isolation. This usually requires either careful feature engineering, or a significant number of samples. This is far from what we desire: ideally, robots should be able to learn from very few demonstrations of any given task, and instantly generalize to new situations of the same task, without requiring task-specific engineering. In this paper, we propose a meta-learning framework for achieving such capability, which we call one-shot imitation learning.

Specifically, we consider the setting where there is a very large set of tasks, and each task has many instantiations. For example, a task could be to stack all blocks on a table into a single tower, another task could be to place all blocks on a table into two-block towers, etc. In each case, different instances of the task would consist of different sets of blocks with different initial states. At training time, our algorithm is presented with pairs of demonstrations for a subset of all tasks. A neural net is trained that takes as input one demonstration and the current state (which initially is the initial state of the other demonstration of the pair), and outputs an action with the goal that the resulting sequence of states and actions matches as closely as possible with the second demonstration. At test time, a demonstration of a single instance of a new task is presented, and the neural net is expected to perform well on new instances of this new task. The use of soft attention allows the model to generalize to conditions and tasks unseen in the training data. We anticipate that by training this model on a much greater variety of tasks and settings, we will obtain a general system that can turn any demonstrations into robust policies that can accomplish an overwhelming variety of tasks.

Videos available at [this https URL⁠(opens in a new window)](https://bit.ly/nips2017-oneshot) .

* [Robotics](/research/index/?tags=robotics)

## Authors

Yan Duan, Marcin Andrychowicz, Bradly Stadie, Jonathan Ho, Jonas Schneider, Ilya Sutskever, Pieter Abbeel, Wojciech Zaremba

## Related articles

![Outstretched robot arm solving a Rubik's cube in its palm in front of a cloudy purple background](https://images.ctfassets.net/kftzwdyauwt9/9267c72e-6cc1-42f6-d23abb5fa261/3bb199192cd8749d8adc83a71751833c/solving-rubiks-cube.jpg?w=3840&q=90&fm=webp)

[Solving Rubik’s Cube with a robot hand

MilestoneOct 15, 2019](/index/solving-rubiks-cube/)

![Learning Dexterity](https://images.ctfassets.net/kftzwdyauwt9/296c85d3-a3a1-448a-083f6b2029b1/695e55d1e8c1f265c5e8d9b1e9fda631/learning-dexterity.jpg?w=3840&q=90&fm=webp)

[Learning dexterity

MilestoneJul 30, 2018](/index/learning-dexterity/)

![Multi Goal Reinforcement Learning Challenging Robotics Environments And Request For Research](https://images.ctfassets.net/kftzwdyauwt9/bf0d1994-27c2-4cfa-f062b70d11c9/37d2a2c11b1486a6fe1685c1a79adfb5/image-55.webp?w=3840&q=90&fm=webp)

[Multi-Goal Reinforcement Learning: Challenging robotics environments and request for research

PublicationFeb 26, 2018](/index/multi-goal-reinforcement-learning/)
