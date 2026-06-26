<!-- source: https://openai.com/index/teen-safety-policies-gpt-oss-safeguard/ -->

March 24, 2026

[Safety](/news/safety-alignment/)

# Helping developers build safer AI experiences for teens

Introducing a set of teen safety policies formatted as prompts for gpt-oss-safeguard

Today, we’re releasing prompt-based [safety policies⁠(opens in a new window)](https://github.com/openai/teen-safety-policy-pack) to help developers create age-appropriate protections for teens. Built to work with our open-weight safety model, [gpt-oss-safeguard⁠(opens in a new window)](https://huggingface.co/openai/gpt-oss-safeguard-20b), these policies simplify how developers turn safety requirements into usable classifiers for real-world systems.

We released open weight models to democratize access to powerful AI and support broad innovation. At the same time, we believe safety and innovation go hand in hand, and that developers should have access to capable models as well as the tools and policies to deploy them safely and responsibly. We developed these policies to support developers in their safety efforts to protect young users, with input from trusted external organizations including [Common Sense Media⁠(opens in a new window)](https://www.commonsensemedia.org) and [everyone.ai⁠(opens in a new window)](http://everyone.ai).

We recognize that teens and adults have different needs, and that teens need additional protections. These policies are designed to help developers account for those differences and build experiences that are both empowering and appropriate for younger users.

### Building on our broader work to protect young people

We have long been committed to building AI that expands opportunities for young people while keeping them safe. As part of this work, we updated our [Model Spec⁠(opens in a new window)](https://model-spec.openai.com/2025-12-18.html)—the guidelines that define the intended behavior of OpenAI’s models—to include [Under-18 (U18) principles⁠(opens in a new window)](https://model-spec.openai.com/2025-12-18.html#chatgpt_u18), and introduced product-level safeguards such as [parental controls⁠](https://openai.com/index/introducing-parental-controls/) and [age prediction⁠](https://openai.com/index/our-approach-to-age-prediction/) to better protect younger users. We have also called for industry-wide protections through our [Teen Safety Blueprint⁠](https://openai.com/index/introducing-the-teen-safety-blueprint/).

Today’s release builds on that foundation. We’re making these safety policies available to developers to support them in deploying safety protections for teens and helping democratize access across the open weights ecosystem.

### Translating teen safety into clear, usable policies

While safety classifiers like gpt-oss-safeguard can detect harmful content, they depend on clear definitions of what that content is. In practice, one of the biggest challenges developers face is defining policies that accurately capture teen-specific risks and can be consistently applied in real systems.   
  
Even experienced teams often struggle to translate high-level safety goals into precise, operational rules, especially since it requires both subject matter expertise and deep AI knowledge. This can lead to gaps in protection, inconsistent enforcement, or overly broad filtering. Clear, well-scoped policies are a critical foundation for effective safety systems.

### Helping developers operationalize teen safety

To address this challenge, we are releasing a set of [safety policies⁠(opens in a new window)](https://github.com/openai/teen-safety-policy-pack), tailored to common risks faced by teens and informed by careful review of existing research about teens’ unique developmental differences. These policies are structured as prompts that can be directly used with [gpt-oss-safeguard⁠(opens in a new window)](https://huggingface.co/openai/gpt-oss-safeguard-20b) and other reasoning models, enabling developers to more easily apply consistent safety standards across their systems.

The initial release includes policies covering:

* Graphic violent content
* Graphic sexual content
* Harmful body ideals and behaviors
* Dangerous activities and challenges
* Romantic or violent roleplay
* Age-restricted goods and services

These policies can be used for real-time content filtering, as well as offline analysis of user-generated content.

By structuring policies as prompts, developers can more easily integrate them into existing workflows, adapt them to their use cases, and iterate over time.

![Diagram depicting teen safety policy categories and teen-related content feeding into a GPT-OSS safeguard system, which produces policy decisions informed by internal reasoning.](https://images.ctfassets.net/kftzwdyauwt9/tpc83mGxV22vPETJsE3DO/998e3a19c99a6dc13bb285282a4dd583/Translating_safety_policies_into_enforceable_safeguards.png?w=3840&q=90&fm=webp)

### Developed with input from external experts

We worked with external organizations including [Common Sense Media⁠(opens in a new window)](https://www.commonsensemedia.org) and [everyone.ai⁠(opens in a new window)](http://everyone.ai) to inform the development of these policies. Their expertise helped shape the scope of content to cover, strengthen the structure of the prompts, and refine the edge cases to consider when evaluating them.

This work reflects an ongoing effort to collaborate with experts and the broader ecosystem to improve how AI systems support young people.

*“One of the biggest gaps in AI safety for teens has been the lack of clear, operational policies that developers can build from. Many times, developers are starting from scratch. These prompt-based policies help set a meaningful safety floor across the ecosystem, and because they're released as open source, they can be adapted and improved over time. We're encouraged to see this kind of infrastructure being made available broadly, and we hope it catalyzes more shared youth-safety starting points across the industry.”*

—**Robbie Torney, Head of AI & Digital Assessments, Common Sense Media**

*“Efforts like this that make youth safety policies more operational are valuable because they help translate expert knowledge into guidance that can be used in real systems. Content policies are an important first step, and they also open the door to broader work on how model behavior can shape youth-relevant risks over time. Inspired by this work and our own research,* [*everyone.ai*⁠(opens in a new window)](http://everyone.ai/) *has also created an initial behavioral policy focused on risks like exclusivity and overreliance."*

*—***Dr. Mathilde Cerioli, Chief Scientist at everyone.AI**

### A starting point, not a complete solution

The policies are intended as a starting point, not as a comprehensive or final definition or guarantee of teen safety. Each application has unique risks, audiences and contexts, and developers are best positioned to understand the risks that their products and AI integrations may present. We strongly encourage developers to adapt and extend these policies based on their specific needs and combine them with other safeguards such as product design decisions, user controls, teen-friendly transparency, monitoring systems and thoughtful, age-appropriate responses.

We believe a layered [defense in depth⁠⁠](https://openai.com/safety/how-we-think-about-safety-alignment/#defense-in-depth) approach is essential to building safer AI systems. These policies draw from our internal experience, but they do not reflect the full extent of OpenAI’s internal policies or safeguards.

### The road forward

We are releasing these policies as open source through the [ROOST Model Community⁠(opens in a new window)](https://github.com/roostorg/model-community) to encourage collaboration and iteration. To contribute, provide feedback, or share additional teen safety policies, visit the [RMC GitHub repository.⁠(opens in a new window)](https://github.com/roostorg/open-models)

Developers and organizations can adapt these policies to their specific applications, translate them into different languages, and extend them to cover additional risk areas. Over time, we hope this contributes to a more robust and shared foundation for implementing safety policies in AI systems.

To get started with gpt-oss-safeguard, download it from [Hugging Face⁠(opens in a new window)](https://huggingface.co/collections/openai/gpt-oss-safeguard).

## Keep reading

![oai 1x1](https://images.ctfassets.net/kftzwdyauwt9/7eONRWq61MKUix4tK4t88Y/170085acc9b241a0bdfba429bd217907/oai_1x1.png?w=3840&q=90&fm=webp)

[Advancing youth safety and opportunity through global leadership

Global AffairsJun 2, 2026](/index/advancing-youth-safety-and-opportunity-through-global-leadership/)

![Technical foundations > Art Card](https://images.ctfassets.net/kftzwdyauwt9/6gugGfSiM1oO6UHxxwnqTk/c7173a5a2c096a8f8a24c258ddfa22dd/ArtCard-TechnicalFoundations.png?w=3840&q=90&fm=webp)

[A shared playbook for trustworthy third party evaluations

SafetyMay 29, 2026](/index/trustworthy-third-party-evaluations-foundations/)

![Frontier Governance Framework > card image ](https://images.ctfassets.net/kftzwdyauwt9/2KoiHuErR5YxXGUnhCU8VY/e392c6249ec4644e07e944edea22e837/Frame2.png?w=3840&q=90&fm=webp)

[OpenAI’s Frontier Governance Framework

SafetyMay 28, 2026](/index/openai-frontier-governance-framework/)
