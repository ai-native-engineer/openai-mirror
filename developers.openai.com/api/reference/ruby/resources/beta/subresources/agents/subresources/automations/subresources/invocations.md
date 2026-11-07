<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/agents/subresources/automations/subresources/invocations/ -->

# Invocations

## Invoke an automation

`beta.agents.automations.invocations.create(automation_id) -> AutomationInvocation`

**post** `/agents/automations/{automation_id}/invocations`

Queues a manual delivery without changing the saved schedule.

### Parameters

- `automation_id: String`

  `minLength: 0`, `maxLength: 1048576`

### Returns

- `class AutomationInvocation`

  One attempted delivery by an automation.

  - `id: String`

    The invocation ID.

    `minLength: 0`

  - `automation_id: String`

    The automation that owns the invocation.

    `minLength: 0`

  - `created_at: Integer`

    The creation time as a Unix timestamp in seconds.

    `format: int64`

  - `error: Error{ code, message}`

    The permanent delivery failure, or null when no failure occurred.

    - `code: String`

      A machine-readable error code.

      `minLength: 0`

    - `message: String`

      A public explanation of the delivery failure.

      `minLength: 0`

  - `object: :"agent.automation.invocation"`

    Always `agent.automation.invocation`.

    - `:"agent.automation.invocation"`

  - `scheduled_at: Integer`

    The intended occurrence as a Unix timestamp in seconds, or null for manual runs.

    `format: int64`

  - `session_id: String`

    The target or newly created session ID, or null before one is available.

    `minLength: 0`

  - `skip_reason: :pending_delivery`

    Why an occurrence was skipped, or null when it was not skipped.

    - `:pending_delivery`

  - `source: AutomationInvocationSource`

    Whether the invocation was manual or scheduled.

    - `class Manual`

      - `type: :manual`

        The type of the object. Always `manual`.

        - `:manual`

    - `class Automation`

      - `automation: Automation`

        The automation snapshot for this occurrence, excluding confidential values.

        - `class PeriodicAutomation`

          Fields shared by periodic and one-time automations.

          - `id: String`

            The automation ID.

            `minLength: 0`

          - `created_at: Integer`

            The creation time as a Unix timestamp in seconds.

            `format: int64`

          - `created_by: AutomationCreatedBy`

            Service-recorded provenance; callers cannot supply this field.

            - `class Developer`

              - `type: :developer`

                The type of the object. Always `developer`.

                - `:developer`

            - `class Agent`

              - `session_id: String`

                The creator session, which is also the automation's target.

                `minLength: 0`

              - `tool_call_id: String`

                The tool call that created the automation.

                `minLength: 0`

              - `type: :agent`

                The type of the object. Always `agent`.

                - `:agent`

          - `expression: String`

            The cron expression determining scheduled occurrences.

            `minLength: 0`

          - `metadata: Hash[Symbol, String]`

            Custom string key-value pairs attached to the automation.

          - `name: String`

            The automation's display name.

            `minLength: 0`

          - `object: :"agent.automation"`

            Always `agent.automation`.

            - `:"agent.automation"`

          - `status: :active | :paused`

            Whether scheduled delivery is active or paused.

            - `:active`

            - `:paused`

          - `target: AutomationTarget`

            The session configuration or existing session receiving invocations.

            - `class NewSession`

              - `agent: AutomationAgentConfig`

                The inline agent configuration, or null when agent_id is configured.

                - `instructions: String`

                  Custom instructions, or null when absent.

                  `minLength: 0`

                - `model: String`

                  The requested model name.

                  `minLength: 0`

                - `multi_agent: MultiAgentConfig`

                  The configuration for creating and coordinating subagents.

                  - `enabled: bool`

                    Whether subagent tools are enabled. Defaults to false.

                  - `max_concurrent_subagents: Integer`

                    Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

                    `format: int64`, `minimum: 1`, `maximum: 4294967295`

                - `reasoning: AgentReasoning`

                  The configured reasoning policy.

                  - `effort: :none | :minimal | :low | 4 more`

                    The requested reasoning effort, or `null` when the model selects its own default.

                    - `:none`

                    - `:minimal`

                    - `:low`

                    - `:medium`

                    - `:high`

                    - `:xhigh`

                    - `:max`

                  - `summary: :concise | :detailed | :auto`

                    The requested reasoning summary format, or `null` when summaries are disabled.

                    - `:concise`

                      Returns a concise reasoning summary when supported.

                    - `:detailed`

                      Returns a detailed reasoning summary when supported.

                    - `:auto`

                      Automatically selects the most detailed summary supported by the model.

                - `service_tier: :auto | :default | :flex | 3 more`

                  The configured service-tier policy.

                  - `:auto`

                  - `:default`

                  - `:flex`

                  - `:priority`

                  - `:fast`

                  - `:ultrafast`

                - `text: AgentText`

                  The configured output format and verbosity.

                  - `format_: TextFormat`

                    The effective output format. Defaults to ordinary text.

                    - `class Text`

                      Generates ordinary text without a structured-output constraint.

                      - `type: :text`

                        The type of the object. Always `text`.

                        - `:text`

                    - `class JSONSchema`

                      Constrains generated text to a JSON Schema.

                      - `schema: Hash[Symbol, untyped]`

                        The JSON Schema that generated text must match.

                      - `type: :json_schema`

                        The type of the object. Always `json_schema`.

                        - `:json_schema`

                  - `verbosity: :low | :medium | :high`

                    The amount of text produced by the agent. Defaults to `medium`.

                    - `:low`

                    - `:medium`

                    - `:high`

                - `tools: Array[AgentTool]`

                  Configured tools, excluding confidential credentials.

                  `minItems: 0`, `maxItems: 2000`

                  - `class Function`

                    A function defined by the application.

                    - `defer_loading: bool`

                      Whether the function is deferred and discovered through tool search.

                    - `description: String`

                      A description of what the function does.

                      `minLength: 0`

                    - `name: String`

                      The name of the function.

                      `minLength: 0`

                    - `parameters: Hash[Symbol, untyped]`

                      A JSON Schema object describing the function's arguments.

                    - `type: :function`

                      The type of the object. Always `function`.

                      - `:function`

                    - `async: bool`

                      Whether the agent continues without waiting for the function result.

                  - `class ProgrammaticToolCalling`

                    Enables calling tools from model-generated code.

                    - `enabled: bool`

                      Whether tools can be called from model-generated code.

                    - `type: :programmatic_tool_calling`

                      The type of the object. Always `programmatic_tool_calling`.

                      - `:programmatic_tool_calling`

                  - `class Mcp`

                    Tools provided by a remote MCP server.

                    - `allowed_tools: Array[String]`

                      The MCP tools the agent may call.

                      `minItems: 0`, `maxItems: 2000`

                    - `connection_origin: :service | :environment`

                      Where outbound MCP HTTP connections originate.

                      - `:service`

                      - `:environment`

                    - `credential_id: String`

                      The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

                      `minLength: 0`

                    - `request_metadata: Hash[Symbol, untyped]`

                      Metadata included with requests to this MCP server.

                    - `required: bool`

                      Whether this MCP server must initialize before the first turn.

                    - `server_label: String`

                      A label used to identify the MCP server in tool calls.

                      `minLength: 0`

                    - `transport: McpTransport`

                      The transport used to connect to the MCP server.

                      - `class HTTP`

                        Connects to an MCP server over HTTP.

                        - `server_url: String`

                          The URL of the MCP server.

                          `minLength: 0`

                        - `type: :http`

                          The type of the object. Always `http`.

                          - `:http`

                      - `class Stdio`

                        Starts an MCP server as a local process.

                        - `args: Array[String]`

                          Arguments passed to the MCP server command.

                          `minItems: 0`, `maxItems: 2000`

                        - `command: String`

                          The command used to start the MCP server.

                          `minLength: 0`

                        - `cwd: String`

                          The working directory used to start the MCP server.

                          `minLength: 0`

                        - `env_vars: Array[String]`

                          Environment variable names inherited from the execution environment.

                          `minItems: 0`, `maxItems: 2000`

                        - `type: :stdio`

                          The type of the object. Always `stdio`.

                          - `:stdio`

                    - `type: :mcp`

                      The type of the object. Always `mcp`.

                      - `:mcp`

                  - `class WebSearch`

                    Web search.

                    - `allowed_domains: Array[String]`

                      Allowed search domains, or `null` when the search is unrestricted.

                      `minItems: 0`, `maxItems: 2000`

                    - `context_size: :low | :medium | :high`

                      The amount of search context made available to the model. Defaults to `medium`.

                      - `:low`

                      - `:medium`

                      - `:high`

                    - `location: Location{ city, country, region, timezone}`

                      Approximate location used to localize search results, if provided.

                      - `city: String`

                        The city name.

                        `minLength: 0`

                      - `country: String`

                        The two-letter ISO country code, such as `US`.

                        `minLength: 0`

                      - `region: String`

                        The region or state name.

                        `minLength: 0`

                      - `timezone: String`

                        The IANA timezone, such as `America/Los_Angeles`.

                        `minLength: 0`

                    - `mode: :disabled | :cached | :live`

                      The source used for web search results.

                      - `:disabled`

                      - `:cached`

                      - `:live`

                    - `type: :web_search`

                      The type of the object. Always `web_search`.

                      - `:web_search`

                  - `class ComputerUse`

                    Browser use in an OpenAI-hosted session.

                    - `include_screenshots: bool`

                      Whether computer tool outputs include screenshots.

                    - `type: :computer_use`

                      The type of the object. Always `computer_use`.

                      - `:computer_use`

                  - `class Automations`

                    Lets the agent manage its own scheduled wakeups.

                    - `type: :automations`

                      The type of the object. Always `automations`.

                      - `:automations`

                - `compaction: Compaction{ async}`

                  The effective context compaction settings.

                  - `async: bool`

                    Whether context is compacted in the background. Defaults to true.

                - `experimental: Experimental{ time_awareness}`

                  The effective experimental settings for the agent.

                  - `time_awareness: bool`

                    Whether the model receives periodic current-time reminders.

              - `agent_id: String`

                The saved agent reference, or null when an inline agent is configured.

                `minLength: 0`

              - `environment: AutomationEnvironment`

                Configuration or references used to select the execution environment.

                - `class None`

                  - `type: :none`

                    The type of the object. Always `none`.

                    - `:none`

                - `class OpenAIHosted`

                  Hosted environment selection with confidential setup commands and variables omitted.

                  - `capability_directories: Array[String]`

                    Directory overrides, or null to inherit the template or creation default.

                    `minItems: 0`, `maxItems: 2000`

                  - `container_size: :small | :medium | :large`

                    The configured container size, or null to use the creation default.

                    - `:small`

                    - `:medium`

                    - `:large`

                  - `desktop: Desktop{ enabled}`

                    Desktop overrides, or null to inherit the template or creation default.

                    - `enabled: bool`

                      Whether the environment provisions a desktop and browser proxy.

                  - `environment_id: String`

                    An existing environment reference, or null when provisioning a new environment.

                    `minLength: 0`

                  - `environment_template_id: String`

                    A template reference, or null when no template is selected.

                    `minLength: 0`

                  - `files: Array[FileID{ file_id, path, type} | Inline{ path, size_bytes, type}]`

                    File overrides, excluding contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `class FileID`

                      A project-scoped Files API reference resolved separately for each session.

                      - `file_id: String`

                        The ID of the uploaded file.

                        `minLength: 0`

                      - `path: String`

                        The file's absolute path inside the environment.

                        `minLength: 0`

                      - `type: :file_id`

                        The type of the object. Always `file_id`.

                        - `:file_id`

                    - `class Inline`

                      Metadata for confidential inline file contents.

                      - `path: String`

                        The file's absolute path inside the environment.

                        `minLength: 0`

                      - `size_bytes: Integer`

                        The decoded size of the inline file in bytes.

                        `format: int64`, `minimum: 0`

                      - `type: :inline`

                        The type of the object. Always `inline`.

                        - `:inline`

                  - `network: Network{ access, allowed_domains}`

                    Network overrides, or null to inherit the template or creation default.

                    - `access: :enabled | :disabled | :restricted`

                      The environment's network access mode.

                      - `:enabled`

                        Allows unrestricted network access.

                      - `:disabled`

                        Disables network access.

                      - `:restricted`

                        Applies the configured domain restrictions.

                    - `allowed_domains: Array[String]`

                      Domains the environment may access when network access is restricted.

                      `minItems: 0`, `maxItems: 2000`

                  - `packages: Packages{ npm, python, system_}`

                    Package overrides, or null to inherit the template or creation default.

                    - `npm: Array[String]`

                      npm packages installed globally in the environment.

                      `minItems: 0`, `maxItems: 16384`

                    - `python: Array[String]`

                      Python packages installed in the environment.

                      `minItems: 0`, `maxItems: 16384`

                    - `system_: Array[String]`

                      System packages installed in the environment.

                      `minItems: 0`, `maxItems: 16384`

                  - `plugins: Array[HostedPlugin]`

                    Plugin overrides, excluding archive contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `description: String`

                      The installed plugin description.

                      `minLength: 0`

                    - `name: String`

                      The installed plugin name.

                      `minLength: 0`

                    - `type: :inline`

                      The type of the object. Always `inline`.

                      - `:inline`

                  - `skills: Array[SkillReference{ skill_id, type, version} | Inline{ description, name, type}]`

                    Skill overrides, excluding archive contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `class SkillReference`

                      A skill resolved afresh from the Skills API whenever a session starts.

                      - `skill_id: String`

                        The referenced skill ID.

                        `minLength: 0`

                      - `type: :skill_reference`

                        The type of the object. Always `skill_reference`.

                        - `:skill_reference`

                      - `version: String`

                        The requested version selector, including `latest`.

                        `minLength: 0`

                    - `class Inline`

                      Safe metadata for an inline skill archive.

                      - `description: String`

                        The skill description declared in `SKILL.md`.

                        `minLength: 0`

                      - `name: String`

                        The skill name declared in `SKILL.md`.

                        `minLength: 0`

                      - `type: :inline`

                        The type of the object. Always `inline`.

                        - `:inline`

                  - `type: :openai_hosted`

                    The type of the object. Always `openai_hosted`.

                    - `:openai_hosted`

                - `class SelfHosted`

                  - `capability_directories: Array[String]`

                    Directories that expose capabilities to the agent.

                    `minItems: 0`, `maxItems: 2000`

                  - `environment_id: String`

                    An existing registration, or null to create a session-owned environment.

                    `minLength: 0`

                  - `type: :self_hosted`

                    The type of the object. Always `self_hosted`.

                    - `:self_hosted`

                  - `workspace_directory: String`

                    The absolute project directory in the environment.

                    `minLength: 0`

              - `input: Array[Input{ content, role, type}]`

                Initial input delivered to each new session.

                `minItems: 0`, `maxItems: 2000`

                - `content: Array[InputContent]`

                  The content of the message.

                  `minItems: 0`, `maxItems: 2000`

                  - `class InputText`

                    Text input recorded in a session item.

                    - `text: String`

                      The text supplied to the agent.

                      `minLength: 0`

                    - `type: :input_text`

                      The type of the object. Always `input_text`.

                      - `:input_text`

                  - `class InputImage`

                    Image input recorded in a session item.

                    - `image_url: String`

                      The URL of the image supplied to the agent, which may be a base64-encoded data URL.

                      `minLength: 0`

                    - `type: :input_image`

                      The type of the object. Always `input_image`.

                      - `:input_image`

                - `role: :user`

                  The role of the message author. Always `user`.

                  - `:user`

                - `type: :message`

                  The type of the input item. Always `message`.

                  - `:message`

              - `metadata: Hash[Symbol, String]`

                Metadata attached to each new session.

              - `type: :new_session`

                The type of the object. Always `new_session`.

                - `:new_session`

              - `vault_ids: Array[String]`

                Vaults made available to each new session.

                `minItems: 0`, `maxItems: 2000`

            - `class ExistingSession`

              - `instructions: String`

                Saved instructions delivered as an automation notification.

                `minLength: 0`

              - `session_id: String`

                The session receiving each invocation.

                `minLength: 0`

              - `type: :existing_session`

                The type of the object. Always `existing_session`.

                - `:existing_session`

          - `timezone: String`

            The timezone used to interpret the expression.

            `minLength: 0`

          - `type: :periodic`

            The type of the object. Always `periodic`.

            - `:periodic`

        - `class OneTimeAutomation`

          Fields shared by periodic and one-time automations.

          - `id: String`

            The automation ID.

            `minLength: 0`

          - `created_at: Integer`

            The creation time as a Unix timestamp in seconds.

            `format: int64`

          - `created_by: AutomationCreatedBy`

            Service-recorded provenance; callers cannot supply this field.

          - `metadata: Hash[Symbol, String]`

            Custom string key-value pairs attached to the automation.

          - `name: String`

            The automation's display name.

            `minLength: 0`

          - `object: :"agent.automation"`

            Always `agent.automation`.

            - `:"agent.automation"`

          - `run_at: Integer`

            The Unix timestamp, in seconds, of the scheduled occurrence.

            `format: int64`

          - `status: :active | :paused | :completed`

            Completion means the schedule has finished, not the agent's work.

            - `:active`

            - `:paused`

            - `:completed`

          - `target: AutomationTarget`

            The session configuration or existing session receiving invocations.

          - `type: :once`

            The type of the object. Always `once`.

            - `:once`

      - `type: :automation`

        The type of the object. Always `automation`.

        - `:automation`

  - `status: :queued | :completed | :failed | :skipped`

    Delivery status; completed does not mean the agent's work has finished.

    - `:queued`

    - `:completed`

    - `:failed`

    - `:skipped`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

