<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/agents/subresources/sessions/methods/create/ -->

## Create an agent session

`beta.agents.sessions.create(SessionCreateParams**kwargs)  -> AgentSession`

**post** `/agents/sessions`

Creates a managed agent session, optionally submits initial input, and returns the session or streams its events when stream is true. See [running sessions](/api/docs/guides/agents-api/sessions).

- `environment: EnvironmentParam`

  An inline execution environment or a reference to an environment template.

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

    - `environment_template_id: Optional[str]`

      A reusable hosted template applied before inline session configuration. Omitted fields inherit the template; network overrides cannot broaden its policy.

    - `files: Optional[List[HostedEnvironmentFileParam]]`

      Files available before the agent starts. Defaults to an empty list.

      - `class HostedEnvironmentFileParamFileID: …`

        A file previously uploaded through the OpenAI Files API.

        - `file_id: str`

          The ID of the uploaded file.

        - `path: str`

          The absolute destination path inside `/workspace`.

        - `type: Literal["file_id"]`

          The type of the object. Always `file_id`.

          - `"file_id"`

      - `class HostedEnvironmentFileParamInline: …`

        A file supplied directly as standard-base64 data.

        - `data: str`

          The standard-base64-encoded file contents.

        - `path: str`

          The absolute destination path inside `/workspace`.

        - `type: Literal["inline"]`

          The type of the object. Always `inline`.

          - `"inline"`

    - `network: Optional[EnvironmentParamOpenAIHostedNetwork]`

      Network access policy for the environment. Defaults to disabled for GA requests and enabled for beta requests.

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

      - `blocked_domains: Optional[List[str]]`

        Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

    - `packages: Optional[EnvironmentParamOpenAIHostedPackages]`

      Packages to install in the environment. Defaults to empty package lists.

      - `npm: Optional[List[str]]`

        npm packages to install globally. Defaults to an empty list.

      - `python: Optional[List[str]]`

        Python packages to install. Defaults to an empty list.

      - `system: Optional[List[str]]`

        System packages to install. Defaults to an empty list.

    - `plugins: Optional[List[HostedPluginParam]]`

      Plugins provided as inline ZIP archives. Defaults to an empty list.

      - `description: str`

        The plugin description declared in `.codex-plugin/plugin.json`.

      - `name: str`

        The plugin name declared in `.codex-plugin/plugin.json`.

      - `source: InlineCapabilitySourceParam`

        Provides ZIP bytes encoded with standard base64.

        - `data: str`

          Standard-base64 encoded ZIP archive bytes.

        - `media_type: Literal["application/zip"]`

          The archive media type, always `application/zip`.

          - `"application/zip"`

            A ZIP archive.

        - `type: Literal["base64"]`

          The type of the object. Always `base64`.

          - `"base64"`

      - `type: Literal["inline"]`

        The type of the object. Always `inline`.

        - `"inline"`

    - `setup_commands: Optional[List[SetupCommandParam]]`

      Ordered, confidential setup commands. Command bodies are never returned.

      - `command: str`

        The shell command to execute.

      - `cwd: Optional[str]`

        The absolute working directory. Defaults to `/workspace`.

    - `skills: Optional[List[HostedSkillParam]]`

      Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

      - `class HostedSkillParamSkillReference: …`

        References a skill uploaded through the Skills API.

        - `skill_id: str`

          The ID of the skill created through `/v1/skills`.

        - `type: Literal["skill_reference"]`

          The type of the object. Always `skill_reference`.

          - `"skill_reference"`

        - `version: Optional[str]`

          The skill version, a positive integer or `latest`; omission selects the default.

      - `class HostedSkillParamInline: …`

        Supplies a skill ZIP directly in the session request.

        - `description: str`

          The skill description declared in `SKILL.md`.

        - `name: str`

          The skill name declared in `SKILL.md`.

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

    - `capability_directories: Optional[List[str]]`

      Directories that contain capabilities exposed to the agent. Defaults to an empty list.

