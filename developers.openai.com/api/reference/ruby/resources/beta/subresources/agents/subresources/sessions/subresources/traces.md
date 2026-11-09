<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/agents/subresources/sessions/subresources/traces/ -->

# Traces

## List agent session traces

`beta.agents.sessions.traces.list(session_id, **kwargs) -> CursorPage<SessionTrace>`

**get** `/agents/sessions/{session_id}/traces`

Lists published root-turn traces as OTLP JSON, ordered by turn creation time and ID. Unpublished traces are skipped. Each page returns data available when read; it does not wait for late traces. Trace reads and the JSON response are limited to 16 MiB per request. If the limit is exceeded, request fewer traces.

### Parameters

- `session_id: String`

  `minLength: 0`, `maxLength: 1048576`

- `after: String`

  Return resources after this resource ID in the selected order.

  `minLength: 0`, `maxLength: 1048576`

- `limit: Integer`

  The maximum number of resources to return, between 1 and 100. Defaults to 20.

  `format: int64`, `minimum: 1`, `maximum: 100`

- `order: :asc | :desc`

  The order in which resources are returned. Defaults to `desc`.

  - `:asc`

    Returns resources in ascending order.

  - `:desc`

    Returns resources in descending order.

### Returns

- `class SessionTrace`

  - `id: String`

    The root turn ID. Use this ID as the pagination anchor.

    `minLength: 0`

  - `created_at: Integer`

    The Unix timestamp in seconds when the root turn was created.

    `format: int64`

  - `object: :"agent.session.trace"`

    The object type, which is always `agent.session.trace`.

    - `:"agent.session.trace"`

  - `otlp: Hash[Symbol, untyped]`

    An OTLP JSON ExportTraceServiceRequest containing resourceSpans. Only currently published data is returned; later trace updates are not awaited.

  - `session_id: String`

    The session that owns this trace.

    `minLength: 0`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.beta.agents.sessions.traces.list("session_id")

puts(page)
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

- `class SessionTrace`

  - `id: String`

    The root turn ID. Use this ID as the pagination anchor.

    `minLength: 0`

  - `created_at: Integer`

    The Unix timestamp in seconds when the root turn was created.

    `format: int64`

  - `object: :"agent.session.trace"`

    The object type, which is always `agent.session.trace`.

    - `:"agent.session.trace"`

  - `otlp: Hash[Symbol, untyped]`

    An OTLP JSON ExportTraceServiceRequest containing resourceSpans. Only currently published data is returned; later trace updates are not awaited.

  - `session_id: String`

    The session that owns this trace.

    `minLength: 0`
