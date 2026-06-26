<!-- source: https://openai.com/index/point-e/ -->

December 16, 2022

[Publication](/research/index/publication/)

# Point-E: A system for generating 3D point clouds from complex prompts

[Read paper(opens in a new window)](https://arxiv.org/abs/2212.08751)[View code(opens in a new window)](https://github.com/openai/point-e)[View model card(opens in a new window)](https://github.com/openai/point-e/blob/main/model-card.md)

![Point E A System For Generating 3d Point Clouds From Complex Prompts](https://images.ctfassets.net/kftzwdyauwt9/7e4ba260-7655-4049-5a2568c94158/2f2af956a356ee2b507296d01e45e766/image-5.webp?w=3840&q=90&fm=webp)

## Abstract

While recent work on text-conditional 3D object generation has shown promising results, the state-of-the-art methods typically require multiple GPU-hours to produce a single sample. This is in stark contrast to state-of-the-art generative image models, which produce samples in a number of seconds or minutes. In this paper, we explore an alternative method for 3D object generation which produces 3D models in only 1-2 minutes on a single GPU. Our method first generates a single synthetic view using a text-to-image diffusion model, and then produces a 3D point cloud using a second diffusion model which conditions on the generated image. While our method still falls short of the state-of-the-art in terms of sample quality, it is one to two orders of magnitude faster to sample from, offering a practical trade-off for some use cases. We release our pre-trained point cloud diffusion models, as well as evaluation code and models, at [this https URL⁠(opens in a new window)](https://github.com/openai/point-e).

* [Point-E](/research/index/?tags=point-e)
* [Generative Models](/research/index/?tags=generative-models)
* [Software & Engineering](/research/index/?tags=software-engineering)

## Authors

Alex Nichol, Heewoo Jun, Prafulla Dhariwal, Pamela Mishkin, Mark Chen

## Related articles

![Multimodal Neurons](https://images.ctfassets.net/kftzwdyauwt9/e16f419f-09bf-4266-7ca3cdd2ae33/0a11dd23053f257828e7c68a815cd632/multimodal-neurons.png?w=3840&q=90&fm=webp)

[Multimodal neurons in artificial neural networks

MilestoneMar 4, 2021](/index/multimodal-neurons/)

![CLIP](https://images.ctfassets.net/kftzwdyauwt9/5e490f66-703f-4228-221ca64049ed/8ed4358ba4b9f8779e07a2b15d7256e1/image_125.png?w=3840&q=90&fm=webp)

[CLIP: Connecting text and images

MilestoneJan 5, 2021](/index/clip/)

![Image GPT](https://images.ctfassets.net/kftzwdyauwt9/5ae77333-6ec9-4b5b-345335df9dfe/be9cfca3194bf819fbd8f45fd49a5185/image_127.png?w=3840&q=90&fm=webp)

[Image GPT

PublicationJun 17, 2020](/index/image-gpt/)
