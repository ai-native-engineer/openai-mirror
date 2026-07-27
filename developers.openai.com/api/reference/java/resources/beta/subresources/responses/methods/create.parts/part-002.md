<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/responses/methods/create/ -->
<!-- part of: https://developers.openai.com/api/reference/java/resources/beta/subresources/responses/methods/create/ -->

<!-- chunk-start -->

WINDOWS("windows")

MAC("mac")

LINUX("linux")

UBUNTU("ubuntu")

BROWSER("browser")

JsonValue; type "computer\_use\_preview"constant"computer\_use\_preview"constant

The type of the computer use tool. Always `computer_use_preview`.

class BetaWebSearchTool:

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

WEB\_SEARCH("web\_search")

WEB\_SEARCH\_2025\_08\_26("web\_search\_2025\_08\_26")

Optional<Filters> filters

Filters for the search.

Optional<List<String>> allowedDomains

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The approximate location of the user.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

Optional<Type> type

The type of location approximation. Always `approximate`.

Mcp

String serverLabel

A label for this MCP server, used to identify it in tool calls.

JsonValue; type "mcp"constant"mcp"constant

The type of the MCP tool. Always `mcp`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<AllowedTools> allowedTools

List of allowed tool names or a filter object.

List<String>

class McpToolFilter:

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<String> authorization

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

Optional<ConnectorId> connectorId

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

CONNECTOR\_DROPBOX("connector\_dropbox")

CONNECTOR\_GMAIL("connector\_gmail")

CONNECTOR\_GOOGLECALENDAR("connector\_googlecalendar")

CONNECTOR\_GOOGLEDRIVE("connector\_googledrive")

CONNECTOR\_MICROSOFTTEAMS("connector\_microsoftteams")

CONNECTOR\_OUTLOOKCALENDAR("connector\_outlookcalendar")

CONNECTOR\_OUTLOOKEMAIL("connector\_outlookemail")

CONNECTOR\_SHAREPOINT("connector\_sharepoint")

Optional<Boolean> deferLoading

Whether this MCP tool is deferred and discovered via tool search.

Optional<Headers> headers

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

Optional<RequireApproval> requireApproval

Specify which of the MCP server’s tools require approval.

class McpToolApprovalFilter:

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

Optional<Always> always

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<Never> never

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

enum McpToolApprovalSetting:

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

ALWAYS("always")

NEVER("never")

Optional<String> serverDescription

Optional description of the MCP server, used to provide more context.

Optional<String> serverUrl

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

Optional<String> tunnelId

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter

Container container

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

String

class CodeInterpreterToolAuto:

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

JsonValue; type "auto"constant"auto"constant

Always `auto`.

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the code interpreter container.

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

JsonValue; type "code\_interpreter"constant"code\_interpreter"constant

The type of the code interpreter tool. Always `code_interpreter`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

JsonValue;

JsonValue; type "programmatic\_tool\_calling"constant"programmatic\_tool\_calling"constant

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration

JsonValue; type "image\_generation"constant"image\_generation"constant

The type of the image generation tool. Always `image_generation`.

Optional<Action> action

Whether to generate a new image or edit an existing image. Default: `auto`.

GENERATE("generate")

EDIT("edit")

AUTO("auto")

Optional<Background> background

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

TRANSPARENT("transparent")

OPAQUE("opaque")

AUTO("auto")

Optional<InputFidelity> inputFidelity

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

HIGH("high")

LOW("low")

Optional<InputImageMask> inputImageMask

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

Optional<String> fileId

File ID for the mask image.

Optional<String> imageUrl

Base64-encoded mask image.

Optional<Model> model

The image generation model to use. Default: `gpt-image-1`.

GPT\_IMAGE\_1("gpt-image-1")

GPT\_IMAGE\_1\_MINI("gpt-image-1-mini")

GPT\_IMAGE\_2("gpt-image-2")

GPT\_IMAGE\_2\_2026\_04\_21("gpt-image-2-2026-04-21")

GPT\_IMAGE\_1\_5("gpt-image-1.5")

CHATGPT\_IMAGE\_LATEST("chatgpt-image-latest")

Optional<Moderation> moderation

Moderation level for the generated image. Default: `auto`.

AUTO("auto")

LOW("low")

Optional<Long> outputCompression

Compression level for the output image. Default: 100.

minimum0

maximum100

Optional<OutputFormat> outputFormat

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

PNG("png")

WEBP("webp")

JPEG("jpeg")

Optional<Long> partialImages

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

Optional<Quality> quality

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

LOW("low")

MEDIUM("medium")

HIGH("high")

AUTO("auto")

Optional<Size> size

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

\_1024X1024("1024x1024")

\_1024X1536("1024x1536")

\_1536X1024("1536x1024")

AUTO("auto")

JsonValue;

JsonValue; type "local\_shell"constant"local\_shell"constant

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool:

A tool that allows the model to execute shell commands.

JsonValue; type "shell"constant"shell"constant

The type of the shell tool. Always `shell`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Environment> environment

class BetaContainerAuto:

JsonValue; type "container\_auto"constant"container\_auto"constant

Automatically creates a container for this request

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the container.

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

Optional<List<Skill>> skills

An optional list of skills referenced by id or inline data.

class BetaSkillReference:

String skillId

The ID of the referenced skill.

maxLength64

minLength1

JsonValue; type "skill\_reference"constant"skill\_reference"constant

References a skill created with the /v1/skills endpoint.

Optional<String> version

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class BetaInlineSkill:

String description

The description of the skill.

String name

The name of the skill.

[BetaInlineSkillSource](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) source

Inline skill payload

String data

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

JsonValue; mediaType "application/zip"constant"application/zip"constant

The media type of the inline skill payload. Must be `application/zip`.

JsonValue; type "base64"constant"base64"constant

The type of the inline skill source. Must be `base64`.

JsonValue; type "inline"constant"inline"constant

Defines an inline skill for this request.

class BetaLocalEnvironment:

JsonValue; type "local"constant"local"constant

Use a local computer environment.

Optional<List<[BetaLocalSkill](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))>> skills

An optional list of skills.

String description

The description of the skill.

String name

The name of the skill.

String path

The path to the directory containing the skill.

class BetaContainerReference:

String containerId

The ID of the referenced container.

JsonValue; type "container\_reference"constant"container\_reference"constant

References a container created with the /v1/containers endpoint

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<Format> format

The input format for the custom tool. Default is unconstrained text.

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

A grammar defined by the user.

String definition

The grammar definition.

Syntax syntax

The syntax of the grammar definition. One of `lark` or `regex`.

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

Grammar format. Always `grammar`.

class BetaNamespaceTool:

Groups function/custom tools under a shared namespace.

String description

A description of the namespace shown to the model.

minLength1

String name

The namespace name used in tool calls (for example, `crm`).

minLength1

List<Tool> tools

The function/custom tools available inside this namespace.

class Function:

String name

maxLength128

minLength1

JsonValue; type "function"constant"function"constant

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this function should be deferred and discovered via tool search.

Optional<String> description

Optional<OutputSchema> outputSchema

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

Optional<JsonValue> parameters

Optional<Boolean> strict

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<Format> format

The input format for the custom tool. Default is unconstrained text.

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

A grammar defined by the user.

String definition

The grammar definition.

Syntax syntax

The syntax of the grammar definition. One of `lark` or `regex`.

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

Grammar format. Always `grammar`.

JsonValue; type "namespace"constant"namespace"constant

The type of the tool. Always `namespace`.

class BetaToolSearchTool:

Hosted or BYOT tool search configuration for deferred tools.

JsonValue; type "tool\_search"constant"tool\_search"constant

The type of the tool. Always `tool_search`.

Optional<String> description

Description shown to the model for a client-executed tool search tool.

Optional<Execution> execution

Whether tool search is executed by the server or by the client.

SERVER("server")

CLIENT("client")

Optional<JsonValue> parameters

Parameter schema for a client-executed tool search tool.

class BetaWebSearchPreviewTool:

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

WEB\_SEARCH\_PREVIEW("web\_search\_preview")

WEB\_SEARCH\_PREVIEW\_2025\_03\_11("web\_search\_preview\_2025\_03\_11")

Optional<List<SearchContentType>> searchContentTypes

TEXT("text")

IMAGE("image")

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The user’s location.

JsonValue; type "approximate"constant"approximate"constant

The type of location approximation. Always `approximate`.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

class BetaApplyPatchTool:

Allows the assistant to create, delete, or update files using unified diffs.

JsonValue; type "apply\_patch"constant"apply\_patch"constant

The type of the tool. Always `apply_patch`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

JsonValue; type "additional\_tools"constant"additional\_tools"constant

The item type. Always `additional_tools`.

Optional<String> id

The unique ID of this additional tools item.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseReasoningItem:

A description of the chain of thought used by a reasoning model while generating
a response. Be sure to include these items in your `input` to the Responses API
for subsequent turns of a conversation if you are manually
[managing context](https://platform.openai.com/docs/guides/conversation-state).

String id

The unique identifier of the reasoning content.

List<Summary> summary

Reasoning summary content.

String text

A summary of the reasoning output from the model so far.

JsonValue; type "summary\_text"constant"summary\_text"constant

The type of the object. Always `summary_text`.

JsonValue; type "reasoning"constant"reasoning"constant

The type of the object. Always `reasoning`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<List<Content>> content

Reasoning text content.

String text

The reasoning text from the model.

JsonValue; type "reasoning\_text"constant"reasoning\_text"constant

The type of the reasoning text. Always `reasoning_text`.

Optional<String> encryptedContent

The encrypted content of the reasoning item. This is populated by default
for reasoning items returned by `POST /v1/responses` and WebSocket
`response.create` requests.

Optional<Status> status

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

class BetaResponseCompactionItemParam:

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

String encryptedContent

The encrypted content of the compaction summary.

maxLength10485760

JsonValue; type "compaction"constant"compaction"constant

The type of the item. Always `compaction`.

Optional<String> id

The ID of the compaction item.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

ImageGenerationCall

String id

The unique ID of the image generation call.

Optional<String> result

The generated image encoded in base64.

Status status

The status of the image generation call.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

GENERATING("generating")

FAILED("failed")

JsonValue; type "image\_generation\_call"constant"image\_generation\_call"constant

The type of the image generation call. Always `image_generation_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseCodeInterpreterToolCall:

A tool call to run code.

String id

The unique ID of the code interpreter tool call.

Optional<String> code

The code to run, or null if not available.

String containerId

The ID of the container used to run the code.

Optional<List<Output>> outputs

The outputs generated by the code interpreter, such as logs or images.
Can be null if no outputs are available.

class Logs:

The logs output from the code interpreter.

String logs

The logs output from the code interpreter.

JsonValue; type "logs"constant"logs"constant

The type of the output. Always `logs`.

class Image:

The image output from the code interpreter.

JsonValue; type "image"constant"image"constant

The type of the output. Always `image`.

String url

The URL of the image output from the code interpreter.

formaturi

Status status

The status of the code interpreter tool call. Valid values are `in_progress`, `completed`, `incomplete`, `interpreting`, and `failed`.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

INTERPRETING("interpreting")

FAILED("failed")

JsonValue; type "code\_interpreter\_call"constant"code\_interpreter\_call"constant

The type of the code interpreter tool call. Always `code_interpreter_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

LocalShellCall

String id

The unique ID of the local shell call.

Action action

Execute a shell command on the server.

List<String> command

The command to run.

Env env

Environment variables to set for the command.

JsonValue; type "exec"constant"exec"constant

The type of the local shell action. Always `exec`.

Optional<Long> timeoutMs

Optional timeout in milliseconds for the command.

Optional<String> user

Optional user to run the command as.

Optional<String> workingDirectory

Optional working directory to run the command in.

String callId

The unique ID of the local shell tool call generated by the model.

Status status

The status of the local shell call.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "local\_shell\_call"constant"local\_shell\_call"constant

The type of the local shell call. Always `local_shell_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

LocalShellCallOutput

String id

The unique ID of the local shell tool call generated by the model.

String output

A JSON string of the output of the local shell tool call.

JsonValue; type "local\_shell\_call\_output"constant"local\_shell\_call\_output"constant

The type of the local shell tool call output. Always `local_shell_call_output`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Status> status

The status of the item. One of `in_progress`, `completed`, or `incomplete`.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

ShellCall

Action action

The shell commands and limits that describe how to run the tool call.

List<String> commands

Ordered shell commands for the execution environment to run.

Optional<Long> maxOutputLength

Maximum number of UTF-8 characters to capture from combined stdout and stderr output.

Optional<Long> timeoutMs

Maximum wall-clock time in milliseconds to allow the shell commands to run.

String callId

The unique ID of the shell tool call generated by the model.

maxLength64

minLength1

JsonValue; type "shell\_call"constant"shell\_call"constant

The type of the item. Always `shell_call`.

Optional<String> id

The unique ID of the shell tool call. Populated when this item is returned via API.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

The caller type. Always `direct`.

class Program:

String callerId

The call ID of the program item that produced this tool call.

maxLength64

minLength1

JsonValue; type "program"constant"program"constant

The caller type. Always `program`.

Optional<Environment> environment

The environment to execute the shell commands in.

class BetaLocalEnvironment:

JsonValue; type "local"constant"local"constant

Use a local computer environment.

Optional<List<[BetaLocalSkill](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))>> skills

An optional list of skills.

String description

The description of the skill.

String name

The name of the skill.

String path

The path to the directory containing the skill.

class BetaContainerReference:

String containerId

The ID of the referenced container.

JsonValue; type "container\_reference"constant"container\_reference"constant

References a container created with the /v1/containers endpoint

Optional<Status> status

The status of the shell call. One of `in_progress`, `completed`, or `incomplete`.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

ShellCallOutput

String callId

The unique ID of the shell tool call generated by the model.

maxLength64

minLength1

List<[BetaResponseFunctionShellCallOutputContent](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_shell_call_output_content%20%3E%20(schema))> output

Captured chunks of stdout and stderr output, along with their associated outcomes.

Outcome outcome

The exit or timeout outcome associated with this shell call.

JsonValue;

JsonValue; type "timeout"constant"timeout"constant

The outcome type. Always `timeout`.

class Exit:

Indicates that the shell commands finished and returned an exit code.

long exitCode

The exit code returned by the shell process.

JsonValue; type "exit"constant"exit"constant

The outcome type. Always `exit`.

String stderr

Captured stderr output for the shell call.

maxLength10485760

String stdout

Captured stdout output for the shell call.

maxLength10485760

JsonValue; type "shell\_call\_output"constant"shell\_call\_output"constant

The type of the item. Always `shell_call_output`.

Optional<String> id

The unique ID of the shell tool call output. Populated when this item is returned via API.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

The caller type. Always `direct`.

class Program:

String callerId

The call ID of the program item that produced this tool call.

maxLength64

minLength1

JsonValue; type "program"constant"program"constant

The caller type. Always `program`.

Optional<Long> maxOutputLength

The maximum number of UTF-8 characters captured for this shell call’s combined output.

Optional<Status> status

The status of the shell call output.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

ApplyPatchCall

String callId

The unique ID of the apply patch tool call generated by the model.

maxLength64

minLength1

Operation operation

The specific create, delete, or update instruction for the apply\_patch tool call.

class CreateFile:

Instruction for creating a new file via the apply\_patch tool.

String diff

Unified diff content to apply when creating the file.

maxLength10485760

String path

Path of the file to create relative to the workspace root.

minLength1

JsonValue; type "create\_file"constant"create\_file"constant

The operation type. Always `create_file`.

class DeleteFile:

Instruction for deleting an existing file via the apply\_patch tool.

String path

Path of the file to delete relative to the workspace root.

minLength1

JsonValue; type "delete\_file"constant"delete\_file"constant

The operation type. Always `delete_file`.

class UpdateFile:

Instruction for updating an existing file via the apply\_patch tool.

String diff

Unified diff content to apply to the existing file.

maxLength10485760

String path

Path of the file to update relative to the workspace root.

minLength1

JsonValue; type "update\_file"constant"update\_file"constant

The operation type. Always `update_file`.

Status status

The status of the apply patch tool call. One of `in_progress` or `completed`.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

JsonValue; type "apply\_patch\_call"constant"apply\_patch\_call"constant

The type of the item. Always `apply_patch_call`.

Optional<String> id

The unique ID of the apply patch tool call. Populated when this item is returned via API.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

The caller type. Always `direct`.

class Program:

String callerId

The call ID of the program item that produced this tool call.

maxLength64

minLength1

JsonValue; type "program"constant"program"constant

The caller type. Always `program`.

ApplyPatchCallOutput

String callId

The unique ID of the apply patch tool call generated by the model.

maxLength64

minLength1

Status status

The status of the apply patch tool call output. One of `completed` or `failed`.

COMPLETED("completed")

FAILED("failed")

JsonValue; type "apply\_patch\_call\_output"constant"apply\_patch\_call\_output"constant

The type of the item. Always `apply_patch_call_output`.

Optional<String> id

The unique ID of the apply patch tool call output. Populated when this item is returned via API.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

The caller type. Always `direct`.

class Program:

String callerId

The call ID of the program item that produced this tool call.

maxLength64

minLength1

JsonValue; type "program"constant"program"constant

The caller type. Always `program`.

Optional<String> output

Optional human-readable log text from the apply patch tool (e.g., patch results or errors).

maxLength10485760

McpListTools

String id

The unique ID of the list.

String serverLabel

The label of the MCP server.

List<Tool> tools

The tools available on the server.

JsonValue inputSchema

The JSON schema describing the tool’s input.

String name

The name of the tool.

Optional<JsonValue> annotations

Additional annotations about the tool.

Optional<String> description

The description of the tool.

JsonValue; type "mcp\_list\_tools"constant"mcp\_list\_tools"constant

The type of the item. Always `mcp_list_tools`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<String> error

Error message if the server could not list tools.

McpApprovalRequest

String id

The unique ID of the approval request.

String arguments

A JSON string of arguments for the tool.

String name

The name of the tool to run.

String serverLabel

The label of the MCP server making the request.

JsonValue; type "mcp\_approval\_request"constant"mcp\_approval\_request"constant

The type of the item. Always `mcp_approval_request`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

McpApprovalResponse

String approvalRequestId

The ID of the approval request being answered.

boolean approve

Whether the request was approved.

JsonValue; type "mcp\_approval\_response"constant"mcp\_approval\_response"constant

The type of the item. Always `mcp_approval_response`.

Optional<String> id

The unique ID of the approval response

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<String> reason

Optional reason for the decision.

McpCall

String id

The unique ID of the tool call.

String arguments

A JSON string of the arguments passed to the tool.

String name

The name of the tool that was run.

String serverLabel

The label of the MCP server running the tool.

JsonValue; type "mcp\_call"constant"mcp\_call"constant

The type of the item. Always `mcp_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<String> approvalRequestId

Unique identifier for the MCP tool call approval request.
Include this value in a subsequent `mcp_approval_response` input to approve or reject the corresponding tool call.

Optional<String> error

The error from the tool call, if any.

Optional<String> output

The output from the tool call.

Optional<Status> status

The status of the tool call. One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

CALLING("calling")

FAILED("failed")

class BetaResponseCustomToolCallOutput:

The output of a custom tool call from your code, being sent back to the model.

String callId

The call ID, used to map this custom tool call output to a custom tool call.

Output output

The output from the custom tool call generated by your code.
Can be a string or an list of output content.

String

List<BetaFunctionAndCustomToolCallOutput>

class BetaResponseInputText:

A text input to the model.

String text

The text input to the model.

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputImage:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail detail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

JsonValue; type "input\_image"constant"input\_image"constant

The type of the input item. Always `input_image`.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> imageUrl

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile:

A file input to the model.

JsonValue; type "input\_file"constant"input\_file"constant

The type of the input item. Always `input_file`.

Optional<Detail> detail

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

AUTO("auto")

LOW("low")

HIGH("high")

Optional<String> fileData

The content of the file to be sent to the model.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> fileUrl

The URL of the file to be sent to the model.

formaturi

Optional<String> filename

The name of the file to be sent to the model.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

JsonValue; type "custom\_tool\_call\_output"constant"custom\_tool\_call\_output"constant

The type of the custom tool call output. Always `custom_tool_call_output`.

Optional<String> id

The unique ID of the custom tool call output in the OpenAI platform.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

The caller type. Always `direct`.

class Program:

String callerId

The call ID of the program item that produced this tool call.

maxLength64

minLength1

JsonValue; type "program"constant"program"constant

The caller type. Always `program`.

class BetaResponseCustomToolCall:

A call to a custom tool created by the model.

String callId

An identifier used to map this custom tool call to a tool call output.

String input

The input for the custom tool call generated by the model.

String name

The name of the custom tool being called.

JsonValue; type "custom\_tool\_call"constant"custom\_tool\_call"constant

The type of the custom tool call. Always `custom_tool_call`.

Optional<String> id

The unique ID of the custom tool call in the OpenAI platform.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

class Program:

String callerId

The call ID of the program item that produced this tool call.

JsonValue; type "program"constant"program"constant

Optional<String> namespace

The namespace of the custom tool being called.

CompactionTrigger

JsonValue; type "compaction\_trigger"constant"compaction\_trigger"constant

The type of the item. Always `compaction_trigger`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

ItemReference

String id

The ID of the item to reference.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Type> type

The type of item to reference. Always `item_reference`.

Program

String id

The unique ID of this program item.

String callId

The stable call ID of the program item.

maxLength64

minLength1

String code

The JavaScript source executed by programmatic tool calling.

maxLength10485760

String fingerprint

Opaque program replay fingerprint that must be round-tripped.

maxLength10485760

JsonValue; type "program"constant"program"constant

The item type. Always `program`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

ProgramOutput

String id

The unique ID of this program output item.

String callId

The call ID of the program item.

maxLength64

minLength1

String result

The result produced by the program item.

maxLength10485760

Status status

The terminal status of the program output.

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "program\_output"constant"program\_output"constant

The item type. Always `program_output`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Metadata> metadata

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

Model model

Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model guide](https://platform.openai.com/docs/models)
to browse and compare available models.

GPT\_5\_6\_SOL("gpt-5.6-sol")

GPT\_5\_6\_TERRA("gpt-5.6-terra")

GPT\_5\_6\_LUNA("gpt-5.6-luna")

GPT\_5\_4("gpt-5.4")

GPT\_5\_4\_MINI("gpt-5.4-mini")

GPT\_5\_4\_NANO("gpt-5.4-nano")

GPT\_5\_4\_MINI\_2026\_03\_17("gpt-5.4-mini-2026-03-17")

GPT\_5\_4\_NANO\_2026\_03\_17("gpt-5.4-nano-2026-03-17")

GPT\_5\_3\_CHAT\_LATEST("gpt-5.3-chat-latest")

GPT\_5\_2("gpt-5.2")

GPT\_5\_2\_2025\_12\_11("gpt-5.2-2025-12-11")

GPT\_5\_2\_CHAT\_LATEST("gpt-5.2-chat-latest")

GPT\_5\_2\_PRO("gpt-5.2-pro")

GPT\_5\_2\_PRO\_2025\_12\_11("gpt-5.2-pro-2025-12-11")

GPT\_5\_1("gpt-5.1")

GPT\_5\_1\_2025\_11\_13("gpt-5.1-2025-11-13")

GPT\_5\_1\_CODEX("gpt-5.1-codex")

GPT\_5\_1\_MINI("gpt-5.1-mini")

GPT\_5\_1\_CHAT\_LATEST("gpt-5.1-chat-latest")

GPT\_5("gpt-5")

GPT\_5\_MINI("gpt-5-mini")

GPT\_5\_NANO("gpt-5-nano")

GPT\_5\_2025\_08\_07("gpt-5-2025-08-07")

GPT\_5\_MINI\_2025\_08\_07("gpt-5-mini-2025-08-07")

GPT\_5\_NANO\_2025\_08\_07("gpt-5-nano-2025-08-07")

GPT\_5\_CHAT\_LATEST("gpt-5-chat-latest")

GPT\_4\_1("gpt-4.1")

GPT\_4\_1\_MINI("gpt-4.1-mini")

GPT\_4\_1\_NANO("gpt-4.1-nano")

GPT\_4\_1\_2025\_04\_14("gpt-4.1-2025-04-14")

GPT\_4\_1\_MINI\_2025\_04\_14("gpt-4.1-mini-2025-04-14")

GPT\_4\_1\_NANO\_2025\_04\_14("gpt-4.1-nano-2025-04-14")

O4\_MINI("o4-mini")

O4\_MINI\_2025\_04\_16("o4-mini-2025-04-16")

O3("o3")

O3\_2025\_04\_16("o3-2025-04-16")

O3\_MINI("o3-mini")

O3\_MINI\_2025\_01\_31("o3-mini-2025-01-31")

O1("o1")

O1\_2024\_12\_17("o1-2024-12-17")

O1\_PREVIEW("o1-preview")

O1\_PREVIEW\_2024\_09\_12("o1-preview-2024-09-12")

O1\_MINI("o1-mini")

O1\_MINI\_2024\_09\_12("o1-mini-2024-09-12")

GPT\_4O("gpt-4o")

GPT\_4O\_2024\_11\_20("gpt-4o-2024-11-20")

GPT\_4O\_2024\_08\_06("gpt-4o-2024-08-06")

GPT\_4O\_2024\_05\_13("gpt-4o-2024-05-13")

GPT\_4O\_AUDIO\_PREVIEW("gpt-4o-audio-preview")

GPT\_4O\_AUDIO\_PREVIEW\_2024\_10\_01("gpt-4o-audio-preview-2024-10-01")

GPT\_4O\_AUDIO\_PREVIEW\_2024\_12\_17("gpt-4o-audio-preview-2024-12-17")

GPT\_4O\_AUDIO\_PREVIEW\_2025\_06\_03("gpt-4o-audio-preview-2025-06-03")

GPT\_4O\_MINI\_AUDIO\_PREVIEW("gpt-4o-mini-audio-preview")

GPT\_4O\_MINI\_AUDIO\_PREVIEW\_2024\_12\_17("gpt-4o-mini-audio-preview-2024-12-17")

GPT\_4O\_SEARCH\_PREVIEW("gpt-4o-search-preview")

GPT\_4O\_MINI\_SEARCH\_PREVIEW("gpt-4o-mini-search-preview")

GPT\_4O\_SEARCH\_PREVIEW\_2025\_03\_11("gpt-4o-search-preview-2025-03-11")

GPT\_4O\_MINI\_SEARCH\_PREVIEW\_2025\_03\_11("gpt-4o-mini-search-preview-2025-03-11")

CHATGPT\_4O\_LATEST("chatgpt-4o-latest")

CODEX\_MINI\_LATEST("codex-mini-latest")

GPT\_4O\_MINI("gpt-4o-mini")

GPT\_4O\_MINI\_2024\_07\_18("gpt-4o-mini-2024-07-18")

GPT\_4\_TURBO("gpt-4-turbo")

GPT\_4\_TURBO\_2024\_04\_09("gpt-4-turbo-2024-04-09")

GPT\_4\_0125\_PREVIEW("gpt-4-0125-preview")

GPT\_4\_TURBO\_PREVIEW("gpt-4-turbo-preview")

GPT\_4\_1106\_PREVIEW("gpt-4-1106-preview")

GPT\_4\_VISION\_PREVIEW("gpt-4-vision-preview")

GPT\_4("gpt-4")

GPT\_4\_0314("gpt-4-0314")

GPT\_4\_0613("gpt-4-0613")

GPT\_4\_32K("gpt-4-32k")

GPT\_4\_32K\_0314("gpt-4-32k-0314")

GPT\_4\_32K\_0613("gpt-4-32k-0613")

GPT\_3\_5\_TURBO("gpt-3.5-turbo")

GPT\_3\_5\_TURBO\_16K("gpt-3.5-turbo-16k")

GPT\_3\_5\_TURBO\_0301("gpt-3.5-turbo-0301")

GPT\_3\_5\_TURBO\_0613("gpt-3.5-turbo-0613")

GPT\_3\_5\_TURBO\_1106("gpt-3.5-turbo-1106")

GPT\_3\_5\_TURBO\_0125("gpt-3.5-turbo-0125")

GPT\_3\_5\_TURBO\_16K\_0613("gpt-3.5-turbo-16k-0613")

O1\_PRO("o1-pro")

O1\_PRO\_2025\_03\_19("o1-pro-2025-03-19")

O3\_PRO("o3-pro")

O3\_PRO\_2025\_06\_10("o3-pro-2025-06-10")

O3\_DEEP\_RESEARCH("o3-deep-research")

O3\_DEEP\_RESEARCH\_2025\_06\_26("o3-deep-research-2025-06-26")

O4\_MINI\_DEEP\_RESEARCH("o4-mini-deep-research")

O4\_MINI\_DEEP\_RESEARCH\_2025\_06\_26("o4-mini-deep-research-2025-06-26")

COMPUTER\_USE\_PREVIEW("computer-use-preview")

COMPUTER\_USE\_PREVIEW\_2025\_03\_11("computer-use-preview-2025-03-11")

GPT\_5\_CODEX("gpt-5-codex")

GPT\_5\_PRO("gpt-5-pro")

GPT\_5\_PRO\_2025\_10\_06("gpt-5-pro-2025-10-06")

GPT\_5\_1\_CODEX\_MAX("gpt-5.1-codex-max")

JsonValue; object\_ "response"constant"response"constant

The object type of this resource - always set to `response`.

List<[BetaResponseOutputItem](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema))> output

An array of content items generated by the model.

* The length and order of items in the `output` array is dependent
  on the model’s response.
* Rather than accessing the first item in the `output` array and
  assuming it’s an `assistant` message with the content generated by
  the model, you might consider using the `output_text` property where
  supported in SDKs.

class BetaResponseOutputMessage:

An output message from the model.

String id

The unique ID of the output message.

List<Content> content

The content of the output message.

class BetaResponseOutputText:

A text output from the model.

List<Annotation> annotations

The annotations of the text output.

class FileCitation:

A citation to a file.

String fileId

The ID of the file.

String filename

The filename of the file cited.

long index

The index of the file in the list of files.

JsonValue; type "file\_citation"constant"file\_citation"constant

The type of the file citation. Always `file_citation`.

class UrlCitation:

A citation for a web resource used to generate a model response.

long endIndex

The index of the last character of the URL citation in the message.

long startIndex

The index of the first character of the URL citation in the message.

String title

The title of the web resource.

JsonValue; type "url\_citation"constant"url\_citation"constant

The type of the URL citation. Always `url_citation`.

String url

The URL of the web resource.

formaturi

class ContainerFileCitation:

A citation for a container file used to generate a model response.

String containerId

The ID of the container file.

long endIndex

The index of the last character of the container file citation in the message.

String fileId

The ID of the file.

String filename

The filename of the container file cited.

long startIndex

The index of the first character of the container file citation in the message.

JsonValue; type "container\_file\_citation"constant"container\_file\_citation"constant

The type of the container file citation. Always `container_file_citation`.

class FilePath:

A path to a file.

String fileId

The ID of the file.

long index

The index of the file in the list of files.

JsonValue; type "file\_path"constant"file\_path"constant

The type of the file path. Always `file_path`.

String text

The text output from the model.

JsonValue; type "output\_text"constant"output\_text"constant

The type of the output text. Always `output_text`.

Optional<List<Logprob>> logprobs

String token

List<long> bytes

double logprob

List<TopLogprob> topLogprobs

String token

List<long> bytes

double logprob

class BetaResponseOutputRefusal:

A refusal from the model.

String refusal

The refusal explanation from the model.

JsonValue; type "refusal"constant"refusal"constant

The type of the refusal. Always `refusal`.

JsonValue; role "assistant"constant"assistant"constant

The role of the output message. Always `assistant`.

Status status

The status of the message input. One of `in_progress`, `completed`, or
`incomplete`. Populated when input items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "message"constant"message"constant

The type of the output message. Always `message`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Phase> phase

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

COMMENTARY("commentary")

FINAL\_ANSWER("final\_answer")

class BetaResponseFileSearchToolCall:

The results of a file search tool call. See the
[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

String id

The unique ID of the file search tool call.

List<String> queries

The queries used to search for files.

Status status

The status of the file search tool call. One of `in_progress`,
`searching`, `incomplete` or `failed`,

IN\_PROGRESS("in\_progress")

SEARCHING("searching")

COMPLETED("completed")

INCOMPLETE("incomplete")

FAILED("failed")

JsonValue; type "file\_search\_call"constant"file\_search\_call"constant

The type of the file search tool call. Always `file_search_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<List<Result>> results

The results of the file search tool call.

Optional<Attributes> attributes

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

String

double

boolean

Optional<String> fileId

The unique ID of the file.

Optional<String> filename

The name of the file.

Optional<Double> score

The relevance score of the file - a value between 0 and 1.

formatfloat

Optional<String> text

The text that was retrieved from the file.

class BetaResponseFunctionToolCall:

A tool call to run a function. See the
[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

String arguments

A JSON string of the arguments to pass to the function.

String callId

The unique ID of the function tool call generated by the model.

String name

The name of the function to run.

JsonValue; type "function\_call"constant"function\_call"constant

The type of the function tool call. Always `function_call`.

Optional<String> id

The unique ID of the function tool call.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

class Program:

String callerId

The call ID of the program item that produced this tool call.

JsonValue; type "program"constant"program"constant

Optional<String> namespace

The namespace of the function to run.

Optional<Status> status

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

class BetaResponseFunctionToolCallOutputItem:

String id

The unique ID of the function call tool output.

String callId

The unique ID of the function tool call generated by the model.

Output output

The output from the function call generated by your code.
Can be a string or an list of output content.

String

List<BetaFunctionAndCustomToolCallOutput>

class BetaResponseInputText:

A text input to the model.

String text

The text input to the model.

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputImage:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail detail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

JsonValue; type "input\_image"constant"input\_image"constant

The type of the input item. Always `input_image`.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> imageUrl

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile:

A file input to the model.

JsonValue; type "input\_file"constant"input\_file"constant

The type of the input item. Always `input_file`.

Optional<Detail> detail

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

AUTO("auto")

LOW("low")

HIGH("high")

Optional<String> fileData

The content of the file to be sent to the model.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> fileUrl

The URL of the file to be sent to the model.

formaturi

Optional<String> filename

The name of the file to be sent to the model.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

Status status

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "function\_call\_output"constant"function\_call\_output"constant

The type of the function tool call output. Always `function_call_output`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

The caller type. Always `direct`.

class Program:

String callerId

The call ID of the program item that produced this tool call.

maxLength64

minLength1

JsonValue; type "program"constant"program"constant

The caller type. Always `program`.

Optional<String> createdBy

The identifier of the actor that created the item.

AgentMessage

String id

The unique ID of the agent message.

String author

The sending agent identity.

List<Content> content

Encrypted content sent between agents.

class BetaResponseInputText:

A text input to the model.

String text

The text input to the model.

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseOutputText:

A text output from the model.

List<Annotation> annotations

The annotations of the text output.

class FileCitation:

A citation to a file.

String fileId

The ID of the file.

String filename

The filename of the file cited.

long index

The index of the file in the list of files.

JsonValue; type "file\_citation"constant"file\_citation"constant

The type of the file citation. Always `file_citation`.

class UrlCitation:

A citation for a web resource used to generate a model response.

long endIndex

The index of the last character of the URL citation in the message.

long startIndex

The index of the first character of the URL citation in the message.

String title

The title of the web resource.

JsonValue; type "url\_citation"constant"url\_citation"constant

The type of the URL citation. Always `url_citation`.

String url

The URL of the web resource.

formaturi

class ContainerFileCitation:

A citation for a container file used to generate a model response.

String containerId

The ID of the container file.

long endIndex

The index of the last character of the container file citation in the message.

String fileId

The ID of the file.

String filename

The filename of the container file cited.

long startIndex

The index of the first character of the container file citation in the message.

JsonValue; type "container\_file\_citation"constant"container\_file\_citation"constant

The type of the container file citation. Always `container_file_citation`.

class FilePath:

A path to a file.

String fileId

The ID of the file.

long index

The index of the file in the list of files.

JsonValue; type "file\_path"constant"file\_path"constant

The type of the file path. Always `file_path`.

String text

The text output from the model.

JsonValue; type "output\_text"constant"output\_text"constant

The type of the output text. Always `output_text`.

Optional<List<Logprob>> logprobs

String token

List<long> bytes

double logprob

List<TopLogprob> topLogprobs

String token

List<long> bytes

double logprob

class Text:

A text content.

String text

JsonValue; type "text"constant"text"constant

class SummaryText:

A summary text from the model.

String text

A summary of the reasoning output from the model so far.

JsonValue; type "summary\_text"constant"summary\_text"constant

The type of the object. Always `summary_text`.

class ReasoningText:

Reasoning text from the model.

String text

The reasoning text from the model.

JsonValue; type "reasoning\_text"constant"reasoning\_text"constant

The type of the reasoning text. Always `reasoning_text`.

class BetaResponseOutputRefusal:

A refusal from the model.

String refusal

The refusal explanation from the model.

JsonValue; type "refusal"constant"refusal"constant

The type of the refusal. Always `refusal`.

class BetaResponseInputImage:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail detail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

JsonValue; type "input\_image"constant"input\_image"constant

The type of the input item. Always `input_image`.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> imageUrl

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class ComputerScreenshot:

A screenshot of a computer.

Detail detail

The detail level of the screenshot image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

Optional<String> fileId

The identifier of an uploaded file that contains the screenshot.

Optional<String> imageUrl

The URL of the screenshot image.

formaturi

JsonValue; type "computer\_screenshot"constant"computer\_screenshot"constant

Specifies the event type. For a computer screenshot, this property is always set to `computer_screenshot`.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile:

A file input to the model.

JsonValue; type "input\_file"constant"input\_file"constant

The type of the input item. Always `input_file`.

Optional<Detail> detail

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

AUTO("auto")

LOW("low")

HIGH("high")

Optional<String> fileData

The content of the file to be sent to the model.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> fileUrl

The URL of the file to be sent to the model.

formaturi

Optional<String> filename

The name of the file to be sent to the model.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class EncryptedContent:

Opaque encrypted content that Responses API decrypts inside trusted model execution.

String encryptedContent

Opaque encrypted content.

JsonValue; type "encrypted\_content"constant"encrypted\_content"constant

The type of the input item. Always `encrypted_content`.

String recipient

The destination agent identity.

JsonValue; type "agent\_message"constant"agent\_message"constant

The type of the item. Always `agent_message`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

MultiAgentCall

String id

The unique ID of the multi-agent call item.

Action action

The multi-agent action to execute.

SPAWN\_AGENT("spawn\_agent")

INTERRUPT\_AGENT("interrupt\_agent")

LIST\_AGENTS("list\_agents")

SEND\_MESSAGE("send\_message")

FOLLOWUP\_TASK("followup\_task")

WAIT\_AGENT("wait\_agent")

String arguments

The JSON string of arguments generated for the action.

String callId

The unique ID linking this call to its output.

JsonValue; type "multi\_agent\_call"constant"multi\_agent\_call"constant

The type of the multi-agent call. Always `multi_agent_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

MultiAgentCallOutput

String id

The unique ID of the multi-agent call output item.

Action action

The multi-agent action that produced this result.

SPAWN\_AGENT("spawn\_agent")

INTERRUPT\_AGENT("interrupt\_agent")

LIST\_AGENTS("list\_agents")

SEND\_MESSAGE("send\_message")

FOLLOWUP\_TASK("followup\_task")

WAIT\_AGENT("wait\_agent")

String callId

The unique ID of the multi-agent call.

List<[BetaResponseOutputText](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema))> output

Text output returned by the multi-agent action.

List<Annotation> annotations

The annotations of the text output.

class FileCitation:

A citation to a file.

String fileId

The ID of the file.

String filename

The filename of the file cited.

long index

The index of the file in the list of files.

JsonValue; type "file\_citation"constant"file\_citation"constant

The type of the file citation. Always `file_citation`.

class UrlCitation:

A citation for a web resource used to generate a model response.

long endIndex

The index of the last character of the URL citation in the message.

long startIndex

The index of the first character of the URL citation in the message.

String title

The title of the web resource.

JsonValue; type "url\_citation"constant"url\_citation"constant

The type of the URL citation. Always `url_citation`.

String url

The URL of the web resource.

formaturi

class ContainerFileCitation:

A citation for a container file used to generate a model response.

String containerId

The ID of the container file.

long endIndex

The index of the last character of the container file citation in the message.

String fileId

The ID of the file.

String filename

The filename of the container file cited.

long startIndex

The index of the first character of the container file citation in the message.

JsonValue; type "container\_file\_citation"constant"container\_file\_citation"constant

The type of the container file citation. Always `container_file_citation`.

class FilePath:

A path to a file.

String fileId

The ID of the file.

long index

The index of the file in the list of files.

JsonValue; type "file\_path"constant"file\_path"constant

The type of the file path. Always `file_path`.

String text

The text output from the model.

JsonValue; type "output\_text"constant"output\_text"constant

The type of the output text. Always `output_text`.

Optional<List<Logprob>> logprobs

String token

List<long> bytes

double logprob

List<TopLogprob> topLogprobs

String token

List<long> bytes

double logprob

JsonValue; type "multi\_agent\_call\_output"constant"multi\_agent\_call\_output"constant

The type of the multi-agent result. Always `multi_agent_call_output`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseFunctionWebSearch:

The results of a web search tool call. See the
[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

String id

The unique ID of the web search tool call.

Action action

An object describing the specific action taken in this web search call.
Includes details on how the model used the web (search, open\_page, find\_in\_page).

class Search:

Action type “search” - Performs a web search query.

JsonValue; type "search"constant"search"constant

The action type.

Optional<List<String>> queries

The search queries.

DeprecatedOptional<String> query

The search query.

Optional<List<Source>> sources

The sources used in the search.

JsonValue; type "url"constant"url"constant

The type of source. Always `url`.

String url

The URL of the source.

formaturi

class OpenPage:

Action type “open\_page” - Opens a specific URL from search results.

JsonValue; type "open\_page"constant"open\_page"constant

The action type.

Optional<String> url

The URL opened by the model.

formaturi

class FindInPage:

Action type “find\_in\_page”: Searches for a pattern within a loaded page.

String pattern

The pattern or text to search for within the page.

JsonValue; type "find\_in\_page"constant"find\_in\_page"constant

The action type.

String url

The URL of the page searched for the pattern.

formaturi

Status status

The status of the web search tool call.

IN\_PROGRESS("in\_progress")

SEARCHING("searching")

COMPLETED("completed")

FAILED("failed")

JsonValue; type "web\_search\_call"constant"web\_search\_call"constant

The type of the web search tool call. Always `web_search_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseComputerToolCall:

A tool call to a computer use tool. See the
[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

String id

The unique ID of the computer call.

String callId

An identifier used when responding to the tool call with output.

List<PendingSafetyCheck> pendingSafetyChecks

The pending safety checks for the computer call.

String id

The ID of the pending safety check.

Optional<String> code

The type of the pending safety check.

Optional<String> message

Details about the pending safety check.

Status status

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

Type type

The type of the computer call. Always `computer_call`.

Optional<[BetaComputerAction](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action%20%3E%20(schema))> action

A click action.

Click

Button button

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

LEFT("left")

RIGHT("right")

WHEEL("wheel")

BACK("back")

FORWARD("forward")

JsonValue; type "click"constant"click"constant

Specifies the event type. For a click action, this property is always `click`.

long x

The x-coordinate where the click occurred.

long y

The y-coordinate where the click occurred.

Optional<List<String>> keys

The keys being held while clicking.

DoubleClick

Optional<List<String>> keys

The keys being held while double-clicking.

JsonValue; type "double\_click"constant"double\_click"constant

Specifies the event type. For a double click action, this property is always set to `double_click`.

long x

The x-coordinate where the double click occurred.

long y

The y-coordinate where the double click occurred.

Drag

List<Path> path

An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

[
  { x: 100, y: 200 },
  { x: 200, y: 300 }
]

long x

The x-coordinate.

long y

The y-coordinate.

JsonValue; type "drag"constant"drag"constant

Specifies the event type. For a drag action, this property is always set to `drag`.

Optional<List<String>> keys

The keys being held while dragging the mouse.

Keypress

List<String> keys

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

JsonValue; type "keypress"constant"keypress"constant

Specifies the event type. For a keypress action, this property is always set to `keypress`.

Move

JsonValue; type "move"constant"move"constant

Specifies the event type. For a move action, this property is always set to `move`.

long x

The x-coordinate to move to.

long y

The y-coordinate to move to.

Optional<List<String>> keys

The keys being held while moving the mouse.

JsonValue;

JsonValue; type "screenshot"constant"screenshot"constant

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

Scroll

long scrollX

The horizontal scroll distance.

long scrollY

The vertical scroll distance.

JsonValue; type "scroll"constant"scroll"constant

Specifies the event type. For a scroll action, this property is always set to `scroll`.

long x

The x-coordinate where the scroll occurred.

long y

The y-coordinate where the scroll occurred.

Optional<List<String>> keys

The keys being held while scrolling.

Type

String text

The text to type.

JsonValue; type "type"constant"type"constant

Specifies the event type. For a type action, this property is always set to `type`.

JsonValue;

JsonValue; type "wait"constant"wait"constant

Specifies the event type. For a wait action, this property is always set to `wait`.

Optional<List<[BetaComputerAction](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action%20%3E%20(schema))>> actions

Flattened batched actions for `computer_use`. Each action includes an
`type` discriminator and action-specific fields.

Click

Button button

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

LEFT("left")

RIGHT("right")

WHEEL("wheel")

BACK("back")

FORWARD("forward")

JsonValue; type "click"constant"click"constant

Specifies the event type. For a click action, this property is always `click`.

long x

The x-coordinate where the click occurred.

long y

The y-coordinate where the click occurred.

Optional<List<String>> keys

The keys being held while clicking.

DoubleClick

Optional<List<String>> keys

The keys being held while double-clicking.

JsonValue; type "double\_click"constant"double\_click"constant

Specifies the event type. For a double click action, this property is always set to `double_click`.

long x

The x-coordinate where the double click occurred.

long y

The y-coordinate where the double click occurred.

Drag

List<Path> path

An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

[
  { x: 100, y: 200 },
  { x: 200, y: 300 }
]

long x

The x-coordinate.

long y

The y-coordinate.

JsonValue; type "drag"constant"drag"constant

Specifies the event type. For a drag action, this property is always set to `drag`.

Optional<List<String>> keys

The keys being held while dragging the mouse.

Keypress

List<String> keys

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

JsonValue; type "keypress"constant"keypress"constant

Specifies the event type. For a keypress action, this property is always set to `keypress`.

Move

JsonValue; type "move"constant"move"constant

Specifies the event type. For a move action, this property is always set to `move`.

long x

The x-coordinate to move to.

long y

The y-coordinate to move to.

Optional<List<String>> keys

The keys being held while moving the mouse.

JsonValue;

JsonValue; type "screenshot"constant"screenshot"constant

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

Scroll

long scrollX

The horizontal scroll distance.

long scrollY

The vertical scroll distance.

JsonValue; type "scroll"constant"scroll"constant

Specifies the event type. For a scroll action, this property is always set to `scroll`.

long x

The x-coordinate where the scroll occurred.

long y

The y-coordinate where the scroll occurred.

Optional<List<String>> keys

The keys being held while scrolling.

Type

String text

The text to type.

JsonValue; type "type"constant"type"constant

Specifies the event type. For a type action, this property is always set to `type`.

JsonValue;

JsonValue; type "wait"constant"wait"constant

Specifies the event type. For a wait action, this property is always set to `wait`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseComputerToolCallOutputItem:

String id

The unique ID of the computer call tool output.

String callId

The ID of the computer tool call that produced the output.

[BetaResponseComputerToolCallOutputScreenshot](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema)) output

A computer screenshot image used with the computer use tool.

JsonValue; type "computer\_screenshot"constant"computer\_screenshot"constant

Specifies the event type. For a computer screenshot, this property is
always set to `computer_screenshot`.

Optional<String> fileId

The identifier of an uploaded file that contains the screenshot.

Optional<String> imageUrl

The URL of the screenshot image.

formaturi

Status status

The status of the message input. One of `in_progress`, `completed`, or
`incomplete`. Populated when input items are returned via API.

COMPLETED("completed")

INCOMPLETE("incomplete")

FAILED("failed")

IN\_PROGRESS("in\_progress")

JsonValue; type "computer\_call\_output"constant"computer\_call\_output"constant

The type of the computer tool call output. Always `computer_call_output`.

Optional<List<AcknowledgedSafetyCheck>> acknowledgedSafetyChecks

The safety checks reported by the API that have been acknowledged by the
developer.

String id

The ID of the pending safety check.

Optional<String> code

The type of the pending safety check.

Optional<String> message

Details about the pending safety check.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<String> createdBy

The identifier of the actor that created the item.

class BetaResponseReasoningItem:

A description of the chain of thought used by a reasoning model while generating
a response. Be sure to include these items in your `input` to the Responses API
for subsequent turns of a conversation if you are manually
[managing context](https://platform.openai.com/docs/guides/conversation-state).

String id

The unique identifier of the reasoning content.

List<Summary> summary

Reasoning summary content.

String text

A summary of the reasoning output from the model so far.

JsonValue; type "summary\_text"constant"summary\_text"constant

The type of the object. Always `summary_text`.

JsonValue; type "reasoning"constant"reasoning"constant

The type of the object. Always `reasoning`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<List<Content>> content

Reasoning text content.

String text

The reasoning text from the model.

JsonValue; type "reasoning\_text"constant"reasoning\_text"constant

The type of the reasoning text. Always `reasoning_text`.

Optional<String> encryptedContent

The encrypted content of the reasoning item. This is populated by default
for reasoning items returned by `POST /v1/responses` and WebSocket
`response.create` requests.

Optional<Status> status

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

Program

String id

The unique ID of the program item.

String callId

The stable call ID of the program item.

String code

The JavaScript source executed by programmatic tool calling.

String fingerprint

Opaque program replay fingerprint that must be round-tripped.

JsonValue; type "program"constant"program"constant

The type of the item. Always `program`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

ProgramOutput

String id

The unique ID of the program output item.

String callId

The call ID of the program item.

String result

The result produced by the program item.

Status status

The terminal status of the program output item.

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "program\_output"constant"program\_output"constant

The type of the item. Always `program_output`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseToolSearchCall:

String id

The unique ID of the tool search call item.

JsonValue arguments

Arguments used for the tool search call.

Optional<String> callId

The unique ID of the tool search call generated by the model.

Execution execution

Whether tool search was executed by the server or by the client.

SERVER("server")

CLIENT("client")

Status status

The status of the tool search call item that was recorded.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "tool\_search\_call"constant"tool\_search\_call"constant

The type of the item. Always `tool_search_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<String> createdBy

The identifier of the actor that created the item.

class BetaResponseToolSearchOutputItem:

String id

The unique ID of the tool search output item.

Optional<String> callId

The unique ID of the tool search call generated by the model.

Execution execution

Whether tool search was executed by the server or by the client.

SERVER("server")

CLIENT("client")

Status status

The status of the tool search output item that was recorded.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

List<[BetaTool](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))> tools

The loaded tool definitions returned by tool search.

class BetaFunctionTool:

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

String name

The name of the function to call.

Optional<Parameters> parameters

A JSON schema object describing the parameters of the function.

Optional<Boolean> strict

Whether strict parameter validation is enforced for this function tool.

JsonValue; type "function"constant"function"constant

The type of the function tool. Always `function`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this function is deferred and loaded via tool search.

Optional<String> description

A description of the function. Used by the model to determine whether or not to call the function.

Optional<OutputSchema> outputSchema

A JSON schema object describing the JSON value encoded in string outputs for this function.

class BetaFileSearchTool:

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

JsonValue; type "file\_search"constant"file\_search"constant

The type of the file search tool. Always `file_search`.

List<String> vectorStoreIds

The IDs of the vector stores to search.

Optional<Filters> filters

A filter to apply.

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

String

double

boolean

List<ComparisonFilterValueItem>

String

double

class CompoundFilter:

Combine multiple filters using `and` or `or`.

List<Filter> filters

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

String

double

boolean

List<ComparisonFilterValueItem>

String

double

JsonValue

Type type

Type of operation: `and` or `or`.

AND("and")

OR("or")

Optional<Long> maxNumResults

The maximum number of results to return. This number should be between 1 and 50 inclusive.

Optional<RankingOptions> rankingOptions

Ranking options for search.

Optional<HybridSearch> hybridSearch

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

double embeddingWeight

The weight of the embedding in the reciprocal ranking fusion.

double textWeight

The weight of the text in the reciprocal ranking fusion.

Optional<Ranker> ranker

The ranker to use for the file search.

AUTO("auto")

DEFAULT\_2024\_11\_15("default-2024-11-15")

Optional<Double> scoreThreshold

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class BetaComputerTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

JsonValue; type "computer"constant"computer"constant

The type of the computer tool. Always `computer`.

class BetaComputerUsePreviewTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

long displayHeight

The height of the computer display.

long displayWidth

The width of the computer display.

Environment environment

The type of computer environment to control.

WINDOWS("windows")

MAC("mac")

LINUX("linux")

UBUNTU("ubuntu")

BROWSER("browser")

JsonValue; type "computer\_use\_preview"constant"computer\_use\_preview"constant

The type of the computer use tool. Always `computer_use_preview`.

class BetaWebSearchTool:

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

WEB\_SEARCH("web\_search")

WEB\_SEARCH\_2025\_08\_26("web\_search\_2025\_08\_26")

Optional<Filters> filters

Filters for the search.

Optional<List<String>> allowedDomains

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The approximate location of the user.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

Optional<Type> type

The type of location approximation. Always `approximate`.

Mcp

String serverLabel

A label for this MCP server, used to identify it in tool calls.

JsonValue; type "mcp"constant"mcp"constant

The type of the MCP tool. Always `mcp`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<AllowedTools> allowedTools

List of allowed tool names or a filter object.

List<String>

class McpToolFilter:

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<String> authorization

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

Optional<ConnectorId> connectorId

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

CONNECTOR\_DROPBOX("connector\_dropbox")

CONNECTOR\_GMAIL("connector\_gmail")

CONNECTOR\_GOOGLECALENDAR("connector\_googlecalendar")

CONNECTOR\_GOOGLEDRIVE("connector\_googledrive")

CONNECTOR\_MICROSOFTTEAMS("connector\_microsoftteams")

CONNECTOR\_OUTLOOKCALENDAR("connector\_outlookcalendar")

CONNECTOR\_OUTLOOKEMAIL("connector\_outlookemail")

CONNECTOR\_SHAREPOINT("connector\_sharepoint")

Optional<Boolean> deferLoading

Whether this MCP tool is deferred and discovered via tool search.

Optional<Headers> headers

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

Optional<RequireApproval> requireApproval

Specify which of the MCP server’s tools require approval.

class McpToolApprovalFilter:

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

Optional<Always> always

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<Never> never

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

enum McpToolApprovalSetting:

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

ALWAYS("always")

NEVER("never")

Optional<String> serverDescription

Optional description of the MCP server, used to provide more context.

Optional<String> serverUrl

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

Optional<String> tunnelId

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter

Container container

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

String

class CodeInterpreterToolAuto:

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

JsonValue; type "auto"constant"auto"constant

Always `auto`.

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the code interpreter container.

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

JsonValue; type "code\_interpreter"constant"code\_interpreter"constant

The type of the code interpreter tool. Always `code_interpreter`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

JsonValue;

JsonValue; type "programmatic\_tool\_calling"constant"programmatic\_tool\_calling"constant

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration

JsonValue; type "image\_generation"constant"image\_generation"constant

The type of the image generation tool. Always `image_generation`.

Optional<Action> action

Whether to generate a new image or edit an existing image. Default: `auto`.

GENERATE("generate")

EDIT("edit")

AUTO("auto")

Optional<Background> background

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

TRANSPARENT("transparent")

OPAQUE("opaque")

AUTO("auto")

Optional<InputFidelity> inputFidelity

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

HIGH("high")

LOW("low")

Optional<InputImageMask> inputImageMask

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

Optional<String> fileId

File ID for the mask image.

Optional<String> imageUrl

Base64-encoded mask image.

Optional<Model> model

The image generation model to use. Default: `gpt-image-1`.

GPT\_IMAGE\_1("gpt-image-1")

GPT\_IMAGE\_1\_MINI("gpt-image-1-mini")

GPT\_IMAGE\_2("gpt-image-2")

GPT\_IMAGE\_2\_2026\_04\_21("gpt-image-2-2026-04-21")

GPT\_IMAGE\_1\_5("gpt-image-1.5")

CHATGPT\_IMAGE\_LATEST("chatgpt-image-latest")

Optional<Moderation> moderation

Moderation level for the generated image. Default: `auto`.

AUTO("auto")

LOW("low")

Optional<Long> outputCompression

Compression level for the output image. Default: 100.

minimum0

maximum100

Optional<OutputFormat> outputFormat

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

PNG("png")

WEBP("webp")

JPEG("jpeg")

Optional<Long> partialImages

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

Optional<Quality> quality

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

LOW("low")

MEDIUM("medium")

HIGH("high")

AUTO("auto")

Optional<Size> size

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

\_1024X1024("1024x1024")

\_1024X1536("1024x1536")

\_1536X1024("1536x1024")

AUTO("auto")

JsonValue;

JsonValue; type "local\_shell"constant"local\_shell"constant

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool:

A tool that allows the model to execute shell commands.

JsonValue; type "shell"constant"shell"constant

The type of the shell tool. Always `shell`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Environment> environment

class BetaContainerAuto:

JsonValue; type "container\_auto"constant"container\_auto"constant

Automatically creates a container for this request

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the container.

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

Optional<List<Skill>> skills

An optional list of skills referenced by id or inline data.

class BetaSkillReference:

String skillId

The ID of the referenced skill.

maxLength64

minLength1

JsonValue; type "skill\_reference"constant"skill\_reference"constant

References a skill created with the /v1/skills endpoint.

Optional<String> version

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class BetaInlineSkill:

String description

The description of the skill.

String name

The name of the skill.

[BetaInlineSkillSource](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) source

Inline skill payload

String data

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

JsonValue; mediaType "application/zip"constant"application/zip"constant

The media type of the inline skill payload. Must be `application/zip`.

JsonValue; type "base64"constant"base64"constant

The type of the inline skill source. Must be `base64`.

JsonValue; type "inline"constant"inline"constant

Defines an inline skill for this request.

class BetaLocalEnvironment:

JsonValue; type "local"constant"local"constant

Use a local computer environment.

Optional<List<[BetaLocalSkill](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))>> skills

An optional list of skills.

String description

The description of the skill.

String name

The name of the skill.

String path

The path to the directory containing the skill.

class BetaContainerReference:

String containerId

The ID of the referenced container.

JsonValue; type "container\_reference"constant"container\_reference"constant

References a container created with the /v1/containers endpoint

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<Format> format

The input format for the custom tool. Default is unconstrained text.

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

A grammar defined by the user.

String definition

The grammar definition.

Syntax syntax

The syntax of the grammar definition. One of `lark` or `regex`.

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

Grammar format. Always `grammar`.

class BetaNamespaceTool:

Groups function/custom tools under a shared namespace.

String description

A description of the namespace shown to the model.

minLength1

String name

The namespace name used in tool calls (for example, `crm`).

minLength1

List<Tool> tools

The function/custom tools available inside this namespace.

class Function:

String name

maxLength128

minLength1

JsonValue; type "function"constant"function"constant

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this function should be deferred and discovered via tool search.

Optional<String> description

Optional<OutputSchema> outputSchema

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

Optional<JsonValue> parameters

Optional<Boolean> strict

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<Format> format

The input format for the custom tool. Default is unconstrained text.

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

A grammar defined by the user.

String definition

The grammar definition.

Syntax syntax

The syntax of the grammar definition. One of `lark` or `regex`.

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

Grammar format. Always `grammar`.

JsonValue; type "namespace"constant"namespace"constant

The type of the tool. Always `namespace`.

class BetaToolSearchTool:

Hosted or BYOT tool search configuration for deferred tools.

JsonValue; type "tool\_search"constant"tool\_search"constant

The type of the tool. Always `tool_search`.

Optional<String> description

Description shown to the model for a client-executed tool search tool.

Optional<Execution> execution

Whether tool search is executed by the server or by the client.

SERVER("server")

CLIENT("client")

Optional<JsonValue> parameters

Parameter schema for a client-executed tool search tool.

class BetaWebSearchPreviewTool:

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

WEB\_SEARCH\_PREVIEW("web\_search\_preview")

WEB\_SEARCH\_PREVIEW\_2025\_03\_11("web\_search\_preview\_2025\_03\_11")

Optional<List<SearchContentType>> searchContentTypes

TEXT("text")

IMAGE("image")

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The user’s location.

JsonValue; type "approximate"constant"approximate"constant

The type of location approximation. Always `approximate`.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

class BetaApplyPatchTool:

Allows the assistant to create, delete, or update files using unified diffs.

JsonValue; type "apply\_patch"constant"apply\_patch"constant

The type of the tool. Always `apply_patch`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

JsonValue; type "tool\_search\_output"constant"tool\_search\_output"constant

The type of the item. Always `tool_search_output`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<String> createdBy

The identifier of the actor that created the item.

AdditionalTools

String id

The unique ID of the additional tools item.

Role role

The role that provided the additional tools.

UNKNOWN("unknown")

USER("user")

ASSISTANT("assistant")

SYSTEM("system")

CRITIC("critic")

DISCRIMINATOR("discriminator")

DEVELOPER("developer")

TOOL("tool")

List<[BetaTool](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))> tools

The additional tool definitions made available at this item.

class BetaFunctionTool:

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

String name

The name of the function to call.

Optional<Parameters> parameters

A JSON schema object describing the parameters of the function.

Optional<Boolean> strict

Whether strict parameter validation is enforced for this function tool.

JsonValue; type "function"constant"function"constant

The type of the function tool. Always `function`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this function is deferred and loaded via tool search.

Optional<String> description

A description of the function. Used by the model to determine whether or not to call the function.

Optional<OutputSchema> outputSchema

A JSON schema object describing the JSON value encoded in string outputs for this function.

class BetaFileSearchTool:

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

JsonValue; type "file\_search"constant"file\_search"constant

The type of the file search tool. Always `file_search`.

List<String> vectorStoreIds

The IDs of the vector stores to search.

Optional<Filters> filters

A filter to apply.

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

String

double

boolean

List<ComparisonFilterValueItem>

String

double

class CompoundFilter:

Combine multiple filters using `and` or `or`.

List<Filter> filters

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

String

double

boolean

List<ComparisonFilterValueItem>

String

double

JsonValue

Type type

Type of operation: `and` or `or`.

AND("and")

OR("or")

Optional<Long> maxNumResults

The maximum number of results to return. This number should be between 1 and 50 inclusive.

Optional<RankingOptions> rankingOptions

Ranking options for search.

Optional<HybridSearch> hybridSearch

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

double embeddingWeight

The weight of the embedding in the reciprocal ranking fusion.

double textWeight

The weight of the text in the reciprocal ranking fusion.

Optional<Ranker> ranker

The ranker to use for the file search.

AUTO("auto")

DEFAULT\_2024\_11\_15("default-2024-11-15")

Optional<Double> scoreThreshold

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class BetaComputerTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

JsonValue; type "computer"constant"computer"constant

The type of the computer tool. Always `computer`.

class BetaComputerUsePreviewTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

long displayHeight

The height of the computer display.

long displayWidth

The width of the computer display.

Environment environment

The type of computer environment to control.

WINDOWS("windows")

MAC("mac")

LINUX("linux")

UBUNTU("ubuntu")

BROWSER("browser")

JsonValue; type "computer\_use\_preview"constant"computer\_use\_preview"constant

The type of the computer use tool. Always `computer_use_preview`.

class BetaWebSearchTool:

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

WEB\_SEARCH("web\_search")

WEB\_SEARCH\_2025\_08\_26("web\_search\_2025\_08\_26")

Optional<Filters> filters

Filters for the search.

Optional<List<String>> allowedDomains

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The approximate location of the user.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

Optional<Type> type

The type of location approximation. Always `approximate`.

Mcp

String serverLabel

A label for this MCP server, used to identify it in tool calls.

JsonValue; type "mcp"constant"mcp"constant

The type of the MCP tool. Always `mcp`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<AllowedTools> allowedTools

List of allowed tool names or a filter object.

List<String>

class McpToolFilter:

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<String> authorization

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

Optional<ConnectorId> connectorId

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

CONNECTOR\_DROPBOX("connector\_dropbox")

CONNECTOR\_GMAIL("connector\_gmail")

CONNECTOR\_GOOGLECALENDAR("connector\_googlecalendar")

CONNECTOR\_GOOGLEDRIVE("connector\_googledrive")

CONNECTOR\_MICROSOFTTEAMS("connector\_microsoftteams")

CONNECTOR\_OUTLOOKCALENDAR("connector\_outlookcalendar")

CONNECTOR\_OUTLOOKEMAIL("connector\_outlookemail")

CONNECTOR\_SHAREPOINT("connector\_sharepoint")

Optional<Boolean> deferLoading

Whether this MCP tool is deferred and discovered via tool search.

Optional<Headers> headers

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

Optional<RequireApproval> requireApproval

Specify which of the MCP server’s tools require approval.

class McpToolApprovalFilter:

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

Optional<Always> always

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<Never> never

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

enum McpToolApprovalSetting:

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

ALWAYS("always")

NEVER("never")

Optional<String> serverDescription

Optional description of the MCP server, used to provide more context.

Optional<String> serverUrl

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

Optional<String> tunnelId

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter

Container container

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

String

class CodeInterpreterToolAuto:

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

JsonValue; type "auto"constant"auto"constant

Always `auto`.

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the code interpreter container.

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

JsonValue; type "code\_interpreter"constant"code\_interpreter"constant

The type of the code interpreter tool. Always `code_interpreter`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

JsonValue;

JsonValue; type "programmatic\_tool\_calling"constant"programmatic\_tool\_calling"constant

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration

JsonValue; type "image\_generation"constant"image\_generation"constant

The type of the image generation tool. Always `image_generation`.

Optional<Action> action

Whether to generate a new image or edit an existing image. Default: `auto`.

GENERATE("generate")

EDIT("edit")

AUTO("auto")

Optional<Background> background

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

TRANSPARENT("transparent")

OPAQUE("opaque")

AUTO("auto")

Optional<InputFidelity> inputFidelity

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

HIGH("high")

LOW("low")

Optional<InputImageMask> inputImageMask

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

Optional<String> fileId

File ID for the mask image.

Optional<String> imageUrl

Base64-encoded mask image.

Optional<Model> model

The image generation model to use. Default: `gpt-image-1`.

GPT\_IMAGE\_1("gpt-image-1")

GPT\_IMAGE\_1\_MINI("gpt-image-1-mini")

GPT\_IMAGE\_2("gpt-image-2")

GPT\_IMAGE\_2\_2026\_04\_21("gpt-image-2-2026-04-21")

GPT\_IMAGE\_1\_5("gpt-image-1.5")

CHATGPT\_IMAGE\_LATEST("chatgpt-image-latest")

Optional<Moderation> moderation

Moderation level for the generated image. Default: `auto`.

AUTO("auto")

LOW("low")

Optional<Long> outputCompression

Compression level for the output image. Default: 100.

minimum0

maximum100

Optional<OutputFormat> outputFormat

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

PNG("png")

WEBP("webp")

JPEG("jpeg")

Optional<Long> partialImages

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

Optional<Quality> quality

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

LOW("low")

MEDIUM("medium")

HIGH("high")

AUTO("auto")

Optional<Size> size

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

\_1024X1024("1024x1024")

\_1024X1536("1024x1536")

\_1536X1024("1536x1024")

AUTO("auto")

JsonValue;

JsonValue; type "local\_shell"constant"local\_shell"constant

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool:

A tool that allows the model to execute shell commands.

JsonValue; type "shell"constant"shell"constant

The type of the shell tool. Always `shell`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Environment> environment

class BetaContainerAuto:

JsonValue; type "container\_auto"constant"container\_auto"constant

Automatically creates a container for this request

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the container.

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

Optional<List<Skill>> skills

An optional list of skills referenced by id or inline data.

class BetaSkillReference:

String skillId

The ID of the referenced skill.

maxLength64

minLength1

JsonValue; type "skill\_reference"constant"skill\_reference"constant

References a skill created with the /v1/skills endpoint.

Optional<String> version

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class BetaInlineSkill:

String description

The description of the skill.

String name

The name of the skill.

[BetaInlineSkillSource](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) source

Inline skill payload

String data

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

JsonValue; mediaType "application/zip"constant"application/zip"constant

The media type of the inline skill payload. Must be `application/zip`.

JsonValue; type "base64"constant"base64"constant

The type of the inline skill source. Must be `base64`.

JsonValue; type "inline"constant"inline"constant

Defines an inline skill for this request.

class BetaLocalEnvironment:

JsonValue; type "local"constant"local"constant

Use a local computer environment.

Optional<List<[BetaLocalSkill](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))>> skills

An optional list of skills.

String description

The description of the skill.

String name

The name of the skill.

String path

The path to the directory containing the skill.

class BetaContainerReference:

String containerId

The ID of the referenced container.

JsonValue; type "container\_reference"constant"container\_reference"constant

References a container created with the /v1/containers endpoint

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<Format> format

The input format for the custom tool. Default is unconstrained text.

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

A grammar defined by the user.

String definition

The grammar definition.

Syntax syntax

The syntax of the grammar definition. One of `lark` or `regex`.

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

Grammar format. Always `grammar`.

class BetaNamespaceTool:

Groups function/custom tools under a shared namespace.

String description

A description of the namespace shown to the model.

minLength1

String name

The namespace name used in tool calls (for example, `crm`).

minLength1

List<Tool> tools

The function/custom tools available inside this namespace.

class Function:

String name

maxLength128

minLength1

JsonValue; type "function"constant"function"constant

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this function should be deferred and discovered via tool search.

Optional<String> description

Optional<OutputSchema> outputSchema

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

Optional<JsonValue> parameters

Optional<Boolean> strict

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<Format> format

The input format for the custom tool. Default is unconstrained text.

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

A grammar defined by the user.

String definition

The grammar definition.

Syntax syntax

The syntax of the grammar definition. One of `lark` or `regex`.

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

Grammar format. Always `grammar`.

JsonValue; type "namespace"constant"namespace"constant

The type of the tool. Always `namespace`.

class BetaToolSearchTool:

Hosted or BYOT tool search configuration for deferred tools.

JsonValue; type "tool\_search"constant"tool\_search"constant

The type of the tool. Always `tool_search`.

Optional<String> description

Description shown to the model for a client-executed tool search tool.

Optional<Execution> execution

Whether tool search is executed by the server or by the client.

SERVER("server")

CLIENT("client")

Optional<JsonValue> parameters

Parameter schema for a client-executed tool search tool.

class BetaWebSearchPreviewTool:

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

WEB\_SEARCH\_PREVIEW("web\_search\_preview")

WEB\_SEARCH\_PREVIEW\_2025\_03\_11("web\_search\_preview\_2025\_03\_11")

Optional<List<SearchContentType>> searchContentTypes

TEXT("text")

IMAGE("image")

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The user’s location.

JsonValue; type "approximate"constant"approximate"constant

The type of location approximation. Always `approximate`.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

class BetaApplyPatchTool:

Allows the assistant to create, delete, or update files using unified diffs.

JsonValue; type "apply\_patch"constant"apply\_patch"constant

The type of the tool. Always `apply_patch`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

JsonValue; type "additional\_tools"constant"additional\_tools"constant

The type of the item. Always `additional_tools`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseCompactionItem:

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

String id

The unique ID of the compaction item.

String encryptedContent

The encrypted content that was produced by compaction.

JsonValue; type "compaction"constant"compaction"constant

The type of the item. Always `compaction`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<String> createdBy

The identifier of the actor that created the item.

ImageGenerationCall

String id

The unique ID of the image generation call.

Optional<String> result

The generated image encoded in base64.

Status status

The status of the image generation call.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

GENERATING("generating")

FAILED("failed")

JsonValue; type "image\_generation\_call"constant"image\_generation\_call"constant

The type of the image generation call. Always `image_generation_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseCodeInterpreterToolCall:

A tool call to run code.

String id

The unique ID of the code interpreter tool call.

Optional<String> code

The code to run, or null if not available.

String containerId

The ID of the container used to run the code.

Optional<List<Output>> outputs

The outputs generated by the code interpreter, such as logs or images.
Can be null if no outputs are available.

class Logs:

The logs output from the code interpreter.

String logs

The logs output from the code interpreter.

JsonValue; type "logs"constant"logs"constant

The type of the output. Always `logs`.

class Image:

The image output from the code interpreter.

JsonValue; type "image"constant"image"constant

The type of the output. Always `image`.

String url

The URL of the image output from the code interpreter.

formaturi

Status status

The status of the code interpreter tool call. Valid values are `in_progress`, `completed`, `incomplete`, `interpreting`, and `failed`.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

INTERPRETING("interpreting")

FAILED("failed")

JsonValue; type "code\_interpreter\_call"constant"code\_interpreter\_call"constant

The type of the code interpreter tool call. Always `code_interpreter_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

LocalShellCall

String id

The unique ID of the local shell call.

Action action

Execute a shell command on the server.

List<String> command

The command to run.

Env env

Environment variables to set for the command.

JsonValue; type "exec"constant"exec"constant

The type of the local shell action. Always `exec`.

Optional<Long> timeoutMs

Optional timeout in milliseconds for the command.

Optional<String> user

Optional user to run the command as.

Optional<String> workingDirectory

Optional working directory to run the command in.

String callId

The unique ID of the local shell tool call generated by the model.

Status status

The status of the local shell call.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "local\_shell\_call"constant"local\_shell\_call"constant

The type of the local shell call. Always `local_shell_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

LocalShellCallOutput

String id

The unique ID of the local shell tool call generated by the model.

String output

A JSON string of the output of the local shell tool call.

JsonValue; type "local\_shell\_call\_output"constant"local\_shell\_call\_output"constant

The type of the local shell tool call output. Always `local_shell_call_output`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Status> status

The status of the item. One of `in_progress`, `completed`, or `incomplete`.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

class BetaResponseFunctionShellToolCall:

A tool call that executes one or more shell commands in a managed environment.

String id

The unique ID of the shell tool call. Populated when this item is returned via API.

Action action

The shell commands and limits that describe how to run the tool call.

List<String> commands

Optional<Long> maxOutputLength

Optional maximum number of characters to return from each command.

Optional<Long> timeoutMs

Optional timeout in milliseconds for the commands.

String callId

The unique ID of the shell tool call generated by the model.

Optional<Environment> environment

Represents the use of a local environment to perform shell actions.

class BetaResponseLocalEnvironment:

Represents the use of a local environment to perform shell actions.

JsonValue; type "local"constant"local"constant

The environment type. Always `local`.

class BetaResponseContainerReference:

Represents a container created with /v1/containers.

String containerId

JsonValue; type "container\_reference"constant"container\_reference"constant

The environment type. Always `container_reference`.

Status status

The status of the shell call. One of `in_progress`, `completed`, or `incomplete`.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "shell\_call"constant"shell\_call"constant

The type of the item. Always `shell_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

class Program:

String callerId

The call ID of the program item that produced this tool call.

JsonValue; type "program"constant"program"constant

Optional<String> createdBy

The ID of the entity that created this tool call.

class BetaResponseFunctionShellToolCallOutput:

The output of a shell tool call that was emitted.

String id

The unique ID of the shell call output. Populated when this item is returned via API.

String callId

The unique ID of the shell tool call generated by the model.

Optional<Long> maxOutputLength

The maximum length of the shell command output. This is generated by the model and should be passed back with the raw output.

List<Output> output

An array of shell call output contents

Outcome outcome

Represents either an exit outcome (with an exit code) or a timeout outcome for a shell call output chunk.

JsonValue;

JsonValue; type "timeout"constant"timeout"constant

The outcome type. Always `timeout`.

class Exit:

Indicates that the shell commands finished and returned an exit code.

long exitCode

Exit code from the shell process.

JsonValue; type "exit"constant"exit"constant

The outcome type. Always `exit`.

String stderr

The standard error output that was captured.

String stdout

The standard output that was captured.

Optional<String> createdBy

The identifier of the actor that created the item.

Status status

The status of the shell call output. One of `in_progress`, `completed`, or `incomplete`.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "shell\_call\_output"constant"shell\_call\_output"constant

The type of the shell call output. Always `shell_call_output`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

class Program:

String callerId

The call ID of the program item that produced this tool call.

JsonValue; type "program"constant"program"constant

Optional<String> createdBy

The identifier of the actor that created the item.

class BetaResponseApplyPatchToolCall:

A tool call that applies file diffs by creating, deleting, or updating files.

String id

The unique ID of the apply patch tool call. Populated when this item is returned via API.

String callId

The unique ID of the apply patch tool call generated by the model.

Operation operation

One of the create\_file, delete\_file, or update\_file operations applied via apply\_patch.

class CreateFile:

Instruction describing how to create a file via the apply\_patch tool.

String diff

Diff to apply.

String path

Path of the file to create.

JsonValue; type "create\_file"constant"create\_file"constant

Create a new file with the provided diff.

class DeleteFile:

Instruction describing how to delete a file via the apply\_patch tool.

String path

Path of the file to delete.

JsonValue; type "delete\_file"constant"delete\_file"constant

Delete the specified file.

class UpdateFile:

Instruction describing how to update a file via the apply\_patch tool.

String diff

Diff to apply.

String path

Path of the file to update.

JsonValue; type "update\_file"constant"update\_file"constant

Update an existing file with the provided diff.

Status status

The status of the apply patch tool call. One of `in_progress` or `completed`.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

JsonValue; type "apply\_patch\_call"constant"apply\_patch\_call"constant

The type of the item. Always `apply_patch_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

class Program:

String callerId

The call ID of the program item that produced this tool call.

JsonValue; type "program"constant"program"constant

Optional<String> createdBy

The ID of the entity that created this tool call.

class BetaResponseApplyPatchToolCallOutput:

The output emitted by an apply patch tool call.

String id

The unique ID of the apply patch tool call output. Populated when this item is returned via API.

String callId

The unique ID of the apply patch tool call generated by the model.

Status status

The status of the apply patch tool call output. One of `completed` or `failed`.

COMPLETED("completed")

FAILED("failed")

JsonValue; type "apply\_patch\_call\_output"constant"apply\_patch\_call\_output"constant

The type of the item. Always `apply_patch_call_output`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

class Program:

String callerId

The call ID of the program item that produced this tool call.

JsonValue; type "program"constant"program"constant

Optional<String> createdBy

The ID of the entity that created this tool call output.

Optional<String> output

Optional textual output returned by the apply patch tool.

McpCall

String id

The unique ID of the tool call.

String arguments

A JSON string of the arguments passed to the tool.

String name

The name of the tool that was run.

String serverLabel

The label of the MCP server running the tool.

JsonValue; type "mcp\_call"constant"mcp\_call"constant

The type of the item. Always `mcp_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<String> approvalRequestId

Unique identifier for the MCP tool call approval request.
Include this value in a subsequent `mcp_approval_response` input to approve or reject the corresponding tool call.

Optional<String> error

The error from the tool call, if any.

Optional<String> output

The output from the tool call.

Optional<Status> status

The status of the tool call. One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

CALLING("calling")

FAILED("failed")

McpListTools

String id

The unique ID of the list.

String serverLabel

The label of the MCP server.

List<Tool> tools

The tools available on the server.

JsonValue inputSchema

The JSON schema describing the tool’s input.

String name

The name of the tool.

Optional<JsonValue> annotations

Additional annotations about the tool.

Optional<String> description

The description of the tool.

JsonValue; type "mcp\_list\_tools"constant"mcp\_list\_tools"constant

The type of the item. Always `mcp_list_tools`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<String> error

Error message if the server could not list tools.

McpApprovalRequest

String id

The unique ID of the approval request.

String arguments

A JSON string of arguments for the tool.

String name

The name of the tool to run.

String serverLabel

The label of the MCP server making the request.

JsonValue; type "mcp\_approval\_request"constant"mcp\_approval\_request"constant

The type of the item. Always `mcp_approval_request`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

McpApprovalResponse

String id

The unique ID of the approval response

String approvalRequestId

The ID of the approval request being answered.

boolean approve

Whether the request was approved.

JsonValue; type "mcp\_approval\_response"constant"mcp\_approval\_response"constant

The type of the item. Always `mcp_approval_response`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<String> reason

Optional reason for the decision.

class BetaResponseCustomToolCall:

A call to a custom tool created by the model.

String callId

An identifier used to map this custom tool call to a tool call output.

String input

The input for the custom tool call generated by the model.

String name

The name of the custom tool being called.

JsonValue; type "custom\_tool\_call"constant"custom\_tool\_call"constant

The type of the custom tool call. Always `custom_tool_call`.

Optional<String> id

The unique ID of the custom tool call in the OpenAI platform.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

class Program:

String callerId

The call ID of the program item that produced this tool call.

JsonValue; type "program"constant"program"constant

Optional<String> namespace

The namespace of the custom tool being called.

class BetaResponseCustomToolCallOutputItem:

The output of a custom tool call from your code, being sent back to the model.

String id

The unique ID of the custom tool call output item.

Status status

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

Optional<String> createdBy

The identifier of the actor that created the item.

boolean parallelToolCalls

Whether to allow the model to run tool calls in parallel.

Optional<Double> temperature

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
We generally recommend altering this or `top_p` but not both.

minimum0

maximum2

ToolChoice toolChoice

How the model should select which tool (or tools) to use when generating
a response. See the `tools` parameter to see how to specify which tools
the model can call.

enum BetaToolChoiceOptions:

Controls which (if any) tool is called by the model.

`none` means the model will not call any tool and instead generates a message.

`auto` means the model can pick between generating a message or calling one or
more tools.

`required` means the model must call one or more tools.

NONE("none")

AUTO("auto")

REQUIRED("required")

class BetaToolChoiceAllowed:

Constrains the tools available to the model to a pre-defined set.

Mode mode

Constrains the tools available to the model to a pre-defined set.

`auto` allows the model to pick from among the allowed tools and generate a
message.

`required` requires the model to call one or more of the allowed tools.

AUTO("auto")

REQUIRED("required")

List<Tool> tools

A list of tool definitions that the model should be allowed to call.

For the Responses API, the list of tool definitions might look like:

[
  { "type": "function", "name": "get_weather" },
  { "type": "mcp", "server_label": "deepwiki" },
  { "type": "image_generation" }
]

JsonValue; type "allowed\_tools"constant"allowed\_tools"constant

Allowed tool configuration type. Always `allowed_tools`.

class BetaToolChoiceTypes:

Indicates that the model should use a built-in tool to generate a response.
[Learn more about built-in tools](https://platform.openai.com/docs/guides/tools).

Type type

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

FILE\_SEARCH("file\_search")

WEB\_SEARCH\_PREVIEW("web\_search\_preview")

COMPUTER("computer")

COMPUTER\_USE\_PREVIEW("computer\_use\_preview")

COMPUTER\_USE("computer\_use")

WEB\_SEARCH\_PREVIEW\_2025\_03\_11("web\_search\_preview\_2025\_03\_11")

IMAGE\_GENERATION("image\_generation")

CODE\_INTERPRETER("code\_interpreter")

class BetaToolChoiceFunction:

Use this option to force the model to call a specific function.

String name

The name of the function to call.

JsonValue; type "function"constant"function"constant

For function calling, the type is always `function`.

class BetaToolChoiceMcp:

Use this option to force the model to call a specific tool on a remote MCP server.

String serverLabel

The label of the MCP server to use.

JsonValue; type "mcp"constant"mcp"constant

For MCP tools, the type is always `mcp`.

Optional<String> name

The name of the tool to call on the server.

class BetaToolChoiceCustom:

Use this option to force the model to call a specific custom tool.

String name

The name of the custom tool to call.

JsonValue; type "custom"constant"custom"constant

For custom tool calling, the type is always `custom`.

JsonValue;

JsonValue; type "programmatic\_tool\_calling"constant"programmatic\_tool\_calling"constant

The tool to call. Always `programmatic_tool_calling`.

class BetaToolChoiceApplyPatch:

Forces the model to call the apply\_patch tool when executing a tool call.

JsonValue; type "apply\_patch"constant"apply\_patch"constant

The tool to call. Always `apply_patch`.

class BetaToolChoiceShell:

Forces the model to call the shell tool when a tool call is required.

JsonValue; type "shell"constant"shell"constant

The tool to call. Always `shell`.

List<[BetaTool](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))> tools

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

class BetaFunctionTool:

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

String name

The name of the function to call.

Optional<Parameters> parameters

A JSON schema object describing the parameters of the function.

Optional<Boolean> strict

Whether strict parameter validation is enforced for this function tool.

JsonValue; type "function"constant"function"constant

The type of the function tool. Always `function`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this function is deferred and loaded via tool search.

Optional<String> description

A description of the function. Used by the model to determine whether or not to call the function.

Optional<OutputSchema> outputSchema

A JSON schema object describing the JSON value encoded in string outputs for this function.

class BetaFileSearchTool:

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

JsonValue; type "file\_search"constant"file\_search"constant

The type of the file search tool. Always `file_search`.

List<String> vectorStoreIds

The IDs of the vector stores to search.

Optional<Filters> filters

A filter to apply.

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

String

double

boolean

List<ComparisonFilterValueItem>

String

double

class CompoundFilter:

Combine multiple filters using `and` or `or`.

List<Filter> filters

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

String

double

boolean

List<ComparisonFilterValueItem>

String

double

JsonValue

Type type

Type of operation: `and` or `or`.

AND("and")

OR("or")

Optional<Long> maxNumResults

The maximum number of results to return. This number should be between 1 and 50 inclusive.

Optional<RankingOptions> rankingOptions

Ranking options for search.

Optional<HybridSearch> hybridSearch

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

double embeddingWeight

The weight of the embedding in the reciprocal ranking fusion.

double textWeight

The weight of the text in the reciprocal ranking fusion.

Optional<Ranker> ranker

The ranker to use for the file search.

AUTO("auto")

DEFAULT\_2024\_11\_15("default-2024-11-15")

Optional<Double> scoreThreshold

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class BetaComputerTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

JsonValue; type "computer"constant"computer"constant

The type of the computer tool. Always `computer`.

class BetaComputerUsePreviewTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

long displayHeight

The height of the computer display.

long displayWidth

The width of the computer display.

Environment environment

The type of computer environment to control.

WINDOWS("windows")

MAC("mac")

LINUX("linux")

UBUNTU("ubuntu")

BROWSER("browser")

JsonValue; type "computer\_use\_preview"constant"computer\_use\_preview"constant

The type of the computer use tool. Always `computer_use_preview`.

class BetaWebSearchTool:

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

WEB\_SEARCH("web\_search")

WEB\_SEARCH\_2025\_08\_26("web\_search\_2025\_08\_26")

Optional<Filters> filters

Filters for the search.

Optional<List<String>> allowedDomains

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The approximate location of the user.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

Optional<Type> type

The type of location approximation. Always `approximate`.

Mcp

String serverLabel

A label for this MCP server, used to identify it in tool calls.

JsonValue; type "mcp"constant"mcp"constant

The type of the MCP tool. Always `mcp`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<AllowedTools> allowedTools

List of allowed tool names or a filter object.

List<String>

class McpToolFilter:

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<String> authorization

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

Optional<ConnectorId> connectorId

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

CONNECTOR\_DROPBOX("connector\_dropbox")

CONNECTOR\_GMAIL("connector\_gmail")

CONNECTOR\_GOOGLECALENDAR("connector\_googlecalendar")

CONNECTOR\_GOOGLEDRIVE("connector\_googledrive")

CONNECTOR\_MICROSOFTTEAMS("connector\_microsoftteams")

CONNECTOR\_OUTLOOKCALENDAR("connector\_outlookcalendar")

CONNECTOR\_OUTLOOKEMAIL("connector\_outlookemail")

CONNECTOR\_SHAREPOINT("connector\_sharepoint")

Optional<Boolean> deferLoading

Whether this MCP tool is deferred and discovered via tool search.

Optional<Headers> headers

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

Optional<RequireApproval> requireApproval

Specify which of the MCP server’s tools require approval.

class McpToolApprovalFilter:

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

Optional<Always> always

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<Never> never

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

enum McpToolApprovalSetting:

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

ALWAYS("always")

NEVER("never")

Optional<String> serverDescription

Optional description of the MCP server, used to provide more context.

Optional<String> serverUrl

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

Optional<String> tunnelId

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter

Container container

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

String

class CodeInterpreterToolAuto:

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

JsonValue; type "auto"constant"auto"constant

Always `auto`.

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the code interpreter container.

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

JsonValue; type "code\_interpreter"constant"code\_interpreter"constant

The type of the code interpreter tool. Always `code_interpreter`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

JsonValue;

JsonValue; type "programmatic\_tool\_calling"constant"programmatic\_tool\_calling"constant

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration

JsonValue; type "image\_generation"constant"image\_generation"constant

The type of the image generation tool. Always `image_generation`.

Optional<Action> action

Whether to generate a new image or edit an existing image. Default: `auto`.

GENERATE("generate")

EDIT("edit")

AUTO("auto")

Optional<Background> background

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

TRANSPARENT("transparent")

OPAQUE("opaque")

AUTO("auto")

Optional<InputFidelity> inputFidelity

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

HIGH("high")

LOW("low")

Optional<InputImageMask> inputImageMask

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

Optional<String> fileId

File ID for the mask image.

Optional<String> imageUrl

Base64-encoded mask image.

Optional<Model> model

The image generation model to use. Default: `gpt-image-1`.

GPT\_IMAGE\_1("gpt-image-1")

GPT\_IMAGE\_1\_MINI("gpt-image-1-mini")

GPT\_IMAGE\_2("gpt-image-2")

GPT\_IMAGE\_2\_2026\_04\_21("gpt-image-2-2026-04-21")

GPT\_IMAGE\_1\_5("gpt-image-1.5")

CHATGPT\_IMAGE\_LATEST("chatgpt-image-latest")

Optional<Moderation> moderation

Moderation level for the generated image. Default: `auto`.

AUTO("auto")

LOW("low")

Optional<Long> outputCompression

Compression level for the output image. Default: 100.

minimum0

maximum100

Optional<OutputFormat> outputFormat

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

PNG("png")

WEBP("webp")

JPEG("jpeg")

Optional<Long> partialImages

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

Optional<Quality> quality

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

LOW("low")

MEDIUM("medium")

HIGH("high")

AUTO("auto")

Optional<Size> size

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

\_1024X1024("1024x1024")

\_1024X1536("1024x1536")

\_1536X1024("1536x1024")

AUTO("auto")

JsonValue;

JsonValue; type "local\_shell"constant"local\_shell"constant

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool:

A tool that allows the model to execute shell commands.

JsonValue; type "shell"constant"shell"constant

The type of the shell tool. Always `shell`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Environment> environment

class BetaContainerAuto:

JsonValue; type "container\_auto"constant"container\_auto"constant

Automatically creates a container for this request

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the container.

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

Optional<List<Skill>> skills

An optional list of skills referenced by id or inline data.

class BetaSkillReference:

String skillId

The ID of the referenced skill.

maxLength64

minLength1

JsonValue; type "skill\_reference"constant"skill\_reference"constant

References a skill created with the /v1/skills endpoint.

Optional<String> version

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class BetaInlineSkill:

String description

The description of the skill.

String name

The name of the skill.

[BetaInlineSkillSource](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) source

Inline skill payload

String data

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

JsonValue; mediaType "application/zip"constant"application/zip"constant

The media type of the inline skill payload. Must be `application/zip`.

JsonValue; type "base64"constant"base64"constant

The type of the inline skill source. Must be `base64`.

JsonValue; type "inline"constant"inline"constant

Defines an inline skill for this request.

class BetaLocalEnvironment:

JsonValue; type "local"constant"local"constant

Use a local computer environment.

Optional<List<[BetaLocalSkill](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))>> skills

An optional list of skills.

String description

The description of the skill.

String name

The name of the skill.

String path

The path to the directory containing the skill.

class BetaContainerReference:

String containerId

The ID of the referenced container.

JsonValue; type "container\_reference"constant"container\_reference"constant

References a container created with the /v1/containers endpoint

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<Format> format

The input format for the custom tool. Default is unconstrained text.

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

A grammar defined by the user.

String definition

The grammar definition.

Syntax syntax

The syntax of the grammar definition. One of `lark` or `regex`.

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

Grammar format. Always `grammar`.

class BetaNamespaceTool:

Groups function/custom tools under a shared namespace.

String description

A description of the namespace shown to the model.

minLength1

String name

The namespace name used in tool calls (for example, `crm`).

minLength1

List<Tool> tools

The function/custom tools available inside this namespace.

class Function:

String name

maxLength128

minLength1

JsonValue; type "function"constant"function"constant

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this function should be deferred and discovered via tool search.

Optional<String> description

Optional<OutputSchema> outputSchema

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

Optional<JsonValue> parameters

Optional<Boolean> strict

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<Format> format

The input format for the custom tool. Default is unconstrained text.

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

A grammar defined by the user.

String definition

The grammar definition.

Syntax syntax

The syntax of the grammar definition. One of `lark` or `regex`.

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

Grammar format. Always `grammar`.

JsonValue; type "namespace"constant"namespace"constant

The type of the tool. Always `namespace`.

class BetaToolSearchTool:

Hosted or BYOT tool search configuration for deferred tools.

JsonValue; type "tool\_search"constant"tool\_search"constant

The type of the tool. Always `tool_search`.

Optional<String> description

Description shown to the model for a client-executed tool search tool.

Optional<Execution> execution

Whether tool search is executed by the server or by the client.

SERVER("server")

CLIENT("client")

Optional<JsonValue> parameters

Parameter schema for a client-executed tool search tool.

class BetaWebSearchPreviewTool:

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

WEB\_SEARCH\_PREVIEW("web\_search\_preview")

WEB\_SEARCH\_PREVIEW\_2025\_03\_11("web\_search\_preview\_2025\_03\_11")

Optional<List<SearchContentType>> searchContentTypes

TEXT("text")

IMAGE("image")

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The user’s location.

JsonValue; type "approximate"constant"approximate"constant

The type of location approximation. Always `approximate`.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

class BetaApplyPatchTool:

Allows the assistant to create, delete, or update files using unified diffs.

JsonValue; type "apply\_patch"constant"apply\_patch"constant

The type of the tool. Always `apply_patch`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Double> topP

An alternative to sampling with temperature, called nucleus sampling,
where the model considers the results of the tokens with top\_p probability
mass. So 0.1 means only the tokens comprising the top 10% probability mass
are considered.

We generally recommend altering this or `temperature` but not both.

minimum0

maximum1

Optional<Boolean> background

Whether to run the model response in the background.
[Learn more](https://platform.openai.com/docs/guides/background).

Optional<Double> completedAt

Unix timestamp (in seconds) of when this Response was completed.
Only present when the status is `completed`.

formatunixtime

Optional<Conversation> conversation

The conversation that this response belonged to. Input items and output items from this response were automatically added to this conversation.

String id

The unique ID of the conversation that this response was associated with.

Optional<Long> maxOutputTokens

An upper bound for the number of tokens that can be generated for a response, including visible output tokens and [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

Optional<Long> maxToolCalls

The maximum number of total calls to built-in tools that can be processed in a response. This maximum number applies across all built-in tool calls, not per individual tool. Any further attempts to call a tool by the model will be ignored.

Optional<Moderation> moderation

Moderation results for the response input and output, if moderated completions were requested.

Input input

Moderation for the response input.

class ModerationResult:

A moderation result produced for the response input or output.

Categories categories

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

CategoryAppliedInputTypes categoryAppliedInputTypes

Which modalities of input are reflected by the score for each category.

TEXT("text")

IMAGE("image")

CategoryScores categoryScores

A dictionary of moderation categories to scores.

boolean flagged

A boolean indicating whether the content was flagged by any category.

String model

The moderation model that produced this result.

JsonValue; type "moderation\_result"constant"moderation\_result"constant

The object type, which was always `moderation_result` for successful moderation results.

class Error:

An error produced while attempting moderation for the response input or output.

String code

The error code.

String message

The error message.

JsonValue; type "error"constant"error"constant

The object type, which was always `error` for moderation failures.

Output output

Moderation for the response output.

class ModerationResult:

A moderation result produced for the response input or output.

Categories categories

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

CategoryAppliedInputTypes categoryAppliedInputTypes

Which modalities of input are reflected by the score for each category.

TEXT("text")

IMAGE("image")

CategoryScores categoryScores

A dictionary of moderation categories to scores.

boolean flagged

A boolean indicating whether the content was flagged by any category.

String model

The moderation model that produced this result.

JsonValue; type "moderation\_result"constant"moderation\_result"constant

The object type, which was always `moderation_result` for successful moderation results.

class Error:

An error produced while attempting moderation for the response input or output.

String code

The error code.

String message

The error message.

JsonValue; type "error"constant"error"constant

The object type, which was always `error` for moderation failures.

Optional<String> previousResponseId

The unique ID of the previous response to the model. Use this to
create multi-turn conversations. Learn more about
[conversation state](https://platform.openai.com/docs/guides/conversation-state). Cannot be used in conjunction with `conversation`.

Optional<[BetaResponsePrompt](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_prompt%20%3E%20(schema))> prompt

Reference to a prompt template and its variables.
[Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

String id

The unique identifier of the prompt template to use.

Optional<Variables> variables

Optional map of values to substitute in for variables in your
prompt. The substitution values can either be strings, or other
Response input types like images or files.

String

class BetaResponseInputText:

A text input to the model.

String text

The text input to the model.

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputImage:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail detail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

JsonValue; type "input\_image"constant"input\_image"constant

The type of the input item. Always `input_image`.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> imageUrl

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile:

A file input to the model.

JsonValue; type "input\_file"constant"input\_file"constant

The type of the input item. Always `input_file`.

Optional<Detail> detail

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

AUTO("auto")

LOW("low")

HIGH("high")

Optional<String> fileData

The content of the file to be sent to the model.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> fileUrl

The URL of the file to be sent to the model.

formaturi

Optional<String> filename

The name of the file to be sent to the model.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

Optional<String> version

Optional version of the prompt template.

Optional<String> promptCacheKey

Used by OpenAI to cache responses for similar requests to optimize your cache hit rates. Replaces the `user` field. [Learn more](https://platform.openai.com/docs/guides/prompt-caching).

Optional<PromptCacheOptions> promptCacheOptions

The prompt-caching options that were applied to the response. Supported for `gpt-5.6` and later models.

Mode mode

Whether implicit prompt-cache breakpoints were enabled.

IMPLICIT("implicit")

EXPLICIT("explicit")

Ttl ttl

The minimum lifetime applied to each cache breakpoint.

DeprecatedOptional<PromptCacheRetention> promptCacheRetention

Deprecated. Use `prompt_cache_options.ttl` instead.

The retention policy for the prompt cache. Set to `24h` to enable extended prompt caching, which keeps cached prefixes active for longer, up to a maximum of 24 hours. [Learn more](https://platform.openai.com/docs/guides/prompt-caching#prompt-cache-retention).
This field expresses a maximum retention policy, while
`prompt_cache_options.ttl` expresses a minimum cache lifetime. The two
fields are independent and do not interact.
For `gpt-5.5`, `gpt-5.5-pro`, and future models, only `24h` is supported.

For older models that support both `in_memory` and `24h`, the default depends on your organization’s data retention policy:

* Organizations without ZDR enabled default to `24h`.
* Organizations with ZDR enabled default to `in_memory` when `prompt_cache_retention` is not specified.

IN\_MEMORY("in\_memory")

\_24H("24h")

Optional<Reasoning> reasoning

**gpt-5 and o-series models only**

Configuration options for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).

Optional<Context> context

Controls which reasoning items are rendered back to the model on later turns.
If omitted or set to `auto`, the model determines the context mode. The
`gpt-5.6` model family defaults to `all_turns`; earlier models default to
`current_turn`.

When returned on a response, this is the effective reasoning context mode
used for the response.

AUTO("auto")

CURRENT\_TURN("current\_turn")

ALL\_TURNS("all\_turns")

Optional<Effort> effort

Constrains effort on reasoning for reasoning models. Currently supported
values are `none`, `minimal`, `low`, `medium`, `high`, `xhigh`, and `max`.
Reducing reasoning effort can result in faster responses and fewer tokens
used on reasoning in a response. Not all reasoning models support every
value. See the
[reasoning guide](https://platform.openai.com/docs/guides/reasoning)
for model-specific support.

NONE("none")

MINIMAL("minimal")

LOW("low")

MEDIUM("medium")

HIGH("high")

XHIGH("xhigh")

MAX("max")

DeprecatedOptional<GenerateSummary> generateSummary

**Deprecated:** use `summary` instead.

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

AUTO("auto")

CONCISE("concise")

DETAILED("detailed")

Optional<Mode> mode

Controls the reasoning execution mode for the request.

When returned on a response, this is the effective execution mode.

STANDARD("standard")

PRO("pro")

Optional<Summary> summary

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

`concise` is supported for `computer-use-preview` models and all reasoning models after `gpt-5`.

AUTO("auto")

CONCISE("concise")

DETAILED("detailed")

Optional<String> safetyIdentifier

A stable identifier used to help detect users of your application that may be violating OpenAI’s usage policies.
The IDs should be a string that uniquely identifies each user, with a maximum length of 64 characters. We recommend hashing their username or email address, in order to avoid sending us any identifying information. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

maxLength64

Optional<ServiceTier> serviceTier

Specifies the processing type used for serving the request.

* If set to ‘auto’, then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use ‘default’.
* If set to ‘default’, then the request will be processed with the standard pricing and performance for the selected model.
* If set to ‘[flex](https://platform.openai.com/docs/guides/flex-processing)’ or ‘[priority](https://openai.com/api-priority-processing/)’, then the request will be processed with the corresponding service tier.
* When not set, the default behavior is ‘auto’.

When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.

AUTO("auto")

DEFAULT("default")

FLEX("flex")

SCALE("scale")

PRIORITY("priority")

Optional<[BetaResponseStatus](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_status%20%3E%20(schema))> status

The status of the response generation. One of `completed`, `failed`,
`in_progress`, `cancelled`, `queued`, or `incomplete`.

COMPLETED("completed")

FAILED("failed")

IN\_PROGRESS("in\_progress")

CANCELLED("cancelled")

QUEUED("queued")

INCOMPLETE("incomplete")

Optional<[BetaResponseTextConfig](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_text_config%20%3E%20(schema))> text

Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:

* [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
* [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

Optional<[BetaResponseFormatTextConfig](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_format_text_config%20%3E%20(schema))> format

An object specifying the format that the model must output.

Configuring `{ "type": "json_schema" }` enables Structured Outputs,
which ensures the model will match your supplied JSON schema. Learn more in the
[Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

The default format is `{ "type": "text" }` with no additional options.

**Not recommended for gpt-4o and newer models:**

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

JsonValue;

JsonValue; type "text"constant"text"constant

The type of response format being defined. Always `text`.

class BetaResponseFormatTextJsonSchemaConfig:

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

String name

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

Schema schema

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

JsonValue; type "json\_schema"constant"json\_schema"constant

The type of response format being defined. Always `json_schema`.

Optional<String> description

A description of what the response format is for, used by the model to
determine how to respond in the format.

Optional<Boolean> strict

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

JsonValue;

JsonValue; type "json\_object"constant"json\_object"constant

The type of response format being defined. Always `json_object`.

Optional<Verbosity> verbosity

Constrains the verbosity of the model’s response. Lower values will result in
more concise responses, while higher values will result in more verbose responses.
Currently supported values are `low`, `medium`, and `high`. The default is
`medium`.

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<Long> topLogprobs

An integer between 0 and 20 specifying the maximum number of most likely
tokens to return at each token position, each with an associated log
probability. In some cases, the number of returned tokens may be fewer than
requested.

minimum0

maximum20

Optional<Truncation> truncation

The truncation strategy to use for the model response.

* `auto`: If the input to this Response exceeds
  the model’s context window size, the model will truncate the
  response to fit the context window by dropping items from the beginning of the conversation.
* `disabled` (default): If the input size will exceed the context window
  size for a model, the request will fail with a 400 error.

AUTO("auto")

DISABLED("disabled")

Optional<[BetaResponseUsage](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_usage%20%3E%20(schema))> usage

Represents token usage details including input tokens, output tokens,
a breakdown of output tokens, and the total tokens used.

long inputTokens

The number of input tokens.

InputTokensDetails inputTokensDetails

A detailed breakdown of the input tokens.

long cacheWriteTokens

The number of input tokens that were written to the cache.

long cachedTokens

The number of tokens that were retrieved from the cache.
[More on prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

long outputTokens

The number of output tokens.

OutputTokensDetails outputTokensDetails

A detailed breakdown of the output tokens.

long reasoningTokens

The number of reasoning tokens.

long totalTokens

The total number of tokens used.

DeprecatedOptional<String> user

This field is being replaced by `safety_identifier` and `prompt_cache_key`. Use `prompt_cache_key` instead to maintain caching optimizations.
A stable identifier for your end-users.
Used to boost cache hit rates by better bucketing similar requests and to help OpenAI detect and prevent abuse. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

long sequenceNumber

The sequence number for this event.

JsonValue; type "response.created"constant"response.created"constant

The type of the event. Always `response.created`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseErrorEvent:

Emitted when an error occurs.

Optional<String> code

The error code.

String message

The error message.

Optional<String> param

The error parameter.

long sequenceNumber

The sequence number of this event.

JsonValue; type "error"constant"error"constant

The type of the event. Always `error`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseFileSearchCallCompletedEvent:

Emitted when a file search call is completed (results found).

String itemId

The ID of the output item that the file search call is initiated.

long outputIndex

The index of the output item that the file search call is initiated.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.file\_search\_call.completed"constant"response.file\_search\_call.completed"constant

The type of the event. Always `response.file_search_call.completed`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseFileSearchCallInProgressEvent:

Emitted when a file search call is initiated.

String itemId

The ID of the output item that the file search call is initiated.

long outputIndex

The index of the output item that the file search call is initiated.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.file\_search\_call.in\_progress"constant"response.file\_search\_call.in\_progress"constant

The type of the event. Always `response.file_search_call.in_progress`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseFileSearchCallSearchingEvent:

Emitted when a file search is currently searching.

String itemId

The ID of the output item that the file search call is initiated.

long outputIndex

The index of the output item that the file search call is searching.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.file\_search\_call.searching"constant"response.file\_search\_call.searching"constant

The type of the event. Always `response.file_search_call.searching`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseFunctionCallArgumentsDeltaEvent:

Emitted when there is a partial function-call arguments delta.

String delta

The function-call arguments delta that is added.

String itemId

The ID of the output item that the function-call arguments delta is added to.

long outputIndex

The index of the output item that the function-call arguments delta is added to.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.function\_call\_arguments.delta"constant"response.function\_call\_arguments.delta"constant

The type of the event. Always `response.function_call_arguments.delta`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseFunctionCallArgumentsDoneEvent:

Emitted when function-call arguments are finalized.

String arguments

The function-call arguments.

String itemId

The ID of the item.

String name

The name of the function that was called.

long outputIndex

The index of the output item.

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.function\_call\_arguments.done"constant"response.function\_call\_arguments.done"constant

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseInProgressEvent:

Emitted when the response is in progress.

[BetaResponse](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema)) response

The response that is in progress.

String id

Unique identifier for this Response.

double createdAt

Unix timestamp (in seconds) of when this Response was created.

formatunixtime

Optional<[BetaResponseError](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_error%20%3E%20(schema))> error

An error object returned when the model fails to generate a Response.

Code code

The error code for the response.

SERVER\_ERROR("server\_error")

RATE\_LIMIT\_EXCEEDED("rate\_limit\_exceeded")

INVALID\_PROMPT("invalid\_prompt")

DATA\_RESIDENCY\_MISMATCH("data\_residency\_mismatch")

BIO\_POLICY("bio\_policy")

VECTOR\_STORE\_TIMEOUT("vector\_store\_timeout")

INVALID\_IMAGE("invalid\_image")

INVALID\_IMAGE\_FORMAT("invalid\_image\_format")

INVALID\_BASE64\_IMAGE("invalid\_base64\_image")

INVALID\_IMAGE\_URL("invalid\_image\_url")

IMAGE\_TOO\_LARGE("image\_too\_large")

IMAGE\_TOO\_SMALL("image\_too\_small")

IMAGE\_PARSE\_ERROR("image\_parse\_error")

IMAGE\_CONTENT\_POLICY\_VIOLATION("image\_content\_policy\_violation")

INVALID\_IMAGE\_MODE("invalid\_image\_mode")

IMAGE\_FILE\_TOO\_LARGE("image\_file\_too\_large")

UNSUPPORTED\_IMAGE\_MEDIA\_TYPE("unsupported\_image\_media\_type")

EMPTY\_IMAGE\_FILE("empty\_image\_file")

FAILED\_TO\_DOWNLOAD\_IMAGE("failed\_to\_download\_image")

IMAGE\_FILE\_NOT\_FOUND("image\_file\_not\_found")

String message

A human-readable description of the error.

Optional<IncompleteDetails> incompleteDetails

Details about why the response is incomplete.

Optional<Reason> reason

The reason why the response is incomplete.

MAX\_OUTPUT\_TOKENS("max\_output\_tokens")

CONTENT\_FILTER("content\_filter")

Optional<Instructions> instructions

A system (or developer) message inserted into the model’s context.

When using along with `previous_response_id`, the instructions from a previous
response will not be carried over to the next response. This makes it simple
to swap out system (or developer) messages in new responses.

String

List<[BetaResponseInputItem](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_item%20%3E%20(schema))>

class BetaEasyInputMessage:

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

Content content

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

String

List<[BetaResponseInputContent](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_content%20%3E%20(schema))>

class BetaResponseInputText:

A text input to the model.

String text

The text input to the model.

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputImage:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail detail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

JsonValue; type "input\_image"constant"input\_image"constant

The type of the input item. Always `input_image`.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> imageUrl

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile:

A file input to the model.

JsonValue; type "input\_file"constant"input\_file"constant

The type of the input item. Always `input_file`.

Optional<Detail> detail

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

AUTO("auto")

LOW("low")

HIGH("high")

Optional<String> fileData

The content of the file to be sent to the model.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> fileUrl

The URL of the file to be sent to the model.

formaturi

Optional<String> filename

The name of the file to be sent to the model.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

Role role

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

USER("user")

ASSISTANT("assistant")

SYSTEM("system")

DEVELOPER("developer")

Optional<Phase> phase

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

COMMENTARY("commentary")

FINAL\_ANSWER("final\_answer")

Optional<Type> type

The type of the message input. Always `message`.

Message

List<[BetaResponseInputContent](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_content%20%3E%20(schema))> content

A list of one or many input items to the model, containing different content
types.

class BetaResponseInputText:

A text input to the model.

String text

The text input to the model.

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputImage:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail detail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

JsonValue; type "input\_image"constant"input\_image"constant

The type of the input item. Always `input_image`.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> imageUrl

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile:

A file input to the model.

JsonValue; type "input\_file"constant"input\_file"constant

The type of the input item. Always `input_file`.

Optional<Detail> detail

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

AUTO("auto")

LOW("low")

HIGH("high")

Optional<String> fileData

The content of the file to be sent to the model.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> fileUrl

The URL of the file to be sent to the model.

formaturi

Optional<String> filename

The name of the file to be sent to the model.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

Role role

The role of the message input. One of `user`, `system`, or `developer`.

USER("user")

SYSTEM("system")

DEVELOPER("developer")

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Status> status

The status of item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

Optional<Type> type

The type of the message input. Always set to `message`.

class BetaResponseOutputMessage:

An output message from the model.

String id

The unique ID of the output message.

List<Content> content

The content of the output message.

class BetaResponseOutputText:

A text output from the model.

List<Annotation> annotations

The annotations of the text output.

class FileCitation:

A citation to a file.

String fileId

The ID of the file.

String filename

The filename of the file cited.

long index

The index of the file in the list of files.

JsonValue; type "file\_citation"constant"file\_citation"constant

The type of the file citation. Always `file_citation`.

class UrlCitation:

A citation for a web resource used to generate a model response.

long endIndex

The index of the last character of the URL citation in the message.

long startIndex

The index of the first character of the URL citation in the message.

String title

The title of the web resource.

JsonValue; type "url\_citation"constant"url\_citation"constant

The type of the URL citation. Always `url_citation`.

String url

The URL of the web resource.

formaturi

class ContainerFileCitation:

A citation for a container file used to generate a model response.

String containerId

The ID of the container file.

long endIndex

The index of the last character of the container file citation in the message.

String fileId

The ID of the file.

String filename

The filename of the container file cited.

long startIndex

The index of the first character of the container file citation in the message.

JsonValue; type "container\_file\_citation"constant"container\_file\_citation"constant

The type of the container file citation. Always `container_file_citation`.

class FilePath:

A path to a file.

String fileId

The ID of the file.

long index

The index of the file in the list of files.

JsonValue; type "file\_path"constant"file\_path"constant

The type of the file path. Always `file_path`.

String text

The text output from the model.

JsonValue; type "output\_text"constant"output\_text"constant

The type of the output text. Always `output_text`.

Optional<List<Logprob>> logprobs

String token

List<long> bytes

double logprob

List<TopLogprob> topLogprobs

String token

List<long> bytes

double logprob

class BetaResponseOutputRefusal:

A refusal from the model.

String refusal

The refusal explanation from the model.

JsonValue; type "refusal"constant"refusal"constant

The type of the refusal. Always `refusal`.

JsonValue; role "assistant"constant"assistant"constant

The role of the output message. Always `assistant`.

Status status

The status of the message input. One of `in_progress`, `completed`, or
`incomplete`. Populated when input items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "message"constant"message"constant

The type of the output message. Always `message`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Phase> phase

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

COMMENTARY("commentary")

FINAL\_ANSWER("final\_answer")

class BetaResponseFileSearchToolCall:

The results of a file search tool call. See the
[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

String id

The unique ID of the file search tool call.

List<String> queries

The queries used to search for files.

Status status

The status of the file search tool call. One of `in_progress`,
`searching`, `incomplete` or `failed`,

IN\_PROGRESS("in\_progress")

SEARCHING("searching")

COMPLETED("completed")

INCOMPLETE("incomplete")

FAILED("failed")

JsonValue; type "file\_search\_call"constant"file\_search\_call"constant

The type of the file search tool call. Always `file_search_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<List<Result>> results

The results of the file search tool call.

Optional<Attributes> attributes

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

String

double

boolean

Optional<String> fileId

The unique ID of the file.

Optional<String> filename

The name of the file.

Optional<Double> score

The relevance score of the file - a value between 0 and 1.

formatfloat

Optional<String> text

The text that was retrieved from the file.

class BetaResponseComputerToolCall:

A tool call to a computer use tool. See the
[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

String id

The unique ID of the computer call.

String callId

An identifier used when responding to the tool call with output.

List<PendingSafetyCheck> pendingSafetyChecks

The pending safety checks for the computer call.

String id

The ID of the pending safety check.

Optional<String> code

The type of the pending safety check.

Optional<String> message

Details about the pending safety check.

Status status

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

Type type

The type of the computer call. Always `computer_call`.

Optional<[BetaComputerAction](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action%20%3E%20(schema))> action

A click action.

Click

Button button

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

LEFT("left")

RIGHT("right")

WHEEL("wheel")

BACK("back")

FORWARD("forward")

JsonValue; type "click"constant"click"constant

Specifies the event type. For a click action, this property is always `click`.

long x

The x-coordinate where the click occurred.

long y

The y-coordinate where the click occurred.

Optional<List<String>> keys

The keys being held while clicking.

DoubleClick

Optional<List<String>> keys

The keys being held while double-clicking.

JsonValue; type "double\_click"constant"double\_click"constant

Specifies the event type. For a double click action, this property is always set to `double_click`.

long x

The x-coordinate where the double click occurred.

long y

The y-coordinate where the double click occurred.

Drag

List<Path> path

An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

[
  { x: 100, y: 200 },
  { x: 200, y: 300 }
]

long x

The x-coordinate.

long y

The y-coordinate.

JsonValue; type "drag"constant"drag"constant

Specifies the event type. For a drag action, this property is always set to `drag`.

Optional<List<String>> keys

The keys being held while dragging the mouse.

Keypress

List<String> keys

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

JsonValue; type "keypress"constant"keypress"constant

Specifies the event type. For a keypress action, this property is always set to `keypress`.

Move

JsonValue; type "move"constant"move"constant

Specifies the event type. For a move action, this property is always set to `move`.

long x

The x-coordinate to move to.

long y

The y-coordinate to move to.

Optional<List<String>> keys

The keys being held while moving the mouse.

JsonValue;

JsonValue; type "screenshot"constant"screenshot"constant

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

Scroll

long scrollX

The horizontal scroll distance.

long scrollY

The vertical scroll distance.

JsonValue; type "scroll"constant"scroll"constant

Specifies the event type. For a scroll action, this property is always set to `scroll`.

long x

The x-coordinate where the scroll occurred.

long y

The y-coordinate where the scroll occurred.

Optional<List<String>> keys

The keys being held while scrolling.

Type

String text

The text to type.

JsonValue; type "type"constant"type"constant

Specifies the event type. For a type action, this property is always set to `type`.

JsonValue;

JsonValue; type "wait"constant"wait"constant

Specifies the event type. For a wait action, this property is always set to `wait`.

Optional<List<[BetaComputerAction](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action%20%3E%20(schema))>> actions

Flattened batched actions for `computer_use`. Each action includes an
`type` discriminator and action-specific fields.

Click

Button button

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

LEFT("left")

RIGHT("right")

WHEEL("wheel")

BACK("back")

FORWARD("forward")

JsonValue; type "click"constant"click"constant

Specifies the event type. For a click action, this property is always `click`.

long x

The x-coordinate where the click occurred.

long y

The y-coordinate where the click occurred.

Optional<List<String>> keys

The keys being held while clicking.

DoubleClick

Optional<List<String>> keys

The keys being held while double-clicking.

JsonValue; type "double\_click"constant"double\_click"constant

Specifies the event type. For a double click action, this property is always set to `double_click`.

long x

The x-coordinate where the double click occurred.

long y

The y-coordinate where the double click occurred.

Drag

List<Path> path

An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

[
  { x: 100, y: 200 },
  { x: 200, y: 300 }
]

long x

The x-coordinate.

long y

The y-coordinate.

JsonValue; type "drag"constant"drag"constant

Specifies the event type. For a drag action, this property is always set to `drag`.

Optional<List<String>> keys

The keys being held while dragging the mouse.

Keypress

List<String> keys

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

JsonValue; type "keypress"constant"keypress"constant

Specifies the event type. For a keypress action, this property is always set to `keypress`.

Move

JsonValue; type "move"constant"move"constant

Specifies the event type. For a move action, this property is always set to `move`.

long x

The x-coordinate to move to.

long y

The y-coordinate to move to.

Optional<List<String>> keys

The keys being held while moving the mouse.

JsonValue;

JsonValue; type "screenshot"constant"screenshot"constant

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

Scroll

long scrollX

The horizontal scroll distance.

long scrollY

The vertical scroll distance.

JsonValue; type "scroll"constant"scroll"constant

Specifies the event type. For a scroll action, this property is always set to `scroll`.

long x

The x-coordinate where the scroll occurred.

long y

The y-coordinate where the scroll occurred.

Optional<List<String>> keys

The keys being held while scrolling.

Type

String text

The text to type.

JsonValue; type "type"constant"type"constant

Specifies the event type. For a type action, this property is always set to `type`.

JsonValue;

JsonValue; type "wait"constant"wait"constant

Specifies the event type. For a wait action, this property is always set to `wait`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

ComputerCallOutput

String callId

The ID of the computer tool call that produced the output.

maxLength64

minLength1

[BetaResponseComputerToolCallOutputScreenshot](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema)) output

A computer screenshot image used with the computer use tool.

JsonValue; type "computer\_screenshot"constant"computer\_screenshot"constant

Specifies the event type. For a computer screenshot, this property is
always set to `computer_screenshot`.

Optional<String> fileId

The identifier of an uploaded file that contains the screenshot.

Optional<String> imageUrl

The URL of the screenshot image.

formaturi

JsonValue; type "computer\_call\_output"constant"computer\_call\_output"constant

The type of the computer tool call output. Always `computer_call_output`.

Optional<String> id

The ID of the computer tool call output.

Optional<List<AcknowledgedSafetyCheck>> acknowledgedSafetyChecks

The safety checks reported by the API that have been acknowledged by the developer.

String id

The ID of the pending safety check.

Optional<String> code

The type of the pending safety check.

Optional<String> message

Details about the pending safety check.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Status> status

The status of the message input. One of `in_progress`, `completed`, or `incomplete`. Populated when input items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

class BetaResponseFunctionWebSearch:

The results of a web search tool call. See the
[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

String id

The unique ID of the web search tool call.

Action action

An object describing the specific action taken in this web search call.
Includes details on how the model used the web (search, open\_page, find\_in\_page).

class Search:

Action type “search” - Performs a web search query.

JsonValue; type "search"constant"search"constant

The action type.

Optional<List<String>> queries

The search queries.

DeprecatedOptional<String> query

The search query.

Optional<List<Source>> sources

The sources used in the search.

JsonValue; type "url"constant"url"constant

The type of source. Always `url`.

String url

The URL of the source.

formaturi

class OpenPage:

Action type “open\_page” - Opens a specific URL from search results.

JsonValue; type "open\_page"constant"open\_page"constant

The action type.

Optional<String> url

The URL opened by the model.

formaturi

class FindInPage:

Action type “find\_in\_page”: Searches for a pattern within a loaded page.

String pattern

The pattern or text to search for within the page.

JsonValue; type "find\_in\_page"constant"find\_in\_page"constant

The action type.

String url

The URL of the page searched for the pattern.

formaturi

Status status

The status of the web search tool call.

IN\_PROGRESS("in\_progress")

SEARCHING("searching")

COMPLETED("completed")

FAILED("failed")

JsonValue; type "web\_search\_call"constant"web\_search\_call"constant

The type of the web search tool call. Always `web_search_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseFunctionToolCall:

A tool call to run a function. See the
[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

String arguments

A JSON string of the arguments to pass to the function.

String callId

The unique ID of the function tool call generated by the model.

String name

The name of the function to run.

JsonValue; type "function\_call"constant"function\_call"constant

The type of the function tool call. Always `function_call`.

Optional<String> id

The unique ID of the function tool call.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

class Program:

String callerId

The call ID of the program item that produced this tool call.

JsonValue; type "program"constant"program"constant

Optional<String> namespace

The namespace of the function to run.

Optional<Status> status

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

FunctionCallOutput

String callId

The unique ID of the function tool call generated by the model.

maxLength64

minLength1

Output output

Text, image, or file output of the function tool call.

String

List<[BetaResponseFunctionCallOutputItem](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item%20%3E%20(schema))>

class BetaResponseInputTextContent:

A text input to the model.

String text

The text input to the model.

maxLength10485760

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputImageContent:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

JsonValue; type "input\_image"constant"input\_image"constant

The type of the input item. Always `input_image`.

Optional<Detail> detail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> imageUrl

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

maxLength20971520

formaturi

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputFileContent:

A file input to the model.

JsonValue; type "input\_file"constant"input\_file"constant

The type of the input item. Always `input_file`.

Optional<Detail> detail

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

AUTO("auto")

LOW("low")

HIGH("high")

Optional<String> fileData

The base64-encoded data of the file to be sent to the model.

maxLength73400320

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> fileUrl

The URL of the file to be sent to the model.

formaturi

Optional<String> filename

The name of the file to be sent to the model.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

JsonValue; type "function\_call\_output"constant"function\_call\_output"constant

The type of the function tool call output. Always `function_call_output`.

Optional<String> id

The unique ID of the function tool call output. Populated when this item is returned via API.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

The caller type. Always `direct`.

class Program:

String callerId

The call ID of the program item that produced this tool call.

maxLength64

minLength1

JsonValue; type "program"constant"program"constant

The caller type. Always `program`.

Optional<Status> status

The status of the item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

AgentMessage

String author

The sending agent identity.

List<Content> content

Plaintext, image, or encrypted content sent between agents.

class BetaResponseInputTextContent:

A text input to the model.

String text

The text input to the model.

maxLength10485760

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputImageContent:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

JsonValue; type "input\_image"constant"input\_image"constant

The type of the input item. Always `input_image`.

Optional<Detail> detail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> imageUrl

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

maxLength20971520

formaturi

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class EncryptedContent:

Opaque encrypted content that Responses API decrypts inside trusted model execution.

String encryptedContent

Opaque encrypted content.

maxLength10485760

JsonValue; type "encrypted\_content"constant"encrypted\_content"constant

The type of the input item. Always `encrypted_content`.

String recipient

The destination agent identity.

JsonValue; type "agent\_message"constant"agent\_message"constant

The item type. Always `agent_message`.

Optional<String> id

The unique ID of this agent message item.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

MultiAgentCall

Action action

The multi-agent action that was executed.

SPAWN\_AGENT("spawn\_agent")

INTERRUPT\_AGENT("interrupt\_agent")

LIST\_AGENTS("list\_agents")

SEND\_MESSAGE("send\_message")

FOLLOWUP\_TASK("followup\_task")

WAIT\_AGENT("wait\_agent")

String arguments

The action arguments as a JSON string.

String callId

The unique ID linking this call to its output.

maxLength64

minLength1

JsonValue; type "multi\_agent\_call"constant"multi\_agent\_call"constant

The item type. Always `multi_agent_call`.

Optional<String> id

The unique ID of this multi-agent call.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

MultiAgentCallOutput

Action action

The multi-agent action that produced this result.

SPAWN\_AGENT("spawn\_agent")

INTERRUPT\_AGENT("interrupt\_agent")

LIST\_AGENTS("list\_agents")

SEND\_MESSAGE("send\_message")

FOLLOWUP\_TASK("followup\_task")

WAIT\_AGENT("wait\_agent")

String callId

The unique ID of the multi-agent call.

maxLength64

minLength1

List<Output> output

Text output returned by the multi-agent action.

String text

The text content.

maxLength10485760

JsonValue; type "output\_text"constant"output\_text"constant

The content type. Always `output_text`.

Optional<List<Annotation>> annotations

Citations associated with the text content.

class FileCitation:

String fileId

The ID of the file.

String filename

The filename of the file cited.

long index

The index of the file in the list of files.

minimum0

JsonValue; type "file\_citation"constant"file\_citation"constant

The citation type. Always `file_citation`.

class UrlCitation:

long endIndex

The index of the last character of the citation in the message.

minimum0

long startIndex

The index of the first character of the citation in the message.

minimum0

String title

The title of the cited resource.

JsonValue; type "url\_citation"constant"url\_citation"constant

The citation type. Always `url_citation`.

String url

The URL of the cited resource.

formaturi

class ContainerFileCitation:

String containerId

The ID of the container.

long endIndex

The index of the last character of the citation in the message.

minimum0

String fileId

The ID of the container file.

String filename

The filename of the container file cited.

long startIndex

The index of the first character of the citation in the message.

minimum0

JsonValue; type "container\_file\_citation"constant"container\_file\_citation"constant

The citation type. Always `container_file_citation`.

JsonValue; type "multi\_agent\_call\_output"constant"multi\_agent\_call\_output"constant

The item type. Always `multi_agent_call_output`.

Optional<String> id

The unique ID of this multi-agent call output.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

ToolSearchCall

JsonValue arguments

The arguments supplied to the tool search call.

JsonValue; type "tool\_search\_call"constant"tool\_search\_call"constant

The item type. Always `tool_search_call`.

Optional<String> id

The unique ID of this tool search call.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<String> callId

The unique ID of the tool search call generated by the model.

maxLength64

minLength1

Optional<Execution> execution

Whether tool search was executed by the server or by the client.

SERVER("server")

CLIENT("client")

Optional<Status> status

The status of the tool search call.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

class BetaResponseToolSearchOutputItemParam:

List<[BetaTool](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))> tools

The loaded tool definitions returned by the tool search output.

class BetaFunctionTool:

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

String name

The name of the function to call.

Optional<Parameters> parameters

A JSON schema object describing the parameters of the function.

Optional<Boolean> strict

Whether strict parameter validation is enforced for this function tool.

JsonValue; type "function"constant"function"constant

The type of the function tool. Always `function`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this function is deferred and loaded via tool search.

Optional<String> description

A description of the function. Used by the model to determine whether or not to call the function.

Optional<OutputSchema> outputSchema

A JSON schema object describing the JSON value encoded in string outputs for this function.

class BetaFileSearchTool:

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

JsonValue; type "file\_search"constant"file\_search"constant

The type of the file search tool. Always `file_search`.

List<String> vectorStoreIds

The IDs of the vector stores to search.

Optional<Filters> filters

A filter to apply.

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

String

double

boolean

List<ComparisonFilterValueItem>

String

double

class CompoundFilter:

Combine multiple filters using `and` or `or`.

List<Filter> filters

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

String

double

boolean

List<ComparisonFilterValueItem>

String

double

JsonValue

Type type

Type of operation: `and` or `or`.

AND("and")

OR("or")

Optional<Long> maxNumResults

The maximum number of results to return. This number should be between 1 and 50 inclusive.

Optional<RankingOptions> rankingOptions

Ranking options for search.

Optional<HybridSearch> hybridSearch

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

double embeddingWeight

The weight of the embedding in the reciprocal ranking fusion.

double textWeight

The weight of the text in the reciprocal ranking fusion.

Optional<Ranker> ranker

The ranker to use for the file search.

AUTO("auto")

DEFAULT\_2024\_11\_15("default-2024-11-15")

Optional<Double> scoreThreshold

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class BetaComputerTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

JsonValue; type "computer"constant"computer"constant

The type of the computer tool. Always `computer`.

class BetaComputerUsePreviewTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

long displayHeight

The height of the computer display.

long displayWidth

The width of the computer display.

Environment environment

The type of computer environment to control.

WINDOWS("windows")

MAC("mac")

LINUX("linux")

UBUNTU("ubuntu")

BROWSER("browser")

JsonValue; type "computer\_use\_preview"constant"computer\_use\_preview"constant

The type of the computer use tool. Always `computer_use_preview`.

class BetaWebSearchTool:

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

WEB\_SEARCH("web\_search")

WEB\_SEARCH\_2025\_08\_26("web\_search\_2025\_08\_26")

Optional<Filters> filters

Filters for the search.

Optional<List<String>> allowedDomains

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The approximate location of the user.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

Optional<Type> type

The type of location approximation. Always `approximate`.

Mcp

String serverLabel

A label for this MCP server, used to identify it in tool calls.

JsonValue; type "mcp"constant"mcp"constant

The type of the MCP tool. Always `mcp`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<AllowedTools> allowedTools

List of allowed tool names or a filter object.

List<String>

class McpToolFilter:

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<String> authorization

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

Optional<ConnectorId> connectorId

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

CONNECTOR\_DROPBOX("connector\_dropbox")

CONNECTOR\_GMAIL("connector\_gmail")

CONNECTOR\_GOOGLECALENDAR("connector\_googlecalendar")

CONNECTOR\_GOOGLEDRIVE("connector\_googledrive")

CONNECTOR\_MICROSOFTTEAMS("connector\_microsoftteams")

CONNECTOR\_OUTLOOKCALENDAR("connector\_outlookcalendar")

CONNECTOR\_OUTLOOKEMAIL("connector\_outlookemail")

CONNECTOR\_SHAREPOINT("connector\_sharepoint")

Optional<Boolean> deferLoading

Whether this MCP tool is deferred and discovered via tool search.

Optional<Headers> headers

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

Optional<RequireApproval> requireApproval

Specify which of the MCP server’s tools require approval.

class McpToolApprovalFilter:

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

Optional<Always> always

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<Never> never

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

enum McpToolApprovalSetting:

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

ALWAYS("always")

NEVER("never")

Optional<String> serverDescription

Optional description of the MCP server, used to provide more context.

Optional<String> serverUrl

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

Optional<String> tunnelId

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter

Container container

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

String

class CodeInterpreterToolAuto:

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

JsonValue; type "auto"constant"auto"constant

Always `auto`.

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the code interpreter container.

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

JsonValue; type "code\_interpreter"constant"code\_interpreter"constant

The type of the code interpreter tool. Always `code_interpreter`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

JsonValue;

JsonValue; type "programmatic\_tool\_calling"constant"programmatic\_tool\_calling"constant

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration

JsonValue; type "image\_generation"constant"image\_generation"constant

The type of the image generation tool. Always `image_generation`.

Optional<Action> action

Whether to generate a new image or edit an existing image. Default: `auto`.

GENERATE("generate")

EDIT("edit")

AUTO("auto")

Optional<Background> background

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

TRANSPARENT("transparent")

OPAQUE("opaque")

AUTO("auto")

Optional<InputFidelity> inputFidelity

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

HIGH("high")

LOW("low")

Optional<InputImageMask> inputImageMask

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

Optional<String> fileId

File ID for the mask image.

Optional<String> imageUrl

Base64-encoded mask image.

Optional<Model> model

The image generation model to use. Default: `gpt-image-1`.

GPT\_IMAGE\_1("gpt-image-1")

GPT\_IMAGE\_1\_MINI("gpt-image-1-mini")

GPT\_IMAGE\_2("gpt-image-2")

GPT\_IMAGE\_2\_2026\_04\_21("gpt-image-2-2026-04-21")

GPT\_IMAGE\_1\_5("gpt-image-1.5")

CHATGPT\_IMAGE\_LATEST("chatgpt-image-latest")

Optional<Moderation> moderation

Moderation level for the generated image. Default: `auto`.

AUTO("auto")

LOW("low")

Optional<Long> outputCompression

Compression level for the output image. Default: 100.

minimum0

maximum100

Optional<OutputFormat> outputFormat

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

PNG("png")

WEBP("webp")

JPEG("jpeg")

Optional<Long> partialImages

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

Optional<Quality> quality

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

LOW("low")

MEDIUM("medium")

HIGH("high")

AUTO("auto")

Optional<Size> size

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

\_1024X1024("1024x1024")

\_1024X1536("1024x1536")

\_1536X1024("1536x1024")

AUTO("auto")

JsonValue;

JsonValue; type "local\_shell"constant"local\_shell"constant

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool:

A tool that allows the model to execute shell commands.

JsonValue; type "shell"constant"shell"constant

The type of the shell tool. Always `shell`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Environment> environment

class BetaContainerAuto:

JsonValue; type "container\_auto"constant"container\_auto"constant

Automatically creates a container for this request

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the container.

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

Optional<List<Skill>> skills

An optional list of skills referenced by id or inline data.

class BetaSkillReference:

String skillId

The ID of the referenced skill.

maxLength64

minLength1

JsonValue; type "skill\_reference"constant"skill\_reference"constant

References a skill created with the /v1/skills endpoint.

Optional<String> version

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class BetaInlineSkill:

String description

The description of the skill.

String name

The name of the skill.

[BetaInlineSkillSource](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) source

Inline skill payload

String data

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

JsonValue; mediaType "application/zip"constant"application/zip"constant

The media type of the inline skill payload. Must be `application/zip`.

JsonValue; type "base64"constant"base64"constant

The type of the inline skill source. Must be `base64`.

JsonValue; type "inline"constant"inline"constant

Defines an inline skill for this request.

class BetaLocalEnvironment:

JsonValue; type "local"constant"local"constant

Use a local computer environment.

Optional<List<[BetaLocalSkill](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))>> skills

An optional list of skills.

String description

The description of the skill.

String name

The name of the skill.

String path

The path to the directory containing the skill.

class BetaContainerReference:

String containerId

The ID of the referenced container.

JsonValue; type "container\_reference"constant"container\_reference"constant

References a container created with the /v1/containers endpoint

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<Format> format

The input format for the custom tool. Default is unconstrained text.

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

A grammar defined by the user.

String definition

The grammar definition.

Syntax syntax

The syntax of the grammar definition. One of `lark` or `regex`.

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

Grammar format. Always `grammar`.

class BetaNamespaceTool:

Groups function/custom tools under a shared namespace.

String description

A description of the namespace shown to the model.

minLength1

String name

The namespace name used in tool calls (for example, `crm`).

minLength1

List<Tool> tools

The function/custom tools available inside this namespace.

class Function:

String name

maxLength128

minLength1

JsonValue; type "function"constant"function"constant

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this function should be deferred and discovered via tool search.

Optional<String> description

Optional<OutputSchema> outputSchema

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

Optional<JsonValue> parameters

Optional<Boolean> strict

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<Format> format

The input format for the custom tool. Default is unconstrained text.

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

A grammar defined by the user.

String definition

The grammar definition.

Syntax syntax

The syntax of the grammar definition. One of `lark` or `regex`.

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

Grammar format. Always `grammar`.

JsonValue; type "namespace"constant"namespace"constant

The type of the tool. Always `namespace`.

class BetaToolSearchTool:

Hosted or BYOT tool search configuration for deferred tools.

JsonValue; type "tool\_search"constant"tool\_search"constant

The type of the tool. Always `tool_search`.

Optional<String> description

Description shown to the model for a client-executed tool search tool.

Optional<Execution> execution

Whether tool search is executed by the server or by the client.

SERVER("server")

CLIENT("client")

Optional<JsonValue> parameters

Parameter schema for a client-executed tool search tool.

class BetaWebSearchPreviewTool:

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

WEB\_SEARCH\_PREVIEW("web\_search\_preview")

WEB\_SEARCH\_PREVIEW\_2025\_03\_11("web\_search\_preview\_2025\_03\_11")

Optional<List<SearchContentType>> searchContentTypes

TEXT("text")

IMAGE("image")

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The user’s location.

JsonValue; type "approximate"constant"approximate"constant

The type of location approximation. Always `approximate`.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

class BetaApplyPatchTool:

Allows the assistant to create, delete, or update files using unified diffs.

JsonValue; type "apply\_patch"constant"apply\_patch"constant

The type of the tool. Always `apply_patch`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

JsonValue; type "tool\_search\_output"constant"tool\_search\_output"constant

The item type. Always `tool_search_output`.

Optional<String> id

The unique ID of this tool search output.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<String> callId

The unique ID of the tool search call generated by the model.

maxLength64

minLength1

Optional<Execution> execution

Whether tool search was executed by the server or by the client.

SERVER("server")

CLIENT("client")

Optional<Status> status

The status of the tool search output.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

AdditionalTools

JsonValue; role "developer"constant"developer"constant

The role that provided the additional tools. Only `developer` is supported.

List<[BetaTool](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))> tools

A list of additional tools made available at this item.

class BetaFunctionTool:

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

String name

The name of the function to call.

Optional<Parameters> parameters

A JSON schema object describing the parameters of the function.

Optional<Boolean> strict

Whether strict parameter validation is enforced for this function tool.

JsonValue; type "function"constant"function"constant

The type of the function tool. Always `function`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this function is deferred and loaded via tool search.

Optional<String> description

A description of the function. Used by the model to determine whether or not to call the function.

Optional<OutputSchema> outputSchema

A JSON schema object describing the JSON value encoded in string outputs for this function.

class BetaFileSearchTool:

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

JsonValue; type "file\_search"constant"file\_search"constant

The type of the file search tool. Always `file_search`.

List<String> vectorStoreIds

The IDs of the vector stores to search.

Optional<Filters> filters

A filter to apply.

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

String

double

boolean

List<ComparisonFilterValueItem>

String

double

class CompoundFilter:

Combine multiple filters using `and` or `or`.

List<Filter> filters

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

String

double

boolean

List<ComparisonFilterValueItem>

String

double

JsonValue

Type type

Type of operation: `and` or `or`.

AND("and")

OR("or")

Optional<Long> maxNumResults

The maximum number of results to return. This number should be between 1 and 50 inclusive.

Optional<RankingOptions> rankingOptions

Ranking options for search.

Optional<HybridSearch> hybridSearch

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

double embeddingWeight

The weight of the embedding in the reciprocal ranking fusion.

double textWeight

The weight of the text in the reciprocal ranking fusion.

Optional<Ranker> ranker

The ranker to use for the file search.

AUTO("auto")

DEFAULT\_2024\_11\_15("default-2024-11-15")

Optional<Double> scoreThreshold

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class BetaComputerTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

JsonValue; type "computer"constant"computer"constant

The type of the computer tool. Always `computer`.

class BetaComputerUsePreviewTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

long displayHeight

The height of the computer display.

long displayWidth

The width of the computer display.

Environment environment

The type of computer environment to control.

WINDOWS("windows")

MAC("mac")

LINUX("linux")

UBUNTU("ubuntu")

BROWSER("browser")

JsonValue; type "computer\_use\_preview"constant"computer\_use\_preview"constant

The type of the computer use tool. Always `computer_use_preview`.

class BetaWebSearchTool:

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

WEB\_SEARCH("web\_search")

WEB\_SEARCH\_2025\_08\_26("web\_search\_2025\_08\_26")

Optional<Filters> filters

Filters for the search.

Optional<List<String>> allowedDomains

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The approximate location of the user.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

Optional<Type> type

The type of location approximation. Always `approximate`.

Mcp

String serverLabel

A label for this MCP server, used to identify it in tool calls.

JsonValue; type "mcp"constant"mcp"constant

The type of the MCP tool. Always `mcp`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<AllowedTools> allowedTools

List of allowed tool names or a filter object.

List<String>

class McpToolFilter:

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<String> authorization

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

Optional<ConnectorId> connectorId

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

CONNECTOR\_DROPBOX("connector\_dropbox")

CONNECTOR\_GMAIL("connector\_gmail")

CONNECTOR\_GOOGLECALENDAR("connector\_googlecalendar")

CONNECTOR\_GOOGLEDRIVE("connector\_googledrive")

CONNECTOR\_MICROSOFTTEAMS("connector\_microsoftteams")

CONNECTOR\_OUTLOOKCALENDAR("connector\_outlookcalendar")

CONNECTOR\_OUTLOOKEMAIL("connector\_outlookemail")

CONNECTOR\_SHAREPOINT("connector\_sharepoint")

Optional<Boolean> deferLoading

Whether this MCP tool is deferred and discovered via tool search.

Optional<Headers> headers

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

Optional<RequireApproval> requireApproval

Specify which of the MCP server’s tools require approval.

class McpToolApprovalFilter:

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

Optional<Always> always

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<Never> never

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

enum McpToolApprovalSetting:

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

ALWAYS("always")

NEVER("never")

Optional<String> serverDescription

Optional description of the MCP server, used to provide more context.

Optional<String> serverUrl

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

Optional<String> tunnelId

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter

Container container

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

String

class CodeInterpreterToolAuto:

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

JsonValue; type "auto"constant"auto"constant

Always `auto`.

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the code interpreter container.

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

JsonValue; type "code\_interpreter"constant"code\_interpreter"constant

The type of the code interpreter tool. Always `code_interpreter`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

JsonValue;

JsonValue; type "programmatic\_tool\_calling"constant"programmatic\_tool\_calling"constant

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration

JsonValue; type "image\_generation"constant"image\_generation"constant

The type of the image generation tool. Always `image_generation`.

Optional<Action> action

Whether to generate a new image or edit an existing image. Default: `auto`.

GENERATE("generate")

EDIT("edit")

AUTO("auto")

Optional<Background> background

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

TRANSPARENT("transparent")

OPAQUE("opaque")

AUTO("auto")

Optional<InputFidelity> inputFidelity

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

HIGH("high")

LOW("low")

Optional<InputImageMask> inputImageMask

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

Optional<String> fileId

File ID for the mask image.

Optional<String> imageUrl

Base64-encoded mask image.

Optional<Model> model

The image generation model to use. Default: `gpt-image-1`.

GPT\_IMAGE\_1("gpt-image-1")

GPT\_IMAGE\_1\_MINI("gpt-image-1-mini")

GPT\_IMAGE\_2("gpt-image-2")

GPT\_IMAGE\_2\_2026\_04\_21("gpt-image-2-2026-04-21")

GPT\_IMAGE\_1\_5("gpt-image-1.5")

CHATGPT\_IMAGE\_LATEST("chatgpt-image-latest")

Optional<Moderation> moderation

Moderation level for the generated image. Default: `auto`.

AUTO("auto")

LOW("low")

Optional<Long> outputCompression

Compression level for the output image. Default: 100.

minimum0

maximum100

Optional<OutputFormat> outputFormat

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

PNG("png")

WEBP("webp")

JPEG("jpeg")

Optional<Long> partialImages

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

Optional<Quality> quality

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

LOW("low")

MEDIUM("medium")

HIGH("high")

AUTO("auto")

Optional<Size> size

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

\_1024X1024("1024x1024")

\_1024X1536("1024x1536")

\_1536X1024("1536x1024")

AUTO("auto")

JsonValue;

JsonValue; type "local\_shell"constant"local\_shell"constant

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool:

A tool that allows the model to execute shell commands.

JsonValue; type "shell"constant"shell"constant

The type of the shell tool. Always `shell`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Environment> environment

class BetaContainerAuto:

JsonValue; type "container\_auto"constant"container\_auto"constant

Automatically creates a container for this request

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the container.

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

Optional<List<Skill>> skills

An optional list of skills referenced by id or inline data.

class BetaSkillReference:

String skillId

The ID of the referenced skill.

maxLength64

minLength1

JsonValue; type "skill\_reference"constant"skill\_reference"constant

References a skill created with the /v1/skills endpoint.

Optional<String> version

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class BetaInlineSkill:

String description

The description of the skill.

String name

The name of the skill.

[BetaInlineSkillSource](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) source

Inline skill payload

String data

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

JsonValue; mediaType "application/zip"constant"application/zip"constant

The media type of the inline skill payload. Must be `application/zip`.

JsonValue; type "base64"constant"base64"constant

The type of the inline skill source. Must be `base64`.

JsonValue; type "inline"constant"inline"constant

Defines an inline skill for this request.

class BetaLocalEnvironment:

JsonValue; type "local"constant"local"constant

Use a local computer environment.

Optional<List<[BetaLocalSkill](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))>> skills

An optional list of skills.

String description

The description of the skill.

String name

The name of the skill.

String path

The path to the directory containing the skill.

class BetaContainerReference:

String containerId

The ID of the referenced container.

JsonValue; type "container\_reference"constant"container\_reference"constant

References a container created with the /v1/containers endpoint

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<Format> format

The input format for the custom tool. Default is unconstrained text.

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

A grammar defined by the user.

String definition

The grammar definition.

Syntax syntax

The syntax of the grammar definition. One of `lark` or `regex`.

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

Grammar format. Always `grammar`.

class BetaNamespaceTool:

Groups function/custom tools under a shared namespace.

String description

A description of the namespace shown to the model.

minLength1

String name

The namespace name used in tool calls (for example, `crm`).

minLength1

List<Tool> tools

The function/custom tools available inside this namespace.

class Function:

String name

maxLength128

minLength1

JsonValue; type "function"constant"function"constant

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this function should be deferred and discovered via tool search.

Optional<String> description

Optional<OutputSchema> outputSchema

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

Optional<JsonValue> parameters

Optional<Boolean> strict

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<Format> format

The input format for the custom tool. Default is unconstrained text.

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

A grammar defined by the user.

String definition

The grammar definition.

Syntax syntax

The syntax of the grammar definition. One of `lark` or `regex`.

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

Grammar format. Always `grammar`.

JsonValue; type "namespace"constant"namespace"constant

The type of the tool. Always `namespace`.

class BetaToolSearchTool:

Hosted or BYOT tool search configuration for deferred tools.

JsonValue; type "tool\_search"constant"tool\_search"constant

The type of the tool. Always `tool_search`.

Optional<String> description

Description shown to the model for a client-executed tool search tool.

Optional<Execution> execution

Whether tool search is executed by the server or by the client.

SERVER("server")

CLIENT("client")

Optional<JsonValue> parameters

Parameter schema for a client-executed tool search tool.

class BetaWebSearchPreviewTool:

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

WEB\_SEARCH\_PREVIEW("web\_search\_preview")

WEB\_SEARCH\_PREVIEW\_2025\_03\_11("web\_search\_preview\_2025\_03\_11")

Optional<List<SearchContentType>> searchContentTypes

TEXT("text")

IMAGE("image")

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The user’s location.

JsonValue; type "approximate"constant"approximate"constant

The type of location approximation. Always `approximate`.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

class BetaApplyPatchTool:

Allows the assistant to create, delete, or update files using unified diffs.

JsonValue; type "apply\_patch"constant"apply\_patch"constant

The type of the tool. Always `apply_patch`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

JsonValue; type "additional\_tools"constant"additional\_tools"constant

The item type. Always `additional_tools`.

Optional<String> id

The unique ID of this additional tools item.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseReasoningItem:

A description of the chain of thought used by a reasoning model while generating
a response. Be sure to include these items in your `input` to the Responses API
for subsequent turns of a conversation if you are manually
[managing context](https://platform.openai.com/docs/guides/conversation-state).

String id

The unique identifier of the reasoning content.

List<Summary> summary

Reasoning summary content.

String text

A summary of the reasoning output from the model so far.

JsonValue; type "summary\_text"constant"summary\_text"constant

The type of the object. Always `summary_text`.

JsonValue; type "reasoning"constant"reasoning"constant

The type of the object. Always `reasoning`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<List<Content>> content

Reasoning text content.

String text

The reasoning text from the model.

JsonValue; type "reasoning\_text"constant"reasoning\_text"constant

The type of the reasoning text. Always `reasoning_text`.

Optional<String> encryptedContent

The encrypted content of the reasoning item. This is populated by default
for reasoning items returned by `POST /v1/responses` and WebSocket
`response.create` requests.

Optional<Status> status

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

class BetaResponseCompactionItemParam:

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

String encryptedContent

The encrypted content of the compaction summary.

maxLength10485760

JsonValue; type "compaction"constant"compaction"constant

The type of the item. Always `compaction`.

Optional<String> id

The ID of the compaction item.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

ImageGenerationCall

String id

The unique ID of the image generation call.

Optional<String> result

The generated image encoded in base64.

Status status

The status of the image generation call.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

GENERATING("generating")

FAILED("failed")

JsonValue; type "image\_generation\_call"constant"image\_generation\_call"constant

The type of the image generation call. Always `image_generation_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseCodeInterpreterToolCall:

A tool call to run code.

String id

The unique ID of the code interpreter tool call.

Optional<String> code

The code to run, or null if not available.

String containerId

The ID of the container used to run the code.

Optional<List<Output>> outputs

The outputs generated by the code interpreter, such as logs or images.
Can be null if no outputs are available.

class Logs:

The logs output from the code interpreter.

String logs

The logs output from the code interpreter.

JsonValue; type "logs"constant"logs"constant

The type of the output. Always `logs`.

class Image:

The image output from the code interpreter.

JsonValue; type "image"constant"image"constant

The type of the output. Always `image`.

String url

The URL of the image output from the code interpreter.

formaturi

Status status

The status of the code interpreter tool call. Valid values are `in_progress`, `completed`, `incomplete`, `interpreting`, and `failed`.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

INTERPRETING("interpreting")

FAILED("failed")

JsonValue; type "code\_interpreter\_call"constant"code\_interpreter\_call"constant

The type of the code interpreter tool call. Always `code_interpreter_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

LocalShellCall

String id

The unique ID of the local shell call.

Action action

Execute a shell command on the server.

List<String> command

The command to run.

Env env

Environment variables to set for the command.

JsonValue; type "exec"constant"exec"constant

The type of the local shell action. Always `exec`.

Optional<Long> timeoutMs

Optional timeout in milliseconds for the command.

Optional<String> user

Optional user to run the command as.

Optional<String> workingDirectory

Optional working directory to run the command in.

String callId

The unique ID of the local shell tool call generated by the model.

Status status

The status of the local shell call.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "local\_shell\_call"constant"local\_shell\_call"constant

The type of the local shell call. Always `local_shell_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

LocalShellCallOutput

String id

The unique ID of the local shell tool call generated by the model.

String output

A JSON string of the output of the local shell tool call.

JsonValue; type "local\_shell\_call\_output"constant"local\_shell\_call\_output"constant

The type of the local shell tool call output. Always `local_shell_call_output`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Status> status

The status of the item. One of `in_progress`, `completed`, or `incomplete`.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

ShellCall

Action action

The shell commands and limits that describe how to run the tool call.

List<String> commands

Ordered shell commands for the execution environment to run.

Optional<Long> maxOutputLength

Maximum number of UTF-8 characters to capture from combined stdout and stderr output.

Optional<Long> timeoutMs

Maximum wall-clock time in milliseconds to allow the shell commands to run.

String callId

The unique ID of the shell tool call generated by the model.

maxLength64

minLength1

JsonValue; type "shell\_call"constant"shell\_call"constant

The type of the item. Always `shell_call`.

Optional<String> id

The unique ID of the shell tool call. Populated when this item is returned via API.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

The caller type. Always `direct`.

class Program:

String callerId

The call ID of the program item that produced this tool call.

maxLength64

minLength1

JsonValue; type "program"constant"program"constant

The caller type. Always `program`.

Optional<Environment> environment

The environment to execute the shell commands in.

class BetaLocalEnvironment:

JsonValue; type "local"constant"local"constant

Use a local computer environment.

Optional<List<[BetaLocalSkill](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))>> skills

An optional list of skills.

String description

The description of the skill.

String name

The name of the skill.

String path

The path to the directory containing the skill.

class BetaContainerReference:

String containerId

The ID of the referenced container.

JsonValue; type "container\_reference"constant"container\_reference"constant

References a container created with the /v1/containers endpoint

Optional<Status> status

The status of the shell call. One of `in_progress`, `completed`, or `incomplete`.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

ShellCallOutput

String callId

The unique ID of the shell tool call generated by the model.

maxLength64

minLength1

List<[BetaResponseFunctionShellCallOutputContent](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_shell_call_output_content%20%3E%20(schema))> output

Captured chunks of stdout and stderr output, along with their associated outcomes.

Outcome outcome

The exit or timeout outcome associated with this shell call.

JsonValue;

JsonValue; type "timeout"constant"timeout"constant

The outcome type. Always `timeout`.

class Exit:

Indicates that the shell commands finished and returned an exit code.

long exitCode

The exit code returned by the shell process.

JsonValue; type "exit"constant"exit"constant

The outcome type. Always `exit`.

String stderr

Captured stderr output for the shell call.

maxLength10485760

String stdout

Captured stdout output for the shell call.

maxLength10485760

JsonValue; type "shell\_call\_output"constant"shell\_call\_output"constant

The type of the item. Always `shell_call_output`.

Optional<String> id

The unique ID of the shell tool call output. Populated when this item is returned via API.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

The caller type. Always `direct`.

class Program:

String callerId

The call ID of the program item that produced this tool call.

maxLength64

minLength1

JsonValue; type "program"constant"program"constant

The caller type. Always `program`.

Optional<Long> maxOutputLength

The maximum number of UTF-8 characters captured for this shell call’s combined output.

Optional<Status> status

The status of the shell call output.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

ApplyPatchCall

String callId

The unique ID of the apply patch tool call generated by the model.

maxLength64

minLength1

Operation operation

The specific create, delete, or update instruction for the apply\_patch tool call.

class CreateFile:

Instruction for creating a new file via the apply\_patch tool.

String diff

Unified diff content to apply when creating the file.

maxLength10485760

String path

Path of the file to create relative to the workspace root.

minLength1

JsonValue; type "create\_file"constant"create\_file"constant

The operation type. Always `create_file`.

class DeleteFile:

Instruction for deleting an existing file via the apply\_patch tool.

String path

Path of the file to delete relative to the workspace root.

minLength1

JsonValue; type "delete\_file"constant"delete\_file"constant

The operation type. Always `delete_file`.

class UpdateFile:

Instruction for updating an existing file via the apply\_patch tool.

String diff

Unified diff content to apply to the existing file.

maxLength10485760

String path

Path of the file to update relative to the workspace root.

minLength1

JsonValue; type "update\_file"constant"update\_file"constant

The operation type. Always `update_file`.

Status status

The status of the apply patch tool call. One of `in_progress` or `completed`.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

JsonValue; type "apply\_patch\_call"constant"apply\_patch\_call"constant

The type of the item. Always `apply_patch_call`.

Optional<String> id

The unique ID of the apply patch tool call. Populated when this item is returned via API.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

The caller type. Always `direct`.

class Program:

String callerId

The call ID of the program item that produced this tool call.

maxLength64

minLength1

JsonValue; type "program"constant"program"constant

The caller type. Always `program`.

ApplyPatchCallOutput

String callId

The unique ID of the apply patch tool call generated by the model.

maxLength64

minLength1

Status status

The status of the apply patch tool call output. One of `completed` or `failed`.

COMPLETED("completed")

FAILED("failed")

JsonValue; type "apply\_patch\_call\_output"constant"apply\_patch\_call\_output"constant

The type of the item. Always `apply_patch_call_output`.

Optional<String> id

The unique ID of the apply patch tool call output. Populated when this item is returned via API.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

The caller type. Always `direct`.

class Program:

String callerId

The call ID of the program item that produced this tool call.

maxLength64

minLength1

JsonValue; type "program"constant"program"constant

The caller type. Always `program`.

Optional<String> output

Optional human-readable log text from the apply patch tool (e.g., patch results or errors).

maxLength10485760

McpListTools

String id

The unique ID of the list.

String serverLabel

The label of the MCP server.

List<Tool> tools

The tools available on the server.

JsonValue inputSchema

The JSON schema describing the tool’s input.

String name

The name of the tool.

Optional<JsonValue> annotations

Additional annotations about the tool.

Optional<String> description

The description of the tool.

JsonValue; type "mcp\_list\_tools"constant"mcp\_list\_tools"constant

The type of the item. Always `mcp_list_tools`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<String> error

Error message if the server could not list tools.

McpApprovalRequest

String id

The unique ID of the approval request.

String arguments

A JSON string of arguments for the tool.

String name

The name of the tool to run.

String serverLabel

The label of the MCP server making the request.

JsonValue; type "mcp\_approval\_request"constant"mcp\_approval\_request"constant

The type of the item. Always `mcp_approval_request`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

McpApprovalResponse

String approvalRequestId

The ID of the approval request being answered.

boolean approve

Whether the request was approved.

JsonValue; type "mcp\_approval\_response"constant"mcp\_approval\_response"constant

The type of the item. Always `mcp_approval_response`.

Optional<String> id

The unique ID of the approval response

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<String> reason

Optional reason for the decision.

McpCall

String id

The unique ID of the tool call.

String arguments

A JSON string of the arguments passed to the tool.

String name

The name of the tool that was run.

String serverLabel

The label of the MCP server running the tool.

JsonValue; type "mcp\_call"constant"mcp\_call"constant

The type of the item. Always `mcp_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<String> approvalRequestId

Unique identifier for the MCP tool call approval request.
Include this value in a subsequent `mcp_approval_response` input to approve or reject the corresponding tool call.

Optional<String> error

The error from the tool call, if any.

Optional<String> output

The output from the tool call.

Optional<Status> status

The status of the tool call. One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

CALLING("calling")

FAILED("failed")

class BetaResponseCustomToolCallOutput:

The output of a custom tool call from your code, being sent back to the model.

String callId

The call ID, used to map this custom tool call output to a custom tool call.

Output output

The output from the custom tool call generated by your code.
Can be a string or an list of output content.

String

List<BetaFunctionAndCustomToolCallOutput>

class BetaResponseInputText:

A text input to the model.

String text

The text input to the model.

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputImage:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail detail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

JsonValue; type "input\_image"constant"input\_image"constant

The type of the input item. Always `input_image`.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> imageUrl

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile:

A file input to the model.

JsonValue; type "input\_file"constant"input\_file"constant

The type of the input item. Always `input_file`.

Optional<Detail> detail

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

AUTO("auto")

LOW("low")

HIGH("high")

Optional<String> fileData

The content of the file to be sent to the model.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> fileUrl

The URL of the file to be sent to the model.

formaturi

Optional<String> filename

The name of the file to be sent to the model.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

JsonValue; type "custom\_tool\_call\_output"constant"custom\_tool\_call\_output"constant

The type of the custom tool call output. Always `custom_tool_call_output`.

Optional<String> id

The unique ID of the custom tool call output in the OpenAI platform.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

The caller type. Always `direct`.

class Program:

String callerId

The call ID of the program item that produced this tool call.

maxLength64

minLength1

JsonValue; type "program"constant"program"constant

The caller type. Always `program`.

class BetaResponseCustomToolCall:

A call to a custom tool created by the model.

String callId

An identifier used to map this custom tool call to a tool call output.

String input

The input for the custom tool call generated by the model.

String name

The name of the custom tool being called.

JsonValue; type "custom\_tool\_call"constant"custom\_tool\_call"constant

The type of the custom tool call. Always `custom_tool_call`.

Optional<String> id

The unique ID of the custom tool call in the OpenAI platform.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

class Program:

String callerId

The call ID of the program item that produced this tool call.

JsonValue; type "program"constant"program"constant

Optional<String> namespace

The namespace of the custom tool being called.

CompactionTrigger

JsonValue; type "compaction\_trigger"constant"compaction\_trigger"constant

The type of the item. Always `compaction_trigger`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

ItemReference

String id

The ID of the item to reference.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Type> type

The type of item to reference. Always `item_reference`.

Program

String id

The unique ID of this program item.

String callId

The stable call ID of the program item.

maxLength64

minLength1

String code

The JavaScript source executed by programmatic tool calling.

maxLength10485760

String fingerprint

Opaque program replay fingerprint that must be round-tripped.

maxLength10485760

JsonValue; type "program"constant"program"constant

The item type. Always `program`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

ProgramOutput

String id

The unique ID of this program output item.

String callId

The call ID of the program item.

maxLength64

minLength1

String result

The result produced by the program item.

maxLength10485760

Status status

The terminal status of the program output.

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "program\_output"constant"program\_output"constant

The item type. Always `program_output`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Metadata> metadata

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

Model model

Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model guide](https://platform.openai.com/docs/models)
to browse and compare available models.

GPT\_5\_6\_SOL("gpt-5.6-sol")

GPT\_5\_6\_TERRA("gpt-5.6-terra")

GPT\_5\_6\_LUNA("gpt-5.6-luna")

GPT\_5\_4("gpt-5.4")

GPT\_5\_4\_MINI("gpt-5.4-mini")

GPT\_5\_4\_NANO("gpt-5.4-nano")

GPT\_5\_4\_MINI\_2026\_03\_17("gpt-5.4-mini-2026-03-17")

GPT\_5\_4\_NANO\_2026\_03\_17("gpt-5.4-nano-2026-03-17")

GPT\_5\_3\_CHAT\_LATEST("gpt-5.3-chat-latest")

GPT\_5\_2("gpt-5.2")

GPT\_5\_2\_2025\_12\_11("gpt-5.2-2025-12-11")

GPT\_5\_2\_CHAT\_LATEST("gpt-5.2-chat-latest")

GPT\_5\_2\_PRO("gpt-5.2-pro")

GPT\_5\_2\_PRO\_2025\_12\_11("gpt-5.2-pro-2025-12-11")

GPT\_5\_1("gpt-5.1")

GPT\_5\_1\_2025\_11\_13("gpt-5.1-2025-11-13")

GPT\_5\_1\_CODEX("gpt-5.1-codex")

GPT\_5\_1\_MINI("gpt-5.1-mini")

GPT\_5\_1\_CHAT\_LATEST("gpt-5.1-chat-latest")

GPT\_5("gpt-5")

GPT\_5\_MINI("gpt-5-mini")

GPT\_5\_NANO("gpt-5-nano")

GPT\_5\_2025\_08\_07("gpt-5-2025-08-07")

GPT\_5\_MINI\_2025\_08\_07("gpt-5-mini-2025-08-07")

GPT\_5\_NANO\_2025\_08\_07("gpt-5-nano-2025-08-07")

GPT\_5\_CHAT\_LATEST("gpt-5-chat-latest")

GPT\_4\_1("gpt-4.1")

GPT\_4\_1\_MINI("gpt-4.1-mini")

GPT\_4\_1\_NANO("gpt-4.1-nano")

GPT\_4\_1\_2025\_04\_14("gpt-4.1-2025-04-14")

GPT\_4\_1\_MINI\_2025\_04\_14("gpt-4.1-mini-2025-04-14")

GPT\_4\_1\_NANO\_2025\_04\_14("gpt-4.1-nano-2025-04-14")

O4\_MINI("o4-mini")

O4\_MINI\_2025\_04\_16("o4-mini-2025-04-16")

O3("o3")

O3\_2025\_04\_16("o3-2025-04-16")

O3\_MINI("o3-mini")

O3\_MINI\_2025\_01\_31("o3-mini-2025-01-31")

O1("o1")

O1\_2024\_12\_17("o1-2024-12-17")

O1\_PREVIEW("o1-preview")

O1\_PREVIEW\_2024\_09\_12("o1-preview-2024-09-12")

O1\_MINI("o1-mini")

O1\_MINI\_2024\_09\_12("o1-mini-2024-09-12")

GPT\_4O("gpt-4o")

GPT\_4O\_2024\_11\_20("gpt-4o-2024-11-20")

GPT\_4O\_2024\_08\_06("gpt-4o-2024-08-06")

GPT\_4O\_2024\_05\_13("gpt-4o-2024-05-13")

GPT\_4O\_AUDIO\_PREVIEW("gpt-4o-audio-preview")

GPT\_4O\_AUDIO\_PREVIEW\_2024\_10\_01("gpt-4o-audio-preview-2024-10-01")

GPT\_4O\_AUDIO\_PREVIEW\_2024\_12\_17("gpt-4o-audio-preview-2024-12-17")

GPT\_4O\_AUDIO\_PREVIEW\_2025\_06\_03("gpt-4o-audio-preview-2025-06-03")

GPT\_4O\_MINI\_AUDIO\_PREVIEW("gpt-4o-mini-audio-preview")

GPT\_4O\_MINI\_AUDIO\_PREVIEW\_2024\_12\_17("gpt-4o-mini-audio-preview-2024-12-17")

GPT\_4O\_SEARCH\_PREVIEW("gpt-4o-search-preview")

GPT\_4O\_MINI\_SEARCH\_PREVIEW("gpt-4o-mini-search-preview")

GPT\_4O\_SEARCH\_PREVIEW\_2025\_03\_11("gpt-4o-search-preview-2025-03-11")

GPT\_4O\_MINI\_SEARCH\_PREVIEW\_2025\_03\_11("gpt-4o-mini-search-preview-2025-03-11")

CHATGPT\_4O\_LATEST("chatgpt-4o-latest")

CODEX\_MINI\_LATEST("codex-mini-latest")

GPT\_4O\_MINI("gpt-4o-mini")

GPT\_4O\_MINI\_2024\_07\_18("gpt-4o-mini-2024-07-18")

GPT\_4\_TURBO("gpt-4-turbo")

GPT\_4\_TURBO\_2024\_04\_09("gpt-4-turbo-2024-04-09")

GPT\_4\_0125\_PREVIEW("gpt-4-0125-preview")

GPT\_4\_TURBO\_PREVIEW("gpt-4-turbo-preview")

GPT\_4\_1106\_PREVIEW("gpt-4-1106-preview")

GPT\_4\_VISION\_PREVIEW("gpt-4-vision-preview")

GPT\_4("gpt-4")

GPT\_4\_0314("gpt-4-0314")

GPT\_4\_0613("gpt-4-0613")

GPT\_4\_32K("gpt-4-32k")

GPT\_4\_32K\_0314("gpt-4-32k-0314")

GPT\_4\_32K\_0613("gpt-4-32k-0613")

GPT\_3\_5\_TURBO("gpt-3.5-turbo")

GPT\_3\_5\_TURBO\_16K("gpt-3.5-turbo-16k")

GPT\_3\_5\_TURBO\_0301("gpt-3.5-turbo-0301")

GPT\_3\_5\_TURBO\_0613("gpt-3.5-turbo-0613")

GPT\_3\_5\_TURBO\_1106("gpt-3.5-turbo-1106")

GPT\_3\_5\_TURBO\_0125("gpt-3.5-turbo-0125")

GPT\_3\_5\_TURBO\_16K\_0613("gpt-3.5-turbo-16k-0613")

O1\_PRO("o1-pro")

O1\_PRO\_2025\_03\_19("o1-pro-2025-03-19")

O3\_PRO("o3-pro")

O3\_PRO\_2025\_06\_10("o3-pro-2025-06-10")

O3\_DEEP\_RESEARCH("o3-deep-research")

O3\_DEEP\_RESEARCH\_2025\_06\_26("o3-deep-research-2025-06-26")

O4\_MINI\_DEEP\_RESEARCH("o4-mini-deep-research")

O4\_MINI\_DEEP\_RESEARCH\_2025\_06\_26("o4-mini-deep-research-2025-06-26")

COMPUTER\_USE\_PREVIEW("computer-use-preview")

COMPUTER\_USE\_PREVIEW\_2025\_03\_11("computer-use-preview-2025-03-11")

GPT\_5\_CODEX("gpt-5-codex")

GPT\_5\_PRO("gpt-5-pro")

GPT\_5\_PRO\_2025\_10\_06("gpt-5-pro-2025-10-06")

GPT\_5\_1\_CODEX\_MAX("gpt-5.1-codex-max")

JsonValue; object\_ "response"constant"response"constant

The object type of this resource - always set to `response`.

List<[BetaResponseOutputItem](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema))> output

An array of content items generated by the model.

* The length and order of items in the `output` array is dependent
  on the model’s response.
* Rather than accessing the first item in the `output` array and
  assuming it’s an `assistant` message with the content generated by
  the model, you might consider using the `output_text` property where
  supported in SDKs.

class BetaResponseOutputMessage:

An output message from the model.

String id

The unique ID of the output message.

List<Content> content

The content of the output message.

class BetaResponseOutputText:

A text output from the model.

List<Annotation> annotations

The annotations of the text output.

class FileCitation:

A citation to a file.

String fileId

The ID of the file.

String filename

The filename of the file cited.

long index

The index of the file in the list of files.

JsonValue; type "file\_citation"constant"file\_citation"constant

The type of the file citation. Always `file_citation`.

class UrlCitation:

A citation for a web resource used to generate a model response.

long endIndex

The index of the last character of the URL citation in the message.

long startIndex

The index of the first character of the URL citation in the message.

String title

The title of the web resource.

JsonValue; type "url\_citation"constant"url\_citation"constant

The type of the URL citation. Always `url_citation`.

String url

The URL of the web resource.

formaturi

class ContainerFileCitation:

A citation for a container file used to generate a model response.

String containerId

The ID of the container file.

long endIndex

The index of the last character of the container file citation in the message.

String fileId

The ID of the file.

String filename

The filename of the container file cited.

long startIndex

The index of the first character of the container file citation in the message.

JsonValue; type "container\_file\_citation"constant"container\_file\_citation"constant

The type of the container file citation. Always `container_file_citation`.

class FilePath:

A path to a file.

String fileId

The ID of the file.

long index

The index of the file in the list of files.

JsonValue; type "file\_path"constant"file\_path"constant

The type of the file path. Always `file_path`.

String text

The text output from the model.

JsonValue; type "output\_text"constant"output\_text"constant

The type of the output text. Always `output_text`.

Optional<List<Logprob>> logprobs

String token

List<long> bytes

double logprob

List<TopLogprob> topLogprobs

String token

List<long> bytes

double logprob

class BetaResponseOutputRefusal:

A refusal from the model.

String refusal

The refusal explanation from the model.

JsonValue; type "refusal"constant"refusal"constant

The type of the refusal. Always `refusal`.

JsonValue; role "assistant"constant"assistant"constant

The role of the output message. Always `assistant`.

Status status

The status of the message input. One of `in_progress`, `completed`, or
`incomplete`. Populated when input items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "message"constant"message"constant

The type of the output message. Always `message`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Phase> phase

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

COMMENTARY("commentary")

FINAL\_ANSWER("final\_answer")

class BetaResponseFileSearchToolCall:

The results of a file search tool call. See the
[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

String id

The unique ID of the file search tool call.

List<String> queries

The queries used to search for files.

Status status

The status of the file search tool call. One of `in_progress`,
`searching`, `incomplete` or `failed`,

IN\_PROGRESS("in\_progress")

SEARCHING("searching")

COMPLETED("completed")

INCOMPLETE("incomplete")

FAILED("failed")

JsonValue; type "file\_search\_call"constant"file\_search\_call"constant

The type of the file search tool call. Always `file_search_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<List<Result>> results

The results of the file search tool call.

Optional<Attributes> attributes

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

String

double

boolean

Optional<String> fileId

The unique ID of the file.

Optional<String> filename

The name of the file.

Optional<Double> score

The relevance score of the file - a value between 0 and 1.

formatfloat

Optional<String> text

The text that was retrieved from the file.

class BetaResponseFunctionToolCall:

A tool call to run a function. See the
[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

String arguments

A JSON string of the arguments to pass to the function.

String callId

The unique ID of the function tool call generated by the model.

String name

The name of the function to run.

JsonValue; type "function\_call"constant"function\_call"constant

The type of the function tool call. Always `function_call`.

Optional<String> id

The unique ID of the function tool call.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

class Program:

String callerId

The call ID of the program item that produced this tool call.

JsonValue; type "program"constant"program"constant

Optional<String> namespace

The namespace of the function to run.

Optional<Status> status

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

class BetaResponseFunctionToolCallOutputItem:

String id

The unique ID of the function call tool output.

String callId

The unique ID of the function tool call generated by the model.

Output output

The output from the function call generated by your code.
Can be a string or an list of output content.

String

List<BetaFunctionAndCustomToolCallOutput>

class BetaResponseInputText:

A text input to the model.

String text

The text input to the model.

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputImage:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail detail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

JsonValue; type "input\_image"constant"input\_image"constant

The type of the input item. Always `input_image`.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> imageUrl

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile:

A file input to the model.

JsonValue; type "input\_file"constant"input\_file"constant

The type of the input item. Always `input_file`.

Optional<Detail> detail

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

AUTO("auto")

LOW("low")

HIGH("high")

Optional<String> fileData

The content of the file to be sent to the model.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> fileUrl

The URL of the file to be sent to the model.

formaturi

Optional<String> filename

The name of the file to be sent to the model.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

Status status

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "function\_call\_output"constant"function\_call\_output"constant

The type of the function tool call output. Always `function_call_output`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

The caller type. Always `direct`.

class Program:

String callerId

The call ID of the program item that produced this tool call.

maxLength64

minLength1

JsonValue; type "program"constant"program"constant

The caller type. Always `program`.

Optional<String> createdBy

The identifier of the actor that created the item.

AgentMessage

String id

The unique ID of the agent message.

String author

The sending agent identity.

List<Content> content

Encrypted content sent between agents.

class BetaResponseInputText:

A text input to the model.

String text

The text input to the model.

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseOutputText:

A text output from the model.

List<Annotation> annotations

The annotations of the text output.

class FileCitation:

A citation to a file.

String fileId

The ID of the file.

String filename

The filename of the file cited.

long index

The index of the file in the list of files.

JsonValue; type "file\_citation"constant"file\_citation"constant

The type of the file citation. Always `file_citation`.

class UrlCitation:

A citation for a web resource used to generate a model response.

long endIndex

The index of the last character of the URL citation in the message.

long startIndex

The index of the first character of the URL citation in the message.

String title

The title of the web resource.

JsonValue; type "url\_citation"constant"url\_citation"constant

The type of the URL citation. Always `url_citation`.

String url

The URL of the web resource.

formaturi

class ContainerFileCitation:

A citation for a container file used to generate a model response.

String containerId

The ID of the container file.

long endIndex

The index of the last character of the container file citation in the message.

String fileId

The ID of the file.

String filename

The filename of the container file cited.

long startIndex

The index of the first character of the container file citation in the message.

JsonValue; type "container\_file\_citation"constant"container\_file\_citation"constant

The type of the container file citation. Always `container_file_citation`.

class FilePath:

A path to a file.

String fileId

The ID of the file.

long index

The index of the file in the list of files.

JsonValue; type "file\_path"constant"file\_path"constant

The type of the file path. Always `file_path`.

String text

The text output from the model.

JsonValue; type "output\_text"constant"output\_text"constant

The type of the output text. Always `output_text`.

Optional<List<Logprob>> logprobs

String token

List<long> bytes

double logprob

List<TopLogprob> topLogprobs

String token

List<long> bytes

double logprob

class Text:

A text content.

String text

JsonValue; type "text"constant"text"constant

class SummaryText:

A summary text from the model.

String text

A summary of the reasoning output from the model so far.

JsonValue; type "summary\_text"constant"summary\_text"constant

The type of the object. Always `summary_text`.

class ReasoningText:

Reasoning text from the model.

String text

The reasoning text from the model.

JsonValue; type "reasoning\_text"constant"reasoning\_text"constant

The type of the reasoning text. Always `reasoning_text`.

class BetaResponseOutputRefusal:

A refusal from the model.

String refusal

The refusal explanation from the model.

JsonValue; type "refusal"constant"refusal"constant

The type of the refusal. Always `refusal`.

class BetaResponseInputImage:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail detail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

JsonValue; type "input\_image"constant"input\_image"constant

The type of the input item. Always `input_image`.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> imageUrl

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class ComputerScreenshot:

A screenshot of a computer.

Detail detail

The detail level of the screenshot image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

Optional<String> fileId

The identifier of an uploaded file that contains the screenshot.

Optional<String> imageUrl

The URL of the screenshot image.

formaturi

JsonValue; type "computer\_screenshot"constant"computer\_screenshot"constant

Specifies the event type. For a computer screenshot, this property is always set to `computer_screenshot`.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile:

A file input to the model.

JsonValue; type "input\_file"constant"input\_file"constant

The type of the input item. Always `input_file`.

Optional<Detail> detail

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

AUTO("auto")

LOW("low")

HIGH("high")

Optional<String> fileData

The content of the file to be sent to the model.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> fileUrl

The URL of the file to be sent to the model.

formaturi

Optional<String> filename

The name of the file to be sent to the model.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class EncryptedContent:

Opaque encrypted content that Responses API decrypts inside trusted model execution.

String encryptedContent

Opaque encrypted content.

JsonValue; type "encrypted\_content"constant"encrypted\_content"constant

The type of the input item. Always `encrypted_content`.

String recipient

The destination agent identity.

JsonValue; type "agent\_message"constant"agent\_message"constant

The type of the item. Always `agent_message`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

MultiAgentCall

String id

The unique ID of the multi-agent call item.

Action action

The multi-agent action to execute.

SPAWN\_AGENT("spawn\_agent")

INTERRUPT\_AGENT("interrupt\_agent")

LIST\_AGENTS("list\_agents")

SEND\_MESSAGE("send\_message")

FOLLOWUP\_TASK("followup\_task")

WAIT\_AGENT("wait\_agent")

String arguments

The JSON string of arguments generated for the action.

String callId

The unique ID linking this call to its output.

JsonValue; type "multi\_agent\_call"constant"multi\_agent\_call"constant

The type of the multi-agent call. Always `multi_agent_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

MultiAgentCallOutput

String id

The unique ID of the multi-agent call output item.

Action action

The multi-agent action that produced this result.

SPAWN\_AGENT("spawn\_agent")

INTERRUPT\_AGENT("interrupt\_agent")

LIST\_AGENTS("list\_agents")

SEND\_MESSAGE("send\_message")

FOLLOWUP\_TASK("followup\_task")

WAIT\_AGENT("wait\_agent")

String callId

The unique ID of the multi-agent call.

List<[BetaResponseOutputText](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema))> output

Text output returned by the multi-agent action.

List<Annotation> annotations

The annotations of the text output.

class FileCitation:

A citation to a file.

String fileId

The ID of the file.

String filename

The filename of the file cited.

long index

The index of the file in the list of files.

JsonValue; type "file\_citation"constant"file\_citation"constant

The type of the file citation. Always `file_citation`.

class UrlCitation:

A citation for a web resource used to generate a model response.

long endIndex

The index of the last character of the URL citation in the message.

long startIndex

The index of the first character of the URL citation in the message.

String title

The title of the web resource.

JsonValue; type "url\_citation"constant"url\_citation"constant

The type of the URL citation. Always `url_citation`.

String url

The URL of the web resource.

formaturi

class ContainerFileCitation:

A citation for a container file used to generate a model response.

String containerId

The ID of the container file.

long endIndex

The index of the last character of the container file citation in the message.

String fileId

The ID of the file.

String filename

The filename of the container file cited.

long startIndex

The index of the first character of the container file citation in the message.

JsonValue; type "container\_file\_citation"constant"container\_file\_citation"constant

The type of the container file citation. Always `container_file_citation`.

class FilePath:

A path to a file.

String fileId

The ID of the file.

long index

The index of the file in the list of files.

JsonValue; type "file\_path"constant"file\_path"constant

The type of the file path. Always `file_path`.

String text

The text output from the model.

JsonValue; type "output\_text"constant"output\_text"constant

The type of the output text. Always `output_text`.

Optional<List<Logprob>> logprobs

String token

List<long> bytes

double logprob

List<TopLogprob> topLogprobs

String token

List<long> bytes

double logprob

JsonValue; type "multi\_agent\_call\_output"constant"multi\_agent\_call\_output"constant

The type of the multi-agent result. Always `multi_agent_call_output`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseFunctionWebSearch:

The results of a web search tool call. See the
[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

String id

The unique ID of the web search tool call.

Action action

An object describing the specific action taken in this web search call.
Includes details on how the model used the web (search, open\_page, find\_in\_page).

class Search:

Action type “search” - Performs a web search query.

JsonValue; type "search"constant"search"constant

The action type.

Optional<List<String>> queries

The search queries.

DeprecatedOptional<String> query

The search query.

Optional<List<Source>> sources

The sources used in the search.

JsonValue; type "url"constant"url"constant

The type of source. Always `url`.

String url

The URL of the source.

formaturi

class OpenPage:

Action type “open\_page” - Opens a specific URL from search results.

JsonValue; type "open\_page"constant"open\_page"constant

The action type.

Optional<String> url

The URL opened by the model.

formaturi

class FindInPage:

Action type “find\_in\_page”: Searches for a pattern within a loaded page.

String pattern

The pattern or text to search for within the page.

JsonValue; type "find\_in\_page"constant"find\_in\_page"constant

The action type.

String url

The URL of the page searched for the pattern.

formaturi

Status status

The status of the web search tool call.

IN\_PROGRESS("in\_progress")

SEARCHING("searching")

COMPLETED("completed")

FAILED("failed")

JsonValue; type "web\_search\_call"constant"web\_search\_call"constant

The type of the web search tool call. Always `web_search_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseComputerToolCall:

A tool call to a computer use tool. See the
[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

String id

The unique ID of the computer call.

String callId

An identifier used when responding to the tool call with output.

List<PendingSafetyCheck> pendingSafetyChecks

The pending safety checks for the computer call.

String id

The ID of the pending safety check.

Optional<String> code

The type of the pending safety check.

Optional<String> message

Details about the pending safety check.

Status status

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

Type type

The type of the computer call. Always `computer_call`.

Optional<[BetaComputerAction](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action%20%3E%20(schema))> action

A click action.

Click

Button button

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

LEFT("left")

RIGHT("right")

WHEEL("wheel")

BACK("back")

FORWARD("forward")

JsonValue; type "click"constant"click"constant

Specifies the event type. For a click action, this property is always `click`.

long x

The x-coordinate where the click occurred.

long y

The y-coordinate where the click occurred.

Optional<List<String>> keys

The keys being held while clicking.

DoubleClick

Optional<List<String>> keys

The keys being held while double-clicking.

JsonValue; type "double\_click"constant"double\_click"constant

Specifies the event type. For a double click action, this property is always set to `double_click`.

long x

The x-coordinate where the double click occurred.

long y

The y-coordinate where the double click occurred.

Drag

List<Path> path

An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

[
  { x: 100, y: 200 },
  { x: 200, y: 300 }
]

long x

The x-coordinate.

long y

The y-coordinate.

JsonValue; type "drag"constant"drag"constant

Specifies the event type. For a drag action, this property is always set to `drag`.

Optional<List<String>> keys

The keys being held while dragging the mouse.

Keypress

List<String> keys

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

JsonValue; type "keypress"constant"keypress"constant

Specifies the event type. For a keypress action, this property is always set to `keypress`.

Move

JsonValue; type "move"constant"move"constant

Specifies the event type. For a move action, this property is always set to `move`.

long x

The x-coordinate to move to.

long y

The y-coordinate to move to.

Optional<List<String>> keys

The keys being held while moving the mouse.

JsonValue;

JsonValue; type "screenshot"constant"screenshot"constant

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

Scroll

long scrollX

The horizontal scroll distance.

long scrollY

The vertical scroll distance.

JsonValue; type "scroll"constant"scroll"constant

Specifies the event type. For a scroll action, this property is always set to `scroll`.

long x

The x-coordinate where the scroll occurred.

long y

The y-coordinate where the scroll occurred.

Optional<List<String>> keys

The keys being held while scrolling.

Type

String text

The text to type.

JsonValue; type "type"constant"type"constant

Specifies the event type. For a type action, this property is always set to `type`.

JsonValue;

JsonValue; type "wait"constant"wait"constant

Specifies the event type. For a wait action, this property is always set to `wait`.

Optional<List<[BetaComputerAction](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action%20%3E%20(schema))>> actions

Flattened batched actions for `computer_use`. Each action includes an
`type` discriminator and action-specific fields.

Click

Button button

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

LEFT("left")

RIGHT("right")

WHEEL("wheel")

BACK("back")

FORWARD("forward")

JsonValue; type "click"constant"click"constant

Specifies the event type. For a click action, this property is always `click`.

long x

The x-coordinate where the click occurred.

long y

The y-coordinate where the click occurred.

Optional<List<String>> keys

The keys being held while clicking.

DoubleClick

Optional<List<String>> keys

The keys being held while double-clicking.

JsonValue; type "double\_click"constant"double\_click"constant

Specifies the event type. For a double click action, this property is always set to `double_click`.

long x

The x-coordinate where the double click occurred.

long y

The y-coordinate where the double click occurred.

Drag

List<Path> path

An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

[
  { x: 100, y: 200 },
  { x: 200, y: 300 }
]

long x

The x-coordinate.

long y

The y-coordinate.

JsonValue; type "drag"constant"drag"constant

Specifies the event type. For a drag action, this property is always set to `drag`.

Optional<List<String>> keys

The keys being held while dragging the mouse.

Keypress

List<String> keys

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

JsonValue; type "keypress"constant"keypress"constant

Specifies the event type. For a keypress action, this property is always set to `keypress`.

Move

JsonValue; type "move"constant"move"constant

Specifies the event type. For a move action, this property is always set to `move`.

long x

The x-coordinate to move to.

long y

The y-coordinate to move to.

Optional<List<String>> keys

The keys being held while moving the mouse.

JsonValue;

JsonValue; type "screenshot"constant"screenshot"constant

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

Scroll

long scrollX

The horizontal scroll distance.

long scrollY

The vertical scroll distance.

JsonValue; type "scroll"constant"scroll"constant

Specifies the event type. For a scroll action, this property is always set to `scroll`.

long x

The x-coordinate where the scroll occurred.

long y

The y-coordinate where the scroll occurred.

Optional<List<String>> keys

The keys being held while scrolling.

Type

String text

The text to type.

JsonValue; type "type"constant"type"constant

Specifies the event type. For a type action, this property is always set to `type`.

JsonValue;

JsonValue; type "wait"constant"wait"constant

Specifies the event type. For a wait action, this property is always set to `wait`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseComputerToolCallOutputItem:

String id

The unique ID of the computer call tool output.

String callId

The ID of the computer tool call that produced the output.

[BetaResponseComputerToolCallOutputScreenshot](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema)) output

A computer screenshot image used with the computer use tool.

JsonValue; type "computer\_screenshot"constant"computer\_screenshot"constant

Specifies the event type. For a computer screenshot, this property is
always set to `computer_screenshot`.

Optional<String> fileId

The identifier of an uploaded file that contains the screenshot.

Optional<String> imageUrl

The URL of the screenshot image.

formaturi

Status status

The status of the message input. One of `in_progress`, `completed`, or
`incomplete`. Populated when input items are returned via API.

COMPLETED("completed")

INCOMPLETE("incomplete")

FAILED("failed")

IN\_PROGRESS("in\_progress")

JsonValue; type "computer\_call\_output"constant"computer\_call\_output"constant

The type of the computer tool call output. Always `computer_call_output`.

Optional<List<AcknowledgedSafetyCheck>> acknowledgedSafetyChecks

The safety checks reported by the API that have been acknowledged by the
developer.

String id

The ID of the pending safety check.

Optional<String> code

The type of the pending safety check.

Optional<String> message

Details about the pending safety check.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<String> createdBy

The identifier of the actor that created the item.

class BetaResponseReasoningItem:

A description of the chain of thought used by a reasoning model while generating
a response. Be sure to include these items in your `input` to the Responses API
for subsequent turns of a conversation if you are manually
[managing context](https://platform.openai.com/docs/guides/conversation-state).

String id

The unique identifier of the reasoning content.

List<Summary> summary

Reasoning summary content.

String text

A summary of the reasoning output from the model so far.

JsonValue; type "summary\_text"constant"summary\_text"constant

The type of the object. Always `summary_text`.

JsonValue; type "reasoning"constant"reasoning"constant

The type of the object. Always `reasoning`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<List<Content>> content

Reasoning text content.

String text

The reasoning text from the model.

JsonValue; type "reasoning\_text"constant"reasoning\_text"constant

The type of the reasoning text. Always `reasoning_text`.

Optional<String> encryptedContent

The encrypted content of the reasoning item. This is populated by default
for reasoning items returned by `POST /v1/responses` and WebSocket
`response.create` requests.

Optional<Status> status

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

Program

String id

The unique ID of the program item.

String callId

The stable call ID of the program item.

String code

The JavaScript source executed by programmatic tool calling.

String fingerprint

Opaque program replay fingerprint that must be round-tripped.

JsonValue; type "program"constant"program"constant

The type of the item. Always `program`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

ProgramOutput

String id

The unique ID of the program output item.

String callId

The call ID of the program item.

String result

The result produced by the program item.

Status status

The terminal status of the program output item.

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "program\_output"constant"program\_output"constant

The type of the item. Always `program_output`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseToolSearchCall:

String id

The unique ID of the tool search call item.

JsonValue arguments

Arguments used for the tool search call.

Optional<String> callId

The unique ID of the tool search call generated by the model.

Execution execution

Whether tool search was executed by the server or by the client.

SERVER("server")

CLIENT("client")

Status status

The status of the tool search call item that was recorded.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "tool\_search\_call"constant"tool\_search\_call"constant

The type of the item. Always `tool_search_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<String> createdBy

The identifier of the actor that created the item.

class BetaResponseToolSearchOutputItem:

String id

The unique ID of the tool search output item.

Optional<String> callId

The unique ID of the tool search call generated by the model.

Execution execution

Whether tool search was executed by the server or by the client.

SERVER("server")

CLIENT("client")

Status status

The status of the tool search output item that was recorded.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

List<[BetaTool](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))> tools

The loaded tool definitions returned by tool search.

class BetaFunctionTool:

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

String name

The name of the function to call.

Optional<Parameters> parameters

A JSON schema object describing the parameters of the function.

Optional<Boolean> strict

Whether strict parameter validation is enforced for this function tool.

JsonValue; type "function"constant"function"constant

The type of the function tool. Always `function`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this function is deferred and loaded via tool search.

Optional<String> description

A description of the function. Used by the model to determine whether or not to call the function.

Optional<OutputSchema> outputSchema

A JSON schema object describing the JSON value encoded in string outputs for this function.

class BetaFileSearchTool:

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

JsonValue; type "file\_search"constant"file\_search"constant

The type of the file search tool. Always `file_search`.

List<String> vectorStoreIds

The IDs of the vector stores to search.

Optional<Filters> filters

A filter to apply.

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

String

double

boolean

List<ComparisonFilterValueItem>

String

double

class CompoundFilter:

Combine multiple filters using `and` or `or`.

List<Filter> filters

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

String

double

boolean

List<ComparisonFilterValueItem>

String

double

JsonValue

Type type

Type of operation: `and` or `or`.

AND("and")

OR("or")

Optional<Long> maxNumResults

The maximum number of results to return. This number should be between 1 and 50 inclusive.

Optional<RankingOptions> rankingOptions

Ranking options for search.

Optional<HybridSearch> hybridSearch

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

double embeddingWeight

The weight of the embedding in the reciprocal ranking fusion.

double textWeight

The weight of the text in the reciprocal ranking fusion.

Optional<Ranker> ranker

The ranker to use for the file search.

AUTO("auto")

DEFAULT\_2024\_11\_15("default-2024-11-15")

Optional<Double> scoreThreshold

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class BetaComputerTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

JsonValue; type "computer"constant"computer"constant

The type of the computer tool. Always `computer`.

class BetaComputerUsePreviewTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

long displayHeight

The height of the computer display.

long displayWidth

The width of the computer display.

Environment environment

The type of computer environment to control.

WINDOWS("windows")

MAC("mac")

LINUX("linux")

UBUNTU("ubuntu")

BROWSER("browser")

JsonValue; type "computer\_use\_preview"constant"computer\_use\_preview"constant

The type of the computer use tool. Always `computer_use_preview`.

class BetaWebSearchTool:

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

WEB\_SEARCH("web\_search")

WEB\_SEARCH\_2025\_08\_26("web\_search\_2025\_08\_26")

Optional<Filters> filters

Filters for the search.

Optional<List<String>> allowedDomains

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The approximate location of the user.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

Optional<Type> type

The type of location approximation. Always `approximate`.

Mcp

String serverLabel

A label for this MCP server, used to identify it in tool calls.

JsonValue; type "mcp"constant"mcp"constant

The type of the MCP tool. Always `mcp`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<AllowedTools> allowedTools

List of allowed tool names or a filter object.

List<String>

class McpToolFilter:

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<String> authorization

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

Optional<ConnectorId> connectorId

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

CONNECTOR\_DROPBOX("connector\_dropbox")

CONNECTOR\_GMAIL("connector\_gmail")

CONNECTOR\_GOOGLECALENDAR("connector\_googlecalendar")

CONNECTOR\_GOOGLEDRIVE("connector\_googledrive")

CONNECTOR\_MICROSOFTTEAMS("connector\_microsoftteams")

CONNECTOR\_OUTLOOKCALENDAR("connector\_outlookcalendar")

CONNECTOR\_OUTLOOKEMAIL("connector\_outlookemail")

CONNECTOR\_SHAREPOINT("connector\_sharepoint")

Optional<Boolean> deferLoading

Whether this MCP tool is deferred and discovered via tool search.

Optional<Headers> headers

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

Optional<RequireApproval> requireApproval

Specify which of the MCP server’s tools require approval.

class McpToolApprovalFilter:

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

Optional<Always> always

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<Never> never

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

enum McpToolApprovalSetting:

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

ALWAYS("always")

NEVER("never")

Optional<String> serverDescription

Optional description of the MCP server, used to provide more context.

Optional<String> serverUrl

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

Optional<String> tunnelId

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter

Container container

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

String

class CodeInterpreterToolAuto:

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

JsonValue; type "auto"constant"auto"constant

Always `auto`.

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the code interpreter container.

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

JsonValue; type "code\_interpreter"constant"code\_interpreter"constant

The type of the code interpreter tool. Always `code_interpreter`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

JsonValue;

JsonValue; type "programmatic\_tool\_calling"constant"programmatic\_tool\_calling"constant

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration

JsonValue; type "image\_generation"constant"image\_generation"constant

The type of the image generation tool. Always `image_generation`.

Optional<Action> action

Whether to generate a new image or edit an existing image. Default: `auto`.

GENERATE("generate")

EDIT("edit")

AUTO("auto")

Optional<Background> background

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

TRANSPARENT("transparent")

OPAQUE("opaque")

AUTO("auto")

Optional<InputFidelity> inputFidelity

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

HIGH("high")

LOW("low")

Optional<InputImageMask> inputImageMask

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

Optional<String> fileId

File ID for the mask image.

Optional<String> imageUrl

Base64-encoded mask image.

Optional<Model> model

The image generation model to use. Default: `gpt-image-1`.

GPT\_IMAGE\_1("gpt-image-1")

GPT\_IMAGE\_1\_MINI("gpt-image-1-mini")

GPT\_IMAGE\_2("gpt-image-2")

GPT\_IMAGE\_2\_2026\_04\_21("gpt-image-2-2026-04-21")

GPT\_IMAGE\_1\_5("gpt-image-1.5")

CHATGPT\_IMAGE\_LATEST("chatgpt-image-latest")

Optional<Moderation> moderation

Moderation level for the generated image. Default: `auto`.

AUTO("auto")

LOW("low")

Optional<Long> outputCompression

Compression level for the output image. Default: 100.

minimum0

maximum100

Optional<OutputFormat> outputFormat

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

PNG("png")

WEBP("webp")

JPEG("jpeg")

Optional<Long> partialImages

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

Optional<Quality> quality

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

LOW("low")

MEDIUM("medium")

HIGH("high")

AUTO("auto")

Optional<Size> size

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

\_1024X1024("1024x1024")

\_1024X1536("1024x1536")

\_1536X1024("1536x1024")

AUTO("auto")

JsonValue;

JsonValue; type "local\_shell"constant"local\_shell"constant

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool:

A tool that allows the model to execute shell commands.

JsonValue; type "shell"constant"shell"constant

The type of the shell tool. Always `shell`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Environment> environment

class BetaContainerAuto:

JsonValue; type "container\_auto"constant"container\_auto"constant

Automatically creates a container for this request

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the container.

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

Optional<List<Skill>> skills

An optional list of skills referenced by id or inline data.

class BetaSkillReference:

String skillId

The ID of the referenced skill.

maxLength64

minLength1

JsonValue; type "skill\_reference"constant"skill\_reference"constant

References a skill created with the /v1/skills endpoint.

Optional<String> version

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class BetaInlineSkill:

String description

The description of the skill.

String name

The name of the skill.

[BetaInlineSkillSource](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) source

Inline skill payload

String data

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

JsonValue; mediaType "application/zip"constant"application/zip"constant

The media type of the inline skill payload. Must be `application/zip`.

JsonValue; type "base64"constant"base64"constant

The type of the inline skill source. Must be `base64`.

JsonValue; type "inline"constant"inline"constant

Defines an inline skill for this request.

class BetaLocalEnvironment:

JsonValue; type "local"constant"local"constant

Use a local computer environment.

Optional<List<[BetaLocalSkill](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))>> skills

An optional list of skills.

String description

The description of the skill.

String name

The name of the skill.

String path

The path to the directory containing the skill.

class BetaContainerReference:

String containerId

The ID of the referenced container.

JsonValue; type "container\_reference"constant"container\_reference"constant

References a container created with the /v1/containers endpoint

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<Format> format

The input format for the custom tool. Default is unconstrained text.

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

A grammar defined by the user.

String definition

The grammar definition.

Syntax syntax

The syntax of the grammar definition. One of `lark` or `regex`.

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

Grammar format. Always `grammar`.

class BetaNamespaceTool:

Groups function/custom tools under a shared namespace.

String description

A description of the namespace shown to the model.

minLength1

String name

The namespace name used in tool calls (for example, `crm`).

minLength1

List<Tool> tools

The function/custom tools available inside this namespace.

class Function:

String name

maxLength128

minLength1

JsonValue; type "function"constant"function"constant

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this function should be deferred and discovered via tool search.

Optional<String> description

Optional<OutputSchema> outputSchema

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

Optional<JsonValue> parameters

Optional<Boolean> strict

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<Format> format

The input format for the custom tool. Default is unconstrained text.

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

A grammar defined by the user.

String definition

The grammar definition.

Syntax syntax

The syntax of the grammar definition. One of `lark` or `regex`.

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

Grammar format. Always `grammar`.

JsonValue; type "namespace"constant"namespace"constant

The type of the tool. Always `namespace`.

class BetaToolSearchTool:

Hosted or BYOT tool search configuration for deferred tools.

JsonValue; type "tool\_search"constant"tool\_search"constant

The type of the tool. Always `tool_search`.

Optional<String> description

Description shown to the model for a client-executed tool search tool.

Optional<Execution> execution

Whether tool search is executed by the server or by the client.

SERVER("server")

CLIENT("client")

Optional<JsonValue> parameters

Parameter schema for a client-executed tool search tool.

class BetaWebSearchPreviewTool:

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

WEB\_SEARCH\_PREVIEW("web\_search\_preview")

WEB\_SEARCH\_PREVIEW\_2025\_03\_11("web\_search\_preview\_2025\_03\_11")

Optional<List<SearchContentType>> searchContentTypes

TEXT("text")

IMAGE("image")

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The user’s location.

JsonValue; type "approximate"constant"approximate"constant

The type of location approximation. Always `approximate`.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

class BetaApplyPatchTool:

Allows the assistant to create, delete, or update files using unified diffs.

JsonValue; type "apply\_patch"constant"apply\_patch"constant

The type of the tool. Always `apply_patch`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

JsonValue; type "tool\_search\_output"constant"tool\_search\_output"constant

The type of the item. Always `tool_search_output`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<String> createdBy

The identifier of the actor that created the item.

AdditionalTools

String id

The unique ID of the additional tools item.

Role role

The role that provided the additional tools.

UNKNOWN("unknown")

USER("user")

ASSISTANT("assistant")

SYSTEM("system")

CRITIC("critic")

DISCRIMINATOR("discriminator")

DEVELOPER("developer")

TOOL("tool")

List<[BetaTool](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))> tools

The additional tool definitions made available at this item.

class BetaFunctionTool:

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

String name

The name of the function to call.

Optional<Parameters> parameters

A JSON schema object describing the parameters of the function.

Optional<Boolean> strict

Whether strict parameter validation is enforced for this function tool.

JsonValue; type "function"constant"function"constant

The type of the function tool. Always `function`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this function is deferred and loaded via tool search.

Optional<String> description

A description of the function. Used by the model to determine whether or not to call the function.

Optional<OutputSchema> outputSchema

A JSON schema object describing the JSON value encoded in string outputs for this function.

class BetaFileSearchTool:

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

JsonValue; type "file\_search"constant"file\_search"constant

The type of the file search tool. Always `file_search`.

List<String> vectorStoreIds

The IDs of the vector stores to search.

Optional<Filters> filters

A filter to apply.

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

String

double

boolean

List<ComparisonFilterValueItem>

String

double

class CompoundFilter:

Combine multiple filters using `and` or `or`.

List<Filter> filters

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

String

double

boolean

List<ComparisonFilterValueItem>

String

double

JsonValue

Type type

Type of operation: `and` or `or`.

AND("and")

OR("or")

Optional<Long> maxNumResults

The maximum number of results to return. This number should be between 1 and 50 inclusive.

Optional<RankingOptions> rankingOptions

Ranking options for search.

Optional<HybridSearch> hybridSearch

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

double embeddingWeight

The weight of the embedding in the reciprocal ranking fusion.

double textWeight

The weight of the text in the reciprocal ranking fusion.

Optional<Ranker> ranker

The ranker to use for the file search.

AUTO("auto")

DEFAULT\_2024\_11\_15("default-2024-11-15")

Optional<Double> scoreThreshold

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class BetaComputerTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

JsonValue; type "computer"constant"computer"constant

The type of the computer tool. Always `computer`.

class BetaComputerUsePreviewTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

long displayHeight

The height of the computer display.

long displayWidth

The width of the computer display.

Environment environment

The type of computer environment to control.

WINDOWS("windows")

MAC("mac")

LINUX("linux")

UBUNTU("ubuntu")

BROWSER("browser")

JsonValue; type "computer\_use\_preview"constant"computer\_use\_preview"constant

The type of the computer use tool. Always `computer_use_preview`.

class BetaWebSearchTool:

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

WEB\_SEARCH("web\_search")

WEB\_SEARCH\_2025\_08\_26("web\_search\_2025\_08\_26")

Optional<Filters> filters

Filters for the search.

Optional<List<String>> allowedDomains

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The approximate location of the user.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

Optional<Type> type

The type of location approximation. Always `approximate`.

Mcp

String serverLabel

A label for this MCP server, used to identify it in tool calls.

JsonValue; type "mcp"constant"mcp"constant

The type of the MCP tool. Always `mcp`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<AllowedTools> allowedTools

List of allowed tool names or a filter object.

List<String>

class McpToolFilter:

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<String> authorization

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

Optional<ConnectorId> connectorId

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

CONNECTOR\_DROPBOX("connector\_dropbox")

CONNECTOR\_GMAIL("connector\_gmail")

CONNECTOR\_GOOGLECALENDAR("connector\_googlecalendar")

CONNECTOR\_GOOGLEDRIVE("connector\_googledrive")

CONNECTOR\_MICROSOFTTEAMS("connector\_microsoftteams")

CONNECTOR\_OUTLOOKCALENDAR("connector\_outlookcalendar")

CONNECTOR\_OUTLOOKEMAIL("connector\_outlookemail")

CONNECTOR\_SHAREPOINT("connector\_sharepoint")

Optional<Boolean> deferLoading

Whether this MCP tool is deferred and discovered via tool search.

Optional<Headers> headers

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

Optional<RequireApproval> requireApproval

Specify which of the MCP server’s tools require approval.

class McpToolApprovalFilter:

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

Optional<Always> always

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<Never> never

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

enum McpToolApprovalSetting:

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

ALWAYS("always")

NEVER("never")

Optional<String> serverDescription

Optional description of the MCP server, used to provide more context.

Optional<String> serverUrl

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

Optional<String> tunnelId

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter

Container container

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

String

class CodeInterpreterToolAuto:

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

JsonValue; type "auto"constant"auto"constant

Always `auto`.

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the code interpreter container.

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

JsonValue; type "code\_interpreter"constant"code\_interpreter"constant

The type of the code interpreter tool. Always `code_interpreter`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

JsonValue;

JsonValue; type "programmatic\_tool\_calling"constant"programmatic\_tool\_calling"constant

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration

JsonValue; type "image\_generation"constant"image\_generation"constant

The type of the image generation tool. Always `image_generation`.

Optional<Action> action

Whether to generate a new image or edit an existing image. Default: `auto`.

GENERATE("generate")

EDIT("edit")

AUTO("auto")

Optional<Background> background

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

TRANSPARENT("transparent")

OPAQUE("opaque")

AUTO("auto")

Optional<InputFidelity> inputFidelity

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

HIGH("high")

LOW("low")

Optional<InputImageMask> inputImageMask

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

Optional<String> fileId

File ID for the mask image.

Optional<String> imageUrl

Base64-encoded mask image.

Optional<Model> model

The image generation model to use. Default: `gpt-image-1`.

GPT\_IMAGE\_1("gpt-image-1")

GPT\_IMAGE\_1\_MINI("gpt-image-1-mini")

GPT\_IMAGE\_2("gpt-image-2")

GPT\_IMAGE\_2\_2026\_04\_21("gpt-image-2-2026-04-21")

GPT\_IMAGE\_1\_5("gpt-image-1.5")

CHATGPT\_IMAGE\_LATEST("chatgpt-image-latest")

Optional<Moderation> moderation

Moderation level for the generated image. Default: `auto`.

AUTO("auto")

LOW("low")

Optional<Long> outputCompression

Compression level for the output image. Default: 100.

minimum0

maximum100

Optional<OutputFormat> outputFormat

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

PNG("png")

WEBP("webp")

JPEG("jpeg")

Optional<Long> partialImages

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

Optional<Quality> quality

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

LOW("low")

MEDIUM("medium")

HIGH("high")

AUTO("auto")

Optional<Size> size

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

\_1024X1024("1024x1024")

\_1024X1536("1024x1536")

\_1536X1024("1536x1024")

AUTO("auto")

JsonValue;

JsonValue; type "local\_shell"constant"local\_shell"constant

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool:

A tool that allows the model to execute shell commands.

JsonValue; type "shell"constant"shell"constant

The type of the shell tool. Always `shell`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Environment> environment

class BetaContainerAuto:

JsonValue; type "container\_auto"constant"container\_auto"constant

Automatically creates a container for this request

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the container.

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

Optional<List<Skill>> skills

An optional list of skills referenced by id or inline data.

class BetaSkillReference:

String skillId

The ID of the referenced skill.

maxLength64

minLength1

JsonValue; type "skill\_reference"constant"skill\_reference"constant

References a skill created with the /v1/skills endpoint.

Optional<String> version

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class BetaInlineSkill:

String description

The description of the skill.

String name

The name of the skill.

[BetaInlineSkillSource](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) source

Inline skill payload

String data

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

JsonValue; mediaType "application/zip"constant"application/zip"constant

The media type of the inline skill payload. Must be `application/zip`.

JsonValue; type "base64"constant"base64"constant

The type of the inline skill source. Must be `base64`.

JsonValue; type "inline"constant"inline"constant

Defines an inline skill for this request.

class BetaLocalEnvironment:

JsonValue; type "local"constant"local"constant

Use a local computer environment.

Optional<List<[BetaLocalSkill](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))>> skills

An optional list of skills.

String description

The description of the skill.

String name

The name of the skill.

String path

The path to the directory containing the skill.

class BetaContainerReference:

String containerId

The ID of the referenced container.

JsonValue; type "container\_reference"constant"container\_reference"constant

References a container created with the /v1/containers endpoint

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<Format> format

The input format for the custom tool. Default is unconstrained text.

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

A grammar defined by the user.

String definition

The grammar definition.

Syntax syntax

The syntax of the grammar definition. One of `lark` or `regex`.

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

Grammar format. Always `grammar`.

class BetaNamespaceTool:

Groups function/custom tools under a shared namespace.

String description

A description of the namespace shown to the model.

minLength1

String name

The namespace name used in tool calls (for example, `crm`).

minLength1

List<Tool> tools

The function/custom tools available inside this namespace.

class Function:

String name

maxLength128

minLength1

JsonValue; type "function"constant"function"constant

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this function should be deferred and discovered via tool search.

Optional<String> description

Optional<OutputSchema> outputSchema

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

Optional<JsonValue> parameters

Optional<Boolean> strict

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<Format> format

The input format for the custom tool. Default is unconstrained text.

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

A grammar defined by the user.

String definition

The grammar definition.

Syntax syntax

The syntax of the grammar definition. One of `lark` or `regex`.

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

Grammar format. Always `grammar`.

JsonValue; type "namespace"constant"namespace"constant

The type of the tool. Always `namespace`.

class BetaToolSearchTool:

Hosted or BYOT tool search configuration for deferred tools.

JsonValue; type "tool\_search"constant"tool\_search"constant

The type of the tool. Always `tool_search`.

Optional<String> description

Description shown to the model for a client-executed tool search tool.

Optional<Execution> execution

Whether tool search is executed by the server or by the client.

SERVER("server")

CLIENT("client")

Optional<JsonValue> parameters

Parameter schema for a client-executed tool search tool.

class BetaWebSearchPreviewTool:

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

WEB\_SEARCH\_PREVIEW("web\_search\_preview")

WEB\_SEARCH\_PREVIEW\_2025\_03\_11("web\_search\_preview\_2025\_03\_11")

Optional<List<SearchContentType>> searchContentTypes

TEXT("text")

IMAGE("image")

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The user’s location.

JsonValue; type "approximate"constant"approximate"constant

The type of location approximation. Always `approximate`.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

class BetaApplyPatchTool:

Allows the assistant to create, delete, or update files using unified diffs.

JsonValue; type "apply\_patch"constant"apply\_patch"constant

The type of the tool. Always `apply_patch`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

JsonValue; type "additional\_tools"constant"additional\_tools"constant

The type of the item. Always `additional_tools`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseCompactionItem:

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

String id

The unique ID of the compaction item.

String encryptedContent

The encrypted content that was produced by compaction.

JsonValue; type "compaction"constant"compaction"constant

The type of the item. Always `compaction`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<String> createdBy

The identifier of the actor that created the item.

ImageGenerationCall

String id

The unique ID of the image generation call.

Optional<String> result

The generated image encoded in base64.

Status status

The status of the image generation call.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

GENERATING("generating")

FAILED("failed")

JsonValue; type "image\_generation\_call"constant"image\_generation\_call"constant

The type of the image generation call. Always `image_generation_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseCodeInterpreterToolCall:

A tool call to run code.

String id

The unique ID of the code interpreter tool call.

Optional<String> code

The code to run, or null if not available.

String containerId

The ID of the container used to run the code.

Optional<List<Output>> outputs

The outputs generated by the code interpreter, such as logs or images.
Can be null if no outputs are available.

class Logs:

The logs output from the code interpreter.

String logs

The logs output from the code interpreter.

JsonValue; type "logs"constant"logs"constant

The type of the output. Always `logs`.

class Image:

The image output from the code interpreter.

JsonValue; type "image"constant"image"constant

The type of the output. Always `image`.

String url

The URL of the image output from the code interpreter.

formaturi

Status status

The status of the code interpreter tool call. Valid values are `in_progress`, `completed`, `incomplete`, `interpreting`, and `failed`.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

INTERPRETING("interpreting")

FAILED("failed")

JsonValue; type "code\_interpreter\_call"constant"code\_interpreter\_call"constant

The type of the code interpreter tool call. Always `code_interpreter_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

LocalShellCall

String id

The unique ID of the local shell call.

Action action

Execute a shell command on the server.

List<String> command

The command to run.

Env env

Environment variables to set for the command.

JsonValue; type "exec"constant"exec"constant

The type of the local shell action. Always `exec`.

Optional<Long> timeoutMs

Optional timeout in milliseconds for the command.

Optional<String> user

Optional user to run the command as.

Optional<String> workingDirectory

Optional working directory to run the command in.

String callId

The unique ID of the local shell tool call generated by the model.

Status status

The status of the local shell call.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "local\_shell\_call"constant"local\_shell\_call"constant

The type of the local shell call. Always `local_shell_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

LocalShellCallOutput

String id

The unique ID of the local shell tool call generated by the model.

String output

A JSON string of the output of the local shell tool call.

JsonValue; type "local\_shell\_call\_output"constant"local\_shell\_call\_output"constant

The type of the local shell tool call output. Always `local_shell_call_output`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Status> status

The status of the item. One of `in_progress`, `completed`, or `incomplete`.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

class BetaResponseFunctionShellToolCall:

A tool call that executes one or more shell commands in a managed environment.

String id

The unique ID of the shell tool call. Populated when this item is returned via API.

Action action

The shell commands and limits that describe how to run the tool call.

List<String> commands

Optional<Long> maxOutputLength

Optional maximum number of characters to return from each command.

Optional<Long> timeoutMs

Optional timeout in milliseconds for the commands.

String callId

The unique ID of the shell tool call generated by the model.

Optional<Environment> environment

Represents the use of a local environment to perform shell actions.

class BetaResponseLocalEnvironment:

Represents the use of a local environment to perform shell actions.

JsonValue; type "local"constant"local"constant

The environment type. Always `local`.

class BetaResponseContainerReference:

Represents a container created with /v1/containers.

String containerId

JsonValue; type "container\_reference"constant"container\_reference"constant

The environment type. Always `container_reference`.

Status status

The status of the shell call. One of `in_progress`, `completed`, or `incomplete`.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "shell\_call"constant"shell\_call"constant

The type of the item. Always `shell_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

class Program:

String callerId

The call ID of the program item that produced this tool call.

JsonValue; type "program"constant"program"constant

Optional<String> createdBy

The ID of the entity that created this tool call.

class BetaResponseFunctionShellToolCallOutput:

The output of a shell tool call that was emitted.

String id

The unique ID of the shell call output. Populated when this item is returned via API.

String callId

The unique ID of the shell tool call generated by the model.

Optional<Long> maxOutputLength

The maximum length of the shell command output. This is generated by the model and should be passed back with the raw output.

List<Output> output

An array of shell call output contents

Outcome outcome

Represents either an exit outcome (with an exit code) or a timeout outcome for a shell call output chunk.

JsonValue;

JsonValue; type "timeout"constant"timeout"constant

The outcome type. Always `timeout`.

class Exit:

Indicates that the shell commands finished and returned an exit code.

long exitCode

Exit code from the shell process.

JsonValue; type "exit"constant"exit"constant

The outcome type. Always `exit`.

String stderr

The standard error output that was captured.

String stdout

The standard output that was captured.

Optional<String> createdBy

The identifier of the actor that created the item.

Status status

The status of the shell call output. One of `in_progress`, `completed`, or `incomplete`.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "shell\_call\_output"constant"shell\_call\_output"constant

The type of the shell call output. Always `shell_call_output`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

class Program:

String callerId

The call ID of the program item that produced this tool call.

JsonValue; type "program"constant"program"constant

Optional<String> createdBy

The identifier of the actor that created the item.

class BetaResponseApplyPatchToolCall:

A tool call that applies file diffs by creating, deleting, or updating files.

String id

The unique ID of the apply patch tool call. Populated when this item is returned via API.

String callId

The unique ID of the apply patch tool call generated by the model.

Operation operation

One of the create\_file, delete\_file, or update\_file operations applied via apply\_patch.

class CreateFile:

Instruction describing how to create a file via the apply\_patch tool.

String diff

Diff to apply.

String path

Path of the file to create.

JsonValue; type "create\_file"constant"create\_file"constant

Create a new file with the provided diff.

class DeleteFile:

Instruction describing how to delete a file via the apply\_patch tool.

String path

Path of the file to delete.

JsonValue; type "delete\_file"constant"delete\_file"constant

Delete the specified file.

class UpdateFile:

Instruction describing how to update a file via the apply\_patch tool.

String diff

Diff to apply.

String path

Path of the file to update.

JsonValue; type "update\_file"constant"update\_file"constant

Update an existing file with the provided diff.

Status status

The status of the apply patch tool call. One of `in_progress` or `completed`.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

JsonValue; type "apply\_patch\_call"constant"apply\_patch\_call"constant

The type of the item. Always `apply_patch_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

class Program:

String callerId

The call ID of the program item that produced this tool call.

JsonValue; type "program"constant"program"constant

Optional<String> createdBy

The ID of the entity that created this tool call.

class BetaResponseApplyPatchToolCallOutput:

The output emitted by an apply patch tool call.

String id

The unique ID of the apply patch tool call output. Populated when this item is returned via API.

String callId

The unique ID of the apply patch tool call generated by the model.

Status status

The status of the apply patch tool call output. One of `completed` or `failed`.

COMPLETED("completed")

FAILED("failed")

JsonValue; type "apply\_patch\_call\_output"constant"apply\_patch\_call\_output"constant

The type of the item. Always `apply_patch_call_output`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

class Program:

String callerId

The call ID of the program item that produced this tool call.

JsonValue; type "program"constant"program"constant

Optional<String> createdBy

The ID of the entity that created this tool call output.

Optional<String> output

Optional textual output returned by the apply patch tool.

McpCall

String id

The unique ID of the tool call.

String arguments

A JSON string of the arguments passed to the tool.

String name

The name of the tool that was run.

String serverLabel

The label of the MCP server running the tool.

JsonValue; type "mcp\_call"constant"mcp\_call"constant

The type of the item. Always `mcp_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<String> approvalRequestId

Unique identifier for the MCP tool call approval request.
Include this value in a subsequent `mcp_approval_response` input to approve or reject the corresponding tool call.

Optional<String> error

The error from the tool call, if any.

Optional<String> output

The output from the tool call.

Optional<Status> status

The status of the tool call. One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

CALLING("calling")

FAILED("failed")

McpListTools

String id

The unique ID of the list.

String serverLabel

The label of the MCP server.

List<Tool> tools

The tools available on the server.

JsonValue inputSchema

The JSON schema describing the tool’s input.

String name

The name of the tool.

Optional<JsonValue> annotations

Additional annotations about the tool.

Optional<String> description

The description of the tool.

JsonValue; type "mcp\_list\_tools"constant"mcp\_list\_tools"constant

The type of the item. Always `mcp_list_tools`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<String> error

Error message if the server could not list tools.

McpApprovalRequest

String id

The unique ID of the approval request.

String arguments

A JSON string of arguments for the tool.

String name

The name of the tool to run.

String serverLabel

The label of the MCP server making the request.

JsonValue; type "mcp\_approval\_request"constant"mcp\_approval\_request"constant

The type of the item. Always `mcp_approval_request`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

McpApprovalResponse

String id

The unique ID of the approval response

String approvalRequestId

The ID of the approval request being answered.

boolean approve

Whether the request was approved.

JsonValue; type "mcp\_approval\_response"constant"mcp\_approval\_response"constant

The type of the item. Always `mcp_approval_response`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<String> reason

Optional reason for the decision.

class BetaResponseCustomToolCall:

A call to a custom tool created by the model.

String callId

An identifier used to map this custom tool call to a tool call output.

String input

The input for the custom tool call generated by the model.

String name

The name of the custom tool being called.

JsonValue; type "custom\_tool\_call"constant"custom\_tool\_call"constant

The type of the custom tool call. Always `custom_tool_call`.

Optional<String> id

The unique ID of the custom tool call in the OpenAI platform.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

class Program:

String callerId

The call ID of the program item that produced this tool call.

JsonValue; type "program"constant"program"constant

Optional<String> namespace

The namespace of the custom tool being called.

class BetaResponseCustomToolCallOutputItem:

The output of a custom tool call from your code, being sent back to the model.

String id

The unique ID of the custom tool call output item.

Status status

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

Optional<String> createdBy

The identifier of the actor that created the item.

boolean parallelToolCalls

Whether to allow the model to run tool calls in parallel.

Optional<Double> temperature

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
We generally recommend altering this or `top_p` but not both.

minimum0

maximum2

ToolChoice toolChoice

How the model should select which tool (or tools) to use when generating
a response. See the `tools` parameter to see how to specify which tools
the model can call.

enum BetaToolChoiceOptions:

Controls which (if any) tool is called by the model.

`none` means the model will not call any tool and instead generates a message.

`auto` means the model can pick between generating a message or calling one or
more tools.

`required` means the model must call one or more tools.

NONE("none")

AUTO("auto")

REQUIRED("required")

class BetaToolChoiceAllowed:

Constrains the tools available to the model to a pre-defined set.

Mode mode

Constrains the tools available to the model to a pre-defined set.

`auto` allows the model to pick from among the allowed tools and generate a
message.

`required` requires the model to call one or more of the allowed tools.

AUTO("auto")

REQUIRED("required")

List<Tool> tools

A list of tool definitions that the model should be allowed to call.

For the Responses API, the list of tool definitions might look like:

[
  { "type": "function", "name": "get_weather" },
  { "type": "mcp", "server_label": "deepwiki" },
  { "type": "image_generation" }
]

JsonValue; type "allowed\_tools"constant"allowed\_tools"constant

Allowed tool configuration type. Always `allowed_tools`.

class BetaToolChoiceTypes:

Indicates that the model should use a built-in tool to generate a response.
[Learn more about built-in tools](https://platform.openai.com/docs/guides/tools).

Type type

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

FILE\_SEARCH("file\_search")

WEB\_SEARCH\_PREVIEW("web\_search\_preview")

COMPUTER("computer")

COMPUTER\_USE\_PREVIEW("computer\_use\_preview")

COMPUTER\_USE("computer\_use")

WEB\_SEARCH\_PREVIEW\_2025\_03\_11("web\_search\_preview\_2025\_03\_11")

IMAGE\_GENERATION("image\_generation")

CODE\_INTERPRETER("code\_interpreter")

class BetaToolChoiceFunction:

Use this option to force the model to call a specific function.

String name

The name of the function to call.

JsonValue; type "function"constant"function"constant

For function calling, the type is always `function`.

class BetaToolChoiceMcp:

Use this option to force the model to call a specific tool on a remote MCP server.

String serverLabel

The label of the MCP server to use.

JsonValue; type "mcp"constant"mcp"constant

For MCP tools, the type is always `mcp`.

Optional<String> name

The name of the tool to call on the server.

class BetaToolChoiceCustom:

Use this option to force the model to call a specific custom tool.

String name

The name of the custom tool to call.

JsonValue; type "custom"constant"custom"constant

For custom tool calling, the type is always `custom`.

JsonValue;

JsonValue; type "programmatic\_tool\_calling"constant"programmatic\_tool\_calling"constant

The tool to call. Always `programmatic_tool_calling`.

class BetaToolChoiceApplyPatch:

Forces the model to call the apply\_patch tool when executing a tool call.

JsonValue; type "apply\_patch"constant"apply\_patch"constant

The tool to call. Always `apply_patch`.

class BetaToolChoiceShell:

Forces the model to call the shell tool when a tool call is required.

JsonValue; type "shell"constant"shell"constant

The tool to call. Always `shell`.

List<[BetaTool](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))> tools

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

class BetaFunctionTool:

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

String name

The name of the function to call.

Optional<Parameters> parameters

A JSON schema object describing the parameters of the function.

Optional<Boolean> strict

Whether strict parameter validation is enforced for this function tool.

JsonValue; type "function"constant"function"constant

The type of the function tool. Always `function`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this function is deferred and loaded via tool search.

Optional<String> description

A description of the function. Used by the model to determine whether or not to call the function.

Optional<OutputSchema> outputSchema

A JSON schema object describing the JSON value encoded in string outputs for this function.

class BetaFileSearchTool:

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

JsonValue; type "file\_search"constant"file\_search"constant

The type of the file search tool. Always `file_search`.

List<String> vectorStoreIds

The IDs of the vector stores to search.

Optional<Filters> filters

A filter to apply.

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

String

double

boolean

List<ComparisonFilterValueItem>

String

double

class CompoundFilter:

Combine multiple filters using `and` or `or`.

List<Filter> filters

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

String

double

boolean

List<ComparisonFilterValueItem>

String

double

JsonValue

Type type

Type of operation: `and` or `or`.

AND("and")

OR("or")

Optional<Long> maxNumResults

The maximum number of results to return. This number should be between 1 and 50 inclusive.

Optional<RankingOptions> rankingOptions

Ranking options for search.

Optional<HybridSearch> hybridSearch

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

double embeddingWeight

The weight of the embedding in the reciprocal ranking fusion.

double textWeight

The weight of the text in the reciprocal ranking fusion.

Optional<Ranker> ranker

The ranker to use for the file search.

AUTO("auto")

DEFAULT\_2024\_11\_15("default-2024-11-15")

Optional<Double> scoreThreshold

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class BetaComputerTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

JsonValue; type "computer"constant"computer"constant

The type of the computer tool. Always `computer`.

class BetaComputerUsePreviewTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

long displayHeight

The height of the computer display.

long displayWidth

The width of the computer display.

Environment environment

The type of computer environment to control.

WINDOWS("windows")

MAC("mac")

LINUX("linux")

UBUNTU("ubuntu")

BROWSER("browser")

JsonValue; type "computer\_use\_preview"constant"computer\_use\_preview"constant

The type of the computer use tool. Always `computer_use_preview`.

class BetaWebSearchTool:

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

WEB\_SEARCH("web\_search")

WEB\_SEARCH\_2025\_08\_26("web\_search\_2025\_08\_26")

Optional<Filters> filters

Filters for the search.

Optional<List<String>> allowedDomains

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The approximate location of the user.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

Optional<Type> type

The type of location approximation. Always `approximate`.

Mcp

String serverLabel

A label for this MCP server, used to identify it in tool calls.

JsonValue; type "mcp"constant"mcp"constant

The type of the MCP tool. Always `mcp`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<AllowedTools> allowedTools

List of allowed tool names or a filter object.

List<String>

class McpToolFilter:

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<String> authorization

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

Optional<ConnectorId> connectorId

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

CONNECTOR\_DROPBOX("connector\_dropbox")

CONNECTOR\_GMAIL("connector\_gmail")

CONNECTOR\_GOOGLECALENDAR("connector\_googlecalendar")

CONNECTOR\_GOOGLEDRIVE("connector\_googledrive")

CONNECTOR\_MICROSOFTTEAMS("connector\_microsoftteams")

CONNECTOR\_OUTLOOKCALENDAR("connector\_outlookcalendar")

CONNECTOR\_OUTLOOKEMAIL("connector\_outlookemail")

CONNECTOR\_SHAREPOINT("connector\_sharepoint")

Optional<Boolean> deferLoading

Whether this MCP tool is deferred and discovered via tool search.

Optional<Headers> headers

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

Optional<RequireApproval> requireApproval

Specify which of the MCP server’s tools require approval.

class McpToolApprovalFilter:

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

Optional<Always> always

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<Never> never

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

enum McpToolApprovalSetting:

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

ALWAYS("always")

NEVER("never")

Optional<String> serverDescription

Optional description of the MCP server, used to provide more context.

Optional<String> serverUrl

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

Optional<String> tunnelId

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter

Container container

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

String

class CodeInterpreterToolAuto:

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

JsonValue; type "auto"constant"auto"constant

Always `auto`.

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the code interpreter container.

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

JsonValue; type "code\_interpreter"constant"code\_interpreter"constant

The type of the code interpreter tool. Always `code_interpreter`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

JsonValue;

JsonValue; type "programmatic\_tool\_calling"constant"programmatic\_tool\_calling"constant

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration

JsonValue; type "image\_generation"constant"image\_generation"constant

The type of the image generation tool. Always `image_generation`.

Optional<Action> action

Whether to generate a new image or edit an existing image. Default: `auto`.

GENERATE("generate")

EDIT("edit")

AUTO("auto")

Optional<Background> background

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

TRANSPARENT("transparent")

OPAQUE("opaque")

AUTO("auto")

Optional<InputFidelity> inputFidelity

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

HIGH("high")

LOW("low")

Optional<InputImageMask> inputImageMask

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

Optional<String> fileId

File ID for the mask image.

Optional<String> imageUrl

Base64-encoded mask image.

Optional<Model> model

The image generation model to use. Default: `gpt-image-1`.

GPT\_IMAGE\_1("gpt-image-1")

GPT\_IMAGE\_1\_MINI("gpt-image-1-mini")

GPT\_IMAGE\_2("gpt-image-2")

GPT\_IMAGE\_2\_2026\_04\_21("gpt-image-2-2026-04-21")

GPT\_IMAGE\_1\_5("gpt-image-1.5")

CHATGPT\_IMAGE\_LATEST("chatgpt-image-latest")

Optional<Moderation> moderation

Moderation level for the generated image. Default: `auto`.

AUTO("auto")

LOW("low")

Optional<Long> outputCompression

Compression level for the output image. Default: 100.

minimum0

maximum100

Optional<OutputFormat> outputFormat

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

PNG("png")

WEBP("webp")

JPEG("jpeg")

Optional<Long> partialImages

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

Optional<Quality> quality

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

LOW("low")

MEDIUM("medium")

HIGH("high")

AUTO("auto")

Optional<Size> size

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

\_1024X1024("1024x1024")

\_1024X1536("1024x1536")

\_1536X1024("1536x1024")

AUTO("auto")

JsonValue;

JsonValue; type "local\_shell"constant"local\_shell"constant

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool:

A tool that allows the model to execute shell commands.

JsonValue; type "shell"constant"shell"constant

The type of the shell tool. Always `shell`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Environment> environment

class BetaContainerAuto:

JsonValue; type "container\_auto"constant"container\_auto"constant

Automatically creates a container for this request

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the container.

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

Optional<List<Skill>> skills

An optional list of skills referenced by id or inline data.

class BetaSkillReference:

String skillId

The ID of the referenced skill.

maxLength64

minLength1

JsonValue; type "skill\_reference"constant"skill\_reference"constant

References a skill created with the /v1/skills endpoint.

Optional<String> version

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class BetaInlineSkill:

String description

The description of the skill.

String name

The name of the skill.

[BetaInlineSkillSource](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) source

Inline skill payload

String data

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

JsonValue; mediaType "application/zip"constant"application/zip"constant

The media type of the inline skill payload. Must be `application/zip`.

JsonValue; type "base64"constant"base64"constant

The type of the inline skill source. Must be `base64`.

JsonValue; type "inline"constant"inline"constant

Defines an inline skill for this request.

class BetaLocalEnvironment:

JsonValue; type "local"constant"local"constant

Use a local computer environment.

Optional<List<[BetaLocalSkill](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))>> skills

An optional list of skills.

String description

The description of the skill.

String name

The name of the skill.

String path

The path to the directory containing the skill.

class BetaContainerReference:

String containerId

The ID of the referenced container.

JsonValue; type "container\_reference"constant"container\_reference"constant

References a container created with the /v1/containers endpoint

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<Format> format

The input format for the custom tool. Default is unconstrained text.

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

A grammar defined by the user.

String definition

The grammar definition.

Syntax syntax

The syntax of the grammar definition. One of `lark` or `regex`.

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

Grammar format. Always `grammar`.

class BetaNamespaceTool:

Groups function/custom tools under a shared namespace.

String description

A description of the namespace shown to the model.

minLength1

String name

The namespace name used in tool calls (for example, `crm`).

minLength1

List<Tool> tools

The function/custom tools available inside this namespace.

class Function:

String name

maxLength128

minLength1

JsonValue; type "function"constant"function"constant

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this function should be deferred and discovered via tool search.

Optional<String> description

Optional<OutputSchema> outputSchema

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

Optional<JsonValue> parameters

Optional<Boolean> strict

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<Format> format

The input format for the custom tool. Default is unconstrained text.

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

A grammar defined by the user.

String definition

The grammar definition.

Syntax syntax

The syntax of the grammar definition. One of `lark` or `regex`.

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

Grammar format. Always `grammar`.

JsonValue; type "namespace"constant"namespace"constant

The type of the tool. Always `namespace`.

class BetaToolSearchTool:

Hosted or BYOT tool search configuration for deferred tools.

JsonValue; type "tool\_search"constant"tool\_search"constant

The type of the tool. Always `tool_search`.

Optional<String> description

Description shown to the model for a client-executed tool search tool.

Optional<Execution> execution

Whether tool search is executed by the server or by the client.

SERVER("server")

CLIENT("client")

Optional<JsonValue> parameters

Parameter schema for a client-executed tool search tool.

class BetaWebSearchPreviewTool:

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

WEB\_SEARCH\_PREVIEW("web\_search\_preview")

WEB\_SEARCH\_PREVIEW\_2025\_03\_11("web\_search\_preview\_2025\_03\_11")

Optional<List<SearchContentType>> searchContentTypes

TEXT("text")

IMAGE("image")

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The user’s location.

JsonValue; type "approximate"constant"approximate"constant

The type of location approximation. Always `approximate`.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

class BetaApplyPatchTool:

Allows the assistant to create, delete, or update files using unified diffs.

JsonValue; type "apply\_patch"constant"apply\_patch"constant

The type of the tool. Always `apply_patch`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Double> topP

An alternative to sampling with temperature, called nucleus sampling,
where the model considers the results of the tokens with top\_p probability
mass. So 0.1 means only the tokens comprising the top 10% probability mass
are considered.

We generally recommend altering this or `temperature` but not both.

minimum0

maximum1

Optional<Boolean> background

Whether to run the model response in the background.
[Learn more](https://platform.openai.com/docs/guides/background).

Optional<Double> completedAt

Unix timestamp (in seconds) of when this Response was completed.
Only present when the status is `completed`.

formatunixtime

Optional<Conversation> conversation

The conversation that this response belonged to. Input items and output items from this response were automatically added to this conversation.

String id

The unique ID of the conversation that this response was associated with.

Optional<Long> maxOutputTokens

An upper bound for the number of tokens that can be generated for a response, including visible output tokens and [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

Optional<Long> maxToolCalls

The maximum number of total calls to built-in tools that can be processed in a response. This maximum number applies across all built-in tool calls, not per individual tool. Any further attempts to call a tool by the model will be ignored.

Optional<Moderation> moderation

Moderation results for the response input and output, if moderated completions were requested.

Input input

Moderation for the response input.

class ModerationResult:

A moderation result produced for the response input or output.

Categories categories

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

CategoryAppliedInputTypes categoryAppliedInputTypes

Which modalities of input are reflected by the score for each category.

TEXT("text")

IMAGE("image")

CategoryScores categoryScores

A dictionary of moderation categories to scores.

boolean flagged

A boolean indicating whether the content was flagged by any category.

String model

The moderation model that produced this result.

JsonValue; type "moderation\_result"constant"moderation\_result"constant

The object type, which was always `moderation_result` for successful moderation results.

class Error:

An error produced while attempting moderation for the response input or output.

String code

The error code.

String message

The error message.

JsonValue; type "error"constant"error"constant

The object type, which was always `error` for moderation failures.

Output output

Moderation for the response output.

class ModerationResult:

A moderation result produced for the response input or output.

Categories categories

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

CategoryAppliedInputTypes categoryAppliedInputTypes

Which modalities of input are reflected by the score for each category.

TEXT("text")

IMAGE("image")

CategoryScores categoryScores

A dictionary of moderation categories to scores.

boolean flagged

A boolean indicating whether the content was flagged by any category.

String model

The moderation model that produced this result.

JsonValue; type "moderation\_result"constant"moderation\_result"constant

The object type, which was always `moderation_result` for successful moderation results.

class Error:

An error produced while attempting moderation for the response input or output.

String code

The error code.

String message

The error message.

JsonValue; type "error"constant"error"constant

The object type, which was always `error` for moderation failures.

Optional<String> previousResponseId

The unique ID of the previous response to the model. Use this to
create multi-turn conversations. Learn more about
[conversation state](https://platform.openai.com/docs/guides/conversation-state). Cannot be used in conjunction with `conversation`.

Optional<[BetaResponsePrompt](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_prompt%20%3E%20(schema))> prompt

Reference to a prompt template and its variables.
[Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

String id

The unique identifier of the prompt template to use.

Optional<Variables> variables

Optional map of values to substitute in for variables in your
prompt. The substitution values can either be strings, or other
Response input types like images or files.

String

class BetaResponseInputText:

A text input to the model.

String text

The text input to the model.

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputImage:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail detail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

JsonValue; type "input\_image"constant"input\_image"constant

The type of the input item. Always `input_image`.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> imageUrl

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile:

A file input to the model.

JsonValue; type "input\_file"constant"input\_file"constant

The type of the input item. Always `input_file`.

Optional<Detail> detail

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

AUTO("auto")

LOW("low")

HIGH("high")

Optional<String> fileData

The content of the file to be sent to the model.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> fileUrl

The URL of the file to be sent to the model.

formaturi

Optional<String> filename

The name of the file to be sent to the model.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

Optional<String> version

Optional version of the prompt template.

Optional<String> promptCacheKey

Used by OpenAI to cache responses for similar requests to optimize your cache hit rates. Replaces the `user` field. [Learn more](https://platform.openai.com/docs/guides/prompt-caching).

Optional<PromptCacheOptions> promptCacheOptions

The prompt-caching options that were applied to the response. Supported for `gpt-5.6` and later models.

Mode mode

Whether implicit prompt-cache breakpoints were enabled.

IMPLICIT("implicit")

EXPLICIT("explicit")

Ttl ttl

The minimum lifetime applied to each cache breakpoint.

DeprecatedOptional<PromptCacheRetention> promptCacheRetention

Deprecated. Use `prompt_cache_options.ttl` instead.

The retention policy for the prompt cache. Set to `24h` to enable extended prompt caching, which keeps cached prefixes active for longer, up to a maximum of 24 hours. [Learn more](https://platform.openai.com/docs/guides/prompt-caching#prompt-cache-retention).
This field expresses a maximum retention policy, while
`prompt_cache_options.ttl` expresses a minimum cache lifetime. The two
fields are independent and do not interact.
For `gpt-5.5`, `gpt-5.5-pro`, and future models, only `24h` is supported.

For older models that support both `in_memory` and `24h`, the default depends on your organization’s data retention policy:

* Organizations without ZDR enabled default to `24h`.
* Organizations with ZDR enabled default to `in_memory` when `prompt_cache_retention` is not specified.

IN\_MEMORY("in\_memory")

\_24H("24h")

Optional<Reasoning> reasoning

**gpt-5 and o-series models only**

Configuration options for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).

Optional<Context> context

Controls which reasoning items are rendered back to the model on later turns.
If omitted or set to `auto`, the model determines the context mode. The
`gpt-5.6` model family defaults to `all_turns`; earlier models default to
`current_turn`.

When returned on a response, this is the effective reasoning context mode
used for the response.

AUTO("auto")

CURRENT\_TURN("current\_turn")

ALL\_TURNS("all\_turns")

Optional<Effort> effort

Constrains effort on reasoning for reasoning models. Currently supported
values are `none`, `minimal`, `low`, `medium`, `high`, `xhigh`, and `max`.
Reducing reasoning effort can result in faster responses and fewer tokens
used on reasoning in a response. Not all reasoning models support every
value. See the
[reasoning guide](https://platform.openai.com/docs/guides/reasoning)
for model-specific support.

NONE("none")

MINIMAL("minimal")

LOW("low")

MEDIUM("medium")

HIGH("high")

XHIGH("xhigh")

MAX("max")

DeprecatedOptional<GenerateSummary> generateSummary

**Deprecated:** use `summary` instead.

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

AUTO("auto")

CONCISE("concise")

DETAILED("detailed")

Optional<Mode> mode

Controls the reasoning execution mode for the request.

When returned on a response, this is the effective execution mode.

STANDARD("standard")

PRO("pro")

Optional<Summary> summary

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

`concise` is supported for `computer-use-preview` models and all reasoning models after `gpt-5`.

AUTO("auto")

CONCISE("concise")

DETAILED("detailed")

Optional<String> safetyIdentifier

A stable identifier used to help detect users of your application that may be violating OpenAI’s usage policies.
The IDs should be a string that uniquely identifies each user, with a maximum length of 64 characters. We recommend hashing their username or email address, in order to avoid sending us any identifying information. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

maxLength64

Optional<ServiceTier> serviceTier

Specifies the processing type used for serving the request.

* If set to ‘auto’, then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use ‘default’.
* If set to ‘default’, then the request will be processed with the standard pricing and performance for the selected model.
* If set to ‘[flex](https://platform.openai.com/docs/guides/flex-processing)’ or ‘[priority](https://openai.com/api-priority-processing/)’, then the request will be processed with the corresponding service tier.
* When not set, the default behavior is ‘auto’.

When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.

AUTO("auto")

DEFAULT("default")

FLEX("flex")

SCALE("scale")

PRIORITY("priority")

Optional<[BetaResponseStatus](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_status%20%3E%20(schema))> status

The status of the response generation. One of `completed`, `failed`,
`in_progress`, `cancelled`, `queued`, or `incomplete`.

COMPLETED("completed")

FAILED("failed")

IN\_PROGRESS("in\_progress")

CANCELLED("cancelled")

QUEUED("queued")

INCOMPLETE("incomplete")

Optional<[BetaResponseTextConfig](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_text_config%20%3E%20(schema))> text

Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:

* [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
* [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

Optional<[BetaResponseFormatTextConfig](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_format_text_config%20%3E%20(schema))> format

An object specifying the format that the model must output.

Configuring `{ "type": "json_schema" }` enables Structured Outputs,
which ensures the model will match your supplied JSON schema. Learn more in the
[Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

The default format is `{ "type": "text" }` with no additional options.

**Not recommended for gpt-4o and newer models:**

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

JsonValue;

JsonValue; type "text"constant"text"constant

The type of response format being defined. Always `text`.

class BetaResponseFormatTextJsonSchemaConfig:

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

String name

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

Schema schema

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

JsonValue; type "json\_schema"constant"json\_schema"constant

The type of response format being defined. Always `json_schema`.

Optional<String> description

A description of what the response format is for, used by the model to
determine how to respond in the format.

Optional<Boolean> strict

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

JsonValue;

JsonValue; type "json\_object"constant"json\_object"constant

The type of response format being defined. Always `json_object`.

Optional<Verbosity> verbosity

Constrains the verbosity of the model’s response. Lower values will result in
more concise responses, while higher values will result in more verbose responses.
Currently supported values are `low`, `medium`, and `high`. The default is
`medium`.

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<Long> topLogprobs

An integer between 0 and 20 specifying the maximum number of most likely
tokens to return at each token position, each with an associated log
probability. In some cases, the number of returned tokens may be fewer than
requested.

minimum0

maximum20

Optional<Truncation> truncation

The truncation strategy to use for the model response.

* `auto`: If the input to this Response exceeds
  the model’s context window size, the model will truncate the
  response to fit the context window by dropping items from the beginning of the conversation.
* `disabled` (default): If the input size will exceed the context window
  size for a model, the request will fail with a 400 error.

AUTO("auto")

DISABLED("disabled")

Optional<[BetaResponseUsage](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_usage%20%3E%20(schema))> usage

Represents token usage details including input tokens, output tokens,
a breakdown of output tokens, and the total tokens used.

long inputTokens

The number of input tokens.

InputTokensDetails inputTokensDetails

A detailed breakdown of the input tokens.

long cacheWriteTokens

The number of input tokens that were written to the cache.

long cachedTokens

The number of tokens that were retrieved from the cache.
[More on prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

long outputTokens

The number of output tokens.

OutputTokensDetails outputTokensDetails

A detailed breakdown of the output tokens.

long reasoningTokens

The number of reasoning tokens.

long totalTokens

The total number of tokens used.

DeprecatedOptional<String> user

This field is being replaced by `safety_identifier` and `prompt_cache_key`. Use `prompt_cache_key` instead to maintain caching optimizations.
A stable identifier for your end-users.
Used to boost cache hit rates by better bucketing similar requests and to help OpenAI detect and prevent abuse. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.in\_progress"constant"response.in\_progress"constant

The type of the event. Always `response.in_progress`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseFailedEvent:

An event that is emitted when a response fails.

[BetaResponse](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema)) response

The response that failed.

String id

Unique identifier for this Response.

double createdAt

Unix timestamp (in seconds) of when this Response was created.

formatunixtime

Optional<[BetaResponseError](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_error%20%3E%20(schema))> error

An error object returned when the model fails to generate a Response.

Code code

The error code for the response.

SERVER\_ERROR("server\_error")

RATE\_LIMIT\_EXCEEDED("rate\_limit\_exceeded")

INVALID\_PROMPT("invalid\_prompt")

DATA\_RESIDENCY\_MISMATCH("data\_residency\_mismatch")

BIO\_POLICY("bio\_policy")

VECTOR\_STORE\_TIMEOUT("vector\_store\_timeout")

INVALID\_IMAGE("invalid\_image")

INVALID\_IMAGE\_FORMAT("invalid\_image\_format")

INVALID\_BASE64\_IMAGE("invalid\_base64\_image")

INVALID\_IMAGE\_URL("invalid\_image\_url")

IMAGE\_TOO\_LARGE("image\_too\_large")

IMAGE\_TOO\_SMALL("image\_too\_small")

IMAGE\_PARSE\_ERROR("image\_parse\_error")

IMAGE\_CONTENT\_POLICY\_VIOLATION("image\_content\_policy\_violation")

INVALID\_IMAGE\_MODE("invalid\_image\_mode")

IMAGE\_FILE\_TOO\_LARGE("image\_file\_too\_large")

UNSUPPORTED\_IMAGE\_MEDIA\_TYPE("unsupported\_image\_media\_type")

EMPTY\_IMAGE\_FILE("empty\_image\_file")

FAILED\_TO\_DOWNLOAD\_IMAGE("failed\_to\_download\_image")

IMAGE\_FILE\_NOT\_FOUND("image\_file\_not\_found")

String message

A human-readable description of the error.

Optional<IncompleteDetails> incompleteDetails

Details about why the response is incomplete.

Optional<Reason> reason

The reason why the response is incomplete.

MAX\_OUTPUT\_TOKENS("max\_output\_tokens")

CONTENT\_FILTER("content\_filter")

Optional<Instructions> instructions

A system (or developer) message inserted into the model’s context.

When using along with `previous_response_id`, the instructions from a previous
response will not be carried over to the next response. This makes it simple
to swap out system (or developer) messages in new responses.

String

List<[BetaResponseInputItem](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_item%20%3E%20(schema))>

class BetaEasyInputMessage:

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

Content content

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

String

List<[BetaResponseInputContent](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_content%20%3E%20(schema))>

class BetaResponseInputText:

A text input to the model.

String text

The text input to the model.

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputImage:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail detail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

JsonValue; type "input\_image"constant"input\_image"constant

The type of the input item. Always `input_image`.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> imageUrl

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile:

A file input to the model.

JsonValue; type "input\_file"constant"input\_file"constant

The type of the input item. Always `input_file`.

Optional<Detail> detail

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

AUTO("auto")

LOW("low")

HIGH("high")

Optional<String> fileData

The content of the file to be sent to the model.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> fileUrl

The URL of the file to be sent to the model.

formaturi

Optional<String> filename

The name of the file to be sent to the model.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

Role role

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

USER("user")

ASSISTANT("assistant")

SYSTEM("system")

DEVELOPER("developer")

Optional<Phase> phase

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

COMMENTARY("commentary")

FINAL\_ANSWER("final\_answer")

Optional<Type> type

The type of the message input. Always `message`.

Message

List<[BetaResponseInputContent](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_content%20%3E%20(schema))> content

A list of one or many input items to the model, containing different content
types.

class BetaResponseInputText:

A text input to the model.

String text

The text input to the model.

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputImage:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail detail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

JsonValue; type "input\_image"constant"input\_image"constant

The type of the input item. Always `input_image`.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> imageUrl

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile:

A file input to the model.

JsonValue; type "input\_file"constant"input\_file"constant

The type of the input item. Always `input_file`.

Optional<Detail> detail

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

AUTO("auto")

LOW("low")

HIGH("high")

Optional<String> fileData

The content of the file to be sent to the model.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> fileUrl

The URL of the file to be sent to the model.

formaturi

Optional<String> filename

The name of the file to be sent to the model.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

Role role

The role of the message input. One of `user`, `system`, or `developer`.

USER("user")

SYSTEM("system")

DEVELOPER("developer")

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Status> status

The status of item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

Optional<Type> type

The type of the message input. Always set to `message`.

class BetaResponseOutputMessage:

An output message from the model.

String id

The unique ID of the output message.

List<Content> content

The content of the output message.

class BetaResponseOutputText:

A text output from the model.

List<Annotation> annotations

The annotations of the text output.

class FileCitation:

A citation to a file.

String fileId

The ID of the file.

String filename

The filename of the file cited.

long index

The index of the file in the list of files.

JsonValue; type "file\_citation"constant"file\_citation"constant

The type of the file citation. Always `file_citation`.

class UrlCitation:

A citation for a web resource used to generate a model response.

long endIndex

The index of the last character of the URL citation in the message.

long startIndex

The index of the first character of the URL citation in the message.

String title

The title of the web resource.

JsonValue; type "url\_citation"constant"url\_citation"constant

The type of the URL citation. Always `url_citation`.

String url

The URL of the web resource.

formaturi

class ContainerFileCitation:

A citation for a container file used to generate a model response.

String containerId

The ID of the container file.

long endIndex

The index of the last character of the container file citation in the message.

String fileId

The ID of the file.

String filename

The filename of the container file cited.

long startIndex

The index of the first character of the container file citation in the message.

JsonValue; type "container\_file\_citation"constant"container\_file\_citation"constant

The type of the container file citation. Always `container_file_citation`.

class FilePath:

A path to a file.

String fileId

The ID of the file.

long index

The index of the file in the list of files.

JsonValue; type "file\_path"constant"file\_path"constant

The type of the file path. Always `file_path`.

String text

The text output from the model.

JsonValue; type "output\_text"constant"output\_text"constant

The type of the output text. Always `output_text`.

Optional<List<Logprob>> logprobs

String token

List<long> bytes

double logprob

List<TopLogprob> topLogprobs

String token

List<long> bytes

double logprob

class BetaResponseOutputRefusal:

A refusal from the model.

String refusal

The refusal explanation from the model.

JsonValue; type "refusal"constant"refusal"constant

The type of the refusal. Always `refusal`.

JsonValue; role "assistant"constant"assistant"constant

The role of the output message. Always `assistant`.

Status status

The status of the message input. One of `in_progress`, `completed`, or
`incomplete`. Populated when input items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "message"constant"message"constant

The type of the output message. Always `message`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Phase> phase

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

COMMENTARY("commentary")

FINAL\_ANSWER("final\_answer")

class BetaResponseFileSearchToolCall:

The results of a file search tool call. See the
[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

String id

The unique ID of the file search tool call.

List<String> queries

The queries used to search for files.

Status status

The status of the file search tool call. One of `in_progress`,
`searching`, `incomplete` or `failed`,

IN\_PROGRESS("in\_progress")

SEARCHING("searching")

COMPLETED("completed")

INCOMPLETE("incomplete")

FAILED("failed")

JsonValue; type "file\_search\_call"constant"file\_search\_call"constant

The type of the file search tool call. Always `file_search_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<List<Result>> results

The results of the file search tool call.

Optional<Attributes> attributes

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

String

double

boolean

Optional<String> fileId

The unique ID of the file.

Optional<String> filename

The name of the file.

Optional<Double> score

The relevance score of the file - a value between 0 and 1.

formatfloat

Optional<String> text

The text that was retrieved from the file.

class BetaResponseComputerToolCall:

A tool call to a computer use tool. See the
[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

String id

The unique ID of the computer call.

String callId

An identifier used when responding to the tool call with output.

List<PendingSafetyCheck> pendingSafetyChecks

The pending safety checks for the computer call.

String id

The ID of the pending safety check.

Optional<String> code

The type of the pending safety check.

Optional<String> message

Details about the pending safety check.

Status status

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

Type type

The type of the computer call. Always `computer_call`.

Optional<[BetaComputerAction](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action%20%3E%20(schema))> action

A click action.

Click

Button button

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

LEFT("left")

RIGHT("right")

WHEEL("wheel")

BACK("back")

FORWARD("forward")

JsonValue; type "click"constant"click"constant

Specifies the event type. For a click action, this property is always `click`.

long x

The x-coordinate where the click occurred.

long y

The y-coordinate where the click occurred.

Optional<List<String>> keys

The keys being held while clicking.

DoubleClick

Optional<List<String>> keys

The keys being held while double-clicking.

JsonValue; type "double\_click"constant"double\_click"constant

Specifies the event type. For a double click action, this property is always set to `double_click`.

long x

The x-coordinate where the double click occurred.

long y

The y-coordinate where the double click occurred.

Drag

List<Path> path

An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

[
  { x: 100, y: 200 },
  { x: 200, y: 300 }
]

long x

The x-coordinate.

long y

The y-coordinate.

JsonValue; type "drag"constant"drag"constant

Specifies the event type. For a drag action, this property is always set to `drag`.

Optional<List<String>> keys

The keys being held while dragging the mouse.

Keypress

List<String> keys

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

JsonValue; type "keypress"constant"keypress"constant

Specifies the event type. For a keypress action, this property is always set to `keypress`.

Move

JsonValue; type "move"constant"move"constant

Specifies the event type. For a move action, this property is always set to `move`.

long x

The x-coordinate to move to.

long y

The y-coordinate to move to.

Optional<List<String>> keys

The keys being held while moving the mouse.

JsonValue;

JsonValue; type "screenshot"constant"screenshot"constant

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

Scroll

long scrollX

The horizontal scroll distance.

long scrollY

The vertical scroll distance.

JsonValue; type "scroll"constant"scroll"constant

Specifies the event type. For a scroll action, this property is always set to `scroll`.

long x

The x-coordinate where the scroll occurred.

long y

The y-coordinate where the scroll occurred.

Optional<List<String>> keys

The keys being held while scrolling.

Type

String text

The text to type.

JsonValue; type "type"constant"type"constant

Specifies the event type. For a type action, this property is always set to `type`.

JsonValue;

JsonValue; type "wait"constant"wait"constant

Specifies the event type. For a wait action, this property is always set to `wait`.

Optional<List<[BetaComputerAction](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action%20%3E%20(schema))>> actions

Flattened batched actions for `computer_use`. Each action includes an
`type` discriminator and action-specific fields.

Click

Button button

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

LEFT("left")

RIGHT("right")

WHEEL("wheel")

BACK("back")

FORWARD("forward")

JsonValue; type "click"constant"click"constant

Specifies the event type. For a click action, this property is always `click`.

long x

The x-coordinate where the click occurred.

long y

The y-coordinate where the click occurred.

Optional<List<String>> keys

The keys being held while clicking.

DoubleClick

Optional<List<String>> keys

The keys being held while double-clicking.

JsonValue; type "double\_click"constant"double\_click"constant

Specifies the event type. For a double click action, this property is always set to `double_click`.

long x

The x-coordinate where the double click occurred.

long y

The y-coordinate where the double click occurred.

Drag

List<Path> path

An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

[
  { x: 100, y: 200 },
  { x: 200, y: 300 }
]

long x

The x-coordinate.

long y

The y-coordinate.

JsonValue; type "drag"constant"drag"constant

Specifies the event type. For a drag action, this property is always set to `drag`.

Optional<List<String>> keys

The keys being held while dragging the mouse.

Keypress

List<String> keys

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

JsonValue; type "keypress"constant"keypress"constant

Specifies the event type. For a keypress action, this property is always set to `keypress`.

Move

JsonValue; type "move"constant"move"constant

Specifies the event type. For a move action, this property is always set to `move`.

long x

The x-coordinate to move to.

long y

The y-coordinate to move to.

Optional<List<String>> keys

The keys being held while moving the mouse.

JsonValue;

JsonValue; type "screenshot"constant"screenshot"constant

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

Scroll

long scrollX

The horizontal scroll distance.

long scrollY

The vertical scroll distance.

JsonValue; type "scroll"constant"scroll"constant

Specifies the event type. For a scroll action, this property is always set to `scroll`.

long x

The x-coordinate where the scroll occurred.

long y

The y-coordinate where the scroll occurred.

Optional<List<String>> keys

The keys being held while scrolling.

Type

String text

The text to type.

JsonValue; type "type"constant"type"constant

Specifies the event type. For a type action, this property is always set to `type`.

JsonValue;

JsonValue; type "wait"constant"wait"constant

Specifies the event type. For a wait action, this property is always set to `wait`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

ComputerCallOutput

String callId

The ID of the computer tool call that produced the output.

maxLength64

minLength1

[BetaResponseComputerToolCallOutputScreenshot](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema)) output

A computer screenshot image used with the computer use tool.

JsonValue; type "computer\_screenshot"constant"computer\_screenshot"constant

Specifies the event type. For a computer screenshot, this property is
always set to `computer_screenshot`.

Optional<String> fileId

The identifier of an uploaded file that contains the screenshot.

Optional<String> imageUrl

The URL of the screenshot image.

formaturi

JsonValue; type "computer\_call\_output"constant"computer\_call\_output"constant

The type of the computer tool call output. Always `computer_call_output`.

Optional<String> id

The ID of the computer tool call output.

Optional<List<AcknowledgedSafetyCheck>> acknowledgedSafetyChecks

The safety checks reported by the API that have been acknowledged by the developer.

String id

The ID of the pending safety check.

Optional<String> code

The type of the pending safety check.

Optional<String> message

Details about the pending safety check.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Status> status

The status of the message input. One of `in_progress`, `completed`, or `incomplete`. Populated when input items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

class BetaResponseFunctionWebSearch:

The results of a web search tool call. See the
[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

String id

The unique ID of the web search tool call.

Action action

An object describing the specific action taken in this web search call.
Includes details on how the model used the web (search, open\_page, find\_in\_page).

class Search:

Action type “search” - Performs a web search query.

JsonValue; type "search"constant"search"constant

The action type.

Optional<List<String>> queries

The search queries.

DeprecatedOptional<String> query

The search query.

Optional<List<Source>> sources

The sources used in the search.

JsonValue; type "url"constant"url"constant

The type of source. Always `url`.

String url

The URL of the source.

formaturi

class OpenPage:

Action type “open\_page” - Opens a specific URL from search results.

JsonValue; type "open\_page"constant"open\_page"constant

The action type.

Optional<String> url

The URL opened by the model.

formaturi

class FindInPage:

Action type “find\_in\_page”: Searches for a pattern within a loaded page.

String pattern

The pattern or text to search for within the page.

JsonValue; type "find\_in\_page"constant"find\_in\_page"constant

The action type.

String url

The URL of the page searched for the pattern.

formaturi

Status status

The status of the web search tool call.

IN\_PROGRESS("in\_progress")

SEARCHING("searching")

COMPLETED("completed")

FAILED("failed")

JsonValue; type "web\_search\_call"constant"web\_search\_call"constant

The type of the web search tool call. Always `web_search_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseFunctionToolCall:

A tool call to run a function. See the
[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

String arguments

A JSON string of the arguments to pass to the function.

String callId

The unique ID of the function tool call generated by the model.

String name

The name of the function to run.

JsonValue; type "function\_call"constant"function\_call"constant

The type of the function tool call. Always `function_call`.

Optional<String> id

The unique ID of the function tool call.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

class Program:

String callerId

The call ID of the program item that produced this tool call.

JsonValue; type "program"constant"program"constant

Optional<String> namespace

The namespace of the function to run.

Optional<Status> status

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

FunctionCallOutput

String callId

The unique ID of the function tool call generated by the model.

maxLength64

minLength1

Output output

Text, image, or file output of the function tool call.

String

List<[BetaResponseFunctionCallOutputItem](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item%20%3E%20(schema))>

class BetaResponseInputTextContent:

A text input to the model.

String text

The text input to the model.

maxLength10485760

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputImageContent:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

JsonValue; type "input\_image"constant"input\_image"constant

The type of the input item. Always `input_image`.

Optional<Detail> detail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> imageUrl

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

maxLength20971520

formaturi

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputFileContent:

A file input to the model.

JsonValue; type "input\_file"constant"input\_file"constant

The type of the input item. Always `input_file`.

Optional<Detail> detail

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

AUTO("auto")

LOW("low")

HIGH("high")

Optional<String> fileData

The base64-encoded data of the file to be sent to the model.

maxLength73400320

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> fileUrl

The URL of the file to be sent to the model.

formaturi

Optional<String> filename

The name of the file to be sent to the model.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

JsonValue; type "function\_call\_output"constant"function\_call\_output"constant

The type of the function tool call output. Always `function_call_output`.

Optional<String> id

The unique ID of the function tool call output. Populated when this item is returned via API.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

The caller type. Always `direct`.

class Program:

String callerId

The call ID of the program item that produced this tool call.

maxLength64

minLength1

JsonValue; type "program"constant"program"constant

The caller type. Always `program`.

Optional<Status> status

The status of the item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

AgentMessage

String author

The sending agent identity.

List<Content> content

Plaintext, image, or encrypted content sent between agents.

class BetaResponseInputTextContent:

A text input to the model.

String text

The text input to the model.

maxLength10485760

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputImageContent:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

JsonValue; type "input\_image"constant"input\_image"constant

The type of the input item. Always `input_image`.

Optional<Detail> detail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> imageUrl

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

maxLength20971520

formaturi

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class EncryptedContent:

Opaque encrypted content that Responses API decrypts inside trusted model execution.

String encryptedContent

Opaque encrypted content.

maxLength10485760

JsonValue; type "encrypted\_content"constant"encrypted\_content"constant

The type of the input item. Always `encrypted_content`.

String recipient

The destination agent identity.

JsonValue; type "agent\_message"constant"agent\_message"constant

The item type. Always `agent_message`.

Optional<String> id

The unique ID of this agent message item.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

MultiAgentCall

Action action

The multi-agent action that was executed.

SPAWN\_AGENT("spawn\_agent")

INTERRUPT\_AGENT("interrupt\_agent")

LIST\_AGENTS("list\_agents")

SEND\_MESSAGE("send\_message")

FOLLOWUP\_TASK("followup\_task")

WAIT\_AGENT("wait\_agent")

String arguments

The action arguments as a JSON string.

String callId

The unique ID linking this call to its output.

maxLength64

minLength1

JsonValue; type "multi\_agent\_call"constant"multi\_agent\_call"constant

The item type. Always `multi_agent_call`.

Optional<String> id

The unique ID of this multi-agent call.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

MultiAgentCallOutput

Action action

The multi-agent action that produced this result.

SPAWN\_AGENT("spawn\_agent")

INTERRUPT\_AGENT("interrupt\_agent")

LIST\_AGENTS("list\_agents")

SEND\_MESSAGE("send\_message")

FOLLOWUP\_TASK("followup\_task")

WAIT\_AGENT("wait\_agent")

String callId

The unique ID of the multi-agent call.

maxLength64

minLength1

List<Output> output

Text output returned by the multi-agent action.

String text

The text content.

maxLength10485760

JsonValue; type "output\_text"constant"output\_text"constant

The content type. Always `output_text`.

Optional<List<Annotation>> annotations

Citations associated with the text content.

class FileCitation:

String fileId

The ID of the file.

String filename

The filename of the file cited.

long index

The index of the file in the list of files.

minimum0

JsonValue; type "file\_citation"constant"file\_citation"constant

The citation type. Always `file_citation`.

class UrlCitation:

long endIndex

The index of the last character of the citation in the message.

minimum0

long startIndex

The index of the first character of the citation in the message.

minimum0

String title

The title of the cited resource.

JsonValue; type "url\_citation"constant"url\_citation"constant

The citation type. Always `url_citation`.

String url

The URL of the cited resource.

formaturi

class ContainerFileCitation:

String containerId

The ID of the container.

long endIndex

The index of the last character of the citation in the message.

minimum0

String fileId

The ID of the container file.

String filename

The filename of the container file cited.

long startIndex

The index of the first character of the citation in the message.

minimum0

JsonValue; type "container\_file\_citation"constant"container\_file\_citation"constant

The citation type. Always `container_file_citation`.

JsonValue; type "multi\_agent\_call\_output"constant"multi\_agent\_call\_output"constant

The item type. Always `multi_agent_call_output`.

Optional<String> id

The unique ID of this multi-agent call output.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

ToolSearchCall

JsonValue arguments

The arguments supplied to the tool search call.

JsonValue; type "tool\_search\_call"constant"tool\_search\_call"constant

The item type. Always `tool_search_call`.

Optional<String> id

The unique ID of this tool search call.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<String> callId

The unique ID of the tool search call generated by the model.

maxLength64

minLength1

Optional<Execution> execution

Whether tool search was executed by the server or by the client.

SERVER("server")

CLIENT("client")

Optional<Status> status

The status of the tool search call.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

class BetaResponseToolSearchOutputItemParam:

List<[BetaTool](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))> tools

The loaded tool definitions returned by the tool search output.

class BetaFunctionTool:

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

String name

The name of the function to call.

Optional<Parameters> parameters

A JSON schema object describing the parameters of the function.

Optional<Boolean> strict

Whether strict parameter validation is enforced for this function tool.

JsonValue; type "function"constant"function"constant

The type of the function tool. Always `function`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this function is deferred and loaded via tool search.

Optional<String> description

A description of the function. Used by the model to determine whether or not to call the function.

Optional<OutputSchema> outputSchema

A JSON schema object describing the JSON value encoded in string outputs for this function.

class BetaFileSearchTool:

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

JsonValue; type "file\_search"constant"file\_search"constant

The type of the file search tool. Always `file_search`.

List<String> vectorStoreIds

The IDs of the vector stores to search.

Optional<Filters> filters

A filter to apply.

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

String

double

boolean

List<ComparisonFilterValueItem>

String

double

class CompoundFilter:

Combine multiple filters using `and` or `or`.

List<Filter> filters

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

String

double

boolean

List<ComparisonFilterValueItem>

String

double

JsonValue

Type type

Type of operation: `and` or `or`.

AND("and")

OR("or")

Optional<Long> maxNumResults

The maximum number of results to return. This number should be between 1 and 50 inclusive.

Optional<RankingOptions> rankingOptions

Ranking options for search.

Optional<HybridSearch> hybridSearch

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

double embeddingWeight

The weight of the embedding in the reciprocal ranking fusion.

double textWeight

The weight of the text in the reciprocal ranking fusion.

Optional<Ranker> ranker

The ranker to use for the file search.

AUTO("auto")

DEFAULT\_2024\_11\_15("default-2024-11-15")

Optional<Double> scoreThreshold

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class BetaComputerTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

JsonValue; type "computer"constant"computer"constant

The type of the computer tool. Always `computer`.

class BetaComputerUsePreviewTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

long displayHeight

The height of the computer display.

long displayWidth

The width of the computer display.

Environment environment

The type of computer environment to control.

WINDOWS("windows")

MAC("mac")

LINUX("linux")

UBUNTU("ubuntu")

BROWSER("browser")

JsonValue; type "computer\_use\_preview"constant"computer\_use\_preview"constant

The type of the computer use tool. Always `computer_use_preview`.

class BetaWebSearchTool:

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

WEB\_SEARCH("web\_search")

WEB\_SEARCH\_2025\_08\_26("web\_search\_2025\_08\_26")

Optional<Filters> filters

Filters for the search.

Optional<List<String>> allowedDomains

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The approximate location of the user.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

Optional<Type> type

The type of location approximation. Always `approximate`.

Mcp

String serverLabel

A label for this MCP server, used to identify it in tool calls.

JsonValue; type "mcp"constant"mcp"constant

The type of the MCP tool. Always `mcp`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<AllowedTools> allowedTools

List of allowed tool names or a filter object.

List<String>

class McpToolFilter:

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<String> authorization

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

Optional<ConnectorId> connectorId

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

CONNECTOR\_DROPBOX("connector\_dropbox")

CONNECTOR\_GMAIL("connector\_gmail")

CONNECTOR\_GOOGLECALENDAR("connector\_googlecalendar")

CONNECTOR\_GOOGLEDRIVE("connector\_googledrive")

CONNECTOR\_MICROSOFTTEAMS("connector\_microsoftteams")

CONNECTOR\_OUTLOOKCALENDAR("connector\_outlookcalendar")

CONNECTOR\_OUTLOOKEMAIL("connector\_outlookemail")

CONNECTOR\_SHAREPOINT("connector\_sharepoint")

Optional<Boolean> deferLoading

Whether this MCP tool is deferred and discovered via tool search.

Optional<Headers> headers

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

Optional<RequireApproval> requireApproval

Specify which of the MCP server’s tools require approval.

class McpToolApprovalFilter:

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

Optional<Always> always

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<Never> never

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

enum McpToolApprovalSetting:

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

ALWAYS("always")

NEVER("never")

Optional<String> serverDescription

Optional description of the MCP server, used to provide more context.

Optional<String> serverUrl

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

Optional<String> tunnelId

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter

Container container

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

String

class CodeInterpreterToolAuto:

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

JsonValue; type "auto"constant"auto"constant

Always `auto`.

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the code interpreter container.

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

JsonValue; type "code\_interpreter"constant"code\_interpreter"constant

The type of the code interpreter tool. Always `code_interpreter`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

JsonValue;

JsonValue; type "programmatic\_tool\_calling"constant"programmatic\_tool\_calling"constant

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration

JsonValue; type "image\_generation"constant"image\_generation"constant

The type of the image generation tool. Always `image_generation`.

Optional<Action> action

Whether to generate a new image or edit an existing image. Default: `auto`.

GENERATE("generate")

EDIT("edit")

AUTO("auto")

Optional<Background> background

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

TRANSPARENT("transparent")

OPAQUE("opaque")

AUTO("auto")

Optional<InputFidelity> inputFidelity

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

HIGH("high")

LOW("low")

Optional<InputImageMask> inputImageMask

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

Optional<String> fileId

File ID for the mask image.

Optional<String> imageUrl

Base64-encoded mask image.

Optional<Model> model

The image generation model to use. Default: `gpt-image-1`.

GPT\_IMAGE\_1("gpt-image-1")

GPT\_IMAGE\_1\_MINI("gpt-image-1-mini")

GPT\_IMAGE\_2("gpt-image-2")

GPT\_IMAGE\_2\_2026\_04\_21("gpt-image-2-2026-04-21")

GPT\_IMAGE\_1\_5("gpt-image-1.5")

CHATGPT\_IMAGE\_LATEST("chatgpt-image-latest")

Optional<Moderation> moderation

Moderation level for the generated image. Default: `auto`.

AUTO("auto")

LOW("low")

Optional<Long> outputCompression

Compression level for the output image. Default: 100.

minimum0

maximum100

Optional<OutputFormat> outputFormat

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

PNG("png")

WEBP("webp")

JPEG("jpeg")

Optional<Long> partialImages

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

Optional<Quality> quality

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

LOW("low")

MEDIUM("medium")

HIGH("high")

AUTO("auto")

Optional<Size> size

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

\_1024X1024("1024x1024")

\_1024X1536("1024x1536")

\_1536X1024("1536x1024")

AUTO("auto")

JsonValue;

JsonValue; type "local\_shell"constant"local\_shell"constant

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool:

A tool that allows the model to execute shell commands.

JsonValue; type "shell"constant"shell"constant

The type of the shell tool. Always `shell`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Environment> environment

class BetaContainerAuto:

JsonValue; type "container\_auto"constant"container\_auto"constant

Automatically creates a container for this request

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the container.

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

Optional<List<Skill>> skills

An optional list of skills referenced by id or inline data.

class BetaSkillReference:

String skillId

The ID of the referenced skill.

maxLength64

minLength1

JsonValue; type "skill\_reference"constant"skill\_reference"constant

References a skill created with the /v1/skills endpoint.

Optional<String> version

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class BetaInlineSkill:

String description

The description of the skill.

String name

The name of the skill.

[BetaInlineSkillSource](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) source

Inline skill payload

String data

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

JsonValue; mediaType "application/zip"constant"application/zip"constant

The media type of the inline skill payload. Must be `application/zip`.

JsonValue; type "base64"constant"base64"constant

The type of the inline skill source. Must be `base64`.

JsonValue; type "inline"constant"inline"constant

Defines an inline skill for this request.

class BetaLocalEnvironment:

JsonValue; type "local"constant"local"constant

Use a local computer environment.

Optional<List<[BetaLocalSkill](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))>> skills

An optional list of skills.

String description

The description of the skill.

String name

The name of the skill.

String path

The path to the directory containing the skill.

class BetaContainerReference:

String containerId

The ID of the referenced container.

JsonValue; type "container\_reference"constant"container\_reference"constant

References a container created with the /v1/containers endpoint

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<Format> format

The input format for the custom tool. Default is unconstrained text.

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

A grammar defined by the user.

String definition

The grammar definition.

Syntax syntax

The syntax of the grammar definition. One of `lark` or `regex`.

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

Grammar format. Always `grammar`.

class BetaNamespaceTool:

Groups function/custom tools under a shared namespace.

String description

A description of the namespace shown to the model.

minLength1

String name

The namespace name used in tool calls (for example, `crm`).

minLength1

List<Tool> tools

The function/custom tools available inside this namespace.

class Function:

String name

maxLength128

minLength1

JsonValue; type "function"constant"function"constant

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this function should be deferred and discovered via tool search.

Optional<String> description

Optional<OutputSchema> outputSchema

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

Optional<JsonValue> parameters

Optional<Boolean> strict

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<Format> format

The input format for the custom tool. Default is unconstrained text.

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

A grammar defined by the user.

String definition

The grammar definition.

Syntax syntax

The syntax of the grammar definition. One of `lark` or `regex`.

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

Grammar format. Always `grammar`.

JsonValue; type "namespace"constant"namespace"constant

The type of the tool. Always `namespace`.

class BetaToolSearchTool:

Hosted or BYOT tool search configuration for deferred tools.

JsonValue; type "tool\_search"constant"tool\_search"constant

The type of the tool. Always `tool_search`.

Optional<String> description

Description shown to the model for a client-executed tool search tool.

Optional<Execution> execution

Whether tool search is executed by the server or by the client.

SERVER("server")

CLIENT("client")

Optional<JsonValue> parameters

Parameter schema for a client-executed tool search tool.

class BetaWebSearchPreviewTool:

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

WEB\_SEARCH\_PREVIEW("web\_search\_preview")

WEB\_SEARCH\_PREVIEW\_2025\_03\_11("web\_search\_preview\_2025\_03\_11")

Optional<List<SearchContentType>> searchContentTypes

TEXT("text")

IMAGE("image")

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The user’s location.

JsonValue; type "approximate"constant"approximate"constant

The type of location approximation. Always `approximate`.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

class BetaApplyPatchTool:

Allows the assistant to create, delete, or update files using unified diffs.

JsonValue; type "apply\_patch"constant"apply\_patch"constant

The type of the tool. Always `apply_patch`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

JsonValue; type "tool\_search\_output"constant"tool\_search\_output"constant

The item type. Always `tool_search_output`.

Optional<String> id

The unique ID of this tool search output.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<String> callId

The unique ID of the tool search call generated by the model.

maxLength64

minLength1

Optional<Execution> execution

Whether tool search was executed by the server or by the client.

SERVER("server")

CLIENT("client")

Optional<Status> status

The status of the tool search output.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

AdditionalTools

JsonValue; role "developer"constant"developer"constant

The role that provided the additional tools. Only `developer` is supported.

List<[BetaTool](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))> tools

A list of additional tools made available at this item.

class BetaFunctionTool:

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

String name

The name of the function to call.

Optional<Parameters> parameters

A JSON schema object describing the parameters of the function.

Optional<Boolean> strict

Whether strict parameter validation is enforced for this function tool.

JsonValue; type "function"constant"function"constant

The type of the function tool. Always `function`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this function is deferred and loaded via tool search.

Optional<String> description

A description of the function. Used by the model to determine whether or not to call the function.

Optional<OutputSchema> outputSchema

A JSON schema object describing the JSON value encoded in string outputs for this function.

class BetaFileSearchTool:

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

JsonValue; type "file\_search"constant"file\_search"constant

The type of the file search tool. Always `file_search`.

List<String> vectorStoreIds

The IDs of the vector stores to search.

Optional<Filters> filters

A filter to apply.

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

String

double

boolean

List<ComparisonFilterValueItem>

String

double

class CompoundFilter:

Combine multiple filters using `and` or `or`.

List<Filter> filters

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

String

double

boolean

List<ComparisonFilterValueItem>

String

double

JsonValue

Type type

Type of operation: `and` or `or`.

AND("and")

OR("or")

Optional<Long> maxNumResults

The maximum number of results to return. This number should be between 1 and 50 inclusive.

Optional<RankingOptions> rankingOptions

Ranking options for search.

Optional<HybridSearch> hybridSearch

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

double embeddingWeight

The weight of the embedding in the reciprocal ranking fusion.

double textWeight

The weight of the text in the reciprocal ranking fusion.

Optional<Ranker> ranker

The ranker to use for the file search.

AUTO("auto")

DEFAULT\_2024\_11\_15("default-2024-11-15")

Optional<Double> scoreThreshold

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class BetaComputerTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

JsonValue; type "computer"constant"computer"constant

The type of the computer tool. Always `computer`.

class BetaComputerUsePreviewTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

long displayHeight

The height of the computer display.

long displayWidth

The width of the computer display.

Environment environment

The type of computer environment to control.

WINDOWS("windows")

MAC("mac")

LINUX("linux")

UBUNTU("ubuntu")

BROWSER("browser")

JsonValue; type "computer\_use\_preview"constant"computer\_use\_preview"constant

The type of the computer use tool. Always `computer_use_preview`.

class BetaWebSearchTool:

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

WEB\_SEARCH("web\_search")

WEB\_SEARCH\_2025\_08\_26("web\_search\_2025\_08\_26")

Optional<Filters> filters

Filters for the search.

Optional<List<String>> allowedDomains

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The approximate location of the user.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

Optional<Type> type

The type of location approximation. Always `approximate`.

Mcp

String serverLabel

A label for this MCP server, used to identify it in tool calls.

JsonValue; type "mcp"constant"mcp"constant

The type of the MCP tool. Always `mcp`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<AllowedTools> allowedTools

List of allowed tool names or a filter object.

List<String>

class McpToolFilter:

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<String> authorization

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

Optional<ConnectorId> connectorId

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

CONNECTOR\_DROPBOX("connector\_dropbox")

CONNECTOR\_GMAIL("connector\_gmail")

CONNECTOR\_GOOGLECALENDAR("connector\_googlecalendar")

CONNECTOR\_GOOGLEDRIVE("connector\_googledrive")

CONNECTOR\_MICROSOFTTEAMS("connector\_microsoftteams")

CONNECTOR\_OUTLOOKCALENDAR("connector\_outlookcalendar")

CONNECTOR\_OUTLOOKEMAIL("connector\_outlookemail")

CONNECTOR\_SHAREPOINT("connector\_sharepoint")

Optional<Boolean> deferLoading

Whether this MCP tool is deferred and discovered via tool search.

Optional<Headers> headers

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

Optional<RequireApproval> requireApproval

Specify which of the MCP server’s tools require approval.

class McpToolApprovalFilter:

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

Optional<Always> always

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<Never> never

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

enum McpToolApprovalSetting:

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

ALWAYS("always")

NEVER("never")

Optional<String> serverDescription

Optional description of the MCP server, used to provide more context.

Optional<String> serverUrl

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

Optional<String> tunnelId

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter

Container container

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

String

class CodeInterpreterToolAuto:

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

JsonValue; type "auto"constant"auto"constant

Always `auto`.

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the code interpreter container.

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

JsonValue; type "code\_interpreter"constant"code\_interpreter"constant

The type of the code interpreter tool. Always `code_interpreter`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

JsonValue;

JsonValue; type "programmatic\_tool\_calling"constant"programmatic\_tool\_calling"constant

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration

JsonValue; type "image\_generation"constant"image\_generation"constant

The type of the image generation tool. Always `image_generation`.

Optional<Action> action

Whether to generate a new image or edit an existing image. Default: `auto`.

GENERATE("generate")

EDIT("edit")

AUTO("auto")

Optional<Background> background

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

TRANSPARENT("transparent")

OPAQUE("opaque")

AUTO("auto")

Optional<InputFidelity> inputFidelity

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

HIGH("high")

LOW("low")

Optional<InputImageMask> inputImageMask

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

Optional<String> fileId

File ID for the mask image.

Optional<String> imageUrl

Base64-encoded mask image.

Optional<Model> model

The image generation model to use. Default: `gpt-image-1`.

GPT\_IMAGE\_1("gpt-image-1")

GPT\_IMAGE\_1\_MINI("gpt-image-1-mini")

GPT\_IMAGE\_2("gpt-image-2")

GPT\_IMAGE\_2\_2026\_04\_21("gpt-image-2-2026-04-21")

GPT\_IMAGE\_1\_5("gpt-image-1.5")

CHATGPT\_IMAGE\_LATEST("chatgpt-image-latest")

Optional<Moderation> moderation

Moderation level for the generated image. Default: `auto`.

AUTO("auto")

LOW("low")

Optional<Long> outputCompression

Compression level for the output image. Default: 100.

minimum0

maximum100

Optional<OutputFormat> outputFormat

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

PNG("png")

WEBP("webp")

JPEG("jpeg")

Optional<Long> partialImages

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

Optional<Quality> quality

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

LOW("low")

MEDIUM("medium")

HIGH("high")

AUTO("auto")

Optional<Size> size

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

\_1024X1024("1024x1024")

\_1024X1536("1024x1536")

\_1536X1024("1536x1024")

AUTO("auto")

JsonValue;

JsonValue; type "local\_shell"constant"local\_shell"constant

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool:

A tool that allows the model to execute shell commands.

JsonValue; type "shell"constant"shell"constant

The type of the shell tool. Always `shell`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Environment> environment

class BetaContainerAuto:

JsonValue; type "container\_auto"constant"container\_auto"constant

Automatically creates a container for this request

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the container.

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

Optional<List<Skill>> skills

An optional list of skills referenced by id or inline data.

class BetaSkillReference:

String skillId

The ID of the referenced skill.

maxLength64

minLength1

JsonValue; type "skill\_reference"constant"skill\_reference"constant

References a skill created with the /v1/skills endpoint.

Optional<String> version

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class BetaInlineSkill:

String description

The description of the skill.

String name

The name of the skill.

[BetaInlineSkillSource](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) source

Inline skill payload

String data

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

JsonValue; mediaType "application/zip"constant"application/zip"constant

The media type of the inline skill payload. Must be `application/zip`.

JsonValue; type "base64"constant"base64"constant

The type of the inline skill source. Must be `base64`.

JsonValue; type "inline"constant"inline"constant

Defines an inline skill for this request.

class BetaLocalEnvironment:

JsonValue; type "local"constant"local"constant

Use a local computer environment.

Optional<List<[BetaLocalSkill](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))>> skills

An optional list of skills.

String description

The description of the skill.

String name

The name of the skill.

String path

The path to the directory containing the skill.

class BetaContainerReference:

String containerId

The ID of the referenced container.

JsonValue; type "container\_reference"constant"container\_reference"constant

References a container created with the /v1/containers endpoint

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<Format> format

The input format for the custom tool. Default is unconstrained text.

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

A grammar defined by the user.

String definition

The grammar definition.

Syntax syntax

The syntax of the grammar definition. One of `lark` or `regex`.

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

Grammar format. Always `grammar`.

class BetaNamespaceTool:

Groups function/custom tools under a shared namespace.

String description

A description of the namespace shown to the model.

minLength1

String name

The namespace name used in tool calls (for example, `crm`).

minLength1

List<Tool> tools

The function/custom tools available inside this namespace.

class Function:

String name

maxLength128

minLength1

JsonValue; type "function"constant"function"constant

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this function should be deferred and discovered via tool search.

Optional<String> description

Optional<OutputSchema> outputSchema

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

Optional<JsonValue> parameters

Optional<Boolean> strict

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<Format> format

The input format for the custom tool. Default is unconstrained text.

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

A grammar defined by the user.

String definition

The grammar definition.

Syntax syntax

The syntax of the grammar definition. One of `lark` or `regex`.

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

Grammar format. Always `grammar`.

JsonValue; type "namespace"constant"namespace"constant

The type of the tool. Always `namespace`.

class BetaToolSearchTool:

Hosted or BYOT tool search configuration for deferred tools.

JsonValue; type "tool\_search"constant"tool\_search"constant

The type of the tool. Always `tool_search`.

Optional<String> description

Description shown to the model for a client-executed tool search tool.

Optional<Execution> execution

Whether tool search is executed by the server or by the client.

SERVER("server")

CLIENT("client")

Optional<JsonValue> parameters

Parameter schema for a client-executed tool search tool.

class BetaWebSearchPreviewTool:

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

WEB\_SEARCH\_PREVIEW("web\_search\_preview")

WEB\_SEARCH\_PREVIEW\_2025\_03\_11("web\_search\_preview\_2025\_03\_11")

Optional<List<SearchContentType>> searchContentTypes

TEXT("text")

IMAGE("image")

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The user’s location.

JsonValue; type "approximate"constant"approximate"constant

The type of location approximation. Always `approximate`.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

class BetaApplyPatchTool:

Allows the assistant to create, delete, or update files using unified diffs.

JsonValue; type "apply\_patch"constant"apply\_patch"constant

The type of the tool. Always `apply_patch`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

JsonValue; type "additional\_tools"constant"additional\_tools"constant

The item type. Always `additional_tools`.

Optional<String> id

The unique ID of this additional tools item.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseReasoningItem:

A description of the chain of thought used by a reasoning model while generating
a response. Be sure to include these items in your `input` to the Responses API
for subsequent turns of a conversation if you are manually
[managing context](https://platform.openai.com/docs/guides/conversation-state).

String id

The unique identifier of the reasoning content.

List<Summary> summary

Reasoning summary content.

String text

A summary of the reasoning output from the model so far.

JsonValue; type "summary\_text"constant"summary\_text"constant

The type of the object. Always `summary_text`.

JsonValue; type "reasoning"constant"reasoning"constant

The type of the object. Always `reasoning`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<List<Content>> content

Reasoning text content.

String text

The reasoning text from the model.

JsonValue; type "reasoning\_text"constant"reasoning\_text"constant

The type of the reasoning text. Always `reasoning_text`.

Optional<String> encryptedContent

The encrypted content of the reasoning item. This is populated by default
for reasoning items returned by `POST /v1/responses` and WebSocket
`response.create` requests.

Optional<Status> status

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

class BetaResponseCompactionItemParam:

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

String encryptedContent

The encrypted content of the compaction summary.

maxLength10485760

JsonValue; type "compaction"constant"compaction"constant

The type of the item. Always `compaction`.

Optional<String> id

The ID of the compaction item.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

ImageGenerationCall

String id

The unique ID of the image generation call.

Optional<String> result

The generated image encoded in base64.

Status status

The status of the image generation call.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

GENERATING("generating")

FAILED("failed")

JsonValue; type "image\_generation\_call"constant"image\_generation\_call"constant

The type of the image generation call. Always `image_generation_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseCodeInterpreterToolCall:

A tool call to run code.

String id

The unique ID of the code interpreter tool call.

Optional<String> code

The code to run, or null if not available.

String containerId

The ID of the container used to run the code.

Optional<List<Output>> outputs

The outputs generated by the code interpreter, such as logs or images.
Can be null if no outputs are available.

class Logs:

The logs output from the code interpreter.

String logs

The logs output from the code interpreter.

JsonValue; type "logs"constant"logs"constant

The type of the output. Always `logs`.

class Image:

The image output from the code interpreter.

JsonValue; type "image"constant"image"constant

The type of the output. Always `image`.

String url

The URL of the image output from the code interpreter.

formaturi

Status status

The status of the code interpreter tool call. Valid values are `in_progress`, `completed`, `incomplete`, `interpreting`, and `failed`.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

INTERPRETING("interpreting")

FAILED("failed")

JsonValue; type "code\_interpreter\_call"constant"code\_interpreter\_call"constant

The type of the code interpreter tool call. Always `code_interpreter_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

LocalShellCall

String id

The unique ID of the local shell call.

Action action

Execute a shell command on the server.

List<String> command

The command to run.

Env env

Environment variables to set for the command.

JsonValue; type "exec"constant"exec"constant

The type of the local shell action. Always `exec`.

Optional<Long> timeoutMs

Optional timeout in milliseconds for the command.

Optional<String> user

Optional user to run the command as.

Optional<String> workingDirectory

Optional working directory to run the command in.

String callId

The unique ID of the local shell tool call generated by the model.

Status status

The status of the local shell call.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "local\_shell\_call"constant"local\_shell\_call"constant

The type of the local shell call. Always `local_shell_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

LocalShellCallOutput

String id

The unique ID of the local shell tool call generated by the model.

String output

A JSON string of the output of the local shell tool call.

JsonValue; type "local\_shell\_call\_output"constant"local\_shell\_call\_output"constant

The type of the local shell tool call output. Always `local_shell_call_output`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Status> status

The status of the item. One of `in_progress`, `completed`, or `incomplete`.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

ShellCall

Action action

The shell commands and limits that describe how to run the tool call.

List<String> commands

Ordered shell commands for the execution environment to run.

Optional<Long> maxOutputLength

Maximum number of UTF-8 characters to capture from combined stdout and stderr output.

Optional<Long> timeoutMs

Maximum wall-clock time in milliseconds to allow the shell commands to run.

String callId

The unique ID of the shell tool call generated by the model.

maxLength64

minLength1

JsonValue; type "shell\_call"constant"shell\_call"constant

The type of the item. Always `shell_call`.

Optional<String> id

The unique ID of the shell tool call. Populated when this item is returned via API.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

The caller type. Always `direct`.

class Program:

String callerId

The call ID of the program item that produced this tool call.

maxLength64

minLength1

JsonValue; type "program"constant"program"constant

The caller type. Always `program`.

Optional<Environment> environment

The environment to execute the shell commands in.

class BetaLocalEnvironment:

JsonValue; type "local"constant"local"constant

Use a local computer environment.

Optional<List<[BetaLocalSkill](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))>> skills

An optional list of skills.

String description

The description of the skill.

String name

The name of the skill.

String path

The path to the directory containing the skill.

class BetaContainerReference:

String containerId

The ID of the referenced container.

JsonValue; type "container\_reference"constant"container\_reference"constant

References a container created with the /v1/containers endpoint

Optional<Status> status

The status of the shell call. One of `in_progress`, `completed`, or `incomplete`.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

ShellCallOutput

String callId

The unique ID of the shell tool call generated by the model.

maxLength64

minLength1

List<[BetaResponseFunctionShellCallOutputContent](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_shell_call_output_content%20%3E%20(schema))> output

Captured chunks of stdout and stderr output, along with their associated outcomes.

Outcome outcome

The exit or timeout outcome associated with this shell call.

JsonValue;

JsonValue; type "timeout"constant"timeout"constant

The outcome type. Always `timeout`.

class Exit:

Indicates that the shell commands finished and returned an exit code.

long exitCode

The exit code returned by the shell process.

JsonValue; type "exit"constant"exit"constant

The outcome type. Always `exit`.

String stderr

Captured stderr output for the shell call.

maxLength10485760

String stdout

Captured stdout output for the shell call.

maxLength10485760

JsonValue; type "shell\_call\_output"constant"shell\_call\_output"constant

The type of the item. Always `shell_call_output`.

Optional<String> id

The unique ID of the shell tool call output. Populated when this item is returned via API.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

The caller type. Always `direct`.

class Program:

String callerId

The call ID of the program item that produced this tool call.

maxLength64

minLength1

JsonValue; type "program"constant"program"constant

The caller type. Always `program`.

Optional<Long> maxOutputLength

The maximum number of UTF-8 characters captured for this shell call’s combined output.

Optional<Status> status

The status of the shell call output.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

ApplyPatchCall

String callId

The unique ID of the apply patch tool call generated by the model.

maxLength64

minLength1

Operation operation

The specific create, delete, or update instruction for the apply\_patch tool call.

class CreateFile:

Instruction for creating a new file via the apply\_patch tool.

String diff

Unified diff content to apply when creating the file.

maxLength10485760

String path

Path of the file to create relative to the workspace root.

minLength1

JsonValue; type "create\_file"constant"create\_file"constant

The operation type. Always `create_file`.

class DeleteFile:

Instruction for deleting an existing file via the apply\_patch tool.

String path

Path of the file to delete relative to the workspace root.

minLength1

JsonValue; type "delete\_file"constant"delete\_file"constant

The operation type. Always `delete_file`.

class UpdateFile:

Instruction for updating an existing file via the apply\_patch tool.

String diff

Unified diff content to apply to the existing file.

maxLength10485760

String path

Path of the file to update relative to the workspace root.

minLength1

JsonValue; type "update\_file"constant"update\_file"constant

The operation type. Always `update_file`.

Status status

The status of the apply patch tool call. One of `in_progress` or `completed`.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

JsonValue; type "apply\_patch\_call"constant"apply\_patch\_call"constant

The type of the item. Always `apply_patch_call`.

Optional<String> id

The unique ID of the apply patch tool call. Populated when this item is returned via API.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

The caller type. Always `direct`.

class Program:

String callerId

The call ID of the program item that produced this tool call.

maxLength64

minLength1

JsonValue; type "program"constant"program"constant

The caller type. Always `program`.

ApplyPatchCallOutput

String callId

The unique ID of the apply patch tool call generated by the model.

maxLength64

minLength1

Status status

The status of the apply patch tool call output. One of `completed` or `failed`.

COMPLETED("completed")

FAILED("failed")

JsonValue; type "apply\_patch\_call\_output"constant"apply\_patch\_call\_output"constant

The type of the item. Always `apply_patch_call_output`.

Optional<String> id

The unique ID of the apply patch tool call output. Populated when this item is returned via API.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

The caller type. Always `direct`.

class Program:

String callerId

The call ID of the program item that produced this tool call.

maxLength64

minLength1

JsonValue; type "program"constant"program"constant

The caller type. Always `program`.

Optional<String> output

Optional human-readable log text from the apply patch tool (e.g., patch results or errors).

maxLength10485760

McpListTools

String id

The unique ID of the list.

String serverLabel

The label of the MCP server.

List<Tool> tools

The tools available on the server.

JsonValue inputSchema

The JSON schema describing the tool’s input.

String name

The name of the tool.

Optional<JsonValue> annotations

Additional annotations about the tool.

Optional<String> description

The description of the tool.

JsonValue; type "mcp\_list\_tools"constant"mcp\_list\_tools"constant

The type of the item. Always `mcp_list_tools`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<String> error

Error message if the server could not list tools.

McpApprovalRequest

String id

The unique ID of the approval request.

String arguments

A JSON string of arguments for the tool.

String name

The name of the tool to run.

String serverLabel

The label of the MCP server making the request.

JsonValue; type "mcp\_approval\_request"constant"mcp\_approval\_request"constant

The type of the item. Always `mcp_approval_request`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

McpApprovalResponse

String approvalRequestId

The ID of the approval request being answered.

boolean approve

Whether the request was approved.

JsonValue; type "mcp\_approval\_response"constant"mcp\_approval\_response"constant

The type of the item. Always `mcp_approval_response`.

Optional<String> id

The unique ID of the approval response

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<String> reason

Optional reason for the decision.

McpCall

String id

The unique ID of the tool call.

String arguments

A JSON string of the arguments passed to the tool.

String name

The name of the tool that was run.

String serverLabel

The label of the MCP server running the tool.

JsonValue; type "mcp\_call"constant"mcp\_call"constant

The type of the item. Always `mcp_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<String> approvalRequestId

Unique identifier for the MCP tool call approval request.
Include this value in a subsequent `mcp_approval_response` input to approve or reject the corresponding tool call.

Optional<String> error

The error from the tool call, if any.

Optional<String> output

The output from the tool call.

Optional<Status> status

The status of the tool call. One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

CALLING("calling")

FAILED("failed")

class BetaResponseCustomToolCallOutput:

The output of a custom tool call from your code, being sent back to the model.

String callId

The call ID, used to map this custom tool call output to a custom tool call.

Output output

The output from the custom tool call generated by your code.
Can be a string or an list of output content.

String

List<BetaFunctionAndCustomToolCallOutput>

class BetaResponseInputText:

A text input to the model.

String text

The text input to the model.

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputImage:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail detail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

JsonValue; type "input\_image"constant"input\_image"constant

The type of the input item. Always `input_image`.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> imageUrl

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile:

A file input to the model.

JsonValue; type "input\_file"constant"input\_file"constant

The type of the input item. Always `input_file`.

Optional<Detail> detail

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

AUTO("auto")

LOW("low")

HIGH("high")

Optional<String> fileData

The content of the file to be sent to the model.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> fileUrl

The URL of the file to be sent to the model.

formaturi

Optional<String> filename

The name of the file to be sent to the model.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

JsonValue; type "custom\_tool\_call\_output"constant"custom\_tool\_call\_output"constant

The type of the custom tool call output. Always `custom_tool_call_output`.

Optional<String> id

The unique ID of the custom tool call output in the OpenAI platform.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

The caller type. Always `direct`.

class Program:

String callerId

The call ID of the program item that produced this tool call.

maxLength64

minLength1

JsonValue; type "program"constant"program"constant

The caller type. Always `program`.

class BetaResponseCustomToolCall:

A call to a custom tool created by the model.

String callId

An identifier used to map this custom tool call to a tool call output.

String input

The input for the custom tool call generated by the model.

String name

The name of the custom tool being called.

JsonValue; type "custom\_tool\_call"constant"custom\_tool\_call"constant

The type of the custom tool call. Always `custom_tool_call`.

Optional<String> id

The unique ID of the custom tool call in the OpenAI platform.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

class Program:

String callerId

The call ID of the program item that produced this tool call.

JsonValue; type "program"constant"program"constant

Optional<String> namespace

The namespace of the custom tool being called.

CompactionTrigger

JsonValue; type "compaction\_trigger"constant"compaction\_trigger"constant

The type of the item. Always `compaction_trigger`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

ItemReference

String id

The ID of the item to reference.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Type> type

The type of item to reference. Always `item_reference`.

Program

String id

The unique ID of this program item.

String callId

The stable call ID of the program item.

maxLength64

minLength1

String code

The JavaScript source executed by programmatic tool calling.

maxLength10485760

String fingerprint

Opaque program replay fingerprint that must be round-tripped.

maxLength10485760

JsonValue; type "program"constant"program"constant

The item type. Always `program`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

ProgramOutput

String id

The unique ID of this program output item.

String callId

The call ID of the program item.

maxLength64

minLength1

String result

The result produced by the program item.

maxLength10485760

Status status

The terminal status of the program output.

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "program\_output"constant"program\_output"constant

The item type. Always `program_output`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Metadata> metadata

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

Model model

Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model guide](https://platform.openai.com/docs/models)
to browse and compare available models.

GPT\_5\_6\_SOL("gpt-5.6-sol")

GPT\_5\_6\_TERRA("gpt-5.6-terra")

GPT\_5\_6\_LUNA("gpt-5.6-luna")

GPT\_5\_4("gpt-5.4")

GPT\_5\_4\_MINI("gpt-5.4-mini")

GPT\_5\_4\_NANO("gpt-5.4-nano")

GPT\_5\_4\_MINI\_2026\_03\_17("gpt-5.4-mini-2026-03-17")

GPT\_5\_4\_NANO\_2026\_03\_17("gpt-5.4-nano-2026-03-17")

GPT\_5\_3\_CHAT\_LATEST("gpt-5.3-chat-latest")

GPT\_5\_2("gpt-5.2")

GPT\_5\_2\_2025\_12\_11("gpt-5.2-2025-12-11")

GPT\_5\_2\_CHAT\_LATEST("gpt-5.2-chat-latest")

GPT\_5\_2\_PRO("gpt-5.2-pro")

GPT\_5\_2\_PRO\_2025\_12\_11("gpt-5.2-pro-2025-12-11")

GPT\_5\_1("gpt-5.1")

GPT\_5\_1\_2025\_11\_13("gpt-5.1-2025-11-13")

GPT\_5\_1\_CODEX("gpt-5.1-codex")

GPT\_5\_1\_MINI("gpt-5.1-mini")

GPT\_5\_1\_CHAT\_LATEST("gpt-5.1-chat-latest")

GPT\_5("gpt-5")

GPT\_5\_MINI("gpt-5-mini")

GPT\_5\_NANO("gpt-5-nano")

GPT\_5\_2025\_08\_07("gpt-5-2025-08-07")

GPT\_5\_MINI\_2025\_08\_07("gpt-5-mini-2025-08-07")

GPT\_5\_NANO\_2025\_08\_07("gpt-5-nano-2025-08-07")

GPT\_5\_CHAT\_LATEST("gpt-5-chat-latest")

GPT\_4\_1("gpt-4.1")

GPT\_4\_1\_MINI("gpt-4.1-mini")

GPT\_4\_1\_NANO("gpt-4.1-nano")

GPT\_4\_1\_2025\_04\_14("gpt-4.1-2025-04-14")

GPT\_4\_1\_MINI\_2025\_04\_14("gpt-4.1-mini-2025-04-14")

GPT\_4\_1\_NANO\_2025\_04\_14("gpt-4.1-nano-2025-04-14")

O4\_MINI("o4-mini")

O4\_MINI\_2025\_04\_16("o4-mini-2025-04-16")

O3("o3")

O3\_2025\_04\_16("o3-2025-04-16")

O3\_MINI("o3-mini")

O3\_MINI\_2025\_01\_31("o3-mini-2025-01-31")

O1("o1")

O1\_2024\_12\_17("o1-2024-12-17")

O1\_PREVIEW("o1-preview")

O1\_PREVIEW\_2024\_09\_12("o1-preview-2024-09-12")

O1\_MINI("o1-mini")

O1\_MINI\_2024\_09\_12("o1-mini-2024-09-12")

GPT\_4O("gpt-4o")

GPT\_4O\_2024\_11\_20("gpt-4o-2024-11-20")

GPT\_4O\_2024\_08\_06("gpt-4o-2024-08-06")

GPT\_4O\_2024\_05\_13("gpt-4o-2024-05-13")

GPT\_4O\_AUDIO\_PREVIEW("gpt-4o-audio-preview")

GPT\_4O\_AUDIO\_PREVIEW\_2024\_10\_01("gpt-4o-audio-preview-2024-10-01")

GPT\_4O\_AUDIO\_PREVIEW\_2024\_12\_17("gpt-4o-audio-preview-2024-12-17")

GPT\_4O\_AUDIO\_PREVIEW\_2025\_06\_03("gpt-4o-audio-preview-2025-06-03")

GPT\_4O\_MINI\_AUDIO\_PREVIEW("gpt-4o-mini-audio-preview")

GPT\_4O\_MINI\_AUDIO\_PREVIEW\_2024\_12\_17("gpt-4o-mini-audio-preview-2024-12-17")

GPT\_4O\_SEARCH\_PREVIEW("gpt-4o-search-preview")

GPT\_4O\_MINI\_SEARCH\_PREVIEW("gpt-4o-mini-search-preview")

GPT\_4O\_SEARCH\_PREVIEW\_2025\_03\_11("gpt-4o-search-preview-2025-03-11")

GPT\_4O\_MINI\_SEARCH\_PREVIEW\_2025\_03\_11("gpt-4o-mini-search-preview-2025-03-11")

CHATGPT\_4O\_LATEST("chatgpt-4o-latest")

CODEX\_MINI\_LATEST("codex-mini-latest")

GPT\_4O\_MINI("gpt-4o-mini")

GPT\_4O\_MINI\_2024\_07\_18("gpt-4o-mini-2024-07-18")

GPT\_4\_TURBO("gpt-4-turbo")

GPT\_4\_TURBO\_2024\_04\_09("gpt-4-turbo-2024-04-09")

GPT\_4\_0125\_PREVIEW("gpt-4-0125-preview")

GPT\_4\_TURBO\_PREVIEW("gpt-4-turbo-preview")

GPT\_4\_1106\_PREVIEW("gpt-4-1106-preview")

GPT\_4\_VISION\_PREVIEW("gpt-4-vision-preview")

GPT\_4("gpt-4")

GPT\_4\_0314("gpt-4-0314")

GPT\_4\_0613("gpt-4-0613")

GPT\_4\_32K("gpt-4-32k")

GPT\_4\_32K\_0314("gpt-4-32k-0314")

GPT\_4\_32K\_0613("gpt-4-32k-0613")

GPT\_3\_5\_TURBO("gpt-3.5-turbo")

GPT\_3\_5\_TURBO\_16K("gpt-3.5-turbo-16k")

GPT\_3\_5\_TURBO\_0301("gpt-3.5-turbo-0301")

GPT\_3\_5\_TURBO\_0613("gpt-3.5-turbo-0613")

GPT\_3\_5\_TURBO\_1106("gpt-3.5-turbo-1106")

GPT\_3\_5\_TURBO\_0125("gpt-3.5-turbo-0125")

GPT\_3\_5\_TURBO\_16K\_0613("gpt-3.5-turbo-16k-0613")

O1\_PRO("o1-pro")

O1\_PRO\_2025\_03\_19("o1-pro-2025-03-19")

O3\_PRO("o3-pro")

O3\_PRO\_2025\_06\_10("o3-pro-2025-06-10")

O3\_DEEP\_RESEARCH("o3-deep-research")

O3\_DEEP\_RESEARCH\_2025\_06\_26("o3-deep-research-2025-06-26")

O4\_MINI\_DEEP\_RESEARCH("o4-mini-deep-research")

O4\_MINI\_DEEP\_RESEARCH\_2025\_06\_26("o4-mini-deep-research-2025-06-26")

COMPUTER\_USE\_PREVIEW("computer-use-preview")

COMPUTER\_USE\_PREVIEW\_2025\_03\_11("computer-use-preview-2025-03-11")

GPT\_5\_CODEX("gpt-5-codex")

GPT\_5\_PRO("gpt-5-pro")

GPT\_5\_PRO\_2025\_10\_06("gpt-5-pro-2025-10-06")

GPT\_5\_1\_CODEX\_MAX("gpt-5.1-codex-max")

JsonValue; object\_ "response"constant"response"constant

The object type of this resource - always set to `response`.

List<[BetaResponseOutputItem](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema))> output

An array of content items generated by the model.

* The length and order of items in the `output` array is dependent
  on the model’s response.
* Rather than accessing the first item in the `output` array and
  assuming it’s an `assistant` message with the content generated by
  the model, you might consider using the `output_text` property where
  supported in SDKs.

class BetaResponseOutputMessage:

An output message from the model.

String id

The unique ID of the output message.

List<Content> content

The content of the output message.

class BetaResponseOutputText:

A text output from the model.

List<Annotation> annotations

The annotations of the text output.

class FileCitation:

A citation to a file.

String fileId

The ID of the file.

String filename

The filename of the file cited.

long index

The index of the file in the list of files.

JsonValue; type "file\_citation"constant"file\_citation"constant

The type of the file citation. Always `file_citation`.

class UrlCitation:

A citation for a web resource used to generate a model response.

long endIndex

The index of the last character of the URL citation in the message.

long startIndex

The index of the first character of the URL citation in the message.

String title

The title of the web resource.

JsonValue; type "url\_citation"constant"url\_citation"constant

The type of the URL citation. Always `url_citation`.

String url

The URL of the web resource.

formaturi

class ContainerFileCitation:

A citation for a container file used to generate a model response.

String containerId

The ID of the container file.

long endIndex

The index of the last character of the container file citation in the message.

String fileId

The ID of the file.

String filename

The filename of the container file cited.

long startIndex

The index of the first character of the container file citation in the message.

JsonValue; type "container\_file\_citation"constant"container\_file\_citation"constant

The type of the container file citation. Always `container_file_citation`.

class FilePath:

A path to a file.

String fileId

The ID of the file.

long index

The index of the file in the list of files.

JsonValue; type "file\_path"constant"file\_path"constant

The type of the file path. Always `file_path`.

String text

The text output from the model.

JsonValue; type "output\_text"constant"output\_text"constant

The type of the output text. Always `output_text`.

Optional<List<Logprob>> logprobs

String token

List<long> bytes

double logprob

List<TopLogprob> topLogprobs

String token

List<long> bytes

double logprob

class BetaResponseOutputRefusal:

A refusal from the model.

String refusal

The refusal explanation from the model.

JsonValue; type "refusal"constant"refusal"constant

The type of the refusal. Always `refusal`.

JsonValue; role "assistant"constant"assistant"constant

The role of the output message. Always `assistant`.

Status status

The status of the message input. One of `in_progress`, `completed`, or
`incomplete`. Populated when input items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "message"constant"message"constant

The type of the output message. Always `message`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Phase> phase

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

COMMENTARY("commentary")

FINAL\_ANSWER("final\_answer")

class BetaResponseFileSearchToolCall:

The results of a file search tool call. See the
[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

String id

The unique ID of the file search tool call.

List<String> queries

The queries used to search for files.

Status status

The status of the file search tool call. One of `in_progress`,
`searching`, `incomplete` or `failed`,

IN\_PROGRESS("in\_progress")

SEARCHING("searching")

COMPLETED("completed")

INCOMPLETE("incomplete")

FAILED("failed")

JsonValue; type "file\_search\_call"constant"file\_search\_call"constant

The type of the file search tool call. Always `file_search_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<List<Result>> results

The results of the file search tool call.

Optional<Attributes> attributes

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

String

double

boolean

Optional<String> fileId

The unique ID of the file.

Optional<String> filename

The name of the file.

Optional<Double> score

The relevance score of the file - a value between 0 and 1.

formatfloat

Optional<String> text

The text that was retrieved from the file.

class BetaResponseFunctionToolCall:

A tool call to run a function. See the
[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

String arguments

A JSON string of the arguments to pass to the function.

String callId

The unique ID of the function tool call generated by the model.

String name

The name of the function to run.

JsonValue; type "function\_call"constant"function\_call"constant

The type of the function tool call. Always `function_call`.

Optional<String> id

The unique ID of the function tool call.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

class Program:

String callerId

The call ID of the program item that produced this tool call.

JsonValue; type "program"constant"program"constant

Optional<String> namespace

The namespace of the function to run.

Optional<Status> status

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

class BetaResponseFunctionToolCallOutputItem:

String id

The unique ID of the function call tool output.

String callId

The unique ID of the function tool call generated by the model.

Output output

The output from the function call generated by your code.
Can be a string or an list of output content.

String

List<BetaFunctionAndCustomToolCallOutput>

class BetaResponseInputText:

A text input to the model.

String text

The text input to the model.

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputImage:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail detail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

JsonValue; type "input\_image"constant"input\_image"constant

The type of the input item. Always `input_image`.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> imageUrl

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile:

A file input to the model.

JsonValue; type "input\_file"constant"input\_file"constant

The type of the input item. Always `input_file`.

Optional<Detail> detail

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

AUTO("auto")

LOW("low")

HIGH("high")

Optional<String> fileData

The content of the file to be sent to the model.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> fileUrl

The URL of the file to be sent to the model.

formaturi

Optional<String> filename

The name of the file to be sent to the model.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

Status status

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "function\_call\_output"constant"function\_call\_output"constant

The type of the function tool call output. Always `function_call_output`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

The caller type. Always `direct`.

class Program:

String callerId

The call ID of the program item that produced this tool call.

maxLength64

minLength1

JsonValue; type "program"constant"program"constant

The caller type. Always `program`.

Optional<String> createdBy

The identifier of the actor that created the item.

AgentMessage

String id

The unique ID of the agent message.

String author

The sending agent identity.

List<Content> content

Encrypted content sent between agents.

class BetaResponseInputText:

A text input to the model.

String text

The text input to the model.

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseOutputText:

A text output from the model.

List<Annotation> annotations

The annotations of the text output.

class FileCitation:

A citation to a file.

String fileId

The ID of the file.

String filename

The filename of the file cited.

long index

The index of the file in the list of files.

JsonValue; type "file\_citation"constant"file\_citation"constant

The type of the file citation. Always `file_citation`.

class UrlCitation:

A citation for a web resource used to generate a model response.

long endIndex

The index of the last character of the URL citation in the message.

long startIndex

The index of the first character of the URL citation in the message.

String title

The title of the web resource.

JsonValue; type "url\_citation"constant"url\_citation"constant

The type of the URL citation. Always `url_citation`.

String url

The URL of the web resource.

formaturi

class ContainerFileCitation:

A citation for a container file used to generate a model response.

String containerId

The ID of the container file.

long endIndex

The index of the last character of the container file citation in the message.

String fileId

The ID of the file.

String filename

The filename of the container file cited.

long startIndex

The index of the first character of the container file citation in the message.

JsonValue; type "container\_file\_citation"constant"container\_file\_citation"constant

The type of the container file citation. Always `container_file_citation`.

class FilePath:

A path to a file.

String fileId

The ID of the file.

long index

The index of the file in the list of files.

JsonValue; type "file\_path"constant"file\_path"constant

The type of the file path. Always `file_path`.

String text

The text output from the model.

JsonValue; type "output\_text"constant"output\_text"constant

The type of the output text. Always `output_text`.

Optional<List<Logprob>> logprobs

String token

List<long> bytes

double logprob

List<TopLogprob> topLogprobs

String token

List<long> bytes

double logprob

class Text:

A text content.

String text

JsonValue; type "text"constant"text"constant

class SummaryText:

A summary text from the model.

String text

A summary of the reasoning output from the model so far.

JsonValue; type "summary\_text"constant"summary\_text"constant

The type of the object. Always `summary_text`.

class ReasoningText:

Reasoning text from the model.

String text

The reasoning text from the model.

JsonValue; type "reasoning\_text"constant"reasoning\_text"constant

The type of the reasoning text. Always `reasoning_text`.

class BetaResponseOutputRefusal:

A refusal from the model.

String refusal

The refusal explanation from the model.

JsonValue; type "refusal"constant"refusal"constant

The type of the refusal. Always `refusal`.

class BetaResponseInputImage:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail detail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

JsonValue; type "input\_image"constant"input\_image"constant

The type of the input item. Always `input_image`.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> imageUrl

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class ComputerScreenshot:

A screenshot of a computer.

Detail detail

The detail level of the screenshot image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

Optional<String> fileId

The identifier of an uploaded file that contains the screenshot.

Optional<String> imageUrl

The URL of the screenshot image.

formaturi

JsonValue; type "computer\_screenshot"constant"computer\_screenshot"constant

Specifies the event type. For a computer screenshot, this property is always set to `computer_screenshot`.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile:

A file input to the model.

JsonValue; type "input\_file"constant"input\_file"constant

The type of the input item. Always `input_file`.

Optional<Detail> detail

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

AUTO("auto")

LOW("low")

HIGH("high")

Optional<String> fileData

The content of the file to be sent to the model.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> fileUrl

The URL of the file to be sent to the model.

formaturi

Optional<String> filename

The name of the file to be sent to the model.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class EncryptedContent:

Opaque encrypted content that Responses API decrypts inside trusted model execution.

String encryptedContent

Opaque encrypted content.

JsonValue; type "encrypted\_content"constant"encrypted\_content"constant

The type of the input item. Always `encrypted_content`.

String recipient

The destination agent identity.

JsonValue; type "agent\_message"constant"agent\_message"constant

The type of the item. Always `agent_message`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

MultiAgentCall

String id

The unique ID of the multi-agent call item.

Action action

The multi-agent action to execute.

SPAWN\_AGENT("spawn\_agent")

INTERRUPT\_AGENT("interrupt\_agent")

LIST\_AGENTS("list\_agents")

SEND\_MESSAGE("send\_message")

FOLLOWUP\_TASK("followup\_task")

WAIT\_AGENT("wait\_agent")

String arguments

The JSON string of arguments generated for the action.

String callId

The unique ID linking this call to its output.

JsonValue; type "multi\_agent\_call"constant"multi\_agent\_call"constant

The type of the multi-agent call. Always `multi_agent_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

MultiAgentCallOutput

String id

The unique ID of the multi-agent call output item.

Action action

The multi-agent action that produced this result.

SPAWN\_AGENT("spawn\_agent")

INTERRUPT\_AGENT("interrupt\_agent")

LIST\_AGENTS("list\_agents")

SEND\_MESSAGE("send\_message")

FOLLOWUP\_TASK("followup\_task")

WAIT\_AGENT("wait\_agent")

String callId

The unique ID of the multi-agent call.

List<[BetaResponseOutputText](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema))> output

Text output returned by the multi-agent action.

List<Annotation> annotations

The annotations of the text output.

class FileCitation:

A citation to a file.

String fileId

The ID of the file.

String filename

The filename of the file cited.

long index

The index of the file in the list of files.

JsonValue; type "file\_citation"constant"file\_citation"constant

The type of the file citation. Always `file_citation`.

class UrlCitation:

A citation for a web resource used to generate a model response.

long endIndex

The index of the last character of the URL citation in the message.

long startIndex

The index of the first character of the URL citation in the message.

String title

The title of the web resource.

JsonValue; type "url\_citation"constant"url\_citation"constant

The type of the URL citation. Always `url_citation`.

String url

The URL of the web resource.

formaturi

class ContainerFileCitation:

A citation for a container file used to generate a model response.

String containerId

The ID of the container file.

long endIndex

The index of the last character of the container file citation in the message.

String fileId

The ID of the file.

String filename

The filename of the container file cited.

long startIndex

The index of the first character of the container file citation in the message.

JsonValue; type "container\_file\_citation"constant"container\_file\_citation"constant

The type of the container file citation. Always `container_file_citation`.

class FilePath:

A path to a file.

String fileId

The ID of the file.

long index

The index of the file in the list of files.

JsonValue; type "file\_path"constant"file\_path"constant

The type of the file path. Always `file_path`.

String text

The text output from the model.

JsonValue; type "output\_text"constant"output\_text"constant

The type of the output text. Always `output_text`.

Optional<List<Logprob>> logprobs

String token

List<long> bytes

double logprob

List<TopLogprob> topLogprobs

String token

List<long> bytes

double logprob

JsonValue; type "multi\_agent\_call\_output"constant"multi\_agent\_call\_output"constant

The type of the multi-agent result. Always `multi_agent_call_output`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseFunctionWebSearch:

The results of a web search tool call. See the
[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

String id

The unique ID of the web search tool call.

Action action

An object describing the specific action taken in this web search call.
Includes details on how the model used the web (search, open\_page, find\_in\_page).

class Search:

Action type “search” - Performs a web search query.

JsonValue; type "search"constant"search"constant

The action type.

Optional<List<String>> queries

The search queries.

DeprecatedOptional<String> query

The search query.

Optional<List<Source>> sources

The sources used in the search.

JsonValue; type "url"constant"url"constant

The type of source. Always `url`.

String url

The URL of the source.

formaturi

class OpenPage:

Action type “open\_page” - Opens a specific URL from search results.

JsonValue; type "open\_page"constant"open\_page"constant

The action type.

Optional<String> url

The URL opened by the model.

formaturi

class FindInPage:

Action type “find\_in\_page”: Searches for a pattern within a loaded page.

String pattern

The pattern or text to search for within the page.

JsonValue; type "find\_in\_page"constant"find\_in\_page"constant

The action type.

String url

The URL of the page searched for the pattern.

formaturi

Status status

The status of the web search tool call.

IN\_PROGRESS("in\_progress")

SEARCHING("searching")

COMPLETED("completed")

FAILED("failed")

JsonValue; type "web\_search\_call"constant"web\_search\_call"constant

The type of the web search tool call. Always `web_search_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseComputerToolCall:

A tool call to a computer use tool. See the
[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

String id

The unique ID of the computer call.

String callId

An identifier used when responding to the tool call with output.

List<PendingSafetyCheck> pendingSafetyChecks

The pending safety checks for the computer call.

String id

The ID of the pending safety check.

Optional<String> code

The type of the pending safety check.

Optional<String> message

Details about the pending safety check.

Status status

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

Type type

The type of the computer call. Always `computer_call`.

Optional<[BetaComputerAction](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action%20%3E%20(schema))> action

A click action.

Click

Button button

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

LEFT("left")

RIGHT("right")

WHEEL("wheel")

BACK("back")

FORWARD("forward")

JsonValue; type "click"constant"click"constant

Specifies the event type. For a click action, this property is always `click`.

long x

The x-coordinate where the click occurred.

long y

The y-coordinate where the click occurred.

Optional<List<String>> keys

The keys being held while clicking.

DoubleClick

Optional<List<String>> keys

The keys being held while double-clicking.

JsonValue; type "double\_click"constant"double\_click"constant

Specifies the event type. For a double click action, this property is always set to `double_click`.

long x

The x-coordinate where the double click occurred.

long y

The y-coordinate where the double click occurred.

Drag

List<Path> path

An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

[
  { x: 100, y: 200 },
  { x: 200, y: 300 }
]

long x

The x-coordinate.

long y

The y-coordinate.

JsonValue; type "drag"constant"drag"constant

Specifies the event type. For a drag action, this property is always set to `drag`.

Optional<List<String>> keys

The keys being held while dragging the mouse.

Keypress

List<String> keys

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

JsonValue; type "keypress"constant"keypress"constant

Specifies the event type. For a keypress action, this property is always set to `keypress`.

Move

JsonValue; type "move"constant"move"constant

Specifies the event type. For a move action, this property is always set to `move`.

long x

The x-coordinate to move to.

long y

The y-coordinate to move to.

Optional<List<String>> keys

The keys being held while moving the mouse.

JsonValue;

JsonValue; type "screenshot"constant"screenshot"constant

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

Scroll

long scrollX

The horizontal scroll distance.

long scrollY

The vertical scroll distance.

JsonValue; type "scroll"constant"scroll"constant

Specifies the event type. For a scroll action, this property is always set to `scroll`.

long x

The x-coordinate where the scroll occurred.

long y

The y-coordinate where the scroll occurred.

Optional<List<String>> keys

The keys being held while scrolling.

Type

String text

The text to type.

JsonValue; type "type"constant"type"constant

Specifies the event type. For a type action, this property is always set to `type`.

JsonValue;

JsonValue; type "wait"constant"wait"constant

Specifies the event type. For a wait action, this property is always set to `wait`.

Optional<List<[BetaComputerAction](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action%20%3E%20(schema))>> actions

Flattened batched actions for `computer_use`. Each action includes an
`type` discriminator and action-specific fields.

Click

Button button

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

LEFT("left")

RIGHT("right")

WHEEL("wheel")

BACK("back")

FORWARD("forward")

JsonValue; type "click"constant"click"constant

Specifies the event type. For a click action, this property is always `click`.

long x

The x-coordinate where the click occurred.

long y

The y-coordinate where the click occurred.

Optional<List<String>> keys

The keys being held while clicking.

DoubleClick

Optional<List<String>> keys

The keys being held while double-clicking.

JsonValue; type "double\_click"constant"double\_click"constant

Specifies the event type. For a double click action, this property is always set to `double_click`.

long x

The x-coordinate where the double click occurred.

long y

The y-coordinate where the double click occurred.

Drag

List<Path> path

An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

[
  { x: 100, y: 200 },
  { x: 200, y: 300 }
]

long x

The x-coordinate.

long y

The y-coordinate.

JsonValue; type "drag"constant"drag"constant

Specifies the event type. For a drag action, this property is always set to `drag`.

Optional<List<String>> keys

The keys being held while dragging the mouse.

Keypress

List<String> keys

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

JsonValue; type "keypress"constant"keypress"constant

Specifies the event type. For a keypress action, this property is always set to `keypress`.

Move

JsonValue; type "move"constant"move"constant

Specifies the event type. For a move action, this property is always set to `move`.

long x

The x-coordinate to move to.

long y

The y-coordinate to move to.

Optional<List<String>> keys

The keys being held while moving the mouse.

JsonValue;

JsonValue; type "screenshot"constant"screenshot"constant

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

Scroll

long scrollX

The horizontal scroll distance.

long scrollY

The vertical scroll distance.

JsonValue; type "scroll"constant"scroll"constant

Specifies the event type. For a scroll action, this property is always set to `scroll`.

long x

The x-coordinate where the scroll occurred.

long y

The y-coordinate where the scroll occurred.

Optional<List<String>> keys

The keys being held while scrolling.

Type

String text

The text to type.

JsonValue; type "type"constant"type"constant

Specifies the event type. For a type action, this property is always set to `type`.

JsonValue;

JsonValue; type "wait"constant"wait"constant

Specifies the event type. For a wait action, this property is always set to `wait`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseComputerToolCallOutputItem:

String id

The unique ID of the computer call tool output.

String callId

The ID of the computer tool call that produced the output.

[BetaResponseComputerToolCallOutputScreenshot](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema)) output

A computer screenshot image used with the computer use tool.

JsonValue; type "computer\_screenshot"constant"computer\_screenshot"constant

Specifies the event type. For a computer screenshot, this property is
always set to `computer_screenshot`.

Optional<String> fileId

The identifier of an uploaded file that contains the screenshot.

Optional<String> imageUrl

The URL of the screenshot image.

formaturi

Status status

The status of the message input. One of `in_progress`, `completed`, or
`incomplete`. Populated when input items are returned via API.

COMPLETED("completed")

INCOMPLETE("incomplete")

FAILED("failed")

IN\_PROGRESS("in\_progress")

JsonValue; type "computer\_call\_output"constant"computer\_call\_output"constant

The type of the computer tool call output. Always `computer_call_output`.

Optional<List<AcknowledgedSafetyCheck>> acknowledgedSafetyChecks

The safety checks reported by the API that have been acknowledged by the
developer.

String id

The ID of the pending safety check.

Optional<String> code

The type of the pending safety check.

Optional<String> message

Details about the pending safety check.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<String> createdBy

The identifier of the actor that created the item.

class BetaResponseReasoningItem:

A description of the chain of thought used by a reasoning model while generating
a response. Be sure to include these items in your `input` to the Responses API
for subsequent turns of a conversation if you are manually
[managing context](https://platform.openai.com/docs/guides/conversation-state).

String id

The unique identifier of the reasoning content.

List<Summary> summary

Reasoning summary content.

String text

A summary of the reasoning output from the model so far.

JsonValue; type "summary\_text"constant"summary\_text"constant

The type of the object. Always `summary_text`.

JsonValue; type "reasoning"constant"reasoning"constant

The type of the object. Always `reasoning`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<List<Content>> content

Reasoning text content.

String text

The reasoning text from the model.

JsonValue; type "reasoning\_text"constant"reasoning\_text"constant

The type of the reasoning text. Always `reasoning_text`.

Optional<String> encryptedContent

The encrypted content of the reasoning item. This is populated by default
for reasoning items returned by `POST /v1/responses` and WebSocket
`response.create` requests.

Optional<Status> status

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

Program

String id

The unique ID of the program item.

String callId

The stable call ID of the program item.

String code

The JavaScript source executed by programmatic tool calling.

String fingerprint

Opaque program replay fingerprint that must be round-tripped.

JsonValue; type "program"constant"program"constant

The type of the item. Always `program`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

ProgramOutput

String id

The unique ID of the program output item.

String callId

The call ID of the program item.

String result

The result produced by the program item.

Status status

The terminal status of the program output item.

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "program\_output"constant"program\_output"constant

The type of the item. Always `program_output`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseToolSearchCall:

String id

The unique ID of the tool search call item.

JsonValue arguments

Arguments used for the tool search call.

Optional<String> callId

The unique ID of the tool search call generated by the model.

Execution execution

Whether tool search was executed by the server or by the client.

SERVER("server")

CLIENT("client")

Status status

The status of the tool search call item that was recorded.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "tool\_search\_call"constant"tool\_search\_call"constant

The type of the item. Always `tool_search_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<String> createdBy

The identifier of the actor that created the item.

class BetaResponseToolSearchOutputItem:

String id

The unique ID of the tool search output item.

Optional<String> callId

The unique ID of the tool search call generated by the model.

Execution execution

Whether tool search was executed by the server or by the client.

SERVER("server")

CLIENT("client")

Status status

The status of the tool search output item that was recorded.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

List<[BetaTool](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))> tools

The loaded tool definitions returned by tool search.

class BetaFunctionTool:

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

String name

The name of the function to call.

Optional<Parameters> parameters

A JSON schema object describing the parameters of the function.

Optional<Boolean> strict

Whether strict parameter validation is enforced for this function tool.

JsonValue; type "function"constant"function"constant

The type of the function tool. Always `function`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this function is deferred and loaded via tool search.

Optional<String> description

A description of the function. Used by the model to determine whether or not to call the function.

Optional<OutputSchema> outputSchema

A JSON schema object describing the JSON value encoded in string outputs for this function.

class BetaFileSearchTool:

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

JsonValue; type "file\_search"constant"file\_search"constant

The type of the file search tool. Always `file_search`.

List<String> vectorStoreIds

The IDs of the vector stores to search.

Optional<Filters> filters

A filter to apply.

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

String

double

boolean

List<ComparisonFilterValueItem>

String

double

class CompoundFilter:

Combine multiple filters using `and` or `or`.

List<Filter> filters

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

String

double

boolean

List<ComparisonFilterValueItem>

String

double

JsonValue

Type type

Type of operation: `and` or `or`.

AND("and")

OR("or")

Optional<Long> maxNumResults

The maximum number of results to return. This number should be between 1 and 50 inclusive.

Optional<RankingOptions> rankingOptions

Ranking options for search.

Optional<HybridSearch> hybridSearch

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

double embeddingWeight

The weight of the embedding in the reciprocal ranking fusion.

double textWeight

The weight of the text in the reciprocal ranking fusion.

Optional<Ranker> ranker

The ranker to use for the file search.

AUTO("auto")

DEFAULT\_2024\_11\_15("default-2024-11-15")

Optional<Double> scoreThreshold

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class BetaComputerTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

JsonValue; type "computer"constant"computer"constant

The type of the computer tool. Always `computer`.

class BetaComputerUsePreviewTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

long displayHeight

The height of the computer display.

long displayWidth

The width of the computer display.

Environment environment

The type of computer environment to control.

WINDOWS("windows")

MAC("mac")

LINUX("linux")

UBUNTU("ubuntu")

BROWSER("browser")

JsonValue; type "computer\_use\_preview"constant"computer\_use\_preview"constant

The type of the computer use tool. Always `computer_use_preview`.

class BetaWebSearchTool:

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

WEB\_SEARCH("web\_search")

WEB\_SEARCH\_2025\_08\_26("web\_search\_2025\_08\_26")

Optional<Filters> filters

Filters for the search.

Optional<List<String>> allowedDomains

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The approximate location of the user.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

Optional<Type> type

The type of location approximation. Always `approximate`.

Mcp

String serverLabel

A label for this MCP server, used to identify it in tool calls.

JsonValue; type "mcp"constant"mcp"constant

The type of the MCP tool. Always `mcp`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<AllowedTools> allowedTools

List of allowed tool names or a filter object.

List<String>

class McpToolFilter:

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<String> authorization

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

Optional<ConnectorId> connectorId

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

CONNECTOR\_DROPBOX("connector\_dropbox")

CONNECTOR\_GMAIL("connector\_gmail")

CONNECTOR\_GOOGLECALENDAR("connector\_googlecalendar")

CONNECTOR\_GOOGLEDRIVE("connector\_googledrive")

CONNECTOR\_MICROSOFTTEAMS("connector\_microsoftteams")

CONNECTOR\_OUTLOOKCALENDAR("connector\_outlookcalendar")

CONNECTOR\_OUTLOOKEMAIL("connector\_outlookemail")

CONNECTOR\_SHAREPOINT("connector\_sharepoint")

Optional<Boolean> deferLoading

Whether this MCP tool is deferred and discovered via tool search.

Optional<Headers> headers

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

Optional<RequireApproval> requireApproval

Specify which of the MCP server’s tools require approval.

class McpToolApprovalFilter:

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

Optional<Always> always

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<Never> never

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

enum McpToolApprovalSetting:

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

ALWAYS("always")

NEVER("never")

Optional<String> serverDescription

Optional description of the MCP server, used to provide more context.

Optional<String> serverUrl

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

Optional<String> tunnelId

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter

Container container

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

String

class CodeInterpreterToolAuto:

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

JsonValue; type "auto"constant"auto"constant

Always `auto`.

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the code interpreter container.

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

JsonValue; type "code\_interpreter"constant"code\_interpreter"constant

The type of the code interpreter tool. Always `code_interpreter`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

JsonValue;

JsonValue; type "programmatic\_tool\_calling"constant"programmatic\_tool\_calling"constant

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration

JsonValue; type "image\_generation"constant"image\_generation"constant

The type of the image generation tool. Always `image_generation`.

Optional<Action> action

Whether to generate a new image or edit an existing image. Default: `auto`.

GENERATE("generate")

EDIT("edit")

AUTO("auto")

Optional<Background> background

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

TRANSPARENT("transparent")

OPAQUE("opaque")

AUTO("auto")

Optional<InputFidelity> inputFidelity

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

HIGH("high")

LOW("low")

Optional<InputImageMask> inputImageMask

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

Optional<String> fileId

File ID for the mask image.

Optional<String> imageUrl

Base64-encoded mask image.

Optional<Model> model

The image generation model to use. Default: `gpt-image-1`.

GPT\_IMAGE\_1("gpt-image-1")

GPT\_IMAGE\_1\_MINI("gpt-image-1-mini")

GPT\_IMAGE\_2("gpt-image-2")

GPT\_IMAGE\_2\_2026\_04\_21("gpt-image-2-2026-04-21")

GPT\_IMAGE\_1\_5("gpt-image-1.5")

CHATGPT\_IMAGE\_LATEST("chatgpt-image-latest")

Optional<Moderation> moderation

Moderation level for the generated image. Default: `auto`.

AUTO("auto")

LOW("low")

Optional<Long> outputCompression

Compression level for the output image. Default: 100.

minimum0

maximum100

Optional<OutputFormat> outputFormat

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

PNG("png")

WEBP("webp")

JPEG("jpeg")

Optional<Long> partialImages

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

Optional<Quality> quality

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

LOW("low")

MEDIUM("medium")

HIGH("high")

AUTO("auto")

Optional<Size> size

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

\_1024X1024("1024x1024")

\_1024X1536("1024x1536")

\_1536X1024("1536x1024")

AUTO("auto")

JsonValue;

JsonValue; type "local\_shell"constant"local\_shell"constant

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool:

A tool that allows the model to execute shell commands.

JsonValue; type "shell"constant"shell"constant

The type of the shell tool. Always `shell`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Environment> environment

class BetaContainerAuto:

JsonValue; type "container\_auto"constant"container\_auto"constant

Automatically creates a container for this request

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the container.

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

Optional<List<Skill>> skills

An optional list of skills referenced by id or inline data.

class BetaSkillReference:

String skillId

The ID of the referenced skill.

maxLength64

minLength1

JsonValue; type "skill\_reference"constant"skill\_reference"constant

References a skill created with the /v1/skills endpoint.

Optional<String> version

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class BetaInlineSkill:

String description

The description of the skill.

String name

The name of the skill.

[BetaInlineSkillSource](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) source

Inline skill payload

String data

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

JsonValue; mediaType "application/zip"constant"application/zip"constant

The media type of the inline skill payload. Must be `application/zip`.

JsonValue; type "base64"constant"base64"constant

The type of the inline skill source. Must be `base64`.

JsonValue; type "inline"constant"inline"constant

Defines an inline skill for this request.

class BetaLocalEnvironment:

JsonValue; type "local"constant"local"constant

Use a local computer environment.

Optional<List<[BetaLocalSkill](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))>> skills

An optional list of skills.

String description

The description of the skill.

String name

The name of the skill.

String path

The path to the directory containing the skill.

class BetaContainerReference:

String containerId

The ID of the referenced container.

JsonValue; type "container\_reference"constant"container\_reference"constant

References a container created with the /v1/containers endpoint

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<Format> format

The input format for the custom tool. Default is unconstrained text.

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

A grammar defined by the user.

String definition

The grammar definition.

Syntax syntax

The syntax of the grammar definition. One of `lark` or `regex`.

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

Grammar format. Always `grammar`.

class BetaNamespaceTool:

Groups function/custom tools under a shared namespace.

String description

A description of the namespace shown to the model.

minLength1

String name

The namespace name used in tool calls (for example, `crm`).

minLength1

List<Tool> tools

The function/custom tools available inside this namespace.

class Function:

String name

maxLength128

minLength1

JsonValue; type "function"constant"function"constant

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this function should be deferred and discovered via tool search.

Optional<String> description

Optional<OutputSchema> outputSchema

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

Optional<JsonValue> parameters

Optional<Boolean> strict

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<Format> format

The input format for the custom tool. Default is unconstrained text.

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

A grammar defined by the user.

String definition

The grammar definition.

Syntax syntax

The syntax of the grammar definition. One of `lark` or `regex`.

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

Grammar format. Always `grammar`.

JsonValue; type "namespace"constant"namespace"constant

The type of the tool. Always `namespace`.

class BetaToolSearchTool:

Hosted or BYOT tool search configuration for deferred tools.

JsonValue; type "tool\_search"constant"tool\_search"constant

The type of the tool. Always `tool_search`.

Optional<String> description

Description shown to the model for a client-executed tool search tool.

Optional<Execution> execution

Whether tool search is executed by the server or by the client.

SERVER("server")

CLIENT("client")

Optional<JsonValue> parameters

Parameter schema for a client-executed tool search tool.

class BetaWebSearchPreviewTool:

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

WEB\_SEARCH\_PREVIEW("web\_search\_preview")

WEB\_SEARCH\_PREVIEW\_2025\_03\_11("web\_search\_preview\_2025\_03\_11")

Optional<List<SearchContentType>> searchContentTypes

TEXT("text")

IMAGE("image")

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The user’s location.

JsonValue; type "approximate"constant"approximate"constant

The type of location approximation. Always `approximate`.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

class BetaApplyPatchTool:

Allows the assistant to create, delete, or update files using unified diffs.

JsonValue; type "apply\_patch"constant"apply\_patch"constant

The type of the tool. Always `apply_patch`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

JsonValue; type "tool\_search\_output"constant"tool\_search\_output"constant

The type of the item. Always `tool_search_output`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<String> createdBy

The identifier of the actor that created the item.

AdditionalTools

String id

The unique ID of the additional tools item.

Role role

The role that provided the additional tools.

UNKNOWN("unknown")

USER("user")

ASSISTANT("assistant")

SYSTEM("system")

CRITIC("critic")

DISCRIMINATOR("discriminator")

DEVELOPER("developer")

TOOL("tool")

List<[BetaTool](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))> tools

The additional tool definitions made available at this item.

class BetaFunctionTool:

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

String name

The name of the function to call.

Optional<Parameters> parameters

A JSON schema object describing the parameters of the function.

Optional<Boolean> strict

Whether strict parameter validation is enforced for this function tool.

JsonValue; type "function"constant"function"constant

The type of the function tool. Always `function`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this function is deferred and loaded via tool search.

Optional<String> description

A description of the function. Used by the model to determine whether or not to call the function.

Optional<OutputSchema> outputSchema

A JSON schema object describing the JSON value encoded in string outputs for this function.

class BetaFileSearchTool:

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

JsonValue; type "file\_search"constant"file\_search"constant

The type of the file search tool. Always `file_search`.

List<String> vectorStoreIds

The IDs of the vector stores to search.

Optional<Filters> filters

A filter to apply.

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

String

double

boolean

List<ComparisonFilterValueItem>

String

double

class CompoundFilter:

Combine multiple filters using `and` or `or`.

List<Filter> filters

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

String

double

boolean

List<ComparisonFilterValueItem>

String

double

JsonValue

Type type

Type of operation: `and` or `or`.

AND("and")

OR("or")

Optional<Long> maxNumResults

The maximum number of results to return. This number should be between 1 and 50 inclusive.

Optional<RankingOptions> rankingOptions

Ranking options for search.

Optional<HybridSearch> hybridSearch

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

double embeddingWeight

The weight of the embedding in the reciprocal ranking fusion.

double textWeight

The weight of the text in the reciprocal ranking fusion.

Optional<Ranker> ranker

The ranker to use for the file search.

AUTO("auto")

DEFAULT\_2024\_11\_15("default-2024-11-15")

Optional<Double> scoreThreshold

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class BetaComputerTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

JsonValue; type "computer"constant"computer"constant

The type of the computer tool. Always `computer`.

class BetaComputerUsePreviewTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

long displayHeight

The height of the computer display.

long displayWidth

The width of the computer display.

Environment environment

The type of computer environment to control.

WINDOWS("windows")

MAC("mac")

LINUX("linux")

UBUNTU("ubuntu")

BROWSER("browser")

JsonValue; type "computer\_use\_preview"constant"computer\_use\_preview"constant

The type of the computer use tool. Always `computer_use_preview`.

class BetaWebSearchTool:

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

WEB\_SEARCH("web\_search")

WEB\_SEARCH\_2025\_08\_26("web\_search\_2025\_08\_26")

Optional<Filters> filters

Filters for the search.

Optional<List<String>> allowedDomains

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The approximate location of the user.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

Optional<Type> type

The type of location approximation. Always `approximate`.

Mcp

String serverLabel

A label for this MCP server, used to identify it in tool calls.

JsonValue; type "mcp"constant"mcp"constant

The type of the MCP tool. Always `mcp`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<AllowedTools> allowedTools

List of allowed tool names or a filter object.

List<String>

class McpToolFilter:

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<String> authorization

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

Optional<ConnectorId> connectorId

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

CONNECTOR\_DROPBOX("connector\_dropbox")

CONNECTOR\_GMAIL("connector\_gmail")

CONNECTOR\_GOOGLECALENDAR("connector\_googlecalendar")

CONNECTOR\_GOOGLEDRIVE("connector\_googledrive")

CONNECTOR\_MICROSOFTTEAMS("connector\_microsoftteams")

CONNECTOR\_OUTLOOKCALENDAR("connector\_outlookcalendar")

CONNECTOR\_OUTLOOKEMAIL("connector\_outlookemail")

CONNECTOR\_SHAREPOINT("connector\_sharepoint")

Optional<Boolean> deferLoading

Whether this MCP tool is deferred and discovered via tool search.

Optional<Headers> headers

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

Optional<RequireApproval> requireApproval

Specify which of the MCP server’s tools require approval.

class McpToolApprovalFilter:

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

Optional<Always> always

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<Never> never

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

enum McpToolApprovalSetting:

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

ALWAYS("always")

NEVER("never")

Optional<String> serverDescription

Optional description of the MCP server, used to provide more context.

Optional<String> serverUrl

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

Optional<String> tunnelId

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter

Container container

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

String

class CodeInterpreterToolAuto:

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

JsonValue; type "auto"constant"auto"constant

Always `auto`.

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the code interpreter container.

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

JsonValue; type "code\_interpreter"constant"code\_interpreter"constant

The type of the code interpreter tool. Always `code_interpreter`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

JsonValue;

JsonValue; type "programmatic\_tool\_calling"constant"programmatic\_tool\_calling"constant

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration

JsonValue; type "image\_generation"constant"image\_generation"constant

The type of the image generation tool. Always `image_generation`.

Optional<Action> action

Whether to generate a new image or edit an existing image. Default: `auto`.

GENERATE("generate")

EDIT("edit")

AUTO("auto")

Optional<Background> background

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

TRANSPARENT("transparent")

OPAQUE("opaque")

AUTO("auto")

Optional<InputFidelity> inputFidelity

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

HIGH("high")

LOW("low")

Optional<InputImageMask> inputImageMask

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

Optional<String> fileId

File ID for the mask image.

Optional<String> imageUrl

Base64-encoded mask image.

Optional<Model> model

The image generation model to use. Default: `gpt-image-1`.

GPT\_IMAGE\_1("gpt-image-1")

GPT\_IMAGE\_1\_MINI("gpt-image-1-mini")

GPT\_IMAGE\_2("gpt-image-2")

GPT\_IMAGE\_2\_2026\_04\_21("gpt-image-2-2026-04-21")

GPT\_IMAGE\_1\_5("gpt-image-1.5")

CHATGPT\_IMAGE\_LATEST("chatgpt-image-latest")

Optional<Moderation> moderation

Moderation level for the generated image. Default: `auto`.

AUTO("auto")

LOW("low")

Optional<Long> outputCompression

Compression level for the output image. Default: 100.

minimum0

maximum100

Optional<OutputFormat> outputFormat

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

PNG("png")

WEBP("webp")

JPEG("jpeg")

Optional<Long> partialImages

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

Optional<Quality> quality

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

LOW("low")

MEDIUM("medium")

HIGH("high")

AUTO("auto")

Optional<Size> size

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

\_1024X1024("1024x1024")

\_1024X1536("1024x1536")

\_1536X1024("1536x1024")

AUTO("auto")

JsonValue;

JsonValue; type "local\_shell"constant"local\_shell"constant

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool:

A tool that allows the model to execute shell commands.

JsonValue; type "shell"constant"shell"constant

The type of the shell tool. Always `shell`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Environment> environment

class BetaContainerAuto:

JsonValue; type "container\_auto"constant"container\_auto"constant

Automatically creates a container for this request

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the container.

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

Optional<List<Skill>> skills

An optional list of skills referenced by id or inline data.

class BetaSkillReference:

String skillId

The ID of the referenced skill.

maxLength64

minLength1

JsonValue; type "skill\_reference"constant"skill\_reference"constant

References a skill created with the /v1/skills endpoint.

Optional<String> version

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class BetaInlineSkill:

String description

The description of the skill.

String name

The name of the skill.

[BetaInlineSkillSource](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) source

Inline skill payload

String data

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

JsonValue; mediaType "application/zip"constant"application/zip"constant

The media type of the inline skill payload. Must be `application/zip`.

JsonValue; type "base64"constant"base64"constant

The type of the inline skill source. Must be `base64`.

JsonValue; type "inline"constant"inline"constant

Defines an inline skill for this request.

class BetaLocalEnvironment:

JsonValue; type "local"constant"local"constant

Use a local computer environment.

Optional<List<[BetaLocalSkill](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))>> skills

An optional list of skills.

String description

The description of the skill.

String name

The name of the skill.

String path

The path to the directory containing the skill.

class BetaContainerReference:

String containerId

The ID of the referenced container.

JsonValue; type "container\_reference"constant"container\_reference"constant

References a container created with the /v1/containers endpoint

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<Format> format

The input format for the custom tool. Default is unconstrained text.

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

A grammar defined by the user.

String definition

The grammar definition.

Syntax syntax

The syntax of the grammar definition. One of `lark` or `regex`.

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

Grammar format. Always `grammar`.

class BetaNamespaceTool:

Groups function/custom tools under a shared namespace.

String description

A description of the namespace shown to the model.

minLength1

String name

The namespace name used in tool calls (for example, `crm`).

minLength1

List<Tool> tools

The function/custom tools available inside this namespace.

class Function:

String name

maxLength128

minLength1

JsonValue; type "function"constant"function"constant

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this function should be deferred and discovered via tool search.

Optional<String> description

Optional<OutputSchema> outputSchema

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

Optional<JsonValue> parameters

Optional<Boolean> strict

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<Format> format

The input format for the custom tool. Default is unconstrained text.

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

A grammar defined by the user.

String definition

The grammar definition.

Syntax syntax

The syntax of the grammar definition. One of `lark` or `regex`.

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

Grammar format. Always `grammar`.

JsonValue; type "namespace"constant"namespace"constant

The type of the tool. Always `namespace`.

class BetaToolSearchTool:

Hosted or BYOT tool search configuration for deferred tools.

JsonValue; type "tool\_search"constant"tool\_search"constant

The type of the tool. Always `tool_search`.

Optional<String> description

Description shown to the model for a client-executed tool search tool.

Optional<Execution> execution

Whether tool search is executed by the server or by the client.

SERVER("server")

CLIENT("client")

Optional<JsonValue> parameters

Parameter schema for a client-executed tool search tool.

class BetaWebSearchPreviewTool:

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

WEB\_SEARCH\_PREVIEW("web\_search\_preview")

WEB\_SEARCH\_PREVIEW\_2025\_03\_11("web\_search\_preview\_2025\_03\_11")

Optional<List<SearchContentType>> searchContentTypes

TEXT("text")

IMAGE("image")

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The user’s location.

JsonValue; type "approximate"constant"approximate"constant

The type of location approximation. Always `approximate`.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

class BetaApplyPatchTool:

Allows the assistant to create, delete, or update files using unified diffs.

JsonValue; type "apply\_patch"constant"apply\_patch"constant

The type of the tool. Always `apply_patch`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

JsonValue; type "additional\_tools"constant"additional\_tools"constant

The type of the item. Always `additional_tools`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseCompactionItem:

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

String id

The unique ID of the compaction item.

String encryptedContent

The encrypted content that was produced by compaction.

JsonValue; type "compaction"constant"compaction"constant

The type of the item. Always `compaction`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<String> createdBy

The identifier of the actor that created the item.

ImageGenerationCall

String id

The unique ID of the image generation call.

Optional<String> result

The generated image encoded in base64.

Status status

The status of the image generation call.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

GENERATING("generating")

FAILED("failed")

JsonValue; type "image\_generation\_call"constant"image\_generation\_call"constant

The type of the image generation call. Always `image_generation_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseCodeInterpreterToolCall:

A tool call to run code.

String id

The unique ID of the code interpreter tool call.

Optional<String> code

The code to run, or null if not available.

String containerId

The ID of the container used to run the code.

Optional<List<Output>> outputs

The outputs generated by the code interpreter, such as logs or images.
Can be null if no outputs are available.

class Logs:

The logs output from the code interpreter.

String logs

The logs output from the code interpreter.

JsonValue; type "logs"constant"logs"constant

The type of the output. Always `logs`.

class Image:

The image output from the code interpreter.

JsonValue; type "image"constant"image"constant

The type of the output. Always `image`.

String url

The URL of the image output from the code interpreter.

formaturi

Status status

The status of the code interpreter tool call. Valid values are `in_progress`, `completed`, `incomplete`, `interpreting`, and `failed`.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

INTERPRETING("interpreting")

FAILED("failed")

JsonValue; type "code\_interpreter\_call"constant"code\_interpreter\_call"constant

The type of the code interpreter tool call. Always `code_interpreter_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

LocalShellCall

String id

The unique ID of the local shell call.

Action action

Execute a shell command on the server.

List<String> command

The command to run.

Env env

Environment variables to set for the command.

JsonValue; type "exec"constant"exec"constant

The type of the local shell action. Always `exec`.

Optional<Long> timeoutMs

Optional timeout in milliseconds for the command.

Optional<String> user

Optional user to run the command as.

Optional<String> workingDirectory

Optional working directory to run the command in.

String callId

The unique ID of the local shell tool call generated by the model.

Status status

The status of the local shell call.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "local\_shell\_call"constant"local\_shell\_call"constant

The type of the local shell call. Always `local_shell_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

LocalShellCallOutput

String id

The unique ID of the local shell tool call generated by the model.

String output

A JSON string of the output of the local shell tool call.

JsonValue; type "local\_shell\_call\_output"constant"local\_shell\_call\_output"constant

The type of the local shell tool call output. Always `local_shell_call_output`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Status> status

The status of the item. One of `in_progress`, `completed`, or `incomplete`.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

class BetaResponseFunctionShellToolCall:

A tool call that executes one or more shell commands in a managed environment.

String id

The unique ID of the shell tool call. Populated when this item is returned via API.

Action action

The shell commands and limits that describe how to run the tool call.

List<String> commands

Optional<Long> maxOutputLength

Optional maximum number of characters to return from each command.

Optional<Long> timeoutMs

Optional timeout in milliseconds for the commands.

String callId

The unique ID of the shell tool call generated by the model.

Optional<Environment> environment

Represents the use of a local environment to perform shell actions.

class BetaResponseLocalEnvironment:

Represents the use of a local environment to perform shell actions.

JsonValue; type "local"constant"local"constant

The environment type. Always `local`.

class BetaResponseContainerReference:

Represents a container created with /v1/containers.

String containerId

JsonValue; type "container\_reference"constant"container\_reference"constant

The environment type. Always `container_reference`.

Status status

The status of the shell call. One of `in_progress`, `completed`, or `incomplete`.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "shell\_call"constant"shell\_call"constant

The type of the item. Always `shell_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

class Program:

String callerId

The call ID of the program item that produced this tool call.

JsonValue; type "program"constant"program"constant

Optional<String> createdBy

The ID of the entity that created this tool call.

class BetaResponseFunctionShellToolCallOutput:

The output of a shell tool call that was emitted.

String id

The unique ID of the shell call output. Populated when this item is returned via API.

String callId

The unique ID of the shell tool call generated by the model.

Optional<Long> maxOutputLength

The maximum length of the shell command output. This is generated by the model and should be passed back with the raw output.

List<Output> output

An array of shell call output contents

Outcome outcome

Represents either an exit outcome (with an exit code) or a timeout outcome for a shell call output chunk.

JsonValue;

JsonValue; type "timeout"constant"timeout"constant

The outcome type. Always `timeout`.

class Exit:

Indicates that the shell commands finished and returned an exit code.

long exitCode

Exit code from the shell process.

JsonValue; type "exit"constant"exit"constant

The outcome type. Always `exit`.

String stderr

The standard error output that was captured.

String stdout

The standard output that was captured.

Optional<String> createdBy

The identifier of the actor that created the item.

Status status

The status of the shell call output. One of `in_progress`, `completed`, or `incomplete`.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "shell\_call\_output"constant"shell\_call\_output"constant

The type of the shell call output. Always `shell_call_output`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

class Program:

String callerId

The call ID of the program item that produced this tool call.

JsonValue; type "program"constant"program"constant

Optional<String> createdBy

The identifier of the actor that created the item.

class BetaResponseApplyPatchToolCall:

A tool call that applies file diffs by creating, deleting, or updating files.

String id

The unique ID of the apply patch tool call. Populated when this item is returned via API.

String callId

The unique ID of the apply patch tool call generated by the model.

Operation operation

One of the create\_file, delete\_file, or update\_file operations applied via apply\_patch.

class CreateFile:

Instruction describing how to create a file via the apply\_patch tool.

String diff

Diff to apply.

String path

Path of the file to create.

JsonValue; type "create\_file"constant"create\_file"constant

Create a new file with the provided diff.

class DeleteFile:

Instruction describing how to delete a file via the apply\_patch tool.

String path

Path of the file to delete.

JsonValue; type "delete\_file"constant"delete\_file"constant

Delete the specified file.

class UpdateFile:

Instruction describing how to update a file via the apply\_patch tool.

String diff

Diff to apply.

String path

Path of the file to update.

JsonValue; type "update\_file"constant"update\_file"constant

Update an existing file with the provided diff.

Status status

The status of the apply patch tool call. One of `in_progress` or `completed`.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

JsonValue; type "apply\_patch\_call"constant"apply\_patch\_call"constant

The type of the item. Always `apply_patch_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

class Program:

String callerId

The call ID of the program item that produced this tool call.

JsonValue; type "program"constant"program"constant

Optional<String> createdBy

The ID of the entity that created this tool call.

class BetaResponseApplyPatchToolCallOutput:

The output emitted by an apply patch tool call.

String id

The unique ID of the apply patch tool call output. Populated when this item is returned via API.

String callId

The unique ID of the apply patch tool call generated by the model.

Status status

The status of the apply patch tool call output. One of `completed` or `failed`.

COMPLETED("completed")

FAILED("failed")

JsonValue; type "apply\_patch\_call\_output"constant"apply\_patch\_call\_output"constant

The type of the item. Always `apply_patch_call_output`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

class Program:

String callerId

The call ID of the program item that produced this tool call.

JsonValue; type "program"constant"program"constant

Optional<String> createdBy

The ID of the entity that created this tool call output.

Optional<String> output

Optional textual output returned by the apply patch tool.

McpCall

String id

The unique ID of the tool call.

String arguments

A JSON string of the arguments passed to the tool.

String name

The name of the tool that was run.

String serverLabel

The label of the MCP server running the tool.

JsonValue; type "mcp\_call"constant"mcp\_call"constant

The type of the item. Always `mcp_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<String> approvalRequestId

Unique identifier for the MCP tool call approval request.
Include this value in a subsequent `mcp_approval_response` input to approve or reject the corresponding tool call.

Optional<String> error

The error from the tool call, if any.

Optional<String> output

The output from the tool call.

Optional<Status> status

The status of the tool call. One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

CALLING("calling")

FAILED("failed")

McpListTools

String id

The unique ID of the list.

String serverLabel

The label of the MCP server.

List<Tool> tools

The tools available on the server.

JsonValue inputSchema

The JSON schema describing the tool’s input.

String name

The name of the tool.

Optional<JsonValue> annotations

Additional annotations about the tool.

Optional<String> description

The description of the tool.

JsonValue; type "mcp\_list\_tools"constant"mcp\_list\_tools"constant

The type of the item. Always `mcp_list_tools`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<String> error

Error message if the server could not list tools.

McpApprovalRequest

String id

The unique ID of the approval request.

String arguments

A JSON string of arguments for the tool.

String name

The name of the tool to run.

String serverLabel

The label of the MCP server making the request.

JsonValue; type "mcp\_approval\_request"constant"mcp\_approval\_request"constant

The type of the item. Always `mcp_approval_request`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

McpApprovalResponse

String id

The unique ID of the approval response

String approvalRequestId

The ID of the approval request being answered.

boolean approve

Whether the request was approved.

JsonValue; type "mcp\_approval\_response"constant"mcp\_approval\_response"constant

The type of the item. Always `mcp_approval_response`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<String> reason

Optional reason for the decision.

class BetaResponseCustomToolCall:

A call to a custom tool created by the model.

String callId

An identifier used to map this custom tool call to a tool call output.

String input

The input for the custom tool call generated by the model.

String name

The name of the custom tool being called.

JsonValue; type "custom\_tool\_call"constant"custom\_tool\_call"constant

The type of the custom tool call. Always `custom_tool_call`.

Optional<String> id

The unique ID of the custom tool call in the OpenAI platform.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

class Program:

String callerId

The call ID of the program item that produced this tool call.

JsonValue; type "program"constant"program"constant

Optional<String> namespace

The namespace of the custom tool being called.

class BetaResponseCustomToolCallOutputItem:

The output of a custom tool call from your code, being sent back to the model.

String id

The unique ID of the custom tool call output item.

Status status

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

Optional<String> createdBy

The identifier of the actor that created the item.

boolean parallelToolCalls

Whether to allow the model to run tool calls in parallel.

Optional<Double> temperature

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
We generally recommend altering this or `top_p` but not both.

minimum0

maximum2

ToolChoice toolChoice

How the model should select which tool (or tools) to use when generating
a response. See the `tools` parameter to see how to specify which tools
the model can call.

enum BetaToolChoiceOptions:

Controls which (if any) tool is called by the model.

`none` means the model will not call any tool and instead generates a message.

`auto` means the model can pick between generating a message or calling one or
more tools.

`required` means the model must call one or more tools.

NONE("none")

AUTO("auto")

REQUIRED("required")

class BetaToolChoiceAllowed:

Constrains the tools available to the model to a pre-defined set.

Mode mode

Constrains the tools available to the model to a pre-defined set.

`auto` allows the model to pick from among the allowed tools and generate a
message.

`required` requires the model to call one or more of the allowed tools.

AUTO("auto")

REQUIRED("required")

List<Tool> tools

A list of tool definitions that the model should be allowed to call.

For the Responses API, the list of tool definitions might look like:

[
  { "type": "function", "name": "get_weather" },
  { "type": "mcp", "server_label": "deepwiki" },
  { "type": "image_generation" }
]

JsonValue; type "allowed\_tools"constant"allowed\_tools"constant

Allowed tool configuration type. Always `allowed_tools`.

class BetaToolChoiceTypes:

Indicates that the model should use a built-in tool to generate a response.
[Learn more about built-in tools](https://platform.openai.com/docs/guides/tools).

Type type

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

FILE\_SEARCH("file\_search")

WEB\_SEARCH\_PREVIEW("web\_search\_preview")

COMPUTER("computer")

COMPUTER\_USE\_PREVIEW("computer\_use\_preview")

COMPUTER\_USE("computer\_use")

WEB\_SEARCH\_PREVIEW\_2025\_03\_11("web\_search\_preview\_2025\_03\_11")

IMAGE\_GENERATION("image\_generation")

CODE\_INTERPRETER("code\_interpreter")

class BetaToolChoiceFunction:

Use this option to force the model to call a specific function.

String name

The name of the function to call.

JsonValue; type "function"constant"function"constant

For function calling, the type is always `function`.

class BetaToolChoiceMcp:

Use this option to force the model to call a specific tool on a remote MCP server.

String serverLabel

The label of the MCP server to use.

JsonValue; type "mcp"constant"mcp"constant

For MCP tools, the type is always `mcp`.

Optional<String> name

The name of the tool to call on the server.

class BetaToolChoiceCustom:

Use this option to force the model to call a specific custom tool.

String name

The name of the custom tool to call.

JsonValue; type "custom"constant"custom"constant

For custom tool calling, the type is always `custom`.

JsonValue;

JsonValue; type "programmatic\_tool\_calling"constant"programmatic\_tool\_calling"constant

The tool to call. Always `programmatic_tool_calling`.

class BetaToolChoiceApplyPatch:

Forces the model to call the apply\_patch tool when executing a tool call.

JsonValue; type "apply\_patch"constant"apply\_patch"constant

The tool to call. Always `apply_patch`.

class BetaToolChoiceShell:

Forces the model to call the shell tool when a tool call is required.

JsonValue; type "shell"constant"shell"constant

The tool to call. Always `shell`.

List<[BetaTool](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))> tools

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

class BetaFunctionTool:

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

String name

The name of the function to call.

Optional<Parameters> parameters

A JSON schema object describing the parameters of the function.

Optional<Boolean> strict

Whether strict parameter validation is enforced for this function tool.

JsonValue; type "function"constant"function"constant

The type of the function tool. Always `function`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this function is deferred and loaded via tool search.

Optional<String> description

A description of the function. Used by the model to determine whether or not to call the function.

Optional<OutputSchema> outputSchema

A JSON schema object describing the JSON value encoded in string outputs for this function.

class BetaFileSearchTool:

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

JsonValue; type "file\_search"constant"file\_search"constant

The type of the file search tool. Always `file_search`.

List<String> vectorStoreIds

The IDs of the vector stores to search.

Optional<Filters> filters

A filter to apply.

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

String

double

boolean

List<ComparisonFilterValueItem>

String

double

class CompoundFilter:

Combine multiple filters using `and` or `or`.

List<Filter> filters

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

String

double

boolean

List<ComparisonFilterValueItem>

String

double

JsonValue

Type type

Type of operation: `and` or `or`.

AND("and")

OR("or")

Optional<Long> maxNumResults

The maximum number of results to return. This number should be between 1 and 50 inclusive.

Optional<RankingOptions> rankingOptions

Ranking options for search.

Optional<HybridSearch> hybridSearch

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

double embeddingWeight

The weight of the embedding in the reciprocal ranking fusion.

double textWeight

The weight of the text in the reciprocal ranking fusion.

Optional<Ranker> ranker

The ranker to use for the file search.

AUTO("auto")

DEFAULT\_2024\_11\_15("default-2024-11-15")

Optional<Double> scoreThreshold

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class BetaComputerTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

JsonValue; type "computer"constant"computer"constant

The type of the computer tool. Always `computer`.

class BetaComputerUsePreviewTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

long displayHeight

The height of the computer display.

long displayWidth

The width of the computer display.

Environment environment

The type of computer environment to control.

WINDOWS("windows")

MAC("mac")

LINUX("linux")

UBUNTU("ubuntu")

BROWSER("browser")

JsonValue; type "computer\_use\_preview"constant"computer\_use\_preview"constant

The type of the computer use tool. Always `computer_use_preview`.

class BetaWebSearchTool:

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

WEB\_SEARCH("web\_search")

WEB\_SEARCH\_2025\_08\_26("web\_search\_2025\_08\_26")

Optional<Filters> filters

Filters for the search.

Optional<List<String>> allowedDomains

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The approximate location of the user.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

Optional<Type> type

The type of location approximation. Always `approximate`.

Mcp

String serverLabel

A label for this MCP server, used to identify it in tool calls.

JsonValue; type "mcp"constant"mcp"constant

The type of the MCP tool. Always `mcp`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<AllowedTools> allowedTools

List of allowed tool names or a filter object.

List<String>

class McpToolFilter:

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<String> authorization

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

Optional<ConnectorId> connectorId

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

CONNECTOR\_DROPBOX("connector\_dropbox")

CONNECTOR\_GMAIL("connector\_gmail")

CONNECTOR\_GOOGLECALENDAR("connector\_googlecalendar")

CONNECTOR\_GOOGLEDRIVE("connector\_googledrive")

CONNECTOR\_MICROSOFTTEAMS("connector\_microsoftteams")

CONNECTOR\_OUTLOOKCALENDAR("connector\_outlookcalendar")

CONNECTOR\_OUTLOOKEMAIL("connector\_outlookemail")

CONNECTOR\_SHAREPOINT("connector\_sharepoint")

Optional<Boolean> deferLoading

Whether this MCP tool is deferred and discovered via tool search.

Optional<Headers> headers

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

Optional<RequireApproval> requireApproval

Specify which of the MCP server’s tools require approval.

class McpToolApprovalFilter:

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

Optional<Always> always

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<Never> never

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

enum McpToolApprovalSetting:

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

ALWAYS("always")

NEVER("never")

Optional<String> serverDescription

Optional description of the MCP server, used to provide more context.

Optional<String> serverUrl

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

Optional<String> tunnelId

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter

Container container

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

String

class CodeInterpreterToolAuto:

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

JsonValue; type "auto"constant"auto"constant

Always `auto`.

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the code interpreter container.

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

JsonValue; type "code\_interpreter"constant"code\_interpreter"constant

The type of the code interpreter tool. Always `code_interpreter`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

JsonValue;

JsonValue; type "programmatic\_tool\_calling"constant"programmatic\_tool\_calling"constant

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration

JsonValue; type "image\_generation"constant"image\_generation"constant

The type of the image generation tool. Always `image_generation`.

Optional<Action> action

Whether to generate a new image or edit an existing image. Default: `auto`.

GENERATE("generate")

EDIT("edit")

AUTO("auto")

Optional<Background> background

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

TRANSPARENT("transparent")

OPAQUE("opaque")

AUTO("auto")

Optional<InputFidelity> inputFidelity

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

HIGH("high")

LOW("low")

Optional<InputImageMask> inputImageMask

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

Optional<String> fileId

File ID for the mask image.

Optional<String> imageUrl

Base64-encoded mask image.

Optional<Model> model

The image generation model to use. Default: `gpt-image-1`.

GPT\_IMAGE\_1("gpt-image-1")

GPT\_IMAGE\_1\_MINI("gpt-image-1-mini")

GPT\_IMAGE\_2("gpt-image-2")

GPT\_IMAGE\_2\_2026\_04\_21("gpt-image-2-2026-04-21")

GPT\_IMAGE\_1\_5("gpt-image-1.5")

CHATGPT\_IMAGE\_LATEST("chatgpt-image-latest")

Optional<Moderation> moderation

Moderation level for the generated image. Default: `auto`.

AUTO("auto")

LOW("low")

Optional<Long> outputCompression

Compression level for the output image. Default: 100.

minimum0

maximum100

Optional<OutputFormat> outputFormat

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

PNG("png")

WEBP("webp")

JPEG("jpeg")

Optional<Long> partialImages

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

Optional<Quality> quality

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

LOW("low")

MEDIUM("medium")

HIGH("high")

AUTO("auto")

Optional<Size> size

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

\_1024X1024("1024x1024")

\_1024X1536("1024x1536")

\_1536X1024("1536x1024")

AUTO("auto")

JsonValue;

JsonValue; type "local\_shell"constant"local\_shell"constant

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool:

A tool that allows the model to execute shell commands.

JsonValue; type "shell"constant"shell"constant

The type of the shell tool. Always `shell`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Environment> environment

class BetaContainerAuto:

JsonValue; type "container\_auto"constant"container\_auto"constant

Automatically creates a container for this request

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the container.

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

class BetaContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class BetaContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[BetaContainerNetworkPolicyDomainSecret](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

Optional<List<Skill>> skills

An optional list of skills referenced by id or inline data.

class BetaSkillReference:

String skillId

The ID of the referenced skill.

maxLength64

minLength1

JsonValue; type "skill\_reference"constant"skill\_reference"constant

References a skill created with the /v1/skills endpoint.

Optional<String> version

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class BetaInlineSkill:

String description

The description of the skill.

String name

The name of the skill.

[BetaInlineSkillSource](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) source

Inline skill payload

String data

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

JsonValue; mediaType "application/zip"constant"application/zip"constant

The media type of the inline skill payload. Must be `application/zip`.

JsonValue; type "base64"constant"base64"constant

The type of the inline skill source. Must be `base64`.

JsonValue; type "inline"constant"inline"constant

Defines an inline skill for this request.

class BetaLocalEnvironment:

JsonValue; type "local"constant"local"constant

Use a local computer environment.

Optional<List<[BetaLocalSkill](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))>> skills

An optional list of skills.

String description

The description of the skill.

String name

The name of the skill.

String path

The path to the directory containing the skill.

class BetaContainerReference:

String containerId

The ID of the referenced container.

JsonValue; type "container\_reference"constant"container\_reference"constant

References a container created with the /v1/containers endpoint

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<Format> format

The input format for the custom tool. Default is unconstrained text.

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

A grammar defined by the user.

String definition

The grammar definition.

Syntax syntax

The syntax of the grammar definition. One of `lark` or `regex`.

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

Grammar format. Always `grammar`.

class BetaNamespaceTool:

Groups function/custom tools under a shared namespace.

String description

A description of the namespace shown to the model.

minLength1

String name

The namespace name used in tool calls (for example, `crm`).

minLength1

List<Tool> tools

The function/custom tools available inside this namespace.

class Function:

String name

maxLength128

minLength1

JsonValue; type "function"constant"function"constant

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this function should be deferred and discovered via tool search.

Optional<String> description

Optional<OutputSchema> outputSchema

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

Optional<JsonValue> parameters

Optional<Boolean> strict

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

class BetaCustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<Format> format

The input format for the custom tool. Default is unconstrained text.

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

A grammar defined by the user.

String definition

The grammar definition.

Syntax syntax

The syntax of the grammar definition. One of `lark` or `regex`.

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

Grammar format. Always `grammar`.

JsonValue; type "namespace"constant"namespace"constant

The type of the tool. Always `namespace`.

class BetaToolSearchTool:

Hosted or BYOT tool search configuration for deferred tools.

JsonValue; type "tool\_search"constant"tool\_search"constant

The type of the tool. Always `tool_search`.

Optional<String> description

Description shown to the model for a client-executed tool search tool.

Optional<Execution> execution

Whether tool search is executed by the server or by the client.

SERVER("server")

CLIENT("client")

Optional<JsonValue> parameters

Parameter schema for a client-executed tool search tool.

class BetaWebSearchPreviewTool:

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

WEB\_SEARCH\_PREVIEW("web\_search\_preview")

WEB\_SEARCH\_PREVIEW\_2025\_03\_11("web\_search\_preview\_2025\_03\_11")

Optional<List<SearchContentType>> searchContentTypes

TEXT("text")

IMAGE("image")

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The user’s location.

JsonValue; type "approximate"constant"approximate"constant

The type of location approximation. Always `approximate`.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

class BetaApplyPatchTool:

Allows the assistant to create, delete, or update files using unified diffs.

JsonValue; type "apply\_patch"constant"apply\_patch"constant

The type of the tool. Always `apply_patch`.

Optional<List<AllowedCaller>> allowedCallers

The tool invocation context(s).

DIRECT("direct")

PROGRAMMATIC("programmatic")

Optional<Double> topP

An alternative to sampling with temperature, called nucleus sampling,
where the model considers the results of the tokens with top\_p probability
mass. So 0.1 means only the tokens comprising the top 10% probability mass
are considered.

We generally recommend altering this or `temperature` but not both.

minimum0

maximum1

Optional<Boolean> background

Whether to run the model response in the background.
[Learn more](https://platform.openai.com/docs/guides/background).

Optional<Double> completedAt

Unix timestamp (in seconds) of when this Response was completed.
Only present when the status is `completed`.

formatunixtime

Optional<Conversation> conversation

The conversation that this response belonged to. Input items and output items from this response were automatically added to this conversation.

String id

The unique ID of the conversation that this response was associated with.

Optional<Long> maxOutputTokens

An upper bound for the number of tokens that can be generated for a response, including visible output tokens and [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

Optional<Long> maxToolCalls

The maximum number of total calls to built-in tools that can be processed in a response. This maximum number applies across all built-in tool calls, not per individual tool. Any further attempts to call a tool by the model will be ignored.

Optional<Moderation> moderation

Moderation results for the response input and output, if moderated completions were requested.

Input input

Moderation for the response input.

class ModerationResult:

A moderation result produced for the response input or output.

Categories categories

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

CategoryAppliedInputTypes categoryAppliedInputTypes

Which modalities of input are reflected by the score for each category.

TEXT("text")

IMAGE("image")

CategoryScores categoryScores

A dictionary of moderation categories to scores.

boolean flagged

A boolean indicating whether the content was flagged by any category.

String model

The moderation model that produced this result.

JsonValue; type "moderation\_result"constant"moderation\_result"constant

The object type, which was always `moderation_result` for successful moderation results.

class Error:

An error produced while attempting moderation for the response input or output.

String code

The error code.

String message

The error message.

JsonValue; type "error"constant"error"constant

The object type, which was always `error` for moderation failures.

Output output

Moderation for the response output.

class ModerationResult:

A moderation result produced for the response input or output.

Categories categories

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

CategoryAppliedInputTypes categoryAppliedInputTypes

Which modalities of input are reflected by the score for each category.

TEXT("text")

IMAGE("image")

CategoryScores categoryScores

A dictionary of moderation categories to scores.

boolean flagged

A boolean indicating whether the content was flagged by any category.

String model

The moderation model that produced this result.

JsonValue; type "moderation\_result"constant"moderation\_result"constant

The object type, which was always `moderation_result` for successful moderation results.

class Error:

An error produced while attempting moderation for the response input or output.

String code

The error code.

String message

The error message.

JsonValue; type "error"constant"error"constant

The object type, which was always `error` for moderation failures.

Optional<String> previousResponseId

The unique ID of the previous response to the model. Use this to
create multi-turn conversations. Learn more about
[conversation state](https://platform.openai.com/docs/guides/conversation-state). Cannot be used in conjunction with `conversation`.

Optional<[BetaResponsePrompt](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_prompt%20%3E%20(schema))> prompt

Reference to a prompt template and its variables.
[Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

String id

The unique identifier of the prompt template to use.

Optional<Variables> variables

Optional map of values to substitute in for variables in your
prompt. The substitution values can either be strings, or other
Response input types like images or files.

String

class BetaResponseInputText:

A text input to the model.

String text

The text input to the model.

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputImage:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail detail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

JsonValue; type "input\_image"constant"input\_image"constant

The type of the input item. Always `input_image`.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> imageUrl

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile:

A file input to the model.

JsonValue; type "input\_file"constant"input\_file"constant

The type of the input item. Always `input_file`.

Optional<Detail> detail

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

AUTO("auto")

LOW("low")

HIGH("high")

Optional<String> fileData

The content of the file to be sent to the model.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> fileUrl

The URL of the file to be sent to the model.

formaturi

Optional<String> filename

The name of the file to be sent to the model.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

Optional<String> version

Optional version of the prompt template.

Optional<String> promptCacheKey

Used by OpenAI to cache responses for similar requests to optimize your cache hit rates. Replaces the `user` field. [Learn more](https://platform.openai.com/docs/guides/prompt-caching).

Optional<PromptCacheOptions> promptCacheOptions

The prompt-caching options that were applied to the response. Supported for `gpt-5.6` and later models.

Mode mode

Whether implicit prompt-cache breakpoints were enabled.

IMPLICIT("implicit")

EXPLICIT("explicit")

Ttl ttl

The minimum lifetime applied to each cache breakpoint.

DeprecatedOptional<PromptCacheRetention> promptCacheRetention

Deprecated. Use `prompt_cache_options.ttl` instead.

The retention policy for the prompt cache. Set to `24h` to enable extended prompt caching, which keeps cached prefixes active for longer, up to a maximum of 24 hours. [Learn more](https://platform.openai.com/docs/guides/prompt-caching#prompt-cache-retention).
This field expresses a maximum retention policy, while
`prompt_cache_options.ttl` expresses a minimum cache lifetime. The two
fields are independent and do not interact.
For `gpt-5.5`, `gpt-5.5-pro`, and future models, only `24h` is supported.

For older models that support both `in_memory` and `24h`, the default depends on your organization’s data retention policy:

* Organizations without ZDR enabled default to `24h`.
* Organizations with ZDR enabled default to `in_memory` when `prompt_cache_retention` is not specified.

IN\_MEMORY("in\_memory")

\_24H("24h")

Optional<Reasoning> reasoning

**gpt-5 and o-series models only**

Configuration options for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).

Optional<Context> context

Controls which reasoning items are rendered back to the model on later turns.
If omitted or set to `auto`, the model determines the context mode. The
`gpt-5.6` model family defaults to `all_turns`; earlier models default to
`current_turn`.

When returned on a response, this is the effective reasoning context mode
used for the response.

AUTO("auto")

CURRENT\_TURN("current\_turn")

ALL\_TURNS("all\_turns")

Optional<Effort> effort

Constrains effort on reasoning for reasoning models. Currently supported
values are `none`, `minimal`, `low`, `medium`, `high`, `xhigh`, and `max`.
Reducing reasoning effort can result in faster responses and fewer tokens
used on reasoning in a response. Not all reasoning models support every
value. See the
[reasoning guide](https://platform.openai.com/docs/guides/reasoning)
for model-specific support.

NONE("none")

MINIMAL("minimal")

LOW("low")

MEDIUM("medium")

HIGH("high")

XHIGH("xhigh")

MAX("max")

DeprecatedOptional<GenerateSummary> generateSummary

**Deprecated:** use `summary` instead.

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

AUTO("auto")

CONCISE("concise")

DETAILED("detailed")

Optional<Mode> mode

Controls the reasoning execution mode for the request.

When returned on a response, this is the effective execution mode.

STANDARD("standard")

PRO("pro")

Optional<Summary> summary

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

`concise` is supported for `computer-use-preview` models and all reasoning models after `gpt-5`.

AUTO("auto")

CONCISE("concise")

DETAILED("detailed")

Optional<String> safetyIdentifier

A stable identifier used to help detect users of your application that may be violating OpenAI’s usage policies.
The IDs should be a string that uniquely identifies each user, with a maximum length of 64 characters. We recommend hashing their username or email address, in order to avoid sending us any identifying information. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

maxLength64

Optional<ServiceTier> serviceTier

Specifies the processing type used for serving the request.

* If set to ‘auto’, then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use ‘default’.
* If set to ‘default’, then the request will be processed with the standard pricing and performance for the selected model.
* If set to ‘[flex](https://platform.openai.com/docs/guides/flex-processing)’ or ‘[priority](https://openai.com/api-priority-processing/)’, then the request will be processed with the corresponding service tier.
* When not set, the default behavior is ‘auto’.

When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.

AUTO("auto")

DEFAULT("default")

FLEX("flex")

SCALE("scale")

PRIORITY("priority")

Optional<[BetaResponseStatus](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_status%20%3E%20(schema))> status

The status of the response generation. One of `completed`, `failed`,
`in_progress`, `cancelled`, `queued`, or `incomplete`.

COMPLETED("completed")

FAILED("failed")

IN\_PROGRESS("in\_progress")

CANCELLED("cancelled")

QUEUED("queued")

INCOMPLETE("incomplete")

Optional<[BetaResponseTextConfig](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_text_config%20%3E%20(schema))> text

Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:

* [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
* [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

Optional<[BetaResponseFormatTextConfig](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_format_text_config%20%3E%20(schema))> format

An object specifying the format that the model must output.

Configuring `{ "type": "json_schema" }` enables Structured Outputs,
which ensures the model will match your supplied JSON schema. Learn more in the
[Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

The default format is `{ "type": "text" }` with no additional options.

**Not recommended for gpt-4o and newer models:**

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

JsonValue;

JsonValue; type "text"constant"text"constant

The type of response format being defined. Always `text`.

class BetaResponseFormatTextJsonSchemaConfig:

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

String name

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

Schema schema

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

JsonValue; type "json\_schema"constant"json\_schema"constant

The type of response format being defined. Always `json_schema`.

Optional<String> description

A description of what the response format is for, used by the model to
determine how to respond in the format.

Optional<Boolean> strict

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

JsonValue;

JsonValue; type "json\_object"constant"json\_object"constant

The type of response format being defined. Always `json_object`.

Optional<Verbosity> verbosity

Constrains the verbosity of the model’s response. Lower values will result in
more concise responses, while higher values will result in more verbose responses.
Currently supported values are `low`, `medium`, and `high`. The default is
`medium`.

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<Long> topLogprobs

An integer between 0 and 20 specifying the maximum number of most likely
tokens to return at each token position, each with an associated log
probability. In some cases, the number of returned tokens may be fewer than
requested.

minimum0

maximum20

Optional<Truncation> truncation

The truncation strategy to use for the model response.

* `auto`: If the input to this Response exceeds
  the model’s context window size, the model will truncate the
  response to fit the context window by dropping items from the beginning of the conversation.
* `disabled` (default): If the input size will exceed the context window
  size for a model, the request will fail with a 400 error.

AUTO("auto")

DISABLED("disabled")

Optional<[BetaResponseUsage](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_usage%20%3E%20(schema))> usage

Represents token usage details including input tokens, output tokens,
a breakdown of output tokens, and the total tokens used.

long inputTokens

The number of input tokens.

InputTokensDetails inputTokensDetails

A detailed breakdown of the input tokens.

long cacheWriteTokens

The number of input tokens that were written to the cache.

long cachedTokens

The number of tokens that were retrieved from the cache.
[More on prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

long outputTokens

The number of output tokens.

OutputTokensDetails outputTokensDetails

A detailed breakdown of the output tokens.

long reasoningTokens

The number of reasoning tokens.

long totalTokens

The total number of tokens used.

DeprecatedOptional<String> user

This field is being replaced by `safety_identifier` and `prompt_cache_key`. Use `prompt_cache_key` instead to maintain caching optimizations.
A stable identifier for your end-users.
Used to boost cache hit rates by better bucketing similar requests and to help OpenAI detect and prevent abuse. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

long sequenceNumber

The sequence number of this event.

JsonValue; type "response.failed"constant"response.failed"constant

The type of the event. Always `response.failed`.

Optional<Agent> agent

The agent that owns this multi-agent streaming event.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseIncompleteEvent:

An event that is emitted when a response finishes as incomplete.

[BetaResponse](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema)) response

The response that was incomplete.

String id

Unique identifier for this Response.

double createdAt

Unix timestamp (in seconds) of when this Response was created.

formatunixtime

Optional<[BetaResponseError](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_error%20%3E%20(schema))> error

An error object returned when the model fails to generate a Response.

Code code

The error code for the response.

SERVER\_ERROR("server\_error")

RATE\_LIMIT\_EXCEEDED("rate\_limit\_exceeded")

INVALID\_PROMPT("invalid\_prompt")

DATA\_RESIDENCY\_MISMATCH("data\_residency\_mismatch")

BIO\_POLICY("bio\_policy")

VECTOR\_STORE\_TIMEOUT("vector\_store\_timeout")

INVALID\_IMAGE("invalid\_image")

INVALID\_IMAGE\_FORMAT("invalid\_image\_format")

INVALID\_BASE64\_IMAGE("invalid\_base64\_image")

INVALID\_IMAGE\_URL("invalid\_image\_url")

IMAGE\_TOO\_LARGE("image\_too\_large")

IMAGE\_TOO\_SMALL("image\_too\_small")

IMAGE\_PARSE\_ERROR("image\_parse\_error")

IMAGE\_CONTENT\_POLICY\_VIOLATION("image\_content\_policy\_violation")

INVALID\_IMAGE\_MODE("invalid\_image\_mode")

IMAGE\_FILE\_TOO\_LARGE("image\_file\_too\_large")

UNSUPPORTED\_IMAGE\_MEDIA\_TYPE("unsupported\_image\_media\_type")

EMPTY\_IMAGE\_FILE("empty\_image\_file")

FAILED\_TO\_DOWNLOAD\_IMAGE("failed\_to\_download\_image")

IMAGE\_FILE\_NOT\_FOUND("image\_file\_not\_found")

String message

A human-readable description of the error.

Optional<IncompleteDetails> incompleteDetails

Details about why the response is incomplete.

Optional<Reason> reason

The reason why the response is incomplete.

MAX\_OUTPUT\_TOKENS("max\_output\_tokens")

CONTENT\_FILTER("content\_filter")

Optional<Instructions> instructions

A system (or developer) message inserted into the model’s context.

When using along with `previous_response_id`, the instructions from a previous
response will not be carried over to the next response. This makes it simple
to swap out system (or developer) messages in new responses.

String

List<[BetaResponseInputItem](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_item%20%3E%20(schema))>

class BetaEasyInputMessage:

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

Content content

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

String

List<[BetaResponseInputContent](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_content%20%3E%20(schema))>

class BetaResponseInputText:

A text input to the model.

String text

The text input to the model.

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputImage:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail detail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

JsonValue; type "input\_image"constant"input\_image"constant

The type of the input item. Always `input_image`.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> imageUrl

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile:

A file input to the model.

JsonValue; type "input\_file"constant"input\_file"constant

The type of the input item. Always `input_file`.

Optional<Detail> detail

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

AUTO("auto")

LOW("low")

HIGH("high")

Optional<String> fileData

The content of the file to be sent to the model.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> fileUrl

The URL of the file to be sent to the model.

formaturi

Optional<String> filename

The name of the file to be sent to the model.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

Role role

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

USER("user")

ASSISTANT("assistant")

SYSTEM("system")

DEVELOPER("developer")

Optional<Phase> phase

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

COMMENTARY("commentary")

FINAL\_ANSWER("final\_answer")

Optional<Type> type

The type of the message input. Always `message`.

Message

List<[BetaResponseInputContent](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_content%20%3E%20(schema))> content

A list of one or many input items to the model, containing different content
types.

class BetaResponseInputText:

A text input to the model.

String text

The text input to the model.

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputImage:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail detail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

JsonValue; type "input\_image"constant"input\_image"constant

The type of the input item. Always `input_image`.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> imageUrl

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputFile:

A file input to the model.

JsonValue; type "input\_file"constant"input\_file"constant

The type of the input item. Always `input_file`.

Optional<Detail> detail

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

AUTO("auto")

LOW("low")

HIGH("high")

Optional<String> fileData

The content of the file to be sent to the model.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> fileUrl

The URL of the file to be sent to the model.

formaturi

Optional<String> filename

The name of the file to be sent to the model.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

Role role

The role of the message input. One of `user`, `system`, or `developer`.

USER("user")

SYSTEM("system")

DEVELOPER("developer")

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Status> status

The status of item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

Optional<Type> type

The type of the message input. Always set to `message`.

class BetaResponseOutputMessage:

An output message from the model.

String id

The unique ID of the output message.

List<Content> content

The content of the output message.

class BetaResponseOutputText:

A text output from the model.

List<Annotation> annotations

The annotations of the text output.

class FileCitation:

A citation to a file.

String fileId

The ID of the file.

String filename

The filename of the file cited.

long index

The index of the file in the list of files.

JsonValue; type "file\_citation"constant"file\_citation"constant

The type of the file citation. Always `file_citation`.

class UrlCitation:

A citation for a web resource used to generate a model response.

long endIndex

The index of the last character of the URL citation in the message.

long startIndex

The index of the first character of the URL citation in the message.

String title

The title of the web resource.

JsonValue; type "url\_citation"constant"url\_citation"constant

The type of the URL citation. Always `url_citation`.

String url

The URL of the web resource.

formaturi

class ContainerFileCitation:

A citation for a container file used to generate a model response.

String containerId

The ID of the container file.

long endIndex

The index of the last character of the container file citation in the message.

String fileId

The ID of the file.

String filename

The filename of the container file cited.

long startIndex

The index of the first character of the container file citation in the message.

JsonValue; type "container\_file\_citation"constant"container\_file\_citation"constant

The type of the container file citation. Always `container_file_citation`.

class FilePath:

A path to a file.

String fileId

The ID of the file.

long index

The index of the file in the list of files.

JsonValue; type "file\_path"constant"file\_path"constant

The type of the file path. Always `file_path`.

String text

The text output from the model.

JsonValue; type "output\_text"constant"output\_text"constant

The type of the output text. Always `output_text`.

Optional<List<Logprob>> logprobs

String token

List<long> bytes

double logprob

List<TopLogprob> topLogprobs

String token

List<long> bytes

double logprob

class BetaResponseOutputRefusal:

A refusal from the model.

String refusal

The refusal explanation from the model.

JsonValue; type "refusal"constant"refusal"constant

The type of the refusal. Always `refusal`.

JsonValue; role "assistant"constant"assistant"constant

The role of the output message. Always `assistant`.

Status status

The status of the message input. One of `in_progress`, `completed`, or
`incomplete`. Populated when input items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

JsonValue; type "message"constant"message"constant

The type of the output message. Always `message`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Phase> phase

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

COMMENTARY("commentary")

FINAL\_ANSWER("final\_answer")

class BetaResponseFileSearchToolCall:

The results of a file search tool call. See the
[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

String id

The unique ID of the file search tool call.

List<String> queries

The queries used to search for files.

Status status

The status of the file search tool call. One of `in_progress`,
`searching`, `incomplete` or `failed`,

IN\_PROGRESS("in\_progress")

SEARCHING("searching")

COMPLETED("completed")

INCOMPLETE("incomplete")

FAILED("failed")

JsonValue; type "file\_search\_call"constant"file\_search\_call"constant

The type of the file search tool call. Always `file_search_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<List<Result>> results

The results of the file search tool call.

Optional<Attributes> attributes

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

String

double

boolean

Optional<String> fileId

The unique ID of the file.

Optional<String> filename

The name of the file.

Optional<Double> score

The relevance score of the file - a value between 0 and 1.

formatfloat

Optional<String> text

The text that was retrieved from the file.

class BetaResponseComputerToolCall:

A tool call to a computer use tool. See the
[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

String id

The unique ID of the computer call.

String callId

An identifier used when responding to the tool call with output.

List<PendingSafetyCheck> pendingSafetyChecks

The pending safety checks for the computer call.

String id

The ID of the pending safety check.

Optional<String> code

The type of the pending safety check.

Optional<String> message

Details about the pending safety check.

Status status

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

Type type

The type of the computer call. Always `computer_call`.

Optional<[BetaComputerAction](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action%20%3E%20(schema))> action

A click action.

Click

Button button

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

LEFT("left")

RIGHT("right")

WHEEL("wheel")

BACK("back")

FORWARD("forward")

JsonValue; type "click"constant"click"constant

Specifies the event type. For a click action, this property is always `click`.

long x

The x-coordinate where the click occurred.

long y

The y-coordinate where the click occurred.

Optional<List<String>> keys

The keys being held while clicking.

DoubleClick

Optional<List<String>> keys

The keys being held while double-clicking.

JsonValue; type "double\_click"constant"double\_click"constant

Specifies the event type. For a double click action, this property is always set to `double_click`.

long x

The x-coordinate where the double click occurred.

long y

The y-coordinate where the double click occurred.

Drag

List<Path> path

An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

[
  { x: 100, y: 200 },
  { x: 200, y: 300 }
]

long x

The x-coordinate.

long y

The y-coordinate.

JsonValue; type "drag"constant"drag"constant

Specifies the event type. For a drag action, this property is always set to `drag`.

Optional<List<String>> keys

The keys being held while dragging the mouse.

Keypress

List<String> keys

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

JsonValue; type "keypress"constant"keypress"constant

Specifies the event type. For a keypress action, this property is always set to `keypress`.

Move

JsonValue; type "move"constant"move"constant

Specifies the event type. For a move action, this property is always set to `move`.

long x

The x-coordinate to move to.

long y

The y-coordinate to move to.

Optional<List<String>> keys

The keys being held while moving the mouse.

JsonValue;

JsonValue; type "screenshot"constant"screenshot"constant

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

Scroll

long scrollX

The horizontal scroll distance.

long scrollY

The vertical scroll distance.

JsonValue; type "scroll"constant"scroll"constant

Specifies the event type. For a scroll action, this property is always set to `scroll`.

long x

The x-coordinate where the scroll occurred.

long y

The y-coordinate where the scroll occurred.

Optional<List<String>> keys

The keys being held while scrolling.

Type

String text

The text to type.

JsonValue; type "type"constant"type"constant

Specifies the event type. For a type action, this property is always set to `type`.

JsonValue;

JsonValue; type "wait"constant"wait"constant

Specifies the event type. For a wait action, this property is always set to `wait`.

Optional<List<[BetaComputerAction](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action%20%3E%20(schema))>> actions

Flattened batched actions for `computer_use`. Each action includes an
`type` discriminator and action-specific fields.

Click

Button button

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

LEFT("left")

RIGHT("right")

WHEEL("wheel")

BACK("back")

FORWARD("forward")

JsonValue; type "click"constant"click"constant

Specifies the event type. For a click action, this property is always `click`.

long x

The x-coordinate where the click occurred.

long y

The y-coordinate where the click occurred.

Optional<List<String>> keys

The keys being held while clicking.

DoubleClick

Optional<List<String>> keys

The keys being held while double-clicking.

JsonValue; type "double\_click"constant"double\_click"constant

Specifies the event type. For a double click action, this property is always set to `double_click`.

long x

The x-coordinate where the double click occurred.

long y

The y-coordinate where the double click occurred.

Drag

List<Path> path

An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

[
  { x: 100, y: 200 },
  { x: 200, y: 300 }
]

long x

The x-coordinate.

long y

The y-coordinate.

JsonValue; type "drag"constant"drag"constant

Specifies the event type. For a drag action, this property is always set to `drag`.

Optional<List<String>> keys

The keys being held while dragging the mouse.

Keypress

List<String> keys

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

JsonValue; type "keypress"constant"keypress"constant

Specifies the event type. For a keypress action, this property is always set to `keypress`.

Move

JsonValue; type "move"constant"move"constant

Specifies the event type. For a move action, this property is always set to `move`.

long x

The x-coordinate to move to.

long y

The y-coordinate to move to.

Optional<List<String>> keys

The keys being held while moving the mouse.

JsonValue;

JsonValue; type "screenshot"constant"screenshot"constant

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

Scroll

long scrollX

The horizontal scroll distance.

long scrollY

The vertical scroll distance.

JsonValue; type "scroll"constant"scroll"constant

Specifies the event type. For a scroll action, this property is always set to `scroll`.

long x

The x-coordinate where the scroll occurred.

long y

The y-coordinate where the scroll occurred.

Optional<List<String>> keys

The keys being held while scrolling.

Type

String text

The text to type.

JsonValue; type "type"constant"type"constant

Specifies the event type. For a type action, this property is always set to `type`.

JsonValue;

JsonValue; type "wait"constant"wait"constant

Specifies the event type. For a wait action, this property is always set to `wait`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

ComputerCallOutput

String callId

The ID of the computer tool call that produced the output.

maxLength64

minLength1

[BetaResponseComputerToolCallOutputScreenshot](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema)) output

A computer screenshot image used with the computer use tool.

JsonValue; type "computer\_screenshot"constant"computer\_screenshot"constant

Specifies the event type. For a computer screenshot, this property is
always set to `computer_screenshot`.

Optional<String> fileId

The identifier of an uploaded file that contains the screenshot.

Optional<String> imageUrl

The URL of the screenshot image.

formaturi

JsonValue; type "computer\_call\_output"constant"computer\_call\_output"constant

The type of the computer tool call output. Always `computer_call_output`.

Optional<String> id

The ID of the computer tool call output.

Optional<List<AcknowledgedSafetyCheck>> acknowledgedSafetyChecks

The safety checks reported by the API that have been acknowledged by the developer.

String id

The ID of the pending safety check.

Optional<String> code

The type of the pending safety check.

Optional<String> message

Details about the pending safety check.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Status> status

The status of the message input. One of `in_progress`, `completed`, or `incomplete`. Populated when input items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

class BetaResponseFunctionWebSearch:

The results of a web search tool call. See the
[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

String id

The unique ID of the web search tool call.

Action action

An object describing the specific action taken in this web search call.
Includes details on how the model used the web (search, open\_page, find\_in\_page).

class Search:

Action type “search” - Performs a web search query.

JsonValue; type "search"constant"search"constant

The action type.

Optional<List<String>> queries

The search queries.

DeprecatedOptional<String> query

The search query.

Optional<List<Source>> sources

The sources used in the search.

JsonValue; type "url"constant"url"constant

The type of source. Always `url`.

String url

The URL of the source.

formaturi

class OpenPage:

Action type “open\_page” - Opens a specific URL from search results.

JsonValue; type "open\_page"constant"open\_page"constant

The action type.

Optional<String> url

The URL opened by the model.

formaturi

class FindInPage:

Action type “find\_in\_page”: Searches for a pattern within a loaded page.

String pattern

The pattern or text to search for within the page.

JsonValue; type "find\_in\_page"constant"find\_in\_page"constant

The action type.

String url

The URL of the page searched for the pattern.

formaturi

Status status

The status of the web search tool call.

IN\_PROGRESS("in\_progress")

SEARCHING("searching")

COMPLETED("completed")

FAILED("failed")

JsonValue; type "web\_search\_call"constant"web\_search\_call"constant

The type of the web search tool call. Always `web_search_call`.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

class BetaResponseFunctionToolCall:

A tool call to run a function. See the
[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

String arguments

A JSON string of the arguments to pass to the function.

String callId

The unique ID of the function tool call generated by the model.

String name

The name of the function to run.

JsonValue; type "function\_call"constant"function\_call"constant

The type of the function tool call. Always `function_call`.

Optional<String> id

The unique ID of the function tool call.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

class Program:

String callerId

The call ID of the program item that produced this tool call.

JsonValue; type "program"constant"program"constant

Optional<String> namespace

The namespace of the function to run.

Optional<Status> status

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

FunctionCallOutput

String callId

The unique ID of the function tool call generated by the model.

maxLength64

minLength1

Output output

Text, image, or file output of the function tool call.

String

List<[BetaResponseFunctionCallOutputItem](/api/reference/java/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item%20%3E%20(schema))>

class BetaResponseInputTextContent:

A text input to the model.

String text

The text input to the model.

maxLength10485760

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputImageContent:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

JsonValue; type "input\_image"constant"input\_image"constant

The type of the input item. Always `input_image`.

Optional<Detail> detail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> imageUrl

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

maxLength20971520

formaturi

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputFileContent:

A file input to the model.

JsonValue; type "input\_file"constant"input\_file"constant

The type of the input item. Always `input_file`.

Optional<Detail> detail

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

AUTO("auto")

LOW("low")

HIGH("high")

Optional<String> fileData

The base64-encoded data of the file to be sent to the model.

maxLength73400320

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> fileUrl

The URL of the file to be sent to the model.

formaturi

Optional<String> filename

The name of the file to be sent to the model.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

JsonValue; type "function\_call\_output"constant"function\_call\_output"constant

The type of the function tool call output. Always `function_call_output`.

Optional<String> id

The unique ID of the function tool call output. Populated when this item is returned via API.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

Optional<Caller> caller

The execution context that produced this tool call.

JsonValue;

JsonValue; type "direct"constant"direct"constant

The caller type. Always `direct`.

class Program:

String callerId

The call ID of the program item that produced this tool call.

maxLength64

minLength1

JsonValue; type "program"constant"program"constant

The caller type. Always `program`.

Optional<Status> status

The status of the item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

INCOMPLETE("incomplete")

AgentMessage

String author

The sending agent identity.

List<Content> content

Plaintext, image, or encrypted content sent between agents.

class BetaResponseInputTextContent:

A text input to the model.

String text

The text input to the model.

maxLength10485760

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class BetaResponseInputImageContent:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

JsonValue; type "input\_image"constant"input\_image"constant

The type of the input item. Always `input_image`.

Optional<Detail> detail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> imageUrl

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

maxLength20971520

formaturi

Optional<PromptCacheBreakpoint> promptCacheBreakpoint

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

JsonValue; mode "explicit"constant"explicit"constant

The breakpoint mode. Always `explicit`.

class EncryptedContent:

Opaque encrypted content that Responses API decrypts inside trusted model execution.

String encryptedContent

Opaque encrypted content.

maxLength10485760

JsonValue; type "encrypted\_content"constant"encrypted\_content"constant

The type of the input item. Always `encrypted_content`.

String recipient

The destination agent identity.

JsonValue; type "agent\_message"constant"agent\_message"constant

The item type. Always `agent_message`.

Optional<String> id

The unique ID of this agent message item.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

MultiAgentCall

Action action

The multi-agent action that was executed.

SPAWN\_AGENT("spawn\_agent")

INTERRUPT\_AGENT("interrupt\_agent")

LIST\_AGENTS("list\_agents")

SEND\_MESSAGE("send\_message")

FOLLOWUP\_TASK("followup\_task")

WAIT\_AGENT("wait\_agent")

String arguments

The action arguments as a JSON string.

String callId

The unique ID linking this call to its output.

maxLength64

minLength1

JsonValue; type "multi\_agent\_call"constant"multi\_agent\_call"constant

The item type. Always `multi_agent_call`.

Optional<String> id

The unique ID of this multi-agent call.

Optional<Agent> agent

The agent that produced this item.

String agentName

The canonical name of the agent that produced this item.

MultiAgentCallOutput

Action action

The multi-agent action that produced this result.

SPAWN\_AGENT("spawn\_agent")

INTERRUPT\_AGENT("interrupt\_agent")

LIST\_AGENTS("list\_agents")

SEND\_MESSAGE("send\_message")

FOLLOWUP\_TASK("followup\_task")

WAIT\_AGENT("wait\_agent")

String callId

The unique ID of the multi-agent call.

maxLength64

minLength1

List<Output> output

Text output returned by the multi-agent action.

String text

The text content.

maxLength10485760

JsonValue; type "output\_text"constant"output\_text"constant

The content type. Always `output_text`.

Optional<List<Annotation>> annotations

Citations associated with the text content.

class FileCitation:

String fileId

The ID of the file.

String filename

The filename of the file cited.

long index

The index of the file in the list of files.

minimum0

JsonValue; type "file\_citation"constant"file\_citation"constant

The citation type. Always `file_citation`.

class UrlCitation:

long endIndex

The index of the last character of the citation in the message.

minimum0

long startIndex

The index of the first character of the citation in the message.

minimum0

String title

The title of the cited resource.

JsonValue; type "url\_citation"constant"url\_citation"constant

The citation type. Always `url_citation`.

String url

The URL of the cited resource.

formaturi

class ContainerFileCitation:

String containerId

The ID of the container.

long endIndex

The index of the last character of the citation in the message.

minimum0

String fileId

The ID of the container file.

String filename

The filename of the container file cited.

long startIndex

The index of the first character of the citation in the message.

minimum0

JsonValue; type "container\_file\_citation"constant"container\_file\_citation"constant

The citation type. Always `container_file_citation`.

JsonValue; type "multi\_agent\_call\_output"constant"multi\_agent\_call\_output"constant

The item type. Always `multi_agent_call_output`.

Optional<String> id

The unique ID of this multi-agent call output.
