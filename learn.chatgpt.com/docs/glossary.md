<!-- source: https://learn.chatgpt.com/docs/glossary -->

OverviewFeaturesConfigurationDevelopersSecurityAdministrationUse CasesResourcesDocs sectionOverview

Use this glossary as a quick reference for Codex terms across the app, CLI, IDE extension, cloud, SDK, and related integrations.

| Term | Definition | Applies to |
| --- | --- | --- |
| [Action](/codex/agent-approvals-security) | An operation performed by a person, ChatGPT, or Codex, such as editing a file, running a command, or using a connected service. | Desktop app, Web, Mobile, CLI, IDE extension, Cloud |
| [Agent](/codex) | The Codex agent that reasons over context, uses tools, and completes a task. | Desktop app, CLI, IDE extension, Cloud |
| [AGENTS.md](/codex/agent-configuration/agents-md) | Repository or user guidance file that gives Codex persistent instructions. | Desktop app, CLI, IDE extension, Cloud |
| [Analytics dashboard](/codex/enterprise/workspace-analytics) | Admin hub for ChatGPT workspace adoption and Codex-focused reporting. | Enterprise |
| [API key sign-in](/codex/auth#sign-in-with-an-api-key) | Authentication using an OpenAI API key. | Desktop app, CLI, IDE extension |
| [Approval policy](/codex/agent-approvals-security#sandbox-and-approvals) | Rules for when Codex must ask before taking an action. | Desktop app, CLI, IDE extension |
| [Approval request](/codex/agent-approvals-security#automatic-approval-reviews) | Codex asking to allow a restricted action. | Desktop app, CLI, IDE extension |
| [Apps (configuration)](/codex/plugins) | Codex configuration and app-server fields that store connector settings under the `apps` name. | Desktop app, CLI, IDE extension |
| [Appshot](/codex/appshots) | Snapshot of the frontmost app window sent to a ChatGPT or Codex chat. | Desktop app |
| [Auth cache](/codex/auth#login-caching) | Locally stored login credentials reused by Codex. | Desktop app, CLI, IDE extension |
| [Automatic approval review](/codex/agent-approvals-security#automatic-approval-reviews) | Model-based review of eligible approval requests before they proceed. | Desktop app, CLI, IDE extension |
| [Chat](/codex/projects#start-a-chat) | A saved space for exchanging messages with ChatGPT or Codex, including shared context, results, and actions. Quick chat starts a ChatGPT chat from Codex. | Desktop app, Web, Mobile, CLI, IDE extension, Cloud |
| [ChatGPT desktop app](/codex/app) | Desktop app with ChatGPT and Codex, including Chat and Work, projects, file previews, scheduled tasks, and developer tools. | Desktop |
| [ChatGPT sign-in](/codex/auth#sign-in-with-chatgpt) | Authentication using a ChatGPT account and workspace permissions. | Desktop app, CLI, IDE extension, Cloud |
| [ChatGPT Work](/codex/get-started-with-work) | The agent in ChatGPT for research, analysis, and creating documents, presentations, spreadsheets, and other finished work. | Desktop app, Web |
| [Chronicle](/codex/customization/chronicle) | Opt-in feature that builds memories from recent screen context. | Desktop app |
| [Cloud](/codex/cloud) | Mode where Codex works remotely in an OpenAI-managed environment. | Desktop app, IDE extension, Web |
| [Cloud chat](/codex/environments/cloud-environment#how-codex-cloud-tasks-run) | A Codex chat that runs remotely in a cloud environment. | Cloud |
| [Cloud environment](/codex/environments/cloud-environment) | Configured container setup used for Codex cloud chats. | Cloud |
| [Codex](/codex) | OpenAI's coding agent for software development tasks. | Desktop app, CLI, IDE extension, Web, Cloud, SDK |
| [Codex app-server](/codex/app-server) | Local JSON-RPC server for embedding Codex threads, turns, approvals, history, and streamed events in custom clients. | Desktop app, IDE extension, SDK |
| [Codex CLI](/codex/cli) | Terminal client for running Codex interactively or in scripts. | Terminal |
| [Codex cloud](/codex/cloud) | OpenAI-managed execution environment where Codex can work on repository tasks remotely. | Web, Desktop app, IDE extension |
| [codex exec](/codex/non-interactive-mode) | CLI command for running Codex non-interactively from scripts or CI. | CLI |
| [Codex IDE extension](/codex/ide) | Editor integration for using Codex inside IDEs like VS Code, JetBrains IDEs, Cursor, and Windsurf. | IDE |
| [Codex SDK](/codex/codex-sdk) | Programmatic interface for building Codex-powered workflows or integrations. | SDK |
| [Codex-managed worktree](/codex/environments/git-worktrees#codex-managed-and-permanent-worktrees) | A temporary worktree Codex creates and manages for a chat. | Desktop app |
| [Compaction](/codex/prompting#context) | Summarizing older context so long-running work can continue. | Desktop app, CLI, IDE extension, Cloud |
| [Compliance API](/codex/enterprise/compliance-api) | API for exporting supported ChatGPT workspace records and audit metadata. | Enterprise |
| [Computer Use](/codex/computer-use) | Desktop capability that lets ChatGPT interact with other applications through the UI. | Desktop app |
| [Computer Use in the browser](/codex/browser?surface=app#app-computer-use-in-the-browser) | Capability that lets ChatGPT operate the built-in browser directly. | Desktop app |
| [config.toml](/codex/config-file/config-reference#configtoml) | Local Codex configuration files. | Desktop app, CLI, IDE extension |
| [Connected host](/codex/remote-connections#what-comes-from-the-connected-host) | Computer or development environment that provides files, tools, and shell access for ChatGPT or Codex chats opened through Remote. | Desktop app, Mobile |
| [Connector](/codex/plugins) | A component of a plugin that connects ChatGPT or Codex to data and actions in an external service. | Desktop app (ChatGPT Work, Codex), Web (ChatGPT Work) |
| [Container cache](/codex/environments/cloud-environment#container-caching) | Saved cloud container state reused to speed up future cloud chats. | Cloud |
| [Context](/codex/prompting#context) | Information Codex can use while working, such as files, prior messages, tool output, and instructions. | Desktop app, CLI, IDE extension, Cloud, SDK |
| [Context window](/api/docs/guides/conversation-state#managing-the-context-window) | The maximum amount of information the model can consider at once. | Desktop app, CLI, IDE extension, Cloud, SDK |
| [Conversation](/codex/projects#start-a-chat) | The ongoing exchange of messages and shared context between a person and ChatGPT or Codex within a chat. | Desktop app, Web, Mobile, CLI, IDE extension, Cloud |
| [Custom agent](/codex/agent-configuration/subagents#custom-agents) | User-defined agent role with its own instructions and settings. | Desktop app, CLI |
| [Deny-read rule](/codex/permissions#deny-reads-with-exact-paths-or-globs) | Filesystem permission rule that prevents Codex from reading sensitive paths or glob matches. | Desktop app, CLI, IDE extension, Enterprise |
| [Diff](/codex/code-review?surface=app#app-what-changes-it-shows) | Set of Git file changes shown for inspection, comments, staging, or reverting. | Desktop app, Git, Review |
| [Domain allowlist](/codex/cloud/internet-access#domain-allowlist) | Set of domains Codex cloud can reach when agent internet access is enabled. | Cloud |
| [Environment (local)](/codex/environments/local-environment) | Desktop app configuration that tells Codex how to set up worktrees for a project. | Desktop app, Worktree |
| [Environment variable](/codex/environments/cloud-environment#environment-variables-and-secrets) | Runtime configuration value available during task execution. | Cloud, CLI, IDE extension |
| [Ephemeral session](/codex/non-interactive-mode#basic-usage) | Non-interactive run that skips saving session state after it completes. | CLI |
| [Fast mode](/codex/agent-configuration/speed#fast-mode) | Speed setting that makes supported models respond faster at a higher credit cost. | CLI, IDE extension |
| [Filesystem permission](/codex/permissions#filesystem-permissions) | Permission profile rule that grants or denies read and write access to paths. | Desktop app, CLI, IDE extension |
| [Finding](/codex/automations#managing-tasks) | A notable result or issue surfaced by a scheduled task. | Desktop app |
| [Full access](/codex/sandboxing#configure-defaults) | Mode where Codex runs without normal sandbox restrictions. | Desktop app, CLI, IDE extension |
| [Git worktree](/codex/environments/git-worktrees#whats-a-worktree) | A second checkout of the same repository for parallel branch work. | Desktop app, Git |
| [Handoff](/codex/environments/git-worktrees#working-between-local-and-worktree) | Moving a chat and its work between Local and Worktree. | Desktop app |
| [Heartbeat](/codex/automations#schedule-a-task-inside-a-chat) | A recurring scheduled task that returns ChatGPT to the same chat. | Desktop app |
| [Hook](/codex/hooks) | A lifecycle handler that runs when a Codex event matches, such as tool use, permission requests, or when a turn stops. | Desktop app, CLI, IDE extension |
| [Hook event](/codex/hooks#config-shape) | Lifecycle point where configured hook handlers can run. | Desktop app, CLI, IDE extension |
| [Hunk](/codex/code-review?surface=app#app-staging-and-reverting-files) | Contiguous section of a diff that can be staged, unstaged, or reverted independently. | Desktop app, Git, Review |
| [Inline comment](/codex/code-review?surface=app#app-inline-comments-for-feedback) | Line-specific feedback attached to a diff. | Desktop app |
| [Live web search](/codex/config-file/config-basic#web-search-mode) | Real-time web lookup for current information. | Desktop app, CLI, IDE extension |
| [Local](/codex/environments/git-worktrees#working-between-local-and-worktree) | Mode where Codex works on the user's computer. | Desktop app, CLI, IDE extension |
| [Local chat](/codex/environments/modes) | A ChatGPT or Codex chat that runs on the user's machine. | Desktop app, CLI, IDE extension |
| [Maintenance script](/codex/environments/cloud-environment#container-caching) | Optional script run when a cached cloud container resumes. | Cloud |
| [Managed configuration](/codex/enterprise/managed-configuration) | Organization-controlled Codex defaults and restrictions. | Enterprise |
| [MCP](/codex/extend/mcp) | Model Context Protocol, a standard for connecting Codex to external tools and context. | Desktop app, CLI, IDE extension |
| [MCP resource](/codex/extend/mcp#supported-mcp-features) | Readable context exposed by an MCP server for Codex to inspect. | Desktop app, CLI, IDE extension |
| [MCP server](/codex/extend/mcp#supported-mcp-features) | External tool or context provider exposed through MCP. | Desktop app, CLI, IDE extension |
| [MCP tool](/codex/extend/mcp#supported-mcp-features) | Action exposed by an MCP server that Codex can call during a task. | Desktop app, CLI, IDE extension |
| [MDM](/codex/enterprise/managed-configuration#macos-managed-preferences-mdm) | Mobile device management tooling for distributing device profiles and managed Codex settings. | Enterprise |
| [Memories](/codex/customization/memories) | Locally stored context Codex can reuse across sessions. | Desktop app, CLI, IDE extension |
| [Model](/codex/models) | The AI model Codex uses for reasoning and tool work. | Desktop app, CLI, IDE extension, Cloud, SDK |
| [Network access](/codex/agent-approvals-security#network-access) | Permission for commands or environments to reach the internet. | Desktop app, CLI, IDE extension, Cloud |
| [Network policy](/codex/agent-approvals-security#network-policy) | Domain-based allow and deny rules that constrain sandboxed outbound network traffic. | Desktop app, CLI, IDE extension |
| [Non-interactive mode](/codex/non-interactive-mode) | CLI mode for running Codex from scripts or CI. | CLI |
| [Output schema](/codex/non-interactive-mode#create-structured-outputs-with-a-schema) | JSON Schema passed to `codex exec` to constrain the final response. | CLI |
| [Permanent worktree](/codex/environments/git-worktrees#codex-managed-and-permanent-worktrees) | A long-lived worktree kept as its own project. | Desktop app |
| [Permission profile](/codex/permissions#define-and-select-a-profile) | Named least-privilege policy that combines filesystem and network rules for local command execution. | Desktop app, CLI, IDE extension |
| [Plan](/codex/learn/best-practices#plan-first-for-difficult-tasks) | Codex's proposed or tracked steps for completing a task. | Desktop app, CLI, IDE extension, Cloud |
| [Plugin](/codex/plugins) | An installable bundle of capabilities, such as skills, connectors, and tools, distributed through the universal directory shared by ChatGPT and Codex. | Desktop app (ChatGPT Work, Codex), Web (ChatGPT Work), CLI |
| [Plugin manifest](https://developers.openai.com/plugins/build/plugins#plugin-structure) | Plugin metadata file that identifies a plugin and points to bundled skills, connector mappings, MCP servers, hooks, and metadata. | Plugin authoring |
| [Prefix rule](/codex/agent-configuration/rules#understand-the-rules-language) | Command-rule pattern that allows, prompts for, or forbids matching command prefixes. | Desktop app, CLI, IDE extension, Enterprise |
| [Profile](/codex/config-file/config-advanced#profiles) | Named configuration preset for Codex. | CLI, IDE extension |
| [Progressive disclosure](/codex/build-skills) | Loading skill details only when needed to preserve context. | Desktop app, Web (ChatGPT Work), CLI, IDE extension |
| [Project](/codex/projects) | A group of related chats and shared sources, or a local folder used for file-based work. | Desktop app |
| [Prompt](/codex/prompting) | A question, instruction, or goal sent to ChatGPT or Codex. | Desktop app, CLI, IDE extension, Cloud, SDK |
| [Pull request review](/codex/code-review?surface=app#app-pull-request-reviews) | Codex review of changes or feedback on a pull request. | Desktop app, CLI, GitHub |
| [RBAC](/codex/enterprise/roles-and-workspace-permissions) | Role-based access control for workspace permissions. | Enterprise |
| [Read-only mode](/codex/sandboxing) | Mode where Codex can inspect but not modify without approval. | Desktop app, CLI, IDE extension |
| [Reasoning effort](/codex/config-file/config-basic#reasoning-effort) | Setting that controls how much reasoning budget a model uses. | Desktop app, CLI, IDE extension, SDK |
| [Remote connection](/codex/remote-connections) | Connection that lets you access ChatGPT or Codex chats on another device through a connected host. | Desktop app, Mobile |
| [requirements.toml](/codex/config-file/config-reference#requirementstoml) | Admin-enforced requirements file for managed Codex setups. | Enterprise |
| [Review pane](/codex/code-review?surface=app) | Desktop app view for inspecting diffs, comments, and Git changes. | Desktop app |
| [Rules](/codex/agent-configuration/rules) | Policies that allow, prompt for, or deny command prefixes or permission exceptions. | Desktop app, CLI, IDE extension |
| [Sandbox](/codex/sandboxing) | Enforced boundary limiting what Codex commands can access or modify. | Desktop app, CLI, IDE extension |
| [Sandbox mode](/codex/config-file/config-basic#sandbox-level) | Configuration that defines Codex's filesystem and network limits. | Desktop app, CLI, IDE extension |
| [Sandbox preset](/codex/codex-sdk#sandbox-presets) | SDK shorthand for common sandbox policies such as read-only, workspace-write, or full access. | SDK |
| [Schedule](/codex/automations) | The timing rule for a scheduled task. | Desktop app |
| [Scheduled run](/codex/automations#managing-tasks) | One execution of a scheduled task, including its status and any resulting findings. | Desktop app, Web |
| [Scheduled task](/codex/automations) | A prompt ChatGPT runs at a future time or on a recurring schedule, with its own settings and run history. | Desktop app, Web |
| [Scheduled task in a chat](/codex/automations#schedule-a-task-inside-a-chat) | A scheduled task that uses an existing chat's context and returns each run's results to that chat. | Desktop app, Web |
| [Secret](/codex/environments/cloud-environment#environment-variables-and-secrets) | Encrypted value available to setup scripts but removed before the agent phase. | Cloud |
| [Setup script](/codex/environments/local-environment#setup-scripts) | Script run before the agent starts to install dependencies or prepare tools. | Desktop app worktrees |
| [Skill](/codex/build-skills) | Reusable workflow package with instructions and optional scripts or references. | Desktop app, Web (ChatGPT Work), CLI, IDE extension |
| [Skill invocation](/codex/build-skills#how-codex-uses-skills) | Explicit or implicit activation of a skill. | Desktop app, Web (ChatGPT Work), CLI, IDE extension |
| [Slash command](/codex/developer-commands?surface=cli) | Command entered with a leading slash to control or inspect a Codex CLI session. | CLI |
| [Standalone scheduled task](/codex/automations) | Scheduled task whose runs each start a new chat and report findings in Triage. | Desktop app, Web |
| [Standalone task](/codex/projects) | A Codex task that isn't grouped within a project. | Desktop app, CLI, IDE extension, Cloud |
| [STDIO MCP server](/codex/extend/mcp#stdio-servers) | MCP server launched as a local process by a configured command and arguments. | CLI, IDE extension |
| [Streamable HTTP MCP server](/codex/extend/mcp#streamable-http-servers) | MCP server reached over HTTP, optionally with bearer token or OAuth authentication. | CLI, IDE extension |
| [Subagent](/codex/agent-configuration/subagents) | Specialized child agent spawned to work on part of a task. | Desktop app, CLI |
| [Subagent workflow](/codex/agent-configuration/subagents#core-terms) | Workflow where Codex runs delegated agents in parallel and combines their results. | Desktop app, CLI |
| [Task](/codex/projects) | A defined outcome ChatGPT or Codex works toward, such as fixing a bug, creating a document, or researching a topic. | Desktop app, Web, Mobile, CLI, IDE extension, Cloud |
| [Thread](/codex/app-server#threads) | A technical object in Codex app-server APIs that contains turns and stored conversation history. | App-server, SDK |
| [Thread fork](/codex/app-server#start-or-resume-a-thread) | New thread branched from the stored history of an existing thread. | App-server, SDK |
| [Turn](/codex/app-server#core-primitives) | One exchange in a chat, usually a user prompt plus the agent's response and actions. | Desktop app, CLI, IDE extension, Cloud, SDK |
| [Universal image](/codex/environments/cloud-environment#default-universal-image) | Default Codex cloud container image with common tools preinstalled. | Cloud |
| [Web search cache](/codex/config-file/config-basic#web-search-mode) | Pre-indexed search results Codex can use without live browsing. | Desktop app, CLI, IDE extension |
| [Worktree](/codex/environments/git-worktrees) | Mode where Codex isolates changes in a separate Git worktree. | Desktop app |
| [Writable roots](/codex/agent-approvals-security#protected-paths-in-writable-roots) | Directories Codex is allowed to modify. | Desktop app, CLI, IDE extension |

Term

[Action](/codex/agent-approvals-security)

Definition

An operation performed by a person, ChatGPT, or Codex, such as editing a file, running a command, or using a connected service.

Applies to

Desktop app, Web, Mobile, CLI, IDE extension, Cloud

Term

[Agent](/codex)

Definition

The Codex agent that reasons over context, uses tools, and completes a task.

Applies to

Desktop app, CLI, IDE extension, Cloud

Term

[AGENTS.md](/codex/agent-configuration/agents-md)

Definition

Repository or user guidance file that gives Codex persistent instructions.

Applies to

Desktop app, CLI, IDE extension, Cloud

Term

[Analytics dashboard](/codex/enterprise/workspace-analytics)

Definition

Admin hub for ChatGPT workspace adoption and Codex-focused reporting.

Applies to

Enterprise

Term

[API key sign-in](/codex/auth#sign-in-with-an-api-key)

Definition

Authentication using an OpenAI API key.

Applies to

Desktop app, CLI, IDE extension

Term

[Approval policy](/codex/agent-approvals-security#sandbox-and-approvals)

Definition

Rules for when Codex must ask before taking an action.

Applies to

Desktop app, CLI, IDE extension

Term

[Approval request](/codex/agent-approvals-security#automatic-approval-reviews)

Definition

Codex asking to allow a restricted action.

Applies to

Desktop app, CLI, IDE extension

Term

[Apps (configuration)](/codex/plugins)

Definition

Codex configuration and app-server fields that store connector settings under the `apps` name.

Applies to

Desktop app, CLI, IDE extension

Term

[Appshot](/codex/appshots)

Definition

Snapshot of the frontmost app window sent to a ChatGPT or Codex chat.

Applies to

Desktop app

Term

[Auth cache](/codex/auth#login-caching)

Definition

Locally stored login credentials reused by Codex.

Applies to

Desktop app, CLI, IDE extension

Term

[Automatic approval review](/codex/agent-approvals-security#automatic-approval-reviews)

Definition

Model-based review of eligible approval requests before they proceed.

Applies to

Desktop app, CLI, IDE extension

Term

[Chat](/codex/projects#start-a-chat)

Definition

A saved space for exchanging messages with ChatGPT or Codex, including shared context, results, and actions. Quick chat starts a ChatGPT chat from Codex.

Applies to

Desktop app, Web, Mobile, CLI, IDE extension, Cloud

Term

[ChatGPT desktop app](/codex/app)

Definition

Desktop app with ChatGPT and Codex, including Chat and Work, projects, file previews, scheduled tasks, and developer tools.

Applies to

Desktop

Term

[ChatGPT sign-in](/codex/auth#sign-in-with-chatgpt)

Definition

Authentication using a ChatGPT account and workspace permissions.

Applies to

Desktop app, CLI, IDE extension, Cloud

Term

[ChatGPT Work](/codex/get-started-with-work)

Definition

The agent in ChatGPT for research, analysis, and creating documents, presentations, spreadsheets, and other finished work.

Applies to

Desktop app, Web

Term

[Chronicle](/codex/customization/chronicle)

Definition

Opt-in feature that builds memories from recent screen context.

Applies to

Desktop app

Term

[Cloud](/codex/cloud)

Definition

Mode where Codex works remotely in an OpenAI-managed environment.

Applies to

Desktop app, IDE extension, Web

Term

[Cloud chat](/codex/environments/cloud-environment#how-codex-cloud-tasks-run)

Definition

A Codex chat that runs remotely in a cloud environment.

Applies to

Cloud

Term

[Cloud environment](/codex/environments/cloud-environment)

Definition

Configured container setup used for Codex cloud chats.

Applies to

Cloud

Term

[Codex](/codex)

Definition

OpenAI's coding agent for software development tasks.

Applies to

Desktop app, CLI, IDE extension, Web, Cloud, SDK

Term

[Codex app-server](/codex/app-server)

Definition

Local JSON-RPC server for embedding Codex threads, turns, approvals, history, and streamed events in custom clients.

Applies to

Desktop app, IDE extension, SDK

Term

[Codex CLI](/codex/cli)

Definition

Terminal client for running Codex interactively or in scripts.

Applies to

Terminal

Term

[Codex cloud](/codex/cloud)

Definition

OpenAI-managed execution environment where Codex can work on repository tasks remotely.

Applies to

Web, Desktop app, IDE extension

Term

[codex exec](/codex/non-interactive-mode)

Definition

CLI command for running Codex non-interactively from scripts or CI.

Applies to

CLI

Term

[Codex IDE extension](/codex/ide)

Definition

Editor integration for using Codex inside IDEs like VS Code, JetBrains IDEs, Cursor, and Windsurf.

Applies to

IDE

Term

[Codex SDK](/codex/codex-sdk)

Definition

Programmatic interface for building Codex-powered workflows or integrations.

Applies to

SDK

Term

[Codex-managed worktree](/codex/environments/git-worktrees#codex-managed-and-permanent-worktrees)

Definition

A temporary worktree Codex creates and manages for a chat.

Applies to

Desktop app

Term

[Compaction](/codex/prompting#context)

Definition

Summarizing older context so long-running work can continue.

Applies to

Desktop app, CLI, IDE extension, Cloud

Term

[Compliance API](/codex/enterprise/compliance-api)

Definition

API for exporting supported ChatGPT workspace records and audit metadata.

Applies to

Enterprise

Term

[Computer Use](/codex/computer-use)

Definition

Desktop capability that lets ChatGPT interact with other applications through the UI.

Applies to

Desktop app

Term

[Computer Use in the browser](/codex/browser?surface=app#app-computer-use-in-the-browser)

Definition

Capability that lets ChatGPT operate the built-in browser directly.

Applies to

Desktop app

Term

[config.toml](/codex/config-file/config-reference#configtoml)

Definition

Local Codex configuration files.

Applies to

Desktop app, CLI, IDE extension

Term

[Connected host](/codex/remote-connections#what-comes-from-the-connected-host)

Definition

Computer or development environment that provides files, tools, and shell access for ChatGPT or Codex chats opened through Remote.

Applies to

Desktop app, Mobile

Term

[Connector](/codex/plugins)

Definition

A component of a plugin that connects ChatGPT or Codex to data and actions in an external service.

Applies to

Desktop app (ChatGPT Work, Codex), Web (ChatGPT Work)

Term

[Container cache](/codex/environments/cloud-environment#container-caching)

Definition

Saved cloud container state reused to speed up future cloud chats.

Applies to

Cloud

Term

[Context](/codex/prompting#context)

Definition

Information Codex can use while working, such as files, prior messages, tool output, and instructions.

Applies to

Desktop app, CLI, IDE extension, Cloud, SDK

Term

[Context window](/api/docs/guides/conversation-state#managing-the-context-window)

Definition

The maximum amount of information the model can consider at once.

Applies to

Desktop app, CLI, IDE extension, Cloud, SDK

Term

[Conversation](/codex/projects#start-a-chat)

Definition

The ongoing exchange of messages and shared context between a person and ChatGPT or Codex within a chat.

Applies to

Desktop app, Web, Mobile, CLI, IDE extension, Cloud

Term

[Custom agent](/codex/agent-configuration/subagents#custom-agents)

Definition

User-defined agent role with its own instructions and settings.

Applies to

Desktop app, CLI

Term

[Deny-read rule](/codex/permissions#deny-reads-with-exact-paths-or-globs)

Definition

Filesystem permission rule that prevents Codex from reading sensitive paths or glob matches.

Applies to

Desktop app, CLI, IDE extension, Enterprise

Term

[Diff](/codex/code-review?surface=app#app-what-changes-it-shows)

Definition

Set of Git file changes shown for inspection, comments, staging, or reverting.

Applies to

Desktop app, Git, Review

Term

[Domain allowlist](/codex/cloud/internet-access#domain-allowlist)

Definition

Set of domains Codex cloud can reach when agent internet access is enabled.

Applies to

Cloud

Term

[Environment (local)](/codex/environments/local-environment)

Definition

Desktop app configuration that tells Codex how to set up worktrees for a project.

Applies to

Desktop app, Worktree

Term

[Environment variable](/codex/environments/cloud-environment#environment-variables-and-secrets)

Definition

Runtime configuration value available during task execution.

Applies to

Cloud, CLI, IDE extension

Term

[Ephemeral session](/codex/non-interactive-mode#basic-usage)

Definition

Non-interactive run that skips saving session state after it completes.

Applies to

CLI

Term

[Fast mode](/codex/agent-configuration/speed#fast-mode)

Definition

Speed setting that makes supported models respond faster at a higher credit cost.

Applies to

CLI, IDE extension

Term

[Filesystem permission](/codex/permissions#filesystem-permissions)

Definition

Permission profile rule that grants or denies read and write access to paths.

Applies to

Desktop app, CLI, IDE extension

Term

[Finding](/codex/automations#managing-tasks)

Definition

A notable result or issue surfaced by a scheduled task.

Applies to

Desktop app

Term

[Full access](/codex/sandboxing#configure-defaults)

Definition

Mode where Codex runs without normal sandbox restrictions.

Applies to

Desktop app, CLI, IDE extension

Term

[Git worktree](/codex/environments/git-worktrees#whats-a-worktree)

Definition

A second checkout of the same repository for parallel branch work.

Applies to

Desktop app, Git

Term

[Handoff](/codex/environments/git-worktrees#working-between-local-and-worktree)

Definition

Moving a chat and its work between Local and Worktree.

Applies to

Desktop app

Term

[Heartbeat](/codex/automations#schedule-a-task-inside-a-chat)

Definition

A recurring scheduled task that returns ChatGPT to the same chat.

Applies to

Desktop app

Term

[Hook](/codex/hooks)

Definition

A lifecycle handler that runs when a Codex event matches, such as tool use, permission requests, or when a turn stops.

Applies to

Desktop app, CLI, IDE extension

Term

[Hook event](/codex/hooks#config-shape)

Definition

Lifecycle point where configured hook handlers can run.

Applies to

Desktop app, CLI, IDE extension

Term

[Hunk](/codex/code-review?surface=app#app-staging-and-reverting-files)

Definition

Contiguous section of a diff that can be staged, unstaged, or reverted independently.

Applies to

Desktop app, Git, Review

Term

[Inline comment](/codex/code-review?surface=app#app-inline-comments-for-feedback)

Definition

Line-specific feedback attached to a diff.

Applies to

Desktop app

Term

[Live web search](/codex/config-file/config-basic#web-search-mode)

Definition

Real-time web lookup for current information.

Applies to

Desktop app, CLI, IDE extension

Term

[Local](/codex/environments/git-worktrees#working-between-local-and-worktree)

Definition

Mode where Codex works on the user's computer.

Applies to

Desktop app, CLI, IDE extension

Term

[Local chat](/codex/environments/modes)

Definition

A ChatGPT or Codex chat that runs on the user's machine.

Applies to

Desktop app, CLI, IDE extension

Term

[Maintenance script](/codex/environments/cloud-environment#container-caching)

Definition

Optional script run when a cached cloud container resumes.

Applies to

Cloud

Term

[Managed configuration](/codex/enterprise/managed-configuration)

Definition

Organization-controlled Codex defaults and restrictions.

Applies to

Enterprise

Term

[MCP](/codex/extend/mcp)

Definition

Model Context Protocol, a standard for connecting Codex to external tools and context.

Applies to

Desktop app, CLI, IDE extension

Term

[MCP resource](/codex/extend/mcp#supported-mcp-features)

Definition

Readable context exposed by an MCP server for Codex to inspect.

Applies to

Desktop app, CLI, IDE extension

Term

[MCP server](/codex/extend/mcp#supported-mcp-features)

Definition

External tool or context provider exposed through MCP.

Applies to

Desktop app, CLI, IDE extension

Term

[MCP tool](/codex/extend/mcp#supported-mcp-features)

Definition

Action exposed by an MCP server that Codex can call during a task.

Applies to

Desktop app, CLI, IDE extension

Term

[MDM](/codex/enterprise/managed-configuration#macos-managed-preferences-mdm)

Definition

Mobile device management tooling for distributing device profiles and managed Codex settings.

Applies to

Enterprise

Term

[Memories](/codex/customization/memories)

Definition

Locally stored context Codex can reuse across sessions.

Applies to

Desktop app, CLI, IDE extension

Term

[Model](/codex/models)

Definition

The AI model Codex uses for reasoning and tool work.

Applies to

Desktop app, CLI, IDE extension, Cloud, SDK

Term

[Network access](/codex/agent-approvals-security#network-access)

Definition

Permission for commands or environments to reach the internet.

Applies to

Desktop app, CLI, IDE extension, Cloud

Term

[Network policy](/codex/agent-approvals-security#network-policy)

Definition

Domain-based allow and deny rules that constrain sandboxed outbound network traffic.

Applies to

Desktop app, CLI, IDE extension

Term

[Non-interactive mode](/codex/non-interactive-mode)

Definition

CLI mode for running Codex from scripts or CI.

Applies to

CLI

Term

[Output schema](/codex/non-interactive-mode#create-structured-outputs-with-a-schema)

Definition

JSON Schema passed to `codex exec` to constrain the final response.

Applies to

CLI

Term

[Permanent worktree](/codex/environments/git-worktrees#codex-managed-and-permanent-worktrees)

Definition

A long-lived worktree kept as its own project.

Applies to

Desktop app

Term

[Permission profile](/codex/permissions#define-and-select-a-profile)

Definition

Named least-privilege policy that combines filesystem and network rules for local command execution.

Applies to

Desktop app, CLI, IDE extension

Term

[Plan](/codex/learn/best-practices#plan-first-for-difficult-tasks)

Definition

Codex's proposed or tracked steps for completing a task.

Applies to

Desktop app, CLI, IDE extension, Cloud

Term

[Plugin](/codex/plugins)

Definition

An installable bundle of capabilities, such as skills, connectors, and tools, distributed through the universal directory shared by ChatGPT and Codex.

Applies to

Desktop app (ChatGPT Work, Codex), Web (ChatGPT Work), CLI

Term

[Plugin manifest](https://developers.openai.com/plugins/build/plugins#plugin-structure)

Definition

Plugin metadata file that identifies a plugin and points to bundled skills, connector mappings, MCP servers, hooks, and metadata.

Applies to

Plugin authoring

Term

[Prefix rule](/codex/agent-configuration/rules#understand-the-rules-language)

Definition

Command-rule pattern that allows, prompts for, or forbids matching command prefixes.

Applies to

Desktop app, CLI, IDE extension, Enterprise

Term

[Profile](/codex/config-file/config-advanced#profiles)

Definition

Named configuration preset for Codex.

Applies to

CLI, IDE extension

Term

[Progressive disclosure](/codex/build-skills)

Definition

Loading skill details only when needed to preserve context.

Applies to

Desktop app, Web (ChatGPT Work), CLI, IDE extension

Term

[Project](/codex/projects)

Definition

A group of related chats and shared sources, or a local folder used for file-based work.

Applies to

Desktop app

Term

[Prompt](/codex/prompting)

Definition

A question, instruction, or goal sent to ChatGPT or Codex.

Applies to

Desktop app, CLI, IDE extension, Cloud, SDK

Term

[Pull request review](/codex/code-review?surface=app#app-pull-request-reviews)

Definition

Codex review of changes or feedback on a pull request.

Applies to

Desktop app, CLI, GitHub

Term

[RBAC](/codex/enterprise/roles-and-workspace-permissions)

Definition

Role-based access control for workspace permissions.

Applies to

Enterprise

Term

[Read-only mode](/codex/sandboxing)

Definition

Mode where Codex can inspect but not modify without approval.

Applies to

Desktop app, CLI, IDE extension

Term

[Reasoning effort](/codex/config-file/config-basic#reasoning-effort)

Definition

Setting that controls how much reasoning budget a model uses.

Applies to

Desktop app, CLI, IDE extension, SDK

Term

[Remote connection](/codex/remote-connections)

Definition

Connection that lets you access ChatGPT or Codex chats on another device through a connected host.

Applies to

Desktop app, Mobile

Term

[requirements.toml](/codex/config-file/config-reference#requirementstoml)

Definition

Admin-enforced requirements file for managed Codex setups.

Applies to

Enterprise

Term

[Review pane](/codex/code-review?surface=app)

Definition

Desktop app view for inspecting diffs, comments, and Git changes.

Applies to

Desktop app

Term

[Rules](/codex/agent-configuration/rules)

Definition

Policies that allow, prompt for, or deny command prefixes or permission exceptions.

Applies to

Desktop app, CLI, IDE extension

Term

[Sandbox](/codex/sandboxing)

Definition

Enforced boundary limiting what Codex commands can access or modify.

Applies to

Desktop app, CLI, IDE extension

Term

[Sandbox mode](/codex/config-file/config-basic#sandbox-level)

Definition

Configuration that defines Codex's filesystem and network limits.

Applies to

Desktop app, CLI, IDE extension

Term

[Sandbox preset](/codex/codex-sdk#sandbox-presets)

Definition

SDK shorthand for common sandbox policies such as read-only, workspace-write, or full access.

Applies to

SDK

Term

[Schedule](/codex/automations)

Definition

The timing rule for a scheduled task.

Applies to

Desktop app

Term

[Scheduled run](/codex/automations#managing-tasks)

Definition

One execution of a scheduled task, including its status and any resulting findings.

Applies to

Desktop app, Web

Term

[Scheduled task](/codex/automations)

Definition

A prompt ChatGPT runs at a future time or on a recurring schedule, with its own settings and run history.

Applies to

Desktop app, Web

Term

[Scheduled task in a chat](/codex/automations#schedule-a-task-inside-a-chat)

Definition

A scheduled task that uses an existing chat's context and returns each run's results to that chat.

Applies to

Desktop app, Web

Term

[Secret](/codex/environments/cloud-environment#environment-variables-and-secrets)

Definition

Encrypted value available to setup scripts but removed before the agent phase.

Applies to

Cloud

Term

[Setup script](/codex/environments/local-environment#setup-scripts)

Definition

Script run before the agent starts to install dependencies or prepare tools.

Applies to

Desktop app worktrees

Term

[Skill](/codex/build-skills)

Definition

Reusable workflow package with instructions and optional scripts or references.

Applies to

Desktop app, Web (ChatGPT Work), CLI, IDE extension

Term

[Skill invocation](/codex/build-skills#how-codex-uses-skills)

Definition

Explicit or implicit activation of a skill.

Applies to

Desktop app, Web (ChatGPT Work), CLI, IDE extension

Term

[Slash command](/codex/developer-commands?surface=cli)

Definition

Command entered with a leading slash to control or inspect a Codex CLI session.

Applies to

CLI

Term

[Standalone scheduled task](/codex/automations)

Definition

Scheduled task whose runs each start a new chat and report findings in Triage.

Applies to

Desktop app, Web

Term

[Standalone task](/codex/projects)

Definition

A Codex task that isn't grouped within a project.

Applies to

Desktop app, CLI, IDE extension, Cloud

Term

[STDIO MCP server](/codex/extend/mcp#stdio-servers)

Definition

MCP server launched as a local process by a configured command and arguments.

Applies to

CLI, IDE extension

Term

[Streamable HTTP MCP server](/codex/extend/mcp#streamable-http-servers)

Definition

MCP server reached over HTTP, optionally with bearer token or OAuth authentication.

Applies to

CLI, IDE extension

Term

[Subagent](/codex/agent-configuration/subagents)

Definition

Specialized child agent spawned to work on part of a task.

Applies to

Desktop app, CLI

Term

[Subagent workflow](/codex/agent-configuration/subagents#core-terms)

Definition

Workflow where Codex runs delegated agents in parallel and combines their results.

Applies to

Desktop app, CLI

Term

[Task](/codex/projects)

Definition

A defined outcome ChatGPT or Codex works toward, such as fixing a bug, creating a document, or researching a topic.

Applies to

Desktop app, Web, Mobile, CLI, IDE extension, Cloud

Term

[Thread](/codex/app-server#threads)

Definition

A technical object in Codex app-server APIs that contains turns and stored conversation history.

Applies to

App-server, SDK

Term

[Thread fork](/codex/app-server#start-or-resume-a-thread)

Definition

New thread branched from the stored history of an existing thread.

Applies to

App-server, SDK

Term

[Turn](/codex/app-server#core-primitives)

Definition

One exchange in a chat, usually a user prompt plus the agent's response and actions.

Applies to

Desktop app, CLI, IDE extension, Cloud, SDK

Term

[Universal image](/codex/environments/cloud-environment#default-universal-image)

Definition

Default Codex cloud container image with common tools preinstalled.

Applies to

Cloud

Term

[Web search cache](/codex/config-file/config-basic#web-search-mode)

Definition

Pre-indexed search results Codex can use without live browsing.

Applies to

Desktop app, CLI, IDE extension

Term

[Worktree](/codex/environments/git-worktrees)

Definition

Mode where Codex isolates changes in a separate Git worktree.

Applies to

Desktop app

Term

[Writable roots](/codex/agent-approvals-security#protected-paths-in-writable-roots)

Definition

Directories Codex is allowed to modify.

Applies to

Desktop app, CLI, IDE extension

Expand to view all
