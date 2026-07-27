<!-- source: https://developers.openai.com/api/reference/go/resources/responses/methods/create/ -->
<!-- part of: https://developers.openai.com/api/reference/go/resources/responses/methods/create/ -->

<!-- chunk-start -->

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

string

string

One of the following:

const ToolImageGenerationSize1024x1024 ToolImageGenerationSize = "1024x1024"

const ToolImageGenerationSize1024x1536 ToolImageGenerationSize = "1024x1536"

const ToolImageGenerationSize1536x1024 ToolImageGenerationSize = "1536x1024"

const ToolImageGenerationSizeAuto ToolImageGenerationSize = "auto"

type ToolLocalShell struct{…}

A tool that allows the model to execute shell commands in a local environment.

Type LocalShell

The type of the local shell tool. Always `local_shell`.

type FunctionShellTool struct{…}

A tool that allows the model to execute shell commands.

Type Shell

The type of the shell tool. Always `shell`.

Environment FunctionShellToolEnvironmentUnionOptional

One of the following:

type ContainerAuto struct{…}

Type ContainerAuto

Automatically creates a container for this request

FileIDs []stringOptional

An optional list of uploaded files to make available to your code.

MemoryLimit ContainerAutoMemoryLimitOptional

The memory limit for the container.

One of the following:

const ContainerAutoMemoryLimit1g ContainerAutoMemoryLimit = "1g"

const ContainerAutoMemoryLimit4g ContainerAutoMemoryLimit = "4g"

const ContainerAutoMemoryLimit16g ContainerAutoMemoryLimit = "16g"

const ContainerAutoMemoryLimit64g ContainerAutoMemoryLimit = "64g"

NetworkPolicy ContainerAutoNetworkPolicyUnionOptional

Network access policy for the container.

One of the following:

type ContainerNetworkPolicyDisabled struct{…}

Type Disabled

Disable outbound network access. Always `disabled`.

type ContainerNetworkPolicyAllowlist struct{…}

AllowedDomains []string

A list of allowed domains when type is `allowlist`.

Type Allowlist

Allow outbound network access only to specified domains. Always `allowlist`.

DomainSecrets [][ContainerNetworkPolicyDomainSecret](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))Optional

Optional domain-scoped secrets for allowlisted domains.

Domain string

The domain associated with the secret.

minLength1

Name string

The name of the secret to inject for the domain.

minLength1

Value string

The secret value to inject for the domain.

maxLength10485760

minLength1

Skills []ContainerAutoSkillUnionOptional

An optional list of skills referenced by id or inline data.

One of the following:

type SkillReference struct{…}

SkillID string

The ID of the referenced skill.

maxLength64

minLength1

Type SkillReference

References a skill created with the /v1/skills endpoint.

Version stringOptional

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

type InlineSkill struct{…}

Description string

The description of the skill.

Name string

The name of the skill.

Source [InlineSkillSource](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema))

Inline skill payload

Data string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

MediaType ApplicationZip

The media type of the inline skill payload. Must be `application/zip`.

Type Base64

The type of the inline skill source. Must be `base64`.

Type Inline

Defines an inline skill for this request.

type LocalEnvironment struct{…}

Type Local

Use a local computer environment.

Skills [][LocalSkill](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema))Optional

An optional list of skills.

Description string

The description of the skill.

Name string

The name of the skill.

Path string

The path to the directory containing the skill.

type ContainerReference struct{…}

ContainerID string

The ID of the referenced container.

Type ContainerReference

References a container created with the /v1/containers endpoint

type CustomTool struct{…}

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

Name string

The name of the custom tool, used to identify it in tool calls.

Type Custom

The type of the custom tool. Always `custom`.

DeferLoading boolOptional

Whether this tool should be deferred and discovered via tool search.

Description stringOptional

Optional description of the custom tool, used to provide more context.

Format [CustomToolInputFormatUnion](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))Optional

The input format for the custom tool. Default is unconstrained text.

One of the following:

type CustomToolInputFormatText struct{…}

Unconstrained free-form text.

Type Text

Unconstrained text format. Always `text`.

type CustomToolInputFormatGrammar struct{…}

A grammar defined by the user.

Definition string

The grammar definition.

Syntax string

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

const CustomToolInputFormatGrammarSyntaxLark CustomToolInputFormatGrammarSyntax = "lark"

const CustomToolInputFormatGrammarSyntaxRegex CustomToolInputFormatGrammarSyntax = "regex"

Type Grammar

Grammar format. Always `grammar`.

type NamespaceTool struct{…}

Groups function/custom tools under a shared namespace.

Description string

A description of the namespace shown to the model.

minLength1

Name string

The namespace name used in tool calls (for example, `crm`).

minLength1

Tools []NamespaceToolToolUnion

The function/custom tools available inside this namespace.

One of the following:

type NamespaceToolToolFunction struct{…}

Name string

maxLength128

minLength1

Type Function

DeferLoading boolOptional

Whether this function should be deferred and discovered via tool search.

Description stringOptional

Parameters anyOptional

Strict boolOptional

type CustomTool struct{…}

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

Name string

The name of the custom tool, used to identify it in tool calls.

Type Custom

The type of the custom tool. Always `custom`.

DeferLoading boolOptional

Whether this tool should be deferred and discovered via tool search.

Description stringOptional

Optional description of the custom tool, used to provide more context.

Format [CustomToolInputFormatUnion](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))Optional

The input format for the custom tool. Default is unconstrained text.

One of the following:

type CustomToolInputFormatText struct{…}

Unconstrained free-form text.

Type Text

Unconstrained text format. Always `text`.

type CustomToolInputFormatGrammar struct{…}

A grammar defined by the user.

Definition string

The grammar definition.

Syntax string

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

const CustomToolInputFormatGrammarSyntaxLark CustomToolInputFormatGrammarSyntax = "lark"

const CustomToolInputFormatGrammarSyntaxRegex CustomToolInputFormatGrammarSyntax = "regex"

Type Grammar

Grammar format. Always `grammar`.

Type Namespace

The type of the tool. Always `namespace`.

type ToolSearchTool struct{…}

Hosted or BYOT tool search configuration for deferred tools.

Type ToolSearch

The type of the tool. Always `tool_search`.

Description stringOptional

Description shown to the model for a client-executed tool search tool.

Execution ToolSearchToolExecutionOptional

Whether tool search is executed by the server or by the client.

One of the following:

const ToolSearchToolExecutionServer ToolSearchToolExecution = "server"

const ToolSearchToolExecutionClient ToolSearchToolExecution = "client"

Parameters anyOptional

Parameter schema for a client-executed tool search tool.

type WebSearchPreviewTool struct{…}

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type WebSearchPreviewToolType

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

One of the following:

const WebSearchPreviewToolTypeWebSearchPreview WebSearchPreviewToolType = "web\_search\_preview"

const WebSearchPreviewToolTypeWebSearchPreview2025\_03\_11 WebSearchPreviewToolType = "web\_search\_preview\_2025\_03\_11"

SearchContentTypes []stringOptional

One of the following:

const WebSearchPreviewToolSearchContentTypeText WebSearchPreviewToolSearchContentType = "text"

const WebSearchPreviewToolSearchContentTypeImage WebSearchPreviewToolSearchContentType = "image"

SearchContextSize WebSearchPreviewToolSearchContextSizeOptional

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

const WebSearchPreviewToolSearchContextSizeLow WebSearchPreviewToolSearchContextSize = "low"

const WebSearchPreviewToolSearchContextSizeMedium WebSearchPreviewToolSearchContextSize = "medium"

const WebSearchPreviewToolSearchContextSizeHigh WebSearchPreviewToolSearchContextSize = "high"

UserLocation WebSearchPreviewToolUserLocationOptional

The user’s location.

Type Approximate

The type of location approximation. Always `approximate`.

City stringOptional

Free text input for the city of the user, e.g. `San Francisco`.

Country stringOptional

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Region stringOptional

Free text input for the region of the user, e.g. `California`.

Timezone stringOptional

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type ApplyPatchTool struct{…}

Allows the assistant to create, delete, or update files using unified diffs.

Type ApplyPatch

The type of the tool. Always `apply_patch`.

Type ToolSearchOutput

The type of the item. Always `tool_search_output`.

CreatedBy stringOptional

The identifier of the actor that created the item.

type ResponseOutputItemAdditionalTools struct{…}

ID string

The unique ID of the additional tools item.

Role string

The role that provided the additional tools.

One of the following:

const ResponseOutputItemAdditionalToolsRoleUnknown ResponseOutputItemAdditionalToolsRole = "unknown"

const ResponseOutputItemAdditionalToolsRoleUser ResponseOutputItemAdditionalToolsRole = "user"

const ResponseOutputItemAdditionalToolsRoleAssistant ResponseOutputItemAdditionalToolsRole = "assistant"

const ResponseOutputItemAdditionalToolsRoleSystem ResponseOutputItemAdditionalToolsRole = "system"

const ResponseOutputItemAdditionalToolsRoleCritic ResponseOutputItemAdditionalToolsRole = "critic"

const ResponseOutputItemAdditionalToolsRoleDiscriminator ResponseOutputItemAdditionalToolsRole = "discriminator"

const ResponseOutputItemAdditionalToolsRoleDeveloper ResponseOutputItemAdditionalToolsRole = "developer"

const ResponseOutputItemAdditionalToolsRoleTool ResponseOutputItemAdditionalToolsRole = "tool"

Tools [][ToolUnion](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20tool%20%3E%20(schema))

The additional tool definitions made available at this item.

One of the following:

type FunctionTool struct{…}

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

Name string

The name of the function to call.

Parameters map[string, any]

A JSON schema object describing the parameters of the function.

Strict bool

Whether to enforce strict parameter validation. Default `true`.

Type Function

The type of the function tool. Always `function`.

DeferLoading boolOptional

Whether this function is deferred and loaded via tool search.

Description stringOptional

A description of the function. Used by the model to determine whether or not to call the function.

type FileSearchTool struct{…}

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

Type FileSearch

The type of the file search tool. Always `file_search`.

VectorStoreIDs []string

The IDs of the vector stores to search.

Filters FileSearchToolFiltersUnionOptional

A filter to apply.

One of the following:

type ComparisonFilter struct{…}

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

Key string

The key to compare against the value.

Type ComparisonFilterType

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

One of the following:

const ComparisonFilterTypeEq ComparisonFilterType = "eq"

const ComparisonFilterTypeNe ComparisonFilterType = "ne"

const ComparisonFilterTypeGt ComparisonFilterType = "gt"

const ComparisonFilterTypeGte ComparisonFilterType = "gte"

const ComparisonFilterTypeLt ComparisonFilterType = "lt"

const ComparisonFilterTypeLte ComparisonFilterType = "lte"

const ComparisonFilterTypeIn ComparisonFilterType = "in"

const ComparisonFilterTypeNin ComparisonFilterType = "nin"

Value ComparisonFilterValueUnion

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

string

float64

bool

type ComparisonFilterValueArray []ComparisonFilterValueArrayItemUnion

One of the following:

string

float64

type CompoundFilter struct{…}

Combine multiple filters using `and` or `or`.

Filters [][ComparisonFilter](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema))

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

One of the following:

type ComparisonFilter struct{…}

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

Key string

The key to compare against the value.

Type ComparisonFilterType

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

One of the following:

const ComparisonFilterTypeEq ComparisonFilterType = "eq"

const ComparisonFilterTypeNe ComparisonFilterType = "ne"

const ComparisonFilterTypeGt ComparisonFilterType = "gt"

const ComparisonFilterTypeGte ComparisonFilterType = "gte"

