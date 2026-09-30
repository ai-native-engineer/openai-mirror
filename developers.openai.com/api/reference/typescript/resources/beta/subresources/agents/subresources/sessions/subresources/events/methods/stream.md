<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/agents/subresources/sessions/subresources/events/methods/stream/ -->

## Stream agent session events

`client.beta.agents.sessions.events.stream(stringsessionID, RequestOptionsoptions?): AgentSessionEvent | Stream<AgentSessionEvent>`

**get** `/agents/sessions/{session_id}/events`

Streams live events for an agent session. See [session events](/api/docs/guides/agents-api/sessions/events).

- `sessionID: string`

- `AgentSessionEvent = AgentSessionErrorEvent | AgentSessionEnvironmentReadyEvent | AgentSessionEnvironmentResetEvent | 28 more`

  An event emitted by a Managed Agents session.

  - `AgentSessionErrorEvent`

    Emitted when a turn or session fails.

    - `error: SessionError`

      The error that occurred.

      - `code: string | null`

        The machine-readable error code, if any.

      - `message: string`

        A customer-safe explanation of the error.

      - `param: string | null`

        The request parameter associated with the error, if any.

      - `type: string`

        The error type.

    - `event_id: string`

      The unique ID of the event.

    - `session_id: string`

      The ID of the session associated with the event.

    - `type: "error"`

      The type of the object. Always `error`.

      - `"error"`

  - `AgentSessionEnvironmentReadyEvent`

    Emitted when a hosted session environment is ready to connect.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

      - `id: string`

        The public ID of the environment.

      - `error: Error | null`

        The error reported while preparing the environment, if any.

        - `code: string`

          A machine-readable error code.

        - `message: string`

          A human-readable error message.

        - `type: string`

          The error type.

      - `status: "pending" | "ready" | "connected" | 2 more`

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

      - `type: string`

        The environment type.

    - `event_id: string`

      The unique ID of the event.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.environment.ready"`

      The type of the object. Always `agent.session.environment.ready`.

      - `"agent.session.environment.ready"`

  - `AgentSessionEnvironmentResetEvent`

    Emitted after a hosted sandbox is replaced. Conversation history survives; changes to the previous sandbox's files and processes do not.

    - `environment_id: string`

      The stable environment ID, retained across sandbox replacements.

    - `event_id: string`

      The unique ID of the event.

    - `reset_count: number`

      Monotonically increasing reset number. Repeated notifications share this number.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The associated turn, when applicable.

    - `type: "agent.session.environment.reset"`

      The type of the object. Always `agent.session.environment.reset`.

      - `"agent.session.environment.reset"`

  - `AgentOutputCommandExecutionOutputDeltaEvent`

    Emitted when command execution produces an output delta.

    - `delta: string`

      The output text that was appended.

    - `event_id: string`

      The unique ID of the event.

    - `item_id: string`

      The ID of the command execution item.

    - `output_index: number`

      The index of the item in the turn output.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.output.command_execution_output.delta"`

      The type of the object. Always `agent.output.command_execution_output.delta`.

      - `"agent.output.command_execution_output.delta"`

  - `AgentSessionCreatedEvent`

    Emitted when a session is created.

    - `event_id: string`

      The unique ID of the event.

    - `session: AgentSession`

      The session that was created.

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

    - `type: "agent.session.created"`

      The type of the object. Always `agent.session.created`.

      - `"agent.session.created"`

  - `AgentSessionTurnCreatedEvent`

    Emitted when a turn is created.

    - `event_id: string`

      The unique ID of the event.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn: Turn`

      The turn at the time it was created.

      - `id: string`

        The ID of the turn.

      - `agent_id: string`

        The ID of the agent that ran the turn.

      - `completed_at: number | null`

        The Unix timestamp, in seconds, when the turn reached a terminal state.

      - `created_at: number`

        The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

      - `error: SessionTurnError | null`

        A customer-safe error. Non-null only for a failed turn.

        - `code: "context_length_exceeded" | "session_budget_exceeded" | "usage_limit_exceeded" | 16 more`

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

        - `message: string`

          A customer-safe explanation of the failure.

      - `object: "agent.session.turn"`

        The object type. Always `agent.session.turn`.

        - `"agent.session.turn"`

      - `session_id: string`

        The ID of the session that owns the turn.

      - `started_at: number | null`

        The Unix timestamp, in seconds, when the turn started.

      - `status: "queued" | "in_progress" | "waiting" | 3 more`

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

      - `subagent_id: string | null`

        The ID of the subagent that ran the turn, if applicable.

      - `usage: TokenUsage | null`

        Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `turn_id: string`

      The ID of the turn associated with the event.

    - `type: "agent.session.turn.created"`

      The type of the object. Always `agent.session.turn.created`.

      - `"agent.session.turn.created"`

  - `AgentSessionTurnInProgressEvent`

    Emitted when a turn starts running.

    - `event_id: string`

      The unique ID of the event.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn: Turn`

      The turn at the time it started running.

    - `turn_id: string`

      The ID of the turn associated with the event.

    - `type: "agent.session.turn.in_progress"`

      The type of the object. Always `agent.session.turn.in_progress`.

      - `"agent.session.turn.in_progress"`

  - `AgentSessionTurnCompletedEvent`

    Emitted when a turn completes.

    - `event_id: string`

      The unique ID of the event.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn: Turn`

      The completed turn.

    - `turn_id: string`

      The ID of the turn associated with the event.

    - `type: "agent.session.turn.completed"`

      The type of the object. Always `agent.session.turn.completed`.

      - `"agent.session.turn.completed"`

    - `usage: TokenUsage | null`

      Token usage by the root agent during the turn, when available.

  - `AgentSessionTurnFailedEvent`

    Emitted when a turn fails.

    - `event_id: string`

      The unique ID of the event.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn: Turn`

      The failed turn.

    - `turn_id: string`

      The ID of the turn associated with the event.

    - `type: "agent.session.turn.failed"`

      The type of the object. Always `agent.session.turn.failed`.

      - `"agent.session.turn.failed"`

    - `usage: TokenUsage | null`

      Token usage by the root agent during the turn, when available.

  - `AgentSessionTurnCancelledEvent`

    Emitted when a turn is cancelled.

    - `event_id: string`

      The unique ID of the event.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn: Turn`

      The cancelled turn.

    - `turn_id: string`

      The ID of the turn associated with the event.

    - `type: "agent.session.turn.cancelled"`

      The type of the object. Always `agent.session.turn.cancelled`.

      - `"agent.session.turn.cancelled"`

    - `usage: TokenUsage | null`

      Token usage by the root agent during the turn, when available.

  - `AgentSessionTurnItemAddedEvent`

    Emitted when an item is added to a turn.

    - `event_id: string`

      The unique ID of the event.

    - `item: AgentSessionItem`

      The item that was added.

      - `AgentSessionMessage`

        A user or assistant message recorded in a session.

        - `id: string | null`

          The ID of this item, or null for legacy user messages whose ID was not recorded.

        - `content: Array<AgentSessionMessageContent>`

          The content of the message. User messages contain input text or images; assistant messages contain output text.

          - `MessageContentResourceInputText`

            Text supplied by the user.

            - `text: string`

              The text supplied by the user.

            - `type: "input_text"`

              The type of the object. Always `input_text`.

              - `"input_text"`

          - `MessageContentResourceInputImage`

            An image supplied by the user.

            - `image_url: string`

              The URL of the image supplied by the user, which may be a base64-encoded data URL.

            - `type: "input_image"`

              The type of the object. Always `input_image`.

              - `"input_image"`

          - `MessageContentResourceOutputText`

            Text produced by the assistant.

            - `text: string`

              The text produced by the assistant.

            - `type: "output_text"`

              The type of the object. Always `output_text`.

              - `"output_text"`

        - `phase: "commentary" | "final_answer" | null`

          The phase of an assistant message. Null for user messages.

          - `"commentary"`

            Commentary produced while the agent works.

          - `"final_answer"`

            The agent's final answer.

        - `role: "user" | "assistant"`

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

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "message"`

          The item type. Always `message`.

          - `"message"`

      - `AgentReasoningItem`

        A reasoning item produced by the agent.

        - `id: string`

          The ID of the reasoning item.

        - `status: AgentOutputItemStatus | null`

          The status of the reasoning item.

        - `summary: Array<SummaryText>`

          The reasoning summaries produced by the agent.

          - `text: string`

            The reasoning summary text.

          - `type: "summary_text"`

            The content type. Always `summary_text`.

            - `"summary_text"`

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "reasoning"`

          The item type. Always `reasoning`.

          - `"reasoning"`

      - `AgentFunctionCallItem`

        A function call produced by the agent.

        - `id: string`

          The ID of the function call item.

        - `arguments: unknown`

          The arguments to pass to the function.

        - `call_id: string`

          The ID used to submit the function result.

        - `name: string`

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

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "function_call"`

          The item type. Always `function_call`.

          - `"function_call"`

      - `FunctionCallOutputItemResource`

        The result supplied for a function call.

        - `id: string`

          The ID of the function call output item.

        - `call_id: string`

          The ID of the function call that produced this output.

        - `error: string | null`

          The error message, if the call failed.

        - `output: AgentFunctionCallOutput | null`

          The function result, if the call succeeded.

          - `string`

          - `Array<InputContent>`

            - `InputContentResourceInputText`

              Text input recorded in a session item.

              - `text: string`

                The text supplied to the agent.

              - `type: "input_text"`

                The type of the object. Always `input_text`.

                - `"input_text"`

            - `InputContentResourceInputImage`

              Image input recorded in a session item.

              - `image_url: string`

                The URL of the image supplied to the agent, which may be a base64-encoded data URL.

              - `type: "input_image"`

                The type of the object. Always `input_image`.

                - `"input_image"`

        - `status: AgentFunctionCallStatus`

          The status of the function call.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "function_call_output"`

          The item type. Always `function_call_output`.

          - `"function_call_output"`

      - `AgentMessageItemResource`

        A message exchanged between agent threads.

        - `id: string`

          The ID of the message.

        - `content: Array<AgentContent>`

          The content exchanged between the agents.

          - `OutputText`

            A text content part produced by the agent.

            - `text: string`

              The text produced by the agent.

            - `type: "output_text"`

              The content type. Always `output_text`.

              - `"output_text"`

          - `EncryptedContentResource`

            Encrypted content exchanged between agents.

            - `encrypted_content: string`

              The encrypted content payload.

            - `type: "encrypted_content"`

              The content type. Always `encrypted_content`.

              - `"encrypted_content"`

        - `recipient_agent_id: string`

          The ID or name of the receiving agent.

        - `sender_agent_id: string`

          The ID or name of the sending agent.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "agent_message"`

          The item type. Always `agent_message`.

          - `"agent_message"`

      - `AgentMcpCallItem`

        A call to a tool on an MCP server.

        - `id: string`

          The ID of the MCP call item.

        - `arguments: unknown`

          The arguments passed to the MCP tool.

        - `error: unknown`

          The error returned by the MCP tool, if any.

        - `name: string`

          The name of the MCP tool.

        - `output: unknown`

          The output returned by the MCP tool, if any.

        - `server_label: string`

          The label of the MCP server.

        - `status: AgentFunctionCallStatus`

          The status of the MCP tool call.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "mcp_call"`

          The item type. Always `mcp_call`.

          - `"mcp_call"`

      - `ComputerUseCallItemResource`

        One execution of the platform-provided computer-use capability.

        - `id: string`

          The ID of the activity item.

        - `output: Output | null`

          The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

          - `image_url: string`

            The complete JPEG image as a base64 data URL.

          - `type: "computer_screenshot"`

            The content type. Always `computer_screenshot`.

            - `"computer_screenshot"`

        - `status: AgentFunctionCallStatus`

          The execution status of the activity.

        - `title: string | null`

          A model-generated description of the activity, when available.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "computer_use_call"`

          The item type. Always `computer_use_call`.

          - `"computer_use_call"`

      - `BrowserAuthenticationRequestItemResource`

        A credential-free history record of the emitted login request.

        - `id: string`

          The stable history item ID.

        - `request: Request`

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

        - `request_id: string`

        - `turn_id: string`

        - `type: "computer_use_approval_request"`

          The item type. Always computer_use_approval_request.

          - `"computer_use_approval_request"`

      - `ComputerUseApprovalRequestResultItemResource`

        A credential-free record of an admitted response, not proof of completion.

        - `id: string`

          The stable history item ID.

        - `request_id: string`

          The registered request answered by this item.

        - `response: ComputerUseApprovalResponseKindResourceBrowserAuthenticationSubmitResource | ComputerUseApprovalResponseKindResourceBrowserAuthenticationCancelResource`

          The admitted response, without submitted credential values.

          - `ComputerUseApprovalResponseKindResourceBrowserAuthenticationSubmitResource`

            - `action: "submit"`

              - `"submit"`

            - `selected_option: string | null`

              The chosen sign-in method, or null when no options were offered.

            - `type: "browser_authentication"`

              - `"browser_authentication"`

          - `ComputerUseApprovalResponseKindResourceBrowserAuthenticationCancelResource`

            - `action: "cancel"`

              - `"cancel"`

            - `type: "browser_authentication"`

              - `"browser_authentication"`

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "computer_use_approval_request_result"`

          - `"computer_use_approval_request_result"`

      - `AgentWebSearchCallItem`

        A web search call produced by the agent.

        - `id: string`

          The ID of the web search call.

        - `action: WebSearchAction | null`

          The action performed by the web search tool.

          - `WebSearchActionResourceSearch`

            A search query or group of search queries.

            - `queries: Array<string> | null`

              The search queries, when multiple queries were used.

            - `query: string | null`

              The search query, when a single query was used.

            - `type: "search"`

              The type of the object. Always `search`.

              - `"search"`

          - `WebSearchActionResourceOpenPage`

            Opens a web page.

            - `type: "open_page"`

              The type of the object. Always `open_page`.

              - `"open_page"`

            - `url: string | null`

              The URL of the page that was opened.

          - `WebSearchActionResourceFindInPage`

            Finds text within a web page.

            - `pattern: string | null`

              The text pattern that was searched for.

            - `type: "find_in_page"`

              The type of the object. Always `find_in_page`.

              - `"find_in_page"`

            - `url: string | null`

              The URL of the page that was searched.

          - `WebSearchActionResourceOther`

            Another web search action.

            - `type: "other"`

              The type of the object. Always `other`.

              - `"other"`

        - `status: AgentOutputItemStatus`

          The status of the web search call.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "web_search_call"`

          The item type. Always `web_search_call`.

          - `"web_search_call"`

      - `AgentCommandExecutionItem`

        A command execution produced by the agent.

        - `id: string`

          The ID of the command execution item.

        - `command: string`

          The command that was executed.

        - `cwd: string | null`

          The working directory used to execute the command.

        - `duration_ms: number | null`

          The command duration in milliseconds.

        - `exit_code: number | null`

          The process exit code, if the command completed.

        - `output: string | null`

          The command output, if available.

        - `status: AgentFunctionCallStatus`

          The status of the command execution.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "command_execution"`

          The item type. Always `command_execution`.

          - `"command_execution"`

      - `AgentCreateSubagentCallItem`

        A request to spawn a subagent.

        - `id: string`

          The ID of the tool call item.

        - `agent_id: string`

          The ID of the agent that requested the subagent.

        - `content: Array<AgentContent>`

          The task given to the spawned agent.

          - `OutputText`

            A text content part produced by the agent.

          - `EncryptedContentResource`

            Encrypted content exchanged between agents.

        - `model: string | null`

          The model requested for the spawned agent.

        - `reasoning_effort: string | null`

          The reasoning effort requested for the spawned agent.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "create_subagent_call"`

          The item type. Always `create_subagent_call`.

          - `"create_subagent_call"`

            The current public item type.

      - `AgentSendSubagentInputCallItem`

        A request to send input to another agent.

        - `id: string`

          The ID of the tool call item.

        - `content: Array<AgentContent>`

          The input sent to the receiving agent.

          - `OutputText`

            A text content part produced by the agent.

          - `EncryptedContentResource`

            Encrypted content exchanged between agents.

        - `recipient_agent_id: string`

          The ID of the agent receiving the input.

        - `sender_agent_id: string`

          The ID of the agent sending the input.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "send_subagent_input_call"`

          The item type. Always `send_subagent_input_call`.

          - `"send_subagent_input_call"`

            The current public item type.

      - `AgentResumeSubagentCallItem`

        A request to resume a subagent.

        - `id: string`

          The ID of the tool call item.

        - `recipient_agent_id: string`

          The ID of the agent to resume.

        - `sender_agent_id: string`

          The ID of the agent requesting the resume.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "resume_subagent_call"`

          The item type. Always `resume_subagent_call`.

          - `"resume_subagent_call"`

            The current public item type.

      - `AgentWaitForSubagentsCallItem`

        A request to wait for one or more subagents.

        - `id: string`

          The ID of the tool call item.

        - `recipient_agent_ids: Array<string>`

          The IDs of the agents to wait for.

        - `sender_agent_id: string`

          The ID of the agent waiting for results.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "wait_for_subagents_call"`

          The item type. Always `wait_for_subagents_call`.

          - `"wait_for_subagents_call"`

            The current public item type.

      - `AgentInterruptSubagentCallItem`

        A request to interrupt a subagent's current turn. The subagent remains available.

        - `id: string`

          The ID of the tool call item.

        - `recipient_agent_id: string`

          The ID of the agent to interrupt.

        - `sender_agent_id: string`

          The ID of the agent requesting the interrupt.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "interrupt_subagent_call"`

          The item type. Always `interrupt_subagent_call`.

          - `"interrupt_subagent_call"`

            The current public item type.

      - `AgentCloseSubagentCallItem`

        A request to close a subagent.

        - `id: string`

          The ID of the tool call item.

        - `recipient_agent_id: string`

          The ID of the agent to close.

        - `sender_agent_id: string`

          The ID of the agent requesting the close.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "close_subagent_call"`

          The item type. Always `close_subagent_call`.

          - `"close_subagent_call"`

            The current public item type.

    - `output_index: number | null`

      The index of the item in the turn output, when the item is agent output.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.turn.item.added"`

      The type of the object. Always `agent.session.turn.item.added`.

      - `"agent.session.turn.item.added"`

  - `AgentSessionIdleEvent`

    Emitted when a session becomes idle.

    - `event_id: string`

      The unique ID of the event.

    - `session: AgentSession`

      The session that became idle.

    - `type: "agent.session.idle"`

      The type of the object. Always `agent.session.idle`.

      - `"agent.session.idle"`

  - `AgentSessionInProgressEvent`

    Emitted when a session starts processing a turn.

    - `event_id: string`

      The unique ID of the event.

    - `session: AgentSession`

      The session that started processing.

    - `type: "agent.session.in_progress"`

      The type of the object. Always `agent.session.in_progress`.

      - `"agent.session.in_progress"`

  - `AgentSessionRequiresActionEvent`

    Emitted when a session is waiting for one or more required actions.

    - `event_id: string`

      The unique ID of the event.

    - `session: AgentSession`

      The session and its current required actions.

    - `type: "agent.session.requires_action"`

      The type of the object. Always `agent.session.requires_action`.

      - `"agent.session.requires_action"`

  - `AgentSessionFailedEvent`

    Emitted when a session fails.

    - `event_id: string`

      The unique ID of the event.

    - `session: AgentSession`

      The failed session.

    - `type: "agent.session.failed"`

      The type of the object. Always `agent.session.failed`.

      - `"agent.session.failed"`

  - `AgentSessionEnvironmentPendingEvent`

    Emitted while a session environment is being prepared.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: string`

      The unique ID of the event.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.environment.pending"`

      The type of the object. Always `agent.session.environment.pending`.

      - `"agent.session.environment.pending"`

  - `AgentSessionEnvironmentConnectedEvent`

    Emitted when a session environment connects.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: string`

      The unique ID of the event.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.environment.connected"`

      The type of the object. Always `agent.session.environment.connected`.

      - `"agent.session.environment.connected"`

  - `AgentSessionEnvironmentDisconnectedEvent`

    Emitted when a session environment disconnects.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: string`

      The unique ID of the event.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.environment.disconnected"`

      The type of the object. Always `agent.session.environment.disconnected`.

      - `"agent.session.environment.disconnected"`

  - `AgentSessionEnvironmentFailedEvent`

    Emitted when a session environment fails.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: string`

      The unique ID of the event.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.environment.failed"`

      The type of the object. Always `agent.session.environment.failed`.

      - `"agent.session.environment.failed"`

  - `AgentSessionSubagentCreatedEvent`

    Emitted when a subagent is created.

    - `event_id: string`

      The unique ID of the event.

    - `subagent: Subagent`

      The subagent that was created.

      - `id: string`

        The ID of the subagent.

      - `closed_at: number | null`

        The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

      - `instructions: Array<AgentContent> | null`

        Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

        - `OutputText`

          A text content part produced by the agent.

        - `EncryptedContentResource`

          Encrypted content exchanged between agents.

      - `name: string | null`

        The runner-assigned nickname, or null when unavailable.

      - `object: "agent.session.subagent"`

        The object type. Always `agent.session.subagent`.

        - `"agent.session.subagent"`

      - `opened_at: number`

        The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

      - `parent_agent_id: string`

        The ID of the agent that created this subagent.

      - `session_id: string`

        The ID of the session that owns the subagent.

      - `status: "active" | "closed"`

        The current status of the subagent.

        - `"active"`

          The subagent remains available, including while idle between turns.

        - `"closed"`

          The subagent is closed.

    - `type: "agent.session.subagent.created"`

      The type of the object. Always `agent.session.subagent.created`.

      - `"agent.session.subagent.created"`

  - `AgentSessionSubagentActiveEvent`

    Emitted when a closed subagent successfully resumes.

    - `event_id: string`

      The unique ID of the event.

    - `subagent: Subagent`

      The subagent that resumed.

    - `type: "agent.session.subagent.active"`

      The type of the object. Always `agent.session.subagent.active`.

      - `"agent.session.subagent.active"`

  - `AgentSessionSubagentClosedEvent`

    Emitted when a subagent is closed.

    - `event_id: string`

      The unique ID of the event.

    - `subagent: Subagent`

      The subagent that was closed.

    - `type: "agent.session.subagent.closed"`

      The type of the object. Always `agent.session.subagent.closed`.

      - `"agent.session.subagent.closed"`

  - `AgentSessionTurnItemDoneEvent`

    Emitted when an output item is complete.

    - `event_id: string`

      The unique ID of the event.

    - `item: AgentOutputItem`

      The completed output item.

      - `AgentSessionAssistantMessage`

        An assistant message produced by the agent.

        - `id: string`

          The ID of the message.

        - `content: Array<OutputText>`

          The content of the message.

          - `text: string`

            The text produced by the agent.

          - `type: "output_text"`

            The content type. Always `output_text`.

        - `phase: "commentary" | "final_answer" | null`

          The phase of the assistant message.

          - `"commentary"`

            Commentary produced while the agent works.

          - `"final_answer"`

            The agent's final answer.

        - `role: "assistant"`

          The role of the message author. Always `assistant`.

          - `"assistant"`

        - `status: AgentOutputItemStatus`

          The status of the message.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "message"`

          The item type. Always `message`.

          - `"message"`

      - `AgentReasoningItem`

        A reasoning item produced by the agent.

      - `AgentFunctionCallItem`

        A function call produced by the agent.

      - `AgentMcpCallItem`

        A call to a tool on an MCP server.

      - `ComputerUseCallItemResource`

        One execution of the platform-provided computer-use capability.

        - `id: string`

          The ID of the activity item.

        - `output: Output | null`

          The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

          - `image_url: string`

            The complete JPEG image as a base64 data URL.

          - `type: "computer_screenshot"`

            The content type. Always `computer_screenshot`.

            - `"computer_screenshot"`

        - `status: AgentFunctionCallStatus`

          The execution status of the activity.

        - `title: string | null`

          A model-generated description of the activity, when available.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "computer_use_call"`

          The item type. Always `computer_use_call`.

          - `"computer_use_call"`

      - `BrowserAuthenticationRequestItemResource`

        A credential-free history record of the emitted login request.

        - `id: string`

          The stable history item ID.

        - `request: Request`

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

        - `request_id: string`

        - `turn_id: string`

        - `type: "computer_use_approval_request"`

          The item type. Always computer_use_approval_request.

          - `"computer_use_approval_request"`

      - `AgentWebSearchCallItem`

        A web search call produced by the agent.

      - `AgentCommandExecutionItem`

        A command execution produced by the agent.

      - `AgentCreateSubagentCallItem`

        A request to spawn a subagent.

      - `AgentSendSubagentInputCallItem`

        A request to send input to another agent.

      - `AgentResumeSubagentCallItem`

        A request to resume a subagent.

      - `AgentWaitForSubagentsCallItem`

        A request to wait for one or more subagents.

      - `AgentInterruptSubagentCallItem`

        A request to interrupt a subagent's current turn. The subagent remains available.

      - `AgentCloseSubagentCallItem`

        A request to close a subagent.

    - `output_index: number`

      The index of the output item in the turn output.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.turn.item.done"`

      The type of the object. Always `agent.session.turn.item.done`.

      - `"agent.session.turn.item.done"`

  - `AgentSessionTurnContentPartAddedEvent`

    Emitted when an output text content part is added.

    - `content_index: number`

      The index of the content part in the message.

    - `event_id: string`

      The unique ID of the event.

    - `item_id: string`

      The ID of the message item.

    - `output_index: number`

      The index of the item in the turn output.

    - `part: OutputText`

      The initial content part.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.turn.content_part.added"`

      The type of the object. Always `agent.session.turn.content_part.added`.

      - `"agent.session.turn.content_part.added"`

  - `AgentSessionTurnContentPartDoneEvent`

    Emitted when an output content part is complete.

    - `content_index: number`

      The index of the content part in the message.

    - `event_id: string`

      The unique ID of the event.

    - `item_id: string`

      The ID of the message item.

    - `output_index: number`

      The index of the item in the turn output.

    - `part: OutputText`

      The completed content part.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.turn.content_part.done"`

      The type of the object. Always `agent.session.turn.content_part.done`.

      - `"agent.session.turn.content_part.done"`

  - `AgentSessionTurnOutputTextDeltaEvent`

    Emitted when text is appended to an output text content part.

    - `content_index: number`

      The index of the content part in the message.

    - `delta: string`

      The text that was appended.

    - `event_id: string`

      The unique ID of the event.

    - `item_id: string`

      The ID of the message item.

    - `output_index: number`

      The index of the item in the turn output.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.turn.output_text.delta"`

      The type of the object. Always `agent.session.turn.output_text.delta`.

      - `"agent.session.turn.output_text.delta"`

  - `AgentSessionTurnOutputTextDoneEvent`

    Emitted when an output text content part is complete.

    - `content_index: number`

      The index of the content part in the message.

    - `event_id: string`

      The unique ID of the event.

    - `item_id: string`

      The ID of the message item.

    - `output_index: number`

      The index of the item in the turn output.

    - `session_id: string`

      The ID of the session associated with the event.

    - `text: string`

      The complete output text.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.turn.output_text.done"`

      The type of the object. Always `agent.session.turn.output_text.done`.

      - `"agent.session.turn.output_text.done"`

  - `AgentSessionTurnReasoningSummaryPartAddedEvent`

    Emitted when a reasoning summary content part is added.

    - `event_id: string`

      The unique ID of the event.

    - `item_id: string`

      The ID of the reasoning item.

    - `output_index: number`

      The index of the item in the turn output.

    - `part: SummaryText`

      The initial summary part.

      - `text: string`

        The reasoning summary text.

      - `type: "summary_text"`

        The content type. Always `summary_text`.

    - `session_id: string`

      The ID of the session associated with the event.

    - `summary_index: number`

      The index of the summary content part.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.turn.reasoning_summary_part.added"`

      The type of the object. Always `agent.session.turn.reasoning_summary_part.added`.

      - `"agent.session.turn.reasoning_summary_part.added"`

  - `AgentSessionTurnReasoningSummaryPartDoneEvent`

    Emitted when a reasoning summary part is complete.

    - `event_id: string`

      The unique ID of the event.

    - `item_id: string`

      The ID of the reasoning item.

    - `output_index: number`

      The index of the item in the turn output.

    - `part: SummaryText`

      The completed summary part.

    - `session_id: string`

      The ID of the session associated with the event.

    - `status: "incomplete" | null`

      Present as `incomplete` when summary generation was interrupted.

      - `"incomplete"`

    - `summary_index: number`

      The index of the summary part.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.turn.reasoning_summary_part.done"`

      The type of the object. Always `agent.session.turn.reasoning_summary_part.done`.

      - `"agent.session.turn.reasoning_summary_part.done"`

  - `AgentSessionTurnReasoningSummaryTextDeltaEvent`

    Emitted when text is appended to a reasoning summary.

    - `delta: string`

      The summary text that was appended.

    - `event_id: string`

      The unique ID of the event.

    - `item_id: string`

      The ID of the reasoning item.

    - `output_index: number`

      The index of the item in the turn output.

    - `session_id: string`

      The ID of the session associated with the event.

    - `summary_index: number`

      The index of the summary content part.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.turn.reasoning_summary_text.delta"`

      The type of the object. Always `agent.session.turn.reasoning_summary_text.delta`.

      - `"agent.session.turn.reasoning_summary_text.delta"`

  - `AgentSessionTurnReasoningSummaryTextDoneEvent`

    Emitted when a reasoning summary content part is complete.

    - `event_id: string`

      The unique ID of the event.

    - `item_id: string`

      The ID of the reasoning item.

    - `output_index: number`

      The index of the item in the turn output.

    - `session_id: string`

      The ID of the session associated with the event.

    - `summary_index: number`

      The index of the summary content part.

    - `text: string`

      The complete reasoning summary text.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.turn.reasoning_summary_text.done"`

      The type of the object. Always `agent.session.turn.reasoning_summary_text.done`.

      - `"agent.session.turn.reasoning_summary_text.done"`

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const agentSessionEvent = await client.beta.agents.sessions.events.stream('session_id');

console.log(agentSessionEvent);
