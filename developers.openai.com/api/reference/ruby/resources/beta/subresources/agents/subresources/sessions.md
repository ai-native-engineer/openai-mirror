<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/agents/subresources/sessions/ -->

# Sessions

## Create an agent session

`beta.agents.sessions.create(**kwargs) -> AgentSession`

**post** `/agents/sessions`

Creates a managed agent session, optionally submits initial input, and returns the session or streams its events when stream is true. See [running sessions](/api/docs/guides/agents-api/sessions).

### Parameters

- `environment: EnvironmentParam`

  An inline execution environment or a reference to an environment template.

  - `class None`

    Runs the agent without an execution environment.

    - `type: :none`

      The type of the object. Always `none`.

      - `:none`

  - `class OpenAIHosted`

    An existing OpenAI-hosted environment or new inline/template-based hosted configuration.

    - `type: :openai_hosted`

      The type of the object. Always `openai_hosted`.

      - `:openai_hosted`

    - `capability_directories: Array[String]`

      Directories that contain capabilities exposed to the agent. Defaults to an empty list.

    - `container_size: :small | :medium | :large`

      The hosted container size. Omission selects the medium tier.

      - `:small`

      - `:medium`

      - `:large`

    - `desktop: Desktop{ enabled}`

      Desktop provisioning. Omission or null inherits the template setting, or defaults to disabled.

      - `enabled: bool`

        Whether to provision the desktop and its browser proxy.

    - `env: Hash[Symbol, String]`

      Environment variables made available to the agent.

    - `environment_template_id: String`

      A reusable hosted template applied before inline session configuration. Omitted fields inherit the template; network overrides cannot broaden its policy.

    - `files: Array[HostedEnvironmentFileParam]`

      Files available before the agent starts. Defaults to an empty list.

      - `class FileID`

        A file previously uploaded through the OpenAI Files API.

        - `file_id: String`

          The ID of the uploaded file.

        - `path: String`

          The absolute destination path inside `/workspace`.

        - `type: :file_id`

          The type of the object. Always `file_id`.

          - `:file_id`

      - `class Inline`

        A file supplied directly as standard-base64 data.

        - `data: String`

          The standard-base64-encoded file contents.

        - `path: String`

          The absolute destination path inside `/workspace`.

        - `type: :inline`

          The type of the object. Always `inline`.

          - `:inline`

    - `network: Network{ access, allowed_domains, blocked_domains}`

      Network access policy for the environment. Defaults to disabled for GA requests and enabled for beta requests.

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

      - `blocked_domains: Array[String]`

        Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

    - `packages: Packages{ npm, python, system_}`

      Packages to install in the environment. Defaults to empty package lists.

      - `npm: Array[String]`

        npm packages to install globally. Defaults to an empty list.

      - `python: Array[String]`

        Python packages to install. Defaults to an empty list.

      - `system_: Array[String]`

        System packages to install. Defaults to an empty list.

    - `plugins: Array[HostedPluginParam]`

      Plugins provided as inline ZIP archives. Defaults to an empty list.

      - `description: String`

        The plugin description declared in `.codex-plugin/plugin.json`.

      - `name: String`

        The plugin name declared in `.codex-plugin/plugin.json`.

      - `source: InlineCapabilitySourceParam`

        Provides ZIP bytes encoded with standard base64.

        - `data: String`

          Standard-base64 encoded ZIP archive bytes.

        - `media_type: :"application/zip"`

          The archive media type, always `application/zip`.

          - `:"application/zip"`

            A ZIP archive.

        - `type: :base64`

          The type of the object. Always `base64`.

          - `:base64`

      - `type: :inline`

        The type of the object. Always `inline`.

        - `:inline`

    - `setup_commands: Array[SetupCommandParam]`

      Ordered, confidential setup commands. Command bodies are never returned.

      - `command: String`

        The shell command to execute.

      - `cwd: String`

        The absolute working directory. Defaults to `/workspace`.

    - `skills: Array[HostedSkillParam]`

      Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

      - `class SkillReference`

        References a skill uploaded through the Skills API.

        - `skill_id: String`

          The ID of the skill created through `/v1/skills`.

        - `type: :skill_reference`

          The type of the object. Always `skill_reference`.

          - `:skill_reference`

        - `version: String`

          The skill version, a positive integer or `latest`; omission selects the default.

      - `class Inline`

        Supplies a skill ZIP directly in the session request.

        - `description: String`

          The skill description declared in `SKILL.md`.

        - `name: String`

          The skill name declared in `SKILL.md`.

        - `source: InlineCapabilitySourceParam`

          Provides ZIP bytes encoded with standard base64.

        - `type: :inline`

          The type of the object. Always `inline`.

          - `:inline`

  - `class SelfHosted`

    An application-hosted environment configured inline.

    - `type: :self_hosted`

      The type of the object. Always `self_hosted`.

      - `:self_hosted`

    - `workspace_directory: String`

      Absolute project directory inside the self-hosted environment.

    - `capability_directories: Array[String]`

      Directories that contain capabilities exposed to the agent. Defaults to an empty list.

- `agent: Agent{ instructions, model, multi_agent, 4 more}`

  Agent configuration. With `agent_id`, supplied fields override the saved agent for this session. Without `agent_id`, `model` is required.

  - `instructions: String`

    Additional instructions appended to the agent's default base instructions. Omit to leave unchanged.

  - `model: String`

    The model to use for the agent. The requested model name is preserved.

  - `multi_agent: MultiAgentConfigParam`

    Configuration for creating and coordinating subagents.

    - `enabled: bool`

      Whether subagent tools are enabled.

    - `max_concurrent_subagents: Integer`

      Maximum number of subagents that may run concurrently. Defaults to 6.

  - `reasoning: AgentReasoningParam`

    Configuration for model reasoning. Omit to keep the current settings; pass `null` to reset to the model's default effort.

    - `effort: :none | :minimal | :low | 4 more`

      The amount of reasoning effort the model should use. Omission lets the model select it.

      - `:none`

      - `:minimal`

      - `:low`

      - `:medium`

      - `:high`

      - `:xhigh`

      - `:max`

    - `summary: :concise | :detailed | :auto`

      Controls whether the response includes a reasoning summary.

      - `:concise`

        Returns a concise reasoning summary when supported.

      - `:detailed`

        Returns a detailed reasoning summary when supported.

      - `:auto`

        Automatically selects the most detailed summary supported by the model.

  - `service_tier: :auto | :default | :flex | 3 more`

    The service tier used for model requests.

    - `:auto`

      Selects the service tier automatically.

    - `:default`

      Uses the default service tier.

    - `:flex`

      Uses the flex service tier.

    - `:priority`

      Uses the priority service tier.

    - `:fast`

      Uses the fast service tier.

    - `:ultrafast`

      Uses the ultrafast service tier.

  - `text: AgentTextParam`

    Configuration for text generated by the agent.

    - `format_: TextFormatParam`

      The output format. Omission uses ordinary text (`{"type": "text"}`).

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

      The amount of text the model should produce. Defaults to `medium`, matching Responses.

      - `:low`

        Produces less text.

      - `:medium`

        Uses the default amount of text.

      - `:high`

        Produces more text.

  - `tools: Array[AgentToolParam]`

    Tools available to the agent. Omit to inherit, or pass null to clear them.

    - `class Function`

      A function defined by the application.

      - `description: String`

        A description of what the function does.

      - `name: String`

        The name of the function.

      - `parameters: Hash[Symbol, untyped]`

        A JSON Schema object describing the function's arguments.

      - `type: :function`

        The type of the object. Always `function`.

        - `:function`

      - `defer_loading: bool`

        Whether this function is deferred and discovered through tool search. Defaults to `false`.

    - `class ToolSearch`

      Discovers deferred function tools and loads them into the model context.

      - `type: :tool_search`

        The type of the object. Always `tool_search`.

        - `:tool_search`

    - `class ProgrammaticToolCalling`

      Enables calling tools from model-generated code.

      - `type: :programmatic_tool_calling`

        The type of the object. Always `programmatic_tool_calling`.

        - `:programmatic_tool_calling`

      - `enabled: bool`

        Whether tools can be called from model-generated code. Defaults to `true`.

    - `class Mcp`

      Tools provided by a remote MCP server.

      - `server_label: String`

        A label used to identify the MCP server in tool calls.

      - `transport: McpTransportParam`

        The transport used to connect to the MCP server.

        - `class HTTP`

          Connects to an MCP server over HTTP.

          - `server_url: String`

            The URL of the MCP server.

          - `type: :http`

            The type of the object. Always `http`.

            - `:http`

          - `authorization: String`

            The authorization value sent to the MCP server, if any.

          - `headers: Hash[Symbol, String]`

            Additional HTTP headers sent to the MCP server.

        - `class Stdio`

          Starts an MCP server as a local process.

          - `command: String`

            The command used to start the MCP server.

          - `cwd: String`

            The working directory used to start the MCP server.

          - `type: :stdio`

            The type of the object. Always `stdio`.

            - `:stdio`

          - `args: Array[String]`

            Arguments passed to the MCP server command.

          - `env: Hash[Symbol, String]`

            Environment variables set for the MCP server process.

          - `env_vars: Array[String]`

            Environment variable names to inherit from the selected execution environment.

      - `type: :mcp`

        The type of the object. Always `mcp`.

        - `:mcp`

      - `allowed_tools: Array[String]`

        The MCP tools the agent may call. All server tools are allowed when omitted.

      - `connection_origin: :service | :environment`

        Selects where outbound MCP HTTP connections originate. Omitted or `service` uses the Managed Agents service network; `environment` uses the session's selected environment.

        - `:service`

          Uses the Managed Agents service network.

        - `:environment`

          Uses the session's execution environment.

      - `credential_id: String`

        The attached vault credential used to authenticate this MCP server. Optional when exactly one attached credential matches the server URL.

      - `request_metadata: Hash[Symbol, untyped]`

        Metadata included with requests to this MCP server.

      - `required: bool`

        Whether this MCP server must initialize before the first turn. Defaults to `false`.

    - `class WebSearch`

      Web search.

      - `type: :web_search`

        The type of the object. Always `web_search`.

        - `:web_search`

      - `allowed_domains: Array[String]`

        Domains the search may include.

      - `context_size: :low | :medium | :high`

        The amount of search context made available to the model. Defaults to `medium`.

        - `:low`

        - `:medium`

        - `:high`

      - `location: Location{ city, country, region, timezone}`

        Approximate location used to localize search results.

        - `city: String`

          The city name.

        - `country: String`

          The two-letter ISO country code, such as `US`.

        - `region: String`

          The region or state name.

        - `timezone: String`

          The IANA timezone, such as `America/Los_Angeles`.

      - `mode: :disabled | :cached | :live`

        The source used for web search results. Defaults to `live`.

        - `:disabled`

          Disables web search.

        - `:cached`

          Uses cached search results.

        - `:live`

          Searches the live web.

    - `class ComputerUse`

      Browser use in an OpenAI-hosted session.

      - `type: :computer_use`

        The type of the object. Always `computer_use`.

        - `:computer_use`

      - `include_screenshots: bool`

        Whether computer tool outputs include screenshots. Defaults to `false`.

- `agent_id: String`

  The ID of a saved reusable agent. Omit `agent` to use its configuration unchanged.

- `input: String | Array[AgentSessionInputMessageParam]`

  Initial input to submit when the session is created. A string is shorthand for a single user message. Required when `environment.type` is `none`, or when `stream` is `true` for an environment that is not `self_hosted`; optional for self-hosted and non-streaming execution environments.

  - `String = String`

  - `UnionMember1 = Array[AgentSessionInputMessageParam]`

    - `content: Array[InputContentParam]`

      The content of the message.

      - `class InputText`

        Text input to the model.

        - `text: String`

          The text sent to the model.

        - `type: :input_text`

          The type of the object. Always `input_text`.

          - `:input_text`

      - `class InputImage`

        Image input to the model.

        - `image_url: String`

          The URL of the image sent to the model.

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

  Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters. Omission or null defaults to an empty map.

- `stream: bool`

  Whether to stream session events as server-sent events. Defaults to `false`.

- `vault_ids: Array[String]`

  The IDs of vaults made available to the session.

### Returns

- `class AgentSession`

  A Managed Agents session.

  - `id: String`

    The ID of the session.

  - `agent: Agent{ id, instructions, model, 6 more}`

    The agent running in the session.

    - `id: String`

      The ID of the agent.

    - `instructions: String`

      Custom instructions appended to the agent's default base instructions.

    - `model: String`

      The model used by the agent.

    - `multi_agent: MultiAgentConfig`

      Configuration for creating and coordinating subagents.

      - `enabled: bool`

        Whether subagent tools are enabled. Defaults to false.

      - `max_concurrent_subagents: Integer`

        Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

    - `name: String`

      The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

    - `reasoning: AgentReasoning`

      The agent's reasoning configuration.

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

      The effective service-tier policy for model requests. Defaults to `auto`.

      - `:auto`

      - `:default`

      - `:flex`

      - `:priority`

      - `:fast`

      - `:ultrafast`

    - `text: AgentText`

      Configuration for text generated by the agent.

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

      Tools available to the agent.

      - `class Function`

        A function defined by the application.

        - `defer_loading: bool`

          Whether the function is deferred and discovered through tool search.

        - `description: String`

          A description of what the function does.

        - `name: String`

          The name of the function.

        - `parameters: Hash[Symbol, untyped]`

          A JSON Schema object describing the function's arguments.

        - `type: :function`

          The type of the object. Always `function`.

          - `:function`

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

        - `connection_origin: :service | :environment`

          Where outbound MCP HTTP connections originate.

          - `:service`

          - `:environment`

        - `credential_id: String`

          The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

        - `request_metadata: Hash[Symbol, untyped]`

          Metadata included with requests to this MCP server.

        - `required: bool`

          Whether this MCP server must initialize before the first turn.

        - `server_label: String`

          A label used to identify the MCP server in tool calls.

        - `transport: McpTransport`

          The transport used to connect to the MCP server.

          - `class HTTP`

            Connects to an MCP server over HTTP.

            - `server_url: String`

              The URL of the MCP server.

            - `type: :http`

              The type of the object. Always `http`.

              - `:http`

          - `class Stdio`

            Starts an MCP server as a local process.

            - `args: Array[String]`

              Arguments passed to the MCP server command.

            - `command: String`

              The command used to start the MCP server.

            - `cwd: String`

              The working directory used to start the MCP server.

            - `env_vars: Array[String]`

              Environment variable names inherited from the execution environment.

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

        - `context_size: :low | :medium | :high`

          The amount of search context made available to the model. Defaults to `medium`.

          - `:low`

          - `:medium`

          - `:high`

        - `location: Location{ city, country, region, timezone}`

          Approximate location used to localize search results, if provided.

          - `city: String`

            The city name.

          - `country: String`

            The two-letter ISO country code, such as `US`.

          - `region: String`

            The region or state name.

          - `timezone: String`

            The IANA timezone, such as `America/Los_Angeles`.

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

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the session was created.

  - `environment: Environment`

    The execution environment for the session.

    - `class None`

      The session talks to CCA without selecting or provisioning an execution environment.

      - `type: :none`

        The type of the object. Always `none`.

        - `:none`

    - `class OpenAIHosted`

      An environment hosted by OpenAI.

      - `id: String`

        The public ID of the environment.

      - `capability_directories: Array[String]`

        Directories that contain capabilities exposed to the agent.

      - `desktop: Desktop{ enabled}`

        The effective desktop configuration.

        - `enabled: bool`

          Whether the environment provisions a desktop and browser proxy.

      - `files: Array[HostedEnvironmentFile]`

        Files available in the environment, excluding their contents.

        - `class HostedEnvironmentFileID`

          A file copied from the OpenAI Files API.

          - `id: String`

            The session-scoped ID of the file in the execution environment.

          - `file_id: String`

            The ID of the uploaded file.

          - `path: String`

            The file's absolute path inside the environment.

          - `size_bytes: Integer`

            The decoded file size in bytes.

          - `type: :file_id`

            The type of the object. Always `file_id`.

            - `:file_id`

        - `class Inline`

          A file supplied inline when the session was created.

          - `id: String`

            The session-scoped ID of the file in the execution environment.

          - `path: String`

            The file's absolute path inside the environment.

          - `size_bytes: Integer`

            The decoded file size in bytes.

          - `type: :inline`

            The type of the object. Always `inline`.

            - `:inline`

      - `network: Network{ access, allowed_domains}`

        The effective network access policy for the environment.

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

      - `packages: Packages{ npm, python, system_}`

        Packages installed in the environment.

        - `npm: Array[String]`

          npm packages installed globally in the environment.

        - `python: Array[String]`

          Python packages installed in the environment.

        - `system_: Array[String]`

          System packages installed in the environment.

      - `plugins: Array[HostedPlugin]`

        Plugins installed in the environment, excluding their archive contents.

        - `description: String`

          The installed plugin description.

        - `name: String`

          The installed plugin name.

        - `type: :inline`

          The type of the object. Always `inline`.

          - `:inline`

      - `skills: Array[HostedSkill]`

        Skills installed in the environment, excluding their archive contents.

        - `class HostedSkillReference`

          A skill installed from the Skills API.

          - `description: String`

            The installed skill description.

          - `name: String`

            The installed skill name.

          - `skill_id: String`

            The referenced skill ID.

          - `type: :skill_reference`

            The type of the object. Always `skill_reference`.

            - `:skill_reference`

          - `version: String`

            The concrete skill version installed for this session.

        - `class Inline`

          A skill installed from an inline ZIP archive.

          - `description: String`

            The installed skill description.

          - `name: String`

            The installed skill name.

          - `type: :inline`

            The type of the object. Always `inline`.

            - `:inline`

      - `type: :openai_hosted`

        The type of the object. Always `openai_hosted`.

        - `:openai_hosted`

      - `container_size: :small | :medium | :large`

        The effective CPU and memory tier, or null when unknown or outside the public tiers.

        - `:small`

        - `:medium`

        - `:large`

    - `class SelfHosted`

      An environment hosted by the application.

      - `id: String`

        The public ID of the environment.

      - `capability_directories: Array[String]`

        Directories that contain capabilities exposed to the agent.

      - `remote_url: String`

        Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

      - `type: :self_hosted`

        The type of the object. Always `self_hosted`.

        - `:self_hosted`

      - `workspace_directory: String`

        The absolute project directory inside the environment. Defaults to `/workspace`.

  - `error: String`

    The error that caused the session to fail, if any.

  - `last_active_at: Integer`

    The Unix timestamp, in seconds, when the session was last active.

  - `metadata: Hash[Symbol, String]`

    Custom string key-value pairs attached to the session.

  - `object: :"agent.session"`

    The object type. Always `agent.session`.

    - `:"agent.session"`

  - `required_actions: Array[ComputerUseApprovalRequest{ request, request_id, turn_id, type} | FunctionCall{ arguments, call_id, name, 2 more} | EnvironmentConnection{ environment_id, type}]`

    Actions that must be completed before the session can continue.

    - `class ComputerUseApprovalRequest`

      Respond to a computer-use request.

      - `request: BrowserAuthentication{ credential_origin, fields, options, 2 more} | BrowserOriginAccess{ origin, reason, type}`

        The information needed to render the request.

        - `class BrowserAuthentication`

          A registered form awaiting the application's response.

          - `credential_origin: String`

            The registered form or frame origin where values will be entered.

          - `fields: Array[Field{ id, label, required, type}]`

            Controls to render. All submitted values are sensitive.

            - `id: String`

              The field ID to submit as field_id in a fields entry.

            - `label: String`

              The label to display beside the control.

            - `required: bool`

              Whether this control requires a nonempty value.

            - `type: String`

              The rendering type, such as email, password, or text.

          - `options: Array[Option{ id, field_ids, label}]`

            Sign-in methods. Empty for a plain form.

            - `id: String`

              The option ID to submit as selected_option.

            - `field_ids: Array[String]`

              IDs from the registered fields that this method accepts.

            - `label: String`

              The method label to display.

          - `reason: String`

            Why the agent needs the user to sign in.

          - `type: :browser_authentication`

            The type of the object. Always `browser_authentication`.

            - `:browser_authentication`

        - `class BrowserOriginAccess`

          A browser origin awaiting the application's approval decision.

          - `origin: String`

            The origin the browser needs permission to access.

          - `reason: String`

            The browser's explanation for this request, or null when unavailable.

          - `type: :browser_origin_access`

            The type of the object. Always `browser_origin_access`.

            - `:browser_origin_access`

      - `request_id: String`

        The registered request ID to echo when responding.

      - `turn_id: String`

        The turn that requested approval.

      - `type: :computer_use_approval_request`

        The type of the object. Always `computer_use_approval_request`.

        - `:computer_use_approval_request`

    - `class FunctionCall`

      Run a function tool and submit its result.

      - `arguments: untyped`

        The arguments supplied by the model.

      - `call_id: String`

        The ID to include when submitting the function result.

      - `name: String`

        The function name.

      - `turn_id: String`

        The ID of the turn that requested the function call.

      - `type: :function_call`

        The type of the object. Always `function_call`.

        - `:function_call`

    - `class EnvironmentConnection`

      Reconnect a session environment.

      - `environment_id: String`

        The ID of the environment to reconnect.

      - `type: :environment_connection`

        The type of the object. Always `environment_connection`.

        - `:environment_connection`

  - `status: :idle | :in_progress | :requires_action | :failed`

    The current status of the session.

    - `:idle`

      The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

    - `:in_progress`

      The session is processing a turn.

    - `:requires_action`

      The session is waiting for one or more required actions.

    - `:failed`

      The session failed.

  - `usage: TokenUsage`

    Best-effort token usage for the session, or null if unknown. Recorded usage may change.

    - `input_tokens: Integer`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails{ cached_tokens}`

      A breakdown of the agent's input token usage.

      - `cached_tokens: Integer`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: Integer`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails{ reasoning_tokens}`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: Integer`

        The number of output tokens used for reasoning.

    - `total_tokens: Integer`

      The total number of input and output tokens used by the agent.

  - `vault_ids: Array[String]`

    The IDs of vaults made available to the session.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

agent_session = openai.beta.agents.sessions.create(environment: {type: :none})

