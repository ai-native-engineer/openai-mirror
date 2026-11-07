<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/subresources/sessions/subresources/traces/ -->

# Traces

## List agent session traces

`TraceListPage beta().agents().sessions().traces().list(TraceListParamsparams = TraceListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/sessions/{session_id}/traces`

Lists published root-turn traces as OTLP JSON, ordered by turn creation time and ID. Unpublished traces are skipped. Each page returns data available when read; it does not wait for late traces. Trace reads and the JSON response are limited to 16 MiB per request. If the limit is exceeded, request fewer traces.

### Parameters

- `TraceListParams params`

  - `Optional<String> sessionId`

    `minLength: 0`, `maxLength: 1048576`

  - `Optional<String> after`

    Return resources after this resource ID in the selected order.

    `minLength: 0`, `maxLength: 1048576`

  - `Optional<Long> limit`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

    `format: int64`, `minimum: 1`, `maximum: 100`

  - `Optional<Order> order`

    The order in which resources are returned. Defaults to `desc`.

    - `ASC("asc")`

      Returns resources in ascending order.

    - `DESC("desc")`

      Returns resources in descending order.

### Returns

- `class SessionTrace:`

  - `String id`

    The root turn ID. Use this ID as the pagination anchor.

    `minLength: 0`

  - `long createdAt`

    The Unix timestamp in seconds when the root turn was created.

    `format: int64`

  - `JsonValue; object_ "agent.session.trace"constant`

    The object type, which is always `agent.session.trace`.

    - `AGENT_SESSION_TRACE("agent.session.trace")`

  - `Otlp otlp`

    An OTLP JSON ExportTraceServiceRequest containing resourceSpans. Only currently published data is returned; later trace updates are not awaited.

  - `String sessionId`

    The session that owns this trace.

    `minLength: 0`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.sessions.traces.TraceListPage;
import com.openai.models.beta.agents.sessions.traces.TraceListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        TraceListPage page = client.beta().agents().sessions().traces().list("session_id");
    }
}
```

#### 200 — Example

```json
{
  "data": [
    {
      "id": "id",
      "created_at": 0,
      "object": "agent.session.trace",
      "otlp": {
        "foo": "bar"
      },
      "session_id": "session_id"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Domain Types

### Session Trace

- `class SessionTrace:`

  - `String id`

    The root turn ID. Use this ID as the pagination anchor.

    `minLength: 0`

  - `long createdAt`

    The Unix timestamp in seconds when the root turn was created.

    `format: int64`

  - `JsonValue; object_ "agent.session.trace"constant`

    The object type, which is always `agent.session.trace`.

    - `AGENT_SESSION_TRACE("agent.session.trace")`

  - `Otlp otlp`

    An OTLP JSON ExportTraceServiceRequest containing resourceSpans. Only currently published data is returned; later trace updates are not awaited.

  - `String sessionId`

    The session that owns this trace.

    `minLength: 0`
