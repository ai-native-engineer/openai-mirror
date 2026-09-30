<!-- source: https://help.openai.com/en/articles/20001545-using-codex-cloud -->

# Using Codex Cloud

Learn how Codex Cloud runs coding tasks, keeps task files, and works with your account and workspace.

Learn how Codex Cloud runs coding tasks, keeps task files, and works with your account and workspace.

Codex Cloud runs coding tasks on OpenAI-managed computers. Once an environment is prepared for your project, you can start and continue tasks from desktop, web, or mobile.

For plan availability and usage limits, see: [Using Codex with your ChatGPT plan](https://help.openai.com/articles/11369540). In a managed workspace, your administrator also controls Codex cloud access.

# Prepare an environment for your project

A cloud environment brings together the repositories, tools, dependencies, and access settings Codex needs for your project. A published environment lets you reuse that setup for new tasks.

Environments are created and published on desktop or web. Once an environment is ready, you can use it for tasks across supported devices.

For the complete walkthrough, see: [Set up and configure Codex Cloud](https://developers.openai.com/codex/environments/cloud-environments). The developer guide covers connecting repositories, preparing and testing the environment, adding credentials, configuring network access, and connecting private services.

# Run a task and review the results

Choose a published environment and describe what you want Codex to do. For example, you can ask it to investigate a bug, make a code change, or run the project’s tests. Each task starts from the prepared setup in its own isolated workspace, with separate working files and changes.

Cloud tasks can continue while your computer is asleep. After you create and publish an environment on desktop or web, you can select it for a mobile task and continue the same cloud task across supported devices. Remote access to a task running on your own computer is a separate workflow.

Review the changes and test results before using the work. If you need further changes, continue in the same task.

# Continue your work and update the setup

Return to the original task to continue unfinished work. Starting a new task creates a separate workspace and does not recover another task’s uncommitted changes. Commit important work to source control.

By default, saved virtual machine (VM) state is recoverable for up to 7 days after the last start of a turn or task resume. This recovery window describes saved VM state; it is not a conversation-history retention period.

Changes to an environment’s published setup apply to new tasks. Existing tasks keep their own state. If your project needs different tools, dependencies, or access settings, see: [Update a cloud environment](https://developers.openai.com/codex/environments/cloud-environments).

# FAQ

## Why can’t I see or use the cloud controls?

Check that you’re signed in to the intended account and workspace. Availability depends on your plan and workspace settings. In a managed workspace, ask an administrator to check your cloud access and the permissions needed for the action you’re trying to take. Being an owner or admin does not by itself make every feature available on your plan.

## Why is GitHub connected but my task can’t access or push to a repository?

Confirm that the connected GitHub account has access to the repository and that the environment includes it. Each person uses their own GitHub connection. Access to an environment does not replace repository permissions or the task’s Git setup.

Identify whether the failure happens when selecting a repository, preparing the environment, fetching code, or pushing changes. For repository setup and connection requirements, see: [Connect repositories for Codex Cloud](https://developers.openai.com/codex/environments/cloud-environments). If the issue continues, include the failing step when contacting Support.

## What should I do if a task or its files are unavailable?

Check that you’re opening the original task. If you still can’t access the work, [contact Support](https://help.openai.com/articles/6614161) with the task link or ID if available. Include when you last accessed the work and what is missing.

## What does sharing an environment share?

In ChatGPT Enterprise, sharing an environment makes its prepared setup available to authorized workspace members. It does not give them access to another person’s task or automatically give them permission to edit the environment.

Prepared files and environment-owned credentials or connections can give teammates access to shared resources. Personal vault values are not copied to teammates. Before sharing, review which files, credentials, and connections teammates can use: [Share an environment in Enterprise](https://developers.openai.com/codex/environments/cloud-environments).

## What happens to the previous Codex cloud experience?

Code Review, Security Review, and the existing Linear and GitHub integration workflows continue to use Codex Cloud (Legacy) during the transition.

Supported legacy environments can be migrated to the new experience. Migration is something you initiate; it leaves the original environment unchanged, and existing legacy task history remains viewable. For environment setup and configuration, see: [Codex Cloud developer guide](https://developers.openai.com/codex/environments/cloud-environments).

# Data restrictions

Codex in the cloud is not covered by the OpenAI BAA. Do not use it to process protected health information (PHI). For details, see: [HIPAA eligible products and functionality](https://help.openai.com/articles/20001069).
