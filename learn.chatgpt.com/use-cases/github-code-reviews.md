<!-- source: https://learn.chatgpt.com/use-cases/github-code-reviews -->

OverviewFeaturesConfigurationDevelopersSecurityAdministrationUse CasesResourcesDocs sectionUse Cases

ChatGPT use cases

![](/assets/OpenAI-black-wordmark.svg)

![Codex](/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex use case

# Review GitHub pull requests

Catch regressions and potential issues before human review.

Difficulty **Easy**

Time horizon **5s**

Use Codex code review in GitHub to automatically surface regressions, missing tests, and documentation issues directly on a pull request.

## Best for

* Teams that want another review signal before human merge approval
* Large codebases for projects in production

# Contents

[← All use cases](/codex/use-cases) 

Copy page   [Export as PDF](/codex/use-cases/github-code-reviews/?export=pdf)

Use Codex code review in GitHub to automatically surface regressions, missing tests, and documentation issues directly on a pull request.

Easy

5s

Related links

[Codex code review in GitHub](/codex/third-party/github)  [Custom instructions with AGENTS.md](/codex/agent-configuration/agents-md)

## Best for

* Teams that want another review signal before human merge approval
* Large codebases for projects in production

## Skills & Plugins

* [Security Best Practices](https://github.com/openai/skills/tree/main/skills/.curated/security-best-practices)

  Focus the review on risky surfaces such as secrets, auth, and dependency changes.

| Skill | Why use it |
| --- | --- |
| [Security Best Practices](https://github.com/openai/skills/tree/main/skills/.curated/security-best-practices) | Focus the review on risky surfaces such as secrets, auth, and dependency changes. |

## Starter prompt

@codex review for security regressions, missing tests, and risky behavior changes.

@codex review for security regressions, missing tests, and risky behavior changes.

## How to use

Start by adding Codex code review to your GitHub organization or repository.
See [Codex code review in GitHub](/codex/third-party/github) for more details.

You can set up Codex to automatically review every pull request, or you can request a review with `@codex review` in a pull request comment.

If Codex flags a regression or potential issue, you can ask it to fix it by commenting on the pull request with a follow-up prompt like `@codex fix it`.

This will start a new cloud chat that will fix the issue and update the pull request.

## Define review guidance

To customize what Codex reviews, add a `## Code Review Rules` section to the
`AGENTS.md` closest to the code the rules govern. For example:

```
## Code Review Rules

### Experiment cohorts

- Do not filter treatment comparisons on post-exposure behavior, including conversion or retention.
  Safe path: build cohorts from assignment or exposure; report conversion as an outcome.
```

Put repository-wide rules in the root `AGENTS.md` and service-specific rules
in a nested file. Keep rules concise, describe the behavior to flag and any
safe path or exception, and leave formatting and lint checks in CI. See
[Customize what Codex reviews](/codex/third-party/github#customize-what-codex-reviews)
for setup and rule-writing guidance.

## Related use cases

[![](/codex/use-cases/chatgpt-apps.webp)

### Bring your app to ChatGPT

Build one narrow ChatGPT app outcome end to end: define the tools, scaffold the MCP server...

Integrations  Code](/codex/use-cases/chatgpt-apps)[![](/codex/use-cases/build-unit-plan-from-sources.webp)

### Build a unit plan from source files

Use ChatGPT with standards, curriculum guidance, prior lesson files, a school calendar...

Integrations  Knowledge Work](/codex/use-cases/build-unit-plan-from-sources)[![](/codex/use-cases/new-hire-onboarding.webp)

### Coordinate new-hire onboarding

Use ChatGPT to gather approved new-hire context, stage tracker updates, draft team-by-team...

Integrations  Data](/codex/use-cases/new-hire-onboarding)
