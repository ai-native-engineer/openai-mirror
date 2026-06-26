<!-- source: https://openai.com/index/our-response-to-the-tanstack-npm-supply-chain-attack/ -->

May 13, 2026

[Company](/news/company-announcements/)[Security](/news/security/)

# Our response to the TanStack npm supply chain attack

Update now

*Amended: Update your macOS applications by June 26, 2026*

*We are extending the update deadline for macOS users to June 26, 2026.  We have been coordinating with Apple on this timeline to protect our users. New notarization with the previous certificate has been blocked, and we have found no evidence of malicious software being signed with any OpenAI certificate or unauthorized changes to our published software. These safeguards continue to help protect users by default while we complete the migration.  You can update safely through an in-app update or at the official links below.*

---

We recently identified a security issue involving a common open-source library, TanStack npm, that is part of a broader attack known as [Mini Shai-Hulud⁠(opens in a new window)](https://digital.nhs.uk/cyber-alerts/2026/cc-4781?__cf_chl_tk=Z4ZM7V1dpv.vsg8WZKif8WGUwIAex5O1lc4PNtP8kbU-1778622246-1.0.1.1-TYh2i2iW_1.OOBQKrxw3aErpyJOIuZjtPFyY1s3KnUc). We found no evidence that OpenAI user data was accessed, that our production systems or intellectual property were compromised, or that our software was altered.

We have taken decisive steps to protect our user data, systems, and intellectual property. As part of our response, we are taking steps to protect the process that certifies our macOS applications are legitimate OpenAI apps.

### Update your macOS applications by June 12, 2026

We are updating our security certificates, which will require all macOS users to update their OpenAI apps to the latest versions. This helps prevent any risk, however unlikely, of someone attempting to distribute a fake app that appears to be from OpenAI. You can update safely through an in-app update or at the official links below:

* [ChatGPT Desktop⁠(opens in a new window)](https://chatgpt.com/download)
* [Codex App⁠](/codex/)
* [Codex CLI⁠(opens in a new window)](https://github.com/openai/codex)
* [Atlas⁠](/atlas/)

The security and privacy of your information are a top priority. We’re committed to being transparent and taking quick action when issues arise. We’re sharing more technical details and FAQs below.

## What happened and what we are doing

On May 11, 2026 UTC, TanStack, a widely used open-source library, [was compromised as part of a broader software supply chain attack known as Mini Shai-Hulud⁠(opens in a new window)](https://socket.dev/blog/tanstack-npm-packages-compromised-mini-shai-hulud-supply-chain-attack).

Two employee devices in our corporate environment were impacted by this attack. Upon identification of the malicious activity, we worked quickly to investigate, contain, and take steps to protect our systems. As part of our investigation and response, we engaged a third-party digital forensics and incident response firm.

We observed activity consistent with the malware’s publicly described behavior, including unauthorized access and credential-focused exfiltration activity, in a limited subset of internal source code repositories to which the two impacted employees had access. We confirmed that only limited credential material was successfully exfiltrated from these code repositories and that no other information or code was impacted.

We acted immediately to contain the activity. We isolated impacted systems and identities, revoked user sessions, rotated all credentials across impacted repositories, temporarily restricted code-deployment workflows, and thoroughly scrutinized user and credential behavior. As part of our investigation, we have not observed evidence of impact to customer data, or our intellectual property, and our analysis has not identified misuse of impacted credentials or follow-on access by the threat actor.

The impacted source code repositories included signing certificates for our products, including iOS, macOS, and Windows. As a result, we are rotating code-signing certificates as a precaution, which will require macOS users to update their applications. Users do not need to take any action for Windows and iOS apps. Additional guidance will be provided to macOS users regarding these required updates.

In addition to rotating certificates, we are coordinating with platform providers to prevent any unauthorized use of these certificates by stopping new notarizations. We have also reviewed all notarization of software using our previous certificates to confirm no unexpected software signing has occurred with these keys, and validated that our published software did not have unauthorized modifications. We have found no evidence of compromise or risk to existing software installations.

Once we fully revoke our certificate on June 12, 2026, new downloads and launches of apps signed with the previous certificate will be blocked by macOS security protections.

After the [Axios incident](/index/axios-developer-tool-compromise/), we accelerated the deployment of specific security controls and technologies to reduce the impact of supply chain attacks such as this one. Our security response included further hardening of sensitive credential materials used in our CI/CD pipeline, deployment of package manager configurations with controls like minimumReleaseAge, and additional security software to validate the provenance of new packages.

This incident occurred during our phased deployment and rollout of these controls, and the two impacted employee devices did not have the updated configurations that would have prevented the download of the newly observed package containing malware.

This incident reflects a broader shift in the threat landscape: attackers are increasingly targeting shared software dependencies and development tooling rather than any single company. Modern software is built on a deeply interconnected ecosystem of open-source libraries, package managers, and continuous integration and continuous deployment infrastructure, which means that a vulnerability introduced upstream can propagate widely and quickly across organizations. We are continuing to invest in controls that validate the integrity and provenance of third-party components and to strengthen our defenses against these kinds of ecosystem-level supply chain attacks.

## FAQ

**Were OpenAI products or user data compromised?**

No. We have found no evidence that OpenAI products or user data were compromised or exposed.

**Have you seen malware signed as OpenAI?**

No. We have found no evidence of malicious software being signed with any of OpenAI’s certificates.

**Do I need to change my password?**

No. Customer/user passwords and API keys were not affected.

**What platforms does this affect?**

Our signing keys for Windows, macOS, iOS, and Android were impacted. All of our applications are being re-signed and released with new certificates. macOS users will need to take action to update by June 12, 2026 for applications to continue functioning.

**Why are you asking me to update my Mac apps?**

Updating ensures you are running versions signed with our latest certificate. This certificate helps customers know that software comes from the legitimate developer, OpenAI.

**Where do I download the updated macOS apps?**

Only download OpenAI apps from in-app updates or the official webpages below:

* [ChatGPT⁠(opens in a new window)](https://chatgpt.com/download)
* [Codex App⁠](/codex/)
* [Codex CLI⁠(opens in a new window)](https://github.com/openai/codex)
* [Atlas⁠](/atlas/)

Do not install apps from links in emails, messages, ads, or third-party download sites. Be cautious of unexpected “OpenAI,” “ChatGPT,” or “Codex” installers sent through email, text, chat messages, ads, file-sharing links, or third-party download sites.

**What happens after June 12, 2026?**

Effective June 12, 2026, older versions of our macOS desktop apps will no longer receive updates or support, and may not be functional. These versions represent the last releases signed with our outdated certificate:

* ChatGPT Desktop: 1.2026.118
* Codex App: 26.506.31421
* Codex CLI: 0.130.0
* Atlas: 1.2026.119.1

**Why are you not revoking the certificate immediately?**

We have worked to block any further notarization of macOS apps with the impacted notarization material. This means that any fraudulent app posing as an OpenAI app using the impacted certificate will lack notarization, and therefore will be blocked by default by macOS security protections unless a user explicitly bypasses those protections. Because new notarization with the previous certificate is blocked, and because the revocation may cause macOS to block new downloads and first-time launches of apps signed with the previous certificate, we are giving our users until June 12, 2026 to update to minimize disruption. This window will help minimize user risk and allow impacted clients to update through built-in update mechanisms, ensuring they are appropriately remediated. We are working with our partners to monitor for any indicators of misuse of the signing certificate, and will accelerate the revocation timeline if we identify malicious activity during this window.

* [2026](/news/?tags=2026)

## Author

## Keep reading

![How agents are transforming work > Cover image](https://images.ctfassets.net/kftzwdyauwt9/7hmtkjKv0DxS4Yt8mQZju2/c168bfa2010da64bcc9dd60d6b5491e8/Art_Card__1_.png?w=3840&q=90&fm=webp)

[How agents are transforming work

CompanyJun 25, 2026](/index/how-agents-are-transforming-work/)

![OpenAI and Broadcom Jalapeño inference chip card image](https://images.ctfassets.net/kftzwdyauwt9/21KcazqOHUF7Cq71Hpfcnc/81ad98a1978845b441ab14e008168c75/openai-broadcom-jalapeno-inference-chip-image-1_1.png?w=3840&q=90&fm=webp)

[OpenAI and Broadcom unveil LLM-optimized inference chip

CompanyJun 24, 2026](/index/openai-broadcom-jalapeno-inference-chip/)

![Expanding Daybreak Art Card](https://images.ctfassets.net/kftzwdyauwt9/735NOZviyogUBIFxd2EmWX/fa8baf9fc26e64f442ffa86d5fd9a41e/Art_Card__6_.png?w=3840&q=90&fm=webp)

[Daybreak: Tools for securing every organization in the world

SecurityJun 22, 2026](/index/daybreak-securing-the-world/)
