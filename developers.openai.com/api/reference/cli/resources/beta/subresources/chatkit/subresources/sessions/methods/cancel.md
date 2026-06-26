<!-- source: https://developers.openai.com/api/reference/cli/resources/beta/subresources/chatkit/subresources/sessions/methods/cancel/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Beta](/api/reference/cli/resources/beta)

[ChatKit](/api/reference/cli/resources/beta/subresources/chatkit)

[Sessions](/api/reference/cli/resources/beta/subresources/chatkit/subresources/sessions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Cancel chat session

$ openai beta:chatkit:sessions cancel

POST/chatkit/sessions/{session\_id}/cancel

Cancel an active ChatKit session and return its most recent metadata.

Cancelling prevents new requests from using the issued client secret.

##### ParametersExpand Collapse

--session-id: string

Unique identifier for the ChatKit session to cancel.

##### ReturnsExpand Collapse

chat\_session: object { id, chatkit\_configuration, client\_secret, 7 more }

Represents a ChatKit session and its resolved configuration.

id: string

Identifier for the ChatKit session.

chatkit\_configuration: object { automatic\_thread\_titling, file\_upload, history }

Resolved ChatKit feature configuration for the session.

automatic\_thread\_titling: object { enabled }

Automatic thread titling preferences.

enabled: boolean

Whether automatic thread titling is enabled.

file\_upload: object { enabled, max\_file\_size, max\_files }

Upload settings for the session.

enabled: boolean

Indicates if uploads are enabled for the session.

max\_file\_size: number

Maximum upload size in megabytes.

max\_files: number

Maximum number of uploads allowed during the session.

history: object { enabled, recent\_threads }

History retention configuration.

enabled: boolean

Indicates if chat history is persisted for the session.

recent\_threads: number

Number of prior threads surfaced in history views. Defaults to null when all history is retained.

client\_secret: string

Ephemeral client secret that authenticates session requests.

expires\_at: number

Unix timestamp (in seconds) for when the session expires.

max\_requests\_per\_1\_minute: number

Convenience copy of the per-minute request limit.

object: "chatkit.session"

Type discriminator that is always `chatkit.session`.

rate\_limits: object { max\_requests\_per\_1\_minute }

Resolved rate limit values.

max\_requests\_per\_1\_minute: number

Maximum allowed requests per one-minute window.

status: "active" or "expired" or "cancelled"

Current lifecycle state of the session.

"active"

"expired"

"cancelled"

user: string

User identifier associated with the session.

workflow: object { id, state\_variables, tracing, version }

Workflow metadata for the session.

id: string

Identifier of the workflow backing the session.

state\_variables: map[string or boolean or number]

State variable key-value pairs applied when invoking the workflow. Defaults to null when no overrides were provided.

union\_member\_0: string

union\_member\_1: boolean

union\_member\_2: number

tracing: object { enabled }

Tracing settings applied to the workflow.

enabled: boolean

Indicates whether tracing is enabled.

version: string

Specific workflow version used for the session. Defaults to null when using the latest deployment.

### Cancel chat session

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai beta:chatkit:sessions cancel \
  --api-key 'My API Key' \
  --session-id cksess_123

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
