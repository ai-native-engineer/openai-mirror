<!-- source: https://developers.openai.com/api/reference/resources/live/ -->

# Live

##### [Create session](/api/reference/resources/live/methods/create)

POST/live/sessions

##### ModelsExpand Collapse

AudioFormat = object { rate, type }  or object { rate, type }  or object { rate, type }

Audio encoding and sample rate for audio sent and received over a Live WebSocket connection. WebRTC and SIP negotiate their media format separately.

AudioPCM object { rate, type }

Raw, mono 16-bit little-endian PCM audio for a Live WebSocket connection.

rate: 16000 or 24000

Audio sample rate in hertz. Live WebSocket PCM audio supports 16000 or 24000 Hz.

minimum16000

maximum24000

16000

24000

type: "audio/pcm"

The audio encoding. Always `audio/pcm`.

AudioPCMU object { rate, type }

Raw, mono G.711 μ-law audio for a Live WebSocket connection.

rate: number

Audio sample rate in hertz. G.711 audio uses 8000 Hz.

minimum8000

maximum8000

type: "audio/pcmu"

The audio encoding. Always `audio/pcmu`.

AudioPCMA object { rate, type }

Raw, mono G.711 A-law audio for a Live WebSocket connection.

rate: number

Audio sample rate in hertz. G.711 audio uses 8000 Hz.

minimum8000

maximum8000

type: "audio/pcma"

The audio encoding. Always `audio/pcma`.

ClientConfig object { data\_channel }

Startup-only capabilities for an untrusted frontend attached to a unified WebRTC session. Trusted sideband connections are unaffected.

data\_channel: [DataChannelConfig](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20data_channel_config%20%3E%20(schema)) { allowed\_client\_events, allowed\_server\_events }

Client and server event permissions for the WebRTC frontend data channel.

ClientDelegation object { type }

Delegate tasks to your application. The Live session emits delegation events that your backend handles.

type: "client"

The delegation owner. Always `client` for tasks handled by your application.

ClientEvent = [SessionStartEvent](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20session_start_event%20%3E%20(schema)) { session, type, event\_id }  or [SessionUpdateEvent](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20session_update_event%20%3E%20(schema)) { session, type, event\_id }  or [InputAudioAppendEvent](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20input_audio_append_event%20%3E%20(schema)) { audio, type, event\_id }  or 8 more

Client events for Live. Initialize a primary WebSocket with session.start and wait for session.started. WebRTC creation already starts the session. Audio append is primary WebSocket-only. See the [Live prompting guide](https://developers.openai.com/api/docs/guides/live-prompting) before writing frontend instructions and delegation policies.

SessionStartEvent object { session, type, event\_id }

Start a Live session on a primary WebSocket. Send this event before other commands and wait for `session.started`.

session: [SessionConfig](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20session_config%20%3E%20(schema)) { model, audio, client, 4 more }

Initial configuration for a primary WebSocket. Send session.start first and wait for session.started before application commands. WebRTC creation already starts the session; do not send this event again on its data channel.

type: "session.start"

The Live client event type. Always `session.start`.

event\_id: optional string or null

Optional client identifier for correlating this command with a server event’s client\_event\_id or error.client\_event\_id.

maxLength512

SessionUpdateEvent object { session, type, event\_id }

Update the delegation settings of an active Live session. The server acknowledges accepted changes with `session.updated`.

session: [SessionUpdateConfig](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20session_update_config%20%3E%20(schema)) { delegation }

Sparse delegation updates. Omitted settings retain their values. The delegation type cannot change, including resetting Responses delegation to null or client. Model, frontend instructions, audio, and startup input are immutable.

type: "session.update"

The Live client event type. Always `session.update`.

event\_id: optional string or null

Optional client identifier for correlating this command with a server event’s client\_event\_id or error.client\_event\_id.

maxLength512

InputAudioAppendEvent object { audio, type, event\_id }

Send audio to a Live session over its primary WebSocket. WebRTC and SIP sessions send audio over their media transport.

audio: string

Base64-encoded raw audio in the startup-selected format, without a WAV or other container header. Primary WebSocket only; media transports use their audio track. Audio appends have no acknowledgment. Reflected sideband server events reuse this event type and audio key, with no timestamps or event\_id; their audio is always mono PCM16LE at 24 kHz.

minLength1

type: "session.input\_audio.append"

The Live client event type. Always `session.input_audio.append`.

event\_id: optional string or null

Optional client identifier for correlating this command with a server event’s client\_event\_id or error.client\_event\_id.

maxLength512

InputAudioMuteEvent object { type, event\_id }

Mute audio input to the Live model without closing the session. The server acknowledges with `session.input_audio.muted`.

type: "session.input\_audio.mute"

The Live client event type. Always `session.input_audio.mute`.

event\_id: optional string or null

Optional client identifier for correlating this command with a server event’s client\_event\_id or error.client\_event\_id.

maxLength512

InputAudioUnmuteEvent object { type, event\_id }

Resume audio input to a Live model after muting it. The server acknowledges with `session.input_audio.unmuted`.

type: "session.input\_audio.unmute"

The Live client event type. Always `session.input_audio.unmute`.

event\_id: optional string or null

Optional client identifier for correlating this command with a server event’s client\_event\_id or error.client\_event\_id.

maxLength512

InstructionsAppendEvent object { content, delegation\_id, type, event\_id }

Append instructions to the Live conversation while it is running, optionally associating them with an existing client delegation.

content: string

Instruction text to append, limited to 500 tokens. This is a plain string, not an array of content parts.

delegation\_id: string or null

Required, nullable. Set null for general session context, or use the ID from session.delegation.created for an existing client delegation. Non-null IDs are not accepted with Responses delegation.

minLength1

type: "session.instructions.append"

The Live client event type. Always `session.instructions.append`.

event\_id: optional string or null

Optional client identifier for correlating this command with a server event’s client\_event\_id or error.client\_event\_id.

maxLength512

ThinkingAppendEvent object { content, delegation\_id, type, event\_id }

Provide silent reasoning or progress context to the Live model, optionally for an existing client delegation.

content: string

Silent reasoning or progress context, limited to 500 tokens. It does not directly request speech, but can influence later speech and is not a secrecy boundary.

delegation\_id: string or null

Required, nullable. Set null for general session context, or use the ID from session.delegation.created for an existing client delegation. Non-null IDs are not accepted with Responses delegation.

minLength1

type: "session.thinking.append"

The Live client event type. Always `session.thinking.append`.

event\_id: optional string or null

Optional client identifier for correlating this command with a server event’s client\_event\_id or error.client\_event\_id.

maxLength512

CommentaryAppendEvent object { content, delegation\_id, type, event\_id }

Provide context the Live model can communicate to the user, optionally for an existing client delegation.

content: string

Speakable context for the Live model, limited to 500 tokens. Use this for a result the model should communicate; use session.thinking.append for silent context.

delegation\_id: string or null

Required, nullable. Set null for general session context, or use the ID from session.delegation.created for an existing client delegation. Non-null IDs are not accepted with Responses delegation.

minLength1

type: "session.commentary.append"

The Live client event type. Always `session.commentary.append`.

event\_id: optional string or null

Optional client identifier for correlating this command with a server event’s client\_event\_id or error.client\_event\_id.

maxLength512

ResponseItemCreateEvent object { item, type, event\_id }

Add an input item to the Live session’s Responses backend. Requires Responses delegation; use `response.create` to request a response.

item: [EasyInputMessage](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)) { content, role, phase, type }  or object { content, role, status, type }  or [ResponseOutputMessage](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_output_message%20%3E%20(schema)) { id, content, role, 3 more }  or 30 more

An input item to append to the Responses backend conversation, such as a user message or a function tool result.

