<!-- source: https://developers.openai.com/api/reference/cli/resources/beta/subresources/chatkit/subresources/sessions/methods/create/ -->

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

# Create ChatKit session

$ openai beta:chatkit:sessions create

POST/chatkit/sessions

Create a ChatKit session.

##### ParametersExpand Collapse

--user: string

A free-form string that identifies your end user; ensures this Session can access other objects that have the same `user` scope.

--workflow: object { id, state\_variables, tracing, version }

Workflow that powers the session.

--chatkit-configuration: optional object { automatic\_thread\_titling, file\_upload, history }

Optional overrides for ChatKit runtime configuration features

--expires-after: optional object { anchor, seconds }

Optional override for session expiration timing in seconds from creation. Defaults to 10 minutes.

--rate-limits: optional object { max\_requests\_per\_1\_minute }

Optional override for per-minute request limits. When omitted, defaults to 10.

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

### Create ChatKit session

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai beta:chatkit:sessions create \
  --api-key 'My API Key' \
  --user x \
  --workflow '{id: id}'

  "client_secret": "chatkit_token_123",
  "expires_at": 1735689600,
  "workflow": {
    "id": "workflow_alpha",
    "version": "2024-10-01"
  "scope": {
    "project": "alpha",
    "environment": "staging"
  "max_requests_per_1_minute": 60,
  "max_requests_per_session": 500,
  "status": "active"

##### Returns Examples

  "client_secret": "chatkit_token_123",
  "expires_at": 1735689600,
  "workflow": {
    "id": "workflow_alpha",
    "version": "2024-10-01"
  "scope": {
    "project": "alpha",
    "environment": "staging"
  "max_requests_per_1_minute": 60,
  "max_requests_per_session": 500,
  "status": "active"
