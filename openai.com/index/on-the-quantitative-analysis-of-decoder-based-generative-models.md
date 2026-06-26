<!-- source: https://openai.com/index/on-the-quantitative-analysis-of-decoder-based-generative-models/ -->

November 14, 2016

[Publication](/research/index/publication/)

# On the quantitative analysis of decoder-based generative models

[Read paper(opens in a new window)](https://arxiv.org/abs/1611.04273)

![On The Quantitative Analysis Of Decoder Based Generative Models](https://images.ctfassets.net/kftzwdyauwt9/dc69b05f-82e6-46cc-4ba3583e9ce5/22f6616def67d45acc87ca56764356c8/image-9.webp?w=3840&q=90&fm=webp)

## Abstract

The past several years have seen remarkable progress in generative models which produce convincing samples of images and other modalities. A shared component of many powerful generative models is a decoder network, a parametric deep neural net that defines a generative distribution. Examples include variational autoencoders, generative adversarial networks, and generative moment matching networks. Unfortunately, it can be difficult to quantify the performance of these models because of the intractability of log-likelihood estimation, and inspecting samples can be misleading. We propose to use Annealed Importance Sampling for evaluating log-likelihoods for decoder-based models and validate its accuracy using bidirectional Monte Carlo. The evaluation code is provided at [this https URL⁠(opens in a new window)](https://github.com/tonywu95/eval_gen). Using this technique, we analyze the performance of decoder-based models, the effectiveness of existing log-likelihood estimators, the degree of overfitting, and the degree to which these models miss important modes of the data distribution.

* [Generative Models](/research/index/?tags=generative-models)

## Authors

Yuhuai Wu, Yura Burda, Ruslan Salakhutdinov, Roger Grosse

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
