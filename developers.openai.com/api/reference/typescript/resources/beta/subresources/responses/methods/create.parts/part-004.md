<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/responses/methods/create/ -->
<!-- part of: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/responses/methods/create/ -->

<!-- chunk-start -->

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" | "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

type: "namespace"

The type of the tool. Always `namespace`.

BetaToolSearchTool { type, description, execution, parameters }

Hosted or BYOT tool search configuration for deferred tools.

type: "tool\_search"

The type of the tool. Always `tool_search`.

description?: string | null

Description shown to the model for a client-executed tool search tool.

execution?: "server" | "client"

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters?: unknown

Parameter schema for a client-executed tool search tool.

BetaWebSearchPreviewTool { type, search\_content\_types, search\_context\_size, user\_location }

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search\_preview" | "web\_search\_preview\_2025\_03\_11"

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types?: Array<"text" | "image">

"text"

"image"

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location?: UserLocation | null

The user’s location.

type: "approximate"

The type of location approximation. Always `approximate`.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

BetaApplyPatchTool { type, allowed\_callers }

Allows the assistant to create, delete, or update files using unified diffs.

type: "apply\_patch"

The type of the tool. Always `apply_patch`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

type: "tool\_search\_output"

The type of the item. Always `tool_search_output`.

agent?: Agent { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

created\_by?: string

The identifier of the actor that created the item.

AdditionalTools { id, role, tools, 2 more }

id: string

The unique ID of the additional tools item.

role: "unknown" | "user" | "assistant" | 5 more

The role that provided the additional tools.

"unknown"

"user"

"assistant"

"system"

"critic"

"discriminator"

"developer"

"tool"

tools: Array<[BetaTool](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))>

The additional tool definitions made available at this item.

BetaFunctionTool { name, parameters, strict, 5 more }

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: string

The name of the function to call.

parameters: Record<string, unknown> | null

A JSON schema object describing the parameters of the function.

strict: boolean | null

Whether strict parameter validation is enforced for this function tool.

type: "function"

The type of the function tool. Always `function`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this function is deferred and loaded via tool search.

description?: string | null

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema?: Record<string, unknown> | null

A JSON schema object describing the JSON value encoded in string outputs for this function.

BetaFileSearchTool { type, vector\_store\_ids, filters, 2 more }

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: "file\_search"

The type of the file search tool. Always `file_search`.

vector\_store\_ids: Array<string>

The IDs of the vector stores to search.

filters?: ComparisonFilter { key, type, value }  | CompoundFilter { filters, type }  | null

A filter to apply.

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

string

number

boolean

Array<string | number>

string

number

CompoundFilter { filters, type }

Combine multiple filters using `and` or `or`.

filters: Array<ComparisonFilter { key, type, value }  | unknown>

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

string

number

boolean

Array<string | number>

string

number

unknown

type: "and" | "or"

Type of operation: `and` or `or`.

"and"

"or"

max\_num\_results?: number

The maximum number of results to return. This number should be between 1 and 50 inclusive.

ranking\_options?: RankingOptions { hybrid\_search, ranker, score\_threshold }

Ranking options for search.

hybrid\_search?: HybridSearch { embedding\_weight, text\_weight }

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

embedding\_weight: number

The weight of the embedding in the reciprocal ranking fusion.

text\_weight: number

The weight of the text in the reciprocal ranking fusion.

ranker?: "auto" | "default-2024-11-15"

The ranker to use for the file search.

"auto"

"default-2024-11-15"

score\_threshold?: number

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