puts(agent_session)
```

#### Response

```json
{
  "id": "id",
  "agent": {
    "id": "id",
    "instructions": "instructions",
    "model": "model",
    "multi_agent": {
      "enabled": true,
      "max_concurrent_subagents": 1
    },
    "name": "name",
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
        "type": "function"
      }
    ]
  },
  "created_at": 0,
  "environment": {
    "type": "none"
  },
  "error": "error",
  "last_active_at": 0,
  "metadata": {
    "foo": "string"
  },
  "object": "agent.session",
  "required_actions": [
    {
      "request": {
        "credential_origin": "credential_origin",
        "fields": [
          {
            "id": "id",
            "label": "label",
            "required": true,
            "type": "type"
          }
        ],
        "options": [
          {
            "id": "id",
            "field_ids": [
              "string"
            ],
            "label": "label"
          }
        ],
        "reason": "reason",
        "type": "browser_authentication"
      },
      "request_id": "request_id",
      "turn_id": "turn_id",
      "type": "computer_use_approval_request"
    }
  ],
  "status": "idle",
  "usage": {
    "input_tokens": 0,
    "input_tokens_details": {
      "cached_tokens": 0
    },
    "output_tokens": 0,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "total_tokens": 0
  },
  "vault_ids": [
    "string"
  ]
}
```

## Delete an agent session

`beta.agents.sessions.delete(session_id) -> AgentSessionDeleted`

**delete** `/agents/sessions/{session_id}`

Removes a managed agent session from the public API and returns a deletion confirmation. If backend execution has ended, deletion can cancel a still-open public turn and abandon unpublished outputs. Running execution must be cancelled first. Physical cleanup may continue asynchronously. See [managing sessions](/api/docs/guides/agents-api/sessions/manage).

### Parameters

- `session_id: String`

### Returns

- `class AgentSessionDeleted`

  A Managed Agents session removed from the public API. Physical cleanup may continue asynchronously.

  - `id: String`

    The ID of the deleted session.

  - `deleted: bool`

    Whether the session has been removed from the public API. Always `true`. Physical cleanup may still be in progress.

  - `object: :"agent.session.deleted"`

    The object type. Always `agent.session.deleted`.

    - `:"agent.session.deleted"`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

agent_session_deleted = openai.beta.agents.sessions.delete("session_id")

puts(agent_session_deleted)
```

#### Response

```json
{
  "id": "id",
  "deleted": true,
  "object": "agent.session.deleted"
}
```

## List agent sessions

`beta.agents.sessions.list(**kwargs) -> CursorPage<AgentSession>`

**get** `/agents/sessions`

Lists managed agent sessions using ID-based pagination and the requested sort order. See [managing sessions](/api/docs/guides/agents-api/sessions/manage).

### Parameters

- `after: String`

  Return resources after this resource ID in the selected order.

- `agent_id: String`

  Only return sessions whose root agent has this ID. Omit to return sessions for all agents.

- `limit: Integer`

  The maximum number of resources to return.

- `order: :asc | :desc`

  Sort order by the `created_at` timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `desc`.

  - `:asc`

    Returns resources in ascending order.

  - `:desc`

    Returns resources in descending order.

### Returns

- `class AgentSession`

  A Managed Agents session.

  - `id: String`

    The ID of the session.

  - `agent: Agent{ id, instructions, model, 6 more}`

    The agent running in the session.

    - `id: String`

      The ID of the agent.

    - `instructions: String`

      Custom instructions appended to the agent's default base instructions.

    - `model: String`

      The model used by the agent.

    - `multi_agent: MultiAgentConfig`

      Configuration for creating and coordinating subagents.

      - `enabled: bool`

        Whether subagent tools are enabled. Defaults to false.

      - `max_concurrent_subagents: Integer`

        Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

    - `name: String`

      The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

    - `reasoning: AgentReasoning`

      The agent's reasoning configuration.

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

      The effective service-tier policy for model requests. Defaults to `auto`.

      - `:auto`

      - `:default`

      - `:flex`

      - `:priority`

      - `:fast`

      - `:ultrafast`

    - `text: AgentText`

      Configuration for text generated by the agent.

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

      Tools available to the agent.

      - `class Function`

        A function defined by the application.

        - `defer_loading: bool`

          Whether the function is deferred and discovered through tool search.

        - `description: String`

          A description of what the function does.

        - `name: String`

          The name of the function.

        - `parameters: Hash[Symbol, untyped]`

          A JSON Schema object describing the function's arguments.

        - `type: :function`

          The type of the object. Always `function`.

          - `:function`

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

        - `connection_origin: :service | :environment`

          Where outbound MCP HTTP connections originate.

          - `:service`

          - `:environment`

        - `credential_id: String`

          The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

        - `request_metadata: Hash[Symbol, untyped]`

          Metadata included with requests to this MCP server.

        - `required: bool`

          Whether this MCP server must initialize before the first turn.

        - `server_label: String`

          A label used to identify the MCP server in tool calls.

        - `transport: McpTransport`

          The transport used to connect to the MCP server.

          - `class HTTP`

            Connects to an MCP server over HTTP.

            - `server_url: String`

              The URL of the MCP server.

            - `type: :http`

              The type of the object. Always `http`.

              - `:http`

          - `class Stdio`

            Starts an MCP server as a local process.

            - `args: Array[String]`

              Arguments passed to the MCP server command.

            - `command: String`

              The command used to start the MCP server.

            - `cwd: String`

              The working directory used to start the MCP server.

            - `env_vars: Array[String]`

              Environment variable names inherited from the execution environment.

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

        - `context_size: :low | :medium | :high`

          The amount of search context made available to the model. Defaults to `medium`.

          - `:low`

          - `:medium`

          - `:high`

        - `location: Location{ city, country, region, timezone}`

          Approximate location used to localize search results, if provided.

          - `city: String`

            The city name.

          - `country: String`

            The two-letter ISO country code, such as `US`.

          - `region: String`

            The region or state name.

          - `timezone: String`

            The IANA timezone, such as `America/Los_Angeles`.

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

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the session was created.

  - `environment: Environment`

    The execution environment for the session.

    - `class None`

      The session talks to CCA without selecting or provisioning an execution environment.

      - `type: :none`

        The type of the object. Always `none`.

        - `:none`

    - `class OpenAIHosted`

      An environment hosted by OpenAI.

      - `id: String`

        The public ID of the environment.

      - `capability_directories: Array[String]`

        Directories that contain capabilities exposed to the agent.

      - `desktop: Desktop{ enabled}`

        The effective desktop configuration.

        - `enabled: bool`

          Whether the environment provisions a desktop and browser proxy.

      - `files: Array[HostedEnvironmentFile]`

        Files available in the environment, excluding their contents.

        - `class HostedEnvironmentFileID`

          A file copied from the OpenAI Files API.

          - `id: String`

            The session-scoped ID of the file in the execution environment.

          - `file_id: String`

            The ID of the uploaded file.

          - `path: String`

            The file's absolute path inside the environment.

          - `size_bytes: Integer`

            The decoded file size in bytes.

          - `type: :file_id`

            The type of the object. Always `file_id`.

            - `:file_id`

        - `class Inline`

          A file supplied inline when the session was created.

          - `id: String`

            The session-scoped ID of the file in the execution environment.

          - `path: String`

            The file's absolute path inside the environment.

          - `size_bytes: Integer`

            The decoded file size in bytes.

          - `type: :inline`

            The type of the object. Always `inline`.

            - `:inline`

      - `network: Network{ access, allowed_domains}`

        The effective network access policy for the environment.

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

      - `packages: Packages{ npm, python, system_}`

        Packages installed in the environment.

        - `npm: Array[String]`

          npm packages installed globally in the environment.

        - `python: Array[String]`

          Python packages installed in the environment.

        - `system_: Array[String]`

          System packages installed in the environment.

      - `plugins: Array[HostedPlugin]`

        Plugins installed in the environment, excluding their archive contents.

        - `description: String`

          The installed plugin description.

        - `name: String`

          The installed plugin name.

        - `type: :inline`

          The type of the object. Always `inline`.

          - `:inline`

      - `skills: Array[HostedSkill]`

        Skills installed in the environment, excluding their archive contents.

        - `class HostedSkillReference`

          A skill installed from the Skills API.

          - `description: String`

            The installed skill description.

          - `name: String`

            The installed skill name.

          - `skill_id: String`

            The referenced skill ID.

          - `type: :skill_reference`

            The type of the object. Always `skill_reference`.

            - `:skill_reference`

          - `version: String`

            The concrete skill version installed for this session.

        - `class Inline`

          A skill installed from an inline ZIP archive.

          - `description: String`

            The installed skill description.

          - `name: String`

            The installed skill name.

          - `type: :inline`

            The type of the object. Always `inline`.

            - `:inline`

      - `type: :openai_hosted`

        The type of the object. Always `openai_hosted`.

        - `:openai_hosted`

      - `container_size: :small | :medium | :large`

        The effective CPU and memory tier, or null when unknown or outside the public tiers.

        - `:small`

        - `:medium`

        - `:large`

    - `class SelfHosted`

      An environment hosted by the application.

      - `id: String`

        The public ID of the environment.

      - `capability_directories: Array[String]`

        Directories that contain capabilities exposed to the agent.

      - `remote_url: String`

        Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

      - `type: :self_hosted`

        The type of the object. Always `self_hosted`.

        - `:self_hosted`

      - `workspace_directory: String`

        The absolute project directory inside the environment. Defaults to `/workspace`.

  - `error: String`

    The error that caused the session to fail, if any.

  - `last_active_at: Integer`

    The Unix timestamp, in seconds, when the session was last active.

  - `metadata: Hash[Symbol, String]`

    Custom string key-value pairs attached to the session.

  - `object: :"agent.session"`

    The object type. Always `agent.session`.

    - `:"agent.session"`

  - `required_actions: Array[ComputerUseApprovalRequest{ request, request_id, turn_id, type} | FunctionCall{ arguments, call_id, name, 2 more} | EnvironmentConnection{ environment_id, type}]`

    Actions that must be completed before the session can continue.

    - `class ComputerUseApprovalRequest`

      Respond to a computer-use request.

      - `request: BrowserAuthentication{ credential_origin, fields, options, 2 more} | BrowserOriginAccess{ origin, reason, type}`

        The information needed to render the request.

        - `class BrowserAuthentication`

          A registered form awaiting the application's response.

          - `credential_origin: String`

            The registered form or frame origin where values will be entered.

          - `fields: Array[Field{ id, label, required, type}]`

            Controls to render. All submitted values are sensitive.

            - `id: String`

              The field ID to submit as field_id in a fields entry.

            - `label: String`

              The label to display beside the control.

            - `required: bool`

              Whether this control requires a nonempty value.

            - `type: String`

              The rendering type, such as email, password, or text.

          - `options: Array[Option{ id, field_ids, label}]`

            Sign-in methods. Empty for a plain form.

            - `id: String`

              The option ID to submit as selected_option.

            - `field_ids: Array[String]`

              IDs from the registered fields that this method accepts.

            - `label: String`

              The method label to display.

          - `reason: String`

            Why the agent needs the user to sign in.

          - `type: :browser_authentication`

            The type of the object. Always `browser_authentication`.

            - `:browser_authentication`

        - `class BrowserOriginAccess`

          A browser origin awaiting the application's approval decision.

          - `origin: String`

            The origin the browser needs permission to access.

          - `reason: String`

            The browser's explanation for this request, or null when unavailable.

          - `type: :browser_origin_access`

            The type of the object. Always `browser_origin_access`.

            - `:browser_origin_access`

      - `request_id: String`

        The registered request ID to echo when responding.

      - `turn_id: String`

        The turn that requested approval.

      - `type: :computer_use_approval_request`

        The type of the object. Always `computer_use_approval_request`.

        - `:computer_use_approval_request`

    - `class FunctionCall`

      Run a function tool and submit its result.

      - `arguments: untyped`

        The arguments supplied by the model.

      - `call_id: String`

        The ID to include when submitting the function result.

      - `name: String`

        The function name.

      - `turn_id: String`

        The ID of the turn that requested the function call.

      - `type: :function_call`

        The type of the object. Always `function_call`.

        - `:function_call`

    - `class EnvironmentConnection`

      Reconnect a session environment.

      - `environment_id: String`

        The ID of the environment to reconnect.

      - `type: :environment_connection`

        The type of the object. Always `environment_connection`.

        - `:environment_connection`

  - `status: :idle | :in_progress | :requires_action | :failed`

    The current status of the session.

    - `:idle`

      The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

    - `:in_progress`

      The session is processing a turn.

    - `:requires_action`

      The session is waiting for one or more required actions.

    - `:failed`

      The session failed.

  - `usage: TokenUsage`

    Best-effort token usage for the session, or null if unknown. Recorded usage may change.

    - `input_tokens: Integer`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails{ cached_tokens}`

      A breakdown of the agent's input token usage.

      - `cached_tokens: Integer`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: Integer`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails{ reasoning_tokens}`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: Integer`

        The number of output tokens used for reasoning.

    - `total_tokens: Integer`

      The total number of input and output tokens used by the agent.

  - `vault_ids: Array[String]`

    The IDs of vaults made available to the session.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.beta.agents.sessions.list

puts(page)
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "agent": {
        "id": "id",
        "instructions": "instructions",
        "model": "model",
        "multi_agent": {
          "enabled": true,
          "max_concurrent_subagents": 1
        },
        "name": "name",
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
            "type": "function"
          }
        ]
      },
      "created_at": 0,
      "environment": {
        "type": "none"
      },
      "error": "error",
      "last_active_at": 0,
      "metadata": {
        "foo": "string"
      },
      "object": "agent.session",
      "required_actions": [
        {
          "request": {
            "credential_origin": "credential_origin",
            "fields": [
              {
                "id": "id",
                "label": "label",
                "required": true,
                "type": "type"
              }
            ],
            "options": [
              {
                "id": "id",
                "field_ids": [
                  "string"
                ],
                "label": "label"
              }
            ],
            "reason": "reason",
            "type": "browser_authentication"
          },
          "request_id": "request_id",
          "turn_id": "turn_id",
          "type": "computer_use_approval_request"
        }
      ],
      "status": "idle",
      "usage": {
        "input_tokens": 0,
        "input_tokens_details": {
          "cached_tokens": 0
        },
        "output_tokens": 0,
        "output_tokens_details": {
          "reasoning_tokens": 0
        },
        "total_tokens": 0
      },
      "vault_ids": [
        "string"
      ]
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve an agent session

`beta.agents.sessions.retrieve(session_id) -> AgentSession`

**get** `/agents/sessions/{session_id}`

Retrieves the current state of a managed agent session. See [managing sessions](/api/docs/guides/agents-api/sessions/manage).

### Parameters

- `session_id: String`

### Returns

- `class AgentSession`

  A Managed Agents session.

  - `id: String`

    The ID of the session.

  - `agent: Agent{ id, instructions, model, 6 more}`

    The agent running in the session.

    - `id: String`

      The ID of the agent.

    - `instructions: String`

      Custom instructions appended to the agent's default base instructions.

    - `model: String`

      The model used by the agent.

    - `multi_agent: MultiAgentConfig`

      Configuration for creating and coordinating subagents.

      - `enabled: bool`

        Whether subagent tools are enabled. Defaults to false.

      - `max_concurrent_subagents: Integer`

        Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

    - `name: String`

      The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

    - `reasoning: AgentReasoning`

      The agent's reasoning configuration.

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

      The effective service-tier policy for model requests. Defaults to `auto`.

      - `:auto`

      - `:default`

      - `:flex`

      - `:priority`

      - `:fast`

      - `:ultrafast`

    - `text: AgentText`

      Configuration for text generated by the agent.

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

      Tools available to the agent.

      - `class Function`

        A function defined by the application.

        - `defer_loading: bool`

          Whether the function is deferred and discovered through tool search.

        - `description: String`

          A description of what the function does.

        - `name: String`

          The name of the function.

        - `parameters: Hash[Symbol, untyped]`

          A JSON Schema object describing the function's arguments.

        - `type: :function`

          The type of the object. Always `function`.

          - `:function`

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

        - `connection_origin: :service | :environment`

          Where outbound MCP HTTP connections originate.

          - `:service`

          - `:environment`

        - `credential_id: String`

          The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

        - `request_metadata: Hash[Symbol, untyped]`

          Metadata included with requests to this MCP server.

        - `required: bool`

          Whether this MCP server must initialize before the first turn.

        - `server_label: String`

          A label used to identify the MCP server in tool calls.

        - `transport: McpTransport`

          The transport used to connect to the MCP server.

          - `class HTTP`

            Connects to an MCP server over HTTP.

            - `server_url: String`

              The URL of the MCP server.

            - `type: :http`

              The type of the object. Always `http`.

              - `:http`

          - `class Stdio`

            Starts an MCP server as a local process.

            - `args: Array[String]`

              Arguments passed to the MCP server command.

            - `command: String`

              The command used to start the MCP server.

            - `cwd: String`

              The working directory used to start the MCP server.

            - `env_vars: Array[String]`

              Environment variable names inherited from the execution environment.

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

        - `context_size: :low | :medium | :high`

          The amount of search context made available to the model. Defaults to `medium`.

          - `:low`

          - `:medium`

          - `:high`

        - `location: Location{ city, country, region, timezone}`

          Approximate location used to localize search results, if provided.

          - `city: String`

            The city name.

          - `country: String`

            The two-letter ISO country code, such as `US`.

          - `region: String`

            The region or state name.

          - `timezone: String`

            The IANA timezone, such as `America/Los_Angeles`.

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

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the session was created.

  - `environment: Environment`

    The execution environment for the session.

    - `class None`

      The session talks to CCA without selecting or provisioning an execution environment.

      - `type: :none`

        The type of the object. Always `none`.

        - `:none`

    - `class OpenAIHosted`

      An environment hosted by OpenAI.

      - `id: String`

        The public ID of the environment.

      - `capability_directories: Array[String]`

        Directories that contain capabilities exposed to the agent.

      - `desktop: Desktop{ enabled}`

        The effective desktop configuration.

        - `enabled: bool`

          Whether the environment provisions a desktop and browser proxy.

      - `files: Array[HostedEnvironmentFile]`

        Files available in the environment, excluding their contents.

        - `class HostedEnvironmentFileID`

          A file copied from the OpenAI Files API.

          - `id: String`

            The session-scoped ID of the file in the execution environment.

          - `file_id: String`

            The ID of the uploaded file.

          - `path: String`

            The file's absolute path inside the environment.

          - `size_bytes: Integer`

            The decoded file size in bytes.

          - `type: :file_id`

            The type of the object. Always `file_id`.

            - `:file_id`

        - `class Inline`

          A file supplied inline when the session was created.

          - `id: String`

            The session-scoped ID of the file in the execution environment.

          - `path: String`

            The file's absolute path inside the environment.

          - `size_bytes: Integer`

            The decoded file size in bytes.

          - `type: :inline`

            The type of the object. Always `inline`.

            - `:inline`

      - `network: Network{ access, allowed_domains}`

        The effective network access policy for the environment.

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

      - `packages: Packages{ npm, python, system_}`

        Packages installed in the environment.

        - `npm: Array[String]`

          npm packages installed globally in the environment.

        - `python: Array[String]`

          Python packages installed in the environment.

        - `system_: Array[String]`

          System packages installed in the environment.

      - `plugins: Array[HostedPlugin]`

        Plugins installed in the environment, excluding their archive contents.

        - `description: String`

          The installed plugin description.

        - `name: String`

          The installed plugin name.

        - `type: :inline`

          The type of the object. Always `inline`.

          - `:inline`

      - `skills: Array[HostedSkill]`

        Skills installed in the environment, excluding their archive contents.

        - `class HostedSkillReference`

          A skill installed from the Skills API.

          - `description: String`

            The installed skill description.

          - `name: String`

            The installed skill name.

          - `skill_id: String`

            The referenced skill ID.

          - `type: :skill_reference`

            The type of the object. Always `skill_reference`.

            - `:skill_reference`

          - `version: String`

            The concrete skill version installed for this session.

        - `class Inline`

          A skill installed from an inline ZIP archive.

          - `description: String`

            The installed skill description.

          - `name: String`

            The installed skill name.

          - `type: :inline`

            The type of the object. Always `inline`.

            - `:inline`

      - `type: :openai_hosted`

        The type of the object. Always `openai_hosted`.

        - `:openai_hosted`

      - `container_size: :small | :medium | :large`

        The effective CPU and memory tier, or null when unknown or outside the public tiers.

        - `:small`

        - `:medium`

        - `:large`

    - `class SelfHosted`

      An environment hosted by the application.

      - `id: String`

        The public ID of the environment.

      - `capability_directories: Array[String]`

        Directories that contain capabilities exposed to the agent.

      - `remote_url: String`

        Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

      - `type: :self_hosted`

        The type of the object. Always `self_hosted`.

        - `:self_hosted`

      - `workspace_directory: String`

        The absolute project directory inside the environment. Defaults to `/workspace`.

  - `error: String`

    The error that caused the session to fail, if any.

  - `last_active_at: Integer`

    The Unix timestamp, in seconds, when the session was last active.

  - `metadata: Hash[Symbol, String]`

    Custom string key-value pairs attached to the session.

  - `object: :"agent.session"`

    The object type. Always `agent.session`.

    - `:"agent.session"`

  - `required_actions: Array[ComputerUseApprovalRequest{ request, request_id, turn_id, type} | FunctionCall{ arguments, call_id, name, 2 more} | EnvironmentConnection{ environment_id, type}]`

    Actions that must be completed before the session can continue.

    - `class ComputerUseApprovalRequest`

      Respond to a computer-use request.

      - `request: BrowserAuthentication{ credential_origin, fields, options, 2 more} | BrowserOriginAccess{ origin, reason, type}`

        The information needed to render the request.

        - `class BrowserAuthentication`

          A registered form awaiting the application's response.

          - `credential_origin: String`

            The registered form or frame origin where values will be entered.

          - `fields: Array[Field{ id, label, required, type}]`

            Controls to render. All submitted values are sensitive.

            - `id: String`

              The field ID to submit as field_id in a fields entry.

            - `label: String`

              The label to display beside the control.

            - `required: bool`

              Whether this control requires a nonempty value.

            - `type: String`

              The rendering type, such as email, password, or text.

          - `options: Array[Option{ id, field_ids, label}]`

            Sign-in methods. Empty for a plain form.

            - `id: String`

              The option ID to submit as selected_option.

            - `field_ids: Array[String]`

              IDs from the registered fields that this method accepts.

            - `label: String`

              The method label to display.

          - `reason: String`

            Why the agent needs the user to sign in.

          - `type: :browser_authentication`

            The type of the object. Always `browser_authentication`.

            - `:browser_authentication`

        - `class BrowserOriginAccess`

          A browser origin awaiting the application's approval decision.

          - `origin: String`

            The origin the browser needs permission to access.

          - `reason: String`

            The browser's explanation for this request, or null when unavailable.

          - `type: :browser_origin_access`

            The type of the object. Always `browser_origin_access`.

            - `:browser_origin_access`

      - `request_id: String`

        The registered request ID to echo when responding.

      - `turn_id: String`

        The turn that requested approval.

      - `type: :computer_use_approval_request`

        The type of the object. Always `computer_use_approval_request`.

        - `:computer_use_approval_request`

    - `class FunctionCall`

      Run a function tool and submit its result.

      - `arguments: untyped`

        The arguments supplied by the model.

      - `call_id: String`

        The ID to include when submitting the function result.

      - `name: String`

        The function name.

      - `turn_id: String`

        The ID of the turn that requested the function call.

      - `type: :function_call`

        The type of the object. Always `function_call`.

        - `:function_call`

    - `class EnvironmentConnection`

      Reconnect a session environment.

      - `environment_id: String`

        The ID of the environment to reconnect.

      - `type: :environment_connection`

        The type of the object. Always `environment_connection`.

        - `:environment_connection`

  - `status: :idle | :in_progress | :requires_action | :failed`

    The current status of the session.

    - `:idle`

      The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

    - `:in_progress`

      The session is processing a turn.

    - `:requires_action`

      The session is waiting for one or more required actions.

    - `:failed`

      The session failed.

  - `usage: TokenUsage`

    Best-effort token usage for the session, or null if unknown. Recorded usage may change.

    - `input_tokens: Integer`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails{ cached_tokens}`

      A breakdown of the agent's input token usage.

      - `cached_tokens: Integer`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: Integer`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails{ reasoning_tokens}`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: Integer`

        The number of output tokens used for reasoning.

    - `total_tokens: Integer`

      The total number of input and output tokens used by the agent.

  - `vault_ids: Array[String]`

    The IDs of vaults made available to the session.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

