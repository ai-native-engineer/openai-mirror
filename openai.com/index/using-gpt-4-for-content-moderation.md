<!-- source: https://openai.com/index/using-gpt-4-for-content-moderation/ -->

August 15, 2023

[Safety](/news/safety-alignment/)

# Using GPT‑4 for content moderation

We use GPT‑4 for content policy development and content moderation decisions, enabling more consistent labeling, a faster feedback loop for policy refinement, and less involvement from human moderators.

![A watercolor-style abstract digital painting with a soft blue foreground, a greenish sky, and a vivid pink cloud-like form spreading from the left side.](https://images.ctfassets.net/kftzwdyauwt9/3oQb5QVQxMYse1jLzumHT2/3abfb15b70771a33cc1166ff75fe76f7/Using_GPT-4_for_content_moderation.png?w=3840&q=90&fm=webp)

Content moderation plays a crucial role in sustaining the health of digital platforms. A content moderation system using GPT‑4 results in much faster iteration on policy changes, reducing the cycle from months to hours. GPT‑4 is also able to interpret rules and nuances in long content policy documentation and adapt instantly to policy updates, resulting in more consistent labeling. We believe this offers a more positive vision of the future of digital platforms, where AI can help moderate online traffic according to platform-specific policy and relieve the mental burden of a large number of human moderators. Anyone with OpenAI API access can implement this approach to create their own AI-assisted moderation system.

## Challenges in content moderation

Content moderation demands meticulous effort, sensitivity, a profound understanding of context, as well as quick adaptation to new use cases, making it both time consuming and challenging. Traditionally, the burden of this task has fallen on human moderators sifting through large amounts of content to filter out toxic and harmful material, supported by smaller vertical-specific machine learning models. The process is inherently slow and can lead to mental stress on human moderators.

## Using large language models

We're exploring the use of LLMs to address these challenges. Our large language models like GPT‑4 can understand and generate natural language, making them applicable to content moderation. The models can make moderation judgments based on policy guidelines provided to them.

With this system, the process of developing and customizing content policies is trimmed down from months to hours. 

1. Once a policy guideline is written, policy experts can create a golden set of data by identifying a small number of examples and assigning them labels according to the policy.
2. Then, GPT‑4 reads the policy and assigns labels to the same dataset, without seeing the answers.
3. By examining the discrepancies between GPT‑4’s judgments and those of a human, the policy experts can ask GPT‑4 to come up with reasoning behind its labels, analyze the ambiguity in policy definitions, resolve confusion and provide further clarification in the policy accordingly. We can repeat steps 2 and 3 until we are satisfied with the policy quality.

This iterative process yields refined content policies that are translated into classifiers, enabling the deployment of the policy and content moderation at scale.

Optionally, to handle large amounts of data at scale, we can use GPT‑4's predictions to fine-tune a much smaller model.

Loading...

This simple yet powerful idea offers several improvements to traditional approaches to content moderation: 

* **More consistent labels.** Content policies are continually evolving and often very detailed. People may interpret policies differently or some moderators may take longer to digest new policy changes, leading to inconsistent labels. In comparison, LLMs are sensitive to granular differences in wording and can instantly adapt to policy updates to offer a consistent content experience for users.
* **Faster feedback loop.** The cycle of policy updates – developing a new policy, labeling, and gathering human feedback – can often be a long and drawn-out process. GPT‑4 can reduce this process down to hours, enabling faster responses to new harms.
* **Reduced mental burden.** Continual exposure to harmful or offensive content can lead to emotional exhaustion and psychological stress among human moderators. Automating this type of work is beneficial for the wellbeing of those involved.

![Fact Factory Blog Diagram](https://images.ctfassets.net/kftzwdyauwt9/3d69d379-568e-45f9-560237c50035/e894e4d578562cd60d38755229526dec/fact-factory-blog-diagram.jpg?w=3840&q=90&fm=webp)

Illustration of the process of how we leverage GPT‑4 for content moderation, from policy development to moderation at scale.

Different from Constitutional AI ([Bai, et al. 2022⁠(opens in a new window)](https://arxiv.org/abs/2212.08073)) which mainly relies on the model's own internalized judgment of what is safe vs not, our approach makes platform-specific content policy iteration much faster and less effortful. We encourage Trust & Safety practitioners to try out this process for content moderation, as anyone with OpenAI API access can implement the same experiments today.

Loading...

We are actively exploring further enhancement of GPT‑4’s prediction quality, for example, by incorporating chain-of-thought reasoning or self-critique. We are also experimenting with ways to detect unknown risks and, inspired by Constitutional AI, aim to leverage models to identify potentially harmful content given high-level descriptions of what is considered harmful. These findings would then inform updates to existing content policies, or the development of policies on entirely new risk areas.

## Limitations

Judgments by language models are vulnerable to undesired biases that might have been introduced into the model during training. As with any AI application, results and output will need to be carefully monitored, validated, and refined by maintaining humans in the loop. By reducing human involvement in some parts of the moderation process that can be handled by language models, human resources can be more focused on addressing the complex edge cases most needed for policy refinement. As we continue to refine and develop this method, we remain committed to transparency and will continue to share our learnings and progress with the community.

## Authors

Lilian Weng, Vik Goel, Andrea Vallone

## Acknowledgments

Ian Kivlichan, CJ Weinmann, Jeff Belgum, Todor Markov, Dave Willner

## Related articles

![Jetbrains > Hero > Media item > Asset](https://images.ctfassets.net/kftzwdyauwt9/46d99f08-c849-4c73-5a6c7b83ea9c/6e0eaaaf815df2a53f997b36ce57ad13/jetbrains.png?w=3840&q=90&fm=webp)

[Embedding AI into developer software

Mar 21, 2024](/index/jetbrains/)

![Unload](https://images.ctfassets.net/kftzwdyauwt9/15d768b2-bd52-4e68-bebaf96d50b3/e3f414371811a69d73091cc36a44ce8f/holiday_extras.png?w=3840&q=90&fm=webp)

[Building a data-driven, efficient culture with AI

Mar 18, 2024](/index/holiday-extras/)

![Screenshot 2024 03 12 At 1128 27am](https://images.ctfassets.net/kftzwdyauwt9/e4cda57a-c977-4855-16b96e288c99/40db1a7d78522f9f9030942dd4a3e72b/superhuman.png?w=3840&q=90&fm=webp)

[Reimagining the email experience with AI

Mar 18, 2024](/index/superhuman/)
