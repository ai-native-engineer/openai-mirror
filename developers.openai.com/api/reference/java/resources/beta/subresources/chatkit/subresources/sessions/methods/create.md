<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/chatkit/subresources/sessions/methods/create/ -->

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

# Create ChatKit session

[ChatSession](/api/reference/java/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session%20%3E%20(schema)) beta().chatkit().sessions().create(SessionCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/chatkit/sessions

Create a ChatKit session.

##### ParametersExpand Collapse

SessionCreateParams params

String user

A free-form string that identifies your end user; ensures this Session can access other objects that have the same `user` scope.

minLength1

[ChatSessionWorkflowParam](/api/reference/java/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_workflow_param%20%3E%20(schema)) workflow

Workflow that powers the session.

Optional<[ChatSessionChatKitConfigurationParam](/api/reference/java/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_chatkit_configuration_param%20%3E%20(schema))> chatkitConfiguration

Optional overrides for ChatKit runtime configuration features

Optional<[ChatSessionExpiresAfterParam](/api/reference/java/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_expires_after_param%20%3E%20(schema))> expiresAfter

Optional override for session expiration timing in seconds from creation. Defaults to 10 minutes.

Optional<[ChatSessionRateLimitsParam](/api/reference/java/resources/beta#(resource)%20beta.chatkit.threads%20%3E%20(model)%20chat_session_rate_limits_param%20%3E%20(schema))> rateLimits

Optional override for per-minute request limits. When omitted, defaults to 10.

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

### Create ChatKit session

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
import com.openai.models.beta.chatkit.sessions.SessionCreateParams;
import com.openai.models.beta.chatkit.threads.ChatSession;
import com.openai.models.beta.chatkit.threads.ChatSessionWorkflowParam;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        SessionCreateParams params = SessionCreateParams.builder()
            .user("user")
            .workflow(ChatSessionWorkflowParam.builder()
                .id("id")
                .build())
            .build();
        ChatSession chatSession = client.beta().chatkit().sessions().create(params);

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
