<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/responses/ -->
<!-- part of: https://developers.openai.com/api/reference/resources/beta/subresources/responses/ -->

<!-- chunk-start -->

title: string

type: "url\_citation"

url: string

ContainerFileCitation object { container\_id, end\_index, file\_id, 3 more }

container\_id: string

end\_index: number

file\_id: string

filename: string

start\_index: number

type: "container\_file\_citation"

FilePath object { file\_id, index, type }

file\_id: string

index: number

type: "file\_path"

logprobs: array of object { token, bytes, logprob, top\_logprobs }

token: string

bytes: array of number

logprob: number

top\_logprobs: array of object { token, bytes, logprob }

token: string

bytes: array of number

logprob: number

text: string

type: "output\_text"

BetaResponseOutputRefusal object { refusal, type }

refusal: string

type: "refusal"

role: "assistant"

status: "in\_progress" or "completed" or "incomplete"

"in\_progress"

"completed"

"incomplete"

type: "message"

agent: optional object { agent\_name }

agent\_name: string

phase: optional "commentary" or "final\_answer"

"commentary"

"final\_answer"

FileSearchCall object { id, queries, status, 3 more }

[file search guide](/docs/guides/tools-file-search) for more information.

id: string

queries: array of string

status: "in\_progress" or "searching" or "completed" or 2 more

"in\_progress"

"searching"

"completed"

"incomplete"

"failed"

type: "file\_search\_call"

agent: optional object { agent\_name }

agent\_name: string

results: optional array of object { attributes, file\_id, filename, 2 more }

attributes: optional map[string or number or boolean]

string

number

boolean

file\_id: optional string

filename: optional string

score: optional number

formatfloat

text: optional string

ComputerCall object { id, call\_id, pending\_safety\_checks, 5 more }

[computer use guide](/docs/guides/tools-computer-use) for more information.

id: string

call\_id: string

pending\_safety\_checks: array of object { id, code, message }

id: string

code: optional string

message: optional string

status: "in\_progress" or "completed" or "incomplete"

"in\_progress"

"completed"

"incomplete"

type: "computer\_call"

action: optional [BetaComputerAction](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action%20%3E%20(schema))

actions: optional [BetaComputerActionList](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action_list%20%3E%20(schema)) { Click, DoubleClick, Drag, 6 more }

agent: optional object { agent\_name }

agent\_name: string

ComputerCallOutput object { id, call\_id, output, 5 more }

id: string

The unique ID of the computer call tool output.

call\_id: string

output: [BetaResponseComputerToolCallOutputScreenshot](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema)) { type, file\_id, image\_url }

status: "completed" or "incomplete" or "failed" or "in\_progress"

"completed"

"incomplete"

"failed"

"in\_progress"

type: "computer\_call\_output"

acknowledged\_safety\_checks: optional array of object { id, code, message }

The safety checks reported by the API that have been acknowledged by the
developer.

id: string

code: optional string

message: optional string

agent: optional object { agent\_name }

agent\_name: string

created\_by: optional string

The identifier of the actor that created the item.

WebSearchCall object { id, action, status, 2 more }

[web search guide](/docs/guides/tools-web-search) for more information.

id: string

action: object { type, queries, query, sources }  or object { type, url }  or object { pattern, type, url }

Search object { type, queries, query, sources }

type: "search"

queries: optional array of string

Deprecatedquery: optional string

sources: optional array of object { type, url }

type: "url"

url: string

OpenPage object { type, url }

type: "open\_page"

url: optional string

FindInPage object { pattern, type, url }

pattern: string

type: "find\_in\_page"

url: string

status: "in\_progress" or "searching" or "completed" or "failed"

"in\_progress"

"searching"

"completed"

"failed"

type: "web\_search\_call"

agent: optional object { agent\_name }

agent\_name: string

FunctionCall object { id, arguments, call\_id, 7 more }

id: string

arguments: string

A JSON string of the arguments to pass to the function.

call\_id: string

name: string

The name of the function to run.

status: "in\_progress" or "completed" or "incomplete"

"in\_progress"

"completed"

"incomplete"

type: "function\_call"

The type of the function tool call. Always `function_call`.

agent: optional object { agent\_name }

agent\_name: string

caller: optional object { type }  or object { caller\_id, type }

Direct object { type }

type: "direct"

Program object { caller\_id, type }

caller\_id: string

type: "program"

created\_by: optional string

The identifier of the actor that created the item.

namespace: optional string

The namespace of the function to run.

FunctionCallOutput object { id, call\_id, output, 5 more }

id: string

The unique ID of the function call tool output.

call\_id: string

