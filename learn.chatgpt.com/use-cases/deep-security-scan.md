<!-- source: https://learn.chatgpt.com/use-cases/deep-security-scan -->

OverviewFeaturesConfigurationDevelopersSecurityAdministrationUse CasesResourcesDocs sectionUse Cases

ChatGPT use cases

![](/assets/OpenAI-black-wordmark.svg)

![Codex](/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex use case

# Run a deep security scan

Search an authorized repository deeply for plausible vulnerabilities.

Difficulty **Advanced**

Time horizon **Long-running**

Use the Codex Security plugin to run a more comprehensive audit of a repository or scoped folder that repeats discovery, validates candidates, and produces reviewable coverage, detailed finding reports, and structural hardening guidance.

## Best for

* Application security reviews of a repository or component that you own or are authorized to assess.
* More comprehensive reviews where additional runtime and token use are appropriate for finding more candidate issues.
* Security teams that need traceable finding evidence before deciding what to remediate.

# Contents

[← All use cases](/codex/use-cases) 

Copy page   [Export as PDF](/codex/use-cases/deep-security-scan/?export=pdf)

Use the Codex Security plugin to run a more comprehensive audit of a repository or scoped folder that repeats discovery, validates candidates, and produces reviewable coverage, detailed finding reports, and structural hardening guidance.

Advanced

Long-running

Related links

[Deep-scan guide](/codex/security/plugin/deep-scans)  [Agent approvals and security](/codex/agent-approvals-security)  [Codex cyber safety](/codex/cyber-safety)

## Best for

* Application security reviews of a repository or component that you own or are authorized to assess.
* More comprehensive reviews where additional runtime and token use are appropriate for finding more candidate issues.
* Security teams that need traceable finding evidence before deciding what to remediate.

## Skills & Plugins

* [Codex Security:deep Security Scan](/codex/security/plugin/deep-scans)

  Run repeated discovery passes over a repository or scoped folder, validate surviving findings, analyze attack paths, and generate detailed reports and structural hardening guidance.

| Skill | Why use it |
| --- | --- |
| [Codex Security:deep Security Scan](/codex/security/plugin/deep-scans) | Run repeated discovery passes over a repository or scoped folder, validate surviving findings, analyze attack paths, and generate detailed reports and structural hardening guidance. |

## Starter prompt

Use $codex-security:deep-security-scan to run a deep security scan on [this repository / absolute path to a scoped folder].
Scope and rules:
- I am authorized to assess this repository.
- Keep the scan within [the entire repository / the exact folder named above].
- Use the Codex Security plugin's deep-scan workflow; do not reinterpret this as a pull request or diff review.
Return the scan directory and report.md path. Summarize the findings, reviewed surfaces, structural hardening guidance, and proof gaps that require human review first.

Use $codex-security:deep-security-scan to run a deep security scan on [this repository / absolute path to a scoped folder].
Scope and rules:
- I am authorized to assess this repository.
- Keep the scan within [the entire repository / the exact folder named above].
- Use the Codex Security plugin's deep-scan workflow; do not reinterpret this as a pull request or diff review.
Return the scan directory and report.md path. Summarize the findings, reviewed surfaces, structural hardening guidance, and proof gaps that require human review first.

## Choose a deep repository review

Use a deep scan when you need a more comprehensive vulnerability review across
a repository or explicit folder and can budget for a longer run. The Codex
Security plugin repeats discovery passes before validating and prioritizing
findings, so this workflow takes more time and resources than an ordinary scan.

A deep scan can review an entire repository or one explicitly named package or
directory. To review a pull request, commit, branch diff, or working-tree patch,
use
[$codex-security:security-diff-scan](/codex/use-cases/scan-code-changes-for-security).

## Prepare an authorized scan

1. Open the repository in Codex and complete the [Codex Security plugin quickstart](/codex/security/plugin).
2. Confirm that you own the repository or have authorization to assess it.
3. Add architecture, trust-boundary, security-invariant, finding-criteria,
   exclusion, and severity guidance in `SECURITY.md`. Use nested `SECURITY.md`
   files for directory-specific policy.
4. Keep supported build, test, and validation commands and other repository
   instructions in `AGENTS.md`.
5. Run the starter prompt and let the scan complete its repeated discovery,
   validation, attack-path analysis, per-finding reporting, structural
   hardening, and final reporting stages.
6. Review the findings workspace, detailed reports, hardening portfolio, and
   any proof gaps before asking Codex to change code or reproduce a finding
   further.

## Review evidence before remediation

The final result should identify affected locations, why the behavior is
reachable, what validation Codex performed, any remaining proof gaps, and a
bounded remediation direction. Distinguish findings without validation evidence
from validated findings.

Start remediation only for a finding you have selected and reviewed. Use
[Remediate a vulnerability backlog](/codex/use-cases/remediate-vulnerability-backlog)
to fix findings one at a time with focused regression validation.

For setup, preflight, scoped targets, and runtime expectations, see [Run a deep
security scan](/codex/security/plugin/deep-scans).

## Related use cases

[![](/codex/use-cases/scan-code-changes-for-security.webp)

### Scan code changes for security

Use the Codex Security plugin to examine a Git-backed change set, validate plausible...

Engineering  Quality](/codex/use-cases/scan-code-changes-for-security)[![](/codex/use-cases/dependency-incident-audits.webp)

### Audit dependency incidents

Use Codex to turn a public package or supply chain advisory into a read-only audit, then...

Engineering  Quality](/codex/use-cases/dependency-incident-audits)[![](/codex/use-cases/remediate-vulnerability-backlog.webp)

### Remediate a vulnerability backlog

Bring in approved findings from ticketing tools or vulnerability reporting systems, then use...

Engineering  Quality](/codex/use-cases/remediate-vulnerability-backlog)