agent_session = openai.beta.agents.sessions.retrieve("session_id")

puts(agent_session)
```

#### Response

```json
{
  "id": "id",
  "agent": {
    "id": "id",
    "instructions": "instructions",
    "model": "model",
    "multi_agent": {
      "enabled": true,
      "max_concurrent_subagents": 1
    },
    "name": "name",
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
        "type": "function"
      }
    ]
  },
  "created_at": 0,
  "environment": {
    "type": "none"
  },
  "error": "error",
  "last_active_at": 0,
  "metadata": {
    "foo": "string"
  },
  "object": "agent.session",
  "required_actions": [
    {
      "request": {
        "credential_origin": "credential_origin",
        "fields": [
          {
            "id": "id",
            "label": "label",
            "required": true,
            "type": "type"
          }
        ],
        "options": [
          {
            "id": "id",
            "field_ids": [
              "string"
            ],
            "label": "label"
          }
        ],
        "reason": "reason",
        "type": "browser_authentication"
      },
      "request_id": "request_id",
      "turn_id": "turn_id",
      "type": "computer_use_approval_request"
    }
  ],
  "status": "idle",
  "usage": {
    "input_tokens": 0,
    "input_tokens_details": {
      "cached_tokens": 0
    },
    "output_tokens": 0,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "total_tokens": 0
  },
  "vault_ids": [
    "string"
  ]
}
```

## Update an agent session

`beta.agents.sessions.update(session_id, **kwargs) -> AgentSession`

**post** `/agents/sessions/{session_id}`

Updates session metadata, model, reasoning effort, or service tier. Model settings apply to subsequent turns. Omitted fields are unchanged. See [managing sessions](/api/docs/guides/agents-api/sessions/manage).

### Parameters

- `session_id: String`

- `agent: Agent{ model, reasoning, service_tier}`

  Model settings for subsequent turns. Omitted fields stay unchanged.

  - `model: String`

    The model for subsequent turns. Omit to keep the current model.

  - `reasoning: Reasoning{ effort}`

    Reasoning settings to update. Omit to keep the current effort.

    - `effort: :none | :minimal | :low | 4 more`

      Omit to keep the current effort. Null selects the model's default effort.

      - `:none`

      - `:minimal`

      - `:low`

      - `:medium`

      - `:high`

      - `:xhigh`

      - `:max`

  - `service_tier: :auto | :default | :flex | 3 more`

    Omit to keep the current tier. Null resets it to auto.

    - `:auto`

      Selects the service tier automatically.

    - `:default`

      Uses the default service tier.

    - `:flex`

      Uses the flex service tier.

    - `:priority`

      Uses the priority service tier.

    - `:fast`

      Uses the fast service tier.

    - `:ultrafast`

      Uses the ultrafast service tier.

- `metadata: Hash[Symbol, String]`

  Replaces all metadata. Omit to leave unchanged, or pass null or {} to clear it. Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters.

### Returns

- `class AgentSession`

  A Managed Agents session.

  - `id: String`

    The ID of the session.

  - `agent: Agent{ id, instructions, model, 6 more}`

    The agent running in the session.

    - `id: String`

      The ID of the agent.

    - `instructions: String`

      Custom instructions appended to the agent's default base instructions.

    - `model: String`

      The model used by the agent.

    - `multi_agent: MultiAgentConfig`

      Configuration for creating and coordinating subagents.

      - `enabled: bool`

        Whether subagent tools are enabled. Defaults to false.

      - `max_concurrent_subagents: Integer`

        Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

    - `name: String`

      The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

    - `reasoning: AgentReasoning`

      The agent's reasoning configuration.

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

      The effective service-tier policy for model requests. Defaults to `auto`.

      - `:auto`

      - `:default`

      - `:flex`

      - `:priority`

      - `:fast`

      - `:ultrafast`

    - `text: AgentText`

      Configuration for text generated by the agent.

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

      Tools available to the agent.

      - `class Function`

        A function defined by the application.

        - `defer_loading: bool`

          Whether the function is deferred and discovered through tool search.

        - `description: String`

          A description of what the function does.

        - `name: String`

          The name of the function.

        - `parameters: Hash[Symbol, untyped]`

          A JSON Schema object describing the function's arguments.

        - `type: :function`

          The type of the object. Always `function`.

          - `:function`

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

        - `connection_origin: :service | :environment`

          Where outbound MCP HTTP connections originate.

          - `:service`

          - `:environment`

        - `credential_id: String`

          The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

        - `request_metadata: Hash[Symbol, untyped]`

          Metadata included with requests to this MCP server.

        - `required: bool`

          Whether this MCP server must initialize before the first turn.

        - `server_label: String`

          A label used to identify the MCP server in tool calls.

        - `transport: McpTransport`

          The transport used to connect to the MCP server.

          - `class HTTP`

            Connects to an MCP server over HTTP.

            - `server_url: String`

              The URL of the MCP server.

            - `type: :http`

              The type of the object. Always `http`.

              - `:http`

          - `class Stdio`

            Starts an MCP server as a local process.

            - `args: Array[String]`

              Arguments passed to the MCP server command.

            - `command: String`

              The command used to start the MCP server.

            - `cwd: String`

              The working directory used to start the MCP server.

            - `env_vars: Array[String]`

              Environment variable names inherited from the execution environment.

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

        - `context_size: :low | :medium | :high`

          The amount of search context made available to the model. Defaults to `medium`.

          - `:low`

          - `:medium`

          - `:high`

        - `location: Location{ city, country, region, timezone}`

          Approximate location used to localize search results, if provided.

          - `city: String`

            The city name.

          - `country: String`

            The two-letter ISO country code, such as `US`.

          - `region: String`

            The region or state name.

          - `timezone: String`

            The IANA timezone, such as `America/Los_Angeles`.

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

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the session was created.

  - `environment: Environment`

    The execution environment for the session.

    - `class None`

      The session talks to CCA without selecting or provisioning an execution environment.

      - `type: :none`

        The type of the object. Always `none`.

        - `:none`

    - `class OpenAIHosted`

      An environment hosted by OpenAI.

      - `id: String`

        The public ID of the environment.

      - `capability_directories: Array[String]`

        Directories that contain capabilities exposed to the agent.

      - `desktop: Desktop{ enabled}`

        The effective desktop configuration.

        - `enabled: bool`

          Whether the environment provisions a desktop and browser proxy.

      - `files: Array[HostedEnvironmentFile]`

        Files available in the environment, excluding their contents.

        - `class HostedEnvironmentFileID`

          A file copied from the OpenAI Files API.

          - `id: String`

            The session-scoped ID of the file in the execution environment.

          - `file_id: String`

            The ID of the uploaded file.

          - `path: String`

            The file's absolute path inside the environment.

          - `size_bytes: Integer`

            The decoded file size in bytes.

          - `type: :file_id`

            The type of the object. Always `file_id`.

            - `:file_id`

        - `class Inline`

          A file supplied inline when the session was created.

          - `id: String`

            The session-scoped ID of the file in the execution environment.

          - `path: String`

            The file's absolute path inside the environment.

          - `size_bytes: Integer`

            The decoded file size in bytes.

          - `type: :inline`

            The type of the object. Always `inline`.

            - `:inline`

      - `network: Network{ access, allowed_domains}`

        The effective network access policy for the environment.

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

      - `packages: Packages{ npm, python, system_}`

        Packages installed in the environment.

        - `npm: Array[String]`

          npm packages installed globally in the environment.

        - `python: Array[String]`

          Python packages installed in the environment.

        - `system_: Array[String]`

          System packages installed in the environment.

      - `plugins: Array[HostedPlugin]`

        Plugins installed in the environment, excluding their archive contents.

        - `description: String`

          The installed plugin description.

        - `name: String`

          The installed plugin name.

        - `type: :inline`

          The type of the object. Always `inline`.

          - `:inline`

      - `skills: Array[HostedSkill]`

        Skills installed in the environment, excluding their archive contents.

        - `class HostedSkillReference`

          A skill installed from the Skills API.

          - `description: String`

            The installed skill description.

          - `name: String`

            The installed skill name.

          - `skill_id: String`

            The referenced skill ID.

          - `type: :skill_reference`

            The type of the object. Always `skill_reference`.

            - `:skill_reference`

          - `version: String`

            The concrete skill version installed for this session.

        - `class Inline`

          A skill installed from an inline ZIP archive.

          - `description: String`

            The installed skill description.

          - `name: String`

            The installed skill name.

          - `type: :inline`

            The type of the object. Always `inline`.

            - `:inline`

      - `type: :openai_hosted`

        The type of the object. Always `openai_hosted`.

        - `:openai_hosted`

      - `container_size: :small | :medium | :large`

        The effective CPU and memory tier, or null when unknown or outside the public tiers.

        - `:small`

        - `:medium`

        - `:large`

    - `class SelfHosted`

      An environment hosted by the application.

      - `id: String`

        The public ID of the environment.

      - `capability_directories: Array[String]`

        Directories that contain capabilities exposed to the agent.

      - `remote_url: String`

        Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

      - `type: :self_hosted`

        The type of the object. Always `self_hosted`.

        - `:self_hosted`

      - `workspace_directory: String`

        The absolute project directory inside the environment. Defaults to `/workspace`.

  - `error: String`

    The error that caused the session to fail, if any.

  - `last_active_at: Integer`

    The Unix timestamp, in seconds, when the session was last active.

  - `metadata: Hash[Symbol, String]`

    Custom string key-value pairs attached to the session.

  - `object: :"agent.session"`

    The object type. Always `agent.session`.

    - `:"agent.session"`

  - `required_actions: Array[ComputerUseApprovalRequest{ request, request_id, turn_id, type} | FunctionCall{ arguments, call_id, name, 2 more} | EnvironmentConnection{ environment_id, type}]`

    Actions that must be completed before the session can continue.

    - `class ComputerUseApprovalRequest`

      Respond to a computer-use request.

      - `request: BrowserAuthentication{ credential_origin, fields, options, 2 more} | BrowserOriginAccess{ origin, reason, type}`

        The information needed to render the request.

        - `class BrowserAuthentication`

          A registered form awaiting the application's response.

          - `credential_origin: String`

            The registered form or frame origin where values will be entered.

          - `fields: Array[Field{ id, label, required, type}]`

            Controls to render. All submitted values are sensitive.

            - `id: String`

              The field ID to submit as field_id in a fields entry.

            - `label: String`

              The label to display beside the control.

            - `required: bool`

              Whether this control requires a nonempty value.

            - `type: String`

              The rendering type, such as email, password, or text.

          - `options: Array[Option{ id, field_ids, label}]`

            Sign-in methods. Empty for a plain form.

            - `id: String`

              The option ID to submit as selected_option.

            - `field_ids: Array[String]`

              IDs from the registered fields that this method accepts.

            - `label: String`

              The method label to display.

          - `reason: String`

            Why the agent needs the user to sign in.

          - `type: :browser_authentication`

            The type of the object. Always `browser_authentication`.

            - `:browser_authentication`

        - `class BrowserOriginAccess`

          A browser origin awaiting the application's approval decision.

          - `origin: String`

            The origin the browser needs permission to access.

          - `reason: String`

            The browser's explanation for this request, or null when unavailable.

          - `type: :browser_origin_access`

            The type of the object. Always `browser_origin_access`.

            - `:browser_origin_access`

      - `request_id: String`

        The registered request ID to echo when responding.

      - `turn_id: String`

        The turn that requested approval.

      - `type: :computer_use_approval_request`

        The type of the object. Always `computer_use_approval_request`.

        - `:computer_use_approval_request`

    - `class FunctionCall`

      Run a function tool and submit its result.

      - `arguments: untyped`

        The arguments supplied by the model.

      - `call_id: String`

        The ID to include when submitting the function result.

      - `name: String`

        The function name.

      - `turn_id: String`

        The ID of the turn that requested the function call.

      - `type: :function_call`

        The type of the object. Always `function_call`.

        - `:function_call`

    - `class EnvironmentConnection`

      Reconnect a session environment.

      - `environment_id: String`

        The ID of the environment to reconnect.

      - `type: :environment_connection`

        The type of the object. Always `environment_connection`.

        - `:environment_connection`

  - `status: :idle | :in_progress | :requires_action | :failed`

    The current status of the session.

    - `:idle`

      The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

    - `:in_progress`

      The session is processing a turn.

    - `:requires_action`

      The session is waiting for one or more required actions.

    - `:failed`

      The session failed.

  - `usage: TokenUsage`

    Best-effort token usage for the session, or null if unknown. Recorded usage may change.

    - `input_tokens: Integer`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails{ cached_tokens}`

      A breakdown of the agent's input token usage.

      - `cached_tokens: Integer`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: Integer`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails{ reasoning_tokens}`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: Integer`

        The number of output tokens used for reasoning.

    - `total_tokens: Integer`

      The total number of input and output tokens used by the agent.

  - `vault_ids: Array[String]`

    The IDs of vaults made available to the session.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

agent_session = openai.beta.agents.sessions.update("session_id")

puts(agent_session)
```

#### Response

```json
{
  "id": "id",
  "agent": {
    "id": "id",
    "instructions": "instructions",
    "model": "model",
    "multi_agent": {
      "enabled": true,
      "max_concurrent_subagents": 1
    },
    "name": "name",
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
        "type": "function"
      }
    ]
  },
  "created_at": 0,
  "environment": {
    "type": "none"
  },
  "error": "error",
  "last_active_at": 0,
  "metadata": {
    "foo": "string"
  },
  "object": "agent.session",
  "required_actions": [
    {
      "request": {
        "credential_origin": "credential_origin",
        "fields": [
          {
            "id": "id",
            "label": "label",
            "required": true,
            "type": "type"
          }
        ],
        "options": [
          {
            "id": "id",
            "field_ids": [
              "string"
            ],
            "label": "label"
          }
        ],
        "reason": "reason",
        "type": "browser_authentication"
      },
      "request_id": "request_id",
      "turn_id": "turn_id",
      "type": "computer_use_approval_request"
    }
  ],
  "status": "idle",
  "usage": {
    "input_tokens": 0,
    "input_tokens_details": {
      "cached_tokens": 0
    },
    "output_tokens": 0,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "total_tokens": 0
  },
  "vault_ids": [
    "string"
  ]
}
```

# Artifacts

## Retrieve agent session artifact content

`beta.agents.sessions.artifacts.content(artifact_id, **kwargs) -> StringIO`

**get** `/agents/sessions/{session_id}/artifacts/{artifact_id}/content`

Downloads immutable session artifact bytes after the execution environment expires. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `session_id: String`

- `artifact_id: String`

### Returns

- `StringIO`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

response = openai.beta.agents.sessions.artifacts.content("artifact_id", session_id: "session_id")

puts(response)
```

## Delete an agent session artifact

`beta.agents.sessions.artifacts.delete(artifact_id, **kwargs) -> SessionArtifactDeleted`

**delete** `/agents/sessions/{session_id}/artifacts/{artifact_id}`

Deletes an immutable session artifact without deleting its live environment file or original Files API object. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `session_id: String`

- `artifact_id: String`

### Returns

- `class SessionArtifactDeleted`

  Confirmation that an immutable session artifact was deleted.

  - `id: String`

    The ID of the deleted session artifact.

  - `deleted: bool`

    Whether the session artifact was deleted. Always `true`.

  - `object: :"agent.session.artifact.deleted"`

    The object type. Always `agent.session.artifact.deleted`.

    - `:"agent.session.artifact.deleted"`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

session_artifact_deleted = openai.beta.agents.sessions.artifacts.delete("artifact_id", session_id: "session_id")

puts(session_artifact_deleted)
```

#### Response

```json
{
  "id": "id",
  "deleted": true,
  "object": "agent.session.artifact.deleted"
}
```

## List agent session artifacts

`beta.agents.sessions.artifacts.list(session_id, **kwargs) -> CursorPage<SessionArtifact>`

**get** `/agents/sessions/{session_id}/artifacts`

Lists immutable artifacts published by completed hosted session turns. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `session_id: String`

- `after: String`

  Return artifacts after this immutable artifact ID.

- `environment_id: String`

  Restrict the listing to artifacts produced by this environment.

- `limit: Integer`

  The maximum number of artifacts to return, between 1 and 100.

- `order: :asc | :desc`

  Sort by creation time and ID. Defaults to descending.

  - `:asc`

    Returns resources in ascending order.

  - `:desc`

    Returns resources in descending order.

### Returns

- `class SessionArtifact`

  An immutable file published by a completed hosted session turn.

  - `id: String`

    The immutable artifact ID.

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the artifact was published.

  - `environment_id: String`

    The ID of the environment that produced the artifact.

  - `object: :"agent.session.artifact"`

    The object type. Always `agent.session.artifact`.

    - `:"agent.session.artifact"`

  - `path: String`

    The original absolute file path in the execution environment.

  - `session_id: String`

    The ID of the session that owns the artifact.

  - `size_bytes: Integer`

    The immutable artifact size in bytes.

  - `turn_id: String`

    The ID of the completed turn that published the artifact.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.beta.agents.sessions.artifacts.list("session_id")

puts(page)
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "created_at": 0,
      "environment_id": "environment_id",
      "object": "agent.session.artifact",
      "path": "path",
      "session_id": "session_id",
      "size_bytes": 0,
      "turn_id": "turn_id"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve an agent session artifact

`beta.agents.sessions.artifacts.retrieve(artifact_id, **kwargs) -> SessionArtifact`

**get** `/agents/sessions/{session_id}/artifacts/{artifact_id}`

Retrieves immutable metadata for one durable session artifact. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `session_id: String`

- `artifact_id: String`

### Returns

- `class SessionArtifact`

  An immutable file published by a completed hosted session turn.

  - `id: String`

    The immutable artifact ID.

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the artifact was published.

  - `environment_id: String`

    The ID of the environment that produced the artifact.

  - `object: :"agent.session.artifact"`

    The object type. Always `agent.session.artifact`.

    - `:"agent.session.artifact"`

  - `path: String`

    The original absolute file path in the execution environment.

  - `session_id: String`

    The ID of the session that owns the artifact.

  - `size_bytes: Integer`

    The immutable artifact size in bytes.

  - `turn_id: String`

    The ID of the completed turn that published the artifact.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

session_artifact = openai.beta.agents.sessions.artifacts.retrieve("artifact_id", session_id: "session_id")