const ComparisonFilterTypeLt ComparisonFilterType = "lt"

const ComparisonFilterTypeLte ComparisonFilterType = "lte"

const ComparisonFilterTypeIn ComparisonFilterType = "in"

const ComparisonFilterTypeNin ComparisonFilterType = "nin"

Value ComparisonFilterValueUnion

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

string

float64

bool

type ComparisonFilterValueArray []ComparisonFilterValueArrayItemUnion

One of the following:

string

float64

Type CompoundFilterType

Type of operation: `and` or `or`.

One of the following:

const CompoundFilterTypeAnd CompoundFilterType = "and"

const CompoundFilterTypeOr CompoundFilterType = "or"

MaxNumResults int64Optional

The maximum number of results to return. This number should be between 1 and 50 inclusive.

RankingOptions FileSearchToolRankingOptionsOptional

Ranking options for search.

HybridSearch FileSearchToolRankingOptionsHybridSearchOptional

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

EmbeddingWeight float64

The weight of the embedding in the reciprocal ranking fusion.

TextWeight float64

The weight of the text in the reciprocal ranking fusion.

Ranker stringOptional

The ranker to use for the file search.

One of the following:

const FileSearchToolRankingOptionsRankerAuto FileSearchToolRankingOptionsRanker = "auto"

const FileSearchToolRankingOptionsRankerDefault2024\_11\_15 FileSearchToolRankingOptionsRanker = "default-2024-11-15"

ScoreThreshold float64Optional

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

type ComputerTool struct{…}

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

Type Computer

The type of the computer tool. Always `computer`.

type ComputerUsePreviewTool struct{…}

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

DisplayHeight int64

The height of the computer display.

DisplayWidth int64

The width of the computer display.

Environment ComputerUsePreviewToolEnvironment

The type of computer environment to control.

One of the following:

const ComputerUsePreviewToolEnvironmentWindows ComputerUsePreviewToolEnvironment = "windows"

const ComputerUsePreviewToolEnvironmentMac ComputerUsePreviewToolEnvironment = "mac"

const ComputerUsePreviewToolEnvironmentLinux ComputerUsePreviewToolEnvironment = "linux"

const ComputerUsePreviewToolEnvironmentUbuntu ComputerUsePreviewToolEnvironment = "ubuntu"

const ComputerUsePreviewToolEnvironmentBrowser ComputerUsePreviewToolEnvironment = "browser"

Type ComputerUsePreview

The type of the computer use tool. Always `computer_use_preview`.

type WebSearchTool struct{…}

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type WebSearchToolType

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

One of the following:

const WebSearchToolTypeWebSearch WebSearchToolType = "web\_search"

const WebSearchToolTypeWebSearch2025\_08\_26 WebSearchToolType = "web\_search\_2025\_08\_26"

Filters WebSearchToolFiltersOptional

Filters for the search.

AllowedDomains []stringOptional

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

SearchContextSize WebSearchToolSearchContextSizeOptional

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

const WebSearchToolSearchContextSizeLow WebSearchToolSearchContextSize = "low"

const WebSearchToolSearchContextSizeMedium WebSearchToolSearchContextSize = "medium"

const WebSearchToolSearchContextSizeHigh WebSearchToolSearchContextSize = "high"

UserLocation WebSearchToolUserLocationOptional

The approximate location of the user.

City stringOptional

Free text input for the city of the user, e.g. `San Francisco`.

Country stringOptional

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Region stringOptional

Free text input for the region of the user, e.g. `California`.

Timezone stringOptional

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

Type stringOptional

The type of location approximation. Always `approximate`.

type ToolMcp struct{…}

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

ServerLabel string

A label for this MCP server, used to identify it in tool calls.

Type Mcp

The type of the MCP tool. Always `mcp`.

AllowedTools ToolMcpAllowedToolsUnionOptional

List of allowed tool names or a filter object.

One of the following:

type ToolMcpAllowedToolsMcpAllowedTools []string

A string array of allowed tool names

type ToolMcpAllowedToolsMcpToolFilter struct{…}

A filter object to specify which tools are allowed.

ReadOnly boolOptional

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

ToolNames []stringOptional

List of allowed tool names.

Authorization stringOptional

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

ConnectorID stringOptional

Identifier for service connectors, like those available in ChatGPT. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided. Learn more
about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

Currently supported `connector_id` values are:

* Dropbox: `connector_dropbox`
* Gmail: `connector_gmail`
* Google Calendar: `connector_googlecalendar`
* Google Drive: `connector_googledrive`
* Microsoft Teams: `connector_microsoftteams`
* Outlook Calendar: `connector_outlookcalendar`
* Outlook Email: `connector_outlookemail`
* SharePoint: `connector_sharepoint`

One of the following:

const ToolMcpConnectorIDConnectorDropbox ToolMcpConnectorID = "connector\_dropbox"

const ToolMcpConnectorIDConnectorGmail ToolMcpConnectorID = "connector\_gmail"

const ToolMcpConnectorIDConnectorGooglecalendar ToolMcpConnectorID = "connector\_googlecalendar"

const ToolMcpConnectorIDConnectorGoogledrive ToolMcpConnectorID = "connector\_googledrive"

const ToolMcpConnectorIDConnectorMicrosoftteams ToolMcpConnectorID = "connector\_microsoftteams"

const ToolMcpConnectorIDConnectorOutlookcalendar ToolMcpConnectorID = "connector\_outlookcalendar"

const ToolMcpConnectorIDConnectorOutlookemail ToolMcpConnectorID = "connector\_outlookemail"

const ToolMcpConnectorIDConnectorSharepoint ToolMcpConnectorID = "connector\_sharepoint"

DeferLoading boolOptional

Whether this MCP tool is deferred and discovered via tool search.

Headers map[string, string]Optional

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

RequireApproval ToolMcpRequireApprovalUnionOptional

Specify which of the MCP server’s tools require approval.

One of the following:

type ToolMcpRequireApprovalMcpToolApprovalFilter struct{…}

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

Always ToolMcpRequireApprovalMcpToolApprovalFilterAlwaysOptional

A filter object to specify which tools are allowed.

ReadOnly boolOptional

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

ToolNames []stringOptional

List of allowed tool names.

Never ToolMcpRequireApprovalMcpToolApprovalFilterNeverOptional

A filter object to specify which tools are allowed.

ReadOnly boolOptional

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

ToolNames []stringOptional

List of allowed tool names.

type ToolMcpRequireApprovalMcpToolApprovalSetting string

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

One of the following:

const ToolMcpRequireApprovalMcpToolApprovalSettingAlways ToolMcpRequireApprovalMcpToolApprovalSetting = "always"

const ToolMcpRequireApprovalMcpToolApprovalSettingNever ToolMcpRequireApprovalMcpToolApprovalSetting = "never"

ServerDescription stringOptional

Optional description of the MCP server, used to provide more context.

ServerURL stringOptional

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

TunnelID stringOptional

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

type ToolCodeInterpreter struct{…}

A tool that runs Python code to help generate a response to a prompt.

Container ToolCodeInterpreterContainerUnion

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

One of the following:

string

type ToolCodeInterpreterContainerCodeInterpreterContainerAuto struct{…}

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

Type Auto

Always `auto`.

FileIDs []stringOptional

An optional list of uploaded files to make available to your code.

MemoryLimit stringOptional

The memory limit for the code interpreter container.

One of the following:

const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit1g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "1g"

const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit4g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "4g"

const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit16g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "16g"

const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit64g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "64g"

NetworkPolicy ToolCodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicyUnionOptional

Network access policy for the container.

One of the following:

type ContainerNetworkPolicyDisabled struct{…}

Type Disabled

Disable outbound network access. Always `disabled`.

type ContainerNetworkPolicyAllowlist struct{…}

AllowedDomains []string

A list of allowed domains when type is `allowlist`.

Type Allowlist

Allow outbound network access only to specified domains. Always `allowlist`.

DomainSecrets [][ContainerNetworkPolicyDomainSecret](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))Optional

Optional domain-scoped secrets for allowlisted domains.

Domain string

The domain associated with the secret.

minLength1

Name string

The name of the secret to inject for the domain.

minLength1

Value string

The secret value to inject for the domain.

maxLength10485760

minLength1

Type CodeInterpreter

The type of the code interpreter tool. Always `code_interpreter`.

type ToolImageGeneration struct{…}

A tool that generates images using the GPT image models.

Type ImageGeneration

The type of the image generation tool. Always `image_generation`.

Action stringOptional

Whether to generate a new image or edit an existing image. Default: `auto`.

One of the following:

const ToolImageGenerationActionGenerate ToolImageGenerationAction = "generate"

const ToolImageGenerationActionEdit ToolImageGenerationAction = "edit"

const ToolImageGenerationActionAuto ToolImageGenerationAction = "auto"

Background stringOptional

Allows to set transparency for the background of the generated image(s).
This parameter is only supported for GPT image models that support
transparent backgrounds. Must be one of `transparent`, `opaque`, or
`auto` (default value). When `auto` is used, the model will
automatically determine the best background for the image.

`gpt-image-2` and `gpt-image-2-2026-04-21` do not support
transparent backgrounds. Requests with `background` set to
`transparent` will return an error for these models; use `opaque` or
`auto` instead.

If `transparent`, the output format needs to support transparency,
so it should be set to either `png` (default value) or `webp`.

One of the following:

const ToolImageGenerationBackgroundTransparent ToolImageGenerationBackground = "transparent"

const ToolImageGenerationBackgroundOpaque ToolImageGenerationBackground = "opaque"

const ToolImageGenerationBackgroundAuto ToolImageGenerationBackground = "auto"

InputFidelity stringOptional

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

One of the following:

const ToolImageGenerationInputFidelityHigh ToolImageGenerationInputFidelity = "high"

const ToolImageGenerationInputFidelityLow ToolImageGenerationInputFidelity = "low"

InputImageMask ToolImageGenerationInputImageMaskOptional

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

FileID stringOptional

File ID for the mask image.

ImageURL stringOptional

Base64-encoded mask image.

Model stringOptional

The image generation model to use. Default: `gpt-image-1`.

One of the following:

string

string

One of the following:

const ToolImageGenerationModelGPTImage1 ToolImageGenerationModel = "gpt-image-1"

const ToolImageGenerationModelGPTImage1Mini ToolImageGenerationModel = "gpt-image-1-mini"

const ToolImageGenerationModelGPTImage2 ToolImageGenerationModel = "gpt-image-2"

const ToolImageGenerationModelGPTImage2\_2026\_04\_21 ToolImageGenerationModel = "gpt-image-2-2026-04-21"

const ToolImageGenerationModelGPTImage1\_5 ToolImageGenerationModel = "gpt-image-1.5"

const ToolImageGenerationModelChatgptImageLatest ToolImageGenerationModel = "chatgpt-image-latest"

Moderation stringOptional

Moderation level for the generated image. Default: `auto`.

One of the following:

const ToolImageGenerationModerationAuto ToolImageGenerationModeration = "auto"

const ToolImageGenerationModerationLow ToolImageGenerationModeration = "low"

OutputCompression int64Optional

Compression level for the output image. Default: 100.

minimum0

maximum100

OutputFormat stringOptional

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

One of the following:

const ToolImageGenerationOutputFormatPNG ToolImageGenerationOutputFormat = "png"

const ToolImageGenerationOutputFormatWebP ToolImageGenerationOutputFormat = "webp"

const ToolImageGenerationOutputFormatJPEG ToolImageGenerationOutputFormat = "jpeg"

PartialImages int64Optional

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

Quality stringOptional

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

