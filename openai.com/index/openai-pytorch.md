<!-- source: https://openai.com/index/openai-pytorch/ -->

January 30, 2020

[Safety](/news/safety-alignment/)

# OpenAI standardizes on PyTorch

We are standardizing OpenAI’s deep learning framework on PyTorch.

![A softly textured landscape painting showing a wide field of pink and yellow hues under a pale blue sky with light purple and rose-colored clouds.](https://images.ctfassets.net/kftzwdyauwt9/69p9SVLnABq61LzLKmH11f/f80118caa8f753ce00366cbb63e3cce5/openai-pytorch.jpg?w=3840&q=90&fm=webp)

We are standardizing OpenAI’s deep learning framework on [PyTorch⁠(opens in a new window)](https://pytorch.org/). In the past, we implemented projects in many frameworks depending on their relative strengths. We’ve now chosen to standardize to make it easier for our team to create and share optimized implementations of our models.

As part of this move, we’ve just released a [PyTorch-enabled version⁠(opens in a new window)](https://github.com/openai/spinningup) of [Spinning Up in Deep RL⁠](/index/spinning-up-in-deep-rl/), an open-source educational resource produced by OpenAI that makes it easier to learn about deep reinforcement learning. We are also in the process of writing PyTorch bindings for our highly-optimized [blocksparse kernels⁠](/index/block-sparse-gpu-kernels/), and will open-source those bindings in upcoming months.

The main reason we’ve chosen PyTorch is to increase our research productivity at scale on GPUs. It is very easy to try and execute new research ideas in PyTorch; for example, switching to PyTorch decreased our iteration time on research ideas in generative modeling from weeks to days. We’re also excited to be joining a rapidly-growing developer community, including organizations like Facebook and Microsoft, in pushing scale and performance on GPUs.

Going forward we’ll primarily use PyTorch as our deep learning framework but sometimes use other ones when there’s a specific technical reason to do so. Many of our teams have already made the switch, and we look forward to contributing to the PyTorch community in upcoming months.

* [Framework](/news/?tags=framework)
* [2020](/news/?tags=2020)

## Author

## Related articles

![Newspartnership Cover](https://images.ctfassets.net/kftzwdyauwt9/ffffbd46-a171-41c5-25d9eec16b7d/bd1bc987f38b1c2901819b4c211886a2/NewsPartnership_Cover.png?w=3840&q=90&fm=webp)

[Global news partnerships: Le Monde and Prisa Media

CompanyMar 13, 2024](/index/global-news-partnerships-le-monde-and-prisa-media/)

![New board of directors](https://images.ctfassets.net/kftzwdyauwt9/5J9s3ItUUDOTebSo0ZVmun/642e8632be32866792c7aaae0113aaa5/44.png?w=3840&q=90&fm=webp)

[OpenAI announces new members to board of directors

CompanyMar 8, 2024](/index/openai-announces-new-members-to-board-of-directors/)

![News > Company carousel > Review completed > Media](https://images.ctfassets.net/kftzwdyauwt9/3BEH4mYgX0MXC45XOsbOru/fdcc0dadabd87f8e9a776a2f34647de0/37.png?w=3840&q=90&fm=webp)

[Review completed & Altman, Brockman to continue to lead OpenAI

CompanyMar 8, 2024](/index/review-completed-altman-brockman-to-continue-to-lead-openai/)
