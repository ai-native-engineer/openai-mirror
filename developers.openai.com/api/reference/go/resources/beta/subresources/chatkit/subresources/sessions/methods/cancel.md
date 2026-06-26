<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/chatkit/subresources/sessions/methods/cancel/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Beta](/api/reference/go/resources/beta)

[ChatKit](/api/reference/go/resources/beta/subresources/chatkit)

[Sessions](/api/reference/go/resources/beta/subresources/chatkit/subresources/sessions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Cancel chat session

client.Beta.ChatKit.Sessions.Cancel(ctx, sessionID) (\*[ChatSession](/api/reference/go/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)), error)

POST/chatkit/sessions/{session\_id}/cancel

Cancel an active ChatKit session and return its most recent metadata.

Cancelling prevents new requests from using the issued client secret.

##### ParametersExpand Collapse

sessionID string

##### ReturnsExpand Collapse

type ChatSession struct{…}

Represents a ChatKit session and its resolved configuration.

ID string

Identifier for the ChatKit session.

ChatKitConfiguration [ChatSessionChatKitConfiguration](/api/reference/go/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration%20%3E%20(schema))

Resolved ChatKit feature configuration for the session.

AutomaticThreadTitling [ChatSessionAutomaticThreadTitling](/api/reference/go/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_automatic_thread_titling%20%3E%20(schema))

Automatic thread titling preferences.

Enabled bool

Whether automatic thread titling is enabled.

FileUpload [ChatSessionFileUpload](/api/reference/go/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_file_upload%20%3E%20(schema))

Upload settings for the session.

Enabled bool

Indicates if uploads are enabled for the session.

MaxFileSize int64

Maximum upload size in megabytes.

MaxFiles int64

Maximum number of uploads allowed during the session.

History [ChatSessionHistory](/api/reference/go/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_history%20%3E%20(schema))

History retention configuration.

Enabled bool

Indicates if chat history is persisted for the session.

RecentThreads int64

Number of prior threads surfaced in history views. Defaults to null when all history is retained.

ClientSecret string

Ephemeral client secret that authenticates session requests.

ExpiresAt int64

Unix timestamp (in seconds) for when the session expires.

formatunixtime

MaxRequestsPer1Minute int64

Convenience copy of the per-minute request limit.

Object ChatKitSession

Type discriminator that is always `chatkit.session`.

RateLimits [ChatSessionRateLimits](/api/reference/go/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_rate_limits%20%3E%20(schema))

Resolved rate limit values.

MaxRequestsPer1Minute int64

Maximum allowed requests per one-minute window.

Status [ChatSessionStatus](/api/reference/go/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_status%20%3E%20(schema))

Current lifecycle state of the session.

One of the following:

const ChatSessionStatusActive [ChatSessionStatus](/api/reference/go/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_status%20%3E%20(schema)) = "active"

const ChatSessionStatusExpired [ChatSessionStatus](/api/reference/go/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_status%20%3E%20(schema)) = "expired"

const ChatSessionStatusCancelled [ChatSessionStatus](/api/reference/go/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_status%20%3E%20(schema)) = "cancelled"

User string

User identifier associated with the session.

Workflow [ChatKitWorkflow](/api/reference/go/resources/beta#(resource)%20beta.chatkit%20%3E%20(model)%20chatkit_workflow%20%3E%20(schema))

Workflow metadata for the session.

ID string

Identifier of the workflow backing the session.

StateVariables map[string, ChatKitWorkflowStateVariableUnion]

State variable key-value pairs applied when invoking the workflow. Defaults to null when no overrides were provided.

One of the following:

string

bool

float64

Tracing ChatKitWorkflowTracing

Tracing settings applied to the workflow.

Enabled bool

Indicates whether tracing is enabled.

Version string

Specific workflow version used for the session. Defaults to null when using the latest deployment.

### Cancel chat session

Go

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient()
  chatSession, err := client.Beta.ChatKit.Sessions.Cancel(context.TODO(), "cksess_123")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", chatSession.ID)

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
