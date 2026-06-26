<!-- source: https://openai.com/index/critiques/ -->

June 13, 2022

[Publication](/research/index/publication/)

# AI-written critiques help humans notice flaws

[Read paper(opens in a new window)](https://arxiv.org/abs/2206.05802)[View dataset(opens in a new window)](https://openaipublic.blob.core.windows.net/critiques/README.md)

![Ai Written Critiques Help Humans Notice Flaws](https://images.ctfassets.net/kftzwdyauwt9/533e7e34-5b5d-4f0b-c175293c0363/1e96f2bf24cec03d982566ac4125beb1/image-8.webp?w=3840&q=90&fm=webp)

We trained “critique-writing” models to describe flaws in summaries. Human evaluators find flaws in summaries much more often when shown our model’s critiques. Larger models are better at self-critiquing, with scale improving critique-writing more than summary-writing. This shows promise for using AI systems to assist human supervision of AI systems on difficult tasks.

We want to ensure that future AI systems performing very difficult tasks remain aligned with human intent. [Many⁠](/index/learning-to-summarize-with-human-feedback/) [previous⁠(opens in a new window)](https://arxiv.org/abs/2204.05862) [works⁠(opens in a new window)](https://www.deepmind.com/publications/gophercite-teaching-language-models-to-support-answers-with-verified-quotes) on [aligning language models⁠](/index/instruction-following/) rely on human evaluations as a training signal. However, humans struggle at evaluating very difficult tasks—for example, it is hard to spot every bug in a codebase or every factual error in a long essay. Models may then learn to give outputs that look good to humans but have errors we systematically fail to notice.

To mitigate this problem, we want to train AI assistants that help humans provide feedback on hard tasks. These assistants should point out flaws, help humans understand what’s going on, and answer their questions. An example of this is our past work on [book summarization⁠](/index/summarizing-books/): reading the entire book is a lot of work, but humans assisted with chapter summaries have a much easier time evaluating a book summary.

As a proof of concept, we used supervised learning to train language models to write critiques of topic-based summaries of short stories, Wikipedia articles, and other texts from the internet. We use these models to assist human evaluators and study scaling properties of critique writing.

## Experiments with AI assistance

Loading...

To see how useful our models are for evaluation assistance, we show labelers 8 model-written critiques of each summary, with a control group that receives no assistance. We use topic-based summaries from three sources: written by our models, written by humans, and written by humans deliberately to have important yet subtle flaws.

Loading...

Even though summarization isn’t actually a difficult task for humans and our models aren’t more capable than humans, they already provide meaningful assistance: when asked to evaluate model-written summaries, the assisted group finds 50% more flaws than the control group. For deliberately misleading summaries, assistance increases how often humans spot the intended flaw from 27% to 45%.

## Scaling properties of critiques

Assistance on model-written summaries only works if they are able to critique themselves. We ask humans to rate the helpfulness of model-written self-critiques, and find larger models are better at self-critiquing.

Loading...

We also find that large models are able to directly improve their outputs, using their self-critiques, which small models are unable to do. Using better critiques helps models make better improvements than they do with worse critiques, or with no critiques.

## Do models tell us everything they know?

To provide the best evaluation assistance on difficult tasks, we would like models to communicate all problems that they “know about.” Whenever a model correctly predicts that an answer is flawed, can the model also produce a concrete critique that humans understand?

This is particularly important for supervising models that could attempt to mislead human supervisors or hide information. We would like to train equally smart assistance models to point out what humans don’t notice.

Unfortunately, we found that models are better at discriminating than at critiquing their own answers, indicating they know about some problems that they can’t or don’t articulate. Furthermore, the gap between discrimination and critique ability did not appear to decrease for larger models. Reducing this gap is an important priority for our alignment research.

## Next steps

An important limitation of this work is that topic-based summarization is not actually a difficult task: humans understand it quite well and it takes them only about 10 minutes to evaluate a summary. To understand the limits of AI-assisted evaluation better, we need to work with tasks that are much more difficult for humans to evaluate.

Nevertheless, these results make us optimistic that we can train models to provide humans with meaningful feedback assistance. This is an important pillar of our alignment strategy, starting with the work on [debate⁠](/index/debate/) and [recursive reward modeling⁠(opens in a new window)](https://deepmindsafetyresearch.medium.com/scalable-agent-alignment-via-reward-modeling-bf4ab06dfd84). In the long run, we want to build assistants that can be trusted to take on all of the cognitive labor needed for evaluation, so humans can focus on communicating their preferences.

* [GPT](/research/index/?tags=gpt)
* [Language](/research/index/?tags=language)
* [Learning Paradigms](/research/index/?tags=learning-paradigms)

## Authors

Jan Leike, Jeffrey Wu, Catherine Yeh, William Saunders

## Related articles

![Disrupting malicious > media](https://images.ctfassets.net/kftzwdyauwt9/5080983d-9c4d-4479-17e421d7380a/0b42f77c2478bc5bc7bde3fddfc68462/45.png?w=3840&q=90&fm=webp)

[Disrupting malicious uses of AI by state-affiliated threat actors

SecurityFeb 14, 2024](/index/disrupting-malicious-uses-of-ai-by-state-affiliated-threat-actors/)

![](https://images.ctfassets.net/kftzwdyauwt9/ec66425e-99ca-4314-d04b087f8727/de7341b6a5281c2a220b93a737ce19b0/building-an-early-warning-system-for-llm-aided-biological-threat-creation.jpg?w=3840&q=90&fm=webp)

[Building an early warning system for LLM-aided biological threat creation

PublicationJan 31, 2024](/index/building-an-early-warning-system-for-llm-aided-biological-threat-creation/)

![Democratic Inputs To AI Grant Program Update](https://images.ctfassets.net/kftzwdyauwt9/f50ce1d2-4f61-4ed2-e560c624d631/6f4dd4542898a35d0a91b137f85c9834/Democratic_inputs_to_AI_grant_program_lessons_learned_and_implementation_plans.jpg?w=3840&q=90&fm=webp)

[Democratic inputs to AI grant program: lessons learned and implementation plans

SafetyJan 16, 2024](/index/democratic-inputs-to-ai-grant-program-update/)
