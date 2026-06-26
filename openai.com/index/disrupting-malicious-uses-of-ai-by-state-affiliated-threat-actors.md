<!-- source: https://openai.com/index/disrupting-malicious-uses-of-ai-by-state-affiliated-threat-actors/ -->

February 14, 2024

[Security](/news/security/)

# Disrupting malicious uses of AI by state-affiliated threat actors

We terminated accounts associated with state-affiliated threat actors. Our findings show our models offer only limited, incremental capabilities for malicious cybersecurity tasks.

![Softly blurred digital painting of an orange flower with a green stem against a warm yellow-orange background.](https://images.ctfassets.net/kftzwdyauwt9/5080983d-9c4d-4479-17e421d7380a/0b42f77c2478bc5bc7bde3fddfc68462/45.png?w=3840&q=90&fm=webp)

We build AI tools that improve lives and help solve complex challenges, but we know that malicious actors will sometimes try to abuse our tools to harm others, including in furtherance of cyber operations. Among those malicious actors, state-affiliated groups—which may have access to advanced technology, large financial resources, and skilled personnel—can pose unique risks to the digital ecosystem and human welfare. 

In partnership with Microsoft Threat Intelligence, we have disrupted five state-affiliated actors that sought to use AI services in support of malicious cyber activities. We also outline our approach to detect and disrupt such actors in order to promote information sharing and transparency regarding their activities.

## Disruption of threat actors

Based on collaboration and information sharing with Microsoft, we disrupted five state-affiliated malicious actors: two China-affiliated threat actors known as Charcoal Typhoon and Salmon Typhoon; the Iran-affiliated threat actor known as Crimson Sandstorm; the North Korea-affiliated actor known as Emerald Sleet; and the Russia-affiliated actor known as Forest Blizzard. The identified OpenAI accounts associated with these actors were terminated.

These actors generally sought to use OpenAI services for querying open-source information, translating, finding coding errors, and running basic coding tasks. 

Specifically: 

* Charcoal Typhoon used our services to research various companies and cybersecurity tools, debug code and generate scripts, and create content likely for use in phishing campaigns.
* Salmon Typhoon used our services to translate technical papers, retrieve publicly available information on multiple intelligence agencies and regional threat actors, assist with coding, and research common ways processes could be hidden on a system.
* Crimson Sandstorm used our services for scripting support related to app and web development, generating content likely for spear-phishing campaigns, and researching common ways malware could evade detection.
* Emerald Sleet used our services to identify experts and organizations focused on defense issues in the Asia-Pacific region, understand publicly available vulnerabilities, help with basic scripting tasks, and draft content that could be used in phishing campaigns.
* Forest Blizzard used our services primarily for open-source research into satellite communication protocols and radar imaging technology, as well as for support with scripting tasks.

Additional technical details on the nature of the threat actors and their activities can be found in the [Microsoft blog post⁠(opens in a new window)](https://aka.ms/emerging-AI-threats) published today. 

The activities of these actors are consistent with previous [red team assessments⁠(opens in a new window)](https://cdn.openai.com/papers/gpt-4.pdf) we conducted in partnership with external cybersecurity experts, which found that GPT‑4 offers only limited, incremental capabilities for malicious cybersecurity tasks beyond what is already achievable with publicly available, non-AI powered tools\_.\_

## A multi-pronged approach to AI safety

Although the capabilities of our current models for malicious cybersecurity tasks are limited, we believe it’s important to stay ahead of significant and evolving threats. To respond to the threat, we are taking a multi-pronged approach to combating malicious state-affiliated actors’ use of our platform: 

* **Monitoring and disrupting malicious state affiliated actors.** We invest in technology and teams to identify and disrupt sophisticated threat actors’ activities. Our Intelligence and Investigations, Safety, Security, and Integrity teams investigate malicious actors in a variety of ways, including using our models to pursue leads, analyze how adversaries are interacting with our platform, and assess their broader intentions. Upon detection, OpenAI takes appropriate action to disrupt their activities, such as disabling their accounts, terminating services, or limiting access to resources.
* **Working together with the AI ecosystem.** OpenAI collaborates with industry partners and other stakeholders to regularly exchange information about malicious state-affiliated actors’ detected use of AI. This collaboration reflects our [voluntary commitment⁠](/index/moving-ai-governance-forward/) to promote the safe, secure and transparent development and use of AI technology, and aims to promote collective responses to ecosystem-wide risks via information sharing.
* **Iterating on safety mitigations.** Learning from real-world use (and misuse) is a key component of creating and releasing increasingly safe AI systems over time. We take lessons learned from these actors' abuse and use them to inform our iterative approach to safety. Understanding how the most sophisticated malicious actors seek to use our systems for harm gives us a signal into practices that may become more widespread in the future, and allows us to continuously evolve our safeguards.
* **Public transparency.** We have long sought to highlight potential misuses of AI [[link 1⁠(opens in a new window)](https://cdn.openai.com/papers/gpt-4-system-card.pdf), [link 2⁠](/index/forecasting-misuse/)] and share what we have [learned⁠](/index/language-model-safety-and-misuse/) about safety [[link 1,⁠](/index/language-model-safety-and-misuse/) [link 2]⁠](https://openai.com/blog/best-practices-for-deploying-language-models) with the industry and the public. As part of our ongoing efforts to advance responsible use of AI, OpenAI will continue to inform the public and stakeholders about the nature and extent of malicious state-affiliated actors’ use of AI detected within our systems and the measures taken against them, when warranted. We believe that sharing and transparency foster greater awareness and preparedness among all stakeholders, leading to stronger collective defense against ever-evolving adversaries.

The vast majority of people use our systems to help improve their daily lives, from virtual tutors for students to apps that can transcribe the world for people who are seeing impaired. As is the case with many other ecosystems, there are a handful of malicious actors that require sustained attention so that everyone else can continue to enjoy the benefits. Although we work to minimize potential misuse by such actors, we will not be able to stop every instance. But by continuing to innovate, investigate, collaborate, and share, we make it harder for malicious actors to remain undetected across the digital ecosystem and improve the experience for everyone else.

* [Alignment](/news/?tags=alignment)
* [Policies and Procedures](/news/?tags=policies-procedures)
* [2024](/news/?tags=2024)

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
