<!-- source: https://openai.com/index/a-connection-between-generative-adversarial-networks-inverse-reinforcement-learning-and-energy-based-models/ -->

November 11, 2016

[Publication](/research/index/publication/)

# A connection between generative adversarial networks, inverse reinforcement learning, and energy-based models

[Read paper(opens in a new window)](https://arxiv.org/abs/1611.03852)

![A Connection Between Generative Adversarial Networks Inverse Reinforcement Learning And Energy Based Models](https://images.ctfassets.net/kftzwdyauwt9/b2f86a82-8a28-4a17-2d63b27e59c5/d9e87832ea4761bd97615069a2b15e93/image-10.webp?w=3840&q=90&fm=webp)

## Abstract

Generative adversarial networks (GANs) are a recently proposed class of generative models in which a generator is trained to optimize a cost function that is being simultaneously learned by a discriminator. While the idea of learning cost functions is relatively new to the field of generative modeling, learning costs has long been studied in control and reinforcement learning (RL) domains, typically for imitation learning from demonstrations. In these fields, learning cost function underlying observed behavior is known as inverse reinforcement learning (IRL) or inverse optimal control. While at first the connection between cost learning in RL and cost learning in generative modeling may appear to be a superficial one, we show in this paper that certain IRL methods are in fact mathematically equivalent to GANs. In particular, we demonstrate an equivalence between a sample-based algorithm for maximum entropy IRL and a GAN in which the generator's density can be evaluated and is provided as an additional input to the discriminator. Interestingly, maximum entropy IRL is a special case of an energy-based model. We discuss the interpretation of GANs as an algorithm for training energy-based models, and relate this interpretation to other recent work that seeks to connect GANs and EBMs. By formally highlighting the connection between GANs, IRL, and EBMs, we hope that researchers in all three communities can better identify and apply transferable ideas from one domain to another, particularly for developing more stable and scalable algorithms: a major challenge in all three domains.

* [Generative Models](/research/index/?tags=generative-models)

## Authors

Chelsea Finn, Paul Christiano, Pieter Abbeel, Sergey Levine

## Related articles

![Hierarchical Text Conditional Image Generation With Clip Latents](https://images.ctfassets.net/kftzwdyauwt9/7c44eedc-3563-4438-c613706c52b1/fcfc38b26fd4878a3c6b4ca8d1d73b17/hierarchical-text-conditional-image-generation-with-clip-latents.jpg?w=3840&q=90&fm=webp)

[Hierarchical text-conditional image generation with CLIP latents

PublicationApr 13, 2022](/index/hierarchical-text-conditional-image-generation-with-clip-latents/)

![DALL·E](https://images.ctfassets.net/kftzwdyauwt9/ed21faee-ce44-4d91-f5cc39941d47/bdd3983530857e93d205304e219e2d95/dall-e.jpg?w=3840&q=90&fm=webp)

[DALL·E: Creating images from text

MilestoneJan 5, 2021](/index/dall-e/)

![Image GPT](https://images.ctfassets.net/kftzwdyauwt9/5ae77333-6ec9-4b5b-345335df9dfe/be9cfca3194bf819fbd8f45fd49a5185/image_127.png?w=3840&q=90&fm=webp)

[Image GPT

PublicationJun 17, 2020](/index/image-gpt/)