- `agent: Optional[Agent]`

  Agent configuration. With `agent_id`, supplied fields override the saved agent for this session. Without `agent_id`, `model` is required.

  - `instructions: Optional[str]`

    Additional instructions appended to the agent's default base instructions. Omit to leave unchanged.

  - `model: Optional[str]`

    The model to use for the agent. The requested model name is preserved.

  - `multi_agent: Optional[MultiAgentConfigParam]`

    Configuration for creating and coordinating subagents.

    - `enabled: bool`

      Whether subagent tools are enabled.

    - `max_concurrent_subagents: Optional[int]`

      Maximum number of subagents that may run concurrently. Defaults to 6.

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

  - `tools: Optional[Iterable[AgentToolParam]]`

    Tools available to the agent. Omit to inherit, or pass null to clear them.

    - `class AgentToolConfigParamFunction: …`

      A function defined by the application.

      - `description: str`

        A description of what the function does.

      - `name: str`

        The name of the function.

      - `parameters: Dict[str, object]`

        A JSON Schema object describing the function's arguments.

      - `type: Literal["function"]`

        The type of the object. Always `function`.

        - `"function"`

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

      - `transport: McpTransportParam`

        The transport used to connect to the MCP server.

        - `class McpTransportConfigParamHTTP: …`

          Connects to an MCP server over HTTP.

          - `server_url: str`

            The URL of the MCP server.

          - `type: Literal["http"]`

            The type of the object. Always `http`.

            - `"http"`

          - `authorization: Optional[str]`

            The authorization value sent to the MCP server, if any.

          - `headers: Optional[Dict[str, str]]`

            Additional HTTP headers sent to the MCP server.

        - `class McpTransportConfigParamStdio: …`

          Starts an MCP server as a local process.

          - `command: str`

            The command used to start the MCP server.

          - `cwd: str`

            The working directory used to start the MCP server.

          - `type: Literal["stdio"]`

            The type of the object. Always `stdio`.

            - `"stdio"`

          - `args: Optional[List[str]]`

            Arguments passed to the MCP server command.

          - `env: Optional[Dict[str, str]]`

            Environment variables set for the MCP server process.

          - `env_vars: Optional[List[str]]`

            Environment variable names to inherit from the selected execution environment.

      - `type: Literal["mcp"]`

        The type of the object. Always `mcp`.

        - `"mcp"`

      - `allowed_tools: Optional[List[str]]`

        The MCP tools the agent may call. All server tools are allowed when omitted.

      - `connection_origin: Optional[Literal["service", "environment"]]`

        Selects where outbound MCP HTTP connections originate. Omitted or `service` uses the Managed Agents service network; `environment` uses the session's selected environment.

        - `"service"`

          Uses the Managed Agents service network.

        - `"environment"`

          Uses the session's execution environment.

      - `credential_id: Optional[str]`

        The attached vault credential used to authenticate this MCP server. Optional when exactly one attached credential matches the server URL.

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

      - `context_size: Optional[Literal["low", "medium", "high"]]`

        The amount of search context made available to the model. Defaults to `medium`.

        - `"low"`

        - `"medium"`

        - `"high"`

      - `location: Optional[AgentToolConfigParamWebSearchLocation]`

        Approximate location used to localize search results.

        - `city: Optional[str]`

          The city name.

        - `country: Optional[str]`

          The two-letter ISO country code, such as `US`.

        - `region: Optional[str]`

          The region or state name.

        - `timezone: Optional[str]`

          The IANA timezone, such as `America/Los_Angeles`.

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

- `agent_id: Optional[str]`

  The ID of a saved reusable agent. Omit `agent` to use its configuration unchanged.

