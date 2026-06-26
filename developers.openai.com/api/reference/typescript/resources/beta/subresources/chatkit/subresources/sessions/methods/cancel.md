<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/chatkit/subresources/sessions/methods/cancel/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Beta](/api/reference/typescript/resources/beta)

[ChatKit](/api/reference/typescript/resources/beta/subresources/chatkit)

[Sessions](/api/reference/typescript/resources/beta/subresources/chatkit/subresources/sessions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Cancel chat session

client.beta.chatkit.sessions.cancel(stringsessionID, RequestOptionsoptions?): [ChatSession](/api/reference/typescript/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)) { id, chatkit\_configuration, client\_secret, 7 more }

POST/chatkit/sessions/{session\_id}/cancel

Cancel an active ChatKit session and return its most recent metadata.

Cancelling prevents new requests from using the issued client secret.

##### ParametersExpand Collapse

sessionID: string

##### ReturnsExpand Collapse

ChatSession { id, chatkit\_configuration, client\_secret, 7 more }

Represents a ChatKit session and its resolved configuration.

id: string

Identifier for the ChatKit session.

chatkit\_configuration: [ChatSessionChatKitConfiguration](/api/reference/typescript/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration%20%3E%20(schema)) { automatic\_thread\_titling, file\_upload, history }

Resolved ChatKit feature configuration for the session.

automatic\_thread\_titling: [ChatSessionAutomaticThreadTitling](/api/reference/typescript/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_automatic_thread_titling%20%3E%20(schema)) { enabled }

Automatic thread titling preferences.

enabled: boolean

Whether automatic thread titling is enabled.

file\_upload: [ChatSessionFileUpload](/api/reference/typescript/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_file_upload%20%3E%20(schema)) { enabled, max\_file\_size, max\_files }

Upload settings for the session.

enabled: boolean

Indicates if uploads are enabled for the session.

max\_file\_size: number | null

Maximum upload size in megabytes.

max\_files: number | null

Maximum number of uploads allowed during the session.

history: [ChatSessionHistory](/api/reference/typescript/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_history%20%3E%20(schema)) { enabled, recent\_threads }

History retention configuration.

enabled: boolean

Indicates if chat history is persisted for the session.

recent\_threads: number | null

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

rate\_limits: [ChatSessionRateLimits](/api/reference/typescript/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_rate_limits%20%3E%20(schema)) { max\_requests\_per\_1\_minute }

Resolved rate limit values.

max\_requests\_per\_1\_minute: number

Maximum allowed requests per one-minute window.

status: [ChatSessionStatus](/api/reference/typescript/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_status%20%3E%20(schema))

Current lifecycle state of the session.

One of the following:

"active"

"expired"

"cancelled"

user: string

User identifier associated with the session.

workflow: [ChatKitWorkflow](/api/reference/typescript/resources/beta#(resource)%20beta.chatkit%20%3E%20(model)%20chatkit_workflow%20%3E%20(schema)) { id, state\_variables, tracing, version }

Workflow metadata for the session.

id: string

Identifier of the workflow backing the session.

state\_variables: Record<string, string | boolean | number> | null

State variable key-value pairs applied when invoking the workflow. Defaults to null when no overrides were provided.

One of the following:

string

boolean

number

tracing: Tracing { enabled }

Tracing settings applied to the workflow.

enabled: boolean

Indicates whether tracing is enabled.

version: string | null

Specific workflow version used for the session. Defaults to null when using the latest deployment.

### Cancel chat session

TypeScript

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import OpenAI from 'openai';

const client = new OpenAI();

const chatSession = await client.beta.chatkit.sessions.cancel('cksess_123');

console.log(chatSession.id);

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
