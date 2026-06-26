<!-- source: https://developers.openai.com/api/reference/cli/resources/conversations/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Conversations](/api/reference/cli/resources/conversations)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve a conversation

$ openai conversations retrieve

GET/conversations/{conversation\_id}

Get a conversation

##### ParametersExpand Collapse

--conversation-id: string

The ID of the conversation to retrieve.

##### ReturnsExpand Collapse

conversation: object { id, created\_at, metadata, object }

id: string

The unique ID of the conversation.

created\_at: number

The time at which the conversation was created, measured in seconds since the Unix epoch.

metadata: unknown

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format, and querying for objects via API or the dashboard.
Keys are strings with a maximum length of 64 characters. Values are strings with a maximum length of 512 characters.

object: "conversation"

The object type, which is always `conversation`.

### Retrieve a conversation

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai conversations retrieve \
  --api-key 'My API Key' \
  --conversation-id conv_123

  "id": "conv_123",
  "object": "conversation",
  "created_at": 1741900000,
  "metadata": {"topic": "demo"}

##### Returns Examples

  "id": "conv_123",
  "object": "conversation",
  "created_at": 1741900000,
  "metadata": {"topic": "demo"}
