<!-- source: https://developers.openai.com/api/reference/resources/conversations/methods/update/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Conversations](/api/reference/resources/conversations)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Update a conversation

POST/conversations/{conversation\_id}

Update a conversation

##### Path ParametersExpand Collapse

conversation\_id: string

##### Body ParametersJSONExpand Collapse

metadata: [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

##### ReturnsExpand Collapse

Conversation object { id, created\_at, metadata, object }

id: string

The unique ID of the conversation.

created\_at: number

The time at which the conversation was created, measured in seconds since the Unix epoch.

formatunixtime

metadata: unknown

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format, and querying for objects via API or the dashboard.
Keys are strings with a maximum length of 64 characters. Values are strings with a maximum length of 512 characters.

object: "conversation"

The object type, which is always `conversation`.

### Update a conversation

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/conversations/conv_123 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "metadata": {"topic": "project-x"}
  }'

  "id": "conv_123",
  "object": "conversation",
  "created_at": 1741900000,
  "metadata": {"topic": "project-x"}

##### Returns Examples

  "id": "conv_123",
  "object": "conversation",
  "created_at": 1741900000,
  "metadata": {"topic": "project-x"}
