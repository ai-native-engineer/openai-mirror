<!-- source: https://openai.com/index/sim-to-real-transfer-of-robotic-control-with-dynamics-randomization/ -->

October 18, 2017

[Publication](/research/index/publication/)

# Sim-to-real transfer of robotic control with dynamics randomization

[Read paper(opens in a new window)](https://arxiv.org/abs/1710.06537)

![Sim To Real Transfer Of Robotic Control With Dynamics Randomization](https://images.ctfassets.net/kftzwdyauwt9/4355603c-38f0-4654-756530801efe/cacb8e12df1acd77b82e38f7c173701d/image-62.webp?w=3840&q=90&fm=webp)

## Abstract

Simulations are attractive environments for training agents as they provide an abundant source of data and alleviate certain safety concerns during the training process. But the behaviours developed by agents in simulation are often specific to the characteristics of the simulator. Due to modeling error, strategies that are successful in simulation may not transfer to their real world counterparts. In this paper, we demonstrate a simple method to bridge this "reality gap". By randomizing the dynamics of the simulator during training, we are able to develop policies that are capable of adapting to very different dynamics, including ones that differ significantly from the dynamics on which the policies were trained. This adaptivity enables the policies to generalize to the dynamics of the real world without any training on the physical system. Our approach is demonstrated on an object pushing task using a robotic arm. Despite being trained exclusively in simulation, our policies are able to maintain a similar level of performance when deployed on a real robot, reliably moving an object to a desired location from random initial configurations. We explore the impact of various design decisions and show that the resulting policies are robust to significant calibration error.

* [Simulated Environments](/research/index/?tags=simulated-environments)
* [Robotics](/research/index/?tags=robotics)

## Authors

Xue Bin Peng, Marcin Andrychowicz, Wojciech Zaremba, Pieter Abbeel

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
