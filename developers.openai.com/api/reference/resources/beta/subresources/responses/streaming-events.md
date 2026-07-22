<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/responses/streaming-events/ -->

An event that is emitted when a response is created.

response: [BetaResponse](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema)) { id, created\_at, error, 32 more }

The response that was created.

sequence\_number: number

The sequence number for this event.

type: "response.created"

The type of the event. Always `response.created`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.created

  "type": "response.created",
  "response": {
    "id": "resp_67ccfcdd16748190a91872c75d38539e09e4d4aac714747c",
    "object": "response",
    "created_at": 1741487325,
    "status": "in_progress",
    "completed_at": null,
    "error": null,
    "incomplete_details": null,
    "instructions": null,
    "max_output_tokens": null,
    "model": "gpt-4o-2024-08-06",
    "output": [],
    "parallel_tool_calls": true,
    "previous_response_id": null,
    "reasoning": {
      "effort": null,
      "summary": null
    },
    "store": true,
    "temperature": 1,
    "text": {
      "format": {
        "type": "text"
    },
    "tool_choice": "auto",
    "tools": [],
    "top_p": 1,
    "truncation": "disabled",
    "usage": null,
    "user": null,
    "metadata": {}
  },
  "sequence_number": 1

Emitted when the response is in progress.

response: [BetaResponse](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema)) { id, created\_at, error, 32 more }

The response that is in progress.

sequence\_number: number

The sequence number of this event.

type: "response.in\_progress"

The type of the event. Always `response.in_progress`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.in\_progress

  "type": "response.in_progress",
  "response": {
    "id": "resp_67ccfcdd16748190a91872c75d38539e09e4d4aac714747c",
    "object": "response",
    "created_at": 1741487325,
    "status": "in_progress",
    "completed_at": null,
    "error": null,
    "incomplete_details": null,
    "instructions": null,
    "max_output_tokens": null,
    "model": "gpt-4o-2024-08-06",
    "output": [],
    "parallel_tool_calls": true,
    "previous_response_id": null,
    "reasoning": {
      "effort": null,
      "summary": null
    },
    "store": true,
    "temperature": 1,
    "text": {
      "format": {
        "type": "text"
    },
    "tool_choice": "auto",
    "tools": [],
    "top_p": 1,
    "truncation": "disabled",
    "usage": null,
    "user": null,
    "metadata": {}
  },
  "sequence_number": 1

Emitted when the model response is complete.

response: [BetaResponse](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema)) { id, created\_at, error, 32 more }

Properties of the completed response.

sequence\_number: number

The sequence number for this event.

type: "response.completed"

The type of the event. Always `response.completed`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.completed

  "type": "response.completed",
  "response": {
    "id": "resp_123",
    "object": "response",
    "created_at": 1740855869,
    "status": "completed",
    "completed_at": 1740855870,
    "error": null,
    "incomplete_details": null,
    "input": [],
    "instructions": null,
    "max_output_tokens": null,
    "model": "gpt-4o-mini-2024-07-18",
    "output": [
        "id": "msg_123",
        "type": "message",
        "role": "assistant",
        "content": [
            "type": "output_text",
            "text": "In a shimmering forest under a sky full of stars, a lonely unicorn named Lila discovered a hidden pond that glowed with moonlight. Every night, she would leave sparkling, magical flowers by the water's edge, hoping to share her beauty with others. One enchanting evening, she woke to find a group of friendly animals gathered around, eager to be friends and share in her magic.",
            "annotations": []
    ],
    "previous_response_id": null,
    "reasoning_effort": null,
    "store": false,
    "temperature": 1,
    "text": {
      "format": {
        "type": "text"
    },
    "tool_choice": "auto",
    "tools": [],
    "top_p": 1,
    "truncation": "disabled",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "output_tokens_details": {
        "reasoning_tokens": 0
      },
      "total_tokens": 0
    },
    "user": null,
    "metadata": {}
  },
  "sequence_number": 1

An event that is emitted when a response fails.

response: [BetaResponse](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema)) { id, created\_at, error, 32 more }

The response that failed.

sequence\_number: number

The sequence number of this event.

type: "response.failed"