- `input: Optional[Union[str, Iterable[AgentSessionInputMessageParam], null]]`

  Initial input to submit when the session is created. A string is shorthand for a single user message. Required when `environment.type` is `none`, or when `stream` is `true` for an environment that is not `self_hosted`; optional for self-hosted and non-streaming execution environments.

  - `str`

  - `Iterable[AgentSessionInputMessageParam]`

    - `content: List[InputContentParam]`

      The content of the message.

      - `class InputContentParamInputText: …`

        Text input to the model.

        - `text: str`

          The text sent to the model.

        - `type: Literal["input_text"]`

          The type of the object. Always `input_text`.

          - `"input_text"`

      - `class InputContentParamInputImage: …`

        Image input to the model.

        - `image_url: str`

          The URL of the image sent to the model.

        - `type: Literal["input_image"]`

          The type of the object. Always `input_image`.

          - `"input_image"`

    - `role: Literal["user"]`

      The role of the message author. Always `user`.

      - `"user"`

    - `type: Optional[Literal["message"]]`

      The type of the input item. Always `message`.

      - `"message"`

- `metadata: Optional[Dict[str, str]]`

  Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters. Omission or null defaults to an empty map.

- `stream: Optional[Literal[false]]`

  Whether to stream session events as server-sent events. Defaults to `false`.

  - `false`

- `vault_ids: Optional[Sequence[str]]`

  The IDs of vaults made available to the session.