BetaComputerTool { type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: "computer"

The type of the computer tool. Always `computer`.

BetaComputerUsePreviewTool { display\_height, display\_width, environment, type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: number

The height of the computer display.

display\_width: number

The width of the computer display.

environment: "windows" | "mac" | "linux" | 2 more

The type of computer environment to control.

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

The type of the computer use tool. Always `computer_use_preview`.

BetaWebSearchTool { type, filters, search\_context\_size, user\_location }

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search" | "web\_search\_2025\_08\_26"

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

"web\_search"

"web\_search\_2025\_08\_26"

filters?: Filters | null

Filters for the search.

allowed\_domains?: Array<string> | null

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location?: UserLocation | null

The approximate location of the user.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type?: "approximate"

The type of location approximation. Always `approximate`.

Mcp { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: string

A label for this MCP server, used to identify it in tool calls.

type: "mcp"

The type of the MCP tool. Always `mcp`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools?: Array<string> | McpToolFilter { read\_only, tool\_names }  | null

List of allowed tool names or a filter object.

Array<string>

McpToolFilter { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

authorization?: string

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

connector\_id?: "connector\_dropbox" | "connector\_gmail" | "connector\_googlecalendar" | 5 more

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

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading?: boolean

Whether this MCP tool is deferred and discovered via tool search.

headers?: Record<string, string> | null

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval?: McpToolApprovalFilter { always, never }  | "always" | "never" | null

Specify which of the MCP server’s tools require approval.

McpToolApprovalFilter { always, never }

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always?: Always { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

never?: Never { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

"always" | "never"

"always"

"never"

server\_description?: string

Optional description of the MCP server, used to provide more context.

server\_url?: string

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

tunnel\_id?: string

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string | CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

string

CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: "auto"

Always `auto`.

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the code interpreter container.

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

type: "code\_interpreter"

The type of the code interpreter tool. Always `code_interpreter`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

ProgrammaticToolCalling { type }

type: "programmatic\_tool\_calling"

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

The type of the image generation tool. Always `image_generation`.

action?: "generate" | "edit" | "auto"

Whether to generate a new image or edit an existing image. Default: `auto`.

"generate"

"edit"

"auto"

background?: "transparent" | "opaque" | "auto"

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

"transparent"

"opaque"

"auto"

input\_fidelity?: "high" | "low" | null

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

"high"

"low"

input\_image\_mask?: InputImageMask { file\_id, image\_url }

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

file\_id?: string

File ID for the mask image.

image\_url?: string

Base64-encoded mask image.

model?: (string & {}) | "gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

The image generation model to use. Default: `gpt-image-1`.

(string & {})

"gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation?: "auto" | "low"

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression?: number

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format?: "png" | "webp" | "jpeg"

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

"png"

"webp"

"jpeg"

partial\_images?: number

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

quality?: "low" | "medium" | "high" | "auto"

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

"low"

"medium"

"high"

"auto"

size?: (string & {}) | "1024x1024" | "1024x1536" | "1536x1024" | "auto"

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

(string & {})

"1024x1024" | "1024x1536" | "1536x1024" | "auto"

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

LocalShell { type }

A tool that allows the model to execute shell commands in a local environment.

type: "local\_shell"

The type of the local shell tool. Always `local_shell`.

BetaFunctionShellTool { type, allowed\_callers, environment }

A tool that allows the model to execute shell commands.

type: "shell"

The type of the shell tool. Always `shell`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

environment?: [BetaContainerAuto](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  | [BetaLocalEnvironment](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  | [BetaContainerReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }  | null

BetaContainerAuto { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

Automatically creates a container for this request

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

skills?: Array<[BetaSkillReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_skill_reference%20%3E%20(schema)) { skill\_id, type, version }  | [BetaInlineSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill%20%3E%20(schema)) { description, name, source, type } >

An optional list of skills referenced by id or inline data.

BetaSkillReference { skill\_id, type, version }

skill\_id: string

The ID of the referenced skill.

maxLength64

minLength1

type: "skill\_reference"

References a skill created with the /v1/skills endpoint.

version?: string

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

BetaInlineSkill { description, name, source, type }

description: string

The description of the skill.

name: string

The name of the skill.

source: [BetaInlineSkillSource](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

Inline skill payload

data: string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: "application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: "base64"

The type of the inline skill source. Must be `base64`.

type: "inline"

Defines an inline skill for this request.

BetaLocalEnvironment { type, skills }

type: "local"

Use a local computer environment.

skills?: Array<[BetaLocalSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path } >

An optional list of skills.

description: string

The description of the skill.

name: string

The name of the skill.

path: string

The path to the directory containing the skill.

BetaContainerReference { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: Text { type }  | Grammar { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" | "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

BetaNamespaceTool { description, name, tools, type }

Groups function/custom tools under a shared namespace.

description: string

A description of the namespace shown to the model.

minLength1

name: string

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: Array<Function { name, type, allowed\_callers, 5 more }  | [BetaCustomTool](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_custom_tool%20%3E%20(schema)) { name, type, allowed\_callers, 3 more } >

The function/custom tools available inside this namespace.

Function { name, type, allowed\_callers, 5 more }

name: string

maxLength128

minLength1

type: "function"

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this function should be deferred and discovered via tool search.

description?: string | null

output\_schema?: Record<string, unknown> | null

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters?: unknown

strict?: boolean | null

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: Text { type }  | Grammar { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" | "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

type: "namespace"

The type of the tool. Always `namespace`.

BetaToolSearchTool { type, description, execution, parameters }

Hosted or BYOT tool search configuration for deferred tools.

type: "tool\_search"

The type of the tool. Always `tool_search`.

description?: string | null

Description shown to the model for a client-executed tool search tool.

execution?: "server" | "client"

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters?: unknown

Parameter schema for a client-executed tool search tool.

BetaWebSearchPreviewTool { type, search\_content\_types, search\_context\_size, user\_location }

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search\_preview" | "web\_search\_preview\_2025\_03\_11"

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types?: Array<"text" | "image">

"text"

"image"

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location?: UserLocation | null

The user’s location.

type: "approximate"

The type of location approximation. Always `approximate`.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

BetaApplyPatchTool { type, allowed\_callers }

Allows the assistant to create, delete, or update files using unified diffs.

type: "apply\_patch"

The type of the tool. Always `apply_patch`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

type: "additional\_tools"

The type of the item. Always `additional_tools`.

agent?: Agent { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseCompactionItem { id, encrypted\_content, type, 2 more }

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

id: string

The unique ID of the compaction item.

encrypted\_content: string

The encrypted content that was produced by compaction.

type: "compaction"

The type of the item. Always `compaction`.

agent?: Agent { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

created\_by?: string

The identifier of the actor that created the item.

ImageGenerationCall { id, result, status, 2 more }

An image generation request made by the model.

id: string

The unique ID of the image generation call.

result: string | null

The generated image encoded in base64.

status: "in\_progress" | "completed" | "generating" | "failed"

The status of the image generation call.

"in\_progress"

"completed"

"generating"

"failed"

type: "image\_generation\_call"

The type of the image generation call. Always `image_generation_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseCodeInterpreterToolCall { id, code, container\_id, 4 more }

A tool call to run code.

id: string

The unique ID of the code interpreter tool call.

code: string | null

The code to run, or null if not available.

container\_id: string

The ID of the container used to run the code.

outputs: Array<Logs { logs, type }  | Image { type, url } > | null

The outputs generated by the code interpreter, such as logs or images.
Can be null if no outputs are available.

Logs { logs, type }

The logs output from the code interpreter.

logs: string

The logs output from the code interpreter.

type: "logs"

The type of the output. Always `logs`.

Image { type, url }

The image output from the code interpreter.

type: "image"

The type of the output. Always `image`.

url: string

The URL of the image output from the code interpreter.

formaturi

status: "in\_progress" | "completed" | "incomplete" | 2 more

The status of the code interpreter tool call. Valid values are `in_progress`, `completed`, `incomplete`, `interpreting`, and `failed`.

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: "code\_interpreter\_call"

The type of the code interpreter tool call. Always `code_interpreter_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

LocalShellCall { id, action, call\_id, 3 more }

A tool call to run a command on the local shell.

id: string

The unique ID of the local shell call.

action: Action { command, env, type, 3 more }

Execute a shell command on the server.

command: Array<string>

The command to run.

env: Record<string, string>

Environment variables to set for the command.

type: "exec"

The type of the local shell action. Always `exec`.

timeout\_ms?: number | null

Optional timeout in milliseconds for the command.

user?: string | null

Optional user to run the command as.

working\_directory?: string | null

Optional working directory to run the command in.

call\_id: string

The unique ID of the local shell tool call generated by the model.

status: "in\_progress" | "completed" | "incomplete"

The status of the local shell call.

"in\_progress"

"completed"

"incomplete"

type: "local\_shell\_call"

The type of the local shell call. Always `local_shell_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

LocalShellCallOutput { id, output, type, 2 more }

The output of a local shell tool call.

id: string

The unique ID of the local shell tool call generated by the model.

output: string

A JSON string of the output of the local shell tool call.

type: "local\_shell\_call\_output"

The type of the local shell tool call output. Always `local_shell_call_output`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

status?: "in\_progress" | "completed" | "incomplete" | null

The status of the item. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

BetaResponseFunctionShellToolCall { id, action, call\_id, 6 more }

A tool call that executes one or more shell commands in a managed environment.

id: string

The unique ID of the shell tool call. Populated when this item is returned via API.

action: Action { commands, max\_output\_length, timeout\_ms }

The shell commands and limits that describe how to run the tool call.

commands: Array<string>

max\_output\_length: number | null

Optional maximum number of characters to return from each command.

timeout\_ms: number | null

Optional timeout in milliseconds for the commands.

call\_id: string

The unique ID of the shell tool call generated by the model.

environment: [BetaResponseLocalEnvironment](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_local_environment%20%3E%20(schema)) { type }  | [BetaResponseContainerReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_container_reference%20%3E%20(schema)) { container\_id, type }  | null

Represents the use of a local environment to perform shell actions.

BetaResponseLocalEnvironment { type }

Represents the use of a local environment to perform shell actions.

type: "local"

The environment type. Always `local`.

BetaResponseContainerReference { container\_id, type }

Represents a container created with /v1/containers.

container\_id: string

type: "container\_reference"

The environment type. Always `container_reference`.

status: "in\_progress" | "completed" | "incomplete"

The status of the shell call. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

type: "shell\_call"

The type of the item. Always `shell_call`.

agent?: Agent { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

type: "program"

created\_by?: string

The ID of the entity that created this tool call.

BetaResponseFunctionShellToolCallOutput { id, call\_id, max\_output\_length, 6 more }

The output of a shell tool call that was emitted.

id: string

The unique ID of the shell call output. Populated when this item is returned via API.

call\_id: string

The unique ID of the shell tool call generated by the model.

max\_output\_length: number | null

The maximum length of the shell command output. This is generated by the model and should be passed back with the raw output.

output: Array<Output>

An array of shell call output contents

outcome: Timeout { type }  | Exit { exit\_code, type }

Represents either an exit outcome (with an exit code) or a timeout outcome for a shell call output chunk.

Timeout { type }

Indicates that the shell call exceeded its configured time limit.

type: "timeout"

The outcome type. Always `timeout`.

Exit { exit\_code, type }

Indicates that the shell commands finished and returned an exit code.

exit\_code: number

Exit code from the shell process.

type: "exit"

The outcome type. Always `exit`.

stderr: string

The standard error output that was captured.

stdout: string

The standard output that was captured.

created\_by?: string

The identifier of the actor that created the item.

status: "in\_progress" | "completed" | "incomplete"

The status of the shell call output. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

type: "shell\_call\_output"

The type of the shell call output. Always `shell_call_output`.

agent?: Agent { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

type: "program"

created\_by?: string

The identifier of the actor that created the item.

BetaResponseApplyPatchToolCall { id, call\_id, operation, 5 more }

A tool call that applies file diffs by creating, deleting, or updating files.

id: string

The unique ID of the apply patch tool call. Populated when this item is returned via API.

call\_id: string

The unique ID of the apply patch tool call generated by the model.

operation: CreateFile { diff, path, type }  | DeleteFile { path, type }  | UpdateFile { diff, path, type }

One of the create\_file, delete\_file, or update\_file operations applied via apply\_patch.

CreateFile { diff, path, type }

Instruction describing how to create a file via the apply\_patch tool.

diff: string

Diff to apply.

path: string

Path of the file to create.

type: "create\_file"

Create a new file with the provided diff.

DeleteFile { path, type }

Instruction describing how to delete a file via the apply\_patch tool.

path: string

Path of the file to delete.

type: "delete\_file"

Delete the specified file.

UpdateFile { diff, path, type }

Instruction describing how to update a file via the apply\_patch tool.

diff: string

Diff to apply.

path: string

Path of the file to update.

type: "update\_file"

Update an existing file with the provided diff.

status: "in\_progress" | "completed"

The status of the apply patch tool call. One of `in_progress` or `completed`.

"in\_progress"

"completed"

type: "apply\_patch\_call"

The type of the item. Always `apply_patch_call`.

agent?: Agent { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

type: "program"

created\_by?: string

The ID of the entity that created this tool call.

BetaResponseApplyPatchToolCallOutput { id, call\_id, status, 5 more }

The output emitted by an apply patch tool call.

id: string

The unique ID of the apply patch tool call output. Populated when this item is returned via API.

call\_id: string

The unique ID of the apply patch tool call generated by the model.

status: "completed" | "failed"

The status of the apply patch tool call output. One of `completed` or `failed`.

"completed"

"failed"

type: "apply\_patch\_call\_output"

The type of the item. Always `apply_patch_call_output`.

agent?: Agent { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

type: "program"

created\_by?: string

The ID of the entity that created this tool call output.

output?: string | null

Optional textual output returned by the apply patch tool.

McpCall { id, arguments, name, 7 more }

An invocation of a tool on an MCP server.

id: string

The unique ID of the tool call.

arguments: string

A JSON string of the arguments passed to the tool.

name: string

The name of the tool that was run.

server\_label: string

The label of the MCP server running the tool.

type: "mcp\_call"

The type of the item. Always `mcp_call`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

approval\_request\_id?: string | null

Unique identifier for the MCP tool call approval request.
Include this value in a subsequent `mcp_approval_response` input to approve or reject the corresponding tool call.

error?: string | null

The error from the tool call, if any.

output?: string | null

The output from the tool call.

status?: "in\_progress" | "completed" | "incomplete" | 2 more

The status of the tool call. One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.

"in\_progress"

"completed"

"incomplete"

"calling"

"failed"

McpListTools { id, server\_label, tools, 3 more }

A list of tools available on an MCP server.

id: string

The unique ID of the list.

server\_label: string

The label of the MCP server.

tools: Array<Tool>

The tools available on the server.

input\_schema: unknown

The JSON schema describing the tool’s input.

name: string

The name of the tool.

annotations?: unknown

Additional annotations about the tool.

description?: string | null

The description of the tool.

type: "mcp\_list\_tools"

The type of the item. Always `mcp_list_tools`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

error?: string | null

Error message if the server could not list tools.

McpApprovalRequest { id, arguments, name, 3 more }

A request for human approval of a tool invocation.

id: string

The unique ID of the approval request.

arguments: string

A JSON string of arguments for the tool.

name: string

The name of the tool to run.

server\_label: string

The label of the MCP server making the request.

type: "mcp\_approval\_request"

The type of the item. Always `mcp_approval_request`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

McpApprovalResponse { id, approval\_request\_id, approve, 3 more }

A response to an MCP approval request.

id: string

The unique ID of the approval response

approval\_request\_id: string

The ID of the approval request being answered.

approve: boolean

Whether the request was approved.

type: "mcp\_approval\_response"

The type of the item. Always `mcp_approval_response`.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

reason?: string | null

Optional reason for the decision.

BetaResponseCustomToolCall { call\_id, input, name, 5 more }

A call to a custom tool created by the model.

call\_id: string

An identifier used to map this custom tool call to a tool call output.

input: string

The input for the custom tool call generated by the model.

name: string

The name of the custom tool being called.

type: "custom\_tool\_call"

The type of the custom tool call. Always `custom_tool_call`.

id?: string

The unique ID of the custom tool call in the OpenAI platform.

agent?: Agent | null

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller?: Direct { type }  | Program { caller\_id, type }  | null

The execution context that produced this tool call.

Direct { type }

type: "direct"

Program { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

type: "program"

namespace?: string

The namespace of the custom tool being called.

BetaResponseCustomToolCallOutputItem extends [BetaResponseCustomToolCallOutput](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_custom_tool_call_output%20%3E%20(schema)) { call\_id, output, type, 3 more }  { id, status, created\_by }

The output of a custom tool call from your code, being sent back to the model.

id: string

The unique ID of the custom tool call output item.

status: "in\_progress" | "completed" | "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

created\_by?: string

The identifier of the actor that created the item.

parallel\_tool\_calls: boolean

Whether to allow the model to run tool calls in parallel.

temperature: number | null

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
We generally recommend altering this or `top_p` but not both.

minimum0

maximum2

tool\_choice: [BetaToolChoiceOptions](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool_choice_options%20%3E%20(schema)) | [BetaToolChoiceAllowed](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool_choice_allowed%20%3E%20(schema)) { mode, tools, type }  | [BetaToolChoiceTypes](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool_choice_types%20%3E%20(schema)) { type }  | 6 more

How the model should select which tool (or tools) to use when generating
a response. See the `tools` parameter to see how to specify which tools
the model can call.

BetaToolChoiceOptions = "none" | "auto" | "required"

Controls which (if any) tool is called by the model.

`none` means the model will not call any tool and instead generates a message.

`auto` means the model can pick between generating a message or calling one or
more tools.

`required` means the model must call one or more tools.

"none"

"auto"

"required"

BetaToolChoiceAllowed { mode, tools, type }

Constrains the tools available to the model to a pre-defined set.

mode: "auto" | "required"

Constrains the tools available to the model to a pre-defined set.

`auto` allows the model to pick from among the allowed tools and generate a
message.

`required` requires the model to call one or more of the allowed tools.

"auto"

"required"

tools: Array<Record<string, unknown>>

A list of tool definitions that the model should be allowed to call.

For the Responses API, the list of tool definitions might look like:

[
  { "type": "function", "name": "get_weather" },
  { "type": "mcp", "server_label": "deepwiki" },
  { "type": "image_generation" }
]

type: "allowed\_tools"

Allowed tool configuration type. Always `allowed_tools`.

BetaToolChoiceTypes { type }

Indicates that the model should use a built-in tool to generate a response.
[Learn more about built-in tools](https://platform.openai.com/docs/guides/tools).

type: "file\_search" | "web\_search\_preview" | "computer" | 5 more

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

"file\_search"

"web\_search\_preview"

"computer"

"computer\_use\_preview"

"computer\_use"

"web\_search\_preview\_2025\_03\_11"

"image\_generation"

"code\_interpreter"

BetaToolChoiceFunction { name, type }

Use this option to force the model to call a specific function.

name: string

The name of the function to call.

type: "function"

For function calling, the type is always `function`.

BetaToolChoiceMcp { server\_label, type, name }

Use this option to force the model to call a specific tool on a remote MCP server.

server\_label: string

The label of the MCP server to use.

type: "mcp"

For MCP tools, the type is always `mcp`.

name?: string | null

The name of the tool to call on the server.

BetaToolChoiceCustom { name, type }

Use this option to force the model to call a specific custom tool.

name: string

The name of the custom tool to call.

type: "custom"

For custom tool calling, the type is always `custom`.

BetaSpecificProgrammaticToolCallingParam { type }

type: "programmatic\_tool\_calling"

The tool to call. Always `programmatic_tool_calling`.

BetaToolChoiceApplyPatch { type }

Forces the model to call the apply\_patch tool when executing a tool call.

type: "apply\_patch"

The tool to call. Always `apply_patch`.

BetaToolChoiceShell { type }

Forces the model to call the shell tool when a tool call is required.

type: "shell"

The tool to call. Always `shell`.

tools: Array<[BetaTool](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))>

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

BetaFunctionTool { name, parameters, strict, 5 more }

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: string

The name of the function to call.

parameters: Record<string, unknown> | null

A JSON schema object describing the parameters of the function.

strict: boolean | null

Whether strict parameter validation is enforced for this function tool.

type: "function"

The type of the function tool. Always `function`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this function is deferred and loaded via tool search.

description?: string | null

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema?: Record<string, unknown> | null

A JSON schema object describing the JSON value encoded in string outputs for this function.

BetaFileSearchTool { type, vector\_store\_ids, filters, 2 more }

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: "file\_search"

The type of the file search tool. Always `file_search`.

vector\_store\_ids: Array<string>

The IDs of the vector stores to search.

filters?: ComparisonFilter { key, type, value }  | CompoundFilter { filters, type }  | null

A filter to apply.

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

string

number

boolean

Array<string | number>

string

number

CompoundFilter { filters, type }

Combine multiple filters using `and` or `or`.

filters: Array<ComparisonFilter { key, type, value }  | unknown>

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

string

number

boolean

Array<string | number>

string

number

unknown

type: "and" | "or"

Type of operation: `and` or `or`.

"and"

"or"

max\_num\_results?: number

The maximum number of results to return. This number should be between 1 and 50 inclusive.

ranking\_options?: RankingOptions { hybrid\_search, ranker, score\_threshold }

Ranking options for search.

hybrid\_search?: HybridSearch { embedding\_weight, text\_weight }

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

embedding\_weight: number

The weight of the embedding in the reciprocal ranking fusion.

text\_weight: number

The weight of the text in the reciprocal ranking fusion.

ranker?: "auto" | "default-2024-11-15"

The ranker to use for the file search.

"auto"

"default-2024-11-15"

score\_threshold?: number

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

BetaComputerTool { type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: "computer"

The type of the computer tool. Always `computer`.

BetaComputerUsePreviewTool { display\_height, display\_width, environment, type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: number

The height of the computer display.

display\_width: number

The width of the computer display.

environment: "windows" | "mac" | "linux" | 2 more

The type of computer environment to control.

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

The type of the computer use tool. Always `computer_use_preview`.

BetaWebSearchTool { type, filters, search\_context\_size, user\_location }

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search" | "web\_search\_2025\_08\_26"

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

"web\_search"

"web\_search\_2025\_08\_26"

filters?: Filters | null

Filters for the search.

allowed\_domains?: Array<string> | null

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location?: UserLocation | null

The approximate location of the user.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type?: "approximate"

The type of location approximation. Always `approximate`.

Mcp { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: string

A label for this MCP server, used to identify it in tool calls.

type: "mcp"

The type of the MCP tool. Always `mcp`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools?: Array<string> | McpToolFilter { read\_only, tool\_names }  | null

List of allowed tool names or a filter object.

Array<string>

McpToolFilter { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

authorization?: string

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

connector\_id?: "connector\_dropbox" | "connector\_gmail" | "connector\_googlecalendar" | 5 more

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

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading?: boolean

Whether this MCP tool is deferred and discovered via tool search.

headers?: Record<string, string> | null

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval?: McpToolApprovalFilter { always, never }  | "always" | "never" | null

Specify which of the MCP server’s tools require approval.

McpToolApprovalFilter { always, never }

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always?: Always { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

never?: Never { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

"always" | "never"

"always"

"never"

server\_description?: string

Optional description of the MCP server, used to provide more context.

server\_url?: string

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

tunnel\_id?: string

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string | CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

string

CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: "auto"

Always `auto`.

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the code interpreter container.

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

type: "code\_interpreter"

The type of the code interpreter tool. Always `code_interpreter`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

ProgrammaticToolCalling { type }

type: "programmatic\_tool\_calling"

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

The type of the image generation tool. Always `image_generation`.

action?: "generate" | "edit" | "auto"

Whether to generate a new image or edit an existing image. Default: `auto`.

"generate"

"edit"

"auto"

background?: "transparent" | "opaque" | "auto"

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

"transparent"

"opaque"

"auto"

input\_fidelity?: "high" | "low" | null

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

"high"

"low"

input\_image\_mask?: InputImageMask { file\_id, image\_url }

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

file\_id?: string

File ID for the mask image.

image\_url?: string

Base64-encoded mask image.

model?: (string & {}) | "gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

The image generation model to use. Default: `gpt-image-1`.

(string & {})

"gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation?: "auto" | "low"

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression?: number

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format?: "png" | "webp" | "jpeg"

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

"png"

"webp"

"jpeg"

partial\_images?: number

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

quality?: "low" | "medium" | "high" | "auto"

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

"low"

"medium"

"high"

"auto"

size?: (string & {}) | "1024x1024" | "1024x1536" | "1536x1024" | "auto"

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

(string & {})

"1024x1024" | "1024x1536" | "1536x1024" | "auto"

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

LocalShell { type }

A tool that allows the model to execute shell commands in a local environment.

type: "local\_shell"

The type of the local shell tool. Always `local_shell`.

BetaFunctionShellTool { type, allowed\_callers, environment }

A tool that allows the model to execute shell commands.

type: "shell"

The type of the shell tool. Always `shell`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

environment?: [BetaContainerAuto](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  | [BetaLocalEnvironment](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  | [BetaContainerReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }  | null

BetaContainerAuto { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

Automatically creates a container for this request

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

skills?: Array<[BetaSkillReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_skill_reference%20%3E%20(schema)) { skill\_id, type, version }  | [BetaInlineSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill%20%3E%20(schema)) { description, name, source, type } >

An optional list of skills referenced by id or inline data.

BetaSkillReference { skill\_id, type, version }

skill\_id: string

The ID of the referenced skill.

maxLength64

minLength1

type: "skill\_reference"

References a skill created with the /v1/skills endpoint.

version?: string

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

BetaInlineSkill { description, name, source, type }

description: string

The description of the skill.

name: string

The name of the skill.

source: [BetaInlineSkillSource](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

Inline skill payload

data: string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: "application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: "base64"

The type of the inline skill source. Must be `base64`.

type: "inline"

Defines an inline skill for this request.

BetaLocalEnvironment { type, skills }

type: "local"

Use a local computer environment.

skills?: Array<[BetaLocalSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path } >

An optional list of skills.

description: string

The description of the skill.

name: string

The name of the skill.

path: string

The path to the directory containing the skill.

BetaContainerReference { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: Text { type }  | Grammar { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" | "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

BetaNamespaceTool { description, name, tools, type }

Groups function/custom tools under a shared namespace.

description: string

A description of the namespace shown to the model.

minLength1

name: string

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: Array<Function { name, type, allowed\_callers, 5 more }  | [BetaCustomTool](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_custom_tool%20%3E%20(schema)) { name, type, allowed\_callers, 3 more } >

The function/custom tools available inside this namespace.

Function { name, type, allowed\_callers, 5 more }

name: string

maxLength128

minLength1

type: "function"

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this function should be deferred and discovered via tool search.

description?: string | null

output\_schema?: Record<string, unknown> | null

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters?: unknown

strict?: boolean | null

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: Text { type }  | Grammar { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" | "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

type: "namespace"

The type of the tool. Always `namespace`.

BetaToolSearchTool { type, description, execution, parameters }

Hosted or BYOT tool search configuration for deferred tools.

type: "tool\_search"

The type of the tool. Always `tool_search`.

description?: string | null

Description shown to the model for a client-executed tool search tool.

execution?: "server" | "client"

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters?: unknown

Parameter schema for a client-executed tool search tool.

BetaWebSearchPreviewTool { type, search\_content\_types, search\_context\_size, user\_location }

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search\_preview" | "web\_search\_preview\_2025\_03\_11"

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types?: Array<"text" | "image">

"text"

"image"

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location?: UserLocation | null

The user’s location.

type: "approximate"

The type of location approximation. Always `approximate`.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

BetaApplyPatchTool { type, allowed\_callers }

Allows the assistant to create, delete, or update files using unified diffs.

type: "apply\_patch"

The type of the tool. Always `apply_patch`.

allowed\_callers?: Array<"direct" | "programmatic"> | null

The tool invocation context(s).

"direct"

"programmatic"

top\_p: number | null

An alternative to sampling with temperature, called nucleus sampling,
where the model considers the results of the tokens with top\_p probability
mass. So 0.1 means only the tokens comprising the top 10% probability mass
are considered.

We generally recommend altering this or `temperature` but not both.

minimum0

maximum1

background?: boolean | null

Whether to run the model response in the background.
[Learn more](https://platform.openai.com/docs/guides/background).

completed\_at?: number | null

Unix timestamp (in seconds) of when this Response was completed.
Only present when the status is `completed`.

formatunixtime

conversation?: Conversation | null

The conversation that this response belonged to. Input items and output items from this response were automatically added to this conversation.

id: string

The unique ID of the conversation that this response was associated with.

max\_output\_tokens?: number | null

An upper bound for the number of tokens that can be generated for a response, including visible output tokens and [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

max\_tool\_calls?: number | null

The maximum number of total calls to built-in tools that can be processed in a response. This maximum number applies across all built-in tool calls, not per individual tool. Any further attempts to call a tool by the model will be ignored.

moderation?: Moderation | null

Moderation results for the response input and output, if moderated completions were requested.

input: ModerationResult { categories, category\_applied\_input\_types, category\_scores, 3 more }  | Error { code, message, type }

Moderation for the response input.

ModerationResult { categories, category\_applied\_input\_types, category\_scores, 3 more }

A moderation result produced for the response input or output.

categories: Record<string, boolean>

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

category\_applied\_input\_types: Record<string, Array<"text" | "image">>

Which modalities of input are reflected by the score for each category.

"text"

"image"

category\_scores: Record<string, number>

A dictionary of moderation categories to scores.

flagged: boolean

A boolean indicating whether the content was flagged by any category.

model: string

The moderation model that produced this result.

type: "moderation\_result"

The object type, which was always `moderation_result` for successful moderation results.

Error { code, message, type }

An error produced while attempting moderation for the response input or output.

code: string

The error code.

message: string

The error message.

type: "error"

The object type, which was always `error` for moderation failures.

output: ModerationResult { categories, category\_applied\_input\_types, category\_scores, 3 more }  | Error { code, message, type }

Moderation for the response output.

ModerationResult { categories, category\_applied\_input\_types, category\_scores, 3 more }

A moderation result produced for the response input or output.

categories: Record<string, boolean>

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

category\_applied\_input\_types: Record<string, Array<"text" | "image">>

Which modalities of input are reflected by the score for each category.

"text"

"image"

category\_scores: Record<string, number>

A dictionary of moderation categories to scores.

flagged: boolean

A boolean indicating whether the content was flagged by any category.

model: string

The moderation model that produced this result.

type: "moderation\_result"

The object type, which was always `moderation_result` for successful moderation results.

Error { code, message, type }

An error produced while attempting moderation for the response input or output.

code: string

The error code.

message: string

The error message.

type: "error"

The object type, which was always `error` for moderation failures.

previous\_response\_id?: string | null

The unique ID of the previous response to the model. Use this to
create multi-turn conversations. Learn more about
[conversation state](https://platform.openai.com/docs/guides/conversation-state). Cannot be used in conjunction with `conversation`.

prompt?: [BetaResponsePrompt](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_prompt%20%3E%20(schema)) { id, variables, version }  | null

Reference to a prompt template and its variables.
[Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

id: string

The unique identifier of the prompt template to use.

variables?: Record<string, string | [BetaResponseInputText](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  | [BetaResponseInputImage](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  | [BetaResponseInputFile](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more } > | null

Optional map of values to substitute in for variables in your
prompt. The substitution values can either be strings, or other
Response input types like images or files.

string

BetaResponseInputText { text, type, prompt\_cache\_breakpoint }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputImage { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: "low" | "high" | "auto" | "original"

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

type: "input\_image"

The type of the input item. Always `input_image`.

file\_id?: string | null

The ID of the file to be sent to the model.

image\_url?: string | null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

BetaResponseInputFile { type, detail, file\_data, 4 more }

A file input to the model.

type: "input\_file"

The type of the input item. Always `input_file`.

detail?: "auto" | "low" | "high"

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

"low"

"high"

file\_data?: string

The content of the file to be sent to the model.

file\_id?: string | null

The ID of the file to be sent to the model.

file\_url?: string

The URL of the file to be sent to the model.

formaturi

filename?: string

The name of the file to be sent to the model.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

version?: string | null

Optional version of the prompt template.

prompt\_cache\_key?: string | null

Used by OpenAI to cache responses for similar requests to optimize your cache hit rates. Replaces the `user` field. [Learn more](https://platform.openai.com/docs/guides/prompt-caching).

prompt\_cache\_options?: PromptCacheOptions { mode, ttl }

The prompt-caching options that were applied to the response. Supported for `gpt-5.6` and later models.

mode: "implicit" | "explicit"

Whether implicit prompt-cache breakpoints were enabled.

"implicit"

"explicit"

ttl: "30m"

The minimum lifetime applied to each cache breakpoint.

Deprecatedprompt\_cache\_retention?: "in\_memory" | "24h" | null

Deprecated. Use `prompt_cache_options.ttl` instead.

The retention policy for the prompt cache. Set to `24h` to enable extended prompt caching, which keeps cached prefixes active for longer, up to a maximum of 24 hours. [Learn more](https://platform.openai.com/docs/guides/prompt-caching#prompt-cache-retention).
This field expresses a maximum retention policy, while
`prompt_cache_options.ttl` expresses a minimum cache lifetime. The two
fields are independent and do not interact.
For `gpt-5.5`, `gpt-5.5-pro`, and future models, only `24h` is supported.

For older models that support both `in_memory` and `24h`, the default depends on your organization’s data retention policy:

* Organizations without ZDR enabled default to `24h`.
* Organizations with ZDR enabled default to `in_memory` when `prompt_cache_retention` is not specified.

"in\_memory"

"24h"

reasoning?: Reasoning | null

**gpt-5 and o-series models only**

Configuration options for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).

context?: "auto" | "current\_turn" | "all\_turns" | null

Controls which reasoning items are rendered back to the model on later turns.
If omitted or set to `auto`, the model determines the context mode. The
`gpt-5.6` model family defaults to `all_turns`; earlier models default to
`current_turn`.

When returned on a response, this is the effective reasoning context mode
used for the response.

"auto"

"current\_turn"

"all\_turns"

effort?: "none" | "minimal" | "low" | 4 more | null

Constrains effort on reasoning for reasoning models. Currently supported
values are `none`, `minimal`, `low`, `medium`, `high`, `xhigh`, and `max`.
Reducing reasoning effort can result in faster responses and fewer tokens
used on reasoning in a response. Not all reasoning models support every
value. See the
[reasoning guide](https://platform.openai.com/docs/guides/reasoning)
for model-specific support.

"none"

"minimal"

"low"

"medium"

"high"

"xhigh"

"max"

Deprecatedgenerate\_summary?: "auto" | "concise" | "detailed" | null

**Deprecated:** use `summary` instead.

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

"auto"

"concise"

"detailed"

mode?: (string & {}) | "standard" | "pro"

Controls the reasoning execution mode for the request.

When returned on a response, this is the effective execution mode.

(string & {})

"standard" | "pro"

"standard"

"pro"

summary?: "auto" | "concise" | "detailed" | null

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

`concise` is supported for `computer-use-preview` models and all reasoning models after `gpt-5`.

"auto"

"concise"

"detailed"

safety\_identifier?: string | null

A stable identifier used to help detect users of your application that may be violating OpenAI’s usage policies.
The IDs should be a string that uniquely identifies each user, with a maximum length of 64 characters. We recommend hashing their username or email address, in order to avoid sending us any identifying information. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

maxLength64

service\_tier?: "auto" | "default" | "flex" | 2 more | null

Specifies the processing type used for serving the request.

* If set to ‘auto’, then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use ‘default’.
* If set to ‘default’, then the request will be processed with the standard pricing and performance for the selected model.
* If set to ‘[flex](https://platform.openai.com/docs/guides/flex-processing)’ or ‘[priority](https://openai.com/api-priority-processing/)’, then the request will be processed with the corresponding service tier.
* When not set, the default behavior is ‘auto’.

When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.

"auto"

"default"

"flex"

"scale"

"priority"

status?: [BetaResponseStatus](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_status%20%3E%20(schema))

The status of the response generation. One of `completed`, `failed`,
`in_progress`, `cancelled`, `queued`, or `incomplete`.

"completed"

"failed"

"in\_progress"

"cancelled"

"queued"

"incomplete"

text?: [BetaResponseTextConfig](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_text_config%20%3E%20(schema)) { format, verbosity }

Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:

* [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
* [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

format?: [BetaResponseFormatTextConfig](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_format_text_config%20%3E%20(schema))

An object specifying the format that the model must output.

Configuring `{ "type": "json_schema" }` enables Structured Outputs,
which ensures the model will match your supplied JSON schema. Learn more in the
[Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

The default format is `{ "type": "text" }` with no additional options.

**Not recommended for gpt-4o and newer models:**

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

Text { type }

Default response format. Used to generate text responses.

type: "text"

The type of response format being defined. Always `text`.

BetaResponseFormatTextJSONSchemaConfig { name, schema, type, 2 more }

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

name: string

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

schema: Record<string, unknown>

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

type: "json\_schema"

The type of response format being defined. Always `json_schema`.

description?: string

A description of what the response format is for, used by the model to
determine how to respond in the format.

strict?: boolean | null

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

JSONObject { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: "json\_object"

The type of response format being defined. Always `json_object`.

verbosity?: "low" | "medium" | "high" | null

Constrains the verbosity of the model’s response. Lower values will result in
more concise responses, while higher values will result in more verbose responses.
Currently supported values are `low`, `medium`, and `high`. The default is
`medium`.

"low"

"medium"

"high"

top\_logprobs?: number | null

An integer between 0 and 20 specifying the maximum number of most likely
tokens to return at each token position, each with an associated log
probability. In some cases, the number of returned tokens may be fewer than
requested.

minimum0

maximum20

truncation?: "auto" | "disabled" | null

The truncation strategy to use for the model response.

* `auto`: If the input to this Response exceeds
  the model’s context window size, the model will truncate the
  response to fit the context window by dropping items from the beginning of the conversation.
* `disabled` (default): If the input size will exceed the context window
  size for a model, the request will fail with a 400 error.

"auto"

"disabled"

usage?: [BetaResponseUsage](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_usage%20%3E%20(schema)) { input\_tokens, input\_tokens\_details, output\_tokens, 2 more }

Represents token usage details including input tokens, output tokens,
a breakdown of output tokens, and the total tokens used.

input\_tokens: number

The number of input tokens.

input\_tokens\_details: InputTokensDetails { cache\_write\_tokens, cached\_tokens }

A detailed breakdown of the input tokens.

cache\_write\_tokens: number

The number of input tokens that were written to the cache.

cached\_tokens: number

The number of tokens that were retrieved from the cache.
[More on prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

output\_tokens: number

The number of output tokens.

output\_tokens\_details: OutputTokensDetails { reasoning\_tokens }

A detailed breakdown of the output tokens.

reasoning\_tokens: number

The number of reasoning tokens.

total\_tokens: number

The total number of tokens used.

Deprecateduser?: string

This field is being replaced by `safety_identifier` and `prompt_cache_key`. Use `prompt_cache_key` instead to maintain caching optimizations.
A stable identifier for your end-users.
Used to boost cache hit rates by better bucketing similar requests and to help OpenAI detect and prevent abuse. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

sequence\_number: number

The sequence number for this event.

type: "response.queued"

The type of the event. Always ‘response.queued’.

agent?: Agent | null

The agent that owns this multi-agent streaming event.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseCustomToolCallInputDeltaEvent { delta, item\_id, output\_index, 3 more }

Event representing a delta (partial update) to the input of a custom tool call.

delta: string

The incremental input data (delta) for the custom tool call.

item\_id: string

Unique identifier for the API item associated with this event.

output\_index: number

The index of the output this delta applies to.

sequence\_number: number

The sequence number of this event.

type: "response.custom\_tool\_call\_input.delta"

The event type identifier.

agent?: Agent | null

The agent that owns this multi-agent streaming event.

agent\_name: string

The canonical name of the agent that produced this item.

BetaResponseCustomToolCallInputDoneEvent { input, item\_id, output\_index, 3 more }

Event indicating that input for a custom tool call is complete.

input: string

The complete input data for the custom tool call.

item\_id: string

Unique identifier for the API item associated with this event.

output\_index: number

The index of the output this event applies to.

sequence\_number: number

The sequence number of this event.

type: "response.custom\_tool\_call\_input.done"

The event type identifier.

agent?: Agent | null

The agent that owns this multi-agent streaming event.

agent\_name: string

The canonical name of the agent that produced this item.

Text inputImage inputFile inputWeb searchFile searchStreamingFunctionsReasoning

### Create a model response

TypeScript

import OpenAI from "openai";

const openai = new OpenAI();

const response = await openai.responses.create({
    model: "gpt-5.4",
    input: "Tell me a three sentence bedtime story about a unicorn."
});

console.log(response);

  "id": "resp_67ccd2bed1ec8190b14f964abc0542670bb6a6b452d3795b",
  "object": "response",
  "created_at": 1741476542,
  "status": "completed",
  "completed_at": 1741476543,
  "error": null,
  "incomplete_details": null,
  "instructions": null,
  "max_output_tokens": null,
  "model": "gpt-5.4",
  "output": [
      "type": "message",
      "id": "msg_67ccd2bf17f0819081ff3bb2cf6508e60bb6a6b452d3795b",
      "status": "completed",
      "role": "assistant",
      "content": [
          "type": "output_text",
          "text": "In a peaceful grove beneath a silver moon, a unicorn named Lumina discovered a hidden pool that reflected the stars. As she dipped her horn into the water, the pool began to shimmer, revealing a pathway to a magical realm of endless night skies. Filled with wonder, Lumina whispered a wish for all who dream to find their own hidden magic, and as she glanced back, her hoofprints sparkled like stardust.",
          "annotations": []
      ]
  ],
  "parallel_tool_calls": true,
  "previous_response_id": null,
  "reasoning": {
    "effort": null,
    "summary": null
  },
  "store": true,
  "temperature": 1.0,
  "text": {
    "format": {
      "type": "text"
  },
  "tool_choice": "auto",
  "tools": [],
  "top_p": 1.0,
  "truncation": "disabled",
  "usage": {
    "input_tokens": 36,
    "input_tokens_details": {
      "cached_tokens": 0,
      "cache_write_tokens": 0
    },
    "output_tokens": 87,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "total_tokens": 123
  },
  "user": null,
  "metadata": {}

### Create a model response

TypeScript

import OpenAI from "openai";

const openai = new OpenAI();

const response = await openai.responses.create({
    model: "gpt-5.4",
    input: [
            role: "user",
            content: [
                { type: "input_text", text: "what is in this image?" },
                    type: "input_image",
                    image_url:
                        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                },
            ],
        },
    ],
});

console.log(response);

  "id": "resp_67ccd3a9da748190baa7f1570fe91ac604becb25c45c1d41",
  "object": "response",
  "created_at": 1741476777,
  "status": "completed",
  "completed_at": 1741476778,
  "error": null,
  "incomplete_details": null,
  "instructions": null,
  "max_output_tokens": null,
  "model": "gpt-5.4",
  "output": [
      "type": "message",
      "id": "msg_67ccd3acc8d48190a77525dc6de64b4104becb25c45c1d41",
      "status": "completed",
      "role": "assistant",
      "content": [
          "type": "output_text",
          "text": "The image depicts a scenic landscape with a wooden boardwalk or pathway leading through lush, green grass under a blue sky with some clouds. The setting suggests a peaceful natural area, possibly a park or nature reserve. There are trees and shrubs in the background.",
          "annotations": []
      ]
  ],
  "parallel_tool_calls": true,
  "previous_response_id": null,
  "reasoning": {
    "effort": null,
    "summary": null
  },
  "store": true,
  "temperature": 1.0,
  "text": {
    "format": {
      "type": "text"
  },
  "tool_choice": "auto",
  "tools": [],
  "top_p": 1.0,
  "truncation": "disabled",
  "usage": {
    "input_tokens": 328,
    "input_tokens_details": {
      "cached_tokens": 0,
      "cache_write_tokens": 0
    },
    "output_tokens": 52,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "total_tokens": 380
  },
  "user": null,
  "metadata": {}

### Create a model response

TypeScript

import OpenAI from "openai";

const openai = new OpenAI();

const response = await openai.responses.create({
    model: "gpt-5.4",
    input: [
            role: "user",
            content: [
                { type: "input_text", text: "what is in this file?" },
                    type: "input_file",
                    file_url: "https://www.berkshirehathaway.com/letters/2024ltr.pdf",
                    detail: "auto",
                },
            ],
        },
    ],
});

console.log(response);

  "id": "resp_686eef60237881a2bd1180bb8b13de430e34c516d176ff86",
  "object": "response",
  "created_at": 1752100704,
  "status": "completed",
  "completed_at": 1752100705,
  "background": false,
  "error": null,
  "incomplete_details": null,
  "instructions": null,
  "max_output_tokens": null,
  "max_tool_calls": null,
  "model": "gpt-5.4",
  "output": [
      "id": "msg_686eef60d3e081a29283bdcbc4322fd90e34c516d176ff86",
      "type": "message",
      "status": "completed",
      "content": [
          "type": "output_text",
          "annotations": [],
          "logprobs": [],
          "text": "The file seems to contain excerpts from a letter to the shareholders of Berkshire Hathaway Inc., likely written by Warren Buffett. It covers several topics:\n\n1. **Communication Philosophy**: Buffett emphasizes the importance of transparency and candidness in reporting mistakes and successes to shareholders.\n\n2. **Mistakes and Learnings**: The letter acknowledges past mistakes in business assessments and management hires, highlighting the importance of correcting errors promptly.\n\n3. **CEO Succession**: Mention of Greg Abel stepping in as the new CEO and continuing the tradition of honest communication.\n\n4. **Pete Liegl Story**: A detailed account of acquiring Forest River and the relationship with its founder, highlighting trust and effective business decisions.\n\n5. **2024 Performance**: Overview of business performance, particularly in insurance and investment activities, with a focus on GEICO's improvement.\n\n6. **Tax Contributions**: Discussion of significant tax payments to the U.S. Treasury, credited to shareholders' reinvestments.\n\n7. **Investment Strategy**: A breakdown of Berkshire\u2019s investments in both controlled subsidiaries and marketable equities, along with a focus on long-term holding strategies.\n\n8. **American Capitalism**: Reflections on America\u2019s economic development and Berkshire\u2019s role within it.\n\n9. **Property-Casualty Insurance**: Insights into the P/C insurance business model and its challenges and benefits.\n\n10. **Japanese Investments**: Information about Berkshire\u2019s investments in Japanese companies and future plans.\n\n11. **Annual Meeting**: Details about the upcoming annual gathering in Omaha, including schedule changes and new book releases.\n\n12. **Personal Anecdotes**: Light-hearted stories about family and interactions, conveying Buffett's personable approach.\n\n13. **Financial Performance Data**: Tables comparing Berkshire\u2019s annual performance to the S&P 500, showing impressive long-term gains.\n\nOverall, the letter reinforces Berkshire Hathaway's commitment to transparency, investment in both its businesses and the wider economy, and emphasizes strong leadership and prudent financial management."
      ],
      "role": "assistant"
  ],
  "parallel_tool_calls": true,
  "previous_response_id": null,
  "reasoning": {
    "effort": null,
    "summary": null
  },
  "service_tier": "default",
  "store": true,
  "temperature": 1.0,
  "text": {
    "format": {
      "type": "text"
  },
  "tool_choice": "auto",
  "tools": [],
  "top_logprobs": 0,
  "top_p": 1.0,
  "truncation": "disabled",
  "usage": {
    "input_tokens": 8438,
    "input_tokens_details": {
      "cached_tokens": 0,
      "cache_write_tokens": 0
    },
    "output_tokens": 398,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "total_tokens": 8836
  },
  "user": null,
  "metadata": {}

### Create a model response

TypeScript

import OpenAI from "openai";

const openai = new OpenAI();

const response = await openai.responses.create({
    model: "gpt-5.4",
    tools: [{ type: "web_search_preview" }],
    input: "What was a positive news story from today?",
});

console.log(response);

  "id": "resp_67ccf18ef5fc8190b16dbee19bc54e5f087bb177ab789d5c",
  "object": "response",
  "created_at": 1741484430,
  "status": "completed",
  "completed_at": 1741484431,
  "error": null,
  "incomplete_details": null,
  "instructions": null,
  "max_output_tokens": null,
  "model": "gpt-5.4",
  "output": [
      "type": "web_search_call",
      "id": "ws_67ccf18f64008190a39b619f4c8455ef087bb177ab789d5c",
      "status": "completed"
    },
      "type": "message",
      "id": "msg_67ccf190ca3881909d433c50b1f6357e087bb177ab789d5c",
      "status": "completed",
      "role": "assistant",
      "content": [
          "type": "output_text",
          "text": "As of today, March 9, 2025, one notable positive news story...",
          "annotations": [
              "type": "url_citation",
              "start_index": 442,
              "end_index": 557,
              "url": "https://.../?utm_source=chatgpt.com",
              "title": "..."
            },
              "type": "url_citation",
              "start_index": 962,
              "end_index": 1077,
              "url": "https://.../?utm_source=chatgpt.com",
              "title": "..."
            },
              "type": "url_citation",
              "start_index": 1336,
              "end_index": 1451,
              "url": "https://.../?utm_source=chatgpt.com",
              "title": "..."
          ]
      ]
  ],
  "parallel_tool_calls": true,
  "previous_response_id": null,
  "reasoning": {
    "effort": null,
    "summary": null
  },
  "store": true,
  "temperature": 1.0,
  "text": {
    "format": {
      "type": "text"
  },
  "tool_choice": "auto",
  "tools": [
      "type": "web_search_preview",
      "domains": [],
      "search_context_size": "medium",
      "user_location": {
        "type": "approximate",
        "city": null,
        "country": "US",
        "region": null,
        "timezone": null
  ],
  "top_p": 1.0,
  "truncation": "disabled",
  "usage": {
    "input_tokens": 328,
    "input_tokens_details": {
      "cached_tokens": 0,
      "cache_write_tokens": 0
    },
    "output_tokens": 356,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "total_tokens": 684
  },
  "user": null,
  "metadata": {}

### Create a model response

TypeScript

import OpenAI from "openai";

const openai = new OpenAI();

const response = await openai.responses.create({
    model: "gpt-5.4",
    tools: [{
      type: "file_search",
      vector_store_ids: ["vs_1234567890"],
      max_num_results: 20
    }],
    input: "What are the attributes of an ancient brown dragon?",
});

console.log(response);

  "id": "resp_67ccf4c55fc48190b71bd0463ad3306d09504fb6872380d7",
  "object": "response",
  "created_at": 1741485253,
  "status": "completed",
  "completed_at": 1741485254,
  "error": null,
  "incomplete_details": null,
  "instructions": null,
  "max_output_tokens": null,
  "model": "gpt-5.4",
  "output": [
      "type": "file_search_call",
      "id": "fs_67ccf4c63cd08190887ef6464ba5681609504fb6872380d7",
      "status": "completed",
      "queries": [
        "attributes of an ancient brown dragon"
      ],
      "results": null
    },
      "type": "message",
      "id": "msg_67ccf4c93e5c81909d595b369351a9d309504fb6872380d7",
      "status": "completed",
      "role": "assistant",
      "content": [
          "type": "output_text",
          "text": "The attributes of an ancient brown dragon include...",
          "annotations": [
              "type": "file_citation",
              "index": 320,
              "file_id": "file-4wDz5b167pAf72nx1h9eiN",
              "filename": "dragons.pdf"
            },
              "type": "file_citation",
              "index": 576,
              "file_id": "file-4wDz5b167pAf72nx1h9eiN",
              "filename": "dragons.pdf"
            },
              "type": "file_citation",
              "index": 815,
              "file_id": "file-4wDz5b167pAf72nx1h9eiN",
              "filename": "dragons.pdf"
            },
              "type": "file_citation",
              "index": 815,
              "file_id": "file-4wDz5b167pAf72nx1h9eiN",
              "filename": "dragons.pdf"
            },
              "type": "file_citation",
              "index": 1030,
              "file_id": "file-4wDz5b167pAf72nx1h9eiN",
              "filename": "dragons.pdf"
            },
              "type": "file_citation",
              "index": 1030,
              "file_id": "file-4wDz5b167pAf72nx1h9eiN",
              "filename": "dragons.pdf"
            },
              "type": "file_citation",
              "index": 1156,
              "file_id": "file-4wDz5b167pAf72nx1h9eiN",
              "filename": "dragons.pdf"
            },
              "type": "file_citation",
              "index": 1225,
              "file_id": "file-4wDz5b167pAf72nx1h9eiN",
              "filename": "dragons.pdf"
          ]
      ]
  ],
  "parallel_tool_calls": true,
  "previous_response_id": null,
  "reasoning": {
    "effort": null,
    "summary": null
  },
  "store": true,
  "temperature": 1.0,
  "text": {
    "format": {
      "type": "text"
  },
  "tool_choice": "auto",
  "tools": [
      "type": "file_search",
      "filters": null,
      "max_num_results": 20,
      "ranking_options": {
        "ranker": "auto",
        "score_threshold": 0.0
      },
      "vector_store_ids": [
        "vs_1234567890"
      ]
  ],
  "top_p": 1.0,
  "truncation": "disabled",
  "usage": {
    "input_tokens": 18307,
    "input_tokens_details": {
      "cached_tokens": 0,
      "cache_write_tokens": 0
    },
    "output_tokens": 348,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "total_tokens": 18655
  },
  "user": null,
  "metadata": {}

### Create a model response

TypeScript

import OpenAI from "openai";

const openai = new OpenAI();

const response = await openai.responses.create({
    model: "gpt-5.4",
    instructions: "You are a helpful assistant.",
    input: "Hello!",
    stream: true,
});

for await (const event of response) {
    console.log(event);

event: response.created
data: {"type":"response.created","response":{"id":"resp_67c9fdcecf488190bdd9a0409de3a1ec07b8b0ad4e5eb654","object":"response","created_at":1741290958,"status":"in_progress","error":null,"incomplete_details":null,"instructions":"You are a helpful assistant.","max_output_tokens":null,"model":"gpt-5.4","output":[],"parallel_tool_calls":true,"previous_response_id":null,"reasoning":{"effort":null,"summary":null},"store":true,"temperature":1.0,"text":{"format":{"type":"text"}},"tool_choice":"auto","tools":[],"top_p":1.0,"truncation":"disabled","usage":null,"user":null,"metadata":{}}}

event: response.in_progress
data: {"type":"response.in_progress","response":{"id":"resp_67c9fdcecf488190bdd9a0409de3a1ec07b8b0ad4e5eb654","object":"response","created_at":1741290958,"status":"in_progress","error":null,"incomplete_details":null,"instructions":"You are a helpful assistant.","max_output_tokens":null,"model":"gpt-5.4","output":[],"parallel_tool_calls":true,"previous_response_id":null,"reasoning":{"effort":null,"summary":null},"store":true,"temperature":1.0,"text":{"format":{"type":"text"}},"tool_choice":"auto","tools":[],"top_p":1.0,"truncation":"disabled","usage":null,"user":null,"metadata":{}}}

event: response.output_item.added
data: {"type":"response.output_item.added","output_index":0,"item":{"id":"msg_67c9fdcf37fc8190ba82116e33fb28c507b8b0ad4e5eb654","type":"message","status":"in_progress","role":"assistant","content":[]}}

event: response.content_part.added
data: {"type":"response.content_part.added","item_id":"msg_67c9fdcf37fc8190ba82116e33fb28c507b8b0ad4e5eb654","output_index":0,"content_index":0,"part":{"type":"output_text","text":"","annotations":[]}}

event: response.output_text.delta
data: {"type":"response.output_text.delta","item_id":"msg_67c9fdcf37fc8190ba82116e33fb28c507b8b0ad4e5eb654","output_index":0,"content_index":0,"delta":"Hi"}

...

event: response.output_text.done
data: {"type":"response.output_text.done","item_id":"msg_67c9fdcf37fc8190ba82116e33fb28c507b8b0ad4e5eb654","output_index":0,"content_index":0,"text":"Hi there! How can I assist you today?"}

event: response.content_part.done
data: {"type":"response.content_part.done","item_id":"msg_67c9fdcf37fc8190ba82116e33fb28c507b8b0ad4e5eb654","output_index":0,"content_index":0,"part":{"type":"output_text","text":"Hi there! How can I assist you today?","annotations":[]}}

event: response.output_item.done
data: {"type":"response.output_item.done","output_index":0,"item":{"id":"msg_67c9fdcf37fc8190ba82116e33fb28c507b8b0ad4e5eb654","type":"message","status":"completed","role":"assistant","content":[{"type":"output_text","text":"Hi there! How can I assist you today?","annotations":[]}]}}

event: response.completed
data: {"type":"response.completed","response":{"id":"resp_67c9fdcecf488190bdd9a0409de3a1ec07b8b0ad4e5eb654","object":"response","created_at":1741290958,"status":"completed","error":null,"incomplete_details":null,"instructions":"You are a helpful assistant.","max_output_tokens":null,"model":"gpt-5.4","output":[{"id":"msg_67c9fdcf37fc8190ba82116e33fb28c507b8b0ad4e5eb654","type":"message","status":"completed","role":"assistant","content":[{"type":"output_text","text":"Hi there! How can I assist you today?","annotations":[]}]}],"parallel_tool_calls":true,"previous_response_id":null,"reasoning":{"effort":null,"summary":null},"store":true,"temperature":1.0,"text":{"format":{"type":"text"}},"tool_choice":"auto","tools":[],"top_p":1.0,"truncation":"disabled","usage":{"input_tokens":37,"output_tokens":11,"output_tokens_details":{"reasoning_tokens":0},"total_tokens":48},"user":null,"metadata":{}}}

### Create a model response

TypeScript

import OpenAI from "openai";

const openai = new OpenAI();

const tools = [
        type: "function",
        name: "get_current_weather",
        description: "Get the current weather in a given location",
        parameters: {
            type: "object",
            properties: {
                location: {
                    type: "string",
                    description: "The city and state, e.g. San Francisco, CA",
                },
                unit: { type: "string", enum: ["celsius", "fahrenheit"] },
            },
            required: ["location", "unit"],
        },
    },
];

const response = await openai.responses.create({
    model: "gpt-5.4",
    tools: tools,
    input: "What is the weather like in Boston today?",
    tool_choice: "auto",
});

console.log(response);

  "id": "resp_67ca09c5efe0819096d0511c92b8c890096610f474011cc0",
  "object": "response",
  "created_at": 1741294021,
  "status": "completed",
  "completed_at": 1741294022,
  "error": null,
  "incomplete_details": null,
  "instructions": null,
  "max_output_tokens": null,
  "model": "gpt-5.4",
  "output": [
      "type": "function_call",
      "id": "fc_67ca09c6bedc8190a7abfec07b1a1332096610f474011cc0",
      "call_id": "call_unLAR8MvFNptuiZK6K6HCy5k",
      "name": "get_current_weather",
      "arguments": "{\"location\":\"Boston, MA\",\"unit\":\"celsius\"}",
      "status": "completed"
  ],
  "parallel_tool_calls": true,
  "previous_response_id": null,
  "reasoning": {
    "effort": null,
    "summary": null
  },
  "store": true,
  "temperature": 1.0,
  "text": {
    "format": {
      "type": "text"
  },
  "tool_choice": "auto",
  "tools": [
      "type": "function",
      "description": "Get the current weather in a given location",
      "name": "get_current_weather",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The city and state, e.g. San Francisco, CA"
          },
          "unit": {
            "type": "string",
            "enum": [
              "celsius",
              "fahrenheit"
            ]
        },
        "required": [
          "location",
          "unit"
        ]
      },
      "strict": true
  ],
  "top_p": 1.0,
  "truncation": "disabled",
  "usage": {
    "input_tokens": 291,
    "output_tokens": 23,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "total_tokens": 314
  },
  "user": null,
  "metadata": {}

### Create a model response

TypeScript

import OpenAI from "openai";
const openai = new OpenAI();

const response = await openai.responses.create({
    model: "o3-mini",
    input: "How much wood would a woodchuck chuck?",
    reasoning: {
      effort: "high"
});

console.log(response);

  "id": "resp_67ccd7eca01881908ff0b5146584e408072912b2993db808",
  "object": "response",
  "created_at": 1741477868,
  "status": "completed",
  "completed_at": 1741477869,
  "error": null,
  "incomplete_details": null,
  "instructions": null,
  "max_output_tokens": null,
  "model": "o1-2024-12-17",
  "output": [
      "type": "message",
      "id": "msg_67ccd7f7b5848190a6f3e95d809f6b44072912b2993db808",
      "status": "completed",
      "role": "assistant",
      "content": [
          "type": "output_text",
          "text": "The classic tongue twister...",
          "annotations": []
      ]
  ],
  "parallel_tool_calls": true,
  "previous_response_id": null,
  "reasoning": {
    "effort": "high",
    "summary": null
  },
  "store": true,
  "temperature": 1.0,
  "text": {
    "format": {
      "type": "text"
  },
  "tool_choice": "auto",
  "tools": [],
  "top_p": 1.0,
  "truncation": "disabled",
  "usage": {
    "input_tokens": 81,
    "input_tokens_details": {
      "cached_tokens": 0,
      "cache_write_tokens": 0
    },
    "output_tokens": 1035,
    "output_tokens_details": {
      "reasoning_tokens": 832
    },
    "total_tokens": 1116
  },
  "user": null,
  "metadata": {}

200 example

  "id": "id",
  "created_at": 0,
  "error": {
    "code": "server_error",
    "message": "message"
  },
  "incomplete_details": {
    "reason": "max_output_tokens"
  },
  "instructions": "string",
  "metadata": {
    "foo": "string"
  },
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
      "agent": {
        "agent_name": "agent_name"
      },
      "phase": "commentary"
  ],
  "parallel_tool_calls": true,
  "temperature": 1,
  "tool_choice": "none",
  "tools": [
      "name": "name",
      "parameters": {
        "foo": "bar"
      },
      "strict": true,
      "type": "function",
      "allowed_callers": [
        "direct"
      ],
      "defer_loading": true,
      "description": "description",
      "output_schema": {
        "foo": "bar"
  ],
  "top_p": 1,
  "background": true,
  "completed_at": 0,
  "conversation": {
    "id": "id"
  },
  "max_output_tokens": 0,
  "max_tool_calls": 0,
  "moderation": {
    "input": {
      "categories": {
        "foo": true
      },
      "category_applied_input_types": {
        "foo": [
          "text"
        ]
      },
      "category_scores": {
        "foo": 0
      },
      "flagged": true,
      "model": "model",
      "type": "moderation_result"
    },
    "output": {
      "categories": {
        "foo": true
      },
      "category_applied_input_types": {
        "foo": [
          "text"
        ]
      },
      "category_scores": {
        "foo": 0
      },
      "flagged": true,
      "model": "model",
      "type": "moderation_result"
  },
  "output_text": "output_text",
  "previous_response_id": "previous_response_id",
  "prompt": {
    "id": "id",
    "variables": {
      "foo": "string"
    },
    "version": "version"
  },
  "prompt_cache_key": "prompt-cache-key-1234",
  "prompt_cache_options": {
    "mode": "implicit",
    "ttl": "30m"
  },
  "prompt_cache_retention": "in_memory",
  "reasoning": {
    "context": "auto",
    "effort": "none",
    "generate_summary": "auto",
    "mode": "standard",
    "summary": "auto"
  },
  "safety_identifier": "safety-identifier-1234",
  "service_tier": "auto",
  "status": "completed",
  "text": {
    "format": {
      "type": "text"
    },
    "verbosity": "low"
  },
  "top_logprobs": 0,
  "truncation": "auto",
  "usage": {
    "input_tokens": 0,
    "input_tokens_details": {
      "cache_write_tokens": 0,
      "cached_tokens": 0
    },
    "output_tokens": 0,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "total_tokens": 0
  },
  "user": "user-1234"
