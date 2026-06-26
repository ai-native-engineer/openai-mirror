<!-- source: https://openai.com/index/variational-lossy-autoencoder/ -->

November 8, 2016

[Publication](/research/index/publication/)

# Variational lossy autoencoder

[Read paper(opens in a new window)](https://arxiv.org/abs/1611.02731)

![Variational Lossy Autoencoder](https://images.ctfassets.net/kftzwdyauwt9/a591db18-ce53-4427-5df3e0459482/b3b9ed4511fe9a8977d6d6c0608a046d/image-12.webp?w=3840&q=90&fm=webp)

## Abstract

Representation learning seeks to expose certain aspects of observed data in a learned representation that's amenable to downstream tasks like classification. For instance, a good representation for 2D images might be one that describes only global structure and discards information about detailed texture. In this paper, we present a simple but principled method to learn such global representations by combining Variational Autoencoder (VAE) with neural autoregressive models such as RNN, MADE and PixelRNN/CNN. Our proposed VAE model allows us to have control over what the global latent code can learn and , by designing the architecture accordingly, we can force the global latent code to discard irrelevant information such as texture in 2D images, and hence the VAE only "autoencodes" data in a lossy fashion. In addition, by leveraging autoregressive models as both prior distribution p(z) and decoding distribution p(x|z), we can greatly improve generative modeling performance of VAEs, achieving new state-of-the-art results on MNIST, OMNIGLOT and Caltech-101 Silhouettes density estimation tasks.

* [Generative Models](/research/index/?tags=generative-models)

## Authors

Xi Chen, Durk Kingma, Tim Salimans, Yan Duan, Prafulla Dhariwal, John Schulman, Ilya Sutskever, Pieter Abbeel

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
