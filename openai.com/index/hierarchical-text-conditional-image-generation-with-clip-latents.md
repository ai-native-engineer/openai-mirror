<!-- source: https://openai.com/index/hierarchical-text-conditional-image-generation-with-clip-latents/ -->

April 13, 2022

[Publication](/research/index/publication/)

# Hierarchical text-conditional image generation with CLIP latents

[Read paper(opens in a new window)](https://arxiv.org/abs/2204.06125)

![Hierarchical Text Conditional Image Generation With Clip Latents](https://images.ctfassets.net/kftzwdyauwt9/7c44eedc-3563-4438-c613706c52b1/fcfc38b26fd4878a3c6b4ca8d1d73b17/hierarchical-text-conditional-image-generation-with-clip-latents.jpg?w=3840&q=90&fm=webp)

## Abstract

Contrastive models like CLIP have been shown to learn robust representations of images that capture both semantics and style. To leverage these representations for image generation, we propose a two-stage model: a prior that generates a CLIP image embedding given a text caption, and a decoder that generates an image conditioned on the image embedding. We show that explicitly generating image representations improves image diversity with minimal loss in photorealism and caption similarity. Our decoders conditioned on image representations can also produce variations of an image that preserve both its semantics and style, while varying the non-essential details absent from the image representation. Moreover, the joint embedding space of CLIP enables language-guided image manipulations in a zero-shot fashion. We use diffusion models for the decoder and experiment with both autoregressive and diffusion models for the prior, finding that the latter are computationally more efficient and produce higher-quality samples.

* [CLIP](/research/index/?tags=technology-clip)
* [Generative Models](/research/index/?tags=generative-models)
* [Learning Paradigms](/research/index/?tags=learning-paradigms)

## Authors

Aditya Ramesh, Prafulla Dhariwal, Alex Nichol, Casey Chu, Mark Chen

## Related articles

![Whisper](https://images.ctfassets.net/kftzwdyauwt9/13c810cb-0592-442d-190ab7378bef/a7cb2299d034abe93023f662f8d32263/Speech_Rec_16_9.png?w=3840&q=90&fm=webp)

[Introducing Whisper

ReleaseSep 21, 2022](/index/whisper/)

![An aerial view of a crowd of people facing away, wearing hats and bearing flags](https://images.ctfassets.net/kftzwdyauwt9/d22f177f-5116-4b3b-5ddcdbe54569/b657a1299069351973db72804b5811d1/image_131.png?w=3840&q=90&fm=webp)

[DALL·E 2 pre-training mitigations

PublicationJun 28, 2022](/index/dall-e-2-pre-training-mitigations/)

![Solving Some Formal Math Olympiad Problems](https://images.ctfassets.net/kftzwdyauwt9/107bb1e1-daad-40bf-85975dfa741c/57d987d185a7a46828ea203bb0132867/image-12_copy.png?w=3840&q=90&fm=webp)

[Solving (some) formal math olympiad problems

MilestoneFeb 2, 2022](/index/formal-math/)
