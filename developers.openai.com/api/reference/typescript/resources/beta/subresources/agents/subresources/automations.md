<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/agents/subresources/automations/ -->

# Automations

## Create an automation

`client.beta.agents.automations.create(AutomationCreateParamsbody, RequestOptionsoptions?): Automation`

**post** `/agents/automations`

Saves an active automation without invoking it immediately.

### Parameters

- `AutomationCreateParams = CreateAutomationParamsPeriodic | CreateAutomationParamsOnce`

  - `AutomationCreateParamsBase`

    - `expression: string`

      A standard five-field cron expression defining scheduled occurrences.

      `minLength: 1`, `maxLength: 256`

    - `name: string`

      A human-readable name for the automation.

      `minLength: 1`, `maxLength: 256`

    - `target: AutomationTargetParam`

      The session an automation invocation targets.

      - `AutomationTargetParamNewSession`

        Create a session for each invocation.

        - `environment: EnvironmentParam`

          The execution environment for each new session.

          - `EnvironmentParamNone`

            Runs the agent without an execution environment.

            - `type: "none"`

              The type of the object. Always `none`.

              - `"none"`

          - `EnvironmentParamOpenAIHosted`

            An existing OpenAI-hosted environment or new inline/template-based hosted configuration.

            - `type: "openai_hosted"`

              The type of the object. Always `openai_hosted`.

              - `"openai_hosted"`

            - `capability_directories?: Array<string> | null`

              Directories that contain capabilities exposed to the agent. Defaults to an empty list.

              `minItems: 0`, `maxItems: 16384`

            - `container_size?: "small" | "medium" | "large"`

              The hosted container size. Omission selects the medium tier.

              - `"small"`

              - `"medium"`

              - `"large"`

            - `desktop?: Desktop | null`

              Desktop provisioning. Omission or null inherits the template setting, or defaults to disabled.

              - `enabled: boolean`

                Whether to provision the desktop and its browser proxy.

            - `env?: Record<string, string> | null`

              Environment variables made available to the agent.

            - `environment_id?: string`

              An existing prewarmed environment. Cannot be combined with a template or inline configuration.

              `minLength: 9`, `maxLength: 256`

            - `environment_template_id?: string`

              A reusable hosted template applied before inline session configuration. Omitted fields inherit the template; network overrides cannot broaden its policy.

              `minLength: 0`, `maxLength: 64`

            - `files?: Array<HostedEnvironmentFileParam> | null`

              Files available before the agent starts. Defaults to an empty list.

              `minItems: 0`, `maxItems: 50`

              - `HostedEnvironmentFileParamFileID`

                A file previously uploaded through the OpenAI Files API.

                - `file_id: string`

                  The ID of the uploaded file.

                  `minLength: 1`, `maxLength: 256`

                - `path: string`

                  The absolute destination path inside `/workspace`.

                  `minLength: 1`, `maxLength: 4096`

                - `type: "file_id"`

                  The type of the object. Always `file_id`.

                  - `"file_id"`

              - `HostedEnvironmentFileParamInline`

                A file supplied directly as standard-base64 data.

                - `data: string`

                  The standard-base64-encoded file contents.

                  `minLength: 0`, `maxLength: 6990508`

                - `path: string`

                  The absolute destination path inside `/workspace`.

                  `minLength: 1`, `maxLength: 4096`

                - `type: "inline"`

                  The type of the object. Always `inline`.

                  - `"inline"`

            - `network?: Network | null`

              Network access policy for the environment. If omitted, the API version determines whether network access is enabled or disabled.

              - `access: "enabled" | "disabled" | "restricted"`

                The environment's network access mode.

                - `"enabled"`

                  Allows unrestricted network access.

                - `"disabled"`

                  Disables network access.

                - `"restricted"`

                  Applies the configured domain restrictions.

              - `allowed_domains?: Array<string> | null`

                Domains the environment may access when network access is restricted.

                `minItems: 0`, `maxItems: 16384`

              - `blocked_domains?: Array<string> | null`

                Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

                `minItems: 0`, `maxItems: 100`

            - `packages?: Packages | null`

              Packages to install in the environment. Defaults to empty package lists.

              - `npm?: Array<string> | null`

                npm packages to install globally. Defaults to an empty list.

                `minItems: 0`, `maxItems: 16384`

              - `python?: Array<string> | null`

                Python packages to install. Defaults to an empty list.

                `minItems: 0`, `maxItems: 16384`

              - `system?: Array<string> | null`

                System packages to install. Defaults to an empty list.

                `minItems: 0`, `maxItems: 16384`

            - `plugins?: Array<HostedPluginParam> | null`

              Plugins provided as inline ZIP archives. Defaults to an empty list.

              `minItems: 0`, `maxItems: 32`

              - `description: string`

                The plugin description declared in `.codex-plugin/plugin.json`.

                `minLength: 0`, `maxLength: 1048576`

              - `name: string`

                The plugin name declared in `.codex-plugin/plugin.json`.

                `minLength: 1`, `maxLength: 64`

              - `source: InlineCapabilitySourceParam`

                Provides ZIP bytes encoded with standard base64.

                - `data: string`

                  Standard-base64 encoded ZIP archive bytes.

                  `minLength: 1`, `maxLength: 70254592`

                - `media_type: "application/zip"`

                  The archive media type, always `application/zip`.

                  - `"application/zip"`

                - `type: "base64"`

                  The type of the object. Always `base64`.

                  - `"base64"`

              - `type: "inline"`

                The type of the object. Always `inline`.

                - `"inline"`

            - `setup_commands?: Array<SetupCommandParam> | null`

              Ordered, confidential setup commands. Command bodies are never returned.

              `minItems: 0`, `maxItems: 16`

              - `command: string`

                The shell command to execute.

                `minLength: 0`, `maxLength: 65536`

              - `cwd?: string | null`

                The absolute working directory. Defaults to `/workspace`.

                `minLength: 0`, `maxLength: 4096`

            - `skills?: Array<HostedSkillParam> | null`

              Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

              `minItems: 0`, `maxItems: 200`

              - `HostedSkillParamSkillReference`

                References a skill uploaded through the Skills API.

                - `skill_id: string`

                  The ID of the skill created through `/v1/skills`.

                  `minLength: 1`, `maxLength: 64`

                - `type: "skill_reference"`

                  The type of the object. Always `skill_reference`.

                  - `"skill_reference"`

                - `version?: string | null`

                  The skill version, a positive integer or `latest`; omission selects the default.

                  `minLength: 0`, `maxLength: 1048576`

              - `HostedSkillParamInline`

                Supplies a skill ZIP directly in the session request.

                - `description: string`

                  The skill description declared in `SKILL.md`.

                  `minLength: 0`, `maxLength: 1048576`

                - `name: string`

                  The skill name declared in `SKILL.md`.

                  `minLength: 1`, `maxLength: 64`

                - `source: InlineCapabilitySourceParam`

                  Provides ZIP bytes encoded with standard base64.

                - `type: "inline"`

                  The type of the object. Always `inline`.

                  - `"inline"`

          - `EnvironmentParamSelfHosted`

            An application-hosted environment configured inline.

            - `type: "self_hosted"`

              The type of the object. Always `self_hosted`.

              - `"self_hosted"`

            - `workspace_directory: string`

              Absolute project directory inside the self-hosted environment.

              `minLength: 0`, `maxLength: 1048576`

            - `capability_directories?: Array<string> | null`

              Directories that contain capabilities exposed to the agent. Defaults to an empty list.

              `minItems: 0`, `maxItems: 16384`

        - `input: Array<AgentSessionInputMessageParam>`

          Initial user messages submitted with each new session.

          `minItems: 0`, `maxItems: 16384`

          - `content: Array<InputContentParam>`

            The content of the message.

            `minItems: 0`, `maxItems: 16384`

            - `InputContentParamInputText`

              Text input to the model.

              - `text: string`

                The text sent to the model.

                `minLength: 0`, `maxLength: 1048576`

              - `type: "input_text"`

                The type of the object. Always `input_text`.

                - `"input_text"`

            - `InputContentParamInputImage`

              Image input to the model.

              - `image_url: string`

                The URL of the image sent to the model.

                `minLength: 0`, `maxLength: 1048576`

              - `type: "input_image"`

                The type of the object. Always `input_image`.

                - `"input_image"`

          - `role: "user"`

            The role of the message author. Always `user`.

            - `"user"`

          - `type?: "message"`

            The type of the input item. Always `message`.

            - `"message"`

        - `type: "new_session"`

          The type of the object. Always `new_session`.

          - `"new_session"`

        - `agent?: Agent`

          Inline agent configuration. Provide exactly one of agent and agent_id.

          - `compaction?: Compaction | null`

            Context compaction settings. Omit to keep the current settings. A supplied object replaces the settings; null or an empty object enables background compaction.

            - `async?: boolean | null`

              Whether to compact context in the background. Omission or null defaults to true. Set to false to use blocking compaction. Background compaction may increase token usage.

          - `experimental?: Experimental`

            Experimental settings to merge by key. Omitted settings keep their current values.

            - `time_awareness?: boolean`

              Whether to give the model periodic current-time reminders. Omit to keep the current setting.

          - `instructions?: string | null`

            Additional instructions appended to the agent's default base instructions. Omit to leave unchanged.

            `minLength: 0`, `maxLength: 1048576`

          - `model?: string`

            The model to use for the agent. The requested model name is preserved.

            `minLength: 0`, `maxLength: 1048576`

          - `multi_agent?: MultiAgentConfigParam | null`

            Configuration for creating and coordinating subagents.

            - `enabled: boolean`

              Whether subagent tools are enabled.

            - `max_concurrent_subagents?: number`

              Maximum number of subagents that may run concurrently. Defaults to 6.

              `format: int64`, `minimum: 1`, `maximum: 4294967295`

          - `reasoning?: AgentReasoningParam | null`

            Configuration for model reasoning. Omit to keep the current settings; pass `null` to reset to the model's default effort.

            - `effort?: "none" | "minimal" | "low" | 4 more | null`

              The amount of reasoning effort the model should use. Omission lets the model select it.

              - `"none"`

              - `"minimal"`

              - `"low"`

              - `"medium"`

              - `"high"`

              - `"xhigh"`

              - `"max"`

            - `summary?: "concise" | "detailed" | "auto" | null`

              Controls whether the response includes a reasoning summary.

              - `"concise"`

                Returns a concise reasoning summary when supported.

              - `"detailed"`

                Returns a detailed reasoning summary when supported.

              - `"auto"`

                Automatically selects the most detailed summary supported by the model.

          - `service_tier?: "auto" | "default" | "flex" | 3 more | null`

            The service tier used for model requests.

            - `"auto"`

              Selects the service tier automatically.

            - `"default"`

              Uses the default service tier.

            - `"flex"`

              Uses the flex service tier.

            - `"priority"`

              Uses the priority service tier.

            - `"fast"`

              Uses the fast service tier.

            - `"ultrafast"`

              Uses the ultrafast service tier.

          - `text?: AgentTextParam | null`

            Configuration for text generated by the agent.

            - `format?: TextFormatParam | null`

              The output format. Omission uses ordinary text (`{"type": "text"}`).

              - `TextFormatParamText`

                Generates ordinary text without a structured-output constraint.

                - `type: "text"`

                  The type of the object. Always `text`.

                  - `"text"`

              - `TextFormatParamJSONSchema`

                Constrains generated text to a JSON Schema.

                - `schema: Record<string, unknown>`

                  The JSON Schema that generated text must match.

                - `type: "json_schema"`

                  The type of the object. Always `json_schema`.

                  - `"json_schema"`

            - `verbosity?: "low" | "medium" | "high" | null`

              The amount of text the model should produce. Defaults to `medium`, matching Responses.

              - `"low"`

                Produces less text.

              - `"medium"`

                Uses the default amount of text.

              - `"high"`

                Produces more text.

          - `tools?: Array<AgentToolParam> | null`

            Tools available to the agent. Omit to inherit, or pass null to clear them. The resolved tool list must fit within 3 MiB (3,145,728 bytes) of compact UTF-8 JSON.

            `minItems: 0`, `maxItems: 16384`

            - `AgentToolConfigParamFunction`

              A function defined by the application.

              - `description: string`

                A description of what the function does.

                `minLength: 0`, `maxLength: 1048576`

              - `name: string`

                The name of the function.

                `minLength: 0`, `maxLength: 1048576`

              - `parameters: Record<string, unknown>`

                A JSON Schema object describing the function's arguments.

              - `type: "function"`

                The type of the object. Always `function`.

                - `"function"`

              - `async?: boolean`

                Whether the agent continues without waiting for the function result. Defaults to `false`.

              - `defer_loading?: boolean`

                Whether this function is deferred and discovered through tool search. Defaults to `false`.

            - `AgentToolConfigParamToolSearch`

              Discovers deferred function tools and loads them into the model context.

              - `type: "tool_search"`

                The type of the object. Always `tool_search`.

                - `"tool_search"`

            - `AgentToolConfigParamProgrammaticToolCalling`

              Enables calling tools from model-generated code.

              - `type: "programmatic_tool_calling"`

                The type of the object. Always `programmatic_tool_calling`.

                - `"programmatic_tool_calling"`

              - `enabled?: boolean`

                Whether tools can be called from model-generated code. Defaults to `true`.

            - `AgentToolConfigParamMcp`

              Tools provided by a remote MCP server.

              - `server_label: string`

                A label used to identify the MCP server in tool calls.

                `minLength: 0`, `maxLength: 1048576`

              - `transport: McpTransportParam`

                The transport used to connect to the MCP server.

                - `McpTransportConfigParamHTTP`

                  Connects to an MCP server over HTTP.

                  - `server_url: string`

                    The URL of the MCP server.

                    `minLength: 0`, `maxLength: 1048576`

                  - `type: "http"`

                    The type of the object. Always `http`.

                    - `"http"`

                  - `authorization?: string | null`

                    The authorization value sent to the MCP server, if any.

                    `minLength: 0`, `maxLength: 1048576`

                  - `headers?: Record<string, string> | null`

                    Additional HTTP headers sent to the MCP server.

                - `McpTransportConfigParamStdio`

                  Starts an MCP server as a local process.

                  - `command: string`

                    The command used to start the MCP server.

                    `minLength: 0`, `maxLength: 1048576`

                  - `cwd: string`

                    The working directory used to start the MCP server.

                    `minLength: 0`, `maxLength: 1048576`

                  - `type: "stdio"`

                    The type of the object. Always `stdio`.

                    - `"stdio"`

                  - `args?: Array<string> | null`

                    Arguments passed to the MCP server command.

                    `minItems: 0`, `maxItems: 16384`

                  - `env?: Record<string, string> | null`

                    Environment variables set for the MCP server process.

                  - `env_vars?: Array<string> | null`

                    Environment variable names to inherit from the selected execution environment.

                    `minItems: 0`, `maxItems: 16384`

              - `type: "mcp"`

                The type of the object. Always `mcp`.

                - `"mcp"`

              - `allowed_tools?: Array<string> | null`

                The MCP tools the agent may call. All server tools are allowed when omitted.

                `minItems: 0`, `maxItems: 16384`

              - `connection_origin?: "service" | "environment" | null`

                Selects where outbound MCP HTTP connections originate. Omitted or `service` uses the Managed Agents service network; `environment` uses the session's selected environment.

                - `"service"`

                  Uses the Managed Agents service network.

                - `"environment"`

                  Uses the session's execution environment.

              - `credential_id?: string | null`

                The attached vault credential used to authenticate this MCP server. Optional when exactly one attached credential matches the server URL.

                `minLength: 0`, `maxLength: 1048576`

              - `request_metadata?: Record<string, unknown> | null`

                Metadata included with requests to this MCP server.

              - `required?: boolean`

                Whether this MCP server must initialize before the first turn. Defaults to `false`.

            - `AgentToolConfigParamWebSearch`

              Web search.

              - `type: "web_search"`

                The type of the object. Always `web_search`.

                - `"web_search"`

              - `allowed_domains?: Array<string> | null`

                Domains the search may include.

                `minItems: 0`, `maxItems: 16384`

              - `context_size?: "low" | "medium" | "high" | null`

                The amount of search context made available to the model. Defaults to `medium`.

                - `"low"`

                - `"medium"`

                - `"high"`

              - `location?: Location | null`

                Approximate location used to localize search results.

                - `city?: string | null`

                  The city name.

                  `minLength: 0`, `maxLength: 1048576`

                - `country?: string | null`

                  The two-letter ISO country code, such as `US`.

                  `minLength: 0`, `maxLength: 1048576`

                - `region?: string | null`

                  The region or state name.

                  `minLength: 0`, `maxLength: 1048576`

                - `timezone?: string | null`

                  The IANA timezone, such as `America/Los_Angeles`.

                  `minLength: 0`, `maxLength: 1048576`

              - `mode?: "disabled" | "cached" | "live" | null`

                The source used for web search results. Defaults to `live`.

                - `"disabled"`

                  Disables web search.

                - `"cached"`

                  Uses cached search results.

                - `"live"`

                  Searches the live web.

            - `AgentToolConfigParamComputerUse`

              Browser use in an OpenAI-hosted session.

              - `type: "computer_use"`

                The type of the object. Always `computer_use`.

                - `"computer_use"`

              - `include_screenshots?: boolean`

                Whether computer tool outputs include screenshots. Defaults to `false`.

            - `AgentToolConfigParamAutomations`

              Lets the agent manage its own scheduled wakeups.

              - `type: "automations"`

                The type of the object. Always `automations`.

                - `"automations"`

        - `agent_id?: string`

          A saved agent ID. Provide exactly one of agent and agent_id.

          `minLength: 0`, `maxLength: 64`

        - `metadata?: Record<string, string> | null`

          Metadata attached to each new session.

        - `vault_ids?: Array<string> | null`

          The IDs of vaults made available to each new session.

          `minItems: 0`, `maxItems: 16384`

      - `AutomationTargetParamExistingSession`

        Deliver instructions to an existing session.

        - `instructions: string`

          Instructions delivered as an automation notification.

          `minLength: 0`, `maxLength: 1048576`

        - `session_id: string`

          The session receiving each invocation.

          `minLength: 0`, `maxLength: 1048576`

        - `type: "existing_session"`

          The type of the object. Always `existing_session`.

          - `"existing_session"`

    - `timezone: string`

      The IANA timezone used to interpret the cron expression.

      `minLength: 1`, `maxLength: 128`

    - `type: "periodic"`

      The type of the object. Always `periodic`.

      - `"periodic"`

    - `metadata?: Record<string, string>`

  - `CreateAutomationParamsPeriodic extends AutomationCreateParamsBase`

  - `CreateAutomationParamsOnce`

    - `name: string`

      A human-readable name for the automation.

      `minLength: 1`, `maxLength: 256`

    - `run_at: number`

      A future Unix timestamp in seconds.

      `format: int64`

    - `target: AutomationTargetParam`

      The session an automation invocation targets.

    - `type: "once"`

      The type of the object. Always `once`.

      - `"once"`

    - `metadata?: Record<string, string>`

