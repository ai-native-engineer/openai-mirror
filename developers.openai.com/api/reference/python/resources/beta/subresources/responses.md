<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/responses/ -->

[API Reference](/api/reference/python)

[Beta](/api/reference/python/resources/beta)

# Responses

##### [Connect](/api/reference/python/resources/beta/subresources/responses/methods/connect)

beta.responses.connect()

Function

##### [Create a model response](/api/reference/python/resources/beta/subresources/responses/methods/create)

beta.responses.create(ResponseCreateParams\*\*kwargs)  -> [BetaResponse](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

POST/responses

##### [Get a model response](/api/reference/python/resources/beta/subresources/responses/methods/retrieve)

beta.responses.retrieve(strresponse\_id, ResponseRetrieveParams\*\*kwargs)  -> [BetaResponse](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

GET/responses/{response\_id}

##### [Delete a model response](/api/reference/python/resources/beta/subresources/responses/methods/delete)

beta.responses.delete(strresponse\_id, ResponseDeleteParams\*\*kwargs)

DELETE/responses/{response\_id}

##### [Cancel a response](/api/reference/python/resources/beta/subresources/responses/methods/cancel)

beta.responses.cancel(strresponse\_id, ResponseCancelParams\*\*kwargs)  -> [BetaResponse](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

POST/responses/{response\_id}/cancel

##### [Compact a response](/api/reference/python/resources/beta/subresources/responses/methods/compact)

beta.responses.compact(ResponseCompactParams\*\*kwargs)  -> [BetaCompactedResponse](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_compacted_response%20%3E%20(schema))

POST/responses/compact

##### ModelsExpand Collapse

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class BetaCompactedResponse: …

id: str

The unique identifier for the compacted response.

created\_at: int

Unix timestamp (in seconds) when the compacted conversation was created.

formatunixtime

object: Literal["response.compaction"]

The object type. Always `response.compaction`.

output: List[[BetaResponseOutputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema))]

The compacted list of output items. This is a list of all user messages, followed by a single compaction item.

class BetaResponseOutputMessage: …

id: str

content: List[Content]

class BetaResponseOutputText: …

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

logprobs: Optional[List[Logprob]]

token: str

bytes: List[int]

logprob: float

top\_logprobs: List[LogprobTopLogprob]

token: str

bytes: List[int]

logprob: float

class BetaResponseOutputRefusal: …

refusal: str

type: Literal["refusal"]

role: Literal["assistant"]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["message"]

agent: Optional[Agent]

agent\_name: str

phase: Optional[Literal["commentary", "final\_answer"]]

"commentary"

"final\_answer"

class BetaResponseFileSearchToolCall: …

[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

id: str

queries: List[str]

status: Literal["in\_progress", "searching", "completed", 2 more]

"in\_progress"

"searching"

"completed"

"incomplete"

"failed"

type: Literal["file\_search\_call"]

agent: Optional[Agent]

agent\_name: str

results: Optional[List[Result]]

attributes: Optional[Dict[str, Union[str, float, bool]]]

str

float

bool

file\_id: Optional[str]

filename: Optional[str]

score: Optional[float]

formatfloat

text: Optional[str]

class BetaResponseFunctionToolCall: …

[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

arguments: str

A JSON string of the arguments to pass to the function.

call\_id: str

name: str

The name of the function to run.

type: Literal["function\_call"]

The type of the function tool call. Always `function_call`.

id: Optional[str]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

namespace: Optional[str]

The namespace of the function to run.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class BetaResponseFunctionToolCallOutputItem: …

id: str

The unique ID of the function call tool output.

call\_id: str

output: Union[str, List[OutputOutputContentList]]

The output from the function call generated by your code.

str

A string of the output of the function call.

List[OutputOutputContentList]

Text, image, or file output of the function call.

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["function\_call\_output"]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class CallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

created\_by: Optional[str]

The identifier of the actor that created the item.

class AgentMessage: …

id: str

The unique ID of the agent message.

author: str

content: List[AgentMessageContent]

Encrypted content sent between agents.

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseOutputText: …

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

logprobs: Optional[List[Logprob]]

token: str

bytes: List[int]

logprob: float

top\_logprobs: List[LogprobTopLogprob]

token: str

bytes: List[int]

logprob: float

class AgentMessageContentText: …

A text content.

text: str

type: Literal["text"]

class AgentMessageContentSummaryText: …

A summary text from the model.

text: str

type: Literal["summary\_text"]

class AgentMessageContentReasoningText: …

text: str

type: Literal["reasoning\_text"]

class BetaResponseOutputRefusal: …

refusal: str

type: Literal["refusal"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class AgentMessageContentComputerScreenshot: …

A screenshot of a computer.

detail: Literal["low", "high", "auto", "original"]

The detail level of the screenshot image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

image\_url: Optional[str]

type: Literal["computer\_screenshot"]

Specifies the event type. For a computer screenshot, this property is always set to `computer_screenshot`.

prompt\_cache\_breakpoint: Optional[AgentMessageContentComputerScreenshotPromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class AgentMessageContentEncryptedContent: …

encrypted\_content: str

type: Literal["encrypted\_content"]

recipient: str

type: Literal["agent\_message"]

The type of the item. Always `agent_message`.

agent: Optional[AgentMessageAgent]

agent\_name: str

class MultiAgentCall: …

id: str

The unique ID of the multi-agent call item.

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

The multi-agent action to execute.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

arguments: str

The JSON string of arguments generated for the action.

call\_id: str

type: Literal["multi\_agent\_call"]

The type of the multi-agent call. Always `multi_agent_call`.

agent: Optional[MultiAgentCallAgent]

agent\_name: str

class MultiAgentCallOutput: …

id: str

The unique ID of the multi-agent call output item.

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

call\_id: str

output: List[[BetaResponseOutputText](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema))]

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

logprobs: Optional[List[Logprob]]

token: str

bytes: List[int]

logprob: float

top\_logprobs: List[LogprobTopLogprob]

token: str

bytes: List[int]

logprob: float

type: Literal["multi\_agent\_call\_output"]

The type of the multi-agent result. Always `multi_agent_call_output`.

agent: Optional[MultiAgentCallOutputAgent]

agent\_name: str

class BetaResponseFunctionWebSearch: …

[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

id: str

action: Action

class ActionSearch: …

type: Literal["search"]

queries: Optional[List[str]]

Deprecatedquery: Optional[str]

sources: Optional[List[ActionSearchSource]]

type: Literal["url"]

url: str

class ActionOpenPage: …

type: Literal["open\_page"]

url: Optional[str]

class ActionFindInPage: …

pattern: str

type: Literal["find\_in\_page"]

url: str

status: Literal["in\_progress", "searching", "completed", "failed"]

"in\_progress"

"searching"

"completed"

"failed"

type: Literal["web\_search\_call"]

agent: Optional[Agent]

agent\_name: str

class BetaResponseComputerToolCall: …

[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

id: str

call\_id: str

pending\_safety\_checks: List[PendingSafetyCheck]

id: str

code: Optional[str]

message: Optional[str]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["computer\_call"]

action: Optional[BetaComputerAction]

actions: Optional[BetaComputerActionList]

agent: Optional[Agent]

agent\_name: str

class BetaResponseComputerToolCallOutputItem: …

id: str

The unique ID of the computer call tool output.

call\_id: str

output: [BetaResponseComputerToolCallOutputScreenshot](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema))

status: Literal["completed", "incomplete", "failed", "in\_progress"]

"completed"

"incomplete"

"failed"

"in\_progress"

type: Literal["computer\_call\_output"]

acknowledged\_safety\_checks: Optional[List[AcknowledgedSafetyCheck]]

The safety checks reported by the API that have been acknowledged by the
developer.

id: str

code: Optional[str]

message: Optional[str]

agent: Optional[Agent]

agent\_name: str

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseReasoningItem: …

[managing context](https://platform.openai.com/docs/guides/conversation-state).

id: str

summary: List[Summary]

text: str

type: Literal["summary\_text"]

type: Literal["reasoning"]

agent: Optional[Agent]

agent\_name: str

content: Optional[List[Content]]

text: str

type: Literal["reasoning\_text"]

encrypted\_content: Optional[str]

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class Program: …

id: str

The unique ID of the program item.

call\_id: str

code: str

fingerprint: str

type: Literal["program"]

The type of the item. Always `program`.

agent: Optional[ProgramAgent]

agent\_name: str

class ProgramOutput: …

id: str

The unique ID of the program output item.

call\_id: str

result: str

status: Literal["completed", "incomplete"]

The terminal status of the program output item.

"completed"

"incomplete"

type: Literal["program\_output"]

The type of the item. Always `program_output`.

agent: Optional[ProgramOutputAgent]

agent\_name: str

class BetaResponseToolSearchCall: …

id: str

The unique ID of the tool search call item.

arguments: object

Arguments used for the tool search call.

call\_id: Optional[str]

execution: Literal["server", "client"]

"server"

"client"

status: Literal["in\_progress", "completed", "incomplete"]

The status of the tool search call item that was recorded.

"in\_progress"

"completed"

"incomplete"

type: Literal["tool\_search\_call"]

The type of the item. Always `tool_search_call`.

agent: Optional[Agent]

agent\_name: str

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseToolSearchOutputItem: …

id: str

The unique ID of the tool search output item.

call\_id: Optional[str]

execution: Literal["server", "client"]

"server"

"client"

status: Literal["in\_progress", "completed", "incomplete"]

The status of the tool search output item that was recorded.

"in\_progress"

"completed"

"incomplete"

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

The loaded tool definitions returned by tool search.

class BetaFunctionTool: …

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

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

input\_fidelity: Optional[Literal["high", "low"]]

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

type: Literal["tool\_search\_output"]

The type of the item. Always `tool_search_output`.

agent: Optional[Agent]

agent\_name: str

created\_by: Optional[str]

The identifier of the actor that created the item.

class AdditionalTools: …

id: str

The unique ID of the additional tools item.

role: Literal["unknown", "user", "assistant", 5 more]

The role that provided the additional tools.

"unknown"

"user"

"assistant"

"system"

"critic"

"discriminator"

"developer"

"tool"

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

The additional tool definitions made available at this item.

class BetaFunctionTool: …

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

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

input\_fidelity: Optional[Literal["high", "low"]]

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

type: Literal["additional\_tools"]

The type of the item. Always `additional_tools`.

agent: Optional[AdditionalToolsAgent]

agent\_name: str

class BetaResponseCompactionItem: …

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

id: str

The unique ID of the compaction item.

encrypted\_content: str

The encrypted content that was produced by compaction.

type: Literal["compaction"]

agent: Optional[Agent]

agent\_name: str

created\_by: Optional[str]

The identifier of the actor that created the item.

class ImageGenerationCall: …

An image generation request made by the model.

id: str

result: Optional[str]

status: Literal["in\_progress", "completed", "generating", "failed"]

"in\_progress"

"completed"

"generating"

"failed"

type: Literal["image\_generation\_call"]

agent: Optional[ImageGenerationCallAgent]

agent\_name: str

class BetaResponseCodeInterpreterToolCall: …

id: str

code: Optional[str]

container\_id: str

outputs: Optional[List[Output]]

class OutputLogs: …

logs: str

type: Literal["logs"]

class OutputImage: …

type: Literal["image"]

url: str

status: Literal["in\_progress", "completed", "incomplete", 2 more]

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: Literal["code\_interpreter\_call"]

agent: Optional[Agent]

agent\_name: str

class LocalShellCall: …

A tool call to run a command on the local shell.

id: str

action: LocalShellCallAction

command: List[str]

env: Dict[str, str]

type: Literal["exec"]

timeout\_ms: Optional[int]

user: Optional[str]

working\_directory: Optional[str]

call\_id: str

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["local\_shell\_call"]

agent: Optional[LocalShellCallAgent]

agent\_name: str

class LocalShellCallOutput: …

The output of a local shell tool call.

id: str

output: str

type: Literal["local\_shell\_call\_output"]

agent: Optional[LocalShellCallOutputAgent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class BetaResponseFunctionShellToolCall: …

A tool call that executes one or more shell commands in a managed environment.

id: str

action: Action

commands: List[str]

max\_output\_length: Optional[int]

Optional maximum number of characters to return from each command.

timeout\_ms: Optional[int]

Optional timeout in milliseconds for the commands.

call\_id: str

environment: Optional[Environment]

Represents the use of a local environment to perform shell actions.

class BetaResponseLocalEnvironment: …

Represents the use of a local environment to perform shell actions.

type: Literal["local"]

The environment type. Always `local`.

class BetaResponseContainerReference: …

Represents a container created with /v1/containers.

container\_id: str

type: Literal["container\_reference"]

The environment type. Always `container_reference`.

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["shell\_call"]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

created\_by: Optional[str]

The ID of the entity that created this tool call.

class BetaResponseFunctionShellToolCallOutput: …

The output of a shell tool call that was emitted.

id: str

The unique ID of the shell call output. Populated when this item is returned via API.

call\_id: str

max\_output\_length: Optional[int]

The maximum length of the shell command output. This is generated by the model and should be passed back with the raw output.

output: List[Output]

An array of shell call output contents

outcome: OutputOutcome

Represents either an exit outcome (with an exit code) or a timeout outcome for a shell call output chunk.

class OutputOutcomeTimeout: …

Indicates that the shell call exceeded its configured time limit.

type: Literal["timeout"]

The outcome type. Always `timeout`.

class OutputOutcomeExit: …

exit\_code: int

Exit code from the shell process.

type: Literal["exit"]

stderr: str

The standard error output that was captured.

stdout: str

The standard output that was captured.

created\_by: Optional[str]

The identifier of the actor that created the item.

status: Literal["in\_progress", "completed", "incomplete"]

The status of the shell call output. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

type: Literal["shell\_call\_output"]

The type of the shell call output. Always `shell_call_output`.

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseApplyPatchToolCall: …

A tool call that applies file diffs by creating, deleting, or updating files.

id: str

call\_id: str

operation: Operation

One of the create\_file, delete\_file, or update\_file operations applied via apply\_patch.

class OperationCreateFile: …

Instruction describing how to create a file via the apply\_patch tool.

diff: str

Diff to apply.

path: str

Path of the file to create.

type: Literal["create\_file"]

Create a new file with the provided diff.

class OperationDeleteFile: …

Instruction describing how to delete a file via the apply\_patch tool.

path: str

Path of the file to delete.

type: Literal["delete\_file"]

Delete the specified file.

class OperationUpdateFile: …

Instruction describing how to update a file via the apply\_patch tool.

diff: str

Diff to apply.

path: str

Path of the file to update.

type: Literal["update\_file"]

Update an existing file with the provided diff.

status: Literal["in\_progress", "completed"]

"in\_progress"

"completed"

type: Literal["apply\_patch\_call"]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

created\_by: Optional[str]

The ID of the entity that created this tool call.

class BetaResponseApplyPatchToolCallOutput: …

The output emitted by an apply patch tool call.

id: str

call\_id: str

status: Literal["completed", "failed"]

"completed"

"failed"

type: Literal["apply\_patch\_call\_output"]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

created\_by: Optional[str]

The ID of the entity that created this tool call output.

output: Optional[str]

Optional textual output returned by the apply patch tool.

class McpCall: …

An invocation of a tool on an MCP server.

id: str

arguments: str

name: str

server\_label: str

type: Literal["mcp\_call"]

agent: Optional[McpCallAgent]

agent\_name: str

approval\_request\_id: Optional[str]

error: Optional[str]

output: Optional[str]

status: Optional[Literal["in\_progress", "completed", "incomplete", 2 more]]

"in\_progress"

"completed"

"incomplete"

"calling"

"failed"

class McpListTools: …

A list of tools available on an MCP server.

id: str

server\_label: str

tools: List[McpListToolsTool]

input\_schema: object

name: str

annotations: Optional[object]

description: Optional[str]

type: Literal["mcp\_list\_tools"]

agent: Optional[McpListToolsAgent]

agent\_name: str

error: Optional[str]

class McpApprovalRequest: …

A request for human approval of a tool invocation.

id: str

arguments: str

name: str

server\_label: str

type: Literal["mcp\_approval\_request"]

agent: Optional[McpApprovalRequestAgent]

agent\_name: str

class McpApprovalResponse: …

A response to an MCP approval request.

id: str

approval\_request\_id: str

approve: bool

type: Literal["mcp\_approval\_response"]

agent: Optional[McpApprovalResponseAgent]

agent\_name: str

reason: Optional[str]

class BetaResponseCustomToolCall: …

call\_id: str

An identifier used to map this custom tool call to a tool call output.

input: str

The input for the custom tool call generated by the model.

name: str

The name of the custom tool being called.

type: Literal["custom\_tool\_call"]

The type of the custom tool call. Always `custom_tool_call`.

id: Optional[str]

The unique ID of the custom tool call in the OpenAI platform.

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

namespace: Optional[str]

The namespace of the custom tool being called.

class BetaResponseCustomToolCallOutputItem: …

id: str

The unique ID of the custom tool call output item.

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

created\_by: Optional[str]

The identifier of the actor that created the item.

usage: [BetaResponseUsage](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_usage%20%3E%20(schema))

Token accounting for the compaction pass, including cached, reasoning, and total tokens.

[BetaComputerAction](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action%20%3E%20(schema))

class Click: …

button: Literal["left", "right", "wheel", 2 more]

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

"left"

"right"

"wheel"

"back"

"forward"

type: Literal["click"]

Specifies the event type. For a click action, this property is always `click`.

x: int

The x-coordinate where the click occurred.

y: int

The y-coordinate where the click occurred.

keys: Optional[List[str]]

The keys being held while clicking.

class DoubleClick: …

A double click action.

keys: Optional[List[str]]

The keys being held while double-clicking.

type: Literal["double\_click"]

Specifies the event type. For a double click action, this property is always set to `double_click`.

x: int

The x-coordinate where the double click occurred.

y: int

The y-coordinate where the double click occurred.

class Drag: …

A drag action.

path: List[DragPath]

An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

  { x: 100, y: 200 },
  { x: 200, y: 300 }

x: int

The x-coordinate.

y: int

The y-coordinate.

type: Literal["drag"]

Specifies the event type. For a drag action, this property is always set to `drag`.

keys: Optional[List[str]]

The keys being held while dragging the mouse.

class Keypress: …

A collection of keypresses the model would like to perform.

keys: List[str]

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

type: Literal["keypress"]

Specifies the event type. For a keypress action, this property is always set to `keypress`.

class Move: …

A mouse move action.

type: Literal["move"]

Specifies the event type. For a move action, this property is always set to `move`.

x: int

The x-coordinate to move to.

y: int

The y-coordinate to move to.

keys: Optional[List[str]]

The keys being held while moving the mouse.

class Screenshot: …

A screenshot action.

type: Literal["screenshot"]

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

class Scroll: …

A scroll action.

scroll\_x: int

The horizontal scroll distance.

scroll\_y: int

The vertical scroll distance.

type: Literal["scroll"]

Specifies the event type. For a scroll action, this property is always set to `scroll`.

x: int

The x-coordinate where the scroll occurred.

y: int

The y-coordinate where the scroll occurred.

keys: Optional[List[str]]

The keys being held while scrolling.

class Type: …

An action to type in text.

text: str

The text to type.

type: Literal["type"]

Specifies the event type. For a type action, this property is always set to `type`.

class Wait: …

A wait action.

type: Literal["wait"]

Specifies the event type. For a wait action, this property is always set to `wait`.

List[[BetaComputerAction](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action%20%3E%20(schema))]

class Click: …

button: Literal["left", "right", "wheel", 2 more]

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

"left"

"right"

"wheel"

"back"

"forward"

type: Literal["click"]

Specifies the event type. For a click action, this property is always `click`.

x: int

The x-coordinate where the click occurred.

y: int

The y-coordinate where the click occurred.

keys: Optional[List[str]]

The keys being held while clicking.

class DoubleClick: …

A double click action.

keys: Optional[List[str]]

The keys being held while double-clicking.

type: Literal["double\_click"]

Specifies the event type. For a double click action, this property is always set to `double_click`.

x: int

The x-coordinate where the double click occurred.

y: int

The y-coordinate where the double click occurred.

class Drag: …

A drag action.

path: List[DragPath]

An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

  { x: 100, y: 200 },
  { x: 200, y: 300 }

x: int

The x-coordinate.

y: int

The y-coordinate.

type: Literal["drag"]

Specifies the event type. For a drag action, this property is always set to `drag`.

keys: Optional[List[str]]

The keys being held while dragging the mouse.

class Keypress: …

A collection of keypresses the model would like to perform.

keys: List[str]

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

type: Literal["keypress"]

Specifies the event type. For a keypress action, this property is always set to `keypress`.

class Move: …

A mouse move action.

type: Literal["move"]

Specifies the event type. For a move action, this property is always set to `move`.

x: int

The x-coordinate to move to.

y: int

The y-coordinate to move to.

keys: Optional[List[str]]

The keys being held while moving the mouse.

class Screenshot: …

A screenshot action.

type: Literal["screenshot"]

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

class Scroll: …

A scroll action.

scroll\_x: int

The horizontal scroll distance.

scroll\_y: int

The vertical scroll distance.

type: Literal["scroll"]

Specifies the event type. For a scroll action, this property is always set to `scroll`.

x: int

The x-coordinate where the scroll occurred.

y: int

The y-coordinate where the scroll occurred.

keys: Optional[List[str]]

The keys being held while scrolling.

class Type: …

An action to type in text.

text: str

The text to type.

type: Literal["type"]

Specifies the event type. For a type action, this property is always set to `type`.

class Wait: …

A wait action.

type: Literal["wait"]

Specifies the event type. For a wait action, this property is always set to `wait`.

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyDomainSecret: …

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaEasyInputMessage: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: Union[str, [BetaResponseInputMessageContentList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema))]

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

str

List[[BetaResponseInputContent](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_content%20%3E%20(schema))]

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

role: Literal["user", "assistant", "system", "developer"]

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

"user"

"assistant"

"system"

"developer"

phase: Optional[Literal["commentary", "final\_answer"]]

"commentary"

"final\_answer"

type: Optional[Literal["message"]]

The type of the message input. Always `message`.

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaFunctionTool: …

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaInlineSkillSource: …

data: str

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: Literal["application/zip"]

The media type of the inline skill payload. Must be `application/zip`.

type: Literal["base64"]

The type of the inline skill source. Must be `base64`.

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaLocalSkill: …

description: str

name: str

path: str

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaResponse: …

id: str

Unique identifier for this Response.

created\_at: float

Unix timestamp (in seconds) of when this Response was created.

formatunixtime

error: Optional[BetaResponseError]

An error object returned when the model fails to generate a Response.

incomplete\_details: Optional[IncompleteDetails]

Details about why the response is incomplete.

reason: Optional[Literal["max\_output\_tokens", "content\_filter"]]

The reason why the response is incomplete.

"max\_output\_tokens"

"content\_filter"

instructions: Union[str, List[[BetaResponseInputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_item%20%3E%20(schema))], null]

A system (or developer) message inserted into the model’s context.

When using along with `previous_response_id`, the instructions from a previous
response will not be carried over to the next response. This makes it simple
to swap out system (or developer) messages in new responses.

str

A text input to the model, equivalent to a text input with the
`developer` role.

List[[BetaResponseInputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_item%20%3E%20(schema))]

A list of one or many input items to the model, containing
different content types.

class BetaEasyInputMessage: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: Union[str, [BetaResponseInputMessageContentList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema))]

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

str

List[[BetaResponseInputContent](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_content%20%3E%20(schema))]

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

role: Literal["user", "assistant", "system", "developer"]

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

"user"

"assistant"

"system"

"developer"

phase: Optional[Literal["commentary", "final\_answer"]]

"commentary"

"final\_answer"

type: Optional[Literal["message"]]

The type of the message input. Always `message`.

class Message: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role.

content: [BetaResponseInputMessageContentList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema))

role: Literal["user", "system", "developer"]

"user"

"system"

"developer"

agent: Optional[MessageAgent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

type: Optional[Literal["message"]]

class BetaResponseOutputMessage: …

id: str

content: List[Content]

class BetaResponseOutputText: …

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

logprobs: Optional[List[Logprob]]

token: str

bytes: List[int]

logprob: float

top\_logprobs: List[LogprobTopLogprob]

token: str

bytes: List[int]

logprob: float

class BetaResponseOutputRefusal: …

refusal: str

type: Literal["refusal"]

role: Literal["assistant"]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["message"]

agent: Optional[Agent]

agent\_name: str

phase: Optional[Literal["commentary", "final\_answer"]]

"commentary"

"final\_answer"

class BetaResponseFileSearchToolCall: …

[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

id: str

queries: List[str]

status: Literal["in\_progress", "searching", "completed", 2 more]

"in\_progress"

"searching"

"completed"

"incomplete"

"failed"

type: Literal["file\_search\_call"]

agent: Optional[Agent]

agent\_name: str

results: Optional[List[Result]]

attributes: Optional[Dict[str, Union[str, float, bool]]]

str

float

bool

file\_id: Optional[str]

filename: Optional[str]

score: Optional[float]

formatfloat

text: Optional[str]

class BetaResponseComputerToolCall: …

[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

id: str

call\_id: str

pending\_safety\_checks: List[PendingSafetyCheck]

id: str

code: Optional[str]

message: Optional[str]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["computer\_call"]

action: Optional[BetaComputerAction]

actions: Optional[BetaComputerActionList]

agent: Optional[Agent]

agent\_name: str

class ComputerCallOutput: …

The output of a computer tool call.

call\_id: str

maxLength64

minLength1

output: [BetaResponseComputerToolCallOutputScreenshot](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema))

type: Literal["computer\_call\_output"]

id: Optional[str]

The ID of the computer tool call output.

acknowledged\_safety\_checks: Optional[List[ComputerCallOutputAcknowledgedSafetyCheck]]

The safety checks reported by the API that have been acknowledged by the developer.

id: str

code: Optional[str]

message: Optional[str]

agent: Optional[ComputerCallOutputAgent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the message input. One of `in_progress`, `completed`, or `incomplete`. Populated when input items are returned via API.

"in\_progress"

"completed"

"incomplete"

class BetaResponseFunctionWebSearch: …

[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

id: str

action: Action

class ActionSearch: …

type: Literal["search"]

queries: Optional[List[str]]

Deprecatedquery: Optional[str]

sources: Optional[List[ActionSearchSource]]

type: Literal["url"]

url: str

class ActionOpenPage: …

type: Literal["open\_page"]

url: Optional[str]

class ActionFindInPage: …

pattern: str

type: Literal["find\_in\_page"]

url: str

status: Literal["in\_progress", "searching", "completed", "failed"]

"in\_progress"

"searching"

"completed"

"failed"

type: Literal["web\_search\_call"]

agent: Optional[Agent]

agent\_name: str

class BetaResponseFunctionToolCall: …

[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

arguments: str

A JSON string of the arguments to pass to the function.

call\_id: str

name: str

The name of the function to run.

type: Literal["function\_call"]

The type of the function tool call. Always `function_call`.

id: Optional[str]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

namespace: Optional[str]

The namespace of the function to run.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class FunctionCallOutput: …

The output of a function tool call.

call\_id: str

maxLength64

minLength1

output: Union[str, [BetaResponseFunctionCallOutputItemList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item_list%20%3E%20(schema))]

Text, image, or file output of the function tool call.

str

A JSON string of the output of the function tool call.

List[[BetaResponseFunctionCallOutputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item%20%3E%20(schema))]

class BetaResponseInputTextContent: …

text: str

maxLength10485760

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImageContent: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

type: Literal["input\_image"]

detail: Optional[Literal["low", "high", "auto", "original"]]

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

image\_url: Optional[str]

maxLength20971520

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFileContent: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

The base64-encoded data of the file to be sent to the model.

maxLength73400320

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

type: Literal["function\_call\_output"]

id: Optional[str]

The unique ID of the function tool call output. Populated when this item is returned via API.

agent: Optional[FunctionCallOutputAgent]

agent\_name: str

caller: Optional[FunctionCallOutputCaller]

class FunctionCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class FunctionCallOutputCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

class AgentMessage: …

A message routed between agents.

author: str

content: List[AgentMessageContent]

Plaintext, image, or encrypted content sent between agents.

class BetaResponseInputTextContent: …

text: str

maxLength10485760

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImageContent: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

type: Literal["input\_image"]

detail: Optional[Literal["low", "high", "auto", "original"]]

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

image\_url: Optional[str]

maxLength20971520

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class AgentMessageContentEncryptedContent: …

encrypted\_content: str

maxLength10485760

type: Literal["encrypted\_content"]

recipient: str

type: Literal["agent\_message"]

The item type. Always `agent_message`.

id: Optional[str]

The unique ID of this agent message item.

agent: Optional[AgentMessageAgent]

agent\_name: str

class MultiAgentCall: …

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

The multi-agent action that was executed.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

arguments: str

The action arguments as a JSON string.

call\_id: str

maxLength64

minLength1

type: Literal["multi\_agent\_call"]

The item type. Always `multi_agent_call`.

id: Optional[str]

The unique ID of this multi-agent call.

agent: Optional[MultiAgentCallAgent]

agent\_name: str

class MultiAgentCallOutput: …

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

call\_id: str

maxLength64

minLength1

output: List[MultiAgentCallOutputOutput]

text: str

The text content.

maxLength10485760

type: Literal["output\_text"]

The content type. Always `output_text`.

annotations: Optional[List[MultiAgentCallOutputOutputAnnotation]]

Citations associated with the text content.

class MultiAgentCallOutputOutputAnnotationFileCitation: …

file\_id: str

filename: str

index: int

minimum0

type: Literal["file\_citation"]

The citation type. Always `file_citation`.

class MultiAgentCallOutputOutputAnnotationURLCitation: …

end\_index: int

The index of the last character of the citation in the message.

minimum0

start\_index: int

The index of the first character of the citation in the message.

minimum0

title: str

The title of the cited resource.

type: Literal["url\_citation"]

The citation type. Always `url_citation`.

url: str

The URL of the cited resource.

class MultiAgentCallOutputOutputAnnotationContainerFileCitation: …

container\_id: str

The ID of the container.

end\_index: int

The index of the last character of the citation in the message.

minimum0

file\_id: str

filename: str

start\_index: int

The index of the first character of the citation in the message.

minimum0

type: Literal["container\_file\_citation"]

The citation type. Always `container_file_citation`.

type: Literal["multi\_agent\_call\_output"]

The item type. Always `multi_agent_call_output`.

id: Optional[str]

The unique ID of this multi-agent call output.

agent: Optional[MultiAgentCallOutputAgent]

agent\_name: str

class ToolSearchCall: …

arguments: object

The arguments supplied to the tool search call.

type: Literal["tool\_search\_call"]

The item type. Always `tool_search_call`.

id: Optional[str]

The unique ID of this tool search call.

agent: Optional[ToolSearchCallAgent]

agent\_name: str

call\_id: Optional[str]

maxLength64

minLength1

execution: Optional[Literal["server", "client"]]

"server"

"client"

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the tool search call.

"in\_progress"

"completed"

"incomplete"

class BetaResponseToolSearchOutputItemParam: …

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

The loaded tool definitions returned by the tool search output.

class BetaFunctionTool: …

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

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

input\_fidelity: Optional[Literal["high", "low"]]

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

type: Literal["tool\_search\_output"]

The item type. Always `tool_search_output`.

id: Optional[str]

The unique ID of this tool search output.

agent: Optional[Agent]

agent\_name: str

call\_id: Optional[str]

maxLength64

minLength1

execution: Optional[Literal["server", "client"]]

"server"

"client"

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the tool search output.

"in\_progress"

"completed"

"incomplete"

class AdditionalTools: …

role: Literal["developer"]

The role that provided the additional tools. Only `developer` is supported.

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

A list of additional tools made available at this item.

class BetaFunctionTool: …

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

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

input\_fidelity: Optional[Literal["high", "low"]]

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

type: Literal["additional\_tools"]

The item type. Always `additional_tools`.

id: Optional[str]

The unique ID of this additional tools item.

agent: Optional[AdditionalToolsAgent]

agent\_name: str

class BetaResponseReasoningItem: …

[managing context](https://platform.openai.com/docs/guides/conversation-state).

id: str

summary: List[Summary]

text: str

type: Literal["summary\_text"]

type: Literal["reasoning"]

agent: Optional[Agent]

agent\_name: str

content: Optional[List[Content]]

text: str

type: Literal["reasoning\_text"]

encrypted\_content: Optional[str]

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class BetaResponseCompactionItemParam: …

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

encrypted\_content: str

The encrypted content of the compaction summary.

maxLength10485760

type: Literal["compaction"]

id: Optional[str]

The ID of the compaction item.

agent: Optional[Agent]

agent\_name: str

class ImageGenerationCall: …

An image generation request made by the model.

id: str

result: Optional[str]

status: Literal["in\_progress", "completed", "generating", "failed"]

"in\_progress"

"completed"

"generating"

"failed"

type: Literal["image\_generation\_call"]

agent: Optional[ImageGenerationCallAgent]

agent\_name: str

class BetaResponseCodeInterpreterToolCall: …

id: str

code: Optional[str]

container\_id: str

outputs: Optional[List[Output]]

class OutputLogs: …

logs: str

type: Literal["logs"]

class OutputImage: …

type: Literal["image"]

url: str

status: Literal["in\_progress", "completed", "incomplete", 2 more]

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: Literal["code\_interpreter\_call"]

agent: Optional[Agent]

agent\_name: str

class LocalShellCall: …

A tool call to run a command on the local shell.

id: str

action: LocalShellCallAction

command: List[str]

env: Dict[str, str]

type: Literal["exec"]

timeout\_ms: Optional[int]

user: Optional[str]

working\_directory: Optional[str]

call\_id: str

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["local\_shell\_call"]

agent: Optional[LocalShellCallAgent]

agent\_name: str

class LocalShellCallOutput: …

The output of a local shell tool call.

id: str

output: str

type: Literal["local\_shell\_call\_output"]

agent: Optional[LocalShellCallOutputAgent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class ShellCall: …

A tool representing a request to execute one or more shell commands.

action: ShellCallAction

commands: List[str]

Ordered shell commands for the execution environment to run.

max\_output\_length: Optional[int]

Maximum number of UTF-8 characters to capture from combined stdout and stderr output.

timeout\_ms: Optional[int]

Maximum wall-clock time in milliseconds to allow the shell commands to run.

call\_id: str

maxLength64

minLength1

type: Literal["shell\_call"]

id: Optional[str]

agent: Optional[ShellCallAgent]

agent\_name: str

caller: Optional[ShellCallCaller]

class ShellCallCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ShellCallCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

environment: Optional[ShellCallEnvironment]

The environment to execute the shell commands in.

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class ShellCallOutput: …

The streamed output items emitted by a shell tool call.

call\_id: str

maxLength64

minLength1

output: List[[BetaResponseFunctionShellCallOutputContent](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_shell_call_output_content%20%3E%20(schema))]

Captured chunks of stdout and stderr output, along with their associated outcomes.

outcome: Outcome

The exit or timeout outcome associated with this shell call.

class OutcomeTimeout: …

Indicates that the shell call exceeded its configured time limit.

type: Literal["timeout"]

The outcome type. Always `timeout`.

class OutcomeExit: …

exit\_code: int

The exit code returned by the shell process.

type: Literal["exit"]

stderr: str

Captured stderr output for the shell call.

maxLength10485760

stdout: str

Captured stdout output for the shell call.

maxLength10485760

type: Literal["shell\_call\_output"]

The type of the item. Always `shell_call_output`.

id: Optional[str]

The unique ID of the shell tool call output. Populated when this item is returned via API.

agent: Optional[ShellCallOutputAgent]

agent\_name: str

caller: Optional[ShellCallOutputCaller]

class ShellCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ShellCallOutputCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

max\_output\_length: Optional[int]

The maximum number of UTF-8 characters captured for this shell call’s combined output.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the shell call output.

"in\_progress"

"completed"

"incomplete"

class ApplyPatchCall: …

A tool call representing a request to create, delete, or update files using diff patches.

call\_id: str

maxLength64

minLength1

operation: ApplyPatchCallOperation

The specific create, delete, or update instruction for the apply\_patch tool call.

class ApplyPatchCallOperationCreateFile: …

Instruction for creating a new file via the apply\_patch tool.

diff: str

Unified diff content to apply when creating the file.

maxLength10485760

path: str

Path of the file to create relative to the workspace root.

minLength1

type: Literal["create\_file"]

The operation type. Always `create_file`.

class ApplyPatchCallOperationDeleteFile: …

Instruction for deleting an existing file via the apply\_patch tool.

path: str

Path of the file to delete relative to the workspace root.

minLength1

type: Literal["delete\_file"]

The operation type. Always `delete_file`.

class ApplyPatchCallOperationUpdateFile: …

Instruction for updating an existing file via the apply\_patch tool.

diff: str

Unified diff content to apply to the existing file.

maxLength10485760

path: str

Path of the file to update relative to the workspace root.

minLength1

type: Literal["update\_file"]

The operation type. Always `update_file`.

status: Literal["in\_progress", "completed"]

"in\_progress"

"completed"

type: Literal["apply\_patch\_call"]

id: Optional[str]

agent: Optional[ApplyPatchCallAgent]

agent\_name: str

caller: Optional[ApplyPatchCallCaller]

class ApplyPatchCallCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ApplyPatchCallCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

class ApplyPatchCallOutput: …

The streamed output emitted by an apply patch tool call.

call\_id: str

maxLength64

minLength1

status: Literal["completed", "failed"]

"completed"

"failed"

type: Literal["apply\_patch\_call\_output"]

id: Optional[str]

agent: Optional[ApplyPatchCallOutputAgent]

agent\_name: str

caller: Optional[ApplyPatchCallOutputCaller]

class ApplyPatchCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ApplyPatchCallOutputCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

output: Optional[str]

Optional human-readable log text from the apply patch tool (e.g., patch results or errors).

maxLength10485760

class McpListTools: …

A list of tools available on an MCP server.

id: str

server\_label: str

tools: List[McpListToolsTool]

input\_schema: object

name: str

annotations: Optional[object]

description: Optional[str]

type: Literal["mcp\_list\_tools"]

agent: Optional[McpListToolsAgent]

agent\_name: str

error: Optional[str]

class McpApprovalRequest: …

A request for human approval of a tool invocation.

id: str

arguments: str

name: str

server\_label: str

type: Literal["mcp\_approval\_request"]

agent: Optional[McpApprovalRequestAgent]

agent\_name: str

class McpApprovalResponse: …

A response to an MCP approval request.

approval\_request\_id: str

approve: bool

type: Literal["mcp\_approval\_response"]

id: Optional[str]

agent: Optional[McpApprovalResponseAgent]

agent\_name: str

reason: Optional[str]

class McpCall: …

An invocation of a tool on an MCP server.

id: str

arguments: str

name: str

server\_label: str

type: Literal["mcp\_call"]

agent: Optional[McpCallAgent]

agent\_name: str

approval\_request\_id: Optional[str]

error: Optional[str]

output: Optional[str]

status: Optional[Literal["in\_progress", "completed", "incomplete", 2 more]]

"in\_progress"

"completed"

"incomplete"

"calling"

"failed"

class BetaResponseCustomToolCallOutput: …

call\_id: str

The call ID, used to map this custom tool call output to a custom tool call.

output: Union[str, List[OutputOutputContentList]]

The output from the custom tool call generated by your code.

str

A string of the output of the custom tool call.

List[OutputOutputContentList]

Text, image, or file output of the custom tool call.

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

type: Literal["custom\_tool\_call\_output"]

The type of the custom tool call output. Always `custom_tool_call_output`.

id: Optional[str]

The unique ID of the custom tool call output in the OpenAI platform.

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class CallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

class BetaResponseCustomToolCall: …

call\_id: str

An identifier used to map this custom tool call to a tool call output.

input: str

The input for the custom tool call generated by the model.

name: str

The name of the custom tool being called.

type: Literal["custom\_tool\_call"]

The type of the custom tool call. Always `custom_tool_call`.

id: Optional[str]

The unique ID of the custom tool call in the OpenAI platform.

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

namespace: Optional[str]

The namespace of the custom tool being called.

class CompactionTrigger: …

Compacts the current context. Must be the final input item.

type: Literal["compaction\_trigger"]

The type of the item. Always `compaction_trigger`.

agent: Optional[CompactionTriggerAgent]

agent\_name: str

class ItemReference: …

An internal identifier for an item to reference.

id: str

The ID of the item to reference.

agent: Optional[ItemReferenceAgent]

agent\_name: str

type: Optional[Literal["item\_reference"]]

The type of item to reference. Always `item_reference`.

class Program: …

id: str

The unique ID of this program item.

call\_id: str

maxLength64

minLength1

code: str

maxLength10485760

fingerprint: str

maxLength10485760

type: Literal["program"]

The item type. Always `program`.

agent: Optional[ProgramAgent]

agent\_name: str

class ProgramOutput: …

id: str

The unique ID of this program output item.

call\_id: str

maxLength64

minLength1

result: str

maxLength10485760

status: Literal["completed", "incomplete"]

The terminal status of the program output.

"completed"

"incomplete"

type: Literal["program\_output"]

The item type. Always `program_output`.

agent: Optional[ProgramOutputAgent]

agent\_name: str

metadata: Optional[Dict[str, str]]

format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: Union[Literal["gpt-5.6-sol", "gpt-5.6-terra", "gpt-5.6-luna", 92 more], str]

Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model guide](https://platform.openai.com/docs/models)
to browse and compare available models.

Literal["gpt-5.6-sol", "gpt-5.6-terra", "gpt-5.6-luna", 92 more]

Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model guide](https://platform.openai.com/docs/models)
to browse and compare available models.

"gpt-5.6-sol"

"gpt-5.6-terra"

"gpt-5.6-luna"

"gpt-5.4"

"gpt-5.4-mini"

"gpt-5.4-nano"

"gpt-5.4-mini-2026-03-17"

"gpt-5.4-nano-2026-03-17"

"gpt-5.3-chat-latest"

"gpt-5.2"

"gpt-5.2-2025-12-11"

"gpt-5.2-chat-latest"

"gpt-5.2-pro"

"gpt-5.2-pro-2025-12-11"

"gpt-5.1"

"gpt-5.1-2025-11-13"

"gpt-5.1-codex"

"gpt-5.1-mini"

"gpt-5.1-chat-latest"

"gpt-5"

"gpt-5-mini"

"gpt-5-nano"

"gpt-5-2025-08-07"

"gpt-5-mini-2025-08-07"

"gpt-5-nano-2025-08-07"

"gpt-5-chat-latest"

"gpt-4.1"

"gpt-4.1-mini"

"gpt-4.1-nano"

"gpt-4.1-2025-04-14"

"gpt-4.1-mini-2025-04-14"

"gpt-4.1-nano-2025-04-14"

"o4-mini"

"o4-mini-2025-04-16"

"o3"

"o3-2025-04-16"

"o3-mini"

"o3-mini-2025-01-31"

"o1"

"o1-2024-12-17"

"o1-preview"

"o1-preview-2024-09-12"

"o1-mini"

"o1-mini-2024-09-12"

"gpt-4o"

"gpt-4o-2024-11-20"

"gpt-4o-2024-08-06"

"gpt-4o-2024-05-13"

"gpt-4o-audio-preview"

"gpt-4o-audio-preview-2024-10-01"

"gpt-4o-audio-preview-2024-12-17"

"gpt-4o-audio-preview-2025-06-03"

"gpt-4o-mini-audio-preview"

"gpt-4o-mini-audio-preview-2024-12-17"

"gpt-4o-search-preview"

"gpt-4o-mini-search-preview"

"gpt-4o-search-preview-2025-03-11"

"gpt-4o-mini-search-preview-2025-03-11"

"chatgpt-4o-latest"

"codex-mini-latest"

"gpt-4o-mini"

"gpt-4o-mini-2024-07-18"

"gpt-4-turbo"

"gpt-4-turbo-2024-04-09"

"gpt-4-0125-preview"

"gpt-4-turbo-preview"

"gpt-4-1106-preview"

"gpt-4-vision-preview"

"gpt-4"

"gpt-4-0314"

"gpt-4-0613"

"gpt-4-32k"

"gpt-4-32k-0314"

"gpt-4-32k-0613"

"gpt-3.5-turbo"

"gpt-3.5-turbo-16k"

"gpt-3.5-turbo-0301"

"gpt-3.5-turbo-0613"

"gpt-3.5-turbo-1106"

"gpt-3.5-turbo-0125"

"gpt-3.5-turbo-16k-0613"

"o1-pro"

"o1-pro-2025-03-19"

"o3-pro"

"o3-pro-2025-06-10"

"o3-deep-research"

"o3-deep-research-2025-06-26"

"o4-mini-deep-research"

"o4-mini-deep-research-2025-06-26"

"computer-use-preview"

"computer-use-preview-2025-03-11"

"gpt-5-codex"

"gpt-5-pro"

"gpt-5-pro-2025-10-06"

"gpt-5.1-codex-max"

str

object: Literal["response"]

The object type of this resource - always set to `response`.

output: List[[BetaResponseOutputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema))]

An array of content items generated by the model.

* The length and order of items in the `output` array is dependent
  on the model’s response.
* Rather than accessing the first item in the `output` array and
  assuming it’s an `assistant` message with the content generated by
  the model, you might consider using the `output_text` property where
  supported in SDKs.

class BetaResponseOutputMessage: …

id: str

content: List[Content]

class BetaResponseOutputText: …

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

logprobs: Optional[List[Logprob]]

token: str

bytes: List[int]

logprob: float

top\_logprobs: List[LogprobTopLogprob]

token: str

bytes: List[int]

logprob: float

class BetaResponseOutputRefusal: …

refusal: str

type: Literal["refusal"]

role: Literal["assistant"]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["message"]

agent: Optional[Agent]

agent\_name: str

phase: Optional[Literal["commentary", "final\_answer"]]

"commentary"

"final\_answer"

class BetaResponseFileSearchToolCall: …

[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

id: str

queries: List[str]

status: Literal["in\_progress", "searching", "completed", 2 more]

"in\_progress"

"searching"

"completed"

"incomplete"

"failed"

type: Literal["file\_search\_call"]

agent: Optional[Agent]

agent\_name: str

results: Optional[List[Result]]

attributes: Optional[Dict[str, Union[str, float, bool]]]

str

float

bool

file\_id: Optional[str]

filename: Optional[str]

score: Optional[float]

formatfloat

text: Optional[str]

class BetaResponseFunctionToolCall: …

[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

arguments: str

A JSON string of the arguments to pass to the function.

call\_id: str

name: str

The name of the function to run.

type: Literal["function\_call"]

The type of the function tool call. Always `function_call`.

id: Optional[str]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

namespace: Optional[str]

The namespace of the function to run.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class BetaResponseFunctionToolCallOutputItem: …

id: str

The unique ID of the function call tool output.

call\_id: str

output: Union[str, List[OutputOutputContentList]]

The output from the function call generated by your code.

str

A string of the output of the function call.

List[OutputOutputContentList]

Text, image, or file output of the function call.

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["function\_call\_output"]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class CallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

created\_by: Optional[str]

The identifier of the actor that created the item.

class AgentMessage: …

id: str

The unique ID of the agent message.

author: str

content: List[AgentMessageContent]

Encrypted content sent between agents.

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseOutputText: …

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

logprobs: Optional[List[Logprob]]

token: str

bytes: List[int]

logprob: float

top\_logprobs: List[LogprobTopLogprob]

token: str

bytes: List[int]

logprob: float

class AgentMessageContentText: …

A text content.

text: str

type: Literal["text"]

class AgentMessageContentSummaryText: …

A summary text from the model.

text: str

type: Literal["summary\_text"]

class AgentMessageContentReasoningText: …

text: str

type: Literal["reasoning\_text"]

class BetaResponseOutputRefusal: …

refusal: str

type: Literal["refusal"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class AgentMessageContentComputerScreenshot: …

A screenshot of a computer.

detail: Literal["low", "high", "auto", "original"]

The detail level of the screenshot image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

image\_url: Optional[str]

type: Literal["computer\_screenshot"]

Specifies the event type. For a computer screenshot, this property is always set to `computer_screenshot`.

prompt\_cache\_breakpoint: Optional[AgentMessageContentComputerScreenshotPromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class AgentMessageContentEncryptedContent: …

encrypted\_content: str

type: Literal["encrypted\_content"]

recipient: str

type: Literal["agent\_message"]

The type of the item. Always `agent_message`.

agent: Optional[AgentMessageAgent]

agent\_name: str

class MultiAgentCall: …

id: str

The unique ID of the multi-agent call item.

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

The multi-agent action to execute.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

arguments: str

The JSON string of arguments generated for the action.

call\_id: str

type: Literal["multi\_agent\_call"]

The type of the multi-agent call. Always `multi_agent_call`.

agent: Optional[MultiAgentCallAgent]

agent\_name: str

class MultiAgentCallOutput: …

id: str

The unique ID of the multi-agent call output item.

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

call\_id: str

output: List[[BetaResponseOutputText](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema))]

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

logprobs: Optional[List[Logprob]]

token: str

bytes: List[int]

logprob: float

top\_logprobs: List[LogprobTopLogprob]

token: str

bytes: List[int]

logprob: float

type: Literal["multi\_agent\_call\_output"]

The type of the multi-agent result. Always `multi_agent_call_output`.

agent: Optional[MultiAgentCallOutputAgent]

agent\_name: str

class BetaResponseFunctionWebSearch: …

[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

id: str

action: Action

class ActionSearch: …

type: Literal["search"]

queries: Optional[List[str]]

Deprecatedquery: Optional[str]

sources: Optional[List[ActionSearchSource]]

type: Literal["url"]

url: str

class ActionOpenPage: …

type: Literal["open\_page"]

url: Optional[str]

class ActionFindInPage: …

pattern: str

type: Literal["find\_in\_page"]

url: str

status: Literal["in\_progress", "searching", "completed", "failed"]

"in\_progress"

"searching"

"completed"

"failed"

type: Literal["web\_search\_call"]

agent: Optional[Agent]

agent\_name: str

class BetaResponseComputerToolCall: …

[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

id: str

call\_id: str

pending\_safety\_checks: List[PendingSafetyCheck]

id: str

code: Optional[str]

message: Optional[str]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["computer\_call"]

action: Optional[BetaComputerAction]

actions: Optional[BetaComputerActionList]

agent: Optional[Agent]

agent\_name: str

class BetaResponseComputerToolCallOutputItem: …

id: str

The unique ID of the computer call tool output.

call\_id: str

output: [BetaResponseComputerToolCallOutputScreenshot](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema))

status: Literal["completed", "incomplete", "failed", "in\_progress"]

"completed"

"incomplete"

"failed"

"in\_progress"

type: Literal["computer\_call\_output"]

acknowledged\_safety\_checks: Optional[List[AcknowledgedSafetyCheck]]

The safety checks reported by the API that have been acknowledged by the
developer.

id: str

code: Optional[str]

message: Optional[str]

agent: Optional[Agent]

agent\_name: str

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseReasoningItem: …

[managing context](https://platform.openai.com/docs/guides/conversation-state).

id: str

summary: List[Summary]

text: str

type: Literal["summary\_text"]

type: Literal["reasoning"]

agent: Optional[Agent]

agent\_name: str

content: Optional[List[Content]]

text: str

type: Literal["reasoning\_text"]

encrypted\_content: Optional[str]

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class Program: …

id: str

The unique ID of the program item.

call\_id: str

code: str

fingerprint: str

type: Literal["program"]

The type of the item. Always `program`.

agent: Optional[ProgramAgent]

agent\_name: str

class ProgramOutput: …

id: str

The unique ID of the program output item.

call\_id: str

result: str

status: Literal["completed", "incomplete"]

The terminal status of the program output item.

"completed"

"incomplete"

type: Literal["program\_output"]

The type of the item. Always `program_output`.

agent: Optional[ProgramOutputAgent]

agent\_name: str

class BetaResponseToolSearchCall: …

id: str

The unique ID of the tool search call item.

arguments: object

Arguments used for the tool search call.

call\_id: Optional[str]

execution: Literal["server", "client"]

"server"

"client"

status: Literal["in\_progress", "completed", "incomplete"]

The status of the tool search call item that was recorded.

"in\_progress"

"completed"

"incomplete"

type: Literal["tool\_search\_call"]

The type of the item. Always `tool_search_call`.

agent: Optional[Agent]

agent\_name: str

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseToolSearchOutputItem: …

id: str

The unique ID of the tool search output item.

call\_id: Optional[str]

execution: Literal["server", "client"]

"server"

"client"

status: Literal["in\_progress", "completed", "incomplete"]

The status of the tool search output item that was recorded.

"in\_progress"

"completed"

"incomplete"

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

The loaded tool definitions returned by tool search.

class BetaFunctionTool: …

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

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

input\_fidelity: Optional[Literal["high", "low"]]

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

type: Literal["tool\_search\_output"]

The type of the item. Always `tool_search_output`.

agent: Optional[Agent]

agent\_name: str

created\_by: Optional[str]

The identifier of the actor that created the item.

class AdditionalTools: …

id: str

The unique ID of the additional tools item.

role: Literal["unknown", "user", "assistant", 5 more]

The role that provided the additional tools.

"unknown"

"user"

"assistant"

"system"

"critic"

"discriminator"

"developer"

"tool"

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

The additional tool definitions made available at this item.

class BetaFunctionTool: …

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

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

input\_fidelity: Optional[Literal["high", "low"]]

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

type: Literal["additional\_tools"]

The type of the item. Always `additional_tools`.

agent: Optional[AdditionalToolsAgent]

agent\_name: str

class BetaResponseCompactionItem: …

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

id: str

The unique ID of the compaction item.

encrypted\_content: str

The encrypted content that was produced by compaction.

type: Literal["compaction"]

agent: Optional[Agent]

agent\_name: str

created\_by: Optional[str]

The identifier of the actor that created the item.

class ImageGenerationCall: …

An image generation request made by the model.

id: str

result: Optional[str]

status: Literal["in\_progress", "completed", "generating", "failed"]

"in\_progress"

"completed"

"generating"

"failed"

type: Literal["image\_generation\_call"]

agent: Optional[ImageGenerationCallAgent]

agent\_name: str

class BetaResponseCodeInterpreterToolCall: …

id: str

code: Optional[str]

container\_id: str

outputs: Optional[List[Output]]

class OutputLogs: …

logs: str

type: Literal["logs"]

class OutputImage: …

type: Literal["image"]

url: str

status: Literal["in\_progress", "completed", "incomplete", 2 more]

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: Literal["code\_interpreter\_call"]

agent: Optional[Agent]

agent\_name: str

class LocalShellCall: …

A tool call to run a command on the local shell.

id: str

action: LocalShellCallAction

command: List[str]

env: Dict[str, str]

type: Literal["exec"]

timeout\_ms: Optional[int]

user: Optional[str]

working\_directory: Optional[str]

call\_id: str

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["local\_shell\_call"]

agent: Optional[LocalShellCallAgent]

agent\_name: str

class LocalShellCallOutput: …

The output of a local shell tool call.

id: str

output: str

type: Literal["local\_shell\_call\_output"]

agent: Optional[LocalShellCallOutputAgent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class BetaResponseFunctionShellToolCall: …

A tool call that executes one or more shell commands in a managed environment.

id: str

action: Action

commands: List[str]

max\_output\_length: Optional[int]

Optional maximum number of characters to return from each command.

timeout\_ms: Optional[int]

Optional timeout in milliseconds for the commands.

call\_id: str

environment: Optional[Environment]

Represents the use of a local environment to perform shell actions.

class BetaResponseLocalEnvironment: …

Represents the use of a local environment to perform shell actions.

type: Literal["local"]

The environment type. Always `local`.

class BetaResponseContainerReference: …

Represents a container created with /v1/containers.

container\_id: str

type: Literal["container\_reference"]

The environment type. Always `container_reference`.

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["shell\_call"]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

created\_by: Optional[str]

The ID of the entity that created this tool call.

class BetaResponseFunctionShellToolCallOutput: …

The output of a shell tool call that was emitted.

id: str

The unique ID of the shell call output. Populated when this item is returned via API.

call\_id: str

max\_output\_length: Optional[int]

The maximum length of the shell command output. This is generated by the model and should be passed back with the raw output.

output: List[Output]

An array of shell call output contents

outcome: OutputOutcome

Represents either an exit outcome (with an exit code) or a timeout outcome for a shell call output chunk.

class OutputOutcomeTimeout: …

Indicates that the shell call exceeded its configured time limit.

type: Literal["timeout"]

The outcome type. Always `timeout`.

class OutputOutcomeExit: …

exit\_code: int

Exit code from the shell process.

type: Literal["exit"]

stderr: str

The standard error output that was captured.

stdout: str

The standard output that was captured.

created\_by: Optional[str]

The identifier of the actor that created the item.

status: Literal["in\_progress", "completed", "incomplete"]

The status of the shell call output. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

type: Literal["shell\_call\_output"]

The type of the shell call output. Always `shell_call_output`.

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseApplyPatchToolCall: …

A tool call that applies file diffs by creating, deleting, or updating files.

id: str

call\_id: str

operation: Operation

One of the create\_file, delete\_file, or update\_file operations applied via apply\_patch.

class OperationCreateFile: …

Instruction describing how to create a file via the apply\_patch tool.

diff: str

Diff to apply.

path: str

Path of the file to create.

type: Literal["create\_file"]

Create a new file with the provided diff.

class OperationDeleteFile: …

Instruction describing how to delete a file via the apply\_patch tool.

path: str

Path of the file to delete.

type: Literal["delete\_file"]

Delete the specified file.

class OperationUpdateFile: …

Instruction describing how to update a file via the apply\_patch tool.

diff: str

Diff to apply.

path: str

Path of the file to update.

type: Literal["update\_file"]

Update an existing file with the provided diff.

status: Literal["in\_progress", "completed"]

"in\_progress"

"completed"

type: Literal["apply\_patch\_call"]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

created\_by: Optional[str]

The ID of the entity that created this tool call.

class BetaResponseApplyPatchToolCallOutput: …

The output emitted by an apply patch tool call.

id: str

call\_id: str

status: Literal["completed", "failed"]

"completed"

"failed"

type: Literal["apply\_patch\_call\_output"]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

created\_by: Optional[str]

The ID of the entity that created this tool call output.

output: Optional[str]

Optional textual output returned by the apply patch tool.

class McpCall: …

An invocation of a tool on an MCP server.

id: str

arguments: str

name: str

server\_label: str

type: Literal["mcp\_call"]

agent: Optional[McpCallAgent]

agent\_name: str

approval\_request\_id: Optional[str]

error: Optional[str]

output: Optional[str]

status: Optional[Literal["in\_progress", "completed", "incomplete", 2 more]]

"in\_progress"

"completed"

"incomplete"

"calling"

"failed"

class McpListTools: …

A list of tools available on an MCP server.

id: str

server\_label: str

tools: List[McpListToolsTool]

input\_schema: object

name: str

annotations: Optional[object]

description: Optional[str]

type: Literal["mcp\_list\_tools"]

agent: Optional[McpListToolsAgent]

agent\_name: str

error: Optional[str]

class McpApprovalRequest: …

A request for human approval of a tool invocation.

id: str

arguments: str

name: str

server\_label: str

type: Literal["mcp\_approval\_request"]

agent: Optional[McpApprovalRequestAgent]

agent\_name: str

class McpApprovalResponse: …

A response to an MCP approval request.

id: str

approval\_request\_id: str

approve: bool

type: Literal["mcp\_approval\_response"]

agent: Optional[McpApprovalResponseAgent]

agent\_name: str

reason: Optional[str]

class BetaResponseCustomToolCall: …

call\_id: str

An identifier used to map this custom tool call to a tool call output.

input: str

The input for the custom tool call generated by the model.

name: str

The name of the custom tool being called.

type: Literal["custom\_tool\_call"]

The type of the custom tool call. Always `custom_tool_call`.

id: Optional[str]

The unique ID of the custom tool call in the OpenAI platform.

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

namespace: Optional[str]

The namespace of the custom tool being called.

class BetaResponseCustomToolCallOutputItem: …

id: str

The unique ID of the custom tool call output item.

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

created\_by: Optional[str]

The identifier of the actor that created the item.

parallel\_tool\_calls: bool

Whether to allow the model to run tool calls in parallel.

temperature: Optional[float]

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
We generally recommend altering this or `top_p` but not both.

minimum0

maximum2

tool\_choice: ToolChoice

How the model should select which tool (or tools) to use when generating
a response. See the `tools` parameter to see how to specify which tools
the model can call.

Literal["none", "auto", "required"]

"none"

"auto"

"required"

class BetaToolChoiceAllowed: …

Constrains the tools available to the model to a pre-defined set.

mode: Literal["auto", "required"]

Constrains the tools available to the model to a pre-defined set.

`auto` allows the model to pick from among the allowed tools and generate a
message.

`required` requires the model to call one or more of the allowed tools.

"auto"

"required"

tools: List[Dict[str, object]]

A list of tool definitions that the model should be allowed to call.

For the Responses API, the list of tool definitions might look like:

  { "type": "function", "name": "get_weather" },
  { "type": "mcp", "server_label": "deepwiki" },
  { "type": "image_generation" }

type: Literal["allowed\_tools"]

Allowed tool configuration type. Always `allowed_tools`.

class BetaToolChoiceTypes: …

Indicates that the model should use a built-in tool to generate a response.
[Learn more about built-in tools](https://platform.openai.com/docs/guides/tools).

type: Literal["file\_search", "web\_search\_preview", "computer", 5 more]

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

class BetaToolChoiceFunction: …

Use this option to force the model to call a specific function.

name: str

type: Literal["function"]

For function calling, the type is always `function`.

class BetaToolChoiceMcp: …

Use this option to force the model to call a specific tool on a remote MCP server.

server\_label: str

The label of the MCP server to use.

type: Literal["mcp"]

For MCP tools, the type is always `mcp`.

name: Optional[str]

The name of the tool to call on the server.

class BetaToolChoiceCustom: …

Use this option to force the model to call a specific custom tool.

name: str

The name of the custom tool to call.

type: Literal["custom"]

For custom tool calling, the type is always `custom`.

class ToolChoiceBetaSpecificProgrammaticToolCallingParam: …

type: Literal["programmatic\_tool\_calling"]

The tool to call. Always `programmatic_tool_calling`.

class BetaToolChoiceApplyPatch: …

Forces the model to call the apply\_patch tool when executing a tool call.

type: Literal["apply\_patch"]

The tool to call. Always `apply_patch`.

class BetaToolChoiceShell: …

Forces the model to call the shell tool when a tool call is required.

type: Literal["shell"]

The tool to call. Always `shell`.

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

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

class BetaFunctionTool: …

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

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

input\_fidelity: Optional[Literal["high", "low"]]

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

top\_p: Optional[float]

An alternative to sampling with temperature, called nucleus sampling,
where the model considers the results of the tokens with top\_p probability
mass. So 0.1 means only the tokens comprising the top 10% probability mass
are considered.

We generally recommend altering this or `temperature` but not both.

minimum0

maximum1

background: Optional[bool]

Whether to run the model response in the background.
[Learn more](https://platform.openai.com/docs/guides/background).

completed\_at: Optional[float]

Unix timestamp (in seconds) of when this Response was completed.
Only present when the status is `completed`.

formatunixtime

conversation: Optional[Conversation]

The conversation that this response belonged to. Input items and output items from this response were automatically added to this conversation.

id: str

The unique ID of the conversation that this response was associated with.

max\_output\_tokens: Optional[int]

An upper bound for the number of tokens that can be generated for a response, including visible output tokens and [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

max\_tool\_calls: Optional[int]

The maximum number of total calls to built-in tools that can be processed in a response. This maximum number applies across all built-in tool calls, not per individual tool. Any further attempts to call a tool by the model will be ignored.

moderation: Optional[Moderation]

Moderation results for the response input and output, if moderated completions were requested.

input: ModerationInput

Moderation for the response input.

class ModerationInputModerationResult: …

A moderation result produced for the response input or output.

categories: Dict[str, bool]

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

category\_applied\_input\_types: Dict[str, List[Literal["text", "image"]]]

Which modalities of input are reflected by the score for each category.

"text"

"image"

category\_scores: Dict[str, float]

A dictionary of moderation categories to scores.

flagged: bool

A boolean indicating whether the content was flagged by any category.

model: str

The moderation model that produced this result.

type: Literal["moderation\_result"]

The object type, which was always `moderation_result` for successful moderation results.

class ModerationInputError: …

An error produced while attempting moderation for the response input or output.

code: str

The error code.

message: str

The error message.

type: Literal["error"]

The object type, which was always `error` for moderation failures.

output: ModerationOutput

Moderation for the response output.

class ModerationOutputModerationResult: …

A moderation result produced for the response input or output.

categories: Dict[str, bool]

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

category\_applied\_input\_types: Dict[str, List[Literal["text", "image"]]]

Which modalities of input are reflected by the score for each category.

"text"

"image"

category\_scores: Dict[str, float]

A dictionary of moderation categories to scores.

flagged: bool

A boolean indicating whether the content was flagged by any category.

model: str

The moderation model that produced this result.

type: Literal["moderation\_result"]

The object type, which was always `moderation_result` for successful moderation results.

class ModerationOutputError: …

An error produced while attempting moderation for the response input or output.

code: str

The error code.

message: str

The error message.

type: Literal["error"]

The object type, which was always `error` for moderation failures.

previous\_response\_id: Optional[str]

The unique ID of the previous response to the model. Use this to
create multi-turn conversations. Learn more about
[conversation state](https://platform.openai.com/docs/guides/conversation-state). Cannot be used in conjunction with `conversation`.

prompt: Optional[BetaResponsePrompt]

Reference to a prompt template and its variables.
[Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

prompt\_cache\_key: Optional[str]

Used by OpenAI to cache responses for similar requests to optimize your cache hit rates. Replaces the `user` field. [Learn more](https://platform.openai.com/docs/guides/prompt-caching).

prompt\_cache\_options: Optional[PromptCacheOptions]

The prompt-caching options that were applied to the response. Supported for `gpt-5.6` and later models.

mode: Literal["implicit", "explicit"]

Whether implicit prompt-cache breakpoints were enabled.

"implicit"

"explicit"

ttl: Literal["30m"]

The minimum lifetime applied to each cache breakpoint.

Deprecatedprompt\_cache\_retention: Optional[Literal["in\_memory", "24h"]]

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

reasoning: Optional[Reasoning]

**gpt-5 and o-series models only**

Configuration options for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).

context: Optional[Literal["auto", "current\_turn", "all\_turns"]]

Controls which reasoning items are rendered back to the model on later turns.
When returned on a response, this is the effective reasoning context mode
used for the response.

"auto"

"current\_turn"

"all\_turns"

effort: Optional[Literal["none", "minimal", "low", 4 more]]

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

Deprecatedgenerate\_summary: Optional[Literal["auto", "concise", "detailed"]]

**Deprecated:** use `summary` instead.

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

"auto"

"concise"

"detailed"

mode: Optional[Union[str, Literal["standard", "pro"], null]]

Controls the reasoning execution mode for the request.

When returned on a response, this is the effective execution mode.

str

Literal["standard", "pro"]

Controls the reasoning execution mode for the request.

When returned on a response, this is the effective execution mode.

"standard"

"pro"

summary: Optional[Literal["auto", "concise", "detailed"]]

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

`concise` is supported for `computer-use-preview` models and all reasoning models after `gpt-5`.

"auto"

"concise"

"detailed"

safety\_identifier: Optional[str]

A stable identifier used to help detect users of your application that may be violating OpenAI’s usage policies.
The IDs should be a string that uniquely identifies each user, with a maximum length of 64 characters. We recommend hashing their username or email address, in order to avoid sending us any identifying information. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

maxLength64

service\_tier: Optional[Literal["auto", "default", "flex", 2 more]]

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

status: Optional[BetaResponseStatus]

The status of the response generation. One of `completed`, `failed`,
`in_progress`, `cancelled`, `queued`, or `incomplete`.

text: Optional[BetaResponseTextConfig]

Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:

* [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
* [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

top\_logprobs: Optional[int]

An integer between 0 and 20 specifying the maximum number of most likely
tokens to return at each token position, each with an associated log
probability. In some cases, the number of returned tokens may be fewer than
requested.

minimum0

maximum20

truncation: Optional[Literal["auto", "disabled"]]

The truncation strategy to use for the model response.

* `auto`: If the input to this Response exceeds
  the model’s context window size, the model will truncate the
  response to fit the context window by dropping items from the beginning of the conversation.
* `disabled` (default): If the input size will exceed the context window
  size for a model, the request will fail with a 400 error.

"auto"

"disabled"

usage: Optional[BetaResponseUsage]

Represents token usage details including input tokens, output tokens,
a breakdown of output tokens, and the total tokens used.

Deprecateduser: Optional[str]

This field is being replaced by `safety_identifier` and `prompt_cache_key`. Use `prompt_cache_key` instead to maintain caching optimizations.
A stable identifier for your end-users.
Used to boost cache hit rates by better bucketing similar requests and to help OpenAI detect and prevent abuse. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

class BetaResponseApplyPatchToolCall: …

A tool call that applies file diffs by creating, deleting, or updating files.

id: str

call\_id: str

operation: Operation

One of the create\_file, delete\_file, or update\_file operations applied via apply\_patch.

class OperationCreateFile: …

Instruction describing how to create a file via the apply\_patch tool.

diff: str

Diff to apply.

path: str

Path of the file to create.

type: Literal["create\_file"]

Create a new file with the provided diff.

class OperationDeleteFile: …

Instruction describing how to delete a file via the apply\_patch tool.

path: str

Path of the file to delete.

type: Literal["delete\_file"]

Delete the specified file.

class OperationUpdateFile: …

Instruction describing how to update a file via the apply\_patch tool.

diff: str

Diff to apply.

path: str

Path of the file to update.

type: Literal["update\_file"]

Update an existing file with the provided diff.

status: Literal["in\_progress", "completed"]

"in\_progress"

"completed"

type: Literal["apply\_patch\_call"]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

created\_by: Optional[str]

The ID of the entity that created this tool call.

class BetaResponseApplyPatchToolCallOutput: …

The output emitted by an apply patch tool call.

id: str

call\_id: str

status: Literal["completed", "failed"]

"completed"

"failed"

type: Literal["apply\_patch\_call\_output"]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

created\_by: Optional[str]

The ID of the entity that created this tool call output.

output: Optional[str]

Optional textual output returned by the apply patch tool.

class BetaResponseAudioDeltaEvent: …

Emitted when there is a partial audio response.

delta: str

A chunk of Base64 encoded response audio bytes.

sequence\_number: int

A sequence number for this chunk of the stream response.

type: Literal["response.audio.delta"]

The type of the event. Always `response.audio.delta`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseAudioDoneEvent: …

Emitted when the audio response is complete.

sequence\_number: int

The sequence number of the delta.

type: Literal["response.audio.done"]

The type of the event. Always `response.audio.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseAudioTranscriptDeltaEvent: …

Emitted when there is a partial transcript of audio.

delta: str

The partial transcript of the audio response.

sequence\_number: int

The sequence number of this event.

type: Literal["response.audio.transcript.delta"]

The type of the event. Always `response.audio.transcript.delta`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseAudioTranscriptDoneEvent: …

Emitted when the full audio transcript is completed.

sequence\_number: int

The sequence number of this event.

type: Literal["response.audio.transcript.done"]

The type of the event. Always `response.audio.transcript.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseCodeInterpreterCallCodeDeltaEvent: …

Emitted when a partial code snippet is streamed by the code interpreter.

delta: str

The partial code snippet being streamed by the code interpreter.

item\_id: str

The unique identifier of the code interpreter tool call item.

output\_index: int

The index of the output item in the response for which the code is being streamed.

sequence\_number: int

The sequence number of this event, used to order streaming events.

type: Literal["response.code\_interpreter\_call\_code.delta"]

The type of the event. Always `response.code_interpreter_call_code.delta`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseCodeInterpreterCallCodeDoneEvent: …

Emitted when the code snippet is finalized by the code interpreter.

code: str

The final code snippet output by the code interpreter.

item\_id: str

The unique identifier of the code interpreter tool call item.

output\_index: int

The index of the output item in the response for which the code is finalized.

sequence\_number: int

The sequence number of this event, used to order streaming events.

type: Literal["response.code\_interpreter\_call\_code.done"]

The type of the event. Always `response.code_interpreter_call_code.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseCodeInterpreterCallCompletedEvent: …

Emitted when the code interpreter call is completed.

item\_id: str

The unique identifier of the code interpreter tool call item.

output\_index: int

The index of the output item in the response for which the code interpreter call is completed.

sequence\_number: int

The sequence number of this event, used to order streaming events.

type: Literal["response.code\_interpreter\_call.completed"]

The type of the event. Always `response.code_interpreter_call.completed`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseCodeInterpreterCallInProgressEvent: …

Emitted when a code interpreter call is in progress.

item\_id: str

The unique identifier of the code interpreter tool call item.

output\_index: int

The index of the output item in the response for which the code interpreter call is in progress.

sequence\_number: int

The sequence number of this event, used to order streaming events.

type: Literal["response.code\_interpreter\_call.in\_progress"]

The type of the event. Always `response.code_interpreter_call.in_progress`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseCodeInterpreterCallInterpretingEvent: …

Emitted when the code interpreter is actively interpreting the code snippet.

item\_id: str

The unique identifier of the code interpreter tool call item.

output\_index: int

The index of the output item in the response for which the code interpreter is interpreting code.

sequence\_number: int

The sequence number of this event, used to order streaming events.

type: Literal["response.code\_interpreter\_call.interpreting"]

The type of the event. Always `response.code_interpreter_call.interpreting`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseCodeInterpreterToolCall: …

id: str

code: Optional[str]

container\_id: str

outputs: Optional[List[Output]]

class OutputLogs: …

logs: str

type: Literal["logs"]

class OutputImage: …

type: Literal["image"]

url: str

status: Literal["in\_progress", "completed", "incomplete", 2 more]

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: Literal["code\_interpreter\_call"]

agent: Optional[Agent]

agent\_name: str

class BetaResponseCompactionItem: …

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

id: str

The unique ID of the compaction item.

encrypted\_content: str

The encrypted content that was produced by compaction.

type: Literal["compaction"]

agent: Optional[Agent]

agent\_name: str

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseCompactionItemParam: …

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

encrypted\_content: str

The encrypted content of the compaction summary.

maxLength10485760

type: Literal["compaction"]

id: Optional[str]

The ID of the compaction item.

agent: Optional[Agent]

agent\_name: str

class BetaResponseCompletedEvent: …

Emitted when the model response is complete.

response: [BetaResponse](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

Properties of the completed response.

sequence\_number: int

The sequence number for this event.

type: Literal["response.completed"]

The type of the event. Always `response.completed`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseComputerToolCall: …

[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

id: str

call\_id: str

pending\_safety\_checks: List[PendingSafetyCheck]

id: str

code: Optional[str]

message: Optional[str]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["computer\_call"]

action: Optional[BetaComputerAction]

actions: Optional[BetaComputerActionList]

agent: Optional[Agent]

agent\_name: str

class BetaResponseComputerToolCallOutputItem: …

id: str

The unique ID of the computer call tool output.

call\_id: str

output: [BetaResponseComputerToolCallOutputScreenshot](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema))

status: Literal["completed", "incomplete", "failed", "in\_progress"]

"completed"

"incomplete"

"failed"

"in\_progress"

type: Literal["computer\_call\_output"]

acknowledged\_safety\_checks: Optional[List[AcknowledgedSafetyCheck]]

The safety checks reported by the API that have been acknowledged by the
developer.

id: str

code: Optional[str]

message: Optional[str]

agent: Optional[Agent]

agent\_name: str

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseComputerToolCallOutputScreenshot: …

type: Literal["computer\_screenshot"]

Specifies the event type. For a computer screenshot, this property is
always set to `computer_screenshot`.

file\_id: Optional[str]

image\_url: Optional[str]

class BetaResponseContainerReference: …

Represents a container created with /v1/containers.

container\_id: str

type: Literal["container\_reference"]

The environment type. Always `container_reference`.

[BetaResponseContent](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_content%20%3E%20(schema))

Multi-modal input and output contents.

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseOutputText: …

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

logprobs: Optional[List[Logprob]]

token: str

bytes: List[int]

logprob: float

top\_logprobs: List[LogprobTopLogprob]

token: str

bytes: List[int]

logprob: float

class BetaResponseOutputRefusal: …

refusal: str

type: Literal["refusal"]

class ReasoningText: …

text: str

type: Literal["reasoning\_text"]

class BetaResponseContentPartAddedEvent: …

Emitted when a new content part is added.

content\_index: int

The index of the content part that was added.

item\_id: str

The ID of the output item that the content part was added to.

output\_index: int

The index of the output item that the content part was added to.

part: Part

The content part that was added.

class BetaResponseOutputText: …

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

logprobs: Optional[List[Logprob]]

token: str

bytes: List[int]

logprob: float

top\_logprobs: List[LogprobTopLogprob]

token: str

bytes: List[int]

logprob: float

class BetaResponseOutputRefusal: …

refusal: str

type: Literal["refusal"]

class PartReasoningText: …

text: str

type: Literal["reasoning\_text"]

sequence\_number: int

The sequence number of this event.

type: Literal["response.content\_part.added"]

The type of the event. Always `response.content_part.added`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseContentPartDoneEvent: …

Emitted when a content part is done.

content\_index: int

The index of the content part that is done.

item\_id: str

The ID of the output item that the content part was added to.

output\_index: int

The index of the output item that the content part was added to.

part: Part

The content part that is done.

class BetaResponseOutputText: …

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

logprobs: Optional[List[Logprob]]

token: str

bytes: List[int]

logprob: float

top\_logprobs: List[LogprobTopLogprob]

token: str

bytes: List[int]

logprob: float

class BetaResponseOutputRefusal: …

refusal: str

type: Literal["refusal"]

class PartReasoningText: …

text: str

type: Literal["reasoning\_text"]

sequence\_number: int

The sequence number of this event.

type: Literal["response.content\_part.done"]

The type of the event. Always `response.content_part.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseConversationParam: …

The conversation that this response belongs to.

id: str

The unique ID of the conversation.

class BetaResponseCreatedEvent: …

An event that is emitted when a response is created.

response: [BetaResponse](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

The response that was created.

sequence\_number: int

The sequence number for this event.

type: Literal["response.created"]

The type of the event. Always `response.created`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseCustomToolCall: …

call\_id: str

An identifier used to map this custom tool call to a tool call output.

input: str

The input for the custom tool call generated by the model.

name: str

The name of the custom tool being called.

type: Literal["custom\_tool\_call"]

The type of the custom tool call. Always `custom_tool_call`.

id: Optional[str]

The unique ID of the custom tool call in the OpenAI platform.

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

namespace: Optional[str]

The namespace of the custom tool being called.

class BetaResponseCustomToolCallInputDeltaEvent: …

Event representing a delta (partial update) to the input of a custom tool call.

delta: str

The incremental input data (delta) for the custom tool call.

item\_id: str

Unique identifier for the API item associated with this event.

output\_index: int

The index of the output this delta applies to.

sequence\_number: int

The sequence number of this event.

type: Literal["response.custom\_tool\_call\_input.delta"]

The event type identifier.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseCustomToolCallInputDoneEvent: …

Event indicating that input for a custom tool call is complete.

input: str

The complete input data for the custom tool call.

item\_id: str

Unique identifier for the API item associated with this event.

output\_index: int

The index of the output this event applies to.

sequence\_number: int

The sequence number of this event.

type: Literal["response.custom\_tool\_call\_input.done"]

The event type identifier.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseCustomToolCallItem: …

id: str

The unique ID of the custom tool call item.

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseCustomToolCallOutput: …

call\_id: str

The call ID, used to map this custom tool call output to a custom tool call.

output: Union[str, List[OutputOutputContentList]]

The output from the custom tool call generated by your code.

str

A string of the output of the custom tool call.

List[OutputOutputContentList]

Text, image, or file output of the custom tool call.

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

type: Literal["custom\_tool\_call\_output"]

The type of the custom tool call output. Always `custom_tool_call_output`.

id: Optional[str]

The unique ID of the custom tool call output in the OpenAI platform.

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class CallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

class BetaResponseCustomToolCallOutputItem: …

id: str

The unique ID of the custom tool call output item.

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseError: …

An error object returned when the model fails to generate a Response.

code: Literal["server\_error", "rate\_limit\_exceeded", "invalid\_prompt", 16 more]

The error code for the response.

"server\_error"

"rate\_limit\_exceeded"

"invalid\_prompt"

"bio\_policy"

"vector\_store\_timeout"

"invalid\_image"

"invalid\_image\_format"

"invalid\_base64\_image"

"invalid\_image\_url"

"image\_too\_large"

"image\_too\_small"

"image\_parse\_error"

"image\_content\_policy\_violation"

"invalid\_image\_mode"

"image\_file\_too\_large"

"unsupported\_image\_media\_type"

"empty\_image\_file"

"failed\_to\_download\_image"

"image\_file\_not\_found"

message: str

A human-readable description of the error.

class BetaResponseErrorEvent: …

Emitted when an error occurs.

code: Optional[str]

The error code.

message: str

The error message.

param: Optional[str]

The error parameter.

sequence\_number: int

The sequence number of this event.

type: Literal["error"]

The type of the event. Always `error`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseFailedEvent: …

An event that is emitted when a response fails.

response: [BetaResponse](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

The response that failed.

sequence\_number: int

The sequence number of this event.

type: Literal["response.failed"]

The type of the event. Always `response.failed`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseFileSearchCallCompletedEvent: …

Emitted when a file search call is completed (results found).

item\_id: str

The ID of the output item that the file search call is initiated.

output\_index: int

The index of the output item that the file search call is initiated.

sequence\_number: int

The sequence number of this event.

type: Literal["response.file\_search\_call.completed"]

The type of the event. Always `response.file_search_call.completed`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseFileSearchCallInProgressEvent: …

Emitted when a file search call is initiated.

item\_id: str

The ID of the output item that the file search call is initiated.

output\_index: int

The index of the output item that the file search call is initiated.

sequence\_number: int

The sequence number of this event.

type: Literal["response.file\_search\_call.in\_progress"]

The type of the event. Always `response.file_search_call.in_progress`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseFileSearchCallSearchingEvent: …

Emitted when a file search is currently searching.

item\_id: str

The ID of the output item that the file search call is initiated.

output\_index: int

The index of the output item that the file search call is searching.

sequence\_number: int

The sequence number of this event.

type: Literal["response.file\_search\_call.searching"]

The type of the event. Always `response.file_search_call.searching`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseFileSearchToolCall: …

[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

id: str

queries: List[str]

status: Literal["in\_progress", "searching", "completed", 2 more]

"in\_progress"

"searching"

"completed"

"incomplete"

"failed"

type: Literal["file\_search\_call"]

agent: Optional[Agent]

agent\_name: str

results: Optional[List[Result]]

attributes: Optional[Dict[str, Union[str, float, bool]]]

str

float

bool

file\_id: Optional[str]

filename: Optional[str]

score: Optional[float]

formatfloat

text: Optional[str]

[BetaResponseFormatTextConfig](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_format_text_config%20%3E%20(schema))

An object specifying the format that the model must output.

Configuring `{ "type": "json_schema" }` enables Structured Outputs,
which ensures the model will match your supplied JSON schema. Learn more in the
[Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

The default format is `{ "type": "text" }` with no additional options.

**Not recommended for gpt-4o and newer models:**

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

class Text: …

Default response format. Used to generate text responses.

type: Literal["text"]

The type of response format being defined. Always `text`.

class BetaResponseFormatTextJSONSchemaConfig: …

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

name: str

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

schema: Dict[str, object]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

type: Literal["json\_schema"]

The type of response format being defined. Always `json_schema`.

description: Optional[str]

A description of what the response format is for, used by the model to
determine how to respond in the format.

strict: Optional[bool]

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

class JSONObject: …

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: Literal["json\_object"]

The type of response format being defined. Always `json_object`.

class BetaResponseFormatTextJSONSchemaConfig: …

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

name: str

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

schema: Dict[str, object]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

type: Literal["json\_schema"]

The type of response format being defined. Always `json_schema`.

description: Optional[str]

A description of what the response format is for, used by the model to
determine how to respond in the format.

strict: Optional[bool]

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

class BetaResponseFunctionCallArgumentsDeltaEvent: …

Emitted when there is a partial function-call arguments delta.

delta: str

The function-call arguments delta that is added.

item\_id: str

The ID of the output item that the function-call arguments delta is added to.

output\_index: int

The index of the output item that the function-call arguments delta is added to.

sequence\_number: int

The sequence number of this event.

type: Literal["response.function\_call\_arguments.delta"]

The type of the event. Always `response.function_call_arguments.delta`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseFunctionCallArgumentsDoneEvent: …

Emitted when function-call arguments are finalized.

arguments: str

The function-call arguments.

item\_id: str

The ID of the item.

name: str

The name of the function that was called.

output\_index: int

The index of the output item.

sequence\_number: int

The sequence number of this event.

type: Literal["response.function\_call\_arguments.done"]

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

[BetaResponseFunctionCallOutputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item%20%3E%20(schema))

A piece of message content, such as text, an image, or a file.

class BetaResponseInputTextContent: …

text: str

maxLength10485760

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImageContent: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

type: Literal["input\_image"]

detail: Optional[Literal["low", "high", "auto", "original"]]

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

image\_url: Optional[str]

maxLength20971520

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFileContent: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

The base64-encoded data of the file to be sent to the model.

maxLength73400320

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

List[[BetaResponseFunctionCallOutputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item%20%3E%20(schema))]

An array of content outputs (text, image, file) for the function tool call.

class BetaResponseInputTextContent: …

text: str

maxLength10485760

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImageContent: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

type: Literal["input\_image"]

detail: Optional[Literal["low", "high", "auto", "original"]]

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

image\_url: Optional[str]

maxLength20971520

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFileContent: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

The base64-encoded data of the file to be sent to the model.

maxLength73400320

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseFunctionShellCallOutputContent: …

Captured stdout and stderr for a portion of a shell tool call output.

outcome: Outcome

The exit or timeout outcome associated with this shell call.

class OutcomeTimeout: …

Indicates that the shell call exceeded its configured time limit.

type: Literal["timeout"]

The outcome type. Always `timeout`.

class OutcomeExit: …

exit\_code: int

The exit code returned by the shell process.

type: Literal["exit"]

stderr: str

Captured stderr output for the shell call.

maxLength10485760

stdout: str

Captured stdout output for the shell call.

maxLength10485760

class BetaResponseFunctionShellToolCall: …

A tool call that executes one or more shell commands in a managed environment.

id: str

action: Action

commands: List[str]

max\_output\_length: Optional[int]

Optional maximum number of characters to return from each command.

timeout\_ms: Optional[int]

Optional timeout in milliseconds for the commands.

call\_id: str

environment: Optional[Environment]

Represents the use of a local environment to perform shell actions.

class BetaResponseLocalEnvironment: …

Represents the use of a local environment to perform shell actions.

type: Literal["local"]

The environment type. Always `local`.

class BetaResponseContainerReference: …

Represents a container created with /v1/containers.

container\_id: str

type: Literal["container\_reference"]

The environment type. Always `container_reference`.

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["shell\_call"]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

created\_by: Optional[str]

The ID of the entity that created this tool call.

class BetaResponseFunctionShellToolCallOutput: …

The output of a shell tool call that was emitted.

id: str

The unique ID of the shell call output. Populated when this item is returned via API.

call\_id: str

max\_output\_length: Optional[int]

The maximum length of the shell command output. This is generated by the model and should be passed back with the raw output.

output: List[Output]

An array of shell call output contents

outcome: OutputOutcome

Represents either an exit outcome (with an exit code) or a timeout outcome for a shell call output chunk.

class OutputOutcomeTimeout: …

Indicates that the shell call exceeded its configured time limit.

type: Literal["timeout"]

The outcome type. Always `timeout`.

class OutputOutcomeExit: …

exit\_code: int

Exit code from the shell process.

type: Literal["exit"]

stderr: str

The standard error output that was captured.

stdout: str

The standard output that was captured.

created\_by: Optional[str]

The identifier of the actor that created the item.

status: Literal["in\_progress", "completed", "incomplete"]

The status of the shell call output. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

type: Literal["shell\_call\_output"]

The type of the shell call output. Always `shell_call_output`.

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseFunctionToolCall: …

[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

arguments: str

A JSON string of the arguments to pass to the function.

call\_id: str

name: str

The name of the function to run.

type: Literal["function\_call"]

The type of the function tool call. Always `function_call`.

id: Optional[str]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

namespace: Optional[str]

The namespace of the function to run.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class BetaResponseFunctionToolCallItem: …

[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

id: str

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseFunctionToolCallOutputItem: …

id: str

The unique ID of the function call tool output.

call\_id: str

output: Union[str, List[OutputOutputContentList]]

The output from the function call generated by your code.

str

A string of the output of the function call.

List[OutputOutputContentList]

Text, image, or file output of the function call.

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["function\_call\_output"]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class CallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseFunctionWebSearch: …

[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

id: str

action: Action

class ActionSearch: …

type: Literal["search"]

queries: Optional[List[str]]

Deprecatedquery: Optional[str]

sources: Optional[List[ActionSearchSource]]

type: Literal["url"]

url: str

class ActionOpenPage: …

type: Literal["open\_page"]

url: Optional[str]

class ActionFindInPage: …

pattern: str

type: Literal["find\_in\_page"]

url: str

status: Literal["in\_progress", "searching", "completed", "failed"]

"in\_progress"

"searching"

"completed"

"failed"

type: Literal["web\_search\_call"]

agent: Optional[Agent]

agent\_name: str

class BetaResponseImageGenCallCompletedEvent: …

Emitted when an image generation tool call has completed and the final image is available.

item\_id: str

The unique identifier of the image generation item being processed.

output\_index: int

The index of the output item in the response’s output array.

sequence\_number: int

The sequence number of this event.

type: Literal["response.image\_generation\_call.completed"]

The type of the event. Always ‘response.image\_generation\_call.completed’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseImageGenCallGeneratingEvent: …

Emitted when an image generation tool call is actively generating an image (intermediate state).

item\_id: str

The unique identifier of the image generation item being processed.

output\_index: int

The index of the output item in the response’s output array.

sequence\_number: int

The sequence number of the image generation item being processed.

type: Literal["response.image\_generation\_call.generating"]

The type of the event. Always ‘response.image\_generation\_call.generating’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseImageGenCallInProgressEvent: …

Emitted when an image generation tool call is in progress.

item\_id: str

The unique identifier of the image generation item being processed.

output\_index: int

The index of the output item in the response’s output array.

sequence\_number: int

The sequence number of the image generation item being processed.

type: Literal["response.image\_generation\_call.in\_progress"]

The type of the event. Always ‘response.image\_generation\_call.in\_progress’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseImageGenCallPartialImageEvent: …

Emitted when a partial image is available during image generation streaming.

item\_id: str

The unique identifier of the image generation item being processed.

output\_index: int

The index of the output item in the response’s output array.

partial\_image\_b64: str

Base64-encoded partial image data, suitable for rendering as an image.

partial\_image\_index: int

0-based index for the partial image (backend is 1-based, but this is 0-based for the user).

sequence\_number: int

The sequence number of the image generation item being processed.

type: Literal["response.image\_generation\_call.partial\_image"]

The type of the event. Always ‘response.image\_generation\_call.partial\_image’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseInProgressEvent: …

Emitted when the response is in progress.

response: [BetaResponse](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

The response that is in progress.

sequence\_number: int

The sequence number of this event.

type: Literal["response.in\_progress"]

The type of the event. Always `response.in_progress`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

Literal["file\_search\_call.results", "web\_search\_call.results", "web\_search\_call.action.sources", 5 more]

Specify additional output data to include in the model response. Currently supported values are:

* `web_search_call.results`: Include the search results of the web search tool call.
* `web_search_call.action.sources`: Include the sources of the web search tool call.
* `code_interpreter_call.outputs`: Includes the outputs of python code execution in code interpreter tool call items.
* `computer_call_output.output.image_url`: Include image urls from the computer call output.
* `file_search_call.results`: Include the search results of the file search tool call.
* `message.input_image.image_url`: Include image urls from the input message.
* `message.output_text.logprobs`: Include logprobs with assistant messages.
* `reasoning.encrypted_content`: Includes an encrypted version of reasoning tokens in reasoning item outputs. This enables reasoning items to be used in multi-turn conversations when using the Responses API statelessly (like when the `store` parameter is set to `false`, or when an organization is enrolled in the zero data retention program).

"file\_search\_call.results"

"web\_search\_call.results"

"web\_search\_call.action.sources"

"message.input\_image.image\_url"

"computer\_call\_output.output.image\_url"

"code\_interpreter\_call.outputs"

"reasoning.encrypted\_content"

"message.output\_text.logprobs"

class BetaResponseIncompleteEvent: …

An event that is emitted when a response finishes as incomplete.

response: [BetaResponse](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

The response that was incomplete.

sequence\_number: int

The sequence number of this event.

type: Literal["response.incomplete"]

The type of the event. Always `response.incomplete`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseInjectCreatedEvent: …

Emitted when all injected input items were validated and committed to the
active response.

response\_id: str

The ID of the response that accepted the input.

sequence\_number: int

The sequence number for this event.

type: Literal["response.inject.created"]

The event discriminator. Always `response.inject.created`.

stream\_id: Optional[str]

The multiplexed WebSocket stream that emitted the event. This field is
present only when WebSocket multiplexing is enabled separately.

class BetaResponseInjectEvent: …

Injects input items into an active response over a WebSocket connection.
The items are validated and committed atomically. Currently, the server
accepts client-owned tool outputs that resume a waiting agent.

input: List[[BetaResponseInputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_item%20%3E%20(schema))]

Input items to inject into the active response.

class BetaEasyInputMessage: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: Union[str, [BetaResponseInputMessageContentList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema))]

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

str

List[[BetaResponseInputContent](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_content%20%3E%20(schema))]

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

role: Literal["user", "assistant", "system", "developer"]

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

"user"

"assistant"

"system"

"developer"

phase: Optional[Literal["commentary", "final\_answer"]]

"commentary"

"final\_answer"

type: Optional[Literal["message"]]

The type of the message input. Always `message`.

class Message: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role.

content: [BetaResponseInputMessageContentList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema))

role: Literal["user", "system", "developer"]

"user"

"system"

"developer"

agent: Optional[MessageAgent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

type: Optional[Literal["message"]]

class BetaResponseOutputMessage: …

id: str

content: List[Content]

class BetaResponseOutputText: …

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

logprobs: Optional[List[Logprob]]

token: str

bytes: List[int]

logprob: float

top\_logprobs: List[LogprobTopLogprob]

token: str

bytes: List[int]

logprob: float

class BetaResponseOutputRefusal: …

refusal: str

type: Literal["refusal"]

role: Literal["assistant"]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["message"]

agent: Optional[Agent]

agent\_name: str

phase: Optional[Literal["commentary", "final\_answer"]]

"commentary"

"final\_answer"

class BetaResponseFileSearchToolCall: …

[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

id: str

queries: List[str]

status: Literal["in\_progress", "searching", "completed", 2 more]

"in\_progress"

"searching"

"completed"

"incomplete"

"failed"

type: Literal["file\_search\_call"]

agent: Optional[Agent]

agent\_name: str

results: Optional[List[Result]]

attributes: Optional[Dict[str, Union[str, float, bool]]]

str

float

bool

file\_id: Optional[str]

filename: Optional[str]

score: Optional[float]

formatfloat

text: Optional[str]

class BetaResponseComputerToolCall: …

[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

id: str

call\_id: str

pending\_safety\_checks: List[PendingSafetyCheck]

id: str

code: Optional[str]

message: Optional[str]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["computer\_call"]

action: Optional[BetaComputerAction]

actions: Optional[BetaComputerActionList]

agent: Optional[Agent]

agent\_name: str

class ComputerCallOutput: …

The output of a computer tool call.

call\_id: str

maxLength64

minLength1

output: [BetaResponseComputerToolCallOutputScreenshot](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema))

type: Literal["computer\_call\_output"]

id: Optional[str]

The ID of the computer tool call output.

acknowledged\_safety\_checks: Optional[List[ComputerCallOutputAcknowledgedSafetyCheck]]

The safety checks reported by the API that have been acknowledged by the developer.

id: str

code: Optional[str]

message: Optional[str]

agent: Optional[ComputerCallOutputAgent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the message input. One of `in_progress`, `completed`, or `incomplete`. Populated when input items are returned via API.

"in\_progress"

"completed"

"incomplete"

class BetaResponseFunctionWebSearch: …

[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

id: str

action: Action

class ActionSearch: …

type: Literal["search"]

queries: Optional[List[str]]

Deprecatedquery: Optional[str]

sources: Optional[List[ActionSearchSource]]

type: Literal["url"]

url: str

class ActionOpenPage: …

type: Literal["open\_page"]

url: Optional[str]

class ActionFindInPage: …

pattern: str

type: Literal["find\_in\_page"]

url: str

status: Literal["in\_progress", "searching", "completed", "failed"]

"in\_progress"

"searching"

"completed"

"failed"

type: Literal["web\_search\_call"]

agent: Optional[Agent]

agent\_name: str

class BetaResponseFunctionToolCall: …

[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

arguments: str

A JSON string of the arguments to pass to the function.

call\_id: str

name: str

The name of the function to run.

type: Literal["function\_call"]

The type of the function tool call. Always `function_call`.

id: Optional[str]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

namespace: Optional[str]

The namespace of the function to run.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class FunctionCallOutput: …

The output of a function tool call.

call\_id: str

maxLength64

minLength1

output: Union[str, [BetaResponseFunctionCallOutputItemList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item_list%20%3E%20(schema))]

Text, image, or file output of the function tool call.

str

A JSON string of the output of the function tool call.

List[[BetaResponseFunctionCallOutputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item%20%3E%20(schema))]

class BetaResponseInputTextContent: …

text: str

maxLength10485760

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImageContent: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

type: Literal["input\_image"]

detail: Optional[Literal["low", "high", "auto", "original"]]

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

image\_url: Optional[str]

maxLength20971520

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFileContent: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

The base64-encoded data of the file to be sent to the model.

maxLength73400320

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

type: Literal["function\_call\_output"]

id: Optional[str]

The unique ID of the function tool call output. Populated when this item is returned via API.

agent: Optional[FunctionCallOutputAgent]

agent\_name: str

caller: Optional[FunctionCallOutputCaller]

class FunctionCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class FunctionCallOutputCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

class AgentMessage: …

A message routed between agents.

author: str

content: List[AgentMessageContent]

Plaintext, image, or encrypted content sent between agents.

class BetaResponseInputTextContent: …

text: str

maxLength10485760

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImageContent: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

type: Literal["input\_image"]

detail: Optional[Literal["low", "high", "auto", "original"]]

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

image\_url: Optional[str]

maxLength20971520

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class AgentMessageContentEncryptedContent: …

encrypted\_content: str

maxLength10485760

type: Literal["encrypted\_content"]

recipient: str

type: Literal["agent\_message"]

The item type. Always `agent_message`.

id: Optional[str]

The unique ID of this agent message item.

agent: Optional[AgentMessageAgent]

agent\_name: str

class MultiAgentCall: …

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

The multi-agent action that was executed.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

arguments: str

The action arguments as a JSON string.

call\_id: str

maxLength64

minLength1

type: Literal["multi\_agent\_call"]

The item type. Always `multi_agent_call`.

id: Optional[str]

The unique ID of this multi-agent call.

agent: Optional[MultiAgentCallAgent]

agent\_name: str

class MultiAgentCallOutput: …

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

call\_id: str

maxLength64

minLength1

output: List[MultiAgentCallOutputOutput]

text: str

The text content.

maxLength10485760

type: Literal["output\_text"]

The content type. Always `output_text`.

annotations: Optional[List[MultiAgentCallOutputOutputAnnotation]]

Citations associated with the text content.

class MultiAgentCallOutputOutputAnnotationFileCitation: …

file\_id: str

filename: str

index: int

minimum0

type: Literal["file\_citation"]

The citation type. Always `file_citation`.

class MultiAgentCallOutputOutputAnnotationURLCitation: …

end\_index: int

The index of the last character of the citation in the message.

minimum0

start\_index: int

The index of the first character of the citation in the message.

minimum0

title: str

The title of the cited resource.

type: Literal["url\_citation"]

The citation type. Always `url_citation`.

url: str

The URL of the cited resource.

class MultiAgentCallOutputOutputAnnotationContainerFileCitation: …

container\_id: str

The ID of the container.

end\_index: int

The index of the last character of the citation in the message.

minimum0

file\_id: str

filename: str

start\_index: int

The index of the first character of the citation in the message.

minimum0

type: Literal["container\_file\_citation"]

The citation type. Always `container_file_citation`.

type: Literal["multi\_agent\_call\_output"]

The item type. Always `multi_agent_call_output`.

id: Optional[str]

The unique ID of this multi-agent call output.

agent: Optional[MultiAgentCallOutputAgent]

agent\_name: str

class ToolSearchCall: …

arguments: object

The arguments supplied to the tool search call.

type: Literal["tool\_search\_call"]

The item type. Always `tool_search_call`.

id: Optional[str]

The unique ID of this tool search call.

agent: Optional[ToolSearchCallAgent]

agent\_name: str

call\_id: Optional[str]

maxLength64

minLength1

execution: Optional[Literal["server", "client"]]

"server"

"client"

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the tool search call.

"in\_progress"

"completed"

"incomplete"

class BetaResponseToolSearchOutputItemParam: …

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

The loaded tool definitions returned by the tool search output.

class BetaFunctionTool: …

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

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

input\_fidelity: Optional[Literal["high", "low"]]

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

type: Literal["tool\_search\_output"]

The item type. Always `tool_search_output`.

id: Optional[str]

The unique ID of this tool search output.

agent: Optional[Agent]

agent\_name: str

call\_id: Optional[str]

maxLength64

minLength1

execution: Optional[Literal["server", "client"]]

"server"

"client"

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the tool search output.

"in\_progress"

"completed"

"incomplete"

class AdditionalTools: …

role: Literal["developer"]

The role that provided the additional tools. Only `developer` is supported.

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

A list of additional tools made available at this item.

class BetaFunctionTool: …

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

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

input\_fidelity: Optional[Literal["high", "low"]]

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

type: Literal["additional\_tools"]

The item type. Always `additional_tools`.

id: Optional[str]

The unique ID of this additional tools item.

agent: Optional[AdditionalToolsAgent]

agent\_name: str

class BetaResponseReasoningItem: …

[managing context](https://platform.openai.com/docs/guides/conversation-state).

id: str

summary: List[Summary]

text: str

type: Literal["summary\_text"]

type: Literal["reasoning"]

agent: Optional[Agent]

agent\_name: str

content: Optional[List[Content]]

text: str

type: Literal["reasoning\_text"]

encrypted\_content: Optional[str]

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class BetaResponseCompactionItemParam: …

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

encrypted\_content: str

The encrypted content of the compaction summary.

maxLength10485760

type: Literal["compaction"]

id: Optional[str]

The ID of the compaction item.

agent: Optional[Agent]

agent\_name: str

class ImageGenerationCall: …

An image generation request made by the model.

id: str

result: Optional[str]

status: Literal["in\_progress", "completed", "generating", "failed"]

"in\_progress"

"completed"

"generating"

"failed"

type: Literal["image\_generation\_call"]

agent: Optional[ImageGenerationCallAgent]

agent\_name: str

class BetaResponseCodeInterpreterToolCall: …

id: str

code: Optional[str]

container\_id: str

outputs: Optional[List[Output]]

class OutputLogs: …

logs: str

type: Literal["logs"]

class OutputImage: …

type: Literal["image"]

url: str

status: Literal["in\_progress", "completed", "incomplete", 2 more]

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: Literal["code\_interpreter\_call"]

agent: Optional[Agent]

agent\_name: str

class LocalShellCall: …

A tool call to run a command on the local shell.

id: str

action: LocalShellCallAction

command: List[str]

env: Dict[str, str]

type: Literal["exec"]

timeout\_ms: Optional[int]

user: Optional[str]

working\_directory: Optional[str]

call\_id: str

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["local\_shell\_call"]

agent: Optional[LocalShellCallAgent]

agent\_name: str

class LocalShellCallOutput: …

The output of a local shell tool call.

id: str

output: str

type: Literal["local\_shell\_call\_output"]

agent: Optional[LocalShellCallOutputAgent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class ShellCall: …

A tool representing a request to execute one or more shell commands.

action: ShellCallAction

commands: List[str]

Ordered shell commands for the execution environment to run.

max\_output\_length: Optional[int]

Maximum number of UTF-8 characters to capture from combined stdout and stderr output.

timeout\_ms: Optional[int]

Maximum wall-clock time in milliseconds to allow the shell commands to run.

call\_id: str

maxLength64

minLength1

type: Literal["shell\_call"]

id: Optional[str]

agent: Optional[ShellCallAgent]

agent\_name: str

caller: Optional[ShellCallCaller]

class ShellCallCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ShellCallCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

environment: Optional[ShellCallEnvironment]

The environment to execute the shell commands in.

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class ShellCallOutput: …

The streamed output items emitted by a shell tool call.

call\_id: str

maxLength64

minLength1

output: List[[BetaResponseFunctionShellCallOutputContent](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_shell_call_output_content%20%3E%20(schema))]

Captured chunks of stdout and stderr output, along with their associated outcomes.

outcome: Outcome

The exit or timeout outcome associated with this shell call.

class OutcomeTimeout: …

Indicates that the shell call exceeded its configured time limit.

type: Literal["timeout"]

The outcome type. Always `timeout`.

class OutcomeExit: …

exit\_code: int

The exit code returned by the shell process.

type: Literal["exit"]

stderr: str

Captured stderr output for the shell call.

maxLength10485760

stdout: str

Captured stdout output for the shell call.

maxLength10485760

type: Literal["shell\_call\_output"]

The type of the item. Always `shell_call_output`.

id: Optional[str]

The unique ID of the shell tool call output. Populated when this item is returned via API.

agent: Optional[ShellCallOutputAgent]

agent\_name: str

caller: Optional[ShellCallOutputCaller]

class ShellCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ShellCallOutputCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

max\_output\_length: Optional[int]

The maximum number of UTF-8 characters captured for this shell call’s combined output.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the shell call output.

"in\_progress"

"completed"

"incomplete"

class ApplyPatchCall: …

A tool call representing a request to create, delete, or update files using diff patches.

call\_id: str

maxLength64

minLength1

operation: ApplyPatchCallOperation

The specific create, delete, or update instruction for the apply\_patch tool call.

class ApplyPatchCallOperationCreateFile: …

Instruction for creating a new file via the apply\_patch tool.

diff: str

Unified diff content to apply when creating the file.

maxLength10485760

path: str

Path of the file to create relative to the workspace root.

minLength1

type: Literal["create\_file"]

The operation type. Always `create_file`.

class ApplyPatchCallOperationDeleteFile: …

Instruction for deleting an existing file via the apply\_patch tool.

path: str

Path of the file to delete relative to the workspace root.

minLength1

type: Literal["delete\_file"]

The operation type. Always `delete_file`.

class ApplyPatchCallOperationUpdateFile: …

Instruction for updating an existing file via the apply\_patch tool.

diff: str

Unified diff content to apply to the existing file.

maxLength10485760

path: str

Path of the file to update relative to the workspace root.

minLength1

type: Literal["update\_file"]

The operation type. Always `update_file`.

status: Literal["in\_progress", "completed"]

"in\_progress"

"completed"

type: Literal["apply\_patch\_call"]

id: Optional[str]

agent: Optional[ApplyPatchCallAgent]

agent\_name: str

caller: Optional[ApplyPatchCallCaller]

class ApplyPatchCallCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ApplyPatchCallCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

class ApplyPatchCallOutput: …

The streamed output emitted by an apply patch tool call.

call\_id: str

maxLength64

minLength1

status: Literal["completed", "failed"]

"completed"

"failed"

type: Literal["apply\_patch\_call\_output"]

id: Optional[str]

agent: Optional[ApplyPatchCallOutputAgent]

agent\_name: str

caller: Optional[ApplyPatchCallOutputCaller]

class ApplyPatchCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ApplyPatchCallOutputCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

output: Optional[str]

Optional human-readable log text from the apply patch tool (e.g., patch results or errors).

maxLength10485760

class McpListTools: …

A list of tools available on an MCP server.

id: str

server\_label: str

tools: List[McpListToolsTool]

input\_schema: object

name: str

annotations: Optional[object]

description: Optional[str]

type: Literal["mcp\_list\_tools"]

agent: Optional[McpListToolsAgent]

agent\_name: str

error: Optional[str]

class McpApprovalRequest: …

A request for human approval of a tool invocation.

id: str

arguments: str

name: str

server\_label: str

type: Literal["mcp\_approval\_request"]

agent: Optional[McpApprovalRequestAgent]

agent\_name: str

class McpApprovalResponse: …

A response to an MCP approval request.

approval\_request\_id: str

approve: bool

type: Literal["mcp\_approval\_response"]

id: Optional[str]

agent: Optional[McpApprovalResponseAgent]

agent\_name: str

reason: Optional[str]

class McpCall: …

An invocation of a tool on an MCP server.

id: str

arguments: str

name: str

server\_label: str

type: Literal["mcp\_call"]

agent: Optional[McpCallAgent]

agent\_name: str

approval\_request\_id: Optional[str]

error: Optional[str]

output: Optional[str]

status: Optional[Literal["in\_progress", "completed", "incomplete", 2 more]]

"in\_progress"

"completed"

"incomplete"

"calling"

"failed"

class BetaResponseCustomToolCallOutput: …

call\_id: str

The call ID, used to map this custom tool call output to a custom tool call.

output: Union[str, List[OutputOutputContentList]]

The output from the custom tool call generated by your code.

str

A string of the output of the custom tool call.

List[OutputOutputContentList]

Text, image, or file output of the custom tool call.

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

type: Literal["custom\_tool\_call\_output"]

The type of the custom tool call output. Always `custom_tool_call_output`.

id: Optional[str]

The unique ID of the custom tool call output in the OpenAI platform.

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class CallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

class BetaResponseCustomToolCall: …

call\_id: str

An identifier used to map this custom tool call to a tool call output.

input: str

The input for the custom tool call generated by the model.

name: str

The name of the custom tool being called.

type: Literal["custom\_tool\_call"]

The type of the custom tool call. Always `custom_tool_call`.

id: Optional[str]

The unique ID of the custom tool call in the OpenAI platform.

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

namespace: Optional[str]

The namespace of the custom tool being called.

class CompactionTrigger: …

Compacts the current context. Must be the final input item.

type: Literal["compaction\_trigger"]

The type of the item. Always `compaction_trigger`.

agent: Optional[CompactionTriggerAgent]

agent\_name: str

class ItemReference: …

An internal identifier for an item to reference.

id: str

The ID of the item to reference.

agent: Optional[ItemReferenceAgent]

agent\_name: str

type: Optional[Literal["item\_reference"]]

The type of item to reference. Always `item_reference`.

class Program: …

id: str

The unique ID of this program item.

call\_id: str

maxLength64

minLength1

code: str

maxLength10485760

fingerprint: str

maxLength10485760

type: Literal["program"]

The item type. Always `program`.

agent: Optional[ProgramAgent]

agent\_name: str

class ProgramOutput: …

id: str

The unique ID of this program output item.

call\_id: str

maxLength64

minLength1

result: str

maxLength10485760

status: Literal["completed", "incomplete"]

The terminal status of the program output.

"completed"

"incomplete"

type: Literal["program\_output"]

The item type. Always `program_output`.

agent: Optional[ProgramOutputAgent]

agent\_name: str

response\_id: str

The ID of the active response that should receive the input.

type: Literal["response.inject"]

The event discriminator. Always `response.inject`.

class BetaResponseInjectFailedEvent: …

Emitted when injected input could not be committed to a response. The event
returns the uncommitted raw input so the client can retry it in another
response when appropriate.

error: Error

Information about why the input was not committed.

code: Literal["response\_already\_completed", "response\_not\_found"]

A machine-readable error code.

"response\_already\_completed"

"response\_not\_found"

message: str

A human-readable description of the error.

input: List[[BetaResponseInputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_item%20%3E%20(schema))]

The raw input items that were not committed.

class BetaEasyInputMessage: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: Union[str, [BetaResponseInputMessageContentList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema))]

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

str

List[[BetaResponseInputContent](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_content%20%3E%20(schema))]

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

role: Literal["user", "assistant", "system", "developer"]

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

"user"

"assistant"

"system"

"developer"

phase: Optional[Literal["commentary", "final\_answer"]]

"commentary"

"final\_answer"

type: Optional[Literal["message"]]

The type of the message input. Always `message`.

class Message: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role.

content: [BetaResponseInputMessageContentList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema))

role: Literal["user", "system", "developer"]

"user"

"system"

"developer"

agent: Optional[MessageAgent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

type: Optional[Literal["message"]]

class BetaResponseOutputMessage: …

id: str

content: List[Content]

class BetaResponseOutputText: …

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

logprobs: Optional[List[Logprob]]

token: str

bytes: List[int]

logprob: float

top\_logprobs: List[LogprobTopLogprob]

token: str

bytes: List[int]

logprob: float

class BetaResponseOutputRefusal: …

refusal: str

type: Literal["refusal"]

role: Literal["assistant"]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["message"]

agent: Optional[Agent]

agent\_name: str

phase: Optional[Literal["commentary", "final\_answer"]]

"commentary"

"final\_answer"

class BetaResponseFileSearchToolCall: …

[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

id: str

queries: List[str]

status: Literal["in\_progress", "searching", "completed", 2 more]

"in\_progress"

"searching"

"completed"

"incomplete"

"failed"

type: Literal["file\_search\_call"]

agent: Optional[Agent]

agent\_name: str

results: Optional[List[Result]]

attributes: Optional[Dict[str, Union[str, float, bool]]]

str

float

bool

file\_id: Optional[str]

filename: Optional[str]

score: Optional[float]

formatfloat

text: Optional[str]

class BetaResponseComputerToolCall: …

[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

id: str

call\_id: str

pending\_safety\_checks: List[PendingSafetyCheck]

id: str

code: Optional[str]

message: Optional[str]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["computer\_call"]

action: Optional[BetaComputerAction]

actions: Optional[BetaComputerActionList]

agent: Optional[Agent]

agent\_name: str

class ComputerCallOutput: …

The output of a computer tool call.

call\_id: str

maxLength64

minLength1

output: [BetaResponseComputerToolCallOutputScreenshot](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema))

type: Literal["computer\_call\_output"]

id: Optional[str]

The ID of the computer tool call output.

acknowledged\_safety\_checks: Optional[List[ComputerCallOutputAcknowledgedSafetyCheck]]

The safety checks reported by the API that have been acknowledged by the developer.

id: str

code: Optional[str]

message: Optional[str]

agent: Optional[ComputerCallOutputAgent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the message input. One of `in_progress`, `completed`, or `incomplete`. Populated when input items are returned via API.

"in\_progress"

"completed"

"incomplete"

class BetaResponseFunctionWebSearch: …

[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

id: str

action: Action

class ActionSearch: …

type: Literal["search"]

queries: Optional[List[str]]

Deprecatedquery: Optional[str]

sources: Optional[List[ActionSearchSource]]

type: Literal["url"]

url: str

class ActionOpenPage: …

type: Literal["open\_page"]

url: Optional[str]

class ActionFindInPage: …

pattern: str

type: Literal["find\_in\_page"]

url: str

status: Literal["in\_progress", "searching", "completed", "failed"]

"in\_progress"

"searching"

"completed"

"failed"

type: Literal["web\_search\_call"]

agent: Optional[Agent]

agent\_name: str

class BetaResponseFunctionToolCall: …

[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

arguments: str

A JSON string of the arguments to pass to the function.

call\_id: str

name: str

The name of the function to run.

type: Literal["function\_call"]

The type of the function tool call. Always `function_call`.

id: Optional[str]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

namespace: Optional[str]

The namespace of the function to run.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class FunctionCallOutput: …

The output of a function tool call.

call\_id: str

maxLength64

minLength1

output: Union[str, [BetaResponseFunctionCallOutputItemList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item_list%20%3E%20(schema))]

Text, image, or file output of the function tool call.

str

A JSON string of the output of the function tool call.

List[[BetaResponseFunctionCallOutputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item%20%3E%20(schema))]

class BetaResponseInputTextContent: …

text: str

maxLength10485760

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImageContent: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

type: Literal["input\_image"]

detail: Optional[Literal["low", "high", "auto", "original"]]

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

image\_url: Optional[str]

maxLength20971520

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFileContent: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

The base64-encoded data of the file to be sent to the model.

maxLength73400320

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

type: Literal["function\_call\_output"]

id: Optional[str]

The unique ID of the function tool call output. Populated when this item is returned via API.

agent: Optional[FunctionCallOutputAgent]

agent\_name: str

caller: Optional[FunctionCallOutputCaller]

class FunctionCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class FunctionCallOutputCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

class AgentMessage: …

A message routed between agents.

author: str

content: List[AgentMessageContent]

Plaintext, image, or encrypted content sent between agents.

class BetaResponseInputTextContent: …

text: str

maxLength10485760

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImageContent: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

type: Literal["input\_image"]

detail: Optional[Literal["low", "high", "auto", "original"]]

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

image\_url: Optional[str]

maxLength20971520

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class AgentMessageContentEncryptedContent: …

encrypted\_content: str

maxLength10485760

type: Literal["encrypted\_content"]

recipient: str

type: Literal["agent\_message"]

The item type. Always `agent_message`.

id: Optional[str]

The unique ID of this agent message item.

agent: Optional[AgentMessageAgent]

agent\_name: str

class MultiAgentCall: …

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

The multi-agent action that was executed.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

arguments: str

The action arguments as a JSON string.

call\_id: str

maxLength64

minLength1

type: Literal["multi\_agent\_call"]

The item type. Always `multi_agent_call`.

id: Optional[str]

The unique ID of this multi-agent call.

agent: Optional[MultiAgentCallAgent]

agent\_name: str

class MultiAgentCallOutput: …

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

call\_id: str

maxLength64

minLength1

output: List[MultiAgentCallOutputOutput]

text: str

The text content.

maxLength10485760

type: Literal["output\_text"]

The content type. Always `output_text`.

annotations: Optional[List[MultiAgentCallOutputOutputAnnotation]]

Citations associated with the text content.

class MultiAgentCallOutputOutputAnnotationFileCitation: …

file\_id: str

filename: str

index: int

minimum0

type: Literal["file\_citation"]

The citation type. Always `file_citation`.

class MultiAgentCallOutputOutputAnnotationURLCitation: …

end\_index: int

The index of the last character of the citation in the message.

minimum0

start\_index: int

The index of the first character of the citation in the message.

minimum0

title: str

The title of the cited resource.

type: Literal["url\_citation"]

The citation type. Always `url_citation`.

url: str

The URL of the cited resource.

class MultiAgentCallOutputOutputAnnotationContainerFileCitation: …

container\_id: str

The ID of the container.

end\_index: int

The index of the last character of the citation in the message.

minimum0

file\_id: str

filename: str

start\_index: int

The index of the first character of the citation in the message.

minimum0

type: Literal["container\_file\_citation"]

The citation type. Always `container_file_citation`.

type: Literal["multi\_agent\_call\_output"]

The item type. Always `multi_agent_call_output`.

id: Optional[str]

The unique ID of this multi-agent call output.

agent: Optional[MultiAgentCallOutputAgent]

agent\_name: str

class ToolSearchCall: …

arguments: object

The arguments supplied to the tool search call.

type: Literal["tool\_search\_call"]

The item type. Always `tool_search_call`.

id: Optional[str]

The unique ID of this tool search call.

agent: Optional[ToolSearchCallAgent]

agent\_name: str

call\_id: Optional[str]

maxLength64

minLength1

execution: Optional[Literal["server", "client"]]

"server"

"client"

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the tool search call.

"in\_progress"

"completed"

"incomplete"

class BetaResponseToolSearchOutputItemParam: …

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

The loaded tool definitions returned by the tool search output.

class BetaFunctionTool: …

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

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

input\_fidelity: Optional[Literal["high", "low"]]

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

type: Literal["tool\_search\_output"]

The item type. Always `tool_search_output`.

id: Optional[str]

The unique ID of this tool search output.

agent: Optional[Agent]

agent\_name: str

call\_id: Optional[str]

maxLength64

minLength1

execution: Optional[Literal["server", "client"]]

"server"

"client"

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the tool search output.

"in\_progress"

"completed"

"incomplete"

class AdditionalTools: …

role: Literal["developer"]

The role that provided the additional tools. Only `developer` is supported.

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

A list of additional tools made available at this item.

class BetaFunctionTool: …

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

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

input\_fidelity: Optional[Literal["high", "low"]]

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

type: Literal["additional\_tools"]

The item type. Always `additional_tools`.

id: Optional[str]

The unique ID of this additional tools item.

agent: Optional[AdditionalToolsAgent]

agent\_name: str

class BetaResponseReasoningItem: …

[managing context](https://platform.openai.com/docs/guides/conversation-state).

id: str

summary: List[Summary]

text: str

type: Literal["summary\_text"]

type: Literal["reasoning"]

agent: Optional[Agent]

agent\_name: str

content: Optional[List[Content]]

text: str

type: Literal["reasoning\_text"]

encrypted\_content: Optional[str]

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class BetaResponseCompactionItemParam: …

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

encrypted\_content: str

The encrypted content of the compaction summary.

maxLength10485760

type: Literal["compaction"]

id: Optional[str]

The ID of the compaction item.

agent: Optional[Agent]

agent\_name: str

class ImageGenerationCall: …

An image generation request made by the model.

id: str

result: Optional[str]

status: Literal["in\_progress", "completed", "generating", "failed"]

"in\_progress"

"completed"

"generating"

"failed"

type: Literal["image\_generation\_call"]

agent: Optional[ImageGenerationCallAgent]

agent\_name: str

class BetaResponseCodeInterpreterToolCall: …

id: str

code: Optional[str]

container\_id: str

outputs: Optional[List[Output]]

class OutputLogs: …

logs: str

type: Literal["logs"]

class OutputImage: …

type: Literal["image"]

url: str

status: Literal["in\_progress", "completed", "incomplete", 2 more]

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: Literal["code\_interpreter\_call"]

agent: Optional[Agent]

agent\_name: str

class LocalShellCall: …

A tool call to run a command on the local shell.

id: str

action: LocalShellCallAction

command: List[str]

env: Dict[str, str]

type: Literal["exec"]

timeout\_ms: Optional[int]

user: Optional[str]

working\_directory: Optional[str]

call\_id: str

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["local\_shell\_call"]

agent: Optional[LocalShellCallAgent]

agent\_name: str

class LocalShellCallOutput: …

The output of a local shell tool call.

id: str

output: str

type: Literal["local\_shell\_call\_output"]

agent: Optional[LocalShellCallOutputAgent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class ShellCall: …

A tool representing a request to execute one or more shell commands.

action: ShellCallAction

commands: List[str]

Ordered shell commands for the execution environment to run.

max\_output\_length: Optional[int]

Maximum number of UTF-8 characters to capture from combined stdout and stderr output.

timeout\_ms: Optional[int]

Maximum wall-clock time in milliseconds to allow the shell commands to run.

call\_id: str

maxLength64

minLength1

type: Literal["shell\_call"]

id: Optional[str]

agent: Optional[ShellCallAgent]

agent\_name: str

caller: Optional[ShellCallCaller]

class ShellCallCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ShellCallCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

environment: Optional[ShellCallEnvironment]

The environment to execute the shell commands in.

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class ShellCallOutput: …

The streamed output items emitted by a shell tool call.

call\_id: str

maxLength64

minLength1

output: List[[BetaResponseFunctionShellCallOutputContent](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_shell_call_output_content%20%3E%20(schema))]

Captured chunks of stdout and stderr output, along with their associated outcomes.

outcome: Outcome

The exit or timeout outcome associated with this shell call.

class OutcomeTimeout: …

Indicates that the shell call exceeded its configured time limit.

type: Literal["timeout"]

The outcome type. Always `timeout`.

class OutcomeExit: …

exit\_code: int

The exit code returned by the shell process.

type: Literal["exit"]

stderr: str

Captured stderr output for the shell call.

maxLength10485760

stdout: str

Captured stdout output for the shell call.

maxLength10485760

type: Literal["shell\_call\_output"]

The type of the item. Always `shell_call_output`.

id: Optional[str]

The unique ID of the shell tool call output. Populated when this item is returned via API.

agent: Optional[ShellCallOutputAgent]

agent\_name: str

caller: Optional[ShellCallOutputCaller]

class ShellCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ShellCallOutputCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

max\_output\_length: Optional[int]

The maximum number of UTF-8 characters captured for this shell call’s combined output.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the shell call output.

"in\_progress"

"completed"

"incomplete"

class ApplyPatchCall: …

A tool call representing a request to create, delete, or update files using diff patches.

call\_id: str

maxLength64

minLength1

operation: ApplyPatchCallOperation

The specific create, delete, or update instruction for the apply\_patch tool call.

class ApplyPatchCallOperationCreateFile: …

Instruction for creating a new file via the apply\_patch tool.

diff: str

Unified diff content to apply when creating the file.

maxLength10485760

path: str

Path of the file to create relative to the workspace root.

minLength1

type: Literal["create\_file"]

The operation type. Always `create_file`.

class ApplyPatchCallOperationDeleteFile: …

Instruction for deleting an existing file via the apply\_patch tool.

path: str

Path of the file to delete relative to the workspace root.

minLength1

type: Literal["delete\_file"]

The operation type. Always `delete_file`.

class ApplyPatchCallOperationUpdateFile: …

Instruction for updating an existing file via the apply\_patch tool.

diff: str

Unified diff content to apply to the existing file.

maxLength10485760

path: str

Path of the file to update relative to the workspace root.

minLength1

type: Literal["update\_file"]

The operation type. Always `update_file`.

status: Literal["in\_progress", "completed"]

"in\_progress"

"completed"

type: Literal["apply\_patch\_call"]

id: Optional[str]

agent: Optional[ApplyPatchCallAgent]

agent\_name: str

caller: Optional[ApplyPatchCallCaller]

class ApplyPatchCallCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ApplyPatchCallCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

class ApplyPatchCallOutput: …

The streamed output emitted by an apply patch tool call.

call\_id: str

maxLength64

minLength1

status: Literal["completed", "failed"]

"completed"

"failed"

type: Literal["apply\_patch\_call\_output"]

id: Optional[str]

agent: Optional[ApplyPatchCallOutputAgent]

agent\_name: str

caller: Optional[ApplyPatchCallOutputCaller]

class ApplyPatchCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ApplyPatchCallOutputCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

output: Optional[str]

Optional human-readable log text from the apply patch tool (e.g., patch results or errors).

maxLength10485760

class McpListTools: …

A list of tools available on an MCP server.

id: str

server\_label: str

tools: List[McpListToolsTool]

input\_schema: object

name: str

annotations: Optional[object]

description: Optional[str]

type: Literal["mcp\_list\_tools"]

agent: Optional[McpListToolsAgent]

agent\_name: str

error: Optional[str]

class McpApprovalRequest: …

A request for human approval of a tool invocation.

id: str

arguments: str

name: str

server\_label: str

type: Literal["mcp\_approval\_request"]

agent: Optional[McpApprovalRequestAgent]

agent\_name: str

class McpApprovalResponse: …

A response to an MCP approval request.

approval\_request\_id: str

approve: bool

type: Literal["mcp\_approval\_response"]

id: Optional[str]

agent: Optional[McpApprovalResponseAgent]

agent\_name: str

reason: Optional[str]

class McpCall: …

An invocation of a tool on an MCP server.

id: str

arguments: str

name: str

server\_label: str

type: Literal["mcp\_call"]

agent: Optional[McpCallAgent]

agent\_name: str

approval\_request\_id: Optional[str]

error: Optional[str]

output: Optional[str]

status: Optional[Literal["in\_progress", "completed", "incomplete", 2 more]]

"in\_progress"

"completed"

"incomplete"

"calling"

"failed"

class BetaResponseCustomToolCallOutput: …

call\_id: str

The call ID, used to map this custom tool call output to a custom tool call.

output: Union[str, List[OutputOutputContentList]]

The output from the custom tool call generated by your code.

str

A string of the output of the custom tool call.

List[OutputOutputContentList]

Text, image, or file output of the custom tool call.

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

type: Literal["custom\_tool\_call\_output"]

The type of the custom tool call output. Always `custom_tool_call_output`.

id: Optional[str]

The unique ID of the custom tool call output in the OpenAI platform.

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class CallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

class BetaResponseCustomToolCall: …

call\_id: str

An identifier used to map this custom tool call to a tool call output.

input: str

The input for the custom tool call generated by the model.

name: str

The name of the custom tool being called.

type: Literal["custom\_tool\_call"]

The type of the custom tool call. Always `custom_tool_call`.

id: Optional[str]

The unique ID of the custom tool call in the OpenAI platform.

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

namespace: Optional[str]

The namespace of the custom tool being called.

class CompactionTrigger: …

Compacts the current context. Must be the final input item.

type: Literal["compaction\_trigger"]

The type of the item. Always `compaction_trigger`.

agent: Optional[CompactionTriggerAgent]

agent\_name: str

class ItemReference: …

An internal identifier for an item to reference.

id: str

The ID of the item to reference.

agent: Optional[ItemReferenceAgent]

agent\_name: str

type: Optional[Literal["item\_reference"]]

The type of item to reference. Always `item_reference`.

class Program: …

id: str

The unique ID of this program item.

call\_id: str

maxLength64

minLength1

code: str

maxLength10485760

fingerprint: str

maxLength10485760

type: Literal["program"]

The item type. Always `program`.

agent: Optional[ProgramAgent]

agent\_name: str

class ProgramOutput: …

id: str

The unique ID of this program output item.

call\_id: str

maxLength64

minLength1

result: str

maxLength10485760

status: Literal["completed", "incomplete"]

The terminal status of the program output.

"completed"

"incomplete"

type: Literal["program\_output"]

The item type. Always `program_output`.

agent: Optional[ProgramOutputAgent]

agent\_name: str

response\_id: str

The ID of the response that rejected the input.

sequence\_number: int

The sequence number for this event.

type: Literal["response.inject.failed"]

The event discriminator. Always `response.inject.failed`.

stream\_id: Optional[str]

The multiplexed WebSocket stream that emitted the event. This field is
present only when WebSocket multiplexing is enabled separately.

List[[BetaResponseInputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_item%20%3E%20(schema))]

A list of one or many input items to the model, containing
different content types.

class BetaEasyInputMessage: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: Union[str, [BetaResponseInputMessageContentList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema))]

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

str

List[[BetaResponseInputContent](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_content%20%3E%20(schema))]

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

role: Literal["user", "assistant", "system", "developer"]

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

"user"

"assistant"

"system"

"developer"

phase: Optional[Literal["commentary", "final\_answer"]]

"commentary"

"final\_answer"

type: Optional[Literal["message"]]

The type of the message input. Always `message`.

class Message: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role.

content: [BetaResponseInputMessageContentList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema))

role: Literal["user", "system", "developer"]

"user"

"system"

"developer"

agent: Optional[MessageAgent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

type: Optional[Literal["message"]]

class BetaResponseOutputMessage: …

id: str

content: List[Content]

class BetaResponseOutputText: …

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

logprobs: Optional[List[Logprob]]

token: str

bytes: List[int]

logprob: float

top\_logprobs: List[LogprobTopLogprob]

token: str

bytes: List[int]

logprob: float

class BetaResponseOutputRefusal: …

refusal: str

type: Literal["refusal"]

role: Literal["assistant"]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["message"]

agent: Optional[Agent]

agent\_name: str

phase: Optional[Literal["commentary", "final\_answer"]]

"commentary"

"final\_answer"

class BetaResponseFileSearchToolCall: …

[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

id: str

queries: List[str]

status: Literal["in\_progress", "searching", "completed", 2 more]

"in\_progress"

"searching"

"completed"

"incomplete"

"failed"

type: Literal["file\_search\_call"]

agent: Optional[Agent]

agent\_name: str

results: Optional[List[Result]]

attributes: Optional[Dict[str, Union[str, float, bool]]]

str

float

bool

file\_id: Optional[str]

filename: Optional[str]

score: Optional[float]

formatfloat

text: Optional[str]

class BetaResponseComputerToolCall: …

[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

id: str

call\_id: str

pending\_safety\_checks: List[PendingSafetyCheck]

id: str

code: Optional[str]

message: Optional[str]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["computer\_call"]

action: Optional[BetaComputerAction]

actions: Optional[BetaComputerActionList]

agent: Optional[Agent]

agent\_name: str

class ComputerCallOutput: …

The output of a computer tool call.

call\_id: str

maxLength64

minLength1

output: [BetaResponseComputerToolCallOutputScreenshot](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema))

type: Literal["computer\_call\_output"]

id: Optional[str]

The ID of the computer tool call output.

acknowledged\_safety\_checks: Optional[List[ComputerCallOutputAcknowledgedSafetyCheck]]

The safety checks reported by the API that have been acknowledged by the developer.

id: str

code: Optional[str]

message: Optional[str]

agent: Optional[ComputerCallOutputAgent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the message input. One of `in_progress`, `completed`, or `incomplete`. Populated when input items are returned via API.

"in\_progress"

"completed"

"incomplete"

class BetaResponseFunctionWebSearch: …

[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

id: str

action: Action

class ActionSearch: …

type: Literal["search"]

queries: Optional[List[str]]

Deprecatedquery: Optional[str]

sources: Optional[List[ActionSearchSource]]

type: Literal["url"]

url: str

class ActionOpenPage: …

type: Literal["open\_page"]

url: Optional[str]

class ActionFindInPage: …

pattern: str

type: Literal["find\_in\_page"]

url: str

status: Literal["in\_progress", "searching", "completed", "failed"]

"in\_progress"

"searching"

"completed"

"failed"

type: Literal["web\_search\_call"]

agent: Optional[Agent]

agent\_name: str

class BetaResponseFunctionToolCall: …

[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

arguments: str

A JSON string of the arguments to pass to the function.

call\_id: str

name: str

The name of the function to run.

type: Literal["function\_call"]

The type of the function tool call. Always `function_call`.

id: Optional[str]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

namespace: Optional[str]

The namespace of the function to run.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class FunctionCallOutput: …

The output of a function tool call.

call\_id: str

maxLength64

minLength1

output: Union[str, [BetaResponseFunctionCallOutputItemList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item_list%20%3E%20(schema))]

Text, image, or file output of the function tool call.

str

A JSON string of the output of the function tool call.

List[[BetaResponseFunctionCallOutputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item%20%3E%20(schema))]

class BetaResponseInputTextContent: …

text: str

maxLength10485760

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImageContent: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

type: Literal["input\_image"]

detail: Optional[Literal["low", "high", "auto", "original"]]

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

image\_url: Optional[str]

maxLength20971520

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFileContent: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

The base64-encoded data of the file to be sent to the model.

maxLength73400320

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

type: Literal["function\_call\_output"]

id: Optional[str]

The unique ID of the function tool call output. Populated when this item is returned via API.

agent: Optional[FunctionCallOutputAgent]

agent\_name: str

caller: Optional[FunctionCallOutputCaller]

class FunctionCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class FunctionCallOutputCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

class AgentMessage: …

A message routed between agents.

author: str

content: List[AgentMessageContent]

Plaintext, image, or encrypted content sent between agents.

class BetaResponseInputTextContent: …

text: str

maxLength10485760

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImageContent: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

type: Literal["input\_image"]

detail: Optional[Literal["low", "high", "auto", "original"]]

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

image\_url: Optional[str]

maxLength20971520

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class AgentMessageContentEncryptedContent: …

encrypted\_content: str

maxLength10485760

type: Literal["encrypted\_content"]

recipient: str

type: Literal["agent\_message"]

The item type. Always `agent_message`.

id: Optional[str]

The unique ID of this agent message item.

agent: Optional[AgentMessageAgent]

agent\_name: str

class MultiAgentCall: …

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

The multi-agent action that was executed.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

arguments: str

The action arguments as a JSON string.

call\_id: str

maxLength64

minLength1

type: Literal["multi\_agent\_call"]

The item type. Always `multi_agent_call`.

id: Optional[str]

The unique ID of this multi-agent call.

agent: Optional[MultiAgentCallAgent]

agent\_name: str

class MultiAgentCallOutput: …

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

call\_id: str

maxLength64

minLength1

output: List[MultiAgentCallOutputOutput]

text: str

The text content.

maxLength10485760

type: Literal["output\_text"]

The content type. Always `output_text`.

annotations: Optional[List[MultiAgentCallOutputOutputAnnotation]]

Citations associated with the text content.

class MultiAgentCallOutputOutputAnnotationFileCitation: …

file\_id: str

filename: str

index: int

minimum0

type: Literal["file\_citation"]

The citation type. Always `file_citation`.

class MultiAgentCallOutputOutputAnnotationURLCitation: …

end\_index: int

The index of the last character of the citation in the message.

minimum0

start\_index: int

The index of the first character of the citation in the message.

minimum0

title: str

The title of the cited resource.

type: Literal["url\_citation"]

The citation type. Always `url_citation`.

url: str

The URL of the cited resource.

class MultiAgentCallOutputOutputAnnotationContainerFileCitation: …

container\_id: str

The ID of the container.

end\_index: int

The index of the last character of the citation in the message.

minimum0

file\_id: str

filename: str

start\_index: int

The index of the first character of the citation in the message.

minimum0

type: Literal["container\_file\_citation"]

The citation type. Always `container_file_citation`.

type: Literal["multi\_agent\_call\_output"]

The item type. Always `multi_agent_call_output`.

id: Optional[str]

The unique ID of this multi-agent call output.

agent: Optional[MultiAgentCallOutputAgent]

agent\_name: str

class ToolSearchCall: …

arguments: object

The arguments supplied to the tool search call.

type: Literal["tool\_search\_call"]

The item type. Always `tool_search_call`.

id: Optional[str]

The unique ID of this tool search call.

agent: Optional[ToolSearchCallAgent]

agent\_name: str

call\_id: Optional[str]

maxLength64

minLength1

execution: Optional[Literal["server", "client"]]

"server"

"client"

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the tool search call.

"in\_progress"

"completed"

"incomplete"

class BetaResponseToolSearchOutputItemParam: …

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

The loaded tool definitions returned by the tool search output.

class BetaFunctionTool: …

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

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

input\_fidelity: Optional[Literal["high", "low"]]

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

type: Literal["tool\_search\_output"]

The item type. Always `tool_search_output`.

id: Optional[str]

The unique ID of this tool search output.

agent: Optional[Agent]

agent\_name: str

call\_id: Optional[str]

maxLength64

minLength1

execution: Optional[Literal["server", "client"]]

"server"

"client"

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the tool search output.

"in\_progress"

"completed"

"incomplete"

class AdditionalTools: …

role: Literal["developer"]

The role that provided the additional tools. Only `developer` is supported.

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

A list of additional tools made available at this item.

class BetaFunctionTool: …

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

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

input\_fidelity: Optional[Literal["high", "low"]]

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

type: Literal["additional\_tools"]

The item type. Always `additional_tools`.

id: Optional[str]

The unique ID of this additional tools item.

agent: Optional[AdditionalToolsAgent]

agent\_name: str

class BetaResponseReasoningItem: …

[managing context](https://platform.openai.com/docs/guides/conversation-state).

id: str

summary: List[Summary]

text: str

type: Literal["summary\_text"]

type: Literal["reasoning"]

agent: Optional[Agent]

agent\_name: str

content: Optional[List[Content]]

text: str

type: Literal["reasoning\_text"]

encrypted\_content: Optional[str]

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class BetaResponseCompactionItemParam: …

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

encrypted\_content: str

The encrypted content of the compaction summary.

maxLength10485760

type: Literal["compaction"]

id: Optional[str]

The ID of the compaction item.

agent: Optional[Agent]

agent\_name: str

class ImageGenerationCall: …

An image generation request made by the model.

id: str

result: Optional[str]

status: Literal["in\_progress", "completed", "generating", "failed"]

"in\_progress"

"completed"

"generating"

"failed"

type: Literal["image\_generation\_call"]

agent: Optional[ImageGenerationCallAgent]

agent\_name: str

class BetaResponseCodeInterpreterToolCall: …

id: str

code: Optional[str]

container\_id: str

outputs: Optional[List[Output]]

class OutputLogs: …

logs: str

type: Literal["logs"]

class OutputImage: …

type: Literal["image"]

url: str

status: Literal["in\_progress", "completed", "incomplete", 2 more]

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: Literal["code\_interpreter\_call"]

agent: Optional[Agent]

agent\_name: str

class LocalShellCall: …

A tool call to run a command on the local shell.

id: str

action: LocalShellCallAction

command: List[str]

env: Dict[str, str]

type: Literal["exec"]

timeout\_ms: Optional[int]

user: Optional[str]

working\_directory: Optional[str]

call\_id: str

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["local\_shell\_call"]

agent: Optional[LocalShellCallAgent]

agent\_name: str

class LocalShellCallOutput: …

The output of a local shell tool call.

id: str

output: str

type: Literal["local\_shell\_call\_output"]

agent: Optional[LocalShellCallOutputAgent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class ShellCall: …

A tool representing a request to execute one or more shell commands.

action: ShellCallAction

commands: List[str]

Ordered shell commands for the execution environment to run.

max\_output\_length: Optional[int]

Maximum number of UTF-8 characters to capture from combined stdout and stderr output.

timeout\_ms: Optional[int]

Maximum wall-clock time in milliseconds to allow the shell commands to run.

call\_id: str

maxLength64

minLength1

type: Literal["shell\_call"]

id: Optional[str]

agent: Optional[ShellCallAgent]

agent\_name: str

caller: Optional[ShellCallCaller]

class ShellCallCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ShellCallCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

environment: Optional[ShellCallEnvironment]

The environment to execute the shell commands in.

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class ShellCallOutput: …

The streamed output items emitted by a shell tool call.

call\_id: str

maxLength64

minLength1

output: List[[BetaResponseFunctionShellCallOutputContent](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_shell_call_output_content%20%3E%20(schema))]

Captured chunks of stdout and stderr output, along with their associated outcomes.

outcome: Outcome

The exit or timeout outcome associated with this shell call.

class OutcomeTimeout: …

Indicates that the shell call exceeded its configured time limit.

type: Literal["timeout"]

The outcome type. Always `timeout`.

class OutcomeExit: …

exit\_code: int

The exit code returned by the shell process.

type: Literal["exit"]

stderr: str

Captured stderr output for the shell call.

maxLength10485760

stdout: str

Captured stdout output for the shell call.

maxLength10485760

type: Literal["shell\_call\_output"]

The type of the item. Always `shell_call_output`.

id: Optional[str]

The unique ID of the shell tool call output. Populated when this item is returned via API.

agent: Optional[ShellCallOutputAgent]

agent\_name: str

caller: Optional[ShellCallOutputCaller]

class ShellCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ShellCallOutputCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

max\_output\_length: Optional[int]

The maximum number of UTF-8 characters captured for this shell call’s combined output.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the shell call output.

"in\_progress"

"completed"

"incomplete"

class ApplyPatchCall: …

A tool call representing a request to create, delete, or update files using diff patches.

call\_id: str

maxLength64

minLength1

operation: ApplyPatchCallOperation

The specific create, delete, or update instruction for the apply\_patch tool call.

class ApplyPatchCallOperationCreateFile: …

Instruction for creating a new file via the apply\_patch tool.

diff: str

Unified diff content to apply when creating the file.

maxLength10485760

path: str

Path of the file to create relative to the workspace root.

minLength1

type: Literal["create\_file"]

The operation type. Always `create_file`.

class ApplyPatchCallOperationDeleteFile: …

Instruction for deleting an existing file via the apply\_patch tool.

path: str

Path of the file to delete relative to the workspace root.

minLength1

type: Literal["delete\_file"]

The operation type. Always `delete_file`.

class ApplyPatchCallOperationUpdateFile: …

Instruction for updating an existing file via the apply\_patch tool.

diff: str

Unified diff content to apply to the existing file.

maxLength10485760

path: str

Path of the file to update relative to the workspace root.

minLength1

type: Literal["update\_file"]

The operation type. Always `update_file`.

status: Literal["in\_progress", "completed"]

"in\_progress"

"completed"

type: Literal["apply\_patch\_call"]

id: Optional[str]

agent: Optional[ApplyPatchCallAgent]

agent\_name: str

caller: Optional[ApplyPatchCallCaller]

class ApplyPatchCallCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ApplyPatchCallCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

class ApplyPatchCallOutput: …

The streamed output emitted by an apply patch tool call.

call\_id: str

maxLength64

minLength1

status: Literal["completed", "failed"]

"completed"

"failed"

type: Literal["apply\_patch\_call\_output"]

id: Optional[str]

agent: Optional[ApplyPatchCallOutputAgent]

agent\_name: str

caller: Optional[ApplyPatchCallOutputCaller]

class ApplyPatchCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ApplyPatchCallOutputCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

output: Optional[str]

Optional human-readable log text from the apply patch tool (e.g., patch results or errors).

maxLength10485760

class McpListTools: …

A list of tools available on an MCP server.

id: str

server\_label: str

tools: List[McpListToolsTool]

input\_schema: object

name: str

annotations: Optional[object]

description: Optional[str]

type: Literal["mcp\_list\_tools"]

agent: Optional[McpListToolsAgent]

agent\_name: str

error: Optional[str]

class McpApprovalRequest: …

A request for human approval of a tool invocation.

id: str

arguments: str

name: str

server\_label: str

type: Literal["mcp\_approval\_request"]

agent: Optional[McpApprovalRequestAgent]

agent\_name: str

class McpApprovalResponse: …

A response to an MCP approval request.

approval\_request\_id: str

approve: bool

type: Literal["mcp\_approval\_response"]

id: Optional[str]

agent: Optional[McpApprovalResponseAgent]

agent\_name: str

reason: Optional[str]

class McpCall: …

An invocation of a tool on an MCP server.

id: str

arguments: str

name: str

server\_label: str

type: Literal["mcp\_call"]

agent: Optional[McpCallAgent]

agent\_name: str

approval\_request\_id: Optional[str]

error: Optional[str]

output: Optional[str]

status: Optional[Literal["in\_progress", "completed", "incomplete", 2 more]]

"in\_progress"

"completed"

"incomplete"

"calling"

"failed"

class BetaResponseCustomToolCallOutput: …

call\_id: str

The call ID, used to map this custom tool call output to a custom tool call.

output: Union[str, List[OutputOutputContentList]]

The output from the custom tool call generated by your code.

str

A string of the output of the custom tool call.

List[OutputOutputContentList]

Text, image, or file output of the custom tool call.

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

type: Literal["custom\_tool\_call\_output"]

The type of the custom tool call output. Always `custom_tool_call_output`.

id: Optional[str]

The unique ID of the custom tool call output in the OpenAI platform.

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class CallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

class BetaResponseCustomToolCall: …

call\_id: str

An identifier used to map this custom tool call to a tool call output.

input: str

The input for the custom tool call generated by the model.

name: str

The name of the custom tool being called.

type: Literal["custom\_tool\_call"]

The type of the custom tool call. Always `custom_tool_call`.

id: Optional[str]

The unique ID of the custom tool call in the OpenAI platform.

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

namespace: Optional[str]

The namespace of the custom tool being called.

class CompactionTrigger: …

Compacts the current context. Must be the final input item.

type: Literal["compaction\_trigger"]

The type of the item. Always `compaction_trigger`.

agent: Optional[CompactionTriggerAgent]

agent\_name: str

class ItemReference: …

An internal identifier for an item to reference.

id: str

The ID of the item to reference.

agent: Optional[ItemReferenceAgent]

agent\_name: str

type: Optional[Literal["item\_reference"]]

The type of item to reference. Always `item_reference`.

class Program: …

id: str

The unique ID of this program item.

call\_id: str

maxLength64

minLength1

code: str

maxLength10485760

fingerprint: str

maxLength10485760

type: Literal["program"]

The item type. Always `program`.

agent: Optional[ProgramAgent]

agent\_name: str

class ProgramOutput: …

id: str

The unique ID of this program output item.

call\_id: str

maxLength64

minLength1

result: str

maxLength10485760

status: Literal["completed", "incomplete"]

The terminal status of the program output.

"completed"

"incomplete"

type: Literal["program\_output"]

The item type. Always `program_output`.

agent: Optional[ProgramOutputAgent]

agent\_name: str

class BetaResponseInputAudio: …

An audio input to the model.

input\_audio: InputAudio

data: str

Base64-encoded audio data.

format: Literal["mp3", "wav"]

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

"mp3"

"wav"

type: Literal["input\_audio"]

The type of the input item. Always `input_audio`.

[BetaResponseInputContent](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_content%20%3E%20(schema))

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFileContent: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

The base64-encoded data of the file to be sent to the model.

maxLength73400320

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImageContent: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

type: Literal["input\_image"]

detail: Optional[Literal["low", "high", "auto", "original"]]

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

image\_url: Optional[str]

maxLength20971520

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

[BetaResponseInputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_item%20%3E%20(schema))

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

class BetaEasyInputMessage: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: Union[str, [BetaResponseInputMessageContentList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema))]

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

str

List[[BetaResponseInputContent](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_content%20%3E%20(schema))]

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

role: Literal["user", "assistant", "system", "developer"]

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

"user"

"assistant"

"system"

"developer"

phase: Optional[Literal["commentary", "final\_answer"]]

"commentary"

"final\_answer"

type: Optional[Literal["message"]]

The type of the message input. Always `message`.

class Message: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role.

content: [BetaResponseInputMessageContentList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema))

role: Literal["user", "system", "developer"]

"user"

"system"

"developer"

agent: Optional[MessageAgent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

type: Optional[Literal["message"]]

class BetaResponseOutputMessage: …

id: str

content: List[Content]

class BetaResponseOutputText: …

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

logprobs: Optional[List[Logprob]]

token: str

bytes: List[int]

logprob: float

top\_logprobs: List[LogprobTopLogprob]

token: str

bytes: List[int]

logprob: float

class BetaResponseOutputRefusal: …

refusal: str

type: Literal["refusal"]

role: Literal["assistant"]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["message"]

agent: Optional[Agent]

agent\_name: str

phase: Optional[Literal["commentary", "final\_answer"]]

"commentary"

"final\_answer"

class BetaResponseFileSearchToolCall: …

[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

id: str

queries: List[str]

status: Literal["in\_progress", "searching", "completed", 2 more]

"in\_progress"

"searching"

"completed"

"incomplete"

"failed"

type: Literal["file\_search\_call"]

agent: Optional[Agent]

agent\_name: str

results: Optional[List[Result]]

attributes: Optional[Dict[str, Union[str, float, bool]]]

str

float

bool

file\_id: Optional[str]

filename: Optional[str]

score: Optional[float]

formatfloat

text: Optional[str]

class BetaResponseComputerToolCall: …

[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

id: str

call\_id: str

pending\_safety\_checks: List[PendingSafetyCheck]

id: str

code: Optional[str]

message: Optional[str]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["computer\_call"]

action: Optional[BetaComputerAction]

actions: Optional[BetaComputerActionList]

agent: Optional[Agent]

agent\_name: str

class ComputerCallOutput: …

The output of a computer tool call.

call\_id: str

maxLength64

minLength1

output: [BetaResponseComputerToolCallOutputScreenshot](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema))

type: Literal["computer\_call\_output"]

id: Optional[str]

The ID of the computer tool call output.

acknowledged\_safety\_checks: Optional[List[ComputerCallOutputAcknowledgedSafetyCheck]]

The safety checks reported by the API that have been acknowledged by the developer.

id: str

code: Optional[str]

message: Optional[str]

agent: Optional[ComputerCallOutputAgent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the message input. One of `in_progress`, `completed`, or `incomplete`. Populated when input items are returned via API.

"in\_progress"

"completed"

"incomplete"

class BetaResponseFunctionWebSearch: …

[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

id: str

action: Action

class ActionSearch: …

type: Literal["search"]

queries: Optional[List[str]]

Deprecatedquery: Optional[str]

sources: Optional[List[ActionSearchSource]]

type: Literal["url"]

url: str

class ActionOpenPage: …

type: Literal["open\_page"]

url: Optional[str]

class ActionFindInPage: …

pattern: str

type: Literal["find\_in\_page"]

url: str

status: Literal["in\_progress", "searching", "completed", "failed"]

"in\_progress"

"searching"

"completed"

"failed"

type: Literal["web\_search\_call"]

agent: Optional[Agent]

agent\_name: str

class BetaResponseFunctionToolCall: …

[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

arguments: str

A JSON string of the arguments to pass to the function.

call\_id: str

name: str

The name of the function to run.

type: Literal["function\_call"]

The type of the function tool call. Always `function_call`.

id: Optional[str]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

namespace: Optional[str]

The namespace of the function to run.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class FunctionCallOutput: …

The output of a function tool call.

call\_id: str

maxLength64

minLength1

output: Union[str, [BetaResponseFunctionCallOutputItemList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item_list%20%3E%20(schema))]

Text, image, or file output of the function tool call.

str

A JSON string of the output of the function tool call.

List[[BetaResponseFunctionCallOutputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item%20%3E%20(schema))]

class BetaResponseInputTextContent: …

text: str

maxLength10485760

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImageContent: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

type: Literal["input\_image"]

detail: Optional[Literal["low", "high", "auto", "original"]]

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

image\_url: Optional[str]

maxLength20971520

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFileContent: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

The base64-encoded data of the file to be sent to the model.

maxLength73400320

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

type: Literal["function\_call\_output"]

id: Optional[str]

The unique ID of the function tool call output. Populated when this item is returned via API.

agent: Optional[FunctionCallOutputAgent]

agent\_name: str

caller: Optional[FunctionCallOutputCaller]

class FunctionCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class FunctionCallOutputCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

class AgentMessage: …

A message routed between agents.

author: str

content: List[AgentMessageContent]

Plaintext, image, or encrypted content sent between agents.

class BetaResponseInputTextContent: …

text: str

maxLength10485760

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImageContent: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

type: Literal["input\_image"]

detail: Optional[Literal["low", "high", "auto", "original"]]

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

image\_url: Optional[str]

maxLength20971520

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class AgentMessageContentEncryptedContent: …

encrypted\_content: str

maxLength10485760

type: Literal["encrypted\_content"]

recipient: str

type: Literal["agent\_message"]

The item type. Always `agent_message`.

id: Optional[str]

The unique ID of this agent message item.

agent: Optional[AgentMessageAgent]

agent\_name: str

class MultiAgentCall: …

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

The multi-agent action that was executed.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

arguments: str

The action arguments as a JSON string.

call\_id: str

maxLength64

minLength1

type: Literal["multi\_agent\_call"]

The item type. Always `multi_agent_call`.

id: Optional[str]

The unique ID of this multi-agent call.

agent: Optional[MultiAgentCallAgent]

agent\_name: str

class MultiAgentCallOutput: …

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

call\_id: str

maxLength64

minLength1

output: List[MultiAgentCallOutputOutput]

text: str

The text content.

maxLength10485760

type: Literal["output\_text"]

The content type. Always `output_text`.

annotations: Optional[List[MultiAgentCallOutputOutputAnnotation]]

Citations associated with the text content.

class MultiAgentCallOutputOutputAnnotationFileCitation: …

file\_id: str

filename: str

index: int

minimum0

type: Literal["file\_citation"]

The citation type. Always `file_citation`.

class MultiAgentCallOutputOutputAnnotationURLCitation: …

end\_index: int

The index of the last character of the citation in the message.

minimum0

start\_index: int

The index of the first character of the citation in the message.

minimum0

title: str

The title of the cited resource.

type: Literal["url\_citation"]

The citation type. Always `url_citation`.

url: str

The URL of the cited resource.

class MultiAgentCallOutputOutputAnnotationContainerFileCitation: …

container\_id: str

The ID of the container.

end\_index: int

The index of the last character of the citation in the message.

minimum0

file\_id: str

filename: str

start\_index: int

The index of the first character of the citation in the message.

minimum0

type: Literal["container\_file\_citation"]

The citation type. Always `container_file_citation`.

type: Literal["multi\_agent\_call\_output"]

The item type. Always `multi_agent_call_output`.

id: Optional[str]

The unique ID of this multi-agent call output.

agent: Optional[MultiAgentCallOutputAgent]

agent\_name: str

class ToolSearchCall: …

arguments: object

The arguments supplied to the tool search call.

type: Literal["tool\_search\_call"]

The item type. Always `tool_search_call`.

id: Optional[str]

The unique ID of this tool search call.

agent: Optional[ToolSearchCallAgent]

agent\_name: str

call\_id: Optional[str]

maxLength64

minLength1

execution: Optional[Literal["server", "client"]]

"server"

"client"

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the tool search call.

"in\_progress"

"completed"

"incomplete"

class BetaResponseToolSearchOutputItemParam: …

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

The loaded tool definitions returned by the tool search output.

class BetaFunctionTool: …

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

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

input\_fidelity: Optional[Literal["high", "low"]]

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

type: Literal["tool\_search\_output"]

The item type. Always `tool_search_output`.

id: Optional[str]

The unique ID of this tool search output.

agent: Optional[Agent]

agent\_name: str

call\_id: Optional[str]

maxLength64

minLength1

execution: Optional[Literal["server", "client"]]

"server"

"client"

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the tool search output.

"in\_progress"

"completed"

"incomplete"

class AdditionalTools: …

role: Literal["developer"]

The role that provided the additional tools. Only `developer` is supported.

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

A list of additional tools made available at this item.

class BetaFunctionTool: …

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

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

input\_fidelity: Optional[Literal["high", "low"]]

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

type: Literal["additional\_tools"]

The item type. Always `additional_tools`.

id: Optional[str]

The unique ID of this additional tools item.

agent: Optional[AdditionalToolsAgent]

agent\_name: str

class BetaResponseReasoningItem: …

[managing context](https://platform.openai.com/docs/guides/conversation-state).

id: str

summary: List[Summary]

text: str

type: Literal["summary\_text"]

type: Literal["reasoning"]

agent: Optional[Agent]

agent\_name: str

content: Optional[List[Content]]

text: str

type: Literal["reasoning\_text"]

encrypted\_content: Optional[str]

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class BetaResponseCompactionItemParam: …

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

encrypted\_content: str

The encrypted content of the compaction summary.

maxLength10485760

type: Literal["compaction"]

id: Optional[str]

The ID of the compaction item.

agent: Optional[Agent]

agent\_name: str

class ImageGenerationCall: …

An image generation request made by the model.

id: str

result: Optional[str]

status: Literal["in\_progress", "completed", "generating", "failed"]

"in\_progress"

"completed"

"generating"

"failed"

type: Literal["image\_generation\_call"]

agent: Optional[ImageGenerationCallAgent]

agent\_name: str

class BetaResponseCodeInterpreterToolCall: …

id: str

code: Optional[str]

container\_id: str

outputs: Optional[List[Output]]

class OutputLogs: …

logs: str

type: Literal["logs"]

class OutputImage: …

type: Literal["image"]

url: str

status: Literal["in\_progress", "completed", "incomplete", 2 more]

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: Literal["code\_interpreter\_call"]

agent: Optional[Agent]

agent\_name: str

class LocalShellCall: …

A tool call to run a command on the local shell.

id: str

action: LocalShellCallAction

command: List[str]

env: Dict[str, str]

type: Literal["exec"]

timeout\_ms: Optional[int]

user: Optional[str]

working\_directory: Optional[str]

call\_id: str

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["local\_shell\_call"]

agent: Optional[LocalShellCallAgent]

agent\_name: str

class LocalShellCallOutput: …

The output of a local shell tool call.

id: str

output: str

type: Literal["local\_shell\_call\_output"]

agent: Optional[LocalShellCallOutputAgent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class ShellCall: …

A tool representing a request to execute one or more shell commands.

action: ShellCallAction

commands: List[str]

Ordered shell commands for the execution environment to run.

max\_output\_length: Optional[int]

Maximum number of UTF-8 characters to capture from combined stdout and stderr output.

timeout\_ms: Optional[int]

Maximum wall-clock time in milliseconds to allow the shell commands to run.

call\_id: str

maxLength64

minLength1

type: Literal["shell\_call"]

id: Optional[str]

agent: Optional[ShellCallAgent]

agent\_name: str

caller: Optional[ShellCallCaller]

class ShellCallCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ShellCallCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

environment: Optional[ShellCallEnvironment]

The environment to execute the shell commands in.

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class ShellCallOutput: …

The streamed output items emitted by a shell tool call.

call\_id: str

maxLength64

minLength1

output: List[[BetaResponseFunctionShellCallOutputContent](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_shell_call_output_content%20%3E%20(schema))]

Captured chunks of stdout and stderr output, along with their associated outcomes.

outcome: Outcome

The exit or timeout outcome associated with this shell call.

class OutcomeTimeout: …

Indicates that the shell call exceeded its configured time limit.

type: Literal["timeout"]

The outcome type. Always `timeout`.

class OutcomeExit: …

exit\_code: int

The exit code returned by the shell process.

type: Literal["exit"]

stderr: str

Captured stderr output for the shell call.

maxLength10485760

stdout: str

Captured stdout output for the shell call.

maxLength10485760

type: Literal["shell\_call\_output"]

The type of the item. Always `shell_call_output`.

id: Optional[str]

The unique ID of the shell tool call output. Populated when this item is returned via API.

agent: Optional[ShellCallOutputAgent]

agent\_name: str

caller: Optional[ShellCallOutputCaller]

class ShellCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ShellCallOutputCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

max\_output\_length: Optional[int]

The maximum number of UTF-8 characters captured for this shell call’s combined output.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the shell call output.

"in\_progress"

"completed"

"incomplete"

class ApplyPatchCall: …

A tool call representing a request to create, delete, or update files using diff patches.

call\_id: str

maxLength64

minLength1

operation: ApplyPatchCallOperation

The specific create, delete, or update instruction for the apply\_patch tool call.

class ApplyPatchCallOperationCreateFile: …

Instruction for creating a new file via the apply\_patch tool.

diff: str

Unified diff content to apply when creating the file.

maxLength10485760

path: str

Path of the file to create relative to the workspace root.

minLength1

type: Literal["create\_file"]

The operation type. Always `create_file`.

class ApplyPatchCallOperationDeleteFile: …

Instruction for deleting an existing file via the apply\_patch tool.

path: str

Path of the file to delete relative to the workspace root.

minLength1

type: Literal["delete\_file"]

The operation type. Always `delete_file`.

class ApplyPatchCallOperationUpdateFile: …

Instruction for updating an existing file via the apply\_patch tool.

diff: str

Unified diff content to apply to the existing file.

maxLength10485760

path: str

Path of the file to update relative to the workspace root.

minLength1

type: Literal["update\_file"]

The operation type. Always `update_file`.

status: Literal["in\_progress", "completed"]

"in\_progress"

"completed"

type: Literal["apply\_patch\_call"]

id: Optional[str]

agent: Optional[ApplyPatchCallAgent]

agent\_name: str

caller: Optional[ApplyPatchCallCaller]

class ApplyPatchCallCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ApplyPatchCallCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

class ApplyPatchCallOutput: …

The streamed output emitted by an apply patch tool call.

call\_id: str

maxLength64

minLength1

status: Literal["completed", "failed"]

"completed"

"failed"

type: Literal["apply\_patch\_call\_output"]

id: Optional[str]

agent: Optional[ApplyPatchCallOutputAgent]

agent\_name: str

caller: Optional[ApplyPatchCallOutputCaller]

class ApplyPatchCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ApplyPatchCallOutputCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

output: Optional[str]

Optional human-readable log text from the apply patch tool (e.g., patch results or errors).

maxLength10485760

class McpListTools: …

A list of tools available on an MCP server.

id: str

server\_label: str

tools: List[McpListToolsTool]

input\_schema: object

name: str

annotations: Optional[object]

description: Optional[str]

type: Literal["mcp\_list\_tools"]

agent: Optional[McpListToolsAgent]

agent\_name: str

error: Optional[str]

class McpApprovalRequest: …

A request for human approval of a tool invocation.

id: str

arguments: str

name: str

server\_label: str

type: Literal["mcp\_approval\_request"]

agent: Optional[McpApprovalRequestAgent]

agent\_name: str

class McpApprovalResponse: …

A response to an MCP approval request.

approval\_request\_id: str

approve: bool

type: Literal["mcp\_approval\_response"]

id: Optional[str]

agent: Optional[McpApprovalResponseAgent]

agent\_name: str

reason: Optional[str]

class McpCall: …

An invocation of a tool on an MCP server.

id: str

arguments: str

name: str

server\_label: str

type: Literal["mcp\_call"]

agent: Optional[McpCallAgent]

agent\_name: str

approval\_request\_id: Optional[str]

error: Optional[str]

output: Optional[str]

status: Optional[Literal["in\_progress", "completed", "incomplete", 2 more]]

"in\_progress"

"completed"

"incomplete"

"calling"

"failed"

class BetaResponseCustomToolCallOutput: …

call\_id: str

The call ID, used to map this custom tool call output to a custom tool call.

output: Union[str, List[OutputOutputContentList]]

The output from the custom tool call generated by your code.

str

A string of the output of the custom tool call.

List[OutputOutputContentList]

Text, image, or file output of the custom tool call.

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

type: Literal["custom\_tool\_call\_output"]

The type of the custom tool call output. Always `custom_tool_call_output`.

id: Optional[str]

The unique ID of the custom tool call output in the OpenAI platform.

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class CallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

class BetaResponseCustomToolCall: …

call\_id: str

An identifier used to map this custom tool call to a tool call output.

input: str

The input for the custom tool call generated by the model.

name: str

The name of the custom tool being called.

type: Literal["custom\_tool\_call"]

The type of the custom tool call. Always `custom_tool_call`.

id: Optional[str]

The unique ID of the custom tool call in the OpenAI platform.

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

namespace: Optional[str]

The namespace of the custom tool being called.

class CompactionTrigger: …

Compacts the current context. Must be the final input item.

type: Literal["compaction\_trigger"]

The type of the item. Always `compaction_trigger`.

agent: Optional[CompactionTriggerAgent]

agent\_name: str

class ItemReference: …

An internal identifier for an item to reference.

id: str

The ID of the item to reference.

agent: Optional[ItemReferenceAgent]

agent\_name: str

type: Optional[Literal["item\_reference"]]

The type of item to reference. Always `item_reference`.

class Program: …

id: str

The unique ID of this program item.

call\_id: str

maxLength64

minLength1

code: str

maxLength10485760

fingerprint: str

maxLength10485760

type: Literal["program"]

The item type. Always `program`.

agent: Optional[ProgramAgent]

agent\_name: str

class ProgramOutput: …

id: str

The unique ID of this program output item.

call\_id: str

maxLength64

minLength1

result: str

maxLength10485760

status: Literal["completed", "incomplete"]

The terminal status of the program output.

"completed"

"incomplete"

type: Literal["program\_output"]

The item type. Always `program_output`.

agent: Optional[ProgramOutputAgent]

agent\_name: str

List[[BetaResponseInputContent](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_content%20%3E%20(schema))]

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputMessageItem: …

id: str

The unique ID of the message input.

content: [BetaResponseInputMessageContentList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema))

role: Literal["user", "system", "developer"]

"user"

"system"

"developer"

type: Literal["message"]

agent: Optional[Agent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputTextContent: …

text: str

maxLength10485760

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

[BetaResponseItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_item%20%3E%20(schema))

Content item used to generate a response.

class BetaResponseInputMessageItem: …

id: str

The unique ID of the message input.

content: [BetaResponseInputMessageContentList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema))

role: Literal["user", "system", "developer"]

"user"

"system"

"developer"

type: Literal["message"]

agent: Optional[Agent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class BetaResponseOutputMessage: …

id: str

content: List[Content]

class BetaResponseOutputText: …

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

logprobs: Optional[List[Logprob]]

token: str

bytes: List[int]

logprob: float

top\_logprobs: List[LogprobTopLogprob]

token: str

bytes: List[int]

logprob: float

class BetaResponseOutputRefusal: …

refusal: str

type: Literal["refusal"]

role: Literal["assistant"]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["message"]

agent: Optional[Agent]

agent\_name: str

phase: Optional[Literal["commentary", "final\_answer"]]

"commentary"

"final\_answer"

class BetaResponseFileSearchToolCall: …

[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

id: str

queries: List[str]

status: Literal["in\_progress", "searching", "completed", 2 more]

"in\_progress"

"searching"

"completed"

"incomplete"

"failed"

type: Literal["file\_search\_call"]

agent: Optional[Agent]

agent\_name: str

results: Optional[List[Result]]

attributes: Optional[Dict[str, Union[str, float, bool]]]

str

float

bool

file\_id: Optional[str]

filename: Optional[str]

score: Optional[float]

formatfloat

text: Optional[str]

class BetaResponseComputerToolCall: …

[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

id: str

call\_id: str

pending\_safety\_checks: List[PendingSafetyCheck]

id: str

code: Optional[str]

message: Optional[str]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["computer\_call"]

action: Optional[BetaComputerAction]

actions: Optional[BetaComputerActionList]

agent: Optional[Agent]

agent\_name: str

class BetaResponseComputerToolCallOutputItem: …

id: str

The unique ID of the computer call tool output.

call\_id: str

output: [BetaResponseComputerToolCallOutputScreenshot](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema))

status: Literal["completed", "incomplete", "failed", "in\_progress"]

"completed"

"incomplete"

"failed"

"in\_progress"

type: Literal["computer\_call\_output"]

acknowledged\_safety\_checks: Optional[List[AcknowledgedSafetyCheck]]

The safety checks reported by the API that have been acknowledged by the
developer.

id: str

code: Optional[str]

message: Optional[str]

agent: Optional[Agent]

agent\_name: str

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseFunctionWebSearch: …

[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

id: str

action: Action

class ActionSearch: …

type: Literal["search"]

queries: Optional[List[str]]

Deprecatedquery: Optional[str]

sources: Optional[List[ActionSearchSource]]

type: Literal["url"]

url: str

class ActionOpenPage: …

type: Literal["open\_page"]

url: Optional[str]

class ActionFindInPage: …

pattern: str

type: Literal["find\_in\_page"]

url: str

status: Literal["in\_progress", "searching", "completed", "failed"]

"in\_progress"

"searching"

"completed"

"failed"

type: Literal["web\_search\_call"]

agent: Optional[Agent]

agent\_name: str

class BetaResponseFunctionToolCallItem: …

[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

id: str

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseFunctionToolCallOutputItem: …

id: str

The unique ID of the function call tool output.

call\_id: str

output: Union[str, List[OutputOutputContentList]]

The output from the function call generated by your code.

str

A string of the output of the function call.

List[OutputOutputContentList]

Text, image, or file output of the function call.

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["function\_call\_output"]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class CallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

created\_by: Optional[str]

The identifier of the actor that created the item.

class AgentMessage: …

id: str

The unique ID of the agent message.

author: str

content: List[AgentMessageContent]

Encrypted content sent between agents.

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseOutputText: …

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

logprobs: Optional[List[Logprob]]

token: str

bytes: List[int]

logprob: float

top\_logprobs: List[LogprobTopLogprob]

token: str

bytes: List[int]

logprob: float

class AgentMessageContentText: …

A text content.

text: str

type: Literal["text"]

class AgentMessageContentSummaryText: …

A summary text from the model.

text: str

type: Literal["summary\_text"]

class AgentMessageContentReasoningText: …

text: str

type: Literal["reasoning\_text"]

class BetaResponseOutputRefusal: …

refusal: str

type: Literal["refusal"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class AgentMessageContentComputerScreenshot: …

A screenshot of a computer.

detail: Literal["low", "high", "auto", "original"]

The detail level of the screenshot image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

image\_url: Optional[str]

type: Literal["computer\_screenshot"]

Specifies the event type. For a computer screenshot, this property is always set to `computer_screenshot`.

prompt\_cache\_breakpoint: Optional[AgentMessageContentComputerScreenshotPromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class AgentMessageContentEncryptedContent: …

encrypted\_content: str

type: Literal["encrypted\_content"]

recipient: str

type: Literal["agent\_message"]

The type of the item. Always `agent_message`.

agent: Optional[AgentMessageAgent]

agent\_name: str

class MultiAgentCall: …

id: str

The unique ID of the multi-agent call item.

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

The multi-agent action to execute.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

arguments: str

The JSON string of arguments generated for the action.

call\_id: str

type: Literal["multi\_agent\_call"]

The type of the multi-agent call. Always `multi_agent_call`.

agent: Optional[MultiAgentCallAgent]

agent\_name: str

class MultiAgentCallOutput: …

id: str

The unique ID of the multi-agent call output item.

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

call\_id: str

output: List[[BetaResponseOutputText](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema))]

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

logprobs: Optional[List[Logprob]]

token: str

bytes: List[int]

logprob: float

top\_logprobs: List[LogprobTopLogprob]

token: str

bytes: List[int]

logprob: float

type: Literal["multi\_agent\_call\_output"]

The type of the multi-agent result. Always `multi_agent_call_output`.

agent: Optional[MultiAgentCallOutputAgent]

agent\_name: str

class BetaResponseToolSearchCall: …

id: str

The unique ID of the tool search call item.

arguments: object

Arguments used for the tool search call.

call\_id: Optional[str]

execution: Literal["server", "client"]

"server"

"client"

status: Literal["in\_progress", "completed", "incomplete"]

The status of the tool search call item that was recorded.

"in\_progress"

"completed"

"incomplete"

type: Literal["tool\_search\_call"]

The type of the item. Always `tool_search_call`.

agent: Optional[Agent]

agent\_name: str

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseToolSearchOutputItem: …

id: str

The unique ID of the tool search output item.

call\_id: Optional[str]

execution: Literal["server", "client"]

"server"

"client"

status: Literal["in\_progress", "completed", "incomplete"]

The status of the tool search output item that was recorded.

"in\_progress"

"completed"

"incomplete"

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

The loaded tool definitions returned by tool search.

class BetaFunctionTool: …

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

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

input\_fidelity: Optional[Literal["high", "low"]]

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

type: Literal["tool\_search\_output"]

The type of the item. Always `tool_search_output`.

agent: Optional[Agent]

agent\_name: str

created\_by: Optional[str]

The identifier of the actor that created the item.

class AdditionalTools: …

id: str

The unique ID of the additional tools item.

role: Literal["unknown", "user", "assistant", 5 more]

The role that provided the additional tools.

"unknown"

"user"

"assistant"

"system"

"critic"

"discriminator"

"developer"

"tool"

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

The additional tool definitions made available at this item.

class BetaFunctionTool: …

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

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

input\_fidelity: Optional[Literal["high", "low"]]

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

type: Literal["additional\_tools"]

The type of the item. Always `additional_tools`.

agent: Optional[AdditionalToolsAgent]

agent\_name: str

class BetaResponseReasoningItem: …

[managing context](https://platform.openai.com/docs/guides/conversation-state).

id: str

summary: List[Summary]

text: str

type: Literal["summary\_text"]

type: Literal["reasoning"]

agent: Optional[Agent]

agent\_name: str

content: Optional[List[Content]]

text: str

type: Literal["reasoning\_text"]

encrypted\_content: Optional[str]

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class Program: …

id: str

The unique ID of the program item.

call\_id: str

code: str

fingerprint: str

type: Literal["program"]

The type of the item. Always `program`.

agent: Optional[ProgramAgent]

agent\_name: str

class ProgramOutput: …

id: str

The unique ID of the program output item.

call\_id: str

result: str

status: Literal["completed", "incomplete"]

The terminal status of the program output item.

"completed"

"incomplete"

type: Literal["program\_output"]

The type of the item. Always `program_output`.

agent: Optional[ProgramOutputAgent]

agent\_name: str

class BetaResponseCompactionItem: …

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

id: str

The unique ID of the compaction item.

encrypted\_content: str

The encrypted content that was produced by compaction.

type: Literal["compaction"]

agent: Optional[Agent]

agent\_name: str

created\_by: Optional[str]

The identifier of the actor that created the item.

class ImageGenerationCall: …

An image generation request made by the model.

id: str

result: Optional[str]

status: Literal["in\_progress", "completed", "generating", "failed"]

"in\_progress"

"completed"

"generating"

"failed"

type: Literal["image\_generation\_call"]

agent: Optional[ImageGenerationCallAgent]

agent\_name: str

class BetaResponseCodeInterpreterToolCall: …

id: str

code: Optional[str]

container\_id: str

outputs: Optional[List[Output]]

class OutputLogs: …

logs: str

type: Literal["logs"]

class OutputImage: …

type: Literal["image"]

url: str

status: Literal["in\_progress", "completed", "incomplete", 2 more]

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: Literal["code\_interpreter\_call"]

agent: Optional[Agent]

agent\_name: str

class LocalShellCall: …

A tool call to run a command on the local shell.

id: str

action: LocalShellCallAction

command: List[str]

env: Dict[str, str]

type: Literal["exec"]

timeout\_ms: Optional[int]

user: Optional[str]

working\_directory: Optional[str]

call\_id: str

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["local\_shell\_call"]

agent: Optional[LocalShellCallAgent]

agent\_name: str

class LocalShellCallOutput: …

The output of a local shell tool call.

id: str

output: str

type: Literal["local\_shell\_call\_output"]

agent: Optional[LocalShellCallOutputAgent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class BetaResponseFunctionShellToolCall: …

A tool call that executes one or more shell commands in a managed environment.

id: str

action: Action

commands: List[str]

max\_output\_length: Optional[int]

Optional maximum number of characters to return from each command.

timeout\_ms: Optional[int]

Optional timeout in milliseconds for the commands.

call\_id: str

environment: Optional[Environment]

Represents the use of a local environment to perform shell actions.

class BetaResponseLocalEnvironment: …

Represents the use of a local environment to perform shell actions.

type: Literal["local"]

The environment type. Always `local`.

class BetaResponseContainerReference: …

Represents a container created with /v1/containers.

container\_id: str

type: Literal["container\_reference"]

The environment type. Always `container_reference`.

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["shell\_call"]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

created\_by: Optional[str]

The ID of the entity that created this tool call.

class BetaResponseFunctionShellToolCallOutput: …

The output of a shell tool call that was emitted.

id: str

The unique ID of the shell call output. Populated when this item is returned via API.

call\_id: str

max\_output\_length: Optional[int]

The maximum length of the shell command output. This is generated by the model and should be passed back with the raw output.

output: List[Output]

An array of shell call output contents

outcome: OutputOutcome

Represents either an exit outcome (with an exit code) or a timeout outcome for a shell call output chunk.

class OutputOutcomeTimeout: …

Indicates that the shell call exceeded its configured time limit.

type: Literal["timeout"]

The outcome type. Always `timeout`.

class OutputOutcomeExit: …

exit\_code: int

Exit code from the shell process.

type: Literal["exit"]

stderr: str

The standard error output that was captured.

stdout: str

The standard output that was captured.

created\_by: Optional[str]

The identifier of the actor that created the item.

status: Literal["in\_progress", "completed", "incomplete"]

The status of the shell call output. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

type: Literal["shell\_call\_output"]

The type of the shell call output. Always `shell_call_output`.

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseApplyPatchToolCall: …

A tool call that applies file diffs by creating, deleting, or updating files.

id: str

call\_id: str

operation: Operation

One of the create\_file, delete\_file, or update\_file operations applied via apply\_patch.

class OperationCreateFile: …

Instruction describing how to create a file via the apply\_patch tool.

diff: str

Diff to apply.

path: str

Path of the file to create.

type: Literal["create\_file"]

Create a new file with the provided diff.

class OperationDeleteFile: …

Instruction describing how to delete a file via the apply\_patch tool.

path: str

Path of the file to delete.

type: Literal["delete\_file"]

Delete the specified file.

class OperationUpdateFile: …

Instruction describing how to update a file via the apply\_patch tool.

diff: str

Diff to apply.

path: str

Path of the file to update.

type: Literal["update\_file"]

Update an existing file with the provided diff.

status: Literal["in\_progress", "completed"]

"in\_progress"

"completed"

type: Literal["apply\_patch\_call"]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

created\_by: Optional[str]

The ID of the entity that created this tool call.

class BetaResponseApplyPatchToolCallOutput: …

The output emitted by an apply patch tool call.

id: str

call\_id: str

status: Literal["completed", "failed"]

"completed"

"failed"

type: Literal["apply\_patch\_call\_output"]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

created\_by: Optional[str]

The ID of the entity that created this tool call output.

output: Optional[str]

Optional textual output returned by the apply patch tool.

class McpListTools: …

A list of tools available on an MCP server.

id: str

server\_label: str

tools: List[McpListToolsTool]

input\_schema: object

name: str

annotations: Optional[object]

description: Optional[str]

type: Literal["mcp\_list\_tools"]

agent: Optional[McpListToolsAgent]

agent\_name: str

error: Optional[str]

class McpApprovalRequest: …

A request for human approval of a tool invocation.

id: str

arguments: str

name: str

server\_label: str

type: Literal["mcp\_approval\_request"]

agent: Optional[McpApprovalRequestAgent]

agent\_name: str

class McpApprovalResponse: …

A response to an MCP approval request.

id: str

approval\_request\_id: str

approve: bool

type: Literal["mcp\_approval\_response"]

agent: Optional[McpApprovalResponseAgent]

agent\_name: str

reason: Optional[str]

class McpCall: …

An invocation of a tool on an MCP server.

id: str

arguments: str

name: str

server\_label: str

type: Literal["mcp\_call"]

agent: Optional[McpCallAgent]

agent\_name: str

approval\_request\_id: Optional[str]

error: Optional[str]

output: Optional[str]

status: Optional[Literal["in\_progress", "completed", "incomplete", 2 more]]

"in\_progress"

"completed"

"incomplete"

"calling"

"failed"

class BetaResponseCustomToolCallItem: …

id: str

The unique ID of the custom tool call item.

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseCustomToolCallOutputItem: …

id: str

The unique ID of the custom tool call output item.

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseLocalEnvironment: …

Represents the use of a local environment to perform shell actions.

type: Literal["local"]

The environment type. Always `local`.

class BetaResponseMcpCallArgumentsDeltaEvent: …

Emitted when there is a delta (partial update) to the arguments of an MCP tool call.

delta: str

A JSON string containing the partial update to the arguments for the MCP tool call.

item\_id: str

The unique identifier of the MCP tool call item being processed.

output\_index: int

The index of the output item in the response’s output array.

sequence\_number: int

The sequence number of this event.

type: Literal["response.mcp\_call\_arguments.delta"]

The type of the event. Always ‘response.mcp\_call\_arguments.delta’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseMcpCallArgumentsDoneEvent: …

Emitted when the arguments for an MCP tool call are finalized.

arguments: str

A JSON string containing the finalized arguments for the MCP tool call.

item\_id: str

The unique identifier of the MCP tool call item being processed.

output\_index: int

The index of the output item in the response’s output array.

sequence\_number: int

The sequence number of this event.

type: Literal["response.mcp\_call\_arguments.done"]

The type of the event. Always ‘response.mcp\_call\_arguments.done’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseMcpCallCompletedEvent: …

Emitted when an MCP tool call has completed successfully.

item\_id: str

The ID of the MCP tool call item that completed.

output\_index: int

The index of the output item that completed.

sequence\_number: int

The sequence number of this event.

type: Literal["response.mcp\_call.completed"]

The type of the event. Always ‘response.mcp\_call.completed’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseMcpCallFailedEvent: …

Emitted when an MCP tool call has failed.

item\_id: str

The ID of the MCP tool call item that failed.

output\_index: int

The index of the output item that failed.

sequence\_number: int

The sequence number of this event.

type: Literal["response.mcp\_call.failed"]

The type of the event. Always ‘response.mcp\_call.failed’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseMcpCallInProgressEvent: …

Emitted when an MCP tool call is in progress.

item\_id: str

The unique identifier of the MCP tool call item being processed.

output\_index: int

The index of the output item in the response’s output array.

sequence\_number: int

The sequence number of this event.

type: Literal["response.mcp\_call.in\_progress"]

The type of the event. Always ‘response.mcp\_call.in\_progress’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseMcpListToolsCompletedEvent: …

Emitted when the list of available MCP tools has been successfully retrieved.

item\_id: str

The ID of the MCP tool call item that produced this output.

output\_index: int

The index of the output item that was processed.

sequence\_number: int

The sequence number of this event.

type: Literal["response.mcp\_list\_tools.completed"]

The type of the event. Always ‘response.mcp\_list\_tools.completed’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseMcpListToolsFailedEvent: …

Emitted when the attempt to list available MCP tools has failed.

item\_id: str

The ID of the MCP tool call item that failed.

output\_index: int

The index of the output item that failed.

sequence\_number: int

The sequence number of this event.

type: Literal["response.mcp\_list\_tools.failed"]

The type of the event. Always ‘response.mcp\_list\_tools.failed’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseMcpListToolsInProgressEvent: …

Emitted when the system is in the process of retrieving the list of available MCP tools.

item\_id: str

The ID of the MCP tool call item that is being processed.

output\_index: int

The index of the output item that is being processed.

sequence\_number: int

The sequence number of this event.

type: Literal["response.mcp\_list\_tools.in\_progress"]

The type of the event. Always ‘response.mcp\_list\_tools.in\_progress’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseOutputAudio: …

An audio output from the model.

data: str

Base64-encoded audio data from the model.

transcript: str

The transcript of the audio data from the model.

type: Literal["output\_audio"]

The type of the output audio. Always `output_audio`.

[BetaResponseOutputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema))

class BetaResponseOutputMessage: …

id: str

content: List[Content]

class BetaResponseOutputText: …

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

logprobs: Optional[List[Logprob]]

token: str

bytes: List[int]

logprob: float

top\_logprobs: List[LogprobTopLogprob]

token: str

bytes: List[int]

logprob: float

class BetaResponseOutputRefusal: …

refusal: str

type: Literal["refusal"]

role: Literal["assistant"]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["message"]

agent: Optional[Agent]

agent\_name: str

phase: Optional[Literal["commentary", "final\_answer"]]

"commentary"

"final\_answer"

class BetaResponseFileSearchToolCall: …

[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

id: str

queries: List[str]

status: Literal["in\_progress", "searching", "completed", 2 more]

"in\_progress"

"searching"

"completed"

"incomplete"

"failed"

type: Literal["file\_search\_call"]

agent: Optional[Agent]

agent\_name: str

results: Optional[List[Result]]

attributes: Optional[Dict[str, Union[str, float, bool]]]

str

float

bool

file\_id: Optional[str]

filename: Optional[str]

score: Optional[float]

formatfloat

text: Optional[str]

class BetaResponseFunctionToolCall: …

[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

arguments: str

A JSON string of the arguments to pass to the function.

call\_id: str

name: str

The name of the function to run.

type: Literal["function\_call"]

The type of the function tool call. Always `function_call`.

id: Optional[str]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

namespace: Optional[str]

The namespace of the function to run.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class BetaResponseFunctionToolCallOutputItem: …

id: str

The unique ID of the function call tool output.

call\_id: str

output: Union[str, List[OutputOutputContentList]]

The output from the function call generated by your code.

str

A string of the output of the function call.

List[OutputOutputContentList]

Text, image, or file output of the function call.

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["function\_call\_output"]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class CallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

created\_by: Optional[str]

The identifier of the actor that created the item.

class AgentMessage: …

id: str

The unique ID of the agent message.

author: str

content: List[AgentMessageContent]

Encrypted content sent between agents.

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseOutputText: …

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

logprobs: Optional[List[Logprob]]

token: str

bytes: List[int]

logprob: float

top\_logprobs: List[LogprobTopLogprob]

token: str

bytes: List[int]

logprob: float

class AgentMessageContentText: …

A text content.

text: str

type: Literal["text"]

class AgentMessageContentSummaryText: …

A summary text from the model.

text: str

type: Literal["summary\_text"]

class AgentMessageContentReasoningText: …

text: str

type: Literal["reasoning\_text"]

class BetaResponseOutputRefusal: …

refusal: str

type: Literal["refusal"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class AgentMessageContentComputerScreenshot: …

A screenshot of a computer.

detail: Literal["low", "high", "auto", "original"]

The detail level of the screenshot image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

image\_url: Optional[str]

type: Literal["computer\_screenshot"]

Specifies the event type. For a computer screenshot, this property is always set to `computer_screenshot`.

prompt\_cache\_breakpoint: Optional[AgentMessageContentComputerScreenshotPromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class AgentMessageContentEncryptedContent: …

encrypted\_content: str

type: Literal["encrypted\_content"]

recipient: str

type: Literal["agent\_message"]

The type of the item. Always `agent_message`.

agent: Optional[AgentMessageAgent]

agent\_name: str

class MultiAgentCall: …

id: str

The unique ID of the multi-agent call item.

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

The multi-agent action to execute.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

arguments: str

The JSON string of arguments generated for the action.

call\_id: str

type: Literal["multi\_agent\_call"]

The type of the multi-agent call. Always `multi_agent_call`.

agent: Optional[MultiAgentCallAgent]

agent\_name: str

class MultiAgentCallOutput: …

id: str

The unique ID of the multi-agent call output item.

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

call\_id: str

output: List[[BetaResponseOutputText](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema))]

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

logprobs: Optional[List[Logprob]]

token: str

bytes: List[int]

logprob: float

top\_logprobs: List[LogprobTopLogprob]

token: str

bytes: List[int]

logprob: float

type: Literal["multi\_agent\_call\_output"]

The type of the multi-agent result. Always `multi_agent_call_output`.

agent: Optional[MultiAgentCallOutputAgent]

agent\_name: str

class BetaResponseFunctionWebSearch: …

[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

id: str

action: Action

class ActionSearch: …

type: Literal["search"]

queries: Optional[List[str]]

Deprecatedquery: Optional[str]

sources: Optional[List[ActionSearchSource]]

type: Literal["url"]

url: str

class ActionOpenPage: …

type: Literal["open\_page"]

url: Optional[str]

class ActionFindInPage: …

pattern: str

type: Literal["find\_in\_page"]

url: str

status: Literal["in\_progress", "searching", "completed", "failed"]

"in\_progress"

"searching"

"completed"

"failed"

type: Literal["web\_search\_call"]

agent: Optional[Agent]

agent\_name: str

class BetaResponseComputerToolCall: …

[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

id: str

call\_id: str

pending\_safety\_checks: List[PendingSafetyCheck]

id: str

code: Optional[str]

message: Optional[str]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["computer\_call"]

action: Optional[BetaComputerAction]

actions: Optional[BetaComputerActionList]

agent: Optional[Agent]

agent\_name: str

class BetaResponseComputerToolCallOutputItem: …

id: str

The unique ID of the computer call tool output.

call\_id: str

output: [BetaResponseComputerToolCallOutputScreenshot](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema))

status: Literal["completed", "incomplete", "failed", "in\_progress"]

"completed"

"incomplete"

"failed"

"in\_progress"

type: Literal["computer\_call\_output"]

acknowledged\_safety\_checks: Optional[List[AcknowledgedSafetyCheck]]

The safety checks reported by the API that have been acknowledged by the
developer.

id: str

code: Optional[str]

message: Optional[str]

agent: Optional[Agent]

agent\_name: str

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseReasoningItem: …

[managing context](https://platform.openai.com/docs/guides/conversation-state).

id: str

summary: List[Summary]

text: str

type: Literal["summary\_text"]

type: Literal["reasoning"]

agent: Optional[Agent]

agent\_name: str

content: Optional[List[Content]]

text: str

type: Literal["reasoning\_text"]

encrypted\_content: Optional[str]

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class Program: …

id: str

The unique ID of the program item.

call\_id: str

code: str

fingerprint: str

type: Literal["program"]

The type of the item. Always `program`.

agent: Optional[ProgramAgent]

agent\_name: str

class ProgramOutput: …

id: str

The unique ID of the program output item.

call\_id: str

result: str

status: Literal["completed", "incomplete"]

The terminal status of the program output item.

"completed"

"incomplete"

type: Literal["program\_output"]

The type of the item. Always `program_output`.

agent: Optional[ProgramOutputAgent]

agent\_name: str

class BetaResponseToolSearchCall: …

id: str

The unique ID of the tool search call item.

arguments: object

Arguments used for the tool search call.

call\_id: Optional[str]

execution: Literal["server", "client"]

"server"

"client"

status: Literal["in\_progress", "completed", "incomplete"]

The status of the tool search call item that was recorded.

"in\_progress"

"completed"

"incomplete"

type: Literal["tool\_search\_call"]

The type of the item. Always `tool_search_call`.

agent: Optional[Agent]

agent\_name: str

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseToolSearchOutputItem: …

id: str

The unique ID of the tool search output item.

call\_id: Optional[str]

execution: Literal["server", "client"]

"server"

"client"

status: Literal["in\_progress", "completed", "incomplete"]

The status of the tool search output item that was recorded.

"in\_progress"

"completed"

"incomplete"

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

The loaded tool definitions returned by tool search.

class BetaFunctionTool: …

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

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

input\_fidelity: Optional[Literal["high", "low"]]

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

type: Literal["tool\_search\_output"]

The type of the item. Always `tool_search_output`.

agent: Optional[Agent]

agent\_name: str

created\_by: Optional[str]

The identifier of the actor that created the item.

class AdditionalTools: …

id: str

The unique ID of the additional tools item.

role: Literal["unknown", "user", "assistant", 5 more]

The role that provided the additional tools.

"unknown"

"user"

"assistant"

"system"

"critic"

"discriminator"

"developer"

"tool"

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

The additional tool definitions made available at this item.

class BetaFunctionTool: …

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

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

input\_fidelity: Optional[Literal["high", "low"]]

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

type: Literal["additional\_tools"]

The type of the item. Always `additional_tools`.

agent: Optional[AdditionalToolsAgent]

agent\_name: str

class BetaResponseCompactionItem: …

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

id: str

The unique ID of the compaction item.

encrypted\_content: str

The encrypted content that was produced by compaction.

type: Literal["compaction"]

agent: Optional[Agent]

agent\_name: str

created\_by: Optional[str]

The identifier of the actor that created the item.

class ImageGenerationCall: …

An image generation request made by the model.

id: str

result: Optional[str]

status: Literal["in\_progress", "completed", "generating", "failed"]

"in\_progress"

"completed"

"generating"

"failed"

type: Literal["image\_generation\_call"]

agent: Optional[ImageGenerationCallAgent]

agent\_name: str

class BetaResponseCodeInterpreterToolCall: …

id: str

code: Optional[str]

container\_id: str

outputs: Optional[List[Output]]

class OutputLogs: …

logs: str

type: Literal["logs"]

class OutputImage: …

type: Literal["image"]

url: str

status: Literal["in\_progress", "completed", "incomplete", 2 more]

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: Literal["code\_interpreter\_call"]

agent: Optional[Agent]

agent\_name: str

class LocalShellCall: …

A tool call to run a command on the local shell.

id: str

action: LocalShellCallAction

command: List[str]

env: Dict[str, str]

type: Literal["exec"]

timeout\_ms: Optional[int]

user: Optional[str]

working\_directory: Optional[str]

call\_id: str

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["local\_shell\_call"]

agent: Optional[LocalShellCallAgent]

agent\_name: str

class LocalShellCallOutput: …

The output of a local shell tool call.

id: str

output: str

type: Literal["local\_shell\_call\_output"]

agent: Optional[LocalShellCallOutputAgent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class BetaResponseFunctionShellToolCall: …

A tool call that executes one or more shell commands in a managed environment.

id: str

action: Action

commands: List[str]

max\_output\_length: Optional[int]

Optional maximum number of characters to return from each command.

timeout\_ms: Optional[int]

Optional timeout in milliseconds for the commands.

call\_id: str

environment: Optional[Environment]

Represents the use of a local environment to perform shell actions.

class BetaResponseLocalEnvironment: …

Represents the use of a local environment to perform shell actions.

type: Literal["local"]

The environment type. Always `local`.

class BetaResponseContainerReference: …

Represents a container created with /v1/containers.

container\_id: str

type: Literal["container\_reference"]

The environment type. Always `container_reference`.

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["shell\_call"]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

created\_by: Optional[str]

The ID of the entity that created this tool call.

class BetaResponseFunctionShellToolCallOutput: …

The output of a shell tool call that was emitted.

id: str

The unique ID of the shell call output. Populated when this item is returned via API.

call\_id: str

max\_output\_length: Optional[int]

The maximum length of the shell command output. This is generated by the model and should be passed back with the raw output.

output: List[Output]

An array of shell call output contents

outcome: OutputOutcome

Represents either an exit outcome (with an exit code) or a timeout outcome for a shell call output chunk.

class OutputOutcomeTimeout: …

Indicates that the shell call exceeded its configured time limit.

type: Literal["timeout"]

The outcome type. Always `timeout`.

class OutputOutcomeExit: …

exit\_code: int

Exit code from the shell process.

type: Literal["exit"]

stderr: str

The standard error output that was captured.

stdout: str

The standard output that was captured.

created\_by: Optional[str]

The identifier of the actor that created the item.

status: Literal["in\_progress", "completed", "incomplete"]

The status of the shell call output. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

type: Literal["shell\_call\_output"]

The type of the shell call output. Always `shell_call_output`.

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseApplyPatchToolCall: …

A tool call that applies file diffs by creating, deleting, or updating files.

id: str

call\_id: str

operation: Operation

One of the create\_file, delete\_file, or update\_file operations applied via apply\_patch.

class OperationCreateFile: …

Instruction describing how to create a file via the apply\_patch tool.

diff: str

Diff to apply.

path: str

Path of the file to create.

type: Literal["create\_file"]

Create a new file with the provided diff.

class OperationDeleteFile: …

Instruction describing how to delete a file via the apply\_patch tool.

path: str

Path of the file to delete.

type: Literal["delete\_file"]

Delete the specified file.

class OperationUpdateFile: …

Instruction describing how to update a file via the apply\_patch tool.

diff: str

Diff to apply.

path: str

Path of the file to update.

type: Literal["update\_file"]

Update an existing file with the provided diff.

status: Literal["in\_progress", "completed"]

"in\_progress"

"completed"

type: Literal["apply\_patch\_call"]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

created\_by: Optional[str]

The ID of the entity that created this tool call.

class BetaResponseApplyPatchToolCallOutput: …

The output emitted by an apply patch tool call.

id: str

call\_id: str

status: Literal["completed", "failed"]

"completed"

"failed"

type: Literal["apply\_patch\_call\_output"]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

created\_by: Optional[str]

The ID of the entity that created this tool call output.

output: Optional[str]

Optional textual output returned by the apply patch tool.

class McpCall: …

An invocation of a tool on an MCP server.

id: str

arguments: str

name: str

server\_label: str

type: Literal["mcp\_call"]

agent: Optional[McpCallAgent]

agent\_name: str

approval\_request\_id: Optional[str]

error: Optional[str]

output: Optional[str]

status: Optional[Literal["in\_progress", "completed", "incomplete", 2 more]]

"in\_progress"

"completed"

"incomplete"

"calling"

"failed"

class McpListTools: …

A list of tools available on an MCP server.

id: str

server\_label: str

tools: List[McpListToolsTool]

input\_schema: object

name: str

annotations: Optional[object]

description: Optional[str]

type: Literal["mcp\_list\_tools"]

agent: Optional[McpListToolsAgent]

agent\_name: str

error: Optional[str]

class McpApprovalRequest: …

A request for human approval of a tool invocation.

id: str

arguments: str

name: str

server\_label: str

type: Literal["mcp\_approval\_request"]

agent: Optional[McpApprovalRequestAgent]

agent\_name: str

class McpApprovalResponse: …

A response to an MCP approval request.

id: str

approval\_request\_id: str

approve: bool

type: Literal["mcp\_approval\_response"]

agent: Optional[McpApprovalResponseAgent]

agent\_name: str

reason: Optional[str]

class BetaResponseCustomToolCall: …

call\_id: str

An identifier used to map this custom tool call to a tool call output.

input: str

The input for the custom tool call generated by the model.

name: str

The name of the custom tool being called.

type: Literal["custom\_tool\_call"]

The type of the custom tool call. Always `custom_tool_call`.

id: Optional[str]

The unique ID of the custom tool call in the OpenAI platform.

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

namespace: Optional[str]

The namespace of the custom tool being called.

class BetaResponseCustomToolCallOutputItem: …

id: str

The unique ID of the custom tool call output item.

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseOutputItemAddedEvent: …

Emitted when a new output item is added.

item: [BetaResponseOutputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema))

The output item that was added.

output\_index: int

The index of the output item that was added.

sequence\_number: int

The sequence number of this event.

type: Literal["response.output\_item.added"]

The type of the event. Always `response.output_item.added`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseOutputItemDoneEvent: …

Emitted when an output item is marked done.

item: [BetaResponseOutputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema))

The output item that was marked done.

output\_index: int

The index of the output item that was marked done.

sequence\_number: int

The sequence number of this event.

type: Literal["response.output\_item.done"]

The type of the event. Always `response.output_item.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseOutputMessage: …

id: str

content: List[Content]

class BetaResponseOutputText: …

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

logprobs: Optional[List[Logprob]]

token: str

bytes: List[int]

logprob: float

top\_logprobs: List[LogprobTopLogprob]

token: str

bytes: List[int]

logprob: float

class BetaResponseOutputRefusal: …

refusal: str

type: Literal["refusal"]

role: Literal["assistant"]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["message"]

agent: Optional[Agent]

agent\_name: str

phase: Optional[Literal["commentary", "final\_answer"]]

"commentary"

"final\_answer"

class BetaResponseOutputRefusal: …

refusal: str

type: Literal["refusal"]

class BetaResponseOutputText: …

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

logprobs: Optional[List[Logprob]]

token: str

bytes: List[int]

logprob: float

top\_logprobs: List[LogprobTopLogprob]

token: str

bytes: List[int]

logprob: float

class BetaResponseOutputTextAnnotationAddedEvent: …

Emitted when an annotation is added to output text content.

annotation: object

The annotation object being added. (See annotation schema for details.)

annotation\_index: int

The index of the annotation within the content part.

content\_index: int

The index of the content part within the output item.

item\_id: str

The unique identifier of the item to which the annotation is being added.

output\_index: int

The index of the output item in the response’s output array.

sequence\_number: int

The sequence number of this event.

type: Literal["response.output\_text.annotation.added"]

The type of the event. Always ‘response.output\_text.annotation.added’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponsePrompt: …

Reference to a prompt template and its variables.
[Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

id: str

The unique identifier of the prompt template to use.

variables: Optional[Dict[str, Variables]]

Optional map of values to substitute in for variables in your
prompt. The substitution values can either be strings, or other
Response input types like images or files.

str

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

version: Optional[str]

Optional version of the prompt template.

class BetaResponseQueuedEvent: …

Emitted when a response is queued and waiting to be processed.

response: [BetaResponse](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

The full response object that is queued.

sequence\_number: int

The sequence number for this event.

type: Literal["response.queued"]

The type of the event. Always ‘response.queued’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseReasoningItem: …

[managing context](https://platform.openai.com/docs/guides/conversation-state).

id: str

summary: List[Summary]

text: str

type: Literal["summary\_text"]

type: Literal["reasoning"]

agent: Optional[Agent]

agent\_name: str

content: Optional[List[Content]]

text: str

type: Literal["reasoning\_text"]

encrypted\_content: Optional[str]

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class BetaResponseReasoningSummaryPartAddedEvent: …

Emitted when a new reasoning summary part is added.

item\_id: str

The ID of the item this summary part is associated with.

output\_index: int

The index of the output item this summary part is associated with.

part: Part

The summary part that was added.

text: str

The text of the summary part.

type: Literal["summary\_text"]

The type of the summary part. Always `summary_text`.

sequence\_number: int

The sequence number of this event.

summary\_index: int

The index of the summary part within the reasoning summary.

type: Literal["response.reasoning\_summary\_part.added"]

The type of the event. Always `response.reasoning_summary_part.added`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseReasoningSummaryPartDoneEvent: …

Emitted when a reasoning summary part is completed.

item\_id: str

The ID of the item this summary part is associated with.

output\_index: int

The index of the output item this summary part is associated with.

part: Part

The completed summary part.

text: str

The text of the summary part.

type: Literal["summary\_text"]

The type of the summary part. Always `summary_text`.

sequence\_number: int

The sequence number of this event.

summary\_index: int

The index of the summary part within the reasoning summary.

type: Literal["response.reasoning\_summary\_part.done"]

The type of the event. Always `response.reasoning_summary_part.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

status: Optional[Literal["incomplete"]]

The completion status of the summary part. Omitted when the part completed
normally and set to `incomplete` when generation was interrupted.

class BetaResponseReasoningSummaryTextDeltaEvent: …

Emitted when a delta is added to a reasoning summary text.

delta: str

The text delta that was added to the summary.

item\_id: str

The ID of the item this summary text delta is associated with.

output\_index: int

The index of the output item this summary text delta is associated with.

sequence\_number: int

The sequence number of this event.

summary\_index: int

The index of the summary part within the reasoning summary.

type: Literal["response.reasoning\_summary\_text.delta"]

The type of the event. Always `response.reasoning_summary_text.delta`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseReasoningSummaryTextDoneEvent: …

Emitted when a reasoning summary text is completed.

item\_id: str

The ID of the item this summary text is associated with.

output\_index: int

The index of the output item this summary text is associated with.

sequence\_number: int

The sequence number of this event.

summary\_index: int

The index of the summary part within the reasoning summary.

text: str

The full text of the completed reasoning summary.

type: Literal["response.reasoning\_summary\_text.done"]

The type of the event. Always `response.reasoning_summary_text.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseReasoningTextDeltaEvent: …

Emitted when a delta is added to a reasoning text.

content\_index: int

The index of the reasoning content part this delta is associated with.

delta: str

The text delta that was added to the reasoning content.

item\_id: str

The ID of the item this reasoning text delta is associated with.

output\_index: int

The index of the output item this reasoning text delta is associated with.

sequence\_number: int

The sequence number of this event.

type: Literal["response.reasoning\_text.delta"]

The type of the event. Always `response.reasoning_text.delta`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseReasoningTextDoneEvent: …

Emitted when a reasoning text is completed.

content\_index: int

The index of the reasoning content part.

item\_id: str

The ID of the item this reasoning text is associated with.

output\_index: int

The index of the output item this reasoning text is associated with.

sequence\_number: int

The sequence number of this event.

text: str

The full text of the completed reasoning content.

type: Literal["response.reasoning\_text.done"]

The type of the event. Always `response.reasoning_text.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseRefusalDeltaEvent: …

Emitted when there is a partial refusal text.

content\_index: int

The index of the content part that the refusal text is added to.

delta: str

The refusal text that is added.

item\_id: str

The ID of the output item that the refusal text is added to.

output\_index: int

The index of the output item that the refusal text is added to.

sequence\_number: int

The sequence number of this event.

type: Literal["response.refusal.delta"]

The type of the event. Always `response.refusal.delta`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseRefusalDoneEvent: …

Emitted when refusal text is finalized.

content\_index: int

The index of the content part that the refusal text is finalized.

item\_id: str

The ID of the output item that the refusal text is finalized.

output\_index: int

The index of the output item that the refusal text is finalized.

refusal: str

The refusal text that is finalized.

sequence\_number: int

The sequence number of this event.

type: Literal["response.refusal.done"]

The type of the event. Always `response.refusal.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

Literal["completed", "failed", "in\_progress", 3 more]

The status of the response generation. One of `completed`, `failed`,
`in_progress`, `cancelled`, `queued`, or `incomplete`.

"completed"

"failed"

"in\_progress"

"cancelled"

"queued"

"incomplete"

[BetaResponseStreamEvent](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_stream_event%20%3E%20(schema))

Emitted when there is a partial audio response.

class BetaResponseAudioDeltaEvent: …

Emitted when there is a partial audio response.

delta: str

A chunk of Base64 encoded response audio bytes.

sequence\_number: int

A sequence number for this chunk of the stream response.

type: Literal["response.audio.delta"]

The type of the event. Always `response.audio.delta`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseAudioDoneEvent: …

Emitted when the audio response is complete.

sequence\_number: int

The sequence number of the delta.

type: Literal["response.audio.done"]

The type of the event. Always `response.audio.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseAudioTranscriptDeltaEvent: …

Emitted when there is a partial transcript of audio.

delta: str

The partial transcript of the audio response.

sequence\_number: int

The sequence number of this event.

type: Literal["response.audio.transcript.delta"]

The type of the event. Always `response.audio.transcript.delta`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseAudioTranscriptDoneEvent: …

Emitted when the full audio transcript is completed.

sequence\_number: int

The sequence number of this event.

type: Literal["response.audio.transcript.done"]

The type of the event. Always `response.audio.transcript.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseCodeInterpreterCallCodeDeltaEvent: …

Emitted when a partial code snippet is streamed by the code interpreter.

delta: str

The partial code snippet being streamed by the code interpreter.

item\_id: str

The unique identifier of the code interpreter tool call item.

output\_index: int

The index of the output item in the response for which the code is being streamed.

sequence\_number: int

The sequence number of this event, used to order streaming events.

type: Literal["response.code\_interpreter\_call\_code.delta"]

The type of the event. Always `response.code_interpreter_call_code.delta`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseCodeInterpreterCallCodeDoneEvent: …

Emitted when the code snippet is finalized by the code interpreter.

code: str

The final code snippet output by the code interpreter.

item\_id: str

The unique identifier of the code interpreter tool call item.

output\_index: int

The index of the output item in the response for which the code is finalized.

sequence\_number: int

The sequence number of this event, used to order streaming events.

type: Literal["response.code\_interpreter\_call\_code.done"]

The type of the event. Always `response.code_interpreter_call_code.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseCodeInterpreterCallCompletedEvent: …

Emitted when the code interpreter call is completed.

item\_id: str

The unique identifier of the code interpreter tool call item.

output\_index: int

The index of the output item in the response for which the code interpreter call is completed.

sequence\_number: int

The sequence number of this event, used to order streaming events.

type: Literal["response.code\_interpreter\_call.completed"]

The type of the event. Always `response.code_interpreter_call.completed`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseCodeInterpreterCallInProgressEvent: …

Emitted when a code interpreter call is in progress.

item\_id: str

The unique identifier of the code interpreter tool call item.

output\_index: int

The index of the output item in the response for which the code interpreter call is in progress.

sequence\_number: int

The sequence number of this event, used to order streaming events.

type: Literal["response.code\_interpreter\_call.in\_progress"]

The type of the event. Always `response.code_interpreter_call.in_progress`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseCodeInterpreterCallInterpretingEvent: …

Emitted when the code interpreter is actively interpreting the code snippet.

item\_id: str

The unique identifier of the code interpreter tool call item.

output\_index: int

The index of the output item in the response for which the code interpreter is interpreting code.

sequence\_number: int

The sequence number of this event, used to order streaming events.

type: Literal["response.code\_interpreter\_call.interpreting"]

The type of the event. Always `response.code_interpreter_call.interpreting`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseCompletedEvent: …

Emitted when the model response is complete.

response: [BetaResponse](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

Properties of the completed response.

sequence\_number: int

The sequence number for this event.

type: Literal["response.completed"]

The type of the event. Always `response.completed`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseContentPartAddedEvent: …

Emitted when a new content part is added.

content\_index: int

The index of the content part that was added.

item\_id: str

The ID of the output item that the content part was added to.

output\_index: int

The index of the output item that the content part was added to.

part: Part

The content part that was added.

class BetaResponseOutputText: …

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

logprobs: Optional[List[Logprob]]

token: str

bytes: List[int]

logprob: float

top\_logprobs: List[LogprobTopLogprob]

token: str

bytes: List[int]

logprob: float

class BetaResponseOutputRefusal: …

refusal: str

type: Literal["refusal"]

class PartReasoningText: …

text: str

type: Literal["reasoning\_text"]

sequence\_number: int

The sequence number of this event.

type: Literal["response.content\_part.added"]

The type of the event. Always `response.content_part.added`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseContentPartDoneEvent: …

Emitted when a content part is done.

content\_index: int

The index of the content part that is done.

item\_id: str

The ID of the output item that the content part was added to.

output\_index: int

The index of the output item that the content part was added to.

part: Part

The content part that is done.

class BetaResponseOutputText: …

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

logprobs: Optional[List[Logprob]]

token: str

bytes: List[int]

logprob: float

top\_logprobs: List[LogprobTopLogprob]

token: str

bytes: List[int]

logprob: float

class BetaResponseOutputRefusal: …

refusal: str

type: Literal["refusal"]

class PartReasoningText: …

text: str

type: Literal["reasoning\_text"]

sequence\_number: int

The sequence number of this event.

type: Literal["response.content\_part.done"]

The type of the event. Always `response.content_part.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseCreatedEvent: …

An event that is emitted when a response is created.

response: [BetaResponse](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

The response that was created.

sequence\_number: int

The sequence number for this event.

type: Literal["response.created"]

The type of the event. Always `response.created`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseErrorEvent: …

Emitted when an error occurs.

code: Optional[str]

The error code.

message: str

The error message.

param: Optional[str]

The error parameter.

sequence\_number: int

The sequence number of this event.

type: Literal["error"]

The type of the event. Always `error`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseFileSearchCallCompletedEvent: …

Emitted when a file search call is completed (results found).

item\_id: str

The ID of the output item that the file search call is initiated.

output\_index: int

The index of the output item that the file search call is initiated.

sequence\_number: int

The sequence number of this event.

type: Literal["response.file\_search\_call.completed"]

The type of the event. Always `response.file_search_call.completed`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseFileSearchCallInProgressEvent: …

Emitted when a file search call is initiated.

item\_id: str

The ID of the output item that the file search call is initiated.

output\_index: int

The index of the output item that the file search call is initiated.

sequence\_number: int

The sequence number of this event.

type: Literal["response.file\_search\_call.in\_progress"]

The type of the event. Always `response.file_search_call.in_progress`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseFileSearchCallSearchingEvent: …

Emitted when a file search is currently searching.

item\_id: str

The ID of the output item that the file search call is initiated.

output\_index: int

The index of the output item that the file search call is searching.

sequence\_number: int

The sequence number of this event.

type: Literal["response.file\_search\_call.searching"]

The type of the event. Always `response.file_search_call.searching`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseFunctionCallArgumentsDeltaEvent: …

Emitted when there is a partial function-call arguments delta.

delta: str

The function-call arguments delta that is added.

item\_id: str

The ID of the output item that the function-call arguments delta is added to.

output\_index: int

The index of the output item that the function-call arguments delta is added to.

sequence\_number: int

The sequence number of this event.

type: Literal["response.function\_call\_arguments.delta"]

The type of the event. Always `response.function_call_arguments.delta`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseFunctionCallArgumentsDoneEvent: …

Emitted when function-call arguments are finalized.

arguments: str

The function-call arguments.

item\_id: str

The ID of the item.

name: str

The name of the function that was called.

output\_index: int

The index of the output item.

sequence\_number: int

The sequence number of this event.

type: Literal["response.function\_call\_arguments.done"]

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseInProgressEvent: …

Emitted when the response is in progress.

response: [BetaResponse](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

The response that is in progress.

sequence\_number: int

The sequence number of this event.

type: Literal["response.in\_progress"]

The type of the event. Always `response.in_progress`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseFailedEvent: …

An event that is emitted when a response fails.

response: [BetaResponse](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

The response that failed.

sequence\_number: int

The sequence number of this event.

type: Literal["response.failed"]

The type of the event. Always `response.failed`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseIncompleteEvent: …

An event that is emitted when a response finishes as incomplete.

response: [BetaResponse](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

The response that was incomplete.

sequence\_number: int

The sequence number of this event.

type: Literal["response.incomplete"]

The type of the event. Always `response.incomplete`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseOutputItemAddedEvent: …

Emitted when a new output item is added.

item: [BetaResponseOutputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema))

The output item that was added.

output\_index: int

The index of the output item that was added.

sequence\_number: int

The sequence number of this event.

type: Literal["response.output\_item.added"]

The type of the event. Always `response.output_item.added`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseOutputItemDoneEvent: …

Emitted when an output item is marked done.

item: [BetaResponseOutputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema))

The output item that was marked done.

output\_index: int

The index of the output item that was marked done.

sequence\_number: int

The sequence number of this event.

type: Literal["response.output\_item.done"]

The type of the event. Always `response.output_item.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseReasoningSummaryPartAddedEvent: …

Emitted when a new reasoning summary part is added.

item\_id: str

The ID of the item this summary part is associated with.

output\_index: int

The index of the output item this summary part is associated with.

part: Part

The summary part that was added.

text: str

The text of the summary part.

type: Literal["summary\_text"]

The type of the summary part. Always `summary_text`.

sequence\_number: int

The sequence number of this event.

summary\_index: int

The index of the summary part within the reasoning summary.

type: Literal["response.reasoning\_summary\_part.added"]

The type of the event. Always `response.reasoning_summary_part.added`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseReasoningSummaryPartDoneEvent: …

Emitted when a reasoning summary part is completed.

item\_id: str

The ID of the item this summary part is associated with.

output\_index: int

The index of the output item this summary part is associated with.

part: Part

The completed summary part.

text: str

The text of the summary part.

type: Literal["summary\_text"]

The type of the summary part. Always `summary_text`.

sequence\_number: int

The sequence number of this event.

summary\_index: int

The index of the summary part within the reasoning summary.

type: Literal["response.reasoning\_summary\_part.done"]

The type of the event. Always `response.reasoning_summary_part.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

status: Optional[Literal["incomplete"]]

The completion status of the summary part. Omitted when the part completed
normally and set to `incomplete` when generation was interrupted.

class BetaResponseReasoningSummaryTextDeltaEvent: …

Emitted when a delta is added to a reasoning summary text.

delta: str

The text delta that was added to the summary.

item\_id: str

The ID of the item this summary text delta is associated with.

output\_index: int

The index of the output item this summary text delta is associated with.

sequence\_number: int

The sequence number of this event.

summary\_index: int

The index of the summary part within the reasoning summary.

type: Literal["response.reasoning\_summary\_text.delta"]

The type of the event. Always `response.reasoning_summary_text.delta`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseReasoningSummaryTextDoneEvent: …

Emitted when a reasoning summary text is completed.

item\_id: str

The ID of the item this summary text is associated with.

output\_index: int

The index of the output item this summary text is associated with.

sequence\_number: int

The sequence number of this event.

summary\_index: int

The index of the summary part within the reasoning summary.

text: str

The full text of the completed reasoning summary.

type: Literal["response.reasoning\_summary\_text.done"]

The type of the event. Always `response.reasoning_summary_text.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseReasoningTextDeltaEvent: …

Emitted when a delta is added to a reasoning text.

content\_index: int

The index of the reasoning content part this delta is associated with.

delta: str

The text delta that was added to the reasoning content.

item\_id: str

The ID of the item this reasoning text delta is associated with.

output\_index: int

The index of the output item this reasoning text delta is associated with.

sequence\_number: int

The sequence number of this event.

type: Literal["response.reasoning\_text.delta"]

The type of the event. Always `response.reasoning_text.delta`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseReasoningTextDoneEvent: …

Emitted when a reasoning text is completed.

content\_index: int

The index of the reasoning content part.

item\_id: str

The ID of the item this reasoning text is associated with.

output\_index: int

The index of the output item this reasoning text is associated with.

sequence\_number: int

The sequence number of this event.

text: str

The full text of the completed reasoning content.

type: Literal["response.reasoning\_text.done"]

The type of the event. Always `response.reasoning_text.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseRefusalDeltaEvent: …

Emitted when there is a partial refusal text.

content\_index: int

The index of the content part that the refusal text is added to.

delta: str

The refusal text that is added.

item\_id: str

The ID of the output item that the refusal text is added to.

output\_index: int

The index of the output item that the refusal text is added to.

sequence\_number: int

The sequence number of this event.

type: Literal["response.refusal.delta"]

The type of the event. Always `response.refusal.delta`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseRefusalDoneEvent: …

Emitted when refusal text is finalized.

content\_index: int

The index of the content part that the refusal text is finalized.

item\_id: str

The ID of the output item that the refusal text is finalized.

output\_index: int

The index of the output item that the refusal text is finalized.

refusal: str

The refusal text that is finalized.

sequence\_number: int

The sequence number of this event.

type: Literal["response.refusal.done"]

The type of the event. Always `response.refusal.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseTextDeltaEvent: …

Emitted when there is an additional text delta.

content\_index: int

The index of the content part that the text delta was added to.

delta: str

The text delta that was added.

item\_id: str

The ID of the output item that the text delta was added to.

logprobs: List[Logprob]

The log probabilities of the tokens in the delta.

token: str

A possible text token.

logprob: float

The log probability of this token.

top\_logprobs: Optional[List[LogprobTopLogprob]]

The log probabilities of up to 20 of the most likely tokens.

token: Optional[str]

A possible text token.

logprob: Optional[float]

The log probability of this token.

output\_index: int

The index of the output item that the text delta was added to.

sequence\_number: int

The sequence number for this event.

type: Literal["response.output\_text.delta"]

The type of the event. Always `response.output_text.delta`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseTextDoneEvent: …

Emitted when text content is finalized.

content\_index: int

The index of the content part that the text content is finalized.

item\_id: str

The ID of the output item that the text content is finalized.

logprobs: List[Logprob]

The log probabilities of the tokens in the delta.

token: str

A possible text token.

logprob: float

The log probability of this token.

top\_logprobs: Optional[List[LogprobTopLogprob]]

The log probabilities of up to 20 of the most likely tokens.

token: Optional[str]

A possible text token.

logprob: Optional[float]

The log probability of this token.

output\_index: int

The index of the output item that the text content is finalized.

sequence\_number: int

The sequence number for this event.

text: str

The text content that is finalized.

type: Literal["response.output\_text.done"]

The type of the event. Always `response.output_text.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseWebSearchCallCompletedEvent: …

Emitted when a web search call is completed.

item\_id: str

Unique ID for the output item associated with the web search call.

output\_index: int

The index of the output item that the web search call is associated with.

sequence\_number: int

The sequence number of the web search call being processed.

type: Literal["response.web\_search\_call.completed"]

The type of the event. Always `response.web_search_call.completed`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseWebSearchCallInProgressEvent: …

Emitted when a web search call is initiated.

item\_id: str

Unique ID for the output item associated with the web search call.

output\_index: int

The index of the output item that the web search call is associated with.

sequence\_number: int

The sequence number of the web search call being processed.

type: Literal["response.web\_search\_call.in\_progress"]

The type of the event. Always `response.web_search_call.in_progress`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseWebSearchCallSearchingEvent: …

Emitted when a web search call is executing.

item\_id: str

Unique ID for the output item associated with the web search call.

output\_index: int

The index of the output item that the web search call is associated with.

sequence\_number: int

The sequence number of the web search call being processed.

type: Literal["response.web\_search\_call.searching"]

The type of the event. Always `response.web_search_call.searching`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseImageGenCallCompletedEvent: …

Emitted when an image generation tool call has completed and the final image is available.

item\_id: str

The unique identifier of the image generation item being processed.

output\_index: int

The index of the output item in the response’s output array.

sequence\_number: int

The sequence number of this event.

type: Literal["response.image\_generation\_call.completed"]

The type of the event. Always ‘response.image\_generation\_call.completed’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseImageGenCallGeneratingEvent: …

Emitted when an image generation tool call is actively generating an image (intermediate state).

item\_id: str

The unique identifier of the image generation item being processed.

output\_index: int

The index of the output item in the response’s output array.

sequence\_number: int

The sequence number of the image generation item being processed.

type: Literal["response.image\_generation\_call.generating"]

The type of the event. Always ‘response.image\_generation\_call.generating’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseImageGenCallInProgressEvent: …

Emitted when an image generation tool call is in progress.

item\_id: str

The unique identifier of the image generation item being processed.

output\_index: int

The index of the output item in the response’s output array.

sequence\_number: int

The sequence number of the image generation item being processed.

type: Literal["response.image\_generation\_call.in\_progress"]

The type of the event. Always ‘response.image\_generation\_call.in\_progress’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseImageGenCallPartialImageEvent: …

Emitted when a partial image is available during image generation streaming.

item\_id: str

The unique identifier of the image generation item being processed.

output\_index: int

The index of the output item in the response’s output array.

partial\_image\_b64: str

Base64-encoded partial image data, suitable for rendering as an image.

partial\_image\_index: int

0-based index for the partial image (backend is 1-based, but this is 0-based for the user).

sequence\_number: int

The sequence number of the image generation item being processed.

type: Literal["response.image\_generation\_call.partial\_image"]

The type of the event. Always ‘response.image\_generation\_call.partial\_image’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseMcpCallArgumentsDeltaEvent: …

Emitted when there is a delta (partial update) to the arguments of an MCP tool call.

delta: str

A JSON string containing the partial update to the arguments for the MCP tool call.

item\_id: str

The unique identifier of the MCP tool call item being processed.

output\_index: int

The index of the output item in the response’s output array.

sequence\_number: int

The sequence number of this event.

type: Literal["response.mcp\_call\_arguments.delta"]

The type of the event. Always ‘response.mcp\_call\_arguments.delta’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseMcpCallArgumentsDoneEvent: …

Emitted when the arguments for an MCP tool call are finalized.

arguments: str

A JSON string containing the finalized arguments for the MCP tool call.

item\_id: str

The unique identifier of the MCP tool call item being processed.

output\_index: int

The index of the output item in the response’s output array.

sequence\_number: int

The sequence number of this event.

type: Literal["response.mcp\_call\_arguments.done"]

The type of the event. Always ‘response.mcp\_call\_arguments.done’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseMcpCallCompletedEvent: …

Emitted when an MCP tool call has completed successfully.

item\_id: str

The ID of the MCP tool call item that completed.

output\_index: int

The index of the output item that completed.

sequence\_number: int

The sequence number of this event.

type: Literal["response.mcp\_call.completed"]

The type of the event. Always ‘response.mcp\_call.completed’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseMcpCallFailedEvent: …

Emitted when an MCP tool call has failed.

item\_id: str

The ID of the MCP tool call item that failed.

output\_index: int

The index of the output item that failed.

sequence\_number: int

The sequence number of this event.

type: Literal["response.mcp\_call.failed"]

The type of the event. Always ‘response.mcp\_call.failed’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseMcpCallInProgressEvent: …

Emitted when an MCP tool call is in progress.

item\_id: str

The unique identifier of the MCP tool call item being processed.

output\_index: int

The index of the output item in the response’s output array.

sequence\_number: int

The sequence number of this event.

type: Literal["response.mcp\_call.in\_progress"]

The type of the event. Always ‘response.mcp\_call.in\_progress’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseMcpListToolsCompletedEvent: …

Emitted when the list of available MCP tools has been successfully retrieved.

item\_id: str

The ID of the MCP tool call item that produced this output.

output\_index: int

The index of the output item that was processed.

sequence\_number: int

The sequence number of this event.

type: Literal["response.mcp\_list\_tools.completed"]

The type of the event. Always ‘response.mcp\_list\_tools.completed’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseMcpListToolsFailedEvent: …

Emitted when the attempt to list available MCP tools has failed.

item\_id: str

The ID of the MCP tool call item that failed.

output\_index: int

The index of the output item that failed.

sequence\_number: int

The sequence number of this event.

type: Literal["response.mcp\_list\_tools.failed"]

The type of the event. Always ‘response.mcp\_list\_tools.failed’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseMcpListToolsInProgressEvent: …

Emitted when the system is in the process of retrieving the list of available MCP tools.

item\_id: str

The ID of the MCP tool call item that is being processed.

output\_index: int

The index of the output item that is being processed.

sequence\_number: int

The sequence number of this event.

type: Literal["response.mcp\_list\_tools.in\_progress"]

The type of the event. Always ‘response.mcp\_list\_tools.in\_progress’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseOutputTextAnnotationAddedEvent: …

Emitted when an annotation is added to output text content.

annotation: object

The annotation object being added. (See annotation schema for details.)

annotation\_index: int

The index of the annotation within the content part.

content\_index: int

The index of the content part within the output item.

item\_id: str

The unique identifier of the item to which the annotation is being added.

output\_index: int

The index of the output item in the response’s output array.

sequence\_number: int

The sequence number of this event.

type: Literal["response.output\_text.annotation.added"]

The type of the event. Always ‘response.output\_text.annotation.added’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseQueuedEvent: …

Emitted when a response is queued and waiting to be processed.

response: [BetaResponse](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

The full response object that is queued.

sequence\_number: int

The sequence number for this event.

type: Literal["response.queued"]

The type of the event. Always ‘response.queued’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseCustomToolCallInputDeltaEvent: …

Event representing a delta (partial update) to the input of a custom tool call.

delta: str

The incremental input data (delta) for the custom tool call.

item\_id: str

Unique identifier for the API item associated with this event.

output\_index: int

The index of the output this delta applies to.

sequence\_number: int

The sequence number of this event.

type: Literal["response.custom\_tool\_call\_input.delta"]

The event type identifier.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseCustomToolCallInputDoneEvent: …

Event indicating that input for a custom tool call is complete.

input: str

The complete input data for the custom tool call.

item\_id: str

Unique identifier for the API item associated with this event.

output\_index: int

The index of the output this event applies to.

sequence\_number: int

The sequence number of this event.

type: Literal["response.custom\_tool\_call\_input.done"]

The event type identifier.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseTextConfig: …

Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:

* [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
* [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

format: Optional[BetaResponseFormatTextConfig]

An object specifying the format that the model must output.

Configuring `{ "type": "json_schema" }` enables Structured Outputs,
which ensures the model will match your supplied JSON schema. Learn more in the
[Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

The default format is `{ "type": "text" }` with no additional options.

**Not recommended for gpt-4o and newer models:**

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

verbosity: Optional[Literal["low", "medium", "high"]]

Constrains the verbosity of the model’s response. Lower values will result in
more concise responses, while higher values will result in more verbose responses.
Currently supported values are `low`, `medium`, and `high`.

"low"

"medium"

"high"

class BetaResponseTextDeltaEvent: …

Emitted when there is an additional text delta.

content\_index: int

The index of the content part that the text delta was added to.

delta: str

The text delta that was added.

item\_id: str

The ID of the output item that the text delta was added to.

logprobs: List[Logprob]

The log probabilities of the tokens in the delta.

token: str

A possible text token.

logprob: float

The log probability of this token.

top\_logprobs: Optional[List[LogprobTopLogprob]]

The log probabilities of up to 20 of the most likely tokens.

token: Optional[str]

A possible text token.

logprob: Optional[float]

The log probability of this token.

output\_index: int

The index of the output item that the text delta was added to.

sequence\_number: int

The sequence number for this event.

type: Literal["response.output\_text.delta"]

The type of the event. Always `response.output_text.delta`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseTextDoneEvent: …

Emitted when text content is finalized.

content\_index: int

The index of the content part that the text content is finalized.

item\_id: str

The ID of the output item that the text content is finalized.

logprobs: List[Logprob]

The log probabilities of the tokens in the delta.

token: str

A possible text token.

logprob: float

The log probability of this token.

top\_logprobs: Optional[List[LogprobTopLogprob]]

The log probabilities of up to 20 of the most likely tokens.

token: Optional[str]

A possible text token.

logprob: Optional[float]

The log probability of this token.

output\_index: int

The index of the output item that the text content is finalized.

sequence\_number: int

The sequence number for this event.

text: str

The text content that is finalized.

type: Literal["response.output\_text.done"]

The type of the event. Always `response.output_text.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseToolSearchCall: …

id: str

The unique ID of the tool search call item.

arguments: object

Arguments used for the tool search call.

call\_id: Optional[str]

execution: Literal["server", "client"]

"server"

"client"

status: Literal["in\_progress", "completed", "incomplete"]

The status of the tool search call item that was recorded.

"in\_progress"

"completed"

"incomplete"

type: Literal["tool\_search\_call"]

The type of the item. Always `tool_search_call`.

agent: Optional[Agent]

agent\_name: str

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseToolSearchOutputItem: …

id: str

The unique ID of the tool search output item.

call\_id: Optional[str]

execution: Literal["server", "client"]

"server"

"client"

status: Literal["in\_progress", "completed", "incomplete"]

The status of the tool search output item that was recorded.

"in\_progress"

"completed"

"incomplete"

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

The loaded tool definitions returned by tool search.

class BetaFunctionTool: …

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

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

input\_fidelity: Optional[Literal["high", "low"]]

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

type: Literal["tool\_search\_output"]

The type of the item. Always `tool_search_output`.

agent: Optional[Agent]

agent\_name: str

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseToolSearchOutputItemParam: …

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

The loaded tool definitions returned by the tool search output.

class BetaFunctionTool: …

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

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

input\_fidelity: Optional[Literal["high", "low"]]

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

type: Literal["tool\_search\_output"]

The item type. Always `tool_search_output`.

id: Optional[str]

The unique ID of this tool search output.

agent: Optional[Agent]

agent\_name: str

call\_id: Optional[str]

maxLength64

minLength1

execution: Optional[Literal["server", "client"]]

"server"

"client"

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the tool search output.

"in\_progress"

"completed"

"incomplete"

class BetaResponseUsage: …

Represents token usage details including input tokens, output tokens,
a breakdown of output tokens, and the total tokens used.

input\_tokens: int

The number of input tokens.

input\_tokens\_details: InputTokensDetails

A detailed breakdown of the input tokens.

cache\_write\_tokens: int

The number of input tokens that were written to the cache.

cached\_tokens: int

The number of tokens that were retrieved from the cache.
[More on prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

output\_tokens: int

The number of output tokens.

output\_tokens\_details: OutputTokensDetails

A detailed breakdown of the output tokens.

reasoning\_tokens: int

The number of reasoning tokens.

total\_tokens: int

The total number of tokens used.

class BetaResponseWebSearchCallCompletedEvent: …

Emitted when a web search call is completed.

item\_id: str

Unique ID for the output item associated with the web search call.

output\_index: int

The index of the output item that the web search call is associated with.

sequence\_number: int

The sequence number of the web search call being processed.

type: Literal["response.web\_search\_call.completed"]

The type of the event. Always `response.web_search_call.completed`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseWebSearchCallInProgressEvent: …

Emitted when a web search call is initiated.

item\_id: str

Unique ID for the output item associated with the web search call.

output\_index: int

The index of the output item that the web search call is associated with.

sequence\_number: int

The sequence number of the web search call being processed.

type: Literal["response.web\_search\_call.in\_progress"]

The type of the event. Always `response.web_search_call.in_progress`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseWebSearchCallSearchingEvent: …

Emitted when a web search call is executing.

item\_id: str

Unique ID for the output item associated with the web search call.

output\_index: int

The index of the output item that the web search call is associated with.

sequence\_number: int

The sequence number of the web search call being processed.

type: Literal["response.web\_search\_call.searching"]

The type of the event. Always `response.web_search_call.searching`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

[BetaResponsesClientEvent](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_responses_client_event%20%3E%20(schema))

Client events accepted by the Responses WebSocket server.

class ResponseCreate: …

Client event for creating a response over a persistent WebSocket connection.
This payload uses the same top-level fields as `POST /v1/responses`.

Notes:

* `stream` is implicit over WebSocket and should not be sent.
* `background` is not supported over WebSocket.

type: Literal["response.create"]

The type of the client event. Always `response.create`.

background: Optional[bool]

Whether to run the model response in the background.
[Learn more](https://platform.openai.com/docs/guides/background).

context\_management: Optional[List[ResponseCreateContextManagement]]

Context management configuration for this request.

type: str

The context management entry type. Currently only ‘compaction’ is supported.

compact\_threshold: Optional[int]

Token threshold at which compaction should be triggered for this entry.

minimum1000

conversation: Optional[ResponseCreateConversation]

The conversation that this response belongs to. Items from this conversation are prepended to `input_items` for this response request.
Input items and output items from this response are automatically added to this conversation after this response completes.

str

The unique ID of the conversation.

class BetaResponseConversationParam: …

The conversation that this response belongs to.

id: str

The unique ID of the conversation.

include: Optional[List[[BetaResponseIncludable](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_includable%20%3E%20(schema))]]

Specify additional output data to include in the model response. Currently supported values are:

* `web_search_call.action.sources`: Include the sources of the web search tool call.
* `code_interpreter_call.outputs`: Includes the outputs of python code execution in code interpreter tool call items.
* `computer_call_output.output.image_url`: Include image urls from the computer call output.
* `file_search_call.results`: Include the search results of the file search tool call.
* `message.input_image.image_url`: Include image urls from the input message.
* `message.output_text.logprobs`: Include logprobs with assistant messages.
* `reasoning.encrypted_content`: Includes an encrypted version of reasoning tokens in reasoning item outputs. This enables reasoning items to be used in multi-turn conversations when using the Responses API statelessly (like when the `store` parameter is set to `false`, or when an organization is enrolled in the zero data retention program).

"file\_search\_call.results"

"web\_search\_call.results"

"web\_search\_call.action.sources"

"message.input\_image.image\_url"

"computer\_call\_output.output.image\_url"

"code\_interpreter\_call.outputs"

"reasoning.encrypted\_content"

"message.output\_text.logprobs"

input: Optional[Union[str, [BetaResponseInput](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input%20%3E%20(schema)), null]]

Text, image, or file inputs to the model, used to generate a response.

Learn more:

* [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
* [Image inputs](https://platform.openai.com/docs/guides/images)
* [File inputs](https://platform.openai.com/docs/guides/pdf-files)
* [Conversation state](https://platform.openai.com/docs/guides/conversation-state)
* [Function calling](https://platform.openai.com/docs/guides/function-calling)

str

A text input to the model, equivalent to a text input with the
`user` role.

List[[BetaResponseInputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_item%20%3E%20(schema))]

class BetaEasyInputMessage: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: Union[str, [BetaResponseInputMessageContentList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema))]

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

str

List[[BetaResponseInputContent](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_content%20%3E%20(schema))]

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

role: Literal["user", "assistant", "system", "developer"]

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

"user"

"assistant"

"system"

"developer"

phase: Optional[Literal["commentary", "final\_answer"]]

"commentary"

"final\_answer"

type: Optional[Literal["message"]]

The type of the message input. Always `message`.

class Message: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role.

content: [BetaResponseInputMessageContentList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema))

role: Literal["user", "system", "developer"]

"user"

"system"

"developer"

agent: Optional[MessageAgent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

type: Optional[Literal["message"]]

class BetaResponseOutputMessage: …

id: str

content: List[Content]

class BetaResponseOutputText: …

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

logprobs: Optional[List[Logprob]]

token: str

bytes: List[int]

logprob: float

top\_logprobs: List[LogprobTopLogprob]

token: str

bytes: List[int]

logprob: float

class BetaResponseOutputRefusal: …

refusal: str

type: Literal["refusal"]

role: Literal["assistant"]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["message"]

agent: Optional[Agent]

agent\_name: str

phase: Optional[Literal["commentary", "final\_answer"]]

"commentary"

"final\_answer"

class BetaResponseFileSearchToolCall: …

[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

id: str

queries: List[str]

status: Literal["in\_progress", "searching", "completed", 2 more]

"in\_progress"

"searching"

"completed"

"incomplete"

"failed"

type: Literal["file\_search\_call"]

agent: Optional[Agent]

agent\_name: str

results: Optional[List[Result]]

attributes: Optional[Dict[str, Union[str, float, bool]]]

str

float

bool

file\_id: Optional[str]

filename: Optional[str]

score: Optional[float]

formatfloat

text: Optional[str]

class BetaResponseComputerToolCall: …

[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

id: str

call\_id: str

pending\_safety\_checks: List[PendingSafetyCheck]

id: str

code: Optional[str]

message: Optional[str]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["computer\_call"]

action: Optional[BetaComputerAction]

actions: Optional[BetaComputerActionList]

agent: Optional[Agent]

agent\_name: str

class ComputerCallOutput: …

The output of a computer tool call.

call\_id: str

maxLength64

minLength1

output: [BetaResponseComputerToolCallOutputScreenshot](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema))

type: Literal["computer\_call\_output"]

id: Optional[str]

The ID of the computer tool call output.

acknowledged\_safety\_checks: Optional[List[ComputerCallOutputAcknowledgedSafetyCheck]]

The safety checks reported by the API that have been acknowledged by the developer.

id: str

code: Optional[str]

message: Optional[str]

agent: Optional[ComputerCallOutputAgent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the message input. One of `in_progress`, `completed`, or `incomplete`. Populated when input items are returned via API.

"in\_progress"

"completed"

"incomplete"

class BetaResponseFunctionWebSearch: …

[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

id: str

action: Action

class ActionSearch: …

type: Literal["search"]

queries: Optional[List[str]]

Deprecatedquery: Optional[str]

sources: Optional[List[ActionSearchSource]]

type: Literal["url"]

url: str

class ActionOpenPage: …

type: Literal["open\_page"]

url: Optional[str]

class ActionFindInPage: …

pattern: str

type: Literal["find\_in\_page"]

url: str

status: Literal["in\_progress", "searching", "completed", "failed"]

"in\_progress"

"searching"

"completed"

"failed"

type: Literal["web\_search\_call"]

agent: Optional[Agent]

agent\_name: str

class BetaResponseFunctionToolCall: …

[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

arguments: str

A JSON string of the arguments to pass to the function.

call\_id: str

name: str

The name of the function to run.

type: Literal["function\_call"]

The type of the function tool call. Always `function_call`.

id: Optional[str]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

namespace: Optional[str]

The namespace of the function to run.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class FunctionCallOutput: …

The output of a function tool call.

call\_id: str

maxLength64

minLength1

output: Union[str, [BetaResponseFunctionCallOutputItemList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item_list%20%3E%20(schema))]

Text, image, or file output of the function tool call.

str

A JSON string of the output of the function tool call.

List[[BetaResponseFunctionCallOutputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item%20%3E%20(schema))]

class BetaResponseInputTextContent: …

text: str

maxLength10485760

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImageContent: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

type: Literal["input\_image"]

detail: Optional[Literal["low", "high", "auto", "original"]]

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

image\_url: Optional[str]

maxLength20971520

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFileContent: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

The base64-encoded data of the file to be sent to the model.

maxLength73400320

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

type: Literal["function\_call\_output"]

id: Optional[str]

The unique ID of the function tool call output. Populated when this item is returned via API.

agent: Optional[FunctionCallOutputAgent]

agent\_name: str

caller: Optional[FunctionCallOutputCaller]

class FunctionCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class FunctionCallOutputCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

class AgentMessage: …

A message routed between agents.

author: str

content: List[AgentMessageContent]

Plaintext, image, or encrypted content sent between agents.

class BetaResponseInputTextContent: …

text: str

maxLength10485760

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImageContent: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

type: Literal["input\_image"]

detail: Optional[Literal["low", "high", "auto", "original"]]

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

image\_url: Optional[str]

maxLength20971520

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class AgentMessageContentEncryptedContent: …

encrypted\_content: str

maxLength10485760

type: Literal["encrypted\_content"]

recipient: str

type: Literal["agent\_message"]

The item type. Always `agent_message`.

id: Optional[str]

The unique ID of this agent message item.

agent: Optional[AgentMessageAgent]

agent\_name: str

class MultiAgentCall: …

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

The multi-agent action that was executed.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

arguments: str

The action arguments as a JSON string.

call\_id: str

maxLength64

minLength1

type: Literal["multi\_agent\_call"]

The item type. Always `multi_agent_call`.

id: Optional[str]

The unique ID of this multi-agent call.

agent: Optional[MultiAgentCallAgent]

agent\_name: str

class MultiAgentCallOutput: …

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

call\_id: str

maxLength64

minLength1

output: List[MultiAgentCallOutputOutput]

text: str

The text content.

maxLength10485760

type: Literal["output\_text"]

The content type. Always `output_text`.

annotations: Optional[List[MultiAgentCallOutputOutputAnnotation]]

Citations associated with the text content.

class MultiAgentCallOutputOutputAnnotationFileCitation: …

file\_id: str

filename: str

index: int

minimum0

type: Literal["file\_citation"]

The citation type. Always `file_citation`.

class MultiAgentCallOutputOutputAnnotationURLCitation: …

end\_index: int

The index of the last character of the citation in the message.

minimum0

start\_index: int

The index of the first character of the citation in the message.

minimum0

title: str

The title of the cited resource.

type: Literal["url\_citation"]

The citation type. Always `url_citation`.

url: str

The URL of the cited resource.

class MultiAgentCallOutputOutputAnnotationContainerFileCitation: …

container\_id: str

The ID of the container.

end\_index: int

The index of the last character of the citation in the message.

minimum0

file\_id: str

filename: str

start\_index: int

The index of the first character of the citation in the message.

minimum0

type: Literal["container\_file\_citation"]

The citation type. Always `container_file_citation`.

type: Literal["multi\_agent\_call\_output"]

The item type. Always `multi_agent_call_output`.

id: Optional[str]

The unique ID of this multi-agent call output.

agent: Optional[MultiAgentCallOutputAgent]

agent\_name: str

class ToolSearchCall: …

arguments: object

The arguments supplied to the tool search call.

type: Literal["tool\_search\_call"]

The item type. Always `tool_search_call`.

id: Optional[str]

The unique ID of this tool search call.

agent: Optional[ToolSearchCallAgent]

agent\_name: str

call\_id: Optional[str]

maxLength64

minLength1

execution: Optional[Literal["server", "client"]]

"server"

"client"

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the tool search call.

"in\_progress"

"completed"

"incomplete"

class BetaResponseToolSearchOutputItemParam: …

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

The loaded tool definitions returned by the tool search output.

class BetaFunctionTool: …

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

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

input\_fidelity: Optional[Literal["high", "low"]]

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

type: Literal["tool\_search\_output"]

The item type. Always `tool_search_output`.

id: Optional[str]

The unique ID of this tool search output.

agent: Optional[Agent]

agent\_name: str

call\_id: Optional[str]

maxLength64

minLength1

execution: Optional[Literal["server", "client"]]

"server"

"client"

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the tool search output.

"in\_progress"

"completed"

"incomplete"

class AdditionalTools: …

role: Literal["developer"]

The role that provided the additional tools. Only `developer` is supported.

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

A list of additional tools made available at this item.

class BetaFunctionTool: …

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

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

input\_fidelity: Optional[Literal["high", "low"]]

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

type: Literal["additional\_tools"]

The item type. Always `additional_tools`.

id: Optional[str]

The unique ID of this additional tools item.

agent: Optional[AdditionalToolsAgent]

agent\_name: str

class BetaResponseReasoningItem: …

[managing context](https://platform.openai.com/docs/guides/conversation-state).

id: str

summary: List[Summary]

text: str

type: Literal["summary\_text"]

type: Literal["reasoning"]

agent: Optional[Agent]

agent\_name: str

content: Optional[List[Content]]

text: str

type: Literal["reasoning\_text"]

encrypted\_content: Optional[str]

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class BetaResponseCompactionItemParam: …

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

encrypted\_content: str

The encrypted content of the compaction summary.

maxLength10485760

type: Literal["compaction"]

id: Optional[str]

The ID of the compaction item.

agent: Optional[Agent]

agent\_name: str

class ImageGenerationCall: …

An image generation request made by the model.

id: str

result: Optional[str]

status: Literal["in\_progress", "completed", "generating", "failed"]

"in\_progress"

"completed"

"generating"

"failed"

type: Literal["image\_generation\_call"]

agent: Optional[ImageGenerationCallAgent]

agent\_name: str

class BetaResponseCodeInterpreterToolCall: …

id: str

code: Optional[str]

container\_id: str

outputs: Optional[List[Output]]

class OutputLogs: …

logs: str

type: Literal["logs"]

class OutputImage: …

type: Literal["image"]

url: str

status: Literal["in\_progress", "completed", "incomplete", 2 more]

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: Literal["code\_interpreter\_call"]

agent: Optional[Agent]

agent\_name: str

class LocalShellCall: …

A tool call to run a command on the local shell.

id: str

action: LocalShellCallAction

command: List[str]

env: Dict[str, str]

type: Literal["exec"]

timeout\_ms: Optional[int]

user: Optional[str]

working\_directory: Optional[str]

call\_id: str

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["local\_shell\_call"]

agent: Optional[LocalShellCallAgent]

agent\_name: str

class LocalShellCallOutput: …

The output of a local shell tool call.

id: str

output: str

type: Literal["local\_shell\_call\_output"]

agent: Optional[LocalShellCallOutputAgent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class ShellCall: …

A tool representing a request to execute one or more shell commands.

action: ShellCallAction

commands: List[str]

Ordered shell commands for the execution environment to run.

max\_output\_length: Optional[int]

Maximum number of UTF-8 characters to capture from combined stdout and stderr output.

timeout\_ms: Optional[int]

Maximum wall-clock time in milliseconds to allow the shell commands to run.

call\_id: str

maxLength64

minLength1

type: Literal["shell\_call"]

id: Optional[str]

agent: Optional[ShellCallAgent]

agent\_name: str

caller: Optional[ShellCallCaller]

class ShellCallCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ShellCallCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

environment: Optional[ShellCallEnvironment]

The environment to execute the shell commands in.

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class ShellCallOutput: …

The streamed output items emitted by a shell tool call.

call\_id: str

maxLength64

minLength1

output: List[[BetaResponseFunctionShellCallOutputContent](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_shell_call_output_content%20%3E%20(schema))]

Captured chunks of stdout and stderr output, along with their associated outcomes.

outcome: Outcome

The exit or timeout outcome associated with this shell call.

class OutcomeTimeout: …

Indicates that the shell call exceeded its configured time limit.

type: Literal["timeout"]

The outcome type. Always `timeout`.

class OutcomeExit: …

exit\_code: int

The exit code returned by the shell process.

type: Literal["exit"]

stderr: str

Captured stderr output for the shell call.

maxLength10485760

stdout: str

Captured stdout output for the shell call.

maxLength10485760

type: Literal["shell\_call\_output"]

The type of the item. Always `shell_call_output`.

id: Optional[str]

The unique ID of the shell tool call output. Populated when this item is returned via API.

agent: Optional[ShellCallOutputAgent]

agent\_name: str

caller: Optional[ShellCallOutputCaller]

class ShellCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ShellCallOutputCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

max\_output\_length: Optional[int]

The maximum number of UTF-8 characters captured for this shell call’s combined output.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the shell call output.

"in\_progress"

"completed"

"incomplete"

class ApplyPatchCall: …

A tool call representing a request to create, delete, or update files using diff patches.

call\_id: str

maxLength64

minLength1

operation: ApplyPatchCallOperation

The specific create, delete, or update instruction for the apply\_patch tool call.

class ApplyPatchCallOperationCreateFile: …

Instruction for creating a new file via the apply\_patch tool.

diff: str

Unified diff content to apply when creating the file.

maxLength10485760

path: str

Path of the file to create relative to the workspace root.

minLength1

type: Literal["create\_file"]

The operation type. Always `create_file`.

class ApplyPatchCallOperationDeleteFile: …

Instruction for deleting an existing file via the apply\_patch tool.

path: str

Path of the file to delete relative to the workspace root.

minLength1

type: Literal["delete\_file"]

The operation type. Always `delete_file`.

class ApplyPatchCallOperationUpdateFile: …

Instruction for updating an existing file via the apply\_patch tool.

diff: str

Unified diff content to apply to the existing file.

maxLength10485760

path: str

Path of the file to update relative to the workspace root.

minLength1

type: Literal["update\_file"]

The operation type. Always `update_file`.

status: Literal["in\_progress", "completed"]

"in\_progress"

"completed"

type: Literal["apply\_patch\_call"]

id: Optional[str]

agent: Optional[ApplyPatchCallAgent]

agent\_name: str

caller: Optional[ApplyPatchCallCaller]

class ApplyPatchCallCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ApplyPatchCallCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

class ApplyPatchCallOutput: …

The streamed output emitted by an apply patch tool call.

call\_id: str

maxLength64

minLength1

status: Literal["completed", "failed"]

"completed"

"failed"

type: Literal["apply\_patch\_call\_output"]

id: Optional[str]

agent: Optional[ApplyPatchCallOutputAgent]

agent\_name: str

caller: Optional[ApplyPatchCallOutputCaller]

class ApplyPatchCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ApplyPatchCallOutputCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

output: Optional[str]

Optional human-readable log text from the apply patch tool (e.g., patch results or errors).

maxLength10485760

class McpListTools: …

A list of tools available on an MCP server.

id: str

server\_label: str

tools: List[McpListToolsTool]

input\_schema: object

name: str

annotations: Optional[object]

description: Optional[str]

type: Literal["mcp\_list\_tools"]

agent: Optional[McpListToolsAgent]

agent\_name: str

error: Optional[str]

class McpApprovalRequest: …

A request for human approval of a tool invocation.

id: str

arguments: str

name: str

server\_label: str

type: Literal["mcp\_approval\_request"]

agent: Optional[McpApprovalRequestAgent]

agent\_name: str

class McpApprovalResponse: …

A response to an MCP approval request.

approval\_request\_id: str

approve: bool

type: Literal["mcp\_approval\_response"]

id: Optional[str]

agent: Optional[McpApprovalResponseAgent]

agent\_name: str

reason: Optional[str]

class McpCall: …

An invocation of a tool on an MCP server.

id: str

arguments: str

name: str

server\_label: str

type: Literal["mcp\_call"]

agent: Optional[McpCallAgent]

agent\_name: str

approval\_request\_id: Optional[str]

error: Optional[str]

output: Optional[str]

status: Optional[Literal["in\_progress", "completed", "incomplete", 2 more]]

"in\_progress"

"completed"

"incomplete"

"calling"

"failed"

class BetaResponseCustomToolCallOutput: …

call\_id: str

The call ID, used to map this custom tool call output to a custom tool call.

output: Union[str, List[OutputOutputContentList]]

The output from the custom tool call generated by your code.

str

A string of the output of the custom tool call.

List[OutputOutputContentList]

Text, image, or file output of the custom tool call.

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

type: Literal["custom\_tool\_call\_output"]

The type of the custom tool call output. Always `custom_tool_call_output`.

id: Optional[str]

The unique ID of the custom tool call output in the OpenAI platform.

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class CallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

class BetaResponseCustomToolCall: …

call\_id: str

An identifier used to map this custom tool call to a tool call output.

input: str

The input for the custom tool call generated by the model.

name: str

The name of the custom tool being called.

type: Literal["custom\_tool\_call"]

The type of the custom tool call. Always `custom_tool_call`.

id: Optional[str]

The unique ID of the custom tool call in the OpenAI platform.

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

namespace: Optional[str]

The namespace of the custom tool being called.

class CompactionTrigger: …

Compacts the current context. Must be the final input item.

type: Literal["compaction\_trigger"]

The type of the item. Always `compaction_trigger`.

agent: Optional[CompactionTriggerAgent]

agent\_name: str

class ItemReference: …

An internal identifier for an item to reference.

id: str

The ID of the item to reference.

agent: Optional[ItemReferenceAgent]

agent\_name: str

type: Optional[Literal["item\_reference"]]

The type of item to reference. Always `item_reference`.

class Program: …

id: str

The unique ID of this program item.

call\_id: str

maxLength64

minLength1

code: str

maxLength10485760

fingerprint: str

maxLength10485760

type: Literal["program"]

The item type. Always `program`.

agent: Optional[ProgramAgent]

agent\_name: str

class ProgramOutput: …

id: str

The unique ID of this program output item.

call\_id: str

maxLength64

minLength1

result: str

maxLength10485760

status: Literal["completed", "incomplete"]

The terminal status of the program output.

"completed"

"incomplete"

type: Literal["program\_output"]

The item type. Always `program_output`.

agent: Optional[ProgramOutputAgent]

agent\_name: str

instructions: Optional[str]

A system (or developer) message inserted into the model’s context.

When using along with `previous_response_id`, the instructions from a previous
response will not be carried over to the next response. This makes it simple
to swap out system (or developer) messages in new responses.

max\_output\_tokens: Optional[int]

An upper bound for the number of tokens that can be generated for a response, including visible output tokens and [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

minimum16

max\_tool\_calls: Optional[int]

The maximum number of total calls to built-in tools that can be processed in a response. This maximum number applies across all built-in tool calls, not per individual tool. Any further attempts to call a tool by the model will be ignored.

metadata: Optional[Dict[str, str]]

format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: Optional[Union[Literal["gpt-5.6-sol", "gpt-5.6-terra", "gpt-5.6-luna", 92 more], str, null]]

Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model guide](https://platform.openai.com/docs/models)
to browse and compare available models.

Literal["gpt-5.6-sol", "gpt-5.6-terra", "gpt-5.6-luna", 92 more]

Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model guide](https://platform.openai.com/docs/models)
to browse and compare available models.

"gpt-5.6-sol"

"gpt-5.6-terra"

"gpt-5.6-luna"

"gpt-5.4"

"gpt-5.4-mini"

"gpt-5.4-nano"

"gpt-5.4-mini-2026-03-17"

"gpt-5.4-nano-2026-03-17"

"gpt-5.3-chat-latest"

"gpt-5.2"

"gpt-5.2-2025-12-11"

"gpt-5.2-chat-latest"

"gpt-5.2-pro"

"gpt-5.2-pro-2025-12-11"

"gpt-5.1"

"gpt-5.1-2025-11-13"

"gpt-5.1-codex"

"gpt-5.1-mini"

"gpt-5.1-chat-latest"

"gpt-5"

"gpt-5-mini"

"gpt-5-nano"

"gpt-5-2025-08-07"

"gpt-5-mini-2025-08-07"

"gpt-5-nano-2025-08-07"

"gpt-5-chat-latest"

"gpt-4.1"

"gpt-4.1-mini"

"gpt-4.1-nano"

"gpt-4.1-2025-04-14"

"gpt-4.1-mini-2025-04-14"

"gpt-4.1-nano-2025-04-14"

"o4-mini"

"o4-mini-2025-04-16"

"o3"

"o3-2025-04-16"

"o3-mini"

"o3-mini-2025-01-31"

"o1"

"o1-2024-12-17"

"o1-preview"

"o1-preview-2024-09-12"

"o1-mini"

"o1-mini-2024-09-12"

"gpt-4o"

"gpt-4o-2024-11-20"

"gpt-4o-2024-08-06"

"gpt-4o-2024-05-13"

"gpt-4o-audio-preview"

"gpt-4o-audio-preview-2024-10-01"

"gpt-4o-audio-preview-2024-12-17"

"gpt-4o-audio-preview-2025-06-03"

"gpt-4o-mini-audio-preview"

"gpt-4o-mini-audio-preview-2024-12-17"

"gpt-4o-search-preview"

"gpt-4o-mini-search-preview"

"gpt-4o-search-preview-2025-03-11"

"gpt-4o-mini-search-preview-2025-03-11"

"chatgpt-4o-latest"

"codex-mini-latest"

"gpt-4o-mini"

"gpt-4o-mini-2024-07-18"

"gpt-4-turbo"

"gpt-4-turbo-2024-04-09"

"gpt-4-0125-preview"

"gpt-4-turbo-preview"

"gpt-4-1106-preview"

"gpt-4-vision-preview"

"gpt-4"

"gpt-4-0314"

"gpt-4-0613"

"gpt-4-32k"

"gpt-4-32k-0314"

"gpt-4-32k-0613"

"gpt-3.5-turbo"

"gpt-3.5-turbo-16k"

"gpt-3.5-turbo-0301"

"gpt-3.5-turbo-0613"

"gpt-3.5-turbo-1106"

"gpt-3.5-turbo-0125"

"gpt-3.5-turbo-16k-0613"

"o1-pro"

"o1-pro-2025-03-19"

"o3-pro"

"o3-pro-2025-06-10"

"o3-deep-research"

"o3-deep-research-2025-06-26"

"o4-mini-deep-research"

"o4-mini-deep-research-2025-06-26"

"computer-use-preview"

"computer-use-preview-2025-03-11"

"gpt-5-codex"

"gpt-5-pro"

"gpt-5-pro-2025-10-06"

"gpt-5.1-codex-max"

str

moderation: Optional[ResponseCreateModeration]

Configuration for running moderation on the input and output of this response.

model: str

The moderation model to use for moderated completions, e.g. ‘omni-moderation-latest’.

policy: Optional[ResponseCreateModerationPolicy]

The policy to apply to moderated response input and output.

input: Optional[ResponseCreateModerationPolicyInput]

The moderation policy for the response input.

mode: Literal["score", "block"]

"score"

"block"

output: Optional[ResponseCreateModerationPolicyOutput]

The moderation policy for the response output.

mode: Literal["score", "block"]

"score"

"block"

multi\_agent: Optional[ResponseCreateMultiAgent]

Configuration for server-hosted multi-agent execution.

enabled: bool

Whether to enable server-hosted multi-agent execution for this response.

max\_concurrent\_subagents: Optional[int]

`max_concurrent_subagents` sets the maximum number of subagents that can be active simultaneously across the entire agent tree. It includes all descendants—children, grandchildren, and deeper subagents—but excludes the root agent.
The API does not impose a fixed upper bound on this setting. The default is `3`, which is recommended for most workloads. Multi-agent runs also have no fixed limit on tree depth or the total number of subagents created during a run.

minimum1

parallel\_tool\_calls: Optional[bool]

Whether to allow the model to run tool calls in parallel.

previous\_response\_id: Optional[str]

The unique ID of the previous response to the model. Use this to
create multi-turn conversations. Learn more about
[conversation state](https://platform.openai.com/docs/guides/conversation-state). Cannot be used in conjunction with `conversation`.

prompt: Optional[BetaResponsePrompt]

Reference to a prompt template and its variables.
[Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).

prompt\_cache\_key: Optional[str]

Used by OpenAI to cache responses for similar requests to optimize your cache hit rates. Replaces the `user` field. [Learn more](https://platform.openai.com/docs/guides/prompt-caching).

prompt\_cache\_options: Optional[ResponseCreatePromptCacheOptions]

Options for prompt caching. Supported for `gpt-5.6` and later models. By default, OpenAI automatically chooses one implicit cache breakpoint. You can add explicit breakpoints to content blocks with `prompt_cache_breakpoint`. Each request can write up to four breakpoints. For cache matching, OpenAI considers up to the latest 80 breakpoints in the conversation, without a content-block lookback limit. Set `mode` to `explicit` to disable the implicit breakpoint. The `ttl` defaults to `30m`, which is currently the only supported value. See the [prompt caching guide](https://platform.openai.com/docs/guides/prompt-caching) for current details.

mode: Optional[Literal["implicit", "explicit"]]

Controls whether OpenAI automatically creates an implicit cache breakpoint. Defaults to `implicit`. With `implicit`, OpenAI creates one implicit breakpoint and writes up to the latest three explicit breakpoints in the request. With `explicit`, OpenAI does not create an implicit breakpoint and writes up to the latest four explicit breakpoints. If there are no explicit breakpoints, the request does not use prompt caching.

"implicit"

"explicit"

ttl: Optional[Literal["30m"]]

The minimum lifetime applied to every implicit and explicit cache breakpoint written by the request. Defaults to `30m`, which is currently the only supported value. The backend may retain cache entries for longer.

Deprecatedprompt\_cache\_retention: Optional[Literal["in\_memory", "24h"]]

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

reasoning: Optional[ResponseCreateReasoning]

**gpt-5 and o-series models only**

Configuration options for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).

context: Optional[Literal["auto", "current\_turn", "all\_turns"]]

Controls which reasoning items are rendered back to the model on later turns.
When returned on a response, this is the effective reasoning context mode
used for the response.

"auto"

"current\_turn"

"all\_turns"

effort: Optional[Literal["none", "minimal", "low", 4 more]]

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

Deprecatedgenerate\_summary: Optional[Literal["auto", "concise", "detailed"]]

**Deprecated:** use `summary` instead.

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

"auto"

"concise"

"detailed"

mode: Optional[Union[str, Literal["standard", "pro"], null]]

Controls the reasoning execution mode for the request.

When returned on a response, this is the effective execution mode.

str

Literal["standard", "pro"]

Controls the reasoning execution mode for the request.

When returned on a response, this is the effective execution mode.

"standard"

"pro"

summary: Optional[Literal["auto", "concise", "detailed"]]

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

`concise` is supported for `computer-use-preview` models and all reasoning models after `gpt-5`.

"auto"

"concise"

"detailed"

safety\_identifier: Optional[str]

A stable identifier used to help detect users of your application that may be violating OpenAI’s usage policies.
The IDs should be a string that uniquely identifies each user, with a maximum length of 64 characters. We recommend hashing their username or email address, in order to avoid sending us any identifying information. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

maxLength64

service\_tier: Optional[Literal["auto", "default", "flex", 2 more]]

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

store: Optional[bool]

Whether to store the generated model response for later retrieval via
API.

stream: Optional[bool]

If set to true, the model response data will be streamed to the client
as it is generated using [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format).
See the [Streaming section below](https://platform.openai.com/docs/api-reference/responses-streaming)
for more information.

stream\_options: Optional[ResponseCreateStreamOptions]

Options for streaming responses. Only set this when you set `stream: true`.

include\_obfuscation: Optional[bool]

When true, stream obfuscation will be enabled. Stream obfuscation adds
random characters to an `obfuscation` field on streaming delta events to
normalize payload sizes as a mitigation to certain side-channel attacks.
These obfuscation fields are included by default, but add a small amount
of overhead to the data stream. You can set `include_obfuscation` to
false to optimize for bandwidth if you trust the network links between
your application and the OpenAI API.

temperature: Optional[float]

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
We generally recommend altering this or `top_p` but not both.

minimum0

maximum2

text: Optional[BetaResponseTextConfig]

Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:

* [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
* [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

tool\_choice: Optional[ResponseCreateToolChoice]

How the model should select which tool (or tools) to use when generating
a response. See the `tools` parameter to see how to specify which tools
the model can call.

Literal["none", "auto", "required"]

"none"

"auto"

"required"

class BetaToolChoiceAllowed: …

Constrains the tools available to the model to a pre-defined set.

mode: Literal["auto", "required"]

Constrains the tools available to the model to a pre-defined set.

`auto` allows the model to pick from among the allowed tools and generate a
message.

`required` requires the model to call one or more of the allowed tools.

"auto"

"required"

tools: List[Dict[str, object]]

A list of tool definitions that the model should be allowed to call.

For the Responses API, the list of tool definitions might look like:

  { "type": "function", "name": "get_weather" },
  { "type": "mcp", "server_label": "deepwiki" },
  { "type": "image_generation" }

type: Literal["allowed\_tools"]

Allowed tool configuration type. Always `allowed_tools`.

class BetaToolChoiceTypes: …

Indicates that the model should use a built-in tool to generate a response.
[Learn more about built-in tools](https://platform.openai.com/docs/guides/tools).

type: Literal["file\_search", "web\_search\_preview", "computer", 5 more]

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

class BetaToolChoiceFunction: …

Use this option to force the model to call a specific function.

name: str

type: Literal["function"]

For function calling, the type is always `function`.

class BetaToolChoiceMcp: …

Use this option to force the model to call a specific tool on a remote MCP server.

server\_label: str

The label of the MCP server to use.

type: Literal["mcp"]

For MCP tools, the type is always `mcp`.

name: Optional[str]

The name of the tool to call on the server.

class BetaToolChoiceCustom: …

Use this option to force the model to call a specific custom tool.

name: str

The name of the custom tool to call.

type: Literal["custom"]

For custom tool calling, the type is always `custom`.

class ResponseCreateToolChoiceBetaSpecificProgrammaticToolCallingParam: …

type: Literal["programmatic\_tool\_calling"]

The tool to call. Always `programmatic_tool_calling`.

class BetaToolChoiceApplyPatch: …

Forces the model to call the apply\_patch tool when executing a tool call.

type: Literal["apply\_patch"]

The tool to call. Always `apply_patch`.

class BetaToolChoiceShell: …

Forces the model to call the shell tool when a tool call is required.

type: Literal["shell"]

The tool to call. Always `shell`.

tools: Optional[List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]]

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

class BetaFunctionTool: …

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

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

input\_fidelity: Optional[Literal["high", "low"]]

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

top\_logprobs: Optional[int]

An integer between 0 and 20 specifying the maximum number of most likely
tokens to return at each token position, each with an associated log
probability. In some cases, the number of returned tokens may be fewer than
requested.

minimum0

maximum20

top\_p: Optional[float]

An alternative to sampling with temperature, called nucleus sampling,
where the model considers the results of the tokens with top\_p probability
mass. So 0.1 means only the tokens comprising the top 10% probability mass
are considered.

We generally recommend altering this or `temperature` but not both.

minimum0

maximum1

Deprecatedtruncation: Optional[Literal["auto", "disabled"]]

The truncation strategy to use for the model response.

* `auto`: If the input to this Response exceeds
  the model’s context window size, the model will truncate the
  response to fit the context window by dropping items from the beginning of the conversation.
* `disabled` (default): If the input size will exceed the context window
  size for a model, the request will fail with a 400 error.

"auto"

"disabled"

Deprecateduser: Optional[str]

This field is being replaced by `safety_identifier` and `prompt_cache_key`. Use `prompt_cache_key` instead to maintain caching optimizations.
A stable identifier for your end-users.
Used to boost cache hit rates by better bucketing similar requests and to help OpenAI detect and prevent abuse. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

class BetaResponseInjectEvent: …

Injects input items into an active response over a WebSocket connection.
The items are validated and committed atomically. Currently, the server
accepts client-owned tool outputs that resume a waiting agent.

input: List[[BetaResponseInputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_item%20%3E%20(schema))]

Input items to inject into the active response.

class BetaEasyInputMessage: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: Union[str, [BetaResponseInputMessageContentList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema))]

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

str

List[[BetaResponseInputContent](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_content%20%3E%20(schema))]

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

role: Literal["user", "assistant", "system", "developer"]

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

"user"

"assistant"

"system"

"developer"

phase: Optional[Literal["commentary", "final\_answer"]]

"commentary"

"final\_answer"

type: Optional[Literal["message"]]

The type of the message input. Always `message`.

class Message: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role.

content: [BetaResponseInputMessageContentList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema))

role: Literal["user", "system", "developer"]

"user"

"system"

"developer"

agent: Optional[MessageAgent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

type: Optional[Literal["message"]]

class BetaResponseOutputMessage: …

id: str

content: List[Content]

class BetaResponseOutputText: …

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

logprobs: Optional[List[Logprob]]

token: str

bytes: List[int]

logprob: float

top\_logprobs: List[LogprobTopLogprob]

token: str

bytes: List[int]

logprob: float

class BetaResponseOutputRefusal: …

refusal: str

type: Literal["refusal"]

role: Literal["assistant"]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["message"]

agent: Optional[Agent]

agent\_name: str

phase: Optional[Literal["commentary", "final\_answer"]]

"commentary"

"final\_answer"

class BetaResponseFileSearchToolCall: …

[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

id: str

queries: List[str]

status: Literal["in\_progress", "searching", "completed", 2 more]

"in\_progress"

"searching"

"completed"

"incomplete"

"failed"

type: Literal["file\_search\_call"]

agent: Optional[Agent]

agent\_name: str

results: Optional[List[Result]]

attributes: Optional[Dict[str, Union[str, float, bool]]]

str

float

bool

file\_id: Optional[str]

filename: Optional[str]

score: Optional[float]

formatfloat

text: Optional[str]

class BetaResponseComputerToolCall: …

[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

id: str

call\_id: str

pending\_safety\_checks: List[PendingSafetyCheck]

id: str

code: Optional[str]

message: Optional[str]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["computer\_call"]

action: Optional[BetaComputerAction]

actions: Optional[BetaComputerActionList]

agent: Optional[Agent]

agent\_name: str

class ComputerCallOutput: …

The output of a computer tool call.

call\_id: str

maxLength64

minLength1

output: [BetaResponseComputerToolCallOutputScreenshot](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema))

type: Literal["computer\_call\_output"]

id: Optional[str]

The ID of the computer tool call output.

acknowledged\_safety\_checks: Optional[List[ComputerCallOutputAcknowledgedSafetyCheck]]

The safety checks reported by the API that have been acknowledged by the developer.

id: str

code: Optional[str]

message: Optional[str]

agent: Optional[ComputerCallOutputAgent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the message input. One of `in_progress`, `completed`, or `incomplete`. Populated when input items are returned via API.

"in\_progress"

"completed"

"incomplete"

class BetaResponseFunctionWebSearch: …

[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

id: str

action: Action

class ActionSearch: …

type: Literal["search"]

queries: Optional[List[str]]

Deprecatedquery: Optional[str]

sources: Optional[List[ActionSearchSource]]

type: Literal["url"]

url: str

class ActionOpenPage: …

type: Literal["open\_page"]

url: Optional[str]

class ActionFindInPage: …

pattern: str

type: Literal["find\_in\_page"]

url: str

status: Literal["in\_progress", "searching", "completed", "failed"]

"in\_progress"

"searching"

"completed"

"failed"

type: Literal["web\_search\_call"]

agent: Optional[Agent]

agent\_name: str

class BetaResponseFunctionToolCall: …

[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

arguments: str

A JSON string of the arguments to pass to the function.

call\_id: str

name: str

The name of the function to run.

type: Literal["function\_call"]

The type of the function tool call. Always `function_call`.

id: Optional[str]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

namespace: Optional[str]

The namespace of the function to run.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class FunctionCallOutput: …

The output of a function tool call.

call\_id: str

maxLength64

minLength1

output: Union[str, [BetaResponseFunctionCallOutputItemList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item_list%20%3E%20(schema))]

Text, image, or file output of the function tool call.

str

A JSON string of the output of the function tool call.

List[[BetaResponseFunctionCallOutputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item%20%3E%20(schema))]

class BetaResponseInputTextContent: …

text: str

maxLength10485760

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImageContent: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

type: Literal["input\_image"]

detail: Optional[Literal["low", "high", "auto", "original"]]

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

image\_url: Optional[str]

maxLength20971520

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFileContent: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

The base64-encoded data of the file to be sent to the model.

maxLength73400320

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

type: Literal["function\_call\_output"]

id: Optional[str]

The unique ID of the function tool call output. Populated when this item is returned via API.

agent: Optional[FunctionCallOutputAgent]

agent\_name: str

caller: Optional[FunctionCallOutputCaller]

class FunctionCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class FunctionCallOutputCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

class AgentMessage: …

A message routed between agents.

author: str

content: List[AgentMessageContent]

Plaintext, image, or encrypted content sent between agents.

class BetaResponseInputTextContent: …

text: str

maxLength10485760

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImageContent: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

type: Literal["input\_image"]

detail: Optional[Literal["low", "high", "auto", "original"]]

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

image\_url: Optional[str]

maxLength20971520

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class AgentMessageContentEncryptedContent: …

encrypted\_content: str

maxLength10485760

type: Literal["encrypted\_content"]

recipient: str

type: Literal["agent\_message"]

The item type. Always `agent_message`.

id: Optional[str]

The unique ID of this agent message item.

agent: Optional[AgentMessageAgent]

agent\_name: str

class MultiAgentCall: …

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

The multi-agent action that was executed.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

arguments: str

The action arguments as a JSON string.

call\_id: str

maxLength64

minLength1

type: Literal["multi\_agent\_call"]

The item type. Always `multi_agent_call`.

id: Optional[str]

The unique ID of this multi-agent call.

agent: Optional[MultiAgentCallAgent]

agent\_name: str

class MultiAgentCallOutput: …

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

call\_id: str

maxLength64

minLength1

output: List[MultiAgentCallOutputOutput]

text: str

The text content.

maxLength10485760

type: Literal["output\_text"]

The content type. Always `output_text`.

annotations: Optional[List[MultiAgentCallOutputOutputAnnotation]]

Citations associated with the text content.

class MultiAgentCallOutputOutputAnnotationFileCitation: …

file\_id: str

filename: str

index: int

minimum0

type: Literal["file\_citation"]

The citation type. Always `file_citation`.

class MultiAgentCallOutputOutputAnnotationURLCitation: …

end\_index: int

The index of the last character of the citation in the message.

minimum0

start\_index: int

The index of the first character of the citation in the message.

minimum0

title: str

The title of the cited resource.

type: Literal["url\_citation"]

The citation type. Always `url_citation`.

url: str

The URL of the cited resource.

class MultiAgentCallOutputOutputAnnotationContainerFileCitation: …

container\_id: str

The ID of the container.

end\_index: int

The index of the last character of the citation in the message.

minimum0

file\_id: str

filename: str

start\_index: int

The index of the first character of the citation in the message.

minimum0

type: Literal["container\_file\_citation"]

The citation type. Always `container_file_citation`.

type: Literal["multi\_agent\_call\_output"]

The item type. Always `multi_agent_call_output`.

id: Optional[str]

The unique ID of this multi-agent call output.

agent: Optional[MultiAgentCallOutputAgent]

agent\_name: str

class ToolSearchCall: …

arguments: object

The arguments supplied to the tool search call.

type: Literal["tool\_search\_call"]

The item type. Always `tool_search_call`.

id: Optional[str]

The unique ID of this tool search call.

agent: Optional[ToolSearchCallAgent]

agent\_name: str

call\_id: Optional[str]

maxLength64

minLength1

execution: Optional[Literal["server", "client"]]

"server"

"client"

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the tool search call.

"in\_progress"

"completed"

"incomplete"

class BetaResponseToolSearchOutputItemParam: …

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

The loaded tool definitions returned by the tool search output.

class BetaFunctionTool: …

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

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

input\_fidelity: Optional[Literal["high", "low"]]

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

type: Literal["tool\_search\_output"]

The item type. Always `tool_search_output`.

id: Optional[str]

The unique ID of this tool search output.

agent: Optional[Agent]

agent\_name: str

call\_id: Optional[str]

maxLength64

minLength1

execution: Optional[Literal["server", "client"]]

"server"

"client"

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the tool search output.

"in\_progress"

"completed"

"incomplete"

class AdditionalTools: …

role: Literal["developer"]

The role that provided the additional tools. Only `developer` is supported.

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

A list of additional tools made available at this item.

class BetaFunctionTool: …

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

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

input\_fidelity: Optional[Literal["high", "low"]]

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

type: Literal["additional\_tools"]

The item type. Always `additional_tools`.

id: Optional[str]

The unique ID of this additional tools item.

agent: Optional[AdditionalToolsAgent]

agent\_name: str

class BetaResponseReasoningItem: …

[managing context](https://platform.openai.com/docs/guides/conversation-state).

id: str

summary: List[Summary]

text: str

type: Literal["summary\_text"]

type: Literal["reasoning"]

agent: Optional[Agent]

agent\_name: str

content: Optional[List[Content]]

text: str

type: Literal["reasoning\_text"]

encrypted\_content: Optional[str]

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class BetaResponseCompactionItemParam: …

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

encrypted\_content: str

The encrypted content of the compaction summary.

maxLength10485760

type: Literal["compaction"]

id: Optional[str]

The ID of the compaction item.

agent: Optional[Agent]

agent\_name: str

class ImageGenerationCall: …

An image generation request made by the model.

id: str

result: Optional[str]

status: Literal["in\_progress", "completed", "generating", "failed"]

"in\_progress"

"completed"

"generating"

"failed"

type: Literal["image\_generation\_call"]

agent: Optional[ImageGenerationCallAgent]

agent\_name: str

class BetaResponseCodeInterpreterToolCall: …

id: str

code: Optional[str]

container\_id: str

outputs: Optional[List[Output]]

class OutputLogs: …

logs: str

type: Literal["logs"]

class OutputImage: …

type: Literal["image"]

url: str

status: Literal["in\_progress", "completed", "incomplete", 2 more]

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: Literal["code\_interpreter\_call"]

agent: Optional[Agent]

agent\_name: str

class LocalShellCall: …

A tool call to run a command on the local shell.

id: str

action: LocalShellCallAction

command: List[str]

env: Dict[str, str]

type: Literal["exec"]

timeout\_ms: Optional[int]

user: Optional[str]

working\_directory: Optional[str]

call\_id: str

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["local\_shell\_call"]

agent: Optional[LocalShellCallAgent]

agent\_name: str

class LocalShellCallOutput: …

The output of a local shell tool call.

id: str

output: str

type: Literal["local\_shell\_call\_output"]

agent: Optional[LocalShellCallOutputAgent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class ShellCall: …

A tool representing a request to execute one or more shell commands.

action: ShellCallAction

commands: List[str]

Ordered shell commands for the execution environment to run.

max\_output\_length: Optional[int]

Maximum number of UTF-8 characters to capture from combined stdout and stderr output.

timeout\_ms: Optional[int]

Maximum wall-clock time in milliseconds to allow the shell commands to run.

call\_id: str

maxLength64

minLength1

type: Literal["shell\_call"]

id: Optional[str]

agent: Optional[ShellCallAgent]

agent\_name: str

caller: Optional[ShellCallCaller]

class ShellCallCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ShellCallCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

environment: Optional[ShellCallEnvironment]

The environment to execute the shell commands in.

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class ShellCallOutput: …

The streamed output items emitted by a shell tool call.

call\_id: str

maxLength64

minLength1

output: List[[BetaResponseFunctionShellCallOutputContent](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_shell_call_output_content%20%3E%20(schema))]

Captured chunks of stdout and stderr output, along with their associated outcomes.

outcome: Outcome

The exit or timeout outcome associated with this shell call.

class OutcomeTimeout: …

Indicates that the shell call exceeded its configured time limit.

type: Literal["timeout"]

The outcome type. Always `timeout`.

class OutcomeExit: …

exit\_code: int

The exit code returned by the shell process.

type: Literal["exit"]

stderr: str

Captured stderr output for the shell call.

maxLength10485760

stdout: str

Captured stdout output for the shell call.

maxLength10485760

type: Literal["shell\_call\_output"]

The type of the item. Always `shell_call_output`.

id: Optional[str]

The unique ID of the shell tool call output. Populated when this item is returned via API.

agent: Optional[ShellCallOutputAgent]

agent\_name: str

caller: Optional[ShellCallOutputCaller]

class ShellCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ShellCallOutputCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

max\_output\_length: Optional[int]

The maximum number of UTF-8 characters captured for this shell call’s combined output.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the shell call output.

"in\_progress"

"completed"

"incomplete"

class ApplyPatchCall: …

A tool call representing a request to create, delete, or update files using diff patches.

call\_id: str

maxLength64

minLength1

operation: ApplyPatchCallOperation

The specific create, delete, or update instruction for the apply\_patch tool call.

class ApplyPatchCallOperationCreateFile: …

Instruction for creating a new file via the apply\_patch tool.

diff: str

Unified diff content to apply when creating the file.

maxLength10485760

path: str

Path of the file to create relative to the workspace root.

minLength1

type: Literal["create\_file"]

The operation type. Always `create_file`.

class ApplyPatchCallOperationDeleteFile: …

Instruction for deleting an existing file via the apply\_patch tool.

path: str

Path of the file to delete relative to the workspace root.

minLength1

type: Literal["delete\_file"]

The operation type. Always `delete_file`.

class ApplyPatchCallOperationUpdateFile: …

Instruction for updating an existing file via the apply\_patch tool.

diff: str

Unified diff content to apply to the existing file.

maxLength10485760

path: str

Path of the file to update relative to the workspace root.

minLength1

type: Literal["update\_file"]

The operation type. Always `update_file`.

status: Literal["in\_progress", "completed"]

"in\_progress"

"completed"

type: Literal["apply\_patch\_call"]

id: Optional[str]

agent: Optional[ApplyPatchCallAgent]

agent\_name: str

caller: Optional[ApplyPatchCallCaller]

class ApplyPatchCallCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ApplyPatchCallCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

class ApplyPatchCallOutput: …

The streamed output emitted by an apply patch tool call.

call\_id: str

maxLength64

minLength1

status: Literal["completed", "failed"]

"completed"

"failed"

type: Literal["apply\_patch\_call\_output"]

id: Optional[str]

agent: Optional[ApplyPatchCallOutputAgent]

agent\_name: str

caller: Optional[ApplyPatchCallOutputCaller]

class ApplyPatchCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ApplyPatchCallOutputCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

output: Optional[str]

Optional human-readable log text from the apply patch tool (e.g., patch results or errors).

maxLength10485760

class McpListTools: …

A list of tools available on an MCP server.

id: str

server\_label: str

tools: List[McpListToolsTool]

input\_schema: object

name: str

annotations: Optional[object]

description: Optional[str]

type: Literal["mcp\_list\_tools"]

agent: Optional[McpListToolsAgent]

agent\_name: str

error: Optional[str]

class McpApprovalRequest: …

A request for human approval of a tool invocation.

id: str

arguments: str

name: str

server\_label: str

type: Literal["mcp\_approval\_request"]

agent: Optional[McpApprovalRequestAgent]

agent\_name: str

class McpApprovalResponse: …

A response to an MCP approval request.

approval\_request\_id: str

approve: bool

type: Literal["mcp\_approval\_response"]

id: Optional[str]

agent: Optional[McpApprovalResponseAgent]

agent\_name: str

reason: Optional[str]

class McpCall: …

An invocation of a tool on an MCP server.

id: str

arguments: str

name: str

server\_label: str

type: Literal["mcp\_call"]

agent: Optional[McpCallAgent]

agent\_name: str

approval\_request\_id: Optional[str]

error: Optional[str]

output: Optional[str]

status: Optional[Literal["in\_progress", "completed", "incomplete", 2 more]]

"in\_progress"

"completed"

"incomplete"

"calling"

"failed"

class BetaResponseCustomToolCallOutput: …

call\_id: str

The call ID, used to map this custom tool call output to a custom tool call.

output: Union[str, List[OutputOutputContentList]]

The output from the custom tool call generated by your code.

str

A string of the output of the custom tool call.

List[OutputOutputContentList]

Text, image, or file output of the custom tool call.

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

type: Literal["custom\_tool\_call\_output"]

The type of the custom tool call output. Always `custom_tool_call_output`.

id: Optional[str]

The unique ID of the custom tool call output in the OpenAI platform.

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class CallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

class BetaResponseCustomToolCall: …

call\_id: str

An identifier used to map this custom tool call to a tool call output.

input: str

The input for the custom tool call generated by the model.

name: str

The name of the custom tool being called.

type: Literal["custom\_tool\_call"]

The type of the custom tool call. Always `custom_tool_call`.

id: Optional[str]

The unique ID of the custom tool call in the OpenAI platform.

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

namespace: Optional[str]

The namespace of the custom tool being called.

class CompactionTrigger: …

Compacts the current context. Must be the final input item.

type: Literal["compaction\_trigger"]

The type of the item. Always `compaction_trigger`.

agent: Optional[CompactionTriggerAgent]

agent\_name: str

class ItemReference: …

An internal identifier for an item to reference.

id: str

The ID of the item to reference.

agent: Optional[ItemReferenceAgent]

agent\_name: str

type: Optional[Literal["item\_reference"]]

The type of item to reference. Always `item_reference`.

class Program: …

id: str

The unique ID of this program item.

call\_id: str

maxLength64

minLength1

code: str

maxLength10485760

fingerprint: str

maxLength10485760

type: Literal["program"]

The item type. Always `program`.

agent: Optional[ProgramAgent]

agent\_name: str

class ProgramOutput: …

id: str

The unique ID of this program output item.

call\_id: str

maxLength64

minLength1

result: str

maxLength10485760

status: Literal["completed", "incomplete"]

The terminal status of the program output.

"completed"

"incomplete"

type: Literal["program\_output"]

The item type. Always `program_output`.

agent: Optional[ProgramOutputAgent]

agent\_name: str

response\_id: str

The ID of the active response that should receive the input.

type: Literal["response.inject"]

The event discriminator. Always `response.inject`.

[BetaResponsesServerEvent](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_responses_server_event%20%3E%20(schema))

Server events emitted by the Responses WebSocket server.

class BetaResponseAudioDeltaEvent: …

Emitted when there is a partial audio response.

delta: str

A chunk of Base64 encoded response audio bytes.

sequence\_number: int

A sequence number for this chunk of the stream response.

type: Literal["response.audio.delta"]

The type of the event. Always `response.audio.delta`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseAudioDoneEvent: …

Emitted when the audio response is complete.

sequence\_number: int

The sequence number of the delta.

type: Literal["response.audio.done"]

The type of the event. Always `response.audio.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseAudioTranscriptDeltaEvent: …

Emitted when there is a partial transcript of audio.

delta: str

The partial transcript of the audio response.

sequence\_number: int

The sequence number of this event.

type: Literal["response.audio.transcript.delta"]

The type of the event. Always `response.audio.transcript.delta`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseAudioTranscriptDoneEvent: …

Emitted when the full audio transcript is completed.

sequence\_number: int

The sequence number of this event.

type: Literal["response.audio.transcript.done"]

The type of the event. Always `response.audio.transcript.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseCodeInterpreterCallCodeDeltaEvent: …

Emitted when a partial code snippet is streamed by the code interpreter.

delta: str

The partial code snippet being streamed by the code interpreter.

item\_id: str

The unique identifier of the code interpreter tool call item.

output\_index: int

The index of the output item in the response for which the code is being streamed.

sequence\_number: int

The sequence number of this event, used to order streaming events.

type: Literal["response.code\_interpreter\_call\_code.delta"]

The type of the event. Always `response.code_interpreter_call_code.delta`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseCodeInterpreterCallCodeDoneEvent: …

Emitted when the code snippet is finalized by the code interpreter.

code: str

The final code snippet output by the code interpreter.

item\_id: str

The unique identifier of the code interpreter tool call item.

output\_index: int

The index of the output item in the response for which the code is finalized.

sequence\_number: int

The sequence number of this event, used to order streaming events.

type: Literal["response.code\_interpreter\_call\_code.done"]

The type of the event. Always `response.code_interpreter_call_code.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseCodeInterpreterCallCompletedEvent: …

Emitted when the code interpreter call is completed.

item\_id: str

The unique identifier of the code interpreter tool call item.

output\_index: int

The index of the output item in the response for which the code interpreter call is completed.

sequence\_number: int

The sequence number of this event, used to order streaming events.

type: Literal["response.code\_interpreter\_call.completed"]

The type of the event. Always `response.code_interpreter_call.completed`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseCodeInterpreterCallInProgressEvent: …

Emitted when a code interpreter call is in progress.

item\_id: str

The unique identifier of the code interpreter tool call item.

output\_index: int

The index of the output item in the response for which the code interpreter call is in progress.

sequence\_number: int

The sequence number of this event, used to order streaming events.

type: Literal["response.code\_interpreter\_call.in\_progress"]

The type of the event. Always `response.code_interpreter_call.in_progress`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseCodeInterpreterCallInterpretingEvent: …

Emitted when the code interpreter is actively interpreting the code snippet.

item\_id: str

The unique identifier of the code interpreter tool call item.

output\_index: int

The index of the output item in the response for which the code interpreter is interpreting code.

sequence\_number: int

The sequence number of this event, used to order streaming events.

type: Literal["response.code\_interpreter\_call.interpreting"]

The type of the event. Always `response.code_interpreter_call.interpreting`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseCompletedEvent: …

Emitted when the model response is complete.

response: [BetaResponse](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

Properties of the completed response.

sequence\_number: int

The sequence number for this event.

type: Literal["response.completed"]

The type of the event. Always `response.completed`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseContentPartAddedEvent: …

Emitted when a new content part is added.

content\_index: int

The index of the content part that was added.

item\_id: str

The ID of the output item that the content part was added to.

output\_index: int

The index of the output item that the content part was added to.

part: Part

The content part that was added.

class BetaResponseOutputText: …

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

logprobs: Optional[List[Logprob]]

token: str

bytes: List[int]

logprob: float

top\_logprobs: List[LogprobTopLogprob]

token: str

bytes: List[int]

logprob: float

class BetaResponseOutputRefusal: …

refusal: str

type: Literal["refusal"]

class PartReasoningText: …

text: str

type: Literal["reasoning\_text"]

sequence\_number: int

The sequence number of this event.

type: Literal["response.content\_part.added"]

The type of the event. Always `response.content_part.added`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseContentPartDoneEvent: …

Emitted when a content part is done.

content\_index: int

The index of the content part that is done.

item\_id: str

The ID of the output item that the content part was added to.

output\_index: int

The index of the output item that the content part was added to.

part: Part

The content part that is done.

class BetaResponseOutputText: …

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

logprobs: Optional[List[Logprob]]

token: str

bytes: List[int]

logprob: float

top\_logprobs: List[LogprobTopLogprob]

token: str

bytes: List[int]

logprob: float

class BetaResponseOutputRefusal: …

refusal: str

type: Literal["refusal"]

class PartReasoningText: …

text: str

type: Literal["reasoning\_text"]

sequence\_number: int

The sequence number of this event.

type: Literal["response.content\_part.done"]

The type of the event. Always `response.content_part.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseCreatedEvent: …

An event that is emitted when a response is created.

response: [BetaResponse](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

The response that was created.

sequence\_number: int

The sequence number for this event.

type: Literal["response.created"]

The type of the event. Always `response.created`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseErrorEvent: …

Emitted when an error occurs.

code: Optional[str]

The error code.

message: str

The error message.

param: Optional[str]

The error parameter.

sequence\_number: int

The sequence number of this event.

type: Literal["error"]

The type of the event. Always `error`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseFileSearchCallCompletedEvent: …

Emitted when a file search call is completed (results found).

item\_id: str

The ID of the output item that the file search call is initiated.

output\_index: int

The index of the output item that the file search call is initiated.

sequence\_number: int

The sequence number of this event.

type: Literal["response.file\_search\_call.completed"]

The type of the event. Always `response.file_search_call.completed`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseFileSearchCallInProgressEvent: …

Emitted when a file search call is initiated.

item\_id: str

The ID of the output item that the file search call is initiated.

output\_index: int

The index of the output item that the file search call is initiated.

sequence\_number: int

The sequence number of this event.

type: Literal["response.file\_search\_call.in\_progress"]

The type of the event. Always `response.file_search_call.in_progress`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseFileSearchCallSearchingEvent: …

Emitted when a file search is currently searching.

item\_id: str

The ID of the output item that the file search call is initiated.

output\_index: int

The index of the output item that the file search call is searching.

sequence\_number: int

The sequence number of this event.

type: Literal["response.file\_search\_call.searching"]

The type of the event. Always `response.file_search_call.searching`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseFunctionCallArgumentsDeltaEvent: …

Emitted when there is a partial function-call arguments delta.

delta: str

The function-call arguments delta that is added.

item\_id: str

The ID of the output item that the function-call arguments delta is added to.

output\_index: int

The index of the output item that the function-call arguments delta is added to.

sequence\_number: int

The sequence number of this event.

type: Literal["response.function\_call\_arguments.delta"]

The type of the event. Always `response.function_call_arguments.delta`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseFunctionCallArgumentsDoneEvent: …

Emitted when function-call arguments are finalized.

arguments: str

The function-call arguments.

item\_id: str

The ID of the item.

name: str

The name of the function that was called.

output\_index: int

The index of the output item.

sequence\_number: int

The sequence number of this event.

type: Literal["response.function\_call\_arguments.done"]

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseInProgressEvent: …

Emitted when the response is in progress.

response: [BetaResponse](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

The response that is in progress.

sequence\_number: int

The sequence number of this event.

type: Literal["response.in\_progress"]

The type of the event. Always `response.in_progress`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseFailedEvent: …

An event that is emitted when a response fails.

response: [BetaResponse](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

The response that failed.

sequence\_number: int

The sequence number of this event.

type: Literal["response.failed"]

The type of the event. Always `response.failed`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseIncompleteEvent: …

An event that is emitted when a response finishes as incomplete.

response: [BetaResponse](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

The response that was incomplete.

sequence\_number: int

The sequence number of this event.

type: Literal["response.incomplete"]

The type of the event. Always `response.incomplete`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseOutputItemAddedEvent: …

Emitted when a new output item is added.

item: [BetaResponseOutputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema))

The output item that was added.

output\_index: int

The index of the output item that was added.

sequence\_number: int

The sequence number of this event.

type: Literal["response.output\_item.added"]

The type of the event. Always `response.output_item.added`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseOutputItemDoneEvent: …

Emitted when an output item is marked done.

item: [BetaResponseOutputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema))

The output item that was marked done.

output\_index: int

The index of the output item that was marked done.

sequence\_number: int

The sequence number of this event.

type: Literal["response.output\_item.done"]

The type of the event. Always `response.output_item.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseReasoningSummaryPartAddedEvent: …

Emitted when a new reasoning summary part is added.

item\_id: str

The ID of the item this summary part is associated with.

output\_index: int

The index of the output item this summary part is associated with.

part: Part

The summary part that was added.

text: str

The text of the summary part.

type: Literal["summary\_text"]

The type of the summary part. Always `summary_text`.

sequence\_number: int

The sequence number of this event.

summary\_index: int

The index of the summary part within the reasoning summary.

type: Literal["response.reasoning\_summary\_part.added"]

The type of the event. Always `response.reasoning_summary_part.added`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseReasoningSummaryPartDoneEvent: …

Emitted when a reasoning summary part is completed.

item\_id: str

The ID of the item this summary part is associated with.

output\_index: int

The index of the output item this summary part is associated with.

part: Part

The completed summary part.

text: str

The text of the summary part.

type: Literal["summary\_text"]

The type of the summary part. Always `summary_text`.

sequence\_number: int

The sequence number of this event.

summary\_index: int

The index of the summary part within the reasoning summary.

type: Literal["response.reasoning\_summary\_part.done"]

The type of the event. Always `response.reasoning_summary_part.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

status: Optional[Literal["incomplete"]]

The completion status of the summary part. Omitted when the part completed
normally and set to `incomplete` when generation was interrupted.

class BetaResponseReasoningSummaryTextDeltaEvent: …

Emitted when a delta is added to a reasoning summary text.

delta: str

The text delta that was added to the summary.

item\_id: str

The ID of the item this summary text delta is associated with.

output\_index: int

The index of the output item this summary text delta is associated with.

sequence\_number: int

The sequence number of this event.

summary\_index: int

The index of the summary part within the reasoning summary.

type: Literal["response.reasoning\_summary\_text.delta"]

The type of the event. Always `response.reasoning_summary_text.delta`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseReasoningSummaryTextDoneEvent: …

Emitted when a reasoning summary text is completed.

item\_id: str

The ID of the item this summary text is associated with.

output\_index: int

The index of the output item this summary text is associated with.

sequence\_number: int

The sequence number of this event.

summary\_index: int

The index of the summary part within the reasoning summary.

text: str

The full text of the completed reasoning summary.

type: Literal["response.reasoning\_summary\_text.done"]

The type of the event. Always `response.reasoning_summary_text.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseReasoningTextDeltaEvent: …

Emitted when a delta is added to a reasoning text.

content\_index: int

The index of the reasoning content part this delta is associated with.

delta: str

The text delta that was added to the reasoning content.

item\_id: str

The ID of the item this reasoning text delta is associated with.

output\_index: int

The index of the output item this reasoning text delta is associated with.

sequence\_number: int

The sequence number of this event.

type: Literal["response.reasoning\_text.delta"]

The type of the event. Always `response.reasoning_text.delta`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseReasoningTextDoneEvent: …

Emitted when a reasoning text is completed.

content\_index: int

The index of the reasoning content part.

item\_id: str

The ID of the item this reasoning text is associated with.

output\_index: int

The index of the output item this reasoning text is associated with.

sequence\_number: int

The sequence number of this event.

text: str

The full text of the completed reasoning content.

type: Literal["response.reasoning\_text.done"]

The type of the event. Always `response.reasoning_text.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseRefusalDeltaEvent: …

Emitted when there is a partial refusal text.

content\_index: int

The index of the content part that the refusal text is added to.

delta: str

The refusal text that is added.

item\_id: str

The ID of the output item that the refusal text is added to.

output\_index: int

The index of the output item that the refusal text is added to.

sequence\_number: int

The sequence number of this event.

type: Literal["response.refusal.delta"]

The type of the event. Always `response.refusal.delta`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseRefusalDoneEvent: …

Emitted when refusal text is finalized.

content\_index: int

The index of the content part that the refusal text is finalized.

item\_id: str

The ID of the output item that the refusal text is finalized.

output\_index: int

The index of the output item that the refusal text is finalized.

refusal: str

The refusal text that is finalized.

sequence\_number: int

The sequence number of this event.

type: Literal["response.refusal.done"]

The type of the event. Always `response.refusal.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseTextDeltaEvent: …

Emitted when there is an additional text delta.

content\_index: int

The index of the content part that the text delta was added to.

delta: str

The text delta that was added.

item\_id: str

The ID of the output item that the text delta was added to.

logprobs: List[Logprob]

The log probabilities of the tokens in the delta.

token: str

A possible text token.

logprob: float

The log probability of this token.

top\_logprobs: Optional[List[LogprobTopLogprob]]

The log probabilities of up to 20 of the most likely tokens.

token: Optional[str]

A possible text token.

logprob: Optional[float]

The log probability of this token.

output\_index: int

The index of the output item that the text delta was added to.

sequence\_number: int

The sequence number for this event.

type: Literal["response.output\_text.delta"]

The type of the event. Always `response.output_text.delta`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseTextDoneEvent: …

Emitted when text content is finalized.

content\_index: int

The index of the content part that the text content is finalized.

item\_id: str

The ID of the output item that the text content is finalized.

logprobs: List[Logprob]

The log probabilities of the tokens in the delta.

token: str

A possible text token.

logprob: float

The log probability of this token.

top\_logprobs: Optional[List[LogprobTopLogprob]]

The log probabilities of up to 20 of the most likely tokens.

token: Optional[str]

A possible text token.

logprob: Optional[float]

The log probability of this token.

output\_index: int

The index of the output item that the text content is finalized.

sequence\_number: int

The sequence number for this event.

text: str

The text content that is finalized.

type: Literal["response.output\_text.done"]

The type of the event. Always `response.output_text.done`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseWebSearchCallCompletedEvent: …

Emitted when a web search call is completed.

item\_id: str

Unique ID for the output item associated with the web search call.

output\_index: int

The index of the output item that the web search call is associated with.

sequence\_number: int

The sequence number of the web search call being processed.

type: Literal["response.web\_search\_call.completed"]

The type of the event. Always `response.web_search_call.completed`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseWebSearchCallInProgressEvent: …

Emitted when a web search call is initiated.

item\_id: str

Unique ID for the output item associated with the web search call.

output\_index: int

The index of the output item that the web search call is associated with.

sequence\_number: int

The sequence number of the web search call being processed.

type: Literal["response.web\_search\_call.in\_progress"]

The type of the event. Always `response.web_search_call.in_progress`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseWebSearchCallSearchingEvent: …

Emitted when a web search call is executing.

item\_id: str

Unique ID for the output item associated with the web search call.

output\_index: int

The index of the output item that the web search call is associated with.

sequence\_number: int

The sequence number of the web search call being processed.

type: Literal["response.web\_search\_call.searching"]

The type of the event. Always `response.web_search_call.searching`.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseImageGenCallCompletedEvent: …

Emitted when an image generation tool call has completed and the final image is available.

item\_id: str

The unique identifier of the image generation item being processed.

output\_index: int

The index of the output item in the response’s output array.

sequence\_number: int

The sequence number of this event.

type: Literal["response.image\_generation\_call.completed"]

The type of the event. Always ‘response.image\_generation\_call.completed’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseImageGenCallGeneratingEvent: …

Emitted when an image generation tool call is actively generating an image (intermediate state).

item\_id: str

The unique identifier of the image generation item being processed.

output\_index: int

The index of the output item in the response’s output array.

sequence\_number: int

The sequence number of the image generation item being processed.

type: Literal["response.image\_generation\_call.generating"]

The type of the event. Always ‘response.image\_generation\_call.generating’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseImageGenCallInProgressEvent: …

Emitted when an image generation tool call is in progress.

item\_id: str

The unique identifier of the image generation item being processed.

output\_index: int

The index of the output item in the response’s output array.

sequence\_number: int

The sequence number of the image generation item being processed.

type: Literal["response.image\_generation\_call.in\_progress"]

The type of the event. Always ‘response.image\_generation\_call.in\_progress’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseImageGenCallPartialImageEvent: …

Emitted when a partial image is available during image generation streaming.

item\_id: str

The unique identifier of the image generation item being processed.

output\_index: int

The index of the output item in the response’s output array.

partial\_image\_b64: str

Base64-encoded partial image data, suitable for rendering as an image.

partial\_image\_index: int

0-based index for the partial image (backend is 1-based, but this is 0-based for the user).

sequence\_number: int

The sequence number of the image generation item being processed.

type: Literal["response.image\_generation\_call.partial\_image"]

The type of the event. Always ‘response.image\_generation\_call.partial\_image’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseMcpCallArgumentsDeltaEvent: …

Emitted when there is a delta (partial update) to the arguments of an MCP tool call.

delta: str

A JSON string containing the partial update to the arguments for the MCP tool call.

item\_id: str

The unique identifier of the MCP tool call item being processed.

output\_index: int

The index of the output item in the response’s output array.

sequence\_number: int

The sequence number of this event.

type: Literal["response.mcp\_call\_arguments.delta"]

The type of the event. Always ‘response.mcp\_call\_arguments.delta’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseMcpCallArgumentsDoneEvent: …

Emitted when the arguments for an MCP tool call are finalized.

arguments: str

A JSON string containing the finalized arguments for the MCP tool call.

item\_id: str

The unique identifier of the MCP tool call item being processed.

output\_index: int

The index of the output item in the response’s output array.

sequence\_number: int

The sequence number of this event.

type: Literal["response.mcp\_call\_arguments.done"]

The type of the event. Always ‘response.mcp\_call\_arguments.done’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseMcpCallCompletedEvent: …

Emitted when an MCP tool call has completed successfully.

item\_id: str

The ID of the MCP tool call item that completed.

output\_index: int

The index of the output item that completed.

sequence\_number: int

The sequence number of this event.

type: Literal["response.mcp\_call.completed"]

The type of the event. Always ‘response.mcp\_call.completed’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseMcpCallFailedEvent: …

Emitted when an MCP tool call has failed.

item\_id: str

The ID of the MCP tool call item that failed.

output\_index: int

The index of the output item that failed.

sequence\_number: int

The sequence number of this event.

type: Literal["response.mcp\_call.failed"]

The type of the event. Always ‘response.mcp\_call.failed’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseMcpCallInProgressEvent: …

Emitted when an MCP tool call is in progress.

item\_id: str

The unique identifier of the MCP tool call item being processed.

output\_index: int

The index of the output item in the response’s output array.

sequence\_number: int

The sequence number of this event.

type: Literal["response.mcp\_call.in\_progress"]

The type of the event. Always ‘response.mcp\_call.in\_progress’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseMcpListToolsCompletedEvent: …

Emitted when the list of available MCP tools has been successfully retrieved.

item\_id: str

The ID of the MCP tool call item that produced this output.

output\_index: int

The index of the output item that was processed.

sequence\_number: int

The sequence number of this event.

type: Literal["response.mcp\_list\_tools.completed"]

The type of the event. Always ‘response.mcp\_list\_tools.completed’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseMcpListToolsFailedEvent: …

Emitted when the attempt to list available MCP tools has failed.

item\_id: str

The ID of the MCP tool call item that failed.

output\_index: int

The index of the output item that failed.

sequence\_number: int

The sequence number of this event.

type: Literal["response.mcp\_list\_tools.failed"]

The type of the event. Always ‘response.mcp\_list\_tools.failed’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseMcpListToolsInProgressEvent: …

Emitted when the system is in the process of retrieving the list of available MCP tools.

item\_id: str

The ID of the MCP tool call item that is being processed.

output\_index: int

The index of the output item that is being processed.

sequence\_number: int

The sequence number of this event.

type: Literal["response.mcp\_list\_tools.in\_progress"]

The type of the event. Always ‘response.mcp\_list\_tools.in\_progress’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseOutputTextAnnotationAddedEvent: …

Emitted when an annotation is added to output text content.

annotation: object

The annotation object being added. (See annotation schema for details.)

annotation\_index: int

The index of the annotation within the content part.

content\_index: int

The index of the content part within the output item.

item\_id: str

The unique identifier of the item to which the annotation is being added.

output\_index: int

The index of the output item in the response’s output array.

sequence\_number: int

The sequence number of this event.

type: Literal["response.output\_text.annotation.added"]

The type of the event. Always ‘response.output\_text.annotation.added’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseQueuedEvent: …

Emitted when a response is queued and waiting to be processed.

response: [BetaResponse](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema))

The full response object that is queued.

sequence\_number: int

The sequence number for this event.

type: Literal["response.queued"]

The type of the event. Always ‘response.queued’.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseCustomToolCallInputDeltaEvent: …

Event representing a delta (partial update) to the input of a custom tool call.

delta: str

The incremental input data (delta) for the custom tool call.

item\_id: str

Unique identifier for the API item associated with this event.

output\_index: int

The index of the output this delta applies to.

sequence\_number: int

The sequence number of this event.

type: Literal["response.custom\_tool\_call\_input.delta"]

The event type identifier.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseCustomToolCallInputDoneEvent: …

Event indicating that input for a custom tool call is complete.

input: str

The complete input data for the custom tool call.

item\_id: str

Unique identifier for the API item associated with this event.

output\_index: int

The index of the output this event applies to.

sequence\_number: int

The sequence number of this event.

type: Literal["response.custom\_tool\_call\_input.done"]

The event type identifier.

agent: Optional[Agent]

The agent that owns this multi-agent streaming event.

agent\_name: str

class BetaResponseInjectCreatedEvent: …

Emitted when all injected input items were validated and committed to the
active response.

response\_id: str

The ID of the response that accepted the input.

sequence\_number: int

The sequence number for this event.

type: Literal["response.inject.created"]

The event discriminator. Always `response.inject.created`.

stream\_id: Optional[str]

The multiplexed WebSocket stream that emitted the event. This field is
present only when WebSocket multiplexing is enabled separately.

class BetaResponseInjectFailedEvent: …

Emitted when injected input could not be committed to a response. The event
returns the uncommitted raw input so the client can retry it in another
response when appropriate.

error: Error

Information about why the input was not committed.

code: Literal["response\_already\_completed", "response\_not\_found"]

A machine-readable error code.

"response\_already\_completed"

"response\_not\_found"

message: str

A human-readable description of the error.

input: List[[BetaResponseInputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_item%20%3E%20(schema))]

The raw input items that were not committed.

class BetaEasyInputMessage: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: Union[str, [BetaResponseInputMessageContentList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema))]

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

str

List[[BetaResponseInputContent](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_content%20%3E%20(schema))]

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

role: Literal["user", "assistant", "system", "developer"]

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

"user"

"assistant"

"system"

"developer"

phase: Optional[Literal["commentary", "final\_answer"]]

"commentary"

"final\_answer"

type: Optional[Literal["message"]]

The type of the message input. Always `message`.

class Message: …

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role.

content: [BetaResponseInputMessageContentList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema))

role: Literal["user", "system", "developer"]

"user"

"system"

"developer"

agent: Optional[MessageAgent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

type: Optional[Literal["message"]]

class BetaResponseOutputMessage: …

id: str

content: List[Content]

class BetaResponseOutputText: …

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

logprobs: Optional[List[Logprob]]

token: str

bytes: List[int]

logprob: float

top\_logprobs: List[LogprobTopLogprob]

token: str

bytes: List[int]

logprob: float

class BetaResponseOutputRefusal: …

refusal: str

type: Literal["refusal"]

role: Literal["assistant"]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["message"]

agent: Optional[Agent]

agent\_name: str

phase: Optional[Literal["commentary", "final\_answer"]]

"commentary"

"final\_answer"

class BetaResponseFileSearchToolCall: …

[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

id: str

queries: List[str]

status: Literal["in\_progress", "searching", "completed", 2 more]

"in\_progress"

"searching"

"completed"

"incomplete"

"failed"

type: Literal["file\_search\_call"]

agent: Optional[Agent]

agent\_name: str

results: Optional[List[Result]]

attributes: Optional[Dict[str, Union[str, float, bool]]]

str

float

bool

file\_id: Optional[str]

filename: Optional[str]

score: Optional[float]

formatfloat

text: Optional[str]

class BetaResponseComputerToolCall: …

[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

id: str

call\_id: str

pending\_safety\_checks: List[PendingSafetyCheck]

id: str

code: Optional[str]

message: Optional[str]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["computer\_call"]

action: Optional[BetaComputerAction]

actions: Optional[BetaComputerActionList]

agent: Optional[Agent]

agent\_name: str

class ComputerCallOutput: …

The output of a computer tool call.

call\_id: str

maxLength64

minLength1

output: [BetaResponseComputerToolCallOutputScreenshot](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema))

type: Literal["computer\_call\_output"]

id: Optional[str]

The ID of the computer tool call output.

acknowledged\_safety\_checks: Optional[List[ComputerCallOutputAcknowledgedSafetyCheck]]

The safety checks reported by the API that have been acknowledged by the developer.

id: str

code: Optional[str]

message: Optional[str]

agent: Optional[ComputerCallOutputAgent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the message input. One of `in_progress`, `completed`, or `incomplete`. Populated when input items are returned via API.

"in\_progress"

"completed"

"incomplete"

class BetaResponseFunctionWebSearch: …

[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

id: str

action: Action

class ActionSearch: …

type: Literal["search"]

queries: Optional[List[str]]

Deprecatedquery: Optional[str]

sources: Optional[List[ActionSearchSource]]

type: Literal["url"]

url: str

class ActionOpenPage: …

type: Literal["open\_page"]

url: Optional[str]

class ActionFindInPage: …

pattern: str

type: Literal["find\_in\_page"]

url: str

status: Literal["in\_progress", "searching", "completed", "failed"]

"in\_progress"

"searching"

"completed"

"failed"

type: Literal["web\_search\_call"]

agent: Optional[Agent]

agent\_name: str

class BetaResponseFunctionToolCall: …

[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

arguments: str

A JSON string of the arguments to pass to the function.

call\_id: str

name: str

The name of the function to run.

type: Literal["function\_call"]

The type of the function tool call. Always `function_call`.

id: Optional[str]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

namespace: Optional[str]

The namespace of the function to run.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class FunctionCallOutput: …

The output of a function tool call.

call\_id: str

maxLength64

minLength1

output: Union[str, [BetaResponseFunctionCallOutputItemList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item_list%20%3E%20(schema))]

Text, image, or file output of the function tool call.

str

A JSON string of the output of the function tool call.

List[[BetaResponseFunctionCallOutputItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_call_output_item%20%3E%20(schema))]

class BetaResponseInputTextContent: …

text: str

maxLength10485760

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImageContent: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

type: Literal["input\_image"]

detail: Optional[Literal["low", "high", "auto", "original"]]

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

image\_url: Optional[str]

maxLength20971520

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFileContent: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

The base64-encoded data of the file to be sent to the model.

maxLength73400320

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

type: Literal["function\_call\_output"]

id: Optional[str]

The unique ID of the function tool call output. Populated when this item is returned via API.

agent: Optional[FunctionCallOutputAgent]

agent\_name: str

caller: Optional[FunctionCallOutputCaller]

class FunctionCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class FunctionCallOutputCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

class AgentMessage: …

A message routed between agents.

author: str

content: List[AgentMessageContent]

Plaintext, image, or encrypted content sent between agents.

class BetaResponseInputTextContent: …

text: str

maxLength10485760

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImageContent: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision)

type: Literal["input\_image"]

detail: Optional[Literal["low", "high", "auto", "original"]]

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

image\_url: Optional[str]

maxLength20971520

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class AgentMessageContentEncryptedContent: …

encrypted\_content: str

maxLength10485760

type: Literal["encrypted\_content"]

recipient: str

type: Literal["agent\_message"]

The item type. Always `agent_message`.

id: Optional[str]

The unique ID of this agent message item.

agent: Optional[AgentMessageAgent]

agent\_name: str

class MultiAgentCall: …

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

The multi-agent action that was executed.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

arguments: str

The action arguments as a JSON string.

call\_id: str

maxLength64

minLength1

type: Literal["multi\_agent\_call"]

The item type. Always `multi_agent_call`.

id: Optional[str]

The unique ID of this multi-agent call.

agent: Optional[MultiAgentCallAgent]

agent\_name: str

class MultiAgentCallOutput: …

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

call\_id: str

maxLength64

minLength1

output: List[MultiAgentCallOutputOutput]

text: str

The text content.

maxLength10485760

type: Literal["output\_text"]

The content type. Always `output_text`.

annotations: Optional[List[MultiAgentCallOutputOutputAnnotation]]

Citations associated with the text content.

class MultiAgentCallOutputOutputAnnotationFileCitation: …

file\_id: str

filename: str

index: int

minimum0

type: Literal["file\_citation"]

The citation type. Always `file_citation`.

class MultiAgentCallOutputOutputAnnotationURLCitation: …

end\_index: int

The index of the last character of the citation in the message.

minimum0

start\_index: int

The index of the first character of the citation in the message.

minimum0

title: str

The title of the cited resource.

type: Literal["url\_citation"]

The citation type. Always `url_citation`.

url: str

The URL of the cited resource.

class MultiAgentCallOutputOutputAnnotationContainerFileCitation: …

container\_id: str

The ID of the container.

end\_index: int

The index of the last character of the citation in the message.

minimum0

file\_id: str

filename: str

start\_index: int

The index of the first character of the citation in the message.

minimum0

type: Literal["container\_file\_citation"]

The citation type. Always `container_file_citation`.

type: Literal["multi\_agent\_call\_output"]

The item type. Always `multi_agent_call_output`.

id: Optional[str]

The unique ID of this multi-agent call output.

agent: Optional[MultiAgentCallOutputAgent]

agent\_name: str

class ToolSearchCall: …

arguments: object

The arguments supplied to the tool search call.

type: Literal["tool\_search\_call"]

The item type. Always `tool_search_call`.

id: Optional[str]

The unique ID of this tool search call.

agent: Optional[ToolSearchCallAgent]

agent\_name: str

call\_id: Optional[str]

maxLength64

minLength1

execution: Optional[Literal["server", "client"]]

"server"

"client"

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the tool search call.

"in\_progress"

"completed"

"incomplete"

class BetaResponseToolSearchOutputItemParam: …

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

The loaded tool definitions returned by the tool search output.

class BetaFunctionTool: …

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

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

input\_fidelity: Optional[Literal["high", "low"]]

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

type: Literal["tool\_search\_output"]

The item type. Always `tool_search_output`.

id: Optional[str]

The unique ID of this tool search output.

agent: Optional[Agent]

agent\_name: str

call\_id: Optional[str]

maxLength64

minLength1

execution: Optional[Literal["server", "client"]]

"server"

"client"

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the tool search output.

"in\_progress"

"completed"

"incomplete"

class AdditionalTools: …

role: Literal["developer"]

The role that provided the additional tools. Only `developer` is supported.

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

A list of additional tools made available at this item.

class BetaFunctionTool: …

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

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

input\_fidelity: Optional[Literal["high", "low"]]

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

type: Literal["additional\_tools"]

The item type. Always `additional_tools`.

id: Optional[str]

The unique ID of this additional tools item.

agent: Optional[AdditionalToolsAgent]

agent\_name: str

class BetaResponseReasoningItem: …

[managing context](https://platform.openai.com/docs/guides/conversation-state).

id: str

summary: List[Summary]

text: str

type: Literal["summary\_text"]

type: Literal["reasoning"]

agent: Optional[Agent]

agent\_name: str

content: Optional[List[Content]]

text: str

type: Literal["reasoning\_text"]

encrypted\_content: Optional[str]

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class BetaResponseCompactionItemParam: …

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

encrypted\_content: str

The encrypted content of the compaction summary.

maxLength10485760

type: Literal["compaction"]

id: Optional[str]

The ID of the compaction item.

agent: Optional[Agent]

agent\_name: str

class ImageGenerationCall: …

An image generation request made by the model.

id: str

result: Optional[str]

status: Literal["in\_progress", "completed", "generating", "failed"]

"in\_progress"

"completed"

"generating"

"failed"

type: Literal["image\_generation\_call"]

agent: Optional[ImageGenerationCallAgent]

agent\_name: str

class BetaResponseCodeInterpreterToolCall: …

id: str

code: Optional[str]

container\_id: str

outputs: Optional[List[Output]]

class OutputLogs: …

logs: str

type: Literal["logs"]

class OutputImage: …

type: Literal["image"]

url: str

status: Literal["in\_progress", "completed", "incomplete", 2 more]

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: Literal["code\_interpreter\_call"]

agent: Optional[Agent]

agent\_name: str

class LocalShellCall: …

A tool call to run a command on the local shell.

id: str

action: LocalShellCallAction

command: List[str]

env: Dict[str, str]

type: Literal["exec"]

timeout\_ms: Optional[int]

user: Optional[str]

working\_directory: Optional[str]

call\_id: str

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["local\_shell\_call"]

agent: Optional[LocalShellCallAgent]

agent\_name: str

class LocalShellCallOutput: …

The output of a local shell tool call.

id: str

output: str

type: Literal["local\_shell\_call\_output"]

agent: Optional[LocalShellCallOutputAgent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class ShellCall: …

A tool representing a request to execute one or more shell commands.

action: ShellCallAction

commands: List[str]

Ordered shell commands for the execution environment to run.

max\_output\_length: Optional[int]

Maximum number of UTF-8 characters to capture from combined stdout and stderr output.

timeout\_ms: Optional[int]

Maximum wall-clock time in milliseconds to allow the shell commands to run.

call\_id: str

maxLength64

minLength1

type: Literal["shell\_call"]

id: Optional[str]

agent: Optional[ShellCallAgent]

agent\_name: str

caller: Optional[ShellCallCaller]

class ShellCallCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ShellCallCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

environment: Optional[ShellCallEnvironment]

The environment to execute the shell commands in.

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class ShellCallOutput: …

The streamed output items emitted by a shell tool call.

call\_id: str

maxLength64

minLength1

output: List[[BetaResponseFunctionShellCallOutputContent](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_shell_call_output_content%20%3E%20(schema))]

Captured chunks of stdout and stderr output, along with their associated outcomes.

outcome: Outcome

The exit or timeout outcome associated with this shell call.

class OutcomeTimeout: …

Indicates that the shell call exceeded its configured time limit.

type: Literal["timeout"]

The outcome type. Always `timeout`.

class OutcomeExit: …

exit\_code: int

The exit code returned by the shell process.

type: Literal["exit"]

stderr: str

Captured stderr output for the shell call.

maxLength10485760

stdout: str

Captured stdout output for the shell call.

maxLength10485760

type: Literal["shell\_call\_output"]

The type of the item. Always `shell_call_output`.

id: Optional[str]

The unique ID of the shell tool call output. Populated when this item is returned via API.

agent: Optional[ShellCallOutputAgent]

agent\_name: str

caller: Optional[ShellCallOutputCaller]

class ShellCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ShellCallOutputCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

max\_output\_length: Optional[int]

The maximum number of UTF-8 characters captured for this shell call’s combined output.

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

The status of the shell call output.

"in\_progress"

"completed"

"incomplete"

class ApplyPatchCall: …

A tool call representing a request to create, delete, or update files using diff patches.

call\_id: str

maxLength64

minLength1

operation: ApplyPatchCallOperation

The specific create, delete, or update instruction for the apply\_patch tool call.

class ApplyPatchCallOperationCreateFile: …

Instruction for creating a new file via the apply\_patch tool.

diff: str

Unified diff content to apply when creating the file.

maxLength10485760

path: str

Path of the file to create relative to the workspace root.

minLength1

type: Literal["create\_file"]

The operation type. Always `create_file`.

class ApplyPatchCallOperationDeleteFile: …

Instruction for deleting an existing file via the apply\_patch tool.

path: str

Path of the file to delete relative to the workspace root.

minLength1

type: Literal["delete\_file"]

The operation type. Always `delete_file`.

class ApplyPatchCallOperationUpdateFile: …

Instruction for updating an existing file via the apply\_patch tool.

diff: str

Unified diff content to apply to the existing file.

maxLength10485760

path: str

Path of the file to update relative to the workspace root.

minLength1

type: Literal["update\_file"]

The operation type. Always `update_file`.

status: Literal["in\_progress", "completed"]

"in\_progress"

"completed"

type: Literal["apply\_patch\_call"]

id: Optional[str]

agent: Optional[ApplyPatchCallAgent]

agent\_name: str

caller: Optional[ApplyPatchCallCaller]

class ApplyPatchCallCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ApplyPatchCallCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

class ApplyPatchCallOutput: …

The streamed output emitted by an apply patch tool call.

call\_id: str

maxLength64

minLength1

status: Literal["completed", "failed"]

"completed"

"failed"

type: Literal["apply\_patch\_call\_output"]

id: Optional[str]

agent: Optional[ApplyPatchCallOutputAgent]

agent\_name: str

caller: Optional[ApplyPatchCallOutputCaller]

class ApplyPatchCallOutputCallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class ApplyPatchCallOutputCallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

output: Optional[str]

Optional human-readable log text from the apply patch tool (e.g., patch results or errors).

maxLength10485760

class McpListTools: …

A list of tools available on an MCP server.

id: str

server\_label: str

tools: List[McpListToolsTool]

input\_schema: object

name: str

annotations: Optional[object]

description: Optional[str]

type: Literal["mcp\_list\_tools"]

agent: Optional[McpListToolsAgent]

agent\_name: str

error: Optional[str]

class McpApprovalRequest: …

A request for human approval of a tool invocation.

id: str

arguments: str

name: str

server\_label: str

type: Literal["mcp\_approval\_request"]

agent: Optional[McpApprovalRequestAgent]

agent\_name: str

class McpApprovalResponse: …

A response to an MCP approval request.

approval\_request\_id: str

approve: bool

type: Literal["mcp\_approval\_response"]

id: Optional[str]

agent: Optional[McpApprovalResponseAgent]

agent\_name: str

reason: Optional[str]

class McpCall: …

An invocation of a tool on an MCP server.

id: str

arguments: str

name: str

server\_label: str

type: Literal["mcp\_call"]

agent: Optional[McpCallAgent]

agent\_name: str

approval\_request\_id: Optional[str]

error: Optional[str]

output: Optional[str]

status: Optional[Literal["in\_progress", "completed", "incomplete", 2 more]]

"in\_progress"

"completed"

"incomplete"

"calling"

"failed"

class BetaResponseCustomToolCallOutput: …

call\_id: str

The call ID, used to map this custom tool call output to a custom tool call.

output: Union[str, List[OutputOutputContentList]]

The output from the custom tool call generated by your code.

str

A string of the output of the custom tool call.

List[OutputOutputContentList]

Text, image, or file output of the custom tool call.

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

type: Literal["custom\_tool\_call\_output"]

The type of the custom tool call output. Always `custom_tool_call_output`.

id: Optional[str]

The unique ID of the custom tool call output in the OpenAI platform.

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class CallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

class BetaResponseCustomToolCall: …

call\_id: str

An identifier used to map this custom tool call to a tool call output.

input: str

The input for the custom tool call generated by the model.

name: str

The name of the custom tool being called.

type: Literal["custom\_tool\_call"]

The type of the custom tool call. Always `custom_tool_call`.

id: Optional[str]

The unique ID of the custom tool call in the OpenAI platform.

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

namespace: Optional[str]

The namespace of the custom tool being called.

class CompactionTrigger: …

Compacts the current context. Must be the final input item.

type: Literal["compaction\_trigger"]

The type of the item. Always `compaction_trigger`.

agent: Optional[CompactionTriggerAgent]

agent\_name: str

class ItemReference: …

An internal identifier for an item to reference.

id: str

The ID of the item to reference.

agent: Optional[ItemReferenceAgent]

agent\_name: str

type: Optional[Literal["item\_reference"]]

The type of item to reference. Always `item_reference`.

class Program: …

id: str

The unique ID of this program item.

call\_id: str

maxLength64

minLength1

code: str

maxLength10485760

fingerprint: str

maxLength10485760

type: Literal["program"]

The item type. Always `program`.

agent: Optional[ProgramAgent]

agent\_name: str

class ProgramOutput: …

id: str

The unique ID of this program output item.

call\_id: str

maxLength64

minLength1

result: str

maxLength10485760

status: Literal["completed", "incomplete"]

The terminal status of the program output.

"completed"

"incomplete"

type: Literal["program\_output"]

The item type. Always `program_output`.

agent: Optional[ProgramOutputAgent]

agent\_name: str

response\_id: str

The ID of the response that rejected the input.

sequence\_number: int

The sequence number for this event.

type: Literal["response.inject.failed"]

The event discriminator. Always `response.inject.failed`.

stream\_id: Optional[str]

The multiplexed WebSocket stream that emitted the event. This field is
present only when WebSocket multiplexing is enabled separately.

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))

A tool that can be used to generate a response.

class BetaFunctionTool: …

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

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

input\_fidelity: Optional[Literal["high", "low"]]

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class BetaToolChoiceAllowed: …

Constrains the tools available to the model to a pre-defined set.

mode: Literal["auto", "required"]

Constrains the tools available to the model to a pre-defined set.

`auto` allows the model to pick from among the allowed tools and generate a
message.

`required` requires the model to call one or more of the allowed tools.

"auto"

"required"

tools: List[Dict[str, object]]

A list of tool definitions that the model should be allowed to call.

For the Responses API, the list of tool definitions might look like:

  { "type": "function", "name": "get_weather" },
  { "type": "mcp", "server_label": "deepwiki" },
  { "type": "image_generation" }

type: Literal["allowed\_tools"]

Allowed tool configuration type. Always `allowed_tools`.

class BetaToolChoiceApplyPatch: …

Forces the model to call the apply\_patch tool when executing a tool call.

type: Literal["apply\_patch"]

The tool to call. Always `apply_patch`.

class BetaToolChoiceCustom: …

Use this option to force the model to call a specific custom tool.

name: str

The name of the custom tool to call.

type: Literal["custom"]

For custom tool calling, the type is always `custom`.

class BetaToolChoiceFunction: …

Use this option to force the model to call a specific function.

name: str

type: Literal["function"]

For function calling, the type is always `function`.

class BetaToolChoiceMcp: …

Use this option to force the model to call a specific tool on a remote MCP server.

server\_label: str

The label of the MCP server to use.

type: Literal["mcp"]

For MCP tools, the type is always `mcp`.

name: Optional[str]

The name of the tool to call on the server.

Literal["none", "auto", "required"]

Controls which (if any) tool is called by the model.

`none` means the model will not call any tool and instead generates a message.

`auto` means the model can pick between generating a message or calling one or
more tools.

`required` means the model must call one or more tools.

"none"

"auto"

"required"

class BetaToolChoiceShell: …

Forces the model to call the shell tool when a tool call is required.

type: Literal["shell"]

The tool to call. Always `shell`.

class BetaToolChoiceTypes: …

Indicates that the model should use a built-in tool to generate a response.
[Learn more about built-in tools](https://platform.openai.com/docs/guides/tools).

type: Literal["file\_search", "web\_search\_preview", "computer", 5 more]

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

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

#### ResponsesInput Items

##### [List input items](/api/reference/python/resources/beta/subresources/responses/subresources/input_items/methods/list)

beta.responses.input\_items.list(strresponse\_id, InputItemListParams\*\*kwargs)  -> SyncCursorPage[[BetaResponseItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_item%20%3E%20(schema))]

GET/responses/{response\_id}/input\_items

##### ModelsExpand Collapse

class BetaResponseItemList: …

A list of Response items.

data: List[[BetaResponseItem](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_item%20%3E%20(schema))]

A list of items used to generate this response.

class BetaResponseInputMessageItem: …

id: str

The unique ID of the message input.

content: [BetaResponseInputMessageContentList](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema))

role: Literal["user", "system", "developer"]

"user"

"system"

"developer"

type: Literal["message"]

agent: Optional[Agent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class BetaResponseOutputMessage: …

id: str

content: List[Content]

class BetaResponseOutputText: …

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

logprobs: Optional[List[Logprob]]

token: str

bytes: List[int]

logprob: float

top\_logprobs: List[LogprobTopLogprob]

token: str

bytes: List[int]

logprob: float

class BetaResponseOutputRefusal: …

refusal: str

type: Literal["refusal"]

role: Literal["assistant"]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["message"]

agent: Optional[Agent]

agent\_name: str

phase: Optional[Literal["commentary", "final\_answer"]]

"commentary"

"final\_answer"

class BetaResponseFileSearchToolCall: …

[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

id: str

queries: List[str]

status: Literal["in\_progress", "searching", "completed", 2 more]

"in\_progress"

"searching"

"completed"

"incomplete"

"failed"

type: Literal["file\_search\_call"]

agent: Optional[Agent]

agent\_name: str

results: Optional[List[Result]]

attributes: Optional[Dict[str, Union[str, float, bool]]]

str

float

bool

file\_id: Optional[str]

filename: Optional[str]

score: Optional[float]

formatfloat

text: Optional[str]

class BetaResponseComputerToolCall: …

[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

id: str

call\_id: str

pending\_safety\_checks: List[PendingSafetyCheck]

id: str

code: Optional[str]

message: Optional[str]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["computer\_call"]

action: Optional[BetaComputerAction]

actions: Optional[BetaComputerActionList]

agent: Optional[Agent]

agent\_name: str

class BetaResponseComputerToolCallOutputItem: …

id: str

The unique ID of the computer call tool output.

call\_id: str

output: [BetaResponseComputerToolCallOutputScreenshot](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema))

status: Literal["completed", "incomplete", "failed", "in\_progress"]

"completed"

"incomplete"

"failed"

"in\_progress"

type: Literal["computer\_call\_output"]

acknowledged\_safety\_checks: Optional[List[AcknowledgedSafetyCheck]]

The safety checks reported by the API that have been acknowledged by the
developer.

id: str

code: Optional[str]

message: Optional[str]

agent: Optional[Agent]

agent\_name: str

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseFunctionWebSearch: …

[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

id: str

action: Action

class ActionSearch: …

type: Literal["search"]

queries: Optional[List[str]]

Deprecatedquery: Optional[str]

sources: Optional[List[ActionSearchSource]]

type: Literal["url"]

url: str

class ActionOpenPage: …

type: Literal["open\_page"]

url: Optional[str]

class ActionFindInPage: …

pattern: str

type: Literal["find\_in\_page"]

url: str

status: Literal["in\_progress", "searching", "completed", "failed"]

"in\_progress"

"searching"

"completed"

"failed"

type: Literal["web\_search\_call"]

agent: Optional[Agent]

agent\_name: str

class BetaResponseFunctionToolCallItem: …

[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

id: str

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseFunctionToolCallOutputItem: …

id: str

The unique ID of the function call tool output.

call\_id: str

output: Union[str, List[OutputOutputContentList]]

The output from the function call generated by your code.

str

A string of the output of the function call.

List[OutputOutputContentList]

Text, image, or file output of the function call.

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["function\_call\_output"]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

The caller type. Always `direct`.

class CallerProgram: …

caller\_id: str

maxLength64

minLength1

type: Literal["program"]

created\_by: Optional[str]

The identifier of the actor that created the item.

class AgentMessage: …

id: str

The unique ID of the agent message.

author: str

content: List[AgentMessageContent]

Encrypted content sent between agents.

class BetaResponseInputText: …

text: str

type: Literal["input\_text"]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseOutputText: …

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

logprobs: Optional[List[Logprob]]

token: str

bytes: List[int]

logprob: float

top\_logprobs: List[LogprobTopLogprob]

token: str

bytes: List[int]

logprob: float

class AgentMessageContentText: …

A text content.

text: str

type: Literal["text"]

class AgentMessageContentSummaryText: …

A summary text from the model.

text: str

type: Literal["summary\_text"]

class AgentMessageContentReasoningText: …

text: str

type: Literal["reasoning\_text"]

class BetaResponseOutputRefusal: …

refusal: str

type: Literal["refusal"]

class BetaResponseInputImage: …

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: Literal["low", "high", "auto", "original"]

"low"

"high"

"auto"

"original"

type: Literal["input\_image"]

file\_id: Optional[str]

image\_url: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class AgentMessageContentComputerScreenshot: …

A screenshot of a computer.

detail: Literal["low", "high", "auto", "original"]

The detail level of the screenshot image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

file\_id: Optional[str]

image\_url: Optional[str]

type: Literal["computer\_screenshot"]

Specifies the event type. For a computer screenshot, this property is always set to `computer_screenshot`.

prompt\_cache\_breakpoint: Optional[AgentMessageContentComputerScreenshotPromptCacheBreakpoint]

mode: Literal["explicit"]

class BetaResponseInputFile: …

type: Literal["input\_file"]

detail: Optional[Literal["auto", "low", "high"]]

"auto"

"low"

"high"

file\_data: Optional[str]

file\_id: Optional[str]

file\_url: Optional[str]

filename: Optional[str]

prompt\_cache\_breakpoint: Optional[PromptCacheBreakpoint]

mode: Literal["explicit"]

class AgentMessageContentEncryptedContent: …

encrypted\_content: str

type: Literal["encrypted\_content"]

recipient: str

type: Literal["agent\_message"]

The type of the item. Always `agent_message`.

agent: Optional[AgentMessageAgent]

agent\_name: str

class MultiAgentCall: …

id: str

The unique ID of the multi-agent call item.

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

The multi-agent action to execute.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

arguments: str

The JSON string of arguments generated for the action.

call\_id: str

type: Literal["multi\_agent\_call"]

The type of the multi-agent call. Always `multi_agent_call`.

agent: Optional[MultiAgentCallAgent]

agent\_name: str

class MultiAgentCallOutput: …

id: str

The unique ID of the multi-agent call output item.

action: Literal["spawn\_agent", "interrupt\_agent", "list\_agents", 3 more]

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

call\_id: str

output: List[[BetaResponseOutputText](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema))]

annotations: List[Annotation]

class AnnotationFileCitation: …

file\_id: str

filename: str

index: int

type: Literal["file\_citation"]

class AnnotationURLCitation: …

end\_index: int

start\_index: int

title: str

type: Literal["url\_citation"]

url: str

class AnnotationContainerFileCitation: …

container\_id: str

end\_index: int

file\_id: str

filename: str

start\_index: int

type: Literal["container\_file\_citation"]

class AnnotationFilePath: …

file\_id: str

index: int

type: Literal["file\_path"]

text: str

type: Literal["output\_text"]

logprobs: Optional[List[Logprob]]

token: str

bytes: List[int]

logprob: float

top\_logprobs: List[LogprobTopLogprob]

token: str

bytes: List[int]

logprob: float

type: Literal["multi\_agent\_call\_output"]

The type of the multi-agent result. Always `multi_agent_call_output`.

agent: Optional[MultiAgentCallOutputAgent]

agent\_name: str

class BetaResponseToolSearchCall: …

id: str

The unique ID of the tool search call item.

arguments: object

Arguments used for the tool search call.

call\_id: Optional[str]

execution: Literal["server", "client"]

"server"

"client"

status: Literal["in\_progress", "completed", "incomplete"]

The status of the tool search call item that was recorded.

"in\_progress"

"completed"

"incomplete"

type: Literal["tool\_search\_call"]

The type of the item. Always `tool_search_call`.

agent: Optional[Agent]

agent\_name: str

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseToolSearchOutputItem: …

id: str

The unique ID of the tool search output item.

call\_id: Optional[str]

execution: Literal["server", "client"]

"server"

"client"

status: Literal["in\_progress", "completed", "incomplete"]

The status of the tool search output item that was recorded.

"in\_progress"

"completed"

"incomplete"

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

The loaded tool definitions returned by tool search.

class BetaFunctionTool: …

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

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

input\_fidelity: Optional[Literal["high", "low"]]

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

type: Literal["tool\_search\_output"]

The type of the item. Always `tool_search_output`.

agent: Optional[Agent]

agent\_name: str

created\_by: Optional[str]

The identifier of the actor that created the item.

class AdditionalTools: …

id: str

The unique ID of the additional tools item.

role: Literal["unknown", "user", "assistant", 5 more]

The role that provided the additional tools.

"unknown"

"user"

"assistant"

"system"

"critic"

"discriminator"

"developer"

"tool"

tools: List[[BetaTool](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))]

The additional tool definitions made available at this item.

class BetaFunctionTool: …

name: str

parameters: Optional[Dict[str, object]]

strict: Optional[bool]

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

class BetaFileSearchTool: …

type: Literal["file\_search"]

vector\_store\_ids: List[str]

filters: Optional[Filters]

class FiltersComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

class FiltersCompoundFilter: …

filters: List[FiltersCompoundFilterFilter]

class FiltersCompoundFilterFilterComparisonFilter: …

key: str

type: Literal["eq", "ne", "gt", 5 more]

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: Union[str, float, bool, List[Union[str, float]]]

str

float

bool

List[Union[str, float]]

str

float

object

type: Literal["and", "or"]

"and"

"or"

max\_num\_results: Optional[int]

ranking\_options: Optional[RankingOptions]

hybrid\_search: Optional[RankingOptionsHybridSearch]

embedding\_weight: float

text\_weight: float

ranker: Optional[Literal["auto", "default-2024-11-15"]]

"auto"

"default-2024-11-15"

score\_threshold: Optional[float]

class BetaComputerTool: …

type: Literal["computer"]

class BetaComputerUsePreviewTool: …

display\_height: int

display\_width: int

environment: Literal["windows", "mac", "linux", 2 more]

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: Literal["computer\_use\_preview"]

class BetaWebSearchTool: …

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: Literal["web\_search", "web\_search\_2025\_08\_26"]

"web\_search"

"web\_search\_2025\_08\_26"

filters: Optional[Filters]

allowed\_domains: Optional[List[str]]

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

type: Optional[Literal["approximate"]]

class Mcp: …

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: str

type: Literal["mcp"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

allowed\_tools: Optional[McpAllowedTools]

List[str]

A string array of allowed tool names

class McpAllowedToolsMcpToolFilter: …

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

authorization: Optional[str]

connector\_id: Optional[Literal["connector\_dropbox", "connector\_gmail", "connector\_googlecalendar", 5 more]]

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: Optional[bool]

headers: Optional[Dict[str, str]]

require\_approval: Optional[McpRequireApproval]

class McpRequireApprovalMcpToolApprovalFilter: …

always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

never: Optional[McpRequireApprovalMcpToolApprovalFilterNever]

read\_only: Optional[bool]

tool\_names: Optional[List[str]]

Literal["always", "never"]

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: Optional[str]

server\_url: Optional[str]

tunnel\_id: Optional[str]

class CodeInterpreter: …

A tool that runs Python code to help generate a response to a prompt.

container: CodeInterpreterContainer

str

The container ID.

class CodeInterpreterContainerCodeInterpreterToolAuto: …

type: Literal["auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[CodeInterpreterContainerCodeInterpreterToolAutoNetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

type: Literal["code\_interpreter"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

class ProgrammaticToolCalling: …

type: Literal["programmatic\_tool\_calling"]

The type of the tool. Always `programmatic_tool_calling`.

class ImageGeneration: …

A tool that generates images using the GPT image models.

type: Literal["image\_generation"]

action: Optional[Literal["generate", "edit", "auto"]]

"generate"

"edit"

"auto"

background: Optional[Literal["transparent", "opaque", "auto"]]

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

input\_fidelity: Optional[Literal["high", "low"]]

"high"

"low"

input\_image\_mask: Optional[ImageGenerationInputImageMask]

file\_id: Optional[str]

image\_url: Optional[str]

model: Optional[Union[str, Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more], null]]

str

Literal["gpt-image-1", "gpt-image-1-mini", "gpt-image-2", 3 more]

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: Optional[Literal["auto", "low"]]

"auto"

"low"

output\_compression: Optional[int]

minimum0

maximum100

output\_format: Optional[Literal["png", "webp", "jpeg"]]

"png"

"webp"

"jpeg"

partial\_images: Optional[int]

minimum0

maximum3

quality: Optional[Literal["low", "medium", "high", "auto"]]

"low"

"medium"

"high"

"auto"

size: Optional[Union[str, Literal["1024x1024", "1024x1536", "1536x1024", "auto"], null]]

str

Literal["1024x1024", "1024x1536", "1536x1024", "auto"]

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

class LocalShell: …

A tool that allows the model to execute shell commands in a local environment.

type: Literal["local\_shell"]

The type of the local shell tool. Always `local_shell`.

class BetaFunctionShellTool: …

type: Literal["shell"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

environment: Optional[Environment]

class BetaContainerAuto: …

type: Literal["container\_auto"]

file\_ids: Optional[List[str]]

memory\_limit: Optional[Literal["1g", "4g", "16g", "64g"]]

"1g"

"4g"

"16g"

"64g"

network\_policy: Optional[NetworkPolicy]

class BetaContainerNetworkPolicyDisabled: …

type: Literal["disabled"]

class BetaContainerNetworkPolicyAllowlist: …

allowed\_domains: List[str]

type: Literal["allowlist"]

domain\_secrets: Optional[List[[BetaContainerNetworkPolicyDomainSecret](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema))]]

domain: str

minLength1

name: str

minLength1

value: str

maxLength10485760

minLength1

skills: Optional[List[Skill]]

class BetaSkillReference: …

skill\_id: str

maxLength64

minLength1

type: Literal["skill\_reference"]

version: Optional[str]

class BetaInlineSkill: …

description: str

name: str

source: [BetaInlineSkillSource](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema))

type: Literal["inline"]

class BetaLocalEnvironment: …

type: Literal["local"]

skills: Optional[List[[BetaLocalSkill](/api/reference/python/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema))]]

description: str

name: str

path: str

class BetaContainerReference: …

container\_id: str

type: Literal["container\_reference"]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

class BetaNamespaceTool: …

description: str

minLength1

name: str

minLength1

tools: List[Tool]

class ToolFunction: …

name: str

maxLength128

minLength1

type: Literal["function"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

output\_schema: Optional[Dict[str, object]]

parameters: Optional[object]

strict: Optional[bool]

class BetaCustomTool: …

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: str

type: Literal["custom"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

defer\_loading: Optional[bool]

description: Optional[str]

format: Optional[Format]

class FormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class FormatGrammar: …

definition: str

syntax: Literal["lark", "regex"]

"lark"

"regex"

type: Literal["grammar"]

type: Literal["namespace"]

class BetaToolSearchTool: …

type: Literal["tool\_search"]

description: Optional[str]

execution: Optional[Literal["server", "client"]]

"server"

"client"

parameters: Optional[object]

class BetaWebSearchPreviewTool: …

type: Literal["web\_search\_preview", "web\_search\_preview\_2025\_03\_11"]

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: Optional[List[Literal["text", "image"]]]

"text"

"image"

search\_context\_size: Optional[Literal["low", "medium", "high"]]

"low"

"medium"

"high"

user\_location: Optional[UserLocation]

type: Literal["approximate"]

city: Optional[str]

country: Optional[str]

region: Optional[str]

timezone: Optional[str]

class BetaApplyPatchTool: …

type: Literal["apply\_patch"]

allowed\_callers: Optional[List[Literal["direct", "programmatic"]]]

"direct"

"programmatic"

type: Literal["additional\_tools"]

The type of the item. Always `additional_tools`.

agent: Optional[AdditionalToolsAgent]

agent\_name: str

class BetaResponseReasoningItem: …

[managing context](https://platform.openai.com/docs/guides/conversation-state).

id: str

summary: List[Summary]

text: str

type: Literal["summary\_text"]

type: Literal["reasoning"]

agent: Optional[Agent]

agent\_name: str

content: Optional[List[Content]]

text: str

type: Literal["reasoning\_text"]

encrypted\_content: Optional[str]

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class Program: …

id: str

The unique ID of the program item.

call\_id: str

code: str

fingerprint: str

type: Literal["program"]

The type of the item. Always `program`.

agent: Optional[ProgramAgent]

agent\_name: str

class ProgramOutput: …

id: str

The unique ID of the program output item.

call\_id: str

result: str

status: Literal["completed", "incomplete"]

The terminal status of the program output item.

"completed"

"incomplete"

type: Literal["program\_output"]

The type of the item. Always `program_output`.

agent: Optional[ProgramOutputAgent]

agent\_name: str

class BetaResponseCompactionItem: …

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

id: str

The unique ID of the compaction item.

encrypted\_content: str

The encrypted content that was produced by compaction.

type: Literal["compaction"]

agent: Optional[Agent]

agent\_name: str

created\_by: Optional[str]

The identifier of the actor that created the item.

class ImageGenerationCall: …

An image generation request made by the model.

id: str

result: Optional[str]

status: Literal["in\_progress", "completed", "generating", "failed"]

"in\_progress"

"completed"

"generating"

"failed"

type: Literal["image\_generation\_call"]

agent: Optional[ImageGenerationCallAgent]

agent\_name: str

class BetaResponseCodeInterpreterToolCall: …

id: str

code: Optional[str]

container\_id: str

outputs: Optional[List[Output]]

class OutputLogs: …

logs: str

type: Literal["logs"]

class OutputImage: …

type: Literal["image"]

url: str

status: Literal["in\_progress", "completed", "incomplete", 2 more]

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: Literal["code\_interpreter\_call"]

agent: Optional[Agent]

agent\_name: str

class LocalShellCall: …

A tool call to run a command on the local shell.

id: str

action: LocalShellCallAction

command: List[str]

env: Dict[str, str]

type: Literal["exec"]

timeout\_ms: Optional[int]

user: Optional[str]

working\_directory: Optional[str]

call\_id: str

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["local\_shell\_call"]

agent: Optional[LocalShellCallAgent]

agent\_name: str

class LocalShellCallOutput: …

The output of a local shell tool call.

id: str

output: str

type: Literal["local\_shell\_call\_output"]

agent: Optional[LocalShellCallOutputAgent]

agent\_name: str

status: Optional[Literal["in\_progress", "completed", "incomplete"]]

"in\_progress"

"completed"

"incomplete"

class BetaResponseFunctionShellToolCall: …

A tool call that executes one or more shell commands in a managed environment.

id: str

action: Action

commands: List[str]

max\_output\_length: Optional[int]

Optional maximum number of characters to return from each command.

timeout\_ms: Optional[int]

Optional timeout in milliseconds for the commands.

call\_id: str

environment: Optional[Environment]

Represents the use of a local environment to perform shell actions.

class BetaResponseLocalEnvironment: …

Represents the use of a local environment to perform shell actions.

type: Literal["local"]

The environment type. Always `local`.

class BetaResponseContainerReference: …

Represents a container created with /v1/containers.

container\_id: str

type: Literal["container\_reference"]

The environment type. Always `container_reference`.

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

type: Literal["shell\_call"]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

created\_by: Optional[str]

The ID of the entity that created this tool call.

class BetaResponseFunctionShellToolCallOutput: …

The output of a shell tool call that was emitted.

id: str

The unique ID of the shell call output. Populated when this item is returned via API.

call\_id: str

max\_output\_length: Optional[int]

The maximum length of the shell command output. This is generated by the model and should be passed back with the raw output.

output: List[Output]

An array of shell call output contents

outcome: OutputOutcome

Represents either an exit outcome (with an exit code) or a timeout outcome for a shell call output chunk.

class OutputOutcomeTimeout: …

Indicates that the shell call exceeded its configured time limit.

type: Literal["timeout"]

The outcome type. Always `timeout`.

class OutputOutcomeExit: …

exit\_code: int

Exit code from the shell process.

type: Literal["exit"]

stderr: str

The standard error output that was captured.

stdout: str

The standard output that was captured.

created\_by: Optional[str]

The identifier of the actor that created the item.

status: Literal["in\_progress", "completed", "incomplete"]

The status of the shell call output. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

type: Literal["shell\_call\_output"]

The type of the shell call output. Always `shell_call_output`.

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseApplyPatchToolCall: …

A tool call that applies file diffs by creating, deleting, or updating files.

id: str

call\_id: str

operation: Operation

One of the create\_file, delete\_file, or update\_file operations applied via apply\_patch.

class OperationCreateFile: …

Instruction describing how to create a file via the apply\_patch tool.

diff: str

Diff to apply.

path: str

Path of the file to create.

type: Literal["create\_file"]

Create a new file with the provided diff.

class OperationDeleteFile: …

Instruction describing how to delete a file via the apply\_patch tool.

path: str

Path of the file to delete.

type: Literal["delete\_file"]

Delete the specified file.

class OperationUpdateFile: …

Instruction describing how to update a file via the apply\_patch tool.

diff: str

Diff to apply.

path: str

Path of the file to update.

type: Literal["update\_file"]

Update an existing file with the provided diff.

status: Literal["in\_progress", "completed"]

"in\_progress"

"completed"

type: Literal["apply\_patch\_call"]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

created\_by: Optional[str]

The ID of the entity that created this tool call.

class BetaResponseApplyPatchToolCallOutput: …

The output emitted by an apply patch tool call.

id: str

call\_id: str

status: Literal["completed", "failed"]

"completed"

"failed"

type: Literal["apply\_patch\_call\_output"]

agent: Optional[Agent]

agent\_name: str

caller: Optional[Caller]

class CallerDirect: …

type: Literal["direct"]

class CallerProgram: …

caller\_id: str

type: Literal["program"]

created\_by: Optional[str]

The ID of the entity that created this tool call output.

output: Optional[str]

Optional textual output returned by the apply patch tool.

class McpListTools: …

A list of tools available on an MCP server.

id: str

server\_label: str

tools: List[McpListToolsTool]

input\_schema: object

name: str

annotations: Optional[object]

description: Optional[str]

type: Literal["mcp\_list\_tools"]

agent: Optional[McpListToolsAgent]

agent\_name: str

error: Optional[str]

class McpApprovalRequest: …

A request for human approval of a tool invocation.

id: str

arguments: str

name: str

server\_label: str

type: Literal["mcp\_approval\_request"]

agent: Optional[McpApprovalRequestAgent]

agent\_name: str

class McpApprovalResponse: …

A response to an MCP approval request.

id: str

approval\_request\_id: str

approve: bool

type: Literal["mcp\_approval\_response"]

agent: Optional[McpApprovalResponseAgent]

agent\_name: str

reason: Optional[str]

class McpCall: …

An invocation of a tool on an MCP server.

id: str

arguments: str

name: str

server\_label: str

type: Literal["mcp\_call"]

agent: Optional[McpCallAgent]

agent\_name: str

approval\_request\_id: Optional[str]

error: Optional[str]

output: Optional[str]

status: Optional[Literal["in\_progress", "completed", "incomplete", 2 more]]

"in\_progress"

"completed"

"incomplete"

"calling"

"failed"

class BetaResponseCustomToolCallItem: …

id: str

The unique ID of the custom tool call item.

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

created\_by: Optional[str]

The identifier of the actor that created the item.

class BetaResponseCustomToolCallOutputItem: …

id: str

The unique ID of the custom tool call output item.

status: Literal["in\_progress", "completed", "incomplete"]

"in\_progress"

"completed"

"incomplete"

created\_by: Optional[str]

The identifier of the actor that created the item.

first\_id: str

The ID of the first item in the list.

has\_more: bool

Whether there are more items available.

last\_id: str

The ID of the last item in the list.

object: Literal["list"]

The type of object returned, must be `list`.

#### ResponsesInput Tokens

##### [Get input token counts](/api/reference/python/resources/beta/subresources/responses/subresources/input_tokens/methods/count)

beta.responses.input\_tokens.count(InputTokenCountParams\*\*kwargs)  -> [InputTokenCountResponse](/api/reference/python/resources/beta#(resource)%20beta.responses.input_tokens%20%3E%20(model)%20input_token_count_response%20%3E%20(schema))

POST/responses/input\_tokens

##### ModelsExpand Collapse

class InputTokenCountResponse: …

input\_tokens: int

object: Literal["response.input\_tokens"]
