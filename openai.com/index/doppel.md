<!-- source: https://openai.com/index/doppel/ -->

October 28, 2025

# Doppel’s AI defense system stops attacks before they spread

With GPT‑5 and reinforcement fine-tuning (RFT), Doppel cut analyst workloads by 80% and now mitigates threats in minutes instead of hours.

[Contact sales](/contact-sales/)

![Doppel logo in white centered on a textured dark metallic background with curved lines and rivets.](https://images.ctfassets.net/kftzwdyauwt9/330fkcLd90UV5uEfkuOpYW/53d9ce732131f0b3706dcd26447b043e/oai_Doppel_16x9__1_.jpg?w=3840&q=90&fm=webp)

Company size: Startup

Region: North America

Industry: Technology

Products: API

Results

80%

reduced analyst workflows

Results

3x

threat handling capacity

A single impersonation site can launch, target thousands of users, and vanish in under an hour. That’s more than enough time for an attacker to do real damage. And with generative tools, they can spin up hundreds more just like it.

Doppel was built to defend organizations from deepfakes and online impersonations, but quickly realized AI meant threats could scale infinitely. Attackers no longer needed to handcraft scams; they could generate endless variants of phishing kits, spoofed domains, and impersonation accounts in seconds.

> “Damage from phishing attacks can happen within minutes as they spread across social media and messaging channels. The ability to generate infinite persuasion at almost no cost changed everything.”

—Rahul Madduluri, Co-founder and CTO, Doppel

## Inside the rollout

To stay ahead, Doppel developed a new kind of social engineering defense system built on OpenAI GPT‑5 and o4-mini models. Doppel’s platform detects, classifies, and takes down threats autonomously, cutting analyst workloads by 80%, triples threat-handling capacity, and reduces response times from hours to minutes.

## Staying ahead of infinitely faster threats

Traditional digital risk protection relied on humans to manually review impersonation sites, phishing domains, and social media profiles and posts. Doppel saw that model breaking down as attackers began to automate, launching threats faster, and across more surface areas, than humans could evaluate them.

> “Our system processes a constant flood of signals to identify the real threats amongst the noise. Once a threat is detected, there is a very narrow window to act before the damage is done. Using AI to automate decision-making is one of the greatest unlocks for the company, allowing us to combat attacks at internet scale and speed.”

—Rahul Madduluri, Co-founder and CTO, Doppel

That speed is critical for Doppel’s customers, organizations that can’t afford to wait hours to confirm a threat. Doppel’s system classifies most threats automatically, using OpenAI models for reasoning and a structured feedback loop known as reinforcement fine-tuning (RFT) to improve the model over time. In RFT, human feedback is used as graded examples, helping models learn to make consistent, explainable decisions on their own.

## Orchestrating LLM-driven threat detection

Doppel’s LLM-driven pipeline sits at the center of its detection stack. After signals are sourced and filtered, the system performs a series of targeted reasoning tasks: reasoning through potential threats, confirming intent, and driving classification decisions. Each stage is designed to balance speed, accuracy, and consistency, while keeping analysts focused on the edge cases that need human judgment.

![A flowchart shows a pipeline for threat detection using LLMs, moving from sourcing and filtering, through feature extraction and classification, to final verification and takedown systems. Models like GPT-5 and o4-mini are used at key stages.](https://images.ctfassets.net/kftzwdyauwt9/6LD8BT5EyvdK3bMlNekE4I/8dfc348b006d07f69841e6383e4730fa/Doppel_Agent_Flow.jpg?w=3840&q=90&fm=webp)

Here’s how it works:

* **Signal filtering and feature extraction:** Doppel’s systems ingest millions of domains, URLs, and accounts daily. A combination of heuristics and OpenAI o4-mini filters out noise and extracts structured features to guide downstream model evaluations.
* **Parallel threat confirmation:** Each signal is passed through multiple GPT‑5 prompts purpose-built for different types of threat analysis. These prompts assess factors like impersonation risk, brand misuse, or social engineering patterns.
* **Threat classification:** The RFT version of o4-mini synthesizes the earlier confirmations to assign a structured label—malicious, benign, or ambiguous—with production-grade consistency.
* **Final verification:** A second GPT‑5 pass validates the model’s decision and generates a natural-language justification. If confidence exceeds threshold, the system auto-initiates enforcement.
* **Human review:** Low-confidence or conflicting results are routed to human analysts. Their decisions are logged and fed back into the RFT loop to continuously improve model consistency.

## Training models through reinforcement fine-tuning (RFT)

Doppel had already seen meaningful gains from its original LLM-enhanced detection pipeline, but when it came to cases where the same threat might be judged differently depending on the analyst, consistency became the limiting factor.

> “One real benefit that came out of RFT is you’re making that model’s decisions more consistent.”

—Kiran Arimilli, Software Engineer, Doppel

To build that consistency, Doppel applied RFT using its own analyst data as the feedback source. Each decision to classify a domain as malicious, benign, or unclear became a graded example. Those labeled examples trained the model to replicate expert judgment, even on ambiguous edge cases.

![A circular diagram shows the Doppel threat classification workflow: production LLMs make decisions → human reviewers provide corrections → model training updates models → deployment sends updated models to production.](https://images.ctfassets.net/kftzwdyauwt9/3TJNHDNkcRBPpalJ70s7NW/349ae2d0169bf33be35c4095592d3e79/DoppelThreatWorkflow.jpg?w=3840&q=90&fm=webp)

Working closely with OpenAI’s applied engineering team, Doppel designed grader functions that evaluated not only accuracy but explanatory quality, rewarding models that reasoned clearly, not just correctly. By turning analyst feedback into structured training data, Doppel helped show how RFT could make automated detection more consistent and reliable.

## Operationalizing trust through transparency

Hyperparameter tuning and iterative evals brought the model closer to human-level consistency. But for Doppel, completing the final mile of automation also meant making decisions immediately understandable.

Each automated takedown now includes an AI-generated justification explaining why a threat was removed, giving customers immediate insight into why action was taken—something that once required analyst intervention.

![A dashboard view shows a takedown alert for the domain “d0ppel.click,” flagged for impersonating Doppel. The summary cites phishing and credential theft, with a timeline on the right showing status updates from creation to resolution on October 10, 2025.](https://images.ctfassets.net/kftzwdyauwt9/2Jlz6U6Tn8QmPrPxKg2Ncf/59a7d0a4cb6075b7c997d2932c4e6fde/Doppel_UI.png?w=3840&q=90&fm=webp)

That visibility enhances trust, which is a critical factor for Doppel’s users. Seeing not just what action was taken, but why, gives teams the confidence to respond quickly and the context to explain those decisions internally or to stakeholders.

## Results at a glance

* Cut analyst workloads by 80%
* Reduced threat response times from hours to minutes
* Tripled threat-handling capacity
* Most threats classified automatically

## What’s next

Having reached near-complete automation for phishing and impersonation domains, Doppel is now applying the same model-driven framework to other high-variance channels.

“Domains are probably the hardest channel we handle,” said Madduluri. “The signals are messy, content changes constantly, and threats evolve fast across several surfaces at once. If we can automate that end to end, we can do it for anything: social media, paid ads, you name it.”

The next milestones include scaling their RFT dataset by an order of magnitude, experimenting with new grading strategies, and using GPT‑5 for upstream feature extraction. These changes will allow Doppel to consolidate pipeline stages and reason over more complex threat indicators earlier in the process.

With each iteration, Doppel is building toward a system that defends what’s real across every surface where trust is under attack.

## OpenAI <3 startups

[Join the community](/leads/startup/)[Start building(opens in a new window)](/startups)

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
