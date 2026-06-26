<!-- source: https://openai.com/index/the-instruction-hierarchy/ -->

April 19, 2024

[Publication](/research/index/publication/)

# The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions

[Read paper(opens in a new window)](https://arxiv.org/abs/2404.13208)

![An abstract image with soft, flowing brushstrokes in warm beige, light brown, and pale blue. The smooth blending of colors creates a calming, fluid composition, evoking a sense of movement and serenity.](https://images.ctfassets.net/kftzwdyauwt9/7KETXhKfus6Y3CS6ON6HNQ/745ec415ffc13f16563cde91a98f8e30/image_44.png?w=3840&q=90&fm=webp)

## Abstract

Today's LLMs are susceptible to prompt injections, jailbreaks, and other attacks that allow adversaries to overwrite a model's original instructions with their own malicious prompts. In this work, we argue that one of the primary vulnerabilities underlying these attacks is that LLMs often consider system prompts (e.g., text from an application developer) to be the same priority as text from untrusted users and third parties. To address this, we propose an instruction hierarchy that explicitly defines how models should behave when instructions of different priorities conflict. We then propose a data generation method to demonstrate this hierarchical instruction following behavior, which teaches LLMs to selectively ignore lower-privileged instructions. We apply this method to GPT‑3.5, showing that it drastically increases robustness -- even for attack types not seen during training -- while imposing minimal degradations on standard capabilities.

* [GPT](/research/index/?tags=gpt)
* [Language](/research/index/?tags=language)
* [Reasonings & Policy](/research/index/?tags=reasoning-policy)
* [Ethics & Safety](/research/index/?tags=ethics-safety)

## Authors

[Eric Wallace⁠(opens in a new window)](https://arxiv.org/search/cs?searchtype=author&query=Wallace,+E)

[Kai Xiao⁠(opens in a new window)](https://arxiv.org/search/cs?searchtype=author&query=Xiao,+K)

[Reimar Leike⁠(opens in a new window)](https://arxiv.org/search/cs?searchtype=author&query=Leike,+R)

[Lilian Weng⁠(opens in a new window)](https://arxiv.org/search/cs?searchtype=author&query=Weng,+L)

[Johannes Heidecke⁠(opens in a new window)](https://arxiv.org/search/cs?searchtype=author&query=Heidecke,+J)

[Alex Beutel⁠(opens in a new window)](https://arxiv.org/search/cs?searchtype=author&query=Beutel,+A)
