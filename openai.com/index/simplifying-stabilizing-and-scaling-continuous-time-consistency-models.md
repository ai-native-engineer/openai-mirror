<!-- source: https://openai.com/index/simplifying-stabilizing-and-scaling-continuous-time-consistency-models/ -->

October 23, 2024

[Milestone](/research/index/milestone/)

# Simplifying, stabilizing, and scaling continuous-time consistency models

Continuous-time consistency models with sample quality comparable to leading diffusion models in just two sampling steps.

[Read paper(opens in a new window)](https://arxiv.org/abs/2410.11081)

Diffusion models have revolutionized generative AI, enabling remarkable advances in generating realistic images, 3D models, audio, and video. However, despite their impressive results, these models are slow at sampling. 

We are sharing a new approach, called sCM, which simplifies the theoretical formulation of continuous-time consistency models, allowing us to stabilize and scale their training for large scale datasets. This approach achieves comparable sample quality to leading diffusion models, while using only two sampling steps. We are also sharing our [research paper⁠(opens in a new window)](https://arxiv.org/abs/2410.11081) to support further progress in this field.

00:00

Sampling procedure of consistency models. Sampling time measured on a single A100 GPU with batch size = 1.

00:00

Sampling procedure of diffusion models. Sampling time measured on a single A100 GPU with batch size = 1.

## Introduction

Current sampling approaches of diffusion models often require dozens to hundreds of sequential steps to generate a single sample, which limits their efficiency and scalability for real-time applications. Various distillation techniques have been developed to accelerate sampling, but they often come with limitations, such as high computational costs, complex training, and reduced sample quality.

Extending our previous research on consistency models [1](#citation-bottom-1),[2](#citation-bottom-2), we have simplified the formulation and further stabilized the training process of continuous-time consistency models. Our new approach, called sCM, has enabled us to scale the training of continuous-time consistency models to an unprecedented 1.5 billion parameters on ImageNet at 512×512 resolution. sCMs can generate samples with quality comparable to diffusion models using only two sampling steps, resulting in a ~50x wall-clock speedup. For example, our largest model, with 1.5 billion parameters, generates a single sample in just 0.11 seconds on a single A100 GPU without any inference optimization. Additional acceleration is easily achievable through customized system optimization, opening up possibilities for real-time generation in various domains such as image, audio, and video.

For rigorous evaluation, we benchmarked sCM against other state-of-the-art generative models by comparing both sample quality, using the standard Fréchet Inception Distance (FID) scores (where lower is better), and effective sampling compute, which estimates the total compute cost for generating each sample. As shown below, our 2-step sCM produces samples with quality comparable to the best previous methods while using less than 10% of the effective sampling compute, significantly accelerating the sampling process.

![Scatter plot comparing Frechet Inception Distance (lower is better) and Effective Sampling Compute for various models. Notable models include sCM (ours), BigGAN, StyleGAN-XL, ADM-G, U-ViT-H/4, MaskGIT, and DiT-XL/2.](https://images.ctfassets.net/kftzwdyauwt9/4W5nMOAqXmB1weUwnCOkuB/86ca88dda14b03de872726e74b7fc88f/02_Light.svg?w=3840&q=90)

## How it works

Consistency models offer a faster alternative to traditional diffusion models for generating high-quality samples. Unlike diffusion models, which generate samples gradually through a large number of denoising steps, consistency models aim to convert noise directly into noise-free samples in a single step. This difference is visualized by paths in the diagram: the blue line represents the gradual sampling process of a diffusion model, while the red curve illustrates the more direct, accelerated sampling of a consistency model. Using techniques like consistency training or consistency distillation [1](#citation-bottom-1),[2](#citation-bottom-2), consistency models can be trained to generate high-quality samples with significantly fewer steps, making them appealing for practical applications that require fast generation.

![Diagram illustrating ODE trajectories between data and noise, showing points connected by curved and straight paths labeled  𝑥 0 x  0 ​  ,  𝑥 𝜃 x  θ ​  ,  𝑥 𝑡 − Δ 𝑡 x  t−Δt ​  , and  𝑥 𝑡 x  t ​  , with mathematical notations.](https://images.ctfassets.net/kftzwdyauwt9/NG5OUFoqxH5H3bPjCHAAb/1c43b4354aa28bdaeb6d0bd5c5900a48/01_Light.svg?w=3840&q=90)

Illustration on diffusion model sampling (red) and consistency model sampling (blue).

We've trained a continuous-time consistency model with 1.5B parameters on ImageNet 512x512, and provided two-step samples from this model to demonstrate its capabilities.

![Consistency Model > Media carousel > Gallery > Image 54 > Asset](https://images.ctfassets.net/kftzwdyauwt9/2QFDUxr71HBpK5HVk8RFbE/bc3808b652fc8d7562a89709ace0b2ba/54.png?w=3840&q=90&fm=webp)

![Consistency Model > Media carousel > Gallery > Image 89 > Asset ](https://images.ctfassets.net/kftzwdyauwt9/1SQv57e3B0AYBP0MGKP84E/e550c74c33c20cdb9ace2a88a8145744/89.png?w=3840&q=90&fm=webp)

![Jellyfish floating underwater with long, thin tentacles and a transparent, circular body.](https://images.ctfassets.net/kftzwdyauwt9/1wiGz9s9iBLWYZiugWlsxz/99ce019517cdcb440e013c801373ff5a/107.png?w=3840&q=90&fm=webp)

![Underwater view of a bright, white sea anemone with tentacles spread out.](https://images.ctfassets.net/kftzwdyauwt9/5DpI6rDkqZwTsaaQQ2SdIC/eef7de1504975556cc33f94c8d9e14fb/108.png?w=3840&q=90&fm=webp)

![A conch shell on wet sand with a striped pattern.](https://images.ctfassets.net/kftzwdyauwt9/3CAYXoSs0xip8sXRUg5rQN/5e86663ddf1499fefbb862297bc04fce/112.png?w=3840&q=90&fm=webp)

![ A snail on a green leaf, with a spiral-patterned shell.](https://images.ctfassets.net/kftzwdyauwt9/3VVgHf1qNxBmuedpFyIhlY/c049699f7dc4ef16ff2556f29cb6a868/113.png?w=3840&q=90&fm=webp)

![A hermit crab with a red body, emerging from a shell on wet sand.](https://images.ctfassets.net/kftzwdyauwt9/7ITvzQSYoROysSkfaraEoH/9eb3f4ce64a53291fbd22c19b724813c/125.png?w=3840&q=90&fm=webp)

![A white wolf resting on a rock, looking alert.](https://images.ctfassets.net/kftzwdyauwt9/3McsTstMqBzxWDbAstLXei/63530f90e4a078fc4ddcd1aaf9e688c3/270.png?w=3840&q=90&fm=webp)

![Close-up of a snow leopard’s face with spotted fur.](https://images.ctfassets.net/kftzwdyauwt9/2fVUQsomNZqKS4mAjhPzp4/2279316816ba2feb8fc48c5e41f26730/289.png?w=3840&q=90&fm=webp)

![Close-up of a lion’s face with a thick mane.](https://images.ctfassets.net/kftzwdyauwt9/4BOrcxJnmqBA6xCDbsB36C/449a858093573ba3622cdae19b33a474/291.png?w=3840&q=90&fm=webp)

![A black beetle crawling on the ground.](https://images.ctfassets.net/kftzwdyauwt9/434JUj9OX3RnOAkCZSAyMn/d62437ce6c3af8161d1e01de6e292c6a/302.png?w=3840&q=90&fm=webp)

![A yellow and black beetle with long antennae on a green leaf.](https://images.ctfassets.net/kftzwdyauwt9/29T3qV7HktrfgxPSXCVBib/eef728775f1d180c24edbbbb526f51cb/303.png?w=3840&q=90&fm=webp)

![A monarch butterfly with bright orange and black wings on a green plant.](https://images.ctfassets.net/kftzwdyauwt9/3zxstEXv6dF9VvXW0yBOSh/d8cca6d4733b5363aab46217d703c0a0/323.png?w=3840&q=90&fm=webp)

![A lionfish with long, spiky fins swimming near a coral reef.](https://images.ctfassets.net/kftzwdyauwt9/3DuGZRwt4pQDfK5ZFidAlo/65a769e12be56d3730bc72ca4e9c74db/396.png?w=3840&q=90&fm=webp)

![A car’s side mirror reflecting a countryside view with hills and trees.](https://images.ctfassets.net/kftzwdyauwt9/117ZYpjpdJOmvUugmW8Bte/c25e95e46bbd4174eb2e9273a4c730bd/475.png?w=3840&q=90&fm=webp)

![A large, ancient stone structure composed of stacked rocks in a grassy landscape.](https://images.ctfassets.net/kftzwdyauwt9/yPGUqSQcRZuQVPQqCobpx/3114e80eb625f694cab4592fda6f587b/649.png?w=3840&q=90&fm=webp)

![A ceramic teapot and two small cups on a wooden table.](https://images.ctfassets.net/kftzwdyauwt9/4J0qESPnmd7pIoZDH5QJsr/e25bd28d97ab7740c7f0eceefbd2eeee/849.png?w=3840&q=90&fm=webp)

![Close-up of a cheeseburger with melted cheese and a soft bun.](https://images.ctfassets.net/kftzwdyauwt9/1fkOdPx4Av7qODin6DgkXB/1116f16ef778642db4ef8cde7afc5e2c/933.png?w=3840&q=90&fm=webp)

![A scenic view of snow-capped mountains with lush green meadows and pine trees.](https://images.ctfassets.net/kftzwdyauwt9/3Q1nWWRVJJleCGLa39cQw4/c561e87980a3c90d649b0907d090290b/970.png?w=3840&q=90&fm=webp)

![Aerial view of a coastal bay with turquoise water surrounded by cliffs.](https://images.ctfassets.net/kftzwdyauwt9/7DhrrR3sKpveBCXzF6ST9t/77e3890e1d8907a088dcc99b6a1d41cc/978.png?w=3840&q=90&fm=webp)

![A fast-flowing turquoise river cutting through rocky hills with dense green vegetation.](https://images.ctfassets.net/kftzwdyauwt9/6Uj0HiRZI2CPYvxjaXzzB7/4534921214f73f22c314490c8d0ac28b/979.png?w=3840&q=90&fm=webp)

Our sCM distills knowledge from a pre-trained diffusion model. A key finding is that sCMs improve proportionally with the teacher diffusion model as both scale up. Specifically, the relative difference in sample quality, measured by the ratio of FID scores, remains consistent across several orders of magnitude in model sizes, causing the absolute difference in sample quality to diminish at scale. Additionally, increasing the sampling steps for sCMs further reduces the quality gap. Notably, two-step samples from sCMs are already comparable (with less than a 10% relative difference in FID scores) to samples from the teacher diffusion model, which requires hundreds of steps to generate.

![Line graph comparing FID against single forward flops for three methods: 1-step SCM (red), 2-step SCM (blue), and Diffusion (orange), across model sizes (S, M, L, XL, XXL). All lines show decreasing FID as flops increase, with Diffusion performing best.](https://images.ctfassets.net/kftzwdyauwt9/u3YyJPCJIFQxOEagfKKZq/d2b13c2dbfe5117fe43ee54bf1f444b2/03_Light-padded.svg?w=3840&q=90)

sCM scales commensurately with teacher diffusion models.

## Limitations

The best sCMs still rely on pre-trained diffusion models for initialization and distillation, resulting in a small but consistent gap in sample quality compared to the teacher diffusion model. Additionally, FID as a metric for sample quality has its own limitations; being close in FID scores does not always reflect actual sample quality, and vice versa. Therefore, the quality of sCMs may need to be assessed differently depending on the requirements of specific applications.

## What's next

We will continue to work toward developing better generative models with both improved inference speed and sample quality. We believe these advancements will unlock new possibilities for real-time, high-quality generative AI across a wide range of domains.

* [Glow](/research/index/?tags=glow)
* [Generative Models](/research/index/?tags=generative-models)
* [Software & Engineering](/research/index/?tags=software-engineering)
* [Simulated Environments](/research/index/?tags=simulated-environments)

## Authors

Cheng Lu, Yang Song

## References

1. 1

   [https://openai.com/index/consistency-models⁠](https://openai.com/index/consistency-models)
2. 2

   [https://openai.com/index/improved-techniques-for-training-consistency-models⁠](https://openai.com/index/improved-techniques-for-training-consistency-models)

1. [https://openai.com/index/video-generation-models-as-world-simulators⁠](https://openai.com/index/video-generation-models-as-world-simulators/)
2. [https://openai.com/index/dall-e-3⁠](https://openai.com/index/dall-e-3/)
3. Albergo, Michael S., Nicholas M. Boffi, and Eric Vanden-Eijnden. “Stochastic interpolants: A unifying framework for flows and diffusions.” *arXiv preprint arXiv:2303.08797* (2023).
4. Albergo, Michael S., and Eric Vanden-Eijnden. “Building normalizing flows with stochastic interpolants.” *arXiv preprint arXiv:2209.15571* (2022).
5. Deng, Jia, et al. “ImageNet: A large-scale hierarchical image database.” *2009 IEEE conference on computer vision and pattern recognition*. Ieee, 2009.
6. Dhariwal, Prafulla, and Alexander Nichol. “Diffusion models beat GANs on image synthesis.” *Advances in neural information processing systems* 34 (2021): 8780-8794.
7. Geng, Zhengyang, et al. “Consistency models made easy.” *arXiv preprint arXiv:2406.14548* (2024).
8. Heek, Jonathan, Emiel Hoogeboom, and Tim Salimans. “Multistep consistency models.” *arXiv preprint arXiv:2403.06807* (2024).
9. Ho, Jonathan, and Tim Salimans. “Classifier-free diffusion guidance.” *arXiv preprint arXiv:2207.12598* (2022).
10. Ho, Jonathan, Ajay Jain, and Pieter Abbeel. “Denoising diffusion probabilistic models.” *Advances in neural information processing systems* 33 (2020): 6840-6851.
11. Hoogeboom, Emiel, Jonathan Heek, and Tim Salimans. “Simple diffusion: End-to-end diffusion for high resolution images.” *International Conference on Machine Learning*. PMLR, 2023.
12. Karras, Tero, et al. “Elucidating the design space of diffusion-based generative models.” *Advances in neural information processing systems* 35 (2022): 26565-26577.
13. Karras, Tero, et al. “Analyzing and improving the training dynamics of diffusion models.” *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*. 2024.
14. Lipman, Yaron, et al. “Flow matching for generative modeling.” *arXiv preprint arXiv:2210.02747* (2022).
15. Liu, Xingchao, Chengyue Gong, and Qiang Liu. “Flow straight and fast: Learning to generate and transfer data with rectified flow.” *arXiv preprint arXiv:2209.03003* (2022).
16. Meng, Chenlin, et al. “On distillation of guided diffusion models.” *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*. 2023.
17. Rombach, Robin, et al. “High-resolution image synthesis with latent diffusion models.” *Proceedings of the IEEE/CVF conference on computer vision and pattern recognition*. 2022.
18. Song, Yang, and Prafulla Dhariwal. “Improved techniques for training consistency models.” *arXiv preprint arXiv:2310.14189* (2023).
19. Song, Yang, and Stefano Ermon. “Generative modeling by estimating gradients of the data distribution.” *Advances in neural information processing systems* 32 (2019).
20. Song, Yang, et al. “Score-based generative modeling through stochastic differential equations.” *arXiv preprint arXiv:2011.13456* (2020).
21. Song, Yang, et al. “Consistency models.” *arXiv preprint arXiv:2303.01469* (2023).
22. Lu, Cheng, et al. “DPM-Solver: A fast ODE solver for diffusion probabilistic model sampling in around 10 steps.” *Advances in Neural Information Processing Systems* 35 (2022): 5775-5787.
23. Lu, Cheng, et al. “DPM-Solver++: Fast solver for guided sampling of diffusion probabilistic models.” *arXiv preprint arXiv:2211.01095* (2022).
24. Wang, Zhengyi, et al. “ProlificDreamer: High-fidelity and diverse text-to-3D generation with variational score distillation.” *Advances in Neural Information Processing Systems* 36 (2024).
