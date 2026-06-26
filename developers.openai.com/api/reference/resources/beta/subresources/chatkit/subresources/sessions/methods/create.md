<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/chatkit/subresources/sessions/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Beta](/api/reference/resources/beta)

[ChatKit](/api/reference/resources/beta/subresources/chatkit)

[Sessions](/api/reference/resources/beta/subresources/chatkit/subresources/sessions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create ChatKit session

POST/chatkit/sessions

Create a ChatKit session.

##### Body ParametersJSONExpand Collapse

user: string

A free-form string that identifies your end user; ensures this Session can access other objects that have the same `user` scope.

minLength1

workflow: [ChatSessionWorkflowParam](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_workflow_param%20%3E%20(schema)) { id, state\_variables, tracing, version }

Workflow that powers the session.

id: string

Identifier for the workflow invoked by the session.

state\_variables: optional map[string or boolean or number]

State variables forwarded to the workflow. Keys may be up to 64 characters, values must be primitive types, and the map defaults to an empty object.

One of the following:

string

boolean

number

tracing: optional object { enabled }

Optional tracing overrides for the workflow invocation. When omitted, tracing is enabled by default.

enabled: optional boolean

Whether tracing is enabled during the session. Defaults to true.

version: optional string

Specific workflow version to run. Defaults to the latest deployed version.

chatkit\_configuration: optional [ChatSessionChatKitConfigurationParam](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration_param%20%3E%20(schema)) { automatic\_thread\_titling, file\_upload, history }

Optional overrides for ChatKit runtime configuration features

automatic\_thread\_titling: optional object { enabled }

Configuration for automatic thread titling. When omitted, automatic thread titling is enabled by default.

enabled: optional boolean

Enable automatic thread title generation. Defaults to true.

file\_upload: optional object { enabled, max\_file\_size, max\_files }

Configuration for upload enablement and limits. When omitted, uploads are disabled by default (max\_files 10, max\_file\_size 512 MB).

enabled: optional boolean

Enable uploads for this session. Defaults to false.

max\_file\_size: optional number

Maximum size in megabytes for each uploaded file. Defaults to 512 MB, which is the maximum allowable size.

maximum512

minimum1

max\_files: optional number

Maximum number of files that can be uploaded to the session. Defaults to 10.

minimum1

history: optional object { enabled, recent\_threads }

Configuration for chat history retention. When omitted, history is enabled by default with no limit on recent\_threads (null).

enabled: optional boolean

Enables chat users to access previous ChatKit threads. Defaults to true.

recent\_threads: optional number

Number of recent ChatKit threads users have access to. Defaults to unlimited when unset.

minimum1

expires\_after: optional [ChatSessionExpiresAfterParam](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_expires_after_param%20%3E%20(schema)) { anchor, seconds }

Optional override for session expiration timing in seconds from creation. Defaults to 10 minutes.

anchor: "created\_at"

Base timestamp used to calculate expiration. Currently fixed to `created_at`.

seconds: number

Number of seconds after the anchor when the session expires.

maximum600

minimum1

formatint64

rate\_limits: optional [ChatSessionRateLimitsParam](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_rate_limits_param%20%3E%20(schema)) { max\_requests\_per\_1\_minute }

Optional override for per-minute request limits. When omitted, defaults to 10.

max\_requests\_per\_1\_minute: optional number

Maximum number of requests allowed per minute for the session. Defaults to 10.

minimum1

##### ReturnsExpand Collapse

ChatSession object { id, chatkit\_configuration, client\_secret, 7 more }

Represents a ChatKit session and its resolved configuration.

id: string

Identifier for the ChatKit session.

chatkit\_configuration: [ChatSessionChatKitConfiguration](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration%20%3E%20(schema)) { automatic\_thread\_titling, file\_upload, history }

Resolved ChatKit feature configuration for the session.

automatic\_thread\_titling: [ChatSessionAutomaticThreadTitling](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_automatic_thread_titling%20%3E%20(schema)) { enabled }

Automatic thread titling preferences.

enabled: boolean

Whether automatic thread titling is enabled.

file\_upload: [ChatSessionFileUpload](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_file_upload%20%3E%20(schema)) { enabled, max\_file\_size, max\_files }

Upload settings for the session.

enabled: boolean

Indicates if uploads are enabled for the session.

max\_file\_size: number

Maximum upload size in megabytes.

max\_files: number

Maximum number of uploads allowed during the session.

history: [ChatSessionHistory](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_history%20%3E%20(schema)) { enabled, recent\_threads }

History retention configuration.

enabled: boolean

Indicates if chat history is persisted for the session.

recent\_threads: number

Number of prior threads surfaced in history views. Defaults to null when all history is retained.

client\_secret: string

Ephemeral client secret that authenticates session requests.

expires\_at: number

Unix timestamp (in seconds) for when the session expires.

formatunixtime

max\_requests\_per\_1\_minute: number

Convenience copy of the per-minute request limit.

object: "chatkit.session"

Type discriminator that is always `chatkit.session`.

rate\_limits: [ChatSessionRateLimits](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_rate_limits%20%3E%20(schema)) { max\_requests\_per\_1\_minute }

Resolved rate limit values.

max\_requests\_per\_1\_minute: number

Maximum allowed requests per one-minute window.

status: [ChatSessionStatus](/api/reference/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_status%20%3E%20(schema))

Current lifecycle state of the session.

One of the following:

"active"

"expired"

"cancelled"

user: string

User identifier associated with the session.

workflow: [ChatKitWorkflow](/api/reference/resources/beta#(resource)%20beta.chatkit%20%3E%20(model)%20chatkit_workflow%20%3E%20(schema)) { id, state\_variables, tracing, version }

Workflow metadata for the session.

id: string

Identifier of the workflow backing the session.

state\_variables: map[string or boolean or number]

State variable key-value pairs applied when invoking the workflow. Defaults to null when no overrides were provided.

One of the following:

string

boolean

number

tracing: object { enabled }

Tracing settings applied to the workflow.

enabled: boolean

Indicates whether tracing is enabled.

version: string

Specific workflow version used for the session. Defaults to null when using the latest deployment.

### Create ChatKit session

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/chatkit/sessions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "OpenAI-Beta: chatkit_beta=v1" \
  -d '{
    "workflow": {
      "id": "workflow_alpha",
      "version": "2024-10-01"
    "scope": {
      "project": "alpha",
      "environment": "staging"
    "expires_after": 1800,
    "max_requests_per_1_minute": 60,
    "max_requests_per_session": 500
  }'

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
