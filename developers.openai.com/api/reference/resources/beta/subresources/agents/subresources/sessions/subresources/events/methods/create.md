<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/agents/subresources/sessions/subresources/events/methods/create/ -->

[Sessions](/api/reference/resources/beta/subresources/agents/subresources/sessions)

[Events](/api/reference/resources/beta/subresources/agents/subresources/sessions/subresources/events)

# Create agent session input events

POST/agents/sessions/{session\_id}/events

Submits message, cancellation, or tool-result events to a managed agent session. See [session events](/api/docs/guides/agents-api/sessions/events).

##### Header ParametersExpand Collapse

"Idempotency-Key": optional string

minLength1

maxLength256

session\_id: string

##### Body ParametersJSONExpand Collapse

events: array of [AgentSessionInputParam](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20agent_session_input_param%20%3E%20(schema))

The input events to submit to the session.

AgentSessionInputMessage object { input, type }

Adds one or more user messages and starts a turn.

input: array of [AgentSessionInputMessageParam](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20agent_session_input_message_param%20%3E%20(schema)) { content, role, type }

The user messages to add to the session.

content: array of [InputContentParam](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20input_content_param%20%3E%20(schema))

The content of the message.

InputText object { text, type }

Text input to the model.

text: string

The text sent to the model.

type: "input\_text"

The type of the object. Always `input_text`.

InputImage object { image\_url, type }

Image input to the model.

image\_url: string

The URL of the image sent to the model.

type: "input\_image"

The type of the object. Always `input_image`.

role: "user"

The role of the message author. Always `user`.

type: optional "message"

The type of the input item. Always `message`.

type: "agent.session.input.message"

The type of the object. Always `agent.session.input.message`.

AgentSessionInputCancel object { type }

Cancels the session’s active turn.

type: "agent.session.input.cancel"

The type of the object. Always `agent.session.input.cancel`.

AgentSessionInputToolResult object { call\_id, success, turn\_id, 3 more }

Submits the result of a function call.

call\_id: string

The ID of the function call.

success: boolean

Whether the function call succeeded.

turn\_id: string

The ID of the turn that requested the function call.

type: "agent.session.input.tool\_result"

The type of the object. Always `agent.session.input.tool_result`.

error: optional string or null

The error message when the call failed.

output: optional [AgentFunctionCallOutputParam](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20agent_function_call_output_param%20%3E%20(schema)) or null

A function result represented as text or supported model-input content.

string

array of [InputContentParam](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20input_content_param%20%3E%20(schema))

InputText object { text, type }

Text input to the model.

text: string

The text sent to the model.

type: "input\_text"

The type of the object. Always `input_text`.

InputImage object { image\_url, type }

Image input to the model.

image\_url: string

The URL of the image sent to the model.

type: "input\_image"

The type of the object. Always `input_image`.

### Create agent session input events

curl https://api.openai.com/v1/agents/sessions/$SESSION_ID/events \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -d '{
          "events": [
              "input": [
                  "content": [
                      "text": "text",
                      "type": "input_text"
                  ],
                  "role": "user"
              ],
              "type": "agent.session.input.message"
          ]
        }'