### Returns

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

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const automation = await client.beta.agents.automations.create({
  expression: 'x',
  name: 'x',
  target: {
    environment: { type: 'none' },
    input: [{ content: [{ text: 'text', type: 'input_text' }], role: 'user' }],
    type: 'new_session',
  },
  timezone: 'x',
  type: 'periodic',
});

console.log(automation);
```

#### 201 — Example

```json
{
  "id": "id",
  "created_at": 0,
  "created_by": {
    "type": "developer"
  },
  "expression": "expression",
  "metadata": {
    "foo": "string"
  },
  "name": "name",
  "object": "agent.automation",
  "status": "active",
  "target": {
    "agent": {
      "instructions": "instructions",
      "model": "model",
      "multi_agent": {
        "enabled": true,
        "max_concurrent_subagents": 1
      },
      "reasoning": {
        "effort": "none",
        "summary": "concise"
      },
      "service_tier": "auto",
      "text": {
        "format": {
          "type": "text"
        },
        "verbosity": "low"
      },
      "tools": [
        {
          "defer_loading": true,
          "description": "description",
          "name": "name",
          "parameters": {
            "foo": "bar"
          },
          "type": "function",
          "async": true
        }
      ],
      "compaction": {
        "async": true
      },
      "experimental": {
        "time_awareness": true
      }
    },
    "agent_id": "agent_id",
    "environment": {
      "type": "none"
    },
    "input": [
      {
        "content": [
          {
            "text": "text",
            "type": "input_text"
          }
        ],
        "role": "user",
        "type": "message"
      }
    ],
    "metadata": {
      "foo": "string"
    },
    "type": "new_session",
    "vault_ids": [
      "string"
    ]
  },
  "timezone": "timezone",
  "type": "periodic"
}
```

## Delete an automation

`client.beta.agents.automations.delete(stringautomationID, RequestOptionsoptions?): AutomationDeleted`

**delete** `/agents/automations/{automation_id}`

Deletes the automation and prevents future invocations without deleting its target session.

### Parameters

- `automationID: string`

  `minLength: 0`, `maxLength: 1048576`

### Returns

- `AutomationDeleted`

  - `id: string`

    The deleted automation ID.

    `minLength: 0`

  - `deleted: boolean`

    Always true.

  - `object: "agent.automation.deleted"`

    Always `agent.automation.deleted`.

    - `"agent.automation.deleted"`

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const automationDeleted = await client.beta.agents.automations.delete('automation_id');

console.log(automationDeleted.id);
```