One of the following:

const ToolImageGenerationQualityLow ToolImageGenerationQuality = "low"

const ToolImageGenerationQualityMedium ToolImageGenerationQuality = "medium"

const ToolImageGenerationQualityHigh ToolImageGenerationQuality = "high"

const ToolImageGenerationQualityAuto ToolImageGenerationQuality = "auto"

Size stringOptional

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

string

string

One of the following:

const ToolImageGenerationSize1024x1024 ToolImageGenerationSize = "1024x1024"

const ToolImageGenerationSize1024x1536 ToolImageGenerationSize = "1024x1536"

const ToolImageGenerationSize1536x1024 ToolImageGenerationSize = "1536x1024"

const ToolImageGenerationSizeAuto ToolImageGenerationSize = "auto"

type ToolLocalShell struct{…}

A tool that allows the model to execute shell commands in a local environment.

Type LocalShell

The type of the local shell tool. Always `local_shell`.

type FunctionShellTool struct{…}

A tool that allows the model to execute shell commands.

Type Shell

The type of the shell tool. Always `shell`.

Environment FunctionShellToolEnvironmentUnionOptional

One of the following:

type ContainerAuto struct{…}

Type ContainerAuto

Automatically creates a container for this request

FileIDs []stringOptional

An optional list of uploaded files to make available to your code.

MemoryLimit ContainerAutoMemoryLimitOptional

The memory limit for the container.

One of the following:

const ContainerAutoMemoryLimit1g ContainerAutoMemoryLimit = "1g"

const ContainerAutoMemoryLimit4g ContainerAutoMemoryLimit = "4g"

const ContainerAutoMemoryLimit16g ContainerAutoMemoryLimit = "16g"

const ContainerAutoMemoryLimit64g ContainerAutoMemoryLimit = "64g"

NetworkPolicy ContainerAutoNetworkPolicyUnionOptional

Network access policy for the container.

One of the following:

type ContainerNetworkPolicyDisabled struct{…}

Type Disabled

Disable outbound network access. Always `disabled`.

type ContainerNetworkPolicyAllowlist struct{…}

AllowedDomains []string

A list of allowed domains when type is `allowlist`.

Type Allowlist

Allow outbound network access only to specified domains. Always `allowlist`.

DomainSecrets [][ContainerNetworkPolicyDomainSecret](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))Optional

Optional domain-scoped secrets for allowlisted domains.

Domain string

The domain associated with the secret.

minLength1

Name string

The name of the secret to inject for the domain.

minLength1

Value string

The secret value to inject for the domain.

maxLength10485760

minLength1

Skills []ContainerAutoSkillUnionOptional

An optional list of skills referenced by id or inline data.

One of the following:

type SkillReference struct{…}

SkillID string

The ID of the referenced skill.

maxLength64

minLength1

Type SkillReference

References a skill created with the /v1/skills endpoint.

Version stringOptional

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

type InlineSkill struct{…}

Description string

The description of the skill.

Name string

The name of the skill.

Source [InlineSkillSource](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema))

Inline skill payload

Data string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

MediaType ApplicationZip

The media type of the inline skill payload. Must be `application/zip`.

Type Base64

The type of the inline skill source. Must be `base64`.

Type Inline

Defines an inline skill for this request.

type LocalEnvironment struct{…}

Type Local

Use a local computer environment.

Skills [][LocalSkill](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema))Optional

An optional list of skills.

Description string

The description of the skill.

Name string

The name of the skill.

Path string

The path to the directory containing the skill.

type ContainerReference struct{…}

ContainerID string

The ID of the referenced container.

Type ContainerReference

References a container created with the /v1/containers endpoint

type CustomTool struct{…}

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

Name string

The name of the custom tool, used to identify it in tool calls.

Type Custom

The type of the custom tool. Always `custom`.

DeferLoading boolOptional

Whether this tool should be deferred and discovered via tool search.

Description stringOptional

Optional description of the custom tool, used to provide more context.

Format [CustomToolInputFormatUnion](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))Optional

The input format for the custom tool. Default is unconstrained text.

One of the following:

type CustomToolInputFormatText struct{…}

Unconstrained free-form text.

Type Text

Unconstrained text format. Always `text`.

type CustomToolInputFormatGrammar struct{…}

A grammar defined by the user.

Definition string

The grammar definition.

Syntax string

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

const CustomToolInputFormatGrammarSyntaxLark CustomToolInputFormatGrammarSyntax = "lark"

const CustomToolInputFormatGrammarSyntaxRegex CustomToolInputFormatGrammarSyntax = "regex"

Type Grammar

Grammar format. Always `grammar`.

type NamespaceTool struct{…}

Groups function/custom tools under a shared namespace.

Description string

A description of the namespace shown to the model.

minLength1

Name string

The namespace name used in tool calls (for example, `crm`).

minLength1

Tools []NamespaceToolToolUnion

The function/custom tools available inside this namespace.

One of the following:

type NamespaceToolToolFunction struct{…}

Name string

maxLength128

minLength1

Type Function

DeferLoading boolOptional

Whether this function should be deferred and discovered via tool search.

Description stringOptional

Parameters anyOptional

Strict boolOptional

type CustomTool struct{…}

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

Name string

The name of the custom tool, used to identify it in tool calls.

Type Custom

The type of the custom tool. Always `custom`.

DeferLoading boolOptional

Whether this tool should be deferred and discovered via tool search.

Description stringOptional

Optional description of the custom tool, used to provide more context.

Format [CustomToolInputFormatUnion](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))Optional

The input format for the custom tool. Default is unconstrained text.

One of the following:

type CustomToolInputFormatText struct{…}

Unconstrained free-form text.

Type Text

Unconstrained text format. Always `text`.

type CustomToolInputFormatGrammar struct{…}

A grammar defined by the user.

Definition string

The grammar definition.

Syntax string

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

const CustomToolInputFormatGrammarSyntaxLark CustomToolInputFormatGrammarSyntax = "lark"

const CustomToolInputFormatGrammarSyntaxRegex CustomToolInputFormatGrammarSyntax = "regex"

Type Grammar

Grammar format. Always `grammar`.

Type Namespace

The type of the tool. Always `namespace`.

type ToolSearchTool struct{…}

Hosted or BYOT tool search configuration for deferred tools.

Type ToolSearch

The type of the tool. Always `tool_search`.

Description stringOptional

Description shown to the model for a client-executed tool search tool.

Execution ToolSearchToolExecutionOptional

Whether tool search is executed by the server or by the client.

One of the following:

const ToolSearchToolExecutionServer ToolSearchToolExecution = "server"

const ToolSearchToolExecutionClient ToolSearchToolExecution = "client"

Parameters anyOptional

Parameter schema for a client-executed tool search tool.

type WebSearchPreviewTool struct{…}

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type WebSearchPreviewToolType

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

One of the following:

const WebSearchPreviewToolTypeWebSearchPreview WebSearchPreviewToolType = "web\_search\_preview"

const WebSearchPreviewToolTypeWebSearchPreview2025\_03\_11 WebSearchPreviewToolType = "web\_search\_preview\_2025\_03\_11"

SearchContentTypes []stringOptional

One of the following:

const WebSearchPreviewToolSearchContentTypeText WebSearchPreviewToolSearchContentType = "text"

const WebSearchPreviewToolSearchContentTypeImage WebSearchPreviewToolSearchContentType = "image"

SearchContextSize WebSearchPreviewToolSearchContextSizeOptional

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

const WebSearchPreviewToolSearchContextSizeLow WebSearchPreviewToolSearchContextSize = "low"

const WebSearchPreviewToolSearchContextSizeMedium WebSearchPreviewToolSearchContextSize = "medium"

const WebSearchPreviewToolSearchContextSizeHigh WebSearchPreviewToolSearchContextSize = "high"

UserLocation WebSearchPreviewToolUserLocationOptional

The user’s location.

Type Approximate

The type of location approximation. Always `approximate`.

City stringOptional

Free text input for the city of the user, e.g. `San Francisco`.

Country stringOptional

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Region stringOptional

Free text input for the region of the user, e.g. `California`.

Timezone stringOptional

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type ApplyPatchTool struct{…}

Allows the assistant to create, delete, or update files using unified diffs.

Type ApplyPatch

The type of the tool. Always `apply_patch`.

Type AdditionalTools

The type of the item. Always `additional_tools`.

type ResponseCompactionItem struct{…}

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

ID string

The unique ID of the compaction item.

EncryptedContent string

The encrypted content that was produced by compaction.

Type Compaction

The type of the item. Always `compaction`.

CreatedBy stringOptional

The identifier of the actor that created the item.

type ResponseOutputItemImageGenerationCall struct{…}

An image generation request made by the model.

ID string

The unique ID of the image generation call.

Result string

The generated image encoded in base64.

Status string

The status of the image generation call.

One of the following:

const ResponseOutputItemImageGenerationCallStatusInProgress ResponseOutputItemImageGenerationCallStatus = "in\_progress"

const ResponseOutputItemImageGenerationCallStatusCompleted ResponseOutputItemImageGenerationCallStatus = "completed"

const ResponseOutputItemImageGenerationCallStatusGenerating ResponseOutputItemImageGenerationCallStatus = "generating"

const ResponseOutputItemImageGenerationCallStatusFailed ResponseOutputItemImageGenerationCallStatus = "failed"

Type ImageGenerationCall

The type of the image generation call. Always `image_generation_call`.

type ResponseCodeInterpreterToolCall struct{…}

A tool call to run code.

ID string

The unique ID of the code interpreter tool call.

Code string

The code to run, or null if not available.

ContainerID string

The ID of the container used to run the code.

Outputs []ResponseCodeInterpreterToolCallOutputUnion

The outputs generated by the code interpreter, such as logs or images.
Can be null if no outputs are available.

One of the following:

type ResponseCodeInterpreterToolCallOutputLogs struct{…}

The logs output from the code interpreter.

Logs string

The logs output from the code interpreter.

Type Logs

The type of the output. Always `logs`.

type ResponseCodeInterpreterToolCallOutputImage struct{…}

The image output from the code interpreter.

Type Image

The type of the output. Always `image`.

URL string

The URL of the image output from the code interpreter.

formaturi

Status ResponseCodeInterpreterToolCallStatus

The status of the code interpreter tool call. Valid values are `in_progress`, `completed`, `incomplete`, `interpreting`, and `failed`.

One of the following:

const ResponseCodeInterpreterToolCallStatusInProgress ResponseCodeInterpreterToolCallStatus = "in\_progress"

const ResponseCodeInterpreterToolCallStatusCompleted ResponseCodeInterpreterToolCallStatus = "completed"

const ResponseCodeInterpreterToolCallStatusIncomplete ResponseCodeInterpreterToolCallStatus = "incomplete"

const ResponseCodeInterpreterToolCallStatusInterpreting ResponseCodeInterpreterToolCallStatus = "interpreting"

const ResponseCodeInterpreterToolCallStatusFailed ResponseCodeInterpreterToolCallStatus = "failed"

Type CodeInterpreterCall

The type of the code interpreter tool call. Always `code_interpreter_call`.

type ResponseOutputItemLocalShellCall struct{…}

A tool call to run a command on the local shell.

ID string

The unique ID of the local shell call.

Action ResponseOutputItemLocalShellCallAction

Execute a shell command on the server.

Command []string

The command to run.

Env map[string, string]

Environment variables to set for the command.

Type Exec

The type of the local shell action. Always `exec`.

TimeoutMs int64Optional

Optional timeout in milliseconds for the command.

User stringOptional

Optional user to run the command as.

WorkingDirectory stringOptional