automation_invocation = openai.beta.agents.automations.invocations.create("automation_id")

puts(automation_invocation)
```

#### 200 — Example

```json
{
  "id": "id",
  "automation_id": "automation_id",
  "created_at": 0,
  "error": {
    "code": "code",
    "message": "message"
  },
  "object": "agent.automation.invocation",
  "scheduled_at": 0,
  "session_id": "session_id",
  "skip_reason": "pending_delivery",
  "source": {
    "type": "manual"
  },
  "status": "queued"
}
```

## List automation invocations

`beta.agents.automations.invocations.list(automation_id, **kwargs) -> CursorPage<AutomationInvocation>`

**get** `/agents/automations/{automation_id}/invocations`

Lists delivery records for a project-owned automation.

### Parameters

- `automation_id: String`

  `minLength: 0`, `maxLength: 1048576`

- `after: String`

  Return resources after this resource ID in the selected order.

  `minLength: 0`, `maxLength: 1048576`

- `limit: Integer`

  The maximum number of resources to return, between 1 and 100. Defaults to 20.

  `format: int64`, `minimum: 1`, `maximum: 100`

- `order: :asc | :desc`

  The order in which resources are returned. Defaults to `desc`.

  - `:asc`

    Returns resources in ascending order.

  - `:desc`

    Returns resources in descending order.

### Returns

- `class AutomationInvocation`

  One attempted delivery by an automation.

  - `id: String`

    The invocation ID.

    `minLength: 0`

  - `automation_id: String`

    The automation that owns the invocation.

    `minLength: 0`

  - `created_at: Integer`

    The creation time as a Unix timestamp in seconds.

    `format: int64`

  - `error: Error{ code, message}`

    The permanent delivery failure, or null when no failure occurred.

    - `code: String`

      A machine-readable error code.

      `minLength: 0`

    - `message: String`

      A public explanation of the delivery failure.

      `minLength: 0`

  - `object: :"agent.automation.invocation"`

    Always `agent.automation.invocation`.

    - `:"agent.automation.invocation"`

  - `scheduled_at: Integer`

    The intended occurrence as a Unix timestamp in seconds, or null for manual runs.

    `format: int64`

  - `session_id: String`

    The target or newly created session ID, or null before one is available.

    `minLength: 0`

  - `skip_reason: :pending_delivery`

    Why an occurrence was skipped, or null when it was not skipped.

    - `:pending_delivery`

  - `source: AutomationInvocationSource`

    Whether the invocation was manual or scheduled.

    - `class Manual`

      - `type: :manual`

        The type of the object. Always `manual`.

        - `:manual`

    - `class Automation`

      - `automation: Automation`

        The automation snapshot for this occurrence, excluding confidential values.

        - `class PeriodicAutomation`

          Fields shared by periodic and one-time automations.

          - `id: String`

            The automation ID.

            `minLength: 0`

          - `created_at: Integer`

            The creation time as a Unix timestamp in seconds.

            `format: int64`

          - `created_by: AutomationCreatedBy`

            Service-recorded provenance; callers cannot supply this field.

            - `class Developer`

              - `type: :developer`

                The type of the object. Always `developer`.

                - `:developer`

            - `class Agent`

              - `session_id: String`

                The creator session, which is also the automation's target.

                `minLength: 0`

              - `tool_call_id: String`

                The tool call that created the automation.

                `minLength: 0`

              - `type: :agent`

                The type of the object. Always `agent`.

                - `:agent`

          - `expression: String`

            The cron expression determining scheduled occurrences.

            `minLength: 0`

          - `metadata: Hash[Symbol, String]`

            Custom string key-value pairs attached to the automation.

          - `name: String`

            The automation's display name.

            `minLength: 0`

          - `object: :"agent.automation"`

            Always `agent.automation`.

            - `:"agent.automation"`

          - `status: :active | :paused`

            Whether scheduled delivery is active or paused.

            - `:active`

            - `:paused`

          - `target: AutomationTarget`

            The session configuration or existing session receiving invocations.

            - `class NewSession`

              - `agent: AutomationAgentConfig`

                The inline agent configuration, or null when agent_id is configured.

                - `instructions: String`

                  Custom instructions, or null when absent.

                  `minLength: 0`

                - `model: String`

                  The requested model name.

                  `minLength: 0`

                - `multi_agent: MultiAgentConfig`

                  The configuration for creating and coordinating subagents.

                  - `enabled: bool`

                    Whether subagent tools are enabled. Defaults to false.

                  - `max_concurrent_subagents: Integer`

                    Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

                    `format: int64`, `minimum: 1`, `maximum: 4294967295`

                - `reasoning: AgentReasoning`

                  The configured reasoning policy.

                  - `effort: :none | :minimal | :low | 4 more`

                    The requested reasoning effort, or `null` when the model selects its own default.

                    - `:none`

                    - `:minimal`

                    - `:low`

                    - `:medium`

                    - `:high`

                    - `:xhigh`

                    - `:max`

                  - `summary: :concise | :detailed | :auto`

                    The requested reasoning summary format, or `null` when summaries are disabled.

                    - `:concise`

                      Returns a concise reasoning summary when supported.

                    - `:detailed`

                      Returns a detailed reasoning summary when supported.

                    - `:auto`

                      Automatically selects the most detailed summary supported by the model.

                - `service_tier: :auto | :default | :flex | 3 more`

                  The configured service-tier policy.

                  - `:auto`

                  - `:default`

                  - `:flex`

                  - `:priority`

                  - `:fast`

                  - `:ultrafast`

                - `text: AgentText`

                  The configured output format and verbosity.

                  - `format_: TextFormat`

                    The effective output format. Defaults to ordinary text.

                    - `class Text`

                      Generates ordinary text without a structured-output constraint.

                      - `type: :text`

                        The type of the object. Always `text`.

                        - `:text`

                    - `class JSONSchema`

                      Constrains generated text to a JSON Schema.

                      - `schema: Hash[Symbol, untyped]`

                        The JSON Schema that generated text must match.

                      - `type: :json_schema`

                        The type of the object. Always `json_schema`.

                        - `:json_schema`

                  - `verbosity: :low | :medium | :high`

                    The amount of text produced by the agent. Defaults to `medium`.

                    - `:low`

                    - `:medium`

                    - `:high`

                - `tools: Array[AgentTool]`

                  Configured tools, excluding confidential credentials.

                  `minItems: 0`, `maxItems: 2000`

                  - `class Function`

                    A function defined by the application.

                    - `defer_loading: bool`

                      Whether the function is deferred and discovered through tool search.

                    - `description: String`

                      A description of what the function does.

                      `minLength: 0`

                    - `name: String`

                      The name of the function.

                      `minLength: 0`

                    - `parameters: Hash[Symbol, untyped]`

                      A JSON Schema object describing the function's arguments.

                    - `type: :function`

                      The type of the object. Always `function`.

                      - `:function`

                    - `async: bool`

                      Whether the agent continues without waiting for the function result.

                  - `class ProgrammaticToolCalling`

                    Enables calling tools from model-generated code.

                    - `enabled: bool`

                      Whether tools can be called from model-generated code.

                    - `type: :programmatic_tool_calling`

                      The type of the object. Always `programmatic_tool_calling`.

                      - `:programmatic_tool_calling`

                  - `class Mcp`

                    Tools provided by a remote MCP server.

                    - `allowed_tools: Array[String]`

                      The MCP tools the agent may call.

                      `minItems: 0`, `maxItems: 2000`

                    - `connection_origin: :service | :environment`

                      Where outbound MCP HTTP connections originate.

                      - `:service`

                      - `:environment`

                    - `credential_id: String`

                      The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

                      `minLength: 0`

                    - `request_metadata: Hash[Symbol, untyped]`

                      Metadata included with requests to this MCP server.

                    - `required: bool`

                      Whether this MCP server must initialize before the first turn.

                    - `server_label: String`

                      A label used to identify the MCP server in tool calls.

                      `minLength: 0`

                    - `transport: McpTransport`

                      The transport used to connect to the MCP server.

                      - `class HTTP`

                        Connects to an MCP server over HTTP.

                        - `server_url: String`

                          The URL of the MCP server.

                          `minLength: 0`

                        - `type: :http`

                          The type of the object. Always `http`.

                          - `:http`

                      - `class Stdio`

                        Starts an MCP server as a local process.

                        - `args: Array[String]`

                          Arguments passed to the MCP server command.

                          `minItems: 0`, `maxItems: 2000`

                        - `command: String`

                          The command used to start the MCP server.

                          `minLength: 0`

                        - `cwd: String`

                          The working directory used to start the MCP server.

                          `minLength: 0`

                        - `env_vars: Array[String]`

                          Environment variable names inherited from the execution environment.

                          `minItems: 0`, `maxItems: 2000`

                        - `type: :stdio`

                          The type of the object. Always `stdio`.

                          - `:stdio`

                    - `type: :mcp`

                      The type of the object. Always `mcp`.

                      - `:mcp`

                  - `class WebSearch`

                    Web search.

                    - `allowed_domains: Array[String]`

                      Allowed search domains, or `null` when the search is unrestricted.

                      `minItems: 0`, `maxItems: 2000`

                    - `context_size: :low | :medium | :high`

                      The amount of search context made available to the model. Defaults to `medium`.

                      - `:low`

                      - `:medium`

                      - `:high`

                    - `location: Location{ city, country, region, timezone}`

                      Approximate location used to localize search results, if provided.

                      - `city: String`

                        The city name.

                        `minLength: 0`

                      - `country: String`

                        The two-letter ISO country code, such as `US`.

                        `minLength: 0`

                      - `region: String`

                        The region or state name.

                        `minLength: 0`

                      - `timezone: String`

                        The IANA timezone, such as `America/Los_Angeles`.

                        `minLength: 0`

                    - `mode: :disabled | :cached | :live`

                      The source used for web search results.

                      - `:disabled`

                      - `:cached`

                      - `:live`

                    - `type: :web_search`

                      The type of the object. Always `web_search`.

                      - `:web_search`

                  - `class ComputerUse`

                    Browser use in an OpenAI-hosted session.

                    - `include_screenshots: bool`

                      Whether computer tool outputs include screenshots.

                    - `type: :computer_use`

                      The type of the object. Always `computer_use`.

                      - `:computer_use`

                  - `class Automations`

                    Lets the agent manage its own scheduled wakeups.

                    - `type: :automations`

                      The type of the object. Always `automations`.

                      - `:automations`

                - `compaction: Compaction{ async}`

                  The effective context compaction settings.

                  - `async: bool`

                    Whether context is compacted in the background. Defaults to true.

                - `experimental: Experimental{ time_awareness}`

                  The effective experimental settings for the agent.

                  - `time_awareness: bool`

                    Whether the model receives periodic current-time reminders.

              - `agent_id: String`

                The saved agent reference, or null when an inline agent is configured.

                `minLength: 0`

              - `environment: AutomationEnvironment`

                Configuration or references used to select the execution environment.

                - `class None`

                  - `type: :none`

                    The type of the object. Always `none`.

                    - `:none`

                - `class OpenAIHosted`

                  Hosted environment selection with confidential setup commands and variables omitted.

                  - `capability_directories: Array[String]`

                    Directory overrides, or null to inherit the template or creation default.

                    `minItems: 0`, `maxItems: 2000`

                  - `container_size: :small | :medium | :large`

                    The configured container size, or null to use the creation default.

                    - `:small`

                    - `:medium`

                    - `:large`

                  - `desktop: Desktop{ enabled}`

                    Desktop overrides, or null to inherit the template or creation default.

                    - `enabled: bool`

                      Whether the environment provisions a desktop and browser proxy.

                  - `environment_id: String`

                    An existing environment reference, or null when provisioning a new environment.

                    `minLength: 0`

                  - `environment_template_id: String`

                    A template reference, or null when no template is selected.

                    `minLength: 0`

                  - `files: Array[FileID{ file_id, path, type} | Inline{ path, size_bytes, type}]`

                    File overrides, excluding contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `class FileID`

                      A project-scoped Files API reference resolved separately for each session.

                      - `file_id: String`

                        The ID of the uploaded file.

                        `minLength: 0`

                      - `path: String`

                        The file's absolute path inside the environment.

                        `minLength: 0`

                      - `type: :file_id`

                        The type of the object. Always `file_id`.

                        - `:file_id`

                    - `class Inline`

                      Metadata for confidential inline file contents.

                      - `path: String`

                        The file's absolute path inside the environment.

                        `minLength: 0`

                      - `size_bytes: Integer`

                        The decoded size of the inline file in bytes.

                        `format: int64`, `minimum: 0`

                      - `type: :inline`

                        The type of the object. Always `inline`.

                        - `:inline`

                  - `network: Network{ access, allowed_domains}`

                    Network overrides, or null to inherit the template or creation default.

                    - `access: :enabled | :disabled | :restricted`

                      The environment's network access mode.

                      - `:enabled`

                        Allows unrestricted network access.

                      - `:disabled`

                        Disables network access.

                      - `:restricted`

                        Applies the configured domain restrictions.

                    - `allowed_domains: Array[String]`

                      Domains the environment may access when network access is restricted.

                      `minItems: 0`, `maxItems: 2000`

                  - `packages: Packages{ npm, python, system_}`

                    Package overrides, or null to inherit the template or creation default.

                    - `npm: Array[String]`

                      npm packages installed globally in the environment.

                      `minItems: 0`, `maxItems: 16384`

                    - `python: Array[String]`

                      Python packages installed in the environment.

                      `minItems: 0`, `maxItems: 16384`

                    - `system_: Array[String]`

                      System packages installed in the environment.

                      `minItems: 0`, `maxItems: 16384`

                  - `plugins: Array[HostedPlugin]`

                    Plugin overrides, excluding archive contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `description: String`

                      The installed plugin description.

                      `minLength: 0`

                    - `name: String`

                      The installed plugin name.

                      `minLength: 0`

                    - `type: :inline`

                      The type of the object. Always `inline`.

                      - `:inline`

                  - `skills: Array[SkillReference{ skill_id, type, version} | Inline{ description, name, type}]`

                    Skill overrides, excluding archive contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `class SkillReference`

                      A skill resolved afresh from the Skills API whenever a session starts.

                      - `skill_id: String`

                        The referenced skill ID.

                        `minLength: 0`

                      - `type: :skill_reference`

                        The type of the object. Always `skill_reference`.

                        - `:skill_reference`

                      - `version: String`

                        The requested version selector, including `latest`.

                        `minLength: 0`

                    - `class Inline`

                      Safe metadata for an inline skill archive.

                      - `description: String`

                        The skill description declared in `SKILL.md`.

                        `minLength: 0`

                      - `name: String`

                        The skill name declared in `SKILL.md`.

                        `minLength: 0`

                      - `type: :inline`

                        The type of the object. Always `inline`.

                        - `:inline`

                  - `type: :openai_hosted`

                    The type of the object. Always `openai_hosted`.

                    - `:openai_hosted`

                - `class SelfHosted`

                  - `capability_directories: Array[String]`

                    Directories that expose capabilities to the agent.

                    `minItems: 0`, `maxItems: 2000`

                  - `environment_id: String`

                    An existing registration, or null to create a session-owned environment.

                    `minLength: 0`

                  - `type: :self_hosted`

                    The type of the object. Always `self_hosted`.

                    - `:self_hosted`

                  - `workspace_directory: String`

                    The absolute project directory in the environment.

                    `minLength: 0`

              - `input: Array[Input{ content, role, type}]`

                Initial input delivered to each new session.

                `minItems: 0`, `maxItems: 2000`

                - `content: Array[InputContent]`

                  The content of the message.

                  `minItems: 0`, `maxItems: 2000`

                  - `class InputText`

                    Text input recorded in a session item.

                    - `text: String`

                      The text supplied to the agent.

                      `minLength: 0`

                    - `type: :input_text`

                      The type of the object. Always `input_text`.

                      - `:input_text`

                  - `class InputImage`

                    Image input recorded in a session item.

                    - `image_url: String`

                      The URL of the image supplied to the agent, which may be a base64-encoded data URL.

                      `minLength: 0`

                    - `type: :input_image`

                      The type of the object. Always `input_image`.

                      - `:input_image`

                - `role: :user`

                  The role of the message author. Always `user`.

                  - `:user`

                - `type: :message`

                  The type of the input item. Always `message`.

                  - `:message`

              - `metadata: Hash[Symbol, String]`

                Metadata attached to each new session.

              - `type: :new_session`

                The type of the object. Always `new_session`.

                - `:new_session`

              - `vault_ids: Array[String]`

                Vaults made available to each new session.

                `minItems: 0`, `maxItems: 2000`

            - `class ExistingSession`

              - `instructions: String`

                Saved instructions delivered as an automation notification.

                `minLength: 0`

              - `session_id: String`

                The session receiving each invocation.

                `minLength: 0`

              - `type: :existing_session`

                The type of the object. Always `existing_session`.

                - `:existing_session`

          - `timezone: String`

            The timezone used to interpret the expression.

            `minLength: 0`

          - `type: :periodic`

            The type of the object. Always `periodic`.

            - `:periodic`

        - `class OneTimeAutomation`

          Fields shared by periodic and one-time automations.

          - `id: String`

            The automation ID.

            `minLength: 0`

          - `created_at: Integer`

            The creation time as a Unix timestamp in seconds.

            `format: int64`

          - `created_by: AutomationCreatedBy`

            Service-recorded provenance; callers cannot supply this field.

          - `metadata: Hash[Symbol, String]`

            Custom string key-value pairs attached to the automation.

          - `name: String`

            The automation's display name.

            `minLength: 0`

          - `object: :"agent.automation"`

            Always `agent.automation`.

            - `:"agent.automation"`

          - `run_at: Integer`

            The Unix timestamp, in seconds, of the scheduled occurrence.

            `format: int64`

          - `status: :active | :paused | :completed`

            Completion means the schedule has finished, not the agent's work.

            - `:active`

            - `:paused`

            - `:completed`

          - `target: AutomationTarget`

            The session configuration or existing session receiving invocations.

          - `type: :once`

            The type of the object. Always `once`.

            - `:once`

      - `type: :automation`

        The type of the object. Always `automation`.

        - `:automation`

  - `status: :queued | :completed | :failed | :skipped`

    Delivery status; completed does not mean the agent's work has finished.

    - `:queued`

    - `:completed`

    - `:failed`

    - `:skipped`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.beta.agents.automations.invocations.list("automation_id")

puts(page)
```