#### 200 — Example

```json
{
  "id": "id",
  "deleted": true,
  "object": "agent.automation.deleted"
}
```

## List automations

`client.beta.agents.automations.list(AutomationListParamsquery?, RequestOptionsoptions?): CursorPage<Automation>`

**get** `/agents/automations`

Lists project-owned automations, optionally filtered by target session.

### Parameters

- `query: AutomationListParams`

  - `after?: string`

    Return resources after this resource ID in the selected order.

    `minLength: 0`, `maxLength: 1048576`

  - `limit?: number`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

    `format: int64`, `minimum: 1`, `maximum: 100`

  - `order?: "asc" | "desc"`

    The order in which resources are returned. Defaults to `desc`.

    - `"asc"`

      Returns resources in ascending order.

    - `"desc"`

      Returns resources in descending order.

  - `session_id?: string`

    Matches existing-session targets, including agent-created automations.

    `minLength: 0`, `maxLength: 1048576`

### Returns

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

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const automation of client.beta.agents.automations.list()) {
  console.log(automation);
}
```

#### 200 — Example

```json
{
  "data": [
    {
      "id": "id",
      "created_at": 0,
      "created_by": {
        "type": "developer"
      },
      "expression": "expression",
      "metadata": {
        "foo": "string"
      },
      "name": "name",
      "object": "agent.automation",
      "status": "active",
      "target": {
        "agent": {
          "instructions": "instructions",
          "model": "model",
          "multi_agent": {
            "enabled": true,
            "max_concurrent_subagents": 1
          },
          "reasoning": {
            "effort": "none",
            "summary": "concise"
          },
          "service_tier": "auto",
          "text": {
            "format": {
              "type": "text"
            },
            "verbosity": "low"
          },
          "tools": [
            {
              "defer_loading": true,
              "description": "description",
              "name": "name",
              "parameters": {
                "foo": "bar"
              },
              "type": "function",
              "async": true
            }
          ],
          "compaction": {
            "async": true
          },
          "experimental": {
            "time_awareness": true
          }
        },
        "agent_id": "agent_id",
        "environment": {
          "type": "none"
        },
        "input": [
          {
            "content": [
              {
                "text": "text",
                "type": "input_text"
              }
            ],
            "role": "user",
            "type": "message"
          }
        ],
        "metadata": {
          "foo": "string"
        },
        "type": "new_session",
        "vault_ids": [
          "string"
        ]
      },
      "timezone": "timezone",
      "type": "periodic"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Pause an automation

`client.beta.agents.automations.pause(stringautomationID, RequestOptionsoptions?): Automation`

**post** `/agents/automations/{automation_id}/pause`

Pauses future scheduled delivery without stopping an active session.

### Parameters

- `automationID: string`

  `minLength: 0`, `maxLength: 1048576`

### Returns

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

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const automation = await client.beta.agents.automations.pause('automation_id');

console.log(automation);
```

#### 200 — Example

```json
{
  "id": "id",
  "created_at": 0,
  "created_by": {
    "type": "developer"
  },
  "expression": "expression",
  "metadata": {
    "foo": "string"
  },
  "name": "name",
  "object": "agent.automation",
  "status": "active",
  "target": {
    "agent": {
      "instructions": "instructions",
      "model": "model",
      "multi_agent": {
        "enabled": true,
        "max_concurrent_subagents": 1
      },
      "reasoning": {
        "effort": "none",
        "summary": "concise"
      },
      "service_tier": "auto",
      "text": {
        "format": {
          "type": "text"
        },
        "verbosity": "low"
      },
      "tools": [
        {
          "defer_loading": true,
          "description": "description",
          "name": "name",
          "parameters": {
            "foo": "bar"
          },
          "type": "function",
          "async": true
        }
      ],
      "compaction": {
        "async": true
      },
      "experimental": {
        "time_awareness": true
      }
    },
    "agent_id": "agent_id",
    "environment": {
      "type": "none"
    },
    "input": [
      {
        "content": [
          {
            "text": "text",
            "type": "input_text"
          }
        ],
        "role": "user",
        "type": "message"
      }
    ],
    "metadata": {
      "foo": "string"
    },
    "type": "new_session",
    "vault_ids": [
      "string"
    ]
  },
  "timezone": "timezone",
  "type": "periodic"
}
```

## Resume an automation

`client.beta.agents.automations.resume(stringautomationID, RequestOptionsoptions?): Automation`

**post** `/agents/automations/{automation_id}/resume`

Resumes scheduled delivery; one-time automations without a pending invocation require a future run_at.

### Parameters

- `automationID: string`

  `minLength: 0`, `maxLength: 1048576`

### Returns

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

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const automation = await client.beta.agents.automations.resume('automation_id');

console.log(automation);
```

#### 200 — Example

```json
{
  "id": "id",
  "created_at": 0,
  "created_by": {
    "type": "developer"
  },
  "expression": "expression",
  "metadata": {
    "foo": "string"
  },
  "name": "name",
  "object": "agent.automation",
  "status": "active",
  "target": {
    "agent": {
      "instructions": "instructions",
      "model": "model",
      "multi_agent": {
        "enabled": true,
        "max_concurrent_subagents": 1
      },
      "reasoning": {
        "effort": "none",
        "summary": "concise"
      },
      "service_tier": "auto",
      "text": {
        "format": {
          "type": "text"
        },
        "verbosity": "low"
      },
      "tools": [
        {
          "defer_loading": true,
          "description": "description",
          "name": "name",
          "parameters": {
            "foo": "bar"
          },
          "type": "function",
          "async": true
        }
      ],
      "compaction": {
        "async": true
      },
      "experimental": {
        "time_awareness": true
      }
    },
    "agent_id": "agent_id",
    "environment": {
      "type": "none"
    },
    "input": [
      {
        "content": [
          {
            "text": "text",
            "type": "input_text"
          }
        ],
        "role": "user",
        "type": "message"
      }
    ],
    "metadata": {
      "foo": "string"
    },
    "type": "new_session",
    "vault_ids": [
      "string"
    ]
  },
  "timezone": "timezone",
  "type": "periodic"
}
```

## Get an automation

`client.beta.agents.automations.retrieve(stringautomationID, RequestOptionsoptions?): Automation`

**get** `/agents/automations/{automation_id}`

Retrieves a project-owned automation.

### Parameters

- `automationID: string`

  `minLength: 0`, `maxLength: 1048576`

### Returns

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

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const automation = await client.beta.agents.automations.retrieve('automation_id');

console.log(automation);
```

#### 200 — Example

```json
{
  "id": "id",
  "created_at": 0,
  "created_by": {
    "type": "developer"
  },
  "expression": "expression",
  "metadata": {
    "foo": "string"
  },
  "name": "name",
  "object": "agent.automation",
  "status": "active",
  "target": {
    "agent": {
      "instructions": "instructions",
      "model": "model",
      "multi_agent": {
        "enabled": true,
        "max_concurrent_subagents": 1
      },
      "reasoning": {
        "effort": "none",
        "summary": "concise"
      },
      "service_tier": "auto",
      "text": {
        "format": {
          "type": "text"
        },
        "verbosity": "low"
      },
      "tools": [
        {
          "defer_loading": true,
          "description": "description",
          "name": "name",
          "parameters": {
            "foo": "bar"
          },
          "type": "function",
          "async": true
        }
      ],
      "compaction": {
        "async": true
      },
      "experimental": {
        "time_awareness": true
      }
    },
    "agent_id": "agent_id",
    "environment": {
      "type": "none"
    },
    "input": [
      {
        "content": [
          {
            "text": "text",
            "type": "input_text"
          }
        ],
        "role": "user",
        "type": "message"
      }
    ],
    "metadata": {
      "foo": "string"
    },
    "type": "new_session",
    "vault_ids": [
      "string"
    ]
  },
  "timezone": "timezone",
  "type": "periodic"
}
```

## Update an automation

`client.beta.agents.automations.update(stringautomationID, AutomationUpdateParamsbody, RequestOptionsoptions?): Automation`

**post** `/agents/automations/{automation_id}`

Updates supplied fields; target and metadata replace the whole field.

### Parameters

- `automationID: string`

  `minLength: 0`, `maxLength: 1048576`

- `body: AutomationUpdateParams`

  - `expression?: string`

    Only accepted for periodic automations.

    `minLength: 1`, `maxLength: 256`

  - `metadata?: Record<string, string>`

    Replaces all metadata; omit to leave unchanged.

  - `name?: string`

    `minLength: 1`, `maxLength: 256`

  - `run_at?: number`

    A future Unix timestamp in seconds; accepted only before a one-time scheduled invocation exists.

    `format: int64`

  - `target?: AutomationTargetParam`

    Replaces the complete target, retaining its type and any creator session.

    - `AutomationTargetParamNewSession`

      Create a session for each invocation.

      - `environment: EnvironmentParam`

        The execution environment for each new session.

        - `EnvironmentParamNone`

          Runs the agent without an execution environment.

          - `type: "none"`

            The type of the object. Always `none`.

            - `"none"`

        - `EnvironmentParamOpenAIHosted`

          An existing OpenAI-hosted environment or new inline/template-based hosted configuration.

          - `type: "openai_hosted"`

            The type of the object. Always `openai_hosted`.

            - `"openai_hosted"`

          - `capability_directories?: Array<string> | null`

            Directories that contain capabilities exposed to the agent. Defaults to an empty list.

            `minItems: 0`, `maxItems: 16384`

          - `container_size?: "small" | "medium" | "large"`

            The hosted container size. Omission selects the medium tier.

            - `"small"`

            - `"medium"`

            - `"large"`

          - `desktop?: Desktop | null`

            Desktop provisioning. Omission or null inherits the template setting, or defaults to disabled.

            - `enabled: boolean`

              Whether to provision the desktop and its browser proxy.

          - `env?: Record<string, string> | null`

            Environment variables made available to the agent.

          - `environment_id?: string`

            An existing prewarmed environment. Cannot be combined with a template or inline configuration.

            `minLength: 9`, `maxLength: 256`

          - `environment_template_id?: string`

            A reusable hosted template applied before inline session configuration. Omitted fields inherit the template; network overrides cannot broaden its policy.

            `minLength: 0`, `maxLength: 64`

          - `files?: Array<HostedEnvironmentFileParam> | null`

            Files available before the agent starts. Defaults to an empty list.

            `minItems: 0`, `maxItems: 50`

            - `HostedEnvironmentFileParamFileID`

              A file previously uploaded through the OpenAI Files API.

              - `file_id: string`

                The ID of the uploaded file.

                `minLength: 1`, `maxLength: 256`

              - `path: string`

                The absolute destination path inside `/workspace`.

                `minLength: 1`, `maxLength: 4096`

              - `type: "file_id"`

                The type of the object. Always `file_id`.

                - `"file_id"`

            - `HostedEnvironmentFileParamInline`

              A file supplied directly as standard-base64 data.

              - `data: string`

                The standard-base64-encoded file contents.

                `minLength: 0`, `maxLength: 6990508`

              - `path: string`

                The absolute destination path inside `/workspace`.

                `minLength: 1`, `maxLength: 4096`

              - `type: "inline"`

                The type of the object. Always `inline`.

                - `"inline"`

          - `network?: Network | null`

            Network access policy for the environment. If omitted, the API version determines whether network access is enabled or disabled.

            - `access: "enabled" | "disabled" | "restricted"`

              The environment's network access mode.

              - `"enabled"`

                Allows unrestricted network access.

              - `"disabled"`

                Disables network access.

              - `"restricted"`

                Applies the configured domain restrictions.

            - `allowed_domains?: Array<string> | null`

              Domains the environment may access when network access is restricted.

              `minItems: 0`, `maxItems: 16384`

            - `blocked_domains?: Array<string> | null`

              Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

              `minItems: 0`, `maxItems: 100`

          - `packages?: Packages | null`

            Packages to install in the environment. Defaults to empty package lists.

            - `npm?: Array<string> | null`

              npm packages to install globally. Defaults to an empty list.

              `minItems: 0`, `maxItems: 16384`

            - `python?: Array<string> | null`

              Python packages to install. Defaults to an empty list.

              `minItems: 0`, `maxItems: 16384`

            - `system?: Array<string> | null`

              System packages to install. Defaults to an empty list.

              `minItems: 0`, `maxItems: 16384`

          - `plugins?: Array<HostedPluginParam> | null`

            Plugins provided as inline ZIP archives. Defaults to an empty list.

            `minItems: 0`, `maxItems: 32`

            - `description: string`

              The plugin description declared in `.codex-plugin/plugin.json`.

              `minLength: 0`, `maxLength: 1048576`

            - `name: string`

              The plugin name declared in `.codex-plugin/plugin.json`.

              `minLength: 1`, `maxLength: 64`

            - `source: InlineCapabilitySourceParam`

              Provides ZIP bytes encoded with standard base64.

              - `data: string`

                Standard-base64 encoded ZIP archive bytes.

                `minLength: 1`, `maxLength: 70254592`

              - `media_type: "application/zip"`

                The archive media type, always `application/zip`.

                - `"application/zip"`

              - `type: "base64"`

                The type of the object. Always `base64`.

                - `"base64"`

            - `type: "inline"`

              The type of the object. Always `inline`.

              - `"inline"`

          - `setup_commands?: Array<SetupCommandParam> | null`

            Ordered, confidential setup commands. Command bodies are never returned.

            `minItems: 0`, `maxItems: 16`

            - `command: string`

              The shell command to execute.

              `minLength: 0`, `maxLength: 65536`

            - `cwd?: string | null`

              The absolute working directory. Defaults to `/workspace`.

              `minLength: 0`, `maxLength: 4096`

          - `skills?: Array<HostedSkillParam> | null`

            Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

            `minItems: 0`, `maxItems: 200`

            - `HostedSkillParamSkillReference`

              References a skill uploaded through the Skills API.

              - `skill_id: string`

                The ID of the skill created through `/v1/skills`.

                `minLength: 1`, `maxLength: 64`

              - `type: "skill_reference"`

                The type of the object. Always `skill_reference`.

                - `"skill_reference"`

              - `version?: string | null`

                The skill version, a positive integer or `latest`; omission selects the default.

                `minLength: 0`, `maxLength: 1048576`

            - `HostedSkillParamInline`

              Supplies a skill ZIP directly in the session request.

              - `description: string`

                The skill description declared in `SKILL.md`.

                `minLength: 0`, `maxLength: 1048576`

              - `name: string`

                The skill name declared in `SKILL.md`.

                `minLength: 1`, `maxLength: 64`

              - `source: InlineCapabilitySourceParam`

                Provides ZIP bytes encoded with standard base64.

              - `type: "inline"`

                The type of the object. Always `inline`.

                - `"inline"`

        - `EnvironmentParamSelfHosted`

          An application-hosted environment configured inline.

          - `type: "self_hosted"`

            The type of the object. Always `self_hosted`.

            - `"self_hosted"`

          - `workspace_directory: string`

            Absolute project directory inside the self-hosted environment.

            `minLength: 0`, `maxLength: 1048576`

          - `capability_directories?: Array<string> | null`

            Directories that contain capabilities exposed to the agent. Defaults to an empty list.

            `minItems: 0`, `maxItems: 16384`

      - `input: Array<AgentSessionInputMessageParam>`

        Initial user messages submitted with each new session.

        `minItems: 0`, `maxItems: 16384`

        - `content: Array<InputContentParam>`

          The content of the message.

          `minItems: 0`, `maxItems: 16384`

          - `InputContentParamInputText`

            Text input to the model.

            - `text: string`

              The text sent to the model.

              `minLength: 0`, `maxLength: 1048576`

            - `type: "input_text"`

              The type of the object. Always `input_text`.

              - `"input_text"`

          - `InputContentParamInputImage`

            Image input to the model.

            - `image_url: string`

              The URL of the image sent to the model.

              `minLength: 0`, `maxLength: 1048576`

            - `type: "input_image"`

              The type of the object. Always `input_image`.

              - `"input_image"`

        - `role: "user"`

          The role of the message author. Always `user`.

          - `"user"`

        - `type?: "message"`

          The type of the input item. Always `message`.

          - `"message"`

      - `type: "new_session"`

        The type of the object. Always `new_session`.

        - `"new_session"`

      - `agent?: Agent`

        Inline agent configuration. Provide exactly one of agent and agent_id.

        - `compaction?: Compaction | null`

          Context compaction settings. Omit to keep the current settings. A supplied object replaces the settings; null or an empty object enables background compaction.

          - `async?: boolean | null`

            Whether to compact context in the background. Omission or null defaults to true. Set to false to use blocking compaction. Background compaction may increase token usage.

        - `experimental?: Experimental`

          Experimental settings to merge by key. Omitted settings keep their current values.

          - `time_awareness?: boolean`

            Whether to give the model periodic current-time reminders. Omit to keep the current setting.

        - `instructions?: string | null`

          Additional instructions appended to the agent's default base instructions. Omit to leave unchanged.

          `minLength: 0`, `maxLength: 1048576`

        - `model?: string`

          The model to use for the agent. The requested model name is preserved.

          `minLength: 0`, `maxLength: 1048576`

        - `multi_agent?: MultiAgentConfigParam | null`

          Configuration for creating and coordinating subagents.

          - `enabled: boolean`

            Whether subagent tools are enabled.

          - `max_concurrent_subagents?: number`

            Maximum number of subagents that may run concurrently. Defaults to 6.

            `format: int64`, `minimum: 1`, `maximum: 4294967295`

        - `reasoning?: AgentReasoningParam | null`

          Configuration for model reasoning. Omit to keep the current settings; pass `null` to reset to the model's default effort.

          - `effort?: "none" | "minimal" | "low" | 4 more | null`

            The amount of reasoning effort the model should use. Omission lets the model select it.

            - `"none"`

            - `"minimal"`

            - `"low"`

            - `"medium"`

            - `"high"`

            - `"xhigh"`

            - `"max"`

          - `summary?: "concise" | "detailed" | "auto" | null`

            Controls whether the response includes a reasoning summary.

            - `"concise"`

              Returns a concise reasoning summary when supported.

            - `"detailed"`

              Returns a detailed reasoning summary when supported.

            - `"auto"`

              Automatically selects the most detailed summary supported by the model.

        - `service_tier?: "auto" | "default" | "flex" | 3 more | null`

          The service tier used for model requests.

          - `"auto"`

            Selects the service tier automatically.

          - `"default"`

            Uses the default service tier.

          - `"flex"`

            Uses the flex service tier.

          - `"priority"`

            Uses the priority service tier.

          - `"fast"`

            Uses the fast service tier.

          - `"ultrafast"`

            Uses the ultrafast service tier.

        - `text?: AgentTextParam | null`

          Configuration for text generated by the agent.

          - `format?: TextFormatParam | null`

            The output format. Omission uses ordinary text (`{"type": "text"}`).

            - `TextFormatParamText`

              Generates ordinary text without a structured-output constraint.

              - `type: "text"`

                The type of the object. Always `text`.

                - `"text"`

            - `TextFormatParamJSONSchema`

              Constrains generated text to a JSON Schema.

              - `schema: Record<string, unknown>`

                The JSON Schema that generated text must match.

              - `type: "json_schema"`

                The type of the object. Always `json_schema`.

                - `"json_schema"`

          - `verbosity?: "low" | "medium" | "high" | null`

            The amount of text the model should produce. Defaults to `medium`, matching Responses.

            - `"low"`

              Produces less text.

            - `"medium"`

              Uses the default amount of text.

            - `"high"`

              Produces more text.

        - `tools?: Array<AgentToolParam> | null`

          Tools available to the agent. Omit to inherit, or pass null to clear them. The resolved tool list must fit within 3 MiB (3,145,728 bytes) of compact UTF-8 JSON.

          `minItems: 0`, `maxItems: 16384`

          - `AgentToolConfigParamFunction`

            A function defined by the application.

            - `description: string`

              A description of what the function does.

              `minLength: 0`, `maxLength: 1048576`

            - `name: string`

              The name of the function.

              `minLength: 0`, `maxLength: 1048576`

            - `parameters: Record<string, unknown>`

              A JSON Schema object describing the function's arguments.

            - `type: "function"`

              The type of the object. Always `function`.

              - `"function"`

            - `async?: boolean`

              Whether the agent continues without waiting for the function result. Defaults to `false`.

            - `defer_loading?: boolean`

              Whether this function is deferred and discovered through tool search. Defaults to `false`.

          - `AgentToolConfigParamToolSearch`

            Discovers deferred function tools and loads them into the model context.

            - `type: "tool_search"`

              The type of the object. Always `tool_search`.

              - `"tool_search"`

          - `AgentToolConfigParamProgrammaticToolCalling`

            Enables calling tools from model-generated code.

            - `type: "programmatic_tool_calling"`

              The type of the object. Always `programmatic_tool_calling`.

              - `"programmatic_tool_calling"`

            - `enabled?: boolean`

              Whether tools can be called from model-generated code. Defaults to `true`.

          - `AgentToolConfigParamMcp`

            Tools provided by a remote MCP server.

            - `server_label: string`

              A label used to identify the MCP server in tool calls.

              `minLength: 0`, `maxLength: 1048576`

            - `transport: McpTransportParam`

              The transport used to connect to the MCP server.

              - `McpTransportConfigParamHTTP`

                Connects to an MCP server over HTTP.

                - `server_url: string`

                  The URL of the MCP server.

                  `minLength: 0`, `maxLength: 1048576`

                - `type: "http"`

                  The type of the object. Always `http`.

                  - `"http"`

                - `authorization?: string | null`

                  The authorization value sent to the MCP server, if any.

                  `minLength: 0`, `maxLength: 1048576`

                - `headers?: Record<string, string> | null`

                  Additional HTTP headers sent to the MCP server.

              - `McpTransportConfigParamStdio`

                Starts an MCP server as a local process.

                - `command: string`

                  The command used to start the MCP server.

                  `minLength: 0`, `maxLength: 1048576`

                - `cwd: string`

                  The working directory used to start the MCP server.

                  `minLength: 0`, `maxLength: 1048576`

                - `type: "stdio"`

                  The type of the object. Always `stdio`.

                  - `"stdio"`

                - `args?: Array<string> | null`

                  Arguments passed to the MCP server command.

                  `minItems: 0`, `maxItems: 16384`

                - `env?: Record<string, string> | null`

                  Environment variables set for the MCP server process.

                - `env_vars?: Array<string> | null`

                  Environment variable names to inherit from the selected execution environment.

                  `minItems: 0`, `maxItems: 16384`

            - `type: "mcp"`

              The type of the object. Always `mcp`.

              - `"mcp"`

            - `allowed_tools?: Array<string> | null`

              The MCP tools the agent may call. All server tools are allowed when omitted.

              `minItems: 0`, `maxItems: 16384`

            - `connection_origin?: "service" | "environment" | null`

              Selects where outbound MCP HTTP connections originate. Omitted or `service` uses the Managed Agents service network; `environment` uses the session's selected environment.

              - `"service"`

                Uses the Managed Agents service network.

              - `"environment"`

                Uses the session's execution environment.

            - `credential_id?: string | null`

              The attached vault credential used to authenticate this MCP server. Optional when exactly one attached credential matches the server URL.

              `minLength: 0`, `maxLength: 1048576`

            - `request_metadata?: Record<string, unknown> | null`

              Metadata included with requests to this MCP server.

            - `required?: boolean`

              Whether this MCP server must initialize before the first turn. Defaults to `false`.

          - `AgentToolConfigParamWebSearch`

            Web search.

            - `type: "web_search"`

              The type of the object. Always `web_search`.

              - `"web_search"`

            - `allowed_domains?: Array<string> | null`

              Domains the search may include.

              `minItems: 0`, `maxItems: 16384`

            - `context_size?: "low" | "medium" | "high" | null`

              The amount of search context made available to the model. Defaults to `medium`.

              - `"low"`

              - `"medium"`

              - `"high"`

            - `location?: Location | null`

              Approximate location used to localize search results.

              - `city?: string | null`

                The city name.

                `minLength: 0`, `maxLength: 1048576`

              - `country?: string | null`

                The two-letter ISO country code, such as `US`.

                `minLength: 0`, `maxLength: 1048576`

              - `region?: string | null`

                The region or state name.

                `minLength: 0`, `maxLength: 1048576`

              - `timezone?: string | null`

                The IANA timezone, such as `America/Los_Angeles`.

                `minLength: 0`, `maxLength: 1048576`

            - `mode?: "disabled" | "cached" | "live" | null`

              The source used for web search results. Defaults to `live`.

              - `"disabled"`

                Disables web search.

              - `"cached"`

                Uses cached search results.

              - `"live"`

                Searches the live web.

          - `AgentToolConfigParamComputerUse`

            Browser use in an OpenAI-hosted session.

            - `type: "computer_use"`

              The type of the object. Always `computer_use`.

              - `"computer_use"`

            - `include_screenshots?: boolean`

              Whether computer tool outputs include screenshots. Defaults to `false`.

          - `AgentToolConfigParamAutomations`

            Lets the agent manage its own scheduled wakeups.

            - `type: "automations"`

              The type of the object. Always `automations`.

              - `"automations"`

      - `agent_id?: string`

        A saved agent ID. Provide exactly one of agent and agent_id.

        `minLength: 0`, `maxLength: 64`

      - `metadata?: Record<string, string> | null`

        Metadata attached to each new session.

      - `vault_ids?: Array<string> | null`

        The IDs of vaults made available to each new session.

        `minItems: 0`, `maxItems: 16384`

    - `AutomationTargetParamExistingSession`

      Deliver instructions to an existing session.

      - `instructions: string`

        Instructions delivered as an automation notification.

        `minLength: 0`, `maxLength: 1048576`

      - `session_id: string`

        The session receiving each invocation.

        `minLength: 0`, `maxLength: 1048576`

      - `type: "existing_session"`

        The type of the object. Always `existing_session`.

        - `"existing_session"`

  - `timezone?: string`

    Only accepted for periodic automations.

    `minLength: 1`, `maxLength: 128`

### Returns

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

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const automation = await client.beta.agents.automations.update('automation_id');

console.log(automation);
```

#### 200 — Example

```json
{
  "id": "id",
  "created_at": 0,
  "created_by": {
    "type": "developer"
  },
  "expression": "expression",
  "metadata": {
    "foo": "string"
  },
  "name": "name",
  "object": "agent.automation",
  "status": "active",
  "target": {
    "agent": {
      "instructions": "instructions",
      "model": "model",
      "multi_agent": {
        "enabled": true,
        "max_concurrent_subagents": 1
      },
      "reasoning": {
        "effort": "none",
        "summary": "concise"
      },
      "service_tier": "auto",
      "text": {
        "format": {
          "type": "text"
        },
        "verbosity": "low"
      },
      "tools": [
        {
          "defer_loading": true,
          "description": "description",
          "name": "name",
          "parameters": {
            "foo": "bar"
          },
          "type": "function",
          "async": true
        }
      ],
      "compaction": {
        "async": true
      },
      "experimental": {
        "time_awareness": true
      }
    },
    "agent_id": "agent_id",
    "environment": {
      "type": "none"
    },
    "input": [
      {
        "content": [
          {
            "text": "text",
            "type": "input_text"
          }
        ],
        "role": "user",
        "type": "message"
      }
    ],
    "metadata": {
      "foo": "string"
    },
    "type": "new_session",
    "vault_ids": [
      "string"
    ]
  },
  "timezone": "timezone",
  "type": "periodic"
}
```

## Domain Types

### Automation

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

### Automation Agent Config

- `AutomationAgentConfig`

  Inline agent configuration without a generated session-local identity.

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

### Automation Created By

- `AutomationCreatedBy = AutomationCreatedByResourceDeveloper | AutomationCreatedByResourceAgent`

  How the automation was created, independently of how an invocation started.

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

### Automation Deleted

- `AutomationDeleted`

  - `id: string`

    The deleted automation ID.

    `minLength: 0`

  - `deleted: boolean`

    Always true.

  - `object: "agent.automation.deleted"`

    Always `agent.automation.deleted`.

    - `"agent.automation.deleted"`

### Automation Environment

- `AutomationEnvironment = AutomationEnvironmentResourceNone | AutomationEnvironmentResourceOpenAIHosted | AutomationEnvironmentResourceSelfHosted`

  Environment selection saved before an invocation creates its session.

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

### Automation Target

- `AutomationTarget = AutomationTargetResourceNewSession | AutomationTargetResourceExistingSession`

  Saved target configuration, excluding confidential request-only values.

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

### Automation Target Param

- `AutomationTargetParam = AutomationTargetParamNewSession | AutomationTargetParamExistingSession`

  The session an automation invocation targets.

  - `AutomationTargetParamNewSession`

    Create a session for each invocation.

    - `environment: EnvironmentParam`

      The execution environment for each new session.

      - `EnvironmentParamNone`

        Runs the agent without an execution environment.

        - `type: "none"`

          The type of the object. Always `none`.

          - `"none"`

      - `EnvironmentParamOpenAIHosted`

        An existing OpenAI-hosted environment or new inline/template-based hosted configuration.

        - `type: "openai_hosted"`

          The type of the object. Always `openai_hosted`.

          - `"openai_hosted"`

        - `capability_directories?: Array<string> | null`

          Directories that contain capabilities exposed to the agent. Defaults to an empty list.

          `minItems: 0`, `maxItems: 16384`

        - `container_size?: "small" | "medium" | "large"`

          The hosted container size. Omission selects the medium tier.

          - `"small"`

          - `"medium"`

          - `"large"`

        - `desktop?: Desktop | null`

          Desktop provisioning. Omission or null inherits the template setting, or defaults to disabled.

          - `enabled: boolean`

            Whether to provision the desktop and its browser proxy.

        - `env?: Record<string, string> | null`

          Environment variables made available to the agent.

        - `environment_id?: string`

          An existing prewarmed environment. Cannot be combined with a template or inline configuration.

          `minLength: 9`, `maxLength: 256`

        - `environment_template_id?: string`

          A reusable hosted template applied before inline session configuration. Omitted fields inherit the template; network overrides cannot broaden its policy.

          `minLength: 0`, `maxLength: 64`

        - `files?: Array<HostedEnvironmentFileParam> | null`

          Files available before the agent starts. Defaults to an empty list.

          `minItems: 0`, `maxItems: 50`

          - `HostedEnvironmentFileParamFileID`

            A file previously uploaded through the OpenAI Files API.

            - `file_id: string`

              The ID of the uploaded file.

              `minLength: 1`, `maxLength: 256`

            - `path: string`

              The absolute destination path inside `/workspace`.

              `minLength: 1`, `maxLength: 4096`

            - `type: "file_id"`

              The type of the object. Always `file_id`.

              - `"file_id"`

          - `HostedEnvironmentFileParamInline`

            A file supplied directly as standard-base64 data.

            - `data: string`

              The standard-base64-encoded file contents.

              `minLength: 0`, `maxLength: 6990508`

            - `path: string`

              The absolute destination path inside `/workspace`.

              `minLength: 1`, `maxLength: 4096`

            - `type: "inline"`

              The type of the object. Always `inline`.

              - `"inline"`

        - `network?: Network | null`

          Network access policy for the environment. If omitted, the API version determines whether network access is enabled or disabled.

          - `access: "enabled" | "disabled" | "restricted"`

            The environment's network access mode.

            - `"enabled"`

              Allows unrestricted network access.

            - `"disabled"`

              Disables network access.

            - `"restricted"`

              Applies the configured domain restrictions.

          - `allowed_domains?: Array<string> | null`

            Domains the environment may access when network access is restricted.

            `minItems: 0`, `maxItems: 16384`

          - `blocked_domains?: Array<string> | null`

            Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

            `minItems: 0`, `maxItems: 100`

        - `packages?: Packages | null`

          Packages to install in the environment. Defaults to empty package lists.

          - `npm?: Array<string> | null`

            npm packages to install globally. Defaults to an empty list.

            `minItems: 0`, `maxItems: 16384`

          - `python?: Array<string> | null`

            Python packages to install. Defaults to an empty list.

            `minItems: 0`, `maxItems: 16384`

          - `system?: Array<string> | null`

            System packages to install. Defaults to an empty list.

            `minItems: 0`, `maxItems: 16384`

        - `plugins?: Array<HostedPluginParam> | null`

          Plugins provided as inline ZIP archives. Defaults to an empty list.

          `minItems: 0`, `maxItems: 32`

          - `description: string`

            The plugin description declared in `.codex-plugin/plugin.json`.

            `minLength: 0`, `maxLength: 1048576`

          - `name: string`

            The plugin name declared in `.codex-plugin/plugin.json`.

            `minLength: 1`, `maxLength: 64`

          - `source: InlineCapabilitySourceParam`

            Provides ZIP bytes encoded with standard base64.

            - `data: string`

              Standard-base64 encoded ZIP archive bytes.

              `minLength: 1`, `maxLength: 70254592`

            - `media_type: "application/zip"`

              The archive media type, always `application/zip`.

              - `"application/zip"`

            - `type: "base64"`

              The type of the object. Always `base64`.

              - `"base64"`

          - `type: "inline"`

            The type of the object. Always `inline`.

            - `"inline"`

        - `setup_commands?: Array<SetupCommandParam> | null`

          Ordered, confidential setup commands. Command bodies are never returned.

          `minItems: 0`, `maxItems: 16`

          - `command: string`

            The shell command to execute.

            `minLength: 0`, `maxLength: 65536`

          - `cwd?: string | null`

            The absolute working directory. Defaults to `/workspace`.

            `minLength: 0`, `maxLength: 4096`

        - `skills?: Array<HostedSkillParam> | null`

          Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

          `minItems: 0`, `maxItems: 200`

          - `HostedSkillParamSkillReference`

            References a skill uploaded through the Skills API.

            - `skill_id: string`

              The ID of the skill created through `/v1/skills`.

              `minLength: 1`, `maxLength: 64`

            - `type: "skill_reference"`

              The type of the object. Always `skill_reference`.

              - `"skill_reference"`

            - `version?: string | null`

              The skill version, a positive integer or `latest`; omission selects the default.

              `minLength: 0`, `maxLength: 1048576`

          - `HostedSkillParamInline`

            Supplies a skill ZIP directly in the session request.

            - `description: string`

              The skill description declared in `SKILL.md`.

              `minLength: 0`, `maxLength: 1048576`

            - `name: string`

              The skill name declared in `SKILL.md`.

              `minLength: 1`, `maxLength: 64`

            - `source: InlineCapabilitySourceParam`

              Provides ZIP bytes encoded with standard base64.

            - `type: "inline"`

              The type of the object. Always `inline`.

              - `"inline"`

      - `EnvironmentParamSelfHosted`

        An application-hosted environment configured inline.

        - `type: "self_hosted"`

          The type of the object. Always `self_hosted`.

          - `"self_hosted"`

        - `workspace_directory: string`

          Absolute project directory inside the self-hosted environment.

          `minLength: 0`, `maxLength: 1048576`

        - `capability_directories?: Array<string> | null`

          Directories that contain capabilities exposed to the agent. Defaults to an empty list.

          `minItems: 0`, `maxItems: 16384`

    - `input: Array<AgentSessionInputMessageParam>`

      Initial user messages submitted with each new session.

      `minItems: 0`, `maxItems: 16384`

      - `content: Array<InputContentParam>`

        The content of the message.

        `minItems: 0`, `maxItems: 16384`

        - `InputContentParamInputText`

          Text input to the model.

          - `text: string`

            The text sent to the model.

            `minLength: 0`, `maxLength: 1048576`

          - `type: "input_text"`

            The type of the object. Always `input_text`.

            - `"input_text"`

        - `InputContentParamInputImage`

          Image input to the model.

          - `image_url: string`

            The URL of the image sent to the model.

            `minLength: 0`, `maxLength: 1048576`

          - `type: "input_image"`

            The type of the object. Always `input_image`.

            - `"input_image"`

      - `role: "user"`

        The role of the message author. Always `user`.

        - `"user"`

      - `type?: "message"`

        The type of the input item. Always `message`.

        - `"message"`

    - `type: "new_session"`

      The type of the object. Always `new_session`.

      - `"new_session"`

    - `agent?: Agent`

      Inline agent configuration. Provide exactly one of agent and agent_id.

      - `compaction?: Compaction | null`

        Context compaction settings. Omit to keep the current settings. A supplied object replaces the settings; null or an empty object enables background compaction.

        - `async?: boolean | null`

          Whether to compact context in the background. Omission or null defaults to true. Set to false to use blocking compaction. Background compaction may increase token usage.

      - `experimental?: Experimental`

        Experimental settings to merge by key. Omitted settings keep their current values.

        - `time_awareness?: boolean`

          Whether to give the model periodic current-time reminders. Omit to keep the current setting.

      - `instructions?: string | null`

        Additional instructions appended to the agent's default base instructions. Omit to leave unchanged.

        `minLength: 0`, `maxLength: 1048576`

      - `model?: string`

        The model to use for the agent. The requested model name is preserved.

        `minLength: 0`, `maxLength: 1048576`

      - `multi_agent?: MultiAgentConfigParam | null`

        Configuration for creating and coordinating subagents.

        - `enabled: boolean`

          Whether subagent tools are enabled.

        - `max_concurrent_subagents?: number`

          Maximum number of subagents that may run concurrently. Defaults to 6.

          `format: int64`, `minimum: 1`, `maximum: 4294967295`

      - `reasoning?: AgentReasoningParam | null`

        Configuration for model reasoning. Omit to keep the current settings; pass `null` to reset to the model's default effort.

        - `effort?: "none" | "minimal" | "low" | 4 more | null`

          The amount of reasoning effort the model should use. Omission lets the model select it.

          - `"none"`

          - `"minimal"`

          - `"low"`

          - `"medium"`

          - `"high"`

          - `"xhigh"`

          - `"max"`

        - `summary?: "concise" | "detailed" | "auto" | null`

          Controls whether the response includes a reasoning summary.

          - `"concise"`

            Returns a concise reasoning summary when supported.

          - `"detailed"`

            Returns a detailed reasoning summary when supported.

          - `"auto"`

            Automatically selects the most detailed summary supported by the model.

      - `service_tier?: "auto" | "default" | "flex" | 3 more | null`

        The service tier used for model requests.

        - `"auto"`

          Selects the service tier automatically.

        - `"default"`

          Uses the default service tier.

        - `"flex"`

          Uses the flex service tier.

        - `"priority"`

          Uses the priority service tier.

        - `"fast"`

          Uses the fast service tier.

        - `"ultrafast"`

          Uses the ultrafast service tier.

      - `text?: AgentTextParam | null`

        Configuration for text generated by the agent.

        - `format?: TextFormatParam | null`

          The output format. Omission uses ordinary text (`{"type": "text"}`).

          - `TextFormatParamText`

            Generates ordinary text without a structured-output constraint.

            - `type: "text"`

              The type of the object. Always `text`.

              - `"text"`

          - `TextFormatParamJSONSchema`

            Constrains generated text to a JSON Schema.

            - `schema: Record<string, unknown>`

              The JSON Schema that generated text must match.

            - `type: "json_schema"`

              The type of the object. Always `json_schema`.

              - `"json_schema"`

        - `verbosity?: "low" | "medium" | "high" | null`

          The amount of text the model should produce. Defaults to `medium`, matching Responses.

          - `"low"`

            Produces less text.

          - `"medium"`

            Uses the default amount of text.

          - `"high"`

            Produces more text.

      - `tools?: Array<AgentToolParam> | null`

        Tools available to the agent. Omit to inherit, or pass null to clear them. The resolved tool list must fit within 3 MiB (3,145,728 bytes) of compact UTF-8 JSON.

        `minItems: 0`, `maxItems: 16384`

        - `AgentToolConfigParamFunction`

          A function defined by the application.

          - `description: string`

            A description of what the function does.

            `minLength: 0`, `maxLength: 1048576`

          - `name: string`

            The name of the function.

            `minLength: 0`, `maxLength: 1048576`

          - `parameters: Record<string, unknown>`

            A JSON Schema object describing the function's arguments.

          - `type: "function"`

            The type of the object. Always `function`.

            - `"function"`

          - `async?: boolean`

            Whether the agent continues without waiting for the function result. Defaults to `false`.

          - `defer_loading?: boolean`

            Whether this function is deferred and discovered through tool search. Defaults to `false`.

        - `AgentToolConfigParamToolSearch`

          Discovers deferred function tools and loads them into the model context.

          - `type: "tool_search"`

            The type of the object. Always `tool_search`.

            - `"tool_search"`

        - `AgentToolConfigParamProgrammaticToolCalling`

          Enables calling tools from model-generated code.

          - `type: "programmatic_tool_calling"`

            The type of the object. Always `programmatic_tool_calling`.

            - `"programmatic_tool_calling"`

          - `enabled?: boolean`

            Whether tools can be called from model-generated code. Defaults to `true`.

        - `AgentToolConfigParamMcp`

          Tools provided by a remote MCP server.

          - `server_label: string`

            A label used to identify the MCP server in tool calls.

            `minLength: 0`, `maxLength: 1048576`

          - `transport: McpTransportParam`

            The transport used to connect to the MCP server.

            - `McpTransportConfigParamHTTP`

              Connects to an MCP server over HTTP.

              - `server_url: string`

                The URL of the MCP server.

                `minLength: 0`, `maxLength: 1048576`

              - `type: "http"`

                The type of the object. Always `http`.

                - `"http"`

              - `authorization?: string | null`

                The authorization value sent to the MCP server, if any.

                `minLength: 0`, `maxLength: 1048576`

              - `headers?: Record<string, string> | null`

                Additional HTTP headers sent to the MCP server.

            - `McpTransportConfigParamStdio`

              Starts an MCP server as a local process.

              - `command: string`

                The command used to start the MCP server.

                `minLength: 0`, `maxLength: 1048576`

              - `cwd: string`

                The working directory used to start the MCP server.

                `minLength: 0`, `maxLength: 1048576`

              - `type: "stdio"`

                The type of the object. Always `stdio`.

                - `"stdio"`

              - `args?: Array<string> | null`

                Arguments passed to the MCP server command.

                `minItems: 0`, `maxItems: 16384`

              - `env?: Record<string, string> | null`

                Environment variables set for the MCP server process.

              - `env_vars?: Array<string> | null`

                Environment variable names to inherit from the selected execution environment.

                `minItems: 0`, `maxItems: 16384`

          - `type: "mcp"`

            The type of the object. Always `mcp`.

            - `"mcp"`

          - `allowed_tools?: Array<string> | null`

            The MCP tools the agent may call. All server tools are allowed when omitted.

            `minItems: 0`, `maxItems: 16384`

          - `connection_origin?: "service" | "environment" | null`

            Selects where outbound MCP HTTP connections originate. Omitted or `service` uses the Managed Agents service network; `environment` uses the session's selected environment.

            - `"service"`

              Uses the Managed Agents service network.

            - `"environment"`

              Uses the session's execution environment.

          - `credential_id?: string | null`

            The attached vault credential used to authenticate this MCP server. Optional when exactly one attached credential matches the server URL.

            `minLength: 0`, `maxLength: 1048576`

          - `request_metadata?: Record<string, unknown> | null`

            Metadata included with requests to this MCP server.

          - `required?: boolean`

            Whether this MCP server must initialize before the first turn. Defaults to `false`.

        - `AgentToolConfigParamWebSearch`

          Web search.

          - `type: "web_search"`

            The type of the object. Always `web_search`.

            - `"web_search"`

          - `allowed_domains?: Array<string> | null`

            Domains the search may include.

            `minItems: 0`, `maxItems: 16384`

          - `context_size?: "low" | "medium" | "high" | null`

            The amount of search context made available to the model. Defaults to `medium`.

            - `"low"`

            - `"medium"`

            - `"high"`

          - `location?: Location | null`

            Approximate location used to localize search results.

            - `city?: string | null`

              The city name.

              `minLength: 0`, `maxLength: 1048576`

            - `country?: string | null`

              The two-letter ISO country code, such as `US`.

              `minLength: 0`, `maxLength: 1048576`

            - `region?: string | null`

              The region or state name.

              `minLength: 0`, `maxLength: 1048576`

            - `timezone?: string | null`

              The IANA timezone, such as `America/Los_Angeles`.

              `minLength: 0`, `maxLength: 1048576`

          - `mode?: "disabled" | "cached" | "live" | null`

            The source used for web search results. Defaults to `live`.

            - `"disabled"`

              Disables web search.

            - `"cached"`

              Uses cached search results.

            - `"live"`

              Searches the live web.

        - `AgentToolConfigParamComputerUse`

          Browser use in an OpenAI-hosted session.

          - `type: "computer_use"`

            The type of the object. Always `computer_use`.

            - `"computer_use"`

          - `include_screenshots?: boolean`

            Whether computer tool outputs include screenshots. Defaults to `false`.

        - `AgentToolConfigParamAutomations`

          Lets the agent manage its own scheduled wakeups.

          - `type: "automations"`

            The type of the object. Always `automations`.

            - `"automations"`

    - `agent_id?: string`

      A saved agent ID. Provide exactly one of agent and agent_id.

      `minLength: 0`, `maxLength: 64`

    - `metadata?: Record<string, string> | null`

      Metadata attached to each new session.

    - `vault_ids?: Array<string> | null`

      The IDs of vaults made available to each new session.

      `minItems: 0`, `maxItems: 16384`

  - `AutomationTargetParamExistingSession`

    Deliver instructions to an existing session.

    - `instructions: string`

      Instructions delivered as an automation notification.

      `minLength: 0`, `maxLength: 1048576`

    - `session_id: string`

      The session receiving each invocation.

      `minLength: 0`, `maxLength: 1048576`

    - `type: "existing_session"`

      The type of the object. Always `existing_session`.

      - `"existing_session"`

### One Time Automation

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

  - `type: "once"`

    The type of the object. Always `once`.

    - `"once"`

### Periodic Automation

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

# Invocations

## Invoke an automation

`client.beta.agents.automations.invocations.create(stringautomationID, RequestOptionsoptions?): AutomationInvocation`

**post** `/agents/automations/{automation_id}/invocations`

Queues a manual delivery without changing the saved schedule.

### Parameters

- `automationID: string`

  `minLength: 0`, `maxLength: 1048576`

### Returns

- `AutomationInvocation`

  One attempted delivery by an automation.

  - `id: string`

    The invocation ID.

    `minLength: 0`

  - `automation_id: string`

    The automation that owns the invocation.

    `minLength: 0`

  - `created_at: number`

    The creation time as a Unix timestamp in seconds.

    `format: int64`

  - `error: Error | null`

    The permanent delivery failure, or null when no failure occurred.

    - `code: string`

      A machine-readable error code.

      `minLength: 0`

    - `message: string`

      A public explanation of the delivery failure.

      `minLength: 0`

  - `object: "agent.automation.invocation"`

    Always `agent.automation.invocation`.

    - `"agent.automation.invocation"`

  - `scheduled_at: number | null`

    The intended occurrence as a Unix timestamp in seconds, or null for manual runs.

    `format: int64`

  - `session_id: string | null`

    The target or newly created session ID, or null before one is available.

    `minLength: 0`

  - `skip_reason: "pending_delivery" | null`

    Why an occurrence was skipped, or null when it was not skipped.

    - `"pending_delivery"`

  - `source: AutomationInvocationSource`

    Whether the invocation was manual or scheduled.

    - `AutomationInvocationSourceResourceManual`

      - `type: "manual"`

        The type of the object. Always `manual`.

        - `"manual"`

    - `AutomationInvocationSourceResourceAutomation`

      - `automation: Automation`

        The automation snapshot for this occurrence, excluding confidential values.

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

      - `type: "automation"`

        The type of the object. Always `automation`.

        - `"automation"`

  - `status: "queued" | "completed" | "failed" | "skipped"`

    Delivery status; completed does not mean the agent's work has finished.

    - `"queued"`

    - `"completed"`

    - `"failed"`

    - `"skipped"`

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const automationInvocation = await client.beta.agents.automations.invocations.create(
  'automation_id',
);

console.log(automationInvocation.id);
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

`client.beta.agents.automations.invocations.list(stringautomationID, InvocationListParamsquery?, RequestOptionsoptions?): CursorPage<AutomationInvocation>`

**get** `/agents/automations/{automation_id}/invocations`

Lists delivery records for a project-owned automation.

### Parameters

- `automationID: string`

  `minLength: 0`, `maxLength: 1048576`

- `query: InvocationListParams`

  - `after?: string`

    Return resources after this resource ID in the selected order.

    `minLength: 0`, `maxLength: 1048576`

  - `limit?: number`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

    `format: int64`, `minimum: 1`, `maximum: 100`

  - `order?: "asc" | "desc"`

    The order in which resources are returned. Defaults to `desc`.

    - `"asc"`

      Returns resources in ascending order.

    - `"desc"`

      Returns resources in descending order.

### Returns

- `AutomationInvocation`

  One attempted delivery by an automation.

  - `id: string`

    The invocation ID.

    `minLength: 0`

  - `automation_id: string`

    The automation that owns the invocation.

    `minLength: 0`

  - `created_at: number`

    The creation time as a Unix timestamp in seconds.

    `format: int64`

  - `error: Error | null`

    The permanent delivery failure, or null when no failure occurred.

    - `code: string`

      A machine-readable error code.

      `minLength: 0`

    - `message: string`

      A public explanation of the delivery failure.

      `minLength: 0`

  - `object: "agent.automation.invocation"`

    Always `agent.automation.invocation`.

    - `"agent.automation.invocation"`

  - `scheduled_at: number | null`

    The intended occurrence as a Unix timestamp in seconds, or null for manual runs.

    `format: int64`

  - `session_id: string | null`

    The target or newly created session ID, or null before one is available.

    `minLength: 0`

  - `skip_reason: "pending_delivery" | null`

    Why an occurrence was skipped, or null when it was not skipped.

    - `"pending_delivery"`

  - `source: AutomationInvocationSource`

    Whether the invocation was manual or scheduled.

    - `AutomationInvocationSourceResourceManual`

      - `type: "manual"`

        The type of the object. Always `manual`.

        - `"manual"`

    - `AutomationInvocationSourceResourceAutomation`

      - `automation: Automation`

        The automation snapshot for this occurrence, excluding confidential values.

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

      - `type: "automation"`

        The type of the object. Always `automation`.

        - `"automation"`

  - `status: "queued" | "completed" | "failed" | "skipped"`

    Delivery status; completed does not mean the agent's work has finished.

    - `"queued"`

    - `"completed"`

    - `"failed"`

    - `"skipped"`

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const automationInvocation of client.beta.agents.automations.invocations.list(
  'automation_id',
)) {
  console.log(automationInvocation.id);
}
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

`client.beta.agents.automations.invocations.retrieve(stringinvocationID, InvocationRetrieveParamsparams, RequestOptionsoptions?): AutomationInvocation`

**get** `/agents/automations/{automation_id}/invocations/{invocation_id}`

Retrieves a delivery record for a project-owned automation.

### Parameters

- `invocationID: string`

  `minLength: 0`, `maxLength: 1048576`

- `params: InvocationRetrieveParams`

  - `automation_id: string`

    `minLength: 0`, `maxLength: 1048576`

### Returns

- `AutomationInvocation`

  One attempted delivery by an automation.

  - `id: string`

    The invocation ID.

    `minLength: 0`

  - `automation_id: string`

    The automation that owns the invocation.

    `minLength: 0`

  - `created_at: number`

    The creation time as a Unix timestamp in seconds.

    `format: int64`

  - `error: Error | null`

    The permanent delivery failure, or null when no failure occurred.

    - `code: string`

      A machine-readable error code.

      `minLength: 0`

    - `message: string`

      A public explanation of the delivery failure.

      `minLength: 0`

  - `object: "agent.automation.invocation"`

    Always `agent.automation.invocation`.

    - `"agent.automation.invocation"`

  - `scheduled_at: number | null`

    The intended occurrence as a Unix timestamp in seconds, or null for manual runs.

    `format: int64`

  - `session_id: string | null`

    The target or newly created session ID, or null before one is available.

    `minLength: 0`

  - `skip_reason: "pending_delivery" | null`

    Why an occurrence was skipped, or null when it was not skipped.

    - `"pending_delivery"`

  - `source: AutomationInvocationSource`

    Whether the invocation was manual or scheduled.

    - `AutomationInvocationSourceResourceManual`

      - `type: "manual"`

        The type of the object. Always `manual`.

        - `"manual"`

    - `AutomationInvocationSourceResourceAutomation`

      - `automation: Automation`

        The automation snapshot for this occurrence, excluding confidential values.

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

      - `type: "automation"`

        The type of the object. Always `automation`.

        - `"automation"`

  - `status: "queued" | "completed" | "failed" | "skipped"`

    Delivery status; completed does not mean the agent's work has finished.

    - `"queued"`

    - `"completed"`

    - `"failed"`

    - `"skipped"`

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const automationInvocation = await client.beta.agents.automations.invocations.retrieve(
  'invocation_id',
  { automation_id: 'automation_id' },
);

console.log(automationInvocation.id);
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

- `AutomationInvocation`

  One attempted delivery by an automation.

  - `id: string`

    The invocation ID.

    `minLength: 0`

  - `automation_id: string`

    The automation that owns the invocation.

    `minLength: 0`

  - `created_at: number`

    The creation time as a Unix timestamp in seconds.

    `format: int64`

  - `error: Error | null`

    The permanent delivery failure, or null when no failure occurred.

    - `code: string`

      A machine-readable error code.

      `minLength: 0`

    - `message: string`

      A public explanation of the delivery failure.

      `minLength: 0`

  - `object: "agent.automation.invocation"`

    Always `agent.automation.invocation`.

    - `"agent.automation.invocation"`

  - `scheduled_at: number | null`

    The intended occurrence as a Unix timestamp in seconds, or null for manual runs.

    `format: int64`

  - `session_id: string | null`

    The target or newly created session ID, or null before one is available.

    `minLength: 0`

  - `skip_reason: "pending_delivery" | null`

    Why an occurrence was skipped, or null when it was not skipped.

    - `"pending_delivery"`

  - `source: AutomationInvocationSource`

    Whether the invocation was manual or scheduled.

    - `AutomationInvocationSourceResourceManual`

      - `type: "manual"`

        The type of the object. Always `manual`.

        - `"manual"`

    - `AutomationInvocationSourceResourceAutomation`

      - `automation: Automation`

        The automation snapshot for this occurrence, excluding confidential values.

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

      - `type: "automation"`

        The type of the object. Always `automation`.

        - `"automation"`

  - `status: "queued" | "completed" | "failed" | "skipped"`

    Delivery status; completed does not mean the agent's work has finished.

    - `"queued"`

    - `"completed"`

    - `"failed"`

    - `"skipped"`

### Automation Invocation Source

- `AutomationInvocationSource = AutomationInvocationSourceResourceManual | AutomationInvocationSourceResourceAutomation`

  - `AutomationInvocationSourceResourceManual`

    - `type: "manual"`

      The type of the object. Always `manual`.

      - `"manual"`

  - `AutomationInvocationSourceResourceAutomation`

    - `automation: Automation`

      The automation snapshot for this occurrence, excluding confidential values.

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

    - `type: "automation"`

      The type of the object. Always `automation`.

      - `"automation"`