Optional working directory to run the command in.

CallID string

The unique ID of the local shell tool call generated by the model.

Status string

The status of the local shell call.

One of the following:

const ResponseOutputItemLocalShellCallStatusInProgress ResponseOutputItemLocalShellCallStatus = "in\_progress"

const ResponseOutputItemLocalShellCallStatusCompleted ResponseOutputItemLocalShellCallStatus = "completed"

const ResponseOutputItemLocalShellCallStatusIncomplete ResponseOutputItemLocalShellCallStatus = "incomplete"

Type LocalShellCall

The type of the local shell call. Always `local_shell_call`.

type ResponseOutputItemLocalShellCallOutput struct{…}

The output of a local shell tool call.

ID string

The unique ID of the local shell tool call generated by the model.

Output string

A JSON string of the output of the local shell tool call.

Type LocalShellCallOutput

The type of the local shell tool call output. Always `local_shell_call_output`.

Status stringOptional

The status of the item. One of `in_progress`, `completed`, or `incomplete`.

One of the following:

const ResponseOutputItemLocalShellCallOutputStatusInProgress ResponseOutputItemLocalShellCallOutputStatus = "in\_progress"

const ResponseOutputItemLocalShellCallOutputStatusCompleted ResponseOutputItemLocalShellCallOutputStatus = "completed"

const ResponseOutputItemLocalShellCallOutputStatusIncomplete ResponseOutputItemLocalShellCallOutputStatus = "incomplete"

type ResponseFunctionShellToolCall struct{…}

A tool call that executes one or more shell commands in a managed environment.

ID string

The unique ID of the shell tool call. Populated when this item is returned via API.

Action ResponseFunctionShellToolCallAction

The shell commands and limits that describe how to run the tool call.

Commands []string

MaxOutputLength int64

Optional maximum number of characters to return from each command.

TimeoutMs int64

Optional timeout in milliseconds for the commands.

CallID string

The unique ID of the shell tool call generated by the model.

Environment ResponseFunctionShellToolCallEnvironmentUnion

Represents the use of a local environment to perform shell actions.

One of the following:

type ResponseLocalEnvironment struct{…}

Represents the use of a local environment to perform shell actions.

Type Local

The environment type. Always `local`.

type ResponseContainerReference struct{…}

Represents a container created with /v1/containers.

ContainerID string

Type ContainerReference

The environment type. Always `container_reference`.

Status ResponseFunctionShellToolCallStatus

The status of the shell call. One of `in_progress`, `completed`, or `incomplete`.

One of the following:

const ResponseFunctionShellToolCallStatusInProgress ResponseFunctionShellToolCallStatus = "in\_progress"

const ResponseFunctionShellToolCallStatusCompleted ResponseFunctionShellToolCallStatus = "completed"

const ResponseFunctionShellToolCallStatusIncomplete ResponseFunctionShellToolCallStatus = "incomplete"

Type ShellCall

The type of the item. Always `shell_call`.

CreatedBy stringOptional

The ID of the entity that created this tool call.

type ResponseFunctionShellToolCallOutput struct{…}

The output of a shell tool call that was emitted.

ID string

The unique ID of the shell call output. Populated when this item is returned via API.

CallID string

The unique ID of the shell tool call generated by the model.

MaxOutputLength int64

The maximum length of the shell command output. This is generated by the model and should be passed back with the raw output.

Output []ResponseFunctionShellToolCallOutputOutput

An array of shell call output contents

Outcome ResponseFunctionShellToolCallOutputOutputOutcomeUnion

Represents either an exit outcome (with an exit code) or a timeout outcome for a shell call output chunk.

One of the following:

type ResponseFunctionShellToolCallOutputOutputOutcomeTimeout struct{…}

Indicates that the shell call exceeded its configured time limit.

Type Timeout

The outcome type. Always `timeout`.

type ResponseFunctionShellToolCallOutputOutputOutcomeExit struct{…}

Indicates that the shell commands finished and returned an exit code.

ExitCode int64

Exit code from the shell process.

Type Exit

The outcome type. Always `exit`.

Stderr string

The standard error output that was captured.

Stdout string

The standard output that was captured.

CreatedBy stringOptional

The identifier of the actor that created the item.

Status ResponseFunctionShellToolCallOutputStatus

The status of the shell call output. One of `in_progress`, `completed`, or `incomplete`.

One of the following:

const ResponseFunctionShellToolCallOutputStatusInProgress ResponseFunctionShellToolCallOutputStatus = "in\_progress"

const ResponseFunctionShellToolCallOutputStatusCompleted ResponseFunctionShellToolCallOutputStatus = "completed"

const ResponseFunctionShellToolCallOutputStatusIncomplete ResponseFunctionShellToolCallOutputStatus = "incomplete"

Type ShellCallOutput

The type of the shell call output. Always `shell_call_output`.

CreatedBy stringOptional

The identifier of the actor that created the item.

type ResponseApplyPatchToolCall struct{…}

A tool call that applies file diffs by creating, deleting, or updating files.

ID string

The unique ID of the apply patch tool call. Populated when this item is returned via API.

CallID string

The unique ID of the apply patch tool call generated by the model.

Operation ResponseApplyPatchToolCallOperationUnion

One of the create\_file, delete\_file, or update\_file operations applied via apply\_patch.

One of the following:

type ResponseApplyPatchToolCallOperationCreateFile struct{…}

Instruction describing how to create a file via the apply\_patch tool.

Diff string

Diff to apply.

Path string

Path of the file to create.

Type CreateFile

Create a new file with the provided diff.

type ResponseApplyPatchToolCallOperationDeleteFile struct{…}

Instruction describing how to delete a file via the apply\_patch tool.

Path string

Path of the file to delete.

Type DeleteFile

Delete the specified file.

type ResponseApplyPatchToolCallOperationUpdateFile struct{…}

Instruction describing how to update a file via the apply\_patch tool.

Diff string

Diff to apply.

Path string

Path of the file to update.

Type UpdateFile

Update an existing file with the provided diff.

Status ResponseApplyPatchToolCallStatus

The status of the apply patch tool call. One of `in_progress` or `completed`.

One of the following:

const ResponseApplyPatchToolCallStatusInProgress ResponseApplyPatchToolCallStatus = "in\_progress"

const ResponseApplyPatchToolCallStatusCompleted ResponseApplyPatchToolCallStatus = "completed"

Type ApplyPatchCall

The type of the item. Always `apply_patch_call`.

CreatedBy stringOptional

The ID of the entity that created this tool call.

type ResponseApplyPatchToolCallOutput struct{…}

The output emitted by an apply patch tool call.

ID string

The unique ID of the apply patch tool call output. Populated when this item is returned via API.

CallID string

The unique ID of the apply patch tool call generated by the model.

Status ResponseApplyPatchToolCallOutputStatus

The status of the apply patch tool call output. One of `completed` or `failed`.

One of the following:

const ResponseApplyPatchToolCallOutputStatusCompleted ResponseApplyPatchToolCallOutputStatus = "completed"

const ResponseApplyPatchToolCallOutputStatusFailed ResponseApplyPatchToolCallOutputStatus = "failed"

Type ApplyPatchCallOutput

The type of the item. Always `apply_patch_call_output`.

CreatedBy stringOptional

The ID of the entity that created this tool call output.

Output stringOptional

Optional textual output returned by the apply patch tool.

type ResponseOutputItemMcpCall struct{…}

An invocation of a tool on an MCP server.

ID string

The unique ID of the tool call.

Arguments string

A JSON string of the arguments passed to the tool.

Name string

The name of the tool that was run.

ServerLabel string

The label of the MCP server running the tool.

Type McpCall

The type of the item. Always `mcp_call`.

ApprovalRequestID stringOptional

Unique identifier for the MCP tool call approval request.
Include this value in a subsequent `mcp_approval_response` input to approve or reject the corresponding tool call.

Error stringOptional

The error from the tool call, if any.

Output stringOptional

The output from the tool call.

Status stringOptional

The status of the tool call. One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.

One of the following:

const ResponseOutputItemMcpCallStatusInProgress ResponseOutputItemMcpCallStatus = "in\_progress"

const ResponseOutputItemMcpCallStatusCompleted ResponseOutputItemMcpCallStatus = "completed"

const ResponseOutputItemMcpCallStatusIncomplete ResponseOutputItemMcpCallStatus = "incomplete"

const ResponseOutputItemMcpCallStatusCalling ResponseOutputItemMcpCallStatus = "calling"

const ResponseOutputItemMcpCallStatusFailed ResponseOutputItemMcpCallStatus = "failed"

type ResponseOutputItemMcpListTools struct{…}

A list of tools available on an MCP server.

ID string

The unique ID of the list.

ServerLabel string

The label of the MCP server.

Tools []ResponseOutputItemMcpListToolsTool

The tools available on the server.

InputSchema any

The JSON schema describing the tool’s input.

Name string

The name of the tool.

Annotations anyOptional

Additional annotations about the tool.

Description stringOptional

The description of the tool.

Type McpListTools

The type of the item. Always `mcp_list_tools`.

Error stringOptional

Error message if the server could not list tools.

type ResponseOutputItemMcpApprovalRequest struct{…}

A request for human approval of a tool invocation.

ID string

The unique ID of the approval request.

Arguments string

A JSON string of arguments for the tool.

Name string

The name of the tool to run.

ServerLabel string

The label of the MCP server making the request.

Type McpApprovalRequest

The type of the item. Always `mcp_approval_request`.

type ResponseOutputItemMcpApprovalResponse struct{…}

A response to an MCP approval request.

ID string

The unique ID of the approval response

ApprovalRequestID string

The ID of the approval request being answered.

Approve bool

Whether the request was approved.

Type McpApprovalResponse

The type of the item. Always `mcp_approval_response`.

Reason stringOptional

Optional reason for the decision.

type ResponseCustomToolCall struct{…}

A call to a custom tool created by the model.

CallID string

An identifier used to map this custom tool call to a tool call output.

Input string

The input for the custom tool call generated by the model.

Name string

The name of the custom tool being called.

Type CustomToolCall

The type of the custom tool call. Always `custom_tool_call`.

ID stringOptional

The unique ID of the custom tool call in the OpenAI platform.

Namespace stringOptional

The namespace of the custom tool being called.

type ResponseCustomToolCallOutputItem struct{…}

The output of a custom tool call from your code, being sent back to the model.

ID string

The unique ID of the custom tool call output item.

Status string

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

One of the following:

const ResponseCustomToolCallOutputItemStatusInProgress ResponseCustomToolCallOutputItemStatus = "in\_progress"

const ResponseCustomToolCallOutputItemStatusCompleted ResponseCustomToolCallOutputItemStatus = "completed"

const ResponseCustomToolCallOutputItemStatusIncomplete ResponseCustomToolCallOutputItemStatus = "incomplete"

CreatedBy stringOptional

The identifier of the actor that created the item.

ParallelToolCalls bool

Whether to allow the model to run tool calls in parallel.

Temperature float64

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
We generally recommend altering this or `top_p` but not both.

minimum0

maximum2

ToolChoice ResponseToolChoiceUnion

How the model should select which tool (or tools) to use when generating
a response. See the `tools` parameter to see how to specify which tools
the model can call.

One of the following:

type ToolChoiceOptions string

Controls which (if any) tool is called by the model.

`none` means the model will not call any tool and instead generates a message.

`auto` means the model can pick between generating a message or calling one or
more tools.

`required` means the model must call one or more tools.

One of the following:

const ToolChoiceOptionsNone [ToolChoiceOptions](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20tool_choice_options%20%3E%20(schema)) = "none"

