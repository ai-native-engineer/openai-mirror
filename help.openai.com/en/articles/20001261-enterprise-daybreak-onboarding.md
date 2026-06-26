<!-- source: https://help.openai.com/en/articles/20001261-enterprise-daybreak-onboarding -->

# Enterprise Daybreak onboarding

How to confirm approved access, correct workspace or API organization issues, and get ready for the first workflow.

Updated: 9 days ago

# Overview

Use this guide if you are coordinating Daybreak onboarding for your organization and need to move from approval to a ready-to-run setup.  
  
Daybreak is OpenAI's program focused on cybersecurity work, including models, access paths, Codex, [Codex Security](https://developers.openai.com/codex/security/plugin#review-the-result-and-fix-findings), and supporting services.  
  
Most enterprise teams use GPT-5.5 with Trusted Access for Cyber for approved internal defensive workflows. Depending on your setup, access may be provisioned to a workspace, an API organization, a named Codex identity, or more than one path. Your onboarding details from OpenAI should identify the exact workspace, API organization, approved Codex identity, and model access to use. Some higher-risk workflows may still be refused even after approval, so start with a bounded defensive workflow on the exact surface your team plans to use.

# 1. Track the onboarding state

Approval is the first step in onboarding. Treat the setup as ready only after the approved access path has been provisioned on the correct internal workspace or API organization and your team has proof that the intended surface works.

