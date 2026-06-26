<!-- source: https://openai.com/index/asymmetric-actor-critic-for-image-based-robot-learning/ -->

October 18, 2017

[Publication](/research/index/publication/)

# Asymmetric actor critic for image-based robot learning

[(opens in a new window)](https://arxiv.org/abs/1710.06542)

![Asymmetric Actor Critic For Image Based Robot Learning](https://images.ctfassets.net/kftzwdyauwt9/c9603185-d85f-4fa4-08f7d3f577d5/a919014ef3188ed743c9b0e4de8c55bd/image-61.webp?w=3840&q=90&fm=webp)

## Abstract

Deep reinforcement learning (RL) has proven a powerful technique in many sequential decision making domains. However, Robotics poses many challenges for RL, most notably training on a physical system can be expensive and dangerous, which has sparked significant interest in learning control policies using a physics simulator. While several recent works have shown promising results in transferring policies trained in simulation to the real world, they often do not fully utilize the advantage of working with a simulator. In this work, we exploit the full state observability in the simulator to train better policies which take as input only partial observations (RGBD images). We do this by employing an actor-critic training algorithm in which the critic is trained on full states while the actor (or policy) gets rendered images as input. We show experimentally on a range of simulated tasks that using these asymmetric inputs significantly improves performance. Finally, we combine this method with domain randomization and show real robot experiments for several tasks like picking, pushing, and moving a block. We achieve this simulation to real world transfer without training on any real world data.

* [Robotics](/research/index/?tags=robotics)

## Authors

Lerrel Pinto, Marcin Andrychowicz, Peter Welinder, Wojciech Zaremba, Pieter Abbeel

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