const ToolChoiceOptionsAuto [ToolChoiceOptions](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20tool_choice_options%20%3E%20(schema)) = "auto"

const ToolChoiceOptionsRequired [ToolChoiceOptions](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20tool_choice_options%20%3E%20(schema)) = "required"

type ToolChoiceAllowed struct{…}

Constrains the tools available to the model to a pre-defined set.

Mode ToolChoiceAllowedMode

Constrains the tools available to the model to a pre-defined set.

`auto` allows the model to pick from among the allowed tools and generate a
message.

`required` requires the model to call one or more of the allowed tools.

One of the following:

const ToolChoiceAllowedModeAuto ToolChoiceAllowedMode = "auto"

const ToolChoiceAllowedModeRequired ToolChoiceAllowedMode = "required"

Tools []map[string, any]

A list of tool definitions that the model should be allowed to call.

For the Responses API, the list of tool definitions might look like:

[
  { "type": "function", "name": "get_weather" },
  { "type": "mcp", "server_label": "deepwiki" },
  { "type": "image_generation" }
]

Type AllowedTools

Allowed tool configuration type. Always `allowed_tools`.

type ToolChoiceTypes struct{…}

Indicates that the model should use a built-in tool to generate a response.
[Learn more about built-in tools](https://platform.openai.com/docs/guides/tools).

Type ToolChoiceTypesType

The type of hosted tool the model should to use. Learn more about
[built-in tools](https://platform.openai.com/docs/guides/tools).

Allowed values are:

* `file_search`
* `web_search_preview`
* `computer`
* `computer_use_preview`
* `computer_use`
* `code_interpreter`
* `image_generation`

One of the following:

const ToolChoiceTypesTypeFileSearch ToolChoiceTypesType = "file\_search"

const ToolChoiceTypesTypeWebSearchPreview ToolChoiceTypesType = "web\_search\_preview"

const ToolChoiceTypesTypeComputer ToolChoiceTypesType = "computer"

const ToolChoiceTypesTypeComputerUsePreview ToolChoiceTypesType = "computer\_use\_preview"

const ToolChoiceTypesTypeComputerUse ToolChoiceTypesType = "computer\_use"

const ToolChoiceTypesTypeWebSearchPreview2025\_03\_11 ToolChoiceTypesType = "web\_search\_preview\_2025\_03\_11"

const ToolChoiceTypesTypeImageGeneration ToolChoiceTypesType = "image\_generation"

const ToolChoiceTypesTypeCodeInterpreter ToolChoiceTypesType = "code\_interpreter"

type ToolChoiceFunction struct{…}

Use this option to force the model to call a specific function.

Name string

The name of the function to call.

Type Function

For function calling, the type is always `function`.

type ToolChoiceMcp struct{…}

Use this option to force the model to call a specific tool on a remote MCP server.

ServerLabel string

The label of the MCP server to use.

Type Mcp

For MCP tools, the type is always `mcp`.

Name stringOptional

The name of the tool to call on the server.

type ToolChoiceCustom struct{…}

Use this option to force the model to call a specific custom tool.

Name string

The name of the custom tool to call.

Type Custom

For custom tool calling, the type is always `custom`.

type ToolChoiceApplyPatch struct{…}

Forces the model to call the apply\_patch tool when executing a tool call.

Type ApplyPatch

The tool to call. Always `apply_patch`.

type ToolChoiceShell struct{…}

Forces the model to call the shell tool when a tool call is required.

Type Shell

The tool to call. Always `shell`.

Tools [][ToolUnion](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20tool%20%3E%20(schema))

An array of tools the model may call while generating a response. You
can specify which tool to use by setting the `tool_choice` parameter.

We support the following categories of tools:

* **Built-in tools**: Tools that are provided by OpenAI that extend the
  model’s capabilities, like [web search](https://platform.openai.com/docs/guides/tools-web-search)
  or [file search](https://platform.openai.com/docs/guides/tools-file-search). Learn more about
  [built-in tools](https://platform.openai.com/docs/guides/tools).
* **MCP Tools**: Integrations with third-party systems via custom MCP servers
  or predefined connectors such as Google Drive and SharePoint. Learn more about
  [MCP Tools](https://platform.openai.com/docs/guides/tools-connectors-mcp).
* **Function calls (custom tools)**: Functions that are defined by you,
  enabling the model to call your own code with strongly typed arguments
  and outputs. Learn more about
  [function calling](https://platform.openai.com/docs/guides/function-calling). You can also use
  custom tools to call your own code.

One of the following:

type FunctionTool struct{…}

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

Name string

The name of the function to call.

Parameters map[string, any]

A JSON schema object describing the parameters of the function.

Strict bool

Whether to enforce strict parameter validation. Default `true`.

Type Function

The type of the function tool. Always `function`.

DeferLoading boolOptional

Whether this function is deferred and loaded via tool search.

Description stringOptional

A description of the function. Used by the model to determine whether or not to call the function.

type FileSearchTool struct{…}

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

Type FileSearch

The type of the file search tool. Always `file_search`.

VectorStoreIDs []string

The IDs of the vector stores to search.

Filters FileSearchToolFiltersUnionOptional

A filter to apply.

One of the following:

type ComparisonFilter struct{…}

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

Key string

The key to compare against the value.

Type ComparisonFilterType

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

One of the following:

const ComparisonFilterTypeEq ComparisonFilterType = "eq"

const ComparisonFilterTypeNe ComparisonFilterType = "ne"

const ComparisonFilterTypeGt ComparisonFilterType = "gt"

const ComparisonFilterTypeGte ComparisonFilterType = "gte"

const ComparisonFilterTypeLt ComparisonFilterType = "lt"

const ComparisonFilterTypeLte ComparisonFilterType = "lte"

const ComparisonFilterTypeIn ComparisonFilterType = "in"

const ComparisonFilterTypeNin ComparisonFilterType = "nin"

Value ComparisonFilterValueUnion

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

string

float64

bool

type ComparisonFilterValueArray []ComparisonFilterValueArrayItemUnion

One of the following:

string

float64

type CompoundFilter struct{…}

Combine multiple filters using `and` or `or`.

Filters [][ComparisonFilter](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema))

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

One of the following:

type ComparisonFilter struct{…}

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

Key string

The key to compare against the value.

Type ComparisonFilterType

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

One of the following:

const ComparisonFilterTypeEq ComparisonFilterType = "eq"

const ComparisonFilterTypeNe ComparisonFilterType = "ne"

const ComparisonFilterTypeGt ComparisonFilterType = "gt"

const ComparisonFilterTypeGte ComparisonFilterType = "gte"

const ComparisonFilterTypeLt ComparisonFilterType = "lt"

const ComparisonFilterTypeLte ComparisonFilterType = "lte"

const ComparisonFilterTypeIn ComparisonFilterType = "in"

const ComparisonFilterTypeNin ComparisonFilterType = "nin"

Value ComparisonFilterValueUnion

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

string

float64

bool

type ComparisonFilterValueArray []ComparisonFilterValueArrayItemUnion

One of the following:

string

float64

Type CompoundFilterType

Type of operation: `and` or `or`.

One of the following:

const CompoundFilterTypeAnd CompoundFilterType = "and"

const CompoundFilterTypeOr CompoundFilterType = "or"

MaxNumResults int64Optional

The maximum number of results to return. This number should be between 1 and 50 inclusive.

RankingOptions FileSearchToolRankingOptionsOptional

Ranking options for search.

HybridSearch FileSearchToolRankingOptionsHybridSearchOptional

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

EmbeddingWeight float64

The weight of the embedding in the reciprocal ranking fusion.

TextWeight float64

The weight of the text in the reciprocal ranking fusion.

Ranker stringOptional

The ranker to use for the file search.

One of the following:

const FileSearchToolRankingOptionsRankerAuto FileSearchToolRankingOptionsRanker = "auto"

const FileSearchToolRankingOptionsRankerDefault2024\_11\_15 FileSearchToolRankingOptionsRanker = "default-2024-11-15"

ScoreThreshold float64Optional

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

type ComputerTool struct{…}

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

Type Computer

The type of the computer tool. Always `computer`.

type ComputerUsePreviewTool struct{…}

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

DisplayHeight int64

The height of the computer display.

DisplayWidth int64

The width of the computer display.

Environment ComputerUsePreviewToolEnvironment

The type of computer environment to control.

One of the following:

const ComputerUsePreviewToolEnvironmentWindows ComputerUsePreviewToolEnvironment = "windows"

const ComputerUsePreviewToolEnvironmentMac ComputerUsePreviewToolEnvironment = "mac"

const ComputerUsePreviewToolEnvironmentLinux ComputerUsePreviewToolEnvironment = "linux"

const ComputerUsePreviewToolEnvironmentUbuntu ComputerUsePreviewToolEnvironment = "ubuntu"

const ComputerUsePreviewToolEnvironmentBrowser ComputerUsePreviewToolEnvironment = "browser"

Type ComputerUsePreview

The type of the computer use tool. Always `computer_use_preview`.

type WebSearchTool struct{…}

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type WebSearchToolType

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

One of the following:

const WebSearchToolTypeWebSearch WebSearchToolType = "web\_search"

const WebSearchToolTypeWebSearch2025\_08\_26 WebSearchToolType = "web\_search\_2025\_08\_26"

Filters WebSearchToolFiltersOptional

Filters for the search.

AllowedDomains []stringOptional

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

SearchContextSize WebSearchToolSearchContextSizeOptional

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

const WebSearchToolSearchContextSizeLow WebSearchToolSearchContextSize = "low"

const WebSearchToolSearchContextSizeMedium WebSearchToolSearchContextSize = "medium"

const WebSearchToolSearchContextSizeHigh WebSearchToolSearchContextSize = "high"

UserLocation WebSearchToolUserLocationOptional

The approximate location of the user.

City stringOptional

Free text input for the city of the user, e.g. `San Francisco`.

Country stringOptional

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Region stringOptional

Free text input for the region of the user, e.g. `California`.

Timezone stringOptional

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

Type stringOptional

The type of location approximation. Always `approximate`.

type ToolMcp struct{…}

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

ServerLabel string

A label for this MCP server, used to identify it in tool calls.

Type Mcp

The type of the MCP tool. Always `mcp`.

AllowedTools ToolMcpAllowedToolsUnionOptional

List of allowed tool names or a filter object.

One of the following:

type ToolMcpAllowedToolsMcpAllowedTools []string

A string array of allowed tool names

type ToolMcpAllowedToolsMcpToolFilter struct{…}

A filter object to specify which tools are allowed.

ReadOnly boolOptional

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

ToolNames []stringOptional

List of allowed tool names.

Authorization stringOptional

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

ConnectorID stringOptional

Identifier for service connectors, like those available in ChatGPT. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided. Learn more
about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

Currently supported `connector_id` values are:

* Dropbox: `connector_dropbox`
* Gmail: `connector_gmail`
* Google Calendar: `connector_googlecalendar`
* Google Drive: `connector_googledrive`
* Microsoft Teams: `connector_microsoftteams`
* Outlook Calendar: `connector_outlookcalendar`
* Outlook Email: `connector_outlookemail`
* SharePoint: `connector_sharepoint`

One of the following:

const ToolMcpConnectorIDConnectorDropbox ToolMcpConnectorID = "connector\_dropbox"

const ToolMcpConnectorIDConnectorGmail ToolMcpConnectorID = "connector\_gmail"

const ToolMcpConnectorIDConnectorGooglecalendar ToolMcpConnectorID = "connector\_googlecalendar"

const ToolMcpConnectorIDConnectorGoogledrive ToolMcpConnectorID = "connector\_googledrive"

const ToolMcpConnectorIDConnectorMicrosoftteams ToolMcpConnectorID = "connector\_microsoftteams"

const ToolMcpConnectorIDConnectorOutlookcalendar ToolMcpConnectorID = "connector\_outlookcalendar"

const ToolMcpConnectorIDConnectorOutlookemail ToolMcpConnectorID = "connector\_outlookemail"

const ToolMcpConnectorIDConnectorSharepoint ToolMcpConnectorID = "connector\_sharepoint"

DeferLoading boolOptional

Whether this MCP tool is deferred and discovered via tool search.

Headers map[string, string]Optional

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

RequireApproval ToolMcpRequireApprovalUnionOptional

Specify which of the MCP server’s tools require approval.

One of the following:

type ToolMcpRequireApprovalMcpToolApprovalFilter struct{…}

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

Always ToolMcpRequireApprovalMcpToolApprovalFilterAlwaysOptional

A filter object to specify which tools are allowed.

ReadOnly boolOptional

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

ToolNames []stringOptional

List of allowed tool names.

Never ToolMcpRequireApprovalMcpToolApprovalFilterNeverOptional

A filter object to specify which tools are allowed.

ReadOnly boolOptional

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

ToolNames []stringOptional

List of allowed tool names.

type ToolMcpRequireApprovalMcpToolApprovalSetting string

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

One of the following:

const ToolMcpRequireApprovalMcpToolApprovalSettingAlways ToolMcpRequireApprovalMcpToolApprovalSetting = "always"

const ToolMcpRequireApprovalMcpToolApprovalSettingNever ToolMcpRequireApprovalMcpToolApprovalSetting = "never"

ServerDescription stringOptional

Optional description of the MCP server, used to provide more context.

ServerURL stringOptional

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

TunnelID stringOptional

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

type ToolCodeInterpreter struct{…}

A tool that runs Python code to help generate a response to a prompt.

Container ToolCodeInterpreterContainerUnion

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

One of the following:

string

type ToolCodeInterpreterContainerCodeInterpreterContainerAuto struct{…}

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

Type Auto

Always `auto`.

FileIDs []stringOptional

An optional list of uploaded files to make available to your code.

MemoryLimit stringOptional

The memory limit for the code interpreter container.

One of the following:

const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit1g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "1g"

const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit4g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "4g"

const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit16g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "16g"

const ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit64g ToolCodeInterpreterContainerCodeInterpreterToolAutoMemoryLimit = "64g"

NetworkPolicy ToolCodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicyUnionOptional

Network access policy for the container.

One of the following:

type ContainerNetworkPolicyDisabled struct{…}

Type Disabled

Disable outbound network access. Always `disabled`.

type ContainerNetworkPolicyAllowlist struct{…}

AllowedDomains []string

A list of allowed domains when type is `allowlist`.

Type Allowlist

Allow outbound network access only to specified domains. Always `allowlist`.

DomainSecrets [][ContainerNetworkPolicyDomainSecret](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))Optional

Optional domain-scoped secrets for allowlisted domains.

Domain string

The domain associated with the secret.

minLength1

Name string

The name of the secret to inject for the domain.

minLength1

Value string

The secret value to inject for the domain.

maxLength10485760

minLength1

Type CodeInterpreter

The type of the code interpreter tool. Always `code_interpreter`.

type ToolImageGeneration struct{…}

A tool that generates images using the GPT image models.

Type ImageGeneration

The type of the image generation tool. Always `image_generation`.

Action stringOptional

Whether to generate a new image or edit an existing image. Default: `auto`.

One of the following:

const ToolImageGenerationActionGenerate ToolImageGenerationAction = "generate"

const ToolImageGenerationActionEdit ToolImageGenerationAction = "edit"

const ToolImageGenerationActionAuto ToolImageGenerationAction = "auto"

Background stringOptional

Allows to set transparency for the background of the generated image(s).
This parameter is only supported for GPT image models that support
transparent backgrounds. Must be one of `transparent`, `opaque`, or
`auto` (default value). When `auto` is used, the model will
automatically determine the best background for the image.

`gpt-image-2` and `gpt-image-2-2026-04-21` do not support
transparent backgrounds. Requests with `background` set to
`transparent` will return an error for these models; use `opaque` or
`auto` instead.

If `transparent`, the output format needs to support transparency,
so it should be set to either `png` (default value) or `webp`.

One of the following:

const ToolImageGenerationBackgroundTransparent ToolImageGenerationBackground = "transparent"

const ToolImageGenerationBackgroundOpaque ToolImageGenerationBackground = "opaque"

const ToolImageGenerationBackgroundAuto ToolImageGenerationBackground = "auto"

InputFidelity stringOptional

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

One of the following:

const ToolImageGenerationInputFidelityHigh ToolImageGenerationInputFidelity = "high"

const ToolImageGenerationInputFidelityLow ToolImageGenerationInputFidelity = "low"

InputImageMask ToolImageGenerationInputImageMaskOptional

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

FileID stringOptional

File ID for the mask image.

ImageURL stringOptional

Base64-encoded mask image.

Model stringOptional

The image generation model to use. Default: `gpt-image-1`.

One of the following:

string

string

One of the following:

const ToolImageGenerationModelGPTImage1 ToolImageGenerationModel = "gpt-image-1"

const ToolImageGenerationModelGPTImage1Mini ToolImageGenerationModel = "gpt-image-1-mini"

const ToolImageGenerationModelGPTImage2 ToolImageGenerationModel = "gpt-image-2"

const ToolImageGenerationModelGPTImage2\_2026\_04\_21 ToolImageGenerationModel = "gpt-image-2-2026-04-21"

const ToolImageGenerationModelGPTImage1\_5 ToolImageGenerationModel = "gpt-image-1.5"

const ToolImageGenerationModelChatgptImageLatest ToolImageGenerationModel = "chatgpt-image-latest"

Moderation stringOptional

Moderation level for the generated image. Default: `auto`.

One of the following:

const ToolImageGenerationModerationAuto ToolImageGenerationModeration = "auto"

const ToolImageGenerationModerationLow ToolImageGenerationModeration = "low"

OutputCompression int64Optional

Compression level for the output image. Default: 100.

minimum0

maximum100

OutputFormat stringOptional

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

One of the following:

const ToolImageGenerationOutputFormatPNG ToolImageGenerationOutputFormat = "png"

const ToolImageGenerationOutputFormatWebP ToolImageGenerationOutputFormat = "webp"

const ToolImageGenerationOutputFormatJPEG ToolImageGenerationOutputFormat = "jpeg"

PartialImages int64Optional

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

Quality stringOptional

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

One of the following:

const ToolImageGenerationQualityLow ToolImageGenerationQuality = "low"

const ToolImageGenerationQualityMedium ToolImageGenerationQuality = "medium"

const ToolImageGenerationQualityHigh ToolImageGenerationQuality = "high"

const ToolImageGenerationQualityAuto ToolImageGenerationQuality = "auto"

Size stringOptional

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

string

string

One of the following:

const ToolImageGenerationSize1024x1024 ToolImageGenerationSize = "1024x1024"

const ToolImageGenerationSize1024x1536 ToolImageGenerationSize = "1024x1536"

const ToolImageGenerationSize1536x1024 ToolImageGenerationSize = "1536x1024"

const ToolImageGenerationSizeAuto ToolImageGenerationSize = "auto"

type ToolLocalShell struct{…}

A tool that allows the model to execute shell commands in a local environment.

Type LocalShell

The type of the local shell tool. Always `local_shell`.

type FunctionShellTool struct{…}

A tool that allows the model to execute shell commands.

Type Shell

The type of the shell tool. Always `shell`.

Environment FunctionShellToolEnvironmentUnionOptional

One of the following:

type ContainerAuto struct{…}

Type ContainerAuto

Automatically creates a container for this request

FileIDs []stringOptional

An optional list of uploaded files to make available to your code.

MemoryLimit ContainerAutoMemoryLimitOptional

The memory limit for the container.

One of the following:

const ContainerAutoMemoryLimit1g ContainerAutoMemoryLimit = "1g"

const ContainerAutoMemoryLimit4g ContainerAutoMemoryLimit = "4g"

const ContainerAutoMemoryLimit16g ContainerAutoMemoryLimit = "16g"

const ContainerAutoMemoryLimit64g ContainerAutoMemoryLimit = "64g"

NetworkPolicy ContainerAutoNetworkPolicyUnionOptional

Network access policy for the container.

One of the following:

type ContainerNetworkPolicyDisabled struct{…}

Type Disabled

Disable outbound network access. Always `disabled`.

type ContainerNetworkPolicyAllowlist struct{…}

AllowedDomains []string

A list of allowed domains when type is `allowlist`.

Type Allowlist

Allow outbound network access only to specified domains. Always `allowlist`.

DomainSecrets [][ContainerNetworkPolicyDomainSecret](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))Optional

Optional domain-scoped secrets for allowlisted domains.

Domain string

The domain associated with the secret.

minLength1

Name string

The name of the secret to inject for the domain.

minLength1

Value string

The secret value to inject for the domain.

maxLength10485760

minLength1

Skills []ContainerAutoSkillUnionOptional

An optional list of skills referenced by id or inline data.

One of the following:

type SkillReference struct{…}

SkillID string

The ID of the referenced skill.

maxLength64

minLength1

Type SkillReference

References a skill created with the /v1/skills endpoint.

Version stringOptional

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

type InlineSkill struct{…}

Description string

The description of the skill.

Name string

The name of the skill.

Source [InlineSkillSource](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema))

Inline skill payload

Data string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

MediaType ApplicationZip

The media type of the inline skill payload. Must be `application/zip`.

Type Base64

The type of the inline skill source. Must be `base64`.

Type Inline

Defines an inline skill for this request.

type LocalEnvironment struct{…}

Type Local

Use a local computer environment.

Skills [][LocalSkill](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema))Optional

An optional list of skills.

Description string

The description of the skill.

Name string

The name of the skill.

Path string

The path to the directory containing the skill.

type ContainerReference struct{…}

ContainerID string

The ID of the referenced container.

Type ContainerReference

References a container created with the /v1/containers endpoint

type CustomTool struct{…}

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

Name string

The name of the custom tool, used to identify it in tool calls.

Type Custom

The type of the custom tool. Always `custom`.

DeferLoading boolOptional

Whether this tool should be deferred and discovered via tool search.

Description stringOptional

Optional description of the custom tool, used to provide more context.

Format [CustomToolInputFormatUnion](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))Optional

The input format for the custom tool. Default is unconstrained text.

One of the following:

type CustomToolInputFormatText struct{…}

Unconstrained free-form text.

Type Text

Unconstrained text format. Always `text`.

type CustomToolInputFormatGrammar struct{…}

A grammar defined by the user.

Definition string

The grammar definition.

Syntax string

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

const CustomToolInputFormatGrammarSyntaxLark CustomToolInputFormatGrammarSyntax = "lark"

const CustomToolInputFormatGrammarSyntaxRegex CustomToolInputFormatGrammarSyntax = "regex"

Type Grammar

Grammar format. Always `grammar`.

type NamespaceTool struct{…}

Groups function/custom tools under a shared namespace.

Description string

A description of the namespace shown to the model.

minLength1

Name string

The namespace name used in tool calls (for example, `crm`).

minLength1

Tools []NamespaceToolToolUnion

The function/custom tools available inside this namespace.

One of the following:

type NamespaceToolToolFunction struct{…}

Name string

maxLength128

minLength1

Type Function

DeferLoading boolOptional

Whether this function should be deferred and discovered via tool search.

Description stringOptional

Parameters anyOptional

Strict boolOptional

type CustomTool struct{…}

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

Name string

The name of the custom tool, used to identify it in tool calls.

Type Custom

The type of the custom tool. Always `custom`.

DeferLoading boolOptional

Whether this tool should be deferred and discovered via tool search.

Description stringOptional

Optional description of the custom tool, used to provide more context.

Format [CustomToolInputFormatUnion](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))Optional

