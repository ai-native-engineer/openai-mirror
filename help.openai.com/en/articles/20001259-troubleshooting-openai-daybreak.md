<!-- source: https://help.openai.com/en/articles/20001259-troubleshooting-openai-daybreak -->

# Troubleshooting OpenAI Daybreak

Troubleshoot individual account-security requirements, verification, API project controls, model access, and cyber safety messages for OpenAI Daybreak.

Updated: 2 days ago

Daybreak Access is OpenAI’s Trusted Access for Cyber program. Daybreak Blue and Daybreak Red are access tiers within Daybreak levels. This article covers individual account-security requirements, verification, workspace and API project controls, model access, legacy GPT-5.5-Cyber access, and unexpected cyber safety messages.

Learn more about [OpenAI Daybreak.](/en/articles/20001258)

# Before you start

Before contacting Support, check the items that apply to your access path:

* If you are approved for Daybreak as an individual, you have checked Your eligibility at [chatgpt.com/cyber](https://chatgpt.com/cyber), including your plan, Advanced Account Security, hardware security keys, and identity-verification status.
* You are using the approved OpenAI organization or workspace and the intended API project.
* You are using the approved access path: Responses API, Codex with Sign in with ChatGPT, or Codex CLI.
* For legacy GPT-5.5-Cyber access, you are using the exact model name `gpt-5.5-cyber-preview`.
* For API, an API organization owner has checked the intended non-default project under Project settings → General → Daybreak model access. Being a project owner alone does not permit you to change these settings. Note that default API projects are not eligible for Daybreak, and that access changes can take up to 15 minutes to propagate.
* For API, you are using a credential from the enabled project; if you moved to a different organization or project, update the workload to use its destination-project key.
* For Codex, a workspace owner has enabled access for you (users can confirm via the Settings > General page under “Daybreak Access”).
* Your organization setup, approved user list, and usage or budget limits are complete.
* Your request is for systems, applications, accounts, networks, or data that you own, operate, or are explicitly authorized to test or analyze.

# Advanced Account Security and individual access

Individual Trusted Access requires an eligible paid plan, Advanced Account Security, and at least one compatible FIDO2 hardware security key. Existing individual users must meet these requirements by Oct 1, 2026 to keep access. Organization-level access follows a separate onboarding process.

## I can't start identity verification

Open [chatgpt.com/cyber](https://chatgpt.com/cyber), sign in to the account you want to use, and check **Your eligibility**. You must complete any unfinished plan or account-security steps before you can start identity verification. If you're still blocked, follow the message shown on the page.

If you already use Advanced Account Security, check that you have at least one qualifying physical hardware key registered to your OpenAI account. Follow the eligibility page's instructions to update your login methods; you do not need to enroll again if your setup already qualifies.

## My security key or passkey doesn't meet the requirements

Advanced Account Security supports several types of passkeys. Individual Daybreak access also requires at least one qualifying physical FIDO2 hardware security key. A software or synced passkey saved on your device or in a password manager does not count.

Register at least one approved physical FIDO2 hardware security key and follow the on-screen setup instructions. A second physical key is optional and can be used as a backup. You do not need to remove other passkeys from your OpenAI account, device, or password manager.

If a compatible key still is not recognized, contact Support with the exact error, a screenshot, your browser and device, and the approximate time of the attempt. Do not send your recovery keys, credentials, or other secrets.

## Unsupported FIDO2 hardware security keys

TrustKey T110 and T120 security keys are currently ineligible for individual Daybreak access.

## I can't find Advanced Account Security

Make sure you are signed in to the account associated with your individual Daybreak application. Advanced Account Security is not available for enterprise-managed accounts or accounts associated with a verified and claimed domain. Availability for other workspace-linked accounts can depend on their configuration.

Check the [Advanced Account Security availability guidance](https://help.openai.com/articles/20001221). If you believe your account should be eligible but cannot continue, contact Support with a screenshot and the error or missing option. For organization-level Daybreak access, follow your organization's onboarding instructions or contact your OpenAI account team.

### Individual security requirements for ChatGPT Business members

Membership in a Business or Team workspace does not exempt individual Daybreak Blue users from the Advanced Account Security and hardware-key requirements. Organization-level Daybreak access follows a separate onboarding process.

If you receive an individual security-setup reminder but cannot enroll in Advanced Account Security, contact Support with the message or error and a screenshot.

## Regain access after a security or plan change

You can lose individual Daybreak approval if Advanced Account Security is disabled or your account has fewer than one qualifying hardware key. Losing Trusted Access does not delete your ChatGPT account or existing chats.

If your revocation notice says your security settings or plan no longer qualify, follow these steps:

* Read the notice to understand which eligibility requirement changed.
* Open [chatgpt.com/cyber](https://chatgpt.com/cyber) and correct the plan or security issue shown under **Your eligibility**.
* Return to the Cyber page and follow the steps shown. If you lost access because of your account-security setup, complete identity verification again.

Updating your security settings does not automatically restore Daybreak. Reapplication is still subject to review and does not guarantee approval. If the flow will not restart, shows an error, or still leaves you without access after approval, follow the instructions in your notice or contact Support with the exact error and a screenshot.

If your notice concerns a different eligibility or policy decision, follow the instructions in that notice. For verification retry options, see the verification guidance below. Support cannot override a verification decision.

## I lost a hardware key or can't sign in

Use another hardware key registered to your account. If you no longer have access to your sign-in methods, use a saved Advanced Account Security recovery key to start account recovery. After you enter a valid recovery key, there is a 48-hour security waiting period before you can complete recovery.

Support can explain the available recovery options, but cannot bypass Advanced Account Security, reset your password, remove the setting, or add or remove sign-in methods to restore routine access. If you lose all of your sign-in methods and recovery keys, you may permanently lose access to your account.

Starting account recovery does not, by itself, remove Trusted Access. Your account must still meet the individual account-security requirements. Read [Advanced Account Security](https://help.openai.com/articles/20001221) for the full recovery steps.

# Verification issues

OpenAI may ask you to complete verification before granting OpenAI Daybreak access. Verification helps OpenAI evaluate whether the request qualifies for Daybreak Blue or Daybreak Red access. The required path can differ by customer type. For Enterprise customers, verification may be handled through an organization-level intake with OpenAI rather than an individual identity-verification flow.

Note that if your individual verification shows that you’re under 18, your request for Daybreak Access will not be approved.

## If verification fails or is denied

If verification is unsuccessful, follow the instructions shown. If the verification flow offers another attempt, you can submit verification again. Another attempt does not guarantee approval. If your account remains ineligible, Support cannot override the decision, grant Daybreak access, or provide details about the checks behind the result.

If OpenAI has instructed you to reapply after an account-security eligibility change or the Daybreak Blue verification issue below, follow those specific instructions. A new application is still subject to review.

### Daybreak is unavailable

Daybreak isn’t available in every region. We may expand availability to additional regions in the future.

If Daybreak is unavailable to your account, we can’t approve it based on our current identity-verification and eligibility requirements. You can still use ChatGPT.

## If you have a technical issue during verification

If the verification flow does not load, stalls, or shows an unexpected technical error:

* Retry the verification flow.
* Make sure your browser and device are up to date.
* If the issue continues, contact Support and include a screenshot of the error, your device and browser, and the approximate time the issue occurred.

## If you completed verification but still appear restricted

For individual Daybreak access, you can remain identity-verified while access is suspended because your Advanced Account Security setup is noncompliant. Check **Your eligibility** at [chatgpt.com/cyber](https://chatgpt.com/cyber) and follow the account-security steps shown. If you have completed the required steps but your status still does not update:

* Sign out and sign back in.
* Refresh the page or reopen the relevant product surface.
* If the issue continues, contact Support with a screenshot, device and browser details, and the approximate completion time.

## If you received a Daybreak Blue reverification email

We corrected a technical issue in our verification process and removed access from affected individual Daybreak Blue accounts. This was our error, and we're sorry for the disruption.

If you received an email asking you to verify again, follow its instructions to reapply. We'll review your application under current eligibility requirements. Reapplying does not guarantee approval or restored access.

If you can't restart verification, encounter an error, or finish the process but still can't access Daybreak Blue, reply to that email with details.

If your access hasn't changed, you don't need to reverify because of this issue. The [account-security requirements for individual Daybreak access](https://help.openai.com/articles/20001258) still apply.

# Daybreak model and project access issues

For the OpenAI API, organization eligibility determines which Daybreak controls can appear. An API organization owner configures the intended non-default project under Project settings → General → Daybreak model access. Workspace access for ChatGPT and Codex sign-in is configured separately through workspace roles.

The available project controls depend on organization eligibility:

* Daybreak Blue appears for organizations eligible for Daybreak Blue or Daybreak Red.
* Daybreak Red appears only for organizations eligible for Daybreak Red.

Enable the Daybreak level approved for the selected project and save. The toggle provides the Daybreak access available to that project; it does not grant models outside your organization’s approval. Some existing organization-level access may continue during migration, so follow your onboarding confirmation for the setup that applies to you.

## GPT-6 Sol, GPT-6 Luna, and Astra availability

GPT-6 Sol and GPT-6 Luna support reduced refusals with Daybreak Blue when your account is approved and Daybreak is enabled for the request. Astra keeps standard safeguards under Daybreak Blue. Reduced refusals on Astra require Daybreak Red access. We’re working to bring reduced refusals on Astra to Daybreak Blue; meanwhile, approved Blue users can choose GPT-6 Sol or GPT-6 Luna for reduced refusals, or continue using Astra with standard safeguards. Your account’s model access and the product you’re using determine which models are available.

## **Enable Daybreak for GPT-6.1 Terra**

If you’re approved for Daybreak Red but still see cyber refusals with GPT-6.1 Terra, check the settings for the way you’re using the model. Daybreak Blue approval alone doesn’t include reduced refusals for Terra. Check model availability separately from Daybreak access: Terra is supported in Work and Codex where enabled, rather than Chat, and does not support UAE inference residency. This is an inference-residency restriction, not a restriction based on your physical location.

Responses API: Use the approved organization and enabled non-default project associated with your API key, and explicitly select the Daybreak setting for the request. If you omit access\_programs.cyber, Terra uses standard safeguards. See [Use Daybreak in the Responses API](https://developers.openai.com/api/docs/guides/daybreak) for request configuration.

Chat Completions: Terra uses standard safeguards on this endpoint. To use Daybreak with an approved project, send your request through the Responses API.

Codex signed in with ChatGPT: Use the intended workspace, confirm your user has approved Daybreak Red access, and turn on the Daybreak toggle before sending your request. Existing workspace permissions still apply.

Update to a supported client if needed and try again. Seeing Terra in the model list or receiving an ordinary response doesn’t confirm that Daybreak is enabled. If an approved, correctly configured request still fails, contact Support with the model, sign-in method, workspace or organization and project IDs, client version, request ID, timestamp, and exact error. Do not include API keys or sensitive prompt content.

## If a Daybreak toggle does not appear

Ask an organization or workspace owner to confirm all of the following:

1. They are viewing the intended approved organization or workspace and, if in the API, are viewing a named project other than the default project.
2. The organization or workspace has been approved for the expected Daybreak access level. Provisioning is complete for the organization and project. OpenAI will send a welcome email to the organization or workspace admin when this is completed.
3. In the API, they opened Project settings → General → Daybreak model access. In Codex sign in via ChatGPT, they opened [Admin Console → Models](https://chatgpt.com/admin/models).
4. Provisioning is complete for the organization and project.

If the expected Daybreak control still does not appear, contact your OpenAI account team to confirm organization eligibility and provisioning. A different model setting is not a substitute for Daybreak approval.

## Issues using Daybreak in the Responses API

If your approval includes OpenAI API access:

1. Use the approved OpenAI organization and the enabled non-default API project.
2. Ask an API organization owner to confirm the approved Daybreak level is enabled under Project settings → General → Daybreak model access, then save.
3. Allow up to about 15 minutes for API project changes to take effect. Use the enabled project’s API key; after migration, use a key from the approved destination project.
4. Send a direct Responses API request using the approved model ID and the matching access\_programs.cyber setting:

| **Access** | access\_programs.cyber | Example model ID |
| --- | --- | --- |
| Daybreak Blue | `daybreak_blue` | `gpt-6-sol` |
| All Daybreak Red organizations | `daybreak_red` | `gpt-5.6-cyber` |
| Daybreak Red with GPT-6 Cyber approval | `daybreak_red` | `gpt-6-cyber` |

Use a direct request as the access check; do not rely on a model-listing surface as the only proof that access is active.

If the request fails:

1. Confirm that the relevant toggle is visible and enabled for the intended project.
2. Confirm that the request uses the correct organization, project API key, exact model ID, and access\_programs.cyber setting. For gpt-6-sol, set daybreak\_blue even if you are approved for Red.
3. Confirm that usage or budget limits are not preventing access.
4. Ask your OpenAI account team to confirm organization eligibility and project provisioning. For GPT-6 Cyber, also check that your organization has model approval, that your outbound IP address is on the [allowlist](/en/articles/20001201-ip-allowlisting-for-openai-api), and that [Private Safety Processing](/en/articles/20001595-getting-started-with-zdr-with-private-safety-processing) is set up if the project uses Zero Data Retention.
5. Collect the exact error text, request ID, timestamp, and time zone before contacting Support.

## Issues using Daybreak in Codex

* Confirm that your account and organization or workspace are approved for the intended Daybreak access.
* Update to the latest supported version of the Codex app or Codex CLI.
* Sign in using the account and authentication method specified in your approval.
* If you sign in with ChatGPT, use the approved workspace and turn the Daybreak toggle on before making a request. GPT-6 Sol and GPT-6 Luna support reduced refusals for approved Daybreak Blue users. All Daybreak Red organizations are eligible for GPT-5.6 Cyber. To use GPT-6 Cyber, your organization also needs approval for that model. If access is missing, a workspace owner should check your assigned roles and saved model permissions.
* If you use an OpenAI API key to sign in to Codex, use a key from the enabled API project. Access follows that project and its approved models. You won’t see a special Daybreak interface. Select an explicit approved model. For example, if your approved Daybreak Blue access includes GPT-6 Sol, run `codex -m gpt-6-sol` in Codex CLI. The `gpt-` prefix is required. For approved Daybreak Red access, specify the approved model ID in `config.toml`. Models with `-cyber` in their name do not appear in the API-key model picker.

### Issues using GPT-5.5-Cyber in the Responses API

If your approval includes Responses API access:

* Use the approved OpenAI organization tied to your access.
* Send a direct Responses API request with the model gpt-5.5-cyber-preview.

If a direct Responses API request succeeds, your model access is active even if the /models endpoint does not list the model.

If the request fails:

* Confirm you are using the correct organization and exact model name.
* Confirm that your organization setup is complete. If you are unsure, contact your OpenAI account team.
* Confirm that usage or budget limits are not preventing access.
* Collect the exact error text, request ID, timestamp, and time zone before contacting Support.

### Issues using GPT-5.5-Cyber in Codex

If your approval includes Codex access:

* Work with your OpenAI account team to make sure your specific user account has been approved for GPT-5.5-Cyber access.
* Update to Codex app version 26.513.20950 or later, or Codex CLI version 0.133.0 or later, depending on which surface you use.
* Sign in to Codex with ChatGPT.
* Check the model picker and select GPT-5.5-Cyber-Preview.

### Common reasons access may not appear

Use the table below to check the most common access issues.

| **Reason** | **Mitigation** |
| --- | --- |
| Wrong OpenAI organization or workspace | Switch to the OpenAI organization or workspace tied to the approved access path. |
| Checking /models instead of testing access directly | Send a direct Responses API request with the approved model. At this time, some Daybreak models may not appear in /models endpoint. |
| Approved user list or organization setup is not aligned | Work with your OpenAI account team to confirm the approved users, organization, and access path. |
| Organization enablement or user provisioning is incomplete | Ask your OpenAI contact to confirm provisioning is complete before escalating to Support. |

## Cyber safety messages after approval

OpenAI Daybreak reduces some cyber-related blocks for approved customers, but it does not remove every safeguard. You may still encounter two different kinds of behavior:

* System-level safety messages that block, slow, or reroute a request before completion.
* Model-level refusals where the model responds but declines to help.

Usage-policy controls still apply in either case.

### Why a cyber safety message can still appear

You may still see a cyber-related message when:

* A request appears high risk or outside ordinary defensive cybersecurity use.
* You are using a standard model rather than an approved cyber-specialized model.
* The request is interpreted as offensive, abusive, or too ambiguous to safely complete.
* A product or API safety control is still applied to the request.

### How this can appear

Depending on the surface, you may see:

* A message saying access was temporarily limited or that the request was routed to a fallback model to reduce cyber-abuse risk.
* An API error such as cyber\_policy.
* A refusal or other warning in the product experience.

### What to do when you receive a safety message

First, confirm which model and access path you used. Then contact Support if you believe:

* A clearly defensive request appears to be blocked unexpectedly.
* You received a cyber\_policy error while using a provisioned Daybreak model or the legacy gpt-5.5-cyber-preview model.
* You confirmed that provisioning is complete and the correct Daybreak level is enabled for the intended workspace user or API project.

Do not send secrets, private keys, exploit targets, or confidential third-party data unless OpenAI specifically instructs you to do so through an approved support path.

## Contacting Support

If you still cannot complete verification, access Daybreak Blue, Daybreak Red, or legacy GPT-5.5-Cyber, or resolve a cyber safety message after working through the steps above, contact Support and include as much of the following as you can:

* Your organization name.
* The OpenAI organization ID used for the request.
* The API project ID used for the request.
* Whether you are using ChatGPT, Codex, or the API.
* The approved access path you expected to use.
* The exact model name used in the API or Codex.
* For API issues, whether an API organization owner can see and enable the expected Daybreak control under Project settings → General → Daybreak model access. For workspace issues, include the affected user’s role assignments and saved model permissions.
* The full error message or safety message.
* The request ID, timestamp, and time zone for API failures.
* A screenshot if the issue is UI visibility, verification flow behavior, or an account settings view.
* A brief redacted description of the cybersecurity task.
* Whether the task involves systems you own or are authorized to test.

# FAQ

## Where do I enable Daybreak Blue or Daybreak Red for an API project?

An owner of the approved API organization can open the intended non-default project and go to Project settings → General → Daybreak model access. Enable the approved Daybreak level and save. Red is shown only for eligible organizations. Changes can take about 15 minutes to take effect.

## Where do I enable Daybreak Blue or Daybreak Red for a Codex sign in via ChatGPT user?

An admin of the approved workspace can open **Roles**, choose **Edit override** for the intended role, or choose **Add role override** to create an override. Under **Cybersecurity**, the admin can set **Daybreak Blue** to On. Enable Daybreak Red only if it is approved for the workspace and these users are authorized to use it. Select **Save**. Changes can take about 10 minutes to take effect.

## Does a model-access setting replace Daybreak approval?

No. Your organization must be approved and the intended project must have the eligible Daybreak level enabled. A model-access setting cannot grant Daybreak approval or expand your approved scope. If an approved model remains unavailable, check its entitlement and your project configuration with your OpenAI account team.

## Does existing Daybreak approval include Daybreak Red?

No. Daybreak Red requires separate approval and activation from Daybreak Blue. Red approval makes your organization eligible for GPT-5.6 Cyber. GPT-6 Cyber requires separate approval for that model.

## Why does the /models endpoint not show GPT-5.5-Cyber?

Some approved models may be directly usable before they appear in model-listing surfaces. Use a direct Responses API request with gpt-5.5-cyber-preview or the relevant model ID to test access.

## Why can I not see GPT-5.5-Cyber in Codex?

If your approval includes Codex access, make sure you are signed in with ChatGPT using an approved user account, then reload Codex or start a new CLI session.

## Is Daybreak available through AWS Bedrock, Azure, or another cloud provider?

Daybreak is available via AWS Bedrock, though it still requires OpenAI approval via the standard Daybreak route - reach out to your AWS account team for access.

## Does Daybreak change my data retention or Zero Data Retention settings?

No. Daybreak access and data-retention settings are separate. Existing data controls apply only if they are enabled for the approved organization or project. If you need Zero Data Retention or a specific data posture, raise it with your OpenAI contact during intake or before using the model.

## Does OpenAI Daybreak remove all cyber-related refusals?

No. OpenAI Daybreak can reduce certain system-level refusal friction for eligible authorized work, but model-level refusals and other usage-policy controls can still apply.

## Why do I need to verify my identity?

OpenAI Daybreak is intended for vetted customers and users working on legitimate authorized cybersecurity tasks. Verification helps OpenAI evaluate access requests responsibly. Depending on the access path, verification may happen through an organization-level intake or a user verification flow.

## How long does verification take?

The verification flow itself may be quick, but final access timing depends on the broader review and provisioning process.

## Can support change a verification result?

No. Support cannot manually override the result of an OpenAI Daybreak verification decision.