output: string or array of [BetaResponseInputText](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [BetaResponseInputImage](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  or [BetaResponseInputFile](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more }

The output from the function call generated by your code.

StringOutput = string

A string of the output of the function call.

OutputContentList = array of [BetaResponseInputText](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [BetaResponseInputImage](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  or [BetaResponseInputFile](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more }

Text, image, or file output of the function call.

BetaResponseInputText object { text, type, prompt\_cache\_breakpoint }

text: string

type: "input\_text"

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

BetaResponseInputImage object { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](/docs/guides/vision).

detail: "low" or "high" or "auto" or "original"

"low"

"high"

"auto"

"original"

type: "input\_image"

file\_id: optional string

image\_url: optional string

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

BetaResponseInputFile object { type, detail, file\_data, 4 more }

type: "input\_file"

detail: optional "auto" or "low" or "high"

"auto"

"low"

"high"

file\_data: optional string

file\_id: optional string

file\_url: optional string

filename: optional string

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

status: "in\_progress" or "completed" or "incomplete"

"in\_progress"

"completed"

"incomplete"

type: "function\_call\_output"

agent: optional object { agent\_name }

agent\_name: string

caller: optional object { type }  or object { caller\_id, type }

Direct object { type }

type: "direct"

The caller type. Always `direct`.

Program object { caller\_id, type }

caller\_id: string

maxLength64

minLength1

type: "program"

created\_by: optional string

The identifier of the actor that created the item.

AgentMessage object { id, author, content, 3 more }

id: string

The unique ID of the agent message.

author: string

content: array of [BetaResponseInputText](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [BetaResponseOutputText](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema)) { annotations, logprobs, text, type }  or object { text, type }  or 7 more

Encrypted content sent between agents.

BetaResponseInputText object { text, type, prompt\_cache\_breakpoint }

text: string

type: "input\_text"

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

BetaResponseOutputText object { annotations, logprobs, text, type }

annotations: array of object { file\_id, filename, index, type }  or object { end\_index, start\_index, title, 2 more }  or object { container\_id, end\_index, file\_id, 3 more }  or object { file\_id, index, type }

FileCitation object { file\_id, filename, index, type }

file\_id: string

filename: string

index: number

type: "file\_citation"

URLCitation object { end\_index, start\_index, title, 2 more }

end\_index: number

start\_index: number

title: string

type: "url\_citation"

url: string

ContainerFileCitation object { container\_id, end\_index, file\_id, 3 more }

container\_id: string

end\_index: number

file\_id: string

filename: string

start\_index: number

type: "container\_file\_citation"

FilePath object { file\_id, index, type }

file\_id: string

index: number

type: "file\_path"

logprobs: array of object { token, bytes, logprob, top\_logprobs }

token: string

bytes: array of number

logprob: number

top\_logprobs: array of object { token, bytes, logprob }

token: string

bytes: array of number

logprob: number

text: string

type: "output\_text"

Text object { text, type }

A text content.

text: string

type: "text"

SummaryText object { text, type }

A summary text from the model.

text: string

type: "summary\_text"

ReasoningText object { text, type }

text: string

type: "reasoning\_text"

BetaResponseOutputRefusal object { refusal, type }

refusal: string

type: "refusal"

BetaResponseInputImage object { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](/docs/guides/vision).

detail: "low" or "high" or "auto" or "original"

"low"

"high"

"auto"

"original"

type: "input\_image"

file\_id: optional string

image\_url: optional string

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

ComputerScreenshot object { detail, file\_id, image\_url, 2 more }

A screenshot of a computer.

detail: "low" or "high" or "auto" or "original"

The detail level of the screenshot image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

file\_id: string

image\_url: string

type: "computer\_screenshot"

Specifies the event type. For a computer screenshot, this property is always set to `computer_screenshot`.

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

BetaResponseInputFile object { type, detail, file\_data, 4 more }

type: "input\_file"

detail: optional "auto" or "low" or "high"

"auto"

"low"

"high"

file\_data: optional string

file\_id: optional string

file\_url: optional string

filename: optional string

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

EncryptedContent object { encrypted\_content, type }

encrypted\_content: string

type: "encrypted\_content"

recipient: string

type: "agent\_message"

The type of the item. Always `agent_message`.

agent: optional object { agent\_name }

agent\_name: string

MultiAgentCall object { id, action, arguments, 3 more }

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

type: "multi\_agent\_call"

The type of the multi-agent call. Always `multi_agent_call`.

agent: optional object { agent\_name }

agent\_name: string

MultiAgentCallOutput object { id, action, call\_id, 3 more }

id: string

The unique ID of the multi-agent call output item.

action: "spawn\_agent" or "interrupt\_agent" or "list\_agents" or 3 more

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

call\_id: string

output: array of [BetaResponseOutputText](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema)) { annotations, logprobs, text, type }

annotations: array of object { file\_id, filename, index, type }  or object { end\_index, start\_index, title, 2 more }  or object { container\_id, end\_index, file\_id, 3 more }  or object { file\_id, index, type }

FileCitation object { file\_id, filename, index, type }

file\_id: string

filename: string

index: number

type: "file\_citation"

URLCitation object { end\_index, start\_index, title, 2 more }

end\_index: number

start\_index: number

title: string

type: "url\_citation"

url: string

ContainerFileCitation object { container\_id, end\_index, file\_id, 3 more }

container\_id: string

end\_index: number

file\_id: string

filename: string

start\_index: number

type: "container\_file\_citation"

FilePath object { file\_id, index, type }

file\_id: string

index: number

type: "file\_path"

logprobs: array of object { token, bytes, logprob, top\_logprobs }

token: string

bytes: array of number

logprob: number

top\_logprobs: array of object { token, bytes, logprob }

token: string

bytes: array of number

logprob: number

text: string

type: "output\_text"

type: "multi\_agent\_call\_output"

The type of the multi-agent result. Always `multi_agent_call_output`.

agent: optional object { agent\_name }

agent\_name: string

ToolSearchCall object { id, arguments, call\_id, 5 more }

id: string

The unique ID of the tool search call item.

arguments: unknown

Arguments used for the tool search call.

call\_id: string

execution: "server" or "client"

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

agent\_name: string

created\_by: optional string

The identifier of the actor that created the item.

ToolSearchOutput object { id, call\_id, execution, 5 more }

id: string

The unique ID of the tool search output item.

call\_id: string

execution: "server" or "client"

"server"

"client"

status: "in\_progress" or "completed" or "incomplete"

The status of the tool search output item that was recorded.

"in\_progress"

"completed"

"incomplete"

tools: array of object { name, parameters, strict, 5 more }  or object { type, vector\_store\_ids, filters, 2 more }  or object { type }  or 13 more

The loaded tool definitions returned by tool search.

Function object { name, parameters, strict, 5 more }

name: string

parameters: map[unknown]

strict: boolean

type: "function"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

output\_schema: optional map[unknown]

FileSearch object { type, vector\_store\_ids, filters, 2 more }

type: "file\_search"

vector\_store\_ids: array of string

filters: optional object { key, type, value }  or object { filters, type }

ComparisonFilter object { key, type, value }

key: string

type: "eq" or "ne" or "gt" or 5 more

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string or number or boolean or array of string or number

string

number

boolean

array of string or number

string

number

CompoundFilter object { filters, type }

filters: array of object { key, type, value }  or unknown

ComparisonFilter object { key, type, value }

key: string

type: "eq" or "ne" or "gt" or 5 more

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string or number or boolean or array of string or number

string

number

boolean

array of string or number

string

number

unknown

type: "and" or "or"

"and"

"or"

max\_num\_results: optional number

ranking\_options: optional object { hybrid\_search, ranker, score\_threshold }

hybrid\_search: optional object { embedding\_weight, text\_weight }

embedding\_weight: number

text\_weight: number

ranker: optional "auto" or "default-2024-11-15"

"auto"

"default-2024-11-15"

score\_threshold: optional number

Computer object { type }

type: "computer"

ComputerUsePreview object { display\_height, display\_width, environment, type }

display\_height: number

display\_width: number

environment: "windows" or "mac" or "linux" or 2 more

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

WebSearch object { type, filters, search\_context\_size, user\_location }

[web search tool](/docs/guides/tools-web-search).

type: "web\_search" or "web\_search\_2025\_08\_26"

"web\_search"

"web\_search\_2025\_08\_26"

filters: optional object { allowed\_domains }

allowed\_domains: optional array of string

search\_context\_size: optional "low" or "medium" or "high"

"low"

"medium"

"high"

user\_location: optional object { city, country, region, 2 more }

city: optional string

country: optional string

region: optional string

timezone: optional string

type: optional "approximate"

Mcp object { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](/docs/guides/tools-remote-mcp).

server\_label: string

type: "mcp"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

allowed\_tools: optional array of string or object { read\_only, tool\_names }

McpAllowedTools = array of string

A string array of allowed tool names

McpToolFilter object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

authorization: optional string

connector\_id: optional "connector\_dropbox" or "connector\_gmail" or "connector\_googlecalendar" or 5 more

about service connectors [here](/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: optional boolean

headers: optional map[string]

require\_approval: optional object { always, never }  or "always" or "never"

McpToolApprovalFilter object { always, never }

always: optional object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

never: optional object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

McpToolApprovalSetting = "always" or "never"

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: optional string

server\_url: optional string

tunnel\_id: optional string

CodeInterpreter object { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string or object { type, file\_ids, memory\_limit, network\_policy }

string

The container ID.

CodeInterpreterToolAuto object { type, file\_ids, memory\_limit, network\_policy }

type: "auto"

file\_ids: optional array of string

memory\_limit: optional "1g" or "4g" or "16g" or "64g"

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [BetaContainerNetworkPolicyDisabled](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  or [BetaContainerNetworkPolicyAllowlist](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

BetaContainerNetworkPolicyDisabled object { type }

type: "disabled"

BetaContainerNetworkPolicyAllowlist object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

type: "allowlist"

domain\_secrets: optional array of [BetaContainerNetworkPolicyDomainSecret](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

domain: string

minLength1

name: string

minLength1

value: string

maxLength10485760

minLength1

type: "code\_interpreter"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

ProgrammaticToolCalling object { type }

type: "programmatic\_tool\_calling"

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration object { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

action: optional "generate" or "edit" or "auto"

"generate"

"edit"

"auto"

background: optional "transparent" or "opaque" or "auto"

Background type for the generated image. One of `transparent`,
`opaque`, or `auto`. Default: `auto`.

"transparent"

"opaque"

"auto"

input\_fidelity: optional "high" or "low"

"high"

"low"

input\_image\_mask: optional object { file\_id, image\_url }

file\_id: optional string

image\_url: optional string

model: optional string or "gpt-image-1" or "gpt-image-1-mini" or "gpt-image-1.5"

string

"gpt-image-1" or "gpt-image-1-mini" or "gpt-image-1.5"

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-1.5"

moderation: optional "auto" or "low"

"auto"

"low"

output\_compression: optional number

minimum0

maximum100

output\_format: optional "png" or "webp" or "jpeg"

"png"

"webp"

"jpeg"

partial\_images: optional number

minimum0

maximum3

quality: optional "low" or "medium" or "high" or "auto"

"low"

"medium"

"high"

"auto"

size: optional string or "1024x1024" or "1024x1536" or "1536x1024" or "auto"

string

"1024x1024" or "1024x1536" or "1536x1024" or "auto"

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

LocalShell object { type }

A tool that allows the model to execute shell commands in a local environment.

type: "local\_shell"

The type of the local shell tool. Always `local_shell`.

Shell object { type, allowed\_callers, environment }

type: "shell"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

environment: optional [BetaContainerAuto](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  or [BetaLocalEnvironment](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  or [BetaContainerReference](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }

BetaContainerAuto object { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

file\_ids: optional array of string

memory\_limit: optional "1g" or "4g" or "16g" or "64g"

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [BetaContainerNetworkPolicyDisabled](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  or [BetaContainerNetworkPolicyAllowlist](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

BetaContainerNetworkPolicyDisabled object { type }

type: "disabled"

BetaContainerNetworkPolicyAllowlist object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

type: "allowlist"

domain\_secrets: optional array of [BetaContainerNetworkPolicyDomainSecret](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

domain: string

minLength1

name: string

minLength1

value: string

maxLength10485760

minLength1

skills: optional array of [BetaSkillReference](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_skill_reference%20%3E%20(schema)) { skill\_id, type, version }  or [BetaInlineSkill](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill%20%3E%20(schema)) { description, name, source, type }

BetaSkillReference object { skill\_id, type, version }

skill\_id: string

maxLength64

minLength1

type: "skill\_reference"

version: optional string

BetaInlineSkill object { description, name, source, type }

description: string

name: string

source: [BetaInlineSkillSource](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

type: "inline"

BetaLocalEnvironment object { type, skills }

type: "local"

skills: optional array of [BetaLocalSkill](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path }

description: string

name: string

path: string

BetaContainerReference object { container\_id, type }

container\_id: string

type: "container\_reference"

Custom object { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](/docs/guides/function-calling#custom-tools)

name: string

type: "custom"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

format: optional object { type }  or object { definition, syntax, type }

Text object { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar object { definition, syntax, type }

definition: string

syntax: "lark" or "regex"

"lark"

"regex"

type: "grammar"

Namespace object { description, name, tools, type }

description: string

minLength1

name: string

minLength1

tools: array of object { name, type, allowed\_callers, 5 more }  or object { name, type, allowed\_callers, 3 more }

Function object { name, type, allowed\_callers, 5 more }

name: string

maxLength128

minLength1

type: "function"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

output\_schema: optional map[unknown]

parameters: optional unknown

strict: optional boolean

Custom object { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](/docs/guides/function-calling#custom-tools)

name: string

type: "custom"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

format: optional object { type }  or object { definition, syntax, type }

Text object { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar object { definition, syntax, type }

definition: string

syntax: "lark" or "regex"

"lark"

"regex"

type: "grammar"

type: "namespace"

ToolSearch object { type, description, execution, parameters }

type: "tool\_search"

description: optional string

execution: optional "server" or "client"

"server"

"client"

parameters: optional unknown

WebSearchPreview object { type, search\_content\_types, search\_context\_size, user\_location }

type: "web\_search\_preview" or "web\_search\_preview\_2025\_03\_11"

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: optional array of "text" or "image"

"text"

"image"

search\_context\_size: optional "low" or "medium" or "high"

"low"

"medium"

"high"

user\_location: optional object { type, city, country, 2 more }

type: "approximate"

city: optional string

country: optional string

region: optional string

timezone: optional string

ApplyPatch object { type, allowed\_callers }

type: "apply\_patch"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

type: "tool\_search\_output"

The type of the item. Always `tool_search_output`.

agent: optional object { agent\_name }

agent\_name: string

created\_by: optional string

The identifier of the actor that created the item.

AdditionalTools object { id, role, tools, 2 more }

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

tools: array of object { name, parameters, strict, 5 more }  or object { type, vector\_store\_ids, filters, 2 more }  or object { type }  or 13 more

The additional tool definitions made available at this item.

Function object { name, parameters, strict, 5 more }

name: string

parameters: map[unknown]

strict: boolean

type: "function"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

output\_schema: optional map[unknown]

FileSearch object { type, vector\_store\_ids, filters, 2 more }

type: "file\_search"

vector\_store\_ids: array of string

filters: optional object { key, type, value }  or object { filters, type }

ComparisonFilter object { key, type, value }

key: string

type: "eq" or "ne" or "gt" or 5 more

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string or number or boolean or array of string or number

string

number

boolean

array of string or number

string

number

CompoundFilter object { filters, type }

filters: array of object { key, type, value }  or unknown

ComparisonFilter object { key, type, value }

key: string

type: "eq" or "ne" or "gt" or 5 more

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string or number or boolean or array of string or number

string

number

boolean

array of string or number

string

number

unknown

type: "and" or "or"

"and"

"or"

max\_num\_results: optional number

ranking\_options: optional object { hybrid\_search, ranker, score\_threshold }

hybrid\_search: optional object { embedding\_weight, text\_weight }

embedding\_weight: number

text\_weight: number

ranker: optional "auto" or "default-2024-11-15"

"auto"

"default-2024-11-15"

score\_threshold: optional number

Computer object { type }

type: "computer"

ComputerUsePreview object { display\_height, display\_width, environment, type }

display\_height: number

display\_width: number

environment: "windows" or "mac" or "linux" or 2 more

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

WebSearch object { type, filters, search\_context\_size, user\_location }

[web search tool](/docs/guides/tools-web-search).

type: "web\_search" or "web\_search\_2025\_08\_26"

"web\_search"

"web\_search\_2025\_08\_26"

filters: optional object { allowed\_domains }

allowed\_domains: optional array of string

search\_context\_size: optional "low" or "medium" or "high"

"low"

"medium"

"high"

user\_location: optional object { city, country, region, 2 more }

city: optional string

country: optional string

region: optional string

timezone: optional string

type: optional "approximate"

Mcp object { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](/docs/guides/tools-remote-mcp).

server\_label: string

type: "mcp"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

allowed\_tools: optional array of string or object { read\_only, tool\_names }

McpAllowedTools = array of string

A string array of allowed tool names

McpToolFilter object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

authorization: optional string

connector\_id: optional "connector\_dropbox" or "connector\_gmail" or "connector\_googlecalendar" or 5 more

about service connectors [here](/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: optional boolean

headers: optional map[string]

require\_approval: optional object { always, never }  or "always" or "never"

McpToolApprovalFilter object { always, never }

always: optional object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

never: optional object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

McpToolApprovalSetting = "always" or "never"

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: optional string

server\_url: optional string

tunnel\_id: optional string

CodeInterpreter object { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string or object { type, file\_ids, memory\_limit, network\_policy }

string

The container ID.

CodeInterpreterToolAuto object { type, file\_ids, memory\_limit, network\_policy }

type: "auto"

file\_ids: optional array of string

memory\_limit: optional "1g" or "4g" or "16g" or "64g"

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [BetaContainerNetworkPolicyDisabled](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  or [BetaContainerNetworkPolicyAllowlist](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

BetaContainerNetworkPolicyDisabled object { type }

type: "disabled"

BetaContainerNetworkPolicyAllowlist object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

type: "allowlist"

domain\_secrets: optional array of [BetaContainerNetworkPolicyDomainSecret](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

domain: string

minLength1

name: string

minLength1

value: string

maxLength10485760

minLength1

type: "code\_interpreter"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

ProgrammaticToolCalling object { type }

type: "programmatic\_tool\_calling"

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration object { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

action: optional "generate" or "edit" or "auto"

"generate"

"edit"

"auto"

background: optional "transparent" or "opaque" or "auto"

Background type for the generated image. One of `transparent`,
`opaque`, or `auto`. Default: `auto`.

"transparent"

"opaque"

"auto"

input\_fidelity: optional "high" or "low"

"high"

"low"

input\_image\_mask: optional object { file\_id, image\_url }

file\_id: optional string

image\_url: optional string

model: optional string or "gpt-image-1" or "gpt-image-1-mini" or "gpt-image-1.5"

string

"gpt-image-1" or "gpt-image-1-mini" or "gpt-image-1.5"

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-1.5"

moderation: optional "auto" or "low"

"auto"

"low"

output\_compression: optional number

minimum0

maximum100

output\_format: optional "png" or "webp" or "jpeg"

"png"

"webp"

"jpeg"

partial\_images: optional number

minimum0

maximum3

quality: optional "low" or "medium" or "high" or "auto"

"low"

"medium"

"high"

"auto"

size: optional string or "1024x1024" or "1024x1536" or "1536x1024" or "auto"

string

"1024x1024" or "1024x1536" or "1536x1024" or "auto"

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

LocalShell object { type }

A tool that allows the model to execute shell commands in a local environment.

type: "local\_shell"

The type of the local shell tool. Always `local_shell`.

Shell object { type, allowed\_callers, environment }

type: "shell"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

environment: optional [BetaContainerAuto](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  or [BetaLocalEnvironment](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  or [BetaContainerReference](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }

BetaContainerAuto object { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

file\_ids: optional array of string

memory\_limit: optional "1g" or "4g" or "16g" or "64g"

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [BetaContainerNetworkPolicyDisabled](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  or [BetaContainerNetworkPolicyAllowlist](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

BetaContainerNetworkPolicyDisabled object { type }

type: "disabled"

BetaContainerNetworkPolicyAllowlist object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

type: "allowlist"

domain\_secrets: optional array of [BetaContainerNetworkPolicyDomainSecret](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

domain: string

minLength1

name: string

minLength1

value: string

maxLength10485760

minLength1

skills: optional array of [BetaSkillReference](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_skill_reference%20%3E%20(schema)) { skill\_id, type, version }  or [BetaInlineSkill](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill%20%3E%20(schema)) { description, name, source, type }

BetaSkillReference object { skill\_id, type, version }

skill\_id: string

maxLength64

minLength1

type: "skill\_reference"

version: optional string

BetaInlineSkill object { description, name, source, type }

description: string

name: string

source: [BetaInlineSkillSource](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

type: "inline"

BetaLocalEnvironment object { type, skills }

type: "local"

skills: optional array of [BetaLocalSkill](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path }

description: string

name: string

path: string

BetaContainerReference object { container\_id, type }

container\_id: string

type: "container\_reference"

Custom object { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](/docs/guides/function-calling#custom-tools)

name: string

type: "custom"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

format: optional object { type }  or object { definition, syntax, type }

Text object { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar object { definition, syntax, type }

definition: string

syntax: "lark" or "regex"

"lark"

"regex"

type: "grammar"

Namespace object { description, name, tools, type }

description: string

minLength1

name: string

minLength1

tools: array of object { name, type, allowed\_callers, 5 more }  or object { name, type, allowed\_callers, 3 more }

Function object { name, type, allowed\_callers, 5 more }

name: string

maxLength128

minLength1

type: "function"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

output\_schema: optional map[unknown]

parameters: optional unknown

strict: optional boolean

Custom object { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](/docs/guides/function-calling#custom-tools)

name: string

type: "custom"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

format: optional object { type }  or object { definition, syntax, type }

Text object { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar object { definition, syntax, type }

definition: string

syntax: "lark" or "regex"

"lark"

"regex"

type: "grammar"

type: "namespace"

ToolSearch object { type, description, execution, parameters }

type: "tool\_search"

description: optional string

execution: optional "server" or "client"

"server"

"client"

parameters: optional unknown

WebSearchPreview object { type, search\_content\_types, search\_context\_size, user\_location }

type: "web\_search\_preview" or "web\_search\_preview\_2025\_03\_11"

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: optional array of "text" or "image"

"text"

"image"

search\_context\_size: optional "low" or "medium" or "high"

"low"

"medium"

"high"

user\_location: optional object { type, city, country, 2 more }

type: "approximate"

city: optional string

country: optional string

region: optional string

timezone: optional string

ApplyPatch object { type, allowed\_callers }

type: "apply\_patch"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

type: "additional\_tools"

The type of the item. Always `additional_tools`.

agent: optional object { agent\_name }

agent\_name: string

Reasoning object { id, summary, type, 4 more }

[managing context](/docs/guides/conversation-state).

id: string

summary: array of object { text, type }

text: string

type: "summary\_text"

type: "reasoning"

agent: optional object { agent\_name }

agent\_name: string

content: optional array of object { text, type }

text: string

type: "reasoning\_text"

encrypted\_content: optional string

status: optional "in\_progress" or "completed" or "incomplete"

"in\_progress"

"completed"

"incomplete"

Program object { id, call\_id, code, 3 more }

id: string

The unique ID of the program item.

call\_id: string

code: string

fingerprint: string

type: "program"

The type of the item. Always `program`.

agent: optional object { agent\_name }

agent\_name: string

ProgramOutput object { id, call\_id, result, 3 more }

id: string

The unique ID of the program output item.

call\_id: string

result: string

status: "completed" or "incomplete"

The terminal status of the program output item.

"completed"

"incomplete"

type: "program\_output"

The type of the item. Always `program_output`.

agent: optional object { agent\_name }

agent\_name: string

Compaction object { id, encrypted\_content, type, 2 more }

A compaction item generated by the [`v1/responses/compact` API](/docs/api-reference/responses/compact).

id: string

The unique ID of the compaction item.

encrypted\_content: string

The encrypted content that was produced by compaction.

type: "compaction"

agent: optional object { agent\_name }

agent\_name: string

created\_by: optional string

The identifier of the actor that created the item.

ImageGenerationCall object { id, result, status, 2 more }

An image generation request made by the model.

id: string

result: string

status: "in\_progress" or "completed" or "generating" or "failed"

"in\_progress"

"completed"

"generating"

"failed"

type: "image\_generation\_call"

agent: optional object { agent\_name }

agent\_name: string

CodeInterpreterCall object { id, code, container\_id, 4 more }

id: string

code: string

container\_id: string

outputs: array of object { logs, type }  or object { type, url }

Logs object { logs, type }

logs: string

type: "logs"

Image object { type, url }

type: "image"

url: string

status: "in\_progress" or "completed" or "incomplete" or 2 more

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: "code\_interpreter\_call"

agent: optional object { agent\_name }

agent\_name: string

LocalShellCall object { id, action, call\_id, 3 more }

A tool call to run a command on the local shell.

id: string

action: object { command, env, type, 3 more }

command: array of string

env: map[string]

type: "exec"

timeout\_ms: optional number

user: optional string

working\_directory: optional string

call\_id: string

status: "in\_progress" or "completed" or "incomplete"

"in\_progress"

"completed"

"incomplete"

type: "local\_shell\_call"

agent: optional object { agent\_name }

agent\_name: string

LocalShellCallOutput object { id, output, type, 2 more }

The output of a local shell tool call.

id: string

output: string

type: "local\_shell\_call\_output"

agent: optional object { agent\_name }

agent\_name: string

status: optional "in\_progress" or "completed" or "incomplete"

"in\_progress"

"completed"

"incomplete"

ShellCall object { id, action, call\_id, 6 more }

A tool call that executes one or more shell commands in a managed environment.

id: string

action: object { commands, max\_output\_length, timeout\_ms }

commands: array of string

max\_output\_length: number

Optional maximum number of characters to return from each command.

timeout\_ms: number

Optional timeout in milliseconds for the commands.

call\_id: string

environment: [BetaResponseLocalEnvironment](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_local_environment%20%3E%20(schema)) { type }  or [BetaResponseContainerReference](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_container_reference%20%3E%20(schema)) { container\_id, type }

Represents the use of a local environment to perform shell actions.

BetaResponseLocalEnvironment object { type }

Represents the use of a local environment to perform shell actions.

type: "local"

The environment type. Always `local`.

BetaResponseContainerReference object { container\_id, type }

Represents a container created with /v1/containers.

container\_id: string

type: "container\_reference"

The environment type. Always `container_reference`.

status: "in\_progress" or "completed" or "incomplete"

"in\_progress"

"completed"

"incomplete"

type: "shell\_call"

agent: optional object { agent\_name }

agent\_name: string

caller: optional object { type }  or object { caller\_id, type }

Direct object { type }

type: "direct"

Program object { caller\_id, type }

caller\_id: string

type: "program"

created\_by: optional string

The ID of the entity that created this tool call.

ShellCallOutput object { id, call\_id, max\_output\_length, 6 more }

The output of a shell tool call that was emitted.

id: string

The unique ID of the shell call output. Populated when this item is returned via API.

call\_id: string

max\_output\_length: number

The maximum length of the shell command output. This is generated by the model and should be passed back with the raw output.

output: array of object { outcome, stderr, stdout, created\_by }

An array of shell call output contents

outcome: object { type }  or object { exit\_code, type }

Represents either an exit outcome (with an exit code) or a timeout outcome for a shell call output chunk.

Timeout object { type }

Indicates that the shell call exceeded its configured time limit.

type: "timeout"

The outcome type. Always `timeout`.

Exit object { exit\_code, type }

exit\_code: number

Exit code from the shell process.

type: "exit"

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

agent\_name: string

caller: optional object { type }  or object { caller\_id, type }

Direct object { type }

type: "direct"

Program object { caller\_id, type }

caller\_id: string

type: "program"

created\_by: optional string

The identifier of the actor that created the item.

ApplyPatchCall object { id, call\_id, operation, 5 more }

A tool call that applies file diffs by creating, deleting, or updating files.

id: string

call\_id: string

operation: object { diff, path, type }  or object { path, type }  or object { diff, path, type }

One of the create\_file, delete\_file, or update\_file operations applied via apply\_patch.

CreateFile object { diff, path, type }

Instruction describing how to create a file via the apply\_patch tool.

diff: string

Diff to apply.

path: string

Path of the file to create.

type: "create\_file"

Create a new file with the provided diff.

DeleteFile object { path, type }

Instruction describing how to delete a file via the apply\_patch tool.

path: string

Path of the file to delete.

type: "delete\_file"

Delete the specified file.

UpdateFile object { diff, path, type }

Instruction describing how to update a file via the apply\_patch tool.

diff: string

Diff to apply.

path: string

Path of the file to update.

type: "update\_file"

Update an existing file with the provided diff.

status: "in\_progress" or "completed"

"in\_progress"

"completed"

type: "apply\_patch\_call"

agent: optional object { agent\_name }

agent\_name: string

caller: optional object { type }  or object { caller\_id, type }

Direct object { type }

type: "direct"

Program object { caller\_id, type }

caller\_id: string

type: "program"

created\_by: optional string

The ID of the entity that created this tool call.

ApplyPatchCallOutput object { id, call\_id, status, 5 more }

The output emitted by an apply patch tool call.

id: string

call\_id: string

status: "completed" or "failed"

"completed"

"failed"

type: "apply\_patch\_call\_output"

agent: optional object { agent\_name }

agent\_name: string

caller: optional object { type }  or object { caller\_id, type }

Direct object { type }

type: "direct"

Program object { caller\_id, type }

caller\_id: string

type: "program"

created\_by: optional string

The ID of the entity that created this tool call output.

output: optional string

Optional textual output returned by the apply patch tool.

McpListTools object { id, server\_label, tools, 3 more }

A list of tools available on an MCP server.

id: string

server\_label: string

tools: array of object { input\_schema, name, annotations, description }

input\_schema: unknown

name: string

annotations: optional unknown

description: optional string

type: "mcp\_list\_tools"

agent: optional object { agent\_name }

agent\_name: string

error: optional string

McpApprovalRequest object { id, arguments, name, 3 more }

A request for human approval of a tool invocation.

id: string

arguments: string

name: string

server\_label: string

type: "mcp\_approval\_request"

agent: optional object { agent\_name }

agent\_name: string

McpApprovalResponse object { id, approval\_request\_id, approve, 3 more }

A response to an MCP approval request.

id: string

approval\_request\_id: string

approve: boolean

type: "mcp\_approval\_response"

agent: optional object { agent\_name }

agent\_name: string

reason: optional string

McpCall object { id, arguments, name, 7 more }

An invocation of a tool on an MCP server.

id: string

arguments: string

name: string

server\_label: string

type: "mcp\_call"

agent: optional object { agent\_name }

agent\_name: string

approval\_request\_id: optional string

error: optional string

output: optional string

status: optional "in\_progress" or "completed" or "incomplete" or 2 more

"in\_progress"

"completed"

"incomplete"

"calling"

"failed"

CustomToolCall object { id, call\_id, input, 7 more }

id: string

The unique ID of the custom tool call item.

call\_id: string

An identifier used to map this custom tool call to a tool call output.

input: string

The input for the custom tool call generated by the model.

name: string

The name of the custom tool being called.

status: "in\_progress" or "completed" or "incomplete"

"in\_progress"

"completed"

"incomplete"

type: "custom\_tool\_call"

The type of the custom tool call. Always `custom_tool_call`.

agent: optional object { agent\_name }

agent\_name: string

caller: optional object { type }  or object { caller\_id, type }

Direct object { type }

type: "direct"

Program object { caller\_id, type }

caller\_id: string

type: "program"

created\_by: optional string

The identifier of the actor that created the item.

namespace: optional string

The namespace of the custom tool being called.

CustomToolCallOutput object { id, call\_id, output, 5 more }

id: string

The unique ID of the custom tool call output item.

call\_id: string

The call ID, used to map this custom tool call output to a custom tool call.

output: string or array of [BetaResponseInputText](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [BetaResponseInputImage](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  or [BetaResponseInputFile](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more }

The output from the custom tool call generated by your code.

StringOutput = string

A string of the output of the custom tool call.

OutputContentList = array of [BetaResponseInputText](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [BetaResponseInputImage](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  or [BetaResponseInputFile](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more }

Text, image, or file output of the custom tool call.

BetaResponseInputText object { text, type, prompt\_cache\_breakpoint }

text: string

type: "input\_text"

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

BetaResponseInputImage object { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](/docs/guides/vision).

detail: "low" or "high" or "auto" or "original"

"low"

"high"

"auto"

"original"

type: "input\_image"

file\_id: optional string

image\_url: optional string

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

BetaResponseInputFile object { type, detail, file\_data, 4 more }

type: "input\_file"

detail: optional "auto" or "low" or "high"

"auto"

"low"

"high"

file\_data: optional string

file\_id: optional string

file\_url: optional string

filename: optional string

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

status: "in\_progress" or "completed" or "incomplete"

"in\_progress"

"completed"

"incomplete"

type: "custom\_tool\_call\_output"

The type of the custom tool call output. Always `custom_tool_call_output`.

agent: optional object { agent\_name }

agent\_name: string

caller: optional object { type }  or object { caller\_id, type }

Direct object { type }

type: "direct"

The caller type. Always `direct`.

Program object { caller\_id, type }

caller\_id: string

maxLength64

minLength1

type: "program"

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

##### [Get input token counts](/api/reference/resources/beta/subresources/responses/subresources/input_tokens/methods/count)

POST/responses/input\_tokens

##### ModelsExpand Collapse

InputTokenCountResponse object { input\_tokens, object }

input\_tokens: number

object: "response.input\_tokens"
