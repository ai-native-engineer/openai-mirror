<!-- source: https://openai.com/index/new-and-improved-content-moderation-tooling/ -->

August 10, 2022

[Product](/news/product-releases/)

# New and improved content moderation tooling

[Read documentation(opens in a new window)](https://platform.openai.com/docs/api-reference/moderations/create)

![New And Improved Content Moderation Tooling](https://images.ctfassets.net/kftzwdyauwt9/5772930c-1b4d-40cf-bf103c8dd331/1933ee15c42afd6a78b56802bd4abdda/image-24.webp?w=3840&q=90&fm=webp)

To help developers protect their applications against possible misuse, we are introducing the faster and more accurate [Moderation endpoint⁠(opens in a new window)](https://beta.openai.com/docs/api-reference/moderations). This endpoint provides OpenAI API developers with free access to [GPT‑based⁠](/index/customized-gpt-3/) classifiers that detect undesired content—an instance of [using AI systems⁠](/index/critiques/) to assist with human supervision of these systems. We have also released both a [technical paper⁠(opens in a new window)](https://arxiv.org/abs/2208.03274) describing our methodology and the [dataset⁠(opens in a new window)](https://github.com/openai/moderation-api-release) used for evaluation.

When given a text input, the Moderation endpoint assesses whether the content is sexual, hateful, violent, or promotes self-harm—content prohibited by our [content policy⁠(opens in a new window)](https://beta.openai.com/docs/usage-guidelines/content-policy). The endpoint has been trained to be quick, accurate, and to perform robustly across a range of applications. Importantly, this reduces the chances of products “saying” the wrong thing, even when deployed to users at-scale. As a consequence, AI can unlock benefits in sensitive settings, like education, where it could not otherwise be used with confidence.

Loading...

The Moderation endpoint helps developers to benefit from our infrastructure investments. Rather than build and maintain their own classifiers—an extensive process, as we document in our [paper⁠(opens in a new window)](https://arxiv.org/abs/2208.03274)—they can instead access accurate classifiers through a single API call.

As part of OpenAI’s [commitment⁠](/charter/) to [making the AI ecosystem safer⁠](/index/best-practices-for-deploying-language-models/), we are providing this endpoint to allow free moderation of all OpenAI API-generated content. For instance, [Inworld⁠(opens in a new window)](https://www.inworld.ai/), an OpenAI API customer, uses the Moderation endpoint to help their AI-based virtual characters remain appropriate for their audiences. By leveraging OpenAI’s technology, Inworld can focus on their core product: creating memorable characters. We currently do not support monitoring of third-party traffic.

Get started with the Moderation endpoint by checking out [the documentation⁠(opens in a new window)](https://beta.openai.com/docs/guides/moderation/overview). More details of the training process and model performance are available in our [paper⁠(opens in a new window)](https://arxiv.org/abs/2208.03274). We have also released an [evaluation dataset⁠(opens in a new window)](https://github.com/openai/moderation-api-release), featuring Common Crawl data labeled within these categories, which we hope will spur further research in this area.

* [View documentation(opens in a new window)](https://beta.openai.com/docs/guides/mode)

* [API Platform](/news/?tags=api-platform)
* [2022](/news/?tags=2022)

## Authors

Todor Markov, Chong Zhang, Sandhini Agarwal, Tyna Eloundou, Teddy Lee, Steven Adler, Angela Jiang, Lilian Weng

## Related articles

![Newspartnership Cover](https://images.ctfassets.net/kftzwdyauwt9/ffffbd46-a171-41c5-25d9eec16b7d/bd1bc987f38b1c2901819b4c211886a2/NewsPartnership_Cover.png?w=3840&q=90&fm=webp)

[Global news partnerships: Le Monde and Prisa Media

CompanyMar 13, 2024](/index/global-news-partnerships-le-monde-and-prisa-media/)

![News > Company carousel > Review completed > Media](https://images.ctfassets.net/kftzwdyauwt9/3BEH4mYgX0MXC45XOsbOru/fdcc0dadabd87f8e9a776a2f34647de0/37.png?w=3840&q=90&fm=webp)

[Review completed & Altman, Brockman to continue to lead OpenAI

CompanyMar 8, 2024](/index/review-completed-altman-brockman-to-continue-to-lead-openai/)

![New board of directors](https://images.ctfassets.net/kftzwdyauwt9/5J9s3ItUUDOTebSo0ZVmun/642e8632be32866792c7aaae0113aaa5/44.png?w=3840&q=90&fm=webp)

[OpenAI announces new members to board of directors

CompanyMar 8, 2024](/index/openai-announces-new-members-to-board-of-directors/)