#### 200 — Example

```json
{
  "data": [
    {
      "id": "id",
      "automation_id": "automation_id",
      "created_at": 0,
      "error": {
        "code": "code",
        "message": "message"
      },
      "object": "agent.automation.invocation",
      "scheduled_at": 0,
      "session_id": "session_id",
      "skip_reason": "pending_delivery",
      "source": {
        "type": "manual"
      },
      "status": "queued"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Get an automation invocation

`beta.agents.automations.invocations.retrieve(invocation_id, **kwargs) -> AutomationInvocation`

**get** `/agents/automations/{automation_id}/invocations/{invocation_id}`

Retrieves a delivery record for a project-owned automation.

### Parameters

- `automation_id: String`

  `minLength: 0`, `maxLength: 1048576`

- `invocation_id: String`

  `minLength: 0`, `maxLength: 1048576`

### Returns

- `class AutomationInvocation`

  One attempted delivery by an automation.

  - `id: String`

    The invocation ID.

    `minLength: 0`

  - `automation_id: String`

    The automation that owns the invocation.

    `minLength: 0`

  - `created_at: Integer`

    The creation time as a Unix timestamp in seconds.

    `format: int64`

  - `error: Error{ code, message}`

    The permanent delivery failure, or null when no failure occurred.

    - `code: String`

      A machine-readable error code.

      `minLength: 0`

    - `message: String`

      A public explanation of the delivery failure.

      `minLength: 0`

  - `object: :"agent.automation.invocation"`

    Always `agent.automation.invocation`.

    - `:"agent.automation.invocation"`

  - `scheduled_at: Integer`

    The intended occurrence as a Unix timestamp in seconds, or null for manual runs.

    `format: int64`

  - `session_id: String`

    The target or newly created session ID, or null before one is available.

    `minLength: 0`

  - `skip_reason: :pending_delivery`

    Why an occurrence was skipped, or null when it was not skipped.

    - `:pending_delivery`

  - `source: AutomationInvocationSource`

    Whether the invocation was manual or scheduled.

    - `class Manual`

      - `type: :manual`

        The type of the object. Always `manual`.

        - `:manual`

    - `class Automation`

      - `automation: Automation`

        The automation snapshot for this occurrence, excluding confidential values.

        - `class PeriodicAutomation`

          Fields shared by periodic and one-time automations.

          - `id: String`

            The automation ID.

            `minLength: 0`

          - `created_at: Integer`

            The creation time as a Unix timestamp in seconds.

            `format: int64`

          - `created_by: AutomationCreatedBy`

            Service-recorded provenance; callers cannot supply this field.

            - `class Developer`

              - `type: :developer`

                The type of the object. Always `developer`.

                - `:developer`

            - `class Agent`

              - `session_id: String`

                The creator session, which is also the automation's target.

                `minLength: 0`

              - `tool_call_id: String`

                The tool call that created the automation.

                `minLength: 0`

              - `type: :agent`

                The type of the object. Always `agent`.

                - `:agent`

          - `expression: String`

            The cron expression determining scheduled occurrences.

            `minLength: 0`

          - `metadata: Hash[Symbol, String]`

            Custom string key-value pairs attached to the automation.

          - `name: String`

            The automation's display name.

            `minLength: 0`

          - `object: :"agent.automation"`

            Always `agent.automation`.

            - `:"agent.automation"`

          - `status: :active | :paused`

            Whether scheduled delivery is active or paused.

            - `:active`

            - `:paused`

          - `target: AutomationTarget`

            The session configuration or existing session receiving invocations.

            - `class NewSession`

              - `agent: AutomationAgentConfig`

                The inline agent configuration, or null when agent_id is configured.

                - `instructions: String`

                  Custom instructions, or null when absent.

                  `minLength: 0`

                - `model: String`

                  The requested model name.

                  `minLength: 0`

                - `multi_agent: MultiAgentConfig`

                  The configuration for creating and coordinating subagents.

                  - `enabled: bool`

                    Whether subagent tools are enabled. Defaults to false.

                  - `max_concurrent_subagents: Integer`

                    Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

                    `format: int64`, `minimum: 1`, `maximum: 4294967295`

                - `reasoning: AgentReasoning`

                  The configured reasoning policy.

                  - `effort: :none | :minimal | :low | 4 more`

                    The requested reasoning effort, or `null` when the model selects its own default.

                    - `:none`

                    - `:minimal`

                    - `:low`

                    - `:medium`

                    - `:high`

                    - `:xhigh`

                    - `:max`

                  - `summary: :concise | :detailed | :auto`

                    The requested reasoning summary format, or `null` when summaries are disabled.

                    - `:concise`

                      Returns a concise reasoning summary when supported.

                    - `:detailed`

                      Returns a detailed reasoning summary when supported.

                    - `:auto`

                      Automatically selects the most detailed summary supported by the model.

                - `service_tier: :auto | :default | :flex | 3 more`

                  The configured service-tier policy.

                  - `:auto`

                  - `:default`

                  - `:flex`

                  - `:priority`

                  - `:fast`

                  - `:ultrafast`

                - `text: AgentText`

                  The configured output format and verbosity.

                  - `format_: TextFormat`

                    The effective output format. Defaults to ordinary text.

                    - `class Text`

                      Generates ordinary text without a structured-output constraint.

                      - `type: :text`

                        The type of the object. Always `text`.

                        - `:text`

                    - `class JSONSchema`

                      Constrains generated text to a JSON Schema.

                      - `schema: Hash[Symbol, untyped]`

                        The JSON Schema that generated text must match.

                      - `type: :json_schema`

                        The type of the object. Always `json_schema`.

                        - `:json_schema`

                  - `verbosity: :low | :medium | :high`

                    The amount of text produced by the agent. Defaults to `medium`.

                    - `:low`

                    - `:medium`

                    - `:high`

                - `tools: Array[AgentTool]`

                  Configured tools, excluding confidential credentials.

                  `minItems: 0`, `maxItems: 2000`

                  - `class Function`

                    A function defined by the application.

                    - `defer_loading: bool`

                      Whether the function is deferred and discovered through tool search.

                    - `description: String`

                      A description of what the function does.

                      `minLength: 0`

                    - `name: String`

                      The name of the function.

                      `minLength: 0`

                    - `parameters: Hash[Symbol, untyped]`

                      A JSON Schema object describing the function's arguments.

                    - `type: :function`

                      The type of the object. Always `function`.

                      - `:function`

                    - `async: bool`

                      Whether the agent continues without waiting for the function result.

                  - `class ProgrammaticToolCalling`

                    Enables calling tools from model-generated code.

                    - `enabled: bool`

                      Whether tools can be called from model-generated code.

                    - `type: :programmatic_tool_calling`

                      The type of the object. Always `programmatic_tool_calling`.

                      - `:programmatic_tool_calling`

                  - `class Mcp`

                    Tools provided by a remote MCP server.

                    - `allowed_tools: Array[String]`

                      The MCP tools the agent may call.

                      `minItems: 0`, `maxItems: 2000`

                    - `connection_origin: :service | :environment`

                      Where outbound MCP HTTP connections originate.

                      - `:service`

                      - `:environment`

                    - `credential_id: String`

                      The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

                      `minLength: 0`

                    - `request_metadata: Hash[Symbol, untyped]`

                      Metadata included with requests to this MCP server.

                    - `required: bool`

                      Whether this MCP server must initialize before the first turn.

                    - `server_label: String`

                      A label used to identify the MCP server in tool calls.

                      `minLength: 0`

                    - `transport: McpTransport`

                      The transport used to connect to the MCP server.

                      - `class HTTP`

                        Connects to an MCP server over HTTP.

                        - `server_url: String`

                          The URL of the MCP server.

                          `minLength: 0`

                        - `type: :http`

                          The type of the object. Always `http`.

                          - `:http`

                      - `class Stdio`

                        Starts an MCP server as a local process.

                        - `args: Array[String]`

                          Arguments passed to the MCP server command.

                          `minItems: 0`, `maxItems: 2000`

                        - `command: String`

                          The command used to start the MCP server.

                          `minLength: 0`

                        - `cwd: String`

                          The working directory used to start the MCP server.

                          `minLength: 0`

                        - `env_vars: Array[String]`

                          Environment variable names inherited from the execution environment.

                          `minItems: 0`, `maxItems: 2000`

                        - `type: :stdio`

                          The type of the object. Always `stdio`.

                          - `:stdio`

                    - `type: :mcp`

                      The type of the object. Always `mcp`.

                      - `:mcp`

                  - `class WebSearch`

                    Web search.

                    - `allowed_domains: Array[String]`

                      Allowed search domains, or `null` when the search is unrestricted.

                      `minItems: 0`, `maxItems: 2000`

                    - `context_size: :low | :medium | :high`

                      The amount of search context made available to the model. Defaults to `medium`.

                      - `:low`

                      - `:medium`

                      - `:high`

                    - `location: Location{ city, country, region, timezone}`

                      Approximate location used to localize search results, if provided.

                      - `city: String`

                        The city name.

                        `minLength: 0`

                      - `country: String`

                        The two-letter ISO country code, such as `US`.

                        `minLength: 0`

                      - `region: String`

                        The region or state name.

                        `minLength: 0`

                      - `timezone: String`

                        The IANA timezone, such as `America/Los_Angeles`.

                        `minLength: 0`

                    - `mode: :disabled | :cached | :live`

                      The source used for web search results.

                      - `:disabled`

                      - `:cached`

                      - `:live`

                    - `type: :web_search`

                      The type of the object. Always `web_search`.

                      - `:web_search`

                  - `class ComputerUse`

                    Browser use in an OpenAI-hosted session.

                    - `include_screenshots: bool`

                      Whether computer tool outputs include screenshots.

                    - `type: :computer_use`

                      The type of the object. Always `computer_use`.

                      - `:computer_use`

                  - `class Automations`

                    Lets the agent manage its own scheduled wakeups.

                    - `type: :automations`

                      The type of the object. Always `automations`.

                      - `:automations`

                - `compaction: Compaction{ async}`

                  The effective context compaction settings.

                  - `async: bool`

                    Whether context is compacted in the background. Defaults to true.

                - `experimental: Experimental{ time_awareness}`

                  The effective experimental settings for the agent.

                  - `time_awareness: bool`

                    Whether the model receives periodic current-time reminders.

              - `agent_id: String`

                The saved agent reference, or null when an inline agent is configured.

                `minLength: 0`

              - `environment: AutomationEnvironment`

                Configuration or references used to select the execution environment.

                - `class None`

                  - `type: :none`

                    The type of the object. Always `none`.

                    - `:none`

                - `class OpenAIHosted`

                  Hosted environment selection with confidential setup commands and variables omitted.

                  - `capability_directories: Array[String]`

                    Directory overrides, or null to inherit the template or creation default.

                    `minItems: 0`, `maxItems: 2000`

                  - `container_size: :small | :medium | :large`

                    The configured container size, or null to use the creation default.

                    - `:small`

                    - `:medium`

                    - `:large`

                  - `desktop: Desktop{ enabled}`

                    Desktop overrides, or null to inherit the template or creation default.

                    - `enabled: bool`

                      Whether the environment provisions a desktop and browser proxy.

                  - `environment_id: String`

                    An existing environment reference, or null when provisioning a new environment.

                    `minLength: 0`

                  - `environment_template_id: String`

                    A template reference, or null when no template is selected.

                    `minLength: 0`

                  - `files: Array[FileID{ file_id, path, type} | Inline{ path, size_bytes, type}]`

                    File overrides, excluding contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `class FileID`

                      A project-scoped Files API reference resolved separately for each session.

                      - `file_id: String`

                        The ID of the uploaded file.

                        `minLength: 0`

                      - `path: String`

                        The file's absolute path inside the environment.

                        `minLength: 0`

                      - `type: :file_id`

                        The type of the object. Always `file_id`.

                        - `:file_id`

                    - `class Inline`

                      Metadata for confidential inline file contents.

                      - `path: String`

                        The file's absolute path inside the environment.

                        `minLength: 0`

                      - `size_bytes: Integer`

                        The decoded size of the inline file in bytes.

                        `format: int64`, `minimum: 0`

                      - `type: :inline`

                        The type of the object. Always `inline`.

                        - `:inline`

                  - `network: Network{ access, allowed_domains}`

                    Network overrides, or null to inherit the template or creation default.

                    - `access: :enabled | :disabled | :restricted`

                      The environment's network access mode.

                      - `:enabled`

                        Allows unrestricted network access.

                      - `:disabled`

                        Disables network access.

                      - `:restricted`

                        Applies the configured domain restrictions.

                    - `allowed_domains: Array[String]`

                      Domains the environment may access when network access is restricted.

                      `minItems: 0`, `maxItems: 2000`

                  - `packages: Packages{ npm, python, system_}`

                    Package overrides, or null to inherit the template or creation default.

                    - `npm: Array[String]`

                      npm packages installed globally in the environment.

                      `minItems: 0`, `maxItems: 16384`

                    - `python: Array[String]`

                      Python packages installed in the environment.

                      `minItems: 0`, `maxItems: 16384`

                    - `system_: Array[String]`

                      System packages installed in the environment.

                      `minItems: 0`, `maxItems: 16384`

                  - `plugins: Array[HostedPlugin]`

                    Plugin overrides, excluding archive contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `description: String`

                      The installed plugin description.

                      `minLength: 0`

                    - `name: String`

                      The installed plugin name.

                      `minLength: 0`

                    - `type: :inline`

                      The type of the object. Always `inline`.

                      - `:inline`

                  - `skills: Array[SkillReference{ skill_id, type, version} | Inline{ description, name, type}]`

                    Skill overrides, excluding archive contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `class SkillReference`

                      A skill resolved afresh from the Skills API whenever a session starts.

                      - `skill_id: String`

                        The referenced skill ID.

                        `minLength: 0`

                      - `type: :skill_reference`

                        The type of the object. Always `skill_reference`.

                        - `:skill_reference`

                      - `version: String`

                        The requested version selector, including `latest`.

                        `minLength: 0`

                    - `class Inline`

                      Safe metadata for an inline skill archive.

                      - `description: String`

                        The skill description declared in `SKILL.md`.

                        `minLength: 0`

                      - `name: String`

                        The skill name declared in `SKILL.md`.

                        `minLength: 0`

                      - `type: :inline`

                        The type of the object. Always `inline`.

                        - `:inline`

                  - `type: :openai_hosted`

                    The type of the object. Always `openai_hosted`.

                    - `:openai_hosted`

                - `class SelfHosted`

                  - `capability_directories: Array[String]`

                    Directories that expose capabilities to the agent.

                    `minItems: 0`, `maxItems: 2000`

                  - `environment_id: String`

                    An existing registration, or null to create a session-owned environment.

                    `minLength: 0`

                  - `type: :self_hosted`

                    The type of the object. Always `self_hosted`.

                    - `:self_hosted`

                  - `workspace_directory: String`

                    The absolute project directory in the environment.

                    `minLength: 0`

              - `input: Array[Input{ content, role, type}]`

                Initial input delivered to each new session.

                `minItems: 0`, `maxItems: 2000`

                - `content: Array[InputContent]`

                  The content of the message.

                  `minItems: 0`, `maxItems: 2000`

                  - `class InputText`

                    Text input recorded in a session item.

                    - `text: String`

                      The text supplied to the agent.

                      `minLength: 0`

                    - `type: :input_text`

                      The type of the object. Always `input_text`.

                      - `:input_text`

                  - `class InputImage`

                    Image input recorded in a session item.

                    - `image_url: String`

                      The URL of the image supplied to the agent, which may be a base64-encoded data URL.

                      `minLength: 0`

                    - `type: :input_image`

                      The type of the object. Always `input_image`.

                      - `:input_image`

                - `role: :user`

                  The role of the message author. Always `user`.

                  - `:user`

                - `type: :message`

                  The type of the input item. Always `message`.

                  - `:message`

              - `metadata: Hash[Symbol, String]`

                Metadata attached to each new session.

              - `type: :new_session`

                The type of the object. Always `new_session`.

                - `:new_session`

              - `vault_ids: Array[String]`

                Vaults made available to each new session.

                `minItems: 0`, `maxItems: 2000`

            - `class ExistingSession`

              - `instructions: String`

                Saved instructions delivered as an automation notification.

                `minLength: 0`

              - `session_id: String`

                The session receiving each invocation.

                `minLength: 0`

              - `type: :existing_session`

                The type of the object. Always `existing_session`.

                - `:existing_session`

          - `timezone: String`

            The timezone used to interpret the expression.

            `minLength: 0`

          - `type: :periodic`

            The type of the object. Always `periodic`.

            - `:periodic`

        - `class OneTimeAutomation`

          Fields shared by periodic and one-time automations.

          - `id: String`

            The automation ID.

            `minLength: 0`

          - `created_at: Integer`

            The creation time as a Unix timestamp in seconds.

            `format: int64`

          - `created_by: AutomationCreatedBy`

            Service-recorded provenance; callers cannot supply this field.

          - `metadata: Hash[Symbol, String]`

            Custom string key-value pairs attached to the automation.

          - `name: String`

            The automation's display name.

            `minLength: 0`

          - `object: :"agent.automation"`

            Always `agent.automation`.

            - `:"agent.automation"`

          - `run_at: Integer`

            The Unix timestamp, in seconds, of the scheduled occurrence.

            `format: int64`

          - `status: :active | :paused | :completed`

            Completion means the schedule has finished, not the agent's work.

            - `:active`

            - `:paused`

            - `:completed`

          - `target: AutomationTarget`

            The session configuration or existing session receiving invocations.

          - `type: :once`

            The type of the object. Always `once`.

            - `:once`

      - `type: :automation`

        The type of the object. Always `automation`.

        - `:automation`

  - `status: :queued | :completed | :failed | :skipped`

    Delivery status; completed does not mean the agent's work has finished.

    - `:queued`

    - `:completed`

    - `:failed`

    - `:skipped`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

automation_invocation = openai.beta.agents.automations.invocations.retrieve("invocation_id", automation_id: "automation_id")

puts(automation_invocation)
```

