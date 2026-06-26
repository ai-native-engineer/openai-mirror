<!-- source: https://developers.openai.com/api/reference/cli/resources/chat/subresources/completions/subresources/messages/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Chat](/api/reference/cli/resources/chat)

[Completions](/api/reference/cli/resources/chat/subresources/completions)

[Messages](/api/reference/cli/resources/chat/subresources/completions/subresources/messages)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Get chat messages

$ openai chat:completions:messages list

GET/chat/completions/{completion\_id}/messages

Get the messages in a stored chat completion. Only Chat Completions that
have been created with the `store` parameter set to `true` will be
returned.

##### ParametersExpand Collapse

--completion-id: string

The ID of the chat completion to retrieve messages from.

--after: optional string

Identifier for the last message from the previous pagination request.

--limit: optional number

Number of messages to retrieve.

--order: optional "asc" or "desc"

Sort order for messages by timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `asc`.

##### ReturnsExpand Collapse

ChatCompletionMessageList: object { data, first\_id, has\_more, 2 more }

An object representing a list of chat completion messages.

data: array of [ChatCompletionStoreMessage](/api/reference/cli/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_store_message%20%3E%20(schema)) { id, content\_parts }

An array of chat completion message objects.

id: string

The identifier of the chat message.

content\_parts: optional array of [ChatCompletionContentPartText](/api/reference/cli/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text, type }  or [ChatCompletionContentPartImage](/api/reference/cli/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)) { image\_url, type }

If a content parts array was provided, this is an array of `text` and `image_url` parts.
Otherwise, null.

chat\_completion\_content\_part\_text: object { text, type }

Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

text: string

The text content.

type: "text"

The type of the content part.

chat\_completion\_content\_part\_image: object { image\_url, type }

Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

image\_url: object { url, detail }

url: string

Either a URL of the image or the base64 encoded image data.

detail: optional "auto" or "low" or "high"

Specifies the detail level of the image. Learn more in the [Vision guide](https://platform.openai.com/docs/guides/vision#low-or-high-fidelity-image-understanding).

"auto"

"low"

"high"

type: "image\_url"

The type of the content part.

first\_id: string

The identifier of the first chat message in the data array.

has\_more: boolean

Indicates whether there are more chat messages available.

last\_id: string

The identifier of the last chat message in the data array.

object: "list"

The type of this object. It is always set to “list”.

### Get chat messages

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai chat:completions:messages list \
  --api-key 'My API Key' \
  --completion-id completion_id

  "object": "list",
  "data": [
      "id": "chatcmpl-AyPNinnUqUDYo9SAdA52NobMflmj2-0",
      "role": "user",
      "content": "write a haiku about ai",
      "name": null,
      "content_parts": null
  ],
  "first_id": "chatcmpl-AyPNinnUqUDYo9SAdA52NobMflmj2-0",
  "last_id": "chatcmpl-AyPNinnUqUDYo9SAdA52NobMflmj2-0",
  "has_more": false

##### Returns Examples

  "object": "list",
  "data": [
      "id": "chatcmpl-AyPNinnUqUDYo9SAdA52NobMflmj2-0",
      "role": "user",
      "content": "write a haiku about ai",
      "name": null,
      "content_parts": null
  ],
  "first_id": "chatcmpl-AyPNinnUqUDYo9SAdA52NobMflmj2-0",
  "last_id": "chatcmpl-AyPNinnUqUDYo9SAdA52NobMflmj2-0",
  "has_more": false
