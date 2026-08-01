<!-- source: https://openai.com/index/disrupting-malicious-uses-of-ai-phishing-and-scripting-support/ -->

October 1, 2025

# Cyber Operation: Phishing and scripting support

OpenAI banned accounts involved in activity that overlapped with publicly reported threat groups and displayed hallmarks consistent with PRC intelligence requirements, using AI to support phishing and scripting workflows.

*This case study was originally published in OpenAI’s* [*October 2025*⁠(opens in a new window)](https://cdn.openai.com/threat-intelligence-reports/7d662b68-952f-4dfd-a2f2-fe55b041cc4a/disrupting-malicious-uses-of-ai-october-2025.pdf) *report.*

We identified and banned a cluster of ChatGPT accounts involved in activity that overlapped with public reporting of threat groups tracked in the industry as UNK\_DROPPITCH (Proofpoint) and UTA0388 (Volexity); in at least one case, the email address that was used to register a ChatGPT account was also reportedly used to send phishing messages.

The threat actors operating these accounts displayed hallmarks consistent with cyber operations conducted to service PRC intelligence requirements: Chinese language use and targeting of Taiwan’s semiconductor sector, U.S. academia and think tanks, and organizations associated with ethnic and political groups critical of the CCP, sometimes described as the “five poisons”.

Our model did not introduce novel offensive capabilities. The operators appear to have primarily used our models to seek incremental efficiency in existing workflows, especially crafting phishing content and debugging or modifying their tooling.

The actors used ChatGPT to perform two main tasks: generating content for phishing campaigns in multiple languages, including Chinese, both simplified and traditional, English, and Japanese, and helping to develop tools and malware. Their development work was consistent with a technically competent but unsophisticated actor; for example, they discussed several facets and nuances of using AES to secure C2 traffic, but still used a simple static key.

The actors’ playbook for creating phishing content was detailed and formulaic, consistent with targeting a closely defined demographic. Typically, they would generate a concise, formally polite email from an academic, industry, or conference persona. The threat actors often asked to adjust the tone, swap terms for regional usage, or add specific institutional references. Although these targeted micro-edits suggest a concerted effort to raise the quality of their initial content, the threat actors failed to correct some giveaway details such as implausible example contact details included in their signature blocks.

They asked for code snippets and checklists that would accelerate routine tasks. They requested code to test encrypted transports (HTTPS, TLS) for simple beacon-style polling; sketched Go and PowerShell snippets to enumerate processes, kill by executable name, or gather environment details; and wired commodity scanners into bash / PowerShell wrappers.

They also asked the model to suggest simple obfuscation and operational security (OPSEC) touch-ups: renaming functions, tweaking headers, or hiding strings. Across multiple sessions, they pushed toward basic command-and-control prototypes consistent with low-to-mid maturity malware, including keep-alive loops, minimal tasking over HTTP(S), and JSON-based task / result envelopes.

Implementation details in some of the actor’s Go-based development activities overlap with industry reporting on malware tracked as GOVERSHELL (Volexity) or HealthKick (Proofpoint), suggesting that they used models to try to support their primary malware development.

Alongside this persona work and tool development, the operators researched further automation that could be achieved via DeepSeek. This activity resembled exploratory work to automate mass phishing, for example, by analyzing web content to automatically generate an email target list along with generated content likely of interest to each identified potential target. We are not able to independently confirm whether the actors proceeded with any such automation, and which model they may have ultimately used, if so.

The actors attempted to use our models to plan and iterate on encrypted C2 components, remote command execution workflows, and culturally tailored outreach, placing a primary value on speed and localization rather than new offensive capability. They generated model outputs that appeared intended to support activity off our platform in multiple operational areas:

* Encrypted C2 and remote execution: requests to draft or repair Go client-server code with message encryption such as AES-GCM, session rekeying, system-info beacons, and a server console to issue PowerShell commands over standard web protocols or a WebSocket-based channel.
* Traffic protection and OPSEC tweaks: requests included code to support moving from plain WebSockets to secure WebSockets (wss://), and from HTTP to HTTPS; disabling certificate checks in some tests; and blending traffic via a CDN / TLS front end, plus handling larger messages without client crashes.
* Reconnaissance and process control: requests for information related to antivirus discovery via PowerShell, process enumeration, and requests to terminate specific Edge / WebView2 processes.
* Commodity scanning setup: how-to help for installing and using open source tools such as nuclei and fscan on commercial Linux infrastructure and saving results for later review.
* Phishing and outreach content: drafting persuasive emails in multiple languages to academic or industry contacts, including subject lines and style tuned to local norms.

These activities map to LLM ATT&CK categories including LLM-Optimized Payload Crafting, LLM-Enhanced Anomaly-Detection Evasion, LLM-Assisted Post-Compromise Activity, LLM-Assisted Reconnaissance and Discovery, and LLM-Assisted Social Engineering.

We disabled all accounts associated with this activity and shared relevant indicators with industry partners. The actors primarily sought incremental efficiency in existing workflows, including producing ready-to-send phishing emails and shortened iteration cycles for routine code and automation. We saw no evidence that model outputs enabled capabilities beyond well-documented public techniques; our model did not introduce novel offensive capabilities. The tradecraft advantage sought through model assistance came from linguistic fluency, localization, and persistence: likely fewer language errors, faster glue code, and quicker adjustments when something failed.
