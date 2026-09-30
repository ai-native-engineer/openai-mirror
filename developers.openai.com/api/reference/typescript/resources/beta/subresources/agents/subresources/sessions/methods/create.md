<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/agents/subresources/sessions/methods/create/ -->

## Create an agent session

`client.beta.agents.sessions.create(SessionCreateParamsbody, RequestOptionsoptions?): AgentSession | Stream<AgentSessionEvent>`

**post** `/agents/sessions`

Creates a managed agent session, optionally submits initial input, and returns the session or streams its events when stream is true. See [running sessions](/api/docs/guides/agents-api/sessions).

- `SessionCreateParams = SessionCreateParamsNonStreaming | SessionCreateParamsStreaming`

  - `SessionCreateParamsBase`

    - `environment: EnvironmentParam`

      An inline execution environment or a reference to an environment template.

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

        - `environment_template_id?: string`

          A reusable hosted template applied before inline session configuration. Omitted fields inherit the template; network overrides cannot broaden its policy.

        - `files?: Array<HostedEnvironmentFileParam> | null`

          Files available before the agent starts. Defaults to an empty list.

          - `HostedEnvironmentFileParamFileID`

            A file previously uploaded through the OpenAI Files API.

            - `file_id: string`

              The ID of the uploaded file.

            - `path: string`

              The absolute destination path inside `/workspace`.

            - `type: "file_id"`

              The type of the object. Always `file_id`.

              - `"file_id"`

          - `HostedEnvironmentFileParamInline`

            A file supplied directly as standard-base64 data.

            - `data: string`

              The standard-base64-encoded file contents.

            - `path: string`

              The absolute destination path inside `/workspace`.

            - `type: "inline"`

              The type of the object. Always `inline`.

              - `"inline"`

        - `network?: Network | null`

          Network access policy for the environment. Defaults to disabled for GA requests and enabled for beta requests.

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

          - `blocked_domains?: Array<string> | null`

            Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

        - `packages?: Packages | null`

          Packages to install in the environment. Defaults to empty package lists.

          - `npm?: Array<string> | null`

            npm packages to install globally. Defaults to an empty list.

          - `python?: Array<string> | null`

            Python packages to install. Defaults to an empty list.

          - `system?: Array<string> | null`

            System packages to install. Defaults to an empty list.

        - `plugins?: Array<HostedPluginParam> | null`

          Plugins provided as inline ZIP archives. Defaults to an empty list.

          - `description: string`

            The plugin description declared in `.codex-plugin/plugin.json`.

          - `name: string`

            The plugin name declared in `.codex-plugin/plugin.json`.

          - `source: InlineCapabilitySourceParam`

            Provides ZIP bytes encoded with standard base64.

            - `data: string`

              Standard-base64 encoded ZIP archive bytes.

            - `media_type: "application/zip"`

              The archive media type, always `application/zip`.

              - `"application/zip"`

                A ZIP archive.

            - `type: "base64"`

              The type of the object. Always `base64`.

              - `"base64"`

          - `type: "inline"`

            The type of the object. Always `inline`.

            - `"inline"`

        - `setup_commands?: Array<SetupCommandParam> | null`

          Ordered, confidential setup commands. Command bodies are never returned.

          - `command: string`

            The shell command to execute.

          - `cwd?: string | null`

            The absolute working directory. Defaults to `/workspace`.

        - `skills?: Array<HostedSkillParam> | null`

          Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

          - `HostedSkillParamSkillReference`

            References a skill uploaded through the Skills API.

            - `skill_id: string`

              The ID of the skill created through `/v1/skills`.

            - `type: "skill_reference"`

              The type of the object. Always `skill_reference`.

              - `"skill_reference"`

            - `version?: string | null`

              The skill version, a positive integer or `latest`; omission selects the default.

          - `HostedSkillParamInline`

            Supplies a skill ZIP directly in the session request.

            - `description: string`

              The skill description declared in `SKILL.md`.

            - `name: string`

              The skill name declared in `SKILL.md`.

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

        - `capability_directories?: Array<string> | null`

          Directories that contain capabilities exposed to the agent. Defaults to an empty list.

    - `agent?: Agent`

      Agent configuration. With `agent_id`, supplied fields override the saved agent for this session. Without `agent_id`, `model` is required.

      - `instructions?: string | null`

        Additional instructions appended to the agent's default base instructions. Omit to leave unchanged.

      - `model?: string`

        The model to use for the agent. The requested model name is preserved.

      - `multi_agent?: MultiAgentConfigParam | null`

        Configuration for creating and coordinating subagents.

        - `enabled: boolean`

          Whether subagent tools are enabled.

        - `max_concurrent_subagents?: number`

          Maximum number of subagents that may run concurrently. Defaults to 6.

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

        - `auto` - Selects the service tier automatically.
        - `default` - Uses the default service tier.
        - `flex` - Uses the flex service tier.
        - `priority` - Uses the priority service tier.
        - `fast` - Uses the fast service tier.
        - `ultrafast` - Uses the ultrafast service tier.

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

        Tools available to the agent. Omit to inherit, or pass null to clear them.

        - `AgentToolConfigParamFunction`

          A function defined by the application.

          - `description: string`

            A description of what the function does.

          - `name: string`

            The name of the function.

          - `parameters: Record<string, unknown>`

            A JSON Schema object describing the function's arguments.

          - `type: "function"`

            The type of the object. Always `function`.

            - `"function"`

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

          - `transport: McpTransportParam`

            The transport used to connect to the MCP server.

            - `McpTransportConfigParamHTTP`

              Connects to an MCP server over HTTP.

              - `server_url: string`

                The URL of the MCP server.

              - `type: "http"`

                The type of the object. Always `http`.

                - `"http"`

              - `authorization?: string | null`

                The authorization value sent to the MCP server, if any.

              - `headers?: Record<string, string> | null`

                Additional HTTP headers sent to the MCP server.

            - `McpTransportConfigParamStdio`

              Starts an MCP server as a local process.

              - `command: string`

                The command used to start the MCP server.

              - `cwd: string`

                The working directory used to start the MCP server.

              - `type: "stdio"`

                The type of the object. Always `stdio`.

                - `"stdio"`

              - `args?: Array<string> | null`

                Arguments passed to the MCP server command.

              - `env?: Record<string, string> | null`

                Environment variables set for the MCP server process.

              - `env_vars?: Array<string> | null`

                Environment variable names to inherit from the selected execution environment.

          - `type: "mcp"`

            The type of the object. Always `mcp`.

            - `"mcp"`

          - `allowed_tools?: Array<string> | null`

            The MCP tools the agent may call. All server tools are allowed when omitted.

          - `connection_origin?: "service" | "environment" | null`

            Selects where outbound MCP HTTP connections originate. Omitted or `service` uses the Managed Agents service network; `environment` uses the session's selected environment.

            - `"service"`

              Uses the Managed Agents service network.

            - `"environment"`

              Uses the session's execution environment.

          - `credential_id?: string | null`

            The attached vault credential used to authenticate this MCP server. Optional when exactly one attached credential matches the server URL.

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

          - `context_size?: "low" | "medium" | "high" | null`

            The amount of search context made available to the model. Defaults to `medium`.

            - `"low"`

            - `"medium"`

            - `"high"`

          - `location?: Location | null`

            Approximate location used to localize search results.

            - `city?: string | null`

              The city name.

            - `country?: string | null`

              The two-letter ISO country code, such as `US`.

            - `region?: string | null`

              The region or state name.

            - `timezone?: string | null`

              The IANA timezone, such as `America/Los_Angeles`.

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

    - `agent_id?: string`

      The ID of a saved reusable agent. Omit `agent` to use its configuration unchanged.

    - `input?: string | Array<AgentSessionInputMessageParam> | null`

      Initial input to submit when the session is created. A string is shorthand for a single user message. Required when `environment.type` is `none`, or when `stream` is `true` for an environment that is not `self_hosted`; optional for self-hosted and non-streaming execution environments.

      - `string`

      - `Array<AgentSessionInputMessageParam>`

        - `content: Array<InputContentParam>`

          The content of the message.

          - `InputContentParamInputText`

            Text input to the model.

            - `text: string`

              The text sent to the model.

            - `type: "input_text"`

              The type of the object. Always `input_text`.

              - `"input_text"`

          - `InputContentParamInputImage`

            Image input to the model.

            - `image_url: string`

              The URL of the image sent to the model.

            - `type: "input_image"`

              The type of the object. Always `input_image`.

              - `"input_image"`

        - `role: "user"`

          The role of the message author. Always `user`.

          - `"user"`

        - `type?: "message"`

          The type of the input item. Always `message`.

          - `"message"`

    - `metadata?: Record<string, string> | null`

      Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters. Omission or null defaults to an empty map.

    - `stream?: false`

      Whether to stream session events as server-sent events. Defaults to `false`.

      - `false`

    - `vault_ids?: Array<string> | null`

      The IDs of vaults made available to the session.

  - `SessionCreateParamsNonStreaming extends SessionCreateParamsBase`

    - `stream?: false`

      Whether to stream session events as server-sent events. Defaults to `false`.

  - `SessionCreateParamsStreaming extends SessionCreateParamsBase`

    - `stream: true`

      Whether to stream session events as server-sent events. Defaults to `false`.

      - `true`

