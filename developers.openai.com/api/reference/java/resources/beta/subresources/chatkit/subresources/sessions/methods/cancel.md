<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/chatkit/subresources/sessions/methods/cancel/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Beta](/api/reference/java/resources/beta)

[ChatKit](/api/reference/java/resources/beta/subresources/chatkit)

[Sessions](/api/reference/java/resources/beta/subresources/chatkit/subresources/sessions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Cancel chat session

[ChatSession](/api/reference/java/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)) beta().chatkit().sessions().cancel(SessionCancelParamsparams = SessionCancelParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/chatkit/sessions/{session\_id}/cancel

Cancel an active ChatKit session and return its most recent metadata.

Cancelling prevents new requests from using the issued client secret.

##### ParametersExpand Collapse

SessionCancelParams params

Optional<String> sessionId

##### ReturnsExpand Collapse

class ChatSession:

Represents a ChatKit session and its resolved configuration.

String id

Identifier for the ChatKit session.

[ChatSessionChatKitConfiguration](/api/reference/java/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration%20%3E%20(schema)) chatkitConfiguration

Resolved ChatKit feature configuration for the session.

[ChatSessionAutomaticThreadTitling](/api/reference/java/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_automatic_thread_titling%20%3E%20(schema)) automaticThreadTitling

Automatic thread titling preferences.

boolean enabled

Whether automatic thread titling is enabled.

[ChatSessionFileUpload](/api/reference/java/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_file_upload%20%3E%20(schema)) fileUpload

Upload settings for the session.

boolean enabled

Indicates if uploads are enabled for the session.

Optional<Long> maxFileSize

Maximum upload size in megabytes.

Optional<Long> maxFiles

Maximum number of uploads allowed during the session.

[ChatSessionHistory](/api/reference/java/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_history%20%3E%20(schema)) history

History retention configuration.

boolean enabled

Indicates if chat history is persisted for the session.

Optional<Long> recentThreads

Number of prior threads surfaced in history views. Defaults to null when all history is retained.

String clientSecret

Ephemeral client secret that authenticates session requests.

long expiresAt

Unix timestamp (in seconds) for when the session expires.

formatunixtime

long maxRequestsPer1Minute

Convenience copy of the per-minute request limit.

JsonValue; object\_ "chatkit.session"constant"chatkit.session"constant

Type discriminator that is always `chatkit.session`.

[ChatSessionRateLimits](/api/reference/java/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_rate_limits%20%3E%20(schema)) rateLimits

Resolved rate limit values.

long maxRequestsPer1Minute

Maximum allowed requests per one-minute window.

[ChatSessionStatus](/api/reference/java/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_status%20%3E%20(schema)) status

Current lifecycle state of the session.

One of the following:

ACTIVE("active")

EXPIRED("expired")

CANCELLED("cancelled")

String user

User identifier associated with the session.

[ChatKitWorkflow](/api/reference/java/resources/beta#(resource)%20beta.chatkit%20%3E%20(model)%20chatkit_workflow%20%3E%20(schema)) workflow

Workflow metadata for the session.

String id

Identifier of the workflow backing the session.

Optional<StateVariables> stateVariables

State variable key-value pairs applied when invoking the workflow. Defaults to null when no overrides were provided.

One of the following:

String

boolean

double

Tracing tracing

Tracing settings applied to the workflow.

boolean enabled

Indicates whether tracing is enabled.

Optional<String> version

Specific workflow version used for the session. Defaults to null when using the latest deployment.

### Cancel chat session

Java

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.chatkit.sessions.SessionCancelParams;
import com.openai.models.beta.chatkit.threads.ChatSession;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ChatSession chatSession = client.beta().chatkit().sessions().cancel("cksess_123");

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
