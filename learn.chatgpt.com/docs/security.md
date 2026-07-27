<!-- source: https://learn.chatgpt.com/docs/security -->

OverviewFeaturesConfigurationDevelopersSecurityAdministrationUse CasesResourcesDocs sectionSecurity

[Install plugin in ChatGPT](https://chatgpt.com/plugins/share/676aca3811d54fa7bcdef5255236b3c4)

For a prescriptive first local scan, start with the [Codex Security plugin
quickstart](/codex/security/plugin).

### Explore plugin use cases

* [Run a security scan](/codex/security/plugin/scans) for a repository or one scoped folder.
* [Run a deep security scan](/codex/security/plugin/deep-scans) when you need a more comprehensive scan and can wait longer for it to finish.
* [Review code changes](/codex/security/plugin/code-changes) before you merge a pull request or branch.
* [Triage a backlog](/codex/security/plugin/triage-backlog) when you have existing security findings to review.
* [Fix and verify findings](/codex/security/plugin/fix-findings) with bounded patches for approved findings.
* [Export or track findings](/codex/security/plugin/export-findings) as portable artifacts or approval-gated tracking destinations.
* [Write vulnerability reports](/codex/security/plugin/vulnerability-reports) from supplied findings, disclosure notes, source, and PoCs.
* [Propose security hardening](/codex/security/plugin/security-hardening) from scan results or other security evidence.
* [See what’s new](/codex/security/plugin/changelog) in the Codex Security plugin.

The plugin runs in your Codex chat. Codex Security cloud scans connected
GitHub repositories through Codex cloud. For Codex sandboxing, approvals,
network controls, and admin settings, see [Agent approvals &
security](/codex/agent-approvals-security).

## Codex Security cloud

Codex Security cloud is currently in research preview. It scans connected
GitHub repositories for likely security issues.

It helps teams:

1. **Find likely vulnerabilities** by using a repo-specific threat model and real code context.
2. **Reduce noise** by validating findings before you review them.
3. **Move findings toward fixes** with ranked results, evidence, and suggested patch options.

## How Codex Security cloud works

Codex Security scans connected repositories commit by commit.
It builds scan context from your repo, checks likely vulnerabilities against that context, and validates high-signal issues in an isolated environment before surfacing them.

You get a workflow focused on:

* repo-specific context instead of generic signatures
* validation evidence that helps reduce false positives
* suggested fixes you can review in GitHub

## Codex Security cloud access and prerequisites

Codex Security cloud works with connected GitHub repositories through Codex
cloud. If a repository isn’t visible, confirm the repository is available in your
Codex cloud workspace or contact your OpenAI account team.

## Related docs

* [Codex Security plugin quickstart](/codex/security/plugin) walks through installation and a first local scan.
* [Codex Security cloud setup](/codex/security/setup) details setup, scanning, and findings review.
* [Improving the threat model](/codex/security/threat-model) explains how to tune scope, attack surface, and criticality assumptions.
* [Codex Security cloud FAQ](/codex/security/faq) covers common cloud product questions.