puts(session_artifact)
```

#### Response

```json
{
  "id": "id",
  "created_at": 0,
  "environment_id": "environment_id",
  "object": "agent.session.artifact",
  "path": "path",
  "session_id": "session_id",
  "size_bytes": 0,
  "turn_id": "turn_id"
}
```

## Domain Types

### Session Artifact

- `class SessionArtifact`

  An immutable file published by a completed hosted session turn.

  - `id: String`

    The immutable artifact ID.

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the artifact was published.

  - `environment_id: String`

    The ID of the environment that produced the artifact.

  - `object: :"agent.session.artifact"`

    The object type. Always `agent.session.artifact`.

    - `:"agent.session.artifact"`

  - `path: String`

    The original absolute file path in the execution environment.

  - `session_id: String`

    The ID of the session that owns the artifact.

  - `size_bytes: Integer`

    The immutable artifact size in bytes.

  - `turn_id: String`

    The ID of the completed turn that published the artifact.

### Session Artifact Deleted

- `class SessionArtifactDeleted`

  Confirmation that an immutable session artifact was deleted.

  - `id: String`

    The ID of the deleted session artifact.

  - `deleted: bool`

    Whether the session artifact was deleted. Always `true`.

  - `object: :"agent.session.artifact.deleted"`

    The object type. Always `agent.session.artifact.deleted`.

    - `:"agent.session.artifact.deleted"`

# Events

## Create agent session input events

`beta.agents.sessions.events.create(session_id, **kwargs) -> void`

**post** `/agents/sessions/{session_id}/events`

Submits message, cancellation, tool-result, or computer-use approval-response events to a managed agent session. Cancellation can recover a still-open turn whose backend execution has ended by marking it cancelled and abandoning unpublished outputs. Saved results, published files, and existing terminal outcomes are preserved. HTTP 202 confirms acceptance, not durable completion. See [session events](/api/docs/guides/agents-api/sessions/events).

### Parameters

- `session_id: String`

- `events: Array[AgentSessionInputParam]`

  The input events to submit to the session.

  - `class AgentSessionInputComputerUseApprovalRequestResult`

    Responds to a pending Computer Use approval request.

    - `request_id: String`

      The registered request ID from the required action.

    - `response: AgentBrowserAuthenticationSubmitParam | AgentBrowserAuthenticationCancelParam | AgentBrowserOriginAccessParam`

      The response for this request type.

      - `class AgentBrowserAuthenticationSubmitParam`

        - `action: :submit`

          - `:submit`

        - `fields: Array[Field{ field_id, value}]`

          Values for up to six active fields in the required action. The submitted field-value mapping and selected option must fit within 120 KiB of JSON.

          - `field_id: String`

            The field ID from the required action.

          - `value: String`

            The value to enter into the registered control.

        - `type: :browser_authentication`

          - `:browser_authentication`

        - `selected_option: String`

          The chosen method. Required when the required action contains options.

      - `class AgentBrowserAuthenticationCancelParam`

        - `action: :cancel`

          - `:cancel`

        - `type: :browser_authentication`

          - `:browser_authentication`

      - `class AgentBrowserOriginAccessParam`

        - `decision: :approve | :deny | :cancel`

          Whether to allow, deny, or cancel the requested origin access.

          - `:approve`

            Allow the browser to access this origin.

          - `:deny`

            Deny access to this origin.

          - `:cancel`

            Dismiss this request without approving access.

        - `type: :browser_origin_access`

          - `:browser_origin_access`

    - `type: :"agent.session.input.computer_use_approval_request_result"`

      The type of the object. Always `agent.session.input.computer_use_approval_request_result`.

      - `:"agent.session.input.computer_use_approval_request_result"`

  - `class AgentSessionInputMessage`

    Adds one or more user messages and starts a turn.

    - `input: Array[AgentSessionInputMessageParam]`

      The user messages to add to the session.

      - `content: Array[InputContentParam]`

        The content of the message.

        - `class InputText`

          Text input to the model.

          - `text: String`

            The text sent to the model.

          - `type: :input_text`

            The type of the object. Always `input_text`.

            - `:input_text`

        - `class InputImage`

          Image input to the model.

          - `image_url: String`

            The URL of the image sent to the model.

          - `type: :input_image`

            The type of the object. Always `input_image`.

            - `:input_image`

      - `role: :user`

        The role of the message author. Always `user`.

        - `:user`

      - `type: :message`

        The type of the input item. Always `message`.

        - `:message`

    - `type: :"agent.session.input.message"`

      The type of the object. Always `agent.session.input.message`.

      - `:"agent.session.input.message"`

  - `class AgentSessionInputCancel`

    Cancels the session's active turn.

    - `type: :"agent.session.input.cancel"`

      The type of the object. Always `agent.session.input.cancel`.

      - `:"agent.session.input.cancel"`

  - `class AgentSessionInputToolResult`

    Submits the result of a function call.

    - `call_id: String`

      The ID of the function call.

    - `success: bool`

      Whether the function call succeeded.

    - `turn_id: String`

      The ID of the turn that requested the function call.

    - `type: :"agent.session.input.tool_result"`

      The type of the object. Always `agent.session.input.tool_result`.

      - `:"agent.session.input.tool_result"`

    - `error: String`

      The error message when the call failed.

    - `output: AgentFunctionCallOutputParam`

      The function result when the call succeeded.

      - `String = String`

      - `UnionMember1 = Array[InputContentParam]`

        - `class InputText`

          Text input to the model.

        - `class InputImage`

          Image input to the model.

- `idempotency_key: String`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

result = openai.beta.agents.sessions.events.create(
  "session_id",
  events: [
    {
      request_id: "request_id",
      response: {action: "submit", fields: [{field_id: "field_id", value: "value"}], type: :browser_authentication},
      type: :"agent.session.input.computer_use_approval_request_result"
    }
  ]
)

puts(result)
```

## Stream agent session events

`beta.agents.sessions.events.stream(session_id) -> AgentSessionEvent`

**get** `/agents/sessions/{session_id}/events`

Streams live events for an agent session. See [session events](/api/docs/guides/agents-api/sessions/events).

### Parameters

- `session_id: String`

### Returns

