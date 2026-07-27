<!-- source: https://learn.chatgpt.com/docs/cloud -->

OverviewFeaturesConfigurationDevelopersSecurityAdministrationUse CasesResourcesDocs sectionOverview

Codex cloud

# Run coding tasks in parallel cloud environments

Run tasks in isolated cloud environments, work in parallel, and start work from the web, GitHub, Linear, or Slack.

[Open Codex cloud  (opens in a new tab)](https://chatgpt.com/codex)

[Set up Codex cloud](#getting-started)

## What should we build?

Ask Codex to do anything in the cloud

Select environment

ChatsCode reviewsArchive

* Add CSV export to the analytics dashboard

  Today · acme/analytics-dashboard · codex/csv-export

  Archive
* Fix the checkout retry edge case

  Yesterday · harbor/payments-api · codex/retry-guard

  +31−1

  Archive
* Document the new authentication flow

  Jun 11 · northstar/developer-portal · codex/auth-docs

  Merged+24−8

  Archive
* Add keyboard navigation to settings

  Jun 10 · evergreen/design-system · codex/keyboard-nav

  Closed+7−4

  Archive

01

## Run work in parallel

Give longer tasks dedicated environments and let them continue while you work on something else.

02

## Reproduce the environment

Configure the dependencies, tools, variables, and setup steps each repository needs.

03

## Review before you merge

Inspect the summary and diff, request a follow-up, or open a pull request when the result is ready.

Quickstart

## Set up Codex cloud

Connect GitHub, create an environment, and start your first cloud chat.

1. 1 

   ### Open Codex and sign in

   Go to [Codex](https://chatgpt.com/codex) and sign in with your ChatGPT account.
2. 2 

   ### Connect GitHub

   Connect your GitHub account when prompted, then choose the repositories
   that Codex can access.
3. 3 

   ### Create an environment

   Open [environment settings](https://chatgpt.com/codex/settings/environments) and create an environment for your repository. Configure any dependencies,
   tools, environment variables, or secrets the task needs.

   For configuration details, see [Cloud environments](/codex/environments/cloud-environment).
4. 4 

   ### Start your first task

   Return to [Codex](https://chatgpt.com/codex), choose your environment, and describe the result you want. You can
   watch the task logs or let the task run in the background.
5. 5 

   ### Review the result

   Review the summary and diff. Ask Codex to make follow-up changes, or open
   a pull request when the work is ready.

## See what Codex cloud can do

Give each task the environment it needs, then review the result on your schedule.

01

### Delegate several tasks

Start work in parallel and return as each task reaches a reviewable result.

[Learn more](/codex/environments/cloud-environment)

ChatsCode reviewsSecurity reviewsArchive

Last 7 days

Fix broken link in documentation

Jul 7 · acme/developer-portal

Merged+1−1

Add tooltips for input and output modalities

Jul 7 · northstar/design-system

Merged+31−16

Older

Analyze survey data for product pain points

May 18 · evergreen/product-research

Cancelled

02

### Build a reproducible environment

Configure the dependencies, tools, variables, and setup steps a repository needs.

[Learn more](/codex/environments/cloud-environment)

#### Environments

Search environments

Create environment

NameRepoNumber of chatsSharingCreatorCreated at

developer-docsacme/developer-portal128Workspacemia@acme.exampleJune 24, 2026

ui-componentsnorthstar/design-system64Workspaceleo@northstar.exampleJune 10, 2026

product-insightsevergreen/product-research27Workspacesam@evergreen.exampleMay 18, 2026

payments-stagingharbor/payments-api312Workspaceava@harbor.exampleApril 30, 2026

03

### Delegate from your integrations

Start work in Codex cloud from GitHub pull requests, Linear issues, or Slack channels and threads.

[Learn more](/codex/developers)

#### GitHub

Pull requests and issues

#### Linear

Issues and comments

#### Slack

Channels and threads

## Use Codex cloud when…

### Work needs to run in the background

Delegate a longer task and return when it is ready.

### You want to compare several attempts

Run tasks in parallel without tying up your local machine.

### Work starts in GitHub, Linear, or Slack

Use integrations to hand off work without leaving the pull request, issue, channel, or thread.

### You are away from your development machine

Start and review work from the web or Codex CLI.
