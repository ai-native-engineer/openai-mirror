<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/agents/subresources/automations/methods/resume/ -->

## Resume an automation

`beta.agents.automations.resume(strautomation_id)  -> Automation`

**post** `/agents/automations/{automation_id}/resume`

Resumes scheduled delivery; one-time automations without a pending invocation require a future run_at.

- `automation_id: str`

  `minLength: 0`, `maxLength: 1048576`

- `Automation`

  A saved automation and its schedule.

  - `class PeriodicAutomation: …`

    Fields shared by periodic and one-time automations.

    - `id: str`

      The automation ID.

      `minLength: 0`

    - `created_at: int`

      The creation time as a Unix timestamp in seconds.

      `format: int64`

    - `created_by: AutomationCreatedBy`

      Service-recorded provenance; callers cannot supply this field.

      - `class AutomationCreatedByResourceDeveloper: …`

        - `type: Literal["developer"]`

          The type of the object. Always `developer`.

          - `"developer"`

      - `class AutomationCreatedByResourceAgent: …`

        - `session_id: str`

          The creator session, which is also the automation's target.

          `minLength: 0`

        - `tool_call_id: str`

          The tool call that created the automation.

          `minLength: 0`

        - `type: Literal["agent"]`

          The type of the object. Always `agent`.

          - `"agent"`

    - `expression: str`

      The cron expression determining scheduled occurrences.

      `minLength: 0`

    - `metadata: Dict[str, str]`

      Custom string key-value pairs attached to the automation.

    - `name: str`

      The automation's display name.

      `minLength: 0`

    - `object: Literal["agent.automation"]`

      Always `agent.automation`.

      - `"agent.automation"`

    - `status: Literal["active", "paused"]`

      Whether scheduled delivery is active or paused.

      - `"active"`

      - `"paused"`

    - `target: AutomationTarget`

      The session configuration or existing session receiving invocations.

      - `class AutomationTargetResourceNewSession: …`

        - `agent: Optional[AutomationAgentConfig]`

          The inline agent configuration, or null when agent_id is configured.

          - `instructions: Optional[str]`

            Custom instructions, or null when absent.

            `minLength: 0`

          - `model: str`

            The requested model name.

            `minLength: 0`

          - `multi_agent: MultiAgentConfig`

            The configuration for creating and coordinating subagents.

            - `enabled: bool`

              Whether subagent tools are enabled. Defaults to false.

            - `max_concurrent_subagents: Optional[int]`

              Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

              `format: int64`, `minimum: 1`, `maximum: 4294967295`

          - `reasoning: AgentReasoning`

            The configured reasoning policy.

            - `effort: Optional[Literal["none", "minimal", "low", 4 more]]`

              The requested reasoning effort, or `null` when the model selects its own default.

              - `"none"`

              - `"minimal"`

              - `"low"`

              - `"medium"`

              - `"high"`

              - `"xhigh"`

              - `"max"`

            - `summary: Optional[Literal["concise", "detailed", "auto"]]`

              The requested reasoning summary format, or `null` when summaries are disabled.

              - `"concise"`

                Returns a concise reasoning summary when supported.

              - `"detailed"`

                Returns a detailed reasoning summary when supported.

              - `"auto"`

                Automatically selects the most detailed summary supported by the model.

          - `service_tier: Literal["auto", "default", "flex", 3 more]`

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

              - `class TextFormatResourceText: …`

                Generates ordinary text without a structured-output constraint.

                - `type: Literal["text"]`

                  The type of the object. Always `text`.

                  - `"text"`

              - `class TextFormatResourceJSONSchema: …`

                Constrains generated text to a JSON Schema.

                - `schema: Dict[str, object]`

                  The JSON Schema that generated text must match.

                - `type: Literal["json_schema"]`

                  The type of the object. Always `json_schema`.

                  - `"json_schema"`

            - `verbosity: Literal["low", "medium", "high"]`

              The amount of text produced by the agent. Defaults to `medium`.

              - `"low"`

              - `"medium"`

              - `"high"`

          - `tools: List[AgentTool]`

            Configured tools, excluding confidential credentials.

            `minItems: 0`, `maxItems: 2000`

            - `class AgentToolResourceFunction: …`

              A function defined by the application.

              - `defer_loading: bool`

                Whether the function is deferred and discovered through tool search.

              - `description: str`

                A description of what the function does.

                `minLength: 0`

              - `name: str`

                The name of the function.

                `minLength: 0`

              - `parameters: Dict[str, object]`

                A JSON Schema object describing the function's arguments.

              - `type: Literal["function"]`

                The type of the object. Always `function`.

                - `"function"`

              - `async_: Optional[bool]`

                Whether the agent continues without waiting for the function result.

            - `class AgentToolResourceProgrammaticToolCalling: …`

              Enables calling tools from model-generated code.

              - `enabled: bool`

                Whether tools can be called from model-generated code.

              - `type: Literal["programmatic_tool_calling"]`

                The type of the object. Always `programmatic_tool_calling`.

                - `"programmatic_tool_calling"`

            - `class AgentToolResourceMcp: …`

              Tools provided by a remote MCP server.

              - `allowed_tools: Optional[List[str]]`

                The MCP tools the agent may call.

                `minItems: 0`, `maxItems: 2000`

              - `connection_origin: Literal["service", "environment"]`

                Where outbound MCP HTTP connections originate.

                - `"service"`

                - `"environment"`

              - `credential_id: Optional[str]`

                The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

                `minLength: 0`

              - `request_metadata: Dict[str, object]`

                Metadata included with requests to this MCP server.

              - `required: bool`

                Whether this MCP server must initialize before the first turn.

              - `server_label: str`

                A label used to identify the MCP server in tool calls.

                `minLength: 0`

              - `transport: McpTransport`

                The transport used to connect to the MCP server.

                - `class McpTransportResourceHTTP: …`

                  Connects to an MCP server over HTTP.

                  - `server_url: str`

                    The URL of the MCP server.

                    `minLength: 0`

                  - `type: Literal["http"]`

                    The type of the object. Always `http`.

                    - `"http"`

                - `class McpTransportResourceStdio: …`

                  Starts an MCP server as a local process.

                  - `args: List[str]`

                    Arguments passed to the MCP server command.

                    `minItems: 0`, `maxItems: 2000`

                  - `command: str`

                    The command used to start the MCP server.

                    `minLength: 0`

                  - `cwd: str`

                    The working directory used to start the MCP server.

                    `minLength: 0`

                  - `env_vars: List[str]`

                    Environment variable names inherited from the execution environment.

                    `minItems: 0`, `maxItems: 2000`

                  - `type: Literal["stdio"]`

                    The type of the object. Always `stdio`.

                    - `"stdio"`

              - `type: Literal["mcp"]`

                The type of the object. Always `mcp`.

                - `"mcp"`

            - `class AgentToolResourceWebSearch: …`

              Web search.

              - `allowed_domains: Optional[List[str]]`

                Allowed search domains, or `null` when the search is unrestricted.

                `minItems: 0`, `maxItems: 2000`

              - `context_size: Literal["low", "medium", "high"]`

                The amount of search context made available to the model. Defaults to `medium`.

                - `"low"`

                - `"medium"`

                - `"high"`

              - `location: Optional[AgentToolResourceWebSearchLocation]`

                Approximate location used to localize search results, if provided.

                - `city: Optional[str]`

                  The city name.

                  `minLength: 0`

                - `country: Optional[str]`

                  The two-letter ISO country code, such as `US`.

                  `minLength: 0`

                - `region: Optional[str]`

                  The region or state name.

                  `minLength: 0`

                - `timezone: Optional[str]`

                  The IANA timezone, such as `America/Los_Angeles`.

                  `minLength: 0`

              - `mode: Literal["disabled", "cached", "live"]`

                The source used for web search results.

                - `"disabled"`

                - `"cached"`

                - `"live"`

              - `type: Literal["web_search"]`

                The type of the object. Always `web_search`.

                - `"web_search"`

            - `class AgentToolResourceComputerUse: …`

              Browser use in an OpenAI-hosted session.

              - `include_screenshots: bool`

                Whether computer tool outputs include screenshots.

              - `type: Literal["computer_use"]`

                The type of the object. Always `computer_use`.

                - `"computer_use"`

            - `class AgentToolResourceAutomations: …`

              Lets the agent manage its own scheduled wakeups.

              - `type: Literal["automations"]`

                The type of the object. Always `automations`.

                - `"automations"`

          - `compaction: Optional[Compaction]`

            The effective context compaction settings.

            - `async_: bool`

              Whether context is compacted in the background. Defaults to true.

          - `experimental: Optional[Experimental]`

            The effective experimental settings for the agent.

            - `time_awareness: bool`

              Whether the model receives periodic current-time reminders.

        - `agent_id: Optional[str]`

          The saved agent reference, or null when an inline agent is configured.

          `minLength: 0`

        - `environment: AutomationEnvironment`

          Configuration or references used to select the execution environment.

          - `class AutomationEnvironmentResourceNone: …`

            - `type: Literal["none"]`

              The type of the object. Always `none`.

              - `"none"`

          - `class AutomationEnvironmentResourceOpenAIHosted: …`

            Hosted environment selection with confidential setup commands and variables omitted.

            - `capability_directories: Optional[List[str]]`

              Directory overrides, or null to inherit the template or creation default.

              `minItems: 0`, `maxItems: 2000`

            - `container_size: Optional[Literal["small", "medium", "large"]]`

              The configured container size, or null to use the creation default.

              - `"small"`

              - `"medium"`

              - `"large"`

            - `desktop: Optional[AutomationEnvironmentResourceOpenAIHostedDesktop]`

              Desktop overrides, or null to inherit the template or creation default.

              - `enabled: bool`

                Whether the environment provisions a desktop and browser proxy.

            - `environment_id: Optional[str]`

              An existing environment reference, or null when provisioning a new environment.

              `minLength: 0`

            - `environment_template_id: Optional[str]`

              A template reference, or null when no template is selected.

              `minLength: 0`

            - `files: Optional[List[AutomationEnvironmentResourceOpenaiHostedFile]]`

              File overrides, excluding contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `class AutomationEnvironmentResourceOpenAIHostedFileHostedTemplateFileResourceFileID: …`

                A project-scoped Files API reference resolved separately for each session.

                - `file_id: str`

                  The ID of the uploaded file.

                  `minLength: 0`

                - `path: str`

                  The file's absolute path inside the environment.

                  `minLength: 0`

                - `type: Literal["file_id"]`

                  The type of the object. Always `file_id`.

                  - `"file_id"`

              - `class AutomationEnvironmentResourceOpenAIHostedFileHostedTemplateFileResourceInline: …`

                Metadata for confidential inline file contents.

                - `path: str`

                  The file's absolute path inside the environment.

                  `minLength: 0`

                - `size_bytes: int`

                  The decoded size of the inline file in bytes.

                  `format: int64`, `minimum: 0`

                - `type: Literal["inline"]`

                  The type of the object. Always `inline`.

                  - `"inline"`

            - `network: Optional[AutomationEnvironmentResourceOpenAIHostedNetwork]`

              Network overrides, or null to inherit the template or creation default.

              - `access: Literal["enabled", "disabled", "restricted"]`

                The environment's network access mode.

                - `"enabled"`

                  Allows unrestricted network access.

                - `"disabled"`

                  Disables network access.

                - `"restricted"`

                  Applies the configured domain restrictions.

              - `allowed_domains: List[str]`

                Domains the environment may access when network access is restricted.

                `minItems: 0`, `maxItems: 2000`

            - `packages: Optional[AutomationEnvironmentResourceOpenAIHostedPackages]`

              Package overrides, or null to inherit the template or creation default.

              - `npm: List[str]`

                npm packages installed globally in the environment.

                `minItems: 0`, `maxItems: 16384`

              - `python: List[str]`

                Python packages installed in the environment.

                `minItems: 0`, `maxItems: 16384`

              - `system: List[str]`

                System packages installed in the environment.

                `minItems: 0`, `maxItems: 16384`

            - `plugins: Optional[List[HostedPlugin]]`

              Plugin overrides, excluding archive contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `description: str`

                The installed plugin description.

                `minLength: 0`

              - `name: str`

                The installed plugin name.

                `minLength: 0`

              - `type: Literal["inline"]`

                The type of the object. Always `inline`.

                - `"inline"`

            - `skills: Optional[List[AutomationEnvironmentResourceOpenaiHostedSkill]]`

              Skill overrides, excluding archive contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `class AutomationEnvironmentResourceOpenAIHostedSkillHostedTemplateSkillResourceSkillReference: …`

                A skill resolved afresh from the Skills API whenever a session starts.

                - `skill_id: str`

                  The referenced skill ID.

                  `minLength: 0`

                - `type: Literal["skill_reference"]`

                  The type of the object. Always `skill_reference`.

                  - `"skill_reference"`

                - `version: Optional[str]`

                  The requested version selector, including `latest`.

                  `minLength: 0`

              - `class AutomationEnvironmentResourceOpenAIHostedSkillHostedTemplateSkillResourceInline: …`

                Safe metadata for an inline skill archive.

                - `description: str`

                  The skill description declared in `SKILL.md`.

                  `minLength: 0`

                - `name: str`

                  The skill name declared in `SKILL.md`.

                  `minLength: 0`

                - `type: Literal["inline"]`

                  The type of the object. Always `inline`.

                  - `"inline"`

            - `type: Literal["openai_hosted"]`

              The type of the object. Always `openai_hosted`.

              - `"openai_hosted"`

          - `class AutomationEnvironmentResourceSelfHosted: …`

            - `capability_directories: List[str]`

              Directories that expose capabilities to the agent.

              `minItems: 0`, `maxItems: 2000`

            - `environment_id: Optional[str]`

              An existing registration, or null to create a session-owned environment.

              `minLength: 0`

            - `type: Literal["self_hosted"]`

              The type of the object. Always `self_hosted`.

              - `"self_hosted"`

            - `workspace_directory: str`

              The absolute project directory in the environment.

              `minLength: 0`

        - `input: List[AutomationTargetResourceNewSessionInput]`

          Initial input delivered to each new session.

          `minItems: 0`, `maxItems: 2000`

          - `content: List[InputContent]`

            The content of the message.

            `minItems: 0`, `maxItems: 2000`

            - `class InputContentResourceInputText: …`

              Text input recorded in a session item.

              - `text: str`

                The text supplied to the agent.

                `minLength: 0`

              - `type: Literal["input_text"]`

                The type of the object. Always `input_text`.

                - `"input_text"`

            - `class InputContentResourceInputImage: …`

              Image input recorded in a session item.

              - `image_url: str`

                The URL of the image supplied to the agent, which may be a base64-encoded data URL.

                `minLength: 0`

              - `type: Literal["input_image"]`

                The type of the object. Always `input_image`.

                - `"input_image"`

          - `role: Literal["user"]`

            The role of the message author. Always `user`.

            - `"user"`

          - `type: Literal["message"]`

            The type of the input item. Always `message`.

            - `"message"`

        - `metadata: Dict[str, str]`

          Metadata attached to each new session.

        - `type: Literal["new_session"]`

          The type of the object. Always `new_session`.

          - `"new_session"`

        - `vault_ids: List[str]`

          Vaults made available to each new session.

          `minItems: 0`, `maxItems: 2000`

      - `class AutomationTargetResourceExistingSession: …`

        - `instructions: str`

          Saved instructions delivered as an automation notification.

          `minLength: 0`

        - `session_id: str`

          The session receiving each invocation.

          `minLength: 0`

        - `type: Literal["existing_session"]`

          The type of the object. Always `existing_session`.

          - `"existing_session"`

    - `timezone: str`

      The timezone used to interpret the expression.

      `minLength: 0`

    - `type: Literal["periodic"]`

      The type of the object. Always `periodic`.

      - `"periodic"`

  - `class OneTimeAutomation: …`

    Fields shared by periodic and one-time automations.

    - `id: str`

      The automation ID.

      `minLength: 0`

    - `created_at: int`

      The creation time as a Unix timestamp in seconds.

      `format: int64`

    - `created_by: AutomationCreatedBy`

      Service-recorded provenance; callers cannot supply this field.

    - `metadata: Dict[str, str]`

      Custom string key-value pairs attached to the automation.

    - `name: str`

      The automation's display name.

      `minLength: 0`

    - `object: Literal["agent.automation"]`

      Always `agent.automation`.

      - `"agent.automation"`

    - `run_at: int`

      The Unix timestamp, in seconds, of the scheduled occurrence.

      `format: int64`

    - `status: Literal["active", "paused", "completed"]`

      Completion means the schedule has finished, not the agent's work.

      - `"active"`

      - `"paused"`

      - `"completed"`

    - `target: AutomationTarget`

      The session configuration or existing session receiving invocations.

    - `type: Literal["once"]`

      The type of the object. Always `once`.

      - `"once"`

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
automation = client.beta.agents.automations.resume(
    "automation_id",
print(automation)

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