- `AgentSessionEvent = AgentSessionErrorEvent | AgentSessionEnvironmentReadyEvent | AgentSessionEnvironmentResetEvent | 28 more`

  An event emitted by a Managed Agents session.

  - `class AgentSessionErrorEvent`

    Emitted when a turn or session fails.

    - `error: SessionError`

      The error that occurred.

      - `code: String`

        The machine-readable error code, if any.

      - `message: String`

        A customer-safe explanation of the error.

      - `param: String`

        The request parameter associated with the error, if any.

      - `type: String`

        The error type.

    - `event_id: String`

      The unique ID of the event.

    - `session_id: String`

      The ID of the session associated with the event.

    - `type: :error`

      The type of the object. Always `error`.

      - `:error`

  - `class AgentSessionEnvironmentReadyEvent`

    Emitted when a hosted session environment is ready to connect.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

      - `id: String`

        The public ID of the environment.

      - `error: Error{ code, message, type}`

        The error reported while preparing the environment, if any.

        - `code: String`

          A machine-readable error code.

        - `message: String`

          A human-readable error message.

        - `type: String`

          The error type.

      - `status: :pending | :ready | :connected | 2 more`

        The environment's connection status.

        - `:pending`

          The environment is being prepared.

        - `:ready`

          The environment is ready to connect.

        - `:connected`

          The environment is connected.

        - `:disconnected`

          The environment is disconnected.

        - `:failed`

          The environment failed to connect.

      - `type: String`

        The environment type.

    - `event_id: String`

      The unique ID of the event.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.environment.ready"`

      The type of the object. Always `agent.session.environment.ready`.

      - `:"agent.session.environment.ready"`

  - `class AgentSessionEnvironmentResetEvent`

    Emitted after a hosted sandbox is replaced. Conversation history survives; changes to the previous sandbox's files and processes do not.

    - `environment_id: String`

      The stable environment ID, retained across sandbox replacements.

    - `event_id: String`

      The unique ID of the event.

    - `reset_count: Integer`

      Monotonically increasing reset number. Repeated notifications share this number.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The associated turn, when applicable.

    - `type: :"agent.session.environment.reset"`

      The type of the object. Always `agent.session.environment.reset`.

      - `:"agent.session.environment.reset"`

  - `class AgentOutputCommandExecutionOutputDeltaEvent`

    Emitted when command execution produces an output delta.

    - `delta: String`

      The output text that was appended.

    - `event_id: String`

      The unique ID of the event.

    - `item_id: String`

      The ID of the command execution item.

    - `output_index: Integer`

      The index of the item in the turn output.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.output.command_execution_output.delta"`

      The type of the object. Always `agent.output.command_execution_output.delta`.

      - `:"agent.output.command_execution_output.delta"`

  - `class AgentSessionCreatedEvent`

    Emitted when a session is created.

    - `event_id: String`

      The unique ID of the event.

    - `session: AgentSession`

      The session that was created.

      - `id: String`

        The ID of the session.

      - `agent: Agent{ id, instructions, model, 6 more}`

        The agent running in the session.

        - `id: String`

          The ID of the agent.

        - `instructions: String`

          Custom instructions appended to the agent's default base instructions.

        - `model: String`

          The model used by the agent.

        - `multi_agent: MultiAgentConfig`

          Configuration for creating and coordinating subagents.

          - `enabled: bool`

            Whether subagent tools are enabled. Defaults to false.

          - `max_concurrent_subagents: Integer`

            Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

        - `name: String`

          The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

        - `reasoning: AgentReasoning`

          The agent's reasoning configuration.

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

          The effective service-tier policy for model requests. Defaults to `auto`.

          - `:auto`

          - `:default`

          - `:flex`

          - `:priority`

          - `:fast`

          - `:ultrafast`

        - `text: AgentText`

          Configuration for text generated by the agent.

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

          Tools available to the agent.

          - `class Function`

            A function defined by the application.

            - `defer_loading: bool`

              Whether the function is deferred and discovered through tool search.

            - `description: String`

              A description of what the function does.

            - `name: String`

              The name of the function.

            - `parameters: Hash[Symbol, untyped]`

              A JSON Schema object describing the function's arguments.

            - `type: :function`

              The type of the object. Always `function`.

              - `:function`

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

            - `connection_origin: :service | :environment`

              Where outbound MCP HTTP connections originate.

              - `:service`

              - `:environment`

            - `credential_id: String`

              The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

            - `request_metadata: Hash[Symbol, untyped]`

              Metadata included with requests to this MCP server.

            - `required: bool`

              Whether this MCP server must initialize before the first turn.

            - `server_label: String`

              A label used to identify the MCP server in tool calls.

            - `transport: McpTransport`

              The transport used to connect to the MCP server.

              - `class HTTP`

                Connects to an MCP server over HTTP.

                - `server_url: String`

                  The URL of the MCP server.

                - `type: :http`

                  The type of the object. Always `http`.

                  - `:http`

              - `class Stdio`

                Starts an MCP server as a local process.

                - `args: Array[String]`

                  Arguments passed to the MCP server command.

                - `command: String`

                  The command used to start the MCP server.

                - `cwd: String`

                  The working directory used to start the MCP server.

                - `env_vars: Array[String]`

                  Environment variable names inherited from the execution environment.

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

            - `context_size: :low | :medium | :high`

              The amount of search context made available to the model. Defaults to `medium`.

              - `:low`

              - `:medium`

              - `:high`

            - `location: Location{ city, country, region, timezone}`

              Approximate location used to localize search results, if provided.

              - `city: String`

                The city name.

              - `country: String`

                The two-letter ISO country code, such as `US`.

              - `region: String`

                The region or state name.

              - `timezone: String`

                The IANA timezone, such as `America/Los_Angeles`.

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

      - `created_at: Integer`

        The Unix timestamp, in seconds, when the session was created.

      - `environment: Environment`

        The execution environment for the session.

        - `class None`

          The session talks to CCA without selecting or provisioning an execution environment.

          - `type: :none`

            The type of the object. Always `none`.

            - `:none`

        - `class OpenAIHosted`

          An environment hosted by OpenAI.

          - `id: String`

            The public ID of the environment.

          - `capability_directories: Array[String]`

            Directories that contain capabilities exposed to the agent.

          - `desktop: Desktop{ enabled}`

            The effective desktop configuration.

            - `enabled: bool`

              Whether the environment provisions a desktop and browser proxy.

          - `files: Array[HostedEnvironmentFile]`

            Files available in the environment, excluding their contents.

            - `class HostedEnvironmentFileID`

              A file copied from the OpenAI Files API.

              - `id: String`

                The session-scoped ID of the file in the execution environment.

              - `file_id: String`

                The ID of the uploaded file.

              - `path: String`

                The file's absolute path inside the environment.

              - `size_bytes: Integer`

                The decoded file size in bytes.

              - `type: :file_id`

                The type of the object. Always `file_id`.

                - `:file_id`

            - `class Inline`

              A file supplied inline when the session was created.

              - `id: String`

                The session-scoped ID of the file in the execution environment.

              - `path: String`

                The file's absolute path inside the environment.

              - `size_bytes: Integer`

                The decoded file size in bytes.

              - `type: :inline`

                The type of the object. Always `inline`.

                - `:inline`

          - `network: Network{ access, allowed_domains}`

            The effective network access policy for the environment.

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

          - `packages: Packages{ npm, python, system_}`

            Packages installed in the environment.

            - `npm: Array[String]`

              npm packages installed globally in the environment.

            - `python: Array[String]`

              Python packages installed in the environment.

            - `system_: Array[String]`

              System packages installed in the environment.

          - `plugins: Array[HostedPlugin]`

            Plugins installed in the environment, excluding their archive contents.

            - `description: String`

              The installed plugin description.

            - `name: String`

              The installed plugin name.

            - `type: :inline`

              The type of the object. Always `inline`.

              - `:inline`

          - `skills: Array[HostedSkill]`

            Skills installed in the environment, excluding their archive contents.

            - `class HostedSkillReference`

              A skill installed from the Skills API.

              - `description: String`

                The installed skill description.

              - `name: String`

                The installed skill name.

              - `skill_id: String`

                The referenced skill ID.

              - `type: :skill_reference`

                The type of the object. Always `skill_reference`.

                - `:skill_reference`

              - `version: String`

                The concrete skill version installed for this session.

            - `class Inline`

              A skill installed from an inline ZIP archive.

              - `description: String`

                The installed skill description.

              - `name: String`

                The installed skill name.

              - `type: :inline`

                The type of the object. Always `inline`.

                - `:inline`

          - `type: :openai_hosted`

            The type of the object. Always `openai_hosted`.

            - `:openai_hosted`

          - `container_size: :small | :medium | :large`

            The effective CPU and memory tier, or null when unknown or outside the public tiers.

            - `:small`

            - `:medium`

            - `:large`

        - `class SelfHosted`

          An environment hosted by the application.

          - `id: String`

            The public ID of the environment.

          - `capability_directories: Array[String]`

            Directories that contain capabilities exposed to the agent.

          - `remote_url: String`

            Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

          - `type: :self_hosted`

            The type of the object. Always `self_hosted`.

            - `:self_hosted`

          - `workspace_directory: String`

            The absolute project directory inside the environment. Defaults to `/workspace`.

      - `error: String`

        The error that caused the session to fail, if any.

      - `last_active_at: Integer`

        The Unix timestamp, in seconds, when the session was last active.

      - `metadata: Hash[Symbol, String]`

        Custom string key-value pairs attached to the session.

      - `object: :"agent.session"`

        The object type. Always `agent.session`.

        - `:"agent.session"`

      - `required_actions: Array[ComputerUseApprovalRequest{ request, request_id, turn_id, type} | FunctionCall{ arguments, call_id, name, 2 more} | EnvironmentConnection{ environment_id, type}]`

        Actions that must be completed before the session can continue.

        - `class ComputerUseApprovalRequest`

          Respond to a computer-use request.

          - `request: BrowserAuthentication{ credential_origin, fields, options, 2 more} | BrowserOriginAccess{ origin, reason, type}`

            The information needed to render the request.

            - `class BrowserAuthentication`

              A registered form awaiting the application's response.

              - `credential_origin: String`

                The registered form or frame origin where values will be entered.

              - `fields: Array[Field{ id, label, required, type}]`

                Controls to render. All submitted values are sensitive.

                - `id: String`

                  The field ID to submit as field_id in a fields entry.

                - `label: String`

                  The label to display beside the control.

                - `required: bool`

                  Whether this control requires a nonempty value.

                - `type: String`

                  The rendering type, such as email, password, or text.

              - `options: Array[Option{ id, field_ids, label}]`

                Sign-in methods. Empty for a plain form.

                - `id: String`

                  The option ID to submit as selected_option.

                - `field_ids: Array[String]`

                  IDs from the registered fields that this method accepts.

                - `label: String`

                  The method label to display.

              - `reason: String`

                Why the agent needs the user to sign in.

              - `type: :browser_authentication`

                The type of the object. Always `browser_authentication`.

                - `:browser_authentication`

            - `class BrowserOriginAccess`

              A browser origin awaiting the application's approval decision.

              - `origin: String`

                The origin the browser needs permission to access.

              - `reason: String`

                The browser's explanation for this request, or null when unavailable.

              - `type: :browser_origin_access`

                The type of the object. Always `browser_origin_access`.

                - `:browser_origin_access`

          - `request_id: String`

            The registered request ID to echo when responding.

          - `turn_id: String`

            The turn that requested approval.

          - `type: :computer_use_approval_request`

            The type of the object. Always `computer_use_approval_request`.

            - `:computer_use_approval_request`

        - `class FunctionCall`

          Run a function tool and submit its result.

          - `arguments: untyped`

            The arguments supplied by the model.

          - `call_id: String`

            The ID to include when submitting the function result.

          - `name: String`

            The function name.

          - `turn_id: String`

            The ID of the turn that requested the function call.

          - `type: :function_call`

            The type of the object. Always `function_call`.

            - `:function_call`

        - `class EnvironmentConnection`

          Reconnect a session environment.

          - `environment_id: String`

            The ID of the environment to reconnect.

          - `type: :environment_connection`

            The type of the object. Always `environment_connection`.

            - `:environment_connection`

      - `status: :idle | :in_progress | :requires_action | :failed`

        The current status of the session.

        - `:idle`

          The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

        - `:in_progress`

          The session is processing a turn.

        - `:requires_action`

          The session is waiting for one or more required actions.

        - `:failed`

          The session failed.

      - `usage: TokenUsage`

        Best-effort token usage for the session, or null if unknown. Recorded usage may change.

        - `input_tokens: Integer`

          The number of input tokens used by the agent.

        - `input_tokens_details: InputTokensDetails{ cached_tokens}`

          A breakdown of the agent's input token usage.

          - `cached_tokens: Integer`

            The number of input tokens retrieved from the prompt cache.

        - `output_tokens: Integer`

          The number of output tokens generated by the agent.

        - `output_tokens_details: OutputTokensDetails{ reasoning_tokens}`

          A breakdown of the agent's output token usage.

          - `reasoning_tokens: Integer`

            The number of output tokens used for reasoning.

        - `total_tokens: Integer`

          The total number of input and output tokens used by the agent.

      - `vault_ids: Array[String]`

        The IDs of vaults made available to the session.

    - `type: :"agent.session.created"`

      The type of the object. Always `agent.session.created`.

      - `:"agent.session.created"`

  - `class AgentSessionTurnCreatedEvent`

    Emitted when a turn is created.

    - `event_id: String`

      The unique ID of the event.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn: Turn`

      The turn at the time it was created.

      - `id: String`

        The ID of the turn.

      - `agent_id: String`

        The ID of the agent that ran the turn.

      - `completed_at: Integer`

        The Unix timestamp, in seconds, when the turn reached a terminal state.

      - `created_at: Integer`

        The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

      - `error: SessionTurnError`

        A customer-safe error. Non-null only for a failed turn.

        - `code: :context_length_exceeded | :session_budget_exceeded | :usage_limit_exceeded | 16 more`

          A stable, machine-readable failure category.

          - `:context_length_exceeded`

            The request exceeds the model's context window.

          - `:session_budget_exceeded`

            The session has reached its usage budget.

          - `:usage_limit_exceeded`

            The organization has reached a usage, plan, or billing limit.

          - `:credit_balance_exhausted`

            The organization has no API credits remaining.

          - `:rate_limit_exceeded`

            The request exceeds the available rate limit.

          - `:flex_unavailable`

            Flex processing is temporarily unavailable.

          - `:server_overloaded`

            The model service is temporarily overloaded.

          - `:cyber_policy`

            The request was rejected by a safety policy.

          - `:misalignment_policy_violation`

            The request was blocked by the safety systems.

          - `:connection_failed`

            The request could not connect to the model service.

          - `:server_error`

            The model service encountered an unexpected error.

          - `:authentication_error`

            The API credentials are invalid or lack the required access.

          - `:invalid_request`

            The request contains invalid input or configuration.

          - `:resource_not_found`

            The requested model or resource is unavailable.

          - `:sandbox_error`

            The request could not complete in its execution environment.

          - `:executor_version_incompatible`

            The executor must be upgraded before it can run this turn.

          - `:active_turn_not_steerable`

            The session cannot accept additional input while a request is running.

          - `:request_timeout`

            The request timed out before the model service responded.

          - `:internal_error`

            An unexpected internal error prevented the session request from completing.

        - `message: String`

          A customer-safe explanation of the failure.

      - `object: :"agent.session.turn"`

        The object type. Always `agent.session.turn`.

        - `:"agent.session.turn"`

      - `session_id: String`

        The ID of the session that owns the turn.

      - `started_at: Integer`

        The Unix timestamp, in seconds, when the turn started.

      - `status: :queued | :in_progress | :waiting | 3 more`

        The current status of the turn.

        - `:queued`

          The turn is waiting to start.

        - `:in_progress`

          The turn is in progress.

        - `:waiting`

          The turn is waiting for external input.

        - `:completed`

          The turn completed successfully.

        - `:failed`

          The turn failed.

        - `:cancelled`

          The turn was cancelled.

      - `subagent_id: String`

        The ID of the subagent that ran the turn, if applicable.

      - `usage: TokenUsage`

        Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `turn_id: String`

      The ID of the turn associated with the event.

    - `type: :"agent.session.turn.created"`

      The type of the object. Always `agent.session.turn.created`.

      - `:"agent.session.turn.created"`

  - `class AgentSessionTurnInProgressEvent`

    Emitted when a turn starts running.

    - `event_id: String`

      The unique ID of the event.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn: Turn`

      The turn at the time it started running.

    - `turn_id: String`

      The ID of the turn associated with the event.

    - `type: :"agent.session.turn.in_progress"`

      The type of the object. Always `agent.session.turn.in_progress`.

      - `:"agent.session.turn.in_progress"`

  - `class AgentSessionTurnCompletedEvent`

    Emitted when a turn completes.

    - `event_id: String`

      The unique ID of the event.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn: Turn`

      The completed turn.

    - `turn_id: String`

      The ID of the turn associated with the event.

    - `type: :"agent.session.turn.completed"`

      The type of the object. Always `agent.session.turn.completed`.

      - `:"agent.session.turn.completed"`

    - `usage: TokenUsage`

      Token usage by the root agent during the turn, when available.

  - `class AgentSessionTurnFailedEvent`

    Emitted when a turn fails.

    - `event_id: String`

      The unique ID of the event.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn: Turn`

      The failed turn.

    - `turn_id: String`

      The ID of the turn associated with the event.

    - `type: :"agent.session.turn.failed"`

      The type of the object. Always `agent.session.turn.failed`.

      - `:"agent.session.turn.failed"`

    - `usage: TokenUsage`

      Token usage by the root agent during the turn, when available.

  - `class AgentSessionTurnCancelledEvent`

    Emitted when a turn is cancelled.

    - `event_id: String`

      The unique ID of the event.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn: Turn`

      The cancelled turn.

    - `turn_id: String`

      The ID of the turn associated with the event.

    - `type: :"agent.session.turn.cancelled"`

      The type of the object. Always `agent.session.turn.cancelled`.

      - `:"agent.session.turn.cancelled"`

    - `usage: TokenUsage`

      Token usage by the root agent during the turn, when available.

  - `class AgentSessionTurnItemAddedEvent`

    Emitted when an item is added to a turn.

    - `event_id: String`

      The unique ID of the event.

    - `item: AgentSessionItem`

      The item that was added.

      - `class AgentSessionMessage`

        A user or assistant message recorded in a session.

        - `id: String`

          The ID of this item, or null for legacy user messages whose ID was not recorded.

        - `content: Array[AgentSessionMessageContent]`

          The content of the message. User messages contain input text or images; assistant messages contain output text.

          - `class InputText`

            Text supplied by the user.

            - `text: String`

              The text supplied by the user.

            - `type: :input_text`

              The type of the object. Always `input_text`.

              - `:input_text`

          - `class InputImage`

            An image supplied by the user.

            - `image_url: String`

              The URL of the image supplied by the user, which may be a base64-encoded data URL.

            - `type: :input_image`

              The type of the object. Always `input_image`.

              - `:input_image`

          - `class OutputText`

            Text produced by the assistant.

            - `text: String`

              The text produced by the assistant.

            - `type: :output_text`

              The type of the object. Always `output_text`.

              - `:output_text`

        - `phase: :commentary | :final_answer`

          The phase of an assistant message. Null for user messages.

          - `:commentary`

            Commentary produced while the agent works.

          - `:final_answer`

            The agent's final answer.

        - `role: :user | :assistant`

          The role of the message author.

          - `:user`

          - `:assistant`

        - `status: AgentOutputItemStatus`

          The status of the message. User messages are always `completed`.

          - `:in_progress`

            The item is in progress.

          - `:completed`

            The item is complete.

          - `:incomplete`

            The item stopped before completing.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :message`

          The item type. Always `message`.

          - `:message`

      - `class AgentReasoningItem`

        A reasoning item produced by the agent.

        - `id: String`

          The ID of the reasoning item.

        - `status: AgentOutputItemStatus`

          The status of the reasoning item.

        - `summary: Array[SummaryText]`

          The reasoning summaries produced by the agent.

          - `text: String`

            The reasoning summary text.

          - `type: :summary_text`

            The content type. Always `summary_text`.

            - `:summary_text`

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :reasoning`

          The item type. Always `reasoning`.

          - `:reasoning`

      - `class AgentFunctionCallItem`

        A function call produced by the agent.

        - `id: String`

          The ID of the function call item.

        - `arguments: untyped`

          The arguments to pass to the function.

        - `call_id: String`

          The ID used to submit the function result.

        - `name: String`

          The name of the function to call.

        - `status: AgentFunctionCallStatus`

          The status of the function call.

          - `:in_progress`

            The call is in progress.

          - `:completed`

            The call completed successfully.

          - `:failed`

            The call failed.

          - `:incomplete`

            The call stopped before completing.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :function_call`

          The item type. Always `function_call`.

          - `:function_call`

      - `class FunctionCallOutput`

        The result supplied for a function call.

        - `id: String`

          The ID of the function call output item.

        - `call_id: String`

          The ID of the function call that produced this output.

        - `error: String`

          The error message, if the call failed.

        - `output: AgentFunctionCallOutput`

          The function result, if the call succeeded.

          - `String = String`

          - `UnionMember1 = Array[InputContent]`

            - `class InputText`

              Text input recorded in a session item.

              - `text: String`

                The text supplied to the agent.

              - `type: :input_text`

                The type of the object. Always `input_text`.

                - `:input_text`

            - `class InputImage`

              Image input recorded in a session item.

              - `image_url: String`

                The URL of the image supplied to the agent, which may be a base64-encoded data URL.

              - `type: :input_image`

                The type of the object. Always `input_image`.

                - `:input_image`

        - `status: AgentFunctionCallStatus`

          The status of the function call.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :function_call_output`

          The item type. Always `function_call_output`.

          - `:function_call_output`

      - `class AgentMessage`

        A message exchanged between agent threads.

        - `id: String`

          The ID of the message.

        - `content: Array[AgentContent]`

          The content exchanged between the agents.

          - `class OutputText`

            A text content part produced by the agent.

            - `text: String`

              The text produced by the agent.

            - `type: :output_text`

              The content type. Always `output_text`.

              - `:output_text`

          - `class EncryptedContent`

            Encrypted content exchanged between agents.

            - `encrypted_content: String`

              The encrypted content payload.

            - `type: :encrypted_content`

              The content type. Always `encrypted_content`.

              - `:encrypted_content`

        - `recipient_agent_id: String`

          The ID or name of the receiving agent.

        - `sender_agent_id: String`

          The ID or name of the sending agent.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :agent_message`

          The item type. Always `agent_message`.

          - `:agent_message`

      - `class AgentMcpCallItem`

        A call to a tool on an MCP server.

        - `id: String`

          The ID of the MCP call item.

        - `arguments: untyped`

          The arguments passed to the MCP tool.

        - `error: untyped`

          The error returned by the MCP tool, if any.

        - `name: String`

          The name of the MCP tool.

        - `output: untyped`

          The output returned by the MCP tool, if any.

        - `server_label: String`

          The label of the MCP server.

        - `status: AgentFunctionCallStatus`

          The status of the MCP tool call.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :mcp_call`

          The item type. Always `mcp_call`.

          - `:mcp_call`

      - `class ComputerUseCall`

        One execution of the platform-provided computer-use capability.

        - `id: String`

          The ID of the activity item.

        - `output: Output{ image_url, type}`

          The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

          - `image_url: String`

            The complete JPEG image as a base64 data URL.

          - `type: :computer_screenshot`

            The content type. Always `computer_screenshot`.

            - `:computer_screenshot`

        - `status: AgentFunctionCallStatus`

          The execution status of the activity.

        - `title: String`

          A model-generated description of the activity, when available.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :computer_use_call`

          The item type. Always `computer_use_call`.

          - `:computer_use_call`

      - `class ComputerUseApprovalRequest`

        A credential-free history record of the emitted login request.

        - `id: String`

          The stable history item ID.

        - `request: Request{ credential_origin, fields, options, 2 more}`

          A registered form awaiting the application's response.

          - `credential_origin: String`

            The registered form or frame origin where values will be entered.

          - `fields: Array[Field{ id, label, required, type}]`

            Controls to render. All submitted values are sensitive.

            - `id: String`

              The field ID to submit as field_id in a fields entry.

            - `label: String`

              The label to display beside the control.

            - `required: bool`

              Whether this control requires a nonempty value.

            - `type: String`

              The rendering type, such as email, password, or text.

          - `options: Array[Option{ id, field_ids, label}]`

            Sign-in methods. Empty for a plain form.

            - `id: String`

              The option ID to submit as selected_option.

            - `field_ids: Array[String]`

              IDs from the registered fields that this method accepts.

            - `label: String`

              The method label to display.

          - `reason: String`

            Why the agent needs the user to sign in.

          - `type: :browser_authentication`

            The type of the object. Always `browser_authentication`.

            - `:browser_authentication`

        - `request_id: String`

        - `turn_id: String`

        - `type: :computer_use_approval_request`

          The item type. Always computer_use_approval_request.

          - `:computer_use_approval_request`

      - `class ComputerUseApprovalRequestResult`

        A credential-free record of an admitted response, not proof of completion.

        - `id: String`

          The stable history item ID.

        - `request_id: String`

          The registered request answered by this item.

        - `response: Submit{ action, selected_option, type} | Cancel{ action, type}`

          The admitted response, without submitted credential values.

          - `class Submit`

            - `action: :submit`

              - `:submit`

            - `selected_option: String`

              The chosen sign-in method, or null when no options were offered.

            - `type: :browser_authentication`

              - `:browser_authentication`

          - `class Cancel`

            - `action: :cancel`

              - `:cancel`

            - `type: :browser_authentication`

              - `:browser_authentication`

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :computer_use_approval_request_result`

          - `:computer_use_approval_request_result`

      - `class AgentWebSearchCallItem`

        A web search call produced by the agent.

        - `id: String`

          The ID of the web search call.

        - `action: WebSearchAction`

          The action performed by the web search tool.

          - `class Search`

            A search query or group of search queries.

            - `queries: Array[String]`

              The search queries, when multiple queries were used.

            - `query: String`

              The search query, when a single query was used.

            - `type: :search`

              The type of the object. Always `search`.

              - `:search`

          - `class OpenPage`

            Opens a web page.

            - `type: :open_page`

              The type of the object. Always `open_page`.

              - `:open_page`

            - `url: String`

              The URL of the page that was opened.

          - `class FindInPage`

            Finds text within a web page.

            - `pattern: String`

              The text pattern that was searched for.

            - `type: :find_in_page`

              The type of the object. Always `find_in_page`.

              - `:find_in_page`

            - `url: String`

              The URL of the page that was searched.

          - `class Other`

            Another web search action.

            - `type: :other`

              The type of the object. Always `other`.

              - `:other`

        - `status: AgentOutputItemStatus`

          The status of the web search call.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :web_search_call`

          The item type. Always `web_search_call`.

          - `:web_search_call`

      - `class AgentCommandExecutionItem`

        A command execution produced by the agent.

        - `id: String`

          The ID of the command execution item.

        - `command: String`

          The command that was executed.

        - `cwd: String`

          The working directory used to execute the command.

        - `duration_ms: Integer`

          The command duration in milliseconds.

        - `exit_code: Integer`

          The process exit code, if the command completed.

        - `output: String`

          The command output, if available.

        - `status: AgentFunctionCallStatus`

          The status of the command execution.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :command_execution`

          The item type. Always `command_execution`.

          - `:command_execution`

      - `class AgentCreateSubagentCallItem`

        A request to spawn a subagent.

        - `id: String`

          The ID of the tool call item.

        - `agent_id: String`

          The ID of the agent that requested the subagent.

        - `content: Array[AgentContent]`

          The task given to the spawned agent.

          - `class OutputText`

            A text content part produced by the agent.

          - `class EncryptedContent`

            Encrypted content exchanged between agents.

        - `model: String`

          The model requested for the spawned agent.

        - `reasoning_effort: String`

          The reasoning effort requested for the spawned agent.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :create_subagent_call`

          The item type. Always `create_subagent_call`.

          - `:create_subagent_call`

            The current public item type.

      - `class AgentSendSubagentInputCallItem`

        A request to send input to another agent.

        - `id: String`

          The ID of the tool call item.

        - `content: Array[AgentContent]`

          The input sent to the receiving agent.

          - `class OutputText`

            A text content part produced by the agent.

          - `class EncryptedContent`

            Encrypted content exchanged between agents.

        - `recipient_agent_id: String`

          The ID of the agent receiving the input.

        - `sender_agent_id: String`

          The ID of the agent sending the input.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :send_subagent_input_call`

          The item type. Always `send_subagent_input_call`.

          - `:send_subagent_input_call`

            The current public item type.

      - `class AgentResumeSubagentCallItem`

        A request to resume a subagent.

        - `id: String`

          The ID of the tool call item.

        - `recipient_agent_id: String`

          The ID of the agent to resume.

        - `sender_agent_id: String`

          The ID of the agent requesting the resume.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :resume_subagent_call`

          The item type. Always `resume_subagent_call`.

          - `:resume_subagent_call`

            The current public item type.

      - `class AgentWaitForSubagentsCallItem`

        A request to wait for one or more subagents.

        - `id: String`

          The ID of the tool call item.

        - `recipient_agent_ids: Array[String]`

          The IDs of the agents to wait for.

        - `sender_agent_id: String`

          The ID of the agent waiting for results.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :wait_for_subagents_call`

          The item type. Always `wait_for_subagents_call`.

          - `:wait_for_subagents_call`

            The current public item type.

      - `class AgentInterruptSubagentCallItem`

        A request to interrupt a subagent's current turn. The subagent remains available.

        - `id: String`

          The ID of the tool call item.

        - `recipient_agent_id: String`

          The ID of the agent to interrupt.

        - `sender_agent_id: String`

          The ID of the agent requesting the interrupt.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :interrupt_subagent_call`

          The item type. Always `interrupt_subagent_call`.

          - `:interrupt_subagent_call`

            The current public item type.

      - `class AgentCloseSubagentCallItem`

        A request to close a subagent.

        - `id: String`

          The ID of the tool call item.

        - `recipient_agent_id: String`

          The ID of the agent to close.

        - `sender_agent_id: String`

          The ID of the agent requesting the close.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :close_subagent_call`

          The item type. Always `close_subagent_call`.

          - `:close_subagent_call`

            The current public item type.

    - `output_index: Integer`

      The index of the item in the turn output, when the item is agent output.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.turn.item.added"`

      The type of the object. Always `agent.session.turn.item.added`.

      - `:"agent.session.turn.item.added"`

  - `class AgentSessionIdleEvent`

    Emitted when a session becomes idle.

    - `event_id: String`

      The unique ID of the event.

    - `session: AgentSession`

      The session that became idle.

    - `type: :"agent.session.idle"`

      The type of the object. Always `agent.session.idle`.

      - `:"agent.session.idle"`

  - `class AgentSessionInProgressEvent`

    Emitted when a session starts processing a turn.

    - `event_id: String`

      The unique ID of the event.

    - `session: AgentSession`

      The session that started processing.

    - `type: :"agent.session.in_progress"`

      The type of the object. Always `agent.session.in_progress`.

      - `:"agent.session.in_progress"`

  - `class AgentSessionRequiresActionEvent`

    Emitted when a session is waiting for one or more required actions.

    - `event_id: String`

      The unique ID of the event.

    - `session: AgentSession`

      The session and its current required actions.

    - `type: :"agent.session.requires_action"`

      The type of the object. Always `agent.session.requires_action`.

      - `:"agent.session.requires_action"`

  - `class AgentSessionFailedEvent`

    Emitted when a session fails.

    - `event_id: String`

      The unique ID of the event.

    - `session: AgentSession`

      The failed session.

    - `type: :"agent.session.failed"`

      The type of the object. Always `agent.session.failed`.

      - `:"agent.session.failed"`

  - `class AgentSessionEnvironmentPendingEvent`

    Emitted while a session environment is being prepared.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: String`

      The unique ID of the event.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.environment.pending"`

      The type of the object. Always `agent.session.environment.pending`.

      - `:"agent.session.environment.pending"`

  - `class AgentSessionEnvironmentConnectedEvent`

    Emitted when a session environment connects.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: String`

      The unique ID of the event.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.environment.connected"`

      The type of the object. Always `agent.session.environment.connected`.

      - `:"agent.session.environment.connected"`

  - `class AgentSessionEnvironmentDisconnectedEvent`

    Emitted when a session environment disconnects.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: String`

      The unique ID of the event.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.environment.disconnected"`

      The type of the object. Always `agent.session.environment.disconnected`.

      - `:"agent.session.environment.disconnected"`

  - `class AgentSessionEnvironmentFailedEvent`

    Emitted when a session environment fails.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: String`

      The unique ID of the event.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.environment.failed"`

      The type of the object. Always `agent.session.environment.failed`.

      - `:"agent.session.environment.failed"`

  - `class AgentSessionSubagentCreatedEvent`

    Emitted when a subagent is created.

    - `event_id: String`

      The unique ID of the event.

    - `subagent: Subagent`

      The subagent that was created.

      - `id: String`

        The ID of the subagent.

      - `closed_at: Integer`

        The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

      - `instructions: Array[AgentContent]`

        Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

        - `class OutputText`

          A text content part produced by the agent.

        - `class EncryptedContent`

          Encrypted content exchanged between agents.

      - `name: String`

        The runner-assigned nickname, or null when unavailable.

      - `object: :"agent.session.subagent"`

        The object type. Always `agent.session.subagent`.

        - `:"agent.session.subagent"`

      - `opened_at: Integer`

        The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

      - `parent_agent_id: String`

        The ID of the agent that created this subagent.

      - `session_id: String`

        The ID of the session that owns the subagent.

      - `status: :active | :closed`

        The current status of the subagent.

        - `:active`

          The subagent remains available, including while idle between turns.

        - `:closed`

          The subagent is closed.

    - `type: :"agent.session.subagent.created"`

      The type of the object. Always `agent.session.subagent.created`.

      - `:"agent.session.subagent.created"`

  - `class AgentSessionSubagentActiveEvent`

    Emitted when a closed subagent successfully resumes.

    - `event_id: String`

      The unique ID of the event.

    - `subagent: Subagent`

      The subagent that resumed.

    - `type: :"agent.session.subagent.active"`

      The type of the object. Always `agent.session.subagent.active`.

      - `:"agent.session.subagent.active"`

  - `class AgentSessionSubagentClosedEvent`

    Emitted when a subagent is closed.

    - `event_id: String`

      The unique ID of the event.

    - `subagent: Subagent`

      The subagent that was closed.

    - `type: :"agent.session.subagent.closed"`

      The type of the object. Always `agent.session.subagent.closed`.

      - `:"agent.session.subagent.closed"`

  - `class AgentSessionTurnItemDoneEvent`

    Emitted when an output item is complete.

    - `event_id: String`

      The unique ID of the event.

    - `item: AgentOutputItem`

      The completed output item.

      - `class AgentSessionAssistantMessage`

        An assistant message produced by the agent.

        - `id: String`

          The ID of the message.

        - `content: Array[OutputText]`

          The content of the message.

          - `text: String`

            The text produced by the agent.

          - `type: :output_text`

            The content type. Always `output_text`.

        - `phase: :commentary | :final_answer`

          The phase of the assistant message.

          - `:commentary`

            Commentary produced while the agent works.

          - `:final_answer`

            The agent's final answer.

        - `role: :assistant`

          The role of the message author. Always `assistant`.

          - `:assistant`

        - `status: AgentOutputItemStatus`

          The status of the message.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :message`

          The item type. Always `message`.

          - `:message`

      - `class AgentReasoningItem`

        A reasoning item produced by the agent.

      - `class AgentFunctionCallItem`

        A function call produced by the agent.

      - `class AgentMcpCallItem`

        A call to a tool on an MCP server.

      - `class ComputerUseCall`

        One execution of the platform-provided computer-use capability.

        - `id: String`

          The ID of the activity item.

        - `output: Output{ image_url, type}`

          The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

          - `image_url: String`

            The complete JPEG image as a base64 data URL.

          - `type: :computer_screenshot`

            The content type. Always `computer_screenshot`.

            - `:computer_screenshot`

        - `status: AgentFunctionCallStatus`

          The execution status of the activity.

        - `title: String`

          A model-generated description of the activity, when available.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :computer_use_call`

          The item type. Always `computer_use_call`.

          - `:computer_use_call`

      - `class ComputerUseApprovalRequest`

        A credential-free history record of the emitted login request.

        - `id: String`

          The stable history item ID.

        - `request: Request{ credential_origin, fields, options, 2 more}`

          A registered form awaiting the application's response.

          - `credential_origin: String`

            The registered form or frame origin where values will be entered.

          - `fields: Array[Field{ id, label, required, type}]`

            Controls to render. All submitted values are sensitive.

            - `id: String`

              The field ID to submit as field_id in a fields entry.

            - `label: String`

              The label to display beside the control.

            - `required: bool`

              Whether this control requires a nonempty value.

            - `type: String`

              The rendering type, such as email, password, or text.

          - `options: Array[Option{ id, field_ids, label}]`

            Sign-in methods. Empty for a plain form.

            - `id: String`

              The option ID to submit as selected_option.

            - `field_ids: Array[String]`

              IDs from the registered fields that this method accepts.

            - `label: String`

              The method label to display.

          - `reason: String`

            Why the agent needs the user to sign in.

          - `type: :browser_authentication`

            The type of the object. Always `browser_authentication`.

            - `:browser_authentication`

        - `request_id: String`

        - `turn_id: String`

        - `type: :computer_use_approval_request`

          The item type. Always computer_use_approval_request.

          - `:computer_use_approval_request`

      - `class AgentWebSearchCallItem`

        A web search call produced by the agent.

      - `class AgentCommandExecutionItem`

        A command execution produced by the agent.

      - `class AgentCreateSubagentCallItem`

        A request to spawn a subagent.

      - `class AgentSendSubagentInputCallItem`

        A request to send input to another agent.

      - `class AgentResumeSubagentCallItem`

        A request to resume a subagent.

      - `class AgentWaitForSubagentsCallItem`

        A request to wait for one or more subagents.

      - `class AgentInterruptSubagentCallItem`

        A request to interrupt a subagent's current turn. The subagent remains available.

      - `class AgentCloseSubagentCallItem`

        A request to close a subagent.

    - `output_index: Integer`

      The index of the output item in the turn output.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.turn.item.done"`

      The type of the object. Always `agent.session.turn.item.done`.

      - `:"agent.session.turn.item.done"`

  - `class AgentSessionTurnContentPartAddedEvent`

    Emitted when an output text content part is added.

    - `content_index: Integer`

      The index of the content part in the message.

    - `event_id: String`

      The unique ID of the event.

    - `item_id: String`

      The ID of the message item.

    - `output_index: Integer`

      The index of the item in the turn output.

    - `part: OutputText`

      The initial content part.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.turn.content_part.added"`

      The type of the object. Always `agent.session.turn.content_part.added`.

      - `:"agent.session.turn.content_part.added"`

  - `class AgentSessionTurnContentPartDoneEvent`

    Emitted when an output content part is complete.

    - `content_index: Integer`

      The index of the content part in the message.

    - `event_id: String`

      The unique ID of the event.

    - `item_id: String`

      The ID of the message item.

    - `output_index: Integer`

      The index of the item in the turn output.

    - `part: OutputText`

      The completed content part.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.turn.content_part.done"`

      The type of the object. Always `agent.session.turn.content_part.done`.

      - `:"agent.session.turn.content_part.done"`

  - `class AgentSessionTurnOutputTextDeltaEvent`

    Emitted when text is appended to an output text content part.

    - `content_index: Integer`

      The index of the content part in the message.

    - `delta: String`

      The text that was appended.

    - `event_id: String`

      The unique ID of the event.

    - `item_id: String`

      The ID of the message item.

    - `output_index: Integer`

      The index of the item in the turn output.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.turn.output_text.delta"`

      The type of the object. Always `agent.session.turn.output_text.delta`.

      - `:"agent.session.turn.output_text.delta"`

  - `class AgentSessionTurnOutputTextDoneEvent`

    Emitted when an output text content part is complete.

    - `content_index: Integer`

      The index of the content part in the message.

    - `event_id: String`

      The unique ID of the event.

    - `item_id: String`

      The ID of the message item.

    - `output_index: Integer`

      The index of the item in the turn output.

    - `session_id: String`

      The ID of the session associated with the event.

    - `text: String`

      The complete output text.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.turn.output_text.done"`

      The type of the object. Always `agent.session.turn.output_text.done`.

      - `:"agent.session.turn.output_text.done"`

  - `class AgentSessionTurnReasoningSummaryPartAddedEvent`

    Emitted when a reasoning summary content part is added.

    - `event_id: String`

      The unique ID of the event.

    - `item_id: String`

      The ID of the reasoning item.

    - `output_index: Integer`

      The index of the item in the turn output.

    - `part: SummaryText`

      The initial summary part.

      - `text: String`

        The reasoning summary text.

      - `type: :summary_text`

        The content type. Always `summary_text`.

    - `session_id: String`

      The ID of the session associated with the event.

    - `summary_index: Integer`

      The index of the summary content part.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.turn.reasoning_summary_part.added"`

      The type of the object. Always `agent.session.turn.reasoning_summary_part.added`.

      - `:"agent.session.turn.reasoning_summary_part.added"`

  - `class AgentSessionTurnReasoningSummaryPartDoneEvent`

    Emitted when a reasoning summary part is complete.

    - `event_id: String`

      The unique ID of the event.

    - `item_id: String`

      The ID of the reasoning item.

    - `output_index: Integer`

      The index of the item in the turn output.

    - `part: SummaryText`

      The completed summary part.

    - `session_id: String`

      The ID of the session associated with the event.

    - `status: :incomplete`

      Present as `incomplete` when summary generation was interrupted.

      - `:incomplete`

    - `summary_index: Integer`

      The index of the summary part.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.turn.reasoning_summary_part.done"`

      The type of the object. Always `agent.session.turn.reasoning_summary_part.done`.

      - `:"agent.session.turn.reasoning_summary_part.done"`

  - `class AgentSessionTurnReasoningSummaryTextDeltaEvent`

    Emitted when text is appended to a reasoning summary.

    - `delta: String`

      The summary text that was appended.

    - `event_id: String`

      The unique ID of the event.

    - `item_id: String`

      The ID of the reasoning item.

    - `output_index: Integer`

      The index of the item in the turn output.

    - `session_id: String`

      The ID of the session associated with the event.

    - `summary_index: Integer`

      The index of the summary content part.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.turn.reasoning_summary_text.delta"`

      The type of the object. Always `agent.session.turn.reasoning_summary_text.delta`.

      - `:"agent.session.turn.reasoning_summary_text.delta"`

  - `class AgentSessionTurnReasoningSummaryTextDoneEvent`

    Emitted when a reasoning summary content part is complete.

    - `event_id: String`

      The unique ID of the event.

    - `item_id: String`

      The ID of the reasoning item.

    - `output_index: Integer`

      The index of the item in the turn output.

    - `session_id: String`

      The ID of the session associated with the event.

    - `summary_index: Integer`

      The index of the summary content part.

    - `text: String`

      The complete reasoning summary text.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.turn.reasoning_summary_text.done"`

      The type of the object. Always `agent.session.turn.reasoning_summary_text.done`.

      - `:"agent.session.turn.reasoning_summary_text.done"`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