The type of the event. Always `response.failed`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.failed

  "type": "response.failed",
  "response": {
    "id": "resp_123",
    "object": "response",
    "created_at": 1740855869,
    "status": "failed",
    "completed_at": null,
    "error": {
      "code": "server_error",
      "message": "The model failed to generate a response."
    },
    "incomplete_details": null,
    "instructions": null,
    "max_output_tokens": null,
    "model": "gpt-4o-mini-2024-07-18",
    "output": [],
    "previous_response_id": null,
    "reasoning_effort": null,
    "store": false,
    "temperature": 1,
    "text": {
      "format": {
        "type": "text"
    },
    "tool_choice": "auto",
    "tools": [],
    "top_p": 1,
    "truncation": "disabled",
    "usage": null,
    "user": null,
    "metadata": {}

An event that is emitted when a response finishes as incomplete.

response: [BetaResponse](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema)) { id, created\_at, error, 32 more }

The response that was incomplete.

sequence\_number: number

The sequence number of this event.

type: "response.incomplete"

The type of the event. Always `response.incomplete`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.incomplete

  "type": "response.incomplete",
  "response": {
    "id": "resp_123",
    "object": "response",
    "created_at": 1740855869,
    "status": "incomplete",
    "completed_at": null,
    "error": null,
    "incomplete_details": {
      "reason": "max_tokens"
    },
    "instructions": null,
    "max_output_tokens": null,
    "model": "gpt-4o-mini-2024-07-18",
    "output": [],
    "previous_response_id": null,
    "reasoning_effort": null,
    "store": false,
    "temperature": 1,
    "text": {
      "format": {
        "type": "text"
    },
    "tool_choice": "auto",
    "tools": [],
    "top_p": 1,
    "truncation": "disabled",
    "usage": null,
    "user": null,
    "metadata": {}
  },
  "sequence_number": 1

Emitted when a new output item is added.

item: [BetaResponseOutputItem](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema))

The output item that was added.

output\_index: number

The index of the output item that was added.

sequence\_number: number

The sequence number of this event.

type: "response.output\_item.added"

The type of the event. Always `response.output_item.added`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.output\_item.added

  "type": "response.output_item.added",
  "output_index": 0,
  "item": {
    "id": "msg_123",
    "status": "in_progress",
    "type": "message",
    "role": "assistant",
    "content": []
  },
  "sequence_number": 1

Emitted when an output item is marked done.

item: [BetaResponseOutputItem](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema))

The output item that was marked done.

output\_index: number

The index of the output item that was marked done.

sequence\_number: number

The sequence number of this event.

type: "response.output\_item.done"

The type of the event. Always `response.output_item.done`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.output\_item.done

  "type": "response.output_item.done",
  "output_index": 0,
  "item": {
    "id": "msg_123",
    "status": "completed",
    "type": "message",
    "role": "assistant",
    "content": [
        "type": "output_text",
        "text": "In a shimmering forest under a sky full of stars, a lonely unicorn named Lila discovered a hidden pond that glowed with moonlight. Every night, she would leave sparkling, magical flowers by the water's edge, hoping to share her beauty with others. One enchanting evening, she woke to find a group of friendly animals gathered around, eager to be friends and share in her magic.",
        "annotations": []
  },
  "sequence_number": 1

Emitted when a new content part is added.

content\_index: number

The index of the content part that was added.

item\_id: string

The ID of the output item that the content part was added to.

output\_index: number

The index of the output item that the content part was added to.

part: [BetaResponseOutputText](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema)) { annotations, logprobs, text, type }  or [BetaResponseOutputRefusal](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_refusal%20%3E%20(schema)) { refusal, type }  or object { text, type }

The content part that was added.

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

BetaResponseOutputRefusal object { refusal, type }

refusal: string

type: "refusal"

ReasoningText object { text, type }

text: string

type: "reasoning\_text"

sequence\_number: number

The sequence number of this event.

type: "response.content\_part.added"

The type of the event. Always `response.content_part.added`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.content\_part.added

  "type": "response.content_part.added",
  "item_id": "msg_123",
  "output_index": 0,
  "content_index": 0,
  "part": {
    "type": "output_text",
    "text": "",
    "annotations": []
  },
  "sequence_number": 1

Emitted when a content part is done.

content\_index: number

The index of the content part that is done.

item\_id: string

The ID of the output item that the content part was added to.

output\_index: number

The index of the output item that the content part was added to.

part: [BetaResponseOutputText](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema)) { annotations, logprobs, text, type }  or [BetaResponseOutputRefusal](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_refusal%20%3E%20(schema)) { refusal, type }  or object { text, type }

The content part that is done.

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

BetaResponseOutputRefusal object { refusal, type }

refusal: string

type: "refusal"

ReasoningText object { text, type }

text: string

type: "reasoning\_text"

sequence\_number: number

The sequence number of this event.

type: "response.content\_part.done"

