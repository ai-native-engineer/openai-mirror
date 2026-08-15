<!-- source: https://help.openai.com/en/articles/20001259-openai-daybreak-common-issues-and-troubleshooting -->

# OpenAI Daybreak - Common Issues and Troubleshooting

Troubleshoot OpenAI Daybreak verification, project-level Daybreak Blue and Daybreak Red controls, model access, legacy GPT-5.5-Cyber access, and cyber safety messages.

Updated: 2 days ago

Daybreak Access is OpenAI’s Trusted Access for Cyber program. Daybreak Blue and Daybreak Red are access levels.

This article covers common issues customers may encounter with Daybreak Access, including verification, API Platform project controls, model access, legacy GPT-5.5-Cyber access, and unexpected cyber safety messages.

Learn more about [OpenAI Daybreak.](/en/articles/20001258)

# Before you start

Confirm the following before contacting Support:

* You are using the approved OpenAI organization or workspace and the intended API project.
* You are using the approved access path: Responses API or Codex with Sign in with ChatGPT, or Codex CLI.
* For the OpenAI API, you are using the exact alias or model ID for the access path you expect: Daybreak Blue uses `gpt-daybreak-blue` (alias) or `gpt-5.6-sol` (model ID), and Daybreak Red uses `gpt-daybreak-red` (alias) or `gpt-5.6-cyber` (model ID).
* For legacy GPT-5.5-Cyber access, you are using the exact model name `gpt-5.5-cyber-preview`.
* For OpenAI API troubleshooting, an organization admin has opened the intended project in API Platform and gone to Project settings → Limits. Only organization admins can see or change the Daybreak controls.
* If the controls are available for your organization, the organization admin has enabled Daybreak for the eligible project and then enabled the specific eligible model. Daybreak Blue appears for organizations eligible for Daybreak Blue or Daybreak Red, and Daybreak Red appears only for organizations eligible for Daybreak Red.
* After an organization admin changes a Daybreak or model setting, create a new project API key or refresh the project credentials before retesting.
* Your organization setup, approved user list, and usage or budget limits are complete.
* Your request is for systems, applications, accounts, networks, or data that you own, operate, or are explicitly authorized to test or analyze.

# Verification issues

OpenAI may ask you to complete verification before granting OpenAI Daybreak access. Verification helps OpenAI evaluate whether the request qualifies for Daybreak Blue or Daybreak Red access. The required path can differ by customer type. For Enterprise customers, verification may be handled through an organization-level intake with OpenAI rather than an individual identity-verification flow.

## If verification fails or is denied

If your verification attempt is not approved, review the current OpenAI Daybreak requirements and follow the instructions in the notice you received. Support cannot manually override a verification result or provide additional details about why a specific result occurred. At this time, OpenAI Daybreak verification does not support retries or appeals.

## If you have a technical issue during verification

If the verification flow does not load, stalls, or shows an unexpected technical error:

1. Retry the verification flow.
2. Make sure your browser and device are up to date.
3. If the issue continues, contact Support and include a screenshot of the error, your device and browser, and the approximate time the issue occurred.

## If you completed verification but still appear restricted

If you completed the verification flow but your status does not update:

1. Sign out and sign back in.
2. Refresh the page or reopen the relevant product surface.
3. If the issue continues, contact Support with a screenshot, device and browser details, and the approximate completion time.

# Daybreak model and project access issues

For the OpenAI API, organization eligibility determines which Daybreak controls can appear. When the controls are available, only organization admins can see or change them in API Platform under Project settings → Limits.

The available controls depend on organization eligibility:

* Daybreak Blue appears for organizations eligible for Daybreak Blue or Daybreak Red.
* Daybreak Red appears only for organizations eligible for Daybreak Red.

In API Platform, an organization admin enables Daybreak for the eligible project and then enables the specific eligible model. Project settings determine API availability for the selected project. Some existing organization-level Trusted Access behavior may continue during migration; follow your onboarding confirmation for the exact access boundary.

## If a Daybreak toggle does not appear

Ask an organization admin to confirm all of the following:

1. They are viewing the intended organization and API project.
2. They opened Project settings → Limits.
3. The organization has been approved for the expected Daybreak access level.
4. Provisioning is complete for the organization and project.

If the expected Daybreak control still does not appear, contact your OpenAI account team.

If Daybreak Blue appears but Daybreak Red does not, ask your OpenAI account team to confirm that the organization has separate Daybreak Red approval and the required model-specific entitlement.

## Issues using Daybreak Blue or Daybreak Red in the Responses API

If your approval includes OpenAI API access:

1. Use the approved OpenAI organization and intended API project.
2. In API Platform, ask an organization admin to open the intended project and go to Project settings → Limits.
3. Ask the organization admin to enable Daybreak for the eligible project and then enable the specific eligible model.
4. Create a new project API key or refresh the project credentials after either setting changes.
5. Send a direct Responses API request using the stable alias or underlying model ID:

| **Access** | **Stable alias** | **Model ID** |
| --- | --- | --- |
| Daybreak Blue | `gpt-daybreak-blue` | `gpt-5.6-sol` |
| Daybreak Red | `gpt-daybreak-red` | `gpt-5.6-cyber` |

Use a direct request as the access check; do not rely on a model-listing surface as the only proof that access is active.

If the request fails:

1. Confirm that Daybreak and the specific eligible model are enabled for the intended API project.
2. Confirm that the request uses the correct organization, project API key, and exact alias or model ID.
3. Confirm with your OpenAI account team that organization eligibility, provisioning, and any model-specific entitlement are complete.
4. Confirm that usage or budget limits are not preventing access.
5. Collect the exact error text, request ID, timestamp, and time zone before contacting Support.

## Issues using Daybreak models in Codex

* Confirm that your account and organization or workspace are approved for the intended Daybreak access.
* Update to the latest supported version of the Codex app or Codex CLI.
* Sign in using the account and authentication method specified in your approval.
* Open the model picker and select the model associated with your approved access.
* If Daybreak Red is unavailable, ask your OpenAI account team to confirm that the separate approval and provisioning are complete.

## Legacy GPT-5.5-Cyber access issues

GPT-5.5-Cyber access can be provisioned for different product surfaces. Approval for one path does not automatically prove that another path is active.

Your approval may cover:

* Responses API access.
* Codex access using Sign in with ChatGPT.

Codex access using API-key authentication is not available today for GPT-5.5-Cyber.

### Issues using GPT-5.5-Cyber in the Responses API

If your approval includes Responses API access:

1. Use the approved OpenAI organization tied to your access.
2. Send a direct Responses API request with the model `gpt-5.5-cyber-preview`.

If a direct Responses API request succeeds, your model access is active even if the `/models` endpoint does not list the model.

If the request fails:

1. Confirm you are using the correct organization and exact model name.
2. Confirm that your organization setup is complete. If you are unsure, contact your OpenAI account team.
3. Confirm that usage or budget limits are not preventing access.
4. Collect the exact error text, request ID, timestamp, and time zone before contacting Support.

### Issues using GPT-5.5-Cyber in Codex

If your approval includes Codex access:

1. Work with your OpenAI account team to make sure your specific user account has been approved for GPT-5.5-Cyber access.
2. Update to Codex app version 26.513.20950 or later, or Codex CLI version 0.133.0 or later, depending on which surface you use.
3. Sign in to Codex with ChatGPT.
4. Check the model picker and select GPT-5.5-Cyber-Preview.

### Common reasons access may not appear

Use the table below to check the most common access issues.

| **Reason** | **Mitigation** |
| --- | --- |
| Wrong OpenAI organization or workspace | Switch to the OpenAI organization or workspace tied to the approved access path. |
| Wrong model name in the Responses API | Use the exact model name `gpt-5.5-cyber-preview`. |
| Checking `/models` instead of testing access directly | Send a direct Responses API request with the approved model. At this time, legacy GPT-5.5-Cyber may not appear in `/models`. |
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
* An API error such as `cyber_policy`.
* A refusal or other warning in the product experience.

### What to do when you receive a safety message

First, confirm which model and access path you used. Then contact Support if you believe:

* A clearly defensive request appears to be blocked unexpectedly.
* You received a `cyber_policy` error while using a provisioned Daybreak model or the legacy `gpt-5.5-cyber-preview` model.
* You confirmed with your OpenAI account contact that your Daybreak Access or legacy GPT-5.5-Cyber provisioning is complete; for API requests, confirm that Daybreak and the specific eligible model are enabled for the intended project.

Do not send secrets, private keys, exploit targets, or confidential third-party data unless OpenAI specifically instructs you to do so through an approved support path.

## Contacting Support

If you still cannot complete verification, access Daybreak Blue, Daybreak Red, or legacy GPT-5.5-Cyber, or resolve a cyber safety message after working through the steps above, contact Support and include as much of the following as you can:

