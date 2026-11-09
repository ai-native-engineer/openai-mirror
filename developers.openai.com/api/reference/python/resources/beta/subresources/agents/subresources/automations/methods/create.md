<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/agents/subresources/automations/methods/create/ -->

## Create an automation

`beta.agents.automations.create(AutomationCreateParams**kwargs)  -> Automation`

**post** `/agents/automations`

Saves an active automation without invoking it immediately.

- `expression: str`

  A standard five-field cron expression defining scheduled occurrences.

  `minLength: 1`, `maxLength: 256`

- `name: str`

  A human-readable name for the automation.

  `minLength: 1`, `maxLength: 256`

- `target: AutomationTargetParam`

  The session an automation invocation targets.

  - `class AutomationTargetParamNewSession: …`

    Create a session for each invocation.

    - `environment: EnvironmentParam`

      The execution environment for each new session.

      - `class EnvironmentParamNone: …`

        Runs the agent without an execution environment.

        - `type: Literal["none"]`

          The type of the object. Always `none`.

          - `"none"`

      - `class EnvironmentParamOpenAIHosted: …`

        An existing OpenAI-hosted environment or new inline/template-based hosted configuration.

        - `type: Literal["openai_hosted"]`

          The type of the object. Always `openai_hosted`.

          - `"openai_hosted"`

        - `capability_directories: Optional[List[str]]`

          Directories that contain capabilities exposed to the agent. Defaults to an empty list.

          `minItems: 0`, `maxItems: 16384`

        - `container_size: Optional[Literal["small", "medium", "large"]]`

          The hosted container size. Omission selects the medium tier.

          - `"small"`

          - `"medium"`

          - `"large"`

        - `desktop: Optional[EnvironmentParamOpenAIHostedDesktop]`

          Desktop provisioning. Omission or null inherits the template setting, or defaults to disabled.

          - `enabled: bool`

            Whether to provision the desktop and its browser proxy.

        - `env: Optional[Dict[str, str]]`

          Environment variables made available to the agent.

        - `environment_id: Optional[str]`

          An existing prewarmed environment. Cannot be combined with a template or inline configuration.

          `minLength: 9`, `maxLength: 256`

        - `environment_template_id: Optional[str]`

          A reusable hosted template applied before inline session configuration. Omitted fields inherit the template; network overrides cannot broaden its policy.

          `minLength: 0`, `maxLength: 64`

        - `files: Optional[List[HostedEnvironmentFileParam]]`

          Files available before the agent starts. Defaults to an empty list.

          `minItems: 0`, `maxItems: 50`

          - `class HostedEnvironmentFileParamFileID: …`

            A file previously uploaded through the OpenAI Files API.

            - `file_id: str`

              The ID of the uploaded file.

              `minLength: 1`, `maxLength: 256`

            - `path: str`

              The absolute destination path inside `/workspace`.

              `minLength: 1`, `maxLength: 4096`

            - `type: Literal["file_id"]`

              The type of the object. Always `file_id`.

              - `"file_id"`

          - `class HostedEnvironmentFileParamInline: …`

            A file supplied directly as standard-base64 data.

            - `data: str`

              The standard-base64-encoded file contents.

              `minLength: 0`, `maxLength: 6990508`

            - `path: str`

              The absolute destination path inside `/workspace`.

              `minLength: 1`, `maxLength: 4096`

            - `type: Literal["inline"]`

              The type of the object. Always `inline`.

              - `"inline"`

        - `network: Optional[EnvironmentParamOpenAIHostedNetwork]`

          Network access policy for the environment. If omitted, the API version determines whether network access is enabled or disabled.

          - `access: Literal["enabled", "disabled", "restricted"]`

            The environment's network access mode.

            - `"enabled"`

              Allows unrestricted network access.

            - `"disabled"`

              Disables network access.

            - `"restricted"`

              Applies the configured domain restrictions.

          - `allowed_domains: Optional[List[str]]`

            Domains the environment may access when network access is restricted.

            `minItems: 0`, `maxItems: 16384`

          - `blocked_domains: Optional[List[str]]`

            Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

            `minItems: 0`, `maxItems: 100`

        - `packages: Optional[EnvironmentParamOpenAIHostedPackages]`

          Packages to install in the environment. Defaults to empty package lists.

          - `npm: Optional[List[str]]`

            npm packages to install globally. Defaults to an empty list.

            `minItems: 0`, `maxItems: 16384`

          - `python: Optional[List[str]]`

            Python packages to install. Defaults to an empty list.

            `minItems: 0`, `maxItems: 16384`

          - `system: Optional[List[str]]`

            System packages to install. Defaults to an empty list.

            `minItems: 0`, `maxItems: 16384`

        - `plugins: Optional[List[HostedPluginParam]]`

          Plugins provided as inline ZIP archives. Defaults to an empty list.

          `minItems: 0`, `maxItems: 32`

          - `description: str`

            The plugin description declared in `.codex-plugin/plugin.json`.

            `minLength: 0`, `maxLength: 1048576`

          - `name: str`

            The plugin name declared in `.codex-plugin/plugin.json`.

            `minLength: 1`, `maxLength: 64`

          - `source: InlineCapabilitySourceParam`

            Provides ZIP bytes encoded with standard base64.

            - `data: str`

              Standard-base64 encoded ZIP archive bytes.

              `minLength: 1`, `maxLength: 70254592`

            - `media_type: Literal["application/zip"]`

              The archive media type, always `application/zip`.

              - `"application/zip"`

            - `type: Literal["base64"]`

              The type of the object. Always `base64`.

              - `"base64"`

          - `type: Literal["inline"]`

            The type of the object. Always `inline`.

            - `"inline"`

        - `setup_commands: Optional[List[SetupCommandParam]]`

          Ordered, confidential setup commands. Command bodies are never returned.

          `minItems: 0`, `maxItems: 16`

          - `command: str`

            The shell command to execute.

            `minLength: 0`, `maxLength: 65536`

          - `cwd: Optional[str]`

            The absolute working directory. Defaults to `/workspace`.

            `minLength: 0`, `maxLength: 4096`

        - `skills: Optional[List[HostedSkillParam]]`

          Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

          `minItems: 0`, `maxItems: 200`

          - `class HostedSkillParamSkillReference: …`

            References a skill uploaded through the Skills API.

            - `skill_id: str`

              The ID of the skill created through `/v1/skills`.

              `minLength: 1`, `maxLength: 64`

            - `type: Literal["skill_reference"]`

              The type of the object. Always `skill_reference`.

              - `"skill_reference"`

            - `version: Optional[str]`

              The skill version, a positive integer or `latest`; omission selects the default.

              `minLength: 0`, `maxLength: 1048576`

          - `class HostedSkillParamInline: …`

            Supplies a skill ZIP directly in the session request.

            - `description: str`

              The skill description declared in `SKILL.md`.

              `minLength: 0`, `maxLength: 1048576`

            - `name: str`

              The skill name declared in `SKILL.md`.

              `minLength: 1`, `maxLength: 64`

            - `source: InlineCapabilitySourceParam`

              Provides ZIP bytes encoded with standard base64.

            - `type: Literal["inline"]`

              The type of the object. Always `inline`.

              - `"inline"`

      - `class EnvironmentParamSelfHosted: …`

        An application-hosted environment configured inline.

        - `type: Literal["self_hosted"]`

          The type of the object. Always `self_hosted`.

          - `"self_hosted"`

        - `workspace_directory: str`

          Absolute project directory inside the self-hosted environment.

          `minLength: 0`, `maxLength: 1048576`

        - `capability_directories: Optional[List[str]]`

          Directories that contain capabilities exposed to the agent. Defaults to an empty list.

          `minItems: 0`, `maxItems: 16384`

    - `input: List[AgentSessionInputMessageParam]`

      Initial user messages submitted with each new session.

      `minItems: 0`, `maxItems: 16384`

      - `content: List[InputContentParam]`

        The content of the message.

        `minItems: 0`, `maxItems: 16384`

        - `class InputContentParamInputText: …`

          Text input to the model.

          - `text: str`

            The text sent to the model.

            `minLength: 0`, `maxLength: 1048576`

          - `type: Literal["input_text"]`

            The type of the object. Always `input_text`.

            - `"input_text"`

        - `class InputContentParamInputImage: …`

          Image input to the model.

          - `image_url: str`

            The URL of the image sent to the model.

            `minLength: 0`, `maxLength: 1048576`

          - `type: Literal["input_image"]`

            The type of the object. Always `input_image`.

            - `"input_image"`

      - `role: Literal["user"]`

        The role of the message author. Always `user`.

        - `"user"`

      - `type: Optional[Literal["message"]]`

        The type of the input item. Always `message`.

        - `"message"`

    - `type: Literal["new_session"]`

      The type of the object. Always `new_session`.

      - `"new_session"`

    - `agent: Optional[AutomationTargetParamNewSessionAgent]`

      Inline agent configuration. Provide exactly one of agent and agent_id.

      - `compaction: Optional[AutomationTargetParamNewSessionAgentCompaction]`

        Context compaction settings. Omit to keep the current settings. A supplied object replaces the settings; null or an empty object enables background compaction.

        - `async_: Optional[bool]`

          Whether to compact context in the background. Omission or null defaults to true. Set to false to use blocking compaction. Background compaction may increase token usage.

      - `experimental: Optional[AutomationTargetParamNewSessionAgentExperimental]`

        Experimental settings to merge by key. Omitted settings keep their current values.

        - `time_awareness: Optional[bool]`

          Whether to give the model periodic current-time reminders. Omit to keep the current setting.

      - `instructions: Optional[str]`

        Additional instructions appended to the agent's default base instructions. Omit to leave unchanged.

        `minLength: 0`, `maxLength: 1048576`

      - `model: Optional[str]`

        The model to use for the agent. The requested model name is preserved.

        `minLength: 0`, `maxLength: 1048576`

      - `multi_agent: Optional[MultiAgentConfigParam]`

        Configuration for creating and coordinating subagents.

        - `enabled: bool`

          Whether subagent tools are enabled.

        - `max_concurrent_subagents: Optional[int]`

          Maximum number of subagents that may run concurrently. Defaults to 6.

          `format: int64`, `minimum: 1`, `maximum: 4294967295`

      - `reasoning: Optional[AgentReasoningParam]`

        Configuration for model reasoning. Omit to keep the current settings; pass `null` to reset to the model's default effort.

        - `effort: Optional[Literal["none", "minimal", "low", 4 more]]`

          The amount of reasoning effort the model should use. Omission lets the model select it.

          - `"none"`

          - `"minimal"`

          - `"low"`

          - `"medium"`

          - `"high"`

          - `"xhigh"`

          - `"max"`

        - `summary: Optional[Literal["concise", "detailed", "auto"]]`

          Controls whether the response includes a reasoning summary.

          - `"concise"`

            Returns a concise reasoning summary when supported.

          - `"detailed"`

            Returns a detailed reasoning summary when supported.

          - `"auto"`

            Automatically selects the most detailed summary supported by the model.

      - `service_tier: Optional[Literal["auto", "default", "flex", 3 more]]`

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

      - `text: Optional[AgentTextParam]`

        Configuration for text generated by the agent.

        - `format: Optional[TextFormatParam]`

          The output format. Omission uses ordinary text (`{"type": "text"}`).

          - `class TextFormatParamText: …`

            Generates ordinary text without a structured-output constraint.

            - `type: Literal["text"]`

              The type of the object. Always `text`.

              - `"text"`

          - `class TextFormatParamJSONSchema: …`

            Constrains generated text to a JSON Schema.

            - `schema: Dict[str, object]`

              The JSON Schema that generated text must match.

            - `type: Literal["json_schema"]`

              The type of the object. Always `json_schema`.

              - `"json_schema"`

        - `verbosity: Optional[Literal["low", "medium", "high"]]`

          The amount of text the model should produce. Defaults to `medium`, matching Responses.

          - `"low"`

            Produces less text.

          - `"medium"`

            Uses the default amount of text.

          - `"high"`

            Produces more text.

      - `tools: Optional[List[AgentToolParam]]`

        Tools available to the agent. Omit to inherit, or pass null to clear them. The resolved tool list must fit within 3 MiB (3,145,728 bytes) of compact UTF-8 JSON.

        `minItems: 0`, `maxItems: 16384`

        - `class AgentToolConfigParamFunction: …`

          A function defined by the application.

          - `description: str`

            A description of what the function does.

            `minLength: 0`, `maxLength: 1048576`

          - `name: str`

            The name of the function.

            `minLength: 0`, `maxLength: 1048576`

          - `parameters: Dict[str, object]`

            A JSON Schema object describing the function's arguments.

          - `type: Literal["function"]`

            The type of the object. Always `function`.

            - `"function"`

          - `async_: Optional[bool]`

            Whether the agent continues without waiting for the function result. Defaults to `false`.

          - `defer_loading: Optional[bool]`

            Whether this function is deferred and discovered through tool search. Defaults to `false`.

        - `class AgentToolConfigParamToolSearch: …`

          Discovers deferred function tools and loads them into the model context.

          - `type: Literal["tool_search"]`

            The type of the object. Always `tool_search`.

            - `"tool_search"`

        - `class AgentToolConfigParamProgrammaticToolCalling: …`

          Enables calling tools from model-generated code.

          - `type: Literal["programmatic_tool_calling"]`

            The type of the object. Always `programmatic_tool_calling`.

            - `"programmatic_tool_calling"`

          - `enabled: Optional[bool]`

            Whether tools can be called from model-generated code. Defaults to `true`.

        - `class AgentToolConfigParamMcp: …`

          Tools provided by a remote MCP server.

          - `server_label: str`

            A label used to identify the MCP server in tool calls.

            `minLength: 0`, `maxLength: 1048576`

          - `transport: McpTransportParam`

            The transport used to connect to the MCP server.

            - `class McpTransportConfigParamHTTP: …`

              Connects to an MCP server over HTTP.

              - `server_url: str`

                The URL of the MCP server.

                `minLength: 0`, `maxLength: 1048576`

              - `type: Literal["http"]`

                The type of the object. Always `http`.

                - `"http"`

              - `authorization: Optional[str]`

                The authorization value sent to the MCP server, if any.

                `minLength: 0`, `maxLength: 1048576`

              - `headers: Optional[Dict[str, str]]`

                Additional HTTP headers sent to the MCP server.

            - `class McpTransportConfigParamStdio: …`

              Starts an MCP server as a local process.

              - `command: str`

                The command used to start the MCP server.

                `minLength: 0`, `maxLength: 1048576`

              - `cwd: str`

                The working directory used to start the MCP server.

                `minLength: 0`, `maxLength: 1048576`

              - `type: Literal["stdio"]`

                The type of the object. Always `stdio`.

                - `"stdio"`

              - `args: Optional[List[str]]`

                Arguments passed to the MCP server command.

                `minItems: 0`, `maxItems: 16384`

              - `env: Optional[Dict[str, str]]`

                Environment variables set for the MCP server process.

              - `env_vars: Optional[List[str]]`

                Environment variable names to inherit from the selected execution environment.

                `minItems: 0`, `maxItems: 16384`

          - `type: Literal["mcp"]`

            The type of the object. Always `mcp`.

            - `"mcp"`

          - `allowed_tools: Optional[List[str]]`

            The MCP tools the agent may call. All server tools are allowed when omitted.

            `minItems: 0`, `maxItems: 16384`

          - `connection_origin: Optional[Literal["service", "environment"]]`

            Selects where outbound MCP HTTP connections originate. Omitted or `service` uses the Managed Agents service network; `environment` uses the session's selected environment.

            - `"service"`

              Uses the Managed Agents service network.

            - `"environment"`

              Uses the session's execution environment.

          - `credential_id: Optional[str]`

            The attached vault credential used to authenticate this MCP server. Optional when exactly one attached credential matches the server URL.

            `minLength: 0`, `maxLength: 1048576`

          - `request_metadata: Optional[Dict[str, object]]`

            Metadata included with requests to this MCP server.

          - `required: Optional[bool]`

            Whether this MCP server must initialize before the first turn. Defaults to `false`.

        - `class AgentToolConfigParamWebSearch: …`

          Web search.

          - `type: Literal["web_search"]`

            The type of the object. Always `web_search`.

            - `"web_search"`

          - `allowed_domains: Optional[List[str]]`

            Domains the search may include.

            `minItems: 0`, `maxItems: 16384`

          - `context_size: Optional[Literal["low", "medium", "high"]]`

            The amount of search context made available to the model. Defaults to `medium`.

            - `"low"`

            - `"medium"`

            - `"high"`

          - `location: Optional[AgentToolConfigParamWebSearchLocation]`

            Approximate location used to localize search results.

            - `city: Optional[str]`

              The city name.

              `minLength: 0`, `maxLength: 1048576`

            - `country: Optional[str]`

              The two-letter ISO country code, such as `US`.

              `minLength: 0`, `maxLength: 1048576`

            - `region: Optional[str]`

              The region or state name.

              `minLength: 0`, `maxLength: 1048576`

            - `timezone: Optional[str]`

              The IANA timezone, such as `America/Los_Angeles`.

              `minLength: 0`, `maxLength: 1048576`

          - `mode: Optional[Literal["disabled", "cached", "live"]]`

            The source used for web search results. Defaults to `live`.

            - `"disabled"`

              Disables web search.

            - `"cached"`

              Uses cached search results.

            - `"live"`

              Searches the live web.

        - `class AgentToolConfigParamComputerUse: …`

          Browser use in an OpenAI-hosted session.

          - `type: Literal["computer_use"]`

            The type of the object. Always `computer_use`.

            - `"computer_use"`

          - `include_screenshots: Optional[bool]`

            Whether computer tool outputs include screenshots. Defaults to `false`.

        - `class AgentToolConfigParamAutomations: …`

          Lets the agent manage its own scheduled wakeups.

          - `type: Literal["automations"]`

            The type of the object. Always `automations`.

            - `"automations"`

    - `agent_id: Optional[str]`

      A saved agent ID. Provide exactly one of agent and agent_id.

      `minLength: 0`, `maxLength: 64`

    - `metadata: Optional[Dict[str, str]]`

      Metadata attached to each new session.

    - `vault_ids: Optional[List[str]]`

      The IDs of vaults made available to each new session.

      `minItems: 0`, `maxItems: 16384`

  - `class AutomationTargetParamExistingSession: …`

    Deliver instructions to an existing session.

    - `instructions: str`

      Instructions delivered as an automation notification.

      `minLength: 0`, `maxLength: 1048576`

    - `session_id: str`

      The session receiving each invocation.

      `minLength: 0`, `maxLength: 1048576`

    - `type: Literal["existing_session"]`

      The type of the object. Always `existing_session`.

      - `"existing_session"`

- `timezone: str`

  The IANA timezone used to interpret the cron expression.

  `minLength: 1`, `maxLength: 128`

- `type: Literal["periodic"]`

  The type of the object. Always `periodic`.

  - `"periodic"`

- `metadata: Optional[AutomationMetadataParam]`

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
automation = client.beta.agents.automations.create(
    expression="x",
    name="x",
    target={
        "environment": {
            "type": "none"
        "input": [{
            "content": [{
                "text": "text",
                "type": "input_text",
            }],
            "role": "user",
        }],
        "type": "new_session",
    timezone="x",
    type="periodic",
print(automation)

#### 201 — Example

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