#### 200 — Example

```json
{
  "id": "id",
  "automation_id": "automation_id",
  "created_at": 0,
  "error": {
    "code": "code",
    "message": "message"
  },
  "object": "agent.automation.invocation",
  "scheduled_at": 0,
  "session_id": "session_id",
  "skip_reason": "pending_delivery",
  "source": {
    "type": "manual"
  },
  "status": "queued"
}
```

## Domain Types

### Automation Invocation

- `class AutomationInvocation`

  One attempted delivery by an automation.

  - `id: String`

    The invocation ID.

    `minLength: 0`

  - `automation_id: String`

    The automation that owns the invocation.

    `minLength: 0`

  - `created_at: Integer`

    The creation time as a Unix timestamp in seconds.

    `format: int64`

  - `error: Error{ code, message}`

    The permanent delivery failure, or null when no failure occurred.

    - `code: String`

      A machine-readable error code.

      `minLength: 0`

    - `message: String`

      A public explanation of the delivery failure.

      `minLength: 0`

  - `object: :"agent.automation.invocation"`

    Always `agent.automation.invocation`.

    - `:"agent.automation.invocation"`

  - `scheduled_at: Integer`

    The intended occurrence as a Unix timestamp in seconds, or null for manual runs.

    `format: int64`

  - `session_id: String`

    The target or newly created session ID, or null before one is available.

    `minLength: 0`

  - `skip_reason: :pending_delivery`

    Why an occurrence was skipped, or null when it was not skipped.

    - `:pending_delivery`

  - `source: AutomationInvocationSource`

    Whether the invocation was manual or scheduled.

    - `class Manual`

      - `type: :manual`

        The type of the object. Always `manual`.

        - `:manual`

    - `class Automation`

      - `automation: Automation`

        The automation snapshot for this occurrence, excluding confidential values.

        - `class PeriodicAutomation`

          Fields shared by periodic and one-time automations.

          - `id: String`

            The automation ID.

            `minLength: 0`

          - `created_at: Integer`

            The creation time as a Unix timestamp in seconds.

            `format: int64`

          - `created_by: AutomationCreatedBy`

            Service-recorded provenance; callers cannot supply this field.

            - `class Developer`

              - `type: :developer`

                The type of the object. Always `developer`.

                - `:developer`

            - `class Agent`

              - `session_id: String`

                The creator session, which is also the automation's target.

                `minLength: 0`

              - `tool_call_id: String`

                The tool call that created the automation.

                `minLength: 0`

              - `type: :agent`

                The type of the object. Always `agent`.

                - `:agent`

          - `expression: String`

            The cron expression determining scheduled occurrences.

            `minLength: 0`

          - `metadata: Hash[Symbol, String]`

            Custom string key-value pairs attached to the automation.

          - `name: String`

            The automation's display name.

            `minLength: 0`

          - `object: :"agent.automation"`

            Always `agent.automation`.

            - `:"agent.automation"`

          - `status: :active | :paused`

            Whether scheduled delivery is active or paused.

            - `:active`

            - `:paused`

          - `target: AutomationTarget`

            The session configuration or existing session receiving invocations.

            - `class NewSession`

              - `agent: AutomationAgentConfig`

                The inline agent configuration, or null when agent_id is configured.

                - `instructions: String`

                  Custom instructions, or null when absent.

                  `minLength: 0`

                - `model: String`

                  The requested model name.

                  `minLength: 0`

                - `multi_agent: MultiAgentConfig`

                  The configuration for creating and coordinating subagents.

                  - `enabled: bool`

                    Whether subagent tools are enabled. Defaults to false.

                  - `max_concurrent_subagents: Integer`

                    Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

                    `format: int64`, `minimum: 1`, `maximum: 4294967295`

                - `reasoning: AgentReasoning`

                  The configured reasoning policy.

                  - `effort: :none | :minimal | :low | 4 more`

                    The requested reasoning effort, or `null` when the model selects its own default.

                    - `:none`

                    - `:minimal`

                    - `:low`

                    - `:medium`

                    - `:high`

                    - `:xhigh`

                    - `:max`

                  - `summary: :concise | :detailed | :auto`

                    The requested reasoning summary format, or `null` when summaries are disabled.

                    - `:concise`

                      Returns a concise reasoning summary when supported.

                    - `:detailed`

                      Returns a detailed reasoning summary when supported.

                    - `:auto`

                      Automatically selects the most detailed summary supported by the model.

                - `service_tier: :auto | :default | :flex | 3 more`

                  The configured service-tier policy.

                  - `:auto`

                  - `:default`

                  - `:flex`

                  - `:priority`

                  - `:fast`

                  - `:ultrafast`

                - `text: AgentText`

                  The configured output format and verbosity.

                  - `format_: TextFormat`

                    The effective output format. Defaults to ordinary text.

                    - `class Text`

                      Generates ordinary text without a structured-output constraint.

                      - `type: :text`

                        The type of the object. Always `text`.

                        - `:text`

                    - `class JSONSchema`

                      Constrains generated text to a JSON Schema.

                      - `schema: Hash[Symbol, untyped]`

                        The JSON Schema that generated text must match.

                      - `type: :json_schema`

                        The type of the object. Always `json_schema`.

                        - `:json_schema`

                  - `verbosity: :low | :medium | :high`

                    The amount of text produced by the agent. Defaults to `medium`.

                    - `:low`

                    - `:medium`

                    - `:high`

                - `tools: Array[AgentTool]`

                  Configured tools, excluding confidential credentials.

                  `minItems: 0`, `maxItems: 2000`

                  - `class Function`

                    A function defined by the application.

                    - `defer_loading: bool`

                      Whether the function is deferred and discovered through tool search.

                    - `description: String`

                      A description of what the function does.

                      `minLength: 0`

                    - `name: String`

                      The name of the function.

                      `minLength: 0`

                    - `parameters: Hash[Symbol, untyped]`

                      A JSON Schema object describing the function's arguments.

                    - `type: :function`

                      The type of the object. Always `function`.

                      - `:function`

                    - `async: bool`

                      Whether the agent continues without waiting for the function result.

                  - `class ProgrammaticToolCalling`

                    Enables calling tools from model-generated code.

                    - `enabled: bool`

                      Whether tools can be called from model-generated code.

                    - `type: :programmatic_tool_calling`

                      The type of the object. Always `programmatic_tool_calling`.

                      - `:programmatic_tool_calling`

                  - `class Mcp`

                    Tools provided by a remote MCP server.

                    - `allowed_tools: Array[String]`

                      The MCP tools the agent may call.

                      `minItems: 0`, `maxItems: 2000`

                    - `connection_origin: :service | :environment`

                      Where outbound MCP HTTP connections originate.

                      - `:service`

                      - `:environment`

                    - `credential_id: String`

                      The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

                      `minLength: 0`

                    - `request_metadata: Hash[Symbol, untyped]`

                      Metadata included with requests to this MCP server.

                    - `required: bool`

                      Whether this MCP server must initialize before the first turn.

                    - `server_label: String`

                      A label used to identify the MCP server in tool calls.

                      `minLength: 0`

                    - `transport: McpTransport`

                      The transport used to connect to the MCP server.

                      - `class HTTP`

                        Connects to an MCP server over HTTP.

                        - `server_url: String`

                          The URL of the MCP server.

                          `minLength: 0`

                        - `type: :http`

                          The type of the object. Always `http`.

                          - `:http`

                      - `class Stdio`

                        Starts an MCP server as a local process.

                        - `args: Array[String]`

                          Arguments passed to the MCP server command.

                          `minItems: 0`, `maxItems: 2000`

                        - `command: String`

                          The command used to start the MCP server.

                          `minLength: 0`

                        - `cwd: String`

                          The working directory used to start the MCP server.

                          `minLength: 0`

                        - `env_vars: Array[String]`

                          Environment variable names inherited from the execution environment.

                          `minItems: 0`, `maxItems: 2000`

                        - `type: :stdio`

                          The type of the object. Always `stdio`.

                          - `:stdio`

                    - `type: :mcp`

                      The type of the object. Always `mcp`.

                      - `:mcp`

                  - `class WebSearch`

                    Web search.

                    - `allowed_domains: Array[String]`

                      Allowed search domains, or `null` when the search is unrestricted.

                      `minItems: 0`, `maxItems: 2000`

                    - `context_size: :low | :medium | :high`

                      The amount of search context made available to the model. Defaults to `medium`.

                      - `:low`

                      - `:medium`

                      - `:high`

                    - `location: Location{ city, country, region, timezone}`

                      Approximate location used to localize search results, if provided.

                      - `city: String`

                        The city name.

                        `minLength: 0`

                      - `country: String`

                        The two-letter ISO country code, such as `US`.

                        `minLength: 0`

                      - `region: String`

                        The region or state name.

                        `minLength: 0`

                      - `timezone: String`

                        The IANA timezone, such as `America/Los_Angeles`.

                        `minLength: 0`

                    - `mode: :disabled | :cached | :live`

                      The source used for web search results.

                      - `:disabled`

                      - `:cached`

                      - `:live`

                    - `type: :web_search`

                      The type of the object. Always `web_search`.

                      - `:web_search`

                  - `class ComputerUse`

                    Browser use in an OpenAI-hosted session.

                    - `include_screenshots: bool`

                      Whether computer tool outputs include screenshots.

                    - `type: :computer_use`

                      The type of the object. Always `computer_use`.

                      - `:computer_use`

                  - `class Automations`

                    Lets the agent manage its own scheduled wakeups.

                    - `type: :automations`

                      The type of the object. Always `automations`.

                      - `:automations`

                - `compaction: Compaction{ async}`

                  The effective context compaction settings.

                  - `async: bool`

                    Whether context is compacted in the background. Defaults to true.

                - `experimental: Experimental{ time_awareness}`

                  The effective experimental settings for the agent.

                  - `time_awareness: bool`

                    Whether the model receives periodic current-time reminders.

              - `agent_id: String`

                The saved agent reference, or null when an inline agent is configured.

                `minLength: 0`

              - `environment: AutomationEnvironment`

                Configuration or references used to select the execution environment.

                - `class None`

                  - `type: :none`

                    The type of the object. Always `none`.

                    - `:none`

                - `class OpenAIHosted`

                  Hosted environment selection with confidential setup commands and variables omitted.

                  - `capability_directories: Array[String]`

                    Directory overrides, or null to inherit the template or creation default.

                    `minItems: 0`, `maxItems: 2000`

                  - `container_size: :small | :medium | :large`

                    The configured container size, or null to use the creation default.

                    - `:small`

                    - `:medium`

                    - `:large`

                  - `desktop: Desktop{ enabled}`

                    Desktop overrides, or null to inherit the template or creation default.

                    - `enabled: bool`

                      Whether the environment provisions a desktop and browser proxy.

                  - `environment_id: String`

                    An existing environment reference, or null when provisioning a new environment.

                    `minLength: 0`

                  - `environment_template_id: String`

                    A template reference, or null when no template is selected.

                    `minLength: 0`

                  - `files: Array[FileID{ file_id, path, type} | Inline{ path, size_bytes, type}]`

                    File overrides, excluding contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `class FileID`

                      A project-scoped Files API reference resolved separately for each session.

                      - `file_id: String`

                        The ID of the uploaded file.

                        `minLength: 0`

                      - `path: String`

                        The file's absolute path inside the environment.

                        `minLength: 0`

                      - `type: :file_id`

                        The type of the object. Always `file_id`.

                        - `:file_id`

                    - `class Inline`

                      Metadata for confidential inline file contents.

                      - `path: String`

                        The file's absolute path inside the environment.

                        `minLength: 0`

                      - `size_bytes: Integer`

                        The decoded size of the inline file in bytes.

                        `format: int64`, `minimum: 0`

                      - `type: :inline`

                        The type of the object. Always `inline`.

                        - `:inline`

                  - `network: Network{ access, allowed_domains}`

                    Network overrides, or null to inherit the template or creation default.

                    - `access: :enabled | :disabled | :restricted`

                      The environment's network access mode.

                      - `:enabled`

                        Allows unrestricted network access.

                      - `:disabled`

                        Disables network access.

                      - `:restricted`

                        Applies the configured domain restrictions.

                    - `allowed_domains: Array[String]`

                      Domains the environment may access when network access is restricted.

                      `minItems: 0`, `maxItems: 2000`

                  - `packages: Packages{ npm, python, system_}`

                    Package overrides, or null to inherit the template or creation default.

                    - `npm: Array[String]`

                      npm packages installed globally in the environment.

                      `minItems: 0`, `maxItems: 16384`

                    - `python: Array[String]`

                      Python packages installed in the environment.

                      `minItems: 0`, `maxItems: 16384`

                    - `system_: Array[String]`

                      System packages installed in the environment.

                      `minItems: 0`, `maxItems: 16384`

                  - `plugins: Array[HostedPlugin]`

                    Plugin overrides, excluding archive contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `description: String`

                      The installed plugin description.

                      `minLength: 0`

                    - `name: String`

                      The installed plugin name.

                      `minLength: 0`

                    - `type: :inline`

                      The type of the object. Always `inline`.

                      - `:inline`

                  - `skills: Array[SkillReference{ skill_id, type, version} | Inline{ description, name, type}]`

                    Skill overrides, excluding archive contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `class SkillReference`

                      A skill resolved afresh from the Skills API whenever a session starts.

                      - `skill_id: String`

                        The referenced skill ID.

                        `minLength: 0`

                      - `type: :skill_reference`

                        The type of the object. Always `skill_reference`.

                        - `:skill_reference`

                      - `version: String`

                        The requested version selector, including `latest`.

                        `minLength: 0`

                    - `class Inline`

                      Safe metadata for an inline skill archive.

                      - `description: String`

                        The skill description declared in `SKILL.md`.

                        `minLength: 0`

                      - `name: String`

                        The skill name declared in `SKILL.md`.

                        `minLength: 0`

                      - `type: :inline`

                        The type of the object. Always `inline`.

                        - `:inline`

                  - `type: :openai_hosted`

                    The type of the object. Always `openai_hosted`.

                    - `:openai_hosted`

                - `class SelfHosted`

                  - `capability_directories: Array[String]`

                    Directories that expose capabilities to the agent.

                    `minItems: 0`, `maxItems: 2000`

                  - `environment_id: String`

                    An existing registration, or null to create a session-owned environment.

                    `minLength: 0`

                  - `type: :self_hosted`

                    The type of the object. Always `self_hosted`.

                    - `:self_hosted`

                  - `workspace_directory: String`

                    The absolute project directory in the environment.

                    `minLength: 0`

              - `input: Array[Input{ content, role, type}]`

                Initial input delivered to each new session.

                `minItems: 0`, `maxItems: 2000`

                - `content: Array[InputContent]`

                  The content of the message.

                  `minItems: 0`, `maxItems: 2000`

                  - `class InputText`

                    Text input recorded in a session item.

                    - `text: String`

                      The text supplied to the agent.

                      `minLength: 0`

                    - `type: :input_text`

                      The type of the object. Always `input_text`.

                      - `:input_text`

                  - `class InputImage`

                    Image input recorded in a session item.

                    - `image_url: String`

                      The URL of the image supplied to the agent, which may be a base64-encoded data URL.

                      `minLength: 0`

                    - `type: :input_image`

                      The type of the object. Always `input_image`.

                      - `:input_image`

                - `role: :user`

                  The role of the message author. Always `user`.

                  - `:user`

                - `type: :message`

                  The type of the input item. Always `message`.

                  - `:message`

              - `metadata: Hash[Symbol, String]`

                Metadata attached to each new session.

              - `type: :new_session`

                The type of the object. Always `new_session`.

                - `:new_session`

              - `vault_ids: Array[String]`

                Vaults made available to each new session.

                `minItems: 0`, `maxItems: 2000`

            - `class ExistingSession`

              - `instructions: String`

                Saved instructions delivered as an automation notification.

                `minLength: 0`

              - `session_id: String`

                The session receiving each invocation.

                `minLength: 0`

              - `type: :existing_session`

                The type of the object. Always `existing_session`.

                - `:existing_session`

          - `timezone: String`

            The timezone used to interpret the expression.

            `minLength: 0`

          - `type: :periodic`

            The type of the object. Always `periodic`.

            - `:periodic`

        - `class OneTimeAutomation`

          Fields shared by periodic and one-time automations.

          - `id: String`

            The automation ID.

            `minLength: 0`

          - `created_at: Integer`

            The creation time as a Unix timestamp in seconds.

            `format: int64`

          - `created_by: AutomationCreatedBy`

            Service-recorded provenance; callers cannot supply this field.

          - `metadata: Hash[Symbol, String]`

            Custom string key-value pairs attached to the automation.

          - `name: String`

            The automation's display name.

            `minLength: 0`

          - `object: :"agent.automation"`

            Always `agent.automation`.

            - `:"agent.automation"`

          - `run_at: Integer`

            The Unix timestamp, in seconds, of the scheduled occurrence.

            `format: int64`

          - `status: :active | :paused | :completed`

            Completion means the schedule has finished, not the agent's work.

            - `:active`

            - `:paused`

            - `:completed`

          - `target: AutomationTarget`

            The session configuration or existing session receiving invocations.

          - `type: :once`

            The type of the object. Always `once`.

            - `:once`

      - `type: :automation`

        The type of the object. Always `automation`.

        - `:automation`

  - `status: :queued | :completed | :failed | :skipped`

    Delivery status; completed does not mean the agent's work has finished.

    - `:queued`

    - `:completed`

    - `:failed`

    - `:skipped`