* Your organization name.
* The OpenAI organization ID used for the request.
* The API project ID used for the request.
* Whether you are using ChatGPT, Codex, or the API.
* The approved access path you expected to use.
* The exact model name used in the API or Codex.
* For API issues, whether an organization admin can see the expected Daybreak control under Project settings → Limits, and whether Daybreak and the specific eligible model are enabled.
* The full error message or safety message.
* The request ID, timestamp, and time zone for API failures.
* A screenshot if the issue is UI visibility, verification flow behavior, or an account settings view.
* A brief redacted description of the cybersecurity task.
* Whether the task involves systems you own or are authorized to test.

# FAQ

## Where do I enable Daybreak Blue or Daybreak Red for an API project?

If the Daybreak project controls are available for your organization, an organization admin can open the intended project in API Platform and go to Project settings → Limits. Only organization admins can see or change these controls. Daybreak Blue appears for organizations eligible for Daybreak Blue or Daybreak Red. Daybreak Red appears only for organizations eligible for Daybreak Red.

## Which Daybreak model name should I use in the OpenAI API?

For Daybreak Blue, use the stable alias `gpt-daybreak-blue` or model ID `gpt-5.6-sol`. For Daybreak Red, use the stable alias `gpt-daybreak-red` or model ID `gpt-5.6-cyber`. Use `gpt-5.5-cyber-preview` for the legacy GPT-5.5-Cyber model.

## Do I need to change a model allow/block list?

Daybreak access and model availability are both configured in API Platform under Project settings → Limits. An organization admin enables Daybreak for the eligible project and then enables the specific eligible model. Project settings determine API availability for the selected project. Some existing organization-level Trusted Access behavior may continue during migration; follow your onboarding confirmation for the exact access boundary.

## Does existing Trusted Access for Cyber or GPT-5.5-Cyber approval include Daybreak Red?

No. Daybreak Red requires separate approval and activation. Existing Trusted Access for Cyber or GPT-5.5-Cyber access does not automatically grant Daybreak Red.

## Does Trusted Access for Cyber approval include GPT-5.5-Cyber?

Not automatically. Trusted Access for Cyber can support many defensive cybersecurity workflows with GPT-5.5. GPT-5.5-Cyber is intended for a narrower set of specialized authorized workflows and may require additional approval and controls.

## Why does the `/models` endpoint not show GPT-5.5-Cyber?

Some approved models may be directly usable before they appear in model-listing surfaces. Use a direct Responses API request with `gpt-5.5-cyber-preview` to test access.

## Why can I not see GPT-5.5-Cyber in Codex?

If your approval includes Codex access, make sure you are signed in with ChatGPT using an approved user account, then reload Codex or start a new CLI session.

## Can I use GPT-5.5-Cyber in Codex with an API key?

Not currently. Use Sign in with ChatGPT for approved Codex cyber access unless OpenAI provides updated guidance.

## Can I use GPT-5.5-Cyber outside Codex?

Yes, if your approval includes API, GPT-5.5-Cyber is not limited to Codex. Approved customers can use it through the approved access path, such as the Responses API or Codex, for authorized internal security workflows.

## Does GPT-5.5-Cyber approval cover both the Responses API and Codex?

Not necessarily. The Responses API and Codex paths are provisioned separately. Approval for one path does not mean the other path is active.

## Is GPT-5.5-Cyber available through AWS Bedrock, Azure, or another cloud provider?

GPT-5.5-Cyber is not generally available through cloud-provider-hosted paths. If a cloud-provider path is required, work with your OpenAI account team.

## Does GPT-5.5-Cyber change my data retention or Zero Data Retention settings?

No. GPT-5.5-Cyber access and data-retention settings are separate. Existing data controls apply only if they are enabled for the approved organization or project. If you need Zero Data Retention or a specific data posture, raise it with your OpenAI contact during intake or before using the model.

## Does OpenAI Daybreak remove all cyber-related refusals?

No. OpenAI Daybreak can reduce certain system-level refusal friction for eligible authorized work, but model-level refusals and other usage-policy controls can still apply.

## What if `gpt-5.5-cyber-preview` returns a `cyber_policy` error?

Contact Support with the request ID, timestamp, model, product surface, exact error text, and a brief redacted description of the task so OpenAI can investigate.

## Why do I need to verify?

OpenAI Daybreak is intended for vetted customers and users working on legitimate authorized cybersecurity tasks. Verification helps OpenAI evaluate access requests responsibly. Depending on the access path, verification may happen through an organization-level intake or a user verification flow.

## How long does verification take?

The verification flow itself may be quick, but final access timing depends on the broader review and provisioning process.

## Can support change a verification result?

No. Support cannot manually override the result of an OpenAI Daybreak verification decision.
