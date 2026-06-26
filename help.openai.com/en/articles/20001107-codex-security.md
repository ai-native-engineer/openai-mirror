<!-- source: https://help.openai.com/en/articles/20001107-codex-security -->

# Codex Security

Updated: 10 days ago

Codex Security is a research preview available for ChatGPT Enterprise, Edu, Business, and Pro users. It helps teams identify, validate, and remediate vulnerabilities in code. It is designed to work more like a security researcher than a traditional scanner: it reads code, runs tests, explores realistic attack paths, and proposes patches that teams can review in their normal workflow.

## Overview

Today, Codex Security connects directly to GitHub repositories. After you enable a repository, it builds a codebase-specific threat model, scans repository history, validates potential vulnerabilities in an isolated environment, and surfaces proposed fixes for human review.  
  
Codex Security is built around three stages: identification, validation, and remediation. During identification, it analyzes the repository and explores realistic attack paths. During validation, it attempts to reproduce each issue to confirm it is real. During remediation, it generates a concrete patch that teams can review and raise into a pull request.

## How Codex Security works

When Codex Security connects to a repository, it scans commits in reverse chronological order and builds a codebase-specific threat model. That model captures attacker entry points, trust boundaries, sensitive data, and high-impact code paths, which Codex uses to focus analysis on realistic attack scenarios. Teams can inspect and edit the threat model so it reflects their real deployment assumptions.  
  
Codex Security follows a closed-loop remediation workflow:

1. **Scan the repository:** Codex connects to your GitHub repository, analyzes the codebase, and builds a threat model from the repository and commit history.
2. **Discover vulnerabilities:** Using that threat model, Codex explores realistic code paths and identifies potential vulnerabilities.
3. **Validate in a sandbox:** Codex runs an automated validator in an isolated environment to reproduce the issue, capture execution details, and confirm exploitability before surfacing the finding.
4. **Generate a patch:** For validated vulnerabilities, Codex produces a minimal patch suggestion that addresses the root cause.
5. **Human review and pull request:** The patch does not automatically modify your code. It is surfaced for human review and can be turned into a pull request for your normal workflow.
6. **Revalidate after remediation:** After a confirmed issue is patched and merged, Codex can revalidate the fix, closing the loop from detection to remediation.

For each finding, Codex Security can produce attack-path analysis that shows how attacker-controlled input could move from an entry point to a sensitive outcome. It scores that path by likelihood and impact and makes the underlying assumptions visible, which helps teams prioritize realistic risks over isolated alerts.  
  
Before surfacing a finding, Codex Security attempts to reproduce it in an isolated environment. The validator records reproduction results, execution details, and proof-of-concept artifacts so teams can focus on findings that have actually been shown to work.  
  
For validated findings, Codex Security proposes a minimal patch that addresses the root cause. It does not automatically modify your code. Instead, the patch is surfaced for human review and can be turned into a pull request in your existing workflow.

## Get started

1. Go to [Codex Security](https://chatgpt.com/codex/cloud/security).
2. Connect and enable the GitHub repositories you want Codex Security to scan.
3. Wait for the initial scan to finish. Codex Security first builds a threat model for the project and scans repository history for existing vulnerabilities. This can take longer for large projects. Scans of new code are faster.
4. Review findings, validation details, and proposed patches.

## Role-based access controls (RBAC)

For Enterprise and Edu workspaces, admins can manage Codex Security access in workspace permissions. Codex Security requires both Codex Cloud and Codex Security access to be enabled for the workspace. Access can also be limited to specific roles or groups through RBAC, including SCIM-synced groups. To let members manage Codex Security scan configurations, also enable the Codex Security admin permission for the appropriate role or group.  
  
To update your workspace’s permissions:

1. In ChatGPT, select your profile icon, then select **Workspace Settings** > **Permissions** to open [workspace permissions](https://chatgpt.com/admin/permissions).
2. Scroll down to **Codex Cloud**.
3. Make sure Codex Cloud access is enabled.
4. Enable or disable access by toggling **Allow members to use Codex Security.**
5. If the role or group should manage scan configurations, also enable **Allow members to administer Codex Security.**

Learn more about [role-based access controls in your ChatGPT workspace](/en/articles/11750701-rbac).

## Best practices

* Start with a small set of repositories and a dedicated group of reviewers. We recommend a focused rollout at first, especially while onboarding and vulnerability sharing are still relatively manual.
* Refine the threat model as you learn. Small updates to the model can improve context and make findings more precise over time.
* If you do not use GitHub Cloud today, consider starting with lower-risk or non-production repositories for evaluation. That can help teams build confidence in the workflow before wider adoption.
* Review generated patch PRs with your normal review process. We also recommend using Codex Code Review on Codex Security PRs so remediation does not introduce regressions.

## FAQ

### Does Codex Security automatically change my code?

No. Codex Security proposes a patch for human review. That proposal can be turned into a pull request, but it does not automatically modify your code.

### Does Codex Security rely on fuzzing or signature-based scanning?

No. Codex Security is using language-model reasoning, test-time compute, tool use, and large context, rather than fuzzing or signature-based scanning.

### Can I inspect or edit the threat model?

Yes. The threat model is visible and editable, so teams can inspect how Codex Security understands the application and update assumptions to match their environment.

### What does validation mean?

Validation is the step where Codex Security tries to reproduce a potential vulnerability in an isolated environment before surfacing it. This is meant to reduce false positives and keep findings high-signal.

### What happens after a finding is validated?

After validation, Codex Security proposes a patch that addresses the root cause and can be turned into a pull request for review.
