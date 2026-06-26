<!-- source: https://openai.com/index/pixelcnn-plus-plus/ -->

January 19, 2017

[Publication](/research/index/publication/)

# PixelCNN++: Improving the PixelCNN with discretized logistic mixture likelihood and other modifications

[Read paper(opens in a new window)](https://arxiv.org/abs/1701.05517)[(opens in a new window)](https://github.com/openai/pixel-cnn)

![Pixelcnn Improving The Pixelcnn With Discretized Logistic Mixture Likelihood And Other Modifications](https://images.ctfassets.net/kftzwdyauwt9/c8131618-9096-4326-6836e24db9bb/b41970949702b84d5f224c5b8816a881/image-7.webp?w=3840&q=90&fm=webp)

## Abstract

PixelCNNs are a recently proposed class of powerful generative models with tractable likelihood. Here we discuss our implementation of PixelCNNs which we make available at [this https URL⁠(opens in a new window)](https://github.com/openai/pixel-cnn). Our implementation contains a number of modifications to the original model that both simplify its structure and improve its performance. 1) We use a discretized logistic mixture likelihood on the pixels, rather than a 256-way softmax, which we find to speed up training. 2) We condition on whole pixels, rather than R/G/B sub-pixels, simplifying the model structure. 3) We use downsampling to efficiently capture structure at multiple resolutions. 4) We introduce additional short-cut connections to further speed up optimization. 5) We regularize the model using dropout. Finally, we present state-of-the-art log likelihood results on CIFAR-10 to demonstrate the usefulness of these modifications.

* [Generative Models](/research/index/?tags=generative-models)

## Authors

Tim Salimans, Andrej Karpathy, Xi Chen, Durk Kingma

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
