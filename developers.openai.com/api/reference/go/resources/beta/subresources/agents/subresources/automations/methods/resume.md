<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/subresources/automations/methods/resume/ -->

## Resume an automation

`client.Beta.Agents.Automations.Resume(ctx, automationID) (*AutomationUnion, error)`

**post** `/agents/automations/{automation_id}/resume`

Resumes scheduled delivery; one-time automations without a pending invocation require a future run_at.

- `automationID string`

  `minLength: 0`, `maxLength: 1048576`

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

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  automation, err := client.Beta.Agents.Automations.Resume(context.TODO(), "automation_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", automation)

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
