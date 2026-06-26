<!-- source: https://help.openai.com/en/articles/20001259-trusted-access-for-cyber-common-issues-and-troubleshooting -->

# Trusted Access for Cyber - Common Issues and Troubleshooting

Troubleshoot Trusted Access for Cyber verification, GPT-5.5-Cyber access, and cyber safety messages after approval.

Updated: 9 days ago

# Overview

This article covers common issues customers may run into relating to the Trusted Access for Cyber program, including verification issues, access issues, and unexpected cyber safety messages when using the models.  
  
Learn more about [Trusted Access for Cyber.](/en/articles/20001258-trusted-access-for-cyber)

# Before you start

Confirm the following before contacting Support:

* You are using the approved OpenAI organization or workspace.
* You are using the approved access path: Responses API or Codex with Sign in with ChatGPT, or Codex CLI.
* You are using the exact model name, when applicable: `gpt-5.5-cyber-preview`.
* Your organization setup, approved user list, and usage or budget limits are complete.
* Your request is for systems, applications, accounts, networks, or data that you own, operate, or are explicitly authorized to test or analyze.

# Verification issues

OpenAI may ask you to complete verification before granting Trusted Access for Cyber. Verification helps OpenAI evaluate whether the request qualifies for trusted cybersecurity access. The required path can differ by customer type. For Enterprise customers, verification may be handled through an organization-level intake with OpenAI rather than an individual identity-verification flow.

## If verification fails or is denied

If your verification attempt is not approved, review the current Trusted Access for Cyber requirements and follow the instructions in the notice you received. Support cannot manually override a verification result or provide additional details about why a specific result occurred. At this time, Trusted Access for Cyber verification does not support retries or appeals.

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

# GPT-5.5-Cyber access issues

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

| Reason | Mitigation |
| --- | --- |
| Wrong OpenAI organization or workspace | Switch to the OpenAI organization or workspace tied to the approved access path. |
| Wrong model name in the Responses API | Use the exact model name `gpt-5.5-cyber-preview`. |
| Checking `/models` instead of testing access directly | Send a direct Responses API request with the approved model. Reminder that at this time, cyber models do not appear in the `/models` endpoint. |
| Approved user list or organization setup is not aligned | Work with your OpenAI account team to confirm the approved users, organization, and access path. |
| Organization enablement or user provisioning is incomplete | Ask your OpenAI contact to confirm provisioning is complete before escalating to Support. |

## Cyber safety messages after approval

Trusted Access for Cyber reduces some cyber-related blocks for approved customers, but it does not remove every safeguard. You may still encounter two different kinds of behavior:

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
* You received a `cyber_policy` error while using `gpt-5.5-cyber-preview`.
* You confirmed with your OpenAI account contact that your Trusted Access for Cyber or GPT-5.5-Cyber provisioning is complete.

Do not send secrets, private keys, exploit targets, or confidential third-party data unless OpenAI specifically instructs you to do so through an approved support path.

## Contacting Support

If you still cannot complete verification, access GPT-5.5-Cyber, or resolve a cyber safety message after working through the steps above, contact Support and include as much of the following as you can:

* Your organization name.
* The OpenAI organization ID used for the request.
* Whether you are using ChatGPT, Codex, or the API.
* The approved access path you expected to use.
* The exact model name used in the API or Codex.
* The full error message or safety message.
* The request ID, timestamp, and time zone for API failures.
* A screenshot if the issue is UI visibility, verification flow behavior, or an account settings view.
* A brief redacted description of the cybersecurity task.
* Whether the task involves systems you own or are authorized to test.

# FAQ

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

## Does Trusted Access remove all cyber-related refusals?

No. Trusted Access can reduce certain system-level refusal friction for eligible defensive work, but model-level refusals and other usage-policy controls can still apply.

## What if `gpt-5.5-cyber-preview` returns a `cyber_policy` error?

Contact Support with the request ID, timestamp, model, product surface, exact error text, and a brief redacted description of the task so OpenAI can investigate.

## Why do I need to verify?

Trusted Access for Cyber is intended for vetted customers and users working on legitimate cybersecurity tasks. Verification helps OpenAI evaluate access requests responsibly. Depending on the access path, verification may happen through an organization-level intake or a user verification flow.

## How long does verification take?

The verification flow itself may be quick, but final access timing depends on the broader review and provisioning process.

## Can support change a verification result?

No. Support cannot manually override the result of a Trusted Access for Cyber verification decision.