agent_session_event = openai.beta.agents.sessions.events.stream("session_id")

puts(agent_session_event)
```

# Items

## List agent session items

`beta.agents.sessions.items.list(session_id, **kwargs) -> CursorPage<AgentSessionItem>`

**get** `/agents/sessions/{session_id}/items`

Lists items produced by the session's root agent, including its interactions with subagents. Each subagent has its own item history. See [inspecting agent output](/api/docs/guides/agents-api/observability).

### Parameters

- `session_id: String`

- `after: String`

  Return resources after this resource ID in the selected order.

- `limit: Integer`

  The maximum number of resources to return, between 1 and 100. Defaults to 20.

- `order: :asc | :desc`

  The order in which resources are returned. Defaults to `desc`.

  - `:asc`

    Returns resources in ascending order.

  - `:desc`

    Returns resources in descending order.

### Returns

- `AgentSessionItem = AgentSessionMessage | AgentReasoningItem | AgentFunctionCallItem | 14 more`

  An item associated with a session turn.

  - `class AgentSessionMessage`

    A user or assistant message recorded in a session.

    - `id: String`

      The ID of this item, or null for legacy user messages whose ID was not recorded.

    - `content: Array[AgentSessionMessageContent]`

      The content of the message. User messages contain input text or images; assistant messages contain output text.

      - `class InputText`

        Text supplied by the user.

        - `text: String`

          The text supplied by the user.

        - `type: :input_text`

          The type of the object. Always `input_text`.

          - `:input_text`

      - `class InputImage`

        An image supplied by the user.

        - `image_url: String`

          The URL of the image supplied by the user, which may be a base64-encoded data URL.

        - `type: :input_image`

          The type of the object. Always `input_image`.

          - `:input_image`

      - `class OutputText`

        Text produced by the assistant.

        - `text: String`

          The text produced by the assistant.

        - `type: :output_text`

          The type of the object. Always `output_text`.

          - `:output_text`

    - `phase: :commentary | :final_answer`

      The phase of an assistant message. Null for user messages.

      - `:commentary`

        Commentary produced while the agent works.

      - `:final_answer`

        The agent's final answer.

    - `role: :user | :assistant`

      The role of the message author.

      - `:user`

      - `:assistant`

    - `status: AgentOutputItemStatus`

      The status of the message. User messages are always `completed`.

      - `:in_progress`

        The item is in progress.

      - `:completed`

        The item is complete.

      - `:incomplete`

        The item stopped before completing.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :message`

      The item type. Always `message`.

      - `:message`

  - `class AgentReasoningItem`

    A reasoning item produced by the agent.

    - `id: String`

      The ID of the reasoning item.

    - `status: AgentOutputItemStatus`

      The status of the reasoning item.

    - `summary: Array[SummaryText]`

      The reasoning summaries produced by the agent.

      - `text: String`

        The reasoning summary text.

      - `type: :summary_text`

        The content type. Always `summary_text`.

        - `:summary_text`

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :reasoning`

      The item type. Always `reasoning`.

      - `:reasoning`

  - `class AgentFunctionCallItem`

    A function call produced by the agent.

    - `id: String`

      The ID of the function call item.

    - `arguments: untyped`

      The arguments to pass to the function.

    - `call_id: String`

      The ID used to submit the function result.

    - `name: String`

      The name of the function to call.

    - `status: AgentFunctionCallStatus`

      The status of the function call.

      - `:in_progress`

        The call is in progress.

      - `:completed`

        The call completed successfully.

      - `:failed`

        The call failed.

      - `:incomplete`

        The call stopped before completing.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :function_call`

      The item type. Always `function_call`.

      - `:function_call`

  - `class FunctionCallOutput`

    The result supplied for a function call.

    - `id: String`

      The ID of the function call output item.

    - `call_id: String`

      The ID of the function call that produced this output.

    - `error: String`

      The error message, if the call failed.

    - `output: AgentFunctionCallOutput`

      The function result, if the call succeeded.

      - `String = String`

      - `UnionMember1 = Array[InputContent]`

        - `class InputText`

          Text input recorded in a session item.

          - `text: String`

            The text supplied to the agent.

          - `type: :input_text`

            The type of the object. Always `input_text`.

            - `:input_text`

        - `class InputImage`

          Image input recorded in a session item.

          - `image_url: String`

            The URL of the image supplied to the agent, which may be a base64-encoded data URL.

          - `type: :input_image`

            The type of the object. Always `input_image`.

            - `:input_image`

    - `status: AgentFunctionCallStatus`

      The status of the function call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :function_call_output`

      The item type. Always `function_call_output`.

      - `:function_call_output`

  - `class AgentMessage`

    A message exchanged between agent threads.

    - `id: String`

      The ID of the message.

    - `content: Array[AgentContent]`

      The content exchanged between the agents.

      - `class OutputText`

        A text content part produced by the agent.

        - `text: String`

          The text produced by the agent.

        - `type: :output_text`

          The content type. Always `output_text`.

          - `:output_text`

      - `class EncryptedContent`

        Encrypted content exchanged between agents.

        - `encrypted_content: String`

          The encrypted content payload.

        - `type: :encrypted_content`

          The content type. Always `encrypted_content`.

          - `:encrypted_content`

    - `recipient_agent_id: String`

      The ID or name of the receiving agent.

    - `sender_agent_id: String`

      The ID or name of the sending agent.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :agent_message`

      The item type. Always `agent_message`.

      - `:agent_message`

  - `class AgentMcpCallItem`

    A call to a tool on an MCP server.

    - `id: String`

      The ID of the MCP call item.

    - `arguments: untyped`

      The arguments passed to the MCP tool.

    - `error: untyped`

      The error returned by the MCP tool, if any.

    - `name: String`

      The name of the MCP tool.

    - `output: untyped`

      The output returned by the MCP tool, if any.

    - `server_label: String`

      The label of the MCP server.

    - `status: AgentFunctionCallStatus`

      The status of the MCP tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :mcp_call`

      The item type. Always `mcp_call`.

      - `:mcp_call`

  - `class ComputerUseCall`

    One execution of the platform-provided computer-use capability.

    - `id: String`

      The ID of the activity item.

    - `output: Output{ image_url, type}`

      The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

      - `image_url: String`

        The complete JPEG image as a base64 data URL.

      - `type: :computer_screenshot`

        The content type. Always `computer_screenshot`.

        - `:computer_screenshot`

    - `status: AgentFunctionCallStatus`

      The execution status of the activity.

    - `title: String`

      A model-generated description of the activity, when available.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :computer_use_call`

      The item type. Always `computer_use_call`.

      - `:computer_use_call`

  - `class ComputerUseApprovalRequest`

    A credential-free history record of the emitted login request.

    - `id: String`

      The stable history item ID.

    - `request: Request{ credential_origin, fields, options, 2 more}`

      A registered form awaiting the application's response.

      - `credential_origin: String`

        The registered form or frame origin where values will be entered.

      - `fields: Array[Field{ id, label, required, type}]`

        Controls to render. All submitted values are sensitive.

        - `id: String`

          The field ID to submit as field_id in a fields entry.

        - `label: String`

          The label to display beside the control.

        - `required: bool`

          Whether this control requires a nonempty value.

        - `type: String`

          The rendering type, such as email, password, or text.

      - `options: Array[Option{ id, field_ids, label}]`

        Sign-in methods. Empty for a plain form.

        - `id: String`

          The option ID to submit as selected_option.

        - `field_ids: Array[String]`

          IDs from the registered fields that this method accepts.

        - `label: String`

          The method label to display.

      - `reason: String`

        Why the agent needs the user to sign in.

      - `type: :browser_authentication`

        The type of the object. Always `browser_authentication`.

        - `:browser_authentication`

    - `request_id: String`

    - `turn_id: String`

    - `type: :computer_use_approval_request`

      The item type. Always computer_use_approval_request.

      - `:computer_use_approval_request`

  - `class ComputerUseApprovalRequestResult`

    A credential-free record of an admitted response, not proof of completion.

    - `id: String`

      The stable history item ID.

    - `request_id: String`

      The registered request answered by this item.

    - `response: Submit{ action, selected_option, type} | Cancel{ action, type}`

      The admitted response, without submitted credential values.

      - `class Submit`

        - `action: :submit`

          - `:submit`

        - `selected_option: String`

          The chosen sign-in method, or null when no options were offered.

        - `type: :browser_authentication`

          - `:browser_authentication`

      - `class Cancel`

        - `action: :cancel`

          - `:cancel`

        - `type: :browser_authentication`

          - `:browser_authentication`

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :computer_use_approval_request_result`

      - `:computer_use_approval_request_result`

  - `class AgentWebSearchCallItem`

    A web search call produced by the agent.

    - `id: String`

      The ID of the web search call.

    - `action: WebSearchAction`

      The action performed by the web search tool.

      - `class Search`

        A search query or group of search queries.

        - `queries: Array[String]`

          The search queries, when multiple queries were used.

        - `query: String`

          The search query, when a single query was used.

        - `type: :search`

          The type of the object. Always `search`.

          - `:search`

      - `class OpenPage`

        Opens a web page.

        - `type: :open_page`

          The type of the object. Always `open_page`.

          - `:open_page`

        - `url: String`

          The URL of the page that was opened.

      - `class FindInPage`

        Finds text within a web page.

        - `pattern: String`

          The text pattern that was searched for.

        - `type: :find_in_page`

          The type of the object. Always `find_in_page`.

          - `:find_in_page`

        - `url: String`

          The URL of the page that was searched.

      - `class Other`

        Another web search action.

        - `type: :other`

          The type of the object. Always `other`.

          - `:other`

    - `status: AgentOutputItemStatus`

      The status of the web search call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :web_search_call`

      The item type. Always `web_search_call`.

      - `:web_search_call`

  - `class AgentCommandExecutionItem`

    A command execution produced by the agent.

    - `id: String`

      The ID of the command execution item.

    - `command: String`

      The command that was executed.

    - `cwd: String`

      The working directory used to execute the command.

    - `duration_ms: Integer`

      The command duration in milliseconds.

    - `exit_code: Integer`

      The process exit code, if the command completed.

    - `output: String`

      The command output, if available.

    - `status: AgentFunctionCallStatus`

      The status of the command execution.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :command_execution`

      The item type. Always `command_execution`.

      - `:command_execution`

  - `class AgentCreateSubagentCallItem`

    A request to spawn a subagent.

    - `id: String`

      The ID of the tool call item.

    - `agent_id: String`

      The ID of the agent that requested the subagent.

    - `content: Array[AgentContent]`

      The task given to the spawned agent.

      - `class OutputText`

        A text content part produced by the agent.

      - `class EncryptedContent`

        Encrypted content exchanged between agents.

    - `model: String`

      The model requested for the spawned agent.

    - `reasoning_effort: String`

      The reasoning effort requested for the spawned agent.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :create_subagent_call`

      The item type. Always `create_subagent_call`.

      - `:create_subagent_call`

        The current public item type.

  - `class AgentSendSubagentInputCallItem`

    A request to send input to another agent.

    - `id: String`

      The ID of the tool call item.

    - `content: Array[AgentContent]`

      The input sent to the receiving agent.

      - `class OutputText`

        A text content part produced by the agent.

      - `class EncryptedContent`

        Encrypted content exchanged between agents.

    - `recipient_agent_id: String`

      The ID of the agent receiving the input.

    - `sender_agent_id: String`

      The ID of the agent sending the input.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :send_subagent_input_call`

      The item type. Always `send_subagent_input_call`.

      - `:send_subagent_input_call`

        The current public item type.

  - `class AgentResumeSubagentCallItem`

    A request to resume a subagent.

    - `id: String`

      The ID of the tool call item.

    - `recipient_agent_id: String`

      The ID of the agent to resume.

    - `sender_agent_id: String`

      The ID of the agent requesting the resume.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :resume_subagent_call`

      The item type. Always `resume_subagent_call`.

      - `:resume_subagent_call`

        The current public item type.

  - `class AgentWaitForSubagentsCallItem`

    A request to wait for one or more subagents.

    - `id: String`

      The ID of the tool call item.

    - `recipient_agent_ids: Array[String]`

      The IDs of the agents to wait for.

    - `sender_agent_id: String`

      The ID of the agent waiting for results.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :wait_for_subagents_call`

      The item type. Always `wait_for_subagents_call`.

      - `:wait_for_subagents_call`

        The current public item type.

  - `class AgentInterruptSubagentCallItem`

    A request to interrupt a subagent's current turn. The subagent remains available.

    - `id: String`

      The ID of the tool call item.

    - `recipient_agent_id: String`

      The ID of the agent to interrupt.

    - `sender_agent_id: String`

      The ID of the agent requesting the interrupt.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :interrupt_subagent_call`

      The item type. Always `interrupt_subagent_call`.

      - `:interrupt_subagent_call`

        The current public item type.

  - `class AgentCloseSubagentCallItem`

    A request to close a subagent.

    - `id: String`

      The ID of the tool call item.

    - `recipient_agent_id: String`

      The ID of the agent to close.

    - `sender_agent_id: String`

      The ID of the agent requesting the close.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :close_subagent_call`

      The item type. Always `close_subagent_call`.

      - `:close_subagent_call`

        The current public item type.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.beta.agents.sessions.items.list("session_id")

puts(page)
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "content": [
        {
          "text": "text",
          "type": "input_text"
        }
      ],
      "phase": "commentary",
      "role": "user",
      "status": "in_progress",
      "turn_id": "turn_id",
      "type": "message"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

# Subagents

## List session subagents

`beta.agents.sessions.subagents.list(session_id, **kwargs) -> CursorPage<Subagent>`

**get** `/agents/sessions/{session_id}/subagents`

Lists subagents in a session, including nested and closed subagents. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `session_id: String`

- `after: String`

  Return resources after this resource ID in the selected order.

- `limit: Integer`

  The maximum number of resources to return, between 1 and 100. Defaults to 20.

- `order: :asc | :desc`

  The order in which resources are returned. Defaults to `desc`.

  - `:asc`

    Returns resources in ascending order.

  - `:desc`

    Returns resources in descending order.

### Returns

- `class Subagent`

  A subagent created within a session.

  - `id: String`

    The ID of the subagent.

  - `closed_at: Integer`

    The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

  - `instructions: Array[AgentContent]`

    Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

    - `class OutputText`

      A text content part produced by the agent.

      - `text: String`

        The text produced by the agent.

      - `type: :output_text`

        The content type. Always `output_text`.

        - `:output_text`

    - `class EncryptedContent`

      Encrypted content exchanged between agents.

      - `encrypted_content: String`

        The encrypted content payload.

      - `type: :encrypted_content`

        The content type. Always `encrypted_content`.

        - `:encrypted_content`

  - `name: String`

    The runner-assigned nickname, or null when unavailable.

  - `object: :"agent.session.subagent"`

    The object type. Always `agent.session.subagent`.

    - `:"agent.session.subagent"`

  - `opened_at: Integer`

    The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

  - `parent_agent_id: String`

    The ID of the agent that created this subagent.

  - `session_id: String`

    The ID of the session that owns the subagent.

  - `status: :active | :closed`

    The current status of the subagent.

    - `:active`

      The subagent remains available, including while idle between turns.

    - `:closed`

      The subagent is closed.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.beta.agents.sessions.subagents.list("session_id")

puts(page)
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "closed_at": 0,
      "instructions": [
        {
          "text": "text",
          "type": "output_text"
        }
      ],
      "name": "name",
      "object": "agent.session.subagent",
      "opened_at": 0,
      "parent_agent_id": "parent_agent_id",
      "session_id": "session_id",
      "status": "active"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve a session subagent

`beta.agents.sessions.subagents.retrieve(subagent_id, **kwargs) -> Subagent`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}`

Retrieves a subagent belonging to this session. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `session_id: String`

- `subagent_id: String`

### Returns

- `class Subagent`

  A subagent created within a session.

  - `id: String`

    The ID of the subagent.

  - `closed_at: Integer`

    The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

  - `instructions: Array[AgentContent]`

    Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

    - `class OutputText`

      A text content part produced by the agent.

      - `text: String`

        The text produced by the agent.

      - `type: :output_text`

        The content type. Always `output_text`.

        - `:output_text`

    - `class EncryptedContent`

      Encrypted content exchanged between agents.

      - `encrypted_content: String`

        The encrypted content payload.

      - `type: :encrypted_content`

        The content type. Always `encrypted_content`.

        - `:encrypted_content`

  - `name: String`

    The runner-assigned nickname, or null when unavailable.

  - `object: :"agent.session.subagent"`

    The object type. Always `agent.session.subagent`.

    - `:"agent.session.subagent"`

  - `opened_at: Integer`

    The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

  - `parent_agent_id: String`

    The ID of the agent that created this subagent.

  - `session_id: String`

    The ID of the session that owns the subagent.

  - `status: :active | :closed`

    The current status of the subagent.

    - `:active`

      The subagent remains available, including while idle between turns.

    - `:closed`

      The subagent is closed.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

subagent = openai.beta.agents.sessions.subagents.retrieve("subagent_id", session_id: "session_id")

puts(subagent)
```

#### Response

```json
{
  "id": "id",
  "closed_at": 0,
  "instructions": [
    {
      "text": "text",
      "type": "output_text"
    }
  ],
  "name": "name",
  "object": "agent.session.subagent",
  "opened_at": 0,
  "parent_agent_id": "parent_agent_id",
  "session_id": "session_id",
  "status": "active"
}
```

# Items

## List subagent items

`beta.agents.sessions.subagents.items.list(subagent_id, **kwargs) -> CursorPage<AgentSessionItem>`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}/items`

Lists this subagent's own items across all of its turns. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `session_id: String`

- `subagent_id: String`

- `after: String`

  Return resources after this resource ID in the selected order.

- `limit: Integer`

  The maximum number of resources to return, between 1 and 100. Defaults to 20.

- `order: :asc | :desc`

  The order in which resources are returned. Defaults to `desc`.

  - `:asc`

    Returns resources in ascending order.

  - `:desc`

    Returns resources in descending order.

### Returns