The input format for the custom tool. Default is unconstrained text.

One of the following:

type CustomToolInputFormatText struct{…}

Unconstrained free-form text.

Type Text

Unconstrained text format. Always `text`.

type CustomToolInputFormatGrammar struct{…}

A grammar defined by the user.

Definition string

The grammar definition.

Syntax string

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

const CustomToolInputFormatGrammarSyntaxLark CustomToolInputFormatGrammarSyntax = "lark"

const CustomToolInputFormatGrammarSyntaxRegex CustomToolInputFormatGrammarSyntax = "regex"

Type Grammar

Grammar format. Always `grammar`.

Type Namespace

The type of the tool. Always `namespace`.

type ToolSearchTool struct{…}

Hosted or BYOT tool search configuration for deferred tools.

Type ToolSearch

The type of the tool. Always `tool_search`.

Description stringOptional

Description shown to the model for a client-executed tool search tool.

Execution ToolSearchToolExecutionOptional

Whether tool search is executed by the server or by the client.

One of the following:

const ToolSearchToolExecutionServer ToolSearchToolExecution = "server"

const ToolSearchToolExecutionClient ToolSearchToolExecution = "client"

Parameters anyOptional

Parameter schema for a client-executed tool search tool.

type WebSearchPreviewTool struct{…}

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type WebSearchPreviewToolType

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

