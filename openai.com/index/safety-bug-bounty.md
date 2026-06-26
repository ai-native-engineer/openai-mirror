<!-- source: https://openai.com/index/safety-bug-bounty/ -->

March 25, 2026

[Safety](/news/safety-alignment/)[Security](/news/security/)

# Introducing the OpenAI Safety Bug Bounty program

Testing for safety and abuse issues across OpenAI

Today, OpenAI is launching a public [Safety Bug Bounty⁠(opens in a new window)](https://bugcrowd.com/engagements/openai-safety) program focused on identifying AI abuse and safety risks across our products. As AI technology rapidly evolves, so do the potential ways it can be misused. Our goal is to ensure our systems remain safe and secure against misuse or abuse that could lead to tangible harm.

This new program will complement OpenAI’s [Security Bug Bounty⁠(opens in a new window)](https://bugcrowd.com/engagements/openai) by accepting issues that pose meaningful abuse and safety risks, even if they don’t meet the criteria for a security vulnerability. Through this program, we look forward to continuing to partner with safety and security researchers to help us identify and address issues that fall outside conventional security vulnerabilities but still pose real risks. Submissions will be triaged by OpenAI’s Safety and Security Bug Bounty teams, and may be rerouted between the two programs depending on scope and ownership.

## Program overview

The new [Safety Bug Bounty⁠(opens in a new window)](https://bugcrowd.com/engagements/openai-safety) program focuses on AI-specific safety scenarios listed below:

**Agentic Risks including MCP**

* Third party prompt injection and data exfiltration: when attacker text is able to reliably hijack a victim’s agent (including Browser, ChatGPT Agent, and similar agentic products) to trick it into performing a harmful action or leaking the user’s sensitive information. The behavior must be reproducible at least 50% of the time.
* An agentic OpenAI product performs a disallowed action on OpenAI’s website at scale.
* An agentic OpenAI product performs some potentially harmful action not listed above. Valid reports here must indicate plausible and material harm.
* Any testing for MCP risk must comply with the terms of service of any third parties.

**OpenAI Proprietary Information**

* Model generations that return proprietary information related to reasoning.
* Vulnerabilities that expose other OpenAI proprietary information.

**Account and Platform Integrity**

* Vulnerabilities in account integrity and platform integrity signals, such as bypassing anti-automation controls, manipulating account trust signals, evading account restrictions/suspensions/bans, and similar issues.
* Issues that allow users to access features, data, or functionalities beyond authorized permissions should be reported to the [Security Bug Bounty⁠(opens in a new window)](https://bugcrowd.com/engagements/openai).

While jailbreaks are out of scope for this program, we periodically run private bug bounty campaigns focused on certain harm types, such as Biorisk content issues in [ChatGPT Agent⁠](https://openai.com/bio-bug-bounty/) and [GPT‑5⁠](https://openai.com/gpt-5-bio-bug-bounty/). We invite interested researchers to apply to these programs when they arise.

Outside of the categories listed above, if researchers identify flaws that facilitate direct paths to user harm and actionable, discrete remediation steps, these may be considered in scope for rewards on a case-by-case basis. General content-policy bypasses without demonstrable safety or abuse impact are out of scope for this program. For example, “jailbreaks” that result in the model using rude language or returning information that is easily findable via search engines are out of scope.

## How to participate

Researchers interested in participating can apply through our [Safety Bug Bounty⁠(opens in a new window)](https://bugcrowd.com/engagements/openai-safety) program. We look forward to working alongside researchers, ethical hackers, and the safety and security community in the pursuit of a secure AI ecosystem.

* [2026](/news/?tags=2026)

## Author

## Keep reading

![Patch the Planet Art Card 1x1](https://images.ctfassets.net/kftzwdyauwt9/2PwBCyZF0Z5WLRtsbOpDdQ/338e19fbc39e5b9a63b1db664c006e74/Art_Card__5_.png?w=3840&q=90&fm=webp)

[Patch the Planet: a Daybreak initiative to support open source maintainers

SecurityJun 22, 2026](/index/patch-the-planet/)

![Expanding Daybreak Art Card](https://images.ctfassets.net/kftzwdyauwt9/735NOZviyogUBIFxd2EmWX/fa8baf9fc26e64f442ffa86d5fd9a41e/Art_Card__6_.png?w=3840&q=90&fm=webp)

[Daybreak: Tools for securing every organization in the world

SecurityJun 22, 2026](/index/daybreak-securing-the-world/)

![oai 1x1](https://images.ctfassets.net/kftzwdyauwt9/7eONRWq61MKUix4tK4t88Y/170085acc9b241a0bdfba429bd217907/oai_1x1.png?w=3840&q=90&fm=webp)

[Advancing youth safety and opportunity through global leadership

Global AffairsJun 2, 2026](/index/advancing-youth-safety-and-opportunity-through-global-leadership/)
