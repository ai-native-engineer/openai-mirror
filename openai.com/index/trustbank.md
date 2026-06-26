<!-- source: https://openai.com/index/trustbank/ -->

January 27, 2026

# TRUSTBANK uses AI agents to personalize Furusato Nozei gifts

TRUSTBANK partnered with Recursive to build Choice AI using OpenAI models, simplifying Furusato Nozei gift discovery.

[Contact sales](/contact-sales/)

![TRUSTBANK Furusato Nozei gifts hero image](https://images.ctfassets.net/kftzwdyauwt9/66RV8MMCS4GLOXB9iPjRVf/7a1183790aaad5a7a537c0e2ef99e5a8/oai_TrustBank_English_1x1.png?w=3840&q=90&fm=webp)

Company size: Enterprise, Partner

Region: Asia-Pacific & Oceania

Industry: Finance

Products: API

Japan's hometown tax donation program, known as Furusato Nozei, allows taxpayers to support municipalities they care about by making a donation. As people move to large cities like Tokyo, local tax bases in rural towns shrink, so the program was designed to let taxpayers redirect a portion of their taxes to the communities they want to support. In practice, it works through a tax credit system: up to an income based cap, most of the donated amount is credited against the donor's income and resident taxes for the following year. In return, municipalities send donors thank-you gifts, typically local specialty products, so donors can enjoy regional offerings while contributing to local communities.

However, many donors find the program difficult to navigate, given the sheer number of municipalities and the enormous catalog of thank-you gifts. To simplify the process and help donors compare options by region or theme, dedicated platforms have emerged. Furusato Choice, operated by TRUSTBANK, is one of Japan's largest Furusato Nozei platforms, with roughly 760,000 thank-you gifts listed. Its intuitive interface has helped municipalities connect with donors, and it has supported many platform users, especially those participating for the first time.

To further improve the experience, TRUSTBANK looked to AI, recognizing its potential to help users make decisions when the range of options feels overwhelming. Using the OpenAI API, the company developed the Choice AI feature, which helps users discover thank-you gifts that match their preferences.

> “Many people find the hometown tax donation system complicated or intimidating.”

—Yuki Tateyama, Product General Manager at Choice Business HQ

## Building Choice AI through collaboration with Recursive

More than 15 years after Furusato Nozei was introduced, many taxpayers still struggle to make the most of it. Yuki Tateyama, Product General Manager at Choice Business HQ, explains, Many people find the hometown tax donation system complicated or intimidating. To address this, we added AI powered features to our Furusato Choice app to make the process easier to navigate. TRUSTBANK's first step was to introduce AI powered search to help users explore thank-you gifts.

Tateyama adds, In the Furusato Nozei system, people are not simply shopping for products they need immediately, as they might on typical ecommerce platforms. Instead, they focus on how to make the best use of their donation limit. With a catalog of thank you gifts on par with major online marketplaces, finding the right option has always been challenging.

![Choice AI phone screens in Furusato Choice app](https://images.ctfassets.net/kftzwdyauwt9/2gBEuuSVlfz68Bw3ub5CKh/fd81ea2466ab5951fc18ca47776762de/TrustBank_UI.png?w=3840&q=90&fm=webp)

Providing personalized recommendations for thank-you gifts, based on each user's information and intent, is an area where AI can be especially effective. However, TRUSTBANK did not have internal developers who specialized in AI, so external support was essential. To address this, TRUSTBANK partnered with Recursive, now an official OpenAI services partner.

Issei Hirano, Head of Platform Promotion in the Product Division, explains the decision, We selected Recursive as our partner because of their advanced AI expertise and their global experience.

He describes how the teams worked together. Recursive provided technical support from the planning stage, designed and implemented the conversational AI agent, and built the RAG system. We prepared the thank-you gift database, defined functional requirements, and integrated these features into our app. This collaboration enabled a smooth build and rollout of Choice AI, allowing users to discover recommended items through interactive conversations within the Furusato Choice app.

## Driving personalization using a multi agent architecture

The core of Choice AI is its multiagent architecture. A routing model analyzes user input to determine intent and delegates tasks to the appropriate agents. Beneath this routing layer, specialized agents such as the Search Agent, Recommendation Agent, and Greeting Agent operate. Each agent can invoke additional subagents and tools, enabling smooth orchestration and accurate, intent based results.

Personalization is also built into the prompting. Matthew Whalley, a software engineer at Recursive who led agent development, explains, We combine agents dynamically based on user specific information. For instance, existing users follow one interaction path, while first time users follow another. We dynamically generate prompts to manage these interaction paths.

![Choice AI multi agent architecture diagram](https://images.ctfassets.net/kftzwdyauwt9/2cr9RZWaSUs2qcgOjCTtLn/899b14b88b4e349d1665c7026fffd45f/Trustbank_Chart_Light.png?w=3840&q=90&fm=webp)

Choice AI currently runs on the GPT‑4.1 series. Whalley explains, By default, we use GPT‑4.1 mini, but we are experimenting with dynamically switching to either the nano version or larger models based on latency and accuracy during testing.

Whalley also notes that analyzing real user behavior led to new insights: Our analysis revealed that many users interact with the app similarly to how they would use a search engine. They provide extensive product information to the LLM and expect immediate recommendations. We also found that short, built in prompts designed to start conversations were used frequently. Based on these findings, the team incorporated a range of improvements into Choice AI. For example, the recommendation flow was adjusted to surface suggestions earlier, and the variety of recommended products was expanded to increase exposure to more diverse options.

## Results at a glance

Choice AI addresses two challenges in the Furusato Nozei experience:

* Reducing user confusion caused by the vast number of thank-you gifts, by offering personalized recommendations through interactive conversations.
* Avoiding concentration on a small set of municipalities or popular items, by helping users discover a wider range of regions and thank-you gifts through tailored suggestions.

With the multiagent architecture inside Choice AI, users can find relevant thank-you gifts even without search skills or detailed product knowledge. Natural conversations, or even vague requests such as a gift for my parents, can be enough to surface suitable recommendations.

Choice AI reduces bias toward specific municipalities or items by adding controlled randomness to search results. Whalley explains, We introduce randomness and vary recommendations across prefectures based on donation data to support fairness and regional diversity, unless users clearly indicate their preferences. This helps users discover smaller municipalities and niche products, creating a more diverse and engaging experience.

As a result, users who used Choice AI saw higher conversion rates than those who relied on standard on-site search. Hirano explains the reason, saying, Because the AI could draw out vague needs, like preferences and budget, that users themselves often struggled to put into words, and could even recommend specific thank-you gifts.

## What's next

Today, Furusato Choice primarily uses AI to improve the experience of searching for thank-you gifts, helping users quickly find options that fit their needs. Looking ahead, the company plans to expand AI into additional areas and further enhance the overall value of the service.

Tateyama envisions Furusato Choice becoming a platform that connects users and municipalities through genuine goodwill, rather than focusing only on economic benefit. To support that vision, the company aims to refine the quality of AI driven recommendations and personalize the end to end user experience, ultimately creating a concierge style service that is closely attuned to each individual user.

## Keep reading

![How agents are transforming work > Cover image](https://images.ctfassets.net/kftzwdyauwt9/7hmtkjKv0DxS4Yt8mQZju2/c168bfa2010da64bcc9dd60d6b5491e8/Art_Card__1_.png?w=3840&q=90&fm=webp)

[How agents are transforming work

CompanyJun 25, 2026](/index/how-agents-are-transforming-work/)

![OpenAI and Broadcom Jalapeño inference chip card image](https://images.ctfassets.net/kftzwdyauwt9/21KcazqOHUF7Cq71Hpfcnc/81ad98a1978845b441ab14e008168c75/openai-broadcom-jalapeno-inference-chip-image-1_1.png?w=3840&q=90&fm=webp)

[OpenAI and Broadcom unveil LLM-optimized inference chip

CompanyJun 24, 2026](/index/openai-broadcom-jalapeno-inference-chip/)

![Helping build shared standards for advanced AI - card image](https://images.ctfassets.net/kftzwdyauwt9/3tqr0Vb3JnK38uBRBw7FAF/a3989888ee148ba286b834076aaa289b/helping-build-shared-standards-for-advanced-ai-1_1.png?w=3840&q=90&fm=webp)

[Helping build shared standards for advanced AI

Global AffairsJun 23, 2026](/index/helping-build-shared-standards-for-advanced-ai/)