One of the following:

const WebSearchPreviewToolTypeWebSearchPreview WebSearchPreviewToolType = "web\_search\_preview"

const WebSearchPreviewToolTypeWebSearchPreview2025\_03\_11 WebSearchPreviewToolType = "web\_search\_preview\_2025\_03\_11"

SearchContentTypes []stringOptional

One of the following:

const WebSearchPreviewToolSearchContentTypeText WebSearchPreviewToolSearchContentType = "text"

const WebSearchPreviewToolSearchContentTypeImage WebSearchPreviewToolSearchContentType = "image"

SearchContextSize WebSearchPreviewToolSearchContextSizeOptional

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

const WebSearchPreviewToolSearchContextSizeLow WebSearchPreviewToolSearchContextSize = "low"

const WebSearchPreviewToolSearchContextSizeMedium WebSearchPreviewToolSearchContextSize = "medium"

const WebSearchPreviewToolSearchContextSizeHigh WebSearchPreviewToolSearchContextSize = "high"

UserLocation WebSearchPreviewToolUserLocationOptional

The user’s location.

Type Approximate

The type of location approximation. Always `approximate`.

City stringOptional

Free text input for the city of the user, e.g. `San Francisco`.

Country stringOptional

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Region stringOptional

Free text input for the region of the user, e.g. `California`.

Timezone stringOptional

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type ApplyPatchTool struct{…}

Allows the assistant to create, delete, or update files using unified diffs.

Type ApplyPatch

The type of the tool. Always `apply_patch`.

TopP float64

An alternative to sampling with temperature, called nucleus sampling,
where the model considers the results of the tokens with top\_p probability
mass. So 0.1 means only the tokens comprising the top 10% probability mass
are considered.

We generally recommend altering this or `temperature` but not both.

minimum0

maximum1

Background boolOptional

Whether to run the model response in the background.
[Learn more](https://platform.openai.com/docs/guides/background).

CompletedAt float64Optional

Unix timestamp (in seconds) of when this Response was completed.
Only present when the status is `completed`.

formatunixtime

Conversation ResponseConversationOptional

The conversation that this response belonged to. Input items and output items from this response were automatically added to this conversation.

ID string

The unique ID of the conversation that this response was associated with.

MaxOutputTokens int64Optional

An upper bound for the number of tokens that can be generated for a response, including visible output tokens and [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

MaxToolCalls int64Optional

The maximum number of total calls to built-in tools that can be processed in a response. This maximum number applies across all built-in tool calls, not per individual tool. Any further attempts to call a tool by the model will be ignored.

Moderation ResponseModerationOptional

Moderation results for the response input and output, if moderated completions were requested.

Input ResponseModerationInputUnion

Moderation for the response input.

One of the following:

type ResponseModerationInputModerationResult struct{…}

A moderation result produced for the response input or output.

Categories map[string, bool]

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

CategoryAppliedInputTypes map[string, []string]

Which modalities of input are reflected by the score for each category.

One of the following:

const ResponseModerationInputModerationResultCategoryAppliedInputTypeText ResponseModerationInputModerationResultCategoryAppliedInputType = "text"

const ResponseModerationInputModerationResultCategoryAppliedInputTypeImage ResponseModerationInputModerationResultCategoryAppliedInputType = "image"

CategoryScores map[string, float64]

A dictionary of moderation categories to scores.

Flagged bool

A boolean indicating whether the content was flagged by any category.

Model string

The moderation model that produced this result.

Type ModerationResult

The object type, which was always `moderation_result` for successful moderation results.

type ResponseModerationInputError struct{…}

An error produced while attempting moderation for the response input or output.

Code string

The error code.

Message string

The error message.

Type Error

The object type, which was always `error` for moderation failures.

Output ResponseModerationOutputUnion

Moderation for the response output.

One of the following:

type ResponseModerationOutputModerationResult struct{…}

A moderation result produced for the response input or output.

Categories map[string, bool]

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

CategoryAppliedInputTypes map[string, []string]

Which modalities of input are reflected by the score for each category.

One of the following:

const ResponseModerationOutputModerationResultCategoryAppliedInputTypeText ResponseModerationOutputModerationResultCategoryAppliedInputType = "text"

const ResponseModerationOutputModerationResultCategoryAppliedInputTypeImage ResponseModerationOutputModerationResultCategoryAppliedInputType = "image"

CategoryScores map[string, float64]

A dictionary of moderation categories to scores.

Flagged bool

A boolean indicating whether the content was flagged by any category.

Model string

The moderation model that produced this result.

Type ModerationResult

The object type, which was always `moderation_result` for successful moderation results.

type ResponseModerationOutputError struct{…}

An error produced while attempting moderation for the response input or output.

Code string

The error code.

Message string

The error message.

Type Error

The object type, which was always `error` for moderation failures.

PreviousResponseID stringOptional

The unique ID of the previous response to the model. Use this to
create multi-turn conversations. Learn more about
[conversation state](https://platform.openai.com/docs/guides/conversation-state). Cannot be used in conjunction with `conversation`.

Prompt [ResponsePrompt](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20response_prompt%20%3E%20(schema))Optional

Reference to a prompt template and its variables.
[Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

ID string

The unique identifier of the prompt template to use.

Variables map[string, ResponsePromptVariableUnion]Optional

Optional map of values to substitute in for variables in your
prompt. The substitution values can either be strings, or other
Response input types like images or files.

One of the following:

string

type ResponseInputText struct{…}

A text input to the model.

Text string

The text input to the model.

Type InputText

The type of the input item. Always `input_text`.

type ResponseInputImage struct{…}

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail ResponseInputImageDetail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

const ResponseInputImageDetailLow ResponseInputImageDetail = "low"

const ResponseInputImageDetailHigh ResponseInputImageDetail = "high"

const ResponseInputImageDetailAuto ResponseInputImageDetail = "auto"

const ResponseInputImageDetailOriginal ResponseInputImageDetail = "original"

Type InputImage

The type of the input item. Always `input_image`.

FileID stringOptional

The ID of the file to be sent to the model.

ImageURL stringOptional

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

type ResponseInputFile struct{…}

A file input to the model.

Type InputFile

The type of the input item. Always `input_file`.

Detail ResponseInputFileDetailOptional

The detail level of the file to be sent to the model. Use `low` for the default rendering behavior, or `high` to render the file at higher quality. Defaults to `low`.

One of the following:

const ResponseInputFileDetailLow ResponseInputFileDetail = "low"

const ResponseInputFileDetailHigh ResponseInputFileDetail = "high"

FileData stringOptional

The content of the file to be sent to the model.

FileID stringOptional

The ID of the file to be sent to the model.

FileURL stringOptional

The URL of the file to be sent to the model.

formaturi

Filename stringOptional

The name of the file to be sent to the model.

Version stringOptional

Optional version of the prompt template.

PromptCacheKey stringOptional

Used by OpenAI to cache responses for similar requests to optimize your cache hit rates. Replaces the `user` field. [Learn more](https://platform.openai.com/docs/guides/prompt-caching).

PromptCacheRetention ResponsePromptCacheRetentionOptional

The retention policy for the prompt cache. Set to `24h` to enable extended prompt caching, which keeps cached prefixes active for longer, up to a maximum of 24 hours. [Learn more](https://platform.openai.com/docs/guides/prompt-caching#prompt-cache-retention).
For `gpt-5.5`, `gpt-5.5-pro`, and future models, only `24h` is supported.

For older models that support both `in_memory` and `24h`, the default depends on your organization’s data retention policy:

* Organizations without ZDR enabled default to `24h`.
* Organizations with ZDR enabled default to `in_memory` when `prompt_cache_retention` is not specified.

One of the following:

const ResponsePromptCacheRetentionInMemory ResponsePromptCacheRetention = "in\_memory"

const ResponsePromptCacheRetention24h ResponsePromptCacheRetention = "24h"

Reasoning [Reasoning](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning%20%3E%20(schema))Optional

**gpt-5 and o-series models only**

Configuration options for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).

Context ReasoningContextOptional

Controls which reasoning items are rendered back to the model on later turns.
When returned on a response, this is the effective reasoning context mode
used for the response.

One of the following:

const ReasoningContextAuto ReasoningContext = "auto"

const ReasoningContextCurrentTurn ReasoningContext = "current\_turn"

const ReasoningContextAllTurns ReasoningContext = "all\_turns"

Effort [ReasoningEffort](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema))Optional

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

One of the following:

const ReasoningEffortNone [ReasoningEffort](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)) = "none"

const ReasoningEffortMinimal [ReasoningEffort](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)) = "minimal"

const ReasoningEffortLow [ReasoningEffort](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)) = "low"

const ReasoningEffortMedium [ReasoningEffort](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)) = "medium"

const ReasoningEffortHigh [ReasoningEffort](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)) = "high"

const ReasoningEffortXhigh [ReasoningEffort](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)) = "xhigh"

DeprecatedGenerateSummary ReasoningGenerateSummaryOptional

**Deprecated:** use `summary` instead.

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

One of the following:

const ReasoningGenerateSummaryAuto ReasoningGenerateSummary = "auto"

const ReasoningGenerateSummaryConcise ReasoningGenerateSummary = "concise"

const ReasoningGenerateSummaryDetailed ReasoningGenerateSummary = "detailed"

Summary ReasoningSummaryOptional

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

`concise` is supported for `computer-use-preview` models and all reasoning models after `gpt-5`.

One of the following:

const ReasoningSummaryAuto ReasoningSummary = "auto"

const ReasoningSummaryConcise ReasoningSummary = "concise"

const ReasoningSummaryDetailed ReasoningSummary = "detailed"

SafetyIdentifier stringOptional

A stable identifier used to help detect users of your application that may be violating OpenAI’s usage policies.
The IDs should be a string that uniquely identifies each user, with a maximum length of 64 characters. We recommend hashing their username or email address, in order to avoid sending us any identifying information. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

