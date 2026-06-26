<!-- source: https://openai.com/index/language-models-are-few-shot-learners/ -->

May 28, 2020

[Milestone](/research/index/milestone/)

# Language models are few-shot learners

[Read paper(opens in a new window)](https://arxiv.org/abs/2005.14165)

Recent work has demonstrated substantial gains on many NLP tasks and benchmarks by pre-training on a large corpus of text followed by fine-tuning on a specific task. While typically task-agnostic in architecture, this method still requires task-specific fine-tuning datasets of thousands or tens of thousands of examples. By contrast, humans can generally perform a new language task from only a few examples or from simple instructions - something which current NLP systems still largely struggle to do. Here we show that scaling up language models greatly improves task-agnostic, few-shot performance, sometimes even reaching competitiveness with prior state-of-the-art fine-tuning approaches. Specifically, we train GPT‑3, an autoregressive language model with 175 billion parameters, 10x more than any previous non-sparse language model, and test its performance in the few-shot setting. For all tasks, GPT‑3 is applied without any gradient updates or fine-tuning, with tasks and few-shot demonstrations specified purely via text interaction with the model. GPT‑3 achieves strong performance on many NLP datasets, including translation, question-answering, and cloze tasks, as well as several tasks that require on-the-fly reasoning or domain adaptation, such as unscrambling words, using a novel word in a sentence, or performing 3-digit arithmetic. At the same time, we also identify some datasets where GPT‑3's few-shot learning still struggles, as well as some datasets where GPT‑3 faces methodological issues related to training on large web corpora. Finally, we find that GPT‑3 can generate samples of news articles which human evaluators have difficulty distinguishing from articles written by humans. We discuss broader societal impacts of this finding and of GPT‑3 in general.

* [GPT](/research/index/?tags=gpt)
* [Language](/research/index/?tags=language)
* [Learning Paradigms](/research/index/?tags=learning-paradigms)
* [Transformers](/research/index/?tags=transformers)

## Authors

Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh

## Authors

Daniel Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, Dario Amodei

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
