<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/agents/subresources/sessions/subresources/events/methods/stream/ -->

## Stream agent session events

`beta.agents.sessions.events.stream(strsession_id)  -> AgentSessionEvent`

**get** `/agents/sessions/{session_id}/events`

Streams live events for an agent session. See [session events](/api/docs/guides/agents-api/sessions/events).

- `session_id: str`

- `AgentSessionEvent`

  An event emitted by a Managed Agents session.

  - `class AgentSessionErrorEvent: …`

    Emitted when a turn or session fails.

    - `error: SessionError`

      The error that occurred.

      - `code: Optional[str]`

        The machine-readable error code, if any.

      - `message: str`

        A customer-safe explanation of the error.

      - `param: Optional[str]`

        The request parameter associated with the error, if any.

      - `type: str`

        The error type.

    - `event_id: str`

      The unique ID of the event.

    - `session_id: str`

      The ID of the session associated with the event.

    - `type: Literal["error"]`

      The type of the object. Always `error`.

      - `"error"`

  - `class AgentSessionEnvironmentReadyEvent: …`

    Emitted when a hosted session environment is ready to connect.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

      - `id: str`

        The public ID of the environment.

      - `error: Optional[Error]`

        The error reported while preparing the environment, if any.

        - `code: str`

          A machine-readable error code.

        - `message: str`

          A human-readable error message.

        - `type: str`

          The error type.

      - `status: Literal["pending", "ready", "connected", 2 more]`

        The environment's connection status.

        - `"pending"`

          The environment is being prepared.

        - `"ready"`

          The environment is ready to connect.

        - `"connected"`

          The environment is connected.

        - `"disconnected"`

          The environment is disconnected.

        - `"failed"`

          The environment failed to connect.

      - `type: str`

        The environment type.

    - `event_id: str`

      The unique ID of the event.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.environment.ready"]`

      The type of the object. Always `agent.session.environment.ready`.

      - `"agent.session.environment.ready"`

  - `class AgentSessionEnvironmentResetEvent: …`

    Emitted after a hosted sandbox is replaced. Conversation history survives; changes to the previous sandbox's files and processes do not.

    - `environment_id: str`

      The stable environment ID, retained across sandbox replacements.

    - `event_id: str`

      The unique ID of the event.

    - `reset_count: int`

      Monotonically increasing reset number. Repeated notifications share this number.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The associated turn, when applicable.

    - `type: Literal["agent.session.environment.reset"]`

      The type of the object. Always `agent.session.environment.reset`.

      - `"agent.session.environment.reset"`

  - `class AgentOutputCommandExecutionOutputDeltaEvent: …`

    Emitted when command execution produces an output delta.

    - `delta: str`

      The output text that was appended.

    - `event_id: str`

      The unique ID of the event.

    - `item_id: str`

      The ID of the command execution item.

    - `output_index: int`

      The index of the item in the turn output.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.output.command_execution_output.delta"]`

      The type of the object. Always `agent.output.command_execution_output.delta`.

      - `"agent.output.command_execution_output.delta"`

  - `class AgentSessionCreatedEvent: …`

    Emitted when a session is created.

    - `event_id: str`

      The unique ID of the event.

    - `session: AgentSession`

      The session that was created.

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

    - `type: Literal["agent.session.created"]`

      The type of the object. Always `agent.session.created`.

      - `"agent.session.created"`

  - `class AgentSessionTurnCreatedEvent: …`

    Emitted when a turn is created.

    - `event_id: str`

      The unique ID of the event.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn: Turn`

      The turn at the time it was created.

      - `id: str`

        The ID of the turn.

      - `agent_id: str`

        The ID of the agent that ran the turn.

      - `completed_at: Optional[int]`

        The Unix timestamp, in seconds, when the turn reached a terminal state.

      - `created_at: int`

        The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

      - `error: Optional[SessionTurnError]`

        A customer-safe error. Non-null only for a failed turn.

        - `code: Literal["context_length_exceeded", "session_budget_exceeded", "usage_limit_exceeded", 16 more]`

          A stable, machine-readable failure category.

          - `"context_length_exceeded"`

            The request exceeds the model's context window.

          - `"session_budget_exceeded"`

            The session has reached its usage budget.

          - `"usage_limit_exceeded"`

            The organization has reached a usage, plan, or billing limit.

          - `"credit_balance_exhausted"`

            The organization has no API credits remaining.

          - `"rate_limit_exceeded"`

            The request exceeds the available rate limit.

          - `"flex_unavailable"`

            Flex processing is temporarily unavailable.

          - `"server_overloaded"`

            The model service is temporarily overloaded.

          - `"cyber_policy"`

            The request was rejected by a safety policy.

          - `"misalignment_policy_violation"`

            The request was blocked by the safety systems.

          - `"connection_failed"`

            The request could not connect to the model service.

          - `"server_error"`

            The model service encountered an unexpected error.

          - `"authentication_error"`

            The API credentials are invalid or lack the required access.

          - `"invalid_request"`

            The request contains invalid input or configuration.

          - `"resource_not_found"`

            The requested model or resource is unavailable.

          - `"sandbox_error"`

            The request could not complete in its execution environment.

          - `"executor_version_incompatible"`

            The executor must be upgraded before it can run this turn.

          - `"active_turn_not_steerable"`

            The session cannot accept additional input while a request is running.

          - `"request_timeout"`

            The request timed out before the model service responded.

          - `"internal_error"`

            An unexpected internal error prevented the session request from completing.

        - `message: str`

          A customer-safe explanation of the failure.

      - `object: Literal["agent.session.turn"]`

        The object type. Always `agent.session.turn`.

        - `"agent.session.turn"`

      - `session_id: str`

        The ID of the session that owns the turn.

      - `started_at: Optional[int]`

        The Unix timestamp, in seconds, when the turn started.

      - `status: Literal["queued", "in_progress", "waiting", 3 more]`

        The current status of the turn.

        - `"queued"`

          The turn is waiting to start.

        - `"in_progress"`

          The turn is in progress.

        - `"waiting"`

          The turn is waiting for external input.

        - `"completed"`

          The turn completed successfully.

        - `"failed"`

          The turn failed.

        - `"cancelled"`

          The turn was cancelled.

      - `subagent_id: Optional[str]`

        The ID of the subagent that ran the turn, if applicable.

      - `usage: Optional[TokenUsage]`

        Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `turn_id: str`

      The ID of the turn associated with the event.

    - `type: Literal["agent.session.turn.created"]`

      The type of the object. Always `agent.session.turn.created`.

      - `"agent.session.turn.created"`

  - `class AgentSessionTurnInProgressEvent: …`

    Emitted when a turn starts running.

    - `event_id: str`

      The unique ID of the event.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn: Turn`

      The turn at the time it started running.

    - `turn_id: str`

      The ID of the turn associated with the event.

    - `type: Literal["agent.session.turn.in_progress"]`

      The type of the object. Always `agent.session.turn.in_progress`.

      - `"agent.session.turn.in_progress"`

  - `class AgentSessionTurnCompletedEvent: …`

    Emitted when a turn completes.

    - `event_id: str`

      The unique ID of the event.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn: Turn`

      The completed turn.

    - `turn_id: str`

      The ID of the turn associated with the event.

    - `type: Literal["agent.session.turn.completed"]`

      The type of the object. Always `agent.session.turn.completed`.

      - `"agent.session.turn.completed"`

    - `usage: Optional[TokenUsage]`

      Token usage by the root agent during the turn, when available.

  - `class AgentSessionTurnFailedEvent: …`

    Emitted when a turn fails.

    - `event_id: str`

      The unique ID of the event.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn: Turn`

      The failed turn.

    - `turn_id: str`

      The ID of the turn associated with the event.

    - `type: Literal["agent.session.turn.failed"]`

      The type of the object. Always `agent.session.turn.failed`.

      - `"agent.session.turn.failed"`

    - `usage: Optional[TokenUsage]`

      Token usage by the root agent during the turn, when available.

  - `class AgentSessionTurnCancelledEvent: …`

    Emitted when a turn is cancelled.

    - `event_id: str`

      The unique ID of the event.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn: Turn`

      The cancelled turn.

    - `turn_id: str`

      The ID of the turn associated with the event.

    - `type: Literal["agent.session.turn.cancelled"]`

      The type of the object. Always `agent.session.turn.cancelled`.

      - `"agent.session.turn.cancelled"`

    - `usage: Optional[TokenUsage]`

      Token usage by the root agent during the turn, when available.

  - `class AgentSessionTurnItemAddedEvent: …`

    Emitted when an item is added to a turn.

    - `event_id: str`

      The unique ID of the event.

    - `item: AgentSessionItem`

      The item that was added.

      - `class AgentSessionMessage: …`

        A user or assistant message recorded in a session.

        - `id: Optional[str]`

          The ID of this item, or null for legacy user messages whose ID was not recorded.

        - `content: List[AgentSessionMessageContent]`

          The content of the message. User messages contain input text or images; assistant messages contain output text.

          - `class MessageContentResourceInputText: …`

            Text supplied by the user.

            - `text: str`

              The text supplied by the user.

            - `type: Literal["input_text"]`

              The type of the object. Always `input_text`.

              - `"input_text"`

          - `class MessageContentResourceInputImage: …`

            An image supplied by the user.

            - `image_url: str`

              The URL of the image supplied by the user, which may be a base64-encoded data URL.

            - `type: Literal["input_image"]`

              The type of the object. Always `input_image`.

              - `"input_image"`

          - `class MessageContentResourceOutputText: …`

            Text produced by the assistant.

            - `text: str`

              The text produced by the assistant.

            - `type: Literal["output_text"]`

              The type of the object. Always `output_text`.

              - `"output_text"`

        - `phase: Optional[Literal["commentary", "final_answer"]]`

          The phase of an assistant message. Null for user messages.

          - `"commentary"`

            Commentary produced while the agent works.

          - `"final_answer"`

            The agent's final answer.

        - `role: Literal["user", "assistant"]`

          The role of the message author.

          - `"user"`

          - `"assistant"`

        - `status: AgentOutputItemStatus`

          The status of the message. User messages are always `completed`.

          - `"in_progress"`

            The item is in progress.

          - `"completed"`

            The item is complete.

          - `"incomplete"`

            The item stopped before completing.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["message"]`

          The item type. Always `message`.

          - `"message"`

      - `class AgentReasoningItem: …`

        A reasoning item produced by the agent.

        - `id: str`

          The ID of the reasoning item.

        - `status: Optional[AgentOutputItemStatus]`

          The status of the reasoning item.

        - `summary: List[SummaryText]`

          The reasoning summaries produced by the agent.

          - `text: str`

            The reasoning summary text.

          - `type: Literal["summary_text"]`

            The content type. Always `summary_text`.

            - `"summary_text"`

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["reasoning"]`

          The item type. Always `reasoning`.

          - `"reasoning"`

      - `class AgentFunctionCallItem: …`

        A function call produced by the agent.

        - `id: str`

          The ID of the function call item.

        - `arguments: object`

          The arguments to pass to the function.

        - `call_id: str`

          The ID used to submit the function result.

        - `name: str`

          The name of the function to call.

        - `status: AgentFunctionCallStatus`

          The status of the function call.

          - `"in_progress"`

            The call is in progress.

          - `"completed"`

            The call completed successfully.

          - `"failed"`

            The call failed.

          - `"incomplete"`

            The call stopped before completing.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["function_call"]`

          The item type. Always `function_call`.

          - `"function_call"`

      - `class FunctionCallOutputItemResource: …`

        The result supplied for a function call.

        - `id: str`

          The ID of the function call output item.

        - `call_id: str`

          The ID of the function call that produced this output.

        - `error: Optional[str]`

          The error message, if the call failed.

        - `output: Optional[AgentFunctionCallOutput]`

          The function result, if the call succeeded.

          - `str`

          - `List[InputContent]`

            - `class InputContentResourceInputText: …`

              Text input recorded in a session item.

              - `text: str`

                The text supplied to the agent.

              - `type: Literal["input_text"]`

                The type of the object. Always `input_text`.

                - `"input_text"`

            - `class InputContentResourceInputImage: …`

              Image input recorded in a session item.

              - `image_url: str`

                The URL of the image supplied to the agent, which may be a base64-encoded data URL.

              - `type: Literal["input_image"]`

                The type of the object. Always `input_image`.

                - `"input_image"`

        - `status: AgentFunctionCallStatus`

          The status of the function call.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["function_call_output"]`

          The item type. Always `function_call_output`.

          - `"function_call_output"`

      - `class AgentMessageItemResource: …`

        A message exchanged between agent threads.

        - `id: str`

          The ID of the message.

        - `content: List[AgentContent]`

          The content exchanged between the agents.

          - `class OutputText: …`

            A text content part produced by the agent.

            - `text: str`

              The text produced by the agent.

            - `type: Literal["output_text"]`

              The content type. Always `output_text`.

              - `"output_text"`

          - `class EncryptedContentResource: …`

            Encrypted content exchanged between agents.

            - `encrypted_content: str`

              The encrypted content payload.

            - `type: Literal["encrypted_content"]`

              The content type. Always `encrypted_content`.

              - `"encrypted_content"`

        - `recipient_agent_id: str`

          The ID or name of the receiving agent.

        - `sender_agent_id: str`

          The ID or name of the sending agent.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["agent_message"]`

          The item type. Always `agent_message`.

          - `"agent_message"`

      - `class AgentMcpCallItem: …`

        A call to a tool on an MCP server.

        - `id: str`

          The ID of the MCP call item.

        - `arguments: object`

          The arguments passed to the MCP tool.

        - `error: object`

          The error returned by the MCP tool, if any.

        - `name: str`

          The name of the MCP tool.

        - `output: object`

          The output returned by the MCP tool, if any.

        - `server_label: str`

          The label of the MCP server.

        - `status: AgentFunctionCallStatus`

          The status of the MCP tool call.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["mcp_call"]`

          The item type. Always `mcp_call`.

          - `"mcp_call"`

      - `class ComputerUseCallItemResource: …`

        One execution of the platform-provided computer-use capability.

        - `id: str`

          The ID of the activity item.

        - `output: Optional[ComputerUseCallItemResourceOutput]`

          The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

          - `image_url: str`

            The complete JPEG image as a base64 data URL.

          - `type: Literal["computer_screenshot"]`

            The content type. Always `computer_screenshot`.

            - `"computer_screenshot"`

        - `status: AgentFunctionCallStatus`

          The execution status of the activity.

        - `title: Optional[str]`

          A model-generated description of the activity, when available.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["computer_use_call"]`

          The item type. Always `computer_use_call`.

          - `"computer_use_call"`

      - `class BrowserAuthenticationRequestItemResource: …`

        A credential-free history record of the emitted login request.

        - `id: str`

          The stable history item ID.

        - `request: BrowserAuthenticationRequestItemResourceRequest`

          A registered form awaiting the application's response.

          - `credential_origin: Optional[str]`

            The registered form or frame origin where values will be entered.

          - `fields: List[BrowserAuthenticationRequestItemResourceRequestField]`

            Controls to render. All submitted values are sensitive.

            - `id: str`

              The field ID to submit as field_id in a fields entry.

            - `label: str`

              The label to display beside the control.

            - `required: bool`

              Whether this control requires a nonempty value.

            - `type: str`

              The rendering type, such as email, password, or text.

          - `options: List[BrowserAuthenticationRequestItemResourceRequestOption]`

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

        - `request_id: str`

        - `turn_id: str`

        - `type: Literal["computer_use_approval_request"]`

          The item type. Always computer_use_approval_request.

          - `"computer_use_approval_request"`

      - `class ComputerUseApprovalRequestResultItemResource: …`

        A credential-free record of an admitted response, not proof of completion.

        - `id: str`

          The stable history item ID.

        - `request_id: str`

          The registered request answered by this item.

        - `response: ComputerUseApprovalRequestResultItemResourceResponse`

          The admitted response, without submitted credential values.

          - `class ComputerUseApprovalRequestResultItemResourceResponseComputerUseApprovalResponseKindResourceBrowserAuthenticationSubmitResource: …`

            - `action: Literal["submit"]`

              - `"submit"`

            - `selected_option: Optional[str]`

              The chosen sign-in method, or null when no options were offered.

            - `type: Literal["browser_authentication"]`

              - `"browser_authentication"`

          - `class ComputerUseApprovalRequestResultItemResourceResponseComputerUseApprovalResponseKindResourceBrowserAuthenticationCancelResource: …`

            - `action: Literal["cancel"]`

              - `"cancel"`

            - `type: Literal["browser_authentication"]`

              - `"browser_authentication"`

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["computer_use_approval_request_result"]`

          - `"computer_use_approval_request_result"`

      - `class AgentWebSearchCallItem: …`

        A web search call produced by the agent.

        - `id: str`

          The ID of the web search call.

        - `action: Optional[WebSearchAction]`

          The action performed by the web search tool.

          - `class WebSearchActionResourceSearch: …`

            A search query or group of search queries.

            - `queries: Optional[List[str]]`

              The search queries, when multiple queries were used.

            - `query: Optional[str]`

              The search query, when a single query was used.

            - `type: Literal["search"]`

              The type of the object. Always `search`.

              - `"search"`

          - `class WebSearchActionResourceOpenPage: …`

            Opens a web page.

            - `type: Literal["open_page"]`

              The type of the object. Always `open_page`.

              - `"open_page"`

            - `url: Optional[str]`

              The URL of the page that was opened.

          - `class WebSearchActionResourceFindInPage: …`

            Finds text within a web page.

            - `pattern: Optional[str]`

              The text pattern that was searched for.

            - `type: Literal["find_in_page"]`

              The type of the object. Always `find_in_page`.

              - `"find_in_page"`

            - `url: Optional[str]`

              The URL of the page that was searched.

          - `class WebSearchActionResourceOther: …`

            Another web search action.

            - `type: Literal["other"]`

              The type of the object. Always `other`.

              - `"other"`

        - `status: AgentOutputItemStatus`

          The status of the web search call.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["web_search_call"]`

          The item type. Always `web_search_call`.

          - `"web_search_call"`

      - `class AgentCommandExecutionItem: …`

        A command execution produced by the agent.

        - `id: str`

          The ID of the command execution item.

        - `command: str`

          The command that was executed.

        - `cwd: Optional[str]`

          The working directory used to execute the command.

        - `duration_ms: Optional[int]`

          The command duration in milliseconds.

        - `exit_code: Optional[int]`

          The process exit code, if the command completed.

        - `output: Optional[str]`

          The command output, if available.

        - `status: AgentFunctionCallStatus`

          The status of the command execution.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["command_execution"]`

          The item type. Always `command_execution`.

          - `"command_execution"`

      - `class AgentCreateSubagentCallItem: …`

        A request to spawn a subagent.

        - `id: str`

          The ID of the tool call item.

        - `agent_id: str`

          The ID of the agent that requested the subagent.

        - `content: List[AgentContent]`

          The task given to the spawned agent.

          - `class OutputText: …`

            A text content part produced by the agent.

          - `class EncryptedContentResource: …`

            Encrypted content exchanged between agents.

        - `model: Optional[str]`

          The model requested for the spawned agent.

        - `reasoning_effort: Optional[str]`

          The reasoning effort requested for the spawned agent.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["create_subagent_call"]`

          The item type. Always `create_subagent_call`.

          - `"create_subagent_call"`

            The current public item type.

      - `class AgentSendSubagentInputCallItem: …`

        A request to send input to another agent.

        - `id: str`

          The ID of the tool call item.

        - `content: List[AgentContent]`

          The input sent to the receiving agent.

          - `class OutputText: …`

            A text content part produced by the agent.

          - `class EncryptedContentResource: …`

            Encrypted content exchanged between agents.

        - `recipient_agent_id: str`

          The ID of the agent receiving the input.

        - `sender_agent_id: str`

          The ID of the agent sending the input.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["send_subagent_input_call"]`

          The item type. Always `send_subagent_input_call`.

          - `"send_subagent_input_call"`

            The current public item type.

      - `class AgentResumeSubagentCallItem: …`

        A request to resume a subagent.

        - `id: str`

          The ID of the tool call item.

        - `recipient_agent_id: str`

          The ID of the agent to resume.

        - `sender_agent_id: str`

          The ID of the agent requesting the resume.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["resume_subagent_call"]`

          The item type. Always `resume_subagent_call`.

          - `"resume_subagent_call"`

            The current public item type.

      - `class AgentWaitForSubagentsCallItem: …`

        A request to wait for one or more subagents.

        - `id: str`

          The ID of the tool call item.

        - `recipient_agent_ids: List[str]`

          The IDs of the agents to wait for.

        - `sender_agent_id: str`

          The ID of the agent waiting for results.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["wait_for_subagents_call"]`

          The item type. Always `wait_for_subagents_call`.

          - `"wait_for_subagents_call"`

            The current public item type.

      - `class AgentInterruptSubagentCallItem: …`

        A request to interrupt a subagent's current turn. The subagent remains available.

        - `id: str`

          The ID of the tool call item.

        - `recipient_agent_id: str`

          The ID of the agent to interrupt.

        - `sender_agent_id: str`

          The ID of the agent requesting the interrupt.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["interrupt_subagent_call"]`

          The item type. Always `interrupt_subagent_call`.

          - `"interrupt_subagent_call"`

            The current public item type.

      - `class AgentCloseSubagentCallItem: …`

        A request to close a subagent.

        - `id: str`

          The ID of the tool call item.

        - `recipient_agent_id: str`

          The ID of the agent to close.

        - `sender_agent_id: str`

          The ID of the agent requesting the close.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["close_subagent_call"]`

          The item type. Always `close_subagent_call`.

          - `"close_subagent_call"`

            The current public item type.

    - `output_index: Optional[int]`

      The index of the item in the turn output, when the item is agent output.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.turn.item.added"]`

      The type of the object. Always `agent.session.turn.item.added`.

      - `"agent.session.turn.item.added"`

  - `class AgentSessionIdleEvent: …`

    Emitted when a session becomes idle.

    - `event_id: str`

      The unique ID of the event.

    - `session: AgentSession`

      The session that became idle.

    - `type: Literal["agent.session.idle"]`

      The type of the object. Always `agent.session.idle`.

      - `"agent.session.idle"`

  - `class AgentSessionInProgressEvent: …`

    Emitted when a session starts processing a turn.

    - `event_id: str`

      The unique ID of the event.

    - `session: AgentSession`

      The session that started processing.

    - `type: Literal["agent.session.in_progress"]`

      The type of the object. Always `agent.session.in_progress`.

      - `"agent.session.in_progress"`

  - `class AgentSessionRequiresActionEvent: …`

    Emitted when a session is waiting for one or more required actions.

    - `event_id: str`

      The unique ID of the event.

    - `session: AgentSession`

      The session and its current required actions.

    - `type: Literal["agent.session.requires_action"]`

      The type of the object. Always `agent.session.requires_action`.

      - `"agent.session.requires_action"`

  - `class AgentSessionFailedEvent: …`

    Emitted when a session fails.

    - `event_id: str`

      The unique ID of the event.

    - `session: AgentSession`

      The failed session.

    - `type: Literal["agent.session.failed"]`

      The type of the object. Always `agent.session.failed`.

      - `"agent.session.failed"`

  - `class AgentSessionEnvironmentPendingEvent: …`

    Emitted while a session environment is being prepared.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: str`

      The unique ID of the event.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.environment.pending"]`

      The type of the object. Always `agent.session.environment.pending`.

      - `"agent.session.environment.pending"`

  - `class AgentSessionEnvironmentConnectedEvent: …`

    Emitted when a session environment connects.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: str`

      The unique ID of the event.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.environment.connected"]`

      The type of the object. Always `agent.session.environment.connected`.

      - `"agent.session.environment.connected"`

  - `class AgentSessionEnvironmentDisconnectedEvent: …`

    Emitted when a session environment disconnects.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: str`

      The unique ID of the event.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.environment.disconnected"]`

      The type of the object. Always `agent.session.environment.disconnected`.

      - `"agent.session.environment.disconnected"`

  - `class AgentSessionEnvironmentFailedEvent: …`

    Emitted when a session environment fails.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: str`

      The unique ID of the event.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.environment.failed"]`

      The type of the object. Always `agent.session.environment.failed`.

      - `"agent.session.environment.failed"`

  - `class AgentSessionSubagentCreatedEvent: …`

    Emitted when a subagent is created.

    - `event_id: str`

      The unique ID of the event.

    - `subagent: Subagent`

      The subagent that was created.

      - `id: str`

        The ID of the subagent.

      - `closed_at: Optional[int]`

        The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

      - `instructions: Optional[List[AgentContent]]`

        Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

        - `class OutputText: …`

          A text content part produced by the agent.

        - `class EncryptedContentResource: …`

          Encrypted content exchanged between agents.

      - `name: Optional[str]`

        The runner-assigned nickname, or null when unavailable.

      - `object: Literal["agent.session.subagent"]`

        The object type. Always `agent.session.subagent`.

        - `"agent.session.subagent"`

      - `opened_at: int`

        The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

      - `parent_agent_id: str`

        The ID of the agent that created this subagent.

      - `session_id: str`

        The ID of the session that owns the subagent.

      - `status: Literal["active", "closed"]`

        The current status of the subagent.

        - `"active"`

          The subagent remains available, including while idle between turns.

        - `"closed"`

          The subagent is closed.

    - `type: Literal["agent.session.subagent.created"]`

      The type of the object. Always `agent.session.subagent.created`.

      - `"agent.session.subagent.created"`

  - `class AgentSessionSubagentActiveEvent: …`

    Emitted when a closed subagent successfully resumes.

    - `event_id: str`

      The unique ID of the event.

    - `subagent: Subagent`

      The subagent that resumed.

    - `type: Literal["agent.session.subagent.active"]`

      The type of the object. Always `agent.session.subagent.active`.

      - `"agent.session.subagent.active"`

  - `class AgentSessionSubagentClosedEvent: …`

    Emitted when a subagent is closed.

    - `event_id: str`

      The unique ID of the event.

    - `subagent: Subagent`

      The subagent that was closed.

    - `type: Literal["agent.session.subagent.closed"]`

      The type of the object. Always `agent.session.subagent.closed`.

      - `"agent.session.subagent.closed"`

  - `class AgentSessionTurnItemDoneEvent: …`

    Emitted when an output item is complete.

    - `event_id: str`

      The unique ID of the event.

    - `item: AgentOutputItem`

      The completed output item.

      - `class AgentSessionAssistantMessage: …`

        An assistant message produced by the agent.

        - `id: str`

          The ID of the message.

        - `content: List[OutputText]`

          The content of the message.

          - `text: str`

            The text produced by the agent.

          - `type: Literal["output_text"]`

            The content type. Always `output_text`.

        - `phase: Optional[Literal["commentary", "final_answer"]]`

          The phase of the assistant message.

          - `"commentary"`

            Commentary produced while the agent works.

          - `"final_answer"`

            The agent's final answer.

        - `role: Literal["assistant"]`

          The role of the message author. Always `assistant`.

          - `"assistant"`

        - `status: AgentOutputItemStatus`

          The status of the message.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["message"]`

          The item type. Always `message`.

          - `"message"`

      - `class AgentReasoningItem: …`

        A reasoning item produced by the agent.

      - `class AgentFunctionCallItem: …`

        A function call produced by the agent.

      - `class AgentMcpCallItem: …`

        A call to a tool on an MCP server.

      - `class ComputerUseCallItemResource: …`

        One execution of the platform-provided computer-use capability.

        - `id: str`

          The ID of the activity item.

        - `output: Optional[ComputerUseCallItemResourceOutput]`

          The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

          - `image_url: str`

            The complete JPEG image as a base64 data URL.

          - `type: Literal["computer_screenshot"]`

            The content type. Always `computer_screenshot`.

            - `"computer_screenshot"`

        - `status: AgentFunctionCallStatus`

          The execution status of the activity.

        - `title: Optional[str]`

          A model-generated description of the activity, when available.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["computer_use_call"]`

          The item type. Always `computer_use_call`.

          - `"computer_use_call"`

      - `class BrowserAuthenticationRequestItemResource: …`

        A credential-free history record of the emitted login request.

        - `id: str`

          The stable history item ID.

        - `request: BrowserAuthenticationRequestItemResourceRequest`

          A registered form awaiting the application's response.

          - `credential_origin: Optional[str]`

            The registered form or frame origin where values will be entered.

          - `fields: List[BrowserAuthenticationRequestItemResourceRequestField]`

            Controls to render. All submitted values are sensitive.

            - `id: str`

              The field ID to submit as field_id in a fields entry.

            - `label: str`

              The label to display beside the control.

            - `required: bool`

              Whether this control requires a nonempty value.

            - `type: str`

              The rendering type, such as email, password, or text.

          - `options: List[BrowserAuthenticationRequestItemResourceRequestOption]`

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

        - `request_id: str`

        - `turn_id: str`

        - `type: Literal["computer_use_approval_request"]`

          The item type. Always computer_use_approval_request.

          - `"computer_use_approval_request"`

      - `class AgentWebSearchCallItem: …`

        A web search call produced by the agent.

      - `class AgentCommandExecutionItem: …`

        A command execution produced by the agent.

      - `class AgentCreateSubagentCallItem: …`

        A request to spawn a subagent.

      - `class AgentSendSubagentInputCallItem: …`

        A request to send input to another agent.

      - `class AgentResumeSubagentCallItem: …`

        A request to resume a subagent.

      - `class AgentWaitForSubagentsCallItem: …`

        A request to wait for one or more subagents.

      - `class AgentInterruptSubagentCallItem: …`

        A request to interrupt a subagent's current turn. The subagent remains available.

      - `class AgentCloseSubagentCallItem: …`

        A request to close a subagent.

    - `output_index: int`

      The index of the output item in the turn output.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.turn.item.done"]`

      The type of the object. Always `agent.session.turn.item.done`.

      - `"agent.session.turn.item.done"`

  - `class AgentSessionTurnContentPartAddedEvent: …`

    Emitted when an output text content part is added.

    - `content_index: int`

      The index of the content part in the message.

    - `event_id: str`

      The unique ID of the event.

    - `item_id: str`

      The ID of the message item.

    - `output_index: int`

      The index of the item in the turn output.

    - `part: OutputText`

      The initial content part.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.turn.content_part.added"]`

      The type of the object. Always `agent.session.turn.content_part.added`.

      - `"agent.session.turn.content_part.added"`

  - `class AgentSessionTurnContentPartDoneEvent: …`

    Emitted when an output content part is complete.

    - `content_index: int`

      The index of the content part in the message.

    - `event_id: str`

      The unique ID of the event.

    - `item_id: str`

      The ID of the message item.

    - `output_index: int`

      The index of the item in the turn output.

    - `part: OutputText`

      The completed content part.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.turn.content_part.done"]`

      The type of the object. Always `agent.session.turn.content_part.done`.

      - `"agent.session.turn.content_part.done"`

  - `class AgentSessionTurnOutputTextDeltaEvent: …`

    Emitted when text is appended to an output text content part.

    - `content_index: int`

      The index of the content part in the message.

    - `delta: str`

      The text that was appended.

    - `event_id: str`

      The unique ID of the event.

    - `item_id: str`

      The ID of the message item.

    - `output_index: int`

      The index of the item in the turn output.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.turn.output_text.delta"]`

      The type of the object. Always `agent.session.turn.output_text.delta`.

      - `"agent.session.turn.output_text.delta"`

  - `class AgentSessionTurnOutputTextDoneEvent: …`

    Emitted when an output text content part is complete.

    - `content_index: int`

      The index of the content part in the message.

    - `event_id: str`

      The unique ID of the event.

    - `item_id: str`

      The ID of the message item.

    - `output_index: int`

      The index of the item in the turn output.

    - `session_id: str`

      The ID of the session associated with the event.

    - `text: str`

      The complete output text.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.turn.output_text.done"]`

      The type of the object. Always `agent.session.turn.output_text.done`.

      - `"agent.session.turn.output_text.done"`

  - `class AgentSessionTurnReasoningSummaryPartAddedEvent: …`

    Emitted when a reasoning summary content part is added.

    - `event_id: str`

      The unique ID of the event.

    - `item_id: str`

      The ID of the reasoning item.

    - `output_index: int`

      The index of the item in the turn output.

    - `part: SummaryText`

      The initial summary part.

      - `text: str`

        The reasoning summary text.

      - `type: Literal["summary_text"]`

        The content type. Always `summary_text`.

    - `session_id: str`

      The ID of the session associated with the event.

    - `summary_index: int`

      The index of the summary content part.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.turn.reasoning_summary_part.added"]`

      The type of the object. Always `agent.session.turn.reasoning_summary_part.added`.

      - `"agent.session.turn.reasoning_summary_part.added"`

  - `class AgentSessionTurnReasoningSummaryPartDoneEvent: …`

    Emitted when a reasoning summary part is complete.

    - `event_id: str`

      The unique ID of the event.

    - `item_id: str`

      The ID of the reasoning item.

    - `output_index: int`

      The index of the item in the turn output.

    - `part: SummaryText`

      The completed summary part.

    - `session_id: str`

      The ID of the session associated with the event.

    - `status: Optional[Literal["incomplete"]]`

      Present as `incomplete` when summary generation was interrupted.

      - `"incomplete"`

    - `summary_index: int`

      The index of the summary part.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.turn.reasoning_summary_part.done"]`

      The type of the object. Always `agent.session.turn.reasoning_summary_part.done`.

      - `"agent.session.turn.reasoning_summary_part.done"`

  - `class AgentSessionTurnReasoningSummaryTextDeltaEvent: …`

    Emitted when text is appended to a reasoning summary.

    - `delta: str`

      The summary text that was appended.

    - `event_id: str`

      The unique ID of the event.

    - `item_id: str`

      The ID of the reasoning item.

    - `output_index: int`

      The index of the item in the turn output.

    - `session_id: str`

      The ID of the session associated with the event.

    - `summary_index: int`

      The index of the summary content part.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.turn.reasoning_summary_text.delta"]`

      The type of the object. Always `agent.session.turn.reasoning_summary_text.delta`.

      - `"agent.session.turn.reasoning_summary_text.delta"`

  - `class AgentSessionTurnReasoningSummaryTextDoneEvent: …`

    Emitted when a reasoning summary content part is complete.

    - `event_id: str`

      The unique ID of the event.

    - `item_id: str`

      The ID of the reasoning item.

    - `output_index: int`

      The index of the item in the turn output.

    - `session_id: str`

      The ID of the session associated with the event.

    - `summary_index: int`

      The index of the summary content part.

    - `text: str`

      The complete reasoning summary text.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.turn.reasoning_summary_text.done"]`

      The type of the object. Always `agent.session.turn.reasoning_summary_text.done`.

      - `"agent.session.turn.reasoning_summary_text.done"`

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
for event in client.beta.agents.sessions.events.stream(
    "session_id",
):
  print(event)