- `AgentSession`

  A Managed Agents session.

  - `id: string`

    The ID of the session.

  - `agent: Agent`

    The agent running in the session.

    - `id: string`

      The ID of the agent.

    - `instructions: string | null`

      Custom instructions appended to the agent's default base instructions.

    - `model: string`

      The model used by the agent.

    - `multi_agent: MultiAgentConfig`

      Configuration for creating and coordinating subagents.

      - `enabled: boolean`

        Whether subagent tools are enabled. Defaults to false.

      - `max_concurrent_subagents: number | null`

        Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

    - `name: string | null`

      The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

    - `reasoning: AgentReasoning`

      The agent's reasoning configuration.

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

      The effective service-tier policy for model requests. Defaults to `auto`.

      - `"auto"`

      - `"default"`

      - `"flex"`

      - `"priority"`

      - `"fast"`

      - `"ultrafast"`

    - `text: AgentText`

      Configuration for text generated by the agent.

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

      Tools available to the agent.

      - `AgentToolResourceFunction`

        A function defined by the application.

        - `defer_loading: boolean`

          Whether the function is deferred and discovered through tool search.

        - `description: string`

          A description of what the function does.

        - `name: string`

          The name of the function.

        - `parameters: Record<string, unknown>`

          A JSON Schema object describing the function's arguments.

        - `type: "function"`

          The type of the object. Always `function`.

          - `"function"`

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

        - `connection_origin: "service" | "environment"`

          Where outbound MCP HTTP connections originate.

          - `"service"`

          - `"environment"`

        - `credential_id: string | null`

          The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

        - `request_metadata: Record<string, unknown>`

          Metadata included with requests to this MCP server.

        - `required: boolean`

          Whether this MCP server must initialize before the first turn.

        - `server_label: string`

          A label used to identify the MCP server in tool calls.

        - `transport: McpTransport`

          The transport used to connect to the MCP server.

          - `McpTransportResourceHTTP`

            Connects to an MCP server over HTTP.

            - `server_url: string`

              The URL of the MCP server.

            - `type: "http"`

              The type of the object. Always `http`.

              - `"http"`

          - `McpTransportResourceStdio`

            Starts an MCP server as a local process.

            - `args: Array<string>`

              Arguments passed to the MCP server command.

            - `command: string`

              The command used to start the MCP server.

            - `cwd: string`

              The working directory used to start the MCP server.

            - `env_vars: Array<string>`

              Environment variable names inherited from the execution environment.

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

        - `context_size: "low" | "medium" | "high"`

          The amount of search context made available to the model. Defaults to `medium`.

          - `"low"`

          - `"medium"`

          - `"high"`

        - `location: Location | null`

          Approximate location used to localize search results, if provided.

          - `city: string | null`

            The city name.

          - `country: string | null`

            The two-letter ISO country code, such as `US`.

          - `region: string | null`

            The region or state name.

          - `timezone: string | null`

            The IANA timezone, such as `America/Los_Angeles`.

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

  - `created_at: number`

    The Unix timestamp, in seconds, when the session was created.

  - `environment: Environment`

    The execution environment for the session.

    - `EnvironmentResourceNone`

      The session talks to CCA without selecting or provisioning an execution environment.

      - `type: "none"`

        The type of the object. Always `none`.

        - `"none"`

    - `EnvironmentResourceOpenAIHosted`

      An environment hosted by OpenAI.

      - `id: string`

        The public ID of the environment.

      - `capability_directories: Array<string>`

        Directories that contain capabilities exposed to the agent.

      - `desktop: Desktop`

        The effective desktop configuration.

        - `enabled: boolean`

          Whether the environment provisions a desktop and browser proxy.

      - `files: Array<HostedEnvironmentFile>`

        Files available in the environment, excluding their contents.

        - `HostedEnvironmentFileID`

          A file copied from the OpenAI Files API.

          - `id: string`

            The session-scoped ID of the file in the execution environment.

          - `file_id: string`

            The ID of the uploaded file.

          - `path: string`

            The file's absolute path inside the environment.

          - `size_bytes: number`

            The decoded file size in bytes.

          - `type: "file_id"`

            The type of the object. Always `file_id`.

            - `"file_id"`

        - `HostedEnvironmentFileResourceInline`

          A file supplied inline when the session was created.

          - `id: string`

            The session-scoped ID of the file in the execution environment.

          - `path: string`

            The file's absolute path inside the environment.

          - `size_bytes: number`

            The decoded file size in bytes.

          - `type: "inline"`

            The type of the object. Always `inline`.

            - `"inline"`

      - `network: Network`

        The effective network access policy for the environment.

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

      - `packages: Packages`

        Packages installed in the environment.

        - `npm: Array<string>`

          npm packages installed globally in the environment.

        - `python: Array<string>`

          Python packages installed in the environment.

        - `system: Array<string>`

          System packages installed in the environment.

      - `plugins: Array<HostedPlugin>`

        Plugins installed in the environment, excluding their archive contents.

        - `description: string`

          The installed plugin description.

        - `name: string`

          The installed plugin name.

        - `type: "inline"`

          The type of the object. Always `inline`.

          - `"inline"`

      - `skills: Array<HostedSkill>`

        Skills installed in the environment, excluding their archive contents.

        - `HostedSkillReference`

          A skill installed from the Skills API.

          - `description: string`

            The installed skill description.

          - `name: string`

            The installed skill name.

          - `skill_id: string`

            The referenced skill ID.

          - `type: "skill_reference"`

            The type of the object. Always `skill_reference`.

            - `"skill_reference"`

          - `version: string`

            The concrete skill version installed for this session.

        - `HostedSkillResourceInline`

          A skill installed from an inline ZIP archive.

          - `description: string`

            The installed skill description.

          - `name: string`

            The installed skill name.

          - `type: "inline"`

            The type of the object. Always `inline`.

            - `"inline"`

      - `type: "openai_hosted"`

        The type of the object. Always `openai_hosted`.

        - `"openai_hosted"`

      - `container_size?: "small" | "medium" | "large" | null`

        The effective CPU and memory tier, or null when unknown or outside the public tiers.

        - `"small"`

        - `"medium"`

        - `"large"`

    - `EnvironmentResourceSelfHosted`

      An environment hosted by the application.

      - `id: string`

        The public ID of the environment.

      - `capability_directories: Array<string>`

        Directories that contain capabilities exposed to the agent.

      - `remote_url: string`

        Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

      - `type: "self_hosted"`

        The type of the object. Always `self_hosted`.

        - `"self_hosted"`

      - `workspace_directory: string`

        The absolute project directory inside the environment. Defaults to `/workspace`.

  - `error: string | null`

    The error that caused the session to fail, if any.

  - `last_active_at: number`

    The Unix timestamp, in seconds, when the session was last active.

  - `metadata: Record<string, string>`

    Custom string key-value pairs attached to the session.

  - `object: "agent.session"`

    The object type. Always `agent.session`.

    - `"agent.session"`

  - `required_actions: Array<SessionRequiredActionResourceComputerUseApprovalRequest | SessionRequiredActionResourceFunctionCall | SessionRequiredActionResourceEnvironmentConnection>`

    Actions that must be completed before the session can continue.

    - `SessionRequiredActionResourceComputerUseApprovalRequest`

      Respond to a computer-use request.

      - `request: ComputerUseApprovalRequestKindResourceBrowserAuthentication | ComputerUseApprovalRequestKindResourceBrowserOriginAccess`

        The information needed to render the request.

        - `ComputerUseApprovalRequestKindResourceBrowserAuthentication`

          A registered form awaiting the application's response.

          - `credential_origin: string | null`

            The registered form or frame origin where values will be entered.

          - `fields: Array<Field>`

            Controls to render. All submitted values are sensitive.

            - `id: string`

              The field ID to submit as field_id in a fields entry.

            - `label: string`

              The label to display beside the control.

            - `required: boolean`

              Whether this control requires a nonempty value.

            - `type: string`

              The rendering type, such as email, password, or text.

          - `options: Array<Option>`

            Sign-in methods. Empty for a plain form.

            - `id: string`

              The option ID to submit as selected_option.

            - `field_ids: Array<string>`

              IDs from the registered fields that this method accepts.

            - `label: string`

              The method label to display.

          - `reason: string | null`

            Why the agent needs the user to sign in.

          - `type: "browser_authentication"`

            The type of the object. Always `browser_authentication`.

            - `"browser_authentication"`

        - `ComputerUseApprovalRequestKindResourceBrowserOriginAccess`

          A browser origin awaiting the application's approval decision.

          - `origin: string`

            The origin the browser needs permission to access.

          - `reason: string | null`

            The browser's explanation for this request, or null when unavailable.

          - `type: "browser_origin_access"`

            The type of the object. Always `browser_origin_access`.

            - `"browser_origin_access"`

      - `request_id: string`

        The registered request ID to echo when responding.

      - `turn_id: string`

        The turn that requested approval.

      - `type: "computer_use_approval_request"`

        The type of the object. Always `computer_use_approval_request`.

        - `"computer_use_approval_request"`

    - `SessionRequiredActionResourceFunctionCall`

      Run a function tool and submit its result.

      - `arguments: unknown`

        The arguments supplied by the model.

      - `call_id: string`

        The ID to include when submitting the function result.

      - `name: string`

        The function name.

      - `turn_id: string`

        The ID of the turn that requested the function call.

      - `type: "function_call"`

        The type of the object. Always `function_call`.

        - `"function_call"`

    - `SessionRequiredActionResourceEnvironmentConnection`

      Reconnect a session environment.

      - `environment_id: string`

        The ID of the environment to reconnect.

      - `type: "environment_connection"`

        The type of the object. Always `environment_connection`.

        - `"environment_connection"`

  - `status: "idle" | "in_progress" | "requires_action" | "failed"`

    The current status of the session.

    - `"idle"`

      The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

    - `"in_progress"`

      The session is processing a turn.

    - `"requires_action"`

      The session is waiting for one or more required actions.

    - `"failed"`

      The session failed.

  - `usage: TokenUsage | null`

    Best-effort token usage for the session, or null if unknown. Recorded usage may change.

    - `input_tokens: number`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails`

      A breakdown of the agent's input token usage.

      - `cached_tokens: number`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: number`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: number`

        The number of output tokens used for reasoning.

    - `total_tokens: number`

      The total number of input and output tokens used by the agent.

  - `vault_ids: Array<string>`

    The IDs of vaults made available to the session.

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const agentSession = await client.beta.agents.sessions.create({ environment: { type: 'none' } });

console.log(agentSession.id);

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
        "description": "description",
        "parameters": {
          "foo": "bar"
        "type": "function"
    ]
  "environment": {
    "type": "none"
  "error": "error",
  "last_active_at": 0,
  "metadata": {
    "foo": "string"
  "object": "agent.session",
  "required_actions": [
      "request": {
        "credential_origin": "credential_origin",
        "fields": [
            "label": "label",
            "required": true,
            "type": "type"
        "options": [
            "field_ids": [
              "string"
            "label": "label"
        "reason": "reason",
        "type": "browser_authentication"
      "request_id": "request_id",
      "turn_id": "turn_id",
      "type": "computer_use_approval_request"
  "status": "idle",
  "usage": {
    "input_tokens": 0,
    "input_tokens_details": {
      "cached_tokens": 0
    "output_tokens": 0,
    "output_tokens_details": {
      "reasoning_tokens": 0
    "total_tokens": 0
  "vault_ids": [
    "string"
  ]
