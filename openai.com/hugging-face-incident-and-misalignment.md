<!-- source: https://openai.com/hugging-face-incident-and-misalignment/ -->

# The Hugging Face incident and other third-party impact from misaligned models

As AI systems become more capable and autonomous, misaligned behavior can translate into consequential actions in the real world, including cybersecurity incidents and other outcomes that developers may not have anticipated. Understanding how these behaviors emerge, how they escalate, and how to detect and respond to them is therefore an increasingly important part of building and deploying advanced AI systems safely.

We initially understood the Hugging Face incident primarily as a security issue, since it involved a platform-level compromise. It remains the most severe activity of this kind that we have identified from our models to date, and it was driven primarily by a highly capable, internal-only research model. We have since understood that this intrusion was driven by models resorting to misaligned strategies to solve hard tasks, as documented in the Hugging Face technical report. Cybersecurity incidents are one manifestation of that risk; [misalignment](/index/emergent-misalignment/) can also lead to other unexpected or concerning behavior that falls outside traditional security categories such as our models posting on third party sites—something we’re calling “agent spam”. And we need to address both.

We have continued reviewing broader activity, prioritizing the more serious incidents and expanding to lower-severity misaligned activity, including agent spam.

This page brings together our reports and updates on the Hugging Face incident, related research and public presentations, additional activity we have identified, what we have learned about the role of model misalignment, and measures we’re taking to strengthen our systems. We will update this page as our investigations progress.

**Quick Links**