maxLength64

ServiceTier ResponseServiceTierOptional

Specifies the processing type used for serving the request.

* If set to ‘auto’, then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use ‘default’.
* If set to ‘default’, then the request will be processed with the standard pricing and performance for the selected model.
* If set to ‘[flex](https://platform.openai.com/docs/guides/flex-processing)’ or ‘[priority](https://openai.com/api-priority-processing/)’, then the request will be processed with the corresponding service tier.
* When not set, the default behavior is ‘auto’.

When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.

One of the following:

const ResponseServiceTierAuto ResponseServiceTier = "auto"

const ResponseServiceTierDefault ResponseServiceTier = "default"

const ResponseServiceTierFlex ResponseServiceTier = "flex"

const ResponseServiceTierScale ResponseServiceTier = "scale"

const ResponseServiceTierPriority ResponseServiceTier = "priority"

Status [ResponseStatus](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20response_status%20%3E%20(schema))Optional

The status of the response generation. One of `completed`, `failed`,
`in_progress`, `cancelled`, `queued`, or `incomplete`.

One of the following:

const ResponseStatusCompleted [ResponseStatus](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20response_status%20%3E%20(schema)) = "completed"

const ResponseStatusFailed [ResponseStatus](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20response_status%20%3E%20(schema)) = "failed"

const ResponseStatusInProgress [ResponseStatus](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20response_status%20%3E%20(schema)) = "in\_progress"

const ResponseStatusCancelled [ResponseStatus](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20response_status%20%3E%20(schema)) = "cancelled"

const ResponseStatusQueued [ResponseStatus](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20response_status%20%3E%20(schema)) = "queued"

const ResponseStatusIncomplete [ResponseStatus](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20response_status%20%3E%20(schema)) = "incomplete"

Text [ResponseTextConfig](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20response_text_config%20%3E%20(schema))Optional

Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:

* [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
* [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

Format [ResponseFormatTextConfigUnion](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20response_format_text_config%20%3E%20(schema))Optional

An object specifying the format that the model must output.

Configuring `{ "type": "json_schema" }` enables Structured Outputs,
which ensures the model will match your supplied JSON schema. Learn more in the
[Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

The default format is `{ "type": "text" }` with no additional options.

**Not recommended for gpt-4o and newer models:**

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

One of the following:

type ResponseFormatText struct{…}

Default response format. Used to generate text responses.

Type Text

The type of response format being defined. Always `text`.

type ResponseFormatTextJSONSchemaConfig struct{…}

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

Name string

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

Schema map[string, any]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

Type JSONSchema

The type of response format being defined. Always `json_schema`.

Description stringOptional

A description of what the response format is for, used by the model to
determine how to respond in the format.

Strict boolOptional

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

type ResponseFormatJSONObject struct{…}

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

Type JSONObject

The type of response format being defined. Always `json_object`.

Verbosity ResponseTextConfigVerbosityOptional

Constrains the verbosity of the model’s response. Lower values will result in
more concise responses, while higher values will result in more verbose responses.
Currently supported values are `low`, `medium`, and `high`.

One of the following:

const ResponseTextConfigVerbosityLow ResponseTextConfigVerbosity = "low"

const ResponseTextConfigVerbosityMedium ResponseTextConfigVerbosity = "medium"

const ResponseTextConfigVerbosityHigh ResponseTextConfigVerbosity = "high"

TopLogprobs int64Optional

An integer between 0 and 20 specifying the maximum number of most likely
tokens to return at each token position, each with an associated log
probability. In some cases, the number of returned tokens may be fewer than
requested.

minimum0

maximum20

Truncation ResponseTruncationOptional

The truncation strategy to use for the model response.

* `auto`: If the input to this Response exceeds
  the model’s context window size, the model will truncate the
  response to fit the context window by dropping items from the beginning of the conversation.
* `disabled` (default): If the input size will exceed the context window
  size for a model, the request will fail with a 400 error.

One of the following:

const ResponseTruncationAuto ResponseTruncation = "auto"

const ResponseTruncationDisabled ResponseTruncation = "disabled"

Usage [ResponseUsage](/api/reference/go/resources/responses#(resource)%20responses%20%3E%20(model)%20response_usage%20%3E%20(schema))Optional

Represents token usage details including input tokens, output tokens,
a breakdown of output tokens, and the total tokens used.

InputTokens int64

The number of input tokens.

InputTokensDetails ResponseUsageInputTokensDetails

A detailed breakdown of the input tokens.

CachedTokens int64

The number of tokens that were retrieved from the cache.
[More on prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

OutputTokens int64

The number of output tokens.

OutputTokensDetails ResponseUsageOutputTokensDetails

A detailed breakdown of the output tokens.

ReasoningTokens int64

The number of reasoning tokens.

TotalTokens int64

The total number of tokens used.

DeprecatedUser stringOptional

This field is being replaced by `safety_identifier` and `prompt_cache_key`. Use `prompt_cache_key` instead to maintain caching optimizations.
A stable identifier for your end-users.
Used to boost cache hit rates by better bucketing similar requests and to help OpenAI detect and prevent abuse. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

SequenceNumber int64

The sequence number for this event.

Type ResponseQueued

The type of the event. Always ‘response.queued’.

type ResponseCustomToolCallInputDeltaEvent struct{…}

Event representing a delta (partial update) to the input of a custom tool call.

Delta string

The incremental input data (delta) for the custom tool call.

ItemID string

Unique identifier for the API item associated with this event.

OutputIndex int64

The index of the output this delta applies to.

SequenceNumber int64

The sequence number of this event.

Type ResponseCustomToolCallInputDelta

The event type identifier.

type ResponseCustomToolCallInputDoneEvent struct{…}

Event indicating that input for a custom tool call is complete.

Input string

The complete input data for the custom tool call.

ItemID string

Unique identifier for the API item associated with this event.

OutputIndex int64

The index of the output this event applies to.

SequenceNumber int64

The sequence number of this event.

Type ResponseCustomToolCallInputDone

The event type identifier.

### Create a model response

Go

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
  "github.com/openai/openai-go/responses"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  response, err := client.Responses.New(context.TODO(), responses.ResponseNewParams{

  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", response.ID)

200 example

  "id": "id",
  "created_at": 0,
  "error": {
    "code": "server_error",
    "message": "message"
  "incomplete_details": {
    "reason": "max_output_tokens"
  "instructions": "string",
  "metadata": {
    "foo": "string"
  "model": "gpt-5.1",
  "object": "response",
  "output": [
      "id": "id",
      "content": [
          "annotations": [
              "file_id": "file_id",
              "filename": "filename",
              "index": 0,
              "type": "file_citation"
          ],
          "text": "text",
          "type": "output_text",
          "logprobs": [
              "token": "token",
              "bytes": [
                0
              ],
              "logprob": 0,
              "top_logprobs": [
                  "token": "token",
                  "bytes": [
                    0
                  ],
                  "logprob": 0
              ]
          ]
      ],
      "role": "assistant",
      "status": "in_progress",
      "type": "message",
      "phase": "commentary"
  ],
  "parallel_tool_calls": true,
  "temperature": 1,
  "tool_choice": "none",
  "tools": [
      "name": "name",
      "parameters": {
        "foo": "bar"
      "strict": true,
      "type": "function",
      "defer_loading": true,
      "description": "description"
  ],
  "top_p": 1,
  "background": true,
  "completed_at": 0,
  "conversation": {
    "id": "id"
  "max_output_tokens": 0,
  "max_tool_calls": 0,
  "moderation": {
    "input": {
      "categories": {
        "foo": true
      "category_applied_input_types": {
        "foo": [
          "text"
        ]
      "category_scores": {
        "foo": 0
      "flagged": true,
      "model": "model",
      "type": "moderation_result"
    "output": {
      "categories": {
        "foo": true
      "category_applied_input_types": {
        "foo": [
          "text"
        ]
      "category_scores": {
        "foo": 0
      "flagged": true,
      "model": "model",
      "type": "moderation_result"
  "output_text": "output_text",
  "previous_response_id": "previous_response_id",
  "prompt": {
    "id": "id",
    "variables": {
      "foo": "string"
    "version": "version"
  "prompt_cache_key": "prompt-cache-key-1234",
  "prompt_cache_retention": "in_memory",
  "reasoning": {
    "context": "auto",
    "effort": "none",
    "generate_summary": "auto",
    "summary": "auto"
  "safety_identifier": "safety-identifier-1234",
  "service_tier": "auto",
  "status": "completed",
  "text": {
    "format": {
      "type": "text"
    "verbosity": "low"
  "top_logprobs": 0,
  "truncation": "auto",
  "usage": {
    "input_tokens": 0,
    "input_tokens_details": {
      "cached_tokens": 0
    "output_tokens": 0,
    "output_tokens_details": {
      "reasoning_tokens": 0
    "total_tokens": 0
  "user": "user-1234"

##### Returns Examples

200 example

  "id": "id",
  "created_at": 0,
  "error": {
    "code": "server_error",
    "message": "message"
  "incomplete_details": {
    "reason": "max_output_tokens"
  "instructions": "string",
  "metadata": {
    "foo": "string"
  "model": "gpt-5.1",
  "object": "response",
  "output": [
      "id": "id",
      "content": [
          "annotations": [
              "file_id": "file_id",
              "filename": "filename",
              "index": 0,
              "type": "file_citation"
          ],
          "text": "text",
          "type": "output_text",
          "logprobs": [
              "token": "token",
              "bytes": [
                0
              ],
              "logprob": 0,
              "top_logprobs": [
                  "token": "token",
                  "bytes": [
                    0
                  ],
                  "logprob": 0
              ]
          ]
      ],
      "role": "assistant",
      "status": "in_progress",
      "type": "message",
      "phase": "commentary"
  ],
  "parallel_tool_calls": true,
  "temperature": 1,
  "tool_choice": "none",
  "tools": [
      "name": "name",
      "parameters": {
        "foo": "bar"
      "strict": true,
      "type": "function",
      "defer_loading": true,
      "description": "description"
  ],
  "top_p": 1,
  "background": true,
  "completed_at": 0,
  "conversation": {
    "id": "id"
  "max_output_tokens": 0,
  "max_tool_calls": 0,
  "moderation": {
    "input": {
      "categories": {
        "foo": true
      "category_applied_input_types": {
        "foo": [
          "text"
        ]
      "category_scores": {
        "foo": 0
      "flagged": true,
      "model": "model",
      "type": "moderation_result"
    "output": {
      "categories": {
        "foo": true
      "category_applied_input_types": {
        "foo": [
          "text"
        ]
      "category_scores": {
        "foo": 0
      "flagged": true,
      "model": "model",
      "type": "moderation_result"
  "output_text": "output_text",
  "previous_response_id": "previous_response_id",
  "prompt": {
    "id": "id",
    "variables": {
      "foo": "string"
    "version": "version"
  "prompt_cache_key": "prompt-cache-key-1234",
  "prompt_cache_retention": "in_memory",
  "reasoning": {
    "context": "auto",
    "effort": "none",
    "generate_summary": "auto",
    "summary": "auto"
  "safety_identifier": "safety-identifier-1234",
  "service_tier": "auto",
  "status": "completed",
  "text": {
    "format": {
      "type": "text"
    "verbosity": "low"
  "top_logprobs": 0,
  "truncation": "auto",
  "usage": {
    "input_tokens": 0,
    "input_tokens_details": {
      "cached_tokens": 0
    "output_tokens": 0,
    "output_tokens_details": {
      "reasoning_tokens": 0
    "total_tokens": 0
  "user": "user-1234"
