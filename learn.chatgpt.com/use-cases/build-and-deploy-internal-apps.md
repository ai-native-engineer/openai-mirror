<!-- source: https://learn.chatgpt.com/use-cases/build-and-deploy-internal-apps -->

OverviewFeaturesConfigurationDevelopersSecurityAdministrationUse CasesResourcesDocs sectionUse Cases

ChatGPT use cases

![](/assets/OpenAI-black-wordmark.svg)

![Codex](/assets/OAI_Codex-Lockup_Fallback_Black.svg)

Codex use case

# Build and deploy internal apps

Turn a team workflow into a hosted internal app with Sites.

Difficulty **Intermediate**

Time horizon **30m**

Use Sites in ChatGPT to build, test, and deploy internal apps, with built-in storage and auth context.

## Best for

* Teams that want to turn recurring workflows into interactive apps.
* Apps that need lightweight structured persistence, file uploads, or workspace-oriented sharing.
* Internal tools that benefit from building, testing, deploying, and iterating in one chat.

# Contents

[← All use cases](/codex/use-cases) 

Copy page   [Export as PDF](/codex/use-cases/build-and-deploy-internal-apps/?export=pdf)

Use Sites in ChatGPT to build, test, and deploy internal apps, with built-in storage and auth context.

Intermediate

30m

Related links

[Sites documentation](/codex/sites)  [Sites showcase](/showcase/sites)

## Best for

* Teams that want to turn recurring workflows into interactive apps.
* Apps that need lightweight structured persistence, file uploads, or workspace-oriented sharing.
* Internal tools that benefit from building, testing, deploying, and iterating in one chat.

## Starter prompt

Build and deploy an internal app for [team or workflow].
Goal:
- [what the app should help people do]
- [who should use it]
- [source docs, data, or connected services ChatGPT should inspect]
Requirements:
- Keep the first version focused on one useful workflow.
- Use D1 for structured data persistence.
- Use R2 for user-uploaded files if needed.
- Test the main flow, persistence, and responsive layout before deploying.
Make it available to all workspace users.

Build and deploy an internal app for [team or workflow].
Goal:
- [what the app should help people do]
- [who should use it]
- [source docs, data, or connected services ChatGPT should inspect]
Requirements:
- Keep the first version focused on one useful workflow.
- Use D1 for structured data persistence.
- Use R2 for user-uploaded files if needed.
- Test the main flow, persistence, and responsive layout before deploying.
Make it available to all workspace users.

## Build and deploy from one chat

Sites is a managed hosting service in ChatGPT. Ask ChatGPT to create an app, and it can build the project, run it for testing, deploy it, and return a URL you can share.

The scope ranges from simple static sites to full-stack JavaScript or TypeScript web apps. That makes Sites a good fit for focused internal tools: onboarding dashboards, enablement hubs, searchable resource libraries, lightweight workflow apps, and reporting views.

See the [Sites documentation](/codex/sites) for setup, storage, deployment, and access guidance.

Start with one useful workflow. A clear first version is easier to review, deploy, and improve than a broad request to recreate an entire internal system.

## Give ChatGPT the workflow context

Tell ChatGPT who the app is for, what people should accomplish, which source material it should inspect, and what should persist between sessions. Be explicit about the intended sharing scope and ask ChatGPT to test the main flow before it deploys.

You can also leverage [Plugins](/codex/plugins) to fetch or refresh data from internal sources.

If you need live data fetching, you can connect to a 3rd party tool using an
API key. But if you want to use plugin connections, you can [schedule a task
from the current chat](/codex/automations#schedule-a-task-inside-a-chat) to
fetch data with plugins on a set schedule, update the app, and redeploy it.

## Choose storage deliberately

Many internal apps need persistence. Sites supports two storage primitives:

* Use D1, a SQLite-compatible database, for structured data such as checklist state, bookmarks, filters, annotations, configuration, and file metadata.
* Use R2 object storage for file bytes such as uploaded documents, images, or other assets that should persist.

Keep structured metadata in D1 and larger file objects in R2. A read-only resource page or static microsite may not need either one.

## Manage and share your projects

You can manage who can visit your deployed projects.

Keep a new project private while you review its content, data handling, and intended audience.

Depending on your account and workspace settings, you can share it with:

* People you invite.
* Everyone in your workspace.
* Anyone with the link.

Sharing lets people visit the project; it doesn’t let them edit it. To change access, open [Sites in ChatGPT](https://chatgpt.com/sites) or ask ChatGPT directly:

Change this site's access to everyone in my workspace.

## Examples

The [Sites showcase](/showcase/sites) includes sites examples with full prompts.

* **[Onboarding Hub](/showcase/onboarding-hub)** combines a first-week checklist, resources, notes, and uploaded documents. It uses D1 for user state and file metadata, and R2 for uploaded file bytes.
* **[Enablement Hub](/showcase/enablement-hub)** provides a searchable training library with filters and saved bookmarks backed by D1.
* **[Pulse Dashboard](/showcase/pulse-dashboard)** presents metrics, trends, and lineage details while using D1 for configuration and cached snapshots.
* **[Sparkboard](/showcase/idea-intake)** turns employee idea intake into a workflow with authenticated submissions, voting, comments, status boards, and contributor rankings.
* **[Launch Cal](/showcase/launch-cal)** organizes upcoming product launches into a monthly calendar with filters, risk signals, checklists, and connected-source references.
* **[Event Planning Hub](/showcase/event-planning-hub)** combines event requests, approvals, templates, milestones, policy readiness, and connected planning resources.

Use those examples as starting points, then narrow the prompt around your team’s workflow and source material.

## Related use cases

[![](/codex/use-cases/deploy-app-or-website.webp)

### Deploy an app or website

Use Codex with Build Web Apps and Vercel to turn a repo, screenshot, design, or rough app...

Front-end  Integrations](/codex/use-cases/deploy-app-or-website)[![](/codex/use-cases/idea-to-proof-of-concept.webp)

### Get from idea to proof of concept

Use Codex with ImageGen to turn a rough idea into a visual direction, implement the smallest...

Front-end  Engineering](/codex/use-cases/idea-to-proof-of-concept)[![](/codex/use-cases/build-student-website.webp)

### Build a student website

Use Sites to scope, build, and test a simple website from student project content, design...

Front-end  Code](/codex/use-cases/build-student-website)
