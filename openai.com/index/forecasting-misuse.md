<!-- source: https://openai.com/index/forecasting-misuse/ -->

January 11, 2023

[Publication](/research/index/publication/)

# Forecasting potential misuses of language models for disinformation campaigns and how to reduce risk

[Read paper(opens in a new window)](https://arxiv.org/abs/2301.04246)

![Forecasting Misuse](https://images.ctfassets.net/kftzwdyauwt9/2e288b87-2d80-4fa6-fec534506748/3d7f206ca8ff228951b0309760646cb0/image-32.webp?w=3840&q=90&fm=webp)

Illustration: Justin Jay Wang

OpenAI researchers collaborated with Georgetown University’s Center for Security and Emerging Technology and the Stanford Internet Observatory to investigate how large language models might be misused for disinformation purposes. The collaboration included an October 2021 workshop bringing together 30 disinformation researchers, machine learning experts, and policy analysts, and culminated in a co-authored report building on more than a year of research. This report outlines the threats that language models pose to the information environment if used to augment disinformation campaigns and introduces a framework for analyzing potential mitigations. Read the full report [here⁠(opens in a new window)](https://arxiv.org/abs/2301.04246).

As generative language models improve, they open up new possibilities in fields as diverse as healthcare, law, education and science. But, as with any new technology, it is worth considering how they can be misused. Against the backdrop of recurring online influence operations—*covert* or *deceptive* efforts to influence the opinions of a target audience—the paper asks:

> How might language models change influence operations, and what steps can be taken to mitigate this threat?

Our work brought together different backgrounds and expertise—researchers with grounding in the tactics, techniques, and procedures of online disinformation campaigns, as well as machine learning experts in the generative artificial intelligence field—to base our analysis on trends in both domains.

We believe that it is critical to analyze the threat of AI-enabled influence operations and outline steps that can be taken *before* language models are used for influence operations at scale. We hope our research will inform policymakers that are new to the AI or disinformation fields, and spur in-depth research into potential mitigation strategies for AI developers, policymakers, and disinformation researchers.

## How Could AI Affect Influence Operations?

When researchers evaluate influence operations, they consider the [actors, behaviors, and content⁠(opens in a new window)](https://www.ivir.nl/publicaties/download/ABC_Framework_2019_Sept_2019.pdf). The widespread availability of technology powered by language models has the potential to impact all three facets:

1. **Actors**: Language models could drive down the cost of running influence operations, placing them within reach of new actors and actor types. Likewise, propagandists-for-hire that automate production of text may gain new competitive advantages.
2. **Behavior**: Influence operations with language models will become easier to scale, and tactics that are currently expensive (e.g., generating personalized content) may become cheaper. Language models may also enable new tactics to emerge—like real-time content generation in chatbots.
3. **Content**: Text creation tools powered by language models may generate more impactful or persuasive messaging compared to propagandists, especially those who lack requisite linguistic or cultural knowledge of their target. They may also make influence operations less discoverable, since they repeatedly create new content without needing to resort to copy-pasting and other noticeable time-saving behaviors.

Our bottom-line judgment is that language models will be useful for propagandists and will likely transform online influence operations. Even if the most advanced models are kept private or controlled through application programming interface (API) access, propagandists will likely gravitate towards open-source alternatives and nation states may invest in the technology themselves.

## Critical Unknowns

Many factors impact whether, and the extent to which, language models will be used in influence operations. Our report dives into many of these considerations. For example:

* What new capabilities for influence will emerge as a side effect of well-intentioned research or commercial investment? Which actors will make significant investments in language models?
* When will easy-to-use tools to generate text become publicly available? Will it be more effective to engineer specific language models for influence operations, rather than apply generic ones?
* Will norms develop that disincentivize actors who wage AI-enabled influence operations? How will actor intentions develop?

While we expect to see diffusion of the technology as well as improvements in the usability, reliability, and efficiency of language models, many questions about the future remain unanswered. Because these are critical possibilities that can change how language models may impact influence operations, additional research to reduce uncertainty is highly valuable.

## A Framework for Mitigations

To chart a path forward, the report lays out key stages in the language model-to-influence operation pipeline. Each of these stages is a point for potential mitigations.To successfully wage an influence operation leveraging a language model, propagandists would require that: (1) a model exists, (2) they can reliably access it, (3) they can disseminate content from the model, and (4) an end user is affected. Many possible mitigation strategies fall along these four steps, as shown below.

| **Stage in the pipeline** | **1. Model Construction** | **2. Model Access** | **3. Content Dissemination** | **4. Belief Formation** |
| --- | --- | --- | --- | --- |
|  | AI developers build models that are more fact-sensitive. | AI providers impose stricter usage restrictions on language models. | Platforms and AI providers coordinate to identify AI content. | Institutions engage in media literacy campaigns. |
|  | Developers spread radioactive data to make generative models detectable. | AI providers develop new norms around model release. | Platforms require “proof of personhood” to post. | Developers provide consumer focused AI tools. |
| **Illustrative Mitigations** | Governments impose restrictions on data collection. | AI providers close security vulnerabilities. | Entities that rely on public input take steps to reduce their exposure to misleading AI content. |  |
|  | Governments impose access controls on AI hardware. |  | Digital provenance standards are widely adopted. |  |

## If a Mitigation Exists, is it Desirable?

Just because a mitigation could reduce the threat of AI-enabled influence operations does not mean that it should be put into place. Some mitigations carry their own downside risks. Others may not be feasible. While we do not explicitly endorse or rate mitigations, the paper provides a set of guiding questions for policymakers and others to consider:

* **Technical Feasibility**: Is the proposed mitigation technically feasible? Does it require significant changes to technical infrastructure?
* **Social Feasibility**: Is the mitigation feasible from a political, legal, and institutional perspective? Does it require costly coordination, are key actors incentivized to implement it, and is it actionable under existing law, regulation, and industry standards?
* **Downside Risk**: What are the potential negative impacts of the mitigation, and how significant are they?
* **Impact**: How effective would a proposed mitigation be at reducing the threat?

We hope this framework will spur ideas for other mitigation strategies, and that the guiding questions will help relevant institutions begin to consider whether various mitigations are worth pursuing.

This report is far from the final word on AI and the future of influence operations. Our aim is to define the present environment and to help set an agenda for future research. We encourage anyone interested in collaborating or discussing relevant projects to connect with us. For more, read the full report [here⁠(opens in a new window)](https://arxiv.org/abs/2301.04246).

* [GPT](/research/index/?tags=gpt)
* [Ethics & Safety](/research/index/?tags=ethics-safety)
* [Reasonings & Policy](/research/index/?tags=reasoning-policy)
* [Language](/research/index/?tags=language)
* [Community & Collaboration](/research/index/?tags=community-collaboration)

## Report authors

Josh A. Goldstein (Georgetown University’s Center for Security and Emerging Technology)Girish Sastry (OpenAI)Micah Musser (Center for Security and Emerging Technology)Renée DiResta (Stanford Internet Observatory)Matthew Gentzel (Longview Philanthropy) (work done at OpenAI)Katerina Sedova (US Department of State) (work done at Center for Security and Emerging Technology prior to government service)

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
