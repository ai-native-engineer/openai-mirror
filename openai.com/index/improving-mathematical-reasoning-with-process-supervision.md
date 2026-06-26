<!-- source: https://openai.com/index/improving-mathematical-reasoning-with-process-supervision/ -->

May 31, 2023

[Publication](/research/index/publication/)

# Improving mathematical reasoning with process supervision

[Read paper(opens in a new window)](https://arxiv.org/abs/2305.20050)[Browse samples](#samples)[Download dataset(opens in a new window)](https://github.com/openai/prm800k)

![Improving Mathematical Reasoning With Process Supervision](https://images.ctfassets.net/kftzwdyauwt9/373bf52a-5373-4d4e-230d7678254c/e6d514bd3908ce99747c59f686779e2b/improving-mathematical-reasoning-with-process-supervision.jpg?w=3840&q=90&fm=webp)

We've trained a model to achieve a new state-of-the-art in mathematical problem solving by rewarding each correct step of reasoning (“process supervision”) instead of simply rewarding the correct final answer (“outcome supervision”). In addition to boosting performance relative to outcome supervision, process supervision also has an important alignment benefit: it directly trains the model to produce a chain-of-thought that is endorsed by humans.

## Introduction

In recent years, large language models have greatly improved in their ability to perform complex multi-step reasoning. However, even state-of-the-art models still produce logical mistakes, often called *hallucinations*. Mitigating hallucinations is a critical step towards building aligned AGI.

We can train reward models to detect hallucinations using either *outcome supervision*, which provides feedback based on a final result, or *process supervision*, which provides feedback for each individual step in a chain-of-thought. Building on previous work[1](#citation-bottom-1), we conduct a detailed comparison of these two methods using the MATH dataset[2](#citation-bottom-2) as our testbed. We find that process supervision leads to significantly better performance, even when judged by outcomes. To encourage related research, we release our full dataset of process supervision.

## Alignment impact

Process supervision has several alignment advantages over outcome supervision. It directly rewards the model for following an aligned chain-of-thought, since each step in the process receives precise supervision. Process supervision is also more likely to produce interpretable reasoning, since it encourages the model to follow a human-approved process. In contrast, outcome supervision may reward an unaligned process, and it is generally harder to scrutinize.

In some cases, safer methods for AI systems can lead to reduced performance[3](#citation-bottom-3), a cost which is known as an *alignment tax*. In general, any alignment tax may hinder the adoption of alignment methods, due to pressure to deploy the most capable model. Our results below show that process supervision in fact incurs a negative alignment tax, at least in the math domain. This could increase the adoption of process supervision, which we believe would have positive alignment side-effects.

## Solving MATH problems

Loading...

We evaluate our process-supervised and outcome-supervised reward models using problems from the MATH test set. We generate many solutions for each problem and then pick the solution ranked the highest by each reward model. The graph shows the percentage of chosen solutions that reach the correct final answer, as a function of the number of solutions considered. Not only does the process-supervised reward model perform better across the board, but the performance gap widens as we consider more solutions per problem. This shows us that the process-supervised reward model is much more reliable.

We showcase 10 problems and solutions below, along with commentary about the reward model’s strengths and weaknesses.

Loading...

It is unknown how broadly these results will generalize beyond the domain of math, and we consider it important for future work to explore the impact of process supervision in other domains. If these results generalize, we may find that process supervision gives us the best of both worlds – a method that is both more performant and more aligned than outcome supervision.

* [GPT](/research/index/?tags=gpt)
* [Language](/research/index/?tags=language)
* [Learning Paradigms](/research/index/?tags=learning-paradigms)
* [Reasonings & Policy](/research/index/?tags=reasoning-policy)

## References

1. 1

   Uesato, J., Kushman N., Kumar R., Song F., Siegel N., Wang L., Creswell A., Irving G. and Higgins, I., 2022. Solving math word problems with process- and outcome-based feedback. arXiv preprint arXiv:2211.14275.
2. 2

   Hendrycks D., Burns C., Kadavath S., Arora A., Basart S., Tang E., Song D. and Steinhardt J., 2021. Measuring Mathematical Problem Solving With the MATH Dataset. arXiv preprint arXiv:2103.03874.
3. 3

   Ouyang L., Wu J., Jiang X., Almedia D., Wainwright C.L., Mishkin P., Zhang C., Agarwal S., Slama K., Ray A., Schulman J., Hilton J., Kelton F., Miller L., Simens M., Askell A., Welinder P., Christiano P., Leike J. and Lowe R., 2022. Training language models to follow instructions with human feedback. arXiv preprint arXiv:2203.02155.

## Authors

Karl Cobbe, Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Jan Leike, Ilya Sutskever

## Contributors

Bowen Baker, Teddy Lee, John Schulman, Greg Brockman, Kendra Rimbach, Hannah Wong, Thomas Degry

## Related articles

![Cloud astronaut](https://images.ctfassets.net/kftzwdyauwt9/f698e023-3373-4385-a039a7370270/29fdcfdd52fe5cf2b38deff2af34648f/VALERIECloudAstronaut.png?w=3840&q=90&fm=webp)

[DALL·E 3 is now available in ChatGPT Plus and Enterprise

ProductOct 19, 2023](/index/dall-e-3-is-now-available-in-chatgpt-plus-and-enterprise/)

![language models can explain neurons in language model](https://images.ctfassets.net/kftzwdyauwt9/3LNxX9CObAlTYvYJcituK5/fcc293879e4d33ed72b751750a3f8f79/language_models_can_explain_neurons_in_language_model.png?w=3840&q=90&fm=webp)

[Language models can explain neurons in language models

PublicationMay 9, 2023](/index/language-models-can-explain-neurons-in-language-models/)

![Solving Some Formal Math Olympiad Problems](https://images.ctfassets.net/kftzwdyauwt9/107bb1e1-daad-40bf-85975dfa741c/57d987d185a7a46828ea203bb0132867/image-12_copy.png?w=3840&q=90&fm=webp)

[Solving (some) formal math olympiad problems

MilestoneFeb 2, 2022](/index/formal-math/)