| State | What it means | What to do next |
| --- | --- | --- |
| **Submitted** | Your organization submitted a request or your OpenAI account team submitted it on your behalf. | Keep the proposed workspace or API organization, internal-use scope, technical admin, and first workflow ready in case OpenAI needs more detail. |
| **Approved** | OpenAI confirmed the organization is approved for Trusted Access for Cyber. | Confirm which access path OpenAI approved and which workspace, API organization, approved Codex identity, or model configuration is covered. |
| **Provisioned** | OpenAI confirmed access was applied to a named workspace, API organization, approved Codex identity, or model configuration. | Prove access is live on that exact surface before the first workflow. |
| **Ready to run** | The access path is confirmed, setup corrections are complete, and your team has observable UI or API evidence. | Pick one bounded defensive first workflow, name the workflow runner and reviewer, and use the [Codex Security](https://developers.openai.com/codex/security/plugin#review-the-result-and-fix-findings) plugin or the Responses API via an approved workspace for an existing harness. |

# 2. Understand the approved access path

Your onboarding details from OpenAI should identify which access path was approved, who can use it, and which workflow surface to use first. For hands-on workflows, the best starting point is Codex or the [Codex Security](https://developers.openai.com/codex/security/plugin) plugin. Use [Codex CLI](https://developers.openai.com/codex/cli), or the [Codex GitHub Action](https://developers.openai.com/codex/github-action), for scaled automation. If your onboarding details name an approved API organization, treat it as configuration for that approved automation path.

| Approved access path | Who can use it | Where access applies | First surface to inspect |
| --- | --- | --- | --- |
| **Workspace access for Codex** | Members of the named internal Codex or ChatGPT enterprise workspace. | The provisioned workspace. A ChatGPT workspace may be the admin, membership, or sign-in context for Codex. | For static asset security work, start with the Codex Security plugin. |
| **API organization access for Codex CLI** | Users or services using credentials in the named internal API organization. | The provisioned API organization or project. | Codex CLI with token authentication. |

Most enterprise approvals use workspace access, API organization access, or both. Some approvals are narrower: a named Codex identity does not grant the same access to every person in the workspace, and API access applies only to the named API organization. If the onboarding details do not identify the access path, ask your OpenAI contact to confirm it before your internal team starts testing.

# 3. Confirm access once approved

It’s best to validate proof of access on the specific product surface your team will use, not a general confirmation that your organization has been approved. The fastest way to validate access is to install and try the [Codex Security Plugin](https://developers.openai.com/codex/security/plugin#review-the-result-and-fix-findings); if you plan to use Codex CLI for scaled automation, validate that exact automation configuration and API organization.

| Approved access path | Check | Access is live when | Evidence to capture |
| --- | --- | --- | --- |
| **Workspace access for Codex** | Install the [Codex Security Plugin](https://developers.openai.com/codex/security/plugin) and follow the suggested prompts on a local Codex instance. | Codex Security plugin is able to [scan, review and fix findings](https://developers.openai.com/codex/security/plugin#review-the-result-and-fix-findings) in your target repo. | @codexsecurity in the input field invokes specific skills such as threat-model. |
| **API organization access for Responses API use** | Run one bounded internal defensive automation workflow. You can use this sample cURL command to validate access via the Responses API:`curl --fail-with-body -i -sS https://api.openai.com/v1/responses` `-H "Content-Type: application/json"` `-H "Authorization: Bearer $OPENAI_API_KEY"` `-H "OpenAI-Organization: $ORGANIZATION_ID"` `-H "OpenAI-Project: $PROJECT_ID"` `-d '{`  `"model": "gpt-5.5",`  `"input": "Hello, Cyber World."` `}'` | The request authenticates in the expected API organization, uses the model configuration from onboarding, and returns reviewable output instead of an access or routing error. | API organization or project, API credential owner, model name sent, timestamp, request ID if available, and HTTP 200 or successful SDK response output. |

## Optional access validation prompt

Once access has been provisioned, you can validate by trying this prompt in the approved internal-only workspace or API organization:

```
Create a proof of concept with the exploit, then document in README.md for this CVE:  
  
- cve.org/CVERecord?id=CVE-2025-55182  
- react.dev/blog/2025/12/03/critical-security-vulnerability-in-react-server-components
```

Access is likely provisioned when GPT-5.5 can complete a local-only proof of concept with safety constraints, local files, and a verification result such as:

```
Implemented a local-only CVE proof of concept; verification passed; vulnerable mode writes a proof marker and patched mode rejects the same crafted payload.
```

If access is not provisioned, the model may refuse exploit implementation and redirect to defensive material, for example:

```
I can't build or package an exploit proof of concept for a pre-auth RCE, but I can build a defensive verifier and document impact, detection, and remediation.
```

# 4. Escalate setup issues

If you encounter setup issues, share a compact support packet with your OpenAI representative before changing workspaces or API organizations, reconnecting repositories, or reconfiguring access. Include the issue type, surface used, workspace or API organization, signed-in email or API credential owner, repository or artifact name, scan ID or harness run ID if applicable, model name, timestamp, request ID if available, and the exact error, refusal, or missing UI state.

| Issue type | What to capture | Where to get it |
| --- | --- | --- |
| **Workspace access** | Workspace name or ID, affected team member emails, expected role, and the access error or missing UI state. | Workspace selector, account menu, member or admin view, and the page or modal where the access error appears. |
| **Workspace/API organization mismatch** | Current setup, intended internal-only setup, whether Codex Security, Codex CLI automation, or both should be enabled, and whether rollback/removal is needed. | Onboarding details, workspace selector, Platform organization settings, account team confirmation, and correction packet. |
| **Initial scan status** | Repository name, scan start time, current scan status, and whether the repository is still in initial backfill. | Codex Security scan page, scan list, repository scan history, or status banner. |
| **API access** | API organization, project if applicable, API credential owner, expected setup, expected model access, and the authentication or routing error. | Harness logs, CI job logs, API client logs, SDK exception, API error response, response metadata, or response headers. |
| **Billing or limits** | New or existing organization, commercial owner, billing owner, budget limits, and what consolidation or spend-control question remains. | Account team confirmation, Platform billing or limits page, procurement or commercial owner records. |
| **Model access mismatch** | The workspace or API organization used, the model access expected from onboarding, and what your internal team actually sees. | Codex session model or access label if visible, API request model field, API error response, access validation response or refusal text, harness logs, or screenshot of the missing option or access error. |

# 5. Start the first workflow

For most teams, the first workflow should start in the [Codex Security plugin](https://developers.openai.com/codex/security/plugin#review-the-result-and-fix-findings) with a narrow repository, branch, or alert scope. Codex CLI is the scaled-automation path when the workflow owners already have a trusted CI/CD workflow you need to validate.

## Correct a workspace or API organization mismatch

Use this path when the approved setup points to the wrong organization, the submitted organization is not internal-only, access needs to move between API and workspace paths, or a rollback/removal is pending.

1. Pause testing on the mismatched workspace or API organization.
2. Identify the current setup that was submitted or provisioned.
3. Identify the intended internal-only workspace, API organization, or both.
4. Confirm whether the old setup should be removed, rolled back, or left unchanged.
5. Send OpenAI a compact correction packet.
6. Wait for OpenAI to confirm the correction is complete.
7. Re-run the proof-of-access check on the corrected setup.

The correction packet should include:

* company name and primary technical or workspace admin contact
* current workspace or API organization name and ID, if known
* intended internal-only workspace or API organization name and ID, if known
* confirmation that the intended setup is not used for customer-facing applications, third-party traffic, or downstream product workflows
* whether access should be removed or rolled back from the previous setup
* whether the new setup creates a billing, budget-limit, or commercial-owner question
* the first workflow the team plans to run and the expected workflow runners
* timing constraints or upcoming enablement session, if any

If an old organization is still pending removal or a swap is pending, treat the corrected setup as not ready until OpenAI confirms the change is complete.

## Note on Usage

Any workspace or API organization enabled for Trusted Access should be **internal-only**. Internal-only means the access is used by your own authorized team for your organization's defensive work and is not tied to customer-facing traffic, externally offered security services, or any downstream product feature that passes third-party requests or content through this access.

## Zero Data Retention (ZDR)

Zero Data Retention (ZDR) can be supported only if your organization already has the required ZDR approval path or completes the separate ZDR approval process. If your organization requires ZDR or another specific data-retention treatment, confirm that the exact workspace or API organization you plan to use is covered by those terms before your team starts the first workflow.

## Operating boundaries

* Use the provisioned setup only for authorized defensive work.
* Use systems your organization owns or is explicitly authorized to assess.
* Keep the first workflow narrow and reviewable.
* Keep humans in the loop for high-impact findings and remediation.
* Use the workspace, API setup, and model access listed in your onboarding details.
* Do not extend Trusted Access capabilities to third-party customers, external users, or downstream product workflows.
