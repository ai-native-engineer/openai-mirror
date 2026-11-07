<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/agents/subresources/automations/methods/resume/ -->

## Resume an automation

`client.beta.agents.automations.resume(stringautomationID, RequestOptionsoptions?): Automation`

**post** `/agents/automations/{automation_id}/resume`

Resumes scheduled delivery; one-time automations without a pending invocation require a future run_at.

- `automationID: string`

  `minLength: 0`, `maxLength: 1048576`

- `Automation = PeriodicAutomation | OneTimeAutomation`

  A saved automation and its schedule.

  - `PeriodicAutomation`

    Fields shared by periodic and one-time automations.

    - `id: string`

      The automation ID.

      `minLength: 0`

    - `created_at: number`

      The creation time as a Unix timestamp in seconds.

      `format: int64`

    - `created_by: AutomationCreatedBy`

      Service-recorded provenance; callers cannot supply this field.

      - `AutomationCreatedByResourceDeveloper`

        - `type: "developer"`

          The type of the object. Always `developer`.

          - `"developer"`

      - `AutomationCreatedByResourceAgent`

        - `session_id: string`

          The creator session, which is also the automation's target.

          `minLength: 0`

        - `tool_call_id: string`

          The tool call that created the automation.

          `minLength: 0`

        - `type: "agent"`

          The type of the object. Always `agent`.

          - `"agent"`

    - `expression: string`

      The cron expression determining scheduled occurrences.

      `minLength: 0`

    - `metadata: Record<string, string>`

      Custom string key-value pairs attached to the automation.

    - `name: string`

      The automation's display name.

      `minLength: 0`

    - `object: "agent.automation"`

      Always `agent.automation`.

      - `"agent.automation"`

    - `status: "active" | "paused"`

      Whether scheduled delivery is active or paused.

      - `"active"`

      - `"paused"`

    - `target: AutomationTarget`

      The session configuration or existing session receiving invocations.

      - `AutomationTargetResourceNewSession`

        - `agent: AutomationAgentConfig | null`

          The inline agent configuration, or null when agent_id is configured.

          - `instructions: string | null`

            Custom instructions, or null when absent.

            `minLength: 0`

          - `model: string`

            The requested model name.

            `minLength: 0`

          - `multi_agent: MultiAgentConfig`

            The configuration for creating and coordinating subagents.

            - `enabled: boolean`

              Whether subagent tools are enabled. Defaults to false.

            - `max_concurrent_subagents: number | null`

              Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

              `format: int64`, `minimum: 1`, `maximum: 4294967295`

          - `reasoning: AgentReasoning`

            The configured reasoning policy.

            - `effort: "none" | "minimal" | "low" | 4 more | null`

              The requested reasoning effort, or `null` when the model selects its own default.

              - `"none"`

              - `"minimal"`

              - `"low"`

              - `"medium"`

              - `"high"`

              - `"xhigh"`

              - `"max"`

            - `summary: "concise" | "detailed" | "auto" | null`

              The requested reasoning summary format, or `null` when summaries are disabled.

              - `"concise"`

                Returns a concise reasoning summary when supported.

              - `"detailed"`

                Returns a detailed reasoning summary when supported.

              - `"auto"`

                Automatically selects the most detailed summary supported by the model.

          - `service_tier: "auto" | "default" | "flex" | 3 more`

            The configured service-tier policy.

            - `"auto"`

            - `"default"`

            - `"flex"`

            - `"priority"`

            - `"fast"`

            - `"ultrafast"`

          - `text: AgentText`

            The configured output format and verbosity.

            - `format: TextFormat`

              The effective output format. Defaults to ordinary text.

              - `TextFormatResourceText`

                Generates ordinary text without a structured-output constraint.

                - `type: "text"`

                  The type of the object. Always `text`.

                  - `"text"`

              - `TextFormatResourceJSONSchema`

                Constrains generated text to a JSON Schema.

                - `schema: Record<string, unknown>`

                  The JSON Schema that generated text must match.

                - `type: "json_schema"`

                  The type of the object. Always `json_schema`.

                  - `"json_schema"`

            - `verbosity: "low" | "medium" | "high"`

              The amount of text produced by the agent. Defaults to `medium`.

              - `"low"`

              - `"medium"`

              - `"high"`

          - `tools: Array<AgentTool>`

            Configured tools, excluding confidential credentials.

            `minItems: 0`, `maxItems: 2000`

            - `AgentToolResourceFunction`

              A function defined by the application.

              - `defer_loading: boolean`

                Whether the function is deferred and discovered through tool search.

              - `description: string`

                A description of what the function does.

                `minLength: 0`

              - `name: string`

                The name of the function.

                `minLength: 0`

              - `parameters: Record<string, unknown>`

                A JSON Schema object describing the function's arguments.

              - `type: "function"`

                The type of the object. Always `function`.

                - `"function"`

              - `async?: boolean`

                Whether the agent continues without waiting for the function result.

            - `AgentToolResourceProgrammaticToolCalling`

              Enables calling tools from model-generated code.

              - `enabled: boolean`

                Whether tools can be called from model-generated code.

              - `type: "programmatic_tool_calling"`

                The type of the object. Always `programmatic_tool_calling`.

                - `"programmatic_tool_calling"`

            - `AgentToolResourceMcp`

              Tools provided by a remote MCP server.

              - `allowed_tools: Array<string> | null`

                The MCP tools the agent may call.

                `minItems: 0`, `maxItems: 2000`

              - `connection_origin: "service" | "environment"`

                Where outbound MCP HTTP connections originate.

                - `"service"`

                - `"environment"`

              - `credential_id: string | null`

                The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

                `minLength: 0`

              - `request_metadata: Record<string, unknown>`

                Metadata included with requests to this MCP server.

              - `required: boolean`

                Whether this MCP server must initialize before the first turn.

              - `server_label: string`

                A label used to identify the MCP server in tool calls.

                `minLength: 0`

              - `transport: McpTransport`

                The transport used to connect to the MCP server.

                - `McpTransportResourceHTTP`

                  Connects to an MCP server over HTTP.

                  - `server_url: string`

                    The URL of the MCP server.

                    `minLength: 0`

                  - `type: "http"`

                    The type of the object. Always `http`.

                    - `"http"`

                - `McpTransportResourceStdio`

                  Starts an MCP server as a local process.

                  - `args: Array<string>`

                    Arguments passed to the MCP server command.

                    `minItems: 0`, `maxItems: 2000`

                  - `command: string`

                    The command used to start the MCP server.

                    `minLength: 0`

                  - `cwd: string`

                    The working directory used to start the MCP server.

                    `minLength: 0`

                  - `env_vars: Array<string>`

                    Environment variable names inherited from the execution environment.

                    `minItems: 0`, `maxItems: 2000`

                  - `type: "stdio"`

                    The type of the object. Always `stdio`.

                    - `"stdio"`

              - `type: "mcp"`

                The type of the object. Always `mcp`.

                - `"mcp"`

            - `AgentToolResourceWebSearch`

              Web search.

              - `allowed_domains: Array<string> | null`

                Allowed search domains, or `null` when the search is unrestricted.

                `minItems: 0`, `maxItems: 2000`

              - `context_size: "low" | "medium" | "high"`

                The amount of search context made available to the model. Defaults to `medium`.

                - `"low"`

                - `"medium"`

                - `"high"`

              - `location: Location | null`

                Approximate location used to localize search results, if provided.

                - `city: string | null`

                  The city name.

                  `minLength: 0`

                - `country: string | null`

                  The two-letter ISO country code, such as `US`.

                  `minLength: 0`

                - `region: string | null`

                  The region or state name.

                  `minLength: 0`

                - `timezone: string | null`

                  The IANA timezone, such as `America/Los_Angeles`.

                  `minLength: 0`

              - `mode: "disabled" | "cached" | "live"`

                The source used for web search results.

                - `"disabled"`

                - `"cached"`

                - `"live"`

              - `type: "web_search"`

                The type of the object. Always `web_search`.

                - `"web_search"`

            - `AgentToolResourceComputerUse`

              Browser use in an OpenAI-hosted session.

              - `include_screenshots: boolean`

                Whether computer tool outputs include screenshots.

              - `type: "computer_use"`

                The type of the object. Always `computer_use`.

                - `"computer_use"`

            - `AgentToolResourceAutomations`

              Lets the agent manage its own scheduled wakeups.

              - `type: "automations"`

                The type of the object. Always `automations`.

                - `"automations"`

          - `compaction?: Compaction`

            The effective context compaction settings.

            - `async: boolean`

              Whether context is compacted in the background. Defaults to true.

          - `experimental?: Experimental`

            The effective experimental settings for the agent.

            - `time_awareness: boolean`

              Whether the model receives periodic current-time reminders.

        - `agent_id: string | null`

          The saved agent reference, or null when an inline agent is configured.

          `minLength: 0`

        - `environment: AutomationEnvironment`

          Configuration or references used to select the execution environment.

          - `AutomationEnvironmentResourceNone`

            - `type: "none"`

              The type of the object. Always `none`.

              - `"none"`

          - `AutomationEnvironmentResourceOpenAIHosted`

            Hosted environment selection with confidential setup commands and variables omitted.

            - `capability_directories: Array<string> | null`

              Directory overrides, or null to inherit the template or creation default.

              `minItems: 0`, `maxItems: 2000`

            - `container_size: "small" | "medium" | "large" | null`

              The configured container size, or null to use the creation default.

              - `"small"`

              - `"medium"`

              - `"large"`

            - `desktop: Desktop | null`

              Desktop overrides, or null to inherit the template or creation default.

              - `enabled: boolean`

                Whether the environment provisions a desktop and browser proxy.

            - `environment_id: string | null`

              An existing environment reference, or null when provisioning a new environment.

              `minLength: 0`

            - `environment_template_id: string | null`

              A template reference, or null when no template is selected.

              `minLength: 0`

            - `files: Array<HostedTemplateFileResourceFileID | HostedTemplateFileResourceInline> | null`

              File overrides, excluding contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `HostedTemplateFileResourceFileID`

                A project-scoped Files API reference resolved separately for each session.

                - `file_id: string`

                  The ID of the uploaded file.

                  `minLength: 0`

                - `path: string`

                  The file's absolute path inside the environment.

                  `minLength: 0`

                - `type: "file_id"`

                  The type of the object. Always `file_id`.

                  - `"file_id"`

              - `HostedTemplateFileResourceInline`

                Metadata for confidential inline file contents.

                - `path: string`

                  The file's absolute path inside the environment.

                  `minLength: 0`

                - `size_bytes: number`

                  The decoded size of the inline file in bytes.

                  `format: int64`, `minimum: 0`

                - `type: "inline"`

                  The type of the object. Always `inline`.

                  - `"inline"`

            - `network: Network | null`

              Network overrides, or null to inherit the template or creation default.

              - `access: "enabled" | "disabled" | "restricted"`

                The environment's network access mode.

                - `"enabled"`

                  Allows unrestricted network access.

                - `"disabled"`

                  Disables network access.

                - `"restricted"`

                  Applies the configured domain restrictions.

              - `allowed_domains: Array<string>`

                Domains the environment may access when network access is restricted.

                `minItems: 0`, `maxItems: 2000`

            - `packages: Packages | null`

              Package overrides, or null to inherit the template or creation default.

              - `npm: Array<string>`

                npm packages installed globally in the environment.

                `minItems: 0`, `maxItems: 16384`

              - `python: Array<string>`

                Python packages installed in the environment.

                `minItems: 0`, `maxItems: 16384`

              - `system: Array<string>`

                System packages installed in the environment.

                `minItems: 0`, `maxItems: 16384`

            - `plugins: Array<HostedPlugin> | null`

              Plugin overrides, excluding archive contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `description: string`

                The installed plugin description.

                `minLength: 0`

              - `name: string`

                The installed plugin name.

                `minLength: 0`

              - `type: "inline"`

                The type of the object. Always `inline`.

                - `"inline"`

            - `skills: Array<HostedTemplateSkillResourceSkillReference | HostedTemplateSkillResourceInline> | null`

              Skill overrides, excluding archive contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `HostedTemplateSkillResourceSkillReference`

                A skill resolved afresh from the Skills API whenever a session starts.

                - `skill_id: string`

                  The referenced skill ID.

                  `minLength: 0`

                - `type: "skill_reference"`

                  The type of the object. Always `skill_reference`.

                  - `"skill_reference"`

                - `version: string | null`

                  The requested version selector, including `latest`.

                  `minLength: 0`

              - `HostedTemplateSkillResourceInline`

                Safe metadata for an inline skill archive.

                - `description: string`

                  The skill description declared in `SKILL.md`.

                  `minLength: 0`

                - `name: string`

                  The skill name declared in `SKILL.md`.

                  `minLength: 0`

                - `type: "inline"`

                  The type of the object. Always `inline`.

                  - `"inline"`

            - `type: "openai_hosted"`

              The type of the object. Always `openai_hosted`.

              - `"openai_hosted"`

          - `AutomationEnvironmentResourceSelfHosted`

            - `capability_directories: Array<string>`

              Directories that expose capabilities to the agent.

              `minItems: 0`, `maxItems: 2000`

            - `environment_id: string | null`

              An existing registration, or null to create a session-owned environment.

              `minLength: 0`

            - `type: "self_hosted"`

              The type of the object. Always `self_hosted`.

              - `"self_hosted"`

            - `workspace_directory: string`

              The absolute project directory in the environment.

              `minLength: 0`

        - `input: Array<Input>`

          Initial input delivered to each new session.

          `minItems: 0`, `maxItems: 2000`

          - `content: Array<InputContent>`

            The content of the message.

            `minItems: 0`, `maxItems: 2000`

            - `InputContentResourceInputText`

              Text input recorded in a session item.

              - `text: string`

                The text supplied to the agent.

                `minLength: 0`

              - `type: "input_text"`

                The type of the object. Always `input_text`.

                - `"input_text"`

            - `InputContentResourceInputImage`

              Image input recorded in a session item.

              - `image_url: string`

                The URL of the image supplied to the agent, which may be a base64-encoded data URL.

                `minLength: 0`

              - `type: "input_image"`

                The type of the object. Always `input_image`.

                - `"input_image"`

          - `role: "user"`

            The role of the message author. Always `user`.

            - `"user"`

          - `type: "message"`

            The type of the input item. Always `message`.

            - `"message"`

        - `metadata: Record<string, string>`

          Metadata attached to each new session.

        - `type: "new_session"`

          The type of the object. Always `new_session`.

          - `"new_session"`

        - `vault_ids: Array<string>`

          Vaults made available to each new session.

          `minItems: 0`, `maxItems: 2000`

      - `AutomationTargetResourceExistingSession`

        - `instructions: string`

          Saved instructions delivered as an automation notification.

          `minLength: 0`

        - `session_id: string`

          The session receiving each invocation.

          `minLength: 0`

        - `type: "existing_session"`

          The type of the object. Always `existing_session`.

          - `"existing_session"`

    - `timezone: string`

      The timezone used to interpret the expression.

      `minLength: 0`

    - `type: "periodic"`

      The type of the object. Always `periodic`.

      - `"periodic"`

  - `OneTimeAutomation`

    Fields shared by periodic and one-time automations.

    - `id: string`

      The automation ID.

      `minLength: 0`

    - `created_at: number`

      The creation time as a Unix timestamp in seconds.

      `format: int64`

    - `created_by: AutomationCreatedBy`

      Service-recorded provenance; callers cannot supply this field.

    - `metadata: Record<string, string>`

      Custom string key-value pairs attached to the automation.

    - `name: string`

      The automation's display name.

      `minLength: 0`

    - `object: "agent.automation"`

      Always `agent.automation`.

      - `"agent.automation"`

    - `run_at: number`

      The Unix timestamp, in seconds, of the scheduled occurrence.

      `format: int64`

    - `status: "active" | "paused" | "completed"`

      Completion means the schedule has finished, not the agent's work.

      - `"active"`

      - `"paused"`

      - `"completed"`

    - `target: AutomationTarget`

      The session configuration or existing session receiving invocations.

    - `type: "once"`

      The type of the object. Always `once`.

      - `"once"`

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const automation = await client.beta.agents.automations.resume('automation_id');

console.log(automation);

  "created_by": {
    "type": "developer"
  "expression": "expression",
  "metadata": {
    "foo": "string"
  "object": "agent.automation",
  "status": "active",
  "target": {
    "agent": {
      "instructions": "instructions",
      "model": "model",
      "multi_agent": {
        "enabled": true,
        "max_concurrent_subagents": 1
      "reasoning": {
        "effort": "none",
        "summary": "concise"
      "service_tier": "auto",
      "text": {
        "format": {
          "type": "text"
        "verbosity": "low"
      "tools": [
          "defer_loading": true,
          "parameters": {
            "foo": "bar"
          "type": "function",
          "async": true
      "compaction": {
        "async": true
      "experimental": {
        "time_awareness": true
    "agent_id": "agent_id",
    "environment": {
      "type": "none"
    "input": [
        "content": [
            "text": "text",
            "type": "input_text"
        "role": "user",
        "type": "message"
    "metadata": {
      "foo": "string"
    "type": "new_session",
    "vault_ids": [
      "string"
    ]
  "timezone": "timezone",
  "type": "periodic"
