<!-- source: https://openai.com/index/robots-that-learn/ -->

May 16, 2017

[Milestone](/research/index/milestone/)

# Robots that learn

We’ve created a robotics system, trained entirely in simulation and deployed on a physical robot, which can learn a new task after seeing it done once.

[Read paper (domain randomization)(opens in a new window)](https://arxiv.org/abs/1703.06907)[Read paper (one-shot imitation learning)(opens in a new window)](https://arxiv.org/abs/1703.07326)

![Robots That Learn](https://images.ctfassets.net/kftzwdyauwt9/9303995f-6ada-40ad-76fbe9bf02ea/79b67763dd00b101bcf1e21eff248aca/robots-that-learn.jpg?w=3840&q=90&fm=webp)

Illustration: Ben Barry

## Algorithms

Last month, we showed an [earlier version⁠(opens in a new window)](https://blog.openai.com/spam-detection-in-the-physical-world/) of this robot where we’d trained its vision system using [domain randomization⁠(opens in a new window)](https://arxiv.org/abs/1703.06907), that is, by showing it simulated objects with a variety of color, backgrounds, and textures, without the use of any real images.

Now, we’ve developed and deployed a new algorithm, [one-shot imitation learning⁠(opens in a new window)](https://arxiv.org/abs/1703.07326), allowing a human to communicate how to do a new task by performing it in [VR⁠(opens in a new window)](https://en.wikipedia.org/wiki/Virtual_reality). Given a single demonstration, the robot is able to solve the same task from an arbitrary starting configuration.

## General procedure

![Stacking Demo](https://images.ctfassets.net/kftzwdyauwt9/7c8cee91-0a4e-4a47-9ed2bd64af2c/9a783be91492634924703c801a653fbd/stacking_demo.gif?w=3840&q=90&fm=webp)

Our system can learn a behavior from a single demonstration delivered within a simulator, then reproduce that behavior in different setups in reality.

The system is powered by two neural networks: a vision network and an imitation network.

The vision network ingests an image from the robot’s camera and outputs state representing the positions of the objects. As [before⁠(opens in a new window)](https://blog.openai.com/spam-detection-in-the-physical-world/), the vision network is trained with hundreds of thousands of simulated images with different perturbations of lighting, textures, and objects. (The vision system is never trained on a real image.)

The imitation network observes a demonstration, processes it to infer the intent of the task, and then accomplishes the intent starting from another starting configuration. Thus, the imitation network must generalize the demonstration to a new setting. But how does the imitation network know how to generalize?

The network learns this from the distribution of training examples. It is trained on dozens of different tasks with thousands of demonstrations for each task. Each training example is a pair of demonstrations that perform the same task. The network is given the entirety of the first demonstration and a single observation from the second demonstration. We then use supervised learning to predict what action the demonstrator took at that observation. In order to predict the action effectively, the robot must learn how to infer the relevant portion of the task from the first demonstration.

Applied to block stacking, the training data consists of pairs of trajectories that stack blocks into a matching set of towers in the same order, but start from different start states. In this way, the imitation network learns to match the demonstrator’s ordering of blocks and size of towers without worrying about the relative location of the towers.

## Block stacking

The task of creating color-coded stacks of blocks is simple enough that we were able to solve it with a scripted policy in simulation. We used the scripted policy to generate the training data for the imitation network. At test time, the imitation network was able to parse demonstrations produced by a human, even though it had never seen messy human data before.

The imitation network uses [soft attention⁠(opens in a new window)](https://arxiv.org/abs/1409.0473) over the demonstration trajectory and the state vector which represents the locations of the blocks, allowing the system to work with demonstrations of variable length. It also performs attention over the locations of the different blocks, allowing it to imitate longer trajectories than it’s ever seen, and stack blocks into a configuration that has more blocks than any demonstration in its training data.

For the imitation network to learn a robust policy, we had to inject a modest amount of noise into the outputs of the scripted policy. This forced the scripted policy to demonstrate how to recover when things go wrong, which taught the imitation network to deal with the disturbances from an imperfect policy. Without injecting the noise, the policy learned by the imitation network would usually fail to complete the stacking task.

If you’d like to help us build this robot, [join us⁠](/careers/) at OpenAI.

* [Simulated Environments](/research/index/?tags=simulated-environments)
* [Robotics](/research/index/?tags=robotics)
* [Learning Paradigms](/research/index/?tags=learning-paradigms)

## Authors

Peter Welinder, Bob McGrew, Jonas Schneider, Yan Duan, Josh Tobin, Rachel Fong, Alex Ray, Filip Wolski, Vikash Kumar, Jonathan Ho

## Authors

Marcin Andrychowicz, Bradly Stadie, Ankur Handa, Matthias Plappert, Erika Reinhardt, Pieter Abbeel, Greg Brockman, Ilya Sutskever, Jack Clark, Wojciech Zaremba

## Related articles

![Point E A System For Generating 3d Point Clouds From Complex Prompts](https://images.ctfassets.net/kftzwdyauwt9/7e4ba260-7655-4049-5a2568c94158/2f2af956a356ee2b507296d01e45e766/image-5.webp?w=3840&q=90&fm=webp)

[Point-E: A system for generating 3D point clouds from complex prompts

PublicationDec 16, 2022](/index/point-e/)

![Multimodal Neurons](https://images.ctfassets.net/kftzwdyauwt9/e16f419f-09bf-4266-7ca3cdd2ae33/0a11dd23053f257828e7c68a815cd632/multimodal-neurons.png?w=3840&q=90&fm=webp)

[Multimodal neurons in artificial neural networks

MilestoneMar 4, 2021](/index/multimodal-neurons/)

![CLIP](https://images.ctfassets.net/kftzwdyauwt9/5e490f66-703f-4228-221ca64049ed/8ed4358ba4b9f8779e07a2b15d7256e1/image_125.png?w=3840&q=90&fm=webp)

[CLIP: Connecting text and images

MilestoneJan 5, 2021](/index/clip/)
