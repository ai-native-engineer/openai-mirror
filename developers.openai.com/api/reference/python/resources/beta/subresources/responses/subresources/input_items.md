<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/responses/subresources/input_items/ -->

[API Reference](/api/reference/python)

[Beta](/api/reference/python/resources/beta)

[Responses](/api/reference/python/resources/beta/subresources/responses)

# Input Items

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