### Automation Invocation Source

- `AutomationInvocationSource = Manual{ type} | Automation{ automation, type}`

  - `class Manual`

    - `type: :manual`

      The type of the object. Always `manual`.

      - `:manual`

  - `class Automation`

    - `automation: Automation`

      The automation snapshot for this occurrence, excluding confidential values.

      - `class PeriodicAutomation`

        Fields shared by periodic and one-time automations.

        - `id: String`

          The automation ID.

          `minLength: 0`

        - `created_at: Integer`

          The creation time as a Unix timestamp in seconds.

          `format: int64`

        - `created_by: AutomationCreatedBy`

          Service-recorded provenance; callers cannot supply this field.

          - `class Developer`

            - `type: :developer`

              The type of the object. Always `developer`.

              - `:developer`

          - `class Agent`

            - `session_id: String`

              The creator session, which is also the automation's target.

              `minLength: 0`

            - `tool_call_id: String`

              The tool call that created the automation.

              `minLength: 0`

            - `type: :agent`

              The type of the object. Always `agent`.

              - `:agent`

        - `expression: String`

          The cron expression determining scheduled occurrences.

          `minLength: 0`

        - `metadata: Hash[Symbol, String]`

          Custom string key-value pairs attached to the automation.

        - `name: String`

          The automation's display name.

          `minLength: 0`

        - `object: :"agent.automation"`

          Always `agent.automation`.

          - `:"agent.automation"`

        - `status: :active | :paused`

          Whether scheduled delivery is active or paused.

          - `:active`

          - `:paused`

        - `target: AutomationTarget`

          The session configuration or existing session receiving invocations.

          - `class NewSession`

            - `agent: AutomationAgentConfig`

              The inline agent configuration, or null when agent_id is configured.

              - `instructions: String`

                Custom instructions, or null when absent.

                `minLength: 0`

              - `model: String`

                The requested model name.

                `minLength: 0`

              - `multi_agent: MultiAgentConfig`

                The configuration for creating and coordinating subagents.

                - `enabled: bool`

                  Whether subagent tools are enabled. Defaults to false.

                - `max_concurrent_subagents: Integer`

                  Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

                  `format: int64`, `minimum: 1`, `maximum: 4294967295`

              - `reasoning: AgentReasoning`

                The configured reasoning policy.

                - `effort: :none | :minimal | :low | 4 more`

                  The requested reasoning effort, or `null` when the model selects its own default.

                  - `:none`

                  - `:minimal`

                  - `:low`

                  - `:medium`

                  - `:high`

                  - `:xhigh`

                  - `:max`

                - `summary: :concise | :detailed | :auto`

                  The requested reasoning summary format, or `null` when summaries are disabled.

                  - `:concise`

                    Returns a concise reasoning summary when supported.

                  - `:detailed`

                    Returns a detailed reasoning summary when supported.

                  - `:auto`

                    Automatically selects the most detailed summary supported by the model.

              - `service_tier: :auto | :default | :flex | 3 more`

                The configured service-tier policy.

                - `:auto`

                - `:default`

                - `:flex`

                - `:priority`

                - `:fast`

                - `:ultrafast`

              - `text: AgentText`

                The configured output format and verbosity.

                - `format_: TextFormat`

                  The effective output format. Defaults to ordinary text.

                  - `class Text`

                    Generates ordinary text without a structured-output constraint.

                    - `type: :text`

                      The type of the object. Always `text`.

                      - `:text`

                  - `class JSONSchema`

                    Constrains generated text to a JSON Schema.

                    - `schema: Hash[Symbol, untyped]`

                      The JSON Schema that generated text must match.

                    - `type: :json_schema`

                      The type of the object. Always `json_schema`.

                      - `:json_schema`

                - `verbosity: :low | :medium | :high`

                  The amount of text produced by the agent. Defaults to `medium`.

                  - `:low`

                  - `:medium`

                  - `:high`

              - `tools: Array[AgentTool]`

                Configured tools, excluding confidential credentials.

                `minItems: 0`, `maxItems: 2000`

                - `class Function`

                  A function defined by the application.

                  - `defer_loading: bool`

                    Whether the function is deferred and discovered through tool search.

                  - `description: String`

                    A description of what the function does.

                    `minLength: 0`

                  - `name: String`

                    The name of the function.

                    `minLength: 0`

                  - `parameters: Hash[Symbol, untyped]`

                    A JSON Schema object describing the function's arguments.

                  - `type: :function`

                    The type of the object. Always `function`.

                    - `:function`

                  - `async: bool`

                    Whether the agent continues without waiting for the function result.

                - `class ProgrammaticToolCalling`

                  Enables calling tools from model-generated code.

                  - `enabled: bool`

                    Whether tools can be called from model-generated code.

                  - `type: :programmatic_tool_calling`

                    The type of the object. Always `programmatic_tool_calling`.

                    - `:programmatic_tool_calling`

                - `class Mcp`

                  Tools provided by a remote MCP server.

                  - `allowed_tools: Array[String]`

                    The MCP tools the agent may call.

                    `minItems: 0`, `maxItems: 2000`

                  - `connection_origin: :service | :environment`

                    Where outbound MCP HTTP connections originate.

                    - `:service`

                    - `:environment`

                  - `credential_id: String`

                    The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

                    `minLength: 0`

                  - `request_metadata: Hash[Symbol, untyped]`

                    Metadata included with requests to this MCP server.

                  - `required: bool`

                    Whether this MCP server must initialize before the first turn.

                  - `server_label: String`

                    A label used to identify the MCP server in tool calls.

                    `minLength: 0`

                  - `transport: McpTransport`

                    The transport used to connect to the MCP server.

                    - `class HTTP`

                      Connects to an MCP server over HTTP.

                      - `server_url: String`

                        The URL of the MCP server.

                        `minLength: 0`

                      - `type: :http`

                        The type of the object. Always `http`.

                        - `:http`

                    - `class Stdio`

                      Starts an MCP server as a local process.

                      - `args: Array[String]`

                        Arguments passed to the MCP server command.

                        `minItems: 0`, `maxItems: 2000`

                      - `command: String`

                        The command used to start the MCP server.

                        `minLength: 0`

                      - `cwd: String`

                        The working directory used to start the MCP server.

                        `minLength: 0`

                      - `env_vars: Array[String]`

                        Environment variable names inherited from the execution environment.

                        `minItems: 0`, `maxItems: 2000`

                      - `type: :stdio`

                        The type of the object. Always `stdio`.

                        - `:stdio`

                  - `type: :mcp`

                    The type of the object. Always `mcp`.

                    - `:mcp`

                - `class WebSearch`

                  Web search.

                  - `allowed_domains: Array[String]`

                    Allowed search domains, or `null` when the search is unrestricted.

                    `minItems: 0`, `maxItems: 2000`

                  - `context_size: :low | :medium | :high`

                    The amount of search context made available to the model. Defaults to `medium`.

                    - `:low`

                    - `:medium`

                    - `:high`

                  - `location: Location{ city, country, region, timezone}`

                    Approximate location used to localize search results, if provided.

                    - `city: String`

                      The city name.

                      `minLength: 0`

                    - `country: String`

                      The two-letter ISO country code, such as `US`.

                      `minLength: 0`

                    - `region: String`

                      The region or state name.

                      `minLength: 0`

                    - `timezone: String`

                      The IANA timezone, such as `America/Los_Angeles`.

                      `minLength: 0`

                  - `mode: :disabled | :cached | :live`

                    The source used for web search results.

                    - `:disabled`

                    - `:cached`

                    - `:live`

                  - `type: :web_search`

                    The type of the object. Always `web_search`.

                    - `:web_search`

                - `class ComputerUse`

                  Browser use in an OpenAI-hosted session.

                  - `include_screenshots: bool`

                    Whether computer tool outputs include screenshots.

                  - `type: :computer_use`

                    The type of the object. Always `computer_use`.

                    - `:computer_use`

                - `class Automations`

                  Lets the agent manage its own scheduled wakeups.

                  - `type: :automations`

                    The type of the object. Always `automations`.

                    - `:automations`

              - `compaction: Compaction{ async}`

                The effective context compaction settings.

                - `async: bool`

                  Whether context is compacted in the background. Defaults to true.

              - `experimental: Experimental{ time_awareness}`

                The effective experimental settings for the agent.

                - `time_awareness: bool`

                  Whether the model receives periodic current-time reminders.

            - `agent_id: String`

              The saved agent reference, or null when an inline agent is configured.

              `minLength: 0`

            - `environment: AutomationEnvironment`

              Configuration or references used to select the execution environment.

              - `class None`

                - `type: :none`

                  The type of the object. Always `none`.

                  - `:none`

              - `class OpenAIHosted`

                Hosted environment selection with confidential setup commands and variables omitted.

                - `capability_directories: Array[String]`

                  Directory overrides, or null to inherit the template or creation default.

                  `minItems: 0`, `maxItems: 2000`

                - `container_size: :small | :medium | :large`

                  The configured container size, or null to use the creation default.

                  - `:small`

                  - `:medium`

                  - `:large`

                - `desktop: Desktop{ enabled}`

                  Desktop overrides, or null to inherit the template or creation default.

                  - `enabled: bool`

                    Whether the environment provisions a desktop and browser proxy.

                - `environment_id: String`

                  An existing environment reference, or null when provisioning a new environment.

                  `minLength: 0`

                - `environment_template_id: String`

                  A template reference, or null when no template is selected.

                  `minLength: 0`

                - `files: Array[FileID{ file_id, path, type} | Inline{ path, size_bytes, type}]`

                  File overrides, excluding contents, or null to inherit.

                  `minItems: 0`, `maxItems: 2000`

                  - `class FileID`

                    A project-scoped Files API reference resolved separately for each session.

                    - `file_id: String`

                      The ID of the uploaded file.

                      `minLength: 0`

                    - `path: String`

                      The file's absolute path inside the environment.

                      `minLength: 0`

                    - `type: :file_id`

                      The type of the object. Always `file_id`.

                      - `:file_id`

                  - `class Inline`

                    Metadata for confidential inline file contents.

                    - `path: String`

                      The file's absolute path inside the environment.

                      `minLength: 0`

                    - `size_bytes: Integer`

                      The decoded size of the inline file in bytes.

                      `format: int64`, `minimum: 0`

                    - `type: :inline`

                      The type of the object. Always `inline`.

                      - `:inline`

                - `network: Network{ access, allowed_domains}`

                  Network overrides, or null to inherit the template or creation default.

                  - `access: :enabled | :disabled | :restricted`

                    The environment's network access mode.

                    - `:enabled`

                      Allows unrestricted network access.

                    - `:disabled`

                      Disables network access.

                    - `:restricted`

                      Applies the configured domain restrictions.

                  - `allowed_domains: Array[String]`

                    Domains the environment may access when network access is restricted.

                    `minItems: 0`, `maxItems: 2000`

                - `packages: Packages{ npm, python, system_}`

                  Package overrides, or null to inherit the template or creation default.

                  - `npm: Array[String]`

                    npm packages installed globally in the environment.

                    `minItems: 0`, `maxItems: 16384`

                  - `python: Array[String]`

                    Python packages installed in the environment.

                    `minItems: 0`, `maxItems: 16384`

                  - `system_: Array[String]`

                    System packages installed in the environment.

                    `minItems: 0`, `maxItems: 16384`

                - `plugins: Array[HostedPlugin]`

                  Plugin overrides, excluding archive contents, or null to inherit.

                  `minItems: 0`, `maxItems: 2000`

                  - `description: String`

                    The installed plugin description.

                    `minLength: 0`

                  - `name: String`

                    The installed plugin name.

                    `minLength: 0`

                  - `type: :inline`

                    The type of the object. Always `inline`.

                    - `:inline`

                - `skills: Array[SkillReference{ skill_id, type, version} | Inline{ description, name, type}]`

                  Skill overrides, excluding archive contents, or null to inherit.

                  `minItems: 0`, `maxItems: 2000`

                  - `class SkillReference`

                    A skill resolved afresh from the Skills API whenever a session starts.

                    - `skill_id: String`

                      The referenced skill ID.

                      `minLength: 0`

                    - `type: :skill_reference`

                      The type of the object. Always `skill_reference`.

                      - `:skill_reference`

                    - `version: String`

                      The requested version selector, including `latest`.

                      `minLength: 0`

                  - `class Inline`

                    Safe metadata for an inline skill archive.

                    - `description: String`

                      The skill description declared in `SKILL.md`.

                      `minLength: 0`

                    - `name: String`

                      The skill name declared in `SKILL.md`.

                      `minLength: 0`

                    - `type: :inline`

                      The type of the object. Always `inline`.

                      - `:inline`

                - `type: :openai_hosted`

                  The type of the object. Always `openai_hosted`.

                  - `:openai_hosted`

              - `class SelfHosted`

                - `capability_directories: Array[String]`

                  Directories that expose capabilities to the agent.

                  `minItems: 0`, `maxItems: 2000`

                - `environment_id: String`

                  An existing registration, or null to create a session-owned environment.

                  `minLength: 0`

                - `type: :self_hosted`

                  The type of the object. Always `self_hosted`.

                  - `:self_hosted`

                - `workspace_directory: String`

                  The absolute project directory in the environment.

                  `minLength: 0`

            - `input: Array[Input{ content, role, type}]`

              Initial input delivered to each new session.

              `minItems: 0`, `maxItems: 2000`

              - `content: Array[InputContent]`

                The content of the message.

                `minItems: 0`, `maxItems: 2000`

                - `class InputText`

                  Text input recorded in a session item.

                  - `text: String`

                    The text supplied to the agent.

                    `minLength: 0`

                  - `type: :input_text`

                    The type of the object. Always `input_text`.

                    - `:input_text`

                - `class InputImage`

                  Image input recorded in a session item.

                  - `image_url: String`

                    The URL of the image supplied to the agent, which may be a base64-encoded data URL.

                    `minLength: 0`

                  - `type: :input_image`

                    The type of the object. Always `input_image`.

                    - `:input_image`

              - `role: :user`

                The role of the message author. Always `user`.

                - `:user`

              - `type: :message`

                The type of the input item. Always `message`.

                - `:message`

            - `metadata: Hash[Symbol, String]`

              Metadata attached to each new session.

            - `type: :new_session`

              The type of the object. Always `new_session`.

              - `:new_session`

            - `vault_ids: Array[String]`

              Vaults made available to each new session.

              `minItems: 0`, `maxItems: 2000`

          - `class ExistingSession`

            - `instructions: String`

              Saved instructions delivered as an automation notification.

              `minLength: 0`

            - `session_id: String`

              The session receiving each invocation.

              `minLength: 0`

            - `type: :existing_session`

              The type of the object. Always `existing_session`.

              - `:existing_session`

        - `timezone: String`

          The timezone used to interpret the expression.

          `minLength: 0`

        - `type: :periodic`

          The type of the object. Always `periodic`.

          - `:periodic`

      - `class OneTimeAutomation`

        Fields shared by periodic and one-time automations.

        - `id: String`

          The automation ID.

          `minLength: 0`

        - `created_at: Integer`

          The creation time as a Unix timestamp in seconds.

          `format: int64`

        - `created_by: AutomationCreatedBy`

          Service-recorded provenance; callers cannot supply this field.

        - `metadata: Hash[Symbol, String]`

          Custom string key-value pairs attached to the automation.

        - `name: String`

          The automation's display name.

          `minLength: 0`

        - `object: :"agent.automation"`

          Always `agent.automation`.

          - `:"agent.automation"`

        - `run_at: Integer`

          The Unix timestamp, in seconds, of the scheduled occurrence.

          `format: int64`

        - `status: :active | :paused | :completed`

          Completion means the schedule has finished, not the agent's work.

          - `:active`

          - `:paused`

          - `:completed`

        - `target: AutomationTarget`

          The session configuration or existing session receiving invocations.

        - `type: :once`

          The type of the object. Always `once`.

          - `:once`

    - `type: :automation`

      The type of the object. Always `automation`.

      - `:automation`
