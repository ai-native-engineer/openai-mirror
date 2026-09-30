<!-- source: https://openai.com/policies/sign-in-with-chatgpt-terms/ -->

OpenAI

September 29, 2026

# Sign in with ChatGPT Terms

These Sign in with ChatGPT Terms (“Terms”) govern your use of Sign in with ChatGPT (“SIWC”) in an application you develop or maintain (“your application” or “your app”). SIWC lets users connect their ChatGPT accounts and use eligible ChatGPT plans to power AI features in your app.

These Terms incorporate the [Terms of Use](/policies/row-terms-of-use/) and our [Service Terms](/policies/service-terms/) (together the “Agreement”). Other capitalized terms have the meanings given in the Agreement.

By integrating or using SIWC in your application, you agree to these Terms. If acting for an organization, you represent that you have the authority to accept these Terms on its behalf.

## 1. Application identity and security

Use your app’s own name during sign-in and activation. Do not impersonate OpenAI, another application, or another open-source project.

Obtain and use SIWC access and refresh tokens (“Authentication Tokens”) only through OpenAI’s supported sign-in flow and as authorized by the user. Do not ask users for their ChatGPT passwords or session cookies.

Keep account information and Authentication Tokens secure. Any persistent storage of Authentication Tokens must be local and under the user’s control, not in a remote or managed environment.

## 2. ChatGPT plan usage

Your app must meet these requirements:

* **User control.** Requests must originate from the user’s local runtime or a remote runtime only that user controls.
* **User authorization.** Requests must be for the authenticated user and arise from their activity or expressly authorized automations or background processes. Obtain express consent before background use. Another user’s activity must not trigger requests to the authenticated user’s account.
* **Connected application only.** Use the user’s plan only for the application they connected. Do not provide general-purpose API access for other tools or unrelated requests.
* **No charge.** Users must be able to use their ChatGPT plan through SIWC without paying you or upgrading to a paid version of your application.

Plan eligibility and usage limits apply. SIWC does not grant extra usage or access to other OpenAI services. These restrictions do not affect separately authorized API use.

## 3. Privacy & Security

You are responsible for the privacy, security, and integrity of your app and your use of SIWC, including determining any applicable legal obligations. You agree to maintain at least reasonable and appropriate organizational, administrative, physical, and technical security measures to keep your app, including your use of SIWC, secure. If you discover vulnerabilities or breaches related to your app or your use of SIWC which may affect your users, you must promptly contact OpenAI and provide details of the vulnerability or breach.

You also agree to only process personal data (i) in accordance with applicable privacy laws, (ii) as authorized by your users, and (iii) in accordance with a legally adequate privacy notice that is presented to users before processing their data. You may not collect personal data beyond what is reasonably necessary to provide the SIWC functionality and power your app. You further agree to provide users with any necessary disclosures or controls, and obtain any necessary consents.

## 4. Prohibited activities

You must not enable or encourage:

* Creating multiple accounts, splitting usage, rotating accounts, or otherwise bypassing usage limits.
* Pooling, transferring, reselling, gifting, or sharing ChatGPT plan usage or Authentication Tokens, except for token handling expressly permitted by these Terms.
* Using one user’s subscription to fulfill another user’s requests.

Your SIWC integration and use must comply with applicable law, these Terms, [the applicable license⁠(opens in a new window)](https://github.com/openai/sign-in-with-chatgpt-devkit/blob/main/LICENSE), and our [Usage Policies](/policies/usage-policies/). You may not:

* Use SIWC in a way that poses a security vulnerability or threat to users, OpenAI, or any third party.
* Interact with users in a manner that is deceptive, false, misleading, or harassing.
* Include any malware, viruses, surveillance, or other malicious code or programs.
* Alter, reverse engineer, or otherwise amend the SIWC software.
* Sublicense SIWC or any underlying technology.
* Otherwise use SIWC for fraudulent, illegal, or abusive purposes.

## 5. User experience and branding

Use OpenAI names, logos, and buttons only as authorized. Do not imply OpenAI sponsorship or endorsement without OpenAI’s prior written permission.

## 6. Enforcement

We may suspend or disable your application’s access to SIWC if it violates these Terms or presents a security, safety, or abuse risk.
