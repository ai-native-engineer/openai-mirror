<!-- source: https://developers.openai.com/api/reference/python/resources/conversations/methods/update/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Conversations](/api/reference/python/resources/conversations)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Update a conversation

conversations.update(strconversation\_id, ConversationUpdateParams\*\*kwargs)  -> [Conversation](/api/reference/python/resources/conversations#(resource)%20conversations%20%3E%20(model)%20conversation%20%3E%20(schema))

POST/conversations/{conversation\_id}

Update a conversation

##### ParametersExpand Collapse

conversation\_id: str

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

##### ReturnsExpand Collapse

class Conversation: …

id: str

The unique ID of the conversation.

created\_at: int

The time at which the conversation was created, measured in seconds since the Unix epoch.

formatunixtime

metadata: object

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format, and querying for objects via API or the dashboard.
Keys are strings with a maximum length of 64 characters. Values are strings with a maximum length of 512 characters.

object: Literal["conversation"]

The object type, which is always `conversation`.

### Update a conversation

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

from openai import OpenAI
client = OpenAI()

updated = client.conversations.update(
  "conv_123",
  metadata={"topic": "project-x"}
print(updated)

  "id": "conv_123",
  "object": "conversation",
  "created_at": 1741900000,
  "metadata": {"topic": "project-x"}

##### Returns Examples

  "id": "conv_123",
  "object": "conversation",
  "created_at": 1741900000,
  "metadata": {"topic": "project-x"}