The type of the event. Always `response.content_part.done`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.content\_part.done

  "type": "response.content_part.done",
  "item_id": "msg_123",
  "output_index": 0,
  "content_index": 0,
  "sequence_number": 1,
  "part": {
    "type": "output_text",
    "text": "In a shimmering forest under a sky full of stars, a lonely unicorn named Lila discovered a hidden pond that glowed with moonlight. Every night, she would leave sparkling, magical flowers by the water's edge, hoping to share her beauty with others. One enchanting evening, she woke to find a group of friendly animals gathered around, eager to be friends and share in her magic.",
    "annotations": []

Emitted when there is an additional text delta.

content\_index: number

The index of the content part that the text delta was added to.

delta: string

The text delta that was added.

item\_id: string

The ID of the output item that the text delta was added to.

logprobs: array of object { token, logprob, top\_logprobs }

The log probabilities of the tokens in the delta.

token: string

A possible text token.

logprob: number

The log probability of this token.

top\_logprobs: optional array of object { token, logprob }

The log probabilities of up to 20 of the most likely tokens.

token: optional string

A possible text token.

logprob: optional number

The log probability of this token.

output\_index: number

The index of the output item that the text delta was added to.

sequence\_number: number

The sequence number for this event.

type: "response.output\_text.delta"

The type of the event. Always `response.output_text.delta`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.output\_text.delta

  "type": "response.output_text.delta",
  "item_id": "msg_123",
  "output_index": 0,
  "content_index": 0,
  "delta": "In",
  "sequence_number": 1

Emitted when text content is finalized.

content\_index: number

The index of the content part that the text content is finalized.

item\_id: string

The ID of the output item that the text content is finalized.

logprobs: array of object { token, logprob, top\_logprobs }

The log probabilities of the tokens in the delta.

token: string

A possible text token.

logprob: number

The log probability of this token.

top\_logprobs: optional array of object { token, logprob }

The log probabilities of up to 20 of the most likely tokens.

token: optional string

A possible text token.

logprob: optional number

The log probability of this token.

output\_index: number

The index of the output item that the text content is finalized.

sequence\_number: number

The sequence number for this event.

text: string

The text content that is finalized.

type: "response.output\_text.done"

The type of the event. Always `response.output_text.done`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.output\_text.done

  "type": "response.output_text.done",
  "item_id": "msg_123",
  "output_index": 0,
  "content_index": 0,
  "text": "In a shimmering forest under a sky full of stars, a lonely unicorn named Lila discovered a hidden pond that glowed with moonlight. Every night, she would leave sparkling, magical flowers by the water's edge, hoping to share her beauty with others. One enchanting evening, she woke to find a group of friendly animals gathered around, eager to be friends and share in her magic.",
  "sequence_number": 1

Emitted when there is a partial refusal text.

content\_index: number

The index of the content part that the refusal text is added to.

delta: string

The refusal text that is added.

item\_id: string

The ID of the output item that the refusal text is added to.

output\_index: number

The index of the output item that the refusal text is added to.

sequence\_number: number

The sequence number of this event.

type: "response.refusal.delta"

The type of the event. Always `response.refusal.delta`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.refusal.delta

  "type": "response.refusal.delta",
  "item_id": "msg_123",
  "output_index": 0,
  "content_index": 0,
  "delta": "refusal text so far",
  "sequence_number": 1

Emitted when refusal text is finalized.

content\_index: number

The index of the content part that the refusal text is finalized.

item\_id: string

The ID of the output item that the refusal text is finalized.

output\_index: number

The index of the output item that the refusal text is finalized.

refusal: string

The refusal text that is finalized.

sequence\_number: number

The sequence number of this event.

type: "response.refusal.done"

The type of the event. Always `response.refusal.done`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.refusal.done

  "type": "response.refusal.done",
  "item_id": "item-abc",
  "output_index": 1,
  "content_index": 2,
  "refusal": "final refusal text",
  "sequence_number": 1

Emitted when there is a partial function-call arguments delta.

delta: string

The function-call arguments delta that is added.

item\_id: string

The ID of the output item that the function-call arguments delta is added to.

output\_index: number

The index of the output item that the function-call arguments delta is added to.

sequence\_number: number

The sequence number of this event.

type: "response.function\_call\_arguments.delta"

The type of the event. Always `response.function_call_arguments.delta`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.function\_call\_arguments.delta

  "type": "response.function_call_arguments.delta",
  "item_id": "item-abc",
  "output_index": 0,
  "delta": "{ \"arg\":"
  "sequence_number": 1

Emitted when function-call arguments are finalized.

arguments: string

The function-call arguments.

item\_id: string

The ID of the item.

name: string

The name of the function that was called.

output\_index: number

The index of the output item.

sequence\_number: number

The sequence number of this event.

type: "response.function\_call\_arguments.done"

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.function\_call\_arguments.done

  "type": "response.function_call_arguments.done",
  "item_id": "item-abc",
  "name": "get_weather",
  "output_index": 1,
  "arguments": "{ \"arg\": 123 }",
  "sequence_number": 1

Emitted when a file search call is initiated.

item\_id: string

The ID of the output item that the file search call is initiated.

output\_index: number

The index of the output item that the file search call is initiated.

sequence\_number: number

The sequence number of this event.

type: "response.file\_search\_call.in\_progress"

The type of the event. Always `response.file_search_call.in_progress`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.file\_search\_call.in\_progress

  "type": "response.file_search_call.in_progress",
  "output_index": 0,
  "item_id": "fs_123",
  "sequence_number": 1

Emitted when a file search is currently searching.

item\_id: string

The ID of the output item that the file search call is initiated.

output\_index: number

The index of the output item that the file search call is searching.

sequence\_number: number

The sequence number of this event.

type: "response.file\_search\_call.searching"

The type of the event. Always `response.file_search_call.searching`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.file\_search\_call.searching

  "type": "response.file_search_call.searching",
  "output_index": 0,
  "item_id": "fs_123",
  "sequence_number": 1

Emitted when a file search call is completed (results found).

item\_id: string

The ID of the output item that the file search call is initiated.

output\_index: number

The index of the output item that the file search call is initiated.

sequence\_number: number

The sequence number of this event.

type: "response.file\_search\_call.completed"

The type of the event. Always `response.file_search_call.completed`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.file\_search\_call.completed

  "type": "response.file_search_call.completed",
  "output_index": 0,
  "item_id": "fs_123",
  "sequence_number": 1

Emitted when a web search call is initiated.

item\_id: string

Unique ID for the output item associated with the web search call.

output\_index: number

The index of the output item that the web search call is associated with.

sequence\_number: number

The sequence number of the web search call being processed.

type: "response.web\_search\_call.in\_progress"

The type of the event. Always `response.web_search_call.in_progress`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.web\_search\_call.in\_progress

  "type": "response.web_search_call.in_progress",
  "output_index": 0,
  "item_id": "ws_123",
  "sequence_number": 0

Emitted when a web search call is executing.

item\_id: string

Unique ID for the output item associated with the web search call.

output\_index: number

The index of the output item that the web search call is associated with.

sequence\_number: number

The sequence number of the web search call being processed.

type: "response.web\_search\_call.searching"

The type of the event. Always `response.web_search_call.searching`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.web\_search\_call.searching

  "type": "response.web_search_call.searching",
  "output_index": 0,
  "item_id": "ws_123",
  "sequence_number": 0

Emitted when a web search call is completed.

item\_id: string

Unique ID for the output item associated with the web search call.

output\_index: number

The index of the output item that the web search call is associated with.

sequence\_number: number

The sequence number of the web search call being processed.

type: "response.web\_search\_call.completed"

The type of the event. Always `response.web_search_call.completed`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.web\_search\_call.completed

  "type": "response.web_search_call.completed",
  "output_index": 0,
  "item_id": "ws_123",
  "sequence_number": 0

Emitted when a new reasoning summary part is added.

item\_id: string

The ID of the item this summary part is associated with.

output\_index: number

The index of the output item this summary part is associated with.

part: object { text, type }

The summary part that was added.

text: string

The text of the summary part.

type: "summary\_text"

The type of the summary part. Always `summary_text`.

sequence\_number: number

The sequence number of this event.

summary\_index: number

The index of the summary part within the reasoning summary.

type: "response.reasoning\_summary\_part.added"

The type of the event. Always `response.reasoning_summary_part.added`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.reasoning\_summary\_part.added

  "type": "response.reasoning_summary_part.added",
  "item_id": "rs_6806bfca0b2481918a5748308061a2600d3ce51bdffd5476",
  "output_index": 0,
  "summary_index": 0,
  "part": {
    "type": "summary_text",
    "text": ""
  },
  "sequence_number": 1

Emitted when a reasoning summary part is completed.

item\_id: string

The ID of the item this summary part is associated with.

output\_index: number

The index of the output item this summary part is associated with.

part: object { text, type }

The completed summary part.

text: string

The text of the summary part.

type: "summary\_text"

The type of the summary part. Always `summary_text`.

sequence\_number: number

The sequence number of this event.

summary\_index: number

The index of the summary part within the reasoning summary.

type: "response.reasoning\_summary\_part.done"

The type of the event. Always `response.reasoning_summary_part.done`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

status: optional "incomplete"

The completion status of the summary part. Omitted when the part completed
normally and set to `incomplete` when generation was interrupted.

OBJECT

### response.reasoning\_summary\_part.done

  "type": "response.reasoning_summary_part.done",
  "item_id": "rs_6806bfca0b2481918a5748308061a2600d3ce51bdffd5476",
  "output_index": 0,
  "summary_index": 0,
  "part": {
    "type": "summary_text",
    "text": "**Responding to a greeting**\n\nThe user just said, \"Hello!\" So, it seems I need to engage. I'll greet them back and offer help since they're looking to chat. I could say something like, \"Hello! How can I assist you today?\" That feels friendly and open. They didn't ask a specific question, so this approach will work well for starting a conversation. Let's see where it goes from there!"
  },
  "sequence_number": 1

Emitted when a delta is added to a reasoning summary text.

delta: string

The text delta that was added to the summary.

item\_id: string

The ID of the item this summary text delta is associated with.

output\_index: number

The index of the output item this summary text delta is associated with.

sequence\_number: number

The sequence number of this event.

summary\_index: number

The index of the summary part within the reasoning summary.

type: "response.reasoning\_summary\_text.delta"

The type of the event. Always `response.reasoning_summary_text.delta`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.reasoning\_summary\_text.delta

  "type": "response.reasoning_summary_text.delta",
  "item_id": "rs_6806bfca0b2481918a5748308061a2600d3ce51bdffd5476",
  "output_index": 0,
  "summary_index": 0,
  "delta": "**Responding to a greeting**\n\nThe user just said, \"Hello!\" So, it seems I need to engage. I'll greet them back and offer help since they're looking to chat. I could say something like, \"Hello! How can I assist you today?\" That feels friendly and open. They didn't ask a specific question, so this approach will work well for starting a conversation. Let's see where it goes from there!",
  "sequence_number": 1

Emitted when a reasoning summary text is completed.

item\_id: string

The ID of the item this summary text is associated with.

output\_index: number

The index of the output item this summary text is associated with.

sequence\_number: number

The sequence number of this event.

summary\_index: number

The index of the summary part within the reasoning summary.

text: string

The full text of the completed reasoning summary.

type: "response.reasoning\_summary\_text.done"

The type of the event. Always `response.reasoning_summary_text.done`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.reasoning\_summary\_text.done

  "type": "response.reasoning_summary_text.done",
  "item_id": "rs_6806bfca0b2481918a5748308061a2600d3ce51bdffd5476",
  "output_index": 0,
  "summary_index": 0,
  "text": "**Responding to a greeting**\n\nThe user just said, \"Hello!\" So, it seems I need to engage. I'll greet them back and offer help since they're looking to chat. I could say something like, \"Hello! How can I assist you today?\" That feels friendly and open. They didn't ask a specific question, so this approach will work well for starting a conversation. Let's see where it goes from there!",
  "sequence_number": 1

Emitted when a delta is added to a reasoning text.

content\_index: number

The index of the reasoning content part this delta is associated with.

delta: string

The text delta that was added to the reasoning content.

item\_id: string

The ID of the item this reasoning text delta is associated with.

output\_index: number

The index of the output item this reasoning text delta is associated with.

sequence\_number: number

The sequence number of this event.

type: "response.reasoning\_text.delta"

The type of the event. Always `response.reasoning_text.delta`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.reasoning\_text.delta

  "type": "response.reasoning_text.delta",
  "item_id": "rs_123",
  "output_index": 0,
  "content_index": 0,
  "delta": "The",
  "sequence_number": 1

Emitted when a reasoning text is completed.

content\_index: number

The index of the reasoning content part.

item\_id: string

The ID of the item this reasoning text is associated with.

output\_index: number

The index of the output item this reasoning text is associated with.

sequence\_number: number

The sequence number of this event.

text: string

The full text of the completed reasoning content.

type: "response.reasoning\_text.done"

The type of the event. Always `response.reasoning_text.done`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.reasoning\_text.done

  "type": "response.reasoning_text.done",
  "item_id": "rs_123",
  "output_index": 0,
  "content_index": 0,
  "text": "The user is asking...",
  "sequence_number": 4

Emitted when an image generation tool call has completed and the final image is available.

item\_id: string

The unique identifier of the image generation item being processed.

output\_index: number

The index of the output item in the response's output array.

sequence\_number: number

The sequence number of this event.

type: "response.image\_generation\_call.completed"

The type of the event. Always 'response.image\_generation\_call.completed'.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.image\_generation\_call.completed

  "type": "response.image_generation_call.completed",
  "output_index": 0,
  "item_id": "item-123",
  "sequence_number": 1

Emitted when an image generation tool call is actively generating an image (intermediate state).

item\_id: string

The unique identifier of the image generation item being processed.

output\_index: number

The index of the output item in the response's output array.

sequence\_number: number

The sequence number of the image generation item being processed.

type: "response.image\_generation\_call.generating"

The type of the event. Always 'response.image\_generation\_call.generating'.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.image\_generation\_call.generating

  "type": "response.image_generation_call.generating",
  "output_index": 0,
  "item_id": "item-123",
  "sequence_number": 0

Emitted when an image generation tool call is in progress.

item\_id: string

The unique identifier of the image generation item being processed.

output\_index: number

The index of the output item in the response's output array.

sequence\_number: number

The sequence number of the image generation item being processed.

type: "response.image\_generation\_call.in\_progress"

The type of the event. Always 'response.image\_generation\_call.in\_progress'.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.image\_generation\_call.in\_progress

  "type": "response.image_generation_call.in_progress",
  "output_index": 0,
  "item_id": "item-123",
  "sequence_number": 0

Emitted when a partial image is available during image generation streaming.

item\_id: string

The unique identifier of the image generation item being processed.

output\_index: number

The index of the output item in the response's output array.

partial\_image\_b64: string

Base64-encoded partial image data, suitable for rendering as an image.

partial\_image\_index: number

0-based index for the partial image (backend is 1-based, but this is 0-based for the user).

sequence\_number: number

The sequence number of the image generation item being processed.

type: "response.image\_generation\_call.partial\_image"

The type of the event. Always 'response.image\_generation\_call.partial\_image'.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.image\_generation\_call.partial\_image

  "type": "response.image_generation_call.partial_image",
  "output_index": 0,
  "item_id": "item-123",
  "sequence_number": 0,
  "partial_image_index": 0,
  "partial_image_b64": "..."

Emitted when there is a delta (partial update) to the arguments of an MCP tool call.

delta: string

A JSON string containing the partial update to the arguments for the MCP tool call.

item\_id: string

The unique identifier of the MCP tool call item being processed.

output\_index: number

The index of the output item in the response's output array.

sequence\_number: number

The sequence number of this event.

type: "response.mcp\_call\_arguments.delta"

The type of the event. Always 'response.mcp\_call\_arguments.delta'.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.mcp\_call\_arguments.delta

  "type": "response.mcp_call_arguments.delta",
  "output_index": 0,
  "item_id": "item-abc",
  "delta": "{",
  "sequence_number": 1

Emitted when the arguments for an MCP tool call are finalized.

arguments: string

A JSON string containing the finalized arguments for the MCP tool call.

item\_id: string

The unique identifier of the MCP tool call item being processed.

output\_index: number

The index of the output item in the response's output array.

sequence\_number: number

The sequence number of this event.

type: "response.mcp\_call\_arguments.done"

The type of the event. Always 'response.mcp\_call\_arguments.done'.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.mcp\_call\_arguments.done

  "type": "response.mcp_call_arguments.done",
  "output_index": 0,
  "item_id": "item-abc",
  "arguments": "{\"arg1\": \"value1\", \"arg2\": \"value2\"}",
  "sequence_number": 1

Emitted when an MCP tool call has completed successfully.

item\_id: string

The ID of the MCP tool call item that completed.

output\_index: number

The index of the output item that completed.

sequence\_number: number

The sequence number of this event.

type: "response.mcp\_call.completed"

The type of the event. Always 'response.mcp\_call.completed'.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.mcp\_call.completed

  "type": "response.mcp_call.completed",
  "sequence_number": 1,
  "item_id": "mcp_682d437d90a88191bf88cd03aae0c3e503937d5f622d7a90",
  "output_index": 0

Emitted when an MCP tool call has failed.

item\_id: string

The ID of the MCP tool call item that failed.

output\_index: number

The index of the output item that failed.

sequence\_number: number

The sequence number of this event.

type: "response.mcp\_call.failed"

The type of the event. Always 'response.mcp\_call.failed'.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.mcp\_call.failed

  "type": "response.mcp_call.failed",
  "sequence_number": 1,
  "item_id": "mcp_682d437d90a88191bf88cd03aae0c3e503937d5f622d7a90",
  "output_index": 0

Emitted when an MCP tool call is in progress.

item\_id: string

The unique identifier of the MCP tool call item being processed.

output\_index: number

The index of the output item in the response's output array.

sequence\_number: number

The sequence number of this event.

type: "response.mcp\_call.in\_progress"

The type of the event. Always 'response.mcp\_call.in\_progress'.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.mcp\_call.in\_progress

  "type": "response.mcp_call.in_progress",
  "sequence_number": 1,
  "output_index": 0,
  "item_id": "mcp_682d437d90a88191bf88cd03aae0c3e503937d5f622d7a90"

Emitted when the list of available MCP tools has been successfully retrieved.

item\_id: string

The ID of the MCP tool call item that produced this output.

output\_index: number

The index of the output item that was processed.

sequence\_number: number

The sequence number of this event.

type: "response.mcp\_list\_tools.completed"

The type of the event. Always 'response.mcp\_list\_tools.completed'.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.mcp\_list\_tools.completed

  "type": "response.mcp_list_tools.completed",
  "sequence_number": 1,
  "output_index": 0,
  "item_id": "mcpl_682d4379df088191886b70f4ec39f90403937d5f622d7a90"

Emitted when the attempt to list available MCP tools has failed.

item\_id: string

The ID of the MCP tool call item that failed.

output\_index: number

The index of the output item that failed.

sequence\_number: number

The sequence number of this event.

type: "response.mcp\_list\_tools.failed"

The type of the event. Always 'response.mcp\_list\_tools.failed'.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.mcp\_list\_tools.failed

  "type": "response.mcp_list_tools.failed",
  "sequence_number": 1,
  "output_index": 0,
  "item_id": "mcpl_682d4379df088191886b70f4ec39f90403937d5f622d7a90"

Emitted when the system is in the process of retrieving the list of available MCP tools.

item\_id: string

The ID of the MCP tool call item that is being processed.

output\_index: number

The index of the output item that is being processed.

sequence\_number: number

The sequence number of this event.

type: "response.mcp\_list\_tools.in\_progress"

The type of the event. Always 'response.mcp\_list\_tools.in\_progress'.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.mcp\_list\_tools.in\_progress

  "type": "response.mcp_list_tools.in_progress",
  "sequence_number": 1,
  "output_index": 0,
  "item_id": "mcpl_682d4379df088191886b70f4ec39f90403937d5f622d7a90"

Emitted when a code interpreter call is in progress.

item\_id: string

The unique identifier of the code interpreter tool call item.

output\_index: number

The index of the output item in the response for which the code interpreter call is in progress.

sequence\_number: number

The sequence number of this event, used to order streaming events.

type: "response.code\_interpreter\_call.in\_progress"

The type of the event. Always `response.code_interpreter_call.in_progress`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.code\_interpreter\_call.in\_progress

  "type": "response.code_interpreter_call.in_progress",
  "output_index": 0,
  "item_id": "ci_12345",
  "sequence_number": 1

Emitted when the code interpreter is actively interpreting the code snippet.

item\_id: string

The unique identifier of the code interpreter tool call item.

output\_index: number

The index of the output item in the response for which the code interpreter is interpreting code.

sequence\_number: number

The sequence number of this event, used to order streaming events.

type: "response.code\_interpreter\_call.interpreting"

The type of the event. Always `response.code_interpreter_call.interpreting`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.code\_interpreter\_call.interpreting

  "type": "response.code_interpreter_call.interpreting",
  "output_index": 4,
  "item_id": "ci_12345",
  "sequence_number": 1

Emitted when the code interpreter call is completed.

item\_id: string

The unique identifier of the code interpreter tool call item.

output\_index: number

The index of the output item in the response for which the code interpreter call is completed.

sequence\_number: number

The sequence number of this event, used to order streaming events.

type: "response.code\_interpreter\_call.completed"

The type of the event. Always `response.code_interpreter_call.completed`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.code\_interpreter\_call.completed

  "type": "response.code_interpreter_call.completed",
  "output_index": 5,
  "item_id": "ci_12345",
  "sequence_number": 1

Emitted when a partial code snippet is streamed by the code interpreter.

delta: string

The partial code snippet being streamed by the code interpreter.

item\_id: string

The unique identifier of the code interpreter tool call item.

output\_index: number

The index of the output item in the response for which the code is being streamed.

sequence\_number: number

The sequence number of this event, used to order streaming events.

type: "response.code\_interpreter\_call\_code.delta"

The type of the event. Always `response.code_interpreter_call_code.delta`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.code\_interpreter\_call\_code.delta

  "type": "response.code_interpreter_call_code.delta",
  "output_index": 0,
  "item_id": "ci_12345",
  "delta": "print('Hello, world')",
  "sequence_number": 1

Emitted when the code snippet is finalized by the code interpreter.

code: string

The final code snippet output by the code interpreter.

item\_id: string

The unique identifier of the code interpreter tool call item.

output\_index: number

The index of the output item in the response for which the code is finalized.

sequence\_number: number

The sequence number of this event, used to order streaming events.

type: "response.code\_interpreter\_call\_code.done"

The type of the event. Always `response.code_interpreter_call_code.done`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.code\_interpreter\_call\_code.done

  "type": "response.code_interpreter_call_code.done",
  "output_index": 3,
  "item_id": "ci_12345",
  "code": "print('done')",
  "sequence_number": 1

Emitted when an annotation is added to output text content.

annotation: unknown

The annotation object being added. (See annotation schema for details.)

annotation\_index: number

The index of the annotation within the content part.

content\_index: number

The index of the content part within the output item.

item\_id: string

The unique identifier of the item to which the annotation is being added.

output\_index: number

The index of the output item in the response's output array.

sequence\_number: number

The sequence number of this event.

type: "response.output\_text.annotation.added"

The type of the event. Always 'response.output\_text.annotation.added'.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.output\_text.annotation.added

  "type": "response.output_text.annotation.added",
  "item_id": "item-abc",
  "output_index": 0,
  "content_index": 0,
  "annotation_index": 0,
  "annotation": {
    "type": "text_annotation",
    "text": "This is a test annotation",
    "start": 0,
    "end": 10
  },
  "sequence_number": 1

Emitted when a response is queued and waiting to be processed.

response: [BetaResponse](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response%20%3E%20(schema)) { id, created\_at, error, 32 more }

The full response object that is queued.

sequence\_number: number

The sequence number for this event.

type: "response.queued"

The type of the event. Always 'response.queued'.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.queued

  "type": "response.queued",
  "response": {
    "id": "res_123",
    "status": "queued",
    "created_at": "2021-01-01T00:00:00Z",
    "updated_at": "2021-01-01T00:00:00Z"
  },
  "sequence_number": 1

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

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.custom\_tool\_call\_input.delta

  "type": "response.custom_tool_call_input.delta",
  "output_index": 0,
  "item_id": "ctc_1234567890abcdef",
  "delta": "partial input text"

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

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.custom\_tool\_call\_input.done

  "type": "response.custom_tool_call_input.done",
  "output_index": 0,
  "item_id": "ctc_1234567890abcdef",
  "input": "final complete input text"

Emitted when an error occurs.

code: string

The error code.

message: string

The error message.

param: string

The error parameter.

sequence\_number: number

The sequence number of this event.

type: "error"

The type of the event. Always `error`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### error

  "type": "error",
  "code": "ERR_SOMETHING",
  "message": "Something went wrong",
  "param": null,
  "sequence_number": 1

Emitted when there is a partial audio response.

delta: string

A chunk of Base64 encoded response audio bytes.

sequence\_number: number

A sequence number for this chunk of the stream response.

type: "response.audio.delta"

The type of the event. Always `response.audio.delta`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.audio.delta

  "type": "response.audio.delta",
  "response_id": "resp_123",
  "delta": "base64encoded...",
  "sequence_number": 1

Emitted when the audio response is complete.

sequence\_number: number

The sequence number of the delta.

type: "response.audio.done"

The type of the event. Always `response.audio.done`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.audio.done

  "type": "response.audio.done",
  "response_id": "resp-123",
  "sequence_number": 1

Emitted when there is a partial transcript of audio.

delta: string

The partial transcript of the audio response.

sequence\_number: number

The sequence number of this event.

type: "response.audio.transcript.delta"

The type of the event. Always `response.audio.transcript.delta`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.audio.transcript.delta

  "type": "response.audio.transcript.delta",
  "response_id": "resp_123",
  "delta": " ... partial transcript ... ",
  "sequence_number": 1

Emitted when the full audio transcript is completed.

sequence\_number: number

The sequence number of this event.

type: "response.audio.transcript.done"

The type of the event. Always `response.audio.transcript.done`.

agent: optional object { agent\_name }

The agent that owns this multi-agent streaming event.

agent\_name: string

OBJECT

### response.audio.transcript.done

  "type": "response.audio.transcript.done",
  "response_id": "resp_123",
  "sequence_number": 1