EasyInputMessage object { content, role, phase, type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: string or [ResponseInputMessageContentList](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_message_content_list%20%3E%20(schema)) { , ,  }

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

TextInput = string

A text input to the model.

ResponseInputMessageContentList = array of [ResponseInputContent](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_content%20%3E%20(schema))

A list of one or many input items to the model, containing different content
types.

ResponseInputText object { text, type, prompt\_cache\_breakpoint }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

ResponseInputImage object { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](/api/docs/guides/images-vision).

detail: [ImageDetail](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20image_detail%20%3E%20(schema))

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

type: "input\_image"

The type of the input item. Always `input_image`.

file\_id: optional string or null

The ID of the file to be sent to the model.

image\_url: optional string or null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

prompt\_cache\_breakpoint: optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

ResponseInputFile object { type, detail, file\_data, 4 more }

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

file\_id: optional string or null

The ID of the file to be sent to the model.

file\_url: optional string

The URL of the file to be sent to the model.

formaturi

filename: optional string

The name of the file to be sent to the model.

prompt\_cache\_breakpoint: optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

role: "user" or "assistant" or "system" or "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

"user"

"assistant"

"system"

"developer"

phase: optional "commentary" or "final\_answer" or null

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

"commentary"

"final\_answer"

type: optional "message"

The type of the message input. Always `message`.

Message object { content, role, status, type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role.

content: [ResponseInputMessageContentList](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_message_content_list%20%3E%20(schema)) { , ,  }

A list of one or many input items to the model, containing different content
types.

role: "user" or "system" or "developer"

The role of the message input. One of `user`, `system`, or `developer`.

"user"

"system"

"developer"

status: optional "in\_progress" or "completed" or "incomplete"

The status of item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: optional "message"

The type of the message input. Always set to `message`.

ResponseOutputMessage object { id, content, role, 3 more }

An output message from the model.

The unique ID of the output message.

content: array of [ResponseOutputText](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_output_text%20%3E%20(schema)) { annotations, logprobs, text, type }  or [ResponseOutputRefusal](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_output_refusal%20%3E%20(schema)) { refusal, type }

The content of the output message.

ResponseOutputText object { annotations, logprobs, text, type }

A text output from the model.

annotations: array of object { file\_id, filename, index, type }  or object { end\_index, start\_index, title, 2 more }  or object { container\_id, end\_index, file\_id, 3 more }  or object { file\_id, index, type }

The annotations of the text output.

FileCitation object { file\_id, filename, index, type }

A citation to a file.

file\_id: string

The ID of the file.

filename: string

The filename of the file cited.

index: number

The index of the file in the list of files.

type: "file\_citation"

The type of the file citation. Always `file_citation`.

URLCitation object { end\_index, start\_index, title, 2 more }

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

formaturi

ContainerFileCitation object { container\_id, end\_index, file\_id, 3 more }

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

FilePath object { file\_id, index, type }

A path to a file.

file\_id: string

The ID of the file.

index: number

The index of the file in the list of files.

type: "file\_path"

The type of the file path. Always `file_path`.

logprobs: array of object { token, bytes, logprob, top\_logprobs }

token: string

bytes: array of number

logprob: number

top\_logprobs: array of object { token, bytes, logprob }

token: string

bytes: array of number

logprob: number

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

ResponseOutputRefusal object { refusal, type }

A refusal from the model.

refusal: string

The refusal explanation from the model.

type: "refusal"

The type of the refusal. Always `refusal`.

role: "assistant"

The role of the output message. Always `assistant`.

status: "in\_progress" or "completed" or "incomplete"

The status of the message input. One of `in_progress`, `completed`, or
`incomplete`. Populated when input items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: "message"

The type of the output message. Always `message`.

phase: optional "commentary" or "final\_answer" or null

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

"commentary"

"final\_answer"

FileSearchCall object { id, queries, status, 2 more }

The results of a file search tool call. See the
[file search guide](/api/docs/guides/tools-file-search) for more information.

The unique ID of the file search tool call.

queries: array of string

The queries used to search for files.

status: "in\_progress" or "searching" or "completed" or 2 more

The status of the file search tool call. One of `in_progress`,
`searching`, `incomplete` or `failed`,

"in\_progress"

"searching"

"completed"

"incomplete"

"failed"

type: "file\_search\_call"

The type of the file search tool call. Always `file_search_call`.

results: optional array of object { attributes, file\_id, filename, 2 more }  or null

The results of the file search tool call.

attributes: optional map[string or number or boolean] or null

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

string

number

boolean

file\_id: optional string

The unique ID of the file.

filename: optional string

The name of the file.

score: optional number

The relevance score of the file - a value between 0 and 1.

formatfloat

text: optional string

The text that was retrieved from the file.

ComputerCall object { id, call\_id, pending\_safety\_checks, 4 more }

A tool call to a computer use tool. See the
[computer use guide](/api/docs/guides/tools-computer-use) for more information.

The unique ID of the computer call.

call\_id: string

An identifier used when responding to the tool call with output.

pending\_safety\_checks: array of object { id, code, message }

The pending safety checks for the computer call.

The ID of the pending safety check.

code: optional string or null

The type of the pending safety check.

message: optional string or null

Details about the pending safety check.

status: "in\_progress" or "completed" or "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: "computer\_call"

The type of the computer call. Always `computer_call`.

action: optional [ComputerAction](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20computer_action%20%3E%20(schema))

A click action.

actions: optional [ComputerActionList](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20computer_action_list%20%3E%20(schema)) { Click, DoubleClick, Drag, 6 more }

Flattened batched actions for `computer_use`. Each action includes an
`type` discriminator and action-specific fields.

ComputerCallOutput object { call\_id, output, type, 3 more }

The output of a computer tool call.

call\_id: string

The ID of the computer tool call that produced the output.

minLength1

maxLength64

output: [ResponseComputerToolCallOutputScreenshot](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_computer_tool_call_output_screenshot%20%3E%20(schema)) { type, file\_id, image\_url }

A computer screenshot image used with the computer use tool.

type: "computer\_call\_output"

The type of the computer tool call output. Always `computer_call_output`.

id: optional string or null

The ID of the computer tool call output.

acknowledged\_safety\_checks: optional array of object { id, code, message }  or null

The safety checks reported by the API that have been acknowledged by the developer.

The ID of the pending safety check.

code: optional string or null

The type of the pending safety check.

message: optional string or null

Details about the pending safety check.

status: optional "in\_progress" or "completed" or "incomplete" or null

The status of the message input. One of `in_progress`, `completed`, or `incomplete`. Populated when input items are returned via API.

"in\_progress"

"completed"

"incomplete"

WebSearchCall object { id, action, status, type }

The results of a web search tool call. See the
[web search guide](/api/docs/guides/tools-web-search) for more information.

The unique ID of the web search tool call.

action: object { type, queries, query, sources }  or object { type, url }  or object { pattern, type, url }

An object describing the specific action taken in this web search call.
Includes details on how the model used the web (search, open\_page, find\_in\_page).

Search object { type, queries, query, sources }

Action type “search” - Performs a web search query.

type: "search"

The action type.

queries: optional array of string

The search queries.

Deprecatedquery: optional string

The search query.

sources: optional array of object { type, url }

The sources used in the search.

type: "url"

The type of source. Always `url`.

url: string

The URL of the source.

formaturi

OpenPage object { type, url }

Action type “open\_page” - Opens a specific URL from search results.

type: "open\_page"

The action type.

url: optional string or null

The URL opened by the model.

formaturi

FindInPage object { pattern, type, url }

Action type “find\_in\_page”: Searches for a pattern within a loaded page.

pattern: string

The pattern or text to search for within the page.

type: "find\_in\_page"

The action type.

url: string

The URL of the page searched for the pattern.

formaturi

status: "in\_progress" or "searching" or "completed" or 2 more

The status of the web search tool call.

"in\_progress"

"searching"

"completed"

"failed"

"incomplete"

type: "web\_search\_call"

The type of the web search tool call. Always `web_search_call`.

FunctionCall object { arguments, call\_id, name, 6 more }

A tool call to run a function. See the
[function calling guide](/api/docs/guides/function-calling) for more information.

arguments: string

A JSON string of the arguments to pass to the function.

call\_id: string

The unique ID of the function tool call generated by the model.

The name of the function to run.

type: "function\_call"

The type of the function tool call. Always `function_call`.

id: optional string

The unique ID of the function tool call.

async: optional boolean

Whether the function tool call runs asynchronously.

caller: optional object { type }  or object { caller\_id, type }  or null

The execution context that produced this tool call.

Direct object { type }

type: "direct"

Program object { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

type: "program"

namespace: optional string

The namespace of the function to run.

status: optional "in\_progress" or "completed" or "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

FunctionCallOutput object { output, type, id, 5 more }

The output of a function tool call.

output: string or array of [ResponseInputTextContent](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text_content%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [ResponseInputImageContent](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_image_content%20%3E%20(schema)) { type, detail, file\_id, 2 more }  or [ResponseInputFileContent](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_file_content%20%3E%20(schema)) { type, detail, file\_data, 4 more }

Text, image, or file output of the function tool call.

string

A JSON string of the output of the function tool call.

array of [ResponseInputTextContent](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text_content%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [ResponseInputImageContent](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_image_content%20%3E%20(schema)) { type, detail, file\_id, 2 more }  or [ResponseInputFileContent](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_file_content%20%3E%20(schema)) { type, detail, file\_data, 4 more }

An array of content outputs (text, image, file) for the function tool call.

ResponseInputTextContent object { text, type, prompt\_cache\_breakpoint }

A text input to the model.

text: string

The text input to the model.

maxLength10485760

type: "input\_text"

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: optional object { mode }  or null

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

ResponseInputImageContent object { type, detail, file\_id, 2 more }

An image input to the model. Learn about [image inputs](/api/docs/guides/images-vision)

type: "input\_image"

The type of the input item. Always `input_image`.

detail: optional [ImageDetail](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20image_detail%20%3E%20(schema)) or null

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

file\_id: optional string or null

The ID of the file to be sent to the model.

image\_url: optional string or null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

maxLength20971520

formaturi

prompt\_cache\_breakpoint: optional object { mode }  or null

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

ResponseInputFileContent object { type, detail, file\_data, 4 more }

A file input to the model.

type: "input\_file"

The type of the input item. Always `input_file`.

detail: optional "auto" or "low" or "high"

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

"low"

"high"

file\_data: optional string or null

The base64-encoded data of the file to be sent to the model.

maxLength73400320

file\_id: optional string or null

The ID of the file to be sent to the model.

file\_url: optional string or null

The URL of the file to be sent to the model.

formaturi

filename: optional string or null

The name of the file to be sent to the model.

prompt\_cache\_breakpoint: optional object { mode }  or null

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

type: "function\_call\_output"

The type of the function tool call output. Always `function_call_output`.

id: optional string or null

The unique ID of the function tool call output. Populated when this item is returned via API.

call\_id: optional string or null

The unique ID of the function tool call generated by the model.

minLength1

maxLength64

caller: optional object { type }  or object { caller\_id, type }  or null

The execution context that produced this tool call.

Direct object { type }

type: "direct"

The caller type. Always `direct`.

Program object { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

minLength1

maxLength64

type: "program"

The caller type. Always `program`.

name: optional string or null

The name of the tool that produced the output.

minLength1

maxLength128

namespace: optional string or null

The namespace of the tool that produced the output.

minLength1

maxLength64

status: optional "in\_progress" or "completed" or "incomplete" or null

The status of the item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

ToolSearchCall object { arguments, type, id, 3 more }

arguments: unknown

The arguments supplied to the tool search call.

type: "tool\_search\_call"

The item type. Always `tool_search_call`.

id: optional string or null

The unique ID of this tool search call.

call\_id: optional string or null

The unique ID of the tool search call generated by the model.

minLength1

maxLength64

execution: optional "server" or "client"

Whether tool search was executed by the server or by the client.

"server"

"client"

status: optional "in\_progress" or "completed" or "incomplete" or null

The status of the tool search call.

"in\_progress"

"completed"

"incomplete"

ToolSearchOutput object { tools, type, id, 3 more }

tools: array of object { name, parameters, strict, 6 more }  or object { type, vector\_store\_ids, filters, 2 more }  or object { type }  or 13 more

The loaded tool definitions returned by the tool search output.

Function object { name, parameters, strict, 6 more }

Defines a function in your own code the model can choose to call. Learn more about [function calling](/api/docs/guides/function-calling).

The name of the function to call.

parameters: map[unknown] or null

A JSON schema object describing the parameters of the function.

strict: boolean or null

Whether strict parameter validation is enforced for this function tool.

type: "function"

The type of the function tool. Always `function`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

async: optional boolean

defer\_loading: optional boolean

Whether this function is deferred and loaded via tool search.

description: optional string or null

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema: optional map[unknown] or null

A JSON schema object describing the JSON value encoded in string outputs for this function.

FileSearch object { type, vector\_store\_ids, filters, 2 more }

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](/api/docs/guides/tools-file-search).

type: "file\_search"

The type of the file search tool. Always `file_search`.

vector\_store\_ids: array of string

The IDs of the vector stores to search.

filters: optional [ComparisonFilter](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key, type, value }  or [CompoundFilter](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20compound_filter%20%3E%20(schema)) { filters, type }  or null

A filter to apply.

ComparisonFilter object { key, type, value }

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

string

number

boolean

array of string or number

string

number

CompoundFilter object { filters, type }

Combine multiple filters using `and` or `or`.

filters: array of [ComparisonFilter](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key, type, value }  or unknown

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

ComparisonFilter object { key, type, value }

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

string

number

boolean

array of string or number

string

number

unknown

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

Computer object { type }

A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

type: "computer"

The type of the computer tool. Always `computer`.

ComputerUsePreview object { display\_height, display\_width, environment, type }

A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

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

WebSearch object { type, external\_web\_access, filters, 2 more }

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](/api/docs/guides/tools-web-search).

type: "web\_search" or "web\_search\_2025\_08\_26"

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

"web\_search"

"web\_search\_2025\_08\_26"

external\_web\_access: optional boolean

Allow live internet access for web search. Defaults to true when omitted. When false, the web search tool runs in offline/cache-only mode and will not fetch new external content.

filters: optional object { allowed\_domains }  or null

Filters for the search.

allowed\_domains: optional array of string or null

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size: optional "low" or "medium" or "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location: optional object { city, country, region, 2 more }  or null

The approximate location of the user.

city: optional string or null

Free text input for the city of the user, e.g. `San Francisco`.

country: optional string or null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region: optional string or null

Free text input for the region of the user, e.g. `California`.

timezone: optional string or null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type: optional "approximate"

The type of location approximation. Always `approximate`.

Mcp object { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](/api/docs/guides/tools-connectors-mcp).

server\_label: string

A label for this MCP server, used to identify it in tool calls.

type: "mcp"

The type of the MCP tool. Always `mcp`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools: optional array of string or object { read\_only, tool\_names }  or null

List of allowed tool names or a filter object.

McpAllowedTools = array of string

A string array of allowed tool names

McpToolFilter object { read\_only, tool\_names }

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
about service connectors [here](/api/docs/guides/tools-connectors-mcp#connectors).

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

headers: optional map[string] or null

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval: optional object { always, never }  or "always" or "never" or null

Specify which of the MCP server’s tools require approval.

McpToolApprovalFilter object { always, never }

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

McpToolApprovalSetting = "always" or "never"

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

formaturi

tunnel\_id: optional string

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter object { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string or object { type, file\_ids, memory\_limit, network\_policy }

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

string

The container ID.

CodeInterpreterToolAuto object { type, file\_ids, memory\_limit, network\_policy }

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: "auto"

Always `auto`.

file\_ids: optional array of string

An optional list of uploaded files to make available to your code.

memory\_limit: optional "1g" or "4g" or "16g" or "64g" or null

The memory limit for the code interpreter container.

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [ContainerNetworkPolicyDisabled](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)) { type }  or [ContainerNetworkPolicyAllowlist](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

ContainerNetworkPolicyDisabled object { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

ContainerNetworkPolicyAllowlist object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: optional array of [ContainerNetworkPolicyDomainSecret](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

minLength1

maxLength10485760

type: "code\_interpreter"

The type of the code interpreter tool. Always `code_interpreter`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

ProgrammaticToolCalling object { type }

type: "programmatic\_tool\_calling"

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration object { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

The type of the image generation tool. Always `image_generation`.

action: optional "generate" or "edit" or "auto"

Whether to generate a new image or edit an existing image. Default: `auto`.

"generate"

"edit"

"auto"

background: optional "transparent" or "opaque" or "auto"

Set the background of the generated image. One of `transparent`, `opaque`,
or `auto`. `gpt-image-2.5-sunburst` and `gpt-image-2.5-flare`, including
their `2026-09-08` snapshots, support `opaque` and `transparent`
backgrounds. Transparent backgrounds are available for supported GPT Image
models. For `gpt-image-2` and `gpt-image-2-2026-04-21`, this support is in
preview. When using `transparent`, set the output format to `png` or `webp`.
Default: `auto`.

"transparent"

"opaque"

"auto"

input\_fidelity: optional "high" or "low" or null

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

model: optional string or "gpt-image-1" or "gpt-image-1-mini" or "gpt-image-1.5" or 6 more

The image generation model to use. One of `gpt-image-1`,
`gpt-image-1-mini`, `gpt-image-1.5`, `gpt-image-2`,
`gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`,
`gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`,
`gpt-image-2.5-flare-2026-09-08`, or `chatgpt-image-latest`. Default:
`gpt-image-1`.

string

"gpt-image-1" or "gpt-image-1-mini" or "gpt-image-1.5" or 6 more

The image generation model to use. One of `gpt-image-1`,
`gpt-image-1-mini`, `gpt-image-1.5`, `gpt-image-2`,
`gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`,
`gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`,
`gpt-image-2.5-flare-2026-09-08`, or `chatgpt-image-latest`. Default:
`gpt-image-1`.

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-1.5"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-2.5-sunburst"

"gpt-image-2.5-sunburst-2026-09-08"

"gpt-image-2.5-flare"

"gpt-image-2.5-flare-2026-09-08"

moderation: optional "auto" or "low"

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression: optional number

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format: optional "png" or "webp" or "jpeg"

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

"png"

"webp"

"jpeg"

partial\_images: optional number

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

quality: optional "low" or "medium" or "high" or 3 more

The quality of the generated image. The GPT image models support `low`,
`medium`, and `high`. `gpt-image-2.5-sunburst` and `gpt-image-2.5-flare`,
including their `2026-09-08` snapshots, also support `xhigh` and `max`.
Default: `auto`.

"low"

"medium"

"high"

"xhigh"

"max"

"auto"

size: optional string or "1024x1024" or "1024x1536" or "1536x1024" or "auto"

The size of the generated images. For `gpt-image-2`, `gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`, `gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`, and `gpt-image-2.5-flare-2026-09-08`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

string

"1024x1024" or "1024x1536" or "1536x1024" or "auto"

The size of the generated images. For `gpt-image-2`, `gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`, `gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`, and `gpt-image-2.5-flare-2026-09-08`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

LocalShell object { type }

A tool that allows the model to execute shell commands in a local environment.

type: "local\_shell"

The type of the local shell tool. Always `local_shell`.

Shell object { type, allowed\_callers, environment }

A tool that allows the model to execute shell commands.

type: "shell"

The type of the shell tool. Always `shell`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

environment: optional [ContainerAuto](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  or [LocalEnvironment](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20local_environment%20%3E%20(schema)) { type, skills }  or [ContainerReference](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_reference%20%3E%20(schema)) { container\_id, type }  or null

ContainerAuto object { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

Automatically creates a container for this request

file\_ids: optional array of string

An optional list of uploaded files to make available to your code.

memory\_limit: optional "1g" or "4g" or "16g" or "64g" or null

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [ContainerNetworkPolicyDisabled](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)) { type }  or [ContainerNetworkPolicyAllowlist](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

ContainerNetworkPolicyDisabled object { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

ContainerNetworkPolicyAllowlist object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: optional array of [ContainerNetworkPolicyDomainSecret](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

minLength1

maxLength10485760

skills: optional array of [SkillReference](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20skill_reference%20%3E%20(schema)) { skill\_id, type, version }  or [InlineSkill](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill%20%3E%20(schema)) { description, name, source, type }

An optional list of skills referenced by id or inline data.

SkillReference object { skill\_id, type, version }

skill\_id: string

The ID of the referenced skill.

minLength1

maxLength64

type: "skill\_reference"

References a skill created with the /v1/skills endpoint.

version: optional string

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

InlineSkill object { description, name, source, type }

description: string

The description of the skill.

The name of the skill.

source: [InlineSkillSource](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

Inline skill payload

type: "inline"

Defines an inline skill for this request.

LocalEnvironment object { type, skills }

type: "local"

Use a local computer environment.

skills: optional array of [LocalSkill](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema)) { description, name, path }

An optional list of skills.

description: string

The description of the skill.

The name of the skill.

path: string

The path to the directory containing the skill.

ContainerReference object { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

Custom object { name, type, allowed\_callers, 4 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](/api/docs/guides/function-calling#custom-tools)

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

async: optional boolean

Whether the tool response can be returned asynchronously versus immediately returned on next response creation.

defer\_loading: optional boolean

Whether this tool should be deferred and discovered via tool search.

description: optional string

Optional description of the custom tool, used to provide more context.

format: optional [CustomToolInputFormat](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))

The input format for the custom tool. Default is unconstrained text.

Namespace object { description, name, tools, type }

Groups function/custom tools under a shared namespace.

description: string

A description of the namespace shown to the model.

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: array of object { name, type, allowed\_callers, 6 more }  or object { name, type, allowed\_callers, 4 more }

The function/custom tools available inside this namespace.

Function object { name, type, allowed\_callers, 6 more }

minLength1

maxLength128

type: "function"

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

async: optional boolean

Whether the tool response can be returned asynchronously versus immediately returned on next response creation.

defer\_loading: optional boolean

Whether this function should be deferred and discovered via tool search.

description: optional string or null

output\_schema: optional map[unknown] or null

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters: optional unknown or null

strict: optional boolean or null

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

Custom object { name, type, allowed\_callers, 4 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](/api/docs/guides/function-calling#custom-tools)

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

async: optional boolean

Whether the tool response can be returned asynchronously versus immediately returned on next response creation.

defer\_loading: optional boolean

Whether this tool should be deferred and discovered via tool search.

description: optional string

Optional description of the custom tool, used to provide more context.

format: optional [CustomToolInputFormat](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))

The input format for the custom tool. Default is unconstrained text.

type: "namespace"

The type of the tool. Always `namespace`.

ToolSearch object { type, description, execution, parameters }

Hosted or BYOT tool search configuration for deferred tools.

type: "tool\_search"

The type of the tool. Always `tool_search`.

description: optional string or null

Description shown to the model for a client-executed tool search tool.

execution: optional "server" or "client"

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters: optional unknown or null

Parameter schema for a client-executed tool search tool.

WebSearchPreview object { type, search\_content\_types, search\_context\_size, user\_location }

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](/api/docs/guides/tools-web-search).

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

user\_location: optional object { type, city, country, 2 more }  or null

The user’s location.

type: "approximate"

The type of location approximation. Always `approximate`.

city: optional string or null

Free text input for the city of the user, e.g. `San Francisco`.

country: optional string or null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region: optional string or null

Free text input for the region of the user, e.g. `California`.

timezone: optional string or null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

ApplyPatch object { type, allowed\_callers }

Allows the assistant to create, delete, or update files using unified diffs.

type: "apply\_patch"

The type of the tool. Always `apply_patch`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

type: "tool\_search\_output"

The item type. Always `tool_search_output`.

id: optional string or null

The unique ID of this tool search output.

call\_id: optional string or null

The unique ID of the tool search call generated by the model.

minLength1

maxLength64

execution: optional "server" or "client"

Whether tool search was executed by the server or by the client.

"server"

"client"

status: optional "in\_progress" or "completed" or "incomplete" or null

The status of the tool search output.

"in\_progress"

"completed"

"incomplete"

AdditionalTools object { role, tools, type, id }

role: "developer"

The role that provided the additional tools. Only `developer` is supported.

tools: array of object { name, parameters, strict, 6 more }  or object { type, vector\_store\_ids, filters, 2 more }  or object { type }  or 13 more

A list of additional tools made available at this item.

Function object { name, parameters, strict, 6 more }

Defines a function in your own code the model can choose to call. Learn more about [function calling](/api/docs/guides/function-calling).

The name of the function to call.

parameters: map[unknown] or null

A JSON schema object describing the parameters of the function.

strict: boolean or null

Whether strict parameter validation is enforced for this function tool.

type: "function"

The type of the function tool. Always `function`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

async: optional boolean

defer\_loading: optional boolean

Whether this function is deferred and loaded via tool search.

description: optional string or null

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema: optional map[unknown] or null

A JSON schema object describing the JSON value encoded in string outputs for this function.

FileSearch object { type, vector\_store\_ids, filters, 2 more }

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](/api/docs/guides/tools-file-search).

type: "file\_search"

The type of the file search tool. Always `file_search`.

vector\_store\_ids: array of string

The IDs of the vector stores to search.

filters: optional [ComparisonFilter](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key, type, value }  or [CompoundFilter](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20compound_filter%20%3E%20(schema)) { filters, type }  or null

A filter to apply.

ComparisonFilter object { key, type, value }

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

string

number

boolean

array of string or number

string

number

CompoundFilter object { filters, type }

Combine multiple filters using `and` or `or`.

filters: array of [ComparisonFilter](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key, type, value }  or unknown

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

ComparisonFilter object { key, type, value }

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

string

number

boolean

array of string or number

string

number

unknown

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

Computer object { type }

A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

type: "computer"

The type of the computer tool. Always `computer`.

ComputerUsePreview object { display\_height, display\_width, environment, type }

A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

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

WebSearch object { type, external\_web\_access, filters, 2 more }

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](/api/docs/guides/tools-web-search).

type: "web\_search" or "web\_search\_2025\_08\_26"

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

"web\_search"

"web\_search\_2025\_08\_26"

external\_web\_access: optional boolean

Allow live internet access for web search. Defaults to true when omitted. When false, the web search tool runs in offline/cache-only mode and will not fetch new external content.

filters: optional object { allowed\_domains }  or null

Filters for the search.

allowed\_domains: optional array of string or null

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size: optional "low" or "medium" or "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location: optional object { city, country, region, 2 more }  or null

The approximate location of the user.

city: optional string or null

Free text input for the city of the user, e.g. `San Francisco`.

country: optional string or null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region: optional string or null

Free text input for the region of the user, e.g. `California`.

timezone: optional string or null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type: optional "approximate"

The type of location approximation. Always `approximate`.

Mcp object { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](/api/docs/guides/tools-connectors-mcp).

server\_label: string

A label for this MCP server, used to identify it in tool calls.

type: "mcp"

The type of the MCP tool. Always `mcp`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools: optional array of string or object { read\_only, tool\_names }  or null

List of allowed tool names or a filter object.

McpAllowedTools = array of string

A string array of allowed tool names

McpToolFilter object { read\_only, tool\_names }

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
about service connectors [here](/api/docs/guides/tools-connectors-mcp#connectors).

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

headers: optional map[string] or null

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval: optional object { always, never }  or "always" or "never" or null

Specify which of the MCP server’s tools require approval.

McpToolApprovalFilter object { always, never }

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

McpToolApprovalSetting = "always" or "never"

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

formaturi

tunnel\_id: optional string

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter object { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string or object { type, file\_ids, memory\_limit, network\_policy }

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

string

The container ID.

CodeInterpreterToolAuto object { type, file\_ids, memory\_limit, network\_policy }

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: "auto"

Always `auto`.

file\_ids: optional array of string

An optional list of uploaded files to make available to your code.

memory\_limit: optional "1g" or "4g" or "16g" or "64g" or null

The memory limit for the code interpreter container.

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [ContainerNetworkPolicyDisabled](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)) { type }  or [ContainerNetworkPolicyAllowlist](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

ContainerNetworkPolicyDisabled object { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

ContainerNetworkPolicyAllowlist object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: optional array of [ContainerNetworkPolicyDomainSecret](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

minLength1

maxLength10485760

type: "code\_interpreter"

The type of the code interpreter tool. Always `code_interpreter`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

ProgrammaticToolCalling object { type }

type: "programmatic\_tool\_calling"

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration object { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

The type of the image generation tool. Always `image_generation`.

action: optional "generate" or "edit" or "auto"

Whether to generate a new image or edit an existing image. Default: `auto`.

"generate"

"edit"

"auto"

background: optional "transparent" or "opaque" or "auto"

Set the background of the generated image. One of `transparent`, `opaque`,
or `auto`. `gpt-image-2.5-sunburst` and `gpt-image-2.5-flare`, including
their `2026-09-08` snapshots, support `opaque` and `transparent`
backgrounds. Transparent backgrounds are available for supported GPT Image
models. For `gpt-image-2` and `gpt-image-2-2026-04-21`, this support is in
preview. When using `transparent`, set the output format to `png` or `webp`.
Default: `auto`.

"transparent"

"opaque"

"auto"

input\_fidelity: optional "high" or "low" or null

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

model: optional string or "gpt-image-1" or "gpt-image-1-mini" or "gpt-image-1.5" or 6 more

The image generation model to use. One of `gpt-image-1`,
`gpt-image-1-mini`, `gpt-image-1.5`, `gpt-image-2`,
`gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`,
`gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`,
`gpt-image-2.5-flare-2026-09-08`, or `chatgpt-image-latest`. Default:
`gpt-image-1`.

string

"gpt-image-1" or "gpt-image-1-mini" or "gpt-image-1.5" or 6 more

The image generation model to use. One of `gpt-image-1`,
`gpt-image-1-mini`, `gpt-image-1.5`, `gpt-image-2`,
`gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`,
`gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`,
`gpt-image-2.5-flare-2026-09-08`, or `chatgpt-image-latest`. Default:
`gpt-image-1`.

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-1.5"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-2.5-sunburst"

"gpt-image-2.5-sunburst-2026-09-08"

"gpt-image-2.5-flare"

"gpt-image-2.5-flare-2026-09-08"

moderation: optional "auto" or "low"

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression: optional number

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format: optional "png" or "webp" or "jpeg"

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

"png"

"webp"

"jpeg"

partial\_images: optional number

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

quality: optional "low" or "medium" or "high" or 3 more

The quality of the generated image. The GPT image models support `low`,
`medium`, and `high`. `gpt-image-2.5-sunburst` and `gpt-image-2.5-flare`,
including their `2026-09-08` snapshots, also support `xhigh` and `max`.
Default: `auto`.

"low"

"medium"

"high"

"xhigh"

"max"

"auto"

size: optional string or "1024x1024" or "1024x1536" or "1536x1024" or "auto"

The size of the generated images. For `gpt-image-2`, `gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`, `gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`, and `gpt-image-2.5-flare-2026-09-08`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

string

"1024x1024" or "1024x1536" or "1536x1024" or "auto"

The size of the generated images. For `gpt-image-2`, `gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`, `gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`, and `gpt-image-2.5-flare-2026-09-08`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

LocalShell object { type }

A tool that allows the model to execute shell commands in a local environment.

type: "local\_shell"

The type of the local shell tool. Always `local_shell`.

Shell object { type, allowed\_callers, environment }

A tool that allows the model to execute shell commands.

type: "shell"

The type of the shell tool. Always `shell`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

environment: optional [ContainerAuto](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  or [LocalEnvironment](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20local_environment%20%3E%20(schema)) { type, skills }  or [ContainerReference](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_reference%20%3E%20(schema)) { container\_id, type }  or null

ContainerAuto object { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

Automatically creates a container for this request

file\_ids: optional array of string

An optional list of uploaded files to make available to your code.

memory\_limit: optional "1g" or "4g" or "16g" or "64g" or null

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [ContainerNetworkPolicyDisabled](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)) { type }  or [ContainerNetworkPolicyAllowlist](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

ContainerNetworkPolicyDisabled object { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

ContainerNetworkPolicyAllowlist object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: optional array of [ContainerNetworkPolicyDomainSecret](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

minLength1

maxLength10485760

skills: optional array of [SkillReference](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20skill_reference%20%3E%20(schema)) { skill\_id, type, version }  or [InlineSkill](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill%20%3E%20(schema)) { description, name, source, type }

An optional list of skills referenced by id or inline data.

SkillReference object { skill\_id, type, version }

skill\_id: string

The ID of the referenced skill.

minLength1

maxLength64

type: "skill\_reference"

References a skill created with the /v1/skills endpoint.

version: optional string

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

InlineSkill object { description, name, source, type }

description: string

The description of the skill.

The name of the skill.

source: [InlineSkillSource](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

Inline skill payload

type: "inline"

Defines an inline skill for this request.

LocalEnvironment object { type, skills }

type: "local"

Use a local computer environment.

skills: optional array of [LocalSkill](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema)) { description, name, path }

An optional list of skills.

description: string

The description of the skill.

The name of the skill.

path: string

The path to the directory containing the skill.

ContainerReference object { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

Custom object { name, type, allowed\_callers, 4 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](/api/docs/guides/function-calling#custom-tools)

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

async: optional boolean

Whether the tool response can be returned asynchronously versus immediately returned on next response creation.

defer\_loading: optional boolean

Whether this tool should be deferred and discovered via tool search.

description: optional string

Optional description of the custom tool, used to provide more context.

format: optional [CustomToolInputFormat](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))

The input format for the custom tool. Default is unconstrained text.

Namespace object { description, name, tools, type }

Groups function/custom tools under a shared namespace.

description: string

A description of the namespace shown to the model.

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: array of object { name, type, allowed\_callers, 6 more }  or object { name, type, allowed\_callers, 4 more }

The function/custom tools available inside this namespace.

Function object { name, type, allowed\_callers, 6 more }

minLength1

maxLength128

type: "function"

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

async: optional boolean

Whether the tool response can be returned asynchronously versus immediately returned on next response creation.

defer\_loading: optional boolean

Whether this function should be deferred and discovered via tool search.

description: optional string or null

output\_schema: optional map[unknown] or null

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters: optional unknown or null

strict: optional boolean or null

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

Custom object { name, type, allowed\_callers, 4 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](/api/docs/guides/function-calling#custom-tools)

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

async: optional boolean

Whether the tool response can be returned asynchronously versus immediately returned on next response creation.

defer\_loading: optional boolean

Whether this tool should be deferred and discovered via tool search.

description: optional string

Optional description of the custom tool, used to provide more context.

format: optional [CustomToolInputFormat](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))

The input format for the custom tool. Default is unconstrained text.

type: "namespace"

The type of the tool. Always `namespace`.

ToolSearch object { type, description, execution, parameters }

Hosted or BYOT tool search configuration for deferred tools.

type: "tool\_search"

The type of the tool. Always `tool_search`.

description: optional string or null

Description shown to the model for a client-executed tool search tool.

execution: optional "server" or "client"

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters: optional unknown or null

Parameter schema for a client-executed tool search tool.

WebSearchPreview object { type, search\_content\_types, search\_context\_size, user\_location }

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](/api/docs/guides/tools-web-search).

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

user\_location: optional object { type, city, country, 2 more }  or null

The user’s location.

type: "approximate"

The type of location approximation. Always `approximate`.

city: optional string or null

Free text input for the city of the user, e.g. `San Francisco`.

country: optional string or null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region: optional string or null

Free text input for the region of the user, e.g. `California`.

timezone: optional string or null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

ApplyPatch object { type, allowed\_callers }

Allows the assistant to create, delete, or update files using unified diffs.

type: "apply\_patch"

The type of the tool. Always `apply_patch`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

type: "additional\_tools"

The item type. Always `additional_tools`.

id: optional string or null

The unique ID of this additional tools item.

ConfigurationUpdate object { type, id, reasoning }

An update to the conversation’s response configuration. The configuration
remains in effect for subsequent responses until it is replaced by another
configuration update.

type: "configuration\_update"

The item type. Always `configuration_update`.

id: optional string or null

The unique ID of the configuration update item.

reasoning: optional object { effort }

Updates to reasoning configuration. Only effort is supported.

effort: optional [ReasoningEffort](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)) or null

The reasoning effort to use for subsequent responses until another
configuration update replaces it.

Reasoning object { id, summary, type, 3 more }

A description of the chain of thought used by a reasoning model while generating
a response. Be sure to include these items in your `input` to the Responses API
for subsequent turns of a conversation if you are manually
[managing context](/api/docs/guides/conversation-state).

The unique identifier of the reasoning content.

summary: array of [SummaryTextContent](/api/reference/resources/conversations#(resource)%20conversations%20%3E%20(model)%20summary_text_content%20%3E%20(schema)) { text, type }

Reasoning summary content.

text: string

A summary of the reasoning output from the model so far.

type: "summary\_text"

The type of the object. Always `summary_text`.

type: "reasoning"

The type of the object. Always `reasoning`.

content: optional array of object { text, type }

Reasoning text content.

text: string

The reasoning text from the model.

type: "reasoning\_text"

The type of the reasoning text. Always `reasoning_text`.

encrypted\_content: optional string or null

The encrypted content of the reasoning item. This is populated by default
for reasoning items returned by `POST /v1/responses` and WebSocket
`response.create` requests.

When streaming, use the completed reasoning item and its
`encrypted_content` from the `response.output_item.done` event in
subsequent requests. The `encrypted_content` in
`response.output_item.added` may be incomplete. This is especially
important when `store` is `false` or when using Zero Data Retention.

status: optional "in\_progress" or "completed" or "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

Compaction object { encrypted\_content, type, id }

A compaction item generated by the [`v1/responses/compact` API](/api/reference/resources/responses/methods/compact).

encrypted\_content: string

The encrypted content of the compaction summary.

maxLength20971520

type: "compaction"

The type of the item. Always `compaction`.

id: optional string or null

The ID of the compaction item.

ImageGenerationCall object { id, result, status, 7 more }

An image generation request made by the model.

The unique ID of the image generation call.

result: string or null

The generated image encoded in base64.

status: "in\_progress" or "completed" or "generating" or "failed"

The status of the image generation call.

"in\_progress"

"completed"

"generating"

"failed"

type: "image\_generation\_call"

The type of the image generation call. Always `image_generation_call`.

action: optional "generate" or "edit" or "auto" or null

The action used for image generation.

"generate"

"edit"

"auto"

background: optional "transparent" or "opaque" or "auto" or null

The background setting used for generation.

"transparent"

"opaque"

"auto"

output\_format: optional "png" or "webp" or "jpeg" or null

The output format used for generation.

"png"

"webp"

"jpeg"

quality: optional "low" or "medium" or "high" or 3 more or null

The quality of the image generated by the image generation tool call. One of `low`, `medium`, `high`, `xhigh`, `max`, or `auto`.

"low"

"medium"

"high"

"xhigh"

"max"

"auto"

revised\_prompt: optional string or null

The prompt that was used after any model prompt rewriting.

size: optional string or "1024x1024" or "1024x1536" or "1536x1024" or null

The image dimensions as a `WIDTHxHEIGHT` string, for example `1536x864`.

string

"1024x1024" or "1024x1536" or "1536x1024"

The image dimensions as a `WIDTHxHEIGHT` string, for example `1536x864`.

"1024x1024"

"1024x1536"

"1536x1024"

CodeInterpreterCall object { id, code, container\_id, 3 more }

A tool call to run code.

The unique ID of the code interpreter tool call.

code: string or null

The code to run, or null if not available.

container\_id: string

The ID of the container used to run the code.

outputs: array of object { logs, type }  or object { type, url }  or null

The outputs generated by the code interpreter, such as logs or images.
Can be null if no outputs are available.

Logs object { logs, type }

The logs output from the code interpreter.

logs: string

The logs output from the code interpreter.

type: "logs"

The type of the output. Always `logs`.

Image object { type, url }

The image output from the code interpreter.

type: "image"

The type of the output. Always `image`.

url: string

The URL of the image output from the code interpreter.

formaturi

status: "in\_progress" or "completed" or "incomplete" or 2 more

The status of the code interpreter tool call. Valid values are `in_progress`, `completed`, `incomplete`, `interpreting`, and `failed`.

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: "code\_interpreter\_call"

The type of the code interpreter tool call. Always `code_interpreter_call`.

LocalShellCall object { id, action, call\_id, 2 more }

A tool call to run a command on the local shell.

The unique ID of the local shell call.

action: object { command, env, type, 3 more }

Execute a shell command on the server.

command: array of string

The command to run.

env: map[string]

Environment variables to set for the command.

type: "exec"

The type of the local shell action. Always `exec`.

timeout\_ms: optional number or null

Optional timeout in milliseconds for the command.

user: optional string or null

Optional user to run the command as.

working\_directory: optional string or null

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

LocalShellCallOutput object { id, output, type, status }

The output of a local shell tool call.

The unique ID of the local shell tool call generated by the model.

output: string

A JSON string of the output of the local shell tool call.

type: "local\_shell\_call\_output"

The type of the local shell tool call output. Always `local_shell_call_output`.

status: optional "in\_progress" or "completed" or "incomplete" or null

The status of the item. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

ShellCall object { action, call\_id, type, 4 more }

A tool representing a request to execute one or more shell commands.

action: object { commands, max\_output\_length, timeout\_ms }

The shell commands and limits that describe how to run the tool call.

commands: array of string

Ordered shell commands for the execution environment to run.

max\_output\_length: optional number or null

Maximum number of UTF-8 characters to capture from combined stdout and stderr output.

timeout\_ms: optional number or null

Maximum wall-clock time in milliseconds to allow the shell commands to run.

call\_id: string

The unique ID of the shell tool call generated by the model.

minLength1

maxLength64

type: "shell\_call"

The type of the item. Always `shell_call`.

id: optional string or null

The unique ID of the shell tool call. Populated when this item is returned via API.

caller: optional object { type }  or object { caller\_id, type }  or null

The execution context that produced this tool call.

Direct object { type }

type: "direct"

The caller type. Always `direct`.

Program object { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

minLength1

maxLength64

type: "program"

The caller type. Always `program`.

environment: optional [LocalEnvironment](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20local_environment%20%3E%20(schema)) { type, skills }  or [ContainerReference](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_reference%20%3E%20(schema)) { container\_id, type }  or null

The environment to execute the shell commands in.

LocalEnvironment object { type, skills }

type: "local"

Use a local computer environment.

skills: optional array of [LocalSkill](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema)) { description, name, path }

An optional list of skills.

description: string

The description of the skill.

The name of the skill.

path: string

The path to the directory containing the skill.

ContainerReference object { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

status: optional "in\_progress" or "completed" or "incomplete" or null

The status of the shell call. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

ShellCallOutput object { call\_id, output, type, 4 more }

The streamed output items emitted by a shell tool call.

call\_id: string

The unique ID of the shell tool call generated by the model.

minLength1

maxLength64

output: array of [ResponseFunctionShellCallOutputContent](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_function_shell_call_output_content%20%3E%20(schema)) { outcome, stderr, stdout }

Captured chunks of stdout and stderr output, along with their associated outcomes.

outcome: object { type }  or object { exit\_code, type }

The exit or timeout outcome associated with this shell call.

Timeout object { type }

Indicates that the shell call exceeded its configured time limit.

type: "timeout"

The outcome type. Always `timeout`.

Exit object { exit\_code, type }

Indicates that the shell commands finished and returned an exit code.

exit\_code: number

The exit code returned by the shell process.

type: "exit"

The outcome type. Always `exit`.

stderr: string

Captured stderr output for the shell call.

maxLength10485760

stdout: string

Captured stdout output for the shell call.

maxLength10485760

type: "shell\_call\_output"

The type of the item. Always `shell_call_output`.

id: optional string or null

The unique ID of the shell tool call output. Populated when this item is returned via API.

caller: optional object { type }  or object { caller\_id, type }  or null

The execution context that produced this tool call.

Direct object { type }

type: "direct"

The caller type. Always `direct`.

Program object { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

minLength1

maxLength64

type: "program"

The caller type. Always `program`.

max\_output\_length: optional number or null

The maximum number of UTF-8 characters captured for this shell call’s combined output.

status: optional "in\_progress" or "completed" or "incomplete" or null

The status of the shell call output.

"in\_progress"

"completed"

"incomplete"

ApplyPatchCall object { call\_id, operation, status, 3 more }

A tool call representing a request to create, delete, or update files using diff patches.

call\_id: string

The unique ID of the apply patch tool call generated by the model.

minLength1

maxLength64

operation: object { diff, path, type }  or object { path, type }  or object { diff, path, type }

The specific create, delete, or update instruction for the apply\_patch tool call.

CreateFile object { diff, path, type }

Instruction for creating a new file via the apply\_patch tool.

diff: string

Unified diff content to apply when creating the file.

maxLength10485760

path: string

Path of the file to create relative to the workspace root.

minLength1

type: "create\_file"

The operation type. Always `create_file`.

DeleteFile object { path, type }

Instruction for deleting an existing file via the apply\_patch tool.

path: string

Path of the file to delete relative to the workspace root.

minLength1

type: "delete\_file"

The operation type. Always `delete_file`.

UpdateFile object { diff, path, type }

Instruction for updating an existing file via the apply\_patch tool.

diff: string

Unified diff content to apply to the existing file.

maxLength10485760

path: string

Path of the file to update relative to the workspace root.

minLength1

type: "update\_file"

The operation type. Always `update_file`.

status: "in\_progress" or "completed"

The status of the apply patch tool call. One of `in_progress` or `completed`.

"in\_progress"

"completed"

type: "apply\_patch\_call"

The type of the item. Always `apply_patch_call`.

id: optional string or null

The unique ID of the apply patch tool call. Populated when this item is returned via API.

caller: optional object { type }  or object { caller\_id, type }  or null

The execution context that produced this tool call.

Direct object { type }

type: "direct"

The caller type. Always `direct`.

Program object { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

minLength1

maxLength64

type: "program"

The caller type. Always `program`.

ApplyPatchCallOutput object { call\_id, status, type, 3 more }

The streamed output emitted by an apply patch tool call.

call\_id: string

The unique ID of the apply patch tool call generated by the model.

minLength1

maxLength64

status: "completed" or "failed"

The status of the apply patch tool call output. One of `completed` or `failed`.

"completed"

"failed"

type: "apply\_patch\_call\_output"

The type of the item. Always `apply_patch_call_output`.

id: optional string or null

The unique ID of the apply patch tool call output. Populated when this item is returned via API.

caller: optional object { type }  or object { caller\_id, type }  or null

The execution context that produced this tool call.

Direct object { type }

type: "direct"

The caller type. Always `direct`.

Program object { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

minLength1

maxLength64

type: "program"

The caller type. Always `program`.

output: optional string or null

Optional human-readable log text from the apply patch tool (e.g., patch results or errors).

maxLength10485760

McpListTools object { id, server\_label, tools, 2 more }

A list of tools available on an MCP server.

The unique ID of the list.

server\_label: string

The label of the MCP server.

tools: array of object { input\_schema, name, annotations, description }

The tools available on the server.

input\_schema: unknown

The JSON schema describing the tool’s input.

The name of the tool.

annotations: optional unknown or null

Additional annotations about the tool.

description: optional string or null

The description of the tool.

type: "mcp\_list\_tools"

The type of the item. Always `mcp_list_tools`.

error: optional string or null

Error message if the server could not list tools.

McpApprovalRequest object { id, arguments, name, 2 more }

A request for human approval of a tool invocation.

The unique ID of the approval request.

arguments: string

A JSON string of arguments for the tool.

The name of the tool to run.

server\_label: string

The label of the MCP server making the request.

type: "mcp\_approval\_request"

The type of the item. Always `mcp_approval_request`.

McpApprovalResponse object { approval\_request\_id, approve, type, 2 more }

A response to an MCP approval request.

approval\_request\_id: string

The ID of the approval request being answered.

approve: boolean

Whether the request was approved.

type: "mcp\_approval\_response"

The type of the item. Always `mcp_approval_response`.

id: optional string or null

The unique ID of the approval response

reason: optional string or null

Optional reason for the decision.

McpCall object { id, arguments, name, 6 more }

An invocation of a tool on an MCP server.

The unique ID of the tool call.

arguments: string

A JSON string of the arguments passed to the tool.

The name of the tool that was run.

server\_label: string

The label of the MCP server running the tool.

type: "mcp\_call"

The type of the item. Always `mcp_call`.

approval\_request\_id: optional string or null

Unique identifier for the MCP tool call approval request.
Include this value in a subsequent `mcp_approval_response` input to approve or reject the corresponding tool call.

error: optional [McpToolCallError](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20mcp_tool_call_error%20%3E%20(schema)) or null

The error from the tool call, if any.

output: optional string or null

The output from the tool call.

status: optional "in\_progress" or "completed" or "incomplete" or 2 more

The status of the tool call. One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.

"in\_progress"

"completed"

"incomplete"

"calling"

"failed"

CustomToolCallOutput object { call\_id, output, type, 2 more }

The output of a custom tool call from your code, being sent back to the model.

call\_id: string

The call ID, used to map this custom tool call output to a custom tool call.

output: string or array of [ResponseInputText](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [ResponseInputImage](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  or [ResponseInputFile](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more }

The output from the custom tool call generated by your code.
Can be a string or an list of output content.

StringOutput = string

A string of the output of the custom tool call.

OutputContentList = array of [ResponseInputText](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [ResponseInputImage](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  or [ResponseInputFile](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more }

Text, image, or file output of the custom tool call.

ResponseInputText object { text, type, prompt\_cache\_breakpoint }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

ResponseInputImage object { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](/api/docs/guides/images-vision).

detail: [ImageDetail](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20image_detail%20%3E%20(schema))

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

type: "input\_image"

The type of the input item. Always `input_image`.

file\_id: optional string or null

The ID of the file to be sent to the model.

image\_url: optional string or null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

prompt\_cache\_breakpoint: optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

ResponseInputFile object { type, detail, file\_data, 4 more }

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

file\_id: optional string or null

The ID of the file to be sent to the model.

file\_url: optional string

The URL of the file to be sent to the model.

formaturi

filename: optional string

The name of the file to be sent to the model.

prompt\_cache\_breakpoint: optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

type: "custom\_tool\_call\_output"

The type of the custom tool call output. Always `custom_tool_call_output`.

id: optional string

The unique ID of the custom tool call output in the OpenAI platform.

caller: optional object { type }  or object { caller\_id, type }  or null

The execution context that produced this tool call.

Direct object { type }

type: "direct"

The caller type. Always `direct`.

Program object { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

minLength1

maxLength64

type: "program"

The caller type. Always `program`.

CustomToolCall object { call\_id, input, name, 5 more }

A call to a custom tool created by the model.

call\_id: string

An identifier used to map this custom tool call to a tool call output.

input: string

The input for the custom tool call generated by the model.

The name of the custom tool being called.

type: "custom\_tool\_call"

The type of the custom tool call. Always `custom_tool_call`.

id: optional string

The unique ID of the custom tool call in the OpenAI platform.

async: optional boolean

Whether the custom tool call runs asynchronously.

caller: optional object { type }  or object { caller\_id, type }  or null

The execution context that produced this tool call.

Direct object { type }

type: "direct"

Program object { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

type: "program"

namespace: optional string

The namespace of the custom tool being called.

CompactionTrigger object { type, id }

Compacts the current context. Must be the final input item.

type: "compaction\_trigger"

The type of the item. Always `compaction_trigger`.

id: optional string or null

The unique ID of this compaction trigger.

ItemReference object { id, type }

An internal identifier for an item to reference.

The ID of the item to reference.

type: optional "item\_reference" or null

The type of item to reference. Always `item_reference`.

Program object { id, call\_id, code, 2 more }

The unique ID of this program item.

call\_id: string

The stable call ID of the program item.

minLength1

maxLength64

code: string

The JavaScript source executed by programmatic tool calling.

maxLength10485760

fingerprint: string

Opaque program replay fingerprint that must be round-tripped.

maxLength10485760

type: "program"

The item type. Always `program`.

ProgramOutput object { id, call\_id, result, 2 more }

The unique ID of this program output item.

call\_id: string

The call ID of the program item.

minLength1

maxLength64

result: string

The result produced by the program item.

maxLength10485760

status: "completed" or "incomplete"

The terminal status of the program output.

"completed"

"incomplete"

type: "program\_output"

The item type. Always `program_output`.

type: "response.item.create"

The Live client event type. Always `response.item.create`.

event\_id: optional string or null

Optional client identifier for correlating this command with a server event’s client\_event\_id or error.client\_event\_id.

maxLength512

ResponseCreateEvent object { type, event\_id }

Request a response from the Live session’s Responses backend, or continue a delegated response waiting for tool results. Requires Responses delegation.

type: "response.create"

The Live client event type. Always `response.create`.

event\_id: optional string or null

Optional client identifier for correlating this command with a server event’s client\_event\_id or error.client\_event\_id.

maxLength512

SessionCloseEvent object { type, event\_id }

Request that the Live session close. The terminal `session.closed` event contains the close reason and final usage.

type: "session.close"

The Live client event type. Always `session.close`.

event\_id: optional string or null

Optional client identifier for correlating this command with a server event’s client\_event\_id or error.client\_event\_id.

maxLength512

CommentaryAppendEvent object { content, delegation\_id, type, event\_id }

Provide context the Live model can communicate to the user, optionally for an existing client delegation.

content: string

Speakable context for the Live model, limited to 500 tokens. Use this for a result the model should communicate; use session.thinking.append for silent context.

delegation\_id: string or null

Required, nullable. Set null for general session context, or use the ID from session.delegation.created for an existing client delegation. Non-null IDs are not accepted with Responses delegation.

minLength1

type: "session.commentary.append"

The Live client event type. Always `session.commentary.append`.

event\_id: optional string or null

Optional client identifier for correlating this command with a server event’s client\_event\_id or error.client\_event\_id.

maxLength512

CommentaryAppendedEvent object { end\_ms, event\_id, start\_ms, 2 more }

Returned when a session.commentary.append command is accepted into the Live session timeline. Acknowledges the added commentary without guaranteeing exact wording or completed audio playback.

end\_ms: number

The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start\_ms.

event\_id: string

The unique ID of the Live server event.

start\_ms: number

The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

type: "session.commentary.appended"

The event type, always `session.commentary.appended`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

CustomVoice object { id }

minLength1

maxLength128

DataChannelConfig object { allowed\_client\_events, allowed\_server\_events }

Control which Live events an untrusted WebRTC frontend can send and receive over its data channel. These restrictions do not apply to trusted sideband connections.

allowed\_client\_events: optional "all" or array of string

Client event types that the frontend data channel may send. Use ‘all’ to allow every client event; an empty array allows none. Omission preserves the existing allow-all behavior.

"all"

array of string

allowed\_server\_events: optional "all" or array of [ServerEventSelector](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20server_event_selector%20%3E%20(schema)) { type, response\_event }

Server events that may be sent to the frontend data channel. Use ‘all’ to allow every server event; an empty array allows none. Omission preserves the existing allow-all behavior. Responses events use an object with type ‘response.event’ and a response\_event selector.

"all"

array of [ServerEventSelector](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20server_event_selector%20%3E%20(schema)) { type, response\_event }

type: string

The outer Live server event type. Use ‘response.event’ for Responses events.

minLength1

maxLength256

response\_event: optional string

The nested Responses event type. Required when type is ‘response.event’; forbidden for other event types.

minLength1

maxLength256

DelegationCreatedEvent object { delegation, event\_id, offset\_ms, 2 more }

Returned when the Live model delegates work to your application or a Responses backend. Contains delegation metadata and the position on the session timeline where the work was delegated.

delegation: object { id, target, type, response\_id }

The delegated work identifier and destination. This object contains metadata, not the task text.

The unique ID of the delegation. Use this as delegation\_id when replying to client-owned work or correlating Responses events.

target: "client" or "responses"

Where the Live model delegated the work: `client` for your application, or `responses` for the configured Responses backend.

"client" or "responses"

Where the Live model delegated the work: `client` for your application, or `responses` for the configured Responses backend.

"client"

"responses"

type: "delegation"

The object type, always `delegation`.

response\_id: optional string

The ID of the Responses API response associated with a Responses delegation. Omitted for client delegations.

event\_id: string

The unique ID of the Live server event.

offset\_ms: number

The position on the Live session timeline where the delegation was created, in milliseconds from the beginning of the session.

type: "session.delegation.created"

The event type, always `session.delegation.created`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

Error object { code, message, type, 2 more }

Details of an error encountered by the Live session, including the affected parameter or client command when available.

code: string

A machine-readable code identifying the Live error, such as `unknown_parameter`.

message: string

A human-readable explanation of the Live error.

type: string

The category of error, such as `invalid_request_error` for an invalid Live client command.

client\_event\_id: optional string

The event\_id of the client command that caused the error, when supplied.

param: optional string

The parameter that caused the error, when applicable, such as `session.voice`.

ErrorEvent object { error, event\_id, type, client\_event\_id }

Reports an error in the Live session, such as an invalid client command. Use error.client\_event\_id, when present, to identify the command that caused the error.

error: [Error](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20error%20%3E%20(schema)) { code, message, type, 2 more }

Details of the Live error and the client command that caused it, when known.

event\_id: string

The unique ID of the Live server event.

type: "error"

The event type, always `error`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

ForkSessionConfig object { audio, client, delegation, store }

Overrides for a stored session after connecting to the fork WebSocket. An empty object inherits the stored configuration; do not supply a new model. audio.format applies only to the new WebSocket connection. client overrides are only supported for WebRTC forks.

audio: optional object { format }

Audio format for a WebSocket fork. WebRTC forks negotiate their audio format and must omit this field.

format: optional [AudioFormat](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20audio_format%20%3E%20(schema))

Audio encoding and sample rate for audio sent and received over a Live WebSocket connection. WebRTC and SIP negotiate their media format separately.

client: optional [ClientConfig](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20client_config%20%3E%20(schema)) { data\_channel }

Frontend data-channel permissions for a WebRTC fork. Omitted permissions inherit the stored values. Not supported for WebSocket forks.

delegation: optional object { type, responses }

Overrides for the stored session’s Responses backend. Only supported when the stored session already uses Responses delegation; the delegation type cannot change.

type: "responses"

The delegation owner. Always `responses` for tasks handled by the Responses API.

responses: optional [ResponsesDelegationUpdateConfig](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20responses_delegation_update_config%20%3E%20(schema)) { instructions, max\_output\_tokens, model, 6 more }

Responses backend settings to update. Omitted settings keep their existing values.

store: optional boolean

Whether to store the forked session. Omission inherits the stored session’s setting.

ForkSessionStartEvent object { session, type, event\_id }

Start a Live session after connecting to a stored session’s fork WebSocket. Send an empty `session` object to use the stored configuration.

session: [ForkSessionConfig](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20fork_session_config%20%3E%20(schema)) { audio, client, delegation, store }

Overrides for a stored session after connecting to the fork WebSocket. An empty object inherits the stored configuration; do not supply a new model. audio.format applies only to the new WebSocket connection. client overrides are only supported for WebRTC forks.

type: "session.start"

The Live client event type. Always `session.start`.

event\_id: optional string or null

Optional client identifier for correlating this command with a server event’s client\_event\_id or error.client\_event\_id.

maxLength512

FunctionTool object { name, type, description, 2 more }

A function tool available to the Responses backend when the Live model delegates a task.

The name the delegated Responses model uses when calling this function.

type: "function"

The tool type. Always `function`.

description: optional string or null

What the function does and when the delegated Responses model should call it.

parameters: optional map[unknown] or null

A JSON Schema object describing the arguments accepted by the function.

strict: optional boolean or null

Whether the delegated Responses model must follow the function’s parameter schema exactly.

InfoEvent object { code, event\_id, message, 2 more }

An informational notice about the Live session, such as the event permissions applied to a frontend data channel.

code: string

A machine-readable code for the notice, such as `data_channel_permissions`.

event\_id: string

The unique ID of the Live server event.

message: string

A human-readable explanation of the Live session notice.

type: "info"

The event type, always `info`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

InitialItem = object { content, role, id, 2 more }  or object { content, role, id, 2 more }  or object { content, role, id, 2 more }

A developer, user, or assistant message supplied as text history before the Live session starts.

Developer object { content, role, id, 2 more }

A developer message included in the initial text history of a Live session.

content: array of object { text, type }

The message content. Supply exactly one text part for the initial Live conversation history.

text: string

The message text to include in the Live session’s initial conversation history.

type: optional "input\_text"

The text content type. Always `input_text`.

role: "developer"

The author of this history message. Always `developer`.

id: optional string or null

An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

status: optional "incomplete" or "completed" or null

The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

"incomplete"

"completed"

type: optional "message"

The history item type. Always `message`.

User object { content, role, id, 2 more }

A user message included in the initial text history of a Live session.

content: array of object { text, type }

The message content. Supply exactly one text part for the initial Live conversation history.

text: string

The message text to include in the Live session’s initial conversation history.

type: optional "input\_text"

The text content type. Always `input_text`.

role: "user"

The author of this history message. Always `user`.

id: optional string or null

An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

status: optional "incomplete" or "completed" or null

The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

"incomplete"

"completed"

type: optional "message"

The history item type. Always `message`.

Assistant object { content, role, id, 2 more }

An assistant message included in the initial text history of a Live session.

content: array of object { text, type }  or object { text, type }

The message content. Supply exactly one text part for the initial Live conversation history.

Text object { text, type }

Assistant text supplied as conversation history when starting a Live session.

text: string

The message text to include in the Live session’s initial conversation history.

type: optional "text"

The text content type. Always `text`.

OutputText object { text, type }

Assistant output text supplied as conversation history when starting a Live session.

text: string

The message text to include in the Live session’s initial conversation history.

type: "output\_text"

The text content type. Always `output_text`.

role: "assistant"

The author of this history message. Always `assistant`.

id: optional string or null

An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

status: optional "incomplete" or "completed" or null

The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

"incomplete"

"completed"

type: optional "message"

The history item type. Always `message`.

InputAudioAppendEvent object { audio, type, event\_id }

Send audio to a Live session over its primary WebSocket. WebRTC and SIP sessions send audio over their media transport.

audio: string

Base64-encoded raw audio in the startup-selected format, without a WAV or other container header. Primary WebSocket only; media transports use their audio track. Audio appends have no acknowledgment. Reflected sideband server events reuse this event type and audio key, with no timestamps or event\_id; their audio is always mono PCM16LE at 24 kHz.

minLength1

type: "session.input\_audio.append"

The Live client event type. Always `session.input_audio.append`.

event\_id: optional string or null

Optional client identifier for correlating this command with a server event’s client\_event\_id or error.client\_event\_id.

maxLength512

InputAudioMuteEvent object { type, event\_id }

Mute audio input to the Live model without closing the session. The server acknowledges with `session.input_audio.muted`.

type: "session.input\_audio.mute"

The Live client event type. Always `session.input_audio.mute`.

event\_id: optional string or null

Optional client identifier for correlating this command with a server event’s client\_event\_id or error.client\_event\_id.

maxLength512

InputAudioMutedEvent object { event\_id, type, client\_event\_id }

Returned when a session.input\_audio.mute command is accepted. Input audio is no longer sent to the model; sideband audio reflection continues.

event\_id: string

The unique ID of the Live server event.

type: "session.input\_audio.muted"

The event type, always `session.input_audio.muted`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

InputAudioUnmuteEvent object { type, event\_id }

Resume audio input to a Live model after muting it. The server acknowledges with `session.input_audio.unmuted`.

type: "session.input\_audio.unmute"

The Live client event type. Always `session.input_audio.unmute`.

event\_id: optional string or null

Optional client identifier for correlating this command with a server event’s client\_event\_id or error.client\_event\_id.

maxLength512

InputAudioUnmutedEvent object { event\_id, type, client\_event\_id }

Returned when a session.input\_audio.unmute command is accepted. Input audio is sent to the model again.

event\_id: string

The unique ID of the Live server event.

type: "session.input\_audio.unmuted"

The event type, always `session.input_audio.unmuted`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

InputTranscriptDeltaEvent object { delta, end\_ms, event\_id, 3 more }

A transcript fragment for user input audio in the Live session. Accumulate fragments in delivery order; these events do not define complete turns or include a transcript-done event.

delta: string

The transcript text fragment for the audio in this time range. Append fragments in delivery order to build the transcript.

end\_ms: number

The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start\_ms.

event\_id: string

The unique ID of the Live server event.

start\_ms: number

The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

type: "session.input\_transcript.delta"

The event type, always `session.input_transcript.delta`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

InstructionsAppendEvent object { content, delegation\_id, type, event\_id }

Append instructions to the Live conversation while it is running, optionally associating them with an existing client delegation.

content: string

Instruction text to append, limited to 500 tokens. This is a plain string, not an array of content parts.

delegation\_id: string or null

Required, nullable. Set null for general session context, or use the ID from session.delegation.created for an existing client delegation. Non-null IDs are not accepted with Responses delegation.

minLength1

type: "session.instructions.append"

The Live client event type. Always `session.instructions.append`.

event\_id: optional string or null

Optional client identifier for correlating this command with a server event’s client\_event\_id or error.client\_event\_id.

maxLength512

InstructionsAppendedEvent object { end\_ms, event\_id, start\_ms, 2 more }

Returned when a session.instructions.append command is accepted into the Live session timeline. Acknowledges the appended instructions without guaranteeing that the model has acted on them.

end\_ms: number

The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start\_ms.

event\_id: string

The unique ID of the Live server event.

start\_ms: number

The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

type: "session.instructions.appended"

The event type, always `session.instructions.appended`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

LiveCreateResponse object { session, transport }

The created Live session identifier and WebRTC answer. Apply transport.sdp as the peer’s remote answer and wait for session.started on the data channel before sending commands.

session: object { id }

The newly created Live session. Use its ID for session controls and sideband connections.

Opaque session identifier. Preserve the returned value unchanged, including its prefix.

transport: object { sdp, type }

WebRTC transport with the SDP answer.

sdp: string

Session Description Protocol message for the WebRTC connection.

minLength1

type: "webrtc"

The transport used for the Live session. Always `webrtc`.

MediaSessionConfig object { model, audio, client, 4 more }

Startup configuration for a Live media session. Follow the [Live prompting guide](https://developers.openai.com/api/docs/guides/live-prompting) when writing frontend instructions and the backend prompt under delegation.responses.instructions.

model: string or "gpt-live-1"

The Live model. Required in the session configuration for every transport; do not pass it as a URL query parameter.

string

"gpt-live-1"

The Live model. Required in the session configuration for every transport; do not pass it as a URL query parameter.

audio: optional object { output }

Startup audio configuration. WebRTC and SIP negotiate their audio format on the media transport.

output: optional object { voice }

Settings for speech generated by the Live model. Choose the voice before starting the session.

voice: optional string or "alloy" or "ash" or "ballad" or 19 more or [CustomVoice](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20custom_voice%20%3E%20(schema)) { id }

The voice used for Live speech, as a built-in voice name or a custom voice object containing its ID. Defaults to `marin` and cannot change after startup.

string

"alloy" or "ash" or "ballad" or 19 more

The voice used for Live speech, as a built-in voice name or a custom voice object containing its ID. Defaults to `marin` and cannot change after startup.

"alloy"

"ash"

"ballad"

"beacon"

"bossa"

"cedar"

"cinder"

"coral"

"delta"

"echo"

"gleam"

"marin"

"meridian"

"quartz"

"ripple"

"sage"

"shimmer"

"stone"

"tempo"

"verse"

"vesper"

"willow"

CustomVoice object { id }

minLength1

maxLength128

client: optional [ClientConfig](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20client_config%20%3E%20(schema)) { data\_channel }

Startup-only capabilities for an untrusted frontend attached to a unified WebRTC session. Trusted sideband connections are unaffected.

delegation: optional [ClientDelegation](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20client_delegation%20%3E%20(schema)) { type }  or object { responses, type }  or null

Who handles tasks delegated by the Live model. Omitted or null selects your application; use `responses` to let the API manage a Responses backend.

ClientDelegation object { type }

Delegate tasks to your application. The Live session emits delegation events that your backend handles.

type: "client"

The delegation owner. Always `client` for tasks handled by your application.

Responses object { responses, type }

Delegate tasks to a Responses model managed by the Live session.

responses: [ResponsesDelegationConfig](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20responses_delegation_config%20%3E%20(schema)) { model, instructions, max\_output\_tokens, 6 more }

Backend model, prompt, and tools used when the Live session delegates a task to Responses.

type: "responses"

The delegation owner. Always `responses` for tasks handled by the Responses API.

input: optional array of [InitialItem](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20initial_item%20%3E%20(schema))

Ordered text-only history supplied before startup. Supports developer, user, and assistant messages with one text part each; at most 128 messages and 8,192 rendered tokens in total.

Developer object { content, role, id, 2 more }

A developer message included in the initial text history of a Live session.

content: array of object { text, type }

The message content. Supply exactly one text part for the initial Live conversation history.

text: string

The message text to include in the Live session’s initial conversation history.

type: optional "input\_text"

The text content type. Always `input_text`.

role: "developer"

The author of this history message. Always `developer`.

id: optional string or null

An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

status: optional "incomplete" or "completed" or null

The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

"incomplete"

"completed"

type: optional "message"

The history item type. Always `message`.

User object { content, role, id, 2 more }

A user message included in the initial text history of a Live session.

content: array of object { text, type }

The message content. Supply exactly one text part for the initial Live conversation history.

text: string

The message text to include in the Live session’s initial conversation history.

type: optional "input\_text"

The text content type. Always `input_text`.

role: "user"

The author of this history message. Always `user`.

id: optional string or null

An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

status: optional "incomplete" or "completed" or null

The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

"incomplete"

"completed"

type: optional "message"

The history item type. Always `message`.

Assistant object { content, role, id, 2 more }

An assistant message included in the initial text history of a Live session.

content: array of object { text, type }  or object { text, type }

The message content. Supply exactly one text part for the initial Live conversation history.

Text object { text, type }

Assistant text supplied as conversation history when starting a Live session.

text: string

The message text to include in the Live session’s initial conversation history.

type: optional "text"

The text content type. Always `text`.

OutputText object { text, type }

Assistant output text supplied as conversation history when starting a Live session.

text: string

The message text to include in the Live session’s initial conversation history.

type: "output\_text"

The text content type. Always `output_text`.

role: "assistant"

The author of this history message. Always `assistant`.

id: optional string or null

An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

status: optional "incomplete" or "completed" or null

The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

"incomplete"

"completed"

type: optional "message"

The history item type. Always `message`.

instructions: optional string or null

Frontend instructions for voice, conversation, interruptions, and when to delegate. Start with the [Live prompting guide](/api/docs/guides/live-prompting); put business rules and tool workflows in a separate [backend prompt](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt). Limited to 16,384 client-supplied tokens. Omitted or blank instructions use server defaults. Immutable after startup.

store: optional boolean

Whether to store the session for later forking and recording download. Defaults to false for new sessions.

MediaSessionForkConfig object { client, delegation, store }

Optional overrides for a stored Live session. Omitted settings are inherited. The model, voice, frontend instructions, and prior conversation come from the stored session. WebRTC negotiates its audio format; audio.format is only supported on WebSocket forks.

client: optional [ClientConfig](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20client_config%20%3E%20(schema)) { data\_channel }

Startup-only capabilities for an untrusted frontend attached to a unified WebRTC session. Trusted sideband connections are unaffected.

delegation: optional object { type, responses }

Update the Responses backend for an existing Live session without changing delegation ownership.

type: "responses"

The delegation owner. Always `responses` for tasks handled by the Responses API.

responses: optional [ResponsesDelegationUpdateConfig](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20responses_delegation_update_config%20%3E%20(schema)) { instructions, max\_output\_tokens, model, 6 more }

Responses backend settings to update. Omitted settings keep their existing values.

store: optional boolean

Whether to store the forked session. Omission inherits the stored session’s setting.

OutputAudioDeltaEvent object { delta, type, end\_ms, start\_ms }

An audio chunk generated by the Live model. Decode and play primary WebSocket chunks in delivery order using the configured session audio format. Sideband connections receive reflected output audio with timestamps.

delta: string

Base64-encoded raw audio. Primary WebSocket events use the session’s configured format; reflected sideband events use mono PCM16LE at 24 kHz.

type: "session.output\_audio.delta"

The event type, always `session.output_audio.delta`.

end\_ms: optional number

Exclusive session-relative end in milliseconds. Required on reflected sideband events; omitted on the primary WebSocket. Dropped output frames leave gaps between reflected ranges.

start\_ms: optional number

Inclusive session-relative start in milliseconds. Required on reflected sideband events; omitted on the primary WebSocket.

OutputTranscriptDeltaEvent object { delta, end\_ms, event\_id, 3 more }

A transcript fragment for assistant output audio in the Live session. Accumulate fragments in delivery order; these events do not define complete turns or include a transcript-done event.

delta: string

The transcript text fragment for the audio in this time range. Append fragments in delivery order to build the transcript.

end\_ms: number

The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start\_ms.

event\_id: string

The unique ID of the Live server event.

start\_ms: number

The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

type: "session.output\_transcript.delta"

The event type, always `session.output_transcript.delta`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

ResponseCreateEvent object { type, event\_id }

Request a response from the Live session’s Responses backend, or continue a delegated response waiting for tool results. Requires Responses delegation.

type: "response.create"

The Live client event type. Always `response.create`.

event\_id: optional string or null

Optional client identifier for correlating this command with a server event’s client\_event\_id or error.client\_event\_id.

maxLength512

ResponseEvent object { event, event\_id, type, 2 more }

A streaming Responses API event from a backend delegated to by the Live session. Use the outer delegation\_id to associate the nested stream with its Live delegation.

event: map[unknown]

The nested Responses streaming event. Dispatch on its type field. Response lifecycle snapshots omit input and clear instructions, tools, and output to keep messages small; consume granular output events for the generated content.

event\_id: string

The unique ID of the Live server event.

type: "response.event"

The event type, always `response.event`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

delegation\_id: optional string or null

The Live delegation associated with the nested Responses event. May be null or omitted when the event cannot be correlated with a delegation.

ResponseItemCreateEvent object { item, type, event\_id }

Add an input item to the Live session’s Responses backend. Requires Responses delegation; use `response.create` to request a response.

item: [EasyInputMessage](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)) { content, role, phase, type }  or object { content, role, status, type }  or [ResponseOutputMessage](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_output_message%20%3E%20(schema)) { id, content, role, 3 more }  or 30 more

An input item to append to the Responses backend conversation, such as a user message or a function tool result.

EasyInputMessage object { content, role, phase, type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: string or [ResponseInputMessageContentList](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_message_content_list%20%3E%20(schema)) { , ,  }

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

TextInput = string

A text input to the model.

ResponseInputMessageContentList = array of [ResponseInputContent](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_content%20%3E%20(schema))

A list of one or many input items to the model, containing different content
types.

ResponseInputText object { text, type, prompt\_cache\_breakpoint }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

ResponseInputImage object { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](/api/docs/guides/images-vision).

detail: [ImageDetail](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20image_detail%20%3E%20(schema))

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

type: "input\_image"

The type of the input item. Always `input_image`.

file\_id: optional string or null

The ID of the file to be sent to the model.

image\_url: optional string or null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

prompt\_cache\_breakpoint: optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

ResponseInputFile object { type, detail, file\_data, 4 more }

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

file\_id: optional string or null

The ID of the file to be sent to the model.

file\_url: optional string

The URL of the file to be sent to the model.

formaturi

filename: optional string

The name of the file to be sent to the model.

prompt\_cache\_breakpoint: optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

role: "user" or "assistant" or "system" or "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

"user"

"assistant"

"system"

"developer"

phase: optional "commentary" or "final\_answer" or null

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

"commentary"

"final\_answer"

type: optional "message"

The type of the message input. Always `message`.

Message object { content, role, status, type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role.

content: [ResponseInputMessageContentList](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_message_content_list%20%3E%20(schema)) { , ,  }

A list of one or many input items to the model, containing different content
types.

role: "user" or "system" or "developer"

The role of the message input. One of `user`, `system`, or `developer`.

"user"

"system"

"developer"

status: optional "in\_progress" or "completed" or "incomplete"

The status of item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: optional "message"

The type of the message input. Always set to `message`.

ResponseOutputMessage object { id, content, role, 3 more }

An output message from the model.

The unique ID of the output message.

content: array of [ResponseOutputText](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_output_text%20%3E%20(schema)) { annotations, logprobs, text, type }  or [ResponseOutputRefusal](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_output_refusal%20%3E%20(schema)) { refusal, type }

The content of the output message.

ResponseOutputText object { annotations, logprobs, text, type }

A text output from the model.

annotations: array of object { file\_id, filename, index, type }  or object { end\_index, start\_index, title, 2 more }  or object { container\_id, end\_index, file\_id, 3 more }  or object { file\_id, index, type }

The annotations of the text output.

FileCitation object { file\_id, filename, index, type }

A citation to a file.

file\_id: string

The ID of the file.

filename: string

The filename of the file cited.

index: number

The index of the file in the list of files.

type: "file\_citation"

The type of the file citation. Always `file_citation`.

URLCitation object { end\_index, start\_index, title, 2 more }

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

formaturi

ContainerFileCitation object { container\_id, end\_index, file\_id, 3 more }

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

FilePath object { file\_id, index, type }

A path to a file.

file\_id: string

The ID of the file.

index: number

The index of the file in the list of files.

type: "file\_path"

The type of the file path. Always `file_path`.

logprobs: array of object { token, bytes, logprob, top\_logprobs }

token: string

bytes: array of number

logprob: number

top\_logprobs: array of object { token, bytes, logprob }

token: string

bytes: array of number

logprob: number

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

ResponseOutputRefusal object { refusal, type }

A refusal from the model.

refusal: string

The refusal explanation from the model.

type: "refusal"

The type of the refusal. Always `refusal`.

role: "assistant"

The role of the output message. Always `assistant`.

status: "in\_progress" or "completed" or "incomplete"

The status of the message input. One of `in_progress`, `completed`, or
`incomplete`. Populated when input items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: "message"

The type of the output message. Always `message`.

phase: optional "commentary" or "final\_answer" or null

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

"commentary"

"final\_answer"

FileSearchCall object { id, queries, status, 2 more }

The results of a file search tool call. See the
[file search guide](/api/docs/guides/tools-file-search) for more information.

The unique ID of the file search tool call.

queries: array of string

The queries used to search for files.

status: "in\_progress" or "searching" or "completed" or 2 more

The status of the file search tool call. One of `in_progress`,
`searching`, `incomplete` or `failed`,

"in\_progress"

"searching"

"completed"

"incomplete"

"failed"

type: "file\_search\_call"

The type of the file search tool call. Always `file_search_call`.

results: optional array of object { attributes, file\_id, filename, 2 more }  or null

The results of the file search tool call.

attributes: optional map[string or number or boolean] or null

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

string

number

boolean

file\_id: optional string

The unique ID of the file.

filename: optional string

The name of the file.

score: optional number

The relevance score of the file - a value between 0 and 1.

formatfloat

text: optional string

The text that was retrieved from the file.

ComputerCall object { id, call\_id, pending\_safety\_checks, 4 more }

A tool call to a computer use tool. See the
[computer use guide](/api/docs/guides/tools-computer-use) for more information.

The unique ID of the computer call.

call\_id: string

An identifier used when responding to the tool call with output.

pending\_safety\_checks: array of object { id, code, message }

The pending safety checks for the computer call.

The ID of the pending safety check.

code: optional string or null

The type of the pending safety check.

message: optional string or null

Details about the pending safety check.

status: "in\_progress" or "completed" or "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: "computer\_call"

The type of the computer call. Always `computer_call`.

action: optional [ComputerAction](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20computer_action%20%3E%20(schema))

A click action.

actions: optional [ComputerActionList](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20computer_action_list%20%3E%20(schema)) { Click, DoubleClick, Drag, 6 more }

Flattened batched actions for `computer_use`. Each action includes an
`type` discriminator and action-specific fields.

ComputerCallOutput object { call\_id, output, type, 3 more }

The output of a computer tool call.

call\_id: string

The ID of the computer tool call that produced the output.

minLength1

maxLength64

output: [ResponseComputerToolCallOutputScreenshot](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_computer_tool_call_output_screenshot%20%3E%20(schema)) { type, file\_id, image\_url }

A computer screenshot image used with the computer use tool.

type: "computer\_call\_output"

The type of the computer tool call output. Always `computer_call_output`.

id: optional string or null

The ID of the computer tool call output.

acknowledged\_safety\_checks: optional array of object { id, code, message }  or null

The safety checks reported by the API that have been acknowledged by the developer.

The ID of the pending safety check.

code: optional string or null

The type of the pending safety check.

message: optional string or null

Details about the pending safety check.

status: optional "in\_progress" or "completed" or "incomplete" or null

The status of the message input. One of `in_progress`, `completed`, or `incomplete`. Populated when input items are returned via API.

"in\_progress"

"completed"

"incomplete"

WebSearchCall object { id, action, status, type }

The results of a web search tool call. See the
[web search guide](/api/docs/guides/tools-web-search) for more information.

The unique ID of the web search tool call.

action: object { type, queries, query, sources }  or object { type, url }  or object { pattern, type, url }

An object describing the specific action taken in this web search call.
Includes details on how the model used the web (search, open\_page, find\_in\_page).

Search object { type, queries, query, sources }

Action type “search” - Performs a web search query.

type: "search"

The action type.

queries: optional array of string

The search queries.

Deprecatedquery: optional string

The search query.

sources: optional array of object { type, url }

The sources used in the search.

type: "url"

The type of source. Always `url`.

url: string

The URL of the source.

formaturi

OpenPage object { type, url }

Action type “open\_page” - Opens a specific URL from search results.

type: "open\_page"

The action type.

url: optional string or null

The URL opened by the model.

formaturi

FindInPage object { pattern, type, url }

Action type “find\_in\_page”: Searches for a pattern within a loaded page.

pattern: string

The pattern or text to search for within the page.

type: "find\_in\_page"

The action type.

url: string

The URL of the page searched for the pattern.

formaturi

status: "in\_progress" or "searching" or "completed" or 2 more

The status of the web search tool call.

"in\_progress"

"searching"

"completed"

"failed"

"incomplete"

type: "web\_search\_call"

The type of the web search tool call. Always `web_search_call`.

FunctionCall object { arguments, call\_id, name, 6 more }

A tool call to run a function. See the
[function calling guide](/api/docs/guides/function-calling) for more information.

arguments: string

A JSON string of the arguments to pass to the function.

call\_id: string

The unique ID of the function tool call generated by the model.

The name of the function to run.

type: "function\_call"

The type of the function tool call. Always `function_call`.

id: optional string

The unique ID of the function tool call.

async: optional boolean

Whether the function tool call runs asynchronously.

caller: optional object { type }  or object { caller\_id, type }  or null

The execution context that produced this tool call.

Direct object { type }

type: "direct"

Program object { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

type: "program"

namespace: optional string

The namespace of the function to run.

status: optional "in\_progress" or "completed" or "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

FunctionCallOutput object { output, type, id, 5 more }

The output of a function tool call.

output: string or array of [ResponseInputTextContent](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text_content%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [ResponseInputImageContent](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_image_content%20%3E%20(schema)) { type, detail, file\_id, 2 more }  or [ResponseInputFileContent](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_file_content%20%3E%20(schema)) { type, detail, file\_data, 4 more }

Text, image, or file output of the function tool call.

string

A JSON string of the output of the function tool call.

array of [ResponseInputTextContent](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text_content%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [ResponseInputImageContent](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_image_content%20%3E%20(schema)) { type, detail, file\_id, 2 more }  or [ResponseInputFileContent](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_file_content%20%3E%20(schema)) { type, detail, file\_data, 4 more }

An array of content outputs (text, image, file) for the function tool call.

ResponseInputTextContent object { text, type, prompt\_cache\_breakpoint }

A text input to the model.

text: string

The text input to the model.

maxLength10485760

type: "input\_text"

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: optional object { mode }  or null

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

ResponseInputImageContent object { type, detail, file\_id, 2 more }

An image input to the model. Learn about [image inputs](/api/docs/guides/images-vision)

type: "input\_image"

The type of the input item. Always `input_image`.

detail: optional [ImageDetail](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20image_detail%20%3E%20(schema)) or null

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

file\_id: optional string or null

The ID of the file to be sent to the model.

image\_url: optional string or null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

maxLength20971520

formaturi

prompt\_cache\_breakpoint: optional object { mode }  or null

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

ResponseInputFileContent object { type, detail, file\_data, 4 more }

A file input to the model.

type: "input\_file"

The type of the input item. Always `input_file`.

detail: optional "auto" or "low" or "high"

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

"low"

"high"

file\_data: optional string or null

The base64-encoded data of the file to be sent to the model.

maxLength73400320

file\_id: optional string or null

The ID of the file to be sent to the model.

file\_url: optional string or null

The URL of the file to be sent to the model.

formaturi

filename: optional string or null

The name of the file to be sent to the model.

prompt\_cache\_breakpoint: optional object { mode }  or null

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

type: "function\_call\_output"

The type of the function tool call output. Always `function_call_output`.

id: optional string or null

The unique ID of the function tool call output. Populated when this item is returned via API.

call\_id: optional string or null

The unique ID of the function tool call generated by the model.

minLength1

maxLength64

caller: optional object { type }  or object { caller\_id, type }  or null

The execution context that produced this tool call.

Direct object { type }

type: "direct"

The caller type. Always `direct`.

Program object { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

minLength1

maxLength64

type: "program"

The caller type. Always `program`.

name: optional string or null

The name of the tool that produced the output.

minLength1

maxLength128

namespace: optional string or null

The namespace of the tool that produced the output.

minLength1

maxLength64

status: optional "in\_progress" or "completed" or "incomplete" or null

The status of the item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

ToolSearchCall object { arguments, type, id, 3 more }

arguments: unknown

The arguments supplied to the tool search call.

type: "tool\_search\_call"

The item type. Always `tool_search_call`.

id: optional string or null

The unique ID of this tool search call.

call\_id: optional string or null

The unique ID of the tool search call generated by the model.

minLength1

maxLength64

execution: optional "server" or "client"

Whether tool search was executed by the server or by the client.

"server"

"client"

status: optional "in\_progress" or "completed" or "incomplete" or null

The status of the tool search call.

"in\_progress"

"completed"

"incomplete"

ToolSearchOutput object { tools, type, id, 3 more }

tools: array of object { name, parameters, strict, 6 more }  or object { type, vector\_store\_ids, filters, 2 more }  or object { type }  or 13 more

The loaded tool definitions returned by the tool search output.

Function object { name, parameters, strict, 6 more }

Defines a function in your own code the model can choose to call. Learn more about [function calling](/api/docs/guides/function-calling).

The name of the function to call.

parameters: map[unknown] or null

A JSON schema object describing the parameters of the function.

strict: boolean or null

Whether strict parameter validation is enforced for this function tool.

type: "function"

The type of the function tool. Always `function`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

async: optional boolean

defer\_loading: optional boolean

Whether this function is deferred and loaded via tool search.

description: optional string or null

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema: optional map[unknown] or null

A JSON schema object describing the JSON value encoded in string outputs for this function.

FileSearch object { type, vector\_store\_ids, filters, 2 more }

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](/api/docs/guides/tools-file-search).

type: "file\_search"

The type of the file search tool. Always `file_search`.

vector\_store\_ids: array of string

The IDs of the vector stores to search.

filters: optional [ComparisonFilter](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key, type, value }  or [CompoundFilter](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20compound_filter%20%3E%20(schema)) { filters, type }  or null

A filter to apply.

ComparisonFilter object { key, type, value }

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

string

number

boolean

array of string or number

string

number

CompoundFilter object { filters, type }

Combine multiple filters using `and` or `or`.

filters: array of [ComparisonFilter](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key, type, value }  or unknown

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

ComparisonFilter object { key, type, value }

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

string

number

boolean

array of string or number

string

number

unknown

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

Computer object { type }

A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

type: "computer"

The type of the computer tool. Always `computer`.

ComputerUsePreview object { display\_height, display\_width, environment, type }

A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

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

WebSearch object { type, external\_web\_access, filters, 2 more }

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](/api/docs/guides/tools-web-search).

type: "web\_search" or "web\_search\_2025\_08\_26"

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

"web\_search"

"web\_search\_2025\_08\_26"

external\_web\_access: optional boolean

Allow live internet access for web search. Defaults to true when omitted. When false, the web search tool runs in offline/cache-only mode and will not fetch new external content.

filters: optional object { allowed\_domains }  or null

Filters for the search.

allowed\_domains: optional array of string or null

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size: optional "low" or "medium" or "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location: optional object { city, country, region, 2 more }  or null

The approximate location of the user.

city: optional string or null

Free text input for the city of the user, e.g. `San Francisco`.

country: optional string or null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region: optional string or null

Free text input for the region of the user, e.g. `California`.

timezone: optional string or null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type: optional "approximate"

The type of location approximation. Always `approximate`.

Mcp object { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](/api/docs/guides/tools-connectors-mcp).

server\_label: string

A label for this MCP server, used to identify it in tool calls.

type: "mcp"

The type of the MCP tool. Always `mcp`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools: optional array of string or object { read\_only, tool\_names }  or null

List of allowed tool names or a filter object.

McpAllowedTools = array of string

A string array of allowed tool names

McpToolFilter object { read\_only, tool\_names }

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
about service connectors [here](/api/docs/guides/tools-connectors-mcp#connectors).

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

headers: optional map[string] or null

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval: optional object { always, never }  or "always" or "never" or null

Specify which of the MCP server’s tools require approval.

McpToolApprovalFilter object { always, never }

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

McpToolApprovalSetting = "always" or "never"

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

formaturi

tunnel\_id: optional string

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter object { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string or object { type, file\_ids, memory\_limit, network\_policy }

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

string

The container ID.

CodeInterpreterToolAuto object { type, file\_ids, memory\_limit, network\_policy }

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: "auto"

Always `auto`.

file\_ids: optional array of string

An optional list of uploaded files to make available to your code.

memory\_limit: optional "1g" or "4g" or "16g" or "64g" or null

The memory limit for the code interpreter container.

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [ContainerNetworkPolicyDisabled](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)) { type }  or [ContainerNetworkPolicyAllowlist](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

ContainerNetworkPolicyDisabled object { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

ContainerNetworkPolicyAllowlist object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: optional array of [ContainerNetworkPolicyDomainSecret](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

minLength1

maxLength10485760

type: "code\_interpreter"

The type of the code interpreter tool. Always `code_interpreter`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

ProgrammaticToolCalling object { type }

type: "programmatic\_tool\_calling"

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration object { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

The type of the image generation tool. Always `image_generation`.

action: optional "generate" or "edit" or "auto"

Whether to generate a new image or edit an existing image. Default: `auto`.

"generate"

"edit"

"auto"

background: optional "transparent" or "opaque" or "auto"

Set the background of the generated image. One of `transparent`, `opaque`,
or `auto`. `gpt-image-2.5-sunburst` and `gpt-image-2.5-flare`, including
their `2026-09-08` snapshots, support `opaque` and `transparent`
backgrounds. Transparent backgrounds are available for supported GPT Image
models. For `gpt-image-2` and `gpt-image-2-2026-04-21`, this support is in
preview. When using `transparent`, set the output format to `png` or `webp`.
Default: `auto`.

"transparent"

"opaque"

"auto"

input\_fidelity: optional "high" or "low" or null

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

model: optional string or "gpt-image-1" or "gpt-image-1-mini" or "gpt-image-1.5" or 6 more

The image generation model to use. One of `gpt-image-1`,
`gpt-image-1-mini`, `gpt-image-1.5`, `gpt-image-2`,
`gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`,
`gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`,
`gpt-image-2.5-flare-2026-09-08`, or `chatgpt-image-latest`. Default:
`gpt-image-1`.

string

"gpt-image-1" or "gpt-image-1-mini" or "gpt-image-1.5" or 6 more

The image generation model to use. One of `gpt-image-1`,
`gpt-image-1-mini`, `gpt-image-1.5`, `gpt-image-2`,
`gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`,
`gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`,
`gpt-image-2.5-flare-2026-09-08`, or `chatgpt-image-latest`. Default:
`gpt-image-1`.

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-1.5"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-2.5-sunburst"

"gpt-image-2.5-sunburst-2026-09-08"

"gpt-image-2.5-flare"

"gpt-image-2.5-flare-2026-09-08"

moderation: optional "auto" or "low"

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression: optional number

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format: optional "png" or "webp" or "jpeg"

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

"png"

"webp"

"jpeg"

partial\_images: optional number

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

quality: optional "low" or "medium" or "high" or 3 more

The quality of the generated image. The GPT image models support `low`,
`medium`, and `high`. `gpt-image-2.5-sunburst` and `gpt-image-2.5-flare`,
including their `2026-09-08` snapshots, also support `xhigh` and `max`.
Default: `auto`.

"low"

"medium"

"high"

"xhigh"

"max"

"auto"

size: optional string or "1024x1024" or "1024x1536" or "1536x1024" or "auto"

The size of the generated images. For `gpt-image-2`, `gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`, `gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`, and `gpt-image-2.5-flare-2026-09-08`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

string

"1024x1024" or "1024x1536" or "1536x1024" or "auto"

The size of the generated images. For `gpt-image-2`, `gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`, `gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`, and `gpt-image-2.5-flare-2026-09-08`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

LocalShell object { type }

A tool that allows the model to execute shell commands in a local environment.

type: "local\_shell"

The type of the local shell tool. Always `local_shell`.

Shell object { type, allowed\_callers, environment }

A tool that allows the model to execute shell commands.

type: "shell"

The type of the shell tool. Always `shell`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

environment: optional [ContainerAuto](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  or [LocalEnvironment](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20local_environment%20%3E%20(schema)) { type, skills }  or [ContainerReference](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_reference%20%3E%20(schema)) { container\_id, type }  or null

ContainerAuto object { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

Automatically creates a container for this request

file\_ids: optional array of string

An optional list of uploaded files to make available to your code.

memory\_limit: optional "1g" or "4g" or "16g" or "64g" or null

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [ContainerNetworkPolicyDisabled](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)) { type }  or [ContainerNetworkPolicyAllowlist](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

ContainerNetworkPolicyDisabled object { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

ContainerNetworkPolicyAllowlist object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: optional array of [ContainerNetworkPolicyDomainSecret](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

minLength1

maxLength10485760

skills: optional array of [SkillReference](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20skill_reference%20%3E%20(schema)) { skill\_id, type, version }  or [InlineSkill](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill%20%3E%20(schema)) { description, name, source, type }

An optional list of skills referenced by id or inline data.

SkillReference object { skill\_id, type, version }

skill\_id: string

The ID of the referenced skill.

minLength1

maxLength64

type: "skill\_reference"

References a skill created with the /v1/skills endpoint.

version: optional string

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

InlineSkill object { description, name, source, type }

description: string

The description of the skill.

The name of the skill.

source: [InlineSkillSource](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

Inline skill payload

type: "inline"

Defines an inline skill for this request.

LocalEnvironment object { type, skills }

type: "local"

Use a local computer environment.

skills: optional array of [LocalSkill](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema)) { description, name, path }

An optional list of skills.

description: string

The description of the skill.

The name of the skill.

path: string

The path to the directory containing the skill.

ContainerReference object { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

Custom object { name, type, allowed\_callers, 4 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](/api/docs/guides/function-calling#custom-tools)

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

async: optional boolean

Whether the tool response can be returned asynchronously versus immediately returned on next response creation.

defer\_loading: optional boolean

Whether this tool should be deferred and discovered via tool search.

description: optional string

Optional description of the custom tool, used to provide more context.

format: optional [CustomToolInputFormat](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))

The input format for the custom tool. Default is unconstrained text.

Namespace object { description, name, tools, type }

Groups function/custom tools under a shared namespace.

description: string

A description of the namespace shown to the model.

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: array of object { name, type, allowed\_callers, 6 more }  or object { name, type, allowed\_callers, 4 more }

The function/custom tools available inside this namespace.

Function object { name, type, allowed\_callers, 6 more }

minLength1

maxLength128

type: "function"

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

async: optional boolean

Whether the tool response can be returned asynchronously versus immediately returned on next response creation.

defer\_loading: optional boolean

Whether this function should be deferred and discovered via tool search.

description: optional string or null

output\_schema: optional map[unknown] or null

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters: optional unknown or null

strict: optional boolean or null

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

Custom object { name, type, allowed\_callers, 4 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](/api/docs/guides/function-calling#custom-tools)

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

async: optional boolean

Whether the tool response can be returned asynchronously versus immediately returned on next response creation.

defer\_loading: optional boolean

Whether this tool should be deferred and discovered via tool search.

description: optional string

Optional description of the custom tool, used to provide more context.

format: optional [CustomToolInputFormat](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))

The input format for the custom tool. Default is unconstrained text.

type: "namespace"

The type of the tool. Always `namespace`.

ToolSearch object { type, description, execution, parameters }

Hosted or BYOT tool search configuration for deferred tools.

type: "tool\_search"

The type of the tool. Always `tool_search`.

description: optional string or null

Description shown to the model for a client-executed tool search tool.

execution: optional "server" or "client"

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters: optional unknown or null

Parameter schema for a client-executed tool search tool.

WebSearchPreview object { type, search\_content\_types, search\_context\_size, user\_location }

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](/api/docs/guides/tools-web-search).

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

user\_location: optional object { type, city, country, 2 more }  or null

The user’s location.

type: "approximate"

The type of location approximation. Always `approximate`.

city: optional string or null

Free text input for the city of the user, e.g. `San Francisco`.

country: optional string or null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region: optional string or null

Free text input for the region of the user, e.g. `California`.

timezone: optional string or null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

ApplyPatch object { type, allowed\_callers }

Allows the assistant to create, delete, or update files using unified diffs.

type: "apply\_patch"

The type of the tool. Always `apply_patch`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

type: "tool\_search\_output"

The item type. Always `tool_search_output`.

id: optional string or null

The unique ID of this tool search output.

call\_id: optional string or null

The unique ID of the tool search call generated by the model.

minLength1

maxLength64

execution: optional "server" or "client"

Whether tool search was executed by the server or by the client.

"server"

"client"

status: optional "in\_progress" or "completed" or "incomplete" or null

The status of the tool search output.

"in\_progress"

"completed"

"incomplete"

AdditionalTools object { role, tools, type, id }

role: "developer"

The role that provided the additional tools. Only `developer` is supported.

tools: array of object { name, parameters, strict, 6 more }  or object { type, vector\_store\_ids, filters, 2 more }  or object { type }  or 13 more

A list of additional tools made available at this item.

Function object { name, parameters, strict, 6 more }

Defines a function in your own code the model can choose to call. Learn more about [function calling](/api/docs/guides/function-calling).

The name of the function to call.

parameters: map[unknown] or null

A JSON schema object describing the parameters of the function.

strict: boolean or null

Whether strict parameter validation is enforced for this function tool.

type: "function"

The type of the function tool. Always `function`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

async: optional boolean

defer\_loading: optional boolean

Whether this function is deferred and loaded via tool search.

description: optional string or null

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema: optional map[unknown] or null

A JSON schema object describing the JSON value encoded in string outputs for this function.

FileSearch object { type, vector\_store\_ids, filters, 2 more }

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](/api/docs/guides/tools-file-search).

type: "file\_search"

The type of the file search tool. Always `file_search`.

vector\_store\_ids: array of string

The IDs of the vector stores to search.

filters: optional [ComparisonFilter](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key, type, value }  or [CompoundFilter](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20compound_filter%20%3E%20(schema)) { filters, type }  or null

A filter to apply.

ComparisonFilter object { key, type, value }

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

string

number

boolean

array of string or number

string

number

CompoundFilter object { filters, type }

Combine multiple filters using `and` or `or`.

filters: array of [ComparisonFilter](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key, type, value }  or unknown

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

ComparisonFilter object { key, type, value }

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

string

number

boolean

array of string or number

string

number

unknown

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

Computer object { type }

A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

type: "computer"

The type of the computer tool. Always `computer`.

ComputerUsePreview object { display\_height, display\_width, environment, type }

A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

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

WebSearch object { type, external\_web\_access, filters, 2 more }

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](/api/docs/guides/tools-web-search).

type: "web\_search" or "web\_search\_2025\_08\_26"

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

"web\_search"

"web\_search\_2025\_08\_26"

external\_web\_access: optional boolean

Allow live internet access for web search. Defaults to true when omitted. When false, the web search tool runs in offline/cache-only mode and will not fetch new external content.

filters: optional object { allowed\_domains }  or null

Filters for the search.

allowed\_domains: optional array of string or null

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size: optional "low" or "medium" or "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location: optional object { city, country, region, 2 more }  or null

The approximate location of the user.

city: optional string or null

Free text input for the city of the user, e.g. `San Francisco`.

country: optional string or null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region: optional string or null

Free text input for the region of the user, e.g. `California`.

timezone: optional string or null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type: optional "approximate"

The type of location approximation. Always `approximate`.

Mcp object { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](/api/docs/guides/tools-connectors-mcp).

server\_label: string

A label for this MCP server, used to identify it in tool calls.

type: "mcp"

The type of the MCP tool. Always `mcp`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools: optional array of string or object { read\_only, tool\_names }  or null

List of allowed tool names or a filter object.

McpAllowedTools = array of string

A string array of allowed tool names

McpToolFilter object { read\_only, tool\_names }

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
about service connectors [here](/api/docs/guides/tools-connectors-mcp#connectors).

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

headers: optional map[string] or null

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval: optional object { always, never }  or "always" or "never" or null

Specify which of the MCP server’s tools require approval.

McpToolApprovalFilter object { always, never }

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

McpToolApprovalSetting = "always" or "never"

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

formaturi

tunnel\_id: optional string

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter object { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string or object { type, file\_ids, memory\_limit, network\_policy }

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

string

The container ID.

CodeInterpreterToolAuto object { type, file\_ids, memory\_limit, network\_policy }

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: "auto"

Always `auto`.

file\_ids: optional array of string

An optional list of uploaded files to make available to your code.

memory\_limit: optional "1g" or "4g" or "16g" or "64g" or null

The memory limit for the code interpreter container.

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [ContainerNetworkPolicyDisabled](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)) { type }  or [ContainerNetworkPolicyAllowlist](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

ContainerNetworkPolicyDisabled object { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

ContainerNetworkPolicyAllowlist object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: optional array of [ContainerNetworkPolicyDomainSecret](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

minLength1

maxLength10485760

type: "code\_interpreter"

The type of the code interpreter tool. Always `code_interpreter`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

ProgrammaticToolCalling object { type }

type: "programmatic\_tool\_calling"

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration object { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

The type of the image generation tool. Always `image_generation`.

action: optional "generate" or "edit" or "auto"

Whether to generate a new image or edit an existing image. Default: `auto`.

"generate"

"edit"

"auto"

background: optional "transparent" or "opaque" or "auto"

Set the background of the generated image. One of `transparent`, `opaque`,
or `auto`. `gpt-image-2.5-sunburst` and `gpt-image-2.5-flare`, including
their `2026-09-08` snapshots, support `opaque` and `transparent`
backgrounds. Transparent backgrounds are available for supported GPT Image
models. For `gpt-image-2` and `gpt-image-2-2026-04-21`, this support is in
preview. When using `transparent`, set the output format to `png` or `webp`.
Default: `auto`.

"transparent"

"opaque"

"auto"

input\_fidelity: optional "high" or "low" or null

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

model: optional string or "gpt-image-1" or "gpt-image-1-mini" or "gpt-image-1.5" or 6 more

The image generation model to use. One of `gpt-image-1`,
`gpt-image-1-mini`, `gpt-image-1.5`, `gpt-image-2`,
`gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`,
`gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`,
`gpt-image-2.5-flare-2026-09-08`, or `chatgpt-image-latest`. Default:
`gpt-image-1`.

string

"gpt-image-1" or "gpt-image-1-mini" or "gpt-image-1.5" or 6 more

The image generation model to use. One of `gpt-image-1`,
`gpt-image-1-mini`, `gpt-image-1.5`, `gpt-image-2`,
`gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`,
`gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`,
`gpt-image-2.5-flare-2026-09-08`, or `chatgpt-image-latest`. Default:
`gpt-image-1`.

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-1.5"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-2.5-sunburst"

"gpt-image-2.5-sunburst-2026-09-08"

"gpt-image-2.5-flare"

"gpt-image-2.5-flare-2026-09-08"

moderation: optional "auto" or "low"

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression: optional number

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format: optional "png" or "webp" or "jpeg"

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

"png"

"webp"

"jpeg"

partial\_images: optional number

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

quality: optional "low" or "medium" or "high" or 3 more

The quality of the generated image. The GPT image models support `low`,
`medium`, and `high`. `gpt-image-2.5-sunburst` and `gpt-image-2.5-flare`,
including their `2026-09-08` snapshots, also support `xhigh` and `max`.
Default: `auto`.

"low"

"medium"

"high"

"xhigh"

"max"

"auto"

size: optional string or "1024x1024" or "1024x1536" or "1536x1024" or "auto"

The size of the generated images. For `gpt-image-2`, `gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`, `gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`, and `gpt-image-2.5-flare-2026-09-08`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

string

"1024x1024" or "1024x1536" or "1536x1024" or "auto"

The size of the generated images. For `gpt-image-2`, `gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`, `gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`, and `gpt-image-2.5-flare-2026-09-08`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

LocalShell object { type }

A tool that allows the model to execute shell commands in a local environment.

type: "local\_shell"

The type of the local shell tool. Always `local_shell`.

Shell object { type, allowed\_callers, environment }

A tool that allows the model to execute shell commands.

type: "shell"

The type of the shell tool. Always `shell`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

environment: optional [ContainerAuto](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  or [LocalEnvironment](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20local_environment%20%3E%20(schema)) { type, skills }  or [ContainerReference](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_reference%20%3E%20(schema)) { container\_id, type }  or null

ContainerAuto object { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

Automatically creates a container for this request

file\_ids: optional array of string

An optional list of uploaded files to make available to your code.

memory\_limit: optional "1g" or "4g" or "16g" or "64g" or null

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [ContainerNetworkPolicyDisabled](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)) { type }  or [ContainerNetworkPolicyAllowlist](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

ContainerNetworkPolicyDisabled object { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

ContainerNetworkPolicyAllowlist object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: optional array of [ContainerNetworkPolicyDomainSecret](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

minLength1

maxLength10485760

skills: optional array of [SkillReference](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20skill_reference%20%3E%20(schema)) { skill\_id, type, version }  or [InlineSkill](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill%20%3E%20(schema)) { description, name, source, type }

An optional list of skills referenced by id or inline data.

SkillReference object { skill\_id, type, version }

skill\_id: string

The ID of the referenced skill.

minLength1

maxLength64

type: "skill\_reference"

References a skill created with the /v1/skills endpoint.

version: optional string

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

InlineSkill object { description, name, source, type }

description: string

The description of the skill.

The name of the skill.

source: [InlineSkillSource](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

Inline skill payload

type: "inline"

Defines an inline skill for this request.

LocalEnvironment object { type, skills }

type: "local"

Use a local computer environment.

skills: optional array of [LocalSkill](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema)) { description, name, path }

An optional list of skills.

description: string

The description of the skill.

The name of the skill.

path: string

The path to the directory containing the skill.

ContainerReference object { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

Custom object { name, type, allowed\_callers, 4 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](/api/docs/guides/function-calling#custom-tools)

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

async: optional boolean

Whether the tool response can be returned asynchronously versus immediately returned on next response creation.

defer\_loading: optional boolean

Whether this tool should be deferred and discovered via tool search.

description: optional string

Optional description of the custom tool, used to provide more context.

format: optional [CustomToolInputFormat](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))

The input format for the custom tool. Default is unconstrained text.

Namespace object { description, name, tools, type }

Groups function/custom tools under a shared namespace.

description: string

A description of the namespace shown to the model.

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: array of object { name, type, allowed\_callers, 6 more }  or object { name, type, allowed\_callers, 4 more }

The function/custom tools available inside this namespace.

Function object { name, type, allowed\_callers, 6 more }

minLength1

maxLength128

type: "function"

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

async: optional boolean

Whether the tool response can be returned asynchronously versus immediately returned on next response creation.

defer\_loading: optional boolean

Whether this function should be deferred and discovered via tool search.

description: optional string or null

output\_schema: optional map[unknown] or null

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters: optional unknown or null

strict: optional boolean or null

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

Custom object { name, type, allowed\_callers, 4 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](/api/docs/guides/function-calling#custom-tools)

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

async: optional boolean

Whether the tool response can be returned asynchronously versus immediately returned on next response creation.

defer\_loading: optional boolean

Whether this tool should be deferred and discovered via tool search.

description: optional string

Optional description of the custom tool, used to provide more context.

format: optional [CustomToolInputFormat](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))

The input format for the custom tool. Default is unconstrained text.

type: "namespace"

The type of the tool. Always `namespace`.

ToolSearch object { type, description, execution, parameters }

Hosted or BYOT tool search configuration for deferred tools.

type: "tool\_search"

The type of the tool. Always `tool_search`.

description: optional string or null

Description shown to the model for a client-executed tool search tool.

execution: optional "server" or "client"

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters: optional unknown or null

Parameter schema for a client-executed tool search tool.

WebSearchPreview object { type, search\_content\_types, search\_context\_size, user\_location }

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](/api/docs/guides/tools-web-search).

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

user\_location: optional object { type, city, country, 2 more }  or null

The user’s location.

type: "approximate"

The type of location approximation. Always `approximate`.

city: optional string or null

Free text input for the city of the user, e.g. `San Francisco`.

country: optional string or null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region: optional string or null

Free text input for the region of the user, e.g. `California`.

timezone: optional string or null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

ApplyPatch object { type, allowed\_callers }

Allows the assistant to create, delete, or update files using unified diffs.

type: "apply\_patch"

The type of the tool. Always `apply_patch`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

type: "additional\_tools"

The item type. Always `additional_tools`.

id: optional string or null

The unique ID of this additional tools item.

ConfigurationUpdate object { type, id, reasoning }

An update to the conversation’s response configuration. The configuration
remains in effect for subsequent responses until it is replaced by another
configuration update.

type: "configuration\_update"

The item type. Always `configuration_update`.

id: optional string or null

The unique ID of the configuration update item.

reasoning: optional object { effort }

Updates to reasoning configuration. Only effort is supported.

effort: optional [ReasoningEffort](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)) or null

The reasoning effort to use for subsequent responses until another
configuration update replaces it.

Reasoning object { id, summary, type, 3 more }

A description of the chain of thought used by a reasoning model while generating
a response. Be sure to include these items in your `input` to the Responses API
for subsequent turns of a conversation if you are manually
[managing context](/api/docs/guides/conversation-state).

The unique identifier of the reasoning content.

summary: array of [SummaryTextContent](/api/reference/resources/conversations#(resource)%20conversations%20%3E%20(model)%20summary_text_content%20%3E%20(schema)) { text, type }

Reasoning summary content.

text: string

A summary of the reasoning output from the model so far.

type: "summary\_text"

The type of the object. Always `summary_text`.

type: "reasoning"

The type of the object. Always `reasoning`.

content: optional array of object { text, type }

Reasoning text content.

text: string

The reasoning text from the model.

type: "reasoning\_text"

The type of the reasoning text. Always `reasoning_text`.

encrypted\_content: optional string or null

The encrypted content of the reasoning item. This is populated by default
for reasoning items returned by `POST /v1/responses` and WebSocket
`response.create` requests.

When streaming, use the completed reasoning item and its
`encrypted_content` from the `response.output_item.done` event in
subsequent requests. The `encrypted_content` in
`response.output_item.added` may be incomplete. This is especially
important when `store` is `false` or when using Zero Data Retention.

status: optional "in\_progress" or "completed" or "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

Compaction object { encrypted\_content, type, id }

A compaction item generated by the [`v1/responses/compact` API](/api/reference/resources/responses/methods/compact).

encrypted\_content: string

The encrypted content of the compaction summary.

maxLength20971520

type: "compaction"

The type of the item. Always `compaction`.

id: optional string or null

The ID of the compaction item.

ImageGenerationCall object { id, result, status, 7 more }

An image generation request made by the model.

The unique ID of the image generation call.

result: string or null

The generated image encoded in base64.

status: "in\_progress" or "completed" or "generating" or "failed"

The status of the image generation call.

"in\_progress"

"completed"

"generating"

"failed"

type: "image\_generation\_call"

The type of the image generation call. Always `image_generation_call`.

action: optional "generate" or "edit" or "auto" or null

The action used for image generation.

"generate"

"edit"

"auto"

background: optional "transparent" or "opaque" or "auto" or null

The background setting used for generation.

"transparent"

"opaque"

"auto"

output\_format: optional "png" or "webp" or "jpeg" or null

The output format used for generation.

"png"

"webp"

"jpeg"

quality: optional "low" or "medium" or "high" or 3 more or null

The quality of the image generated by the image generation tool call. One of `low`, `medium`, `high`, `xhigh`, `max`, or `auto`.

"low"

"medium"

"high"

"xhigh"

"max"

"auto"

revised\_prompt: optional string or null

The prompt that was used after any model prompt rewriting.

size: optional string or "1024x1024" or "1024x1536" or "1536x1024" or null

The image dimensions as a `WIDTHxHEIGHT` string, for example `1536x864`.

string

"1024x1024" or "1024x1536" or "1536x1024"

The image dimensions as a `WIDTHxHEIGHT` string, for example `1536x864`.

"1024x1024"

"1024x1536"

"1536x1024"

CodeInterpreterCall object { id, code, container\_id, 3 more }

A tool call to run code.

The unique ID of the code interpreter tool call.

code: string or null

The code to run, or null if not available.

container\_id: string

The ID of the container used to run the code.

outputs: array of object { logs, type }  or object { type, url }  or null

The outputs generated by the code interpreter, such as logs or images.
Can be null if no outputs are available.

Logs object { logs, type }

The logs output from the code interpreter.

logs: string

The logs output from the code interpreter.

type: "logs"

The type of the output. Always `logs`.

Image object { type, url }

The image output from the code interpreter.

type: "image"

The type of the output. Always `image`.

url: string

The URL of the image output from the code interpreter.

formaturi

status: "in\_progress" or "completed" or "incomplete" or 2 more

The status of the code interpreter tool call. Valid values are `in_progress`, `completed`, `incomplete`, `interpreting`, and `failed`.

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: "code\_interpreter\_call"

The type of the code interpreter tool call. Always `code_interpreter_call`.

LocalShellCall object { id, action, call\_id, 2 more }

A tool call to run a command on the local shell.

The unique ID of the local shell call.

action: object { command, env, type, 3 more }

Execute a shell command on the server.

command: array of string

The command to run.

env: map[string]

Environment variables to set for the command.

type: "exec"

The type of the local shell action. Always `exec`.

timeout\_ms: optional number or null

Optional timeout in milliseconds for the command.

user: optional string or null

Optional user to run the command as.

working\_directory: optional string or null

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

LocalShellCallOutput object { id, output, type, status }

The output of a local shell tool call.

The unique ID of the local shell tool call generated by the model.

output: string

A JSON string of the output of the local shell tool call.

type: "local\_shell\_call\_output"

The type of the local shell tool call output. Always `local_shell_call_output`.

status: optional "in\_progress" or "completed" or "incomplete" or null

The status of the item. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

ShellCall object { action, call\_id, type, 4 more }

A tool representing a request to execute one or more shell commands.

action: object { commands, max\_output\_length, timeout\_ms }

The shell commands and limits that describe how to run the tool call.

commands: array of string

Ordered shell commands for the execution environment to run.

max\_output\_length: optional number or null

Maximum number of UTF-8 characters to capture from combined stdout and stderr output.

timeout\_ms: optional number or null

Maximum wall-clock time in milliseconds to allow the shell commands to run.

call\_id: string

The unique ID of the shell tool call generated by the model.

minLength1

maxLength64

type: "shell\_call"

The type of the item. Always `shell_call`.

id: optional string or null

The unique ID of the shell tool call. Populated when this item is returned via API.

caller: optional object { type }  or object { caller\_id, type }  or null

The execution context that produced this tool call.

Direct object { type }

type: "direct"

The caller type. Always `direct`.

Program object { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

minLength1

maxLength64

type: "program"

The caller type. Always `program`.

environment: optional [LocalEnvironment](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20local_environment%20%3E%20(schema)) { type, skills }  or [ContainerReference](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_reference%20%3E%20(schema)) { container\_id, type }  or null

The environment to execute the shell commands in.

LocalEnvironment object { type, skills }

type: "local"

Use a local computer environment.

skills: optional array of [LocalSkill](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema)) { description, name, path }

An optional list of skills.

description: string

The description of the skill.

The name of the skill.

path: string

The path to the directory containing the skill.

ContainerReference object { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

status: optional "in\_progress" or "completed" or "incomplete" or null

The status of the shell call. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

ShellCallOutput object { call\_id, output, type, 4 more }

The streamed output items emitted by a shell tool call.

call\_id: string

The unique ID of the shell tool call generated by the model.

minLength1

maxLength64

output: array of [ResponseFunctionShellCallOutputContent](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_function_shell_call_output_content%20%3E%20(schema)) { outcome, stderr, stdout }

Captured chunks of stdout and stderr output, along with their associated outcomes.

outcome: object { type }  or object { exit\_code, type }

The exit or timeout outcome associated with this shell call.

Timeout object { type }

Indicates that the shell call exceeded its configured time limit.

type: "timeout"

The outcome type. Always `timeout`.

Exit object { exit\_code, type }

Indicates that the shell commands finished and returned an exit code.

exit\_code: number

The exit code returned by the shell process.

type: "exit"

The outcome type. Always `exit`.

stderr: string

Captured stderr output for the shell call.

maxLength10485760

stdout: string

Captured stdout output for the shell call.

maxLength10485760

type: "shell\_call\_output"

The type of the item. Always `shell_call_output`.

id: optional string or null

The unique ID of the shell tool call output. Populated when this item is returned via API.

caller: optional object { type }  or object { caller\_id, type }  or null

The execution context that produced this tool call.

Direct object { type }

type: "direct"

The caller type. Always `direct`.

Program object { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

minLength1

maxLength64

type: "program"

The caller type. Always `program`.

max\_output\_length: optional number or null

The maximum number of UTF-8 characters captured for this shell call’s combined output.

status: optional "in\_progress" or "completed" or "incomplete" or null

The status of the shell call output.

"in\_progress"

"completed"

"incomplete"

ApplyPatchCall object { call\_id, operation, status, 3 more }

A tool call representing a request to create, delete, or update files using diff patches.

call\_id: string

The unique ID of the apply patch tool call generated by the model.

minLength1

maxLength64

operation: object { diff, path, type }  or object { path, type }  or object { diff, path, type }

The specific create, delete, or update instruction for the apply\_patch tool call.

CreateFile object { diff, path, type }

Instruction for creating a new file via the apply\_patch tool.

diff: string

Unified diff content to apply when creating the file.

maxLength10485760

path: string

Path of the file to create relative to the workspace root.

minLength1

type: "create\_file"

The operation type. Always `create_file`.

DeleteFile object { path, type }

Instruction for deleting an existing file via the apply\_patch tool.

path: string

Path of the file to delete relative to the workspace root.

minLength1

type: "delete\_file"

The operation type. Always `delete_file`.

UpdateFile object { diff, path, type }

Instruction for updating an existing file via the apply\_patch tool.

diff: string

Unified diff content to apply to the existing file.

maxLength10485760

path: string

Path of the file to update relative to the workspace root.

minLength1

type: "update\_file"

The operation type. Always `update_file`.

status: "in\_progress" or "completed"

The status of the apply patch tool call. One of `in_progress` or `completed`.

"in\_progress"

"completed"

type: "apply\_patch\_call"

The type of the item. Always `apply_patch_call`.

id: optional string or null

The unique ID of the apply patch tool call. Populated when this item is returned via API.

caller: optional object { type }  or object { caller\_id, type }  or null

The execution context that produced this tool call.

Direct object { type }

type: "direct"

The caller type. Always `direct`.

Program object { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

minLength1

maxLength64

type: "program"

The caller type. Always `program`.

ApplyPatchCallOutput object { call\_id, status, type, 3 more }

The streamed output emitted by an apply patch tool call.

call\_id: string

The unique ID of the apply patch tool call generated by the model.

minLength1

maxLength64

status: "completed" or "failed"

The status of the apply patch tool call output. One of `completed` or `failed`.

"completed"

"failed"

type: "apply\_patch\_call\_output"

The type of the item. Always `apply_patch_call_output`.

id: optional string or null

The unique ID of the apply patch tool call output. Populated when this item is returned via API.

caller: optional object { type }  or object { caller\_id, type }  or null

The execution context that produced this tool call.

Direct object { type }

type: "direct"

The caller type. Always `direct`.

Program object { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

minLength1

maxLength64

type: "program"

The caller type. Always `program`.

output: optional string or null

Optional human-readable log text from the apply patch tool (e.g., patch results or errors).

maxLength10485760

McpListTools object { id, server\_label, tools, 2 more }

A list of tools available on an MCP server.

The unique ID of the list.

server\_label: string

The label of the MCP server.

tools: array of object { input\_schema, name, annotations, description }

The tools available on the server.

input\_schema: unknown

The JSON schema describing the tool’s input.

The name of the tool.

annotations: optional unknown or null

Additional annotations about the tool.

description: optional string or null

The description of the tool.

type: "mcp\_list\_tools"

The type of the item. Always `mcp_list_tools`.

error: optional string or null

Error message if the server could not list tools.

McpApprovalRequest object { id, arguments, name, 2 more }

A request for human approval of a tool invocation.

The unique ID of the approval request.

arguments: string

A JSON string of arguments for the tool.

The name of the tool to run.

server\_label: string

The label of the MCP server making the request.

type: "mcp\_approval\_request"

The type of the item. Always `mcp_approval_request`.

McpApprovalResponse object { approval\_request\_id, approve, type, 2 more }

A response to an MCP approval request.

approval\_request\_id: string

The ID of the approval request being answered.

approve: boolean

Whether the request was approved.

type: "mcp\_approval\_response"

The type of the item. Always `mcp_approval_response`.

id: optional string or null

The unique ID of the approval response

reason: optional string or null

Optional reason for the decision.

McpCall object { id, arguments, name, 6 more }

An invocation of a tool on an MCP server.

The unique ID of the tool call.

arguments: string

A JSON string of the arguments passed to the tool.

The name of the tool that was run.

server\_label: string

The label of the MCP server running the tool.

type: "mcp\_call"

The type of the item. Always `mcp_call`.

approval\_request\_id: optional string or null

Unique identifier for the MCP tool call approval request.
Include this value in a subsequent `mcp_approval_response` input to approve or reject the corresponding tool call.

error: optional [McpToolCallError](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20mcp_tool_call_error%20%3E%20(schema)) or null

The error from the tool call, if any.

output: optional string or null

The output from the tool call.

status: optional "in\_progress" or "completed" or "incomplete" or 2 more

The status of the tool call. One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.

"in\_progress"

"completed"

"incomplete"

"calling"

"failed"

CustomToolCallOutput object { call\_id, output, type, 2 more }

The output of a custom tool call from your code, being sent back to the model.

call\_id: string

The call ID, used to map this custom tool call output to a custom tool call.

output: string or array of [ResponseInputText](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [ResponseInputImage](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  or [ResponseInputFile](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more }

The output from the custom tool call generated by your code.
Can be a string or an list of output content.

StringOutput = string

A string of the output of the custom tool call.

OutputContentList = array of [ResponseInputText](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [ResponseInputImage](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  or [ResponseInputFile](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more }

Text, image, or file output of the custom tool call.

ResponseInputText object { text, type, prompt\_cache\_breakpoint }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

ResponseInputImage object { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](/api/docs/guides/images-vision).

detail: [ImageDetail](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20image_detail%20%3E%20(schema))

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

type: "input\_image"

The type of the input item. Always `input_image`.

file\_id: optional string or null

The ID of the file to be sent to the model.

image\_url: optional string or null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

prompt\_cache\_breakpoint: optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

ResponseInputFile object { type, detail, file\_data, 4 more }

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

file\_id: optional string or null

The ID of the file to be sent to the model.

file\_url: optional string

The URL of the file to be sent to the model.

formaturi

filename: optional string

The name of the file to be sent to the model.

prompt\_cache\_breakpoint: optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

type: "custom\_tool\_call\_output"

The type of the custom tool call output. Always `custom_tool_call_output`.

id: optional string

The unique ID of the custom tool call output in the OpenAI platform.

caller: optional object { type }  or object { caller\_id, type }  or null

The execution context that produced this tool call.

Direct object { type }

type: "direct"

The caller type. Always `direct`.

Program object { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

minLength1

maxLength64

type: "program"

The caller type. Always `program`.

CustomToolCall object { call\_id, input, name, 5 more }

A call to a custom tool created by the model.

call\_id: string

An identifier used to map this custom tool call to a tool call output.

input: string

The input for the custom tool call generated by the model.

The name of the custom tool being called.

type: "custom\_tool\_call"

The type of the custom tool call. Always `custom_tool_call`.

id: optional string

The unique ID of the custom tool call in the OpenAI platform.

async: optional boolean

Whether the custom tool call runs asynchronously.

caller: optional object { type }  or object { caller\_id, type }  or null

The execution context that produced this tool call.

Direct object { type }

type: "direct"

Program object { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

type: "program"

namespace: optional string

The namespace of the custom tool being called.

CompactionTrigger object { type, id }

Compacts the current context. Must be the final input item.

type: "compaction\_trigger"

The type of the item. Always `compaction_trigger`.

id: optional string or null

The unique ID of this compaction trigger.

ItemReference object { id, type }

An internal identifier for an item to reference.

The ID of the item to reference.

type: optional "item\_reference" or null

The type of item to reference. Always `item_reference`.

Program object { id, call\_id, code, 2 more }

The unique ID of this program item.

call\_id: string

The stable call ID of the program item.

minLength1

maxLength64

code: string

The JavaScript source executed by programmatic tool calling.

maxLength10485760

fingerprint: string

Opaque program replay fingerprint that must be round-tripped.

maxLength10485760

type: "program"

The item type. Always `program`.

ProgramOutput object { id, call\_id, result, 2 more }

The unique ID of this program output item.

call\_id: string

The call ID of the program item.

minLength1

maxLength64

result: string

The result produced by the program item.

maxLength10485760

status: "completed" or "incomplete"

The terminal status of the program output.

"completed"

"incomplete"

type: "program\_output"

The item type. Always `program_output`.

type: "response.item.create"

The Live client event type. Always `response.item.create`.

event\_id: optional string or null

Optional client identifier for correlating this command with a server event’s client\_event\_id or error.client\_event\_id.

maxLength512

ResponsesDelegationConfig object { model, instructions, max\_output\_tokens, 6 more }

Model, prompt, and tool settings for tasks delegated by the Live session to a Responses backend.

model: string

The model used for server-owned Responses delegations.

instructions: optional string or null

Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

max\_output\_tokens: optional number or null

Maximum number of output tokens for each delegated response.

minimum16

parallel\_tool\_calls: optional boolean or null

Whether the delegated Responses model may request multiple tool calls in a single response.

reasoning: optional object { effort, summary }  or null

Reasoning settings passed to each delegated Responses request.

effort: optional "none" or "minimal" or "low" or 3 more or null

How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

"none"

"minimal"

"low"

"medium"

"high"

"xhigh"

summary: optional "concise" or "detailed" or "auto" or null

The reasoning summary to request from the delegated Responses model, when supported.

"concise"

"detailed"

"auto"

service\_tier: optional "auto" or "default" or "fast\_tier\_temp\_pilot" or 3 more or null

Service tier for delegated Responses requests.

"auto"

"default"

"fast\_tier\_temp\_pilot"

"flex"

"priority"

"ultrafast"

text: optional object { verbosity }  or null

Text generation settings passed to each delegated Responses request.

verbosity: optional "low" or "medium" or "high" or null

The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

"low"

"medium"

"high"

tool\_choice: optional "auto" or "none" or "required" or object { name, type }  or object { name, server\_label, type }

Controls which tool the Responses backend uses when handling a task delegated by the Live model.

LiveToolChoiceEnum = "auto" or "none" or "required"

"auto"

"none"

"required"

LiveFunctionToolChoiceParam object { name, type }

minLength1

maxLength64

type: "function"

LiveMCPToolChoiceParam object { name, server\_label, type }

minLength1

maxLength64

server\_label: string

minLength1

maxLength64

type: "mcp"

tools: optional array of [FunctionTool](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20function_tool%20%3E%20(schema)) { name, type, description, 2 more }  or object { type }

Tools available to the Responses backend while it handles tasks delegated by the Live model.

FunctionTool object { name, type, description, 2 more }

A function tool available to the Responses backend when the Live model delegates a task.

The name the delegated Responses model uses when calling this function.

type: "function"

The tool type. Always `function`.

description: optional string or null

What the function does and when the delegated Responses model should call it.

parameters: optional map[unknown] or null

A JSON Schema object describing the arguments accepted by the function.

strict: optional boolean or null

Whether the delegated Responses model must follow the function’s parameter schema exactly.

WebSearch object { type }

A web search tool available to the Live session’s Responses backend.

type: "web\_search"

The tool type. Always `web_search`.

ResponsesDelegationUpdateConfig object { instructions, max\_output\_tokens, model, 6 more }

Updates to the Responses backend of an existing Live session. Omitted settings retain their current values.

instructions: optional string or null

Instructions for the delegated Responses model, separate from Live instructions. See [backend prompting](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt).

max\_output\_tokens: optional number or null

Maximum number of output tokens for each delegated response.

minimum16

model: optional string

The Responses backend model to use for subsequent delegated requests. Omit to keep the current backend model.

parallel\_tool\_calls: optional boolean or null

Whether the delegated Responses model may request multiple tool calls in a single response.

reasoning: optional object { effort, summary }  or null

Reasoning settings passed to each delegated Responses request.

effort: optional "none" or "minimal" or "low" or 3 more or null

How much reasoning effort the delegated Responses model should use. Supported values depend on the backend model.

"none"

"minimal"

"low"

"medium"

"high"

"xhigh"

summary: optional "concise" or "detailed" or "auto" or null

The reasoning summary to request from the delegated Responses model, when supported.

"concise"

"detailed"

"auto"

service\_tier: optional "auto" or "default" or "fast\_tier\_temp\_pilot" or 3 more or null

Service tier for delegated Responses requests.

"auto"

"default"

"fast\_tier\_temp\_pilot"

"flex"

"priority"

"ultrafast"

text: optional object { verbosity }  or null

Text generation settings passed to each delegated Responses request.

verbosity: optional "low" or "medium" or "high" or null

The amount of detail in text generated by the Responses backend. This does not configure the Live model’s spoken delivery.

"low"

"medium"

"high"

tool\_choice: optional "auto" or "none" or "required" or object { name, type }  or object { name, server\_label, type }

Controls which tool the Responses backend uses when handling a task delegated by the Live model.

LiveToolChoiceEnum = "auto" or "none" or "required"

"auto"

"none"

"required"

LiveFunctionToolChoiceParam object { name, type }

minLength1

maxLength64

type: "function"

LiveMCPToolChoiceParam object { name, server\_label, type }

minLength1

maxLength64

server\_label: string

minLength1

maxLength64

type: "mcp"

tools: optional array of [FunctionTool](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20function_tool%20%3E%20(schema)) { name, type, description, 2 more }  or object { type }

Tools available to the Responses backend while it handles tasks delegated by the Live model.

FunctionTool object { name, type, description, 2 more }

A function tool available to the Responses backend when the Live model delegates a task.

The name the delegated Responses model uses when calling this function.

type: "function"

The tool type. Always `function`.

description: optional string or null

What the function does and when the delegated Responses model should call it.

parameters: optional map[unknown] or null

A JSON Schema object describing the arguments accepted by the function.

strict: optional boolean or null

Whether the delegated Responses model must follow the function’s parameter schema exactly.

WebSearch object { type }

A web search tool available to the Live session’s Responses backend.

type: "web\_search"

The tool type. Always `web_search`.

ServerEvent = [SessionStartedEvent](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20session_started_event%20%3E%20(schema)) { event\_id, session, type, client\_event\_id }  or [SessionUpdatedEvent](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20session_updated_event%20%3E%20(schema)) { event\_id, session, type, client\_event\_id }  or [InputAudioMutedEvent](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20input_audio_muted_event%20%3E%20(schema)) { event\_id, type, client\_event\_id }  or 19 more

Server events for Live. Response lifecycle events are wrapped inside response.event; dispatch the nested event by its full type and tolerate new response event types. Follow the [Live prompting guide](https://developers.openai.com/api/docs/guides/live-prompting) when designing the conversation and delegation policy.

SessionStartedEvent object { event\_id, session, type, client\_event\_id }

Returned when a Live session has started. Contains the resolved session configuration, including server defaults.

event\_id: string

The unique ID of the Live server event.

session: [SessionResource](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20session_resource%20%3E%20(schema)) { id, expires\_at, model, 7 more }

The resolved Live session configuration and server-assigned session metadata.

type: "session.started"

The event type, always `session.started`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

SessionUpdatedEvent object { event\_id, session, type, client\_event\_id }

Returned when a Live session update is accepted. Contains the resolved session configuration after the update.

event\_id: string

The unique ID of the Live server event.

session: [SessionResource](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20session_resource%20%3E%20(schema)) { id, expires\_at, model, 7 more }

The resolved Live session configuration and server-assigned session metadata.

type: "session.updated"

The event type, always `session.updated`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

InputAudioMutedEvent object { event\_id, type, client\_event\_id }

Returned when a session.input\_audio.mute command is accepted. Input audio is no longer sent to the model; sideband audio reflection continues.

event\_id: string

The unique ID of the Live server event.

type: "session.input\_audio.muted"

The event type, always `session.input_audio.muted`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

InputAudioUnmutedEvent object { event\_id, type, client\_event\_id }

Returned when a session.input\_audio.unmute command is accepted. Input audio is sent to the model again.

event\_id: string

The unique ID of the Live server event.

type: "session.input\_audio.unmuted"

The event type, always `session.input_audio.unmuted`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

InstructionsAppendedEvent object { end\_ms, event\_id, start\_ms, 2 more }

Returned when a session.instructions.append command is accepted into the Live session timeline. Acknowledges the appended instructions without guaranteeing that the model has acted on them.

end\_ms: number

The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start\_ms.

event\_id: string

The unique ID of the Live server event.

start\_ms: number

The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

type: "session.instructions.appended"

The event type, always `session.instructions.appended`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

ThinkingAppendedEvent object { end\_ms, event\_id, start\_ms, 2 more }

Returned when a session.thinking.append command is accepted into the Live session timeline. Acknowledges the added reasoning context without guaranteeing any spoken output.

end\_ms: number

The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start\_ms.

event\_id: string

The unique ID of the Live server event.

start\_ms: number

The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

type: "session.thinking.appended"

The event type, always `session.thinking.appended`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

CommentaryAppendedEvent object { end\_ms, event\_id, start\_ms, 2 more }

Returned when a session.commentary.append command is accepted into the Live session timeline. Acknowledges the added commentary without guaranteeing exact wording or completed audio playback.

end\_ms: number

The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start\_ms.

event\_id: string

The unique ID of the Live server event.

start\_ms: number

The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

type: "session.commentary.appended"

The event type, always `session.commentary.appended`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

SessionInputAudioAppend object { audio, type }

Input audio received from the primary transport and reflected to a Live sideband connection before model-input muting.

audio: string

Base64-encoded raw mono PCM16LE at 24 kHz received from the primary transport, reflected to the sideband before model-input muting. This server event uses the same audio key as the client command, but is not an acknowledgment of it.

type: "session.input\_audio.append"

The event type, always `session.input_audio.append`.

OutputAudioDeltaEvent object { delta, type, end\_ms, start\_ms }

An audio chunk generated by the Live model. Decode and play primary WebSocket chunks in delivery order using the configured session audio format. Sideband connections receive reflected output audio with timestamps.

delta: string

Base64-encoded raw audio. Primary WebSocket events use the session’s configured format; reflected sideband events use mono PCM16LE at 24 kHz.

type: "session.output\_audio.delta"

The event type, always `session.output_audio.delta`.

end\_ms: optional number

Exclusive session-relative end in milliseconds. Required on reflected sideband events; omitted on the primary WebSocket. Dropped output frames leave gaps between reflected ranges.

start\_ms: optional number

Inclusive session-relative start in milliseconds. Required on reflected sideband events; omitted on the primary WebSocket.

InputTranscriptDeltaEvent object { delta, end\_ms, event\_id, 3 more }

A transcript fragment for user input audio in the Live session. Accumulate fragments in delivery order; these events do not define complete turns or include a transcript-done event.

delta: string

The transcript text fragment for the audio in this time range. Append fragments in delivery order to build the transcript.

end\_ms: number

The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start\_ms.

event\_id: string

The unique ID of the Live server event.

start\_ms: number

The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

type: "session.input\_transcript.delta"

The event type, always `session.input_transcript.delta`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

OutputTranscriptDeltaEvent object { delta, end\_ms, event\_id, 3 more }

A transcript fragment for assistant output audio in the Live session. Accumulate fragments in delivery order; these events do not define complete turns or include a transcript-done event.

delta: string

The transcript text fragment for the audio in this time range. Append fragments in delivery order to build the transcript.

end\_ms: number

The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start\_ms.

event\_id: string

The unique ID of the Live server event.

start\_ms: number

The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

type: "session.output\_transcript.delta"

The event type, always `session.output_transcript.delta`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

DelegationCreatedEvent object { delegation, event\_id, offset\_ms, 2 more }

Returned when the Live model delegates work to your application or a Responses backend. Contains delegation metadata and the position on the session timeline where the work was delegated.

delegation: object { id, target, type, response\_id }

The delegated work identifier and destination. This object contains metadata, not the task text.

The unique ID of the delegation. Use this as delegation\_id when replying to client-owned work or correlating Responses events.

target: "client" or "responses"

Where the Live model delegated the work: `client` for your application, or `responses` for the configured Responses backend.

"client" or "responses"

Where the Live model delegated the work: `client` for your application, or `responses` for the configured Responses backend.

"client"

"responses"

type: "delegation"

The object type, always `delegation`.

response\_id: optional string

The ID of the Responses API response associated with a Responses delegation. Omitted for client delegations.

event\_id: string

The unique ID of the Live server event.

offset\_ms: number

The position on the Live session timeline where the delegation was created, in milliseconds from the beginning of the session.

type: "session.delegation.created"

The event type, always `session.delegation.created`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

ResponseEvent object { event, event\_id, type, 2 more }

A streaming Responses API event from a backend delegated to by the Live session. Use the outer delegation\_id to associate the nested stream with its Live delegation.

event: map[unknown]

The nested Responses streaming event. Dispatch on its type field. Response lifecycle snapshots omit input and clear instructions, tools, and output to keep messages small; consume granular output events for the generated content.

event\_id: string

The unique ID of the Live server event.

type: "response.event"

The event type, always `response.event`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

delegation\_id: optional string or null

The Live delegation associated with the nested Responses event. May be null or omitted when the event cannot be correlated with a delegation.

SessionUsageUpdatedEvent object { event\_id, type, usage, 2 more }

Reports cumulative Live audio usage and, when available, the most recent context-window usage. Delegated Responses token usage is reported separately in response.event events.

event\_id: string

The unique ID of the Live server event.

type: "session.usage.updated"

The event type, always `session.usage.updated`.

usage: [SessionUsage](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20session_usage%20%3E%20(schema)) { seconds }

The cumulative Live audio usage so far.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

context\_window: optional object { usage\_ratio }

The latest measured Live context-window usage. Omitted when the context limit is unknown.

usage\_ratio: number

The latest active context token count divided by the Live model context limit. Can decrease after compaction and may lag between measured audio frames.

SessionClosedEvent object { event\_id, reason, session, 3 more }

Returned after the Live session finishes finalizing, with the close reason, final session snapshot, and cumulative audio usage. A connection closing without this event does not confirm successful finalization.

event\_id: string

The unique ID of the Live server event.

reason: "close\_requested" or "expired" or "content" or 2 more

Why the Live session ended: `close_requested` for an application close or hangup request, `expired` for the session duration limit, `content` for a safety filter, `remote_hangup` for a graceful remote disconnect, or `connection_lost` for an unexpected primary or upstream disconnection.

"close\_requested" or "expired" or "content" or 2 more

Why the Live session ended: `close_requested` for an application close or hangup request, `expired` for the session duration limit, `content` for a safety filter, `remote_hangup` for a graceful remote disconnect, or `connection_lost` for an unexpected primary or upstream disconnection.

"close\_requested"

"expired"

"content"

"remote\_hangup"

"connection\_lost"

session: [SessionResource](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20session_resource%20%3E%20(schema)) { id, expires\_at, model, 7 more }

The resolved Live session configuration and server-assigned session metadata.

type: "session.closed"

The event type, always `session.closed`.

usage: [SessionUsage](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20session_usage%20%3E%20(schema)) { seconds }

The final cumulative Live audio usage after session finalization.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

ErrorEvent object { error, event\_id, type, client\_event\_id }

Reports an error in the Live session, such as an invalid client command. Use error.client\_event\_id, when present, to identify the command that caused the error.

error: [Error](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20error%20%3E%20(schema)) { code, message, type, 2 more }

Details of the Live error and the client command that caused it, when known.

event\_id: string

The unique ID of the Live server event.

type: "error"

The event type, always `error`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

InfoEvent object { code, event\_id, message, 2 more }

An informational notice about the Live session, such as the event permissions applied to a frontend data channel.

code: string

A machine-readable code for the notice, such as `data_channel_permissions`.

event\_id: string

The unique ID of the Live server event.

message: string

A human-readable explanation of the Live session notice.

type: "info"

The event type, always `info`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

TransportDtmfReceived object { event, event\_id, type }

A SIP DTMF keypress received from the caller. Delivered only to sideband observers.

event: string

minLength1

maxLength1

event\_id: string

type: "transport.dtmf.received"

TransportDtmfSend object { event, event\_id, type }

A SIP DTMF keypress successfully sent by the hosted tool. Delivered only to sideband observers; this is not a client command.

event: string

minLength1

maxLength1

event\_id: string

type: "transport.dtmf.send"

TransportRinging object { event\_id, session\_id, type }

The outbound SIP provider leg is ringing or providing early media. Delivered only to sideband observers.

event\_id: string

session\_id: string

The canonical Live session ID.

type: "transport.ringing"

TransportAnswered object { event\_id, session\_id, type }

The outbound SIP provider leg answered and media is established. Delivered only to sideband observers.

event\_id: string

session\_id: string

The canonical Live session ID.

type: "transport.answered"

TransportFailed object { error, event\_id, session\_id, type }

An asynchronous outbound SIP setup failure. Delivered only to sideband observers.

error: object { code, message, type, param }

code: string

The call setup failure code.

message: string

type: "call\_error"

param: optional string

The parameter related to the error, if any. Empty when no parameter applies.

event\_id: string

session\_id: string

The canonical Live session ID.

type: "transport.failed"

ServerEventSelector object { type, response\_event }

A Live server event selector for the WebRTC frontend data channel.

type: string

The outer Live server event type. Use ‘response.event’ for Responses events.

minLength1

maxLength256

response\_event: optional string

The nested Responses event type. Required when type is ‘response.event’; forbidden for other event types.

minLength1

maxLength256

SessionCloseEvent object { type, event\_id }

Request that the Live session close. The terminal `session.closed` event contains the close reason and final usage.

type: "session.close"

The Live client event type. Always `session.close`.

event\_id: optional string or null

Optional client identifier for correlating this command with a server event’s client\_event\_id or error.client\_event\_id.

maxLength512

SessionClosedEvent object { event\_id, reason, session, 3 more }

Returned after the Live session finishes finalizing, with the close reason, final session snapshot, and cumulative audio usage. A connection closing without this event does not confirm successful finalization.

event\_id: string

The unique ID of the Live server event.

reason: "close\_requested" or "expired" or "content" or 2 more

Why the Live session ended: `close_requested` for an application close or hangup request, `expired` for the session duration limit, `content` for a safety filter, `remote_hangup` for a graceful remote disconnect, or `connection_lost` for an unexpected primary or upstream disconnection.

"close\_requested" or "expired" or "content" or 2 more

Why the Live session ended: `close_requested` for an application close or hangup request, `expired` for the session duration limit, `content` for a safety filter, `remote_hangup` for a graceful remote disconnect, or `connection_lost` for an unexpected primary or upstream disconnection.

"close\_requested"

"expired"

"content"

"remote\_hangup"

"connection\_lost"

session: [SessionResource](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20session_resource%20%3E%20(schema)) { id, expires\_at, model, 7 more }

The resolved Live session configuration and server-assigned session metadata.

type: "session.closed"

The event type, always `session.closed`.

usage: [SessionUsage](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20session_usage%20%3E%20(schema)) { seconds }

The final cumulative Live audio usage after session finalization.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

SessionConfig object { model, audio, client, 4 more }

Initial configuration for a Live session, including its model, conversation instructions, audio, and delegated task handling.

model: string or "gpt-live-1"

The Live model. Required in the session configuration for every transport; do not pass it as a URL query parameter.

string

"gpt-live-1"

The Live model. Required in the session configuration for every transport; do not pass it as a URL query parameter.

audio: optional object { format, output }

Startup audio configuration. Only primary WebSockets accept audio.format; WebRTC and SIP negotiate their media format. Voice and format are immutable after startup.

format: optional [AudioFormat](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20audio_format%20%3E%20(schema))

Audio encoding and sample rate for audio sent and received over a Live WebSocket connection. WebRTC and SIP negotiate their media format separately.

output: optional object { voice }

The voice used for speech generated by the Live model.

voice: optional string or "alloy" or "ash" or "ballad" or 19 more or [CustomVoice](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20custom_voice%20%3E%20(schema)) { id }

The voice used for Live speech, as a built-in voice name or a custom voice object containing its ID. Defaults to `marin` and cannot change after startup.

string

"alloy" or "ash" or "ballad" or 19 more

The voice used for Live speech, as a built-in voice name or a custom voice object containing its ID. Defaults to `marin` and cannot change after startup.

"alloy"

"ash"

"ballad"

"beacon"

"bossa"

"cedar"

"cinder"

"coral"

"delta"

"echo"

"gleam"

"marin"

"meridian"

"quartz"

"ripple"

"sage"

"shimmer"

"stone"

"tempo"

"verse"

"vesper"

"willow"

CustomVoice object { id }

minLength1

maxLength128

client: optional [ClientConfig](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20client_config%20%3E%20(schema)) { data\_channel }

Startup-only capabilities for an untrusted frontend attached to a unified WebRTC session. Trusted sideband connections are unaffected.

delegation: optional [ClientDelegation](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20client_delegation%20%3E%20(schema)) { type }  or object { responses, type }  or null

Who handles tasks delegated by the Live model. Omitted or null selects your application; use `responses` to let the API manage a Responses backend.

ClientDelegation object { type }

Delegate tasks to your application. The Live session emits delegation events that your backend handles.

type: "client"

The delegation owner. Always `client` for tasks handled by your application.

Responses object { responses, type }

Delegate tasks to a Responses model managed by the Live session.

responses: [ResponsesDelegationConfig](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20responses_delegation_config%20%3E%20(schema)) { model, instructions, max\_output\_tokens, 6 more }

Backend model, prompt, and tools used when the Live session delegates a task to Responses.

type: "responses"

The delegation owner. Always `responses` for tasks handled by the Responses API.

input: optional array of [InitialItem](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20initial_item%20%3E%20(schema))

Ordered text-only history supplied before startup. Supports developer, user, and assistant messages with one text part each; at most 128 messages and 8,192 rendered tokens in total.

Developer object { content, role, id, 2 more }

A developer message included in the initial text history of a Live session.

content: array of object { text, type }

The message content. Supply exactly one text part for the initial Live conversation history.

text: string

The message text to include in the Live session’s initial conversation history.

type: optional "input\_text"

The text content type. Always `input_text`.

role: "developer"

The author of this history message. Always `developer`.

id: optional string or null

An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

status: optional "incomplete" or "completed" or null

The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

"incomplete"

"completed"

type: optional "message"

The history item type. Always `message`.

User object { content, role, id, 2 more }

A user message included in the initial text history of a Live session.

content: array of object { text, type }

The message content. Supply exactly one text part for the initial Live conversation history.

text: string

The message text to include in the Live session’s initial conversation history.

type: optional "input\_text"

The text content type. Always `input_text`.

role: "user"

The author of this history message. Always `user`.

id: optional string or null

An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

status: optional "incomplete" or "completed" or null

The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

"incomplete"

"completed"

type: optional "message"

The history item type. Always `message`.

Assistant object { content, role, id, 2 more }

An assistant message included in the initial text history of a Live session.

content: array of object { text, type }  or object { text, type }

The message content. Supply exactly one text part for the initial Live conversation history.

Text object { text, type }

Assistant text supplied as conversation history when starting a Live session.

text: string

The message text to include in the Live session’s initial conversation history.

type: optional "text"

The text content type. Always `text`.

OutputText object { text, type }

Assistant output text supplied as conversation history when starting a Live session.

text: string

The message text to include in the Live session’s initial conversation history.

type: "output\_text"

The text content type. Always `output_text`.

role: "assistant"

The author of this history message. Always `assistant`.

id: optional string or null

An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

status: optional "incomplete" or "completed" or null

The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

"incomplete"

"completed"

type: optional "message"

The history item type. Always `message`.

instructions: optional string or null

Frontend instructions for voice, conversation, interruptions, and when to delegate. Start with the [Live prompting guide](/api/docs/guides/live-prompting); put business rules and tool workflows in a separate [backend prompt](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt). Limited to 16,384 client-supplied tokens. Omitted or blank instructions use server defaults. Immutable after startup.

store: optional boolean

Whether to store the session for later forking and recording download. Defaults to false for new sessions.

SessionResource object { id, expires\_at, model, 7 more }

The resolved Live session configuration and server-assigned session metadata.

The unique ID of the Live session. Use this ID for sideband connections, forking, and recording download.

expires\_at: number

The Unix timestamp, in seconds, at which the Live session expires.

model: string or "gpt-live-1"

The Live model. Required in the session configuration for every transport; do not pass it as a URL query parameter.

string

"gpt-live-1"

The Live model. Required in the session configuration for every transport; do not pass it as a URL query parameter.

status: "active"

The status of the session snapshot. Always `active`, including the final snapshot in session.closed; use the event type to determine that the session has closed.

audio: optional object { format, output }

Startup audio configuration. Only primary WebSockets accept audio.format; WebRTC and SIP negotiate their media format. Voice and format are immutable after startup.

format: optional [AudioFormat](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20audio_format%20%3E%20(schema))

Audio encoding and sample rate for audio sent and received over a Live WebSocket connection. WebRTC and SIP negotiate their media format separately.

output: optional object { voice }

The voice used for speech generated by the Live model.

voice: optional string or "alloy" or "ash" or "ballad" or 19 more or [CustomVoice](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20custom_voice%20%3E%20(schema)) { id }

The voice used for Live speech, as a built-in voice name or a custom voice object containing its ID. Defaults to `marin` and cannot change after startup.

string

"alloy" or "ash" or "ballad" or 19 more

The voice used for Live speech, as a built-in voice name or a custom voice object containing its ID. Defaults to `marin` and cannot change after startup.

"alloy"

"ash"

"ballad"

"beacon"

"bossa"

"cedar"

"cinder"

"coral"

"delta"

"echo"

"gleam"

"marin"

"meridian"

"quartz"

"ripple"

"sage"

"shimmer"

"stone"

"tempo"

"verse"

"vesper"

"willow"

CustomVoice object { id }

minLength1

maxLength128

client: optional [ClientConfig](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20client_config%20%3E%20(schema)) { data\_channel }

Startup-only capabilities for an untrusted frontend attached to a unified WebRTC session. Trusted sideband connections are unaffected.

delegation: optional [ClientDelegation](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20client_delegation%20%3E%20(schema)) { type }  or object { responses, type }  or null

Who handles tasks delegated by the Live model. Omitted or null selects your application; use `responses` to let the API manage a Responses backend.

ClientDelegation object { type }

Delegate tasks to your application. The Live session emits delegation events that your backend handles.

type: "client"

The delegation owner. Always `client` for tasks handled by your application.

Responses object { responses, type }

Delegate tasks to a Responses model managed by the Live session.

responses: [ResponsesDelegationConfig](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20responses_delegation_config%20%3E%20(schema)) { model, instructions, max\_output\_tokens, 6 more }

Backend model, prompt, and tools used when the Live session delegates a task to Responses.

type: "responses"

The delegation owner. Always `responses` for tasks handled by the Responses API.

input: optional array of [InitialItem](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20initial_item%20%3E%20(schema))

Ordered text-only history supplied before startup. Supports developer, user, and assistant messages with one text part each; at most 128 messages and 8,192 rendered tokens in total.

Developer object { content, role, id, 2 more }

A developer message included in the initial text history of a Live session.

content: array of object { text, type }

The message content. Supply exactly one text part for the initial Live conversation history.

text: string

The message text to include in the Live session’s initial conversation history.

type: optional "input\_text"

The text content type. Always `input_text`.

role: "developer"

The author of this history message. Always `developer`.

id: optional string or null

An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

status: optional "incomplete" or "completed" or null

The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

"incomplete"

"completed"

type: optional "message"

The history item type. Always `message`.

User object { content, role, id, 2 more }

A user message included in the initial text history of a Live session.

content: array of object { text, type }

The message content. Supply exactly one text part for the initial Live conversation history.

text: string

The message text to include in the Live session’s initial conversation history.

type: optional "input\_text"

The text content type. Always `input_text`.

role: "user"

The author of this history message. Always `user`.

id: optional string or null

An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

status: optional "incomplete" or "completed" or null

The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

"incomplete"

"completed"

type: optional "message"

The history item type. Always `message`.

Assistant object { content, role, id, 2 more }

An assistant message included in the initial text history of a Live session.

content: array of object { text, type }  or object { text, type }

The message content. Supply exactly one text part for the initial Live conversation history.

Text object { text, type }

Assistant text supplied as conversation history when starting a Live session.

text: string

The message text to include in the Live session’s initial conversation history.

type: optional "text"

The text content type. Always `text`.

OutputText object { text, type }

Assistant output text supplied as conversation history when starting a Live session.

text: string

The message text to include in the Live session’s initial conversation history.

type: "output\_text"

The text content type. Always `output_text`.

role: "assistant"

The author of this history message. Always `assistant`.

id: optional string or null

An optional identifier for the supplied history message. Live uses the message’s role and text to initialize the conversation.

status: optional "incomplete" or "completed" or null

The supplied message’s status. Live uses its text as history and does not resume an incomplete message.

"incomplete"

"completed"

type: optional "message"

The history item type. Always `message`.

instructions: optional string or null

Frontend instructions for voice, conversation, interruptions, and when to delegate. Start with the [Live prompting guide](/api/docs/guides/live-prompting); put business rules and tool workflows in a separate [backend prompt](/api/docs/guides/live-delegation#start-with-your-existing-backend-prompt). Limited to 16,384 client-supplied tokens. Omitted or blank instructions use server defaults. Immutable after startup.

store: optional boolean

Whether to store the session for later forking and recording download. Defaults to false for new sessions.

SessionStartEvent object { session, type, event\_id }

Start a Live session on a primary WebSocket. Send this event before other commands and wait for `session.started`.

session: [SessionConfig](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20session_config%20%3E%20(schema)) { model, audio, client, 4 more }

Initial configuration for a primary WebSocket. Send session.start first and wait for session.started before application commands. WebRTC creation already starts the session; do not send this event again on its data channel.

type: "session.start"

The Live client event type. Always `session.start`.

event\_id: optional string or null

Optional client identifier for correlating this command with a server event’s client\_event\_id or error.client\_event\_id.

maxLength512

SessionStartedEvent object { event\_id, session, type, client\_event\_id }

Returned when a Live session has started. Contains the resolved session configuration, including server defaults.

event\_id: string

The unique ID of the Live server event.

session: [SessionResource](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20session_resource%20%3E%20(schema)) { id, expires\_at, model, 7 more }

The resolved Live session configuration and server-assigned session metadata.

type: "session.started"

The event type, always `session.started`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

SessionUpdateConfig object { delegation }

Changes to an active Live session. Only delegation backend settings can be updated after startup.

delegation: optional [ClientDelegation](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20client_delegation%20%3E%20(schema)) { type }  or object { type, responses }  or null

Delegation settings to update. The delegation type must match the current session; omitted settings retain their values.

ClientDelegation object { type }

Delegate tasks to your application. The Live session emits delegation events that your backend handles.

type: "client"

The delegation owner. Always `client` for tasks handled by your application.

Responses object { type, responses }

Update the Responses backend for an existing Live session without changing delegation ownership.

type: "responses"

The delegation owner. Always `responses` for tasks handled by the Responses API.

responses: optional [ResponsesDelegationUpdateConfig](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20responses_delegation_update_config%20%3E%20(schema)) { instructions, max\_output\_tokens, model, 6 more }

Responses backend settings to update. Omitted settings keep their existing values.

SessionUpdateEvent object { session, type, event\_id }

Update the delegation settings of an active Live session. The server acknowledges accepted changes with `session.updated`.

session: [SessionUpdateConfig](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20session_update_config%20%3E%20(schema)) { delegation }

Sparse delegation updates. Omitted settings retain their values. The delegation type cannot change, including resetting Responses delegation to null or client. Model, frontend instructions, audio, and startup input are immutable.

type: "session.update"

The Live client event type. Always `session.update`.

event\_id: optional string or null

Optional client identifier for correlating this command with a server event’s client\_event\_id or error.client\_event\_id.

maxLength512

SessionUpdatedEvent object { event\_id, session, type, client\_event\_id }

Returned when a Live session update is accepted. Contains the resolved session configuration after the update.

event\_id: string

The unique ID of the Live server event.

session: [SessionResource](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20session_resource%20%3E%20(schema)) { id, expires\_at, model, 7 more }

The resolved Live session configuration and server-assigned session metadata.

type: "session.updated"

The event type, always `session.updated`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

SessionUsage object { seconds }

Cumulative audio duration for a Live session. Values are totals for the session, not increments to sum across usage events.

seconds: number

The cumulative Live audio duration in seconds. Do not sum this value across usage events.

SessionUsageUpdatedEvent object { event\_id, type, usage, 2 more }

Reports cumulative Live audio usage and, when available, the most recent context-window usage. Delegated Responses token usage is reported separately in response.event events.

event\_id: string

The unique ID of the Live server event.

type: "session.usage.updated"

The event type, always `session.usage.updated`.

usage: [SessionUsage](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20session_usage%20%3E%20(schema)) { seconds }

The cumulative Live audio usage so far.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

context\_window: optional object { usage\_ratio }

The latest measured Live context-window usage. Omitted when the context limit is unknown.

usage\_ratio: number

The latest active context token count divided by the Live model context limit. Can decrease after compaction and may lag between measured audio frames.

ThinkingAppendEvent object { content, delegation\_id, type, event\_id }

Provide silent reasoning or progress context to the Live model, optionally for an existing client delegation.

content: string

Silent reasoning or progress context, limited to 500 tokens. It does not directly request speech, but can influence later speech and is not a secrecy boundary.

delegation\_id: string or null

Required, nullable. Set null for general session context, or use the ID from session.delegation.created for an existing client delegation. Non-null IDs are not accepted with Responses delegation.

minLength1

type: "session.thinking.append"

The Live client event type. Always `session.thinking.append`.

event\_id: optional string or null

Optional client identifier for correlating this command with a server event’s client\_event\_id or error.client\_event\_id.

maxLength512

ThinkingAppendedEvent object { end\_ms, event\_id, start\_ms, 2 more }

Returned when a session.thinking.append command is accepted into the Live session timeline. Acknowledges the added reasoning context without guaranteeing any spoken output.

end\_ms: number

The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start\_ms.

event\_id: string

The unique ID of the Live server event.

start\_ms: number

The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

type: "session.thinking.appended"

The event type, always `session.thinking.appended`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

#### LiveForks

##### ModelsExpand Collapse

ForkClientEvent = [ForkSessionStartEvent](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20fork_session_start_event%20%3E%20(schema)) { session, type, event\_id }  or [SessionUpdateEvent](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20session_update_event%20%3E%20(schema)) { session, type, event\_id }  or [InputAudioAppendEvent](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20input_audio_append_event%20%3E%20(schema)) { audio, type, event\_id }  or 8 more

Client events for a Live fork WebSocket. First send session.start with an overrides object (which may be empty), then wait for session.started before sending other commands. The model and conversation are inherited from the stored session.

ForkSessionStartEvent object { session, type, event\_id }

Start a Live session after connecting to a stored session’s fork WebSocket. Send an empty `session` object to use the stored configuration.

session: [ForkSessionConfig](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20fork_session_config%20%3E%20(schema)) { audio, client, delegation, store }

Overrides for a stored session after connecting to the fork WebSocket. An empty object inherits the stored configuration; do not supply a new model. audio.format applies only to the new WebSocket connection. client overrides are only supported for WebRTC forks.

type: "session.start"

The Live client event type. Always `session.start`.

event\_id: optional string or null

Optional client identifier for correlating this command with a server event’s client\_event\_id or error.client\_event\_id.

maxLength512

SessionUpdateEvent object { session, type, event\_id }

Update the delegation settings of an active Live session. The server acknowledges accepted changes with `session.updated`.

session: [SessionUpdateConfig](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20session_update_config%20%3E%20(schema)) { delegation }

Sparse delegation updates. Omitted settings retain their values. The delegation type cannot change, including resetting Responses delegation to null or client. Model, frontend instructions, audio, and startup input are immutable.

type: "session.update"

The Live client event type. Always `session.update`.

event\_id: optional string or null

Optional client identifier for correlating this command with a server event’s client\_event\_id or error.client\_event\_id.

maxLength512

InputAudioAppendEvent object { audio, type, event\_id }

Send audio to a Live session over its primary WebSocket. WebRTC and SIP sessions send audio over their media transport.

audio: string

Base64-encoded raw audio in the startup-selected format, without a WAV or other container header. Primary WebSocket only; media transports use their audio track. Audio appends have no acknowledgment. Reflected sideband server events reuse this event type and audio key, with no timestamps or event\_id; their audio is always mono PCM16LE at 24 kHz.

minLength1

type: "session.input\_audio.append"

The Live client event type. Always `session.input_audio.append`.

event\_id: optional string or null

Optional client identifier for correlating this command with a server event’s client\_event\_id or error.client\_event\_id.

maxLength512

InputAudioMuteEvent object { type, event\_id }

Mute audio input to the Live model without closing the session. The server acknowledges with `session.input_audio.muted`.

type: "session.input\_audio.mute"

The Live client event type. Always `session.input_audio.mute`.

event\_id: optional string or null

Optional client identifier for correlating this command with a server event’s client\_event\_id or error.client\_event\_id.

maxLength512

InputAudioUnmuteEvent object { type, event\_id }

Resume audio input to a Live model after muting it. The server acknowledges with `session.input_audio.unmuted`.

type: "session.input\_audio.unmute"

The Live client event type. Always `session.input_audio.unmute`.

event\_id: optional string or null

Optional client identifier for correlating this command with a server event’s client\_event\_id or error.client\_event\_id.

maxLength512

InstructionsAppendEvent object { content, delegation\_id, type, event\_id }

Append instructions to the Live conversation while it is running, optionally associating them with an existing client delegation.

content: string

Instruction text to append, limited to 500 tokens. This is a plain string, not an array of content parts.

delegation\_id: string or null

Required, nullable. Set null for general session context, or use the ID from session.delegation.created for an existing client delegation. Non-null IDs are not accepted with Responses delegation.

minLength1

type: "session.instructions.append"

The Live client event type. Always `session.instructions.append`.

event\_id: optional string or null

Optional client identifier for correlating this command with a server event’s client\_event\_id or error.client\_event\_id.

maxLength512

ThinkingAppendEvent object { content, delegation\_id, type, event\_id }

Provide silent reasoning or progress context to the Live model, optionally for an existing client delegation.

content: string

Silent reasoning or progress context, limited to 500 tokens. It does not directly request speech, but can influence later speech and is not a secrecy boundary.

delegation\_id: string or null

Required, nullable. Set null for general session context, or use the ID from session.delegation.created for an existing client delegation. Non-null IDs are not accepted with Responses delegation.

minLength1

type: "session.thinking.append"

The Live client event type. Always `session.thinking.append`.

event\_id: optional string or null

Optional client identifier for correlating this command with a server event’s client\_event\_id or error.client\_event\_id.

maxLength512

CommentaryAppendEvent object { content, delegation\_id, type, event\_id }

Provide context the Live model can communicate to the user, optionally for an existing client delegation.

content: string

Speakable context for the Live model, limited to 500 tokens. Use this for a result the model should communicate; use session.thinking.append for silent context.

delegation\_id: string or null

Required, nullable. Set null for general session context, or use the ID from session.delegation.created for an existing client delegation. Non-null IDs are not accepted with Responses delegation.

minLength1

type: "session.commentary.append"

The Live client event type. Always `session.commentary.append`.

event\_id: optional string or null

Optional client identifier for correlating this command with a server event’s client\_event\_id or error.client\_event\_id.

maxLength512

ResponseItemCreateEvent object { item, type, event\_id }

Add an input item to the Live session’s Responses backend. Requires Responses delegation; use `response.create` to request a response.

item: [EasyInputMessage](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)) { content, role, phase, type }  or object { content, role, status, type }  or [ResponseOutputMessage](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_output_message%20%3E%20(schema)) { id, content, role, 3 more }  or 30 more

An input item to append to the Responses backend conversation, such as a user message or a function tool result.

EasyInputMessage object { content, role, phase, type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: string or [ResponseInputMessageContentList](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_message_content_list%20%3E%20(schema)) { , ,  }

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

TextInput = string

A text input to the model.

ResponseInputMessageContentList = array of [ResponseInputContent](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_content%20%3E%20(schema))

A list of one or many input items to the model, containing different content
types.

ResponseInputText object { text, type, prompt\_cache\_breakpoint }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

ResponseInputImage object { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](/api/docs/guides/images-vision).

detail: [ImageDetail](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20image_detail%20%3E%20(schema))

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

type: "input\_image"

The type of the input item. Always `input_image`.

file\_id: optional string or null

The ID of the file to be sent to the model.

image\_url: optional string or null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

prompt\_cache\_breakpoint: optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

ResponseInputFile object { type, detail, file\_data, 4 more }

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

file\_id: optional string or null

The ID of the file to be sent to the model.

file\_url: optional string

The URL of the file to be sent to the model.

formaturi

filename: optional string

The name of the file to be sent to the model.

prompt\_cache\_breakpoint: optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

role: "user" or "assistant" or "system" or "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

"user"

"assistant"

"system"

"developer"

phase: optional "commentary" or "final\_answer" or null

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

"commentary"

"final\_answer"

type: optional "message"

The type of the message input. Always `message`.

Message object { content, role, status, type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role.

content: [ResponseInputMessageContentList](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_message_content_list%20%3E%20(schema)) { , ,  }

A list of one or many input items to the model, containing different content
types.

role: "user" or "system" or "developer"

The role of the message input. One of `user`, `system`, or `developer`.

"user"

"system"

"developer"

status: optional "in\_progress" or "completed" or "incomplete"

The status of item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: optional "message"

The type of the message input. Always set to `message`.

ResponseOutputMessage object { id, content, role, 3 more }

An output message from the model.

The unique ID of the output message.

content: array of [ResponseOutputText](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_output_text%20%3E%20(schema)) { annotations, logprobs, text, type }  or [ResponseOutputRefusal](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_output_refusal%20%3E%20(schema)) { refusal, type }

The content of the output message.

ResponseOutputText object { annotations, logprobs, text, type }

A text output from the model.

annotations: array of object { file\_id, filename, index, type }  or object { end\_index, start\_index, title, 2 more }  or object { container\_id, end\_index, file\_id, 3 more }  or object { file\_id, index, type }

The annotations of the text output.

FileCitation object { file\_id, filename, index, type }

A citation to a file.

file\_id: string

The ID of the file.

filename: string

The filename of the file cited.

index: number

The index of the file in the list of files.

type: "file\_citation"

The type of the file citation. Always `file_citation`.

URLCitation object { end\_index, start\_index, title, 2 more }

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

formaturi

ContainerFileCitation object { container\_id, end\_index, file\_id, 3 more }

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

FilePath object { file\_id, index, type }

A path to a file.

file\_id: string

The ID of the file.

index: number

The index of the file in the list of files.

type: "file\_path"

The type of the file path. Always `file_path`.

logprobs: array of object { token, bytes, logprob, top\_logprobs }

token: string

bytes: array of number

logprob: number

top\_logprobs: array of object { token, bytes, logprob }

token: string

bytes: array of number

logprob: number

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

ResponseOutputRefusal object { refusal, type }

A refusal from the model.

refusal: string

The refusal explanation from the model.

type: "refusal"

The type of the refusal. Always `refusal`.

role: "assistant"

The role of the output message. Always `assistant`.

status: "in\_progress" or "completed" or "incomplete"

The status of the message input. One of `in_progress`, `completed`, or
`incomplete`. Populated when input items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: "message"

The type of the output message. Always `message`.

phase: optional "commentary" or "final\_answer" or null

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

"commentary"

"final\_answer"

FileSearchCall object { id, queries, status, 2 more }

The results of a file search tool call. See the
[file search guide](/api/docs/guides/tools-file-search) for more information.

The unique ID of the file search tool call.

queries: array of string

The queries used to search for files.

status: "in\_progress" or "searching" or "completed" or 2 more

The status of the file search tool call. One of `in_progress`,
`searching`, `incomplete` or `failed`,

"in\_progress"

"searching"

"completed"

"incomplete"

"failed"

type: "file\_search\_call"

The type of the file search tool call. Always `file_search_call`.

results: optional array of object { attributes, file\_id, filename, 2 more }  or null

The results of the file search tool call.

attributes: optional map[string or number or boolean] or null

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard. Keys are strings
with a maximum length of 64 characters. Values are strings with a maximum
length of 512 characters, booleans, or numbers.

string

number

boolean

file\_id: optional string

The unique ID of the file.

filename: optional string

The name of the file.

score: optional number

The relevance score of the file - a value between 0 and 1.

formatfloat

text: optional string

The text that was retrieved from the file.

ComputerCall object { id, call\_id, pending\_safety\_checks, 4 more }

A tool call to a computer use tool. See the
[computer use guide](/api/docs/guides/tools-computer-use) for more information.

The unique ID of the computer call.

call\_id: string

An identifier used when responding to the tool call with output.

pending\_safety\_checks: array of object { id, code, message }

The pending safety checks for the computer call.

The ID of the pending safety check.

code: optional string or null

The type of the pending safety check.

message: optional string or null

Details about the pending safety check.

status: "in\_progress" or "completed" or "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

type: "computer\_call"

The type of the computer call. Always `computer_call`.

action: optional [ComputerAction](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20computer_action%20%3E%20(schema))

A click action.

actions: optional [ComputerActionList](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20computer_action_list%20%3E%20(schema)) { Click, DoubleClick, Drag, 6 more }

Flattened batched actions for `computer_use`. Each action includes an
`type` discriminator and action-specific fields.

ComputerCallOutput object { call\_id, output, type, 3 more }

The output of a computer tool call.

call\_id: string

The ID of the computer tool call that produced the output.

minLength1

maxLength64

output: [ResponseComputerToolCallOutputScreenshot](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_computer_tool_call_output_screenshot%20%3E%20(schema)) { type, file\_id, image\_url }

A computer screenshot image used with the computer use tool.

type: "computer\_call\_output"

The type of the computer tool call output. Always `computer_call_output`.

id: optional string or null

The ID of the computer tool call output.

acknowledged\_safety\_checks: optional array of object { id, code, message }  or null

The safety checks reported by the API that have been acknowledged by the developer.

The ID of the pending safety check.

code: optional string or null

The type of the pending safety check.

message: optional string or null

Details about the pending safety check.

status: optional "in\_progress" or "completed" or "incomplete" or null

The status of the message input. One of `in_progress`, `completed`, or `incomplete`. Populated when input items are returned via API.

"in\_progress"

"completed"

"incomplete"

WebSearchCall object { id, action, status, type }

The results of a web search tool call. See the
[web search guide](/api/docs/guides/tools-web-search) for more information.

The unique ID of the web search tool call.

action: object { type, queries, query, sources }  or object { type, url }  or object { pattern, type, url }

An object describing the specific action taken in this web search call.
Includes details on how the model used the web (search, open\_page, find\_in\_page).

Search object { type, queries, query, sources }

Action type “search” - Performs a web search query.

type: "search"

The action type.

queries: optional array of string

The search queries.

Deprecatedquery: optional string

The search query.

sources: optional array of object { type, url }

The sources used in the search.

type: "url"

The type of source. Always `url`.

url: string

The URL of the source.

formaturi

OpenPage object { type, url }

Action type “open\_page” - Opens a specific URL from search results.

type: "open\_page"

The action type.

url: optional string or null

The URL opened by the model.

formaturi

FindInPage object { pattern, type, url }

Action type “find\_in\_page”: Searches for a pattern within a loaded page.

pattern: string

The pattern or text to search for within the page.

type: "find\_in\_page"

The action type.

url: string

The URL of the page searched for the pattern.

formaturi

status: "in\_progress" or "searching" or "completed" or 2 more

The status of the web search tool call.

"in\_progress"

"searching"

"completed"

"failed"

"incomplete"

type: "web\_search\_call"

The type of the web search tool call. Always `web_search_call`.

FunctionCall object { arguments, call\_id, name, 6 more }

A tool call to run a function. See the
[function calling guide](/api/docs/guides/function-calling) for more information.

arguments: string

A JSON string of the arguments to pass to the function.

call\_id: string

The unique ID of the function tool call generated by the model.

The name of the function to run.

type: "function\_call"

The type of the function tool call. Always `function_call`.

id: optional string

The unique ID of the function tool call.

async: optional boolean

Whether the function tool call runs asynchronously.

caller: optional object { type }  or object { caller\_id, type }  or null

The execution context that produced this tool call.

Direct object { type }

type: "direct"

Program object { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

type: "program"

namespace: optional string

The namespace of the function to run.

status: optional "in\_progress" or "completed" or "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

FunctionCallOutput object { output, type, id, 5 more }

The output of a function tool call.

output: string or array of [ResponseInputTextContent](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text_content%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [ResponseInputImageContent](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_image_content%20%3E%20(schema)) { type, detail, file\_id, 2 more }  or [ResponseInputFileContent](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_file_content%20%3E%20(schema)) { type, detail, file\_data, 4 more }

Text, image, or file output of the function tool call.

string

A JSON string of the output of the function tool call.

array of [ResponseInputTextContent](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text_content%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [ResponseInputImageContent](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_image_content%20%3E%20(schema)) { type, detail, file\_id, 2 more }  or [ResponseInputFileContent](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_file_content%20%3E%20(schema)) { type, detail, file\_data, 4 more }

An array of content outputs (text, image, file) for the function tool call.

ResponseInputTextContent object { text, type, prompt\_cache\_breakpoint }

A text input to the model.

text: string

The text input to the model.

maxLength10485760

type: "input\_text"

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: optional object { mode }  or null

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

ResponseInputImageContent object { type, detail, file\_id, 2 more }

An image input to the model. Learn about [image inputs](/api/docs/guides/images-vision)

type: "input\_image"

The type of the input item. Always `input_image`.

detail: optional [ImageDetail](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20image_detail%20%3E%20(schema)) or null

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

file\_id: optional string or null

The ID of the file to be sent to the model.

image\_url: optional string or null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

maxLength20971520

formaturi

prompt\_cache\_breakpoint: optional object { mode }  or null

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

ResponseInputFileContent object { type, detail, file\_data, 4 more }

A file input to the model.

type: "input\_file"

The type of the input item. Always `input_file`.

detail: optional "auto" or "low" or "high"

The detail level of the file to be sent to the model. Use `auto` to let the system select the detail level; for GPT-5.6 and later models, `auto` uses high-quality rendering, which may increase input token usage. Use `low` for lower-cost rendering, or `high` to render the file at higher quality. Defaults to `auto`.

"auto"

"low"

"high"

file\_data: optional string or null

The base64-encoded data of the file to be sent to the model.

maxLength73400320

file\_id: optional string or null

The ID of the file to be sent to the model.

file\_url: optional string or null

The URL of the file to be sent to the model.

formaturi

filename: optional string or null

The name of the file to be sent to the model.

prompt\_cache\_breakpoint: optional object { mode }  or null

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

type: "function\_call\_output"

The type of the function tool call output. Always `function_call_output`.

id: optional string or null

The unique ID of the function tool call output. Populated when this item is returned via API.

call\_id: optional string or null

The unique ID of the function tool call generated by the model.

minLength1

maxLength64

caller: optional object { type }  or object { caller\_id, type }  or null

The execution context that produced this tool call.

Direct object { type }

type: "direct"

The caller type. Always `direct`.

Program object { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

minLength1

maxLength64

type: "program"

The caller type. Always `program`.

name: optional string or null

The name of the tool that produced the output.

minLength1

maxLength128

namespace: optional string or null

The namespace of the tool that produced the output.

minLength1

maxLength64

status: optional "in\_progress" or "completed" or "incomplete" or null

The status of the item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

ToolSearchCall object { arguments, type, id, 3 more }

arguments: unknown

The arguments supplied to the tool search call.

type: "tool\_search\_call"

The item type. Always `tool_search_call`.

id: optional string or null

The unique ID of this tool search call.

call\_id: optional string or null

The unique ID of the tool search call generated by the model.

minLength1

maxLength64

execution: optional "server" or "client"

Whether tool search was executed by the server or by the client.

"server"

"client"

status: optional "in\_progress" or "completed" or "incomplete" or null

The status of the tool search call.

"in\_progress"

"completed"

"incomplete"

ToolSearchOutput object { tools, type, id, 3 more }

tools: array of object { name, parameters, strict, 6 more }  or object { type, vector\_store\_ids, filters, 2 more }  or object { type }  or 13 more

The loaded tool definitions returned by the tool search output.

Function object { name, parameters, strict, 6 more }

Defines a function in your own code the model can choose to call. Learn more about [function calling](/api/docs/guides/function-calling).

The name of the function to call.

parameters: map[unknown] or null

A JSON schema object describing the parameters of the function.

strict: boolean or null

Whether strict parameter validation is enforced for this function tool.

type: "function"

The type of the function tool. Always `function`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

async: optional boolean

defer\_loading: optional boolean

Whether this function is deferred and loaded via tool search.

description: optional string or null

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema: optional map[unknown] or null

A JSON schema object describing the JSON value encoded in string outputs for this function.

FileSearch object { type, vector\_store\_ids, filters, 2 more }

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](/api/docs/guides/tools-file-search).

type: "file\_search"

The type of the file search tool. Always `file_search`.

vector\_store\_ids: array of string

The IDs of the vector stores to search.

filters: optional [ComparisonFilter](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key, type, value }  or [CompoundFilter](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20compound_filter%20%3E%20(schema)) { filters, type }  or null

A filter to apply.

ComparisonFilter object { key, type, value }

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

string

number

boolean

array of string or number

string

number

CompoundFilter object { filters, type }

Combine multiple filters using `and` or `or`.

filters: array of [ComparisonFilter](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key, type, value }  or unknown

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

ComparisonFilter object { key, type, value }

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

string

number

boolean

array of string or number

string

number

unknown

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

Computer object { type }

A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

type: "computer"

The type of the computer tool. Always `computer`.

ComputerUsePreview object { display\_height, display\_width, environment, type }

A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

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

WebSearch object { type, external\_web\_access, filters, 2 more }

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](/api/docs/guides/tools-web-search).

type: "web\_search" or "web\_search\_2025\_08\_26"

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

"web\_search"

"web\_search\_2025\_08\_26"

external\_web\_access: optional boolean

Allow live internet access for web search. Defaults to true when omitted. When false, the web search tool runs in offline/cache-only mode and will not fetch new external content.

filters: optional object { allowed\_domains }  or null

Filters for the search.

allowed\_domains: optional array of string or null

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size: optional "low" or "medium" or "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location: optional object { city, country, region, 2 more }  or null

The approximate location of the user.

city: optional string or null

Free text input for the city of the user, e.g. `San Francisco`.

country: optional string or null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region: optional string or null

Free text input for the region of the user, e.g. `California`.

timezone: optional string or null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type: optional "approximate"

The type of location approximation. Always `approximate`.

Mcp object { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](/api/docs/guides/tools-connectors-mcp).

server\_label: string

A label for this MCP server, used to identify it in tool calls.

type: "mcp"

The type of the MCP tool. Always `mcp`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools: optional array of string or object { read\_only, tool\_names }  or null

List of allowed tool names or a filter object.

McpAllowedTools = array of string

A string array of allowed tool names

McpToolFilter object { read\_only, tool\_names }

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
about service connectors [here](/api/docs/guides/tools-connectors-mcp#connectors).

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

headers: optional map[string] or null

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval: optional object { always, never }  or "always" or "never" or null

Specify which of the MCP server’s tools require approval.

McpToolApprovalFilter object { always, never }

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

McpToolApprovalSetting = "always" or "never"

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

formaturi

tunnel\_id: optional string

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter object { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string or object { type, file\_ids, memory\_limit, network\_policy }

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

string

The container ID.

CodeInterpreterToolAuto object { type, file\_ids, memory\_limit, network\_policy }

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: "auto"

Always `auto`.

file\_ids: optional array of string

An optional list of uploaded files to make available to your code.

memory\_limit: optional "1g" or "4g" or "16g" or "64g" or null

The memory limit for the code interpreter container.

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [ContainerNetworkPolicyDisabled](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)) { type }  or [ContainerNetworkPolicyAllowlist](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

ContainerNetworkPolicyDisabled object { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

ContainerNetworkPolicyAllowlist object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: optional array of [ContainerNetworkPolicyDomainSecret](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

minLength1

maxLength10485760

type: "code\_interpreter"

The type of the code interpreter tool. Always `code_interpreter`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

ProgrammaticToolCalling object { type }

type: "programmatic\_tool\_calling"

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration object { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

The type of the image generation tool. Always `image_generation`.

action: optional "generate" or "edit" or "auto"

Whether to generate a new image or edit an existing image. Default: `auto`.

"generate"

"edit"

"auto"

background: optional "transparent" or "opaque" or "auto"

Set the background of the generated image. One of `transparent`, `opaque`,
or `auto`. `gpt-image-2.5-sunburst` and `gpt-image-2.5-flare`, including
their `2026-09-08` snapshots, support `opaque` and `transparent`
backgrounds. Transparent backgrounds are available for supported GPT Image
models. For `gpt-image-2` and `gpt-image-2-2026-04-21`, this support is in
preview. When using `transparent`, set the output format to `png` or `webp`.
Default: `auto`.

"transparent"

"opaque"

"auto"

input\_fidelity: optional "high" or "low" or null

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

model: optional string or "gpt-image-1" or "gpt-image-1-mini" or "gpt-image-1.5" or 6 more

The image generation model to use. One of `gpt-image-1`,
`gpt-image-1-mini`, `gpt-image-1.5`, `gpt-image-2`,
`gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`,
`gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`,
`gpt-image-2.5-flare-2026-09-08`, or `chatgpt-image-latest`. Default:
`gpt-image-1`.

string

"gpt-image-1" or "gpt-image-1-mini" or "gpt-image-1.5" or 6 more

The image generation model to use. One of `gpt-image-1`,
`gpt-image-1-mini`, `gpt-image-1.5`, `gpt-image-2`,
`gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`,
`gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`,
`gpt-image-2.5-flare-2026-09-08`, or `chatgpt-image-latest`. Default:
`gpt-image-1`.

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-1.5"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-2.5-sunburst"

"gpt-image-2.5-sunburst-2026-09-08"

"gpt-image-2.5-flare"

"gpt-image-2.5-flare-2026-09-08"

moderation: optional "auto" or "low"

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression: optional number

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format: optional "png" or "webp" or "jpeg"

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

"png"

"webp"

"jpeg"

partial\_images: optional number

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

quality: optional "low" or "medium" or "high" or 3 more

The quality of the generated image. The GPT image models support `low`,
`medium`, and `high`. `gpt-image-2.5-sunburst` and `gpt-image-2.5-flare`,
including their `2026-09-08` snapshots, also support `xhigh` and `max`.
Default: `auto`.

"low"

"medium"

"high"

"xhigh"

"max"

"auto"

size: optional string or "1024x1024" or "1024x1536" or "1536x1024" or "auto"

The size of the generated images. For `gpt-image-2`, `gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`, `gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`, and `gpt-image-2.5-flare-2026-09-08`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

string

"1024x1024" or "1024x1536" or "1536x1024" or "auto"

The size of the generated images. For `gpt-image-2`, `gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`, `gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`, and `gpt-image-2.5-flare-2026-09-08`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

LocalShell object { type }

A tool that allows the model to execute shell commands in a local environment.

type: "local\_shell"

The type of the local shell tool. Always `local_shell`.

Shell object { type, allowed\_callers, environment }

A tool that allows the model to execute shell commands.

type: "shell"

The type of the shell tool. Always `shell`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

environment: optional [ContainerAuto](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  or [LocalEnvironment](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20local_environment%20%3E%20(schema)) { type, skills }  or [ContainerReference](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_reference%20%3E%20(schema)) { container\_id, type }  or null

ContainerAuto object { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

Automatically creates a container for this request

file\_ids: optional array of string

An optional list of uploaded files to make available to your code.

memory\_limit: optional "1g" or "4g" or "16g" or "64g" or null

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [ContainerNetworkPolicyDisabled](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)) { type }  or [ContainerNetworkPolicyAllowlist](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

ContainerNetworkPolicyDisabled object { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

ContainerNetworkPolicyAllowlist object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: optional array of [ContainerNetworkPolicyDomainSecret](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

minLength1

maxLength10485760

skills: optional array of [SkillReference](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20skill_reference%20%3E%20(schema)) { skill\_id, type, version }  or [InlineSkill](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill%20%3E%20(schema)) { description, name, source, type }

An optional list of skills referenced by id or inline data.

SkillReference object { skill\_id, type, version }

skill\_id: string

The ID of the referenced skill.

minLength1

maxLength64

type: "skill\_reference"

References a skill created with the /v1/skills endpoint.

version: optional string

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

InlineSkill object { description, name, source, type }

description: string

The description of the skill.

The name of the skill.

source: [InlineSkillSource](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

Inline skill payload

type: "inline"

Defines an inline skill for this request.

LocalEnvironment object { type, skills }

type: "local"

Use a local computer environment.

skills: optional array of [LocalSkill](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema)) { description, name, path }

An optional list of skills.

description: string

The description of the skill.

The name of the skill.

path: string

The path to the directory containing the skill.

ContainerReference object { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

Custom object { name, type, allowed\_callers, 4 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](/api/docs/guides/function-calling#custom-tools)

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

async: optional boolean

Whether the tool response can be returned asynchronously versus immediately returned on next response creation.

defer\_loading: optional boolean

Whether this tool should be deferred and discovered via tool search.

description: optional string

Optional description of the custom tool, used to provide more context.

format: optional [CustomToolInputFormat](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))

The input format for the custom tool. Default is unconstrained text.

Namespace object { description, name, tools, type }

Groups function/custom tools under a shared namespace.

description: string

A description of the namespace shown to the model.

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: array of object { name, type, allowed\_callers, 6 more }  or object { name, type, allowed\_callers, 4 more }

The function/custom tools available inside this namespace.

Function object { name, type, allowed\_callers, 6 more }

minLength1

maxLength128

type: "function"

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

async: optional boolean

Whether the tool response can be returned asynchronously versus immediately returned on next response creation.

defer\_loading: optional boolean

Whether this function should be deferred and discovered via tool search.

description: optional string or null

output\_schema: optional map[unknown] or null

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters: optional unknown or null

strict: optional boolean or null

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

Custom object { name, type, allowed\_callers, 4 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](/api/docs/guides/function-calling#custom-tools)

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

async: optional boolean

Whether the tool response can be returned asynchronously versus immediately returned on next response creation.

defer\_loading: optional boolean

Whether this tool should be deferred and discovered via tool search.

description: optional string

Optional description of the custom tool, used to provide more context.

format: optional [CustomToolInputFormat](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))

The input format for the custom tool. Default is unconstrained text.

type: "namespace"

The type of the tool. Always `namespace`.

ToolSearch object { type, description, execution, parameters }

Hosted or BYOT tool search configuration for deferred tools.

type: "tool\_search"

The type of the tool. Always `tool_search`.

description: optional string or null

Description shown to the model for a client-executed tool search tool.

execution: optional "server" or "client"

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters: optional unknown or null

Parameter schema for a client-executed tool search tool.

WebSearchPreview object { type, search\_content\_types, search\_context\_size, user\_location }

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](/api/docs/guides/tools-web-search).

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

user\_location: optional object { type, city, country, 2 more }  or null

The user’s location.

type: "approximate"

The type of location approximation. Always `approximate`.

city: optional string or null

Free text input for the city of the user, e.g. `San Francisco`.

country: optional string or null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region: optional string or null

Free text input for the region of the user, e.g. `California`.

timezone: optional string or null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

ApplyPatch object { type, allowed\_callers }

Allows the assistant to create, delete, or update files using unified diffs.

type: "apply\_patch"

The type of the tool. Always `apply_patch`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

type: "tool\_search\_output"

The item type. Always `tool_search_output`.

id: optional string or null

The unique ID of this tool search output.

call\_id: optional string or null

The unique ID of the tool search call generated by the model.

minLength1

maxLength64

execution: optional "server" or "client"

Whether tool search was executed by the server or by the client.

"server"

"client"

status: optional "in\_progress" or "completed" or "incomplete" or null

The status of the tool search output.

"in\_progress"

"completed"

"incomplete"

AdditionalTools object { role, tools, type, id }

role: "developer"

The role that provided the additional tools. Only `developer` is supported.

tools: array of object { name, parameters, strict, 6 more }  or object { type, vector\_store\_ids, filters, 2 more }  or object { type }  or 13 more

A list of additional tools made available at this item.

Function object { name, parameters, strict, 6 more }

Defines a function in your own code the model can choose to call. Learn more about [function calling](/api/docs/guides/function-calling).

The name of the function to call.

parameters: map[unknown] or null

A JSON schema object describing the parameters of the function.

strict: boolean or null

Whether strict parameter validation is enforced for this function tool.

type: "function"

The type of the function tool. Always `function`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

async: optional boolean

defer\_loading: optional boolean

Whether this function is deferred and loaded via tool search.

description: optional string or null

A description of the function. Used by the model to determine whether or not to call the function.

output\_schema: optional map[unknown] or null

A JSON schema object describing the JSON value encoded in string outputs for this function.

FileSearch object { type, vector\_store\_ids, filters, 2 more }

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](/api/docs/guides/tools-file-search).

type: "file\_search"

The type of the file search tool. Always `file_search`.

vector\_store\_ids: array of string

The IDs of the vector stores to search.

filters: optional [ComparisonFilter](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key, type, value }  or [CompoundFilter](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20compound_filter%20%3E%20(schema)) { filters, type }  or null

A filter to apply.

ComparisonFilter object { key, type, value }

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

string

number

boolean

array of string or number

string

number

CompoundFilter object { filters, type }

Combine multiple filters using `and` or `or`.

filters: array of [ComparisonFilter](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key, type, value }  or unknown

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

ComparisonFilter object { key, type, value }

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

string

number

boolean

array of string or number

string

number

unknown

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

Computer object { type }

A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

type: "computer"

The type of the computer tool. Always `computer`.

ComputerUsePreview object { display\_height, display\_width, environment, type }

A tool that controls a virtual computer. Learn more about the [computer tool](/api/docs/guides/tools-computer-use).

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

WebSearch object { type, external\_web\_access, filters, 2 more }

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](/api/docs/guides/tools-web-search).

type: "web\_search" or "web\_search\_2025\_08\_26"

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

"web\_search"

"web\_search\_2025\_08\_26"

external\_web\_access: optional boolean

Allow live internet access for web search. Defaults to true when omitted. When false, the web search tool runs in offline/cache-only mode and will not fetch new external content.

filters: optional object { allowed\_domains }  or null

Filters for the search.

allowed\_domains: optional array of string or null

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size: optional "low" or "medium" or "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

"low"

"medium"

"high"

user\_location: optional object { city, country, region, 2 more }  or null

The approximate location of the user.

city: optional string or null

Free text input for the city of the user, e.g. `San Francisco`.

country: optional string or null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region: optional string or null

Free text input for the region of the user, e.g. `California`.

timezone: optional string or null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type: optional "approximate"

The type of location approximation. Always `approximate`.

Mcp object { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](/api/docs/guides/tools-connectors-mcp).

server\_label: string

A label for this MCP server, used to identify it in tool calls.

type: "mcp"

The type of the MCP tool. Always `mcp`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

allowed\_tools: optional array of string or object { read\_only, tool\_names }  or null

List of allowed tool names or a filter object.

McpAllowedTools = array of string

A string array of allowed tool names

McpToolFilter object { read\_only, tool\_names }

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
about service connectors [here](/api/docs/guides/tools-connectors-mcp#connectors).

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

headers: optional map[string] or null

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval: optional object { always, never }  or "always" or "never" or null

Specify which of the MCP server’s tools require approval.

McpToolApprovalFilter object { always, never }

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

McpToolApprovalSetting = "always" or "never"

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

formaturi

tunnel\_id: optional string

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter object { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string or object { type, file\_ids, memory\_limit, network\_policy }

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

string

The container ID.

CodeInterpreterToolAuto object { type, file\_ids, memory\_limit, network\_policy }

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: "auto"

Always `auto`.

file\_ids: optional array of string

An optional list of uploaded files to make available to your code.

memory\_limit: optional "1g" or "4g" or "16g" or "64g" or null

The memory limit for the code interpreter container.

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [ContainerNetworkPolicyDisabled](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)) { type }  or [ContainerNetworkPolicyAllowlist](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

ContainerNetworkPolicyDisabled object { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

ContainerNetworkPolicyAllowlist object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: optional array of [ContainerNetworkPolicyDomainSecret](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

minLength1

maxLength10485760

type: "code\_interpreter"

The type of the code interpreter tool. Always `code_interpreter`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

ProgrammaticToolCalling object { type }

type: "programmatic\_tool\_calling"

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration object { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

The type of the image generation tool. Always `image_generation`.

action: optional "generate" or "edit" or "auto"

Whether to generate a new image or edit an existing image. Default: `auto`.

"generate"

"edit"

"auto"

background: optional "transparent" or "opaque" or "auto"

Set the background of the generated image. One of `transparent`, `opaque`,
or `auto`. `gpt-image-2.5-sunburst` and `gpt-image-2.5-flare`, including
their `2026-09-08` snapshots, support `opaque` and `transparent`
backgrounds. Transparent backgrounds are available for supported GPT Image
models. For `gpt-image-2` and `gpt-image-2-2026-04-21`, this support is in
preview. When using `transparent`, set the output format to `png` or `webp`.
Default: `auto`.

"transparent"

"opaque"

"auto"

input\_fidelity: optional "high" or "low" or null

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

model: optional string or "gpt-image-1" or "gpt-image-1-mini" or "gpt-image-1.5" or 6 more

The image generation model to use. One of `gpt-image-1`,
`gpt-image-1-mini`, `gpt-image-1.5`, `gpt-image-2`,
`gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`,
`gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`,
`gpt-image-2.5-flare-2026-09-08`, or `chatgpt-image-latest`. Default:
`gpt-image-1`.

string

"gpt-image-1" or "gpt-image-1-mini" or "gpt-image-1.5" or 6 more

The image generation model to use. One of `gpt-image-1`,
`gpt-image-1-mini`, `gpt-image-1.5`, `gpt-image-2`,
`gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`,
`gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`,
`gpt-image-2.5-flare-2026-09-08`, or `chatgpt-image-latest`. Default:
`gpt-image-1`.

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-1.5"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-2.5-sunburst"

"gpt-image-2.5-sunburst-2026-09-08"

"gpt-image-2.5-flare"

"gpt-image-2.5-flare-2026-09-08"

moderation: optional "auto" or "low"

Moderation level for the generated image. Default: `auto`.

"auto"

"low"

output\_compression: optional number

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format: optional "png" or "webp" or "jpeg"

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

"png"

"webp"

"jpeg"

partial\_images: optional number

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

quality: optional "low" or "medium" or "high" or 3 more

The quality of the generated image. The GPT image models support `low`,
`medium`, and `high`. `gpt-image-2.5-sunburst` and `gpt-image-2.5-flare`,
including their `2026-09-08` snapshots, also support `xhigh` and `max`.
Default: `auto`.

"low"

"medium"

"high"

"xhigh"

"max"

"auto"

size: optional string or "1024x1024" or "1024x1536" or "1536x1024" or "auto"

The size of the generated images. For `gpt-image-2`, `gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`, `gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`, and `gpt-image-2.5-flare-2026-09-08`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

string

"1024x1024" or "1024x1536" or "1536x1024" or "auto"

The size of the generated images. For `gpt-image-2`, `gpt-image-2-2026-04-21`, `gpt-image-2.5-sunburst`, `gpt-image-2.5-sunburst-2026-09-08`, `gpt-image-2.5-flare`, and `gpt-image-2.5-flare-2026-09-08`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

LocalShell object { type }

A tool that allows the model to execute shell commands in a local environment.

type: "local\_shell"

The type of the local shell tool. Always `local_shell`.

Shell object { type, allowed\_callers, environment }

A tool that allows the model to execute shell commands.

type: "shell"

The type of the shell tool. Always `shell`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

environment: optional [ContainerAuto](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  or [LocalEnvironment](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20local_environment%20%3E%20(schema)) { type, skills }  or [ContainerReference](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_reference%20%3E%20(schema)) { container\_id, type }  or null

ContainerAuto object { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

Automatically creates a container for this request

file\_ids: optional array of string

An optional list of uploaded files to make available to your code.

memory\_limit: optional "1g" or "4g" or "16g" or "64g" or null

The memory limit for the container.

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [ContainerNetworkPolicyDisabled](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)) { type }  or [ContainerNetworkPolicyAllowlist](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

ContainerNetworkPolicyDisabled object { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

ContainerNetworkPolicyAllowlist object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: optional array of [ContainerNetworkPolicyDomainSecret](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

minLength1

maxLength10485760

skills: optional array of [SkillReference](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20skill_reference%20%3E%20(schema)) { skill\_id, type, version }  or [InlineSkill](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill%20%3E%20(schema)) { description, name, source, type }

An optional list of skills referenced by id or inline data.

SkillReference object { skill\_id, type, version }

skill\_id: string

The ID of the referenced skill.

minLength1

maxLength64

type: "skill\_reference"

References a skill created with the /v1/skills endpoint.

version: optional string

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

InlineSkill object { description, name, source, type }

description: string

The description of the skill.

The name of the skill.

source: [InlineSkillSource](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

Inline skill payload

type: "inline"

Defines an inline skill for this request.

LocalEnvironment object { type, skills }

type: "local"

Use a local computer environment.

skills: optional array of [LocalSkill](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema)) { description, name, path }

An optional list of skills.

description: string

The description of the skill.

The name of the skill.

path: string

The path to the directory containing the skill.

ContainerReference object { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

Custom object { name, type, allowed\_callers, 4 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](/api/docs/guides/function-calling#custom-tools)

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

async: optional boolean

Whether the tool response can be returned asynchronously versus immediately returned on next response creation.

defer\_loading: optional boolean

Whether this tool should be deferred and discovered via tool search.

description: optional string

Optional description of the custom tool, used to provide more context.

format: optional [CustomToolInputFormat](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))

The input format for the custom tool. Default is unconstrained text.

Namespace object { description, name, tools, type }

Groups function/custom tools under a shared namespace.

description: string

A description of the namespace shown to the model.

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: array of object { name, type, allowed\_callers, 6 more }  or object { name, type, allowed\_callers, 4 more }

The function/custom tools available inside this namespace.

Function object { name, type, allowed\_callers, 6 more }

minLength1

maxLength128

type: "function"

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

async: optional boolean

Whether the tool response can be returned asynchronously versus immediately returned on next response creation.

defer\_loading: optional boolean

Whether this function should be deferred and discovered via tool search.

description: optional string or null

output\_schema: optional map[unknown] or null

A JSON Schema describing the JSON value encoded in string outputs for this function tool. This does not describe content-array outputs.

parameters: optional unknown or null

strict: optional boolean or null

Whether to enforce strict parameter validation. If omitted, Responses attempts to use strict validation when the schema is compatible, and falls back to non-strict validation otherwise.

Custom object { name, type, allowed\_callers, 4 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](/api/docs/guides/function-calling#custom-tools)

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

async: optional boolean

Whether the tool response can be returned asynchronously versus immediately returned on next response creation.

defer\_loading: optional boolean

Whether this tool should be deferred and discovered via tool search.

description: optional string

Optional description of the custom tool, used to provide more context.

format: optional [CustomToolInputFormat](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))

The input format for the custom tool. Default is unconstrained text.

type: "namespace"

The type of the tool. Always `namespace`.

ToolSearch object { type, description, execution, parameters }

Hosted or BYOT tool search configuration for deferred tools.

type: "tool\_search"

The type of the tool. Always `tool_search`.

description: optional string or null

Description shown to the model for a client-executed tool search tool.

execution: optional "server" or "client"

Whether tool search is executed by the server or by the client.

"server"

"client"

parameters: optional unknown or null

Parameter schema for a client-executed tool search tool.

WebSearchPreview object { type, search\_content\_types, search\_context\_size, user\_location }

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](/api/docs/guides/tools-web-search).

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

user\_location: optional object { type, city, country, 2 more }  or null

The user’s location.

type: "approximate"

The type of location approximation. Always `approximate`.

city: optional string or null

Free text input for the city of the user, e.g. `San Francisco`.

country: optional string or null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region: optional string or null

Free text input for the region of the user, e.g. `California`.

timezone: optional string or null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

ApplyPatch object { type, allowed\_callers }

Allows the assistant to create, delete, or update files using unified diffs.

type: "apply\_patch"

The type of the tool. Always `apply_patch`.

allowed\_callers: optional array of "direct" or "programmatic" or null

The tool invocation context(s).

"direct"

"programmatic"

type: "additional\_tools"

The item type. Always `additional_tools`.

id: optional string or null

The unique ID of this additional tools item.

ConfigurationUpdate object { type, id, reasoning }

An update to the conversation’s response configuration. The configuration
remains in effect for subsequent responses until it is replaced by another
configuration update.

type: "configuration\_update"

The item type. Always `configuration_update`.

id: optional string or null

The unique ID of the configuration update item.

reasoning: optional object { effort }

Updates to reasoning configuration. Only effort is supported.

effort: optional [ReasoningEffort](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)) or null

The reasoning effort to use for subsequent responses until another
configuration update replaces it.

Reasoning object { id, summary, type, 3 more }

A description of the chain of thought used by a reasoning model while generating
a response. Be sure to include these items in your `input` to the Responses API
for subsequent turns of a conversation if you are manually
[managing context](/api/docs/guides/conversation-state).

The unique identifier of the reasoning content.

summary: array of [SummaryTextContent](/api/reference/resources/conversations#(resource)%20conversations%20%3E%20(model)%20summary_text_content%20%3E%20(schema)) { text, type }

Reasoning summary content.

text: string

A summary of the reasoning output from the model so far.

type: "summary\_text"

The type of the object. Always `summary_text`.

type: "reasoning"

The type of the object. Always `reasoning`.

content: optional array of object { text, type }

Reasoning text content.

text: string

The reasoning text from the model.

type: "reasoning\_text"

The type of the reasoning text. Always `reasoning_text`.

encrypted\_content: optional string or null

The encrypted content of the reasoning item. This is populated by default
for reasoning items returned by `POST /v1/responses` and WebSocket
`response.create` requests.

When streaming, use the completed reasoning item and its
`encrypted_content` from the `response.output_item.done` event in
subsequent requests. The `encrypted_content` in
`response.output_item.added` may be incomplete. This is especially
important when `store` is `false` or when using Zero Data Retention.

status: optional "in\_progress" or "completed" or "incomplete"

The status of the item. One of `in_progress`, `completed`, or
`incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

Compaction object { encrypted\_content, type, id }

A compaction item generated by the [`v1/responses/compact` API](/api/reference/resources/responses/methods/compact).

encrypted\_content: string

The encrypted content of the compaction summary.

maxLength20971520

type: "compaction"

The type of the item. Always `compaction`.

id: optional string or null

The ID of the compaction item.

ImageGenerationCall object { id, result, status, 7 more }

An image generation request made by the model.

The unique ID of the image generation call.

result: string or null

The generated image encoded in base64.

status: "in\_progress" or "completed" or "generating" or "failed"

The status of the image generation call.

"in\_progress"

"completed"

"generating"

"failed"

type: "image\_generation\_call"

The type of the image generation call. Always `image_generation_call`.

action: optional "generate" or "edit" or "auto" or null

The action used for image generation.

"generate"

"edit"

"auto"

background: optional "transparent" or "opaque" or "auto" or null

The background setting used for generation.

"transparent"

"opaque"

"auto"

output\_format: optional "png" or "webp" or "jpeg" or null

The output format used for generation.

"png"

"webp"

"jpeg"

quality: optional "low" or "medium" or "high" or 3 more or null

The quality of the image generated by the image generation tool call. One of `low`, `medium`, `high`, `xhigh`, `max`, or `auto`.

"low"

"medium"

"high"

"xhigh"

"max"

"auto"

revised\_prompt: optional string or null

The prompt that was used after any model prompt rewriting.

size: optional string or "1024x1024" or "1024x1536" or "1536x1024" or null

The image dimensions as a `WIDTHxHEIGHT` string, for example `1536x864`.

string

"1024x1024" or "1024x1536" or "1536x1024"

The image dimensions as a `WIDTHxHEIGHT` string, for example `1536x864`.

"1024x1024"

"1024x1536"

"1536x1024"

CodeInterpreterCall object { id, code, container\_id, 3 more }

A tool call to run code.

The unique ID of the code interpreter tool call.

code: string or null

The code to run, or null if not available.

container\_id: string

The ID of the container used to run the code.

outputs: array of object { logs, type }  or object { type, url }  or null

The outputs generated by the code interpreter, such as logs or images.
Can be null if no outputs are available.

Logs object { logs, type }

The logs output from the code interpreter.

logs: string

The logs output from the code interpreter.

type: "logs"

The type of the output. Always `logs`.

Image object { type, url }

The image output from the code interpreter.

type: "image"

The type of the output. Always `image`.

url: string

The URL of the image output from the code interpreter.

formaturi

status: "in\_progress" or "completed" or "incomplete" or 2 more

The status of the code interpreter tool call. Valid values are `in_progress`, `completed`, `incomplete`, `interpreting`, and `failed`.

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: "code\_interpreter\_call"

The type of the code interpreter tool call. Always `code_interpreter_call`.

LocalShellCall object { id, action, call\_id, 2 more }

A tool call to run a command on the local shell.

The unique ID of the local shell call.

action: object { command, env, type, 3 more }

Execute a shell command on the server.

command: array of string

The command to run.

env: map[string]

Environment variables to set for the command.

type: "exec"

The type of the local shell action. Always `exec`.

timeout\_ms: optional number or null

Optional timeout in milliseconds for the command.

user: optional string or null

Optional user to run the command as.

working\_directory: optional string or null

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

LocalShellCallOutput object { id, output, type, status }

The output of a local shell tool call.

The unique ID of the local shell tool call generated by the model.

output: string

A JSON string of the output of the local shell tool call.

type: "local\_shell\_call\_output"

The type of the local shell tool call output. Always `local_shell_call_output`.

status: optional "in\_progress" or "completed" or "incomplete" or null

The status of the item. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

ShellCall object { action, call\_id, type, 4 more }

A tool representing a request to execute one or more shell commands.

action: object { commands, max\_output\_length, timeout\_ms }

The shell commands and limits that describe how to run the tool call.

commands: array of string

Ordered shell commands for the execution environment to run.

max\_output\_length: optional number or null

Maximum number of UTF-8 characters to capture from combined stdout and stderr output.

timeout\_ms: optional number or null

Maximum wall-clock time in milliseconds to allow the shell commands to run.

call\_id: string

The unique ID of the shell tool call generated by the model.

minLength1

maxLength64

type: "shell\_call"

The type of the item. Always `shell_call`.

id: optional string or null

The unique ID of the shell tool call. Populated when this item is returned via API.

caller: optional object { type }  or object { caller\_id, type }  or null

The execution context that produced this tool call.

Direct object { type }

type: "direct"

The caller type. Always `direct`.

Program object { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

minLength1

maxLength64

type: "program"

The caller type. Always `program`.

environment: optional [LocalEnvironment](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20local_environment%20%3E%20(schema)) { type, skills }  or [ContainerReference](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20container_reference%20%3E%20(schema)) { container\_id, type }  or null

The environment to execute the shell commands in.

LocalEnvironment object { type, skills }

type: "local"

Use a local computer environment.

skills: optional array of [LocalSkill](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema)) { description, name, path }

An optional list of skills.

description: string

The description of the skill.

The name of the skill.

path: string

The path to the directory containing the skill.

ContainerReference object { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

status: optional "in\_progress" or "completed" or "incomplete" or null

The status of the shell call. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

ShellCallOutput object { call\_id, output, type, 4 more }

The streamed output items emitted by a shell tool call.

call\_id: string

The unique ID of the shell tool call generated by the model.

minLength1

maxLength64

output: array of [ResponseFunctionShellCallOutputContent](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_function_shell_call_output_content%20%3E%20(schema)) { outcome, stderr, stdout }

Captured chunks of stdout and stderr output, along with their associated outcomes.

outcome: object { type }  or object { exit\_code, type }

The exit or timeout outcome associated with this shell call.

Timeout object { type }

Indicates that the shell call exceeded its configured time limit.

type: "timeout"

The outcome type. Always `timeout`.

Exit object { exit\_code, type }

Indicates that the shell commands finished and returned an exit code.

exit\_code: number

The exit code returned by the shell process.

type: "exit"

The outcome type. Always `exit`.

stderr: string

Captured stderr output for the shell call.

maxLength10485760

stdout: string

Captured stdout output for the shell call.

maxLength10485760

type: "shell\_call\_output"

The type of the item. Always `shell_call_output`.

id: optional string or null

The unique ID of the shell tool call output. Populated when this item is returned via API.

caller: optional object { type }  or object { caller\_id, type }  or null

The execution context that produced this tool call.

Direct object { type }

type: "direct"

The caller type. Always `direct`.

Program object { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

minLength1

maxLength64

type: "program"

The caller type. Always `program`.

max\_output\_length: optional number or null

The maximum number of UTF-8 characters captured for this shell call’s combined output.

status: optional "in\_progress" or "completed" or "incomplete" or null

The status of the shell call output.

"in\_progress"

"completed"

"incomplete"

ApplyPatchCall object { call\_id, operation, status, 3 more }

A tool call representing a request to create, delete, or update files using diff patches.

call\_id: string

The unique ID of the apply patch tool call generated by the model.

minLength1

maxLength64

operation: object { diff, path, type }  or object { path, type }  or object { diff, path, type }

The specific create, delete, or update instruction for the apply\_patch tool call.

CreateFile object { diff, path, type }

Instruction for creating a new file via the apply\_patch tool.

diff: string

Unified diff content to apply when creating the file.

maxLength10485760

path: string

Path of the file to create relative to the workspace root.

minLength1

type: "create\_file"

The operation type. Always `create_file`.

DeleteFile object { path, type }

Instruction for deleting an existing file via the apply\_patch tool.

path: string

Path of the file to delete relative to the workspace root.

minLength1

type: "delete\_file"

The operation type. Always `delete_file`.

UpdateFile object { diff, path, type }

Instruction for updating an existing file via the apply\_patch tool.

diff: string

Unified diff content to apply to the existing file.

maxLength10485760

path: string

Path of the file to update relative to the workspace root.

minLength1

type: "update\_file"

The operation type. Always `update_file`.

status: "in\_progress" or "completed"

The status of the apply patch tool call. One of `in_progress` or `completed`.

"in\_progress"

"completed"

type: "apply\_patch\_call"

The type of the item. Always `apply_patch_call`.

id: optional string or null

The unique ID of the apply patch tool call. Populated when this item is returned via API.

caller: optional object { type }  or object { caller\_id, type }  or null

The execution context that produced this tool call.

Direct object { type }

type: "direct"

The caller type. Always `direct`.

Program object { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

minLength1

maxLength64

type: "program"

The caller type. Always `program`.

ApplyPatchCallOutput object { call\_id, status, type, 3 more }

The streamed output emitted by an apply patch tool call.

call\_id: string

The unique ID of the apply patch tool call generated by the model.

minLength1

maxLength64

status: "completed" or "failed"

The status of the apply patch tool call output. One of `completed` or `failed`.

"completed"

"failed"

type: "apply\_patch\_call\_output"

The type of the item. Always `apply_patch_call_output`.

id: optional string or null

The unique ID of the apply patch tool call output. Populated when this item is returned via API.

caller: optional object { type }  or object { caller\_id, type }  or null

The execution context that produced this tool call.

Direct object { type }

type: "direct"

The caller type. Always `direct`.

Program object { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

minLength1

maxLength64

type: "program"

The caller type. Always `program`.

output: optional string or null

Optional human-readable log text from the apply patch tool (e.g., patch results or errors).

maxLength10485760

McpListTools object { id, server\_label, tools, 2 more }

A list of tools available on an MCP server.

The unique ID of the list.

server\_label: string

The label of the MCP server.

tools: array of object { input\_schema, name, annotations, description }

The tools available on the server.

input\_schema: unknown

The JSON schema describing the tool’s input.

The name of the tool.

annotations: optional unknown or null

Additional annotations about the tool.

description: optional string or null

The description of the tool.

type: "mcp\_list\_tools"

The type of the item. Always `mcp_list_tools`.

error: optional string or null

Error message if the server could not list tools.

McpApprovalRequest object { id, arguments, name, 2 more }

A request for human approval of a tool invocation.

The unique ID of the approval request.

arguments: string

A JSON string of arguments for the tool.

The name of the tool to run.

server\_label: string

The label of the MCP server making the request.

type: "mcp\_approval\_request"

The type of the item. Always `mcp_approval_request`.

McpApprovalResponse object { approval\_request\_id, approve, type, 2 more }

A response to an MCP approval request.

approval\_request\_id: string

The ID of the approval request being answered.

approve: boolean

Whether the request was approved.

type: "mcp\_approval\_response"

The type of the item. Always `mcp_approval_response`.

id: optional string or null

The unique ID of the approval response

reason: optional string or null

Optional reason for the decision.

McpCall object { id, arguments, name, 6 more }

An invocation of a tool on an MCP server.

The unique ID of the tool call.

arguments: string

A JSON string of the arguments passed to the tool.

The name of the tool that was run.

server\_label: string

The label of the MCP server running the tool.

type: "mcp\_call"

The type of the item. Always `mcp_call`.

approval\_request\_id: optional string or null

Unique identifier for the MCP tool call approval request.
Include this value in a subsequent `mcp_approval_response` input to approve or reject the corresponding tool call.

error: optional [McpToolCallError](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20mcp_tool_call_error%20%3E%20(schema)) or null

The error from the tool call, if any.

output: optional string or null

The output from the tool call.

status: optional "in\_progress" or "completed" or "incomplete" or 2 more

The status of the tool call. One of `in_progress`, `completed`, `incomplete`, `calling`, or `failed`.

"in\_progress"

"completed"

"incomplete"

"calling"

"failed"

CustomToolCallOutput object { call\_id, output, type, 2 more }

The output of a custom tool call from your code, being sent back to the model.

call\_id: string

The call ID, used to map this custom tool call output to a custom tool call.

output: string or array of [ResponseInputText](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [ResponseInputImage](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  or [ResponseInputFile](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more }

The output from the custom tool call generated by your code.
Can be a string or an list of output content.

StringOutput = string

A string of the output of the custom tool call.

OutputContentList = array of [ResponseInputText](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [ResponseInputImage](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  or [ResponseInputFile](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more }

Text, image, or file output of the custom tool call.

ResponseInputText object { text, type, prompt\_cache\_breakpoint }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

prompt\_cache\_breakpoint: optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

ResponseInputImage object { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](/api/docs/guides/images-vision).

detail: [ImageDetail](/api/reference/resources/responses#(resource)%20responses%20%3E%20(model)%20image_detail%20%3E%20(schema))

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

type: "input\_image"

The type of the input item. Always `input_image`.

file\_id: optional string or null

The ID of the file to be sent to the model.

image\_url: optional string or null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

prompt\_cache\_breakpoint: optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

ResponseInputFile object { type, detail, file\_data, 4 more }

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

file\_id: optional string or null

The ID of the file to be sent to the model.

file\_url: optional string

The URL of the file to be sent to the model.

formaturi

filename: optional string

The name of the file to be sent to the model.

prompt\_cache\_breakpoint: optional object { mode }

Marks the exact end of a reusable prompt prefix. The breakpoint inherits its TTL from the request’s `prompt_cache_options.ttl`; the boundary is not rounded to a token block.

mode: "explicit"

The breakpoint mode. Always `explicit`.

type: "custom\_tool\_call\_output"

The type of the custom tool call output. Always `custom_tool_call_output`.

id: optional string

The unique ID of the custom tool call output in the OpenAI platform.

caller: optional object { type }  or object { caller\_id, type }  or null

The execution context that produced this tool call.

Direct object { type }

type: "direct"

The caller type. Always `direct`.

Program object { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

minLength1

maxLength64

type: "program"

The caller type. Always `program`.

CustomToolCall object { call\_id, input, name, 5 more }

A call to a custom tool created by the model.

call\_id: string

An identifier used to map this custom tool call to a tool call output.

input: string

The input for the custom tool call generated by the model.

The name of the custom tool being called.

type: "custom\_tool\_call"

The type of the custom tool call. Always `custom_tool_call`.

id: optional string

The unique ID of the custom tool call in the OpenAI platform.

async: optional boolean

Whether the custom tool call runs asynchronously.

caller: optional object { type }  or object { caller\_id, type }  or null

The execution context that produced this tool call.

Direct object { type }

type: "direct"

Program object { caller\_id, type }

caller\_id: string

The call ID of the program item that produced this tool call.

type: "program"

namespace: optional string

The namespace of the custom tool being called.

CompactionTrigger object { type, id }

Compacts the current context. Must be the final input item.

type: "compaction\_trigger"

The type of the item. Always `compaction_trigger`.

id: optional string or null

The unique ID of this compaction trigger.

ItemReference object { id, type }

An internal identifier for an item to reference.

The ID of the item to reference.

type: optional "item\_reference" or null

The type of item to reference. Always `item_reference`.

Program object { id, call\_id, code, 2 more }

The unique ID of this program item.

call\_id: string

The stable call ID of the program item.

minLength1

maxLength64

code: string

The JavaScript source executed by programmatic tool calling.

maxLength10485760

fingerprint: string

Opaque program replay fingerprint that must be round-tripped.

maxLength10485760

type: "program"

The item type. Always `program`.

ProgramOutput object { id, call\_id, result, 2 more }

The unique ID of this program output item.

call\_id: string

The call ID of the program item.

minLength1

maxLength64

result: string

The result produced by the program item.

maxLength10485760

status: "completed" or "incomplete"

The terminal status of the program output.

"completed"

"incomplete"

type: "program\_output"

The item type. Always `program_output`.

type: "response.item.create"

The Live client event type. Always `response.item.create`.

event\_id: optional string or null

Optional client identifier for correlating this command with a server event’s client\_event\_id or error.client\_event\_id.

maxLength512

ResponseCreateEvent object { type, event\_id }

Request a response from the Live session’s Responses backend, or continue a delegated response waiting for tool results. Requires Responses delegation.

type: "response.create"

The Live client event type. Always `response.create`.

event\_id: optional string or null

Optional client identifier for correlating this command with a server event’s client\_event\_id or error.client\_event\_id.

maxLength512

SessionCloseEvent object { type, event\_id }

Request that the Live session close. The terminal `session.closed` event contains the close reason and final usage.

type: "session.close"

The Live client event type. Always `session.close`.

event\_id: optional string or null

Optional client identifier for correlating this command with a server event’s client\_event\_id or error.client\_event\_id.

maxLength512

ForkServerEvent = [SessionStartedEvent](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20session_started_event%20%3E%20(schema)) { event\_id, session, type, client\_event\_id }  or [SessionUpdatedEvent](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20session_updated_event%20%3E%20(schema)) { event\_id, session, type, client\_event\_id }  or [InputAudioMutedEvent](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20input_audio_muted_event%20%3E%20(schema)) { event\_id, type, client\_event\_id }  or 19 more

Server events for Live. Response lifecycle events are wrapped inside response.event; dispatch the nested event by its full type and tolerate new response event types. Follow the [Live prompting guide](https://developers.openai.com/api/docs/guides/live-prompting) when designing the conversation and delegation policy.

SessionStartedEvent object { event\_id, session, type, client\_event\_id }

Returned when a Live session has started. Contains the resolved session configuration, including server defaults.

event\_id: string

The unique ID of the Live server event.

session: [SessionResource](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20session_resource%20%3E%20(schema)) { id, expires\_at, model, 7 more }

The resolved Live session configuration and server-assigned session metadata.

type: "session.started"

The event type, always `session.started`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

SessionUpdatedEvent object { event\_id, session, type, client\_event\_id }

Returned when a Live session update is accepted. Contains the resolved session configuration after the update.

event\_id: string

The unique ID of the Live server event.

session: [SessionResource](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20session_resource%20%3E%20(schema)) { id, expires\_at, model, 7 more }

The resolved Live session configuration and server-assigned session metadata.

type: "session.updated"

The event type, always `session.updated`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

InputAudioMutedEvent object { event\_id, type, client\_event\_id }

Returned when a session.input\_audio.mute command is accepted. Input audio is no longer sent to the model; sideband audio reflection continues.

event\_id: string

The unique ID of the Live server event.

type: "session.input\_audio.muted"

The event type, always `session.input_audio.muted`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

InputAudioUnmutedEvent object { event\_id, type, client\_event\_id }

Returned when a session.input\_audio.unmute command is accepted. Input audio is sent to the model again.

event\_id: string

The unique ID of the Live server event.

type: "session.input\_audio.unmuted"

The event type, always `session.input_audio.unmuted`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

InstructionsAppendedEvent object { end\_ms, event\_id, start\_ms, 2 more }

Returned when a session.instructions.append command is accepted into the Live session timeline. Acknowledges the appended instructions without guaranteeing that the model has acted on them.

end\_ms: number

The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start\_ms.

event\_id: string

The unique ID of the Live server event.

start\_ms: number

The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

type: "session.instructions.appended"

The event type, always `session.instructions.appended`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

ThinkingAppendedEvent object { end\_ms, event\_id, start\_ms, 2 more }

Returned when a session.thinking.append command is accepted into the Live session timeline. Acknowledges the added reasoning context without guaranteeing any spoken output.

end\_ms: number

The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start\_ms.

event\_id: string

The unique ID of the Live server event.

start\_ms: number

The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

type: "session.thinking.appended"

The event type, always `session.thinking.appended`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

CommentaryAppendedEvent object { end\_ms, event\_id, start\_ms, 2 more }

Returned when a session.commentary.append command is accepted into the Live session timeline. Acknowledges the added commentary without guaranteeing exact wording or completed audio playback.

end\_ms: number

The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start\_ms.

event\_id: string

The unique ID of the Live server event.

start\_ms: number

The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

type: "session.commentary.appended"

The event type, always `session.commentary.appended`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

SessionInputAudioAppend object { audio, type }

Input audio received from the primary transport and reflected to a Live sideband connection before model-input muting.

audio: string

Base64-encoded raw mono PCM16LE at 24 kHz received from the primary transport, reflected to the sideband before model-input muting. This server event uses the same audio key as the client command, but is not an acknowledgment of it.

type: "session.input\_audio.append"

The event type, always `session.input_audio.append`.

OutputAudioDeltaEvent object { delta, type, end\_ms, start\_ms }

An audio chunk generated by the Live model. Decode and play primary WebSocket chunks in delivery order using the configured session audio format. Sideband connections receive reflected output audio with timestamps.

delta: string

Base64-encoded raw audio. Primary WebSocket events use the session’s configured format; reflected sideband events use mono PCM16LE at 24 kHz.

type: "session.output\_audio.delta"

The event type, always `session.output_audio.delta`.

end\_ms: optional number

Exclusive session-relative end in milliseconds. Required on reflected sideband events; omitted on the primary WebSocket. Dropped output frames leave gaps between reflected ranges.

start\_ms: optional number

Inclusive session-relative start in milliseconds. Required on reflected sideband events; omitted on the primary WebSocket.

InputTranscriptDeltaEvent object { delta, end\_ms, event\_id, 3 more }

A transcript fragment for user input audio in the Live session. Accumulate fragments in delivery order; these events do not define complete turns or include a transcript-done event.

delta: string

The transcript text fragment for the audio in this time range. Append fragments in delivery order to build the transcript.

end\_ms: number

The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start\_ms.

event\_id: string

The unique ID of the Live server event.

start\_ms: number

The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

type: "session.input\_transcript.delta"

The event type, always `session.input_transcript.delta`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

OutputTranscriptDeltaEvent object { delta, end\_ms, event\_id, 3 more }

A transcript fragment for assistant output audio in the Live session. Accumulate fragments in delivery order; these events do not define complete turns or include a transcript-done event.

delta: string

The transcript text fragment for the audio in this time range. Append fragments in delivery order to build the transcript.

end\_ms: number

The end of this event on the Live session timeline, in milliseconds from the beginning of the session. For appended context, this can equal start\_ms.

event\_id: string

The unique ID of the Live server event.

start\_ms: number

The start of this event on the Live session timeline, in milliseconds from the beginning of the session.

type: "session.output\_transcript.delta"

The event type, always `session.output_transcript.delta`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

DelegationCreatedEvent object { delegation, event\_id, offset\_ms, 2 more }

Returned when the Live model delegates work to your application or a Responses backend. Contains delegation metadata and the position on the session timeline where the work was delegated.

delegation: object { id, target, type, response\_id }

The delegated work identifier and destination. This object contains metadata, not the task text.

The unique ID of the delegation. Use this as delegation\_id when replying to client-owned work or correlating Responses events.

target: "client" or "responses"

Where the Live model delegated the work: `client` for your application, or `responses` for the configured Responses backend.

"client" or "responses"

Where the Live model delegated the work: `client` for your application, or `responses` for the configured Responses backend.

"client"

"responses"

type: "delegation"

The object type, always `delegation`.

response\_id: optional string

The ID of the Responses API response associated with a Responses delegation. Omitted for client delegations.

event\_id: string

The unique ID of the Live server event.

offset\_ms: number

The position on the Live session timeline where the delegation was created, in milliseconds from the beginning of the session.

type: "session.delegation.created"

The event type, always `session.delegation.created`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

ResponseEvent object { event, event\_id, type, 2 more }

A streaming Responses API event from a backend delegated to by the Live session. Use the outer delegation\_id to associate the nested stream with its Live delegation.

event: map[unknown]

The nested Responses streaming event. Dispatch on its type field. Response lifecycle snapshots omit input and clear instructions, tools, and output to keep messages small; consume granular output events for the generated content.

event\_id: string

The unique ID of the Live server event.

type: "response.event"

The event type, always `response.event`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

delegation\_id: optional string or null

The Live delegation associated with the nested Responses event. May be null or omitted when the event cannot be correlated with a delegation.

SessionUsageUpdatedEvent object { event\_id, type, usage, 2 more }

Reports cumulative Live audio usage and, when available, the most recent context-window usage. Delegated Responses token usage is reported separately in response.event events.

event\_id: string

The unique ID of the Live server event.

type: "session.usage.updated"

The event type, always `session.usage.updated`.

usage: [SessionUsage](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20session_usage%20%3E%20(schema)) { seconds }

The cumulative Live audio usage so far.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

context\_window: optional object { usage\_ratio }

The latest measured Live context-window usage. Omitted when the context limit is unknown.

usage\_ratio: number

The latest active context token count divided by the Live model context limit. Can decrease after compaction and may lag between measured audio frames.

SessionClosedEvent object { event\_id, reason, session, 3 more }

Returned after the Live session finishes finalizing, with the close reason, final session snapshot, and cumulative audio usage. A connection closing without this event does not confirm successful finalization.

event\_id: string

The unique ID of the Live server event.

reason: "close\_requested" or "expired" or "content" or 2 more

Why the Live session ended: `close_requested` for an application close or hangup request, `expired` for the session duration limit, `content` for a safety filter, `remote_hangup` for a graceful remote disconnect, or `connection_lost` for an unexpected primary or upstream disconnection.

"close\_requested" or "expired" or "content" or 2 more

Why the Live session ended: `close_requested` for an application close or hangup request, `expired` for the session duration limit, `content` for a safety filter, `remote_hangup` for a graceful remote disconnect, or `connection_lost` for an unexpected primary or upstream disconnection.

"close\_requested"

"expired"

"content"

"remote\_hangup"

"connection\_lost"

session: [SessionResource](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20session_resource%20%3E%20(schema)) { id, expires\_at, model, 7 more }

The resolved Live session configuration and server-assigned session metadata.

type: "session.closed"

The event type, always `session.closed`.

usage: [SessionUsage](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20session_usage%20%3E%20(schema)) { seconds }

The final cumulative Live audio usage after session finalization.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

ErrorEvent object { error, event\_id, type, client\_event\_id }

Reports an error in the Live session, such as an invalid client command. Use error.client\_event\_id, when present, to identify the command that caused the error.

error: [Error](/api/reference/resources/live#(resource)%20live%20%3E%20(model)%20error%20%3E%20(schema)) { code, message, type, 2 more }

Details of the Live error and the client command that caused it, when known.

event\_id: string

The unique ID of the Live server event.

type: "error"

The event type, always `error`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

InfoEvent object { code, event\_id, message, 2 more }

An informational notice about the Live session, such as the event permissions applied to a frontend data channel.

code: string

A machine-readable code for the notice, such as `data_channel_permissions`.

event\_id: string

The unique ID of the Live server event.

message: string

A human-readable explanation of the Live session notice.

type: "info"

The event type, always `info`.

client\_event\_id: optional string

The event\_id of the client command associated with this server event, when supplied.

TransportDtmfReceived object { event, event\_id, type }

A SIP DTMF keypress received from the caller. Delivered only to sideband observers.

event: string

minLength1

maxLength1

event\_id: string

type: "transport.dtmf.received"

TransportDtmfSend object { event, event\_id, type }

A SIP DTMF keypress successfully sent by the hosted tool. Delivered only to sideband observers; this is not a client command.

event: string

minLength1

maxLength1

event\_id: string

type: "transport.dtmf.send"

TransportRinging object { event\_id, session\_id, type }

The outbound SIP provider leg is ringing or providing early media. Delivered only to sideband observers.

event\_id: string

session\_id: string

The canonical Live session ID.

type: "transport.ringing"

TransportAnswered object { event\_id, session\_id, type }

The outbound SIP provider leg answered and media is established. Delivered only to sideband observers.

event\_id: string

session\_id: string

The canonical Live session ID.

type: "transport.answered"

TransportFailed object { error, event\_id, session\_id, type }

An asynchronous outbound SIP setup failure. Delivered only to sideband observers.

error: object { code, message, type, param }

code: string

The call setup failure code.

message: string

type: "call\_error"

param: optional string

The parameter related to the error, if any. Empty when no parameter applies.

event\_id: string

session\_id: string

The canonical Live session ID.

type: "transport.failed"

#### LiveSessions

##### [Accept call](/api/reference/resources/live/subresources/sessions/methods/accept)

POST/live/sessions/{session\_id}/accept

##### [Download recording](/api/reference/resources/live/subresources/sessions/methods/download_recording)

GET/live/sessions/{session\_id}/content

##### [Fork session](/api/reference/resources/live/subresources/sessions/methods/fork)

POST/live/sessions/{session\_id}/fork

##### [Hang up session](/api/reference/resources/live/subresources/sessions/methods/hangup)

POST/live/sessions/{session\_id}/hangup

##### [Transfer call](/api/reference/resources/live/subresources/sessions/methods/refer)

POST/live/sessions/{session\_id}/refer

##### [Reject call](/api/reference/resources/live/subresources/sessions/methods/reject)

POST/live/sessions/{session\_id}/reject

##### ModelsExpand Collapse

SessionForkResponse object { session, transport }

The created Live session identifier and WebRTC answer. Apply transport.sdp as the peer’s remote answer and wait for session.started on the data channel before sending commands.

session: object { id }

The newly created Live session. Use its ID for session controls and sideband connections.

Opaque session identifier. Preserve the returned value unchanged, including its prefix.

transport: object { sdp, type }

WebRTC transport with the SDP answer.

sdp: string

Session Description Protocol message for the WebRTC connection.

minLength1

type: "webrtc"

The transport used for the Live session. Always `webrtc`.

#### LiveSideband
