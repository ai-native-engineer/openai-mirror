<!-- source: https://openai.com/index/efficient-training-of-language-models-to-fill-in-the-middle/ -->

July 28, 2022

[Publication](/research/index/publication/)

# Efficient training of language models to fill in the middle

[Read paper(opens in a new window)](https://arxiv.org/abs/2207.14255)

![Efficient Training Of Language Models To Fill In The Middle](https://images.ctfassets.net/kftzwdyauwt9/78474566-f381-41aa-7fa6e57d06a9/378a1a1a3b3f3b8127d63308a4f8d803/image-7.webp?w=3840&q=90&fm=webp)

## Abstract

We show that autoregressive language models can learn to infill text after we apply a straightforward transformation to the dataset, which simply moves a span of text from the middle of a document to its end. While this data augmentation has garnered much interest in recent years, we provide extensive evidence that training models with a large fraction of data transformed in this way does not harm the original left-to-right generative capability, as measured by perplexity and sampling evaluations across a wide range of scales. Given the usefulness, simplicity, and efficiency of training models to fill-in-the-middle (FIM), we suggest that future autoregressive language models be trained with FIM by default. To this end, we run a series of ablations on key hyperparameters, such as the data transformation frequency, the structure of the transformation, and the method of selecting the infill span. We use these ablations to prescribe strong default settings and best practices to train FIM models. We have released our best infilling model trained with best practices in our API, and release our infilling benchmarks to aid future research.

* [GPT](/research/index/?tags=gpt)
* [Language](/research/index/?tags=language)
* [Learning Paradigms](/research/index/?tags=learning-paradigms)

## Authors

Mohammad Bavarian, Heewoo Jun, Nikolas Tezak, John Schulman, Christine McLeavey Payne, Jerry Tworek, Mark Chen

## Related articles

![Three farmers using a mobile app outside](https://images.ctfassets.net/kftzwdyauwt9/7b26cc3b-46d8-45b0-f67f6de0c8f8/8bc94d083a5a147609cddad159243ef7/digital_green.png?w=3840&q=90&fm=webp)

[Building agricultural database for farmers

Jan 12, 2024](/index/digital-green/)

![Wix cover image](https://images.ctfassets.net/kftzwdyauwt9/6E3QyNLzuWwK3EGBHPw7nQ/fbd0c5a34cc4f4ba096028adbdda8934/oai_Wix_1x1.png?w=3840&q=90&fm=webp)

[Creating websites in minutes with AI Website Builder

May 29, 2025](/index/wix/)

![WHOOP Coach HIIT](https://images.ctfassets.net/kftzwdyauwt9/163d4817-6436-4d20-83e0963f68f1/ef4bec09f31b32f8ca8a953a09da5897/whoop.png?w=3840&q=90&fm=webp)

[Delivering LLM-powered health solutions

Jan 4, 2024](/index/whoop/)
