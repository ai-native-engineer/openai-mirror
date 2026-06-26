<!-- source: https://openai.com/index/paradigm/ -->

# Paradigm

Paradigm uses OpenAI’s API to improve patient access to clinical trials.

[View product](/index/gpt-4/)

![Paradigm Health logo over a close-up background of soft, textured, wavy lines in neutral tones.](https://images.ctfassets.net/kftzwdyauwt9/3ouTRDZlceBivKQP7lufNq/5643bd4bc2f7677bb05318880fc971a8/oai_paradigm-health_hero.png?w=3840&q=90&fm=webp)

Clinical trials are how we discover new cures, and they can be a life-saving form of treatment. [Paradigm⁠(opens in a new window)](https://www.paradigm.inc/) is breaking down barriers in the healthcare industry with technology that brings clinical trials to more people,  such as cancer patients, while reducing the paperwork burden for doctors and nurses to address clinician burnout.

![paradigm](https://images.ctfassets.net/kftzwdyauwt9/4OamB4lO3rgV8jNXXurnZs/3e9c7ac5eec099debfdb5f1f51e88f30/paradigm.png?w=3840&q=90&fm=webp)

## Clinical trial enrollment is broken

The evaluation of patient medical records is a major bottleneck for getting a patient enrolled in a clinical trial that might provide the best possible treatment option. Medical providers rarely have time to search through clinical trials, understand the details of the trial taking place, and then match and qualify patients. The result is that most clinical trials are filled by patients in close proximity to where the trial is taking place, creating bias in the selection process and preventing many patients from accessing the groundbreaking care that could save their lives. 

To solve this, Paradigm deployed and optimized traditional best practice, healthcare domain-specific ML and NLP models to extract and interpret medical record data. These models were trained and evaluated on golden data sets curated by expert clinicians. However, this approach was slow and burdensome.

> “We deployed fine-tuned state-of-the-art healthcare models, which we then further optimized. You spend a lot of time, and you have to do everything use case by use case. You have to build, train, and validate a separate model for every piece of information.”

Jonathan Hirsch, Chief Strategy Officer at Paradigm

Because traditional models only worked so well, clinicians are required to manually review model output to verify that quality standards have been met.

## Using GPT-4 to evaluate clinical trial data sets

Paradigm believed that LLMs, with their ability to summarize unstructured text, could be a great fit for their use case and replace the approach of building one-off ML models. They explored two potential paths: integrating with a custom LLM trained on medical use cases, or integrating with GPT‑4 through OpenAI’s API. 

Paradigm believed they would need a specialized medical model to get good results. They were “shocked” to find that GPT‑4 outperformed a team of highly trained human experts on complex data evaluation tasks. 

Ultimately, they chose OpenAI for several reasons: 

* **Accuracy:** Paradigm ran rigorous evaluations on their expert-curated golden data sets. GPT‑4 was at least 10% more accurate than state-of-the-art ML models on a blended precision/recall metric. In some cases, they saw “unbelievable” improvements. “The accuracy of OpenAI was better than our existing deployment and optimization of industry best-practice expert-trained models, and it was sometimes better than our trained clinicians,” Hirsch said. “The more complex the information, and the more different places that information sat, the better GPT‑4 was.”
* **Ease of use:** “From a product standpoint, everything was just easy. The API was easy to use, and it was easy to integrate into our stack.” The team also appreciated that OpenAI’s support included high-quality API documentation: “Compared to working with other organizations, we can be more self-sufficient with OpenAI.”
* **Multimodal entry and long context windows:** Both features were key for medical record data.
* **Security and regulatory compliance:** “What really sold us on working with OpenAI was your serious approach to supporting regulatory compliance, including supporting our need to comply with HIPAA. Since we serve healthcare providers and their patients, regulatory compliance is a non-negotiable requirement for us.”

## GPT-4 improves product speed, data quality, and costs of operation

* **Extracting new data elements in days, not months:** GPT‑4 has upended how Paradigm thinks about their core infrastructure, completely replacing the process of building ML models one by one for individual data components. This has greatly accelerated Paradigm’s roadmap, allowing them to rapidly expand to new provider partners and types of trials.
* **90% reduction in expert clinician time needed for model validation:** Paradigm estimates that they only need 1/10th of the data to evaluate GPT‑4’s output, compared to previous specialized ML models.
* **10% increase in accuracy:** With more accurate data than before—even outperforming human experts in many cases—GPT‑4 has reduced the need for expert human intervention in model results. Doctors and nurses at Paradigm and their healthcare provider partners are able to spend more time on patient care, rather than reading documents.
* **More equitable access to trials:** While they are still proving this out, Paradigm believes that GPT‑4 can more accurately screen underserved patients for trials. These patients tend to have less structured data in their medical record and more unstructured data (e.g., notes), which GPT‑4 excels at extracting and interpreting.

## Evaluating hundreds of patients per minute

Looking forward, Paradigm is excited about how they can leverage GPT‑4’s natural language understanding to further reduce the burden for clinicians. Rather than needing to write code to analyze data, clinical teams could have a dialog with ChatGPT about a patient’s data, to understand their eligibility for trials, missing information, and next steps.

Paradigm is excited about how they can continue to increase the patient screening rate. With GPT‑4, their platform can potentially evaluate **hundreds of patients per minute**. Compare this to a typical nurse research coordinator, who can manually review around 50 patients *per day*. These efficiency gains can lead to a world where patients have far better access to clinical trials, physicians and nurses can spend more time on patient care and less time on documentation, and new life-saving therapies are brought to market sooner.

## Interested in learning more about ChatGPT for business?

[Talk with our team](/contact-sales/)

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
