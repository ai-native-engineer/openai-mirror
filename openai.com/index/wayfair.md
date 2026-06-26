<!-- source: https://openai.com/index/wayfair/ -->

March 11, 2026

# Wayfair boosts catalog accuracy and support speed with OpenAI

By embedding OpenAI models in supplier and catalog systems, Wayfair improved data accuracy and automated workflows for millions of products.

[Contact sales](/contact-sales/)

![Wayfair logo in white on a purple textured background.](https://images.ctfassets.net/kftzwdyauwt9/1AHxshp97DsdLFaEA7wNFe/f11dd8a1aa25536c436b50c62fec9210/oai_wayfair_1x1.png?w=3840&q=90&fm=webp)

Company size: Enterprise

Region: North America

Industry: Retail

Products: API, ChatGPT

Results

2.5M

Product tags corrected

Results

41K

Supplier support tickets automated per month

Results

1,200

ChatGPT Enterprise seats deployed

Wayfair, one of the world’s largest home goods retailers, has integrated OpenAI models into critical internal systems to improve supplier support workflows and product catalog quality at scale. What began as value-testing small scale releases in 2024 has evolved into a full production system that reduces manual effort, accelerates decision-making and improves data quality across millions of products.

Rather than treat generative AI as an experiment or point solution, Wayfair embedded OpenAI models into core operational workflows. The company focused first where complexity and need for scale were highest: routing and resolving supplier support requests and improving tens of thousands of product attributes consistently across a catalog of roughly 30 million items.

> “What’s been most valuable is the thought partnership. It’s not just access to the models. It’s working through new use cases together and being able to move quickly.”

—Fiona Tan, Chief Technology Officer

## Solving catalog quality at scale

Wayfair’s catalog team manages tens of millions of products across nearly a thousand different product classes. Consistent and accurate product attribute tags—such as color, material, size or specific features—are essential for search, recommendations and merchandising.

"The better our data quality, the more trust we build with the customer. It's essential because it empowers shoppers to make the right buying decisions, directly reducing costly downstream issues like returns from misrepresented products," said Jessica D'Arcy, Associate Director of Catalog Merchandising at Wayfair.

Before OpenAI, tagging improvements primarily relied on suppliers and customers to tell Wayfair that something looked wrong. Manual effort could not keep up with the volume.  Early custom AI models for individual tags were effective, but proved expensive to build and maintain. “We started by building bespoke models for individual tags, and technically that worked,” said Carolyn Phillips, Wayfair’s staff machine learning scientist. “But when you’re looking at 47,000 tags, that approach just doesn’t scale.”

## Building a reusable AI architecture

![UI screenshot of an AI product quality review for a “Round Walnut Solid Wood Coffee Table, 28.7”.” On the left is a product photo of a low round wooden coffee table with cylindrical legs and a vase on top. On the right is a table comparing Original Value vs AI Correction for product attributes. The AI flags several issues: correcting wood species from Walnut to Pine, changing leg design from Bun Feet to Straight Legs, marking Unfinished and Scalloped Edges as No, and adding Drawers Included: No. Dimensions and tabletop thickness remain unchanged. A banner indicates AI Quality Review – 5 issues found, and a footer notes 4 corrections made, 1 attribute added, 2 attributes verified, with all corrections applied automatically.](https://images.ctfassets.net/kftzwdyauwt9/6OP1wkY8q6cQDaebaOCy8U/513037c865bc884734619fe30dec1b7e/wayfair_16x9_AIQR.png?w=3840&q=90&fm=webp)

To get beyond one-off models, Wayfair created a tag-agnostic system built on a single OpenAI model. A “definition agent” ingests the web and internal definitions to produce contextual meaning for each tag. “The real bottleneck wasn’t the model performance,” said Phillips. “It was the human time required to define and encode what each tag actually meant.” This context, along with product data aggregated from across Wayfair’s data ecosystem, feeds into a framework that can classify attributes across product classes. The team is now expanding model coverage to new attributes at 70x the rate they were just a year ago.

The system has now run in production on more than 1 million products. And the first wave of products with enhanced attributes has now been live long enough to measure the impact of improving data quality on the customer journey.  “When you improve attribute completeness, it’s not abstract. You see it show up in SEO and PLA performance—in how customers discover products,” said Phillips. A controlled A/B test showed a substantial and significant increase in impressions, clicks, and page rank in the treatment group.

However, Wayfair didn't simply hand off decisions on correcting product data to the model. “Our objective is to build trust so that customers are completely confident in what they are purchasing,” said Phillips. The company developed structured testing using a hands-on audit process in which associates physically inspect samples to validate model output, and worked with suppliers to validate changes. Now, when data-based confidence is high, automated systems will overwrite the content directly and notify the supplier of the change. And, when a high standard is not met or the tag is deemed high risk, Wayfair first seeks supplier confirmation before making the change.

## Rethinking supplier support workflows with Wilma

Wayfair works with tens of thousands of suppliers to support their comprehensive catalog. To manage supplier support requests, Wayfair associates historically reviewed every incoming ticket, manually identified what suppliers were trying to accomplish, and routed issues to the correct internal owner—a time-consuming and error-prone process. “Supplier requests aren’t simple,” said Graham Ganssle, supplier support and operations at Wayfair. “They span hundreds of issue types, and no single associate can realistically master all of them.”

Wayfair added agentic features to a product named Wilma to augment these workflows with AI. One of the first features in production is ticket triage powered by an OpenAI model. The system reads incoming requests, fills in missing context and routes tickets to the appropriate team. Wilma was designed to be deployable fast; built on a system already integrated with OpenAI APIs, it moved from prototype to live in approximately one month. “Wilma gives associates leverage,” said Ganssle. “It reads the ticket, identifies intent, fills in context from our databases, reaches back out to suppliers if necessary, and points the issue in the right direction.”

Beyond routing, Wayfair has deployed a dozen agentic AI flows for specific resolution teams. For example, a co-pilot for the Replacement Part Operations team reads complex case history, proposes next steps and suggests draft responses that human associates review. These assistants are trained on historical data so they learn what success looks like in context. “The models can synthesize context across the entire journey in a way that’s hard for a single associate to do,” said Ganssle. “That broader visibility contributes to higher customer and supplier satisfaction.”

Wayfair tracks how often the AI’s recommendations match the human agent’s final decision—a metric called “alignment rate.” Within each team, when alignment consistently reaches a predetermined threshold, workflows can shift from assistive (“co-pilot”) to semi-autonomous (“autopilot”) modes. This staged approach builds trust and ensures quality controls during rollout.

> “If you don’t route the issue correctly at the start, everything downstream slows down. Triage is foundational.”

–Graham Ganssle, supplier support operations, Wayfair

## Results at a glance

Wayfair reports measurable improvements since integrating OpenAI models into internal systems.

On the catalog side, the company reduced the number of wrong or missing product attribute tags a customer might see—having corrected 2.5M product tags across over a million of the most visible and purchased products in the Wayfair catalog. They expect to quadruple this impact in the next six months.

In supplier support, triage, co-pilot, and auto-pilot systems have increased throughput by automating 41,000 tickets per month (that’s up to 70% in some workflows) and reduced turnaround times by removing routine manual work from associate workloads. This dramatically cuts time to resolution for multiple workflows, significantly lifts supplier satisfaction, and reduces ticket re-opens in those workflows.

The broader visibility that models provide into tickets and supplier intent—beyond what a single associate can see on a screen—has contributed to that increase in satisfaction.

Operationally, teams report:

* Faster routing and resolution of complex supplier tickets
* Increased supplier satisfaction
* Reduced manual data entry and classification work
* Broader issue coverage without requiring expertise across hundreds of topics
* Higher confidence in catalog attributes before publication.

Wayfair has also deployed more than 1,200 ChatGPT Enterprise seats across its approximately 12,000-person workforce to support ad hoc tasks, internal problem solving and experimentation with generative models.

## What’s next

Wayfair has a long history of investing in machine learning and collaboration with AI platforms and LLM providers to advance their business. Now, advances in frontier models, particularly multimodal systems, are expanding what its teams can build. That matters in home retail, where products are visual, stylistic and often subjective.

“We’re excited about the scope of problems we can now tackle,” said Carolyn Phillips. “Traditional algorithms require tightly defined datasets. These models allow us to work through ambiguity and context in a way that wasn’t previously scalable.”

Looking forward, the employee demand for ChatGPT Enterprise has been strong. Teams at Wayfair see it as a practical tool that helps them move faster.

Customer expectations are also shifting quickly. More shoppers are becoming comfortable using AI in their daily lives, and they are beginning to expect similar capabilities when they browse, compare and buy online.

“At home, customers often don’t have the exact words for what they’re looking for,” said Fiona Tan. “Natural language and multimodal systems help bridge that gap.”

For Wayfair leaders, the goal remains to augment human expertise while scaling internal capability. “We’re building for a world where AI is part of the shopping journey—whether that’s on our site, through support, or through conversational interfaces,” concluded Fiona Tan.

## Join the new era of work

More than 1 million businesses around the world are achieving meaningful results with OpenAI.

[Contact sales](/contact-sales/)

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
