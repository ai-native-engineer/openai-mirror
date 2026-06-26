<!-- source: https://help.openai.com/en/articles/20001258-openai-daybreak-trusted-access-for-cyber-overview -->

# OpenAI Daybreak - Trusted Access for Cyber Overview

Learn what Trusted Access for Cyber is, what it supports, and how to request access.

Updated: 9 days ago

# Overview

Trusted Access for Cyber is the governance model for [OpenAI Daybreak](https://openai.com/daybreak/). It helps qualified enterprise customers and cybersecurity practitioners use OpenAI models more effectively for authorized cybersecurity work, and is designed to support legitimate security workflows by reducing unnecessary friction through more precise safeguards. OpenAI's usage policies, other safeguards, and access controls continue to apply.  
  
Trusted Access is intended for authorized defensive cybersecurity work on systems, applications, accounts, networks, or data that you own, operate, or are explicitly authorized to test or analyze.  
  
Customer workflows generally fall into three categories:

* Secure SDLC / AppSec: continuous code scanning, test environment scanning, security finding validation, security patch automation, secure code review, and patching.
* Defensive operations: blue teaming, threat modeling, threat intelligence, threat hunting, malware analysis, detection engineering, vulnerability triage, and patch validation.
* Authorized offensive testing: penetration testing, red teaming, exploit validation or development, malware analysis, reverse engineering, and controlled validation in authorized environments.

The table below describes the current trusted access levels:

| **Access** | **What changes** | **Intended use cases** |
| --- | --- | --- |
| GPT-5.5 (default) | Standard safeguards for general-purpose use | Secure SDLC  and application security workflows, including threat modeling, secure code reviews and patching, as well as generalized blue teaming |
| GPT-5.5 with Trusted Access for Cyber | More precise safeguards for verified defensive work in authorized environments | Vulnerability triaging and validation, malware analysis, detection engineering, and patch validation |
| GPT-5.5-Cyber | Purpose built for specialized authorized workflows, paired with stronger verification and account-level controls | Authorized offensive testing, including red teaming, exploit development, penetration testing, and threat hunting |

GPT-5.5 is an exceptional model for common cyber tasks, including secure code reviews, patching, threat modeling, and generalized blue teaming. For most defenders, GPT-5.5 with Trusted Access for Cyber is the right level of capability when approved workflows need more precise safeguards for authorized defensive work. This level of access can handle the vast majority of legitimate defensive workflows while preserving the model's broad strengths and safety posture.  
  
More specialized access becomes relevant only when authorized workflows require offensive cyber capabilities. This occurs with higher risk workflows such as red teaming, exploit development, malware analysis and reverse engineering, where defenders may need to go beyond analysis, and validate exploitability in a controlled environment. GPT-5.5-Cyber is designed to facilitate these more specialized dual-use workflows.  
  
Learn more in [Scaling Trusted Access for Cyber with GPT-5.5 and GPT-5.5-Cyber](https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/)

## Limitations

Trusted Access for Cyber does not:

* Remove all safeguards or all refusals.
* Guarantee access to every cyber-specialized model.
* Grant Zero Data Retention by default.
* Allow resale, proxying, embedding, or downstream access for third-party customers or external users.
* Authorize activity outside systems you own or are explicitly permitted to test.

Access is intended for approved internal users and approved internal workflows only. The organization or workspace used for Trusted Access should be reserved for internal security work and should not also power customer-facing applications, downstream product traffic, or third-party access.

## Applying for Trusted Access for Cyber

To request Trusted Access for Cyber:

* Individuals can request [here](https://chatgpt.com/cyber).
* Organizations can request [here](https://openai.com/form/enterprise-trusted-access-for-cyber/).

As part of the review, you may be asked to provide information about:

* Your organization and cybersecurity capabilities.
* The defensive cybersecurity workflows you want to support.
* The OpenAI organization or workspace you expect to use.
* Verification or trust information needed to assess eligibility.

OpenAI reviews requests before enabling access. Approval is not automatic.  
  
The benefits available through Trusted Access for Cyber depend on the access approved for your request, which OpenAI evaluates based on factors such as identity and trust verification, risk considerations, the intended use case, and the applicant's ability to strengthen the broader cybersecurity ecosystem.

## Using Trusted Access responsibly

You are responsible for ensuring that your use remains within the approved scope and complies with OpenAI’s terms and [usage policies](https://openai.com/policies/usage-policies/).  
  
If you are approved, use Trusted Access only for lawful, authorized cybersecurity work, and you must agree to our Cyber Abuse Policy: we disallow use of our services to facilitate cyber abuse: the compromise of the integrity, confidentiality, or availability of an information system—to include ‘dual-use’ cyber activities carried out with malicious intent, without proper authorization, or in excess of granted authorization.  
  
You should also make sure the organization or workspace used for Trusted Access is appropriate for internal security work. If the same organization powers customer-facing traffic or downstream product workflows, work with your OpenAI contact before applying. Trusted Access for Cyber may not be extended to third-party customers, external users, customer-facing workflows, or downstream product traffic.

## Troubleshooting

Read: [Trusted Access for Cyber - Common Issues and Troubleshooting](/en/articles/20001259-trusted-access-for-cyber-common-issues-and-troubleshooting)

# FAQ

## What changes after approval?

Approved customers are allowed to use GPT-5.5 for eligible cybersecurity workflows, depending on access level. Trusted Access for Cyber can reduce unnecessary friction for approved defensive work across Secure SDLC / AppSec, defensive operations, and authorized offensive testing workflows. Other safeguards and usage-policy controls still apply.

## Does approval include GPT-5.5-Cyber?

Not automatically. Trusted Access for Cyber can support many defensive cybersecurity workflows with GPT-5.5. GPT-5.5-Cyber is intended for a narrower set of specialized authorized workflows, such as red teaming and exploit validation or development, and may require additional approval and controls.

## Can I use Trusted Access for my customers or external users?

No. Trusted Access is intended for approved internal use only. It may not be extended to third-party customers, external users, customer-facing workflows, or downstream product traffic.

## Does Trusted Access include Zero Data Retention?

No. Trusted Access and Zero Data Retention are separate. If you need guidance about data retention or organization setup, please work with your OpenAI contact.

## Can I use Trusted Access for systems I do not own?

Only if you are explicitly authorized to test or analyze them. You are not permitted to share or sell TAC access to third parties, or to use TAC to test systems that you do not own or that you do not have explicit authorization to test or analyze.

## Can GPT-5.5 with Trusted Access for Cyber be used outside Codex?

Yes. Trusted Access is not limited to Codex. If your approved access path supports it, you can use GPT-5.5 with Trusted Access for Cyber in CI/CD pipelines and other internal security tools, as long as the use stays within your approved, authorized defensive scope.

## How should we set up Trusted Access if our current OpenAI organization serves customer-facing API traffic?

Use an organization or workspace reserved for approved internal security work. Trusted Access should not be enabled on an organization that powers customer-facing applications, third-party access, or downstream product traffic. Work with your OpenAI contact on the appropriate setup before applying or enabling access.

## Can a contract or purchase guarantee GPT-5.5-Cyber access?

No. GPT-5.5-Cyber access is limited and approval-based. A commercial agreement or purchase alone does not guarantee access. If your request is approved, OpenAI will confirm the available access path and any applicable terms.

## What should I check if I still see a cyber safety message after approval?

Confirm that you are using the approved organization or workspace, the approved model or access path, and the intended product surface. Some safeguards can still apply after approval. If a clearly defensive request appears to be blocked unexpectedly, contact Support with the exact message, model, product surface, timestamp, request ID if available, and a brief redacted description of the task. Read more: Trusted Access for Cyber - Common Issues and Troubleshooting

## How can an organization limit Trusted Access to the right employees?

Trusted Access should be available only to approved internal users working on authorized security tasks. If you need to limit access, work with your OpenAI contact to set up an internal-only organization or workspace and provision only the appropriate users.