- `AgentSessionItem = AgentSessionMessage | AgentReasoningItem | AgentFunctionCallItem | 14 more`

  An item associated with a session turn.

  - `class AgentSessionMessage`

    A user or assistant message recorded in a session.

    - `id: String`

      The ID of this item, or null for legacy user messages whose ID was not recorded.

    - `content: Array[AgentSessionMessageContent]`

      The content of the message. User messages contain input text or images; assistant messages contain output text.

      - `class InputText`

        Text supplied by the user.

        - `text: String`

          The text supplied by the user.

        - `type: :input_text`

          The type of the object. Always `input_text`.

          - `:input_text`

      - `class InputImage`

        An image supplied by the user.

        - `image_url: String`

          The URL of the image supplied by the user, which may be a base64-encoded data URL.

        - `type: :input_image`

          The type of the object. Always `input_image`.

          - `:input_image`

      - `class OutputText`

        Text produced by the assistant.

        - `text: String`

          The text produced by the assistant.

        - `type: :output_text`

          The type of the object. Always `output_text`.

          - `:output_text`

    - `phase: :commentary | :final_answer`

      The phase of an assistant message. Null for user messages.

      - `:commentary`

        Commentary produced while the agent works.

      - `:final_answer`

        The agent's final answer.

    - `role: :user | :assistant`

      The role of the message author.

      - `:user`

      - `:assistant`

    - `status: AgentOutputItemStatus`

      The status of the message. User messages are always `completed`.

      - `:in_progress`

        The item is in progress.

      - `:completed`

        The item is complete.

      - `:incomplete`

        The item stopped before completing.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :message`

      The item type. Always `message`.

      - `:message`

  - `class AgentReasoningItem`

    A reasoning item produced by the agent.

    - `id: String`

      The ID of the reasoning item.

    - `status: AgentOutputItemStatus`

      The status of the reasoning item.

    - `summary: Array[SummaryText]`

      The reasoning summaries produced by the agent.

      - `text: String`

        The reasoning summary text.

      - `type: :summary_text`

        The content type. Always `summary_text`.

        - `:summary_text`

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :reasoning`

      The item type. Always `reasoning`.

      - `:reasoning`

  - `class AgentFunctionCallItem`

    A function call produced by the agent.

    - `id: String`

      The ID of the function call item.

    - `arguments: untyped`

      The arguments to pass to the function.

    - `call_id: String`

      The ID used to submit the function result.

    - `name: String`

      The name of the function to call.

    - `status: AgentFunctionCallStatus`

      The status of the function call.

      - `:in_progress`

        The call is in progress.

      - `:completed`

        The call completed successfully.

      - `:failed`

        The call failed.

      - `:incomplete`

        The call stopped before completing.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :function_call`

      The item type. Always `function_call`.

      - `:function_call`

  - `class FunctionCallOutput`

    The result supplied for a function call.

    - `id: String`

      The ID of the function call output item.

    - `call_id: String`

      The ID of the function call that produced this output.

    - `error: String`

      The error message, if the call failed.

    - `output: AgentFunctionCallOutput`

      The function result, if the call succeeded.

      - `String = String`

      - `UnionMember1 = Array[InputContent]`

        - `class InputText`

          Text input recorded in a session item.

          - `text: String`

            The text supplied to the agent.

          - `type: :input_text`

            The type of the object. Always `input_text`.

            - `:input_text`

        - `class InputImage`

          Image input recorded in a session item.

          - `image_url: String`

            The URL of the image supplied to the agent, which may be a base64-encoded data URL.

          - `type: :input_image`

            The type of the object. Always `input_image`.

            - `:input_image`

    - `status: AgentFunctionCallStatus`

      The status of the function call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :function_call_output`

      The item type. Always `function_call_output`.

      - `:function_call_output`

  - `class AgentMessage`

    A message exchanged between agent threads.

    - `id: String`

      The ID of the message.

    - `content: Array[AgentContent]`

      The content exchanged between the agents.

      - `class OutputText`

        A text content part produced by the agent.

        - `text: String`

          The text produced by the agent.

        - `type: :output_text`

          The content type. Always `output_text`.

          - `:output_text`

      - `class EncryptedContent`

        Encrypted content exchanged between agents.

        - `encrypted_content: String`

          The encrypted content payload.

        - `type: :encrypted_content`

          The content type. Always `encrypted_content`.

          - `:encrypted_content`

    - `recipient_agent_id: String`

      The ID or name of the receiving agent.

    - `sender_agent_id: String`

      The ID or name of the sending agent.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :agent_message`

      The item type. Always `agent_message`.

      - `:agent_message`

  - `class AgentMcpCallItem`

    A call to a tool on an MCP server.

    - `id: String`

      The ID of the MCP call item.

    - `arguments: untyped`

      The arguments passed to the MCP tool.

    - `error: untyped`

      The error returned by the MCP tool, if any.

    - `name: String`

      The name of the MCP tool.

    - `output: untyped`

      The output returned by the MCP tool, if any.

    - `server_label: String`

      The label of the MCP server.

    - `status: AgentFunctionCallStatus`

      The status of the MCP tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :mcp_call`

      The item type. Always `mcp_call`.

      - `:mcp_call`

  - `class ComputerUseCall`

    One execution of the platform-provided computer-use capability.

    - `id: String`

      The ID of the activity item.

    - `output: Output{ image_url, type}`

      The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

      - `image_url: String`

        The complete JPEG image as a base64 data URL.

      - `type: :computer_screenshot`

        The content type. Always `computer_screenshot`.

        - `:computer_screenshot`

    - `status: AgentFunctionCallStatus`

      The execution status of the activity.

    - `title: String`

      A model-generated description of the activity, when available.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :computer_use_call`

      The item type. Always `computer_use_call`.

      - `:computer_use_call`

  - `class ComputerUseApprovalRequest`

    A credential-free history record of the emitted login request.

    - `id: String`

      The stable history item ID.

    - `request: Request{ credential_origin, fields, options, 2 more}`

      A registered form awaiting the application's response.

      - `credential_origin: String`

        The registered form or frame origin where values will be entered.

      - `fields: Array[Field{ id, label, required, type}]`

        Controls to render. All submitted values are sensitive.

        - `id: String`

          The field ID to submit as field_id in a fields entry.

        - `label: String`

          The label to display beside the control.

        - `required: bool`

          Whether this control requires a nonempty value.

        - `type: String`

          The rendering type, such as email, password, or text.

      - `options: Array[Option{ id, field_ids, label}]`

        Sign-in methods. Empty for a plain form.

        - `id: String`

          The option ID to submit as selected_option.

        - `field_ids: Array[String]`

          IDs from the registered fields that this method accepts.

        - `label: String`

          The method label to display.

      - `reason: String`

        Why the agent needs the user to sign in.

      - `type: :browser_authentication`

        The type of the object. Always `browser_authentication`.

        - `:browser_authentication`

    - `request_id: String`

    - `turn_id: String`

    - `type: :computer_use_approval_request`

      The item type. Always computer_use_approval_request.

      - `:computer_use_approval_request`

  - `class ComputerUseApprovalRequestResult`

    A credential-free record of an admitted response, not proof of completion.

    - `id: String`

      The stable history item ID.

    - `request_id: String`

      The registered request answered by this item.

    - `response: Submit{ action, selected_option, type} | Cancel{ action, type}`

      The admitted response, without submitted credential values.

      - `class Submit`

        - `action: :submit`

          - `:submit`

        - `selected_option: String`

          The chosen sign-in method, or null when no options were offered.

        - `type: :browser_authentication`

          - `:browser_authentication`

      - `class Cancel`

        - `action: :cancel`

          - `:cancel`

        - `type: :browser_authentication`

          - `:browser_authentication`

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :computer_use_approval_request_result`

      - `:computer_use_approval_request_result`

  - `class AgentWebSearchCallItem`

    A web search call produced by the agent.

    - `id: String`

      The ID of the web search call.

    - `action: WebSearchAction`

      The action performed by the web search tool.

      - `class Search`

        A search query or group of search queries.

        - `queries: Array[String]`

          The search queries, when multiple queries were used.

        - `query: String`

          The search query, when a single query was used.

        - `type: :search`

          The type of the object. Always `search`.

          - `:search`

      - `class OpenPage`

        Opens a web page.

        - `type: :open_page`

          The type of the object. Always `open_page`.

          - `:open_page`

        - `url: String`

          The URL of the page that was opened.

      - `class FindInPage`

        Finds text within a web page.

        - `pattern: String`

          The text pattern that was searched for.

        - `type: :find_in_page`

          The type of the object. Always `find_in_page`.

          - `:find_in_page`

        - `url: String`

          The URL of the page that was searched.

      - `class Other`

        Another web search action.

        - `type: :other`

          The type of the object. Always `other`.

          - `:other`

    - `status: AgentOutputItemStatus`

      The status of the web search call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :web_search_call`

      The item type. Always `web_search_call`.

      - `:web_search_call`

  - `class AgentCommandExecutionItem`

    A command execution produced by the agent.

    - `id: String`

      The ID of the command execution item.

    - `command: String`

      The command that was executed.

    - `cwd: String`

      The working directory used to execute the command.

    - `duration_ms: Integer`

      The command duration in milliseconds.

    - `exit_code: Integer`

      The process exit code, if the command completed.

    - `output: String`

      The command output, if available.

    - `status: AgentFunctionCallStatus`

      The status of the command execution.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :command_execution`

      The item type. Always `command_execution`.

      - `:command_execution`

  - `class AgentCreateSubagentCallItem`

    A request to spawn a subagent.

    - `id: String`

      The ID of the tool call item.

    - `agent_id: String`

      The ID of the agent that requested the subagent.

    - `content: Array[AgentContent]`

      The task given to the spawned agent.

      - `class OutputText`

        A text content part produced by the agent.

      - `class EncryptedContent`

        Encrypted content exchanged between agents.

    - `model: String`

      The model requested for the spawned agent.

    - `reasoning_effort: String`

      The reasoning effort requested for the spawned agent.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :create_subagent_call`

      The item type. Always `create_subagent_call`.

      - `:create_subagent_call`

        The current public item type.

  - `class AgentSendSubagentInputCallItem`

    A request to send input to another agent.

    - `id: String`

      The ID of the tool call item.

    - `content: Array[AgentContent]`

      The input sent to the receiving agent.

      - `class OutputText`

        A text content part produced by the agent.

      - `class EncryptedContent`

        Encrypted content exchanged between agents.

    - `recipient_agent_id: String`

      The ID of the agent receiving the input.

    - `sender_agent_id: String`

      The ID of the agent sending the input.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :send_subagent_input_call`

      The item type. Always `send_subagent_input_call`.

      - `:send_subagent_input_call`

        The current public item type.

  - `class AgentResumeSubagentCallItem`

    A request to resume a subagent.

    - `id: String`

      The ID of the tool call item.

    - `recipient_agent_id: String`

      The ID of the agent to resume.

    - `sender_agent_id: String`

      The ID of the agent requesting the resume.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :resume_subagent_call`

      The item type. Always `resume_subagent_call`.

      - `:resume_subagent_call`

        The current public item type.

  - `class AgentWaitForSubagentsCallItem`

    A request to wait for one or more subagents.

    - `id: String`

      The ID of the tool call item.

    - `recipient_agent_ids: Array[String]`

      The IDs of the agents to wait for.

    - `sender_agent_id: String`

      The ID of the agent waiting for results.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :wait_for_subagents_call`

      The item type. Always `wait_for_subagents_call`.

      - `:wait_for_subagents_call`

        The current public item type.

  - `class AgentInterruptSubagentCallItem`

    A request to interrupt a subagent's current turn. The subagent remains available.

    - `id: String`

      The ID of the tool call item.

    - `recipient_agent_id: String`

      The ID of the agent to interrupt.

    - `sender_agent_id: String`

      The ID of the agent requesting the interrupt.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :interrupt_subagent_call`

      The item type. Always `interrupt_subagent_call`.

      - `:interrupt_subagent_call`

        The current public item type.

  - `class AgentCloseSubagentCallItem`

    A request to close a subagent.

    - `id: String`

      The ID of the tool call item.

    - `recipient_agent_id: String`

      The ID of the agent to close.

    - `sender_agent_id: String`

      The ID of the agent requesting the close.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :close_subagent_call`

      The item type. Always `close_subagent_call`.

      - `:close_subagent_call`

        The current public item type.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.beta.agents.sessions.subagents.items.list("subagent_id", session_id: "session_id")

puts(page)
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "content": [
        {
          "text": "text",
          "type": "input_text"
        }
      ],
      "phase": "commentary",
      "role": "user",
      "status": "in_progress",
      "turn_id": "turn_id",
      "type": "message"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

# Turns

## List subagent turns

`beta.agents.sessions.subagents.turns.list(subagent_id, **kwargs) -> CursorPage<Turn>`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}/turns`

Lists all turns of this subagent, including turns after a resume. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `session_id: String`

- `subagent_id: String`

- `after: String`

  Return resources after this resource ID in the selected order.

- `limit: Integer`

  The maximum number of resources to return, between 1 and 100. Defaults to 20.

- `order: :asc | :desc`

  The order in which resources are returned. Defaults to `desc`.

  - `:asc`

    Returns resources in ascending order.

  - `:desc`

    Returns resources in descending order.

### Returns

- `class Turn`

  The canonical public representation of a session turn.

  - `id: String`

    The ID of the turn.

  - `agent_id: String`

    The ID of the agent that ran the turn.

  - `completed_at: Integer`

    The Unix timestamp, in seconds, when the turn reached a terminal state.

  - `created_at: Integer`

    The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

  - `error: SessionTurnError`

    A customer-safe error. Non-null only for a failed turn.

    - `code: :context_length_exceeded | :session_budget_exceeded | :usage_limit_exceeded | 16 more`

      A stable, machine-readable failure category.

      - `:context_length_exceeded`

        The request exceeds the model's context window.

      - `:session_budget_exceeded`

        The session has reached its usage budget.

      - `:usage_limit_exceeded`

        The organization has reached a usage, plan, or billing limit.

      - `:credit_balance_exhausted`

        The organization has no API credits remaining.

      - `:rate_limit_exceeded`

        The request exceeds the available rate limit.

      - `:flex_unavailable`

        Flex processing is temporarily unavailable.

      - `:server_overloaded`

        The model service is temporarily overloaded.

      - `:cyber_policy`

        The request was rejected by a safety policy.

      - `:misalignment_policy_violation`

        The request was blocked by the safety systems.

      - `:connection_failed`

        The request could not connect to the model service.

      - `:server_error`

        The model service encountered an unexpected error.

      - `:authentication_error`

        The API credentials are invalid or lack the required access.

      - `:invalid_request`

        The request contains invalid input or configuration.

      - `:resource_not_found`

        The requested model or resource is unavailable.

      - `:sandbox_error`

        The request could not complete in its execution environment.

      - `:executor_version_incompatible`

        The executor must be upgraded before it can run this turn.

      - `:active_turn_not_steerable`

        The session cannot accept additional input while a request is running.

      - `:request_timeout`

        The request timed out before the model service responded.

      - `:internal_error`

        An unexpected internal error prevented the session request from completing.

    - `message: String`

      A customer-safe explanation of the failure.

  - `object: :"agent.session.turn"`

    The object type. Always `agent.session.turn`.

    - `:"agent.session.turn"`

  - `session_id: String`

    The ID of the session that owns the turn.

  - `started_at: Integer`

    The Unix timestamp, in seconds, when the turn started.

  - `status: :queued | :in_progress | :waiting | 3 more`

    The current status of the turn.

    - `:queued`

      The turn is waiting to start.

    - `:in_progress`

      The turn is in progress.

    - `:waiting`

      The turn is waiting for external input.

    - `:completed`

      The turn completed successfully.

    - `:failed`

      The turn failed.

    - `:cancelled`

      The turn was cancelled.

  - `subagent_id: String`

    The ID of the subagent that ran the turn, if applicable.

  - `usage: TokenUsage`

    Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `input_tokens: Integer`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails{ cached_tokens}`

      A breakdown of the agent's input token usage.

      - `cached_tokens: Integer`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: Integer`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails{ reasoning_tokens}`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: Integer`

        The number of output tokens used for reasoning.

    - `total_tokens: Integer`

      The total number of input and output tokens used by the agent.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.beta.agents.sessions.subagents.turns.list("subagent_id", session_id: "session_id")

puts(page)
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "agent_id": "agent_id",
      "completed_at": 0,
      "created_at": 0,
      "error": {
        "code": "context_length_exceeded",
        "message": "message"
      },
      "object": "agent.session.turn",
      "session_id": "session_id",
      "started_at": 0,
      "status": "queued",
      "subagent_id": "subagent_id",
      "usage": {
        "input_tokens": 0,
        "input_tokens_details": {
          "cached_tokens": 0
        },
        "output_tokens": 0,
        "output_tokens_details": {
          "reasoning_tokens": 0
        },
        "total_tokens": 0
      }
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve a subagent turn

`beta.agents.sessions.subagents.turns.retrieve(turn_id, **kwargs) -> Turn`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}/turns/{turn_id}`

Retrieves a turn belonging to this subagent. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `session_id: String`

- `subagent_id: String`

- `turn_id: String`

### Returns

- `class Turn`

  The canonical public representation of a session turn.

  - `id: String`

    The ID of the turn.

  - `agent_id: String`

    The ID of the agent that ran the turn.

  - `completed_at: Integer`

    The Unix timestamp, in seconds, when the turn reached a terminal state.

  - `created_at: Integer`

    The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

  - `error: SessionTurnError`

    A customer-safe error. Non-null only for a failed turn.

    - `code: :context_length_exceeded | :session_budget_exceeded | :usage_limit_exceeded | 16 more`

      A stable, machine-readable failure category.

      - `:context_length_exceeded`

        The request exceeds the model's context window.

      - `:session_budget_exceeded`

        The session has reached its usage budget.

      - `:usage_limit_exceeded`

        The organization has reached a usage, plan, or billing limit.

      - `:credit_balance_exhausted`

        The organization has no API credits remaining.

      - `:rate_limit_exceeded`

        The request exceeds the available rate limit.

      - `:flex_unavailable`

        Flex processing is temporarily unavailable.

      - `:server_overloaded`

        The model service is temporarily overloaded.

      - `:cyber_policy`

        The request was rejected by a safety policy.

      - `:misalignment_policy_violation`

        The request was blocked by the safety systems.

      - `:connection_failed`

        The request could not connect to the model service.

      - `:server_error`

        The model service encountered an unexpected error.

      - `:authentication_error`

        The API credentials are invalid or lack the required access.

      - `:invalid_request`

        The request contains invalid input or configuration.

      - `:resource_not_found`

        The requested model or resource is unavailable.

      - `:sandbox_error`

        The request could not complete in its execution environment.

      - `:executor_version_incompatible`

        The executor must be upgraded before it can run this turn.

      - `:active_turn_not_steerable`

        The session cannot accept additional input while a request is running.

      - `:request_timeout`

        The request timed out before the model service responded.

      - `:internal_error`

        An unexpected internal error prevented the session request from completing.

    - `message: String`

      A customer-safe explanation of the failure.

  - `object: :"agent.session.turn"`

    The object type. Always `agent.session.turn`.

    - `:"agent.session.turn"`

  - `session_id: String`

    The ID of the session that owns the turn.

  - `started_at: Integer`

    The Unix timestamp, in seconds, when the turn started.

  - `status: :queued | :in_progress | :waiting | 3 more`

    The current status of the turn.

    - `:queued`

      The turn is waiting to start.

    - `:in_progress`

      The turn is in progress.

    - `:waiting`

      The turn is waiting for external input.

    - `:completed`

      The turn completed successfully.

    - `:failed`

      The turn failed.

    - `:cancelled`

      The turn was cancelled.

  - `subagent_id: String`

    The ID of the subagent that ran the turn, if applicable.

  - `usage: TokenUsage`

    Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `input_tokens: Integer`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails{ cached_tokens}`

      A breakdown of the agent's input token usage.

      - `cached_tokens: Integer`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: Integer`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails{ reasoning_tokens}`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: Integer`

        The number of output tokens used for reasoning.

    - `total_tokens: Integer`

      The total number of input and output tokens used by the agent.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

turn = openai.beta.agents.sessions.subagents.turns.retrieve(
  "turn_id",
  session_id: "session_id",
  subagent_id: "subagent_id"
)

puts(turn)
```

#### Response

```json
{
  "id": "id",
  "agent_id": "agent_id",
  "completed_at": 0,
  "created_at": 0,
  "error": {
    "code": "context_length_exceeded",
    "message": "message"
  },
  "object": "agent.session.turn",
  "session_id": "session_id",
  "started_at": 0,
  "status": "queued",
  "subagent_id": "subagent_id",
  "usage": {
    "input_tokens": 0,
    "input_tokens_details": {
      "cached_tokens": 0
    },
    "output_tokens": 0,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "total_tokens": 0
  }
}
```

# Items

## List subagent turn items

`beta.agents.sessions.subagents.turns.items.list(turn_id, **kwargs) -> CursorPage<AgentSessionItem>`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}/turns/{turn_id}/items`

Lists items belonging to one turn of this subagent. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `session_id: String`

- `subagent_id: String`

- `turn_id: String`

- `after: String`

  Return resources after this resource ID in the selected order.

- `limit: Integer`

  The maximum number of resources to return, between 1 and 100. Defaults to 20.

- `order: :asc | :desc`

  The order in which resources are returned. Defaults to `desc`.

  - `:asc`

    Returns resources in ascending order.

  - `:desc`

    Returns resources in descending order.

### Returns

