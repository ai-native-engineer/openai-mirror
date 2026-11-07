<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/subresources/automations/ -->

# Automations

## Create an automation

`client.Beta.Agents.Automations.New(ctx, body) (*AutomationUnion, error)`

**post** `/agents/automations`

Saves an active automation without invoking it immediately.

### Parameters

- `body BetaAgentAutomationNewParams`

  - `Expression param.Field[string]`

    A standard five-field cron expression defining scheduled occurrences.

  - `Name param.Field[string]`

    A human-readable name for the automation.

  - `Target param.Field[AutomationTargetParamUnionResp]`

    - `AutomationTargetParamNewSessionResp`

      - `Environment EnvironmentParamUnionResp`

        The execution environment for each new session.

        - `EnvironmentParamNoneResp`

          - `Type None`

            The type of the object. Always `none`.

            - `const NoneNone None = "none"`

        - `EnvironmentParamOpenAIHostedResp`

          - `Type OpenAIHosted`

            The type of the object. Always `openai_hosted`.

            - `const OpenAIHostedOpenAIHosted OpenAIHosted = "openai_hosted"`

          - `CapabilityDirectories []string`

            Directories that contain capabilities exposed to the agent. Defaults to an empty list.

            `minItems: 0`, `maxItems: 16384`

          - `ContainerSize string`

            The hosted container size. Omission selects the medium tier.

            - `const EnvironmentParamOpenAIHostedContainerSizeSmall EnvironmentParamOpenAIHostedContainerSize = "small"`

            - `const EnvironmentParamOpenAIHostedContainerSizeMedium EnvironmentParamOpenAIHostedContainerSize = "medium"`

            - `const EnvironmentParamOpenAIHostedContainerSizeLarge EnvironmentParamOpenAIHostedContainerSize = "large"`

          - `Desktop EnvironmentParamOpenAIHostedDesktopResp`

            Desktop provisioning. Omission or null inherits the template setting, or defaults to disabled.

            - `Enabled bool`

              Whether to provision the desktop and its browser proxy.

          - `Env map[string, string]`

            Environment variables made available to the agent.

          - `EnvironmentID string`

            An existing prewarmed environment. Cannot be combined with a template or inline configuration.

            `minLength: 9`, `maxLength: 256`

          - `EnvironmentTemplateID string`

            A reusable hosted template applied before inline session configuration. Omitted fields inherit the template; network overrides cannot broaden its policy.

            `minLength: 0`, `maxLength: 64`

          - `Files []HostedEnvironmentFileParamUnionResp`

            Files available before the agent starts. Defaults to an empty list.

            `minItems: 0`, `maxItems: 50`

            - `HostedEnvironmentFileParamFileIDResp`

              - `FileID string`

                The ID of the uploaded file.

                `minLength: 1`, `maxLength: 256`

              - `Path string`

                The absolute destination path inside `/workspace`.

                `minLength: 1`, `maxLength: 4096`

              - `Type FileID`

                The type of the object. Always `file_id`.

                - `const FileIDFileID FileID = "file_id"`

            - `HostedEnvironmentFileParamInlineResp`

              - `Data string`

                The standard-base64-encoded file contents.

                `minLength: 0`, `maxLength: 6990508`

              - `Path string`

                The absolute destination path inside `/workspace`.

                `minLength: 1`, `maxLength: 4096`

              - `Type Inline`

                The type of the object. Always `inline`.

                - `const InlineInline Inline = "inline"`

          - `Network EnvironmentParamOpenAIHostedNetworkResp`

            Network access policy for the environment. If omitted, the API version determines whether network access is enabled or disabled.

            - `Access string`

              The environment's network access mode.

              - `const EnvironmentParamOpenAIHostedNetworkAccessEnabled EnvironmentParamOpenAIHostedNetworkAccess = "enabled"`

                Allows unrestricted network access.

              - `const EnvironmentParamOpenAIHostedNetworkAccessDisabled EnvironmentParamOpenAIHostedNetworkAccess = "disabled"`

                Disables network access.

              - `const EnvironmentParamOpenAIHostedNetworkAccessRestricted EnvironmentParamOpenAIHostedNetworkAccess = "restricted"`

                Applies the configured domain restrictions.

            - `AllowedDomains []string`

              Domains the environment may access when network access is restricted.

              `minItems: 0`, `maxItems: 16384`

            - `BlockedDomains []string`

              Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

              `minItems: 0`, `maxItems: 100`

          - `Packages EnvironmentParamOpenAIHostedPackagesResp`

            Packages to install in the environment. Defaults to empty package lists.

            - `Npm []string`

              npm packages to install globally. Defaults to an empty list.

              `minItems: 0`, `maxItems: 16384`

            - `Python []string`

              Python packages to install. Defaults to an empty list.

              `minItems: 0`, `maxItems: 16384`

            - `System []string`

              System packages to install. Defaults to an empty list.

              `minItems: 0`, `maxItems: 16384`

          - `Plugins []HostedPluginParamResp`

            Plugins provided as inline ZIP archives. Defaults to an empty list.

            `minItems: 0`, `maxItems: 32`

            - `Description string`

              The plugin description declared in `.codex-plugin/plugin.json`.

              `minLength: 0`, `maxLength: 1048576`

            - `Name string`

              The plugin name declared in `.codex-plugin/plugin.json`.

              `minLength: 1`, `maxLength: 64`

            - `Source InlineCapabilitySourceParamResp`

              Provides ZIP bytes encoded with standard base64.

              - `Data string`

                Standard-base64 encoded ZIP archive bytes.

                `minLength: 1`, `maxLength: 70254592`

              - `MediaType ApplicationZip`

                The archive media type, always `application/zip`.

                - `const ApplicationZipApplicationZip ApplicationZip = "application/zip"`

              - `Type Base64`

                The type of the object. Always `base64`.

                - `const Base64Base64 Base64 = "base64"`

            - `Type Inline`

              The type of the object. Always `inline`.

              - `const InlineInline Inline = "inline"`

          - `SetupCommands []SetupCommandParamResp`

            Ordered, confidential setup commands. Command bodies are never returned.

            `minItems: 0`, `maxItems: 16`

            - `Command string`

              The shell command to execute.

              `minLength: 0`, `maxLength: 65536`

            - `Cwd string`

              The absolute working directory. Defaults to `/workspace`.

              `minLength: 0`, `maxLength: 4096`

          - `Skills []HostedSkillParamUnionResp`

            Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

            `minItems: 0`, `maxItems: 200`

            - `HostedSkillParamSkillReferenceResp`

              - `SkillID string`

                The ID of the skill created through `/v1/skills`.

                `minLength: 1`, `maxLength: 64`

              - `Type SkillReference`

                The type of the object. Always `skill_reference`.

                - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

              - `Version string`

                The skill version, a positive integer or `latest`; omission selects the default.

                `minLength: 0`, `maxLength: 1048576`

            - `HostedSkillParamInlineResp`

              - `Description string`

                The skill description declared in `SKILL.md`.

                `minLength: 0`, `maxLength: 1048576`

              - `Name string`

                The skill name declared in `SKILL.md`.

                `minLength: 1`, `maxLength: 64`

              - `Source InlineCapabilitySourceParamResp`

                Provides ZIP bytes encoded with standard base64.

              - `Type Inline`

                The type of the object. Always `inline`.

                - `const InlineInline Inline = "inline"`

        - `EnvironmentParamSelfHostedResp`

          - `Type SelfHosted`

            The type of the object. Always `self_hosted`.

            - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

          - `WorkspaceDirectory string`

            Absolute project directory inside the self-hosted environment.

            `minLength: 0`, `maxLength: 1048576`

          - `CapabilityDirectories []string`

            Directories that contain capabilities exposed to the agent. Defaults to an empty list.

            `minItems: 0`, `maxItems: 16384`

      - `Input []AgentSessionInputMessageParamResp`

        Initial user messages submitted with each new session.

        `minItems: 0`, `maxItems: 16384`

        - `Content []InputContentParamUnionResp`

          The content of the message.

          `minItems: 0`, `maxItems: 16384`

          - `InputContentParamInputTextResp`

            - `Text string`

              The text sent to the model.

              `minLength: 0`, `maxLength: 1048576`

            - `Type InputText`

              The type of the object. Always `input_text`.

              - `const InputTextInputText InputText = "input_text"`

          - `InputContentParamInputImageResp`

            - `ImageURL string`

              The URL of the image sent to the model.

              `minLength: 0`, `maxLength: 1048576`

            - `Type InputImage`

              The type of the object. Always `input_image`.

              - `const InputImageInputImage InputImage = "input_image"`

        - `Role User`

          The role of the message author. Always `user`.

          - `const UserUser User = "user"`

        - `Type AgentSessionInputMessageParamType`

          The type of the input item. Always `message`.

          - `const AgentSessionInputMessageParamTypeMessage AgentSessionInputMessageParamType = "message"`

      - `Type NewSession`

        The type of the object. Always `new_session`.

        - `const NewSessionNewSession NewSession = "new_session"`

      - `Agent AutomationTargetParamNewSessionAgentResp`

        Inline agent configuration. Provide exactly one of agent and agent_id.

        - `Compaction AutomationTargetParamNewSessionAgentCompactionResp`

          Context compaction settings. Omit to keep the current settings. A supplied object replaces the settings; null or an empty object enables background compaction.

          - `Async bool`

            Whether to compact context in the background. Omission or null defaults to true. Set to false to use blocking compaction. Background compaction may increase token usage.

        - `Experimental AutomationTargetParamNewSessionAgentExperimentalResp`

          Experimental settings to merge by key. Omitted settings keep their current values.

          - `TimeAwareness bool`

            Whether to give the model periodic current-time reminders. Omit to keep the current setting.

        - `Instructions string`

          Additional instructions appended to the agent's default base instructions. Omit to leave unchanged.

          `minLength: 0`, `maxLength: 1048576`

        - `Model string`

          The model to use for the agent. The requested model name is preserved.

          `minLength: 0`, `maxLength: 1048576`

        - `MultiAgent MultiAgentConfigParamResp`

          Configuration for creating and coordinating subagents.

          - `Enabled bool`

            Whether subagent tools are enabled.

          - `MaxConcurrentSubagents int64`

            Maximum number of subagents that may run concurrently. Defaults to 6.

            `format: int64`, `minimum: 1`, `maximum: 4294967295`

        - `Reasoning AgentReasoningParamResp`

          Configuration for model reasoning. Omit to keep the current settings; pass `null` to reset to the model's default effort.

          - `Effort AgentReasoningParamEffort`

            The amount of reasoning effort the model should use. Omission lets the model select it.

            - `const AgentReasoningParamEffortNone AgentReasoningParamEffort = "none"`

            - `const AgentReasoningParamEffortMinimal AgentReasoningParamEffort = "minimal"`

            - `const AgentReasoningParamEffortLow AgentReasoningParamEffort = "low"`

            - `const AgentReasoningParamEffortMedium AgentReasoningParamEffort = "medium"`

            - `const AgentReasoningParamEffortHigh AgentReasoningParamEffort = "high"`

            - `const AgentReasoningParamEffortXhigh AgentReasoningParamEffort = "xhigh"`

            - `const AgentReasoningParamEffortMax AgentReasoningParamEffort = "max"`

          - `Summary AgentReasoningParamSummary`

            Controls whether the response includes a reasoning summary.

            - `const AgentReasoningParamSummaryConcise AgentReasoningParamSummary = "concise"`

              Returns a concise reasoning summary when supported.

            - `const AgentReasoningParamSummaryDetailed AgentReasoningParamSummary = "detailed"`

              Returns a detailed reasoning summary when supported.

            - `const AgentReasoningParamSummaryAuto AgentReasoningParamSummary = "auto"`

              Automatically selects the most detailed summary supported by the model.

        - `ServiceTier string`

          The service tier used for model requests.

          - `const AutomationTargetParamNewSessionAgentServiceTierAuto AutomationTargetParamNewSessionAgentServiceTier = "auto"`

            Selects the service tier automatically.

          - `const AutomationTargetParamNewSessionAgentServiceTierDefault AutomationTargetParamNewSessionAgentServiceTier = "default"`

            Uses the default service tier.

          - `const AutomationTargetParamNewSessionAgentServiceTierFlex AutomationTargetParamNewSessionAgentServiceTier = "flex"`

            Uses the flex service tier.

          - `const AutomationTargetParamNewSessionAgentServiceTierPriority AutomationTargetParamNewSessionAgentServiceTier = "priority"`

            Uses the priority service tier.

          - `const AutomationTargetParamNewSessionAgentServiceTierFast AutomationTargetParamNewSessionAgentServiceTier = "fast"`

            Uses the fast service tier.

          - `const AutomationTargetParamNewSessionAgentServiceTierUltrafast AutomationTargetParamNewSessionAgentServiceTier = "ultrafast"`

            Uses the ultrafast service tier.

        - `Text AgentTextParamResp`

          Configuration for text generated by the agent.

          - `Format TextFormatParamUnionResp`

            The output format. Omission uses ordinary text (`{"type": "text"}`).

            - `TextFormatParamTextResp`

              - `Type Text`

                The type of the object. Always `text`.

                - `const TextText Text = "text"`

            - `TextFormatParamJSONSchemaResp`

              - `Schema map[string, any]`

                The JSON Schema that generated text must match.

              - `Type JSONSchema`

                The type of the object. Always `json_schema`.

                - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

          - `Verbosity AgentTextParamVerbosity`

            The amount of text the model should produce. Defaults to `medium`, matching Responses.

            - `const AgentTextParamVerbosityLow AgentTextParamVerbosity = "low"`

              Produces less text.

            - `const AgentTextParamVerbosityMedium AgentTextParamVerbosity = "medium"`

              Uses the default amount of text.

            - `const AgentTextParamVerbosityHigh AgentTextParamVerbosity = "high"`

              Produces more text.

        - `Tools []AgentToolParamUnionResp`

          Tools available to the agent. Omit to inherit, or pass null to clear them. The resolved tool list must fit within 3 MiB (3,145,728 bytes) of compact UTF-8 JSON.

          `minItems: 0`, `maxItems: 16384`

          - `AgentToolParamFunctionResp`

            - `Description string`

              A description of what the function does.

              `minLength: 0`, `maxLength: 1048576`

            - `Name string`

              The name of the function.

              `minLength: 0`, `maxLength: 1048576`

            - `Parameters map[string, any]`

              A JSON Schema object describing the function's arguments.

            - `Type Function`

              The type of the object. Always `function`.

              - `const FunctionFunction Function = "function"`

            - `Async bool`

              Whether the agent continues without waiting for the function result. Defaults to `false`.

            - `DeferLoading bool`

              Whether this function is deferred and discovered through tool search. Defaults to `false`.

          - `AgentToolParamToolSearchResp`

            - `Type ToolSearch`

              The type of the object. Always `tool_search`.

              - `const ToolSearchToolSearch ToolSearch = "tool_search"`

          - `AgentToolParamProgrammaticToolCallingResp`

            - `Type ProgrammaticToolCalling`

              The type of the object. Always `programmatic_tool_calling`.

              - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

            - `Enabled bool`

              Whether tools can be called from model-generated code. Defaults to `true`.

          - `AgentToolParamMcpResp`

            - `ServerLabel string`

              A label used to identify the MCP server in tool calls.

              `minLength: 0`, `maxLength: 1048576`

            - `Transport McpTransportParamUnionResp`

              The transport used to connect to the MCP server.

              - `McpTransportParamHTTPResp`

                - `ServerURL string`

                  The URL of the MCP server.

                  `minLength: 0`, `maxLength: 1048576`

                - `Type HTTP`

                  The type of the object. Always `http`.

                  - `const HTTPHTTP HTTP = "http"`

                - `Authorization string`

                  The authorization value sent to the MCP server, if any.

                  `minLength: 0`, `maxLength: 1048576`

                - `Headers map[string, string]`

                  Additional HTTP headers sent to the MCP server.

              - `McpTransportParamStdioResp`

                - `Command string`

                  The command used to start the MCP server.

                  `minLength: 0`, `maxLength: 1048576`

                - `Cwd string`

                  The working directory used to start the MCP server.

                  `minLength: 0`, `maxLength: 1048576`

                - `Type Stdio`

                  The type of the object. Always `stdio`.

                  - `const StdioStdio Stdio = "stdio"`

                - `Args []string`

                  Arguments passed to the MCP server command.

                  `minItems: 0`, `maxItems: 16384`

                - `Env map[string, string]`

                  Environment variables set for the MCP server process.

                - `EnvVars []string`

                  Environment variable names to inherit from the selected execution environment.

                  `minItems: 0`, `maxItems: 16384`

            - `Type Mcp`

              The type of the object. Always `mcp`.

              - `const McpMcp Mcp = "mcp"`

            - `AllowedTools []string`

              The MCP tools the agent may call. All server tools are allowed when omitted.

              `minItems: 0`, `maxItems: 16384`

            - `ConnectionOrigin string`

              Selects where outbound MCP HTTP connections originate. Omitted or `service` uses the Managed Agents service network; `environment` uses the session's selected environment.

              - `const AgentToolParamMcpConnectionOriginService AgentToolParamMcpConnectionOrigin = "service"`

                Uses the Managed Agents service network.

              - `const AgentToolParamMcpConnectionOriginEnvironment AgentToolParamMcpConnectionOrigin = "environment"`

                Uses the session's execution environment.

            - `CredentialID string`

              The attached vault credential used to authenticate this MCP server. Optional when exactly one attached credential matches the server URL.

              `minLength: 0`, `maxLength: 1048576`

            - `RequestMetadata map[string, any]`

              Metadata included with requests to this MCP server.

            - `Required bool`

              Whether this MCP server must initialize before the first turn. Defaults to `false`.

          - `AgentToolParamWebSearchResp`

            - `Type WebSearch`

              The type of the object. Always `web_search`.

              - `const WebSearchWebSearch WebSearch = "web_search"`

            - `AllowedDomains []string`

              Domains the search may include.

              `minItems: 0`, `maxItems: 16384`

            - `ContextSize string`

              The amount of search context made available to the model. Defaults to `medium`.

              - `const AgentToolParamWebSearchContextSizeLow AgentToolParamWebSearchContextSize = "low"`

              - `const AgentToolParamWebSearchContextSizeMedium AgentToolParamWebSearchContextSize = "medium"`

              - `const AgentToolParamWebSearchContextSizeHigh AgentToolParamWebSearchContextSize = "high"`

            - `Location AgentToolParamWebSearchLocationResp`

              Approximate location used to localize search results.

              - `City string`

                The city name.

                `minLength: 0`, `maxLength: 1048576`

              - `Country string`

                The two-letter ISO country code, such as `US`.

                `minLength: 0`, `maxLength: 1048576`

              - `Region string`

                The region or state name.

                `minLength: 0`, `maxLength: 1048576`

              - `Timezone string`

                The IANA timezone, such as `America/Los_Angeles`.

                `minLength: 0`, `maxLength: 1048576`

            - `Mode string`

              The source used for web search results. Defaults to `live`.

              - `const AgentToolParamWebSearchModeDisabled AgentToolParamWebSearchMode = "disabled"`

                Disables web search.

              - `const AgentToolParamWebSearchModeCached AgentToolParamWebSearchMode = "cached"`

                Uses cached search results.

              - `const AgentToolParamWebSearchModeLive AgentToolParamWebSearchMode = "live"`

                Searches the live web.

          - `AgentToolParamComputerUseResp`

            - `Type ComputerUse`

              The type of the object. Always `computer_use`.

              - `const ComputerUseComputerUse ComputerUse = "computer_use"`

            - `IncludeScreenshots bool`

              Whether computer tool outputs include screenshots. Defaults to `false`.

          - `AgentToolParamAutomationsResp`

            - `Type Automations`

              The type of the object. Always `automations`.

              - `const AutomationsAutomations Automations = "automations"`

      - `AgentID string`

        A saved agent ID. Provide exactly one of agent and agent_id.

        `minLength: 0`, `maxLength: 64`

      - `Metadata map[string, string]`

        Metadata attached to each new session.

      - `VaultIDs []string`

        The IDs of vaults made available to each new session.

        `minItems: 0`, `maxItems: 16384`

    - `AutomationTargetParamExistingSessionResp`

      - `Instructions string`

        Instructions delivered as an automation notification.

        `minLength: 0`, `maxLength: 1048576`

      - `SessionID string`

        The session receiving each invocation.

        `minLength: 0`, `maxLength: 1048576`

      - `Type ExistingSession`

        The type of the object. Always `existing_session`.

        - `const ExistingSessionExistingSession ExistingSession = "existing_session"`

  - `Timezone param.Field[string]`

    The IANA timezone used to interpret the cron expression.

  - `Type param.Field[Periodic]`

    The type of the object. Always `periodic`.

    - `const PeriodicPeriodic Periodic = "periodic"`

  - `Metadata param.Field[unknown]`

### Returns

- `type AutomationUnion interface{…}`

  A saved automation and its schedule.

  - `type PeriodicAutomation struct{…}`

    Fields shared by periodic and one-time automations.

    - `ID string`

      The automation ID.

      `minLength: 0`

    - `CreatedAt int64`

      The creation time as a Unix timestamp in seconds.

      `format: int64`

    - `CreatedBy AutomationCreatedByUnion`

      Service-recorded provenance; callers cannot supply this field.

      - `type AutomationCreatedByDeveloper struct{…}`

        - `Type Developer`

          The type of the object. Always `developer`.

          - `const DeveloperDeveloper Developer = "developer"`

      - `type AutomationCreatedByAgent struct{…}`

        - `SessionID string`

          The creator session, which is also the automation's target.

          `minLength: 0`

        - `ToolCallID string`

          The tool call that created the automation.

          `minLength: 0`

        - `Type Agent`

          The type of the object. Always `agent`.

          - `const AgentAgent Agent = "agent"`

    - `Expression string`

      The cron expression determining scheduled occurrences.

      `minLength: 0`

    - `Metadata map[string, string]`

      Custom string key-value pairs attached to the automation.

    - `Name string`

      The automation's display name.

      `minLength: 0`

    - `Object AgentAutomation`

      Always `agent.automation`.

      - `const AgentAutomationAgentAutomation AgentAutomation = "agent.automation"`

    - `Status PeriodicAutomationStatus`

      Whether scheduled delivery is active or paused.

      - `const PeriodicAutomationStatusActive PeriodicAutomationStatus = "active"`

      - `const PeriodicAutomationStatusPaused PeriodicAutomationStatus = "paused"`

    - `Target AutomationTargetUnion`

      The session configuration or existing session receiving invocations.

      - `type AutomationTargetNewSession struct{…}`

        - `Agent AutomationAgentConfig`

          The inline agent configuration, or null when agent_id is configured.

          - `Instructions string`

            Custom instructions, or null when absent.

            `minLength: 0`

          - `Model string`

            The requested model name.

            `minLength: 0`

          - `MultiAgent MultiAgentConfig`

            The configuration for creating and coordinating subagents.

            - `Enabled bool`

              Whether subagent tools are enabled. Defaults to false.

            - `MaxConcurrentSubagents int64`

              Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

              `format: int64`, `minimum: 1`, `maximum: 4294967295`

          - `Reasoning AgentReasoning`

            The configured reasoning policy.

            - `Effort AgentReasoningEffort`

              The requested reasoning effort, or `null` when the model selects its own default.

              - `const AgentReasoningEffortNone AgentReasoningEffort = "none"`

              - `const AgentReasoningEffortMinimal AgentReasoningEffort = "minimal"`

              - `const AgentReasoningEffortLow AgentReasoningEffort = "low"`

              - `const AgentReasoningEffortMedium AgentReasoningEffort = "medium"`

              - `const AgentReasoningEffortHigh AgentReasoningEffort = "high"`

              - `const AgentReasoningEffortXhigh AgentReasoningEffort = "xhigh"`

              - `const AgentReasoningEffortMax AgentReasoningEffort = "max"`

            - `Summary AgentReasoningSummary`

              The requested reasoning summary format, or `null` when summaries are disabled.

              - `const AgentReasoningSummaryConcise AgentReasoningSummary = "concise"`

                Returns a concise reasoning summary when supported.

              - `const AgentReasoningSummaryDetailed AgentReasoningSummary = "detailed"`

                Returns a detailed reasoning summary when supported.

              - `const AgentReasoningSummaryAuto AgentReasoningSummary = "auto"`

                Automatically selects the most detailed summary supported by the model.

          - `ServiceTier AutomationAgentConfigServiceTier`

            The configured service-tier policy.

            - `const AutomationAgentConfigServiceTierAuto AutomationAgentConfigServiceTier = "auto"`

            - `const AutomationAgentConfigServiceTierDefault AutomationAgentConfigServiceTier = "default"`

            - `const AutomationAgentConfigServiceTierFlex AutomationAgentConfigServiceTier = "flex"`

            - `const AutomationAgentConfigServiceTierPriority AutomationAgentConfigServiceTier = "priority"`

            - `const AutomationAgentConfigServiceTierFast AutomationAgentConfigServiceTier = "fast"`

            - `const AutomationAgentConfigServiceTierUltrafast AutomationAgentConfigServiceTier = "ultrafast"`

          - `Text AgentText`

            The configured output format and verbosity.

            - `Format TextFormatUnion`

              The effective output format. Defaults to ordinary text.

              - `type TextFormatText struct{…}`

                Generates ordinary text without a structured-output constraint.

                - `Type Text`

                  The type of the object. Always `text`.

                  - `const TextText Text = "text"`

              - `type TextFormatJSONSchema struct{…}`

                Constrains generated text to a JSON Schema.

                - `Schema map[string, any]`

                  The JSON Schema that generated text must match.

                - `Type JSONSchema`

                  The type of the object. Always `json_schema`.

                  - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

            - `Verbosity AgentTextVerbosity`

              The amount of text produced by the agent. Defaults to `medium`.

              - `const AgentTextVerbosityLow AgentTextVerbosity = "low"`

              - `const AgentTextVerbosityMedium AgentTextVerbosity = "medium"`

              - `const AgentTextVerbosityHigh AgentTextVerbosity = "high"`

          - `Tools []AgentToolUnion`

            Configured tools, excluding confidential credentials.

            `minItems: 0`, `maxItems: 2000`

            - `type AgentToolFunction struct{…}`

              A function defined by the application.

              - `DeferLoading bool`

                Whether the function is deferred and discovered through tool search.

              - `Description string`

                A description of what the function does.

                `minLength: 0`

              - `Name string`

                The name of the function.

                `minLength: 0`

              - `Parameters map[string, any]`

                A JSON Schema object describing the function's arguments.

              - `Type Function`

                The type of the object. Always `function`.

                - `const FunctionFunction Function = "function"`

              - `Async bool`

                Whether the agent continues without waiting for the function result.

            - `type AgentToolProgrammaticToolCalling struct{…}`

              Enables calling tools from model-generated code.

              - `Enabled bool`

                Whether tools can be called from model-generated code.

              - `Type ProgrammaticToolCalling`

                The type of the object. Always `programmatic_tool_calling`.

                - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

            - `type AgentToolMcp struct{…}`

              Tools provided by a remote MCP server.

              - `AllowedTools []string`

                The MCP tools the agent may call.

                `minItems: 0`, `maxItems: 2000`

              - `ConnectionOrigin string`

                Where outbound MCP HTTP connections originate.

                - `const AgentToolMcpConnectionOriginService AgentToolMcpConnectionOrigin = "service"`

                - `const AgentToolMcpConnectionOriginEnvironment AgentToolMcpConnectionOrigin = "environment"`

              - `CredentialID string`

                The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

                `minLength: 0`

              - `RequestMetadata map[string, any]`

                Metadata included with requests to this MCP server.

              - `Required bool`

                Whether this MCP server must initialize before the first turn.

              - `ServerLabel string`

                A label used to identify the MCP server in tool calls.

                `minLength: 0`

              - `Transport McpTransportUnion`

                The transport used to connect to the MCP server.

                - `type McpTransportHTTP struct{…}`

                  Connects to an MCP server over HTTP.

                  - `ServerURL string`

                    The URL of the MCP server.

                    `minLength: 0`

                  - `Type HTTP`

                    The type of the object. Always `http`.

                    - `const HTTPHTTP HTTP = "http"`

                - `type McpTransportStdio struct{…}`

                  Starts an MCP server as a local process.

                  - `Args []string`

                    Arguments passed to the MCP server command.

                    `minItems: 0`, `maxItems: 2000`

                  - `Command string`

                    The command used to start the MCP server.

                    `minLength: 0`

                  - `Cwd string`

                    The working directory used to start the MCP server.

                    `minLength: 0`

                  - `EnvVars []string`

                    Environment variable names inherited from the execution environment.

                    `minItems: 0`, `maxItems: 2000`

                  - `Type Stdio`

                    The type of the object. Always `stdio`.

                    - `const StdioStdio Stdio = "stdio"`

              - `Type Mcp`

                The type of the object. Always `mcp`.

                - `const McpMcp Mcp = "mcp"`

            - `type AgentToolWebSearch struct{…}`

              Web search.

              - `AllowedDomains []string`

                Allowed search domains, or `null` when the search is unrestricted.

                `minItems: 0`, `maxItems: 2000`

              - `ContextSize string`

                The amount of search context made available to the model. Defaults to `medium`.

                - `const AgentToolWebSearchContextSizeLow AgentToolWebSearchContextSize = "low"`

                - `const AgentToolWebSearchContextSizeMedium AgentToolWebSearchContextSize = "medium"`

                - `const AgentToolWebSearchContextSizeHigh AgentToolWebSearchContextSize = "high"`

              - `Location AgentToolWebSearchLocation`

                Approximate location used to localize search results, if provided.

                - `City string`

                  The city name.

                  `minLength: 0`

                - `Country string`

                  The two-letter ISO country code, such as `US`.

                  `minLength: 0`

                - `Region string`

                  The region or state name.

                  `minLength: 0`

                - `Timezone string`

                  The IANA timezone, such as `America/Los_Angeles`.

                  `minLength: 0`

              - `Mode string`

                The source used for web search results.

                - `const AgentToolWebSearchModeDisabled AgentToolWebSearchMode = "disabled"`

                - `const AgentToolWebSearchModeCached AgentToolWebSearchMode = "cached"`

                - `const AgentToolWebSearchModeLive AgentToolWebSearchMode = "live"`

              - `Type WebSearch`

                The type of the object. Always `web_search`.

                - `const WebSearchWebSearch WebSearch = "web_search"`

            - `type AgentToolComputerUse struct{…}`

              Browser use in an OpenAI-hosted session.

              - `IncludeScreenshots bool`

                Whether computer tool outputs include screenshots.

              - `Type ComputerUse`

                The type of the object. Always `computer_use`.

                - `const ComputerUseComputerUse ComputerUse = "computer_use"`

            - `type AgentToolAutomations struct{…}`

              Lets the agent manage its own scheduled wakeups.

              - `Type Automations`

                The type of the object. Always `automations`.

                - `const AutomationsAutomations Automations = "automations"`

          - `Compaction AutomationAgentConfigCompaction`

            The effective context compaction settings.

            - `Async bool`

              Whether context is compacted in the background. Defaults to true.

          - `Experimental AutomationAgentConfigExperimental`

            The effective experimental settings for the agent.

            - `TimeAwareness bool`

              Whether the model receives periodic current-time reminders.

        - `AgentID string`

          The saved agent reference, or null when an inline agent is configured.

          `minLength: 0`

        - `Environment AutomationEnvironmentUnion`

          Configuration or references used to select the execution environment.

          - `type AutomationEnvironmentNone struct{…}`

            - `Type None`

              The type of the object. Always `none`.

              - `const NoneNone None = "none"`

          - `type AutomationEnvironmentOpenAIHosted struct{…}`

            Hosted environment selection with confidential setup commands and variables omitted.

            - `CapabilityDirectories []string`

              Directory overrides, or null to inherit the template or creation default.

              `minItems: 0`, `maxItems: 2000`

            - `ContainerSize string`

              The configured container size, or null to use the creation default.

              - `const AutomationEnvironmentOpenAIHostedContainerSizeSmall AutomationEnvironmentOpenAIHostedContainerSize = "small"`

              - `const AutomationEnvironmentOpenAIHostedContainerSizeMedium AutomationEnvironmentOpenAIHostedContainerSize = "medium"`

              - `const AutomationEnvironmentOpenAIHostedContainerSizeLarge AutomationEnvironmentOpenAIHostedContainerSize = "large"`

            - `Desktop AutomationEnvironmentOpenAIHostedDesktop`

              Desktop overrides, or null to inherit the template or creation default.

              - `Enabled bool`

                Whether the environment provisions a desktop and browser proxy.

            - `EnvironmentID string`

              An existing environment reference, or null when provisioning a new environment.

              `minLength: 0`

            - `EnvironmentTemplateID string`

              A template reference, or null when no template is selected.

              `minLength: 0`

            - `Files []AutomationEnvironmentOpenAIHostedFileUnion`

              File overrides, excluding contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `type AutomationEnvironmentOpenAIHostedFileFileID struct{…}`

                A project-scoped Files API reference resolved separately for each session.

                - `FileID string`

                  The ID of the uploaded file.

                  `minLength: 0`

                - `Path string`

                  The file's absolute path inside the environment.

                  `minLength: 0`

                - `Type FileID`

                  The type of the object. Always `file_id`.

                  - `const FileIDFileID FileID = "file_id"`

              - `type AutomationEnvironmentOpenAIHostedFileInline struct{…}`

                Metadata for confidential inline file contents.

                - `Path string`

                  The file's absolute path inside the environment.

                  `minLength: 0`

                - `SizeBytes int64`

                  The decoded size of the inline file in bytes.

                  `format: int64`, `minimum: 0`

                - `Type Inline`

                  The type of the object. Always `inline`.

                  - `const InlineInline Inline = "inline"`

            - `Network AutomationEnvironmentOpenAIHostedNetwork`

              Network overrides, or null to inherit the template or creation default.

              - `Access string`

                The environment's network access mode.

                - `const AutomationEnvironmentOpenAIHostedNetworkAccessEnabled AutomationEnvironmentOpenAIHostedNetworkAccess = "enabled"`

                  Allows unrestricted network access.

                - `const AutomationEnvironmentOpenAIHostedNetworkAccessDisabled AutomationEnvironmentOpenAIHostedNetworkAccess = "disabled"`

                  Disables network access.

                - `const AutomationEnvironmentOpenAIHostedNetworkAccessRestricted AutomationEnvironmentOpenAIHostedNetworkAccess = "restricted"`

                  Applies the configured domain restrictions.

              - `AllowedDomains []string`

                Domains the environment may access when network access is restricted.

                `minItems: 0`, `maxItems: 2000`

            - `Packages AutomationEnvironmentOpenAIHostedPackages`

              Package overrides, or null to inherit the template or creation default.

              - `Npm []string`

                npm packages installed globally in the environment.

                `minItems: 0`, `maxItems: 16384`

              - `Python []string`

                Python packages installed in the environment.

                `minItems: 0`, `maxItems: 16384`

              - `System []string`

                System packages installed in the environment.

                `minItems: 0`, `maxItems: 16384`

            - `Plugins []HostedPlugin`

              Plugin overrides, excluding archive contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `Description string`

                The installed plugin description.

                `minLength: 0`

              - `Name string`

                The installed plugin name.

                `minLength: 0`

              - `Type Inline`

                The type of the object. Always `inline`.

                - `const InlineInline Inline = "inline"`

            - `Skills []AutomationEnvironmentOpenAIHostedSkillUnion`

              Skill overrides, excluding archive contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `type AutomationEnvironmentOpenAIHostedSkillSkillReference struct{…}`

                A skill resolved afresh from the Skills API whenever a session starts.

                - `SkillID string`

                  The referenced skill ID.

                  `minLength: 0`

                - `Type SkillReference`

                  The type of the object. Always `skill_reference`.

                  - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

                - `Version string`

                  The requested version selector, including `latest`.

                  `minLength: 0`

              - `type AutomationEnvironmentOpenAIHostedSkillInline struct{…}`

                Safe metadata for an inline skill archive.

                - `Description string`

                  The skill description declared in `SKILL.md`.

                  `minLength: 0`

                - `Name string`

                  The skill name declared in `SKILL.md`.

                  `minLength: 0`

                - `Type Inline`

                  The type of the object. Always `inline`.

                  - `const InlineInline Inline = "inline"`

            - `Type OpenAIHosted`

              The type of the object. Always `openai_hosted`.

              - `const OpenAIHostedOpenAIHosted OpenAIHosted = "openai_hosted"`

          - `type AutomationEnvironmentSelfHosted struct{…}`

            - `CapabilityDirectories []string`

              Directories that expose capabilities to the agent.

              `minItems: 0`, `maxItems: 2000`

            - `EnvironmentID string`

              An existing registration, or null to create a session-owned environment.

              `minLength: 0`

            - `Type SelfHosted`

              The type of the object. Always `self_hosted`.

              - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

            - `WorkspaceDirectory string`

              The absolute project directory in the environment.

              `minLength: 0`

        - `Input []AutomationTargetNewSessionInput`

          Initial input delivered to each new session.

          `minItems: 0`, `maxItems: 2000`

          - `Content []InputContentUnion`

            The content of the message.

            `minItems: 0`, `maxItems: 2000`

            - `type InputContentInputText struct{…}`

              Text input recorded in a session item.

              - `Text string`

                The text supplied to the agent.

                `minLength: 0`

              - `Type InputText`

                The type of the object. Always `input_text`.

                - `const InputTextInputText InputText = "input_text"`

            - `type InputContentInputImage struct{…}`

              Image input recorded in a session item.

              - `ImageURL string`

                The URL of the image supplied to the agent, which may be a base64-encoded data URL.

                `minLength: 0`

              - `Type InputImage`

                The type of the object. Always `input_image`.

                - `const InputImageInputImage InputImage = "input_image"`

          - `Role User`

            The role of the message author. Always `user`.

            - `const UserUser User = "user"`

          - `Type Message`

            The type of the input item. Always `message`.

            - `const MessageMessage Message = "message"`

        - `Metadata map[string, string]`

          Metadata attached to each new session.

        - `Type NewSession`

          The type of the object. Always `new_session`.

          - `const NewSessionNewSession NewSession = "new_session"`

        - `VaultIDs []string`

          Vaults made available to each new session.

          `minItems: 0`, `maxItems: 2000`

      - `type AutomationTargetExistingSession struct{…}`

        - `Instructions string`

          Saved instructions delivered as an automation notification.

          `minLength: 0`

        - `SessionID string`

          The session receiving each invocation.

          `minLength: 0`

        - `Type ExistingSession`

          The type of the object. Always `existing_session`.

          - `const ExistingSessionExistingSession ExistingSession = "existing_session"`

    - `Timezone string`

      The timezone used to interpret the expression.

      `minLength: 0`

    - `Type Periodic`

      The type of the object. Always `periodic`.

      - `const PeriodicPeriodic Periodic = "periodic"`

  - `type OneTimeAutomation struct{…}`

    Fields shared by periodic and one-time automations.

    - `ID string`

      The automation ID.

      `minLength: 0`

    - `CreatedAt int64`

      The creation time as a Unix timestamp in seconds.

      `format: int64`

    - `CreatedBy AutomationCreatedByUnion`

      Service-recorded provenance; callers cannot supply this field.

    - `Metadata map[string, string]`

      Custom string key-value pairs attached to the automation.

    - `Name string`

      The automation's display name.

      `minLength: 0`

    - `Object AgentAutomation`

      Always `agent.automation`.

      - `const AgentAutomationAgentAutomation AgentAutomation = "agent.automation"`

    - `RunAt int64`

      The Unix timestamp, in seconds, of the scheduled occurrence.

      `format: int64`

    - `Status OneTimeAutomationStatus`

      Completion means the schedule has finished, not the agent's work.

      - `const OneTimeAutomationStatusActive OneTimeAutomationStatus = "active"`

      - `const OneTimeAutomationStatusPaused OneTimeAutomationStatus = "paused"`

      - `const OneTimeAutomationStatusCompleted OneTimeAutomationStatus = "completed"`

    - `Target AutomationTargetUnion`

      The session configuration or existing session receiving invocations.

    - `Type Once`

      The type of the object. Always `once`.

      - `const OnceOnce Once = "once"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  automation, err := client.Beta.Agents.Automations.New(context.TODO(), openai.BetaAgentAutomationNewParams{
    AutomationScheduleParamUnionResp: openai.AutomationScheduleParamUnion{
      OfPeriodic: &openai.AutomationScheduleParamPeriodic{
        Expression: "x",
        Name: "x",
        Target: openai.AutomationTargetParamUnion{
          OfNewSession: &openai.AutomationTargetParamNewSession{
            Environment: openai.EnvironmentParamUnion{
              OfNone: &openai.EnvironmentParamNone{

              },
            },
            Input: []openai.AgentSessionInputMessageParam{openai.AgentSessionInputMessageParam{
              Content: []openai.InputContentParamUnion{openai.InputContentParamUnion{
                OfInputText: &openai.InputContentParamInputText{
                  Text: "text",
                },
              }},
            }},
          },
        },
        Timezone: "x",
      },
    },
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", automation)
}
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

`client.Beta.Agents.Automations.Delete(ctx, automationID) (*AutomationDeleted, error)`

**delete** `/agents/automations/{automation_id}`

Deletes the automation and prevents future invocations without deleting its target session.

### Parameters

- `automationID string`

  `minLength: 0`, `maxLength: 1048576`

### Returns

- `type AutomationDeleted struct{…}`

  - `ID string`

    The deleted automation ID.

    `minLength: 0`

  - `Deleted bool`

    Always true.

  - `Object AgentAutomationDeleted`

    Always `agent.automation.deleted`.

    - `const AgentAutomationDeletedAgentAutomationDeleted AgentAutomationDeleted = "agent.automation.deleted"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  automationDeleted, err := client.Beta.Agents.Automations.Delete(context.TODO(), "automation_id")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", automationDeleted.ID)
}
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

`client.Beta.Agents.Automations.List(ctx, query) (*CursorPage[AutomationUnion], error)`

**get** `/agents/automations`

Lists project-owned automations, optionally filtered by target session.

### Parameters

- `query BetaAgentAutomationListParams`

  - `After param.Field[string]`

    Return resources after this resource ID in the selected order.

    `minLength: 0`, `maxLength: 1048576`

  - `Limit param.Field[int64]`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

    `format: int64`, `minimum: 1`, `maximum: 100`

  - `Order param.Field[BetaAgentAutomationListParamsOrder]`

    The order in which resources are returned. Defaults to `desc`.

    - `const BetaAgentAutomationListParamsOrderAsc BetaAgentAutomationListParamsOrder = "asc"`

      Returns resources in ascending order.

    - `const BetaAgentAutomationListParamsOrderDesc BetaAgentAutomationListParamsOrder = "desc"`

      Returns resources in descending order.

  - `SessionID param.Field[string]`

    Matches existing-session targets, including agent-created automations.

    `minLength: 0`, `maxLength: 1048576`

### Returns

- `type AutomationUnion interface{…}`

  A saved automation and its schedule.

  - `type PeriodicAutomation struct{…}`

    Fields shared by periodic and one-time automations.

    - `ID string`

      The automation ID.

      `minLength: 0`

    - `CreatedAt int64`

      The creation time as a Unix timestamp in seconds.

      `format: int64`

    - `CreatedBy AutomationCreatedByUnion`

      Service-recorded provenance; callers cannot supply this field.

      - `type AutomationCreatedByDeveloper struct{…}`

        - `Type Developer`

          The type of the object. Always `developer`.

          - `const DeveloperDeveloper Developer = "developer"`

      - `type AutomationCreatedByAgent struct{…}`

        - `SessionID string`

          The creator session, which is also the automation's target.

          `minLength: 0`

        - `ToolCallID string`

          The tool call that created the automation.

          `minLength: 0`

        - `Type Agent`

          The type of the object. Always `agent`.

          - `const AgentAgent Agent = "agent"`

    - `Expression string`

      The cron expression determining scheduled occurrences.

      `minLength: 0`

    - `Metadata map[string, string]`

      Custom string key-value pairs attached to the automation.

    - `Name string`

      The automation's display name.

      `minLength: 0`

    - `Object AgentAutomation`

      Always `agent.automation`.

      - `const AgentAutomationAgentAutomation AgentAutomation = "agent.automation"`

    - `Status PeriodicAutomationStatus`

      Whether scheduled delivery is active or paused.

      - `const PeriodicAutomationStatusActive PeriodicAutomationStatus = "active"`

      - `const PeriodicAutomationStatusPaused PeriodicAutomationStatus = "paused"`

    - `Target AutomationTargetUnion`

      The session configuration or existing session receiving invocations.

      - `type AutomationTargetNewSession struct{…}`

        - `Agent AutomationAgentConfig`

          The inline agent configuration, or null when agent_id is configured.

          - `Instructions string`

            Custom instructions, or null when absent.

            `minLength: 0`

          - `Model string`

            The requested model name.

            `minLength: 0`

          - `MultiAgent MultiAgentConfig`

            The configuration for creating and coordinating subagents.

            - `Enabled bool`

              Whether subagent tools are enabled. Defaults to false.

            - `MaxConcurrentSubagents int64`

              Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

              `format: int64`, `minimum: 1`, `maximum: 4294967295`

          - `Reasoning AgentReasoning`

            The configured reasoning policy.

            - `Effort AgentReasoningEffort`

              The requested reasoning effort, or `null` when the model selects its own default.

              - `const AgentReasoningEffortNone AgentReasoningEffort = "none"`

              - `const AgentReasoningEffortMinimal AgentReasoningEffort = "minimal"`

              - `const AgentReasoningEffortLow AgentReasoningEffort = "low"`

              - `const AgentReasoningEffortMedium AgentReasoningEffort = "medium"`

              - `const AgentReasoningEffortHigh AgentReasoningEffort = "high"`

              - `const AgentReasoningEffortXhigh AgentReasoningEffort = "xhigh"`

              - `const AgentReasoningEffortMax AgentReasoningEffort = "max"`

            - `Summary AgentReasoningSummary`

              The requested reasoning summary format, or `null` when summaries are disabled.

              - `const AgentReasoningSummaryConcise AgentReasoningSummary = "concise"`

                Returns a concise reasoning summary when supported.

              - `const AgentReasoningSummaryDetailed AgentReasoningSummary = "detailed"`

                Returns a detailed reasoning summary when supported.

              - `const AgentReasoningSummaryAuto AgentReasoningSummary = "auto"`

                Automatically selects the most detailed summary supported by the model.

          - `ServiceTier AutomationAgentConfigServiceTier`

            The configured service-tier policy.

            - `const AutomationAgentConfigServiceTierAuto AutomationAgentConfigServiceTier = "auto"`

            - `const AutomationAgentConfigServiceTierDefault AutomationAgentConfigServiceTier = "default"`

            - `const AutomationAgentConfigServiceTierFlex AutomationAgentConfigServiceTier = "flex"`

            - `const AutomationAgentConfigServiceTierPriority AutomationAgentConfigServiceTier = "priority"`

            - `const AutomationAgentConfigServiceTierFast AutomationAgentConfigServiceTier = "fast"`

            - `const AutomationAgentConfigServiceTierUltrafast AutomationAgentConfigServiceTier = "ultrafast"`

          - `Text AgentText`

            The configured output format and verbosity.

            - `Format TextFormatUnion`

              The effective output format. Defaults to ordinary text.

              - `type TextFormatText struct{…}`

                Generates ordinary text without a structured-output constraint.

                - `Type Text`

                  The type of the object. Always `text`.

                  - `const TextText Text = "text"`

              - `type TextFormatJSONSchema struct{…}`

                Constrains generated text to a JSON Schema.

                - `Schema map[string, any]`

                  The JSON Schema that generated text must match.

                - `Type JSONSchema`

                  The type of the object. Always `json_schema`.

                  - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

            - `Verbosity AgentTextVerbosity`

              The amount of text produced by the agent. Defaults to `medium`.

              - `const AgentTextVerbosityLow AgentTextVerbosity = "low"`

              - `const AgentTextVerbosityMedium AgentTextVerbosity = "medium"`

              - `const AgentTextVerbosityHigh AgentTextVerbosity = "high"`

          - `Tools []AgentToolUnion`

            Configured tools, excluding confidential credentials.

            `minItems: 0`, `maxItems: 2000`

            - `type AgentToolFunction struct{…}`

              A function defined by the application.

              - `DeferLoading bool`

                Whether the function is deferred and discovered through tool search.

              - `Description string`

                A description of what the function does.

                `minLength: 0`

              - `Name string`

                The name of the function.

                `minLength: 0`

              - `Parameters map[string, any]`

                A JSON Schema object describing the function's arguments.

              - `Type Function`

                The type of the object. Always `function`.

                - `const FunctionFunction Function = "function"`

              - `Async bool`

                Whether the agent continues without waiting for the function result.

            - `type AgentToolProgrammaticToolCalling struct{…}`

              Enables calling tools from model-generated code.

              - `Enabled bool`

                Whether tools can be called from model-generated code.

              - `Type ProgrammaticToolCalling`

                The type of the object. Always `programmatic_tool_calling`.

                - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

            - `type AgentToolMcp struct{…}`

              Tools provided by a remote MCP server.

              - `AllowedTools []string`

                The MCP tools the agent may call.

                `minItems: 0`, `maxItems: 2000`

              - `ConnectionOrigin string`

                Where outbound MCP HTTP connections originate.

                - `const AgentToolMcpConnectionOriginService AgentToolMcpConnectionOrigin = "service"`

                - `const AgentToolMcpConnectionOriginEnvironment AgentToolMcpConnectionOrigin = "environment"`

              - `CredentialID string`

                The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

                `minLength: 0`

              - `RequestMetadata map[string, any]`

                Metadata included with requests to this MCP server.

              - `Required bool`

                Whether this MCP server must initialize before the first turn.

              - `ServerLabel string`

                A label used to identify the MCP server in tool calls.

                `minLength: 0`

              - `Transport McpTransportUnion`

                The transport used to connect to the MCP server.

                - `type McpTransportHTTP struct{…}`

                  Connects to an MCP server over HTTP.

                  - `ServerURL string`

                    The URL of the MCP server.

                    `minLength: 0`

                  - `Type HTTP`

                    The type of the object. Always `http`.

                    - `const HTTPHTTP HTTP = "http"`

                - `type McpTransportStdio struct{…}`

                  Starts an MCP server as a local process.

                  - `Args []string`

                    Arguments passed to the MCP server command.

                    `minItems: 0`, `maxItems: 2000`

                  - `Command string`

                    The command used to start the MCP server.

                    `minLength: 0`

                  - `Cwd string`

                    The working directory used to start the MCP server.

                    `minLength: 0`

                  - `EnvVars []string`

                    Environment variable names inherited from the execution environment.

                    `minItems: 0`, `maxItems: 2000`

                  - `Type Stdio`

                    The type of the object. Always `stdio`.

                    - `const StdioStdio Stdio = "stdio"`

              - `Type Mcp`

                The type of the object. Always `mcp`.

                - `const McpMcp Mcp = "mcp"`

            - `type AgentToolWebSearch struct{…}`

              Web search.

              - `AllowedDomains []string`

                Allowed search domains, or `null` when the search is unrestricted.

                `minItems: 0`, `maxItems: 2000`

              - `ContextSize string`

                The amount of search context made available to the model. Defaults to `medium`.

                - `const AgentToolWebSearchContextSizeLow AgentToolWebSearchContextSize = "low"`

                - `const AgentToolWebSearchContextSizeMedium AgentToolWebSearchContextSize = "medium"`

                - `const AgentToolWebSearchContextSizeHigh AgentToolWebSearchContextSize = "high"`

              - `Location AgentToolWebSearchLocation`

                Approximate location used to localize search results, if provided.

                - `City string`

                  The city name.

                  `minLength: 0`

                - `Country string`

                  The two-letter ISO country code, such as `US`.

                  `minLength: 0`

                - `Region string`

                  The region or state name.

                  `minLength: 0`

                - `Timezone string`

                  The IANA timezone, such as `America/Los_Angeles`.

                  `minLength: 0`

              - `Mode string`

                The source used for web search results.

                - `const AgentToolWebSearchModeDisabled AgentToolWebSearchMode = "disabled"`

                - `const AgentToolWebSearchModeCached AgentToolWebSearchMode = "cached"`

                - `const AgentToolWebSearchModeLive AgentToolWebSearchMode = "live"`

              - `Type WebSearch`

                The type of the object. Always `web_search`.

                - `const WebSearchWebSearch WebSearch = "web_search"`

            - `type AgentToolComputerUse struct{…}`

              Browser use in an OpenAI-hosted session.

              - `IncludeScreenshots bool`

                Whether computer tool outputs include screenshots.

              - `Type ComputerUse`

                The type of the object. Always `computer_use`.

                - `const ComputerUseComputerUse ComputerUse = "computer_use"`

            - `type AgentToolAutomations struct{…}`

              Lets the agent manage its own scheduled wakeups.

              - `Type Automations`

                The type of the object. Always `automations`.

                - `const AutomationsAutomations Automations = "automations"`

          - `Compaction AutomationAgentConfigCompaction`

            The effective context compaction settings.

            - `Async bool`

              Whether context is compacted in the background. Defaults to true.

          - `Experimental AutomationAgentConfigExperimental`

            The effective experimental settings for the agent.

            - `TimeAwareness bool`

              Whether the model receives periodic current-time reminders.

        - `AgentID string`

          The saved agent reference, or null when an inline agent is configured.

          `minLength: 0`

        - `Environment AutomationEnvironmentUnion`

          Configuration or references used to select the execution environment.

          - `type AutomationEnvironmentNone struct{…}`

            - `Type None`

              The type of the object. Always `none`.

              - `const NoneNone None = "none"`

          - `type AutomationEnvironmentOpenAIHosted struct{…}`

            Hosted environment selection with confidential setup commands and variables omitted.

            - `CapabilityDirectories []string`

              Directory overrides, or null to inherit the template or creation default.

              `minItems: 0`, `maxItems: 2000`

            - `ContainerSize string`

              The configured container size, or null to use the creation default.

              - `const AutomationEnvironmentOpenAIHostedContainerSizeSmall AutomationEnvironmentOpenAIHostedContainerSize = "small"`

              - `const AutomationEnvironmentOpenAIHostedContainerSizeMedium AutomationEnvironmentOpenAIHostedContainerSize = "medium"`

              - `const AutomationEnvironmentOpenAIHostedContainerSizeLarge AutomationEnvironmentOpenAIHostedContainerSize = "large"`

            - `Desktop AutomationEnvironmentOpenAIHostedDesktop`

              Desktop overrides, or null to inherit the template or creation default.

              - `Enabled bool`

                Whether the environment provisions a desktop and browser proxy.

            - `EnvironmentID string`

              An existing environment reference, or null when provisioning a new environment.

              `minLength: 0`

            - `EnvironmentTemplateID string`

              A template reference, or null when no template is selected.

              `minLength: 0`

            - `Files []AutomationEnvironmentOpenAIHostedFileUnion`

              File overrides, excluding contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `type AutomationEnvironmentOpenAIHostedFileFileID struct{…}`

                A project-scoped Files API reference resolved separately for each session.

                - `FileID string`

                  The ID of the uploaded file.

                  `minLength: 0`

                - `Path string`

                  The file's absolute path inside the environment.

                  `minLength: 0`

                - `Type FileID`

                  The type of the object. Always `file_id`.

                  - `const FileIDFileID FileID = "file_id"`

              - `type AutomationEnvironmentOpenAIHostedFileInline struct{…}`

                Metadata for confidential inline file contents.

                - `Path string`

                  The file's absolute path inside the environment.

                  `minLength: 0`

                - `SizeBytes int64`

                  The decoded size of the inline file in bytes.

                  `format: int64`, `minimum: 0`

                - `Type Inline`

                  The type of the object. Always `inline`.

                  - `const InlineInline Inline = "inline"`

            - `Network AutomationEnvironmentOpenAIHostedNetwork`

              Network overrides, or null to inherit the template or creation default.

              - `Access string`

                The environment's network access mode.

                - `const AutomationEnvironmentOpenAIHostedNetworkAccessEnabled AutomationEnvironmentOpenAIHostedNetworkAccess = "enabled"`

                  Allows unrestricted network access.

                - `const AutomationEnvironmentOpenAIHostedNetworkAccessDisabled AutomationEnvironmentOpenAIHostedNetworkAccess = "disabled"`

                  Disables network access.

                - `const AutomationEnvironmentOpenAIHostedNetworkAccessRestricted AutomationEnvironmentOpenAIHostedNetworkAccess = "restricted"`

                  Applies the configured domain restrictions.

              - `AllowedDomains []string`

                Domains the environment may access when network access is restricted.

                `minItems: 0`, `maxItems: 2000`

            - `Packages AutomationEnvironmentOpenAIHostedPackages`

              Package overrides, or null to inherit the template or creation default.

              - `Npm []string`

                npm packages installed globally in the environment.

                `minItems: 0`, `maxItems: 16384`

              - `Python []string`

                Python packages installed in the environment.

                `minItems: 0`, `maxItems: 16384`

              - `System []string`

                System packages installed in the environment.

                `minItems: 0`, `maxItems: 16384`

            - `Plugins []HostedPlugin`

              Plugin overrides, excluding archive contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `Description string`

                The installed plugin description.

                `minLength: 0`

              - `Name string`

                The installed plugin name.

                `minLength: 0`

              - `Type Inline`

                The type of the object. Always `inline`.

                - `const InlineInline Inline = "inline"`

            - `Skills []AutomationEnvironmentOpenAIHostedSkillUnion`

              Skill overrides, excluding archive contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `type AutomationEnvironmentOpenAIHostedSkillSkillReference struct{…}`

                A skill resolved afresh from the Skills API whenever a session starts.

                - `SkillID string`

                  The referenced skill ID.

                  `minLength: 0`

                - `Type SkillReference`

                  The type of the object. Always `skill_reference`.

                  - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

                - `Version string`

                  The requested version selector, including `latest`.

                  `minLength: 0`

              - `type AutomationEnvironmentOpenAIHostedSkillInline struct{…}`

                Safe metadata for an inline skill archive.

                - `Description string`

                  The skill description declared in `SKILL.md`.

                  `minLength: 0`

                - `Name string`

                  The skill name declared in `SKILL.md`.

                  `minLength: 0`

                - `Type Inline`

                  The type of the object. Always `inline`.

                  - `const InlineInline Inline = "inline"`

            - `Type OpenAIHosted`

              The type of the object. Always `openai_hosted`.

              - `const OpenAIHostedOpenAIHosted OpenAIHosted = "openai_hosted"`

          - `type AutomationEnvironmentSelfHosted struct{…}`

            - `CapabilityDirectories []string`

              Directories that expose capabilities to the agent.

              `minItems: 0`, `maxItems: 2000`

            - `EnvironmentID string`

              An existing registration, or null to create a session-owned environment.

              `minLength: 0`

            - `Type SelfHosted`

              The type of the object. Always `self_hosted`.

              - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

            - `WorkspaceDirectory string`

              The absolute project directory in the environment.

              `minLength: 0`

        - `Input []AutomationTargetNewSessionInput`

          Initial input delivered to each new session.

          `minItems: 0`, `maxItems: 2000`

          - `Content []InputContentUnion`

            The content of the message.

            `minItems: 0`, `maxItems: 2000`

            - `type InputContentInputText struct{…}`

              Text input recorded in a session item.

              - `Text string`

                The text supplied to the agent.

                `minLength: 0`

              - `Type InputText`

                The type of the object. Always `input_text`.

                - `const InputTextInputText InputText = "input_text"`

            - `type InputContentInputImage struct{…}`

              Image input recorded in a session item.

              - `ImageURL string`

                The URL of the image supplied to the agent, which may be a base64-encoded data URL.

                `minLength: 0`

              - `Type InputImage`

                The type of the object. Always `input_image`.

                - `const InputImageInputImage InputImage = "input_image"`

          - `Role User`

            The role of the message author. Always `user`.

            - `const UserUser User = "user"`

          - `Type Message`

            The type of the input item. Always `message`.

            - `const MessageMessage Message = "message"`

        - `Metadata map[string, string]`

          Metadata attached to each new session.

        - `Type NewSession`

          The type of the object. Always `new_session`.

          - `const NewSessionNewSession NewSession = "new_session"`

        - `VaultIDs []string`

          Vaults made available to each new session.

          `minItems: 0`, `maxItems: 2000`

      - `type AutomationTargetExistingSession struct{…}`

        - `Instructions string`

          Saved instructions delivered as an automation notification.

          `minLength: 0`

        - `SessionID string`

          The session receiving each invocation.

          `minLength: 0`

        - `Type ExistingSession`

          The type of the object. Always `existing_session`.

          - `const ExistingSessionExistingSession ExistingSession = "existing_session"`

    - `Timezone string`

      The timezone used to interpret the expression.

      `minLength: 0`

    - `Type Periodic`

      The type of the object. Always `periodic`.

      - `const PeriodicPeriodic Periodic = "periodic"`

  - `type OneTimeAutomation struct{…}`

    Fields shared by periodic and one-time automations.

    - `ID string`

      The automation ID.

      `minLength: 0`

    - `CreatedAt int64`

      The creation time as a Unix timestamp in seconds.

      `format: int64`

    - `CreatedBy AutomationCreatedByUnion`

      Service-recorded provenance; callers cannot supply this field.

    - `Metadata map[string, string]`

      Custom string key-value pairs attached to the automation.

    - `Name string`

      The automation's display name.

      `minLength: 0`

    - `Object AgentAutomation`

      Always `agent.automation`.

      - `const AgentAutomationAgentAutomation AgentAutomation = "agent.automation"`

    - `RunAt int64`

      The Unix timestamp, in seconds, of the scheduled occurrence.

      `format: int64`

    - `Status OneTimeAutomationStatus`

      Completion means the schedule has finished, not the agent's work.

      - `const OneTimeAutomationStatusActive OneTimeAutomationStatus = "active"`

      - `const OneTimeAutomationStatusPaused OneTimeAutomationStatus = "paused"`

      - `const OneTimeAutomationStatusCompleted OneTimeAutomationStatus = "completed"`

    - `Target AutomationTargetUnion`

      The session configuration or existing session receiving invocations.

    - `Type Once`

      The type of the object. Always `once`.

      - `const OnceOnce Once = "once"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  page, err := client.Beta.Agents.Automations.List(context.TODO(), openai.BetaAgentAutomationListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
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

`client.Beta.Agents.Automations.Pause(ctx, automationID) (*AutomationUnion, error)`

**post** `/agents/automations/{automation_id}/pause`

Pauses future scheduled delivery without stopping an active session.

### Parameters

- `automationID string`

  `minLength: 0`, `maxLength: 1048576`

### Returns

- `type AutomationUnion interface{…}`

  A saved automation and its schedule.

  - `type PeriodicAutomation struct{…}`

    Fields shared by periodic and one-time automations.

    - `ID string`

      The automation ID.

      `minLength: 0`

    - `CreatedAt int64`

      The creation time as a Unix timestamp in seconds.

      `format: int64`

    - `CreatedBy AutomationCreatedByUnion`

      Service-recorded provenance; callers cannot supply this field.

      - `type AutomationCreatedByDeveloper struct{…}`

        - `Type Developer`

          The type of the object. Always `developer`.

          - `const DeveloperDeveloper Developer = "developer"`

      - `type AutomationCreatedByAgent struct{…}`

        - `SessionID string`

          The creator session, which is also the automation's target.

          `minLength: 0`

        - `ToolCallID string`

          The tool call that created the automation.

          `minLength: 0`

        - `Type Agent`

          The type of the object. Always `agent`.

          - `const AgentAgent Agent = "agent"`

    - `Expression string`

      The cron expression determining scheduled occurrences.

      `minLength: 0`

    - `Metadata map[string, string]`

      Custom string key-value pairs attached to the automation.

    - `Name string`

      The automation's display name.

      `minLength: 0`

    - `Object AgentAutomation`

      Always `agent.automation`.

      - `const AgentAutomationAgentAutomation AgentAutomation = "agent.automation"`

    - `Status PeriodicAutomationStatus`

      Whether scheduled delivery is active or paused.

      - `const PeriodicAutomationStatusActive PeriodicAutomationStatus = "active"`

      - `const PeriodicAutomationStatusPaused PeriodicAutomationStatus = "paused"`

    - `Target AutomationTargetUnion`

      The session configuration or existing session receiving invocations.

      - `type AutomationTargetNewSession struct{…}`

        - `Agent AutomationAgentConfig`

          The inline agent configuration, or null when agent_id is configured.

          - `Instructions string`

            Custom instructions, or null when absent.

            `minLength: 0`

          - `Model string`

            The requested model name.

            `minLength: 0`

          - `MultiAgent MultiAgentConfig`

            The configuration for creating and coordinating subagents.

            - `Enabled bool`

              Whether subagent tools are enabled. Defaults to false.

            - `MaxConcurrentSubagents int64`

              Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

              `format: int64`, `minimum: 1`, `maximum: 4294967295`

          - `Reasoning AgentReasoning`

            The configured reasoning policy.

            - `Effort AgentReasoningEffort`

              The requested reasoning effort, or `null` when the model selects its own default.

              - `const AgentReasoningEffortNone AgentReasoningEffort = "none"`

              - `const AgentReasoningEffortMinimal AgentReasoningEffort = "minimal"`

              - `const AgentReasoningEffortLow AgentReasoningEffort = "low"`

              - `const AgentReasoningEffortMedium AgentReasoningEffort = "medium"`

              - `const AgentReasoningEffortHigh AgentReasoningEffort = "high"`

              - `const AgentReasoningEffortXhigh AgentReasoningEffort = "xhigh"`

              - `const AgentReasoningEffortMax AgentReasoningEffort = "max"`

            - `Summary AgentReasoningSummary`

              The requested reasoning summary format, or `null` when summaries are disabled.

              - `const AgentReasoningSummaryConcise AgentReasoningSummary = "concise"`

                Returns a concise reasoning summary when supported.

              - `const AgentReasoningSummaryDetailed AgentReasoningSummary = "detailed"`

                Returns a detailed reasoning summary when supported.

              - `const AgentReasoningSummaryAuto AgentReasoningSummary = "auto"`

                Automatically selects the most detailed summary supported by the model.

          - `ServiceTier AutomationAgentConfigServiceTier`

            The configured service-tier policy.

            - `const AutomationAgentConfigServiceTierAuto AutomationAgentConfigServiceTier = "auto"`

            - `const AutomationAgentConfigServiceTierDefault AutomationAgentConfigServiceTier = "default"`

            - `const AutomationAgentConfigServiceTierFlex AutomationAgentConfigServiceTier = "flex"`

            - `const AutomationAgentConfigServiceTierPriority AutomationAgentConfigServiceTier = "priority"`

            - `const AutomationAgentConfigServiceTierFast AutomationAgentConfigServiceTier = "fast"`

            - `const AutomationAgentConfigServiceTierUltrafast AutomationAgentConfigServiceTier = "ultrafast"`

          - `Text AgentText`

            The configured output format and verbosity.

            - `Format TextFormatUnion`

              The effective output format. Defaults to ordinary text.

              - `type TextFormatText struct{…}`

                Generates ordinary text without a structured-output constraint.

                - `Type Text`

                  The type of the object. Always `text`.

                  - `const TextText Text = "text"`

              - `type TextFormatJSONSchema struct{…}`

                Constrains generated text to a JSON Schema.

                - `Schema map[string, any]`

                  The JSON Schema that generated text must match.

                - `Type JSONSchema`

                  The type of the object. Always `json_schema`.

                  - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

            - `Verbosity AgentTextVerbosity`

              The amount of text produced by the agent. Defaults to `medium`.

              - `const AgentTextVerbosityLow AgentTextVerbosity = "low"`

              - `const AgentTextVerbosityMedium AgentTextVerbosity = "medium"`

              - `const AgentTextVerbosityHigh AgentTextVerbosity = "high"`

          - `Tools []AgentToolUnion`

            Configured tools, excluding confidential credentials.

            `minItems: 0`, `maxItems: 2000`

            - `type AgentToolFunction struct{…}`

              A function defined by the application.

              - `DeferLoading bool`

                Whether the function is deferred and discovered through tool search.

              - `Description string`

                A description of what the function does.

                `minLength: 0`

              - `Name string`

                The name of the function.

                `minLength: 0`

              - `Parameters map[string, any]`

                A JSON Schema object describing the function's arguments.

              - `Type Function`

                The type of the object. Always `function`.

                - `const FunctionFunction Function = "function"`

              - `Async bool`

                Whether the agent continues without waiting for the function result.

            - `type AgentToolProgrammaticToolCalling struct{…}`

              Enables calling tools from model-generated code.

              - `Enabled bool`

                Whether tools can be called from model-generated code.

              - `Type ProgrammaticToolCalling`

                The type of the object. Always `programmatic_tool_calling`.

                - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

            - `type AgentToolMcp struct{…}`

              Tools provided by a remote MCP server.

              - `AllowedTools []string`

                The MCP tools the agent may call.

                `minItems: 0`, `maxItems: 2000`

              - `ConnectionOrigin string`

                Where outbound MCP HTTP connections originate.

                - `const AgentToolMcpConnectionOriginService AgentToolMcpConnectionOrigin = "service"`

                - `const AgentToolMcpConnectionOriginEnvironment AgentToolMcpConnectionOrigin = "environment"`

              - `CredentialID string`

                The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

                `minLength: 0`

              - `RequestMetadata map[string, any]`

                Metadata included with requests to this MCP server.

              - `Required bool`

                Whether this MCP server must initialize before the first turn.

              - `ServerLabel string`

                A label used to identify the MCP server in tool calls.

                `minLength: 0`

              - `Transport McpTransportUnion`

                The transport used to connect to the MCP server.

                - `type McpTransportHTTP struct{…}`

                  Connects to an MCP server over HTTP.

                  - `ServerURL string`

                    The URL of the MCP server.

                    `minLength: 0`

                  - `Type HTTP`

                    The type of the object. Always `http`.

                    - `const HTTPHTTP HTTP = "http"`

                - `type McpTransportStdio struct{…}`

                  Starts an MCP server as a local process.

                  - `Args []string`

                    Arguments passed to the MCP server command.

                    `minItems: 0`, `maxItems: 2000`

                  - `Command string`

                    The command used to start the MCP server.

                    `minLength: 0`

                  - `Cwd string`

                    The working directory used to start the MCP server.

                    `minLength: 0`

                  - `EnvVars []string`

                    Environment variable names inherited from the execution environment.

                    `minItems: 0`, `maxItems: 2000`

                  - `Type Stdio`

                    The type of the object. Always `stdio`.

                    - `const StdioStdio Stdio = "stdio"`

              - `Type Mcp`

                The type of the object. Always `mcp`.

                - `const McpMcp Mcp = "mcp"`

            - `type AgentToolWebSearch struct{…}`

              Web search.

              - `AllowedDomains []string`

                Allowed search domains, or `null` when the search is unrestricted.

                `minItems: 0`, `maxItems: 2000`

              - `ContextSize string`

                The amount of search context made available to the model. Defaults to `medium`.

                - `const AgentToolWebSearchContextSizeLow AgentToolWebSearchContextSize = "low"`

                - `const AgentToolWebSearchContextSizeMedium AgentToolWebSearchContextSize = "medium"`

                - `const AgentToolWebSearchContextSizeHigh AgentToolWebSearchContextSize = "high"`

              - `Location AgentToolWebSearchLocation`

                Approximate location used to localize search results, if provided.

                - `City string`

                  The city name.

                  `minLength: 0`

                - `Country string`

                  The two-letter ISO country code, such as `US`.

                  `minLength: 0`

                - `Region string`

                  The region or state name.

                  `minLength: 0`

                - `Timezone string`

                  The IANA timezone, such as `America/Los_Angeles`.

                  `minLength: 0`

              - `Mode string`

                The source used for web search results.

                - `const AgentToolWebSearchModeDisabled AgentToolWebSearchMode = "disabled"`

                - `const AgentToolWebSearchModeCached AgentToolWebSearchMode = "cached"`

                - `const AgentToolWebSearchModeLive AgentToolWebSearchMode = "live"`

              - `Type WebSearch`

                The type of the object. Always `web_search`.

                - `const WebSearchWebSearch WebSearch = "web_search"`

            - `type AgentToolComputerUse struct{…}`

              Browser use in an OpenAI-hosted session.

              - `IncludeScreenshots bool`

                Whether computer tool outputs include screenshots.

              - `Type ComputerUse`

                The type of the object. Always `computer_use`.

                - `const ComputerUseComputerUse ComputerUse = "computer_use"`

            - `type AgentToolAutomations struct{…}`

              Lets the agent manage its own scheduled wakeups.

              - `Type Automations`

                The type of the object. Always `automations`.

                - `const AutomationsAutomations Automations = "automations"`

          - `Compaction AutomationAgentConfigCompaction`

            The effective context compaction settings.

            - `Async bool`

              Whether context is compacted in the background. Defaults to true.

          - `Experimental AutomationAgentConfigExperimental`

            The effective experimental settings for the agent.

            - `TimeAwareness bool`

              Whether the model receives periodic current-time reminders.

        - `AgentID string`

          The saved agent reference, or null when an inline agent is configured.

          `minLength: 0`

        - `Environment AutomationEnvironmentUnion`

          Configuration or references used to select the execution environment.

          - `type AutomationEnvironmentNone struct{…}`

            - `Type None`

              The type of the object. Always `none`.

              - `const NoneNone None = "none"`

          - `type AutomationEnvironmentOpenAIHosted struct{…}`

            Hosted environment selection with confidential setup commands and variables omitted.

            - `CapabilityDirectories []string`

              Directory overrides, or null to inherit the template or creation default.

              `minItems: 0`, `maxItems: 2000`

            - `ContainerSize string`

              The configured container size, or null to use the creation default.

              - `const AutomationEnvironmentOpenAIHostedContainerSizeSmall AutomationEnvironmentOpenAIHostedContainerSize = "small"`

              - `const AutomationEnvironmentOpenAIHostedContainerSizeMedium AutomationEnvironmentOpenAIHostedContainerSize = "medium"`

              - `const AutomationEnvironmentOpenAIHostedContainerSizeLarge AutomationEnvironmentOpenAIHostedContainerSize = "large"`

            - `Desktop AutomationEnvironmentOpenAIHostedDesktop`

              Desktop overrides, or null to inherit the template or creation default.

              - `Enabled bool`

                Whether the environment provisions a desktop and browser proxy.

            - `EnvironmentID string`

              An existing environment reference, or null when provisioning a new environment.

              `minLength: 0`

            - `EnvironmentTemplateID string`

              A template reference, or null when no template is selected.

              `minLength: 0`

            - `Files []AutomationEnvironmentOpenAIHostedFileUnion`

              File overrides, excluding contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `type AutomationEnvironmentOpenAIHostedFileFileID struct{…}`

                A project-scoped Files API reference resolved separately for each session.

                - `FileID string`

                  The ID of the uploaded file.

                  `minLength: 0`

                - `Path string`

                  The file's absolute path inside the environment.

                  `minLength: 0`

                - `Type FileID`

                  The type of the object. Always `file_id`.

                  - `const FileIDFileID FileID = "file_id"`

              - `type AutomationEnvironmentOpenAIHostedFileInline struct{…}`

                Metadata for confidential inline file contents.

                - `Path string`

                  The file's absolute path inside the environment.

                  `minLength: 0`

                - `SizeBytes int64`

                  The decoded size of the inline file in bytes.

                  `format: int64`, `minimum: 0`

                - `Type Inline`

                  The type of the object. Always `inline`.

                  - `const InlineInline Inline = "inline"`

            - `Network AutomationEnvironmentOpenAIHostedNetwork`

              Network overrides, or null to inherit the template or creation default.

              - `Access string`

                The environment's network access mode.

                - `const AutomationEnvironmentOpenAIHostedNetworkAccessEnabled AutomationEnvironmentOpenAIHostedNetworkAccess = "enabled"`

                  Allows unrestricted network access.

                - `const AutomationEnvironmentOpenAIHostedNetworkAccessDisabled AutomationEnvironmentOpenAIHostedNetworkAccess = "disabled"`

                  Disables network access.

                - `const AutomationEnvironmentOpenAIHostedNetworkAccessRestricted AutomationEnvironmentOpenAIHostedNetworkAccess = "restricted"`

                  Applies the configured domain restrictions.

              - `AllowedDomains []string`

                Domains the environment may access when network access is restricted.

                `minItems: 0`, `maxItems: 2000`

            - `Packages AutomationEnvironmentOpenAIHostedPackages`

              Package overrides, or null to inherit the template or creation default.

              - `Npm []string`

                npm packages installed globally in the environment.

                `minItems: 0`, `maxItems: 16384`

              - `Python []string`

                Python packages installed in the environment.

                `minItems: 0`, `maxItems: 16384`

              - `System []string`

                System packages installed in the environment.

                `minItems: 0`, `maxItems: 16384`

            - `Plugins []HostedPlugin`

              Plugin overrides, excluding archive contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `Description string`

                The installed plugin description.

                `minLength: 0`

              - `Name string`

                The installed plugin name.

                `minLength: 0`

              - `Type Inline`

                The type of the object. Always `inline`.

                - `const InlineInline Inline = "inline"`

            - `Skills []AutomationEnvironmentOpenAIHostedSkillUnion`

              Skill overrides, excluding archive contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `type AutomationEnvironmentOpenAIHostedSkillSkillReference struct{…}`

                A skill resolved afresh from the Skills API whenever a session starts.

                - `SkillID string`

                  The referenced skill ID.

                  `minLength: 0`

                - `Type SkillReference`

                  The type of the object. Always `skill_reference`.

                  - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

                - `Version string`

                  The requested version selector, including `latest`.

                  `minLength: 0`

              - `type AutomationEnvironmentOpenAIHostedSkillInline struct{…}`

                Safe metadata for an inline skill archive.

                - `Description string`

                  The skill description declared in `SKILL.md`.

                  `minLength: 0`

                - `Name string`

                  The skill name declared in `SKILL.md`.

                  `minLength: 0`

                - `Type Inline`

                  The type of the object. Always `inline`.

                  - `const InlineInline Inline = "inline"`

            - `Type OpenAIHosted`

              The type of the object. Always `openai_hosted`.

              - `const OpenAIHostedOpenAIHosted OpenAIHosted = "openai_hosted"`

          - `type AutomationEnvironmentSelfHosted struct{…}`

            - `CapabilityDirectories []string`

              Directories that expose capabilities to the agent.

              `minItems: 0`, `maxItems: 2000`

            - `EnvironmentID string`

              An existing registration, or null to create a session-owned environment.

              `minLength: 0`

            - `Type SelfHosted`

              The type of the object. Always `self_hosted`.

              - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

            - `WorkspaceDirectory string`

              The absolute project directory in the environment.

              `minLength: 0`

        - `Input []AutomationTargetNewSessionInput`

          Initial input delivered to each new session.

          `minItems: 0`, `maxItems: 2000`

          - `Content []InputContentUnion`

            The content of the message.

            `minItems: 0`, `maxItems: 2000`

            - `type InputContentInputText struct{…}`

              Text input recorded in a session item.

              - `Text string`

                The text supplied to the agent.

                `minLength: 0`

              - `Type InputText`

                The type of the object. Always `input_text`.

                - `const InputTextInputText InputText = "input_text"`

            - `type InputContentInputImage struct{…}`

              Image input recorded in a session item.

              - `ImageURL string`

                The URL of the image supplied to the agent, which may be a base64-encoded data URL.

                `minLength: 0`

              - `Type InputImage`

                The type of the object. Always `input_image`.

                - `const InputImageInputImage InputImage = "input_image"`

          - `Role User`

            The role of the message author. Always `user`.

            - `const UserUser User = "user"`

          - `Type Message`

            The type of the input item. Always `message`.

            - `const MessageMessage Message = "message"`

        - `Metadata map[string, string]`

          Metadata attached to each new session.

        - `Type NewSession`

          The type of the object. Always `new_session`.

          - `const NewSessionNewSession NewSession = "new_session"`

        - `VaultIDs []string`

          Vaults made available to each new session.

          `minItems: 0`, `maxItems: 2000`

      - `type AutomationTargetExistingSession struct{…}`

        - `Instructions string`

          Saved instructions delivered as an automation notification.

          `minLength: 0`

        - `SessionID string`

          The session receiving each invocation.

          `minLength: 0`

        - `Type ExistingSession`

          The type of the object. Always `existing_session`.

          - `const ExistingSessionExistingSession ExistingSession = "existing_session"`

    - `Timezone string`

      The timezone used to interpret the expression.

      `minLength: 0`

    - `Type Periodic`

      The type of the object. Always `periodic`.

      - `const PeriodicPeriodic Periodic = "periodic"`

  - `type OneTimeAutomation struct{…}`

    Fields shared by periodic and one-time automations.

    - `ID string`

      The automation ID.

      `minLength: 0`

    - `CreatedAt int64`

      The creation time as a Unix timestamp in seconds.

      `format: int64`

    - `CreatedBy AutomationCreatedByUnion`

      Service-recorded provenance; callers cannot supply this field.

    - `Metadata map[string, string]`

      Custom string key-value pairs attached to the automation.

    - `Name string`

      The automation's display name.

      `minLength: 0`

    - `Object AgentAutomation`

      Always `agent.automation`.

      - `const AgentAutomationAgentAutomation AgentAutomation = "agent.automation"`

    - `RunAt int64`

      The Unix timestamp, in seconds, of the scheduled occurrence.

      `format: int64`

    - `Status OneTimeAutomationStatus`

      Completion means the schedule has finished, not the agent's work.

      - `const OneTimeAutomationStatusActive OneTimeAutomationStatus = "active"`

      - `const OneTimeAutomationStatusPaused OneTimeAutomationStatus = "paused"`

      - `const OneTimeAutomationStatusCompleted OneTimeAutomationStatus = "completed"`

    - `Target AutomationTargetUnion`

      The session configuration or existing session receiving invocations.

    - `Type Once`

      The type of the object. Always `once`.

      - `const OnceOnce Once = "once"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  automation, err := client.Beta.Agents.Automations.Pause(context.TODO(), "automation_id")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", automation)
}
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

`client.Beta.Agents.Automations.Resume(ctx, automationID) (*AutomationUnion, error)`

**post** `/agents/automations/{automation_id}/resume`

Resumes scheduled delivery; one-time automations without a pending invocation require a future run_at.

### Parameters

- `automationID string`

  `minLength: 0`, `maxLength: 1048576`

### Returns

- `type AutomationUnion interface{…}`

  A saved automation and its schedule.

  - `type PeriodicAutomation struct{…}`

    Fields shared by periodic and one-time automations.

    - `ID string`

      The automation ID.

      `minLength: 0`

    - `CreatedAt int64`

      The creation time as a Unix timestamp in seconds.

      `format: int64`

    - `CreatedBy AutomationCreatedByUnion`

      Service-recorded provenance; callers cannot supply this field.

      - `type AutomationCreatedByDeveloper struct{…}`

        - `Type Developer`

          The type of the object. Always `developer`.

          - `const DeveloperDeveloper Developer = "developer"`

      - `type AutomationCreatedByAgent struct{…}`

        - `SessionID string`

          The creator session, which is also the automation's target.

          `minLength: 0`

        - `ToolCallID string`

          The tool call that created the automation.

          `minLength: 0`

        - `Type Agent`

          The type of the object. Always `agent`.

          - `const AgentAgent Agent = "agent"`

    - `Expression string`

      The cron expression determining scheduled occurrences.

      `minLength: 0`

    - `Metadata map[string, string]`

      Custom string key-value pairs attached to the automation.

    - `Name string`

      The automation's display name.

      `minLength: 0`

    - `Object AgentAutomation`

      Always `agent.automation`.

      - `const AgentAutomationAgentAutomation AgentAutomation = "agent.automation"`

    - `Status PeriodicAutomationStatus`

      Whether scheduled delivery is active or paused.

      - `const PeriodicAutomationStatusActive PeriodicAutomationStatus = "active"`

      - `const PeriodicAutomationStatusPaused PeriodicAutomationStatus = "paused"`

    - `Target AutomationTargetUnion`

      The session configuration or existing session receiving invocations.

      - `type AutomationTargetNewSession struct{…}`

        - `Agent AutomationAgentConfig`

          The inline agent configuration, or null when agent_id is configured.

          - `Instructions string`

            Custom instructions, or null when absent.

            `minLength: 0`

          - `Model string`

            The requested model name.

            `minLength: 0`

          - `MultiAgent MultiAgentConfig`

            The configuration for creating and coordinating subagents.

            - `Enabled bool`

              Whether subagent tools are enabled. Defaults to false.

            - `MaxConcurrentSubagents int64`

              Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

              `format: int64`, `minimum: 1`, `maximum: 4294967295`

          - `Reasoning AgentReasoning`

            The configured reasoning policy.

            - `Effort AgentReasoningEffort`

              The requested reasoning effort, or `null` when the model selects its own default.

              - `const AgentReasoningEffortNone AgentReasoningEffort = "none"`

              - `const AgentReasoningEffortMinimal AgentReasoningEffort = "minimal"`

              - `const AgentReasoningEffortLow AgentReasoningEffort = "low"`

              - `const AgentReasoningEffortMedium AgentReasoningEffort = "medium"`

              - `const AgentReasoningEffortHigh AgentReasoningEffort = "high"`

              - `const AgentReasoningEffortXhigh AgentReasoningEffort = "xhigh"`

              - `const AgentReasoningEffortMax AgentReasoningEffort = "max"`

            - `Summary AgentReasoningSummary`

              The requested reasoning summary format, or `null` when summaries are disabled.

              - `const AgentReasoningSummaryConcise AgentReasoningSummary = "concise"`

                Returns a concise reasoning summary when supported.

              - `const AgentReasoningSummaryDetailed AgentReasoningSummary = "detailed"`

                Returns a detailed reasoning summary when supported.

              - `const AgentReasoningSummaryAuto AgentReasoningSummary = "auto"`

                Automatically selects the most detailed summary supported by the model.

          - `ServiceTier AutomationAgentConfigServiceTier`

            The configured service-tier policy.

            - `const AutomationAgentConfigServiceTierAuto AutomationAgentConfigServiceTier = "auto"`

            - `const AutomationAgentConfigServiceTierDefault AutomationAgentConfigServiceTier = "default"`

            - `const AutomationAgentConfigServiceTierFlex AutomationAgentConfigServiceTier = "flex"`

            - `const AutomationAgentConfigServiceTierPriority AutomationAgentConfigServiceTier = "priority"`

            - `const AutomationAgentConfigServiceTierFast AutomationAgentConfigServiceTier = "fast"`

            - `const AutomationAgentConfigServiceTierUltrafast AutomationAgentConfigServiceTier = "ultrafast"`

          - `Text AgentText`

            The configured output format and verbosity.

            - `Format TextFormatUnion`

              The effective output format. Defaults to ordinary text.

              - `type TextFormatText struct{…}`

                Generates ordinary text without a structured-output constraint.

                - `Type Text`

                  The type of the object. Always `text`.

                  - `const TextText Text = "text"`

              - `type TextFormatJSONSchema struct{…}`

                Constrains generated text to a JSON Schema.

                - `Schema map[string, any]`

                  The JSON Schema that generated text must match.

                - `Type JSONSchema`

                  The type of the object. Always `json_schema`.

                  - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

            - `Verbosity AgentTextVerbosity`

              The amount of text produced by the agent. Defaults to `medium`.

              - `const AgentTextVerbosityLow AgentTextVerbosity = "low"`

              - `const AgentTextVerbosityMedium AgentTextVerbosity = "medium"`

              - `const AgentTextVerbosityHigh AgentTextVerbosity = "high"`

          - `Tools []AgentToolUnion`

            Configured tools, excluding confidential credentials.

            `minItems: 0`, `maxItems: 2000`

            - `type AgentToolFunction struct{…}`

              A function defined by the application.

              - `DeferLoading bool`

                Whether the function is deferred and discovered through tool search.

              - `Description string`

                A description of what the function does.

                `minLength: 0`

              - `Name string`

                The name of the function.

                `minLength: 0`

              - `Parameters map[string, any]`

                A JSON Schema object describing the function's arguments.

              - `Type Function`

                The type of the object. Always `function`.

                - `const FunctionFunction Function = "function"`

              - `Async bool`

                Whether the agent continues without waiting for the function result.

            - `type AgentToolProgrammaticToolCalling struct{…}`

              Enables calling tools from model-generated code.

              - `Enabled bool`

                Whether tools can be called from model-generated code.

              - `Type ProgrammaticToolCalling`

                The type of the object. Always `programmatic_tool_calling`.

                - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

            - `type AgentToolMcp struct{…}`

              Tools provided by a remote MCP server.

              - `AllowedTools []string`

                The MCP tools the agent may call.

                `minItems: 0`, `maxItems: 2000`

              - `ConnectionOrigin string`

                Where outbound MCP HTTP connections originate.

                - `const AgentToolMcpConnectionOriginService AgentToolMcpConnectionOrigin = "service"`

                - `const AgentToolMcpConnectionOriginEnvironment AgentToolMcpConnectionOrigin = "environment"`

              - `CredentialID string`

                The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

                `minLength: 0`

              - `RequestMetadata map[string, any]`

                Metadata included with requests to this MCP server.

              - `Required bool`

                Whether this MCP server must initialize before the first turn.

              - `ServerLabel string`

                A label used to identify the MCP server in tool calls.

                `minLength: 0`

              - `Transport McpTransportUnion`

                The transport used to connect to the MCP server.

                - `type McpTransportHTTP struct{…}`

                  Connects to an MCP server over HTTP.

                  - `ServerURL string`

                    The URL of the MCP server.

                    `minLength: 0`

                  - `Type HTTP`

                    The type of the object. Always `http`.

                    - `const HTTPHTTP HTTP = "http"`

                - `type McpTransportStdio struct{…}`

                  Starts an MCP server as a local process.

                  - `Args []string`

                    Arguments passed to the MCP server command.

                    `minItems: 0`, `maxItems: 2000`

                  - `Command string`

                    The command used to start the MCP server.

                    `minLength: 0`

                  - `Cwd string`

                    The working directory used to start the MCP server.

                    `minLength: 0`

                  - `EnvVars []string`

                    Environment variable names inherited from the execution environment.

                    `minItems: 0`, `maxItems: 2000`

                  - `Type Stdio`

                    The type of the object. Always `stdio`.

                    - `const StdioStdio Stdio = "stdio"`

              - `Type Mcp`

                The type of the object. Always `mcp`.

                - `const McpMcp Mcp = "mcp"`

            - `type AgentToolWebSearch struct{…}`

              Web search.

              - `AllowedDomains []string`

                Allowed search domains, or `null` when the search is unrestricted.

                `minItems: 0`, `maxItems: 2000`

              - `ContextSize string`

                The amount of search context made available to the model. Defaults to `medium`.

                - `const AgentToolWebSearchContextSizeLow AgentToolWebSearchContextSize = "low"`

                - `const AgentToolWebSearchContextSizeMedium AgentToolWebSearchContextSize = "medium"`

                - `const AgentToolWebSearchContextSizeHigh AgentToolWebSearchContextSize = "high"`

              - `Location AgentToolWebSearchLocation`

                Approximate location used to localize search results, if provided.

                - `City string`

                  The city name.

                  `minLength: 0`

                - `Country string`

                  The two-letter ISO country code, such as `US`.

                  `minLength: 0`

                - `Region string`

                  The region or state name.

                  `minLength: 0`

                - `Timezone string`

                  The IANA timezone, such as `America/Los_Angeles`.

                  `minLength: 0`

              - `Mode string`

                The source used for web search results.

                - `const AgentToolWebSearchModeDisabled AgentToolWebSearchMode = "disabled"`

                - `const AgentToolWebSearchModeCached AgentToolWebSearchMode = "cached"`

                - `const AgentToolWebSearchModeLive AgentToolWebSearchMode = "live"`

              - `Type WebSearch`

                The type of the object. Always `web_search`.

                - `const WebSearchWebSearch WebSearch = "web_search"`

            - `type AgentToolComputerUse struct{…}`

              Browser use in an OpenAI-hosted session.

              - `IncludeScreenshots bool`

                Whether computer tool outputs include screenshots.

              - `Type ComputerUse`

                The type of the object. Always `computer_use`.

                - `const ComputerUseComputerUse ComputerUse = "computer_use"`

            - `type AgentToolAutomations struct{…}`

              Lets the agent manage its own scheduled wakeups.

              - `Type Automations`

                The type of the object. Always `automations`.

                - `const AutomationsAutomations Automations = "automations"`

          - `Compaction AutomationAgentConfigCompaction`

            The effective context compaction settings.

            - `Async bool`

              Whether context is compacted in the background. Defaults to true.

          - `Experimental AutomationAgentConfigExperimental`

            The effective experimental settings for the agent.

            - `TimeAwareness bool`

              Whether the model receives periodic current-time reminders.

        - `AgentID string`

          The saved agent reference, or null when an inline agent is configured.

          `minLength: 0`

        - `Environment AutomationEnvironmentUnion`

          Configuration or references used to select the execution environment.

          - `type AutomationEnvironmentNone struct{…}`

            - `Type None`

              The type of the object. Always `none`.

              - `const NoneNone None = "none"`

          - `type AutomationEnvironmentOpenAIHosted struct{…}`

            Hosted environment selection with confidential setup commands and variables omitted.

            - `CapabilityDirectories []string`

              Directory overrides, or null to inherit the template or creation default.

              `minItems: 0`, `maxItems: 2000`

            - `ContainerSize string`

              The configured container size, or null to use the creation default.

              - `const AutomationEnvironmentOpenAIHostedContainerSizeSmall AutomationEnvironmentOpenAIHostedContainerSize = "small"`

              - `const AutomationEnvironmentOpenAIHostedContainerSizeMedium AutomationEnvironmentOpenAIHostedContainerSize = "medium"`

              - `const AutomationEnvironmentOpenAIHostedContainerSizeLarge AutomationEnvironmentOpenAIHostedContainerSize = "large"`

            - `Desktop AutomationEnvironmentOpenAIHostedDesktop`

              Desktop overrides, or null to inherit the template or creation default.

              - `Enabled bool`

                Whether the environment provisions a desktop and browser proxy.

            - `EnvironmentID string`

              An existing environment reference, or null when provisioning a new environment.

              `minLength: 0`

            - `EnvironmentTemplateID string`

              A template reference, or null when no template is selected.

              `minLength: 0`

            - `Files []AutomationEnvironmentOpenAIHostedFileUnion`

              File overrides, excluding contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `type AutomationEnvironmentOpenAIHostedFileFileID struct{…}`

                A project-scoped Files API reference resolved separately for each session.

                - `FileID string`

                  The ID of the uploaded file.

                  `minLength: 0`

                - `Path string`

                  The file's absolute path inside the environment.

                  `minLength: 0`

                - `Type FileID`

                  The type of the object. Always `file_id`.

                  - `const FileIDFileID FileID = "file_id"`

              - `type AutomationEnvironmentOpenAIHostedFileInline struct{…}`

                Metadata for confidential inline file contents.

                - `Path string`

                  The file's absolute path inside the environment.

                  `minLength: 0`

                - `SizeBytes int64`

                  The decoded size of the inline file in bytes.

                  `format: int64`, `minimum: 0`

                - `Type Inline`

                  The type of the object. Always `inline`.

                  - `const InlineInline Inline = "inline"`

            - `Network AutomationEnvironmentOpenAIHostedNetwork`

              Network overrides, or null to inherit the template or creation default.

              - `Access string`

                The environment's network access mode.

                - `const AutomationEnvironmentOpenAIHostedNetworkAccessEnabled AutomationEnvironmentOpenAIHostedNetworkAccess = "enabled"`

                  Allows unrestricted network access.

                - `const AutomationEnvironmentOpenAIHostedNetworkAccessDisabled AutomationEnvironmentOpenAIHostedNetworkAccess = "disabled"`

                  Disables network access.

                - `const AutomationEnvironmentOpenAIHostedNetworkAccessRestricted AutomationEnvironmentOpenAIHostedNetworkAccess = "restricted"`

                  Applies the configured domain restrictions.

              - `AllowedDomains []string`

                Domains the environment may access when network access is restricted.

                `minItems: 0`, `maxItems: 2000`

            - `Packages AutomationEnvironmentOpenAIHostedPackages`

              Package overrides, or null to inherit the template or creation default.

              - `Npm []string`

                npm packages installed globally in the environment.

                `minItems: 0`, `maxItems: 16384`

              - `Python []string`

                Python packages installed in the environment.

                `minItems: 0`, `maxItems: 16384`

              - `System []string`

                System packages installed in the environment.

                `minItems: 0`, `maxItems: 16384`

            - `Plugins []HostedPlugin`

              Plugin overrides, excluding archive contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `Description string`

                The installed plugin description.

                `minLength: 0`

              - `Name string`

                The installed plugin name.

                `minLength: 0`

              - `Type Inline`

                The type of the object. Always `inline`.

                - `const InlineInline Inline = "inline"`

            - `Skills []AutomationEnvironmentOpenAIHostedSkillUnion`

              Skill overrides, excluding archive contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `type AutomationEnvironmentOpenAIHostedSkillSkillReference struct{…}`

                A skill resolved afresh from the Skills API whenever a session starts.

                - `SkillID string`

                  The referenced skill ID.

                  `minLength: 0`

                - `Type SkillReference`

                  The type of the object. Always `skill_reference`.

                  - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

                - `Version string`

                  The requested version selector, including `latest`.

                  `minLength: 0`

              - `type AutomationEnvironmentOpenAIHostedSkillInline struct{…}`

                Safe metadata for an inline skill archive.

                - `Description string`

                  The skill description declared in `SKILL.md`.

                  `minLength: 0`

                - `Name string`

                  The skill name declared in `SKILL.md`.

                  `minLength: 0`

                - `Type Inline`

                  The type of the object. Always `inline`.

                  - `const InlineInline Inline = "inline"`

            - `Type OpenAIHosted`

              The type of the object. Always `openai_hosted`.

              - `const OpenAIHostedOpenAIHosted OpenAIHosted = "openai_hosted"`

          - `type AutomationEnvironmentSelfHosted struct{…}`

            - `CapabilityDirectories []string`

              Directories that expose capabilities to the agent.

              `minItems: 0`, `maxItems: 2000`

            - `EnvironmentID string`

              An existing registration, or null to create a session-owned environment.

              `minLength: 0`

            - `Type SelfHosted`

              The type of the object. Always `self_hosted`.

              - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

            - `WorkspaceDirectory string`

              The absolute project directory in the environment.

              `minLength: 0`

        - `Input []AutomationTargetNewSessionInput`

          Initial input delivered to each new session.

          `minItems: 0`, `maxItems: 2000`

          - `Content []InputContentUnion`

            The content of the message.

            `minItems: 0`, `maxItems: 2000`

            - `type InputContentInputText struct{…}`

              Text input recorded in a session item.

              - `Text string`

                The text supplied to the agent.

                `minLength: 0`

              - `Type InputText`

                The type of the object. Always `input_text`.

                - `const InputTextInputText InputText = "input_text"`

            - `type InputContentInputImage struct{…}`

              Image input recorded in a session item.

              - `ImageURL string`

                The URL of the image supplied to the agent, which may be a base64-encoded data URL.

                `minLength: 0`

              - `Type InputImage`

                The type of the object. Always `input_image`.

                - `const InputImageInputImage InputImage = "input_image"`

          - `Role User`

            The role of the message author. Always `user`.

            - `const UserUser User = "user"`

          - `Type Message`

            The type of the input item. Always `message`.

            - `const MessageMessage Message = "message"`

        - `Metadata map[string, string]`

          Metadata attached to each new session.

        - `Type NewSession`

          The type of the object. Always `new_session`.

          - `const NewSessionNewSession NewSession = "new_session"`

        - `VaultIDs []string`

          Vaults made available to each new session.

          `minItems: 0`, `maxItems: 2000`

      - `type AutomationTargetExistingSession struct{…}`

        - `Instructions string`

          Saved instructions delivered as an automation notification.

          `minLength: 0`

        - `SessionID string`

          The session receiving each invocation.

          `minLength: 0`

        - `Type ExistingSession`

          The type of the object. Always `existing_session`.

          - `const ExistingSessionExistingSession ExistingSession = "existing_session"`

    - `Timezone string`

      The timezone used to interpret the expression.

      `minLength: 0`

    - `Type Periodic`

      The type of the object. Always `periodic`.

      - `const PeriodicPeriodic Periodic = "periodic"`

  - `type OneTimeAutomation struct{…}`

    Fields shared by periodic and one-time automations.

    - `ID string`

      The automation ID.

      `minLength: 0`

    - `CreatedAt int64`

      The creation time as a Unix timestamp in seconds.

      `format: int64`

    - `CreatedBy AutomationCreatedByUnion`

      Service-recorded provenance; callers cannot supply this field.

    - `Metadata map[string, string]`

      Custom string key-value pairs attached to the automation.

    - `Name string`

      The automation's display name.

      `minLength: 0`

    - `Object AgentAutomation`

      Always `agent.automation`.

      - `const AgentAutomationAgentAutomation AgentAutomation = "agent.automation"`

    - `RunAt int64`

      The Unix timestamp, in seconds, of the scheduled occurrence.

      `format: int64`

    - `Status OneTimeAutomationStatus`

      Completion means the schedule has finished, not the agent's work.

      - `const OneTimeAutomationStatusActive OneTimeAutomationStatus = "active"`

      - `const OneTimeAutomationStatusPaused OneTimeAutomationStatus = "paused"`

      - `const OneTimeAutomationStatusCompleted OneTimeAutomationStatus = "completed"`

    - `Target AutomationTargetUnion`

      The session configuration or existing session receiving invocations.

    - `Type Once`

      The type of the object. Always `once`.

      - `const OnceOnce Once = "once"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  automation, err := client.Beta.Agents.Automations.Resume(context.TODO(), "automation_id")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", automation)
}
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

`client.Beta.Agents.Automations.Get(ctx, automationID) (*AutomationUnion, error)`

**get** `/agents/automations/{automation_id}`

Retrieves a project-owned automation.

### Parameters

- `automationID string`

  `minLength: 0`, `maxLength: 1048576`

### Returns

- `type AutomationUnion interface{…}`

  A saved automation and its schedule.

  - `type PeriodicAutomation struct{…}`

    Fields shared by periodic and one-time automations.

    - `ID string`

      The automation ID.

      `minLength: 0`

    - `CreatedAt int64`

      The creation time as a Unix timestamp in seconds.

      `format: int64`

    - `CreatedBy AutomationCreatedByUnion`

      Service-recorded provenance; callers cannot supply this field.

      - `type AutomationCreatedByDeveloper struct{…}`

        - `Type Developer`

          The type of the object. Always `developer`.

          - `const DeveloperDeveloper Developer = "developer"`

      - `type AutomationCreatedByAgent struct{…}`

        - `SessionID string`

          The creator session, which is also the automation's target.

          `minLength: 0`

        - `ToolCallID string`

          The tool call that created the automation.

          `minLength: 0`

        - `Type Agent`

          The type of the object. Always `agent`.

          - `const AgentAgent Agent = "agent"`

    - `Expression string`

      The cron expression determining scheduled occurrences.

      `minLength: 0`

    - `Metadata map[string, string]`

      Custom string key-value pairs attached to the automation.

    - `Name string`

      The automation's display name.

      `minLength: 0`

    - `Object AgentAutomation`

      Always `agent.automation`.

      - `const AgentAutomationAgentAutomation AgentAutomation = "agent.automation"`

    - `Status PeriodicAutomationStatus`

      Whether scheduled delivery is active or paused.

      - `const PeriodicAutomationStatusActive PeriodicAutomationStatus = "active"`

      - `const PeriodicAutomationStatusPaused PeriodicAutomationStatus = "paused"`

    - `Target AutomationTargetUnion`

      The session configuration or existing session receiving invocations.

      - `type AutomationTargetNewSession struct{…}`

        - `Agent AutomationAgentConfig`

          The inline agent configuration, or null when agent_id is configured.

          - `Instructions string`

            Custom instructions, or null when absent.

            `minLength: 0`

          - `Model string`

            The requested model name.

            `minLength: 0`

          - `MultiAgent MultiAgentConfig`

            The configuration for creating and coordinating subagents.

            - `Enabled bool`

              Whether subagent tools are enabled. Defaults to false.

            - `MaxConcurrentSubagents int64`

              Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

              `format: int64`, `minimum: 1`, `maximum: 4294967295`

          - `Reasoning AgentReasoning`

            The configured reasoning policy.

            - `Effort AgentReasoningEffort`

              The requested reasoning effort, or `null` when the model selects its own default.

              - `const AgentReasoningEffortNone AgentReasoningEffort = "none"`

              - `const AgentReasoningEffortMinimal AgentReasoningEffort = "minimal"`

              - `const AgentReasoningEffortLow AgentReasoningEffort = "low"`

              - `const AgentReasoningEffortMedium AgentReasoningEffort = "medium"`

              - `const AgentReasoningEffortHigh AgentReasoningEffort = "high"`

              - `const AgentReasoningEffortXhigh AgentReasoningEffort = "xhigh"`

              - `const AgentReasoningEffortMax AgentReasoningEffort = "max"`

            - `Summary AgentReasoningSummary`

              The requested reasoning summary format, or `null` when summaries are disabled.

              - `const AgentReasoningSummaryConcise AgentReasoningSummary = "concise"`

                Returns a concise reasoning summary when supported.

              - `const AgentReasoningSummaryDetailed AgentReasoningSummary = "detailed"`

                Returns a detailed reasoning summary when supported.

              - `const AgentReasoningSummaryAuto AgentReasoningSummary = "auto"`

                Automatically selects the most detailed summary supported by the model.

          - `ServiceTier AutomationAgentConfigServiceTier`

            The configured service-tier policy.

            - `const AutomationAgentConfigServiceTierAuto AutomationAgentConfigServiceTier = "auto"`

            - `const AutomationAgentConfigServiceTierDefault AutomationAgentConfigServiceTier = "default"`

            - `const AutomationAgentConfigServiceTierFlex AutomationAgentConfigServiceTier = "flex"`

            - `const AutomationAgentConfigServiceTierPriority AutomationAgentConfigServiceTier = "priority"`

            - `const AutomationAgentConfigServiceTierFast AutomationAgentConfigServiceTier = "fast"`

            - `const AutomationAgentConfigServiceTierUltrafast AutomationAgentConfigServiceTier = "ultrafast"`

          - `Text AgentText`

            The configured output format and verbosity.

            - `Format TextFormatUnion`

              The effective output format. Defaults to ordinary text.

              - `type TextFormatText struct{…}`

                Generates ordinary text without a structured-output constraint.

                - `Type Text`

                  The type of the object. Always `text`.

                  - `const TextText Text = "text"`

              - `type TextFormatJSONSchema struct{…}`

                Constrains generated text to a JSON Schema.

                - `Schema map[string, any]`

                  The JSON Schema that generated text must match.

                - `Type JSONSchema`

                  The type of the object. Always `json_schema`.

                  - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

            - `Verbosity AgentTextVerbosity`

              The amount of text produced by the agent. Defaults to `medium`.

              - `const AgentTextVerbosityLow AgentTextVerbosity = "low"`

              - `const AgentTextVerbosityMedium AgentTextVerbosity = "medium"`

              - `const AgentTextVerbosityHigh AgentTextVerbosity = "high"`

          - `Tools []AgentToolUnion`

            Configured tools, excluding confidential credentials.

            `minItems: 0`, `maxItems: 2000`

            - `type AgentToolFunction struct{…}`

              A function defined by the application.

              - `DeferLoading bool`

                Whether the function is deferred and discovered through tool search.

              - `Description string`

                A description of what the function does.

                `minLength: 0`

              - `Name string`

                The name of the function.

                `minLength: 0`

              - `Parameters map[string, any]`

                A JSON Schema object describing the function's arguments.

              - `Type Function`

                The type of the object. Always `function`.

                - `const FunctionFunction Function = "function"`

              - `Async bool`

                Whether the agent continues without waiting for the function result.

            - `type AgentToolProgrammaticToolCalling struct{…}`

              Enables calling tools from model-generated code.

              - `Enabled bool`

                Whether tools can be called from model-generated code.

              - `Type ProgrammaticToolCalling`

                The type of the object. Always `programmatic_tool_calling`.

                - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

            - `type AgentToolMcp struct{…}`

              Tools provided by a remote MCP server.

              - `AllowedTools []string`

                The MCP tools the agent may call.

                `minItems: 0`, `maxItems: 2000`

              - `ConnectionOrigin string`

                Where outbound MCP HTTP connections originate.

                - `const AgentToolMcpConnectionOriginService AgentToolMcpConnectionOrigin = "service"`

                - `const AgentToolMcpConnectionOriginEnvironment AgentToolMcpConnectionOrigin = "environment"`

              - `CredentialID string`

                The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

                `minLength: 0`

              - `RequestMetadata map[string, any]`

                Metadata included with requests to this MCP server.

              - `Required bool`

                Whether this MCP server must initialize before the first turn.

              - `ServerLabel string`

                A label used to identify the MCP server in tool calls.

                `minLength: 0`

              - `Transport McpTransportUnion`

                The transport used to connect to the MCP server.

                - `type McpTransportHTTP struct{…}`

                  Connects to an MCP server over HTTP.

                  - `ServerURL string`

                    The URL of the MCP server.

                    `minLength: 0`

                  - `Type HTTP`

                    The type of the object. Always `http`.

                    - `const HTTPHTTP HTTP = "http"`

                - `type McpTransportStdio struct{…}`

                  Starts an MCP server as a local process.

                  - `Args []string`

                    Arguments passed to the MCP server command.

                    `minItems: 0`, `maxItems: 2000`

                  - `Command string`

                    The command used to start the MCP server.

                    `minLength: 0`

                  - `Cwd string`

                    The working directory used to start the MCP server.

                    `minLength: 0`

                  - `EnvVars []string`

                    Environment variable names inherited from the execution environment.

                    `minItems: 0`, `maxItems: 2000`

                  - `Type Stdio`

                    The type of the object. Always `stdio`.

                    - `const StdioStdio Stdio = "stdio"`

              - `Type Mcp`

                The type of the object. Always `mcp`.

                - `const McpMcp Mcp = "mcp"`

            - `type AgentToolWebSearch struct{…}`

              Web search.

              - `AllowedDomains []string`

                Allowed search domains, or `null` when the search is unrestricted.

                `minItems: 0`, `maxItems: 2000`

              - `ContextSize string`

                The amount of search context made available to the model. Defaults to `medium`.

                - `const AgentToolWebSearchContextSizeLow AgentToolWebSearchContextSize = "low"`

                - `const AgentToolWebSearchContextSizeMedium AgentToolWebSearchContextSize = "medium"`

                - `const AgentToolWebSearchContextSizeHigh AgentToolWebSearchContextSize = "high"`

              - `Location AgentToolWebSearchLocation`

                Approximate location used to localize search results, if provided.

                - `City string`

                  The city name.

                  `minLength: 0`

                - `Country string`

                  The two-letter ISO country code, such as `US`.

                  `minLength: 0`

                - `Region string`

                  The region or state name.

                  `minLength: 0`

                - `Timezone string`

                  The IANA timezone, such as `America/Los_Angeles`.

                  `minLength: 0`

              - `Mode string`

                The source used for web search results.

                - `const AgentToolWebSearchModeDisabled AgentToolWebSearchMode = "disabled"`

                - `const AgentToolWebSearchModeCached AgentToolWebSearchMode = "cached"`

                - `const AgentToolWebSearchModeLive AgentToolWebSearchMode = "live"`

              - `Type WebSearch`

                The type of the object. Always `web_search`.

                - `const WebSearchWebSearch WebSearch = "web_search"`

            - `type AgentToolComputerUse struct{…}`

              Browser use in an OpenAI-hosted session.

              - `IncludeScreenshots bool`

                Whether computer tool outputs include screenshots.

              - `Type ComputerUse`

                The type of the object. Always `computer_use`.

                - `const ComputerUseComputerUse ComputerUse = "computer_use"`

            - `type AgentToolAutomations struct{…}`

              Lets the agent manage its own scheduled wakeups.

              - `Type Automations`

                The type of the object. Always `automations`.

                - `const AutomationsAutomations Automations = "automations"`

          - `Compaction AutomationAgentConfigCompaction`

            The effective context compaction settings.

            - `Async bool`

              Whether context is compacted in the background. Defaults to true.

          - `Experimental AutomationAgentConfigExperimental`

            The effective experimental settings for the agent.

            - `TimeAwareness bool`

              Whether the model receives periodic current-time reminders.

        - `AgentID string`

          The saved agent reference, or null when an inline agent is configured.

          `minLength: 0`

        - `Environment AutomationEnvironmentUnion`

          Configuration or references used to select the execution environment.

          - `type AutomationEnvironmentNone struct{…}`

            - `Type None`

              The type of the object. Always `none`.

              - `const NoneNone None = "none"`

          - `type AutomationEnvironmentOpenAIHosted struct{…}`

            Hosted environment selection with confidential setup commands and variables omitted.

            - `CapabilityDirectories []string`

              Directory overrides, or null to inherit the template or creation default.

              `minItems: 0`, `maxItems: 2000`

            - `ContainerSize string`

              The configured container size, or null to use the creation default.

              - `const AutomationEnvironmentOpenAIHostedContainerSizeSmall AutomationEnvironmentOpenAIHostedContainerSize = "small"`

              - `const AutomationEnvironmentOpenAIHostedContainerSizeMedium AutomationEnvironmentOpenAIHostedContainerSize = "medium"`

              - `const AutomationEnvironmentOpenAIHostedContainerSizeLarge AutomationEnvironmentOpenAIHostedContainerSize = "large"`

            - `Desktop AutomationEnvironmentOpenAIHostedDesktop`

              Desktop overrides, or null to inherit the template or creation default.

              - `Enabled bool`

                Whether the environment provisions a desktop and browser proxy.

            - `EnvironmentID string`

              An existing environment reference, or null when provisioning a new environment.

              `minLength: 0`

            - `EnvironmentTemplateID string`

              A template reference, or null when no template is selected.

              `minLength: 0`

            - `Files []AutomationEnvironmentOpenAIHostedFileUnion`

              File overrides, excluding contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `type AutomationEnvironmentOpenAIHostedFileFileID struct{…}`

                A project-scoped Files API reference resolved separately for each session.

                - `FileID string`

                  The ID of the uploaded file.

                  `minLength: 0`

                - `Path string`

                  The file's absolute path inside the environment.

                  `minLength: 0`

                - `Type FileID`

                  The type of the object. Always `file_id`.

                  - `const FileIDFileID FileID = "file_id"`

              - `type AutomationEnvironmentOpenAIHostedFileInline struct{…}`

                Metadata for confidential inline file contents.

                - `Path string`

                  The file's absolute path inside the environment.

                  `minLength: 0`

                - `SizeBytes int64`

                  The decoded size of the inline file in bytes.

                  `format: int64`, `minimum: 0`

                - `Type Inline`

                  The type of the object. Always `inline`.

                  - `const InlineInline Inline = "inline"`

            - `Network AutomationEnvironmentOpenAIHostedNetwork`

              Network overrides, or null to inherit the template or creation default.

              - `Access string`

                The environment's network access mode.

                - `const AutomationEnvironmentOpenAIHostedNetworkAccessEnabled AutomationEnvironmentOpenAIHostedNetworkAccess = "enabled"`

                  Allows unrestricted network access.

                - `const AutomationEnvironmentOpenAIHostedNetworkAccessDisabled AutomationEnvironmentOpenAIHostedNetworkAccess = "disabled"`

                  Disables network access.

                - `const AutomationEnvironmentOpenAIHostedNetworkAccessRestricted AutomationEnvironmentOpenAIHostedNetworkAccess = "restricted"`

                  Applies the configured domain restrictions.

              - `AllowedDomains []string`

                Domains the environment may access when network access is restricted.

                `minItems: 0`, `maxItems: 2000`

            - `Packages AutomationEnvironmentOpenAIHostedPackages`

              Package overrides, or null to inherit the template or creation default.

              - `Npm []string`

                npm packages installed globally in the environment.

                `minItems: 0`, `maxItems: 16384`

              - `Python []string`

                Python packages installed in the environment.

                `minItems: 0`, `maxItems: 16384`

              - `System []string`

                System packages installed in the environment.

                `minItems: 0`, `maxItems: 16384`

            - `Plugins []HostedPlugin`

              Plugin overrides, excluding archive contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `Description string`

                The installed plugin description.

                `minLength: 0`

              - `Name string`

                The installed plugin name.

                `minLength: 0`

              - `Type Inline`

                The type of the object. Always `inline`.

                - `const InlineInline Inline = "inline"`

            - `Skills []AutomationEnvironmentOpenAIHostedSkillUnion`

              Skill overrides, excluding archive contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `type AutomationEnvironmentOpenAIHostedSkillSkillReference struct{…}`

                A skill resolved afresh from the Skills API whenever a session starts.

                - `SkillID string`

                  The referenced skill ID.

                  `minLength: 0`

                - `Type SkillReference`

                  The type of the object. Always `skill_reference`.

                  - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

                - `Version string`

                  The requested version selector, including `latest`.

                  `minLength: 0`

              - `type AutomationEnvironmentOpenAIHostedSkillInline struct{…}`

                Safe metadata for an inline skill archive.

                - `Description string`

                  The skill description declared in `SKILL.md`.

                  `minLength: 0`

                - `Name string`

                  The skill name declared in `SKILL.md`.

                  `minLength: 0`

                - `Type Inline`

                  The type of the object. Always `inline`.

                  - `const InlineInline Inline = "inline"`

            - `Type OpenAIHosted`

              The type of the object. Always `openai_hosted`.

              - `const OpenAIHostedOpenAIHosted OpenAIHosted = "openai_hosted"`

          - `type AutomationEnvironmentSelfHosted struct{…}`

            - `CapabilityDirectories []string`

              Directories that expose capabilities to the agent.

              `minItems: 0`, `maxItems: 2000`

            - `EnvironmentID string`

              An existing registration, or null to create a session-owned environment.

              `minLength: 0`

            - `Type SelfHosted`

              The type of the object. Always `self_hosted`.

              - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

            - `WorkspaceDirectory string`

              The absolute project directory in the environment.

              `minLength: 0`

        - `Input []AutomationTargetNewSessionInput`

          Initial input delivered to each new session.

          `minItems: 0`, `maxItems: 2000`

          - `Content []InputContentUnion`

            The content of the message.

            `minItems: 0`, `maxItems: 2000`

            - `type InputContentInputText struct{…}`

              Text input recorded in a session item.

              - `Text string`

                The text supplied to the agent.

                `minLength: 0`

              - `Type InputText`

                The type of the object. Always `input_text`.

                - `const InputTextInputText InputText = "input_text"`

            - `type InputContentInputImage struct{…}`

              Image input recorded in a session item.

              - `ImageURL string`

                The URL of the image supplied to the agent, which may be a base64-encoded data URL.

                `minLength: 0`

              - `Type InputImage`

                The type of the object. Always `input_image`.

                - `const InputImageInputImage InputImage = "input_image"`

          - `Role User`

            The role of the message author. Always `user`.

            - `const UserUser User = "user"`

          - `Type Message`

            The type of the input item. Always `message`.

            - `const MessageMessage Message = "message"`

        - `Metadata map[string, string]`

          Metadata attached to each new session.

        - `Type NewSession`

          The type of the object. Always `new_session`.

          - `const NewSessionNewSession NewSession = "new_session"`

        - `VaultIDs []string`

          Vaults made available to each new session.

          `minItems: 0`, `maxItems: 2000`

      - `type AutomationTargetExistingSession struct{…}`

        - `Instructions string`

          Saved instructions delivered as an automation notification.

          `minLength: 0`

        - `SessionID string`

          The session receiving each invocation.

          `minLength: 0`

        - `Type ExistingSession`

          The type of the object. Always `existing_session`.

          - `const ExistingSessionExistingSession ExistingSession = "existing_session"`

    - `Timezone string`

      The timezone used to interpret the expression.

      `minLength: 0`

    - `Type Periodic`

      The type of the object. Always `periodic`.

      - `const PeriodicPeriodic Periodic = "periodic"`

  - `type OneTimeAutomation struct{…}`

    Fields shared by periodic and one-time automations.

    - `ID string`

      The automation ID.

      `minLength: 0`

    - `CreatedAt int64`

      The creation time as a Unix timestamp in seconds.

      `format: int64`

    - `CreatedBy AutomationCreatedByUnion`

      Service-recorded provenance; callers cannot supply this field.

    - `Metadata map[string, string]`

      Custom string key-value pairs attached to the automation.

    - `Name string`

      The automation's display name.

      `minLength: 0`

    - `Object AgentAutomation`

      Always `agent.automation`.

      - `const AgentAutomationAgentAutomation AgentAutomation = "agent.automation"`

    - `RunAt int64`

      The Unix timestamp, in seconds, of the scheduled occurrence.

      `format: int64`

    - `Status OneTimeAutomationStatus`

      Completion means the schedule has finished, not the agent's work.

      - `const OneTimeAutomationStatusActive OneTimeAutomationStatus = "active"`

      - `const OneTimeAutomationStatusPaused OneTimeAutomationStatus = "paused"`

      - `const OneTimeAutomationStatusCompleted OneTimeAutomationStatus = "completed"`

    - `Target AutomationTargetUnion`

      The session configuration or existing session receiving invocations.

    - `Type Once`

      The type of the object. Always `once`.

      - `const OnceOnce Once = "once"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  automation, err := client.Beta.Agents.Automations.Get(context.TODO(), "automation_id")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", automation)
}
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

`client.Beta.Agents.Automations.Update(ctx, automationID, body) (*AutomationUnion, error)`

**post** `/agents/automations/{automation_id}`

Updates supplied fields; target and metadata replace the whole field.

### Parameters

- `automationID string`

  `minLength: 0`, `maxLength: 1048576`

- `body BetaAgentAutomationUpdateParams`

  - `Expression param.Field[string]`

    Only accepted for periodic automations.

    `minLength: 1`, `maxLength: 256`

  - `Metadata param.Field[map[string, string]]`

    Replaces all metadata; omit to leave unchanged.

  - `Name param.Field[string]`

    `minLength: 1`, `maxLength: 256`

  - `RunAt param.Field[int64]`

    A future Unix timestamp in seconds; accepted only before a one-time scheduled invocation exists.

    `format: int64`

  - `Target param.Field[AutomationTargetParamUnionResp]`

    Replaces the complete target, retaining its type and any creator session.

  - `Timezone param.Field[string]`

    Only accepted for periodic automations.

    `minLength: 1`, `maxLength: 128`

### Returns

- `type AutomationUnion interface{…}`

  A saved automation and its schedule.

  - `type PeriodicAutomation struct{…}`

    Fields shared by periodic and one-time automations.

    - `ID string`

      The automation ID.

      `minLength: 0`

    - `CreatedAt int64`

      The creation time as a Unix timestamp in seconds.

      `format: int64`

    - `CreatedBy AutomationCreatedByUnion`

      Service-recorded provenance; callers cannot supply this field.

      - `type AutomationCreatedByDeveloper struct{…}`

        - `Type Developer`

          The type of the object. Always `developer`.

          - `const DeveloperDeveloper Developer = "developer"`

      - `type AutomationCreatedByAgent struct{…}`

        - `SessionID string`

          The creator session, which is also the automation's target.

          `minLength: 0`

        - `ToolCallID string`

          The tool call that created the automation.

          `minLength: 0`

        - `Type Agent`

          The type of the object. Always `agent`.

          - `const AgentAgent Agent = "agent"`

    - `Expression string`

      The cron expression determining scheduled occurrences.

      `minLength: 0`

    - `Metadata map[string, string]`

      Custom string key-value pairs attached to the automation.

    - `Name string`

      The automation's display name.

      `minLength: 0`

    - `Object AgentAutomation`

      Always `agent.automation`.

      - `const AgentAutomationAgentAutomation AgentAutomation = "agent.automation"`

    - `Status PeriodicAutomationStatus`

      Whether scheduled delivery is active or paused.

      - `const PeriodicAutomationStatusActive PeriodicAutomationStatus = "active"`

      - `const PeriodicAutomationStatusPaused PeriodicAutomationStatus = "paused"`

    - `Target AutomationTargetUnion`

      The session configuration or existing session receiving invocations.

      - `type AutomationTargetNewSession struct{…}`

        - `Agent AutomationAgentConfig`

          The inline agent configuration, or null when agent_id is configured.

          - `Instructions string`

            Custom instructions, or null when absent.

            `minLength: 0`

          - `Model string`

            The requested model name.

            `minLength: 0`

          - `MultiAgent MultiAgentConfig`

            The configuration for creating and coordinating subagents.

            - `Enabled bool`

              Whether subagent tools are enabled. Defaults to false.

            - `MaxConcurrentSubagents int64`

              Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

              `format: int64`, `minimum: 1`, `maximum: 4294967295`

          - `Reasoning AgentReasoning`

            The configured reasoning policy.

            - `Effort AgentReasoningEffort`

              The requested reasoning effort, or `null` when the model selects its own default.

              - `const AgentReasoningEffortNone AgentReasoningEffort = "none"`

              - `const AgentReasoningEffortMinimal AgentReasoningEffort = "minimal"`

              - `const AgentReasoningEffortLow AgentReasoningEffort = "low"`

              - `const AgentReasoningEffortMedium AgentReasoningEffort = "medium"`

              - `const AgentReasoningEffortHigh AgentReasoningEffort = "high"`

              - `const AgentReasoningEffortXhigh AgentReasoningEffort = "xhigh"`

              - `const AgentReasoningEffortMax AgentReasoningEffort = "max"`

            - `Summary AgentReasoningSummary`

              The requested reasoning summary format, or `null` when summaries are disabled.

              - `const AgentReasoningSummaryConcise AgentReasoningSummary = "concise"`

                Returns a concise reasoning summary when supported.

              - `const AgentReasoningSummaryDetailed AgentReasoningSummary = "detailed"`

                Returns a detailed reasoning summary when supported.

              - `const AgentReasoningSummaryAuto AgentReasoningSummary = "auto"`

                Automatically selects the most detailed summary supported by the model.

          - `ServiceTier AutomationAgentConfigServiceTier`

            The configured service-tier policy.

            - `const AutomationAgentConfigServiceTierAuto AutomationAgentConfigServiceTier = "auto"`

            - `const AutomationAgentConfigServiceTierDefault AutomationAgentConfigServiceTier = "default"`

            - `const AutomationAgentConfigServiceTierFlex AutomationAgentConfigServiceTier = "flex"`

            - `const AutomationAgentConfigServiceTierPriority AutomationAgentConfigServiceTier = "priority"`

            - `const AutomationAgentConfigServiceTierFast AutomationAgentConfigServiceTier = "fast"`

            - `const AutomationAgentConfigServiceTierUltrafast AutomationAgentConfigServiceTier = "ultrafast"`

          - `Text AgentText`

            The configured output format and verbosity.

            - `Format TextFormatUnion`

              The effective output format. Defaults to ordinary text.

              - `type TextFormatText struct{…}`

                Generates ordinary text without a structured-output constraint.

                - `Type Text`

                  The type of the object. Always `text`.

                  - `const TextText Text = "text"`

              - `type TextFormatJSONSchema struct{…}`

                Constrains generated text to a JSON Schema.

                - `Schema map[string, any]`

                  The JSON Schema that generated text must match.

                - `Type JSONSchema`

                  The type of the object. Always `json_schema`.

                  - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

            - `Verbosity AgentTextVerbosity`

              The amount of text produced by the agent. Defaults to `medium`.

              - `const AgentTextVerbosityLow AgentTextVerbosity = "low"`

              - `const AgentTextVerbosityMedium AgentTextVerbosity = "medium"`

              - `const AgentTextVerbosityHigh AgentTextVerbosity = "high"`

          - `Tools []AgentToolUnion`

            Configured tools, excluding confidential credentials.

            `minItems: 0`, `maxItems: 2000`

            - `type AgentToolFunction struct{…}`

              A function defined by the application.

              - `DeferLoading bool`

                Whether the function is deferred and discovered through tool search.

              - `Description string`

                A description of what the function does.

                `minLength: 0`

              - `Name string`

                The name of the function.

                `minLength: 0`

              - `Parameters map[string, any]`

                A JSON Schema object describing the function's arguments.

              - `Type Function`

                The type of the object. Always `function`.

                - `const FunctionFunction Function = "function"`

              - `Async bool`

                Whether the agent continues without waiting for the function result.

            - `type AgentToolProgrammaticToolCalling struct{…}`

              Enables calling tools from model-generated code.

              - `Enabled bool`

                Whether tools can be called from model-generated code.

              - `Type ProgrammaticToolCalling`

                The type of the object. Always `programmatic_tool_calling`.

                - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

            - `type AgentToolMcp struct{…}`

              Tools provided by a remote MCP server.

              - `AllowedTools []string`

                The MCP tools the agent may call.

                `minItems: 0`, `maxItems: 2000`

              - `ConnectionOrigin string`

                Where outbound MCP HTTP connections originate.

                - `const AgentToolMcpConnectionOriginService AgentToolMcpConnectionOrigin = "service"`

                - `const AgentToolMcpConnectionOriginEnvironment AgentToolMcpConnectionOrigin = "environment"`

              - `CredentialID string`

                The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

                `minLength: 0`

              - `RequestMetadata map[string, any]`

                Metadata included with requests to this MCP server.

              - `Required bool`

                Whether this MCP server must initialize before the first turn.

              - `ServerLabel string`

                A label used to identify the MCP server in tool calls.

                `minLength: 0`

              - `Transport McpTransportUnion`

                The transport used to connect to the MCP server.

                - `type McpTransportHTTP struct{…}`

                  Connects to an MCP server over HTTP.

                  - `ServerURL string`

                    The URL of the MCP server.

                    `minLength: 0`

                  - `Type HTTP`

                    The type of the object. Always `http`.

                    - `const HTTPHTTP HTTP = "http"`

                - `type McpTransportStdio struct{…}`

                  Starts an MCP server as a local process.

                  - `Args []string`

                    Arguments passed to the MCP server command.

                    `minItems: 0`, `maxItems: 2000`

                  - `Command string`

                    The command used to start the MCP server.

                    `minLength: 0`

                  - `Cwd string`

                    The working directory used to start the MCP server.

                    `minLength: 0`

                  - `EnvVars []string`

                    Environment variable names inherited from the execution environment.

                    `minItems: 0`, `maxItems: 2000`

                  - `Type Stdio`

                    The type of the object. Always `stdio`.

                    - `const StdioStdio Stdio = "stdio"`

              - `Type Mcp`

                The type of the object. Always `mcp`.

                - `const McpMcp Mcp = "mcp"`

            - `type AgentToolWebSearch struct{…}`

              Web search.

              - `AllowedDomains []string`

                Allowed search domains, or `null` when the search is unrestricted.

                `minItems: 0`, `maxItems: 2000`

              - `ContextSize string`

                The amount of search context made available to the model. Defaults to `medium`.

                - `const AgentToolWebSearchContextSizeLow AgentToolWebSearchContextSize = "low"`

                - `const AgentToolWebSearchContextSizeMedium AgentToolWebSearchContextSize = "medium"`

                - `const AgentToolWebSearchContextSizeHigh AgentToolWebSearchContextSize = "high"`

              - `Location AgentToolWebSearchLocation`

                Approximate location used to localize search results, if provided.

                - `City string`

                  The city name.

                  `minLength: 0`

                - `Country string`

                  The two-letter ISO country code, such as `US`.

                  `minLength: 0`

                - `Region string`

                  The region or state name.

                  `minLength: 0`

                - `Timezone string`

                  The IANA timezone, such as `America/Los_Angeles`.

                  `minLength: 0`

              - `Mode string`

                The source used for web search results.

                - `const AgentToolWebSearchModeDisabled AgentToolWebSearchMode = "disabled"`

                - `const AgentToolWebSearchModeCached AgentToolWebSearchMode = "cached"`

                - `const AgentToolWebSearchModeLive AgentToolWebSearchMode = "live"`

              - `Type WebSearch`

                The type of the object. Always `web_search`.

                - `const WebSearchWebSearch WebSearch = "web_search"`

            - `type AgentToolComputerUse struct{…}`

              Browser use in an OpenAI-hosted session.

              - `IncludeScreenshots bool`

                Whether computer tool outputs include screenshots.

              - `Type ComputerUse`

                The type of the object. Always `computer_use`.

                - `const ComputerUseComputerUse ComputerUse = "computer_use"`

            - `type AgentToolAutomations struct{…}`

              Lets the agent manage its own scheduled wakeups.

              - `Type Automations`

                The type of the object. Always `automations`.

                - `const AutomationsAutomations Automations = "automations"`

          - `Compaction AutomationAgentConfigCompaction`

            The effective context compaction settings.

            - `Async bool`

              Whether context is compacted in the background. Defaults to true.

          - `Experimental AutomationAgentConfigExperimental`

            The effective experimental settings for the agent.

            - `TimeAwareness bool`

              Whether the model receives periodic current-time reminders.

        - `AgentID string`

          The saved agent reference, or null when an inline agent is configured.

          `minLength: 0`

        - `Environment AutomationEnvironmentUnion`

          Configuration or references used to select the execution environment.

          - `type AutomationEnvironmentNone struct{…}`

            - `Type None`

              The type of the object. Always `none`.

              - `const NoneNone None = "none"`

          - `type AutomationEnvironmentOpenAIHosted struct{…}`

            Hosted environment selection with confidential setup commands and variables omitted.

            - `CapabilityDirectories []string`

              Directory overrides, or null to inherit the template or creation default.

              `minItems: 0`, `maxItems: 2000`

            - `ContainerSize string`

              The configured container size, or null to use the creation default.

              - `const AutomationEnvironmentOpenAIHostedContainerSizeSmall AutomationEnvironmentOpenAIHostedContainerSize = "small"`

              - `const AutomationEnvironmentOpenAIHostedContainerSizeMedium AutomationEnvironmentOpenAIHostedContainerSize = "medium"`

              - `const AutomationEnvironmentOpenAIHostedContainerSizeLarge AutomationEnvironmentOpenAIHostedContainerSize = "large"`

            - `Desktop AutomationEnvironmentOpenAIHostedDesktop`

              Desktop overrides, or null to inherit the template or creation default.

              - `Enabled bool`

                Whether the environment provisions a desktop and browser proxy.

            - `EnvironmentID string`

              An existing environment reference, or null when provisioning a new environment.

              `minLength: 0`

            - `EnvironmentTemplateID string`

              A template reference, or null when no template is selected.

              `minLength: 0`

            - `Files []AutomationEnvironmentOpenAIHostedFileUnion`

              File overrides, excluding contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `type AutomationEnvironmentOpenAIHostedFileFileID struct{…}`

                A project-scoped Files API reference resolved separately for each session.

                - `FileID string`

                  The ID of the uploaded file.

                  `minLength: 0`

                - `Path string`

                  The file's absolute path inside the environment.

                  `minLength: 0`

                - `Type FileID`

                  The type of the object. Always `file_id`.

                  - `const FileIDFileID FileID = "file_id"`

              - `type AutomationEnvironmentOpenAIHostedFileInline struct{…}`

                Metadata for confidential inline file contents.

                - `Path string`

                  The file's absolute path inside the environment.

                  `minLength: 0`

                - `SizeBytes int64`

                  The decoded size of the inline file in bytes.

                  `format: int64`, `minimum: 0`

                - `Type Inline`

                  The type of the object. Always `inline`.

                  - `const InlineInline Inline = "inline"`

            - `Network AutomationEnvironmentOpenAIHostedNetwork`

              Network overrides, or null to inherit the template or creation default.

              - `Access string`

                The environment's network access mode.

                - `const AutomationEnvironmentOpenAIHostedNetworkAccessEnabled AutomationEnvironmentOpenAIHostedNetworkAccess = "enabled"`

                  Allows unrestricted network access.

                - `const AutomationEnvironmentOpenAIHostedNetworkAccessDisabled AutomationEnvironmentOpenAIHostedNetworkAccess = "disabled"`

                  Disables network access.

                - `const AutomationEnvironmentOpenAIHostedNetworkAccessRestricted AutomationEnvironmentOpenAIHostedNetworkAccess = "restricted"`

                  Applies the configured domain restrictions.

              - `AllowedDomains []string`

                Domains the environment may access when network access is restricted.

                `minItems: 0`, `maxItems: 2000`

            - `Packages AutomationEnvironmentOpenAIHostedPackages`

              Package overrides, or null to inherit the template or creation default.

              - `Npm []string`

                npm packages installed globally in the environment.

                `minItems: 0`, `maxItems: 16384`

              - `Python []string`

                Python packages installed in the environment.

                `minItems: 0`, `maxItems: 16384`

              - `System []string`

                System packages installed in the environment.

                `minItems: 0`, `maxItems: 16384`

            - `Plugins []HostedPlugin`

              Plugin overrides, excluding archive contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `Description string`

                The installed plugin description.

                `minLength: 0`

              - `Name string`

                The installed plugin name.

                `minLength: 0`

              - `Type Inline`

                The type of the object. Always `inline`.

                - `const InlineInline Inline = "inline"`

            - `Skills []AutomationEnvironmentOpenAIHostedSkillUnion`

              Skill overrides, excluding archive contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `type AutomationEnvironmentOpenAIHostedSkillSkillReference struct{…}`

                A skill resolved afresh from the Skills API whenever a session starts.

                - `SkillID string`

                  The referenced skill ID.

                  `minLength: 0`

                - `Type SkillReference`

                  The type of the object. Always `skill_reference`.

                  - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

                - `Version string`

                  The requested version selector, including `latest`.

                  `minLength: 0`

              - `type AutomationEnvironmentOpenAIHostedSkillInline struct{…}`

                Safe metadata for an inline skill archive.

                - `Description string`

                  The skill description declared in `SKILL.md`.

                  `minLength: 0`

                - `Name string`

                  The skill name declared in `SKILL.md`.

                  `minLength: 0`

                - `Type Inline`

                  The type of the object. Always `inline`.

                  - `const InlineInline Inline = "inline"`

            - `Type OpenAIHosted`

              The type of the object. Always `openai_hosted`.

              - `const OpenAIHostedOpenAIHosted OpenAIHosted = "openai_hosted"`

          - `type AutomationEnvironmentSelfHosted struct{…}`

            - `CapabilityDirectories []string`

              Directories that expose capabilities to the agent.

              `minItems: 0`, `maxItems: 2000`

            - `EnvironmentID string`

              An existing registration, or null to create a session-owned environment.

              `minLength: 0`

            - `Type SelfHosted`

              The type of the object. Always `self_hosted`.

              - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

            - `WorkspaceDirectory string`

              The absolute project directory in the environment.

              `minLength: 0`

        - `Input []AutomationTargetNewSessionInput`

          Initial input delivered to each new session.

          `minItems: 0`, `maxItems: 2000`

          - `Content []InputContentUnion`

            The content of the message.

            `minItems: 0`, `maxItems: 2000`

            - `type InputContentInputText struct{…}`

              Text input recorded in a session item.

              - `Text string`

                The text supplied to the agent.

                `minLength: 0`

              - `Type InputText`

                The type of the object. Always `input_text`.

                - `const InputTextInputText InputText = "input_text"`

            - `type InputContentInputImage struct{…}`

              Image input recorded in a session item.

              - `ImageURL string`

                The URL of the image supplied to the agent, which may be a base64-encoded data URL.

                `minLength: 0`

              - `Type InputImage`

                The type of the object. Always `input_image`.

                - `const InputImageInputImage InputImage = "input_image"`

          - `Role User`

            The role of the message author. Always `user`.

            - `const UserUser User = "user"`

          - `Type Message`

            The type of the input item. Always `message`.

            - `const MessageMessage Message = "message"`

        - `Metadata map[string, string]`

          Metadata attached to each new session.

        - `Type NewSession`

          The type of the object. Always `new_session`.

          - `const NewSessionNewSession NewSession = "new_session"`

        - `VaultIDs []string`

          Vaults made available to each new session.

          `minItems: 0`, `maxItems: 2000`

      - `type AutomationTargetExistingSession struct{…}`

        - `Instructions string`

          Saved instructions delivered as an automation notification.

          `minLength: 0`

        - `SessionID string`

          The session receiving each invocation.

          `minLength: 0`

        - `Type ExistingSession`

          The type of the object. Always `existing_session`.

          - `const ExistingSessionExistingSession ExistingSession = "existing_session"`

    - `Timezone string`

      The timezone used to interpret the expression.

      `minLength: 0`

    - `Type Periodic`

      The type of the object. Always `periodic`.

      - `const PeriodicPeriodic Periodic = "periodic"`

  - `type OneTimeAutomation struct{…}`

    Fields shared by periodic and one-time automations.

    - `ID string`

      The automation ID.

      `minLength: 0`

    - `CreatedAt int64`

      The creation time as a Unix timestamp in seconds.

      `format: int64`

    - `CreatedBy AutomationCreatedByUnion`

      Service-recorded provenance; callers cannot supply this field.

    - `Metadata map[string, string]`

      Custom string key-value pairs attached to the automation.

    - `Name string`

      The automation's display name.

      `minLength: 0`

    - `Object AgentAutomation`

      Always `agent.automation`.

      - `const AgentAutomationAgentAutomation AgentAutomation = "agent.automation"`

    - `RunAt int64`

      The Unix timestamp, in seconds, of the scheduled occurrence.

      `format: int64`

    - `Status OneTimeAutomationStatus`

      Completion means the schedule has finished, not the agent's work.

      - `const OneTimeAutomationStatusActive OneTimeAutomationStatus = "active"`

      - `const OneTimeAutomationStatusPaused OneTimeAutomationStatus = "paused"`

      - `const OneTimeAutomationStatusCompleted OneTimeAutomationStatus = "completed"`

    - `Target AutomationTargetUnion`

      The session configuration or existing session receiving invocations.

    - `Type Once`

      The type of the object. Always `once`.

      - `const OnceOnce Once = "once"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  automation, err := client.Beta.Agents.Automations.Update(
    context.TODO(),
    "automation_id",
    openai.BetaAgentAutomationUpdateParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", automation)
}
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

- `type AutomationUnion interface{…}`

  A saved automation and its schedule.

  - `type PeriodicAutomation struct{…}`

    Fields shared by periodic and one-time automations.

    - `ID string`

      The automation ID.

      `minLength: 0`

    - `CreatedAt int64`

      The creation time as a Unix timestamp in seconds.

      `format: int64`

    - `CreatedBy AutomationCreatedByUnion`

      Service-recorded provenance; callers cannot supply this field.

      - `type AutomationCreatedByDeveloper struct{…}`

        - `Type Developer`

          The type of the object. Always `developer`.

          - `const DeveloperDeveloper Developer = "developer"`

      - `type AutomationCreatedByAgent struct{…}`

        - `SessionID string`

          The creator session, which is also the automation's target.

          `minLength: 0`

        - `ToolCallID string`

          The tool call that created the automation.

          `minLength: 0`

        - `Type Agent`

          The type of the object. Always `agent`.

          - `const AgentAgent Agent = "agent"`

    - `Expression string`

      The cron expression determining scheduled occurrences.

      `minLength: 0`

    - `Metadata map[string, string]`

      Custom string key-value pairs attached to the automation.

    - `Name string`

      The automation's display name.

      `minLength: 0`

    - `Object AgentAutomation`

      Always `agent.automation`.

      - `const AgentAutomationAgentAutomation AgentAutomation = "agent.automation"`

    - `Status PeriodicAutomationStatus`

      Whether scheduled delivery is active or paused.

      - `const PeriodicAutomationStatusActive PeriodicAutomationStatus = "active"`

      - `const PeriodicAutomationStatusPaused PeriodicAutomationStatus = "paused"`

    - `Target AutomationTargetUnion`

      The session configuration or existing session receiving invocations.

      - `type AutomationTargetNewSession struct{…}`

        - `Agent AutomationAgentConfig`

          The inline agent configuration, or null when agent_id is configured.

          - `Instructions string`

            Custom instructions, or null when absent.

            `minLength: 0`

          - `Model string`

            The requested model name.

            `minLength: 0`

          - `MultiAgent MultiAgentConfig`

            The configuration for creating and coordinating subagents.

            - `Enabled bool`

              Whether subagent tools are enabled. Defaults to false.

            - `MaxConcurrentSubagents int64`

              Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

              `format: int64`, `minimum: 1`, `maximum: 4294967295`

          - `Reasoning AgentReasoning`

            The configured reasoning policy.

            - `Effort AgentReasoningEffort`

              The requested reasoning effort, or `null` when the model selects its own default.

              - `const AgentReasoningEffortNone AgentReasoningEffort = "none"`

              - `const AgentReasoningEffortMinimal AgentReasoningEffort = "minimal"`

              - `const AgentReasoningEffortLow AgentReasoningEffort = "low"`

              - `const AgentReasoningEffortMedium AgentReasoningEffort = "medium"`

              - `const AgentReasoningEffortHigh AgentReasoningEffort = "high"`

              - `const AgentReasoningEffortXhigh AgentReasoningEffort = "xhigh"`

              - `const AgentReasoningEffortMax AgentReasoningEffort = "max"`

            - `Summary AgentReasoningSummary`

              The requested reasoning summary format, or `null` when summaries are disabled.

              - `const AgentReasoningSummaryConcise AgentReasoningSummary = "concise"`

                Returns a concise reasoning summary when supported.

              - `const AgentReasoningSummaryDetailed AgentReasoningSummary = "detailed"`

                Returns a detailed reasoning summary when supported.

              - `const AgentReasoningSummaryAuto AgentReasoningSummary = "auto"`

                Automatically selects the most detailed summary supported by the model.

          - `ServiceTier AutomationAgentConfigServiceTier`

            The configured service-tier policy.

            - `const AutomationAgentConfigServiceTierAuto AutomationAgentConfigServiceTier = "auto"`

            - `const AutomationAgentConfigServiceTierDefault AutomationAgentConfigServiceTier = "default"`

            - `const AutomationAgentConfigServiceTierFlex AutomationAgentConfigServiceTier = "flex"`

            - `const AutomationAgentConfigServiceTierPriority AutomationAgentConfigServiceTier = "priority"`

            - `const AutomationAgentConfigServiceTierFast AutomationAgentConfigServiceTier = "fast"`

            - `const AutomationAgentConfigServiceTierUltrafast AutomationAgentConfigServiceTier = "ultrafast"`

          - `Text AgentText`

            The configured output format and verbosity.

            - `Format TextFormatUnion`

              The effective output format. Defaults to ordinary text.

              - `type TextFormatText struct{…}`

                Generates ordinary text without a structured-output constraint.

                - `Type Text`

                  The type of the object. Always `text`.

                  - `const TextText Text = "text"`

              - `type TextFormatJSONSchema struct{…}`

                Constrains generated text to a JSON Schema.

                - `Schema map[string, any]`

                  The JSON Schema that generated text must match.

                - `Type JSONSchema`

                  The type of the object. Always `json_schema`.

                  - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

            - `Verbosity AgentTextVerbosity`

              The amount of text produced by the agent. Defaults to `medium`.

              - `const AgentTextVerbosityLow AgentTextVerbosity = "low"`

              - `const AgentTextVerbosityMedium AgentTextVerbosity = "medium"`

              - `const AgentTextVerbosityHigh AgentTextVerbosity = "high"`

          - `Tools []AgentToolUnion`

            Configured tools, excluding confidential credentials.

            `minItems: 0`, `maxItems: 2000`

            - `type AgentToolFunction struct{…}`

              A function defined by the application.

              - `DeferLoading bool`

                Whether the function is deferred and discovered through tool search.

              - `Description string`

                A description of what the function does.

                `minLength: 0`

              - `Name string`

                The name of the function.

                `minLength: 0`

              - `Parameters map[string, any]`

                A JSON Schema object describing the function's arguments.

              - `Type Function`

                The type of the object. Always `function`.

                - `const FunctionFunction Function = "function"`

              - `Async bool`

                Whether the agent continues without waiting for the function result.

            - `type AgentToolProgrammaticToolCalling struct{…}`

              Enables calling tools from model-generated code.

              - `Enabled bool`

                Whether tools can be called from model-generated code.

              - `Type ProgrammaticToolCalling`

                The type of the object. Always `programmatic_tool_calling`.

                - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

            - `type AgentToolMcp struct{…}`

              Tools provided by a remote MCP server.

              - `AllowedTools []string`

                The MCP tools the agent may call.

                `minItems: 0`, `maxItems: 2000`

              - `ConnectionOrigin string`

                Where outbound MCP HTTP connections originate.

                - `const AgentToolMcpConnectionOriginService AgentToolMcpConnectionOrigin = "service"`

                - `const AgentToolMcpConnectionOriginEnvironment AgentToolMcpConnectionOrigin = "environment"`

              - `CredentialID string`

                The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

                `minLength: 0`

              - `RequestMetadata map[string, any]`

                Metadata included with requests to this MCP server.

              - `Required bool`

                Whether this MCP server must initialize before the first turn.

              - `ServerLabel string`

                A label used to identify the MCP server in tool calls.

                `minLength: 0`

              - `Transport McpTransportUnion`

                The transport used to connect to the MCP server.

                - `type McpTransportHTTP struct{…}`

                  Connects to an MCP server over HTTP.

                  - `ServerURL string`

                    The URL of the MCP server.

                    `minLength: 0`

                  - `Type HTTP`

                    The type of the object. Always `http`.

                    - `const HTTPHTTP HTTP = "http"`

                - `type McpTransportStdio struct{…}`

                  Starts an MCP server as a local process.

                  - `Args []string`

                    Arguments passed to the MCP server command.

                    `minItems: 0`, `maxItems: 2000`

                  - `Command string`

                    The command used to start the MCP server.

                    `minLength: 0`

                  - `Cwd string`

                    The working directory used to start the MCP server.

                    `minLength: 0`

                  - `EnvVars []string`

                    Environment variable names inherited from the execution environment.

                    `minItems: 0`, `maxItems: 2000`

                  - `Type Stdio`

                    The type of the object. Always `stdio`.

                    - `const StdioStdio Stdio = "stdio"`

              - `Type Mcp`

                The type of the object. Always `mcp`.

                - `const McpMcp Mcp = "mcp"`

            - `type AgentToolWebSearch struct{…}`

              Web search.

              - `AllowedDomains []string`

                Allowed search domains, or `null` when the search is unrestricted.

                `minItems: 0`, `maxItems: 2000`

              - `ContextSize string`

                The amount of search context made available to the model. Defaults to `medium`.

                - `const AgentToolWebSearchContextSizeLow AgentToolWebSearchContextSize = "low"`

                - `const AgentToolWebSearchContextSizeMedium AgentToolWebSearchContextSize = "medium"`

                - `const AgentToolWebSearchContextSizeHigh AgentToolWebSearchContextSize = "high"`

              - `Location AgentToolWebSearchLocation`

                Approximate location used to localize search results, if provided.

                - `City string`

                  The city name.

                  `minLength: 0`

                - `Country string`

                  The two-letter ISO country code, such as `US`.

                  `minLength: 0`

                - `Region string`

                  The region or state name.

                  `minLength: 0`

                - `Timezone string`

                  The IANA timezone, such as `America/Los_Angeles`.

                  `minLength: 0`

              - `Mode string`

                The source used for web search results.

                - `const AgentToolWebSearchModeDisabled AgentToolWebSearchMode = "disabled"`

                - `const AgentToolWebSearchModeCached AgentToolWebSearchMode = "cached"`

                - `const AgentToolWebSearchModeLive AgentToolWebSearchMode = "live"`

              - `Type WebSearch`

                The type of the object. Always `web_search`.

                - `const WebSearchWebSearch WebSearch = "web_search"`

            - `type AgentToolComputerUse struct{…}`

              Browser use in an OpenAI-hosted session.

              - `IncludeScreenshots bool`

                Whether computer tool outputs include screenshots.

              - `Type ComputerUse`

                The type of the object. Always `computer_use`.

                - `const ComputerUseComputerUse ComputerUse = "computer_use"`

            - `type AgentToolAutomations struct{…}`

              Lets the agent manage its own scheduled wakeups.

              - `Type Automations`

                The type of the object. Always `automations`.

                - `const AutomationsAutomations Automations = "automations"`

          - `Compaction AutomationAgentConfigCompaction`

            The effective context compaction settings.

            - `Async bool`

              Whether context is compacted in the background. Defaults to true.

          - `Experimental AutomationAgentConfigExperimental`

            The effective experimental settings for the agent.

            - `TimeAwareness bool`

              Whether the model receives periodic current-time reminders.

        - `AgentID string`

          The saved agent reference, or null when an inline agent is configured.

          `minLength: 0`

        - `Environment AutomationEnvironmentUnion`

          Configuration or references used to select the execution environment.

          - `type AutomationEnvironmentNone struct{…}`

            - `Type None`

              The type of the object. Always `none`.

              - `const NoneNone None = "none"`

          - `type AutomationEnvironmentOpenAIHosted struct{…}`

            Hosted environment selection with confidential setup commands and variables omitted.

            - `CapabilityDirectories []string`

              Directory overrides, or null to inherit the template or creation default.

              `minItems: 0`, `maxItems: 2000`

            - `ContainerSize string`

              The configured container size, or null to use the creation default.

              - `const AutomationEnvironmentOpenAIHostedContainerSizeSmall AutomationEnvironmentOpenAIHostedContainerSize = "small"`

              - `const AutomationEnvironmentOpenAIHostedContainerSizeMedium AutomationEnvironmentOpenAIHostedContainerSize = "medium"`

              - `const AutomationEnvironmentOpenAIHostedContainerSizeLarge AutomationEnvironmentOpenAIHostedContainerSize = "large"`

            - `Desktop AutomationEnvironmentOpenAIHostedDesktop`

              Desktop overrides, or null to inherit the template or creation default.

              - `Enabled bool`

                Whether the environment provisions a desktop and browser proxy.

            - `EnvironmentID string`

              An existing environment reference, or null when provisioning a new environment.

              `minLength: 0`

            - `EnvironmentTemplateID string`

              A template reference, or null when no template is selected.

              `minLength: 0`

            - `Files []AutomationEnvironmentOpenAIHostedFileUnion`

              File overrides, excluding contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `type AutomationEnvironmentOpenAIHostedFileFileID struct{…}`

                A project-scoped Files API reference resolved separately for each session.

                - `FileID string`

                  The ID of the uploaded file.

                  `minLength: 0`

                - `Path string`

                  The file's absolute path inside the environment.

                  `minLength: 0`

                - `Type FileID`

                  The type of the object. Always `file_id`.

                  - `const FileIDFileID FileID = "file_id"`

              - `type AutomationEnvironmentOpenAIHostedFileInline struct{…}`

                Metadata for confidential inline file contents.

                - `Path string`

                  The file's absolute path inside the environment.

                  `minLength: 0`

                - `SizeBytes int64`

                  The decoded size of the inline file in bytes.

                  `format: int64`, `minimum: 0`

                - `Type Inline`

                  The type of the object. Always `inline`.

                  - `const InlineInline Inline = "inline"`

            - `Network AutomationEnvironmentOpenAIHostedNetwork`

              Network overrides, or null to inherit the template or creation default.

              - `Access string`

                The environment's network access mode.

                - `const AutomationEnvironmentOpenAIHostedNetworkAccessEnabled AutomationEnvironmentOpenAIHostedNetworkAccess = "enabled"`

                  Allows unrestricted network access.

                - `const AutomationEnvironmentOpenAIHostedNetworkAccessDisabled AutomationEnvironmentOpenAIHostedNetworkAccess = "disabled"`

                  Disables network access.

                - `const AutomationEnvironmentOpenAIHostedNetworkAccessRestricted AutomationEnvironmentOpenAIHostedNetworkAccess = "restricted"`

                  Applies the configured domain restrictions.

              - `AllowedDomains []string`

                Domains the environment may access when network access is restricted.

                `minItems: 0`, `maxItems: 2000`

            - `Packages AutomationEnvironmentOpenAIHostedPackages`

              Package overrides, or null to inherit the template or creation default.

              - `Npm []string`

                npm packages installed globally in the environment.

                `minItems: 0`, `maxItems: 16384`

              - `Python []string`

                Python packages installed in the environment.

                `minItems: 0`, `maxItems: 16384`

              - `System []string`

                System packages installed in the environment.

                `minItems: 0`, `maxItems: 16384`

            - `Plugins []HostedPlugin`

              Plugin overrides, excluding archive contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `Description string`

                The installed plugin description.

                `minLength: 0`

              - `Name string`

                The installed plugin name.

                `minLength: 0`

              - `Type Inline`

                The type of the object. Always `inline`.

                - `const InlineInline Inline = "inline"`

            - `Skills []AutomationEnvironmentOpenAIHostedSkillUnion`

              Skill overrides, excluding archive contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `type AutomationEnvironmentOpenAIHostedSkillSkillReference struct{…}`

                A skill resolved afresh from the Skills API whenever a session starts.

                - `SkillID string`

                  The referenced skill ID.

                  `minLength: 0`

                - `Type SkillReference`

                  The type of the object. Always `skill_reference`.

                  - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

                - `Version string`

                  The requested version selector, including `latest`.

                  `minLength: 0`

              - `type AutomationEnvironmentOpenAIHostedSkillInline struct{…}`

                Safe metadata for an inline skill archive.

                - `Description string`

                  The skill description declared in `SKILL.md`.

                  `minLength: 0`

                - `Name string`

                  The skill name declared in `SKILL.md`.

                  `minLength: 0`

                - `Type Inline`

                  The type of the object. Always `inline`.

                  - `const InlineInline Inline = "inline"`

            - `Type OpenAIHosted`

              The type of the object. Always `openai_hosted`.

              - `const OpenAIHostedOpenAIHosted OpenAIHosted = "openai_hosted"`

          - `type AutomationEnvironmentSelfHosted struct{…}`

            - `CapabilityDirectories []string`

              Directories that expose capabilities to the agent.

              `minItems: 0`, `maxItems: 2000`

            - `EnvironmentID string`

              An existing registration, or null to create a session-owned environment.

              `minLength: 0`

            - `Type SelfHosted`

              The type of the object. Always `self_hosted`.

              - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

            - `WorkspaceDirectory string`

              The absolute project directory in the environment.

              `minLength: 0`

        - `Input []AutomationTargetNewSessionInput`

          Initial input delivered to each new session.

          `minItems: 0`, `maxItems: 2000`

          - `Content []InputContentUnion`

            The content of the message.

            `minItems: 0`, `maxItems: 2000`

            - `type InputContentInputText struct{…}`

              Text input recorded in a session item.

              - `Text string`

                The text supplied to the agent.

                `minLength: 0`

              - `Type InputText`

                The type of the object. Always `input_text`.

                - `const InputTextInputText InputText = "input_text"`

            - `type InputContentInputImage struct{…}`

              Image input recorded in a session item.

              - `ImageURL string`

                The URL of the image supplied to the agent, which may be a base64-encoded data URL.

                `minLength: 0`

              - `Type InputImage`

                The type of the object. Always `input_image`.

                - `const InputImageInputImage InputImage = "input_image"`

          - `Role User`

            The role of the message author. Always `user`.

            - `const UserUser User = "user"`

          - `Type Message`

            The type of the input item. Always `message`.

            - `const MessageMessage Message = "message"`

        - `Metadata map[string, string]`

          Metadata attached to each new session.

        - `Type NewSession`

          The type of the object. Always `new_session`.

          - `const NewSessionNewSession NewSession = "new_session"`

        - `VaultIDs []string`

          Vaults made available to each new session.

          `minItems: 0`, `maxItems: 2000`

      - `type AutomationTargetExistingSession struct{…}`

        - `Instructions string`

          Saved instructions delivered as an automation notification.

          `minLength: 0`

        - `SessionID string`

          The session receiving each invocation.

          `minLength: 0`

        - `Type ExistingSession`

          The type of the object. Always `existing_session`.

          - `const ExistingSessionExistingSession ExistingSession = "existing_session"`

    - `Timezone string`

      The timezone used to interpret the expression.

      `minLength: 0`

    - `Type Periodic`

      The type of the object. Always `periodic`.

      - `const PeriodicPeriodic Periodic = "periodic"`

  - `type OneTimeAutomation struct{…}`

    Fields shared by periodic and one-time automations.

    - `ID string`

      The automation ID.

      `minLength: 0`

    - `CreatedAt int64`

      The creation time as a Unix timestamp in seconds.

      `format: int64`

    - `CreatedBy AutomationCreatedByUnion`

      Service-recorded provenance; callers cannot supply this field.

    - `Metadata map[string, string]`

      Custom string key-value pairs attached to the automation.

    - `Name string`

      The automation's display name.

      `minLength: 0`

    - `Object AgentAutomation`

      Always `agent.automation`.

      - `const AgentAutomationAgentAutomation AgentAutomation = "agent.automation"`

    - `RunAt int64`

      The Unix timestamp, in seconds, of the scheduled occurrence.

      `format: int64`

    - `Status OneTimeAutomationStatus`

      Completion means the schedule has finished, not the agent's work.

      - `const OneTimeAutomationStatusActive OneTimeAutomationStatus = "active"`

      - `const OneTimeAutomationStatusPaused OneTimeAutomationStatus = "paused"`

      - `const OneTimeAutomationStatusCompleted OneTimeAutomationStatus = "completed"`

    - `Target AutomationTargetUnion`

      The session configuration or existing session receiving invocations.

    - `Type Once`

      The type of the object. Always `once`.

      - `const OnceOnce Once = "once"`

### Automation Agent Config

- `type AutomationAgentConfig struct{…}`

  Inline agent configuration without a generated session-local identity.

  - `Instructions string`

    Custom instructions, or null when absent.

    `minLength: 0`

  - `Model string`

    The requested model name.

    `minLength: 0`

  - `MultiAgent MultiAgentConfig`

    The configuration for creating and coordinating subagents.

    - `Enabled bool`

      Whether subagent tools are enabled. Defaults to false.

    - `MaxConcurrentSubagents int64`

      Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

      `format: int64`, `minimum: 1`, `maximum: 4294967295`

  - `Reasoning AgentReasoning`

    The configured reasoning policy.

    - `Effort AgentReasoningEffort`

      The requested reasoning effort, or `null` when the model selects its own default.

      - `const AgentReasoningEffortNone AgentReasoningEffort = "none"`

      - `const AgentReasoningEffortMinimal AgentReasoningEffort = "minimal"`

      - `const AgentReasoningEffortLow AgentReasoningEffort = "low"`

      - `const AgentReasoningEffortMedium AgentReasoningEffort = "medium"`

      - `const AgentReasoningEffortHigh AgentReasoningEffort = "high"`

      - `const AgentReasoningEffortXhigh AgentReasoningEffort = "xhigh"`

      - `const AgentReasoningEffortMax AgentReasoningEffort = "max"`

    - `Summary AgentReasoningSummary`

      The requested reasoning summary format, or `null` when summaries are disabled.

      - `const AgentReasoningSummaryConcise AgentReasoningSummary = "concise"`

        Returns a concise reasoning summary when supported.

      - `const AgentReasoningSummaryDetailed AgentReasoningSummary = "detailed"`

        Returns a detailed reasoning summary when supported.

      - `const AgentReasoningSummaryAuto AgentReasoningSummary = "auto"`

        Automatically selects the most detailed summary supported by the model.

  - `ServiceTier AutomationAgentConfigServiceTier`

    The configured service-tier policy.

    - `const AutomationAgentConfigServiceTierAuto AutomationAgentConfigServiceTier = "auto"`

    - `const AutomationAgentConfigServiceTierDefault AutomationAgentConfigServiceTier = "default"`

    - `const AutomationAgentConfigServiceTierFlex AutomationAgentConfigServiceTier = "flex"`

    - `const AutomationAgentConfigServiceTierPriority AutomationAgentConfigServiceTier = "priority"`

    - `const AutomationAgentConfigServiceTierFast AutomationAgentConfigServiceTier = "fast"`

    - `const AutomationAgentConfigServiceTierUltrafast AutomationAgentConfigServiceTier = "ultrafast"`

  - `Text AgentText`

    The configured output format and verbosity.

    - `Format TextFormatUnion`

      The effective output format. Defaults to ordinary text.

      - `type TextFormatText struct{…}`

        Generates ordinary text without a structured-output constraint.

        - `Type Text`

          The type of the object. Always `text`.

          - `const TextText Text = "text"`

      - `type TextFormatJSONSchema struct{…}`

        Constrains generated text to a JSON Schema.

        - `Schema map[string, any]`

          The JSON Schema that generated text must match.

        - `Type JSONSchema`

          The type of the object. Always `json_schema`.

          - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

    - `Verbosity AgentTextVerbosity`

      The amount of text produced by the agent. Defaults to `medium`.

      - `const AgentTextVerbosityLow AgentTextVerbosity = "low"`

      - `const AgentTextVerbosityMedium AgentTextVerbosity = "medium"`

      - `const AgentTextVerbosityHigh AgentTextVerbosity = "high"`

  - `Tools []AgentToolUnion`

    Configured tools, excluding confidential credentials.

    `minItems: 0`, `maxItems: 2000`

    - `type AgentToolFunction struct{…}`

      A function defined by the application.

      - `DeferLoading bool`

        Whether the function is deferred and discovered through tool search.

      - `Description string`

        A description of what the function does.

        `minLength: 0`

      - `Name string`

        The name of the function.

        `minLength: 0`

      - `Parameters map[string, any]`

        A JSON Schema object describing the function's arguments.

      - `Type Function`

        The type of the object. Always `function`.

        - `const FunctionFunction Function = "function"`

      - `Async bool`

        Whether the agent continues without waiting for the function result.

    - `type AgentToolProgrammaticToolCalling struct{…}`

      Enables calling tools from model-generated code.

      - `Enabled bool`

        Whether tools can be called from model-generated code.

      - `Type ProgrammaticToolCalling`

        The type of the object. Always `programmatic_tool_calling`.

        - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

    - `type AgentToolMcp struct{…}`

      Tools provided by a remote MCP server.

      - `AllowedTools []string`

        The MCP tools the agent may call.

        `minItems: 0`, `maxItems: 2000`

      - `ConnectionOrigin string`

        Where outbound MCP HTTP connections originate.

        - `const AgentToolMcpConnectionOriginService AgentToolMcpConnectionOrigin = "service"`

        - `const AgentToolMcpConnectionOriginEnvironment AgentToolMcpConnectionOrigin = "environment"`

      - `CredentialID string`

        The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

        `minLength: 0`

      - `RequestMetadata map[string, any]`

        Metadata included with requests to this MCP server.

      - `Required bool`

        Whether this MCP server must initialize before the first turn.

      - `ServerLabel string`

        A label used to identify the MCP server in tool calls.

        `minLength: 0`

      - `Transport McpTransportUnion`

        The transport used to connect to the MCP server.

        - `type McpTransportHTTP struct{…}`

          Connects to an MCP server over HTTP.

          - `ServerURL string`

            The URL of the MCP server.

            `minLength: 0`

          - `Type HTTP`

            The type of the object. Always `http`.

            - `const HTTPHTTP HTTP = "http"`

        - `type McpTransportStdio struct{…}`

          Starts an MCP server as a local process.

          - `Args []string`

            Arguments passed to the MCP server command.

            `minItems: 0`, `maxItems: 2000`

          - `Command string`

            The command used to start the MCP server.

            `minLength: 0`

          - `Cwd string`

            The working directory used to start the MCP server.

            `minLength: 0`

          - `EnvVars []string`

            Environment variable names inherited from the execution environment.

            `minItems: 0`, `maxItems: 2000`

          - `Type Stdio`

            The type of the object. Always `stdio`.

            - `const StdioStdio Stdio = "stdio"`

      - `Type Mcp`

        The type of the object. Always `mcp`.

        - `const McpMcp Mcp = "mcp"`

    - `type AgentToolWebSearch struct{…}`

      Web search.

      - `AllowedDomains []string`

        Allowed search domains, or `null` when the search is unrestricted.

        `minItems: 0`, `maxItems: 2000`

      - `ContextSize string`

        The amount of search context made available to the model. Defaults to `medium`.

        - `const AgentToolWebSearchContextSizeLow AgentToolWebSearchContextSize = "low"`

        - `const AgentToolWebSearchContextSizeMedium AgentToolWebSearchContextSize = "medium"`

        - `const AgentToolWebSearchContextSizeHigh AgentToolWebSearchContextSize = "high"`

      - `Location AgentToolWebSearchLocation`

        Approximate location used to localize search results, if provided.

        - `City string`

          The city name.

          `minLength: 0`

        - `Country string`

          The two-letter ISO country code, such as `US`.

          `minLength: 0`

        - `Region string`

          The region or state name.

          `minLength: 0`

        - `Timezone string`

          The IANA timezone, such as `America/Los_Angeles`.

          `minLength: 0`

      - `Mode string`

        The source used for web search results.

        - `const AgentToolWebSearchModeDisabled AgentToolWebSearchMode = "disabled"`

        - `const AgentToolWebSearchModeCached AgentToolWebSearchMode = "cached"`

        - `const AgentToolWebSearchModeLive AgentToolWebSearchMode = "live"`

      - `Type WebSearch`

        The type of the object. Always `web_search`.

        - `const WebSearchWebSearch WebSearch = "web_search"`

    - `type AgentToolComputerUse struct{…}`

      Browser use in an OpenAI-hosted session.

      - `IncludeScreenshots bool`

        Whether computer tool outputs include screenshots.

      - `Type ComputerUse`

        The type of the object. Always `computer_use`.

        - `const ComputerUseComputerUse ComputerUse = "computer_use"`

    - `type AgentToolAutomations struct{…}`

      Lets the agent manage its own scheduled wakeups.

      - `Type Automations`

        The type of the object. Always `automations`.

        - `const AutomationsAutomations Automations = "automations"`

  - `Compaction AutomationAgentConfigCompaction`

    The effective context compaction settings.

    - `Async bool`

      Whether context is compacted in the background. Defaults to true.

  - `Experimental AutomationAgentConfigExperimental`

    The effective experimental settings for the agent.

    - `TimeAwareness bool`

      Whether the model receives periodic current-time reminders.

### Automation Created By

- `type AutomationCreatedByUnion interface{…}`

  How the automation was created, independently of how an invocation started.

  - `type AutomationCreatedByDeveloper struct{…}`

    - `Type Developer`

      The type of the object. Always `developer`.

      - `const DeveloperDeveloper Developer = "developer"`

  - `type AutomationCreatedByAgent struct{…}`

    - `SessionID string`

      The creator session, which is also the automation's target.

      `minLength: 0`

    - `ToolCallID string`

      The tool call that created the automation.

      `minLength: 0`

    - `Type Agent`

      The type of the object. Always `agent`.

      - `const AgentAgent Agent = "agent"`

### Automation Deleted

- `type AutomationDeleted struct{…}`

  - `ID string`

    The deleted automation ID.

    `minLength: 0`

  - `Deleted bool`

    Always true.

  - `Object AgentAutomationDeleted`

    Always `agent.automation.deleted`.

    - `const AgentAutomationDeletedAgentAutomationDeleted AgentAutomationDeleted = "agent.automation.deleted"`

### Automation Environment

- `type AutomationEnvironmentUnion interface{…}`

  Environment selection saved before an invocation creates its session.

  - `type AutomationEnvironmentNone struct{…}`

    - `Type None`

      The type of the object. Always `none`.

      - `const NoneNone None = "none"`

  - `type AutomationEnvironmentOpenAIHosted struct{…}`

    Hosted environment selection with confidential setup commands and variables omitted.

    - `CapabilityDirectories []string`

      Directory overrides, or null to inherit the template or creation default.

      `minItems: 0`, `maxItems: 2000`

    - `ContainerSize string`

      The configured container size, or null to use the creation default.

      - `const AutomationEnvironmentOpenAIHostedContainerSizeSmall AutomationEnvironmentOpenAIHostedContainerSize = "small"`

      - `const AutomationEnvironmentOpenAIHostedContainerSizeMedium AutomationEnvironmentOpenAIHostedContainerSize = "medium"`

      - `const AutomationEnvironmentOpenAIHostedContainerSizeLarge AutomationEnvironmentOpenAIHostedContainerSize = "large"`

    - `Desktop AutomationEnvironmentOpenAIHostedDesktop`

      Desktop overrides, or null to inherit the template or creation default.

      - `Enabled bool`

        Whether the environment provisions a desktop and browser proxy.

    - `EnvironmentID string`

      An existing environment reference, or null when provisioning a new environment.

      `minLength: 0`

    - `EnvironmentTemplateID string`

      A template reference, or null when no template is selected.

      `minLength: 0`

    - `Files []AutomationEnvironmentOpenAIHostedFileUnion`

      File overrides, excluding contents, or null to inherit.

      `minItems: 0`, `maxItems: 2000`

      - `type AutomationEnvironmentOpenAIHostedFileFileID struct{…}`

        A project-scoped Files API reference resolved separately for each session.

        - `FileID string`

          The ID of the uploaded file.

          `minLength: 0`

        - `Path string`

          The file's absolute path inside the environment.

          `minLength: 0`

        - `Type FileID`

          The type of the object. Always `file_id`.

          - `const FileIDFileID FileID = "file_id"`

      - `type AutomationEnvironmentOpenAIHostedFileInline struct{…}`

        Metadata for confidential inline file contents.

        - `Path string`

          The file's absolute path inside the environment.

          `minLength: 0`

        - `SizeBytes int64`

          The decoded size of the inline file in bytes.

          `format: int64`, `minimum: 0`

        - `Type Inline`

          The type of the object. Always `inline`.

          - `const InlineInline Inline = "inline"`

    - `Network AutomationEnvironmentOpenAIHostedNetwork`

      Network overrides, or null to inherit the template or creation default.

      - `Access string`

        The environment's network access mode.

        - `const AutomationEnvironmentOpenAIHostedNetworkAccessEnabled AutomationEnvironmentOpenAIHostedNetworkAccess = "enabled"`

          Allows unrestricted network access.

        - `const AutomationEnvironmentOpenAIHostedNetworkAccessDisabled AutomationEnvironmentOpenAIHostedNetworkAccess = "disabled"`

          Disables network access.

        - `const AutomationEnvironmentOpenAIHostedNetworkAccessRestricted AutomationEnvironmentOpenAIHostedNetworkAccess = "restricted"`

          Applies the configured domain restrictions.

      - `AllowedDomains []string`

        Domains the environment may access when network access is restricted.

        `minItems: 0`, `maxItems: 2000`

    - `Packages AutomationEnvironmentOpenAIHostedPackages`

      Package overrides, or null to inherit the template or creation default.

      - `Npm []string`

        npm packages installed globally in the environment.

        `minItems: 0`, `maxItems: 16384`

      - `Python []string`

        Python packages installed in the environment.

        `minItems: 0`, `maxItems: 16384`

      - `System []string`

        System packages installed in the environment.

        `minItems: 0`, `maxItems: 16384`

    - `Plugins []HostedPlugin`

      Plugin overrides, excluding archive contents, or null to inherit.

      `minItems: 0`, `maxItems: 2000`

      - `Description string`

        The installed plugin description.

        `minLength: 0`

      - `Name string`

        The installed plugin name.

        `minLength: 0`

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

    - `Skills []AutomationEnvironmentOpenAIHostedSkillUnion`

      Skill overrides, excluding archive contents, or null to inherit.

      `minItems: 0`, `maxItems: 2000`

      - `type AutomationEnvironmentOpenAIHostedSkillSkillReference struct{…}`

        A skill resolved afresh from the Skills API whenever a session starts.

        - `SkillID string`

          The referenced skill ID.

          `minLength: 0`

        - `Type SkillReference`

          The type of the object. Always `skill_reference`.

          - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

        - `Version string`

          The requested version selector, including `latest`.

          `minLength: 0`

      - `type AutomationEnvironmentOpenAIHostedSkillInline struct{…}`

        Safe metadata for an inline skill archive.

        - `Description string`

          The skill description declared in `SKILL.md`.

          `minLength: 0`

        - `Name string`

          The skill name declared in `SKILL.md`.

          `minLength: 0`

        - `Type Inline`

          The type of the object. Always `inline`.

          - `const InlineInline Inline = "inline"`

    - `Type OpenAIHosted`

      The type of the object. Always `openai_hosted`.

      - `const OpenAIHostedOpenAIHosted OpenAIHosted = "openai_hosted"`

  - `type AutomationEnvironmentSelfHosted struct{…}`

    - `CapabilityDirectories []string`

      Directories that expose capabilities to the agent.

      `minItems: 0`, `maxItems: 2000`

    - `EnvironmentID string`

      An existing registration, or null to create a session-owned environment.

      `minLength: 0`

    - `Type SelfHosted`

      The type of the object. Always `self_hosted`.

      - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

    - `WorkspaceDirectory string`

      The absolute project directory in the environment.

      `minLength: 0`

### Automation Schedule Param

- `type AutomationScheduleParamUnionResp interface{…}`

  Creates an automation without invoking it immediately.

  - `AutomationScheduleParamPeriodicResp`

    - `Expression string`

      A standard five-field cron expression defining scheduled occurrences.

      `minLength: 1`, `maxLength: 256`

    - `Name string`

      A human-readable name for the automation.

      `minLength: 1`, `maxLength: 256`

    - `Target AutomationTargetParamUnionResp`

      The session an automation invocation targets.

      - `AutomationTargetParamNewSessionResp`

        - `Environment EnvironmentParamUnionResp`

          The execution environment for each new session.

          - `EnvironmentParamNoneResp`

            - `Type None`

              The type of the object. Always `none`.

              - `const NoneNone None = "none"`

          - `EnvironmentParamOpenAIHostedResp`

            - `Type OpenAIHosted`

              The type of the object. Always `openai_hosted`.

              - `const OpenAIHostedOpenAIHosted OpenAIHosted = "openai_hosted"`

            - `CapabilityDirectories []string`

              Directories that contain capabilities exposed to the agent. Defaults to an empty list.

              `minItems: 0`, `maxItems: 16384`

            - `ContainerSize string`

              The hosted container size. Omission selects the medium tier.

              - `const EnvironmentParamOpenAIHostedContainerSizeSmall EnvironmentParamOpenAIHostedContainerSize = "small"`

              - `const EnvironmentParamOpenAIHostedContainerSizeMedium EnvironmentParamOpenAIHostedContainerSize = "medium"`

              - `const EnvironmentParamOpenAIHostedContainerSizeLarge EnvironmentParamOpenAIHostedContainerSize = "large"`

            - `Desktop EnvironmentParamOpenAIHostedDesktopResp`

              Desktop provisioning. Omission or null inherits the template setting, or defaults to disabled.

              - `Enabled bool`

                Whether to provision the desktop and its browser proxy.

            - `Env map[string, string]`

              Environment variables made available to the agent.

            - `EnvironmentID string`

              An existing prewarmed environment. Cannot be combined with a template or inline configuration.

              `minLength: 9`, `maxLength: 256`

            - `EnvironmentTemplateID string`

              A reusable hosted template applied before inline session configuration. Omitted fields inherit the template; network overrides cannot broaden its policy.

              `minLength: 0`, `maxLength: 64`

            - `Files []HostedEnvironmentFileParamUnionResp`

              Files available before the agent starts. Defaults to an empty list.

              `minItems: 0`, `maxItems: 50`

              - `HostedEnvironmentFileParamFileIDResp`

                - `FileID string`

                  The ID of the uploaded file.

                  `minLength: 1`, `maxLength: 256`

                - `Path string`

                  The absolute destination path inside `/workspace`.

                  `minLength: 1`, `maxLength: 4096`

                - `Type FileID`

                  The type of the object. Always `file_id`.

                  - `const FileIDFileID FileID = "file_id"`

              - `HostedEnvironmentFileParamInlineResp`

                - `Data string`

                  The standard-base64-encoded file contents.

                  `minLength: 0`, `maxLength: 6990508`

                - `Path string`

                  The absolute destination path inside `/workspace`.

                  `minLength: 1`, `maxLength: 4096`

                - `Type Inline`

                  The type of the object. Always `inline`.

                  - `const InlineInline Inline = "inline"`

            - `Network EnvironmentParamOpenAIHostedNetworkResp`

              Network access policy for the environment. If omitted, the API version determines whether network access is enabled or disabled.

              - `Access string`

                The environment's network access mode.

                - `const EnvironmentParamOpenAIHostedNetworkAccessEnabled EnvironmentParamOpenAIHostedNetworkAccess = "enabled"`

                  Allows unrestricted network access.

                - `const EnvironmentParamOpenAIHostedNetworkAccessDisabled EnvironmentParamOpenAIHostedNetworkAccess = "disabled"`

                  Disables network access.

                - `const EnvironmentParamOpenAIHostedNetworkAccessRestricted EnvironmentParamOpenAIHostedNetworkAccess = "restricted"`

                  Applies the configured domain restrictions.

              - `AllowedDomains []string`

                Domains the environment may access when network access is restricted.

                `minItems: 0`, `maxItems: 16384`

              - `BlockedDomains []string`

                Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

                `minItems: 0`, `maxItems: 100`

            - `Packages EnvironmentParamOpenAIHostedPackagesResp`

              Packages to install in the environment. Defaults to empty package lists.

              - `Npm []string`

                npm packages to install globally. Defaults to an empty list.

                `minItems: 0`, `maxItems: 16384`

              - `Python []string`

                Python packages to install. Defaults to an empty list.

                `minItems: 0`, `maxItems: 16384`

              - `System []string`

                System packages to install. Defaults to an empty list.

                `minItems: 0`, `maxItems: 16384`

            - `Plugins []HostedPluginParamResp`

              Plugins provided as inline ZIP archives. Defaults to an empty list.

              `minItems: 0`, `maxItems: 32`

              - `Description string`

                The plugin description declared in `.codex-plugin/plugin.json`.

                `minLength: 0`, `maxLength: 1048576`

              - `Name string`

                The plugin name declared in `.codex-plugin/plugin.json`.

                `minLength: 1`, `maxLength: 64`

              - `Source InlineCapabilitySourceParamResp`

                Provides ZIP bytes encoded with standard base64.

                - `Data string`

                  Standard-base64 encoded ZIP archive bytes.

                  `minLength: 1`, `maxLength: 70254592`

                - `MediaType ApplicationZip`

                  The archive media type, always `application/zip`.

                  - `const ApplicationZipApplicationZip ApplicationZip = "application/zip"`

                - `Type Base64`

                  The type of the object. Always `base64`.

                  - `const Base64Base64 Base64 = "base64"`

              - `Type Inline`

                The type of the object. Always `inline`.

                - `const InlineInline Inline = "inline"`

            - `SetupCommands []SetupCommandParamResp`

              Ordered, confidential setup commands. Command bodies are never returned.

              `minItems: 0`, `maxItems: 16`

              - `Command string`

                The shell command to execute.

                `minLength: 0`, `maxLength: 65536`

              - `Cwd string`

                The absolute working directory. Defaults to `/workspace`.

                `minLength: 0`, `maxLength: 4096`

            - `Skills []HostedSkillParamUnionResp`

              Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

              `minItems: 0`, `maxItems: 200`

              - `HostedSkillParamSkillReferenceResp`

                - `SkillID string`

                  The ID of the skill created through `/v1/skills`.

                  `minLength: 1`, `maxLength: 64`

                - `Type SkillReference`

                  The type of the object. Always `skill_reference`.

                  - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

                - `Version string`

                  The skill version, a positive integer or `latest`; omission selects the default.

                  `minLength: 0`, `maxLength: 1048576`

              - `HostedSkillParamInlineResp`

                - `Description string`

                  The skill description declared in `SKILL.md`.

                  `minLength: 0`, `maxLength: 1048576`

                - `Name string`

                  The skill name declared in `SKILL.md`.

                  `minLength: 1`, `maxLength: 64`

                - `Source InlineCapabilitySourceParamResp`

                  Provides ZIP bytes encoded with standard base64.

                - `Type Inline`

                  The type of the object. Always `inline`.

                  - `const InlineInline Inline = "inline"`

          - `EnvironmentParamSelfHostedResp`

            - `Type SelfHosted`

              The type of the object. Always `self_hosted`.

              - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

            - `WorkspaceDirectory string`

              Absolute project directory inside the self-hosted environment.

              `minLength: 0`, `maxLength: 1048576`

            - `CapabilityDirectories []string`

              Directories that contain capabilities exposed to the agent. Defaults to an empty list.

              `minItems: 0`, `maxItems: 16384`

        - `Input []AgentSessionInputMessageParamResp`

          Initial user messages submitted with each new session.

          `minItems: 0`, `maxItems: 16384`

          - `Content []InputContentParamUnionResp`

            The content of the message.

            `minItems: 0`, `maxItems: 16384`

            - `InputContentParamInputTextResp`

              - `Text string`

                The text sent to the model.

                `minLength: 0`, `maxLength: 1048576`

              - `Type InputText`

                The type of the object. Always `input_text`.

                - `const InputTextInputText InputText = "input_text"`

            - `InputContentParamInputImageResp`

              - `ImageURL string`

                The URL of the image sent to the model.

                `minLength: 0`, `maxLength: 1048576`

              - `Type InputImage`

                The type of the object. Always `input_image`.

                - `const InputImageInputImage InputImage = "input_image"`

          - `Role User`

            The role of the message author. Always `user`.

            - `const UserUser User = "user"`

          - `Type AgentSessionInputMessageParamType`

            The type of the input item. Always `message`.

            - `const AgentSessionInputMessageParamTypeMessage AgentSessionInputMessageParamType = "message"`

        - `Type NewSession`

          The type of the object. Always `new_session`.

          - `const NewSessionNewSession NewSession = "new_session"`

        - `Agent AutomationTargetParamNewSessionAgentResp`

          Inline agent configuration. Provide exactly one of agent and agent_id.

          - `Compaction AutomationTargetParamNewSessionAgentCompactionResp`

            Context compaction settings. Omit to keep the current settings. A supplied object replaces the settings; null or an empty object enables background compaction.

            - `Async bool`

              Whether to compact context in the background. Omission or null defaults to true. Set to false to use blocking compaction. Background compaction may increase token usage.

          - `Experimental AutomationTargetParamNewSessionAgentExperimentalResp`

            Experimental settings to merge by key. Omitted settings keep their current values.

            - `TimeAwareness bool`

              Whether to give the model periodic current-time reminders. Omit to keep the current setting.

          - `Instructions string`

            Additional instructions appended to the agent's default base instructions. Omit to leave unchanged.

            `minLength: 0`, `maxLength: 1048576`

          - `Model string`

            The model to use for the agent. The requested model name is preserved.

            `minLength: 0`, `maxLength: 1048576`

          - `MultiAgent MultiAgentConfigParamResp`

            Configuration for creating and coordinating subagents.

            - `Enabled bool`

              Whether subagent tools are enabled.

            - `MaxConcurrentSubagents int64`

              Maximum number of subagents that may run concurrently. Defaults to 6.

              `format: int64`, `minimum: 1`, `maximum: 4294967295`

          - `Reasoning AgentReasoningParamResp`

            Configuration for model reasoning. Omit to keep the current settings; pass `null` to reset to the model's default effort.

            - `Effort AgentReasoningParamEffort`

              The amount of reasoning effort the model should use. Omission lets the model select it.

              - `const AgentReasoningParamEffortNone AgentReasoningParamEffort = "none"`

              - `const AgentReasoningParamEffortMinimal AgentReasoningParamEffort = "minimal"`

              - `const AgentReasoningParamEffortLow AgentReasoningParamEffort = "low"`

              - `const AgentReasoningParamEffortMedium AgentReasoningParamEffort = "medium"`

              - `const AgentReasoningParamEffortHigh AgentReasoningParamEffort = "high"`

              - `const AgentReasoningParamEffortXhigh AgentReasoningParamEffort = "xhigh"`

              - `const AgentReasoningParamEffortMax AgentReasoningParamEffort = "max"`

            - `Summary AgentReasoningParamSummary`

              Controls whether the response includes a reasoning summary.

              - `const AgentReasoningParamSummaryConcise AgentReasoningParamSummary = "concise"`

                Returns a concise reasoning summary when supported.

              - `const AgentReasoningParamSummaryDetailed AgentReasoningParamSummary = "detailed"`

                Returns a detailed reasoning summary when supported.

              - `const AgentReasoningParamSummaryAuto AgentReasoningParamSummary = "auto"`

                Automatically selects the most detailed summary supported by the model.

          - `ServiceTier string`

            The service tier used for model requests.

            - `const AutomationTargetParamNewSessionAgentServiceTierAuto AutomationTargetParamNewSessionAgentServiceTier = "auto"`

              Selects the service tier automatically.

            - `const AutomationTargetParamNewSessionAgentServiceTierDefault AutomationTargetParamNewSessionAgentServiceTier = "default"`

              Uses the default service tier.

            - `const AutomationTargetParamNewSessionAgentServiceTierFlex AutomationTargetParamNewSessionAgentServiceTier = "flex"`

              Uses the flex service tier.

            - `const AutomationTargetParamNewSessionAgentServiceTierPriority AutomationTargetParamNewSessionAgentServiceTier = "priority"`

              Uses the priority service tier.

            - `const AutomationTargetParamNewSessionAgentServiceTierFast AutomationTargetParamNewSessionAgentServiceTier = "fast"`

              Uses the fast service tier.

            - `const AutomationTargetParamNewSessionAgentServiceTierUltrafast AutomationTargetParamNewSessionAgentServiceTier = "ultrafast"`

              Uses the ultrafast service tier.

          - `Text AgentTextParamResp`

            Configuration for text generated by the agent.

            - `Format TextFormatParamUnionResp`

              The output format. Omission uses ordinary text (`{"type": "text"}`).

              - `TextFormatParamTextResp`

                - `Type Text`

                  The type of the object. Always `text`.

                  - `const TextText Text = "text"`

              - `TextFormatParamJSONSchemaResp`

                - `Schema map[string, any]`

                  The JSON Schema that generated text must match.

                - `Type JSONSchema`

                  The type of the object. Always `json_schema`.

                  - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

            - `Verbosity AgentTextParamVerbosity`

              The amount of text the model should produce. Defaults to `medium`, matching Responses.

              - `const AgentTextParamVerbosityLow AgentTextParamVerbosity = "low"`

                Produces less text.

              - `const AgentTextParamVerbosityMedium AgentTextParamVerbosity = "medium"`

                Uses the default amount of text.

              - `const AgentTextParamVerbosityHigh AgentTextParamVerbosity = "high"`

                Produces more text.

          - `Tools []AgentToolParamUnionResp`

            Tools available to the agent. Omit to inherit, or pass null to clear them. The resolved tool list must fit within 3 MiB (3,145,728 bytes) of compact UTF-8 JSON.

            `minItems: 0`, `maxItems: 16384`

            - `AgentToolParamFunctionResp`

              - `Description string`

                A description of what the function does.

                `minLength: 0`, `maxLength: 1048576`

              - `Name string`

                The name of the function.

                `minLength: 0`, `maxLength: 1048576`

              - `Parameters map[string, any]`

                A JSON Schema object describing the function's arguments.

              - `Type Function`

                The type of the object. Always `function`.

                - `const FunctionFunction Function = "function"`

              - `Async bool`

                Whether the agent continues without waiting for the function result. Defaults to `false`.

              - `DeferLoading bool`

                Whether this function is deferred and discovered through tool search. Defaults to `false`.

            - `AgentToolParamToolSearchResp`

              - `Type ToolSearch`

                The type of the object. Always `tool_search`.

                - `const ToolSearchToolSearch ToolSearch = "tool_search"`

            - `AgentToolParamProgrammaticToolCallingResp`

              - `Type ProgrammaticToolCalling`

                The type of the object. Always `programmatic_tool_calling`.

                - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

              - `Enabled bool`

                Whether tools can be called from model-generated code. Defaults to `true`.

            - `AgentToolParamMcpResp`

              - `ServerLabel string`

                A label used to identify the MCP server in tool calls.

                `minLength: 0`, `maxLength: 1048576`

              - `Transport McpTransportParamUnionResp`

                The transport used to connect to the MCP server.

                - `McpTransportParamHTTPResp`

                  - `ServerURL string`

                    The URL of the MCP server.

                    `minLength: 0`, `maxLength: 1048576`

                  - `Type HTTP`

                    The type of the object. Always `http`.

                    - `const HTTPHTTP HTTP = "http"`

                  - `Authorization string`

                    The authorization value sent to the MCP server, if any.

                    `minLength: 0`, `maxLength: 1048576`

                  - `Headers map[string, string]`

                    Additional HTTP headers sent to the MCP server.

                - `McpTransportParamStdioResp`

                  - `Command string`

                    The command used to start the MCP server.

                    `minLength: 0`, `maxLength: 1048576`

                  - `Cwd string`

                    The working directory used to start the MCP server.

                    `minLength: 0`, `maxLength: 1048576`

                  - `Type Stdio`

                    The type of the object. Always `stdio`.

                    - `const StdioStdio Stdio = "stdio"`

                  - `Args []string`

                    Arguments passed to the MCP server command.

                    `minItems: 0`, `maxItems: 16384`

                  - `Env map[string, string]`

                    Environment variables set for the MCP server process.

                  - `EnvVars []string`

                    Environment variable names to inherit from the selected execution environment.

                    `minItems: 0`, `maxItems: 16384`

              - `Type Mcp`

                The type of the object. Always `mcp`.

                - `const McpMcp Mcp = "mcp"`

              - `AllowedTools []string`

                The MCP tools the agent may call. All server tools are allowed when omitted.

                `minItems: 0`, `maxItems: 16384`

              - `ConnectionOrigin string`

                Selects where outbound MCP HTTP connections originate. Omitted or `service` uses the Managed Agents service network; `environment` uses the session's selected environment.

                - `const AgentToolParamMcpConnectionOriginService AgentToolParamMcpConnectionOrigin = "service"`

                  Uses the Managed Agents service network.

                - `const AgentToolParamMcpConnectionOriginEnvironment AgentToolParamMcpConnectionOrigin = "environment"`

                  Uses the session's execution environment.

              - `CredentialID string`

                The attached vault credential used to authenticate this MCP server. Optional when exactly one attached credential matches the server URL.

                `minLength: 0`, `maxLength: 1048576`

              - `RequestMetadata map[string, any]`

                Metadata included with requests to this MCP server.

              - `Required bool`

                Whether this MCP server must initialize before the first turn. Defaults to `false`.

            - `AgentToolParamWebSearchResp`

              - `Type WebSearch`

                The type of the object. Always `web_search`.

                - `const WebSearchWebSearch WebSearch = "web_search"`

              - `AllowedDomains []string`

                Domains the search may include.

                `minItems: 0`, `maxItems: 16384`

              - `ContextSize string`

                The amount of search context made available to the model. Defaults to `medium`.

                - `const AgentToolParamWebSearchContextSizeLow AgentToolParamWebSearchContextSize = "low"`

                - `const AgentToolParamWebSearchContextSizeMedium AgentToolParamWebSearchContextSize = "medium"`

                - `const AgentToolParamWebSearchContextSizeHigh AgentToolParamWebSearchContextSize = "high"`

              - `Location AgentToolParamWebSearchLocationResp`

                Approximate location used to localize search results.

                - `City string`

                  The city name.

                  `minLength: 0`, `maxLength: 1048576`

                - `Country string`

                  The two-letter ISO country code, such as `US`.

                  `minLength: 0`, `maxLength: 1048576`

                - `Region string`

                  The region or state name.

                  `minLength: 0`, `maxLength: 1048576`

                - `Timezone string`

                  The IANA timezone, such as `America/Los_Angeles`.

                  `minLength: 0`, `maxLength: 1048576`

              - `Mode string`

                The source used for web search results. Defaults to `live`.

                - `const AgentToolParamWebSearchModeDisabled AgentToolParamWebSearchMode = "disabled"`

                  Disables web search.

                - `const AgentToolParamWebSearchModeCached AgentToolParamWebSearchMode = "cached"`

                  Uses cached search results.

                - `const AgentToolParamWebSearchModeLive AgentToolParamWebSearchMode = "live"`

                  Searches the live web.

            - `AgentToolParamComputerUseResp`

              - `Type ComputerUse`

                The type of the object. Always `computer_use`.

                - `const ComputerUseComputerUse ComputerUse = "computer_use"`

              - `IncludeScreenshots bool`

                Whether computer tool outputs include screenshots. Defaults to `false`.

            - `AgentToolParamAutomationsResp`

              - `Type Automations`

                The type of the object. Always `automations`.

                - `const AutomationsAutomations Automations = "automations"`

        - `AgentID string`

          A saved agent ID. Provide exactly one of agent and agent_id.

          `minLength: 0`, `maxLength: 64`

        - `Metadata map[string, string]`

          Metadata attached to each new session.

        - `VaultIDs []string`

          The IDs of vaults made available to each new session.

          `minItems: 0`, `maxItems: 16384`

      - `AutomationTargetParamExistingSessionResp`

        - `Instructions string`

          Instructions delivered as an automation notification.

          `minLength: 0`, `maxLength: 1048576`

        - `SessionID string`

          The session receiving each invocation.

          `minLength: 0`, `maxLength: 1048576`

        - `Type ExistingSession`

          The type of the object. Always `existing_session`.

          - `const ExistingSessionExistingSession ExistingSession = "existing_session"`

    - `Timezone string`

      The IANA timezone used to interpret the cron expression.

      `minLength: 1`, `maxLength: 128`

    - `Type Periodic`

      The type of the object. Always `periodic`.

      - `const PeriodicPeriodic Periodic = "periodic"`

    - `Metadata map[string, string]`

  - `AutomationScheduleParamOnceResp`

    - `Name string`

      A human-readable name for the automation.

      `minLength: 1`, `maxLength: 256`

    - `RunAt int64`

      A future Unix timestamp in seconds.

      `format: int64`

    - `Target AutomationTargetParamUnionResp`

      The session an automation invocation targets.

    - `Type Once`

      The type of the object. Always `once`.

      - `const OnceOnce Once = "once"`

    - `Metadata map[string, string]`

### Automation Target

- `type AutomationTargetUnion interface{…}`

  Saved target configuration, excluding confidential request-only values.

  - `type AutomationTargetNewSession struct{…}`

    - `Agent AutomationAgentConfig`

      The inline agent configuration, or null when agent_id is configured.

      - `Instructions string`

        Custom instructions, or null when absent.

        `minLength: 0`

      - `Model string`

        The requested model name.

        `minLength: 0`

      - `MultiAgent MultiAgentConfig`

        The configuration for creating and coordinating subagents.

        - `Enabled bool`

          Whether subagent tools are enabled. Defaults to false.

        - `MaxConcurrentSubagents int64`

          Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

          `format: int64`, `minimum: 1`, `maximum: 4294967295`

      - `Reasoning AgentReasoning`

        The configured reasoning policy.

        - `Effort AgentReasoningEffort`

          The requested reasoning effort, or `null` when the model selects its own default.

          - `const AgentReasoningEffortNone AgentReasoningEffort = "none"`

          - `const AgentReasoningEffortMinimal AgentReasoningEffort = "minimal"`

          - `const AgentReasoningEffortLow AgentReasoningEffort = "low"`

          - `const AgentReasoningEffortMedium AgentReasoningEffort = "medium"`

          - `const AgentReasoningEffortHigh AgentReasoningEffort = "high"`

          - `const AgentReasoningEffortXhigh AgentReasoningEffort = "xhigh"`

          - `const AgentReasoningEffortMax AgentReasoningEffort = "max"`

        - `Summary AgentReasoningSummary`

          The requested reasoning summary format, or `null` when summaries are disabled.

          - `const AgentReasoningSummaryConcise AgentReasoningSummary = "concise"`

            Returns a concise reasoning summary when supported.

          - `const AgentReasoningSummaryDetailed AgentReasoningSummary = "detailed"`

            Returns a detailed reasoning summary when supported.

          - `const AgentReasoningSummaryAuto AgentReasoningSummary = "auto"`

            Automatically selects the most detailed summary supported by the model.

      - `ServiceTier AutomationAgentConfigServiceTier`

        The configured service-tier policy.

        - `const AutomationAgentConfigServiceTierAuto AutomationAgentConfigServiceTier = "auto"`

        - `const AutomationAgentConfigServiceTierDefault AutomationAgentConfigServiceTier = "default"`

        - `const AutomationAgentConfigServiceTierFlex AutomationAgentConfigServiceTier = "flex"`

        - `const AutomationAgentConfigServiceTierPriority AutomationAgentConfigServiceTier = "priority"`

        - `const AutomationAgentConfigServiceTierFast AutomationAgentConfigServiceTier = "fast"`

        - `const AutomationAgentConfigServiceTierUltrafast AutomationAgentConfigServiceTier = "ultrafast"`

      - `Text AgentText`

        The configured output format and verbosity.

        - `Format TextFormatUnion`

          The effective output format. Defaults to ordinary text.

          - `type TextFormatText struct{…}`

            Generates ordinary text without a structured-output constraint.

            - `Type Text`

              The type of the object. Always `text`.

              - `const TextText Text = "text"`

          - `type TextFormatJSONSchema struct{…}`

            Constrains generated text to a JSON Schema.

            - `Schema map[string, any]`

              The JSON Schema that generated text must match.

            - `Type JSONSchema`

              The type of the object. Always `json_schema`.

              - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

        - `Verbosity AgentTextVerbosity`

          The amount of text produced by the agent. Defaults to `medium`.

          - `const AgentTextVerbosityLow AgentTextVerbosity = "low"`

          - `const AgentTextVerbosityMedium AgentTextVerbosity = "medium"`

          - `const AgentTextVerbosityHigh AgentTextVerbosity = "high"`

      - `Tools []AgentToolUnion`

        Configured tools, excluding confidential credentials.

        `minItems: 0`, `maxItems: 2000`

        - `type AgentToolFunction struct{…}`

          A function defined by the application.

          - `DeferLoading bool`

            Whether the function is deferred and discovered through tool search.

          - `Description string`

            A description of what the function does.

            `minLength: 0`

          - `Name string`

            The name of the function.

            `minLength: 0`

          - `Parameters map[string, any]`

            A JSON Schema object describing the function's arguments.

          - `Type Function`

            The type of the object. Always `function`.

            - `const FunctionFunction Function = "function"`

          - `Async bool`

            Whether the agent continues without waiting for the function result.

        - `type AgentToolProgrammaticToolCalling struct{…}`

          Enables calling tools from model-generated code.

          - `Enabled bool`

            Whether tools can be called from model-generated code.

          - `Type ProgrammaticToolCalling`

            The type of the object. Always `programmatic_tool_calling`.

            - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

        - `type AgentToolMcp struct{…}`

          Tools provided by a remote MCP server.

          - `AllowedTools []string`

            The MCP tools the agent may call.

            `minItems: 0`, `maxItems: 2000`

          - `ConnectionOrigin string`

            Where outbound MCP HTTP connections originate.

            - `const AgentToolMcpConnectionOriginService AgentToolMcpConnectionOrigin = "service"`

            - `const AgentToolMcpConnectionOriginEnvironment AgentToolMcpConnectionOrigin = "environment"`

          - `CredentialID string`

            The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

            `minLength: 0`

          - `RequestMetadata map[string, any]`

            Metadata included with requests to this MCP server.

          - `Required bool`

            Whether this MCP server must initialize before the first turn.

          - `ServerLabel string`

            A label used to identify the MCP server in tool calls.

            `minLength: 0`

          - `Transport McpTransportUnion`

            The transport used to connect to the MCP server.

            - `type McpTransportHTTP struct{…}`

              Connects to an MCP server over HTTP.

              - `ServerURL string`

                The URL of the MCP server.

                `minLength: 0`

              - `Type HTTP`

                The type of the object. Always `http`.

                - `const HTTPHTTP HTTP = "http"`

            - `type McpTransportStdio struct{…}`

              Starts an MCP server as a local process.

              - `Args []string`

                Arguments passed to the MCP server command.

                `minItems: 0`, `maxItems: 2000`

              - `Command string`

                The command used to start the MCP server.

                `minLength: 0`

              - `Cwd string`

                The working directory used to start the MCP server.

                `minLength: 0`

              - `EnvVars []string`

                Environment variable names inherited from the execution environment.

                `minItems: 0`, `maxItems: 2000`

              - `Type Stdio`

                The type of the object. Always `stdio`.

                - `const StdioStdio Stdio = "stdio"`

          - `Type Mcp`

            The type of the object. Always `mcp`.

            - `const McpMcp Mcp = "mcp"`

        - `type AgentToolWebSearch struct{…}`

          Web search.

          - `AllowedDomains []string`

            Allowed search domains, or `null` when the search is unrestricted.

            `minItems: 0`, `maxItems: 2000`

          - `ContextSize string`

            The amount of search context made available to the model. Defaults to `medium`.

            - `const AgentToolWebSearchContextSizeLow AgentToolWebSearchContextSize = "low"`

            - `const AgentToolWebSearchContextSizeMedium AgentToolWebSearchContextSize = "medium"`

            - `const AgentToolWebSearchContextSizeHigh AgentToolWebSearchContextSize = "high"`

          - `Location AgentToolWebSearchLocation`

            Approximate location used to localize search results, if provided.

            - `City string`

              The city name.

              `minLength: 0`

            - `Country string`

              The two-letter ISO country code, such as `US`.

              `minLength: 0`

            - `Region string`

              The region or state name.

              `minLength: 0`

            - `Timezone string`

              The IANA timezone, such as `America/Los_Angeles`.

              `minLength: 0`

          - `Mode string`

            The source used for web search results.

            - `const AgentToolWebSearchModeDisabled AgentToolWebSearchMode = "disabled"`

            - `const AgentToolWebSearchModeCached AgentToolWebSearchMode = "cached"`

            - `const AgentToolWebSearchModeLive AgentToolWebSearchMode = "live"`

          - `Type WebSearch`

            The type of the object. Always `web_search`.

            - `const WebSearchWebSearch WebSearch = "web_search"`

        - `type AgentToolComputerUse struct{…}`

          Browser use in an OpenAI-hosted session.

          - `IncludeScreenshots bool`

            Whether computer tool outputs include screenshots.

          - `Type ComputerUse`

            The type of the object. Always `computer_use`.

            - `const ComputerUseComputerUse ComputerUse = "computer_use"`

        - `type AgentToolAutomations struct{…}`

          Lets the agent manage its own scheduled wakeups.

          - `Type Automations`

            The type of the object. Always `automations`.

            - `const AutomationsAutomations Automations = "automations"`

      - `Compaction AutomationAgentConfigCompaction`

        The effective context compaction settings.

        - `Async bool`

          Whether context is compacted in the background. Defaults to true.

      - `Experimental AutomationAgentConfigExperimental`

        The effective experimental settings for the agent.

        - `TimeAwareness bool`

          Whether the model receives periodic current-time reminders.

    - `AgentID string`

      The saved agent reference, or null when an inline agent is configured.

      `minLength: 0`

    - `Environment AutomationEnvironmentUnion`

      Configuration or references used to select the execution environment.

      - `type AutomationEnvironmentNone struct{…}`

        - `Type None`

          The type of the object. Always `none`.

          - `const NoneNone None = "none"`

      - `type AutomationEnvironmentOpenAIHosted struct{…}`

        Hosted environment selection with confidential setup commands and variables omitted.

        - `CapabilityDirectories []string`

          Directory overrides, or null to inherit the template or creation default.

          `minItems: 0`, `maxItems: 2000`

        - `ContainerSize string`

          The configured container size, or null to use the creation default.

          - `const AutomationEnvironmentOpenAIHostedContainerSizeSmall AutomationEnvironmentOpenAIHostedContainerSize = "small"`

          - `const AutomationEnvironmentOpenAIHostedContainerSizeMedium AutomationEnvironmentOpenAIHostedContainerSize = "medium"`

          - `const AutomationEnvironmentOpenAIHostedContainerSizeLarge AutomationEnvironmentOpenAIHostedContainerSize = "large"`

        - `Desktop AutomationEnvironmentOpenAIHostedDesktop`

          Desktop overrides, or null to inherit the template or creation default.

          - `Enabled bool`

            Whether the environment provisions a desktop and browser proxy.

        - `EnvironmentID string`

          An existing environment reference, or null when provisioning a new environment.

          `minLength: 0`

        - `EnvironmentTemplateID string`

          A template reference, or null when no template is selected.

          `minLength: 0`

        - `Files []AutomationEnvironmentOpenAIHostedFileUnion`

          File overrides, excluding contents, or null to inherit.

          `minItems: 0`, `maxItems: 2000`

          - `type AutomationEnvironmentOpenAIHostedFileFileID struct{…}`

            A project-scoped Files API reference resolved separately for each session.

            - `FileID string`

              The ID of the uploaded file.

              `minLength: 0`

            - `Path string`

              The file's absolute path inside the environment.

              `minLength: 0`

            - `Type FileID`

              The type of the object. Always `file_id`.

              - `const FileIDFileID FileID = "file_id"`

          - `type AutomationEnvironmentOpenAIHostedFileInline struct{…}`

            Metadata for confidential inline file contents.

            - `Path string`

              The file's absolute path inside the environment.

              `minLength: 0`

            - `SizeBytes int64`

              The decoded size of the inline file in bytes.

              `format: int64`, `minimum: 0`

            - `Type Inline`

              The type of the object. Always `inline`.

              - `const InlineInline Inline = "inline"`

        - `Network AutomationEnvironmentOpenAIHostedNetwork`

          Network overrides, or null to inherit the template or creation default.

          - `Access string`

            The environment's network access mode.

            - `const AutomationEnvironmentOpenAIHostedNetworkAccessEnabled AutomationEnvironmentOpenAIHostedNetworkAccess = "enabled"`

              Allows unrestricted network access.

            - `const AutomationEnvironmentOpenAIHostedNetworkAccessDisabled AutomationEnvironmentOpenAIHostedNetworkAccess = "disabled"`

              Disables network access.

            - `const AutomationEnvironmentOpenAIHostedNetworkAccessRestricted AutomationEnvironmentOpenAIHostedNetworkAccess = "restricted"`

              Applies the configured domain restrictions.

          - `AllowedDomains []string`

            Domains the environment may access when network access is restricted.

            `minItems: 0`, `maxItems: 2000`

        - `Packages AutomationEnvironmentOpenAIHostedPackages`

          Package overrides, or null to inherit the template or creation default.

          - `Npm []string`

            npm packages installed globally in the environment.

            `minItems: 0`, `maxItems: 16384`

          - `Python []string`

            Python packages installed in the environment.

            `minItems: 0`, `maxItems: 16384`

          - `System []string`

            System packages installed in the environment.

            `minItems: 0`, `maxItems: 16384`

        - `Plugins []HostedPlugin`

          Plugin overrides, excluding archive contents, or null to inherit.

          `minItems: 0`, `maxItems: 2000`

          - `Description string`

            The installed plugin description.

            `minLength: 0`

          - `Name string`

            The installed plugin name.

            `minLength: 0`

          - `Type Inline`

            The type of the object. Always `inline`.

            - `const InlineInline Inline = "inline"`

        - `Skills []AutomationEnvironmentOpenAIHostedSkillUnion`

          Skill overrides, excluding archive contents, or null to inherit.

          `minItems: 0`, `maxItems: 2000`

          - `type AutomationEnvironmentOpenAIHostedSkillSkillReference struct{…}`

            A skill resolved afresh from the Skills API whenever a session starts.

            - `SkillID string`

              The referenced skill ID.

              `minLength: 0`

            - `Type SkillReference`

              The type of the object. Always `skill_reference`.

              - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

            - `Version string`

              The requested version selector, including `latest`.

              `minLength: 0`

          - `type AutomationEnvironmentOpenAIHostedSkillInline struct{…}`

            Safe metadata for an inline skill archive.

            - `Description string`

              The skill description declared in `SKILL.md`.

              `minLength: 0`

            - `Name string`

              The skill name declared in `SKILL.md`.

              `minLength: 0`

            - `Type Inline`

              The type of the object. Always `inline`.

              - `const InlineInline Inline = "inline"`

        - `Type OpenAIHosted`

          The type of the object. Always `openai_hosted`.

          - `const OpenAIHostedOpenAIHosted OpenAIHosted = "openai_hosted"`

      - `type AutomationEnvironmentSelfHosted struct{…}`

        - `CapabilityDirectories []string`

          Directories that expose capabilities to the agent.

          `minItems: 0`, `maxItems: 2000`

        - `EnvironmentID string`

          An existing registration, or null to create a session-owned environment.

          `minLength: 0`

        - `Type SelfHosted`

          The type of the object. Always `self_hosted`.

          - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

        - `WorkspaceDirectory string`

          The absolute project directory in the environment.

          `minLength: 0`

    - `Input []AutomationTargetNewSessionInput`

      Initial input delivered to each new session.

      `minItems: 0`, `maxItems: 2000`

      - `Content []InputContentUnion`

        The content of the message.

        `minItems: 0`, `maxItems: 2000`

        - `type InputContentInputText struct{…}`

          Text input recorded in a session item.

          - `Text string`

            The text supplied to the agent.

            `minLength: 0`

          - `Type InputText`

            The type of the object. Always `input_text`.

            - `const InputTextInputText InputText = "input_text"`

        - `type InputContentInputImage struct{…}`

          Image input recorded in a session item.

          - `ImageURL string`

            The URL of the image supplied to the agent, which may be a base64-encoded data URL.

            `minLength: 0`

          - `Type InputImage`

            The type of the object. Always `input_image`.

            - `const InputImageInputImage InputImage = "input_image"`

      - `Role User`

        The role of the message author. Always `user`.

        - `const UserUser User = "user"`

      - `Type Message`

        The type of the input item. Always `message`.

        - `const MessageMessage Message = "message"`

    - `Metadata map[string, string]`

      Metadata attached to each new session.

    - `Type NewSession`

      The type of the object. Always `new_session`.

      - `const NewSessionNewSession NewSession = "new_session"`

    - `VaultIDs []string`

      Vaults made available to each new session.

      `minItems: 0`, `maxItems: 2000`

  - `type AutomationTargetExistingSession struct{…}`

    - `Instructions string`

      Saved instructions delivered as an automation notification.

      `minLength: 0`

    - `SessionID string`

      The session receiving each invocation.

      `minLength: 0`

    - `Type ExistingSession`

      The type of the object. Always `existing_session`.

      - `const ExistingSessionExistingSession ExistingSession = "existing_session"`

### Automation Target Param

- `type AutomationTargetParamUnionResp interface{…}`

  The session an automation invocation targets.

  - `AutomationTargetParamNewSessionResp`

    - `Environment EnvironmentParamUnionResp`

      The execution environment for each new session.

      - `EnvironmentParamNoneResp`

        - `Type None`

          The type of the object. Always `none`.

          - `const NoneNone None = "none"`

      - `EnvironmentParamOpenAIHostedResp`

        - `Type OpenAIHosted`

          The type of the object. Always `openai_hosted`.

          - `const OpenAIHostedOpenAIHosted OpenAIHosted = "openai_hosted"`

        - `CapabilityDirectories []string`

          Directories that contain capabilities exposed to the agent. Defaults to an empty list.

          `minItems: 0`, `maxItems: 16384`

        - `ContainerSize string`

          The hosted container size. Omission selects the medium tier.

          - `const EnvironmentParamOpenAIHostedContainerSizeSmall EnvironmentParamOpenAIHostedContainerSize = "small"`

          - `const EnvironmentParamOpenAIHostedContainerSizeMedium EnvironmentParamOpenAIHostedContainerSize = "medium"`

          - `const EnvironmentParamOpenAIHostedContainerSizeLarge EnvironmentParamOpenAIHostedContainerSize = "large"`

        - `Desktop EnvironmentParamOpenAIHostedDesktopResp`

          Desktop provisioning. Omission or null inherits the template setting, or defaults to disabled.

          - `Enabled bool`

            Whether to provision the desktop and its browser proxy.

        - `Env map[string, string]`

          Environment variables made available to the agent.

        - `EnvironmentID string`

          An existing prewarmed environment. Cannot be combined with a template or inline configuration.

          `minLength: 9`, `maxLength: 256`

        - `EnvironmentTemplateID string`

          A reusable hosted template applied before inline session configuration. Omitted fields inherit the template; network overrides cannot broaden its policy.

          `minLength: 0`, `maxLength: 64`

        - `Files []HostedEnvironmentFileParamUnionResp`

          Files available before the agent starts. Defaults to an empty list.

          `minItems: 0`, `maxItems: 50`

          - `HostedEnvironmentFileParamFileIDResp`

            - `FileID string`

              The ID of the uploaded file.

              `minLength: 1`, `maxLength: 256`

            - `Path string`

              The absolute destination path inside `/workspace`.

              `minLength: 1`, `maxLength: 4096`

            - `Type FileID`

              The type of the object. Always `file_id`.

              - `const FileIDFileID FileID = "file_id"`

          - `HostedEnvironmentFileParamInlineResp`

            - `Data string`

              The standard-base64-encoded file contents.

              `minLength: 0`, `maxLength: 6990508`

            - `Path string`

              The absolute destination path inside `/workspace`.

              `minLength: 1`, `maxLength: 4096`

            - `Type Inline`

              The type of the object. Always `inline`.

              - `const InlineInline Inline = "inline"`

        - `Network EnvironmentParamOpenAIHostedNetworkResp`

          Network access policy for the environment. If omitted, the API version determines whether network access is enabled or disabled.

          - `Access string`

            The environment's network access mode.

            - `const EnvironmentParamOpenAIHostedNetworkAccessEnabled EnvironmentParamOpenAIHostedNetworkAccess = "enabled"`

              Allows unrestricted network access.

            - `const EnvironmentParamOpenAIHostedNetworkAccessDisabled EnvironmentParamOpenAIHostedNetworkAccess = "disabled"`

              Disables network access.

            - `const EnvironmentParamOpenAIHostedNetworkAccessRestricted EnvironmentParamOpenAIHostedNetworkAccess = "restricted"`

              Applies the configured domain restrictions.

          - `AllowedDomains []string`

            Domains the environment may access when network access is restricted.

            `minItems: 0`, `maxItems: 16384`

          - `BlockedDomains []string`

            Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

            `minItems: 0`, `maxItems: 100`

        - `Packages EnvironmentParamOpenAIHostedPackagesResp`

          Packages to install in the environment. Defaults to empty package lists.

          - `Npm []string`

            npm packages to install globally. Defaults to an empty list.

            `minItems: 0`, `maxItems: 16384`

          - `Python []string`

            Python packages to install. Defaults to an empty list.

            `minItems: 0`, `maxItems: 16384`

          - `System []string`

            System packages to install. Defaults to an empty list.

            `minItems: 0`, `maxItems: 16384`

        - `Plugins []HostedPluginParamResp`

          Plugins provided as inline ZIP archives. Defaults to an empty list.

          `minItems: 0`, `maxItems: 32`

          - `Description string`

            The plugin description declared in `.codex-plugin/plugin.json`.

            `minLength: 0`, `maxLength: 1048576`

          - `Name string`

            The plugin name declared in `.codex-plugin/plugin.json`.

            `minLength: 1`, `maxLength: 64`

          - `Source InlineCapabilitySourceParamResp`

            Provides ZIP bytes encoded with standard base64.

            - `Data string`

              Standard-base64 encoded ZIP archive bytes.

              `minLength: 1`, `maxLength: 70254592`

            - `MediaType ApplicationZip`

              The archive media type, always `application/zip`.

              - `const ApplicationZipApplicationZip ApplicationZip = "application/zip"`

            - `Type Base64`

              The type of the object. Always `base64`.

              - `const Base64Base64 Base64 = "base64"`

          - `Type Inline`

            The type of the object. Always `inline`.

            - `const InlineInline Inline = "inline"`

        - `SetupCommands []SetupCommandParamResp`

          Ordered, confidential setup commands. Command bodies are never returned.

          `minItems: 0`, `maxItems: 16`

          - `Command string`

            The shell command to execute.

            `minLength: 0`, `maxLength: 65536`

          - `Cwd string`

            The absolute working directory. Defaults to `/workspace`.

            `minLength: 0`, `maxLength: 4096`

        - `Skills []HostedSkillParamUnionResp`

          Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

          `minItems: 0`, `maxItems: 200`

          - `HostedSkillParamSkillReferenceResp`

            - `SkillID string`

              The ID of the skill created through `/v1/skills`.

              `minLength: 1`, `maxLength: 64`

            - `Type SkillReference`

              The type of the object. Always `skill_reference`.

              - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

            - `Version string`

              The skill version, a positive integer or `latest`; omission selects the default.

              `minLength: 0`, `maxLength: 1048576`

          - `HostedSkillParamInlineResp`

            - `Description string`

              The skill description declared in `SKILL.md`.

              `minLength: 0`, `maxLength: 1048576`

            - `Name string`

              The skill name declared in `SKILL.md`.

              `minLength: 1`, `maxLength: 64`

            - `Source InlineCapabilitySourceParamResp`

              Provides ZIP bytes encoded with standard base64.

            - `Type Inline`

              The type of the object. Always `inline`.

              - `const InlineInline Inline = "inline"`

      - `EnvironmentParamSelfHostedResp`

        - `Type SelfHosted`

          The type of the object. Always `self_hosted`.

          - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

        - `WorkspaceDirectory string`

          Absolute project directory inside the self-hosted environment.

          `minLength: 0`, `maxLength: 1048576`

        - `CapabilityDirectories []string`

          Directories that contain capabilities exposed to the agent. Defaults to an empty list.

          `minItems: 0`, `maxItems: 16384`

    - `Input []AgentSessionInputMessageParamResp`

      Initial user messages submitted with each new session.

      `minItems: 0`, `maxItems: 16384`

      - `Content []InputContentParamUnionResp`

        The content of the message.

        `minItems: 0`, `maxItems: 16384`

        - `InputContentParamInputTextResp`

          - `Text string`

            The text sent to the model.

            `minLength: 0`, `maxLength: 1048576`

          - `Type InputText`

            The type of the object. Always `input_text`.

            - `const InputTextInputText InputText = "input_text"`

        - `InputContentParamInputImageResp`

          - `ImageURL string`

            The URL of the image sent to the model.

            `minLength: 0`, `maxLength: 1048576`

          - `Type InputImage`

            The type of the object. Always `input_image`.

            - `const InputImageInputImage InputImage = "input_image"`

      - `Role User`

        The role of the message author. Always `user`.

        - `const UserUser User = "user"`

      - `Type AgentSessionInputMessageParamType`

        The type of the input item. Always `message`.

        - `const AgentSessionInputMessageParamTypeMessage AgentSessionInputMessageParamType = "message"`

    - `Type NewSession`

      The type of the object. Always `new_session`.

      - `const NewSessionNewSession NewSession = "new_session"`

    - `Agent AutomationTargetParamNewSessionAgentResp`

      Inline agent configuration. Provide exactly one of agent and agent_id.

      - `Compaction AutomationTargetParamNewSessionAgentCompactionResp`

        Context compaction settings. Omit to keep the current settings. A supplied object replaces the settings; null or an empty object enables background compaction.

        - `Async bool`

          Whether to compact context in the background. Omission or null defaults to true. Set to false to use blocking compaction. Background compaction may increase token usage.

      - `Experimental AutomationTargetParamNewSessionAgentExperimentalResp`

        Experimental settings to merge by key. Omitted settings keep their current values.

        - `TimeAwareness bool`

          Whether to give the model periodic current-time reminders. Omit to keep the current setting.

      - `Instructions string`

        Additional instructions appended to the agent's default base instructions. Omit to leave unchanged.

        `minLength: 0`, `maxLength: 1048576`

      - `Model string`

        The model to use for the agent. The requested model name is preserved.

        `minLength: 0`, `maxLength: 1048576`

      - `MultiAgent MultiAgentConfigParamResp`

        Configuration for creating and coordinating subagents.

        - `Enabled bool`

          Whether subagent tools are enabled.

        - `MaxConcurrentSubagents int64`

          Maximum number of subagents that may run concurrently. Defaults to 6.

          `format: int64`, `minimum: 1`, `maximum: 4294967295`

      - `Reasoning AgentReasoningParamResp`

        Configuration for model reasoning. Omit to keep the current settings; pass `null` to reset to the model's default effort.

        - `Effort AgentReasoningParamEffort`

          The amount of reasoning effort the model should use. Omission lets the model select it.

          - `const AgentReasoningParamEffortNone AgentReasoningParamEffort = "none"`

          - `const AgentReasoningParamEffortMinimal AgentReasoningParamEffort = "minimal"`

          - `const AgentReasoningParamEffortLow AgentReasoningParamEffort = "low"`

          - `const AgentReasoningParamEffortMedium AgentReasoningParamEffort = "medium"`

          - `const AgentReasoningParamEffortHigh AgentReasoningParamEffort = "high"`

          - `const AgentReasoningParamEffortXhigh AgentReasoningParamEffort = "xhigh"`

          - `const AgentReasoningParamEffortMax AgentReasoningParamEffort = "max"`

        - `Summary AgentReasoningParamSummary`

          Controls whether the response includes a reasoning summary.

          - `const AgentReasoningParamSummaryConcise AgentReasoningParamSummary = "concise"`

            Returns a concise reasoning summary when supported.

          - `const AgentReasoningParamSummaryDetailed AgentReasoningParamSummary = "detailed"`

            Returns a detailed reasoning summary when supported.

          - `const AgentReasoningParamSummaryAuto AgentReasoningParamSummary = "auto"`

            Automatically selects the most detailed summary supported by the model.

      - `ServiceTier string`

        The service tier used for model requests.

        - `const AutomationTargetParamNewSessionAgentServiceTierAuto AutomationTargetParamNewSessionAgentServiceTier = "auto"`

          Selects the service tier automatically.

        - `const AutomationTargetParamNewSessionAgentServiceTierDefault AutomationTargetParamNewSessionAgentServiceTier = "default"`

          Uses the default service tier.

        - `const AutomationTargetParamNewSessionAgentServiceTierFlex AutomationTargetParamNewSessionAgentServiceTier = "flex"`

          Uses the flex service tier.

        - `const AutomationTargetParamNewSessionAgentServiceTierPriority AutomationTargetParamNewSessionAgentServiceTier = "priority"`

          Uses the priority service tier.

        - `const AutomationTargetParamNewSessionAgentServiceTierFast AutomationTargetParamNewSessionAgentServiceTier = "fast"`

          Uses the fast service tier.

        - `const AutomationTargetParamNewSessionAgentServiceTierUltrafast AutomationTargetParamNewSessionAgentServiceTier = "ultrafast"`

          Uses the ultrafast service tier.

      - `Text AgentTextParamResp`

        Configuration for text generated by the agent.

        - `Format TextFormatParamUnionResp`

          The output format. Omission uses ordinary text (`{"type": "text"}`).

          - `TextFormatParamTextResp`

            - `Type Text`

              The type of the object. Always `text`.

              - `const TextText Text = "text"`

          - `TextFormatParamJSONSchemaResp`

            - `Schema map[string, any]`

              The JSON Schema that generated text must match.

            - `Type JSONSchema`

              The type of the object. Always `json_schema`.

              - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

        - `Verbosity AgentTextParamVerbosity`

          The amount of text the model should produce. Defaults to `medium`, matching Responses.

          - `const AgentTextParamVerbosityLow AgentTextParamVerbosity = "low"`

            Produces less text.

          - `const AgentTextParamVerbosityMedium AgentTextParamVerbosity = "medium"`

            Uses the default amount of text.

          - `const AgentTextParamVerbosityHigh AgentTextParamVerbosity = "high"`

            Produces more text.

      - `Tools []AgentToolParamUnionResp`

        Tools available to the agent. Omit to inherit, or pass null to clear them. The resolved tool list must fit within 3 MiB (3,145,728 bytes) of compact UTF-8 JSON.

        `minItems: 0`, `maxItems: 16384`

        - `AgentToolParamFunctionResp`

          - `Description string`

            A description of what the function does.

            `minLength: 0`, `maxLength: 1048576`

          - `Name string`

            The name of the function.

            `minLength: 0`, `maxLength: 1048576`

          - `Parameters map[string, any]`

            A JSON Schema object describing the function's arguments.

          - `Type Function`

            The type of the object. Always `function`.

            - `const FunctionFunction Function = "function"`

          - `Async bool`

            Whether the agent continues without waiting for the function result. Defaults to `false`.

          - `DeferLoading bool`

            Whether this function is deferred and discovered through tool search. Defaults to `false`.

        - `AgentToolParamToolSearchResp`

          - `Type ToolSearch`

            The type of the object. Always `tool_search`.

            - `const ToolSearchToolSearch ToolSearch = "tool_search"`

        - `AgentToolParamProgrammaticToolCallingResp`

          - `Type ProgrammaticToolCalling`

            The type of the object. Always `programmatic_tool_calling`.

            - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

          - `Enabled bool`

            Whether tools can be called from model-generated code. Defaults to `true`.

        - `AgentToolParamMcpResp`

          - `ServerLabel string`

            A label used to identify the MCP server in tool calls.

            `minLength: 0`, `maxLength: 1048576`

          - `Transport McpTransportParamUnionResp`

            The transport used to connect to the MCP server.

            - `McpTransportParamHTTPResp`

              - `ServerURL string`

                The URL of the MCP server.

                `minLength: 0`, `maxLength: 1048576`

              - `Type HTTP`

                The type of the object. Always `http`.

                - `const HTTPHTTP HTTP = "http"`

              - `Authorization string`

                The authorization value sent to the MCP server, if any.

                `minLength: 0`, `maxLength: 1048576`

              - `Headers map[string, string]`

                Additional HTTP headers sent to the MCP server.

            - `McpTransportParamStdioResp`

              - `Command string`

                The command used to start the MCP server.

                `minLength: 0`, `maxLength: 1048576`

              - `Cwd string`

                The working directory used to start the MCP server.

                `minLength: 0`, `maxLength: 1048576`

              - `Type Stdio`

                The type of the object. Always `stdio`.

                - `const StdioStdio Stdio = "stdio"`

              - `Args []string`

                Arguments passed to the MCP server command.

                `minItems: 0`, `maxItems: 16384`

              - `Env map[string, string]`

                Environment variables set for the MCP server process.

              - `EnvVars []string`

                Environment variable names to inherit from the selected execution environment.

                `minItems: 0`, `maxItems: 16384`

          - `Type Mcp`

            The type of the object. Always `mcp`.

            - `const McpMcp Mcp = "mcp"`

          - `AllowedTools []string`

            The MCP tools the agent may call. All server tools are allowed when omitted.

            `minItems: 0`, `maxItems: 16384`

          - `ConnectionOrigin string`

            Selects where outbound MCP HTTP connections originate. Omitted or `service` uses the Managed Agents service network; `environment` uses the session's selected environment.

            - `const AgentToolParamMcpConnectionOriginService AgentToolParamMcpConnectionOrigin = "service"`

              Uses the Managed Agents service network.

            - `const AgentToolParamMcpConnectionOriginEnvironment AgentToolParamMcpConnectionOrigin = "environment"`

              Uses the session's execution environment.

          - `CredentialID string`

            The attached vault credential used to authenticate this MCP server. Optional when exactly one attached credential matches the server URL.

            `minLength: 0`, `maxLength: 1048576`

          - `RequestMetadata map[string, any]`

            Metadata included with requests to this MCP server.

          - `Required bool`

            Whether this MCP server must initialize before the first turn. Defaults to `false`.

        - `AgentToolParamWebSearchResp`

          - `Type WebSearch`

            The type of the object. Always `web_search`.

            - `const WebSearchWebSearch WebSearch = "web_search"`

          - `AllowedDomains []string`

            Domains the search may include.

            `minItems: 0`, `maxItems: 16384`

          - `ContextSize string`

            The amount of search context made available to the model. Defaults to `medium`.

            - `const AgentToolParamWebSearchContextSizeLow AgentToolParamWebSearchContextSize = "low"`

            - `const AgentToolParamWebSearchContextSizeMedium AgentToolParamWebSearchContextSize = "medium"`

            - `const AgentToolParamWebSearchContextSizeHigh AgentToolParamWebSearchContextSize = "high"`

          - `Location AgentToolParamWebSearchLocationResp`

            Approximate location used to localize search results.

            - `City string`

              The city name.

              `minLength: 0`, `maxLength: 1048576`

            - `Country string`

              The two-letter ISO country code, such as `US`.

              `minLength: 0`, `maxLength: 1048576`

            - `Region string`

              The region or state name.

              `minLength: 0`, `maxLength: 1048576`

            - `Timezone string`

              The IANA timezone, such as `America/Los_Angeles`.

              `minLength: 0`, `maxLength: 1048576`

          - `Mode string`

            The source used for web search results. Defaults to `live`.

            - `const AgentToolParamWebSearchModeDisabled AgentToolParamWebSearchMode = "disabled"`

              Disables web search.

            - `const AgentToolParamWebSearchModeCached AgentToolParamWebSearchMode = "cached"`

              Uses cached search results.

            - `const AgentToolParamWebSearchModeLive AgentToolParamWebSearchMode = "live"`

              Searches the live web.

        - `AgentToolParamComputerUseResp`

          - `Type ComputerUse`

            The type of the object. Always `computer_use`.

            - `const ComputerUseComputerUse ComputerUse = "computer_use"`

          - `IncludeScreenshots bool`

            Whether computer tool outputs include screenshots. Defaults to `false`.

        - `AgentToolParamAutomationsResp`

          - `Type Automations`

            The type of the object. Always `automations`.

            - `const AutomationsAutomations Automations = "automations"`

    - `AgentID string`

      A saved agent ID. Provide exactly one of agent and agent_id.

      `minLength: 0`, `maxLength: 64`

    - `Metadata map[string, string]`

      Metadata attached to each new session.

    - `VaultIDs []string`

      The IDs of vaults made available to each new session.

      `minItems: 0`, `maxItems: 16384`

  - `AutomationTargetParamExistingSessionResp`

    - `Instructions string`

      Instructions delivered as an automation notification.

      `minLength: 0`, `maxLength: 1048576`

    - `SessionID string`

      The session receiving each invocation.

      `minLength: 0`, `maxLength: 1048576`

    - `Type ExistingSession`

      The type of the object. Always `existing_session`.

      - `const ExistingSessionExistingSession ExistingSession = "existing_session"`

### One Time Automation

- `type OneTimeAutomation struct{…}`

  Fields shared by periodic and one-time automations.

  - `ID string`

    The automation ID.

    `minLength: 0`

  - `CreatedAt int64`

    The creation time as a Unix timestamp in seconds.

    `format: int64`

  - `CreatedBy AutomationCreatedByUnion`

    Service-recorded provenance; callers cannot supply this field.

    - `type AutomationCreatedByDeveloper struct{…}`

      - `Type Developer`

        The type of the object. Always `developer`.

        - `const DeveloperDeveloper Developer = "developer"`

    - `type AutomationCreatedByAgent struct{…}`

      - `SessionID string`

        The creator session, which is also the automation's target.

        `minLength: 0`

      - `ToolCallID string`

        The tool call that created the automation.

        `minLength: 0`

      - `Type Agent`

        The type of the object. Always `agent`.

        - `const AgentAgent Agent = "agent"`

  - `Metadata map[string, string]`

    Custom string key-value pairs attached to the automation.

  - `Name string`

    The automation's display name.

    `minLength: 0`

  - `Object AgentAutomation`

    Always `agent.automation`.

    - `const AgentAutomationAgentAutomation AgentAutomation = "agent.automation"`

  - `RunAt int64`

    The Unix timestamp, in seconds, of the scheduled occurrence.

    `format: int64`

  - `Status OneTimeAutomationStatus`

    Completion means the schedule has finished, not the agent's work.

    - `const OneTimeAutomationStatusActive OneTimeAutomationStatus = "active"`

    - `const OneTimeAutomationStatusPaused OneTimeAutomationStatus = "paused"`

    - `const OneTimeAutomationStatusCompleted OneTimeAutomationStatus = "completed"`

  - `Target AutomationTargetUnion`

    The session configuration or existing session receiving invocations.

    - `type AutomationTargetNewSession struct{…}`

      - `Agent AutomationAgentConfig`

        The inline agent configuration, or null when agent_id is configured.

        - `Instructions string`

          Custom instructions, or null when absent.

          `minLength: 0`

        - `Model string`

          The requested model name.

          `minLength: 0`

        - `MultiAgent MultiAgentConfig`

          The configuration for creating and coordinating subagents.

          - `Enabled bool`

            Whether subagent tools are enabled. Defaults to false.

          - `MaxConcurrentSubagents int64`

            Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

            `format: int64`, `minimum: 1`, `maximum: 4294967295`

        - `Reasoning AgentReasoning`

          The configured reasoning policy.

          - `Effort AgentReasoningEffort`

            The requested reasoning effort, or `null` when the model selects its own default.

            - `const AgentReasoningEffortNone AgentReasoningEffort = "none"`

            - `const AgentReasoningEffortMinimal AgentReasoningEffort = "minimal"`

            - `const AgentReasoningEffortLow AgentReasoningEffort = "low"`

            - `const AgentReasoningEffortMedium AgentReasoningEffort = "medium"`

            - `const AgentReasoningEffortHigh AgentReasoningEffort = "high"`

            - `const AgentReasoningEffortXhigh AgentReasoningEffort = "xhigh"`

            - `const AgentReasoningEffortMax AgentReasoningEffort = "max"`

          - `Summary AgentReasoningSummary`

            The requested reasoning summary format, or `null` when summaries are disabled.

            - `const AgentReasoningSummaryConcise AgentReasoningSummary = "concise"`

              Returns a concise reasoning summary when supported.

            - `const AgentReasoningSummaryDetailed AgentReasoningSummary = "detailed"`

              Returns a detailed reasoning summary when supported.

            - `const AgentReasoningSummaryAuto AgentReasoningSummary = "auto"`

              Automatically selects the most detailed summary supported by the model.

        - `ServiceTier AutomationAgentConfigServiceTier`

          The configured service-tier policy.

          - `const AutomationAgentConfigServiceTierAuto AutomationAgentConfigServiceTier = "auto"`

          - `const AutomationAgentConfigServiceTierDefault AutomationAgentConfigServiceTier = "default"`

          - `const AutomationAgentConfigServiceTierFlex AutomationAgentConfigServiceTier = "flex"`

          - `const AutomationAgentConfigServiceTierPriority AutomationAgentConfigServiceTier = "priority"`

          - `const AutomationAgentConfigServiceTierFast AutomationAgentConfigServiceTier = "fast"`

          - `const AutomationAgentConfigServiceTierUltrafast AutomationAgentConfigServiceTier = "ultrafast"`

        - `Text AgentText`

          The configured output format and verbosity.

          - `Format TextFormatUnion`

            The effective output format. Defaults to ordinary text.

            - `type TextFormatText struct{…}`

              Generates ordinary text without a structured-output constraint.

              - `Type Text`

                The type of the object. Always `text`.

                - `const TextText Text = "text"`

            - `type TextFormatJSONSchema struct{…}`

              Constrains generated text to a JSON Schema.

              - `Schema map[string, any]`

                The JSON Schema that generated text must match.

              - `Type JSONSchema`

                The type of the object. Always `json_schema`.

                - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

          - `Verbosity AgentTextVerbosity`

            The amount of text produced by the agent. Defaults to `medium`.

            - `const AgentTextVerbosityLow AgentTextVerbosity = "low"`

            - `const AgentTextVerbosityMedium AgentTextVerbosity = "medium"`

            - `const AgentTextVerbosityHigh AgentTextVerbosity = "high"`

        - `Tools []AgentToolUnion`

          Configured tools, excluding confidential credentials.

          `minItems: 0`, `maxItems: 2000`

          - `type AgentToolFunction struct{…}`

            A function defined by the application.

            - `DeferLoading bool`

              Whether the function is deferred and discovered through tool search.

            - `Description string`

              A description of what the function does.

              `minLength: 0`

            - `Name string`

              The name of the function.

              `minLength: 0`

            - `Parameters map[string, any]`

              A JSON Schema object describing the function's arguments.

            - `Type Function`

              The type of the object. Always `function`.

              - `const FunctionFunction Function = "function"`

            - `Async bool`

              Whether the agent continues without waiting for the function result.

          - `type AgentToolProgrammaticToolCalling struct{…}`

            Enables calling tools from model-generated code.

            - `Enabled bool`

              Whether tools can be called from model-generated code.

            - `Type ProgrammaticToolCalling`

              The type of the object. Always `programmatic_tool_calling`.

              - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

          - `type AgentToolMcp struct{…}`

            Tools provided by a remote MCP server.

            - `AllowedTools []string`

              The MCP tools the agent may call.

              `minItems: 0`, `maxItems: 2000`

            - `ConnectionOrigin string`

              Where outbound MCP HTTP connections originate.

              - `const AgentToolMcpConnectionOriginService AgentToolMcpConnectionOrigin = "service"`

              - `const AgentToolMcpConnectionOriginEnvironment AgentToolMcpConnectionOrigin = "environment"`

            - `CredentialID string`

              The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

              `minLength: 0`

            - `RequestMetadata map[string, any]`

              Metadata included with requests to this MCP server.

            - `Required bool`

              Whether this MCP server must initialize before the first turn.

            - `ServerLabel string`

              A label used to identify the MCP server in tool calls.

              `minLength: 0`

            - `Transport McpTransportUnion`

              The transport used to connect to the MCP server.

              - `type McpTransportHTTP struct{…}`

                Connects to an MCP server over HTTP.

                - `ServerURL string`

                  The URL of the MCP server.

                  `minLength: 0`

                - `Type HTTP`

                  The type of the object. Always `http`.

                  - `const HTTPHTTP HTTP = "http"`

              - `type McpTransportStdio struct{…}`

                Starts an MCP server as a local process.

                - `Args []string`

                  Arguments passed to the MCP server command.

                  `minItems: 0`, `maxItems: 2000`

                - `Command string`

                  The command used to start the MCP server.

                  `minLength: 0`

                - `Cwd string`

                  The working directory used to start the MCP server.

                  `minLength: 0`

                - `EnvVars []string`

                  Environment variable names inherited from the execution environment.

                  `minItems: 0`, `maxItems: 2000`

                - `Type Stdio`

                  The type of the object. Always `stdio`.

                  - `const StdioStdio Stdio = "stdio"`

            - `Type Mcp`

              The type of the object. Always `mcp`.

              - `const McpMcp Mcp = "mcp"`

          - `type AgentToolWebSearch struct{…}`

            Web search.

            - `AllowedDomains []string`

              Allowed search domains, or `null` when the search is unrestricted.

              `minItems: 0`, `maxItems: 2000`

            - `ContextSize string`

              The amount of search context made available to the model. Defaults to `medium`.

              - `const AgentToolWebSearchContextSizeLow AgentToolWebSearchContextSize = "low"`

              - `const AgentToolWebSearchContextSizeMedium AgentToolWebSearchContextSize = "medium"`

              - `const AgentToolWebSearchContextSizeHigh AgentToolWebSearchContextSize = "high"`

            - `Location AgentToolWebSearchLocation`

              Approximate location used to localize search results, if provided.

              - `City string`

                The city name.

                `minLength: 0`

              - `Country string`

                The two-letter ISO country code, such as `US`.

                `minLength: 0`

              - `Region string`

                The region or state name.

                `minLength: 0`

              - `Timezone string`

                The IANA timezone, such as `America/Los_Angeles`.

                `minLength: 0`

            - `Mode string`

              The source used for web search results.

              - `const AgentToolWebSearchModeDisabled AgentToolWebSearchMode = "disabled"`

              - `const AgentToolWebSearchModeCached AgentToolWebSearchMode = "cached"`

              - `const AgentToolWebSearchModeLive AgentToolWebSearchMode = "live"`

            - `Type WebSearch`

              The type of the object. Always `web_search`.

              - `const WebSearchWebSearch WebSearch = "web_search"`

          - `type AgentToolComputerUse struct{…}`

            Browser use in an OpenAI-hosted session.

            - `IncludeScreenshots bool`

              Whether computer tool outputs include screenshots.

            - `Type ComputerUse`

              The type of the object. Always `computer_use`.

              - `const ComputerUseComputerUse ComputerUse = "computer_use"`

          - `type AgentToolAutomations struct{…}`

            Lets the agent manage its own scheduled wakeups.

            - `Type Automations`

              The type of the object. Always `automations`.

              - `const AutomationsAutomations Automations = "automations"`

        - `Compaction AutomationAgentConfigCompaction`

          The effective context compaction settings.

          - `Async bool`

            Whether context is compacted in the background. Defaults to true.

        - `Experimental AutomationAgentConfigExperimental`

          The effective experimental settings for the agent.

          - `TimeAwareness bool`

            Whether the model receives periodic current-time reminders.

      - `AgentID string`

        The saved agent reference, or null when an inline agent is configured.

        `minLength: 0`

      - `Environment AutomationEnvironmentUnion`

        Configuration or references used to select the execution environment.

        - `type AutomationEnvironmentNone struct{…}`

          - `Type None`

            The type of the object. Always `none`.

            - `const NoneNone None = "none"`

        - `type AutomationEnvironmentOpenAIHosted struct{…}`

          Hosted environment selection with confidential setup commands and variables omitted.

          - `CapabilityDirectories []string`

            Directory overrides, or null to inherit the template or creation default.

            `minItems: 0`, `maxItems: 2000`

          - `ContainerSize string`

            The configured container size, or null to use the creation default.

            - `const AutomationEnvironmentOpenAIHostedContainerSizeSmall AutomationEnvironmentOpenAIHostedContainerSize = "small"`

            - `const AutomationEnvironmentOpenAIHostedContainerSizeMedium AutomationEnvironmentOpenAIHostedContainerSize = "medium"`

            - `const AutomationEnvironmentOpenAIHostedContainerSizeLarge AutomationEnvironmentOpenAIHostedContainerSize = "large"`

          - `Desktop AutomationEnvironmentOpenAIHostedDesktop`

            Desktop overrides, or null to inherit the template or creation default.

            - `Enabled bool`

              Whether the environment provisions a desktop and browser proxy.

          - `EnvironmentID string`

            An existing environment reference, or null when provisioning a new environment.

            `minLength: 0`

          - `EnvironmentTemplateID string`

            A template reference, or null when no template is selected.

            `minLength: 0`

          - `Files []AutomationEnvironmentOpenAIHostedFileUnion`

            File overrides, excluding contents, or null to inherit.

            `minItems: 0`, `maxItems: 2000`

            - `type AutomationEnvironmentOpenAIHostedFileFileID struct{…}`

              A project-scoped Files API reference resolved separately for each session.

              - `FileID string`

                The ID of the uploaded file.

                `minLength: 0`

              - `Path string`

                The file's absolute path inside the environment.

                `minLength: 0`

              - `Type FileID`

                The type of the object. Always `file_id`.

                - `const FileIDFileID FileID = "file_id"`

            - `type AutomationEnvironmentOpenAIHostedFileInline struct{…}`

              Metadata for confidential inline file contents.

              - `Path string`

                The file's absolute path inside the environment.

                `minLength: 0`

              - `SizeBytes int64`

                The decoded size of the inline file in bytes.

                `format: int64`, `minimum: 0`

              - `Type Inline`

                The type of the object. Always `inline`.

                - `const InlineInline Inline = "inline"`

          - `Network AutomationEnvironmentOpenAIHostedNetwork`

            Network overrides, or null to inherit the template or creation default.

            - `Access string`

              The environment's network access mode.

              - `const AutomationEnvironmentOpenAIHostedNetworkAccessEnabled AutomationEnvironmentOpenAIHostedNetworkAccess = "enabled"`

                Allows unrestricted network access.

              - `const AutomationEnvironmentOpenAIHostedNetworkAccessDisabled AutomationEnvironmentOpenAIHostedNetworkAccess = "disabled"`

                Disables network access.

              - `const AutomationEnvironmentOpenAIHostedNetworkAccessRestricted AutomationEnvironmentOpenAIHostedNetworkAccess = "restricted"`

                Applies the configured domain restrictions.

            - `AllowedDomains []string`

              Domains the environment may access when network access is restricted.

              `minItems: 0`, `maxItems: 2000`

          - `Packages AutomationEnvironmentOpenAIHostedPackages`

            Package overrides, or null to inherit the template or creation default.

            - `Npm []string`

              npm packages installed globally in the environment.

              `minItems: 0`, `maxItems: 16384`

            - `Python []string`

              Python packages installed in the environment.

              `minItems: 0`, `maxItems: 16384`

            - `System []string`

              System packages installed in the environment.

              `minItems: 0`, `maxItems: 16384`

          - `Plugins []HostedPlugin`

            Plugin overrides, excluding archive contents, or null to inherit.

            `minItems: 0`, `maxItems: 2000`

            - `Description string`

              The installed plugin description.

              `minLength: 0`

            - `Name string`

              The installed plugin name.

              `minLength: 0`

            - `Type Inline`

              The type of the object. Always `inline`.

              - `const InlineInline Inline = "inline"`

          - `Skills []AutomationEnvironmentOpenAIHostedSkillUnion`

            Skill overrides, excluding archive contents, or null to inherit.

            `minItems: 0`, `maxItems: 2000`

            - `type AutomationEnvironmentOpenAIHostedSkillSkillReference struct{…}`

              A skill resolved afresh from the Skills API whenever a session starts.

              - `SkillID string`

                The referenced skill ID.

                `minLength: 0`

              - `Type SkillReference`

                The type of the object. Always `skill_reference`.

                - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

              - `Version string`

                The requested version selector, including `latest`.

                `minLength: 0`

            - `type AutomationEnvironmentOpenAIHostedSkillInline struct{…}`

              Safe metadata for an inline skill archive.

              - `Description string`

                The skill description declared in `SKILL.md`.

                `minLength: 0`

              - `Name string`

                The skill name declared in `SKILL.md`.

                `minLength: 0`

              - `Type Inline`

                The type of the object. Always `inline`.

                - `const InlineInline Inline = "inline"`

          - `Type OpenAIHosted`

            The type of the object. Always `openai_hosted`.

            - `const OpenAIHostedOpenAIHosted OpenAIHosted = "openai_hosted"`

        - `type AutomationEnvironmentSelfHosted struct{…}`

          - `CapabilityDirectories []string`

            Directories that expose capabilities to the agent.

            `minItems: 0`, `maxItems: 2000`

          - `EnvironmentID string`

            An existing registration, or null to create a session-owned environment.

            `minLength: 0`

          - `Type SelfHosted`

            The type of the object. Always `self_hosted`.

            - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

          - `WorkspaceDirectory string`

            The absolute project directory in the environment.

            `minLength: 0`

      - `Input []AutomationTargetNewSessionInput`

        Initial input delivered to each new session.

        `minItems: 0`, `maxItems: 2000`

        - `Content []InputContentUnion`

          The content of the message.

          `minItems: 0`, `maxItems: 2000`

          - `type InputContentInputText struct{…}`

            Text input recorded in a session item.

            - `Text string`

              The text supplied to the agent.

              `minLength: 0`

            - `Type InputText`

              The type of the object. Always `input_text`.

              - `const InputTextInputText InputText = "input_text"`

          - `type InputContentInputImage struct{…}`

            Image input recorded in a session item.

            - `ImageURL string`

              The URL of the image supplied to the agent, which may be a base64-encoded data URL.

              `minLength: 0`

            - `Type InputImage`

              The type of the object. Always `input_image`.

              - `const InputImageInputImage InputImage = "input_image"`

        - `Role User`

          The role of the message author. Always `user`.

          - `const UserUser User = "user"`

        - `Type Message`

          The type of the input item. Always `message`.

          - `const MessageMessage Message = "message"`

      - `Metadata map[string, string]`

        Metadata attached to each new session.

      - `Type NewSession`

        The type of the object. Always `new_session`.

        - `const NewSessionNewSession NewSession = "new_session"`

      - `VaultIDs []string`

        Vaults made available to each new session.

        `minItems: 0`, `maxItems: 2000`

    - `type AutomationTargetExistingSession struct{…}`

      - `Instructions string`

        Saved instructions delivered as an automation notification.

        `minLength: 0`

      - `SessionID string`

        The session receiving each invocation.

        `minLength: 0`

      - `Type ExistingSession`

        The type of the object. Always `existing_session`.

        - `const ExistingSessionExistingSession ExistingSession = "existing_session"`

  - `Type Once`

    The type of the object. Always `once`.

    - `const OnceOnce Once = "once"`

### Periodic Automation

- `type PeriodicAutomation struct{…}`

  Fields shared by periodic and one-time automations.

  - `ID string`

    The automation ID.

    `minLength: 0`

  - `CreatedAt int64`

    The creation time as a Unix timestamp in seconds.

    `format: int64`

  - `CreatedBy AutomationCreatedByUnion`

    Service-recorded provenance; callers cannot supply this field.

    - `type AutomationCreatedByDeveloper struct{…}`

      - `Type Developer`

        The type of the object. Always `developer`.

        - `const DeveloperDeveloper Developer = "developer"`

    - `type AutomationCreatedByAgent struct{…}`

      - `SessionID string`

        The creator session, which is also the automation's target.

        `minLength: 0`

      - `ToolCallID string`

        The tool call that created the automation.

        `minLength: 0`

      - `Type Agent`

        The type of the object. Always `agent`.

        - `const AgentAgent Agent = "agent"`

  - `Expression string`

    The cron expression determining scheduled occurrences.

    `minLength: 0`

  - `Metadata map[string, string]`

    Custom string key-value pairs attached to the automation.

  - `Name string`

    The automation's display name.

    `minLength: 0`

  - `Object AgentAutomation`

    Always `agent.automation`.

    - `const AgentAutomationAgentAutomation AgentAutomation = "agent.automation"`

  - `Status PeriodicAutomationStatus`

    Whether scheduled delivery is active or paused.

    - `const PeriodicAutomationStatusActive PeriodicAutomationStatus = "active"`

    - `const PeriodicAutomationStatusPaused PeriodicAutomationStatus = "paused"`

  - `Target AutomationTargetUnion`

    The session configuration or existing session receiving invocations.

    - `type AutomationTargetNewSession struct{…}`

      - `Agent AutomationAgentConfig`

        The inline agent configuration, or null when agent_id is configured.

        - `Instructions string`

          Custom instructions, or null when absent.

          `minLength: 0`

        - `Model string`

          The requested model name.

          `minLength: 0`

        - `MultiAgent MultiAgentConfig`

          The configuration for creating and coordinating subagents.

          - `Enabled bool`

            Whether subagent tools are enabled. Defaults to false.

          - `MaxConcurrentSubagents int64`

            Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

            `format: int64`, `minimum: 1`, `maximum: 4294967295`

        - `Reasoning AgentReasoning`

          The configured reasoning policy.

          - `Effort AgentReasoningEffort`

            The requested reasoning effort, or `null` when the model selects its own default.

            - `const AgentReasoningEffortNone AgentReasoningEffort = "none"`

            - `const AgentReasoningEffortMinimal AgentReasoningEffort = "minimal"`

            - `const AgentReasoningEffortLow AgentReasoningEffort = "low"`

            - `const AgentReasoningEffortMedium AgentReasoningEffort = "medium"`

            - `const AgentReasoningEffortHigh AgentReasoningEffort = "high"`

            - `const AgentReasoningEffortXhigh AgentReasoningEffort = "xhigh"`

            - `const AgentReasoningEffortMax AgentReasoningEffort = "max"`

          - `Summary AgentReasoningSummary`

            The requested reasoning summary format, or `null` when summaries are disabled.

            - `const AgentReasoningSummaryConcise AgentReasoningSummary = "concise"`

              Returns a concise reasoning summary when supported.

            - `const AgentReasoningSummaryDetailed AgentReasoningSummary = "detailed"`

              Returns a detailed reasoning summary when supported.

            - `const AgentReasoningSummaryAuto AgentReasoningSummary = "auto"`

              Automatically selects the most detailed summary supported by the model.

        - `ServiceTier AutomationAgentConfigServiceTier`

          The configured service-tier policy.

          - `const AutomationAgentConfigServiceTierAuto AutomationAgentConfigServiceTier = "auto"`

          - `const AutomationAgentConfigServiceTierDefault AutomationAgentConfigServiceTier = "default"`

          - `const AutomationAgentConfigServiceTierFlex AutomationAgentConfigServiceTier = "flex"`

          - `const AutomationAgentConfigServiceTierPriority AutomationAgentConfigServiceTier = "priority"`

          - `const AutomationAgentConfigServiceTierFast AutomationAgentConfigServiceTier = "fast"`

          - `const AutomationAgentConfigServiceTierUltrafast AutomationAgentConfigServiceTier = "ultrafast"`

        - `Text AgentText`

          The configured output format and verbosity.

          - `Format TextFormatUnion`

            The effective output format. Defaults to ordinary text.

            - `type TextFormatText struct{…}`

              Generates ordinary text without a structured-output constraint.

              - `Type Text`

                The type of the object. Always `text`.

                - `const TextText Text = "text"`

            - `type TextFormatJSONSchema struct{…}`

              Constrains generated text to a JSON Schema.

              - `Schema map[string, any]`

                The JSON Schema that generated text must match.

              - `Type JSONSchema`

                The type of the object. Always `json_schema`.

                - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

          - `Verbosity AgentTextVerbosity`

            The amount of text produced by the agent. Defaults to `medium`.

            - `const AgentTextVerbosityLow AgentTextVerbosity = "low"`

            - `const AgentTextVerbosityMedium AgentTextVerbosity = "medium"`

            - `const AgentTextVerbosityHigh AgentTextVerbosity = "high"`

        - `Tools []AgentToolUnion`

          Configured tools, excluding confidential credentials.

          `minItems: 0`, `maxItems: 2000`

          - `type AgentToolFunction struct{…}`

            A function defined by the application.

            - `DeferLoading bool`

              Whether the function is deferred and discovered through tool search.

            - `Description string`

              A description of what the function does.

              `minLength: 0`

            - `Name string`

              The name of the function.

              `minLength: 0`

            - `Parameters map[string, any]`

              A JSON Schema object describing the function's arguments.

            - `Type Function`

              The type of the object. Always `function`.

              - `const FunctionFunction Function = "function"`

            - `Async bool`

              Whether the agent continues without waiting for the function result.

          - `type AgentToolProgrammaticToolCalling struct{…}`

            Enables calling tools from model-generated code.

            - `Enabled bool`

              Whether tools can be called from model-generated code.

            - `Type ProgrammaticToolCalling`

              The type of the object. Always `programmatic_tool_calling`.

              - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

          - `type AgentToolMcp struct{…}`

            Tools provided by a remote MCP server.

            - `AllowedTools []string`

              The MCP tools the agent may call.

              `minItems: 0`, `maxItems: 2000`

            - `ConnectionOrigin string`

              Where outbound MCP HTTP connections originate.

              - `const AgentToolMcpConnectionOriginService AgentToolMcpConnectionOrigin = "service"`

              - `const AgentToolMcpConnectionOriginEnvironment AgentToolMcpConnectionOrigin = "environment"`

            - `CredentialID string`

              The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

              `minLength: 0`

            - `RequestMetadata map[string, any]`

              Metadata included with requests to this MCP server.

            - `Required bool`

              Whether this MCP server must initialize before the first turn.

            - `ServerLabel string`

              A label used to identify the MCP server in tool calls.

              `minLength: 0`

            - `Transport McpTransportUnion`

              The transport used to connect to the MCP server.

              - `type McpTransportHTTP struct{…}`

                Connects to an MCP server over HTTP.

                - `ServerURL string`

                  The URL of the MCP server.

                  `minLength: 0`

                - `Type HTTP`

                  The type of the object. Always `http`.

                  - `const HTTPHTTP HTTP = "http"`

              - `type McpTransportStdio struct{…}`

                Starts an MCP server as a local process.

                - `Args []string`

                  Arguments passed to the MCP server command.

                  `minItems: 0`, `maxItems: 2000`

                - `Command string`

                  The command used to start the MCP server.

                  `minLength: 0`

                - `Cwd string`

                  The working directory used to start the MCP server.

                  `minLength: 0`

                - `EnvVars []string`

                  Environment variable names inherited from the execution environment.

                  `minItems: 0`, `maxItems: 2000`

                - `Type Stdio`

                  The type of the object. Always `stdio`.

                  - `const StdioStdio Stdio = "stdio"`

            - `Type Mcp`

              The type of the object. Always `mcp`.

              - `const McpMcp Mcp = "mcp"`

          - `type AgentToolWebSearch struct{…}`

            Web search.

            - `AllowedDomains []string`

              Allowed search domains, or `null` when the search is unrestricted.

              `minItems: 0`, `maxItems: 2000`

            - `ContextSize string`

              The amount of search context made available to the model. Defaults to `medium`.

              - `const AgentToolWebSearchContextSizeLow AgentToolWebSearchContextSize = "low"`

              - `const AgentToolWebSearchContextSizeMedium AgentToolWebSearchContextSize = "medium"`

              - `const AgentToolWebSearchContextSizeHigh AgentToolWebSearchContextSize = "high"`

            - `Location AgentToolWebSearchLocation`

              Approximate location used to localize search results, if provided.

              - `City string`

                The city name.

                `minLength: 0`

              - `Country string`

                The two-letter ISO country code, such as `US`.

                `minLength: 0`

              - `Region string`

                The region or state name.

                `minLength: 0`

              - `Timezone string`

                The IANA timezone, such as `America/Los_Angeles`.

                `minLength: 0`

            - `Mode string`

              The source used for web search results.

              - `const AgentToolWebSearchModeDisabled AgentToolWebSearchMode = "disabled"`

              - `const AgentToolWebSearchModeCached AgentToolWebSearchMode = "cached"`

              - `const AgentToolWebSearchModeLive AgentToolWebSearchMode = "live"`

            - `Type WebSearch`

              The type of the object. Always `web_search`.

              - `const WebSearchWebSearch WebSearch = "web_search"`

          - `type AgentToolComputerUse struct{…}`

            Browser use in an OpenAI-hosted session.

            - `IncludeScreenshots bool`

              Whether computer tool outputs include screenshots.

            - `Type ComputerUse`

              The type of the object. Always `computer_use`.

              - `const ComputerUseComputerUse ComputerUse = "computer_use"`

          - `type AgentToolAutomations struct{…}`

            Lets the agent manage its own scheduled wakeups.

            - `Type Automations`

              The type of the object. Always `automations`.

              - `const AutomationsAutomations Automations = "automations"`

        - `Compaction AutomationAgentConfigCompaction`

          The effective context compaction settings.

          - `Async bool`

            Whether context is compacted in the background. Defaults to true.

        - `Experimental AutomationAgentConfigExperimental`

          The effective experimental settings for the agent.

          - `TimeAwareness bool`

            Whether the model receives periodic current-time reminders.

      - `AgentID string`

        The saved agent reference, or null when an inline agent is configured.

        `minLength: 0`

      - `Environment AutomationEnvironmentUnion`

        Configuration or references used to select the execution environment.

        - `type AutomationEnvironmentNone struct{…}`

          - `Type None`

            The type of the object. Always `none`.

            - `const NoneNone None = "none"`

        - `type AutomationEnvironmentOpenAIHosted struct{…}`

          Hosted environment selection with confidential setup commands and variables omitted.

          - `CapabilityDirectories []string`

            Directory overrides, or null to inherit the template or creation default.

            `minItems: 0`, `maxItems: 2000`

          - `ContainerSize string`

            The configured container size, or null to use the creation default.

            - `const AutomationEnvironmentOpenAIHostedContainerSizeSmall AutomationEnvironmentOpenAIHostedContainerSize = "small"`

            - `const AutomationEnvironmentOpenAIHostedContainerSizeMedium AutomationEnvironmentOpenAIHostedContainerSize = "medium"`

            - `const AutomationEnvironmentOpenAIHostedContainerSizeLarge AutomationEnvironmentOpenAIHostedContainerSize = "large"`

          - `Desktop AutomationEnvironmentOpenAIHostedDesktop`

            Desktop overrides, or null to inherit the template or creation default.

            - `Enabled bool`

              Whether the environment provisions a desktop and browser proxy.

          - `EnvironmentID string`

            An existing environment reference, or null when provisioning a new environment.

            `minLength: 0`

          - `EnvironmentTemplateID string`

            A template reference, or null when no template is selected.

            `minLength: 0`

          - `Files []AutomationEnvironmentOpenAIHostedFileUnion`

            File overrides, excluding contents, or null to inherit.

            `minItems: 0`, `maxItems: 2000`

            - `type AutomationEnvironmentOpenAIHostedFileFileID struct{…}`

              A project-scoped Files API reference resolved separately for each session.

              - `FileID string`

                The ID of the uploaded file.

                `minLength: 0`

              - `Path string`

                The file's absolute path inside the environment.

                `minLength: 0`

              - `Type FileID`

                The type of the object. Always `file_id`.

                - `const FileIDFileID FileID = "file_id"`

            - `type AutomationEnvironmentOpenAIHostedFileInline struct{…}`

              Metadata for confidential inline file contents.

              - `Path string`

                The file's absolute path inside the environment.

                `minLength: 0`

              - `SizeBytes int64`

                The decoded size of the inline file in bytes.

                `format: int64`, `minimum: 0`

              - `Type Inline`

                The type of the object. Always `inline`.

                - `const InlineInline Inline = "inline"`

          - `Network AutomationEnvironmentOpenAIHostedNetwork`

            Network overrides, or null to inherit the template or creation default.

            - `Access string`

              The environment's network access mode.

              - `const AutomationEnvironmentOpenAIHostedNetworkAccessEnabled AutomationEnvironmentOpenAIHostedNetworkAccess = "enabled"`

                Allows unrestricted network access.

              - `const AutomationEnvironmentOpenAIHostedNetworkAccessDisabled AutomationEnvironmentOpenAIHostedNetworkAccess = "disabled"`

                Disables network access.

              - `const AutomationEnvironmentOpenAIHostedNetworkAccessRestricted AutomationEnvironmentOpenAIHostedNetworkAccess = "restricted"`

                Applies the configured domain restrictions.

            - `AllowedDomains []string`

              Domains the environment may access when network access is restricted.

              `minItems: 0`, `maxItems: 2000`

          - `Packages AutomationEnvironmentOpenAIHostedPackages`

            Package overrides, or null to inherit the template or creation default.

            - `Npm []string`

              npm packages installed globally in the environment.

              `minItems: 0`, `maxItems: 16384`

            - `Python []string`

              Python packages installed in the environment.

              `minItems: 0`, `maxItems: 16384`

            - `System []string`

              System packages installed in the environment.

              `minItems: 0`, `maxItems: 16384`

          - `Plugins []HostedPlugin`

            Plugin overrides, excluding archive contents, or null to inherit.

            `minItems: 0`, `maxItems: 2000`

            - `Description string`

              The installed plugin description.

              `minLength: 0`

            - `Name string`

              The installed plugin name.

              `minLength: 0`

            - `Type Inline`

              The type of the object. Always `inline`.

              - `const InlineInline Inline = "inline"`

          - `Skills []AutomationEnvironmentOpenAIHostedSkillUnion`

            Skill overrides, excluding archive contents, or null to inherit.

            `minItems: 0`, `maxItems: 2000`

            - `type AutomationEnvironmentOpenAIHostedSkillSkillReference struct{…}`

              A skill resolved afresh from the Skills API whenever a session starts.

              - `SkillID string`

                The referenced skill ID.

                `minLength: 0`

              - `Type SkillReference`

                The type of the object. Always `skill_reference`.

                - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

              - `Version string`

                The requested version selector, including `latest`.

                `minLength: 0`

            - `type AutomationEnvironmentOpenAIHostedSkillInline struct{…}`

              Safe metadata for an inline skill archive.

              - `Description string`

                The skill description declared in `SKILL.md`.

                `minLength: 0`

              - `Name string`

                The skill name declared in `SKILL.md`.

                `minLength: 0`

              - `Type Inline`

                The type of the object. Always `inline`.

                - `const InlineInline Inline = "inline"`

          - `Type OpenAIHosted`

            The type of the object. Always `openai_hosted`.

            - `const OpenAIHostedOpenAIHosted OpenAIHosted = "openai_hosted"`

        - `type AutomationEnvironmentSelfHosted struct{…}`

          - `CapabilityDirectories []string`

            Directories that expose capabilities to the agent.

            `minItems: 0`, `maxItems: 2000`

          - `EnvironmentID string`

            An existing registration, or null to create a session-owned environment.

            `minLength: 0`

          - `Type SelfHosted`

            The type of the object. Always `self_hosted`.

            - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

          - `WorkspaceDirectory string`

            The absolute project directory in the environment.

            `minLength: 0`

      - `Input []AutomationTargetNewSessionInput`

        Initial input delivered to each new session.

        `minItems: 0`, `maxItems: 2000`

        - `Content []InputContentUnion`

          The content of the message.

          `minItems: 0`, `maxItems: 2000`

          - `type InputContentInputText struct{…}`

            Text input recorded in a session item.

            - `Text string`

              The text supplied to the agent.

              `minLength: 0`

            - `Type InputText`

              The type of the object. Always `input_text`.

              - `const InputTextInputText InputText = "input_text"`

          - `type InputContentInputImage struct{…}`

            Image input recorded in a session item.

            - `ImageURL string`

              The URL of the image supplied to the agent, which may be a base64-encoded data URL.

              `minLength: 0`

            - `Type InputImage`

              The type of the object. Always `input_image`.

              - `const InputImageInputImage InputImage = "input_image"`

        - `Role User`

          The role of the message author. Always `user`.

          - `const UserUser User = "user"`

        - `Type Message`

          The type of the input item. Always `message`.

          - `const MessageMessage Message = "message"`

      - `Metadata map[string, string]`

        Metadata attached to each new session.

      - `Type NewSession`

        The type of the object. Always `new_session`.

        - `const NewSessionNewSession NewSession = "new_session"`

      - `VaultIDs []string`

        Vaults made available to each new session.

        `minItems: 0`, `maxItems: 2000`

    - `type AutomationTargetExistingSession struct{…}`

      - `Instructions string`

        Saved instructions delivered as an automation notification.

        `minLength: 0`

      - `SessionID string`

        The session receiving each invocation.

        `minLength: 0`

      - `Type ExistingSession`

        The type of the object. Always `existing_session`.

        - `const ExistingSessionExistingSession ExistingSession = "existing_session"`

  - `Timezone string`

    The timezone used to interpret the expression.

    `minLength: 0`

  - `Type Periodic`

    The type of the object. Always `periodic`.

    - `const PeriodicPeriodic Periodic = "periodic"`

# Invocations

## Invoke an automation

`client.Beta.Agents.Automations.Invocations.New(ctx, automationID) (*AutomationInvocation, error)`

**post** `/agents/automations/{automation_id}/invocations`

Queues a manual delivery without changing the saved schedule.

### Parameters

- `automationID string`

  `minLength: 0`, `maxLength: 1048576`

### Returns

- `type AutomationInvocation struct{…}`

  One attempted delivery by an automation.

  - `ID string`

    The invocation ID.

    `minLength: 0`

  - `AutomationID string`

    The automation that owns the invocation.

    `minLength: 0`

  - `CreatedAt int64`

    The creation time as a Unix timestamp in seconds.

    `format: int64`

  - `Error AutomationInvocationError`

    The permanent delivery failure, or null when no failure occurred.

    - `Code string`

      A machine-readable error code.

      `minLength: 0`

    - `Message string`

      A public explanation of the delivery failure.

      `minLength: 0`

  - `Object AgentAutomationInvocation`

    Always `agent.automation.invocation`.

    - `const AgentAutomationInvocationAgentAutomationInvocation AgentAutomationInvocation = "agent.automation.invocation"`

  - `ScheduledAt int64`

    The intended occurrence as a Unix timestamp in seconds, or null for manual runs.

    `format: int64`

  - `SessionID string`

    The target or newly created session ID, or null before one is available.

    `minLength: 0`

  - `SkipReason PendingDelivery`

    Why an occurrence was skipped, or null when it was not skipped.

    - `const PendingDeliveryPendingDelivery PendingDelivery = "pending_delivery"`

  - `Source AutomationInvocationSourceUnion`

    Whether the invocation was manual or scheduled.

    - `type AutomationInvocationSourceManual struct{…}`

      - `Type Manual`

        The type of the object. Always `manual`.

        - `const ManualManual Manual = "manual"`

    - `type AutomationInvocationSourceAutomation struct{…}`

      - `Automation AutomationUnion`

        The automation snapshot for this occurrence, excluding confidential values.

        - `type PeriodicAutomation struct{…}`

          Fields shared by periodic and one-time automations.

          - `ID string`

            The automation ID.

            `minLength: 0`

          - `CreatedAt int64`

            The creation time as a Unix timestamp in seconds.

            `format: int64`

          - `CreatedBy AutomationCreatedByUnion`

            Service-recorded provenance; callers cannot supply this field.

            - `type AutomationCreatedByDeveloper struct{…}`

              - `Type Developer`

                The type of the object. Always `developer`.

                - `const DeveloperDeveloper Developer = "developer"`

            - `type AutomationCreatedByAgent struct{…}`

              - `SessionID string`

                The creator session, which is also the automation's target.

                `minLength: 0`

              - `ToolCallID string`

                The tool call that created the automation.

                `minLength: 0`

              - `Type Agent`

                The type of the object. Always `agent`.

                - `const AgentAgent Agent = "agent"`

          - `Expression string`

            The cron expression determining scheduled occurrences.

            `minLength: 0`

          - `Metadata map[string, string]`

            Custom string key-value pairs attached to the automation.

          - `Name string`

            The automation's display name.

            `minLength: 0`

          - `Object AgentAutomation`

            Always `agent.automation`.

            - `const AgentAutomationAgentAutomation AgentAutomation = "agent.automation"`

          - `Status PeriodicAutomationStatus`

            Whether scheduled delivery is active or paused.

            - `const PeriodicAutomationStatusActive PeriodicAutomationStatus = "active"`

            - `const PeriodicAutomationStatusPaused PeriodicAutomationStatus = "paused"`

          - `Target AutomationTargetUnion`

            The session configuration or existing session receiving invocations.

            - `type AutomationTargetNewSession struct{…}`

              - `Agent AutomationAgentConfig`

                The inline agent configuration, or null when agent_id is configured.

                - `Instructions string`

                  Custom instructions, or null when absent.

                  `minLength: 0`

                - `Model string`

                  The requested model name.

                  `minLength: 0`

                - `MultiAgent MultiAgentConfig`

                  The configuration for creating and coordinating subagents.

                  - `Enabled bool`

                    Whether subagent tools are enabled. Defaults to false.

                  - `MaxConcurrentSubagents int64`

                    Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

                    `format: int64`, `minimum: 1`, `maximum: 4294967295`

                - `Reasoning AgentReasoning`

                  The configured reasoning policy.

                  - `Effort AgentReasoningEffort`

                    The requested reasoning effort, or `null` when the model selects its own default.

                    - `const AgentReasoningEffortNone AgentReasoningEffort = "none"`

                    - `const AgentReasoningEffortMinimal AgentReasoningEffort = "minimal"`

                    - `const AgentReasoningEffortLow AgentReasoningEffort = "low"`

                    - `const AgentReasoningEffortMedium AgentReasoningEffort = "medium"`

                    - `const AgentReasoningEffortHigh AgentReasoningEffort = "high"`

                    - `const AgentReasoningEffortXhigh AgentReasoningEffort = "xhigh"`

                    - `const AgentReasoningEffortMax AgentReasoningEffort = "max"`

                  - `Summary AgentReasoningSummary`

                    The requested reasoning summary format, or `null` when summaries are disabled.

                    - `const AgentReasoningSummaryConcise AgentReasoningSummary = "concise"`

                      Returns a concise reasoning summary when supported.

                    - `const AgentReasoningSummaryDetailed AgentReasoningSummary = "detailed"`

                      Returns a detailed reasoning summary when supported.

                    - `const AgentReasoningSummaryAuto AgentReasoningSummary = "auto"`

                      Automatically selects the most detailed summary supported by the model.

                - `ServiceTier AutomationAgentConfigServiceTier`

                  The configured service-tier policy.

                  - `const AutomationAgentConfigServiceTierAuto AutomationAgentConfigServiceTier = "auto"`

                  - `const AutomationAgentConfigServiceTierDefault AutomationAgentConfigServiceTier = "default"`

                  - `const AutomationAgentConfigServiceTierFlex AutomationAgentConfigServiceTier = "flex"`

                  - `const AutomationAgentConfigServiceTierPriority AutomationAgentConfigServiceTier = "priority"`

                  - `const AutomationAgentConfigServiceTierFast AutomationAgentConfigServiceTier = "fast"`

                  - `const AutomationAgentConfigServiceTierUltrafast AutomationAgentConfigServiceTier = "ultrafast"`

                - `Text AgentText`

                  The configured output format and verbosity.

                  - `Format TextFormatUnion`

                    The effective output format. Defaults to ordinary text.

                    - `type TextFormatText struct{…}`

                      Generates ordinary text without a structured-output constraint.

                      - `Type Text`

                        The type of the object. Always `text`.

                        - `const TextText Text = "text"`

                    - `type TextFormatJSONSchema struct{…}`

                      Constrains generated text to a JSON Schema.

                      - `Schema map[string, any]`

                        The JSON Schema that generated text must match.

                      - `Type JSONSchema`

                        The type of the object. Always `json_schema`.

                        - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

                  - `Verbosity AgentTextVerbosity`

                    The amount of text produced by the agent. Defaults to `medium`.

                    - `const AgentTextVerbosityLow AgentTextVerbosity = "low"`

                    - `const AgentTextVerbosityMedium AgentTextVerbosity = "medium"`

                    - `const AgentTextVerbosityHigh AgentTextVerbosity = "high"`

                - `Tools []AgentToolUnion`

                  Configured tools, excluding confidential credentials.

                  `minItems: 0`, `maxItems: 2000`

                  - `type AgentToolFunction struct{…}`

                    A function defined by the application.

                    - `DeferLoading bool`

                      Whether the function is deferred and discovered through tool search.

                    - `Description string`

                      A description of what the function does.

                      `minLength: 0`

                    - `Name string`

                      The name of the function.

                      `minLength: 0`

                    - `Parameters map[string, any]`

                      A JSON Schema object describing the function's arguments.

                    - `Type Function`

                      The type of the object. Always `function`.

                      - `const FunctionFunction Function = "function"`

                    - `Async bool`

                      Whether the agent continues without waiting for the function result.

                  - `type AgentToolProgrammaticToolCalling struct{…}`

                    Enables calling tools from model-generated code.

                    - `Enabled bool`

                      Whether tools can be called from model-generated code.

                    - `Type ProgrammaticToolCalling`

                      The type of the object. Always `programmatic_tool_calling`.

                      - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

                  - `type AgentToolMcp struct{…}`

                    Tools provided by a remote MCP server.

                    - `AllowedTools []string`

                      The MCP tools the agent may call.

                      `minItems: 0`, `maxItems: 2000`

                    - `ConnectionOrigin string`

                      Where outbound MCP HTTP connections originate.

                      - `const AgentToolMcpConnectionOriginService AgentToolMcpConnectionOrigin = "service"`

                      - `const AgentToolMcpConnectionOriginEnvironment AgentToolMcpConnectionOrigin = "environment"`

                    - `CredentialID string`

                      The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

                      `minLength: 0`

                    - `RequestMetadata map[string, any]`

                      Metadata included with requests to this MCP server.

                    - `Required bool`

                      Whether this MCP server must initialize before the first turn.

                    - `ServerLabel string`

                      A label used to identify the MCP server in tool calls.

                      `minLength: 0`

                    - `Transport McpTransportUnion`

                      The transport used to connect to the MCP server.

                      - `type McpTransportHTTP struct{…}`

                        Connects to an MCP server over HTTP.

                        - `ServerURL string`

                          The URL of the MCP server.

                          `minLength: 0`

                        - `Type HTTP`

                          The type of the object. Always `http`.

                          - `const HTTPHTTP HTTP = "http"`

                      - `type McpTransportStdio struct{…}`

                        Starts an MCP server as a local process.

                        - `Args []string`

                          Arguments passed to the MCP server command.

                          `minItems: 0`, `maxItems: 2000`

                        - `Command string`

                          The command used to start the MCP server.

                          `minLength: 0`

                        - `Cwd string`

                          The working directory used to start the MCP server.

                          `minLength: 0`

                        - `EnvVars []string`

                          Environment variable names inherited from the execution environment.

                          `minItems: 0`, `maxItems: 2000`

                        - `Type Stdio`

                          The type of the object. Always `stdio`.

                          - `const StdioStdio Stdio = "stdio"`

                    - `Type Mcp`

                      The type of the object. Always `mcp`.

                      - `const McpMcp Mcp = "mcp"`

                  - `type AgentToolWebSearch struct{…}`

                    Web search.

                    - `AllowedDomains []string`

                      Allowed search domains, or `null` when the search is unrestricted.

                      `minItems: 0`, `maxItems: 2000`

                    - `ContextSize string`

                      The amount of search context made available to the model. Defaults to `medium`.

                      - `const AgentToolWebSearchContextSizeLow AgentToolWebSearchContextSize = "low"`

                      - `const AgentToolWebSearchContextSizeMedium AgentToolWebSearchContextSize = "medium"`

                      - `const AgentToolWebSearchContextSizeHigh AgentToolWebSearchContextSize = "high"`

                    - `Location AgentToolWebSearchLocation`

                      Approximate location used to localize search results, if provided.

                      - `City string`

                        The city name.

                        `minLength: 0`

                      - `Country string`

                        The two-letter ISO country code, such as `US`.

                        `minLength: 0`

                      - `Region string`

                        The region or state name.

                        `minLength: 0`

                      - `Timezone string`

                        The IANA timezone, such as `America/Los_Angeles`.

                        `minLength: 0`

                    - `Mode string`

                      The source used for web search results.

                      - `const AgentToolWebSearchModeDisabled AgentToolWebSearchMode = "disabled"`

                      - `const AgentToolWebSearchModeCached AgentToolWebSearchMode = "cached"`

                      - `const AgentToolWebSearchModeLive AgentToolWebSearchMode = "live"`

                    - `Type WebSearch`

                      The type of the object. Always `web_search`.

                      - `const WebSearchWebSearch WebSearch = "web_search"`

                  - `type AgentToolComputerUse struct{…}`

                    Browser use in an OpenAI-hosted session.

                    - `IncludeScreenshots bool`

                      Whether computer tool outputs include screenshots.

                    - `Type ComputerUse`

                      The type of the object. Always `computer_use`.

                      - `const ComputerUseComputerUse ComputerUse = "computer_use"`

                  - `type AgentToolAutomations struct{…}`

                    Lets the agent manage its own scheduled wakeups.

                    - `Type Automations`

                      The type of the object. Always `automations`.

                      - `const AutomationsAutomations Automations = "automations"`

                - `Compaction AutomationAgentConfigCompaction`

                  The effective context compaction settings.

                  - `Async bool`

                    Whether context is compacted in the background. Defaults to true.

                - `Experimental AutomationAgentConfigExperimental`

                  The effective experimental settings for the agent.

                  - `TimeAwareness bool`

                    Whether the model receives periodic current-time reminders.

              - `AgentID string`

                The saved agent reference, or null when an inline agent is configured.

                `minLength: 0`

              - `Environment AutomationEnvironmentUnion`

                Configuration or references used to select the execution environment.

                - `type AutomationEnvironmentNone struct{…}`

                  - `Type None`

                    The type of the object. Always `none`.

                    - `const NoneNone None = "none"`

                - `type AutomationEnvironmentOpenAIHosted struct{…}`

                  Hosted environment selection with confidential setup commands and variables omitted.

                  - `CapabilityDirectories []string`

                    Directory overrides, or null to inherit the template or creation default.

                    `minItems: 0`, `maxItems: 2000`

                  - `ContainerSize string`

                    The configured container size, or null to use the creation default.

                    - `const AutomationEnvironmentOpenAIHostedContainerSizeSmall AutomationEnvironmentOpenAIHostedContainerSize = "small"`

                    - `const AutomationEnvironmentOpenAIHostedContainerSizeMedium AutomationEnvironmentOpenAIHostedContainerSize = "medium"`

                    - `const AutomationEnvironmentOpenAIHostedContainerSizeLarge AutomationEnvironmentOpenAIHostedContainerSize = "large"`

                  - `Desktop AutomationEnvironmentOpenAIHostedDesktop`

                    Desktop overrides, or null to inherit the template or creation default.

                    - `Enabled bool`

                      Whether the environment provisions a desktop and browser proxy.

                  - `EnvironmentID string`

                    An existing environment reference, or null when provisioning a new environment.

                    `minLength: 0`

                  - `EnvironmentTemplateID string`

                    A template reference, or null when no template is selected.

                    `minLength: 0`

                  - `Files []AutomationEnvironmentOpenAIHostedFileUnion`

                    File overrides, excluding contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `type AutomationEnvironmentOpenAIHostedFileFileID struct{…}`

                      A project-scoped Files API reference resolved separately for each session.

                      - `FileID string`

                        The ID of the uploaded file.

                        `minLength: 0`

                      - `Path string`

                        The file's absolute path inside the environment.

                        `minLength: 0`

                      - `Type FileID`

                        The type of the object. Always `file_id`.

                        - `const FileIDFileID FileID = "file_id"`

                    - `type AutomationEnvironmentOpenAIHostedFileInline struct{…}`

                      Metadata for confidential inline file contents.

                      - `Path string`

                        The file's absolute path inside the environment.

                        `minLength: 0`

                      - `SizeBytes int64`

                        The decoded size of the inline file in bytes.

                        `format: int64`, `minimum: 0`

                      - `Type Inline`

                        The type of the object. Always `inline`.

                        - `const InlineInline Inline = "inline"`

                  - `Network AutomationEnvironmentOpenAIHostedNetwork`

                    Network overrides, or null to inherit the template or creation default.

                    - `Access string`

                      The environment's network access mode.

                      - `const AutomationEnvironmentOpenAIHostedNetworkAccessEnabled AutomationEnvironmentOpenAIHostedNetworkAccess = "enabled"`

                        Allows unrestricted network access.

                      - `const AutomationEnvironmentOpenAIHostedNetworkAccessDisabled AutomationEnvironmentOpenAIHostedNetworkAccess = "disabled"`

                        Disables network access.

                      - `const AutomationEnvironmentOpenAIHostedNetworkAccessRestricted AutomationEnvironmentOpenAIHostedNetworkAccess = "restricted"`

                        Applies the configured domain restrictions.

                    - `AllowedDomains []string`

                      Domains the environment may access when network access is restricted.

                      `minItems: 0`, `maxItems: 2000`

                  - `Packages AutomationEnvironmentOpenAIHostedPackages`

                    Package overrides, or null to inherit the template or creation default.

                    - `Npm []string`

                      npm packages installed globally in the environment.

                      `minItems: 0`, `maxItems: 16384`

                    - `Python []string`

                      Python packages installed in the environment.

                      `minItems: 0`, `maxItems: 16384`

                    - `System []string`

                      System packages installed in the environment.

                      `minItems: 0`, `maxItems: 16384`

                  - `Plugins []HostedPlugin`

                    Plugin overrides, excluding archive contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `Description string`

                      The installed plugin description.

                      `minLength: 0`

                    - `Name string`

                      The installed plugin name.

                      `minLength: 0`

                    - `Type Inline`

                      The type of the object. Always `inline`.

                      - `const InlineInline Inline = "inline"`

                  - `Skills []AutomationEnvironmentOpenAIHostedSkillUnion`

                    Skill overrides, excluding archive contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `type AutomationEnvironmentOpenAIHostedSkillSkillReference struct{…}`

                      A skill resolved afresh from the Skills API whenever a session starts.

                      - `SkillID string`

                        The referenced skill ID.

                        `minLength: 0`

                      - `Type SkillReference`

                        The type of the object. Always `skill_reference`.

                        - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

                      - `Version string`

                        The requested version selector, including `latest`.

                        `minLength: 0`

                    - `type AutomationEnvironmentOpenAIHostedSkillInline struct{…}`

                      Safe metadata for an inline skill archive.

                      - `Description string`

                        The skill description declared in `SKILL.md`.

                        `minLength: 0`

                      - `Name string`

                        The skill name declared in `SKILL.md`.

                        `minLength: 0`

                      - `Type Inline`

                        The type of the object. Always `inline`.

                        - `const InlineInline Inline = "inline"`

                  - `Type OpenAIHosted`

                    The type of the object. Always `openai_hosted`.

                    - `const OpenAIHostedOpenAIHosted OpenAIHosted = "openai_hosted"`

                - `type AutomationEnvironmentSelfHosted struct{…}`

                  - `CapabilityDirectories []string`

                    Directories that expose capabilities to the agent.

                    `minItems: 0`, `maxItems: 2000`

                  - `EnvironmentID string`

                    An existing registration, or null to create a session-owned environment.

                    `minLength: 0`

                  - `Type SelfHosted`

                    The type of the object. Always `self_hosted`.

                    - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

                  - `WorkspaceDirectory string`

                    The absolute project directory in the environment.

                    `minLength: 0`

              - `Input []AutomationTargetNewSessionInput`

                Initial input delivered to each new session.

                `minItems: 0`, `maxItems: 2000`

                - `Content []InputContentUnion`

                  The content of the message.

                  `minItems: 0`, `maxItems: 2000`

                  - `type InputContentInputText struct{…}`

                    Text input recorded in a session item.

                    - `Text string`

                      The text supplied to the agent.

                      `minLength: 0`

                    - `Type InputText`

                      The type of the object. Always `input_text`.

                      - `const InputTextInputText InputText = "input_text"`

                  - `type InputContentInputImage struct{…}`

                    Image input recorded in a session item.

                    - `ImageURL string`

                      The URL of the image supplied to the agent, which may be a base64-encoded data URL.

                      `minLength: 0`

                    - `Type InputImage`

                      The type of the object. Always `input_image`.

                      - `const InputImageInputImage InputImage = "input_image"`

                - `Role User`

                  The role of the message author. Always `user`.

                  - `const UserUser User = "user"`

                - `Type Message`

                  The type of the input item. Always `message`.

                  - `const MessageMessage Message = "message"`

              - `Metadata map[string, string]`

                Metadata attached to each new session.

              - `Type NewSession`

                The type of the object. Always `new_session`.

                - `const NewSessionNewSession NewSession = "new_session"`

              - `VaultIDs []string`

                Vaults made available to each new session.

                `minItems: 0`, `maxItems: 2000`

            - `type AutomationTargetExistingSession struct{…}`

              - `Instructions string`

                Saved instructions delivered as an automation notification.

                `minLength: 0`

              - `SessionID string`

                The session receiving each invocation.

                `minLength: 0`

              - `Type ExistingSession`

                The type of the object. Always `existing_session`.

                - `const ExistingSessionExistingSession ExistingSession = "existing_session"`

          - `Timezone string`

            The timezone used to interpret the expression.

            `minLength: 0`

          - `Type Periodic`

            The type of the object. Always `periodic`.

            - `const PeriodicPeriodic Periodic = "periodic"`

        - `type OneTimeAutomation struct{…}`

          Fields shared by periodic and one-time automations.

          - `ID string`

            The automation ID.

            `minLength: 0`

          - `CreatedAt int64`

            The creation time as a Unix timestamp in seconds.

            `format: int64`

          - `CreatedBy AutomationCreatedByUnion`

            Service-recorded provenance; callers cannot supply this field.

          - `Metadata map[string, string]`

            Custom string key-value pairs attached to the automation.

          - `Name string`

            The automation's display name.

            `minLength: 0`

          - `Object AgentAutomation`

            Always `agent.automation`.

            - `const AgentAutomationAgentAutomation AgentAutomation = "agent.automation"`

          - `RunAt int64`

            The Unix timestamp, in seconds, of the scheduled occurrence.

            `format: int64`

          - `Status OneTimeAutomationStatus`

            Completion means the schedule has finished, not the agent's work.

            - `const OneTimeAutomationStatusActive OneTimeAutomationStatus = "active"`

            - `const OneTimeAutomationStatusPaused OneTimeAutomationStatus = "paused"`

            - `const OneTimeAutomationStatusCompleted OneTimeAutomationStatus = "completed"`

          - `Target AutomationTargetUnion`

            The session configuration or existing session receiving invocations.

          - `Type Once`

            The type of the object. Always `once`.

            - `const OnceOnce Once = "once"`

      - `Type Automation`

        The type of the object. Always `automation`.

        - `const AutomationAutomation Automation = "automation"`

  - `Status AutomationInvocationStatus`

    Delivery status; completed does not mean the agent's work has finished.

    - `const AutomationInvocationStatusQueued AutomationInvocationStatus = "queued"`

    - `const AutomationInvocationStatusCompleted AutomationInvocationStatus = "completed"`

    - `const AutomationInvocationStatusFailed AutomationInvocationStatus = "failed"`

    - `const AutomationInvocationStatusSkipped AutomationInvocationStatus = "skipped"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  automationInvocation, err := client.Beta.Agents.Automations.Invocations.New(context.TODO(), "automation_id")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", automationInvocation.ID)
}
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

`client.Beta.Agents.Automations.Invocations.List(ctx, automationID, query) (*CursorPage[AutomationInvocation], error)`

**get** `/agents/automations/{automation_id}/invocations`

Lists delivery records for a project-owned automation.

### Parameters

- `automationID string`

  `minLength: 0`, `maxLength: 1048576`

- `query BetaAgentAutomationInvocationListParams`

  - `After param.Field[string]`

    Return resources after this resource ID in the selected order.

    `minLength: 0`, `maxLength: 1048576`

  - `Limit param.Field[int64]`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

    `format: int64`, `minimum: 1`, `maximum: 100`

  - `Order param.Field[BetaAgentAutomationInvocationListParamsOrder]`

    The order in which resources are returned. Defaults to `desc`.

    - `const BetaAgentAutomationInvocationListParamsOrderAsc BetaAgentAutomationInvocationListParamsOrder = "asc"`

      Returns resources in ascending order.

    - `const BetaAgentAutomationInvocationListParamsOrderDesc BetaAgentAutomationInvocationListParamsOrder = "desc"`

      Returns resources in descending order.

### Returns

- `type AutomationInvocation struct{…}`

  One attempted delivery by an automation.

  - `ID string`

    The invocation ID.

    `minLength: 0`

  - `AutomationID string`

    The automation that owns the invocation.

    `minLength: 0`

  - `CreatedAt int64`

    The creation time as a Unix timestamp in seconds.

    `format: int64`

  - `Error AutomationInvocationError`

    The permanent delivery failure, or null when no failure occurred.

    - `Code string`

      A machine-readable error code.

      `minLength: 0`

    - `Message string`

      A public explanation of the delivery failure.

      `minLength: 0`

  - `Object AgentAutomationInvocation`

    Always `agent.automation.invocation`.

    - `const AgentAutomationInvocationAgentAutomationInvocation AgentAutomationInvocation = "agent.automation.invocation"`

  - `ScheduledAt int64`

    The intended occurrence as a Unix timestamp in seconds, or null for manual runs.

    `format: int64`

  - `SessionID string`

    The target or newly created session ID, or null before one is available.

    `minLength: 0`

  - `SkipReason PendingDelivery`

    Why an occurrence was skipped, or null when it was not skipped.

    - `const PendingDeliveryPendingDelivery PendingDelivery = "pending_delivery"`

  - `Source AutomationInvocationSourceUnion`

    Whether the invocation was manual or scheduled.

    - `type AutomationInvocationSourceManual struct{…}`

      - `Type Manual`

        The type of the object. Always `manual`.

        - `const ManualManual Manual = "manual"`

    - `type AutomationInvocationSourceAutomation struct{…}`

      - `Automation AutomationUnion`

        The automation snapshot for this occurrence, excluding confidential values.

        - `type PeriodicAutomation struct{…}`

          Fields shared by periodic and one-time automations.

          - `ID string`

            The automation ID.

            `minLength: 0`

          - `CreatedAt int64`

            The creation time as a Unix timestamp in seconds.

            `format: int64`

          - `CreatedBy AutomationCreatedByUnion`

            Service-recorded provenance; callers cannot supply this field.

            - `type AutomationCreatedByDeveloper struct{…}`

              - `Type Developer`

                The type of the object. Always `developer`.

                - `const DeveloperDeveloper Developer = "developer"`

            - `type AutomationCreatedByAgent struct{…}`

              - `SessionID string`

                The creator session, which is also the automation's target.

                `minLength: 0`

              - `ToolCallID string`

                The tool call that created the automation.

                `minLength: 0`

              - `Type Agent`

                The type of the object. Always `agent`.

                - `const AgentAgent Agent = "agent"`

          - `Expression string`

            The cron expression determining scheduled occurrences.

            `minLength: 0`

          - `Metadata map[string, string]`

            Custom string key-value pairs attached to the automation.

          - `Name string`

            The automation's display name.

            `minLength: 0`

          - `Object AgentAutomation`

            Always `agent.automation`.

            - `const AgentAutomationAgentAutomation AgentAutomation = "agent.automation"`

          - `Status PeriodicAutomationStatus`

            Whether scheduled delivery is active or paused.

            - `const PeriodicAutomationStatusActive PeriodicAutomationStatus = "active"`

            - `const PeriodicAutomationStatusPaused PeriodicAutomationStatus = "paused"`

          - `Target AutomationTargetUnion`

            The session configuration or existing session receiving invocations.

            - `type AutomationTargetNewSession struct{…}`

              - `Agent AutomationAgentConfig`

                The inline agent configuration, or null when agent_id is configured.

                - `Instructions string`

                  Custom instructions, or null when absent.

                  `minLength: 0`

                - `Model string`

                  The requested model name.

                  `minLength: 0`

                - `MultiAgent MultiAgentConfig`

                  The configuration for creating and coordinating subagents.

                  - `Enabled bool`

                    Whether subagent tools are enabled. Defaults to false.

                  - `MaxConcurrentSubagents int64`

                    Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

                    `format: int64`, `minimum: 1`, `maximum: 4294967295`

                - `Reasoning AgentReasoning`

                  The configured reasoning policy.

                  - `Effort AgentReasoningEffort`

                    The requested reasoning effort, or `null` when the model selects its own default.

                    - `const AgentReasoningEffortNone AgentReasoningEffort = "none"`

                    - `const AgentReasoningEffortMinimal AgentReasoningEffort = "minimal"`

                    - `const AgentReasoningEffortLow AgentReasoningEffort = "low"`

                    - `const AgentReasoningEffortMedium AgentReasoningEffort = "medium"`

                    - `const AgentReasoningEffortHigh AgentReasoningEffort = "high"`

                    - `const AgentReasoningEffortXhigh AgentReasoningEffort = "xhigh"`

                    - `const AgentReasoningEffortMax AgentReasoningEffort = "max"`

                  - `Summary AgentReasoningSummary`

                    The requested reasoning summary format, or `null` when summaries are disabled.

                    - `const AgentReasoningSummaryConcise AgentReasoningSummary = "concise"`

                      Returns a concise reasoning summary when supported.

                    - `const AgentReasoningSummaryDetailed AgentReasoningSummary = "detailed"`

                      Returns a detailed reasoning summary when supported.

                    - `const AgentReasoningSummaryAuto AgentReasoningSummary = "auto"`

                      Automatically selects the most detailed summary supported by the model.

                - `ServiceTier AutomationAgentConfigServiceTier`

                  The configured service-tier policy.

                  - `const AutomationAgentConfigServiceTierAuto AutomationAgentConfigServiceTier = "auto"`

                  - `const AutomationAgentConfigServiceTierDefault AutomationAgentConfigServiceTier = "default"`

                  - `const AutomationAgentConfigServiceTierFlex AutomationAgentConfigServiceTier = "flex"`

                  - `const AutomationAgentConfigServiceTierPriority AutomationAgentConfigServiceTier = "priority"`

                  - `const AutomationAgentConfigServiceTierFast AutomationAgentConfigServiceTier = "fast"`

                  - `const AutomationAgentConfigServiceTierUltrafast AutomationAgentConfigServiceTier = "ultrafast"`

                - `Text AgentText`

                  The configured output format and verbosity.

                  - `Format TextFormatUnion`

                    The effective output format. Defaults to ordinary text.

                    - `type TextFormatText struct{…}`

                      Generates ordinary text without a structured-output constraint.

                      - `Type Text`

                        The type of the object. Always `text`.

                        - `const TextText Text = "text"`

                    - `type TextFormatJSONSchema struct{…}`

                      Constrains generated text to a JSON Schema.

                      - `Schema map[string, any]`

                        The JSON Schema that generated text must match.

                      - `Type JSONSchema`

                        The type of the object. Always `json_schema`.

                        - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

                  - `Verbosity AgentTextVerbosity`

                    The amount of text produced by the agent. Defaults to `medium`.

                    - `const AgentTextVerbosityLow AgentTextVerbosity = "low"`

                    - `const AgentTextVerbosityMedium AgentTextVerbosity = "medium"`

                    - `const AgentTextVerbosityHigh AgentTextVerbosity = "high"`

                - `Tools []AgentToolUnion`

                  Configured tools, excluding confidential credentials.

                  `minItems: 0`, `maxItems: 2000`

                  - `type AgentToolFunction struct{…}`

                    A function defined by the application.

                    - `DeferLoading bool`

                      Whether the function is deferred and discovered through tool search.

                    - `Description string`

                      A description of what the function does.

                      `minLength: 0`

                    - `Name string`

                      The name of the function.

                      `minLength: 0`

                    - `Parameters map[string, any]`

                      A JSON Schema object describing the function's arguments.

                    - `Type Function`

                      The type of the object. Always `function`.

                      - `const FunctionFunction Function = "function"`

                    - `Async bool`

                      Whether the agent continues without waiting for the function result.

                  - `type AgentToolProgrammaticToolCalling struct{…}`

                    Enables calling tools from model-generated code.

                    - `Enabled bool`

                      Whether tools can be called from model-generated code.

                    - `Type ProgrammaticToolCalling`

                      The type of the object. Always `programmatic_tool_calling`.

                      - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

                  - `type AgentToolMcp struct{…}`

                    Tools provided by a remote MCP server.

                    - `AllowedTools []string`

                      The MCP tools the agent may call.

                      `minItems: 0`, `maxItems: 2000`

                    - `ConnectionOrigin string`

                      Where outbound MCP HTTP connections originate.

                      - `const AgentToolMcpConnectionOriginService AgentToolMcpConnectionOrigin = "service"`

                      - `const AgentToolMcpConnectionOriginEnvironment AgentToolMcpConnectionOrigin = "environment"`

                    - `CredentialID string`

                      The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

                      `minLength: 0`

                    - `RequestMetadata map[string, any]`

                      Metadata included with requests to this MCP server.

                    - `Required bool`

                      Whether this MCP server must initialize before the first turn.

                    - `ServerLabel string`

                      A label used to identify the MCP server in tool calls.

                      `minLength: 0`

                    - `Transport McpTransportUnion`

                      The transport used to connect to the MCP server.

                      - `type McpTransportHTTP struct{…}`

                        Connects to an MCP server over HTTP.

                        - `ServerURL string`

                          The URL of the MCP server.

                          `minLength: 0`

                        - `Type HTTP`

                          The type of the object. Always `http`.

                          - `const HTTPHTTP HTTP = "http"`

                      - `type McpTransportStdio struct{…}`

                        Starts an MCP server as a local process.

                        - `Args []string`

                          Arguments passed to the MCP server command.

                          `minItems: 0`, `maxItems: 2000`

                        - `Command string`

                          The command used to start the MCP server.

                          `minLength: 0`

                        - `Cwd string`

                          The working directory used to start the MCP server.

                          `minLength: 0`

                        - `EnvVars []string`

                          Environment variable names inherited from the execution environment.

                          `minItems: 0`, `maxItems: 2000`

                        - `Type Stdio`

                          The type of the object. Always `stdio`.

                          - `const StdioStdio Stdio = "stdio"`

                    - `Type Mcp`

                      The type of the object. Always `mcp`.

                      - `const McpMcp Mcp = "mcp"`

                  - `type AgentToolWebSearch struct{…}`

                    Web search.

                    - `AllowedDomains []string`

                      Allowed search domains, or `null` when the search is unrestricted.

                      `minItems: 0`, `maxItems: 2000`

                    - `ContextSize string`

                      The amount of search context made available to the model. Defaults to `medium`.

                      - `const AgentToolWebSearchContextSizeLow AgentToolWebSearchContextSize = "low"`

                      - `const AgentToolWebSearchContextSizeMedium AgentToolWebSearchContextSize = "medium"`

                      - `const AgentToolWebSearchContextSizeHigh AgentToolWebSearchContextSize = "high"`

                    - `Location AgentToolWebSearchLocation`

                      Approximate location used to localize search results, if provided.

                      - `City string`

                        The city name.

                        `minLength: 0`

                      - `Country string`

                        The two-letter ISO country code, such as `US`.

                        `minLength: 0`

                      - `Region string`

                        The region or state name.

                        `minLength: 0`

                      - `Timezone string`

                        The IANA timezone, such as `America/Los_Angeles`.

                        `minLength: 0`

                    - `Mode string`

                      The source used for web search results.

                      - `const AgentToolWebSearchModeDisabled AgentToolWebSearchMode = "disabled"`

                      - `const AgentToolWebSearchModeCached AgentToolWebSearchMode = "cached"`

                      - `const AgentToolWebSearchModeLive AgentToolWebSearchMode = "live"`

                    - `Type WebSearch`

                      The type of the object. Always `web_search`.

                      - `const WebSearchWebSearch WebSearch = "web_search"`

                  - `type AgentToolComputerUse struct{…}`

                    Browser use in an OpenAI-hosted session.

                    - `IncludeScreenshots bool`

                      Whether computer tool outputs include screenshots.

                    - `Type ComputerUse`

                      The type of the object. Always `computer_use`.

                      - `const ComputerUseComputerUse ComputerUse = "computer_use"`

                  - `type AgentToolAutomations struct{…}`

                    Lets the agent manage its own scheduled wakeups.

                    - `Type Automations`

                      The type of the object. Always `automations`.

                      - `const AutomationsAutomations Automations = "automations"`

                - `Compaction AutomationAgentConfigCompaction`

                  The effective context compaction settings.

                  - `Async bool`

                    Whether context is compacted in the background. Defaults to true.

                - `Experimental AutomationAgentConfigExperimental`

                  The effective experimental settings for the agent.

                  - `TimeAwareness bool`

                    Whether the model receives periodic current-time reminders.

              - `AgentID string`

                The saved agent reference, or null when an inline agent is configured.

                `minLength: 0`

              - `Environment AutomationEnvironmentUnion`

                Configuration or references used to select the execution environment.

                - `type AutomationEnvironmentNone struct{…}`

                  - `Type None`

                    The type of the object. Always `none`.

                    - `const NoneNone None = "none"`

                - `type AutomationEnvironmentOpenAIHosted struct{…}`

                  Hosted environment selection with confidential setup commands and variables omitted.

                  - `CapabilityDirectories []string`

                    Directory overrides, or null to inherit the template or creation default.

                    `minItems: 0`, `maxItems: 2000`

                  - `ContainerSize string`

                    The configured container size, or null to use the creation default.

                    - `const AutomationEnvironmentOpenAIHostedContainerSizeSmall AutomationEnvironmentOpenAIHostedContainerSize = "small"`

                    - `const AutomationEnvironmentOpenAIHostedContainerSizeMedium AutomationEnvironmentOpenAIHostedContainerSize = "medium"`

                    - `const AutomationEnvironmentOpenAIHostedContainerSizeLarge AutomationEnvironmentOpenAIHostedContainerSize = "large"`

                  - `Desktop AutomationEnvironmentOpenAIHostedDesktop`

                    Desktop overrides, or null to inherit the template or creation default.

                    - `Enabled bool`

                      Whether the environment provisions a desktop and browser proxy.

                  - `EnvironmentID string`

                    An existing environment reference, or null when provisioning a new environment.

                    `minLength: 0`

                  - `EnvironmentTemplateID string`

                    A template reference, or null when no template is selected.

                    `minLength: 0`

                  - `Files []AutomationEnvironmentOpenAIHostedFileUnion`

                    File overrides, excluding contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `type AutomationEnvironmentOpenAIHostedFileFileID struct{…}`

                      A project-scoped Files API reference resolved separately for each session.

                      - `FileID string`

                        The ID of the uploaded file.

                        `minLength: 0`

                      - `Path string`

                        The file's absolute path inside the environment.

                        `minLength: 0`

                      - `Type FileID`

                        The type of the object. Always `file_id`.

                        - `const FileIDFileID FileID = "file_id"`

                    - `type AutomationEnvironmentOpenAIHostedFileInline struct{…}`

                      Metadata for confidential inline file contents.

                      - `Path string`

                        The file's absolute path inside the environment.

                        `minLength: 0`

                      - `SizeBytes int64`

                        The decoded size of the inline file in bytes.

                        `format: int64`, `minimum: 0`

                      - `Type Inline`

                        The type of the object. Always `inline`.

                        - `const InlineInline Inline = "inline"`

                  - `Network AutomationEnvironmentOpenAIHostedNetwork`

                    Network overrides, or null to inherit the template or creation default.

                    - `Access string`

                      The environment's network access mode.

                      - `const AutomationEnvironmentOpenAIHostedNetworkAccessEnabled AutomationEnvironmentOpenAIHostedNetworkAccess = "enabled"`

                        Allows unrestricted network access.

                      - `const AutomationEnvironmentOpenAIHostedNetworkAccessDisabled AutomationEnvironmentOpenAIHostedNetworkAccess = "disabled"`

                        Disables network access.

                      - `const AutomationEnvironmentOpenAIHostedNetworkAccessRestricted AutomationEnvironmentOpenAIHostedNetworkAccess = "restricted"`

                        Applies the configured domain restrictions.

                    - `AllowedDomains []string`

                      Domains the environment may access when network access is restricted.

                      `minItems: 0`, `maxItems: 2000`

                  - `Packages AutomationEnvironmentOpenAIHostedPackages`

                    Package overrides, or null to inherit the template or creation default.

                    - `Npm []string`

                      npm packages installed globally in the environment.

                      `minItems: 0`, `maxItems: 16384`

                    - `Python []string`

                      Python packages installed in the environment.

                      `minItems: 0`, `maxItems: 16384`

                    - `System []string`

                      System packages installed in the environment.

                      `minItems: 0`, `maxItems: 16384`

                  - `Plugins []HostedPlugin`

                    Plugin overrides, excluding archive contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `Description string`

                      The installed plugin description.

                      `minLength: 0`

                    - `Name string`

                      The installed plugin name.

                      `minLength: 0`

                    - `Type Inline`

                      The type of the object. Always `inline`.

                      - `const InlineInline Inline = "inline"`

                  - `Skills []AutomationEnvironmentOpenAIHostedSkillUnion`

                    Skill overrides, excluding archive contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `type AutomationEnvironmentOpenAIHostedSkillSkillReference struct{…}`

                      A skill resolved afresh from the Skills API whenever a session starts.

                      - `SkillID string`

                        The referenced skill ID.

                        `minLength: 0`

                      - `Type SkillReference`

                        The type of the object. Always `skill_reference`.

                        - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

                      - `Version string`

                        The requested version selector, including `latest`.

                        `minLength: 0`

                    - `type AutomationEnvironmentOpenAIHostedSkillInline struct{…}`

                      Safe metadata for an inline skill archive.

                      - `Description string`

                        The skill description declared in `SKILL.md`.

                        `minLength: 0`

                      - `Name string`

                        The skill name declared in `SKILL.md`.

                        `minLength: 0`

                      - `Type Inline`

                        The type of the object. Always `inline`.

                        - `const InlineInline Inline = "inline"`

                  - `Type OpenAIHosted`

                    The type of the object. Always `openai_hosted`.

                    - `const OpenAIHostedOpenAIHosted OpenAIHosted = "openai_hosted"`

                - `type AutomationEnvironmentSelfHosted struct{…}`

                  - `CapabilityDirectories []string`

                    Directories that expose capabilities to the agent.

                    `minItems: 0`, `maxItems: 2000`

                  - `EnvironmentID string`

                    An existing registration, or null to create a session-owned environment.

                    `minLength: 0`

                  - `Type SelfHosted`

                    The type of the object. Always `self_hosted`.

                    - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

                  - `WorkspaceDirectory string`

                    The absolute project directory in the environment.

                    `minLength: 0`

              - `Input []AutomationTargetNewSessionInput`

                Initial input delivered to each new session.

                `minItems: 0`, `maxItems: 2000`

                - `Content []InputContentUnion`

                  The content of the message.

                  `minItems: 0`, `maxItems: 2000`

                  - `type InputContentInputText struct{…}`

                    Text input recorded in a session item.

                    - `Text string`

                      The text supplied to the agent.

                      `minLength: 0`

                    - `Type InputText`

                      The type of the object. Always `input_text`.

                      - `const InputTextInputText InputText = "input_text"`

                  - `type InputContentInputImage struct{…}`

                    Image input recorded in a session item.

                    - `ImageURL string`

                      The URL of the image supplied to the agent, which may be a base64-encoded data URL.

                      `minLength: 0`

                    - `Type InputImage`

                      The type of the object. Always `input_image`.

                      - `const InputImageInputImage InputImage = "input_image"`

                - `Role User`

                  The role of the message author. Always `user`.

                  - `const UserUser User = "user"`

                - `Type Message`

                  The type of the input item. Always `message`.

                  - `const MessageMessage Message = "message"`

              - `Metadata map[string, string]`

                Metadata attached to each new session.

              - `Type NewSession`

                The type of the object. Always `new_session`.

                - `const NewSessionNewSession NewSession = "new_session"`

              - `VaultIDs []string`

                Vaults made available to each new session.

                `minItems: 0`, `maxItems: 2000`

            - `type AutomationTargetExistingSession struct{…}`

              - `Instructions string`

                Saved instructions delivered as an automation notification.

                `minLength: 0`

              - `SessionID string`

                The session receiving each invocation.

                `minLength: 0`

              - `Type ExistingSession`

                The type of the object. Always `existing_session`.

                - `const ExistingSessionExistingSession ExistingSession = "existing_session"`

          - `Timezone string`

            The timezone used to interpret the expression.

            `minLength: 0`

          - `Type Periodic`

            The type of the object. Always `periodic`.

            - `const PeriodicPeriodic Periodic = "periodic"`

        - `type OneTimeAutomation struct{…}`

          Fields shared by periodic and one-time automations.

          - `ID string`

            The automation ID.

            `minLength: 0`

          - `CreatedAt int64`

            The creation time as a Unix timestamp in seconds.

            `format: int64`

          - `CreatedBy AutomationCreatedByUnion`

            Service-recorded provenance; callers cannot supply this field.

          - `Metadata map[string, string]`

            Custom string key-value pairs attached to the automation.

          - `Name string`

            The automation's display name.

            `minLength: 0`

          - `Object AgentAutomation`

            Always `agent.automation`.

            - `const AgentAutomationAgentAutomation AgentAutomation = "agent.automation"`

          - `RunAt int64`

            The Unix timestamp, in seconds, of the scheduled occurrence.

            `format: int64`

          - `Status OneTimeAutomationStatus`

            Completion means the schedule has finished, not the agent's work.

            - `const OneTimeAutomationStatusActive OneTimeAutomationStatus = "active"`

            - `const OneTimeAutomationStatusPaused OneTimeAutomationStatus = "paused"`

            - `const OneTimeAutomationStatusCompleted OneTimeAutomationStatus = "completed"`

          - `Target AutomationTargetUnion`

            The session configuration or existing session receiving invocations.

          - `Type Once`

            The type of the object. Always `once`.

            - `const OnceOnce Once = "once"`

      - `Type Automation`

        The type of the object. Always `automation`.

        - `const AutomationAutomation Automation = "automation"`

  - `Status AutomationInvocationStatus`

    Delivery status; completed does not mean the agent's work has finished.

    - `const AutomationInvocationStatusQueued AutomationInvocationStatus = "queued"`

    - `const AutomationInvocationStatusCompleted AutomationInvocationStatus = "completed"`

    - `const AutomationInvocationStatusFailed AutomationInvocationStatus = "failed"`

    - `const AutomationInvocationStatusSkipped AutomationInvocationStatus = "skipped"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  page, err := client.Beta.Agents.Automations.Invocations.List(
    context.TODO(),
    "automation_id",
    openai.BetaAgentAutomationInvocationListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
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

`client.Beta.Agents.Automations.Invocations.Get(ctx, automationID, invocationID) (*AutomationInvocation, error)`

**get** `/agents/automations/{automation_id}/invocations/{invocation_id}`

Retrieves a delivery record for a project-owned automation.

### Parameters

- `automationID string`

  `minLength: 0`, `maxLength: 1048576`

- `invocationID string`

  `minLength: 0`, `maxLength: 1048576`

### Returns

- `type AutomationInvocation struct{…}`

  One attempted delivery by an automation.

  - `ID string`

    The invocation ID.

    `minLength: 0`

  - `AutomationID string`

    The automation that owns the invocation.

    `minLength: 0`

  - `CreatedAt int64`

    The creation time as a Unix timestamp in seconds.

    `format: int64`

  - `Error AutomationInvocationError`

    The permanent delivery failure, or null when no failure occurred.

    - `Code string`

      A machine-readable error code.

      `minLength: 0`

    - `Message string`

      A public explanation of the delivery failure.

      `minLength: 0`

  - `Object AgentAutomationInvocation`

    Always `agent.automation.invocation`.

    - `const AgentAutomationInvocationAgentAutomationInvocation AgentAutomationInvocation = "agent.automation.invocation"`

  - `ScheduledAt int64`

    The intended occurrence as a Unix timestamp in seconds, or null for manual runs.

    `format: int64`

  - `SessionID string`

    The target or newly created session ID, or null before one is available.

    `minLength: 0`

  - `SkipReason PendingDelivery`

    Why an occurrence was skipped, or null when it was not skipped.

    - `const PendingDeliveryPendingDelivery PendingDelivery = "pending_delivery"`

  - `Source AutomationInvocationSourceUnion`

    Whether the invocation was manual or scheduled.

    - `type AutomationInvocationSourceManual struct{…}`

      - `Type Manual`

        The type of the object. Always `manual`.

        - `const ManualManual Manual = "manual"`

    - `type AutomationInvocationSourceAutomation struct{…}`

      - `Automation AutomationUnion`

        The automation snapshot for this occurrence, excluding confidential values.

        - `type PeriodicAutomation struct{…}`

          Fields shared by periodic and one-time automations.

          - `ID string`

            The automation ID.

            `minLength: 0`

          - `CreatedAt int64`

            The creation time as a Unix timestamp in seconds.

            `format: int64`

          - `CreatedBy AutomationCreatedByUnion`

            Service-recorded provenance; callers cannot supply this field.

            - `type AutomationCreatedByDeveloper struct{…}`

              - `Type Developer`

                The type of the object. Always `developer`.

                - `const DeveloperDeveloper Developer = "developer"`

            - `type AutomationCreatedByAgent struct{…}`

              - `SessionID string`

                The creator session, which is also the automation's target.

                `minLength: 0`

              - `ToolCallID string`

                The tool call that created the automation.

                `minLength: 0`

              - `Type Agent`

                The type of the object. Always `agent`.

                - `const AgentAgent Agent = "agent"`

          - `Expression string`

            The cron expression determining scheduled occurrences.

            `minLength: 0`

          - `Metadata map[string, string]`

            Custom string key-value pairs attached to the automation.

          - `Name string`

            The automation's display name.

            `minLength: 0`

          - `Object AgentAutomation`

            Always `agent.automation`.

            - `const AgentAutomationAgentAutomation AgentAutomation = "agent.automation"`

          - `Status PeriodicAutomationStatus`

            Whether scheduled delivery is active or paused.

            - `const PeriodicAutomationStatusActive PeriodicAutomationStatus = "active"`

            - `const PeriodicAutomationStatusPaused PeriodicAutomationStatus = "paused"`

          - `Target AutomationTargetUnion`

            The session configuration or existing session receiving invocations.

            - `type AutomationTargetNewSession struct{…}`

              - `Agent AutomationAgentConfig`

                The inline agent configuration, or null when agent_id is configured.

                - `Instructions string`

                  Custom instructions, or null when absent.

                  `minLength: 0`

                - `Model string`

                  The requested model name.

                  `minLength: 0`

                - `MultiAgent MultiAgentConfig`

                  The configuration for creating and coordinating subagents.

                  - `Enabled bool`

                    Whether subagent tools are enabled. Defaults to false.

                  - `MaxConcurrentSubagents int64`

                    Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

                    `format: int64`, `minimum: 1`, `maximum: 4294967295`

                - `Reasoning AgentReasoning`

                  The configured reasoning policy.

                  - `Effort AgentReasoningEffort`

                    The requested reasoning effort, or `null` when the model selects its own default.

                    - `const AgentReasoningEffortNone AgentReasoningEffort = "none"`

                    - `const AgentReasoningEffortMinimal AgentReasoningEffort = "minimal"`

                    - `const AgentReasoningEffortLow AgentReasoningEffort = "low"`

                    - `const AgentReasoningEffortMedium AgentReasoningEffort = "medium"`

                    - `const AgentReasoningEffortHigh AgentReasoningEffort = "high"`

                    - `const AgentReasoningEffortXhigh AgentReasoningEffort = "xhigh"`

                    - `const AgentReasoningEffortMax AgentReasoningEffort = "max"`

                  - `Summary AgentReasoningSummary`

                    The requested reasoning summary format, or `null` when summaries are disabled.

                    - `const AgentReasoningSummaryConcise AgentReasoningSummary = "concise"`

                      Returns a concise reasoning summary when supported.

                    - `const AgentReasoningSummaryDetailed AgentReasoningSummary = "detailed"`

                      Returns a detailed reasoning summary when supported.

                    - `const AgentReasoningSummaryAuto AgentReasoningSummary = "auto"`

                      Automatically selects the most detailed summary supported by the model.

                - `ServiceTier AutomationAgentConfigServiceTier`

                  The configured service-tier policy.

                  - `const AutomationAgentConfigServiceTierAuto AutomationAgentConfigServiceTier = "auto"`

                  - `const AutomationAgentConfigServiceTierDefault AutomationAgentConfigServiceTier = "default"`

                  - `const AutomationAgentConfigServiceTierFlex AutomationAgentConfigServiceTier = "flex"`

                  - `const AutomationAgentConfigServiceTierPriority AutomationAgentConfigServiceTier = "priority"`

                  - `const AutomationAgentConfigServiceTierFast AutomationAgentConfigServiceTier = "fast"`

                  - `const AutomationAgentConfigServiceTierUltrafast AutomationAgentConfigServiceTier = "ultrafast"`

                - `Text AgentText`

                  The configured output format and verbosity.

                  - `Format TextFormatUnion`

                    The effective output format. Defaults to ordinary text.

                    - `type TextFormatText struct{…}`

                      Generates ordinary text without a structured-output constraint.

                      - `Type Text`

                        The type of the object. Always `text`.

                        - `const TextText Text = "text"`

                    - `type TextFormatJSONSchema struct{…}`

                      Constrains generated text to a JSON Schema.

                      - `Schema map[string, any]`

                        The JSON Schema that generated text must match.

                      - `Type JSONSchema`

                        The type of the object. Always `json_schema`.

                        - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

                  - `Verbosity AgentTextVerbosity`

                    The amount of text produced by the agent. Defaults to `medium`.

                    - `const AgentTextVerbosityLow AgentTextVerbosity = "low"`

                    - `const AgentTextVerbosityMedium AgentTextVerbosity = "medium"`

                    - `const AgentTextVerbosityHigh AgentTextVerbosity = "high"`

                - `Tools []AgentToolUnion`

                  Configured tools, excluding confidential credentials.

                  `minItems: 0`, `maxItems: 2000`

                  - `type AgentToolFunction struct{…}`

                    A function defined by the application.

                    - `DeferLoading bool`

                      Whether the function is deferred and discovered through tool search.

                    - `Description string`

                      A description of what the function does.

                      `minLength: 0`

                    - `Name string`

                      The name of the function.

                      `minLength: 0`

                    - `Parameters map[string, any]`

                      A JSON Schema object describing the function's arguments.

                    - `Type Function`

                      The type of the object. Always `function`.

                      - `const FunctionFunction Function = "function"`

                    - `Async bool`

                      Whether the agent continues without waiting for the function result.

                  - `type AgentToolProgrammaticToolCalling struct{…}`

                    Enables calling tools from model-generated code.

                    - `Enabled bool`

                      Whether tools can be called from model-generated code.

                    - `Type ProgrammaticToolCalling`

                      The type of the object. Always `programmatic_tool_calling`.

                      - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

                  - `type AgentToolMcp struct{…}`

                    Tools provided by a remote MCP server.

                    - `AllowedTools []string`

                      The MCP tools the agent may call.

                      `minItems: 0`, `maxItems: 2000`

                    - `ConnectionOrigin string`

                      Where outbound MCP HTTP connections originate.

                      - `const AgentToolMcpConnectionOriginService AgentToolMcpConnectionOrigin = "service"`

                      - `const AgentToolMcpConnectionOriginEnvironment AgentToolMcpConnectionOrigin = "environment"`

                    - `CredentialID string`

                      The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

                      `minLength: 0`

                    - `RequestMetadata map[string, any]`

                      Metadata included with requests to this MCP server.

                    - `Required bool`

                      Whether this MCP server must initialize before the first turn.

                    - `ServerLabel string`

                      A label used to identify the MCP server in tool calls.

                      `minLength: 0`

                    - `Transport McpTransportUnion`

                      The transport used to connect to the MCP server.

                      - `type McpTransportHTTP struct{…}`

                        Connects to an MCP server over HTTP.

                        - `ServerURL string`

                          The URL of the MCP server.

                          `minLength: 0`

                        - `Type HTTP`

                          The type of the object. Always `http`.

                          - `const HTTPHTTP HTTP = "http"`

                      - `type McpTransportStdio struct{…}`

                        Starts an MCP server as a local process.

                        - `Args []string`

                          Arguments passed to the MCP server command.

                          `minItems: 0`, `maxItems: 2000`

                        - `Command string`

                          The command used to start the MCP server.

                          `minLength: 0`

                        - `Cwd string`

                          The working directory used to start the MCP server.

                          `minLength: 0`

                        - `EnvVars []string`

                          Environment variable names inherited from the execution environment.

                          `minItems: 0`, `maxItems: 2000`

                        - `Type Stdio`

                          The type of the object. Always `stdio`.

                          - `const StdioStdio Stdio = "stdio"`

                    - `Type Mcp`

                      The type of the object. Always `mcp`.

                      - `const McpMcp Mcp = "mcp"`

                  - `type AgentToolWebSearch struct{…}`

                    Web search.

                    - `AllowedDomains []string`

                      Allowed search domains, or `null` when the search is unrestricted.

                      `minItems: 0`, `maxItems: 2000`

                    - `ContextSize string`

                      The amount of search context made available to the model. Defaults to `medium`.

                      - `const AgentToolWebSearchContextSizeLow AgentToolWebSearchContextSize = "low"`

                      - `const AgentToolWebSearchContextSizeMedium AgentToolWebSearchContextSize = "medium"`

                      - `const AgentToolWebSearchContextSizeHigh AgentToolWebSearchContextSize = "high"`

                    - `Location AgentToolWebSearchLocation`

                      Approximate location used to localize search results, if provided.

                      - `City string`

                        The city name.

                        `minLength: 0`

                      - `Country string`

                        The two-letter ISO country code, such as `US`.

                        `minLength: 0`

                      - `Region string`

                        The region or state name.

                        `minLength: 0`

                      - `Timezone string`

                        The IANA timezone, such as `America/Los_Angeles`.

                        `minLength: 0`

                    - `Mode string`

                      The source used for web search results.

                      - `const AgentToolWebSearchModeDisabled AgentToolWebSearchMode = "disabled"`

                      - `const AgentToolWebSearchModeCached AgentToolWebSearchMode = "cached"`

                      - `const AgentToolWebSearchModeLive AgentToolWebSearchMode = "live"`

                    - `Type WebSearch`

                      The type of the object. Always `web_search`.

                      - `const WebSearchWebSearch WebSearch = "web_search"`

                  - `type AgentToolComputerUse struct{…}`

                    Browser use in an OpenAI-hosted session.

                    - `IncludeScreenshots bool`

                      Whether computer tool outputs include screenshots.

                    - `Type ComputerUse`

                      The type of the object. Always `computer_use`.

                      - `const ComputerUseComputerUse ComputerUse = "computer_use"`

                  - `type AgentToolAutomations struct{…}`

                    Lets the agent manage its own scheduled wakeups.

                    - `Type Automations`

                      The type of the object. Always `automations`.

                      - `const AutomationsAutomations Automations = "automations"`

                - `Compaction AutomationAgentConfigCompaction`

                  The effective context compaction settings.

                  - `Async bool`

                    Whether context is compacted in the background. Defaults to true.

                - `Experimental AutomationAgentConfigExperimental`

                  The effective experimental settings for the agent.

                  - `TimeAwareness bool`

                    Whether the model receives periodic current-time reminders.

              - `AgentID string`

                The saved agent reference, or null when an inline agent is configured.

                `minLength: 0`

              - `Environment AutomationEnvironmentUnion`

                Configuration or references used to select the execution environment.

                - `type AutomationEnvironmentNone struct{…}`

                  - `Type None`

                    The type of the object. Always `none`.

                    - `const NoneNone None = "none"`

                - `type AutomationEnvironmentOpenAIHosted struct{…}`

                  Hosted environment selection with confidential setup commands and variables omitted.

                  - `CapabilityDirectories []string`

                    Directory overrides, or null to inherit the template or creation default.

                    `minItems: 0`, `maxItems: 2000`

                  - `ContainerSize string`

                    The configured container size, or null to use the creation default.

                    - `const AutomationEnvironmentOpenAIHostedContainerSizeSmall AutomationEnvironmentOpenAIHostedContainerSize = "small"`

                    - `const AutomationEnvironmentOpenAIHostedContainerSizeMedium AutomationEnvironmentOpenAIHostedContainerSize = "medium"`

                    - `const AutomationEnvironmentOpenAIHostedContainerSizeLarge AutomationEnvironmentOpenAIHostedContainerSize = "large"`

                  - `Desktop AutomationEnvironmentOpenAIHostedDesktop`

                    Desktop overrides, or null to inherit the template or creation default.

                    - `Enabled bool`

                      Whether the environment provisions a desktop and browser proxy.

                  - `EnvironmentID string`

                    An existing environment reference, or null when provisioning a new environment.

                    `minLength: 0`

                  - `EnvironmentTemplateID string`

                    A template reference, or null when no template is selected.

                    `minLength: 0`

                  - `Files []AutomationEnvironmentOpenAIHostedFileUnion`

                    File overrides, excluding contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `type AutomationEnvironmentOpenAIHostedFileFileID struct{…}`

                      A project-scoped Files API reference resolved separately for each session.

                      - `FileID string`

                        The ID of the uploaded file.

                        `minLength: 0`

                      - `Path string`

                        The file's absolute path inside the environment.

                        `minLength: 0`

                      - `Type FileID`

                        The type of the object. Always `file_id`.

                        - `const FileIDFileID FileID = "file_id"`

                    - `type AutomationEnvironmentOpenAIHostedFileInline struct{…}`

                      Metadata for confidential inline file contents.

                      - `Path string`

                        The file's absolute path inside the environment.

                        `minLength: 0`

                      - `SizeBytes int64`

                        The decoded size of the inline file in bytes.

                        `format: int64`, `minimum: 0`

                      - `Type Inline`

                        The type of the object. Always `inline`.

                        - `const InlineInline Inline = "inline"`

                  - `Network AutomationEnvironmentOpenAIHostedNetwork`

                    Network overrides, or null to inherit the template or creation default.

                    - `Access string`

                      The environment's network access mode.

                      - `const AutomationEnvironmentOpenAIHostedNetworkAccessEnabled AutomationEnvironmentOpenAIHostedNetworkAccess = "enabled"`

                        Allows unrestricted network access.

                      - `const AutomationEnvironmentOpenAIHostedNetworkAccessDisabled AutomationEnvironmentOpenAIHostedNetworkAccess = "disabled"`

                        Disables network access.

                      - `const AutomationEnvironmentOpenAIHostedNetworkAccessRestricted AutomationEnvironmentOpenAIHostedNetworkAccess = "restricted"`

                        Applies the configured domain restrictions.

                    - `AllowedDomains []string`

                      Domains the environment may access when network access is restricted.

                      `minItems: 0`, `maxItems: 2000`

                  - `Packages AutomationEnvironmentOpenAIHostedPackages`

                    Package overrides, or null to inherit the template or creation default.

                    - `Npm []string`

                      npm packages installed globally in the environment.

                      `minItems: 0`, `maxItems: 16384`

                    - `Python []string`

                      Python packages installed in the environment.

                      `minItems: 0`, `maxItems: 16384`

                    - `System []string`

                      System packages installed in the environment.

                      `minItems: 0`, `maxItems: 16384`

                  - `Plugins []HostedPlugin`

                    Plugin overrides, excluding archive contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `Description string`

                      The installed plugin description.

                      `minLength: 0`

                    - `Name string`

                      The installed plugin name.

                      `minLength: 0`

                    - `Type Inline`

                      The type of the object. Always `inline`.

                      - `const InlineInline Inline = "inline"`

                  - `Skills []AutomationEnvironmentOpenAIHostedSkillUnion`

                    Skill overrides, excluding archive contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `type AutomationEnvironmentOpenAIHostedSkillSkillReference struct{…}`

                      A skill resolved afresh from the Skills API whenever a session starts.

                      - `SkillID string`

                        The referenced skill ID.

                        `minLength: 0`

                      - `Type SkillReference`

                        The type of the object. Always `skill_reference`.

                        - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

                      - `Version string`

                        The requested version selector, including `latest`.

                        `minLength: 0`

                    - `type AutomationEnvironmentOpenAIHostedSkillInline struct{…}`

                      Safe metadata for an inline skill archive.

                      - `Description string`

                        The skill description declared in `SKILL.md`.

                        `minLength: 0`

                      - `Name string`

                        The skill name declared in `SKILL.md`.

                        `minLength: 0`

                      - `Type Inline`

                        The type of the object. Always `inline`.

                        - `const InlineInline Inline = "inline"`

                  - `Type OpenAIHosted`

                    The type of the object. Always `openai_hosted`.

                    - `const OpenAIHostedOpenAIHosted OpenAIHosted = "openai_hosted"`

                - `type AutomationEnvironmentSelfHosted struct{…}`

                  - `CapabilityDirectories []string`

                    Directories that expose capabilities to the agent.

                    `minItems: 0`, `maxItems: 2000`

                  - `EnvironmentID string`

                    An existing registration, or null to create a session-owned environment.

                    `minLength: 0`

                  - `Type SelfHosted`

                    The type of the object. Always `self_hosted`.

                    - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

                  - `WorkspaceDirectory string`

                    The absolute project directory in the environment.

                    `minLength: 0`

              - `Input []AutomationTargetNewSessionInput`

                Initial input delivered to each new session.

                `minItems: 0`, `maxItems: 2000`

                - `Content []InputContentUnion`

                  The content of the message.

                  `minItems: 0`, `maxItems: 2000`

                  - `type InputContentInputText struct{…}`

                    Text input recorded in a session item.

                    - `Text string`

                      The text supplied to the agent.

                      `minLength: 0`

                    - `Type InputText`

                      The type of the object. Always `input_text`.

                      - `const InputTextInputText InputText = "input_text"`

                  - `type InputContentInputImage struct{…}`

                    Image input recorded in a session item.

                    - `ImageURL string`

                      The URL of the image supplied to the agent, which may be a base64-encoded data URL.

                      `minLength: 0`

                    - `Type InputImage`

                      The type of the object. Always `input_image`.

                      - `const InputImageInputImage InputImage = "input_image"`

                - `Role User`

                  The role of the message author. Always `user`.

                  - `const UserUser User = "user"`

                - `Type Message`

                  The type of the input item. Always `message`.

                  - `const MessageMessage Message = "message"`

              - `Metadata map[string, string]`

                Metadata attached to each new session.

              - `Type NewSession`

                The type of the object. Always `new_session`.

                - `const NewSessionNewSession NewSession = "new_session"`

              - `VaultIDs []string`

                Vaults made available to each new session.

                `minItems: 0`, `maxItems: 2000`

            - `type AutomationTargetExistingSession struct{…}`

              - `Instructions string`

                Saved instructions delivered as an automation notification.

                `minLength: 0`

              - `SessionID string`

                The session receiving each invocation.

                `minLength: 0`

              - `Type ExistingSession`

                The type of the object. Always `existing_session`.

                - `const ExistingSessionExistingSession ExistingSession = "existing_session"`

          - `Timezone string`

            The timezone used to interpret the expression.

            `minLength: 0`

          - `Type Periodic`

            The type of the object. Always `periodic`.

            - `const PeriodicPeriodic Periodic = "periodic"`

        - `type OneTimeAutomation struct{…}`

          Fields shared by periodic and one-time automations.

          - `ID string`

            The automation ID.

            `minLength: 0`

          - `CreatedAt int64`

            The creation time as a Unix timestamp in seconds.

            `format: int64`

          - `CreatedBy AutomationCreatedByUnion`

            Service-recorded provenance; callers cannot supply this field.

          - `Metadata map[string, string]`

            Custom string key-value pairs attached to the automation.

          - `Name string`

            The automation's display name.

            `minLength: 0`

          - `Object AgentAutomation`

            Always `agent.automation`.

            - `const AgentAutomationAgentAutomation AgentAutomation = "agent.automation"`

          - `RunAt int64`

            The Unix timestamp, in seconds, of the scheduled occurrence.

            `format: int64`

          - `Status OneTimeAutomationStatus`

            Completion means the schedule has finished, not the agent's work.

            - `const OneTimeAutomationStatusActive OneTimeAutomationStatus = "active"`

            - `const OneTimeAutomationStatusPaused OneTimeAutomationStatus = "paused"`

            - `const OneTimeAutomationStatusCompleted OneTimeAutomationStatus = "completed"`

          - `Target AutomationTargetUnion`

            The session configuration or existing session receiving invocations.

          - `Type Once`

            The type of the object. Always `once`.

            - `const OnceOnce Once = "once"`

      - `Type Automation`

        The type of the object. Always `automation`.

        - `const AutomationAutomation Automation = "automation"`

  - `Status AutomationInvocationStatus`

    Delivery status; completed does not mean the agent's work has finished.

    - `const AutomationInvocationStatusQueued AutomationInvocationStatus = "queued"`

    - `const AutomationInvocationStatusCompleted AutomationInvocationStatus = "completed"`

    - `const AutomationInvocationStatusFailed AutomationInvocationStatus = "failed"`

    - `const AutomationInvocationStatusSkipped AutomationInvocationStatus = "skipped"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  automationInvocation, err := client.Beta.Agents.Automations.Invocations.Get(
    context.TODO(),
    "automation_id",
    "invocation_id",
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", automationInvocation.ID)
}
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

- `type AutomationInvocation struct{…}`

  One attempted delivery by an automation.

  - `ID string`

    The invocation ID.

    `minLength: 0`

  - `AutomationID string`

    The automation that owns the invocation.

    `minLength: 0`

  - `CreatedAt int64`

    The creation time as a Unix timestamp in seconds.

    `format: int64`

  - `Error AutomationInvocationError`

    The permanent delivery failure, or null when no failure occurred.

    - `Code string`

      A machine-readable error code.

      `minLength: 0`

    - `Message string`

      A public explanation of the delivery failure.

      `minLength: 0`

  - `Object AgentAutomationInvocation`

    Always `agent.automation.invocation`.

    - `const AgentAutomationInvocationAgentAutomationInvocation AgentAutomationInvocation = "agent.automation.invocation"`

  - `ScheduledAt int64`

    The intended occurrence as a Unix timestamp in seconds, or null for manual runs.

    `format: int64`

  - `SessionID string`

    The target or newly created session ID, or null before one is available.

    `minLength: 0`

  - `SkipReason PendingDelivery`

    Why an occurrence was skipped, or null when it was not skipped.

    - `const PendingDeliveryPendingDelivery PendingDelivery = "pending_delivery"`

  - `Source AutomationInvocationSourceUnion`

    Whether the invocation was manual or scheduled.

    - `type AutomationInvocationSourceManual struct{…}`

      - `Type Manual`

        The type of the object. Always `manual`.

        - `const ManualManual Manual = "manual"`

    - `type AutomationInvocationSourceAutomation struct{…}`

      - `Automation AutomationUnion`

        The automation snapshot for this occurrence, excluding confidential values.

        - `type PeriodicAutomation struct{…}`

          Fields shared by periodic and one-time automations.

          - `ID string`

            The automation ID.

            `minLength: 0`

          - `CreatedAt int64`

            The creation time as a Unix timestamp in seconds.

            `format: int64`

          - `CreatedBy AutomationCreatedByUnion`

            Service-recorded provenance; callers cannot supply this field.

            - `type AutomationCreatedByDeveloper struct{…}`

              - `Type Developer`

                The type of the object. Always `developer`.

                - `const DeveloperDeveloper Developer = "developer"`

            - `type AutomationCreatedByAgent struct{…}`

              - `SessionID string`

                The creator session, which is also the automation's target.

                `minLength: 0`

              - `ToolCallID string`

                The tool call that created the automation.

                `minLength: 0`

              - `Type Agent`

                The type of the object. Always `agent`.

                - `const AgentAgent Agent = "agent"`

          - `Expression string`

            The cron expression determining scheduled occurrences.

            `minLength: 0`

          - `Metadata map[string, string]`

            Custom string key-value pairs attached to the automation.

          - `Name string`

            The automation's display name.

            `minLength: 0`

          - `Object AgentAutomation`

            Always `agent.automation`.

            - `const AgentAutomationAgentAutomation AgentAutomation = "agent.automation"`

          - `Status PeriodicAutomationStatus`

            Whether scheduled delivery is active or paused.

            - `const PeriodicAutomationStatusActive PeriodicAutomationStatus = "active"`

            - `const PeriodicAutomationStatusPaused PeriodicAutomationStatus = "paused"`

          - `Target AutomationTargetUnion`

            The session configuration or existing session receiving invocations.

            - `type AutomationTargetNewSession struct{…}`

              - `Agent AutomationAgentConfig`

                The inline agent configuration, or null when agent_id is configured.

                - `Instructions string`

                  Custom instructions, or null when absent.

                  `minLength: 0`

                - `Model string`

                  The requested model name.

                  `minLength: 0`

                - `MultiAgent MultiAgentConfig`

                  The configuration for creating and coordinating subagents.

                  - `Enabled bool`

                    Whether subagent tools are enabled. Defaults to false.

                  - `MaxConcurrentSubagents int64`

                    Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

                    `format: int64`, `minimum: 1`, `maximum: 4294967295`

                - `Reasoning AgentReasoning`

                  The configured reasoning policy.

                  - `Effort AgentReasoningEffort`

                    The requested reasoning effort, or `null` when the model selects its own default.

                    - `const AgentReasoningEffortNone AgentReasoningEffort = "none"`

                    - `const AgentReasoningEffortMinimal AgentReasoningEffort = "minimal"`

                    - `const AgentReasoningEffortLow AgentReasoningEffort = "low"`

                    - `const AgentReasoningEffortMedium AgentReasoningEffort = "medium"`

                    - `const AgentReasoningEffortHigh AgentReasoningEffort = "high"`

                    - `const AgentReasoningEffortXhigh AgentReasoningEffort = "xhigh"`

                    - `const AgentReasoningEffortMax AgentReasoningEffort = "max"`

                  - `Summary AgentReasoningSummary`

                    The requested reasoning summary format, or `null` when summaries are disabled.

                    - `const AgentReasoningSummaryConcise AgentReasoningSummary = "concise"`

                      Returns a concise reasoning summary when supported.

                    - `const AgentReasoningSummaryDetailed AgentReasoningSummary = "detailed"`

                      Returns a detailed reasoning summary when supported.

                    - `const AgentReasoningSummaryAuto AgentReasoningSummary = "auto"`

                      Automatically selects the most detailed summary supported by the model.

                - `ServiceTier AutomationAgentConfigServiceTier`

                  The configured service-tier policy.

                  - `const AutomationAgentConfigServiceTierAuto AutomationAgentConfigServiceTier = "auto"`

                  - `const AutomationAgentConfigServiceTierDefault AutomationAgentConfigServiceTier = "default"`

                  - `const AutomationAgentConfigServiceTierFlex AutomationAgentConfigServiceTier = "flex"`

                  - `const AutomationAgentConfigServiceTierPriority AutomationAgentConfigServiceTier = "priority"`

                  - `const AutomationAgentConfigServiceTierFast AutomationAgentConfigServiceTier = "fast"`

                  - `const AutomationAgentConfigServiceTierUltrafast AutomationAgentConfigServiceTier = "ultrafast"`

                - `Text AgentText`

                  The configured output format and verbosity.

                  - `Format TextFormatUnion`

                    The effective output format. Defaults to ordinary text.

                    - `type TextFormatText struct{…}`

                      Generates ordinary text without a structured-output constraint.

                      - `Type Text`

                        The type of the object. Always `text`.

                        - `const TextText Text = "text"`

                    - `type TextFormatJSONSchema struct{…}`

                      Constrains generated text to a JSON Schema.

                      - `Schema map[string, any]`

                        The JSON Schema that generated text must match.

                      - `Type JSONSchema`

                        The type of the object. Always `json_schema`.

                        - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

                  - `Verbosity AgentTextVerbosity`

                    The amount of text produced by the agent. Defaults to `medium`.

                    - `const AgentTextVerbosityLow AgentTextVerbosity = "low"`

                    - `const AgentTextVerbosityMedium AgentTextVerbosity = "medium"`

                    - `const AgentTextVerbosityHigh AgentTextVerbosity = "high"`

                - `Tools []AgentToolUnion`

                  Configured tools, excluding confidential credentials.

                  `minItems: 0`, `maxItems: 2000`

                  - `type AgentToolFunction struct{…}`

                    A function defined by the application.

                    - `DeferLoading bool`

                      Whether the function is deferred and discovered through tool search.

                    - `Description string`

                      A description of what the function does.

                      `minLength: 0`

                    - `Name string`

                      The name of the function.

                      `minLength: 0`

                    - `Parameters map[string, any]`

                      A JSON Schema object describing the function's arguments.

                    - `Type Function`

                      The type of the object. Always `function`.

                      - `const FunctionFunction Function = "function"`

                    - `Async bool`

                      Whether the agent continues without waiting for the function result.

                  - `type AgentToolProgrammaticToolCalling struct{…}`

                    Enables calling tools from model-generated code.

                    - `Enabled bool`

                      Whether tools can be called from model-generated code.

                    - `Type ProgrammaticToolCalling`

                      The type of the object. Always `programmatic_tool_calling`.

                      - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

                  - `type AgentToolMcp struct{…}`

                    Tools provided by a remote MCP server.

                    - `AllowedTools []string`

                      The MCP tools the agent may call.

                      `minItems: 0`, `maxItems: 2000`

                    - `ConnectionOrigin string`

                      Where outbound MCP HTTP connections originate.

                      - `const AgentToolMcpConnectionOriginService AgentToolMcpConnectionOrigin = "service"`

                      - `const AgentToolMcpConnectionOriginEnvironment AgentToolMcpConnectionOrigin = "environment"`

                    - `CredentialID string`

                      The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

                      `minLength: 0`

                    - `RequestMetadata map[string, any]`

                      Metadata included with requests to this MCP server.

                    - `Required bool`

                      Whether this MCP server must initialize before the first turn.

                    - `ServerLabel string`

                      A label used to identify the MCP server in tool calls.

                      `minLength: 0`

                    - `Transport McpTransportUnion`

                      The transport used to connect to the MCP server.

                      - `type McpTransportHTTP struct{…}`

                        Connects to an MCP server over HTTP.

                        - `ServerURL string`

                          The URL of the MCP server.

                          `minLength: 0`

                        - `Type HTTP`

                          The type of the object. Always `http`.

                          - `const HTTPHTTP HTTP = "http"`

                      - `type McpTransportStdio struct{…}`

                        Starts an MCP server as a local process.

                        - `Args []string`

                          Arguments passed to the MCP server command.

                          `minItems: 0`, `maxItems: 2000`

                        - `Command string`

                          The command used to start the MCP server.

                          `minLength: 0`

                        - `Cwd string`

                          The working directory used to start the MCP server.

                          `minLength: 0`

                        - `EnvVars []string`

                          Environment variable names inherited from the execution environment.

                          `minItems: 0`, `maxItems: 2000`

                        - `Type Stdio`

                          The type of the object. Always `stdio`.

                          - `const StdioStdio Stdio = "stdio"`

                    - `Type Mcp`

                      The type of the object. Always `mcp`.

                      - `const McpMcp Mcp = "mcp"`

                  - `type AgentToolWebSearch struct{…}`

                    Web search.

                    - `AllowedDomains []string`

                      Allowed search domains, or `null` when the search is unrestricted.

                      `minItems: 0`, `maxItems: 2000`

                    - `ContextSize string`

                      The amount of search context made available to the model. Defaults to `medium`.

                      - `const AgentToolWebSearchContextSizeLow AgentToolWebSearchContextSize = "low"`

                      - `const AgentToolWebSearchContextSizeMedium AgentToolWebSearchContextSize = "medium"`

                      - `const AgentToolWebSearchContextSizeHigh AgentToolWebSearchContextSize = "high"`

                    - `Location AgentToolWebSearchLocation`

                      Approximate location used to localize search results, if provided.

                      - `City string`

                        The city name.

                        `minLength: 0`

                      - `Country string`

                        The two-letter ISO country code, such as `US`.

                        `minLength: 0`

                      - `Region string`

                        The region or state name.

                        `minLength: 0`

                      - `Timezone string`

                        The IANA timezone, such as `America/Los_Angeles`.

                        `minLength: 0`

                    - `Mode string`

                      The source used for web search results.

                      - `const AgentToolWebSearchModeDisabled AgentToolWebSearchMode = "disabled"`

                      - `const AgentToolWebSearchModeCached AgentToolWebSearchMode = "cached"`

                      - `const AgentToolWebSearchModeLive AgentToolWebSearchMode = "live"`

                    - `Type WebSearch`

                      The type of the object. Always `web_search`.

                      - `const WebSearchWebSearch WebSearch = "web_search"`

                  - `type AgentToolComputerUse struct{…}`

                    Browser use in an OpenAI-hosted session.

                    - `IncludeScreenshots bool`

                      Whether computer tool outputs include screenshots.

                    - `Type ComputerUse`

                      The type of the object. Always `computer_use`.

                      - `const ComputerUseComputerUse ComputerUse = "computer_use"`

                  - `type AgentToolAutomations struct{…}`

                    Lets the agent manage its own scheduled wakeups.

                    - `Type Automations`

                      The type of the object. Always `automations`.

                      - `const AutomationsAutomations Automations = "automations"`

                - `Compaction AutomationAgentConfigCompaction`

                  The effective context compaction settings.

                  - `Async bool`

                    Whether context is compacted in the background. Defaults to true.

                - `Experimental AutomationAgentConfigExperimental`

                  The effective experimental settings for the agent.

                  - `TimeAwareness bool`

                    Whether the model receives periodic current-time reminders.

              - `AgentID string`

                The saved agent reference, or null when an inline agent is configured.

                `minLength: 0`

              - `Environment AutomationEnvironmentUnion`

                Configuration or references used to select the execution environment.

                - `type AutomationEnvironmentNone struct{…}`

                  - `Type None`

                    The type of the object. Always `none`.

                    - `const NoneNone None = "none"`

                - `type AutomationEnvironmentOpenAIHosted struct{…}`

                  Hosted environment selection with confidential setup commands and variables omitted.

                  - `CapabilityDirectories []string`

                    Directory overrides, or null to inherit the template or creation default.

                    `minItems: 0`, `maxItems: 2000`

                  - `ContainerSize string`

                    The configured container size, or null to use the creation default.

                    - `const AutomationEnvironmentOpenAIHostedContainerSizeSmall AutomationEnvironmentOpenAIHostedContainerSize = "small"`

                    - `const AutomationEnvironmentOpenAIHostedContainerSizeMedium AutomationEnvironmentOpenAIHostedContainerSize = "medium"`

                    - `const AutomationEnvironmentOpenAIHostedContainerSizeLarge AutomationEnvironmentOpenAIHostedContainerSize = "large"`

                  - `Desktop AutomationEnvironmentOpenAIHostedDesktop`

                    Desktop overrides, or null to inherit the template or creation default.

                    - `Enabled bool`

                      Whether the environment provisions a desktop and browser proxy.

                  - `EnvironmentID string`

                    An existing environment reference, or null when provisioning a new environment.

                    `minLength: 0`

                  - `EnvironmentTemplateID string`

                    A template reference, or null when no template is selected.

                    `minLength: 0`

                  - `Files []AutomationEnvironmentOpenAIHostedFileUnion`

                    File overrides, excluding contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `type AutomationEnvironmentOpenAIHostedFileFileID struct{…}`

                      A project-scoped Files API reference resolved separately for each session.

                      - `FileID string`

                        The ID of the uploaded file.

                        `minLength: 0`

                      - `Path string`

                        The file's absolute path inside the environment.

                        `minLength: 0`

                      - `Type FileID`

                        The type of the object. Always `file_id`.

                        - `const FileIDFileID FileID = "file_id"`

                    - `type AutomationEnvironmentOpenAIHostedFileInline struct{…}`

                      Metadata for confidential inline file contents.

                      - `Path string`

                        The file's absolute path inside the environment.

                        `minLength: 0`

                      - `SizeBytes int64`

                        The decoded size of the inline file in bytes.

                        `format: int64`, `minimum: 0`

                      - `Type Inline`

                        The type of the object. Always `inline`.

                        - `const InlineInline Inline = "inline"`

                  - `Network AutomationEnvironmentOpenAIHostedNetwork`

                    Network overrides, or null to inherit the template or creation default.

                    - `Access string`

                      The environment's network access mode.

                      - `const AutomationEnvironmentOpenAIHostedNetworkAccessEnabled AutomationEnvironmentOpenAIHostedNetworkAccess = "enabled"`

                        Allows unrestricted network access.

                      - `const AutomationEnvironmentOpenAIHostedNetworkAccessDisabled AutomationEnvironmentOpenAIHostedNetworkAccess = "disabled"`

                        Disables network access.

                      - `const AutomationEnvironmentOpenAIHostedNetworkAccessRestricted AutomationEnvironmentOpenAIHostedNetworkAccess = "restricted"`

                        Applies the configured domain restrictions.

                    - `AllowedDomains []string`

                      Domains the environment may access when network access is restricted.

                      `minItems: 0`, `maxItems: 2000`

                  - `Packages AutomationEnvironmentOpenAIHostedPackages`

                    Package overrides, or null to inherit the template or creation default.

                    - `Npm []string`

                      npm packages installed globally in the environment.

                      `minItems: 0`, `maxItems: 16384`

                    - `Python []string`

                      Python packages installed in the environment.

                      `minItems: 0`, `maxItems: 16384`

                    - `System []string`

                      System packages installed in the environment.

                      `minItems: 0`, `maxItems: 16384`

                  - `Plugins []HostedPlugin`

                    Plugin overrides, excluding archive contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `Description string`

                      The installed plugin description.

                      `minLength: 0`

                    - `Name string`

                      The installed plugin name.

                      `minLength: 0`

                    - `Type Inline`

                      The type of the object. Always `inline`.

                      - `const InlineInline Inline = "inline"`

                  - `Skills []AutomationEnvironmentOpenAIHostedSkillUnion`

                    Skill overrides, excluding archive contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `type AutomationEnvironmentOpenAIHostedSkillSkillReference struct{…}`

                      A skill resolved afresh from the Skills API whenever a session starts.

                      - `SkillID string`

                        The referenced skill ID.

                        `minLength: 0`

                      - `Type SkillReference`

                        The type of the object. Always `skill_reference`.

                        - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

                      - `Version string`

                        The requested version selector, including `latest`.

                        `minLength: 0`

                    - `type AutomationEnvironmentOpenAIHostedSkillInline struct{…}`

                      Safe metadata for an inline skill archive.

                      - `Description string`

                        The skill description declared in `SKILL.md`.

                        `minLength: 0`

                      - `Name string`

                        The skill name declared in `SKILL.md`.

                        `minLength: 0`

                      - `Type Inline`

                        The type of the object. Always `inline`.

                        - `const InlineInline Inline = "inline"`

                  - `Type OpenAIHosted`

                    The type of the object. Always `openai_hosted`.

                    - `const OpenAIHostedOpenAIHosted OpenAIHosted = "openai_hosted"`

                - `type AutomationEnvironmentSelfHosted struct{…}`

                  - `CapabilityDirectories []string`

                    Directories that expose capabilities to the agent.

                    `minItems: 0`, `maxItems: 2000`

                  - `EnvironmentID string`

                    An existing registration, or null to create a session-owned environment.

                    `minLength: 0`

                  - `Type SelfHosted`

                    The type of the object. Always `self_hosted`.

                    - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

                  - `WorkspaceDirectory string`

                    The absolute project directory in the environment.

                    `minLength: 0`

              - `Input []AutomationTargetNewSessionInput`

                Initial input delivered to each new session.

                `minItems: 0`, `maxItems: 2000`

                - `Content []InputContentUnion`

                  The content of the message.

                  `minItems: 0`, `maxItems: 2000`

                  - `type InputContentInputText struct{…}`

                    Text input recorded in a session item.

                    - `Text string`

                      The text supplied to the agent.

                      `minLength: 0`

                    - `Type InputText`

                      The type of the object. Always `input_text`.

                      - `const InputTextInputText InputText = "input_text"`

                  - `type InputContentInputImage struct{…}`

                    Image input recorded in a session item.

                    - `ImageURL string`

                      The URL of the image supplied to the agent, which may be a base64-encoded data URL.

                      `minLength: 0`

                    - `Type InputImage`

                      The type of the object. Always `input_image`.

                      - `const InputImageInputImage InputImage = "input_image"`

                - `Role User`

                  The role of the message author. Always `user`.

                  - `const UserUser User = "user"`

                - `Type Message`

                  The type of the input item. Always `message`.

                  - `const MessageMessage Message = "message"`

              - `Metadata map[string, string]`

                Metadata attached to each new session.

              - `Type NewSession`

                The type of the object. Always `new_session`.

                - `const NewSessionNewSession NewSession = "new_session"`

              - `VaultIDs []string`

                Vaults made available to each new session.

                `minItems: 0`, `maxItems: 2000`

            - `type AutomationTargetExistingSession struct{…}`

              - `Instructions string`

                Saved instructions delivered as an automation notification.

                `minLength: 0`

              - `SessionID string`

                The session receiving each invocation.

                `minLength: 0`

              - `Type ExistingSession`

                The type of the object. Always `existing_session`.

                - `const ExistingSessionExistingSession ExistingSession = "existing_session"`

          - `Timezone string`

            The timezone used to interpret the expression.

            `minLength: 0`

          - `Type Periodic`

            The type of the object. Always `periodic`.

            - `const PeriodicPeriodic Periodic = "periodic"`

        - `type OneTimeAutomation struct{…}`

          Fields shared by periodic and one-time automations.

          - `ID string`

            The automation ID.

            `minLength: 0`

          - `CreatedAt int64`

            The creation time as a Unix timestamp in seconds.

            `format: int64`

          - `CreatedBy AutomationCreatedByUnion`

            Service-recorded provenance; callers cannot supply this field.

          - `Metadata map[string, string]`

            Custom string key-value pairs attached to the automation.

          - `Name string`

            The automation's display name.

            `minLength: 0`

          - `Object AgentAutomation`

            Always `agent.automation`.

            - `const AgentAutomationAgentAutomation AgentAutomation = "agent.automation"`

          - `RunAt int64`

            The Unix timestamp, in seconds, of the scheduled occurrence.

            `format: int64`

          - `Status OneTimeAutomationStatus`

            Completion means the schedule has finished, not the agent's work.

            - `const OneTimeAutomationStatusActive OneTimeAutomationStatus = "active"`

            - `const OneTimeAutomationStatusPaused OneTimeAutomationStatus = "paused"`

            - `const OneTimeAutomationStatusCompleted OneTimeAutomationStatus = "completed"`

          - `Target AutomationTargetUnion`

            The session configuration or existing session receiving invocations.

          - `Type Once`

            The type of the object. Always `once`.

            - `const OnceOnce Once = "once"`

      - `Type Automation`

        The type of the object. Always `automation`.

        - `const AutomationAutomation Automation = "automation"`

  - `Status AutomationInvocationStatus`

    Delivery status; completed does not mean the agent's work has finished.

    - `const AutomationInvocationStatusQueued AutomationInvocationStatus = "queued"`

    - `const AutomationInvocationStatusCompleted AutomationInvocationStatus = "completed"`

    - `const AutomationInvocationStatusFailed AutomationInvocationStatus = "failed"`

    - `const AutomationInvocationStatusSkipped AutomationInvocationStatus = "skipped"`

### Automation Invocation Source

- `type AutomationInvocationSourceUnion interface{…}`

  - `type AutomationInvocationSourceManual struct{…}`

    - `Type Manual`

      The type of the object. Always `manual`.

      - `const ManualManual Manual = "manual"`

  - `type AutomationInvocationSourceAutomation struct{…}`

    - `Automation AutomationUnion`

      The automation snapshot for this occurrence, excluding confidential values.

      - `type PeriodicAutomation struct{…}`

        Fields shared by periodic and one-time automations.

        - `ID string`

          The automation ID.

          `minLength: 0`

        - `CreatedAt int64`

          The creation time as a Unix timestamp in seconds.

          `format: int64`

        - `CreatedBy AutomationCreatedByUnion`

          Service-recorded provenance; callers cannot supply this field.

          - `type AutomationCreatedByDeveloper struct{…}`

            - `Type Developer`

              The type of the object. Always `developer`.

              - `const DeveloperDeveloper Developer = "developer"`

          - `type AutomationCreatedByAgent struct{…}`

            - `SessionID string`

              The creator session, which is also the automation's target.

              `minLength: 0`

            - `ToolCallID string`

              The tool call that created the automation.

              `minLength: 0`

            - `Type Agent`

              The type of the object. Always `agent`.

              - `const AgentAgent Agent = "agent"`

        - `Expression string`

          The cron expression determining scheduled occurrences.

          `minLength: 0`

        - `Metadata map[string, string]`

          Custom string key-value pairs attached to the automation.

        - `Name string`

          The automation's display name.

          `minLength: 0`

        - `Object AgentAutomation`

          Always `agent.automation`.

          - `const AgentAutomationAgentAutomation AgentAutomation = "agent.automation"`

        - `Status PeriodicAutomationStatus`

          Whether scheduled delivery is active or paused.

          - `const PeriodicAutomationStatusActive PeriodicAutomationStatus = "active"`

          - `const PeriodicAutomationStatusPaused PeriodicAutomationStatus = "paused"`

        - `Target AutomationTargetUnion`

          The session configuration or existing session receiving invocations.

          - `type AutomationTargetNewSession struct{…}`

            - `Agent AutomationAgentConfig`

              The inline agent configuration, or null when agent_id is configured.

              - `Instructions string`

                Custom instructions, or null when absent.

                `minLength: 0`

              - `Model string`

                The requested model name.

                `minLength: 0`

              - `MultiAgent MultiAgentConfig`

                The configuration for creating and coordinating subagents.

                - `Enabled bool`

                  Whether subagent tools are enabled. Defaults to false.

                - `MaxConcurrentSubagents int64`

                  Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

                  `format: int64`, `minimum: 1`, `maximum: 4294967295`

              - `Reasoning AgentReasoning`

                The configured reasoning policy.

                - `Effort AgentReasoningEffort`

                  The requested reasoning effort, or `null` when the model selects its own default.

                  - `const AgentReasoningEffortNone AgentReasoningEffort = "none"`

                  - `const AgentReasoningEffortMinimal AgentReasoningEffort = "minimal"`

                  - `const AgentReasoningEffortLow AgentReasoningEffort = "low"`

                  - `const AgentReasoningEffortMedium AgentReasoningEffort = "medium"`

                  - `const AgentReasoningEffortHigh AgentReasoningEffort = "high"`

                  - `const AgentReasoningEffortXhigh AgentReasoningEffort = "xhigh"`

                  - `const AgentReasoningEffortMax AgentReasoningEffort = "max"`

                - `Summary AgentReasoningSummary`

                  The requested reasoning summary format, or `null` when summaries are disabled.

                  - `const AgentReasoningSummaryConcise AgentReasoningSummary = "concise"`

                    Returns a concise reasoning summary when supported.

                  - `const AgentReasoningSummaryDetailed AgentReasoningSummary = "detailed"`

                    Returns a detailed reasoning summary when supported.

                  - `const AgentReasoningSummaryAuto AgentReasoningSummary = "auto"`

                    Automatically selects the most detailed summary supported by the model.

              - `ServiceTier AutomationAgentConfigServiceTier`

                The configured service-tier policy.

                - `const AutomationAgentConfigServiceTierAuto AutomationAgentConfigServiceTier = "auto"`

                - `const AutomationAgentConfigServiceTierDefault AutomationAgentConfigServiceTier = "default"`

                - `const AutomationAgentConfigServiceTierFlex AutomationAgentConfigServiceTier = "flex"`

                - `const AutomationAgentConfigServiceTierPriority AutomationAgentConfigServiceTier = "priority"`

                - `const AutomationAgentConfigServiceTierFast AutomationAgentConfigServiceTier = "fast"`

                - `const AutomationAgentConfigServiceTierUltrafast AutomationAgentConfigServiceTier = "ultrafast"`

              - `Text AgentText`

                The configured output format and verbosity.

                - `Format TextFormatUnion`

                  The effective output format. Defaults to ordinary text.

                  - `type TextFormatText struct{…}`

                    Generates ordinary text without a structured-output constraint.

                    - `Type Text`

                      The type of the object. Always `text`.

                      - `const TextText Text = "text"`

                  - `type TextFormatJSONSchema struct{…}`

                    Constrains generated text to a JSON Schema.

                    - `Schema map[string, any]`

                      The JSON Schema that generated text must match.

                    - `Type JSONSchema`

                      The type of the object. Always `json_schema`.

                      - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

                - `Verbosity AgentTextVerbosity`

                  The amount of text produced by the agent. Defaults to `medium`.

                  - `const AgentTextVerbosityLow AgentTextVerbosity = "low"`

                  - `const AgentTextVerbosityMedium AgentTextVerbosity = "medium"`

                  - `const AgentTextVerbosityHigh AgentTextVerbosity = "high"`

              - `Tools []AgentToolUnion`

                Configured tools, excluding confidential credentials.

                `minItems: 0`, `maxItems: 2000`

                - `type AgentToolFunction struct{…}`

                  A function defined by the application.

                  - `DeferLoading bool`

                    Whether the function is deferred and discovered through tool search.

                  - `Description string`

                    A description of what the function does.

                    `minLength: 0`

                  - `Name string`

                    The name of the function.

                    `minLength: 0`

                  - `Parameters map[string, any]`

                    A JSON Schema object describing the function's arguments.

                  - `Type Function`

                    The type of the object. Always `function`.

                    - `const FunctionFunction Function = "function"`

                  - `Async bool`

                    Whether the agent continues without waiting for the function result.

                - `type AgentToolProgrammaticToolCalling struct{…}`

                  Enables calling tools from model-generated code.

                  - `Enabled bool`

                    Whether tools can be called from model-generated code.

                  - `Type ProgrammaticToolCalling`

                    The type of the object. Always `programmatic_tool_calling`.

                    - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

                - `type AgentToolMcp struct{…}`

                  Tools provided by a remote MCP server.

                  - `AllowedTools []string`

                    The MCP tools the agent may call.

                    `minItems: 0`, `maxItems: 2000`

                  - `ConnectionOrigin string`

                    Where outbound MCP HTTP connections originate.

                    - `const AgentToolMcpConnectionOriginService AgentToolMcpConnectionOrigin = "service"`

                    - `const AgentToolMcpConnectionOriginEnvironment AgentToolMcpConnectionOrigin = "environment"`

                  - `CredentialID string`

                    The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

                    `minLength: 0`

                  - `RequestMetadata map[string, any]`

                    Metadata included with requests to this MCP server.

                  - `Required bool`

                    Whether this MCP server must initialize before the first turn.

                  - `ServerLabel string`

                    A label used to identify the MCP server in tool calls.

                    `minLength: 0`

                  - `Transport McpTransportUnion`

                    The transport used to connect to the MCP server.

                    - `type McpTransportHTTP struct{…}`

                      Connects to an MCP server over HTTP.

                      - `ServerURL string`

                        The URL of the MCP server.

                        `minLength: 0`

                      - `Type HTTP`

                        The type of the object. Always `http`.

                        - `const HTTPHTTP HTTP = "http"`

                    - `type McpTransportStdio struct{…}`

                      Starts an MCP server as a local process.

                      - `Args []string`

                        Arguments passed to the MCP server command.

                        `minItems: 0`, `maxItems: 2000`

                      - `Command string`

                        The command used to start the MCP server.

                        `minLength: 0`

                      - `Cwd string`

                        The working directory used to start the MCP server.

                        `minLength: 0`

                      - `EnvVars []string`

                        Environment variable names inherited from the execution environment.

                        `minItems: 0`, `maxItems: 2000`

                      - `Type Stdio`

                        The type of the object. Always `stdio`.

                        - `const StdioStdio Stdio = "stdio"`

                  - `Type Mcp`

                    The type of the object. Always `mcp`.

                    - `const McpMcp Mcp = "mcp"`

                - `type AgentToolWebSearch struct{…}`

                  Web search.

                  - `AllowedDomains []string`

                    Allowed search domains, or `null` when the search is unrestricted.

                    `minItems: 0`, `maxItems: 2000`

                  - `ContextSize string`

                    The amount of search context made available to the model. Defaults to `medium`.

                    - `const AgentToolWebSearchContextSizeLow AgentToolWebSearchContextSize = "low"`

                    - `const AgentToolWebSearchContextSizeMedium AgentToolWebSearchContextSize = "medium"`

                    - `const AgentToolWebSearchContextSizeHigh AgentToolWebSearchContextSize = "high"`

                  - `Location AgentToolWebSearchLocation`

                    Approximate location used to localize search results, if provided.

                    - `City string`

                      The city name.

                      `minLength: 0`

                    - `Country string`

                      The two-letter ISO country code, such as `US`.

                      `minLength: 0`

                    - `Region string`

                      The region or state name.

                      `minLength: 0`

                    - `Timezone string`

                      The IANA timezone, such as `America/Los_Angeles`.

                      `minLength: 0`

                  - `Mode string`

                    The source used for web search results.

                    - `const AgentToolWebSearchModeDisabled AgentToolWebSearchMode = "disabled"`

                    - `const AgentToolWebSearchModeCached AgentToolWebSearchMode = "cached"`

                    - `const AgentToolWebSearchModeLive AgentToolWebSearchMode = "live"`

                  - `Type WebSearch`

                    The type of the object. Always `web_search`.

                    - `const WebSearchWebSearch WebSearch = "web_search"`

                - `type AgentToolComputerUse struct{…}`

                  Browser use in an OpenAI-hosted session.

                  - `IncludeScreenshots bool`

                    Whether computer tool outputs include screenshots.

                  - `Type ComputerUse`

                    The type of the object. Always `computer_use`.

                    - `const ComputerUseComputerUse ComputerUse = "computer_use"`

                - `type AgentToolAutomations struct{…}`

                  Lets the agent manage its own scheduled wakeups.

                  - `Type Automations`

                    The type of the object. Always `automations`.

                    - `const AutomationsAutomations Automations = "automations"`

              - `Compaction AutomationAgentConfigCompaction`

                The effective context compaction settings.

                - `Async bool`

                  Whether context is compacted in the background. Defaults to true.

              - `Experimental AutomationAgentConfigExperimental`

                The effective experimental settings for the agent.

                - `TimeAwareness bool`

                  Whether the model receives periodic current-time reminders.

            - `AgentID string`

              The saved agent reference, or null when an inline agent is configured.

              `minLength: 0`

            - `Environment AutomationEnvironmentUnion`

              Configuration or references used to select the execution environment.

              - `type AutomationEnvironmentNone struct{…}`

                - `Type None`

                  The type of the object. Always `none`.

                  - `const NoneNone None = "none"`

              - `type AutomationEnvironmentOpenAIHosted struct{…}`

                Hosted environment selection with confidential setup commands and variables omitted.

                - `CapabilityDirectories []string`

                  Directory overrides, or null to inherit the template or creation default.

                  `minItems: 0`, `maxItems: 2000`

                - `ContainerSize string`

                  The configured container size, or null to use the creation default.

                  - `const AutomationEnvironmentOpenAIHostedContainerSizeSmall AutomationEnvironmentOpenAIHostedContainerSize = "small"`

                  - `const AutomationEnvironmentOpenAIHostedContainerSizeMedium AutomationEnvironmentOpenAIHostedContainerSize = "medium"`

                  - `const AutomationEnvironmentOpenAIHostedContainerSizeLarge AutomationEnvironmentOpenAIHostedContainerSize = "large"`

                - `Desktop AutomationEnvironmentOpenAIHostedDesktop`

                  Desktop overrides, or null to inherit the template or creation default.

                  - `Enabled bool`

                    Whether the environment provisions a desktop and browser proxy.

                - `EnvironmentID string`

                  An existing environment reference, or null when provisioning a new environment.

                  `minLength: 0`

                - `EnvironmentTemplateID string`

                  A template reference, or null when no template is selected.

                  `minLength: 0`

                - `Files []AutomationEnvironmentOpenAIHostedFileUnion`

                  File overrides, excluding contents, or null to inherit.

                  `minItems: 0`, `maxItems: 2000`

                  - `type AutomationEnvironmentOpenAIHostedFileFileID struct{…}`

                    A project-scoped Files API reference resolved separately for each session.

                    - `FileID string`

                      The ID of the uploaded file.

                      `minLength: 0`

                    - `Path string`

                      The file's absolute path inside the environment.

                      `minLength: 0`

                    - `Type FileID`

                      The type of the object. Always `file_id`.

                      - `const FileIDFileID FileID = "file_id"`

                  - `type AutomationEnvironmentOpenAIHostedFileInline struct{…}`

                    Metadata for confidential inline file contents.

                    - `Path string`

                      The file's absolute path inside the environment.

                      `minLength: 0`

                    - `SizeBytes int64`

                      The decoded size of the inline file in bytes.

                      `format: int64`, `minimum: 0`

                    - `Type Inline`

                      The type of the object. Always `inline`.

                      - `const InlineInline Inline = "inline"`

                - `Network AutomationEnvironmentOpenAIHostedNetwork`

                  Network overrides, or null to inherit the template or creation default.

                  - `Access string`

                    The environment's network access mode.

                    - `const AutomationEnvironmentOpenAIHostedNetworkAccessEnabled AutomationEnvironmentOpenAIHostedNetworkAccess = "enabled"`

                      Allows unrestricted network access.

                    - `const AutomationEnvironmentOpenAIHostedNetworkAccessDisabled AutomationEnvironmentOpenAIHostedNetworkAccess = "disabled"`

                      Disables network access.

                    - `const AutomationEnvironmentOpenAIHostedNetworkAccessRestricted AutomationEnvironmentOpenAIHostedNetworkAccess = "restricted"`

                      Applies the configured domain restrictions.

                  - `AllowedDomains []string`

                    Domains the environment may access when network access is restricted.

                    `minItems: 0`, `maxItems: 2000`

                - `Packages AutomationEnvironmentOpenAIHostedPackages`

                  Package overrides, or null to inherit the template or creation default.

                  - `Npm []string`

                    npm packages installed globally in the environment.

                    `minItems: 0`, `maxItems: 16384`

                  - `Python []string`

                    Python packages installed in the environment.

                    `minItems: 0`, `maxItems: 16384`

                  - `System []string`

                    System packages installed in the environment.

                    `minItems: 0`, `maxItems: 16384`

                - `Plugins []HostedPlugin`

                  Plugin overrides, excluding archive contents, or null to inherit.

                  `minItems: 0`, `maxItems: 2000`

                  - `Description string`

                    The installed plugin description.

                    `minLength: 0`

                  - `Name string`

                    The installed plugin name.

                    `minLength: 0`

                  - `Type Inline`

                    The type of the object. Always `inline`.

                    - `const InlineInline Inline = "inline"`

                - `Skills []AutomationEnvironmentOpenAIHostedSkillUnion`

                  Skill overrides, excluding archive contents, or null to inherit.

                  `minItems: 0`, `maxItems: 2000`

                  - `type AutomationEnvironmentOpenAIHostedSkillSkillReference struct{…}`

                    A skill resolved afresh from the Skills API whenever a session starts.

                    - `SkillID string`

                      The referenced skill ID.

                      `minLength: 0`

                    - `Type SkillReference`

                      The type of the object. Always `skill_reference`.

                      - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

                    - `Version string`

                      The requested version selector, including `latest`.

                      `minLength: 0`

                  - `type AutomationEnvironmentOpenAIHostedSkillInline struct{…}`

                    Safe metadata for an inline skill archive.

                    - `Description string`

                      The skill description declared in `SKILL.md`.

                      `minLength: 0`

                    - `Name string`

                      The skill name declared in `SKILL.md`.

                      `minLength: 0`

                    - `Type Inline`

                      The type of the object. Always `inline`.

                      - `const InlineInline Inline = "inline"`

                - `Type OpenAIHosted`

                  The type of the object. Always `openai_hosted`.

                  - `const OpenAIHostedOpenAIHosted OpenAIHosted = "openai_hosted"`

              - `type AutomationEnvironmentSelfHosted struct{…}`

                - `CapabilityDirectories []string`

                  Directories that expose capabilities to the agent.

                  `minItems: 0`, `maxItems: 2000`

                - `EnvironmentID string`

                  An existing registration, or null to create a session-owned environment.

                  `minLength: 0`

                - `Type SelfHosted`

                  The type of the object. Always `self_hosted`.

                  - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

                - `WorkspaceDirectory string`

                  The absolute project directory in the environment.

                  `minLength: 0`

            - `Input []AutomationTargetNewSessionInput`

              Initial input delivered to each new session.

              `minItems: 0`, `maxItems: 2000`

              - `Content []InputContentUnion`

                The content of the message.

                `minItems: 0`, `maxItems: 2000`

                - `type InputContentInputText struct{…}`

                  Text input recorded in a session item.

                  - `Text string`

                    The text supplied to the agent.

                    `minLength: 0`

                  - `Type InputText`

                    The type of the object. Always `input_text`.

                    - `const InputTextInputText InputText = "input_text"`

                - `type InputContentInputImage struct{…}`

                  Image input recorded in a session item.

                  - `ImageURL string`

                    The URL of the image supplied to the agent, which may be a base64-encoded data URL.

                    `minLength: 0`

                  - `Type InputImage`

                    The type of the object. Always `input_image`.

                    - `const InputImageInputImage InputImage = "input_image"`

              - `Role User`

                The role of the message author. Always `user`.

                - `const UserUser User = "user"`

              - `Type Message`

                The type of the input item. Always `message`.

                - `const MessageMessage Message = "message"`

            - `Metadata map[string, string]`

              Metadata attached to each new session.

            - `Type NewSession`

              The type of the object. Always `new_session`.

              - `const NewSessionNewSession NewSession = "new_session"`

            - `VaultIDs []string`

              Vaults made available to each new session.

              `minItems: 0`, `maxItems: 2000`

          - `type AutomationTargetExistingSession struct{…}`

            - `Instructions string`

              Saved instructions delivered as an automation notification.

              `minLength: 0`

            - `SessionID string`

              The session receiving each invocation.

              `minLength: 0`

            - `Type ExistingSession`

              The type of the object. Always `existing_session`.

              - `const ExistingSessionExistingSession ExistingSession = "existing_session"`

        - `Timezone string`

          The timezone used to interpret the expression.

          `minLength: 0`

        - `Type Periodic`

          The type of the object. Always `periodic`.

          - `const PeriodicPeriodic Periodic = "periodic"`

      - `type OneTimeAutomation struct{…}`

        Fields shared by periodic and one-time automations.

        - `ID string`

          The automation ID.

          `minLength: 0`

        - `CreatedAt int64`

          The creation time as a Unix timestamp in seconds.

          `format: int64`

        - `CreatedBy AutomationCreatedByUnion`

          Service-recorded provenance; callers cannot supply this field.

        - `Metadata map[string, string]`

          Custom string key-value pairs attached to the automation.

        - `Name string`

          The automation's display name.

          `minLength: 0`

        - `Object AgentAutomation`

          Always `agent.automation`.

          - `const AgentAutomationAgentAutomation AgentAutomation = "agent.automation"`

        - `RunAt int64`

          The Unix timestamp, in seconds, of the scheduled occurrence.

          `format: int64`

        - `Status OneTimeAutomationStatus`

          Completion means the schedule has finished, not the agent's work.

          - `const OneTimeAutomationStatusActive OneTimeAutomationStatus = "active"`

          - `const OneTimeAutomationStatusPaused OneTimeAutomationStatus = "paused"`

          - `const OneTimeAutomationStatusCompleted OneTimeAutomationStatus = "completed"`

        - `Target AutomationTargetUnion`

          The session configuration or existing session receiving invocations.

        - `Type Once`

          The type of the object. Always `once`.

          - `const OnceOnce Once = "once"`

    - `Type Automation`

      The type of the object. Always `automation`.

      - `const AutomationAutomation Automation = "automation"`
