<!-- source: https://openai.com/index/best-practices-for-deploying-language-models/ -->

June 2, 2022

[Safety](/news/safety-alignment/)

# Best practices for deploying language models

Cohere, OpenAI, and AI21 Labs have developed a preliminary set of best practices applicable to any organization developing or deploying large language models.

![Best Practices For Deploying Language Models](https://images.ctfassets.net/kftzwdyauwt9/06a9f58f-9453-4482-c903ffc460d6/8bb53391cee0c5cd5dfd27275dc9ac9e/best-practices-for-deploying-language-models.png?w=3840&q=90&fm=webp)

Illustration: Justin Jay Wang

Cohere, OpenAI, and AI21 Labs have developed a preliminary set of best practices applicable to any organization developing or deploying large language models. Computers that can read and write are here, and they have the potential to fundamentally impact daily life. The future of human–machine interaction is full of possibility and promise, but any powerful technology needs careful deployment.

The joint statement below represents a step towards building a community to address the global challenges presented by AI progress, and we encourage other organizations who would like to participate to get in touch.

## Joint recommendation for language model deployment

We’re recommending several key principles to help providers of large language models (LLMs) mitigate the risks of this technology in order to achieve its full promise to augment human capabilities.

While these principles were developed specifically based on our experience with providing LLMs through an API, we hope they will be useful regardless of release strategy (such as open-sourcing or use within a company). We expect these recommendations to change significantly over time because the commercial uses of LLMs and accompanying safety considerations are new and evolving. We are actively learning about and addressing LLM limitations and avenues for misuse, and will update these principles and practices in collaboration with the broader community over time.

We’re sharing these principles in hopes that other LLM providers may learn from and adopt them, and to advance public discussion on LLM development and deployment.

### Prohibit misuse

**Publish usage guidelines and terms of use** of LLMs in a way that prohibits material harm to individuals, communities, and society such as through spam, fraud, or astroturfing. Usage guidelines should also specify domains where LLM use requires extra scrutiny and prohibit high-risk use-cases that aren’t appropriate, such as classifying people based on protected characteristics.

**Build systems and infrastructure to enforce usage guidelines**. This may include rate limits, content filtering, application approval prior to production access, monitoring for anomalous activity, and other mitigations.

### Mitigate unintentional harm

**Proactively mitigate harmful model behavior**. Best practices include comprehensive model evaluation to properly assess limitations, minimizing potential sources of bias in training corpora, and techniques to minimize unsafe behavior such as through learning from human feedback.

**Document known weaknesses and vulnerabilities**, such as bias or ability to produce insecure code, as in some cases no degree of preventative action can completely eliminate the potential for unintended harm. Documentation should also include model and use-case-specific safety best practices.

### Thoughtfully collaborate with stakeholders

**Build teams with diverse backgrounds** and solicit broad input. Diverse perspectives are needed to characterize and address how language models will operate in the diversity of the real world, where if unchecked they may reinforce biases or fail to work for some groups.

﻿**Publicly disclose lessons learned regarding LLM safety and misuse** in order to enable widespread adoption and help with cross-industry iteration on best practices.

**Treat all labor in the language model supply chain with respect**. For example, providers should have high standards for the working conditions of those reviewing model outputs in-house and hold vendors to well-specified standards (e.g., ensuring labelers are able to opt out of a given task).

As LLM providers, publishing these principles represents a first step in collaboratively guiding safer large language model development and deployment. We are excited to continue working with each other and with other parties to identify other opportunities to reduce unintentional harms from and prevent malicious use of language models.

* [Download as PDF(opens in a new window)](https://cdn.openai.com/papers/joint-recommendation-for-language-model-deployment.pdf)

## Support from other organizations

> “While LLMs hold a lot of promise, they have significant inherent safety issues which need to be worked on. These best practices serve as an important step in minimizing the harms of these models and maximizing their potential benefits.”
>
> —Anthropic

> “As large language models (LLMs) have become increasingly powerful and expressive, risk mitigation becomes increasingly important. We welcome these and other efforts to proactively seek to mitigate harms and highlight to users areas requiring extra diligence. The principles outlined here are an important contribution to the global conversation.”
>
> —John Bansemer, Director of the CyberAI Project and Senior Fellow, Center for Security and Emerging Technology (CSET)

> “Google affirms the importance of comprehensive strategies in analyzing model and training data to mitigate the risks of harm, bias, and misrepresentation. It is a thoughtful step taken by these AI providers to promote the principles and documentation towards AI safety.”
>
> —Google

> “To realize the promise of large language models, we must continue to collaborate as an industry and share best practices for how to responsibly develop and deploy them while mitigating potential risks. We welcome this and other efforts that drive thoughtful and practical action across the industry, learning from and working with key stakeholders in academia, civil society, and government.”
>
> —Microsoft

> “The safety of foundation models, such as large language models, is a growing social concern. We commend Cohere, OpenAI, and AI21 Labs for taking a first step to outline high-level principles for responsible development and deployment from the perspective of model developers. There is still much work to be done, and we believe it is essential to engage more voices from academia, industry, and civil society to develop more detailed principles and community norms. As we state in our recent [blog post⁠(opens in a new window)](https://crfm.stanford.edu/2022/05/17/community-norms.html), it is not just the end result but the legitimacy of the process that matters.”
>
> —Percy Liang, Director of the Stanford Center for Research on Foundation Models (CRFM)

## Get involved

If you’re developing language models or are working to mitigate their risks, we’d love to talk with you. Please reach out at [bestpractices@openai.com⁠](mailto:bestpractices@openai.com).

* [Framework](/news/?tags=framework)
* [2022](/news/?tags=2022)

## Author

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