- `class AgentSession: …`

  A Managed Agents session.

  - `id: str`

    The ID of the session.

  - `agent: Agent`

    The agent running in the session.

    - `id: str`

      The ID of the agent.

    - `instructions: Optional[str]`

      Custom instructions appended to the agent's default base instructions.

    - `model: str`

      The model used by the agent.

    - `multi_agent: MultiAgentConfig`

      Configuration for creating and coordinating subagents.

      - `enabled: bool`

        Whether subagent tools are enabled. Defaults to false.

      - `max_concurrent_subagents: Optional[int]`

        Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

    - `name: Optional[str]`

      The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

    - `reasoning: AgentReasoning`

      The agent's reasoning configuration.

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

      Tools available to the agent.

      - `class AgentToolResourceFunction: …`

        A function defined by the application.

        - `defer_loading: bool`

          Whether the function is deferred and discovered through tool search.

        - `description: str`

          A description of what the function does.

        - `name: str`

          The name of the function.

        - `parameters: Dict[str, object]`

          A JSON Schema object describing the function's arguments.

        - `type: Literal["function"]`

          The type of the object. Always `function`.

          - `"function"`

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

        - `connection_origin: Literal["service", "environment"]`

          Where outbound MCP HTTP connections originate.

          - `"service"`

          - `"environment"`

        - `credential_id: Optional[str]`

          The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

        - `request_metadata: Dict[str, object]`

          Metadata included with requests to this MCP server.

        - `required: bool`

          Whether this MCP server must initialize before the first turn.

        - `server_label: str`

          A label used to identify the MCP server in tool calls.

        - `transport: McpTransport`

          The transport used to connect to the MCP server.

          - `class McpTransportResourceHTTP: …`

            Connects to an MCP server over HTTP.

            - `server_url: str`

              The URL of the MCP server.

            - `type: Literal["http"]`

              The type of the object. Always `http`.

              - `"http"`

          - `class McpTransportResourceStdio: …`

            Starts an MCP server as a local process.

            - `args: List[str]`

              Arguments passed to the MCP server command.

            - `command: str`

              The command used to start the MCP server.

            - `cwd: str`

              The working directory used to start the MCP server.

            - `env_vars: List[str]`

              Environment variable names inherited from the execution environment.

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

        - `context_size: Literal["low", "medium", "high"]`

          The amount of search context made available to the model. Defaults to `medium`.

          - `"low"`

          - `"medium"`

          - `"high"`

        - `location: Optional[AgentToolResourceWebSearchLocation]`

          Approximate location used to localize search results, if provided.

          - `city: Optional[str]`

            The city name.

          - `country: Optional[str]`

            The two-letter ISO country code, such as `US`.

          - `region: Optional[str]`

            The region or state name.

          - `timezone: Optional[str]`

            The IANA timezone, such as `America/Los_Angeles`.

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

  - `created_at: int`

    The Unix timestamp, in seconds, when the session was created.

  - `environment: Environment`

    The execution environment for the session.

    - `class EnvironmentResourceNone: …`

      The session talks to CCA without selecting or provisioning an execution environment.

      - `type: Literal["none"]`

        The type of the object. Always `none`.

        - `"none"`

    - `class EnvironmentResourceOpenAIHosted: …`

      An environment hosted by OpenAI.

      - `id: str`

        The public ID of the environment.

      - `capability_directories: List[str]`

        Directories that contain capabilities exposed to the agent.

      - `desktop: EnvironmentResourceOpenAIHostedDesktop`

        The effective desktop configuration.

        - `enabled: bool`

          Whether the environment provisions a desktop and browser proxy.

      - `files: List[HostedEnvironmentFile]`

        Files available in the environment, excluding their contents.

        - `class HostedEnvironmentFileID: …`

          A file copied from the OpenAI Files API.

          - `id: str`

            The session-scoped ID of the file in the execution environment.

          - `file_id: str`

            The ID of the uploaded file.

          - `path: str`

            The file's absolute path inside the environment.

          - `size_bytes: int`

            The decoded file size in bytes.

          - `type: Literal["file_id"]`

            The type of the object. Always `file_id`.

            - `"file_id"`

        - `class HostedEnvironmentFileResourceInline: …`

          A file supplied inline when the session was created.

          - `id: str`

            The session-scoped ID of the file in the execution environment.

          - `path: str`

            The file's absolute path inside the environment.

          - `size_bytes: int`

            The decoded file size in bytes.

          - `type: Literal["inline"]`

            The type of the object. Always `inline`.

            - `"inline"`

      - `network: EnvironmentResourceOpenAIHostedNetwork`

        The effective network access policy for the environment.

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

      - `packages: EnvironmentResourceOpenAIHostedPackages`

        Packages installed in the environment.

        - `npm: List[str]`

          npm packages installed globally in the environment.

        - `python: List[str]`

          Python packages installed in the environment.

        - `system: List[str]`

          System packages installed in the environment.

      - `plugins: List[HostedPlugin]`

        Plugins installed in the environment, excluding their archive contents.

        - `description: str`

          The installed plugin description.

        - `name: str`

          The installed plugin name.

        - `type: Literal["inline"]`

          The type of the object. Always `inline`.

          - `"inline"`

      - `skills: List[HostedSkill]`

        Skills installed in the environment, excluding their archive contents.

        - `class HostedSkillReference: …`

          A skill installed from the Skills API.

          - `description: str`

            The installed skill description.

          - `name: str`

            The installed skill name.

          - `skill_id: str`

            The referenced skill ID.

          - `type: Literal["skill_reference"]`

            The type of the object. Always `skill_reference`.

            - `"skill_reference"`

          - `version: str`

            The concrete skill version installed for this session.

        - `class HostedSkillResourceInline: …`

          A skill installed from an inline ZIP archive.

          - `description: str`

            The installed skill description.

          - `name: str`

            The installed skill name.

          - `type: Literal["inline"]`

            The type of the object. Always `inline`.

            - `"inline"`

      - `type: Literal["openai_hosted"]`

        The type of the object. Always `openai_hosted`.

        - `"openai_hosted"`

      - `container_size: Optional[Literal["small", "medium", "large"]]`

        The effective CPU and memory tier, or null when unknown or outside the public tiers.

        - `"small"`

        - `"medium"`

        - `"large"`

    - `class EnvironmentResourceSelfHosted: …`

      An environment hosted by the application.

      - `id: str`

        The public ID of the environment.

      - `capability_directories: List[str]`

        Directories that contain capabilities exposed to the agent.

      - `remote_url: str`

        Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

      - `type: Literal["self_hosted"]`

        The type of the object. Always `self_hosted`.

        - `"self_hosted"`

      - `workspace_directory: str`

        The absolute project directory inside the environment. Defaults to `/workspace`.

  - `error: Optional[str]`

    The error that caused the session to fail, if any.

  - `last_active_at: int`

    The Unix timestamp, in seconds, when the session was last active.

  - `metadata: Dict[str, str]`

    Custom string key-value pairs attached to the session.

  - `object: Literal["agent.session"]`

    The object type. Always `agent.session`.

    - `"agent.session"`

  - `required_actions: List[RequiredAction]`

    Actions that must be completed before the session can continue.

    - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequest: …`

      Respond to a computer-use request.

      - `request: RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequest`

        The information needed to render the request.

        - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthentication: …`

          A registered form awaiting the application's response.

          - `credential_origin: Optional[str]`

            The registered form or frame origin where values will be entered.

          - `fields: List[RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthenticationField]`

            Controls to render. All submitted values are sensitive.

            - `id: str`

              The field ID to submit as field_id in a fields entry.

            - `label: str`

              The label to display beside the control.

            - `required: bool`

              Whether this control requires a nonempty value.

            - `type: str`

              The rendering type, such as email, password, or text.

          - `options: List[RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthenticationOption]`

            Sign-in methods. Empty for a plain form.

            - `id: str`

              The option ID to submit as selected_option.

            - `field_ids: List[str]`

              IDs from the registered fields that this method accepts.

            - `label: str`

              The method label to display.

          - `reason: Optional[str]`

            Why the agent needs the user to sign in.

          - `type: Literal["browser_authentication"]`

            The type of the object. Always `browser_authentication`.

            - `"browser_authentication"`

        - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserOriginAccess: …`

          A browser origin awaiting the application's approval decision.

          - `origin: str`

            The origin the browser needs permission to access.

          - `reason: Optional[str]`

            The browser's explanation for this request, or null when unavailable.

          - `type: Literal["browser_origin_access"]`

            The type of the object. Always `browser_origin_access`.

            - `"browser_origin_access"`

      - `request_id: str`

        The registered request ID to echo when responding.

      - `turn_id: str`

        The turn that requested approval.

      - `type: Literal["computer_use_approval_request"]`

        The type of the object. Always `computer_use_approval_request`.

        - `"computer_use_approval_request"`

    - `class RequiredActionSessionRequiredActionResourceFunctionCall: …`

      Run a function tool and submit its result.

      - `arguments: object`

        The arguments supplied by the model.

      - `call_id: str`

        The ID to include when submitting the function result.

      - `name: str`

        The function name.

      - `turn_id: str`

        The ID of the turn that requested the function call.

      - `type: Literal["function_call"]`

        The type of the object. Always `function_call`.

        - `"function_call"`

    - `class RequiredActionSessionRequiredActionResourceEnvironmentConnection: …`

      Reconnect a session environment.

      - `environment_id: str`

        The ID of the environment to reconnect.

      - `type: Literal["environment_connection"]`

        The type of the object. Always `environment_connection`.

        - `"environment_connection"`

  - `status: Literal["idle", "in_progress", "requires_action", "failed"]`

    The current status of the session.

    - `"idle"`

      The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

    - `"in_progress"`

      The session is processing a turn.

    - `"requires_action"`

      The session is waiting for one or more required actions.

    - `"failed"`

      The session failed.

  - `usage: Optional[TokenUsage]`

    Best-effort token usage for the session, or null if unknown. Recorded usage may change.

    - `input_tokens: int`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails`

      A breakdown of the agent's input token usage.

      - `cached_tokens: int`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: int`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: int`

        The number of output tokens used for reasoning.

    - `total_tokens: int`

      The total number of input and output tokens used by the agent.

  - `vault_ids: List[str]`

    The IDs of vaults made available to the session.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
for session in client.beta.agents.sessions.create(
    environment={
        "type": "none"
):
  print(session)

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
