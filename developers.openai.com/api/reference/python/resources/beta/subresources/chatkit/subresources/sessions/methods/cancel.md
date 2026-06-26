<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/chatkit/subresources/sessions/methods/cancel/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Beta](/api/reference/python/resources/beta)

[ChatKit](/api/reference/python/resources/beta/subresources/chatkit)

[Sessions](/api/reference/python/resources/beta/subresources/chatkit/subresources/sessions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Cancel chat session

beta.chatkit.sessions.cancel(strsession\_id)  -> [ChatSession](/api/reference/python/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema))

POST/chatkit/sessions/{session\_id}/cancel

Cancel an active ChatKit session and return its most recent metadata.

Cancelling prevents new requests from using the issued client secret.

##### ParametersExpand Collapse

session\_id: str

##### ReturnsExpand Collapse

class ChatSession: …

Represents a ChatKit session and its resolved configuration.

id: str

Identifier for the ChatKit session.

chatkit\_configuration: [ChatSessionChatKitConfiguration](/api/reference/python/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration%20%3E%20(schema))

Resolved ChatKit feature configuration for the session.

automatic\_thread\_titling: [ChatSessionAutomaticThreadTitling](/api/reference/python/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_automatic_thread_titling%20%3E%20(schema))

Automatic thread titling preferences.

enabled: bool

Whether automatic thread titling is enabled.

file\_upload: [ChatSessionFileUpload](/api/reference/python/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_file_upload%20%3E%20(schema))

Upload settings for the session.

enabled: bool

Indicates if uploads are enabled for the session.

max\_file\_size: Optional[int]

Maximum upload size in megabytes.

max\_files: Optional[int]

Maximum number of uploads allowed during the session.

history: [ChatSessionHistory](/api/reference/python/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_history%20%3E%20(schema))

History retention configuration.

enabled: bool

Indicates if chat history is persisted for the session.

recent\_threads: Optional[int]

Number of prior threads surfaced in history views. Defaults to null when all history is retained.

client\_secret: str

Ephemeral client secret that authenticates session requests.

expires\_at: int

Unix timestamp (in seconds) for when the session expires.

formatunixtime

max\_requests\_per\_1\_minute: int

Convenience copy of the per-minute request limit.

object: Literal["chatkit.session"]

Type discriminator that is always `chatkit.session`.

rate\_limits: [ChatSessionRateLimits](/api/reference/python/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_rate_limits%20%3E%20(schema))

Resolved rate limit values.

max\_requests\_per\_1\_minute: int

Maximum allowed requests per one-minute window.

status: [ChatSessionStatus](/api/reference/python/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_status%20%3E%20(schema))

Current lifecycle state of the session.

One of the following:

"active"

"expired"

"cancelled"

user: str

User identifier associated with the session.

workflow: [ChatKitWorkflow](/api/reference/python/resources/beta#(resource)%20beta.chatkit%20%3E%20(model)%20chatkit_workflow%20%3E%20(schema))

Workflow metadata for the session.

id: str

Identifier of the workflow backing the session.

state\_variables: Optional[Dict[str, Union[str, bool, float]]]

State variable key-value pairs applied when invoking the workflow. Defaults to null when no overrides were provided.

One of the following:

str

bool

float

tracing: Tracing

Tracing settings applied to the workflow.

enabled: bool

Indicates whether tracing is enabled.

version: Optional[str]

Specific workflow version used for the session. Defaults to null when using the latest deployment.

### Cancel chat session

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
chat_session = client.beta.chatkit.sessions.cancel(
    "cksess_123",
print(chat_session.id)

  "id": "cksess_123",
  "object": "chatkit.session",
  "workflow": {
    "id": "workflow_alpha",
    "version": "1"
  "scope": {
    "customer_id": "cust_456"
  "max_requests_per_1_minute": 30,
  "ttl_seconds": 900,
  "status": "cancelled",
  "cancelled_at": 1712345678

##### Returns Examples

  "id": "cksess_123",
  "object": "chatkit.session",
  "workflow": {
    "id": "workflow_alpha",
    "version": "1"
  "scope": {
    "customer_id": "cust_456"
  "max_requests_per_1_minute": 30,
  "ttl_seconds": 900,
  "status": "cancelled",
  "cancelled_at": 1712345678
