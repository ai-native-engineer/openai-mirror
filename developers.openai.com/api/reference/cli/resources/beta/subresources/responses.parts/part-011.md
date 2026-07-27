<!-- source: https://developers.openai.com/api/reference/cli/resources/beta/subresources/responses/ -->
<!-- part of: https://developers.openai.com/api/reference/cli/resources/beta/subresources/responses/ -->

<!-- chunk-start -->

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

beta\_response\_input\_image: object { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: "low" or "high" or "auto" or "original"

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

type: "input\_image"

The type of the input item. Always `input_image`.

file\_id: optional string

The ID of the file to be sent to the model.

image\_url: optional string

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

prompt\_cache\_breakpoint: optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

beta\_response\_input\_file: object { type, detail, file\_data, 4 more }

A file input to the model.

type: "input\_file"

The type of the input item. Always `input_file`.

detail: optional "auto" or "low" or "high"

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

"low"

"high"

file\_data: optional string

The content of the file to be sent to the model.

file\_id: optional string

The ID of the file to be sent to the model.

file\_url: optional string

The URL of the file to be sent to the model.

filename: optional string

The name of the file to be sent to the model.

prompt\_cache\_breakpoint: optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

status: "in\_progress" or "completed" or "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: "function\_call\_output"

The type of the function tool call output. Always `function_call_output`.

agent: optional object { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller: optional object { type }  or object { caller\_id, type }

The execution context that produced this tool call.

direct: object { type }

program: object { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

type: "program"

The caller type. Always `program`.

created\_by: optional string

The identifier of the actor that created the item.

agent\_message: object { id, author, content, 3 more }

id: string

The unique ID of the agent message.

author: string

The sending agent identity.

content: array of [BetaResponseInputText](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [BetaResponseOutputText](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema)) { annotations, text, type, logprobs }  or object { text, type }  or 7 more

Encrypted content sent between agents.

beta\_response\_input\_text: object { text, type, prompt\_cache\_breakpoint }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

beta\_response\_output\_text: object { annotations, text, type, logprobs }

A text output from the model.

annotations: array of object { file\_id, filename, index, type }  or object { end\_index, start\_index, title, 2 more }  or object { container\_id, end\_index, file\_id, 3 more }  or object { file\_id, index, type }

The annotations of the text output.

file\_citation: object { file\_id, filename, index, type }

A citation to a file.

file\_id: string

The ID of the file.

filename: string

The filename of the file cited.

index: number

The index of the file in the list of files.

type: "file\_citation"

The type of the file citation. Always `file_citation`.

url\_citation: object { end\_index, start\_index, title, 2 more }

A citation for a web resource used to generate a model response.

end\_index: number

The index of the last character of the URL citation in the message.

start\_index: number

The index of the first character of the URL citation in the message.

title: string

The title of the web resource.

type: "url\_citation"

The type of the URL citation. Always `url_citation`.

url: string

The URL of the web resource.

container\_file\_citation: object { container\_id, end\_index, file\_id, 3 more }

A citation for a container file used to generate a model response.

container\_id: string

The ID of the container file.

end\_index: number

The index of the last character of the container file citation in the message.

file\_id: string

The ID of the file.

filename: string

The filename of the container file cited.

start\_index: number

The index of the first character of the container file citation in the message.

type: "container\_file\_citation"

The type of the container file citation. Always `container_file_citation`.

file\_path: object { file\_id, index, type }

A path to a file.

file\_id: string

The ID of the file.

index: number

The index of the file in the list of files.

type: "file\_path"

The type of the file path. Always `file_path`.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

logprobs: optional array of object { token, bytes, logprob, top\_logprobs }

token: string

bytes: array of number

logprob: number

top\_logprobs: array of object { token, bytes, logprob }

token: string

bytes: array of number

logprob: number

text: object { text, type }

A text content.

text: string

type: "text"

summary\_text: object { text, type }

A summary text from the model.

text: string

A summary of the reasoning output from the model so far.

type: "summary\_text"

The type of the object. Always `summary_text`.

reasoning\_text: object { text, type }

Reasoning text from the model.

text: string

The reasoning text from the model.

type: "reasoning\_text"

The type of the reasoning text. Always `reasoning_text`.

beta\_response\_output\_refusal: object { refusal, type }

A refusal from the model.

refusal: string

The refusal explanation from the model.

type: "refusal"

The type of the refusal. Always `refusal`.

beta\_response\_input\_image: object { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: "low" or "high" or "auto" or "original"

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

type: "input\_image"

The type of the input item. Always `input_image`.

file\_id: optional string

The ID of the file to be sent to the model.

image\_url: optional string

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

prompt\_cache\_breakpoint: optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

computer\_screenshot: object { detail, file\_id, image\_url, 2 more }

A screenshot of a computer.

detail: "low" or "high" or "auto" or "original"

The detail level of the screenshot image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

file\_id: string

The identifier of an uploaded file that contains the screenshot.

image\_url: string

The URL of the screenshot image.

type: "computer\_screenshot"

Specifies the event type. For a computer screenshot, this property is always set to `computer_screenshot`.

prompt\_cache\_breakpoint: optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

beta\_response\_input\_file: object { type, detail, file\_data, 4 more }

A file input to the model.

type: "input\_file"

The type of the input item. Always `input_file`.

detail: optional "auto" or "low" or "high"

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

"low"

"high"

file\_data: optional string

The content of the file to be sent to the model.

file\_id: optional string

The ID of the file to be sent to the model.

file\_url: optional string

The URL of the file to be sent to the model.

filename: optional string

The name of the file to be sent to the model.

prompt\_cache\_breakpoint: optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

encrypted\_content: object { encrypted\_content, type }

Opaque encrypted content that Responses API decrypts inside trusted model execution.

encrypted\_content: string

Opaque encrypted content.

type: "encrypted\_content"

The type of the input item. Always `encrypted_content`.

recipient: string

The destination agent identity.

type: "agent\_message"

The type of the item. Always `agent_message`.

agent: optional object { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

multi\_agent\_call: object { id, action, arguments, 3 more }

id: string

The unique ID of the multi-agent call item.

action: "spawn\_agent" or "interrupt\_agent" or "list\_agents" or 3 more

The multi-agent action to execute.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

arguments: string

The JSON string of arguments generated for the action.

call\_id: string

The unique ID linking this call to its output.

type: "multi\_agent\_call"

The type of the multi-agent call. Always `multi_agent_call`.

agent: optional object { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

multi\_agent\_call\_output: object { id, action, call\_id, 3 more }

id: string

The unique ID of the multi-agent call output item.

action: "spawn\_agent" or "interrupt\_agent" or "list\_agents" or 3 more

The multi-agent action that produced this result.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

call\_id: string

The unique ID of the multi-agent call.

output: array of [BetaResponseOutputText](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema)) { annotations, text, type, logprobs }

Text output returned by the multi-agent action.

annotations: array of object { file\_id, filename, index, type }  or object { end\_index, start\_index, title, 2 more }  or object { container\_id, end\_index, file\_id, 3 more }  or object { file\_id, index, type }

The annotations of the text output.

file\_citation: object { file\_id, filename, index, type }

A citation to a file.

file\_id: string

The ID of the file.

filename: string

The filename of the file cited.

index: number

The index of the file in the list of files.

type: "file\_citation"

The type of the file citation. Always `file_citation`.

url\_citation: object { end\_index, start\_index, title, 2 more }

A citation for a web resource used to generate a model response.

end\_index: number

The index of the last character of the URL citation in the message.

start\_index: number

The index of the first character of the URL citation in the message.

title: string

The title of the web resource.

type: "url\_citation"

The type of the URL citation. Always `url_citation`.

url: string

The URL of the web resource.

container\_file\_citation: object { container\_id, end\_index, file\_id, 3 more }

A citation for a container file used to generate a model response.

container\_id: string

The ID of the container file.

end\_index: number

The index of the last character of the container file citation in the message.

file\_id: string

The ID of the file.

filename: string

The filename of the container file cited.

start\_index: number

The index of the first character of the container file citation in the message.

type: "container\_file\_citation"

The type of the container file citation. Always `container_file_citation`.

file\_path: object { file\_id, index, type }

A path to a file.

file\_id: string

The ID of the file.

index: number

The index of the file in the list of files.

type: "file\_path"

The type of the file path. Always `file_path`.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

logprobs: optional array of object { token, bytes, logprob, top\_logprobs }

token: string

bytes: array of number

logprob: number

top\_logprobs: array of object { token, bytes, logprob }

token: string

bytes: array of number

logprob: number

type: "multi\_agent\_call\_output"

The type of the multi-agent result. Always `multi_agent_call_output`.

agent: optional object { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

beta\_response\_tool\_search\_call: object { id, arguments, call\_id, 5 more }

id: string

The unique ID of the tool search call item.

arguments: unknown

Arguments used for the tool search call.

call\_id: string

The unique ID of the tool search call generated by the model.

execution: "server" or "client"

Whether tool search was executed by the server or by the client.

"server"

"client"

status: "in\_progress" or "completed" or "incomplete"

The status of the tool search call item that was recorded.

"in\_progress"

"completed"

"incomplete"

type: "tool\_search\_call"

The type of the item. Always `tool_search_call`.

agent: optional object { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

created\_by: optional string

The identifier of the actor that created the item.

beta\_response\_tool\_search\_output\_item: object { id, call\_id, execution, 5 more }

id: string

The unique ID of the tool search output item.

call\_id: string

The unique ID of the tool search call generated by the model.

execution: "server" or "client"

Whether tool search was executed by the server or by the client.

"server"

"client"

status: "in\_progress" or "completed" or "incomplete"

The status of the tool search output item that was recorded.

"in\_progress"

"completed"

"incomplete"

tools: array of [BetaTool](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))

The loaded tool definitions returned by tool search.

beta\_function\_tool: object { name, parameters, strict, 5 more }

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: string

The name of the function to call.

parameters: map[unknown]

A JSON schema object describing the parameters of the function.

strict: boolean

Whether strict parameter validation is enforced for this function tool.

type: "function"

The type of the function tool. Always `function`.

allowed\_callers: optional array of "direct" or "programmatic"

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: optional boolean

Whether this function is deferred and loaded via tool search.

description: optional string

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema: optional map[unknown]

A JSON schema object describing the JSON value encoded in string outputs for this function.

beta\_file\_search\_tool: object { type, vector\_store\_ids, filters, 2 more }

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: "file\_search"

The type of the file search tool. Always `file_search`.

vector\_store\_ids: array of string

The IDs of the vector stores to search.

filters: optional object { key, type, value }  or object { filters, type }

A filter to apply.

Comparison Filter: object { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" or "ne" or "gt" or 5 more

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

value: string or number or boolean or array of string or number

The value to compare against the attribute key; supports string, number, or boolean types.

union\_member\_0: string

union\_member\_1: number

union\_member\_2: boolean

union\_member\_3: array of string or number

union\_member\_0: string

union\_member\_1: number

Compound Filter: object { filters, type }

Combine multiple filters using `and` or `or`.

filters: array of object { key, type, value }  or unknown

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

Comparison Filter: object { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" or "ne" or "gt" or 5 more

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

value: string or number or boolean or array of string or number

The value to compare against the attribute key; supports string, number, or boolean types.

union\_member\_0: string

union\_member\_1: number

union\_member\_2: boolean

union\_member\_3: array of string or number

union\_member\_0: string

union\_member\_1: number

union\_member\_1: unknown

type: "and" or "or"

Type of operation: `and` or `or`.

"and"

"or"

max\_num\_results: optional number

The maximum number of results to return. This number should be between 1 and 50 inclusive.

ranking\_options: optional object { hybrid\_search, ranker, score\_threshold }

Ranking options for search.

hybrid\_search: optional object { embedding\_weight, text\_weight }

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

embedding\_weight: number

The weight of the embedding in the reciprocal ranking fusion.

text\_weight: number

The weight of the text in the reciprocal ranking fusion.

ranker: optional "auto" or "default-2024-11-15"

The ranker to use for the file search.

"auto"

"default-2024-11-15"

score\_threshold: optional number

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

beta\_computer\_tool: object { type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: "computer"

The type of the computer tool. Always `computer`.

beta\_computer\_use\_preview\_tool: object { display\_height, display\_width, environment, type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: number

The height of the computer display.

display\_width: number

The width of the computer display.

environment: "windows" or "mac" or "linux" or 2 more

The type of computer environment to control.

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

The type of the computer use tool. Always `computer_use_preview`.

beta\_web\_search\_tool: object { type, filters, search\_context\_size, user\_location }

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search" or "web\_search\_2025\_08\_26"

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

"web\_search"

"web\_search\_2025\_08\_26"

filters: optional object { allowed\_domains }

Filters for the search.

allowed\_domains: optional array of string

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size: optional "low" or "medium" or "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location: optional object { city, country, region, 2 more }

The approximate location of the user.

city: optional string

Free text input for the city of the user, e.g. `San Francisco`.

country: optional string

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region: optional string

Free text input for the region of the user, e.g. `California`.

timezone: optional string

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type: optional "approximate"

The type of location approximation. Always `approximate`.

"approximate"

mcp: object { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: string

A label for this MCP server, used to identify it in tool calls.

type: "mcp"

The type of the MCP tool. Always `mcp`.

allowed\_callers: optional array of "direct" or "programmatic"

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools: optional array of string or object { read\_only, tool\_names }

List of allowed tool names or a filter object.

MCP allowed tools: array of string

A string array of allowed tool names

MCP tool filter: object { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only: optional boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: optional array of string

List of allowed tool names.

authorization: optional string

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

connector\_id: optional "connector\_dropbox" or "connector\_gmail" or "connector\_googlecalendar" or 5 more

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

defer\_loading: optional boolean

Whether this MCP tool is deferred and discovered via tool search.

headers: optional map[string]

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval: optional object { always, never }  or "always" or "never"

Specify which of the MCP server’s tools require approval.

MCP tool approval filter: object { always, never }

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always: optional object { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only: optional boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: optional array of string

List of allowed tool names.

never: optional object { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only: optional boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: optional array of string

List of allowed tool names.

MCP tool approval setting: "always" or "never"

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: optional string

Optional description of the MCP server, used to provide more context.

server\_url: optional string

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

tunnel\_id: optional string

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

code\_interpreter: object { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string or object { type, file\_ids, memory\_limit, network\_policy }

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

union\_member\_0: string

The container ID.

CodeInterpreterToolAuto: object { type, file\_ids, memory\_limit, network\_policy }

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: "auto"

Always `auto`.

file\_ids: optional array of string

An optional list of uploaded files to make available to your code.

memory\_limit: optional "1g" or "4g" or "16g" or "64g"

The memory limit for the code interpreter container.

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [BetaContainerNetworkPolicyDisabled](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  or [BetaContainerNetworkPolicyAllowlist](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

beta\_container\_network\_policy\_disabled: object { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

beta\_container\_network\_policy\_allowlist: object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: optional array of [BetaContainerNetworkPolicyDomainSecret](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

name: string

The name of the secret to inject for the domain.

value: string

The secret value to inject for the domain.

type: "code\_interpreter"

The type of the code interpreter tool. Always `code_interpreter`.

allowed\_callers: optional array of "direct" or "programmatic"

The tool invocation context(s).

"direct"

"programmatic"

programmatic\_tool\_calling: object { type }

image\_generation: object { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

The type of the image generation tool. Always `image_generation`.

action: optional "generate" or "edit" or "auto"

Whether to generate a new image or edit an existing image. Default: `auto`.

"generate"

"edit"

"auto"

background: optional "transparent" or "opaque" or "auto"

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

input\_fidelity: optional "high" or "low"

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

"high"

"low"

input\_image\_mask: optional object { file\_id, image\_url }

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

file\_id: optional string

File ID for the mask image.

image\_url: optional string

Base64-encoded mask image.

model: optional string or "gpt-image-1" or "gpt-image-1-mini" or "gpt-image-2" or 3 more

The image generation model to use. Default: `gpt-image-1`.

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: optional "auto" or "low"

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression: optional number

Compression level for the output image. Default: 100.

output\_format: optional "png" or "webp" or "jpeg"

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

"png"

"webp"

"jpeg"

partial\_images: optional number

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

quality: optional "low" or "medium" or "high" or "auto"

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

"low"

"medium"

"high"

"auto"

size: optional string or "1024x1024" or "1024x1536" or "1536x1024" or "auto"

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

local\_shell: object { type }

A tool that allows the model to execute shell commands in a local environment.

beta\_function\_shell\_tool: object { type, allowed\_callers, environment }

A tool that allows the model to execute shell commands.

type: "shell"

The type of the shell tool. Always `shell`.

allowed\_callers: optional array of "direct" or "programmatic"

The tool invocation context(s).

"direct"

"programmatic"

environment: optional [BetaContainerAuto](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  or [BetaLocalEnvironment](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  or [BetaContainerReference](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }

beta\_container\_auto: object { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

Automatically creates a container for this request

file\_ids: optional array of string

An optional list of uploaded files to make available to your code.

memory\_limit: optional "1g" or "4g" or "16g" or "64g"

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [BetaContainerNetworkPolicyDisabled](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  or [BetaContainerNetworkPolicyAllowlist](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

beta\_container\_network\_policy\_disabled: object { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

beta\_container\_network\_policy\_allowlist: object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: optional array of [BetaContainerNetworkPolicyDomainSecret](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

name: string

The name of the secret to inject for the domain.

value: string

The secret value to inject for the domain.

skills: optional array of [BetaSkillReference](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_skill_reference%20%3E%20(schema)) { skill\_id, type, version }  or [BetaInlineSkill](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill%20%3E%20(schema)) { description, name, source, type }

An optional list of skills referenced by id or inline data.

beta\_skill\_reference: object { skill\_id, type, version }

skill\_id: string

The ID of the referenced skill.

type: "skill\_reference"

References a skill created with the /v1/skills endpoint.

version: optional string

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

beta\_inline\_skill: object { description, name, source, type }

description: string

The description of the skill.

name: string

The name of the skill.

source: object { data, media\_type, type }

Inline skill payload

data: string

Base64-encoded skill zip bundle.

media\_type: "application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: "base64"

The type of the inline skill source. Must be `base64`.

type: "inline"

Defines an inline skill for this request.

beta\_local\_environment: object { type, skills }

type: "local"

Use a local computer environment.

skills: optional array of [BetaLocalSkill](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path }

An optional list of skills.

description: string

The description of the skill.

name: string

The name of the skill.

path: string

The path to the directory containing the skill.

beta\_container\_reference: object { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

beta\_custom\_tool: object { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers: optional array of "direct" or "programmatic"

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: optional boolean

Whether this tool should be deferred and discovered via tool search.

description: optional string

Optional description of the custom tool, used to provide more context.

format: optional object { type }  or object { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

text: object { type }

Unconstrained free-form text.

grammar: object { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" or "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

beta\_namespace\_tool: object { description, name, tools, type }

Groups function/custom tools under a shared namespace.

description: string

A description of the namespace shown to the model.

name: string

The namespace name used in tool calls (for example, `crm`).

tools: array of object { name, type, allowed\_callers, 5 more }  or [BetaCustomTool](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_custom_tool%20%3E%20(schema)) { name, type, allowed\_callers, 3 more }

The function/custom tools available inside this namespace.

function: object { name, type, allowed\_callers, 5 more }

name: string

type: "function"

allowed\_callers: optional array of "direct" or "programmatic"

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: optional boolean

Whether this function should be deferred and discovered via tool search.

description: optional string

output\_schema: optional map[unknown]

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters: optional unknown

strict: optional boolean

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

beta\_custom\_tool: object { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers: optional array of "direct" or "programmatic"

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: optional boolean

Whether this tool should be deferred and discovered via tool search.

description: optional string

Optional description of the custom tool, used to provide more context.

format: optional object { type }  or object { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

text: object { type }

Unconstrained free-form text.

grammar: object { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" or "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

type: "namespace"

The type of the tool. Always `namespace`.

beta\_tool\_search\_tool: object { type, description, execution, parameters }

Hosted or BYOT tool search configuration for deferred tools.

type: "tool\_search"

The type of the tool. Always `tool_search`.

description: optional string

Description shown to the model for a client-executed tool search tool.

execution: optional "server" or "client"

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters: optional unknown

Parameter schema for a client-executed tool search tool.

beta\_web\_search\_preview\_tool: object { type, search\_content\_types, search\_context\_size, user\_location }

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search\_preview" or "web\_search\_preview\_2025\_03\_11"

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: optional array of "text" or "image"

"text"

"image"

search\_context\_size: optional "low" or "medium" or "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location: optional object { type, city, country, 2 more }

The user’s location.

type: "approximate"

The type of location approximation. Always `approximate`.

city: optional string

Free text input for the city of the user, e.g. `San Francisco`.

country: optional string

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region: optional string

Free text input for the region of the user, e.g. `California`.

timezone: optional string

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

beta\_apply\_patch\_tool: object { type, allowed\_callers }

Allows the assistant to create, delete, or update files using unified diffs.

type: "apply\_patch"

The type of the tool. Always `apply_patch`.

allowed\_callers: optional array of "direct" or "programmatic"

The tool invocation context(s).

"direct"

"programmatic"

type: "tool\_search\_output"

The type of the item. Always `tool_search_output`.

agent: optional object { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

created\_by: optional string

The identifier of the actor that created the item.

additional\_tools: object { id, role, tools, 2 more }

id: string

The unique ID of the additional tools item.

role: "unknown" or "user" or "assistant" or 5 more

The role that provided the additional tools.

"unknown"

"user"

"assistant"

"system"

"critic"

"discriminator"

"developer"

"tool"

tools: array of [BetaTool](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))

The additional tool definitions made available at this item.

beta\_function\_tool: object { name, parameters, strict, 5 more }

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: string

The name of the function to call.

parameters: map[unknown]

A JSON schema object describing the parameters of the function.

strict: boolean

Whether strict parameter validation is enforced for this function tool.

type: "function"

The type of the function tool. Always `function`.

allowed\_callers: optional array of "direct" or "programmatic"

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: optional boolean

Whether this function is deferred and loaded via tool search.

description: optional string

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema: optional map[unknown]

A JSON schema object describing the JSON value encoded in string outputs for this function.

beta\_file\_search\_tool: object { type, vector\_store\_ids, filters, 2 more }

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: "file\_search"

The type of the file search tool. Always `file_search`.

vector\_store\_ids: array of string

The IDs of the vector stores to search.

filters: optional object { key, type, value }  or object { filters, type }

A filter to apply.

Comparison Filter: object { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" or "ne" or "gt" or 5 more

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

value: string or number or boolean or array of string or number

The value to compare against the attribute key; supports string, number, or boolean types.

union\_member\_0: string

union\_member\_1: number

union\_member\_2: boolean

union\_member\_3: array of string or number

union\_member\_0: string

union\_member\_1: number

Compound Filter: object { filters, type }

Combine multiple filters using `and` or `or`.

filters: array of object { key, type, value }  or unknown

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

Comparison Filter: object { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" or "ne" or "gt" or 5 more

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

value: string or number or boolean or array of string or number

The value to compare against the attribute key; supports string, number, or boolean types.

union\_member\_0: string

union\_member\_1: number

union\_member\_2: boolean

union\_member\_3: array of string or number

union\_member\_0: string

union\_member\_1: number

union\_member\_1: unknown

type: "and" or "or"

Type of operation: `and` or `or`.

"and"

"or"

max\_num\_results: optional number

The maximum number of results to return. This number should be between 1 and 50 inclusive.

ranking\_options: optional object { hybrid\_search, ranker, score\_threshold }

Ranking options for search.

hybrid\_search: optional object { embedding\_weight, text\_weight }

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

embedding\_weight: number

The weight of the embedding in the reciprocal ranking fusion.

text\_weight: number

The weight of the text in the reciprocal ranking fusion.

ranker: optional "auto" or "default-2024-11-15"

The ranker to use for the file search.

"auto"

"default-2024-11-15"

score\_threshold: optional number

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

beta\_computer\_tool: object { type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: "computer"

The type of the computer tool. Always `computer`.

beta\_computer\_use\_preview\_tool: object { display\_height, display\_width, environment, type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: number

The height of the computer display.

display\_width: number

The width of the computer display.

environment: "windows" or "mac" or "linux" or 2 more

The type of computer environment to control.

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

The type of the computer use tool. Always `computer_use_preview`.

beta\_web\_search\_tool: object { type, filters, search\_context\_size, user\_location }

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search" or "web\_search\_2025\_08\_26"

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

"web\_search"

"web\_search\_2025\_08\_26"

filters: optional object { allowed\_domains }

Filters for the search.

allowed\_domains: optional array of string

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size: optional "low" or "medium" or "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location: optional object { city, country, region, 2 more }

The approximate location of the user.

city: optional string

Free text input for the city of the user, e.g. `San Francisco`.

country: optional string

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region: optional string

Free text input for the region of the user, e.g. `California`.

timezone: optional string

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type: optional "approximate"

The type of location approximation. Always `approximate`.

"approximate"

mcp: object { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: string

A label for this MCP server, used to identify it in tool calls.

type: "mcp"

The type of the MCP tool. Always `mcp`.

allowed\_callers: optional array of "direct" or "programmatic"

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools: optional array of string or object { read\_only, tool\_names }

List of allowed tool names or a filter object.

MCP allowed tools: array of string

A string array of allowed tool names

MCP tool filter: object { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only: optional boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: optional array of string

List of allowed tool names.

authorization: optional string

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

connector\_id: optional "connector\_dropbox" or "connector\_gmail" or "connector\_googlecalendar" or 5 more

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

defer\_loading: optional boolean

Whether this MCP tool is deferred and discovered via tool search.

headers: optional map[string]

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval: optional object { always, never }  or "always" or "never"

Specify which of the MCP server’s tools require approval.

MCP tool approval filter: object { always, never }

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always: optional object { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only: optional boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: optional array of string

List of allowed tool names.

never: optional object { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only: optional boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: optional array of string

List of allowed tool names.

MCP tool approval setting: "always" or "never"

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: optional string

Optional description of the MCP server, used to provide more context.

server\_url: optional string

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

tunnel\_id: optional string

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

code\_interpreter: object { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string or object { type, file\_ids, memory\_limit, network\_policy }

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

union\_member\_0: string

The container ID.

CodeInterpreterToolAuto: object { type, file\_ids, memory\_limit, network\_policy }

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: "auto"

Always `auto`.

file\_ids: optional array of string

An optional list of uploaded files to make available to your code.

memory\_limit: optional "1g" or "4g" or "16g" or "64g"

The memory limit for the code interpreter container.

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [BetaContainerNetworkPolicyDisabled](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  or [BetaContainerNetworkPolicyAllowlist](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

beta\_container\_network\_policy\_disabled: object { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

beta\_container\_network\_policy\_allowlist: object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: optional array of [BetaContainerNetworkPolicyDomainSecret](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

name: string

The name of the secret to inject for the domain.

value: string

The secret value to inject for the domain.

type: "code\_interpreter"

The type of the code interpreter tool. Always `code_interpreter`.

allowed\_callers: optional array of "direct" or "programmatic"

The tool invocation context(s).

"direct"

"programmatic"

programmatic\_tool\_calling: object { type }

image\_generation: object { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

The type of the image generation tool. Always `image_generation`.

action: optional "generate" or "edit" or "auto"

Whether to generate a new image or edit an existing image. Default: `auto`.

"generate"

"edit"

"auto"

background: optional "transparent" or "opaque" or "auto"

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

input\_fidelity: optional "high" or "low"

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

"high"

"low"

input\_image\_mask: optional object { file\_id, image\_url }

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

file\_id: optional string

File ID for the mask image.

image\_url: optional string

Base64-encoded mask image.

model: optional string or "gpt-image-1" or "gpt-image-1-mini" or "gpt-image-2" or 3 more

The image generation model to use. Default: `gpt-image-1`.

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: optional "auto" or "low"

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression: optional number

Compression level for the output image. Default: 100.

output\_format: optional "png" or "webp" or "jpeg"

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

"png"

"webp"

"jpeg"

partial\_images: optional number

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

quality: optional "low" or "medium" or "high" or "auto"

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

"low"

"medium"

"high"

"auto"

size: optional string or "1024x1024" or "1024x1536" or "1536x1024" or "auto"

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

local\_shell: object { type }

A tool that allows the model to execute shell commands in a local environment.

beta\_function\_shell\_tool: object { type, allowed\_callers, environment }

A tool that allows the model to execute shell commands.

type: "shell"

The type of the shell tool. Always `shell`.

allowed\_callers: optional array of "direct" or "programmatic"

The tool invocation context(s).

"direct"

"programmatic"

environment: optional [BetaContainerAuto](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  or [BetaLocalEnvironment](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  or [BetaContainerReference](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }

beta\_container\_auto: object { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

Automatically creates a container for this request

file\_ids: optional array of string

An optional list of uploaded files to make available to your code.

memory\_limit: optional "1g" or "4g" or "16g" or "64g"

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [BetaContainerNetworkPolicyDisabled](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  or [BetaContainerNetworkPolicyAllowlist](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

beta\_container\_network\_policy\_disabled: object { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

beta\_container\_network\_policy\_allowlist: object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: optional array of [BetaContainerNetworkPolicyDomainSecret](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

name: string

The name of the secret to inject for the domain.

value: string

The secret value to inject for the domain.

skills: optional array of [BetaSkillReference](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_skill_reference%20%3E%20(schema)) { skill\_id, type, version }  or [BetaInlineSkill](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill%20%3E%20(schema)) { description, name, source, type }

An optional list of skills referenced by id or inline data.

beta\_skill\_reference: object { skill\_id, type, version }

skill\_id: string

The ID of the referenced skill.

type: "skill\_reference"

References a skill created with the /v1/skills endpoint.

version: optional string

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

beta\_inline\_skill: object { description, name, source, type }

description: string

The description of the skill.

name: string

The name of the skill.

source: object { data, media\_type, type }

Inline skill payload

data: string

Base64-encoded skill zip bundle.

media\_type: "application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: "base64"

The type of the inline skill source. Must be `base64`.

type: "inline"

Defines an inline skill for this request.

beta\_local\_environment: object { type, skills }

type: "local"

Use a local computer environment.

skills: optional array of [BetaLocalSkill](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path }

An optional list of skills.

description: string

The description of the skill.

name: string

The name of the skill.

path: string

The path to the directory containing the skill.

beta\_container\_reference: object { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

beta\_custom\_tool: object { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers: optional array of "direct" or "programmatic"

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: optional boolean

Whether this tool should be deferred and discovered via tool search.

description: optional string

Optional description of the custom tool, used to provide more context.

format: optional object { type }  or object { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

text: object { type }

Unconstrained free-form text.

grammar: object { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" or "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

beta\_namespace\_tool: object { description, name, tools, type }

Groups function/custom tools under a shared namespace.

description: string

A description of the namespace shown to the model.

name: string

The namespace name used in tool calls (for example, `crm`).

tools: array of object { name, type, allowed\_callers, 5 more }  or [BetaCustomTool](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_custom_tool%20%3E%20(schema)) { name, type, allowed\_callers, 3 more }

The function/custom tools available inside this namespace.

function: object { name, type, allowed\_callers, 5 more }

name: string

type: "function"

allowed\_callers: optional array of "direct" or "programmatic"

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: optional boolean

Whether this function should be deferred and discovered via tool search.

description: optional string

output\_schema: optional map[unknown]

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters: optional unknown

strict: optional boolean

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

beta\_custom\_tool: object { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers: optional array of "direct" or "programmatic"

The tool invocation context(s).

"direct"

"programmatic"

defer\_loading: optional boolean

Whether this tool should be deferred and discovered via tool search.

description: optional string

Optional description of the custom tool, used to provide more context.

format: optional object { type }  or object { definition, syntax, type }

The input format for the custom tool. Default is unconstrained text.

text: object { type }

Unconstrained free-form text.

grammar: object { definition, syntax, type }

A grammar defined by the user.

definition: string

The grammar definition.

syntax: "lark" or "regex"

The syntax of the grammar definition. One of `lark` or `regex`.

"lark"

"regex"

type: "grammar"

Grammar format. Always `grammar`.

type: "namespace"

The type of the tool. Always `namespace`.

beta\_tool\_search\_tool: object { type, description, execution, parameters }

Hosted or BYOT tool search configuration for deferred tools.

type: "tool\_search"

The type of the tool. Always `tool_search`.

description: optional string

Description shown to the model for a client-executed tool search tool.

execution: optional "server" or "client"

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters: optional unknown

Parameter schema for a client-executed tool search tool.

beta\_web\_search\_preview\_tool: object { type, search\_content\_types, search\_context\_size, user\_location }

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search\_preview" or "web\_search\_preview\_2025\_03\_11"

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: optional array of "text" or "image"

"text"

"image"

search\_context\_size: optional "low" or "medium" or "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location: optional object { type, city, country, 2 more }

The user’s location.

type: "approximate"

The type of location approximation. Always `approximate`.

city: optional string

Free text input for the city of the user, e.g. `San Francisco`.

country: optional string

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region: optional string

Free text input for the region of the user, e.g. `California`.

timezone: optional string

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

beta\_apply\_patch\_tool: object { type, allowed\_callers }

Allows the assistant to create, delete, or update files using unified diffs.

type: "apply\_patch"

The type of the tool. Always `apply_patch`.

allowed\_callers: optional array of "direct" or "programmatic"

The tool invocation context(s).

"direct"

"programmatic"

type: "additional\_tools"

The type of the item. Always `additional_tools`.

agent: optional object { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

beta\_response\_reasoning\_item: object { id, summary, type, 4 more }

A description of the chain of thought used by a reasoning model while generating
a response. Be sure to include these items in your `input` to the Responses API
for subsequent turns of a conversation if you are manually
[managing context](https://platform.openai.com/docs/guides/conversation-state).

id: string

The unique identifier of the reasoning content.

summary: array of object { text, type }

Reasoning summary content.

text: string

A summary of the reasoning output from the model so far.

type: "summary\_text"

The type of the object. Always `summary_text`.

type: "reasoning"

The type of the object. Always `reasoning`.

agent: optional object { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

content: optional array of object { text, type }

Reasoning text content.

text: string

The reasoning text from the model.

type: "reasoning\_text"

The type of the reasoning text. Always `reasoning_text`.

encrypted\_content: optional string

The encrypted content of the reasoning item. This is populated by default
for reasoning items returned by `POST /v1/responses` and WebSocket
`response.create` requests.

status: optional "in\_progress" or "completed" or "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

program: object { id, call\_id, code, 3 more }

id: string

The unique ID of the program item.

call\_id: string

The stable call ID of the program item.

code: string

The JavaScript source executed by programmatic tool calling.

fingerprint: string

Opaque program replay fingerprint that must be round-tripped.

type: "program"

The type of the item. Always `program`.

agent: optional object { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

program\_output: object { id, call\_id, result, 3 more }

id: string

The unique ID of the program output item.

call\_id: string

The call ID of the program item.

result: string

The result produced by the program item.

status: "completed" or "incomplete"

The terminal status of the program output item.

"completed"

"incomplete"

type: "program\_output"

The type of the item. Always `program_output`.

agent: optional object { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

beta\_response\_compaction\_item: object { id, encrypted\_content, type, 2 more }

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

id: string

The unique ID of the compaction item.

encrypted\_content: string

The encrypted content that was produced by compaction.

type: "compaction"

The type of the item. Always `compaction`.

agent: optional object { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

created\_by: optional string

The identifier of the actor that created the item.

image\_generation\_call: object { id, result, status, 2 more }

An image generation request made by the model.

id: string

The unique ID of the image generation call.

result: string

The generated image encoded in base64.

status: "in\_progress" or "completed" or "generating" or "failed"

The status of the image generation call.

"in\_progress"

"completed"

"generating"

"failed"

type: "image\_generation\_call"

The type of the image generation call. Always `image_generation_call`.

agent: optional object { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

beta\_response\_code\_interpreter\_tool\_call: object { id, code, container\_id, 4 more }

A tool call to run code.

id: string

The unique ID of the code interpreter tool call.

code: string

The code to run, or null if not available.

container\_id: string

The ID of the container used to run the code.

outputs: array of object { logs, type }  or object { type, url }

The outputs generated by the code interpreter, such as logs or images.
Can be null if no outputs are available.

logs: object { logs, type }

The logs output from the code interpreter.

logs: string

The logs output from the code interpreter.

type: "logs"

The type of the output. Always `logs`.

image: object { type, url }

The image output from the code interpreter.

type: "image"

The type of the output. Always `image`.

url: string

The URL of the image output from the code interpreter.

status: "in\_progress" or "completed" or "incomplete" or 2 more

The status of the code interpreter tool call. Valid values are `in_progress`, `completed`, `incomplete`, `interpreting`, and `failed`.

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: "code\_interpreter\_call"

The type of the code interpreter tool call. Always `code_interpreter_call`.

agent: optional object { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

local\_shell\_call: object { id, action, call\_id, 3 more }

A tool call to run a command on the local shell.

id: string

The unique ID of the local shell call.

action: object { command, env, type, 3 more }

Execute a shell command on the server.

command: array of string

The command to run.

env: map[string]

Environment variables to set for the command.

type: "exec"

The type of the local shell action. Always `exec`.

timeout\_ms: optional number

Optional timeout in milliseconds for the command.

user: optional string

Optional user to run the command as.

working\_directory: optional string

Optional working directory to run the command in.

call\_id: string

The unique ID of the local shell tool call generated by the model.

status: "in\_progress" or "completed" or "incomplete"

The status of the local shell call.

"in\_progress"

"completed"

"incomplete"

type: "local\_shell\_call"

The type of the local shell call. Always `local_shell_call`.

agent: optional object { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

local\_shell\_call\_output: object { id, output, type, 2 more }

The output of a local shell tool call.

id: string

The unique ID of the local shell tool call generated by the model.

output: string

A JSON string of the output of the local shell tool call.

type: "local\_shell\_call\_output"

The type of the local shell tool call output. Always `local_shell_call_output`.

agent: optional object { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

status: optional "in\_progress" or "completed" or "incomplete"

The status of the item. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

beta\_response\_function\_shell\_tool\_call: object { id, action, call\_id, 6 more }

A tool call that executes one or more shell commands in a managed environment.

id: string

The unique ID of the shell tool call. Populated when this item is returned via API.

action: object { commands, max\_output\_length, timeout\_ms }

The shell commands and limits that describe how to run the tool call.

commands: array of string

max\_output\_length: number

Optional maximum number of characters to return from each command.

timeout\_ms: number

Optional timeout in milliseconds for the commands.

call\_id: string

The unique ID of the shell tool call generated by the model.

environment: [BetaResponseLocalEnvironment](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_local_environment%20%3E%20(schema)) { type }  or [BetaResponseContainerReference](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_container_reference%20%3E%20(schema)) { container\_id, type }

Represents the use of a local environment to perform shell actions.

beta\_response\_local\_environment: object { type }

Represents the use of a local environment to perform shell actions.

type: "local"

The environment type. Always `local`.

beta\_response\_container\_reference: object { container\_id, type }

Represents a container created with /v1/containers.

container\_id: string

type: "container\_reference"

The environment type. Always `container_reference`.

status: "in\_progress" or "completed" or "incomplete"

The status of the shell call. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

type: "shell\_call"

The type of the item. Always `shell_call`.

agent: optional object { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller: optional object { type }  or object { caller\_id, type }

The execution context that produced this tool call.

direct: object { type }

program: object { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

type: "program"

created\_by: optional string

The ID of the entity that created this tool call.

beta\_response\_function\_shell\_tool\_call\_output: object { id, call\_id, max\_output\_length, 6 more }

The output of a shell tool call that was emitted.

id: string

The unique ID of the shell call output. Populated when this item is returned via API.

call\_id: string

The unique ID of the shell tool call generated by the model.

max\_output\_length: number

The maximum length of the shell command output. This is generated by the model and should be passed back with the raw output.

output: array of object { outcome, stderr, stdout, created\_by }

An array of shell call output contents

outcome: object { type }  or object { exit\_code, type }

Represents either an exit outcome (with an exit code) or a timeout outcome for a shell call output chunk.

timeout: object { type }

Indicates that the shell call exceeded its configured time limit.

exit: object { exit\_code, type }

Indicates that the shell commands finished and returned an exit code.

exit\_code: number

Exit code from the shell process.

type: "exit"

The outcome type. Always `exit`.

stderr: string

The standard error output that was captured.

stdout: string

The standard output that was captured.

created\_by: optional string

The identifier of the actor that created the item.

status: "in\_progress" or "completed" or "incomplete"

The status of the shell call output. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

type: "shell\_call\_output"

The type of the shell call output. Always `shell_call_output`.

agent: optional object { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller: optional object { type }  or object { caller\_id, type }

The execution context that produced this tool call.

direct: object { type }

program: object { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

type: "program"

created\_by: optional string

The identifier of the actor that created the item.

beta\_response\_apply\_patch\_tool\_call: object { id, call\_id, operation, 5 more }

A tool call that applies file diffs by creating, deleting, or updating files.

id: string

The unique ID of the apply patch tool call. Populated when this item is returned via API.

call\_id: string

The unique ID of the apply patch tool call generated by the model.

operation: object { diff, path, type }  or object { path, type }  or object { diff, path, type }

One of the create\_file, delete\_file, or update\_file operations applied via apply\_patch.

create\_file: object { diff, path, type }

Instruction describing how to create a file via the apply\_patch tool.

diff: string

Diff to apply.

path: string

Path of the file to create.

type: "create\_file"

Create a new file with the provided diff.

delete\_file: object { path, type }

Instruction describing how to delete a file via the apply\_patch tool.

path: string

Path of the file to delete.

type: "delete\_file"

Delete the specified file.

update\_file: object { diff, path, type }

Instruction describing how to update a file via the apply\_patch tool.

diff: string

Diff to apply.

path: string

Path of the file to update.

type: "update\_file"

Update an existing file with the provided diff.

status: "in\_progress" or "completed"

The status of the apply patch tool call. One of `in_progress` or `completed`.

"in\_progress"

"completed"

type: "apply\_patch\_call"

The type of the item. Always `apply_patch_call`.

agent: optional object { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller: optional object { type }  or object { caller\_id, type }

The execution context that produced this tool call.

direct: object { type }

program: object { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

type: "program"

created\_by: optional string

The ID of the entity that created this tool call.

beta\_response\_apply\_patch\_tool\_call\_output: object { id, call\_id, status, 5 more }

The output emitted by an apply patch tool call.

id: string

The unique ID of the apply patch tool call output. Populated when this item is returned via API.

call\_id: string

The unique ID of the apply patch tool call generated by the model.

status: "completed" or "failed"

The status of the apply patch tool call output. One of `completed` or `failed`.

"completed"

"failed"

type: "apply\_patch\_call\_output"

The type of the item. Always `apply_patch_call_output`.

agent: optional object { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

caller: optional object { type }  or object { caller\_id, type }

The execution context that produced this tool call.

direct: object { type }

program: object { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

type: "program"

created\_by: optional string

The ID of the entity that created this tool call output.

output: optional string

Optional textual output returned by the apply patch tool.

mcp\_list\_tools: object { id, server\_label, tools, 3 more }

A list of tools available on an MCP server.

id: string

The unique ID of the list.

server\_label: string

The label of the MCP server.

tools: array of object { input\_schema, name, annotations, description }

The tools available on the server.

input\_schema: unknown

The JSON schema describing the tool’s input.

name: string

The name of the tool.

annotations: optional unknown

Additional annotations about the tool.

description: optional string

The description of the tool.

type: "mcp\_list\_tools"

The type of the item. Always `mcp_list_tools`.

agent: optional object { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

error: optional string

Error message if the server could not list tools.

mcp\_approval\_request: object { id, arguments, name, 3 more }

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

agent: optional object { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

mcp\_approval\_response: object { id, approval\_request\_id, approve, 3 more }

A response to an MCP approval request.

id: string

The unique ID of the approval response

approval\_request\_id: string

The ID of the approval request being answered.

approve: boolean

Whether the request was approved.

type: "mcp\_approval\_response"

The type of the item. Always `mcp_approval_response`.

agent: optional object { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

reason: optional string

Optional reason for the decision.

mcp\_call: object { id, arguments, name, 7 more }

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

agent: optional object { agent\_name }

The agent that produced this item.

agent\_name: string

The canonical name of the agent that produced this item.

approval\_request\_id: optional string

Unique identifier for the MCP tool call approval request.
Include this value in a subsequent `mcp_approval_response` input to approve or reject the corresponding tool call.

error: optional string

The error from the tool call, if any.

output: optional string

The output from the tool call.

status: optional "in\_progress" or "completed" or "incomplete" or 2 more

The status of the tool call. One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.

"in\_progress"

"completed"

"incomplete"

"calling"

"failed"

beta\_response\_custom\_tool\_call\_item: [BetaResponseCustomToolCall](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_custom_tool_call%20%3E%20(schema)) { call\_id, input, name, 5 more }

A call to a custom tool created by the model.

id: string

The unique ID of the custom tool call item.

status: "in\_progress" or "completed" or "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

created\_by: optional string

The identifier of the actor that created the item.

beta\_response\_custom\_tool\_call\_output\_item: [BetaResponseCustomToolCallOutput](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_custom_tool_call_output%20%3E%20(schema)) { call\_id, output, type, 3 more }

The output of a custom tool call from your code, being sent back to the model.

id: string

The unique ID of the custom tool call output item.

status: "in\_progress" or "completed" or "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

created\_by: optional string

The identifier of the actor that created the item.

first\_id: string

The ID of the first item in the list.

has\_more: boolean

Whether there are more items available.

last\_id: string

The ID of the last item in the list.

object: "list"

The type of object returned, must be `list`.

#### ResponsesInput Tokens

##### [Get input token counts](/api/reference/cli/resources/beta/subresources/responses/subresources/input_tokens/methods/count)

$ openai beta:responses:input-tokens count

POST/responses/input\_tokens
