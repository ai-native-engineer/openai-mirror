<!-- source: https://openai.com/index/spam-detection-in-the-physical-world/ -->

April 1, 2017

[Conclusion](/research/index/conclusion/)

# Spam detection in the physical world

We’ve created the world’s first Spam-detecting AI trained entirely in simulation and deployed on a physical robot.

![Video recording still of a robotic arm picking up a mixture of items on a small square table](https://images.ctfassets.net/kftzwdyauwt9/2614ea0f-57ca-4707-1eb4aafd8adf/27cd1ded47c9979f1590091a35435ca7/image-77.webp?w=3840&q=90&fm=webp)

![Video recording still of a robotic arm picking up a mixture of items on a small square table](https://images.ctfassets.net/kftzwdyauwt9/b61dd248-b0d5-4831-adf1bacb244a/0089f28a12c4ff9c3ea95d6351cc07e4/fetch_spam_wide_shot5.gif?w=3840&q=90&fm=webp)

## Sim-to-real transfer

Deep learning-driven robotic systems are bottlenecked by data collection: it’s extremely costly to obtain the hundreds of thousands of images needed to train the perception system alone. It’s cheap to generate simulated data, but simulations diverge enough from reality that people typically retrain models from scratch when moving to the physical world.

We’ve [shown⁠(opens in a new window)](https://arxiv.org/abs/1703.06907) that domain randomization, an existing idea for making detectors trained on simulated images transfer to real images, works well for cluttered scenes. The method is simple: we randomly vary colors, textures, lighting conditions, and camera settings in simulated scenes. The resulting dataset is sufficiently variable to allow a deep neural network trained on it to generalize to reality.

![Train](https://images.ctfassets.net/kftzwdyauwt9/3f839582-2a5d-43b5-e1b423f4a827/9a2b78f1c202b06e80cc435dbe5ea1f0/train.gif?w=3840&q=90&fm=webp)

Randomly generated scenes. Each frame contains Spam, often hidden among distractor objects. Our Spam model is sourced from the YCB dataset.

## Our implementation

The detector is a neural network based on the [VGG16⁠(opens in a new window)](https://www.cs.toronto.edu/~frossard/post/vgg16/) architecture that predicts the precise 3-D location of Spam in simulated images. Though it has only been trained on simulated scenes, the resulting network is able to detect Spam in real images, even in the presence of never-before-seen “distractor” items arranged in random configurations.

The video below demonstrates the system in action:

## Future work

In the future, we plan to extend this work to detect [phishing⁠(opens in a new window)](https://en.wikipedia.org/wiki/Phishing) and to defend against [adversarial⁠](/index/attacking-machine-learning-with-adversarial-examples/) Spam.

![Video recording still of a can of tuna next to a can of spam wearing costume glasses](https://images.ctfassets.net/kftzwdyauwt9/f7c0c175-3ca4-48c0-2475f257d3dc/9ed40202322e75180679bbf4c98a7427/future-work-still-sm.jpg?w=3840&q=90&fm=webp)

If you’d like to sink your teeth into compelling applied research problems like Spam detection, consider [joining us⁠](/careers/) at OpenAI.

* [Simulated Environments](/research/index/?tags=simulated-environments)
* [Robotics](/research/index/?tags=robotics)

## Authors

Rachel Fong, Josh Tobin, Jack Clark, Alex Ray, Jonas Schneider, Pieter Abbeel, Wojciech Zaremba

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