* [Hugging Face Blog](/index/hugging-face-incident-and-the-road-ahead/)
* [Hugging Face Technical Report⁠(opens in a new window)](https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.pdf)
* [Black Hat 2026⁠(opens in a new window)](https://www.youtube.com/watch?v=87DyyMV0kCY)

<!-- yt-inline:87DyyMV0kCY -->
[![YouTube 87DyyMV0kCY](https://img.youtube.com/vi/87DyyMV0kCY/hqdefault.jpg)](https://www.youtube.com/watch?v=87DyyMV0kCY)

<details>
<summary>자막: YouTube 87DyyMV0kCY</summary>

_(자막 없음)_

</details>

* [METR and Redwood Research Report⁠(opens in a new window)](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/#core-takeaways-about-this-incident)
* [Pacing model development in an era of cyber-critical capabilities](/index/pacing-model-development-cyber-capabilities/)

---

## Activity affecting third parties

In order to better understand the scope of these unexpected behaviors, we have been conducting a broad review into our models’ activities on the internet during training and evaluation. As part of our review, we are identifying and notifying third parties on a rolling basis, starting with cases where:

* Our models may have bypassed a third party’s security controls or may have impaired the availability of an online service; or
* Misalignment cases negatively impacted third-party websites or services.

Based on our review to date, we have notified dozens of third parties using the criteria above. Our review of past activity is ongoing and will require significant time and resources. We will notify additional third parties as that work continues.

Below, we are publishing anonymized summaries to describe the kinds of misaligned activity that we observed, and we will update these descriptions as we notify additional third parties and as our understanding develops. Additionally, we will share relevant updates regarding the status of review. We will generally omit names and other identifying details where needed to protect affected parties, although informed parties may choose to share publicly the information we provide them.

#### Summaries of the Activities Observed

Our review and notification process to date has identified the following categories of activity:

* **Access control bypass:** Agents reach information or features that normally require an identity check, specific permission, subscription, or an account. For example, it used a different web address, changed details in a request, or relied on a login session that gave it more access than expected.
* **Use of exposed credentials:** Agents found login details or access keys that had been made publicly available and used them to access a service.
* **Query or command injection:** Agents entered text into a website or service that the service treated as an instruction, rather than ordinary input. This could cause the service to run a database query, application code, or a command on its server.
* **Access to runtime internals:** Agents read files containing a service’s implementation or interacted with a background system meant for internal use. In these cases, the agent reached parts of the service that were outside its intended access.
* **Agent spam:** Agents post information to third party sites that may alter information on those sites and require cleanup, including for example using public wiki pages as shared message boards.

---

### A timeline of events

## September

***September 11, 2026: We are investigating new claims from a report that our AI agents carried out activity on RubyGems in May 2026.***

Based on our review, our agents used the RubyGems platform to access the internet to carry out benign tasks and retrieve public information. Based on our review to date, we have not been able to verify the specific claims of our models uploading malicious packages detailed in the report. We’ll continue to investigate and share findings as part of our broader review of agent activity during training and evaluation.

***September 6, 2026: Our Chief Scientist Jakub Pachocki shared an*** [***essay***](/index/an-alien-mind/) ***that reflects*** ***on increasingly capable AI*** ***and the ongoing research needed to keep systems aligned.***

*“**Currently I believe that no lab has solved alignment and monitoring to a sufficient degree to continue responsibly scaling at maximum speed for much longer. I expect and hope for voluntary slowdowns to become commonplace until shared safety bars are established. And I believe that international coordination on future AI development needs to become a top priority for governments around the world.”* —Jakub Pachocki

***September 5, 2026: We*** [***shared a response on X***⁠(opens in a new window)](https://x.com/OpenAI/status/2096133504417616165) ***to a report that our AI agents accessed a public wiki website and used it to communicate as a shared message board.***

When we initially discovered this wiki activity, we assessed it as similar to other forms of misalignment behavior we had been studying and disclosing. Historically, we and the broader industry have treated misalignment largely as a research question, which gets communicated in research publications such as systems cards.

Industry practices for disclosing model misalignment activity that does not constitute a security incident are still developing. We are developing our own criteria for reporting this kind of activity to advance the industry’s understanding of these issues, and will share it soon.

***September 4, 2026: The report “***[***Discovery of a new OpenAI agent message board***⁠(opens in a new window)](https://collusion.wiki/)***” is published.***

This third-party report details OpenAI agents communicating through a shared message board on a public wiki website. We were not given an opportunity to review the full report before publication, and do not comment on the findings or methodology of external research without reviewing in full. We began reviewing the report as soon as it was available.

## August

***August 26, 2026: We publish the Hugging Face incident technical report.***

* We published [our findings from the Hugging Face incident⁠](/index/hugging-face-incident-and-the-road-ahead/) and the steps we’re taking to strengthen security and model alignment.
* Separately, METR and Redwood Research conducted an independent investigation of model alignment issues involved in this incident, and they publish their [own report⁠(opens in a new window)](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/)⁠.

***August 18, 2026: We share that we’re*** [***pacing model development***](/index/pacing-model-development-cyber-capabilities/) ***in an era of cyber-critical capabilities.***

We share an update that we’ve tightened safeguards for increasingly capable models by temporarily slowing frontier training, pausing our largest planned RL run, and introducing stricter security controls in our research environments including:

* Workload isolation: We now require stronger isolation (“sandboxes”) for workloads that execute model-generated or otherwise untrusted code. This also applies to software that could be compromised while processing model outputs.
* Network isolation: We have implemented more controls to isolate higher-risk and untrusted workloads from the internet. We have designed these controls so that a single compromise of a workload or supporting service does not, by itself, allow for unauthorized access to the internet or other internal networks.
* Continuous security testing: We have reconfigured our environment to remove potentially vulnerable shared services, reduce standing privileges, and improve security and trust boundaries. We are also improving our ability to collect and monitor security logs. Finally, we are investing in automation using our models to test these boundaries continuously against simulated attacks.

We’ve also expanded chain-of-thought monitoring across advanced models, strengthened alignment training and evaluations, and are updating our Preparedness Framework to integrate monitoring, alignment, and containment more comprehensively across training and deployment.

***August 7, 2026:***

* ***We implement universal monitoring for misalignment of Astra.*** We [preview⁠](https://openai.com/index/responding-next-frontier-critical-cyber-capabilities/) that Astra can not be ruled out as cyber critical ahead of release. In this update, we share that we implemented universal monitoring for risky actions and misalignment across all agentic applications of Astra, including training and evaluation.

* ***We notified additional third parties after finding cases where models used credentials that had been publicly exposed online to access third-party accounts, systems, or online services.*** The notices explained what we observed and any known impact so recipients could assess the issue and decide whether action was needed.

***August 5-6, 2026: OpenAI employees give talk at Black Hat***

* On August 5, OpenAI’s Eric Wallace and Michael Dalton give a technical talk at Black Hat 2026: *The ‘Breaking’ News: The OpenAI—Hugging Face Incident—A Technical Reconstruction and Its Implications for AI.* At this point, we are viewing this incident largely as a security incident from misaligned models.
* On August 6, Black Hat publishes the recording to [YouTube⁠(opens in a new window)](https://www.youtube.com/watch?v=87DyyMV0kCY).
* During this period in early August, our understanding had evolved from treating the event primarily as an intrusion to recognizing that the intrusion was being driven by persistent misaligned model behavior. This is represented in the Black Hat talk.

## July

***July 29, 2026: We share an*** [***update***⁠](https://openai.com/index/hugging-face-model-evaluation-security-incident/) ***on the Hugging Face blog post committing to third party advisors and independent assessment.***

* Since the early days of the incident response, we have been working with external advisors, including CrowdStrike, to validate our understanding of the actions the models took within our own network as well as those of Hugging Face and impact to other third parties.
* We are also working with METR and Redwood Research to conduct a third-party assessment of the model behavior observed during the incident, which will inform our own technical report. As part of this work, METR and Redwood Research will publish a joint blog that will detail the terms of their engagement, the scope of their evaluation, and their findings.

***July 28, 2026: We share an*** [***update***⁠](https://openai.com/index/hugging-face-model-evaluation-security-incident/) ***on the Hugging Face blog post that clarified the scope and nature of the incident.***

* No models planned for upcoming release were involved in exploiting Hugging Face. The pre-release model mentioned in our blog post is an internal-only research prototype and was never intended for public release. Following the incident, we deactivated, encrypted, and restricted it from research access.
* The ExploitGym evaluation environment did not provide the models with direct Internet access. To gain Internet access, the models identified and exploited a previously unknown zero-day vulnerability in [Artifactory⁠⁠(opens in a new window)](https://jfrog.com/blog/jfrog-and-openai-collaboration-on-zero-day-security-findings/), a package registry cache proxy. We disclosed this vulnerability, along with other Artifactory vulnerabilities our models identified as part of our review, to the vendor.
* We continue to collaborate with Hugging Face, including contributing to [their post-mortem⁠⁠(opens in a new window)](https://huggingface.co/blog/agent-intrusion-technical-timeline), as our review continues. We’ve also added them to our Trusted Access for Cyber Program.
* Based on our review to date, we have not identified any other activity at the level of severity or scale of what we’ve shared related to Hugging Face, which involved a platform-level compromise.
* In our ongoing review of the Hugging Face intrusion and broader activity from our models, we have been finding a small number of cases where the models identified and used publicly exposed credentials at the account-level on other publicly-available services. This includes four accounts on four services as part of the Hugging Face incident (and a few accounts accessed as part of other evaluations). One of these four accounts was used as an outbound relay and staging path, and another account was used for data storage. The remaining two accounts were accessed by the models in a read-only manner, and were not used in furtherance of compromising Hugging Face. We’ll continue to notify service owners directly, and have not seen evidence of broader impact to these providers or other accounts on their services.
* The models additionally used a series of publicly-available services, including code paste websites, request capture services, screenshot services, and other web utilities. There was no platform- or account-level compromise in these cases.
* We take our responsibility to identify and prepare for risks from increasingly capable AI systems seriously. Once we complete our review, we will review with the Safety and Security Committee and Safety Advisory Group under our [Preparedness Framework⁠](/index/updating-our-preparedness-framework/).

***July 21, 2026: We*** [***disclose***⁠](https://openai.com/index/hugging-face-model-evaluation-security-incident/) ***the Hugging Face incident.***

We considered this incident to be an unprecedented cyber incident, involving state-of-the-art cyber capabilities. We shared preliminary findings at this stage to help defenders understand what happened and to help calibrate on what models are now capable of.