- `AgentSessionItem = AgentSessionMessage | AgentReasoningItem | AgentFunctionCallItem | 14 more`

  An item associated with a session turn.

  - `class AgentSessionMessage`

    A user or assistant message recorded in a session.

    - `id: String`

      The ID of this item, or null for legacy user messages whose ID was not recorded.

    - `content: Array[AgentSessionMessageContent]`

      The content of the message. User messages contain input text or images; assistant messages contain output text.

      - `class InputText`

        Text supplied by the user.

        - `text: String`

          The text supplied by the user.

        - `type: :input_text`

          The type of the object. Always `input_text`.

          - `:input_text`

      - `class InputImage`

        An image supplied by the user.

        - `image_url: String`

          The URL of the image supplied by the user, which may be a base64-encoded data URL.

        - `type: :input_image`

          The type of the object. Always `input_image`.

          - `:input_image`

      - `class OutputText`

        Text produced by the assistant.

        - `text: String`

          The text produced by the assistant.

        - `type: :output_text`

          The type of the object. Always `output_text`.

          - `:output_text`

    - `phase: :commentary | :final_answer`

      The phase of an assistant message. Null for user messages.

      - `:commentary`

        Commentary produced while the agent works.

      - `:final_answer`

        The agent's final answer.

    - `role: :user | :assistant`

      The role of the message author.

      - `:user`

      - `:assistant`

    - `status: AgentOutputItemStatus`

      The status of the message. User messages are always `completed`.

      - `:in_progress`

        The item is in progress.

      - `:completed`

        The item is complete.

      - `:incomplete`

        The item stopped before completing.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :message`

      The item type. Always `message`.

      - `:message`

  - `class AgentReasoningItem`

    A reasoning item produced by the agent.

    - `id: String`

      The ID of the reasoning item.

    - `status: AgentOutputItemStatus`

      The status of the reasoning item.

    - `summary: Array[SummaryText]`

      The reasoning summaries produced by the agent.

      - `text: String`

        The reasoning summary text.

      - `type: :summary_text`

        The content type. Always `summary_text`.

        - `:summary_text`

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :reasoning`

      The item type. Always `reasoning`.

      - `:reasoning`

  - `class AgentFunctionCallItem`

    A function call produced by the agent.

    - `id: String`

      The ID of the function call item.

    - `arguments: untyped`

      The arguments to pass to the function.

    - `call_id: String`

      The ID used to submit the function result.

    - `name: String`

      The name of the function to call.

    - `status: AgentFunctionCallStatus`

      The status of the function call.

      - `:in_progress`

        The call is in progress.

      - `:completed`

        The call completed successfully.

      - `:failed`

        The call failed.

      - `:incomplete`

        The call stopped before completing.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :function_call`

      The item type. Always `function_call`.

      - `:function_call`

  - `class FunctionCallOutput`

    The result supplied for a function call.

    - `id: String`

      The ID of the function call output item.

    - `call_id: String`

      The ID of the function call that produced this output.

    - `error: String`

      The error message, if the call failed.

    - `output: AgentFunctionCallOutput`

      The function result, if the call succeeded.

      - `String = String`

      - `UnionMember1 = Array[InputContent]`

        - `class InputText`

          Text input recorded in a session item.

          - `text: String`

            The text supplied to the agent.

          - `type: :input_text`

            The type of the object. Always `input_text`.

            - `:input_text`

        - `class InputImage`

          Image input recorded in a session item.

          - `image_url: String`

            The URL of the image supplied to the agent, which may be a base64-encoded data URL.

          - `type: :input_image`

            The type of the object. Always `input_image`.

            - `:input_image`

    - `status: AgentFunctionCallStatus`

      The status of the function call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :function_call_output`

      The item type. Always `function_call_output`.

      - `:function_call_output`

  - `class AgentMessage`

    A message exchanged between agent threads.

    - `id: String`

      The ID of the message.

    - `content: Array[AgentContent]`

      The content exchanged between the agents.

      - `class OutputText`

        A text content part produced by the agent.

        - `text: String`

          The text produced by the agent.

        - `type: :output_text`

          The content type. Always `output_text`.

          - `:output_text`

      - `class EncryptedContent`

        Encrypted content exchanged between agents.

        - `encrypted_content: String`

          The encrypted content payload.

        - `type: :encrypted_content`

          The content type. Always `encrypted_content`.

          - `:encrypted_content`

    - `recipient_agent_id: String`

      The ID or name of the receiving agent.

    - `sender_agent_id: String`

      The ID or name of the sending agent.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :agent_message`

      The item type. Always `agent_message`.

      - `:agent_message`

  - `class AgentMcpCallItem`

    A call to a tool on an MCP server.

    - `id: String`

      The ID of the MCP call item.

    - `arguments: untyped`

      The arguments passed to the MCP tool.

    - `error: untyped`

      The error returned by the MCP tool, if any.

    - `name: String`

      The name of the MCP tool.

    - `output: untyped`

      The output returned by the MCP tool, if any.

    - `server_label: String`

      The label of the MCP server.

    - `status: AgentFunctionCallStatus`

      The status of the MCP tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :mcp_call`

      The item type. Always `mcp_call`.

      - `:mcp_call`

  - `class ComputerUseCall`

    One execution of the platform-provided computer-use capability.

    - `id: String`

      The ID of the activity item.

    - `output: Output{ image_url, type}`

      The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

      - `image_url: String`

        The complete JPEG image as a base64 data URL.

      - `type: :computer_screenshot`

        The content type. Always `computer_screenshot`.

        - `:computer_screenshot`

    - `status: AgentFunctionCallStatus`

      The execution status of the activity.

    - `title: String`

      A model-generated description of the activity, when available.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :computer_use_call`

      The item type. Always `computer_use_call`.

      - `:computer_use_call`

  - `class ComputerUseApprovalRequest`

    A credential-free history record of the emitted login request.

    - `id: String`

      The stable history item ID.

    - `request: Request{ credential_origin, fields, options, 2 more}`

      A registered form awaiting the application's response.

      - `credential_origin: String`

        The registered form or frame origin where values will be entered.

      - `fields: Array[Field{ id, label, required, type}]`

        Controls to render. All submitted values are sensitive.

        - `id: String`

          The field ID to submit as field_id in a fields entry.

        - `label: String`

          The label to display beside the control.

        - `required: bool`

          Whether this control requires a nonempty value.

        - `type: String`

          The rendering type, such as email, password, or text.

      - `options: Array[Option{ id, field_ids, label}]`

        Sign-in methods. Empty for a plain form.

        - `id: String`

          The option ID to submit as selected_option.

        - `field_ids: Array[String]`

          IDs from the registered fields that this method accepts.

        - `label: String`

          The method label to display.

      - `reason: String`

        Why the agent needs the user to sign in.

      - `type: :browser_authentication`

        The type of the object. Always `browser_authentication`.

        - `:browser_authentication`

    - `request_id: String`

    - `turn_id: String`

    - `type: :computer_use_approval_request`

      The item type. Always computer_use_approval_request.

      - `:computer_use_approval_request`

  - `class ComputerUseApprovalRequestResult`

    A credential-free record of an admitted response, not proof of completion.

    - `id: String`

      The stable history item ID.

    - `request_id: String`

      The registered request answered by this item.

    - `response: Submit{ action, selected_option, type} | Cancel{ action, type}`

      The admitted response, without submitted credential values.

      - `class Submit`

        - `action: :submit`

          - `:submit`

        - `selected_option: String`

          The chosen sign-in method, or null when no options were offered.

        - `type: :browser_authentication`

          - `:browser_authentication`

      - `class Cancel`

        - `action: :cancel`

          - `:cancel`

        - `type: :browser_authentication`

          - `:browser_authentication`

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :computer_use_approval_request_result`

      - `:computer_use_approval_request_result`

  - `class AgentWebSearchCallItem`

    A web search call produced by the agent.

    - `id: String`

      The ID of the web search call.

    - `action: WebSearchAction`

      The action performed by the web search tool.

      - `class Search`

        A search query or group of search queries.

        - `queries: Array[String]`

          The search queries, when multiple queries were used.

        - `query: String`

          The search query, when a single query was used.

        - `type: :search`

          The type of the object. Always `search`.

          - `:search`

      - `class OpenPage`

        Opens a web page.

        - `type: :open_page`

          The type of the object. Always `open_page`.

          - `:open_page`

        - `url: String`

          The URL of the page that was opened.

      - `class FindInPage`

        Finds text within a web page.

        - `pattern: String`

          The text pattern that was searched for.

        - `type: :find_in_page`

          The type of the object. Always `find_in_page`.

          - `:find_in_page`

        - `url: String`

          The URL of the page that was searched.

      - `class Other`

        Another web search action.

        - `type: :other`

          The type of the object. Always `other`.

          - `:other`

    - `status: AgentOutputItemStatus`

      The status of the web search call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :web_search_call`

      The item type. Always `web_search_call`.

      - `:web_search_call`

  - `class AgentCommandExecutionItem`

    A command execution produced by the agent.

    - `id: String`

      The ID of the command execution item.

    - `command: String`

      The command that was executed.

    - `cwd: String`

      The working directory used to execute the command.

    - `duration_ms: Integer`

      The command duration in milliseconds.

    - `exit_code: Integer`

      The process exit code, if the command completed.

    - `output: String`

      The command output, if available.

    - `status: AgentFunctionCallStatus`

      The status of the command execution.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :command_execution`

      The item type. Always `command_execution`.

      - `:command_execution`

  - `class AgentCreateSubagentCallItem`

    A request to spawn a subagent.

    - `id: String`

      The ID of the tool call item.

    - `agent_id: String`

      The ID of the agent that requested the subagent.

    - `content: Array[AgentContent]`

      The task given to the spawned agent.

      - `class OutputText`

        A text content part produced by the agent.

      - `class EncryptedContent`

        Encrypted content exchanged between agents.

    - `model: String`

      The model requested for the spawned agent.

    - `reasoning_effort: String`

      The reasoning effort requested for the spawned agent.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :create_subagent_call`

      The item type. Always `create_subagent_call`.

      - `:create_subagent_call`

        The current public item type.

  - `class AgentSendSubagentInputCallItem`

    A request to send input to another agent.

    - `id: String`

      The ID of the tool call item.

    - `content: Array[AgentContent]`

      The input sent to the receiving agent.

      - `class OutputText`

        A text content part produced by the agent.

      - `class EncryptedContent`

        Encrypted content exchanged between agents.

    - `recipient_agent_id: String`

      The ID of the agent receiving the input.

    - `sender_agent_id: String`

      The ID of the agent sending the input.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :send_subagent_input_call`

      The item type. Always `send_subagent_input_call`.

      - `:send_subagent_input_call`

        The current public item type.

  - `class AgentResumeSubagentCallItem`

    A request to resume a subagent.

    - `id: String`

      The ID of the tool call item.

    - `recipient_agent_id: String`

      The ID of the agent to resume.

    - `sender_agent_id: String`

      The ID of the agent requesting the resume.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :resume_subagent_call`

      The item type. Always `resume_subagent_call`.

      - `:resume_subagent_call`

        The current public item type.

  - `class AgentWaitForSubagentsCallItem`

    A request to wait for one or more subagents.

    - `id: String`

      The ID of the tool call item.

    - `recipient_agent_ids: Array[String]`

      The IDs of the agents to wait for.

    - `sender_agent_id: String`

      The ID of the agent waiting for results.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :wait_for_subagents_call`

      The item type. Always `wait_for_subagents_call`.

      - `:wait_for_subagents_call`

        The current public item type.

  - `class AgentInterruptSubagentCallItem`

    A request to interrupt a subagent's current turn. The subagent remains available.

    - `id: String`

      The ID of the tool call item.

    - `recipient_agent_id: String`

      The ID of the agent to interrupt.

    - `sender_agent_id: String`

      The ID of the agent requesting the interrupt.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :interrupt_subagent_call`

      The item type. Always `interrupt_subagent_call`.

      - `:interrupt_subagent_call`

        The current public item type.

  - `class AgentCloseSubagentCallItem`

    A request to close a subagent.

    - `id: String`

      The ID of the tool call item.

    - `recipient_agent_id: String`

      The ID of the agent to close.

    - `sender_agent_id: String`

      The ID of the agent requesting the close.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :close_subagent_call`

      The item type. Always `close_subagent_call`.

      - `:close_subagent_call`

        The current public item type.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.beta.agents.sessions.subagents.turns.items.list(
  "turn_id",
  session_id: "session_id",
  subagent_id: "subagent_id"
)

puts(page)
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "content": [
        {
          "text": "text",
          "type": "input_text"
        }
      ],
      "phase": "commentary",
      "role": "user",
      "status": "in_progress",
      "turn_id": "turn_id",
      "type": "message"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

# Turns

## List agent session turns

`beta.agents.sessions.turns.list(session_id, **kwargs) -> CursorPage<Turn>`

**get** `/agents/sessions/{session_id}/turns`

Lists turns by creation time and turn ID. The after cursor is exclusive in the selected order. See [session turns](/api/docs/guides/agents-api/sessions/manage#inspect-session-turns).

### Parameters

- `session_id: String`

- `after: String`

  Return resources after this resource ID in the selected order.

- `limit: Integer`

  The maximum number of resources to return, between 1 and 100. Defaults to 20.

- `order: :asc | :desc`

  The order in which resources are returned. Defaults to `desc`.

  - `:asc`

    Returns resources in ascending order.

  - `:desc`

    Returns resources in descending order.

### Returns

- `class Turn`

  The canonical public representation of a session turn.

  - `id: String`

    The ID of the turn.

  - `agent_id: String`

    The ID of the agent that ran the turn.

  - `completed_at: Integer`

    The Unix timestamp, in seconds, when the turn reached a terminal state.

  - `created_at: Integer`

    The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

  - `error: SessionTurnError`

    A customer-safe error. Non-null only for a failed turn.

    - `code: :context_length_exceeded | :session_budget_exceeded | :usage_limit_exceeded | 16 more`

      A stable, machine-readable failure category.

      - `:context_length_exceeded`

        The request exceeds the model's context window.

      - `:session_budget_exceeded`

        The session has reached its usage budget.

      - `:usage_limit_exceeded`

        The organization has reached a usage, plan, or billing limit.

      - `:credit_balance_exhausted`

        The organization has no API credits remaining.

      - `:rate_limit_exceeded`

        The request exceeds the available rate limit.

      - `:flex_unavailable`

        Flex processing is temporarily unavailable.

      - `:server_overloaded`

        The model service is temporarily overloaded.

      - `:cyber_policy`

        The request was rejected by a safety policy.

      - `:misalignment_policy_violation`

        The request was blocked by the safety systems.

      - `:connection_failed`

        The request could not connect to the model service.

      - `:server_error`

        The model service encountered an unexpected error.

      - `:authentication_error`

        The API credentials are invalid or lack the required access.

      - `:invalid_request`

        The request contains invalid input or configuration.

      - `:resource_not_found`

        The requested model or resource is unavailable.

      - `:sandbox_error`

        The request could not complete in its execution environment.

      - `:executor_version_incompatible`

        The executor must be upgraded before it can run this turn.

      - `:active_turn_not_steerable`

        The session cannot accept additional input while a request is running.

      - `:request_timeout`

        The request timed out before the model service responded.

      - `:internal_error`

        An unexpected internal error prevented the session request from completing.

    - `message: String`

      A customer-safe explanation of the failure.

  - `object: :"agent.session.turn"`

    The object type. Always `agent.session.turn`.

    - `:"agent.session.turn"`

  - `session_id: String`

    The ID of the session that owns the turn.

  - `started_at: Integer`

    The Unix timestamp, in seconds, when the turn started.

  - `status: :queued | :in_progress | :waiting | 3 more`

    The current status of the turn.

    - `:queued`

      The turn is waiting to start.

    - `:in_progress`

      The turn is in progress.

    - `:waiting`

      The turn is waiting for external input.

    - `:completed`

      The turn completed successfully.

    - `:failed`

      The turn failed.

    - `:cancelled`

      The turn was cancelled.

  - `subagent_id: String`

    The ID of the subagent that ran the turn, if applicable.

  - `usage: TokenUsage`

    Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `input_tokens: Integer`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails{ cached_tokens}`

      A breakdown of the agent's input token usage.

      - `cached_tokens: Integer`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: Integer`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails{ reasoning_tokens}`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: Integer`

        The number of output tokens used for reasoning.

    - `total_tokens: Integer`

      The total number of input and output tokens used by the agent.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.beta.agents.sessions.turns.list("session_id")

puts(page)
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "agent_id": "agent_id",
      "completed_at": 0,
      "created_at": 0,
      "error": {
        "code": "context_length_exceeded",
        "message": "message"
      },
      "object": "agent.session.turn",
      "session_id": "session_id",
      "started_at": 0,
      "status": "queued",
      "subagent_id": "subagent_id",
      "usage": {
        "input_tokens": 0,
        "input_tokens_details": {
          "cached_tokens": 0
        },
        "output_tokens": 0,
        "output_tokens_details": {
          "reasoning_tokens": 0
        },
        "total_tokens": 0
      }
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve an agent session turn

`beta.agents.sessions.turns.retrieve(turn_id, **kwargs) -> Turn`

**get** `/agents/sessions/{session_id}/turns/{turn_id}`

Retrieves a turn's current status, timestamps, usage, and error. Returns 404 if the turn does not belong to the session. See [session turns](/api/docs/guides/agents-api/sessions/manage#inspect-session-turns).

### Parameters

- `session_id: String`

- `turn_id: String`

### Returns

- `class Turn`

  The canonical public representation of a session turn.

  - `id: String`

    The ID of the turn.

  - `agent_id: String`

    The ID of the agent that ran the turn.

  - `completed_at: Integer`

    The Unix timestamp, in seconds, when the turn reached a terminal state.

  - `created_at: Integer`

    The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

  - `error: SessionTurnError`

    A customer-safe error. Non-null only for a failed turn.

    - `code: :context_length_exceeded | :session_budget_exceeded | :usage_limit_exceeded | 16 more`

      A stable, machine-readable failure category.

      - `:context_length_exceeded`

        The request exceeds the model's context window.

      - `:session_budget_exceeded`

        The session has reached its usage budget.

      - `:usage_limit_exceeded`

        The organization has reached a usage, plan, or billing limit.

      - `:credit_balance_exhausted`

        The organization has no API credits remaining.

      - `:rate_limit_exceeded`

        The request exceeds the available rate limit.

      - `:flex_unavailable`

        Flex processing is temporarily unavailable.

      - `:server_overloaded`

        The model service is temporarily overloaded.

      - `:cyber_policy`

        The request was rejected by a safety policy.

      - `:misalignment_policy_violation`

        The request was blocked by the safety systems.

      - `:connection_failed`

        The request could not connect to the model service.

      - `:server_error`

        The model service encountered an unexpected error.

      - `:authentication_error`

        The API credentials are invalid or lack the required access.

      - `:invalid_request`

        The request contains invalid input or configuration.

      - `:resource_not_found`

        The requested model or resource is unavailable.

      - `:sandbox_error`

        The request could not complete in its execution environment.

      - `:executor_version_incompatible`

        The executor must be upgraded before it can run this turn.

      - `:active_turn_not_steerable`

        The session cannot accept additional input while a request is running.

      - `:request_timeout`

        The request timed out before the model service responded.

      - `:internal_error`

        An unexpected internal error prevented the session request from completing.

    - `message: String`

      A customer-safe explanation of the failure.

  - `object: :"agent.session.turn"`

    The object type. Always `agent.session.turn`.

    - `:"agent.session.turn"`

  - `session_id: String`

    The ID of the session that owns the turn.

  - `started_at: Integer`

    The Unix timestamp, in seconds, when the turn started.

  - `status: :queued | :in_progress | :waiting | 3 more`

    The current status of the turn.

    - `:queued`

      The turn is waiting to start.

    - `:in_progress`

      The turn is in progress.

    - `:waiting`

      The turn is waiting for external input.

    - `:completed`

      The turn completed successfully.

    - `:failed`

      The turn failed.

    - `:cancelled`

      The turn was cancelled.

  - `subagent_id: String`

    The ID of the subagent that ran the turn, if applicable.

  - `usage: TokenUsage`

    Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `input_tokens: Integer`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails{ cached_tokens}`

      A breakdown of the agent's input token usage.

      - `cached_tokens: Integer`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: Integer`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails{ reasoning_tokens}`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: Integer`

        The number of output tokens used for reasoning.

    - `total_tokens: Integer`

      The total number of input and output tokens used by the agent.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

turn = openai.beta.agents.sessions.turns.retrieve("turn_id", session_id: "session_id")

puts(turn)
```

#### Response

```json
{
  "id": "id",
  "agent_id": "agent_id",
  "completed_at": 0,
  "created_at": 0,
  "error": {
    "code": "context_length_exceeded",
    "message": "message"
  },
  "object": "agent.session.turn",
  "session_id": "session_id",
  "started_at": 0,
  "status": "queued",
  "subagent_id": "subagent_id",
  "usage": {
    "input_tokens": 0,
    "input_tokens_details": {
      "cached_tokens": 0
    },
    "output_tokens": 0,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "total_tokens": 0
  }
}
```

## Domain Types

### Turn

- `class Turn`

  The canonical public representation of a session turn.

  - `id: String`

    The ID of the turn.

  - `agent_id: String`

    The ID of the agent that ran the turn.

  - `completed_at: Integer`

    The Unix timestamp, in seconds, when the turn reached a terminal state.

  - `created_at: Integer`

    The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

  - `error: SessionTurnError`

    A customer-safe error. Non-null only for a failed turn.

    - `code: :context_length_exceeded | :session_budget_exceeded | :usage_limit_exceeded | 16 more`

      A stable, machine-readable failure category.

      - `:context_length_exceeded`

        The request exceeds the model's context window.

      - `:session_budget_exceeded`

        The session has reached its usage budget.

      - `:usage_limit_exceeded`

        The organization has reached a usage, plan, or billing limit.

      - `:credit_balance_exhausted`

        The organization has no API credits remaining.

      - `:rate_limit_exceeded`

        The request exceeds the available rate limit.

      - `:flex_unavailable`

        Flex processing is temporarily unavailable.

      - `:server_overloaded`

        The model service is temporarily overloaded.

      - `:cyber_policy`

        The request was rejected by a safety policy.

      - `:misalignment_policy_violation`

        The request was blocked by the safety systems.

      - `:connection_failed`

        The request could not connect to the model service.

      - `:server_error`

        The model service encountered an unexpected error.

      - `:authentication_error`

        The API credentials are invalid or lack the required access.

      - `:invalid_request`

        The request contains invalid input or configuration.

      - `:resource_not_found`

        The requested model or resource is unavailable.

      - `:sandbox_error`

        The request could not complete in its execution environment.

      - `:executor_version_incompatible`

        The executor must be upgraded before it can run this turn.

      - `:active_turn_not_steerable`

        The session cannot accept additional input while a request is running.

      - `:request_timeout`

        The request timed out before the model service responded.

      - `:internal_error`

        An unexpected internal error prevented the session request from completing.

    - `message: String`

      A customer-safe explanation of the failure.

  - `object: :"agent.session.turn"`

    The object type. Always `agent.session.turn`.

    - `:"agent.session.turn"`

  - `session_id: String`

    The ID of the session that owns the turn.

  - `started_at: Integer`

    The Unix timestamp, in seconds, when the turn started.

  - `status: :queued | :in_progress | :waiting | 3 more`

    The current status of the turn.

    - `:queued`

      The turn is waiting to start.

    - `:in_progress`

      The turn is in progress.

    - `:waiting`

      The turn is waiting for external input.

    - `:completed`

      The turn completed successfully.

    - `:failed`

      The turn failed.

    - `:cancelled`

      The turn was cancelled.

  - `subagent_id: String`

    The ID of the subagent that ran the turn, if applicable.

  - `usage: TokenUsage`

    Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `input_tokens: Integer`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails{ cached_tokens}`

      A breakdown of the agent's input token usage.

      - `cached_tokens: Integer`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: Integer`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails{ reasoning_tokens}`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: Integer`

        The number of output tokens used for reasoning.

    - `total_tokens: Integer`

      The total number of input and output tokens used by the agent.
