<!-- source: https://developers.openai.com/api/reference/cli/resources/live/subresources/sessions/ -->

# Sessions

## Accept call

`$ openai live:sessions accept`

**post** `/live/sessions/{session_id}/accept`

Accept an incoming SIP call. Supply session with type live, the model, and startup configuration. Before accepting calls, follow the [Live prompting guide](/api/docs/guides/live-prompting) to write frontend conversation instructions and a separate backend prompt. SIP media format is negotiated; omit audio.format.

### Parameters

- `--session-id: string`

  Opaque Live session identifier from the creation response or incoming-call webhook. Preserve the returned value unchanged, including its prefix.

- `--session: object { model, type, audio, 4 more }`

  Model and startup configuration for the Live session that answers the incoming SIP call.

### Example

```cli
openai live:sessions accept \
  --api-key 'My API Key' \
  --session-id session_id \
  --session '{model: gpt-live-1, type: live}'
```

## Download recording

`$ openai live:sessions download-recording`

**get** `/live/sessions/{session_id}/content`

Get Live session content

### Parameters

- `--session-id: string`

  The ID of the stored Live session to download. Use the session ID returned when the session started with storage enabled.

### Returns

- `unnamed_schema_2: file path`

### Example

```cli
openai live:sessions download-recording \
  --api-key 'My API Key' \
  --session-id live_SQ
```

## Fork session

`$ openai live:sessions fork`

**post** `/live/sessions/{session_id}/fork`

Fork a stored Live session onto a new WebRTC connection.

### Parameters

- `--session-id: string`

  The ID of the stored Live session to fork.

- `--transport: object { sdp, type }`

  WebRTC transport with an SDP offer for the new connection to the forked session.

- `--session: optional object { client, delegation, store }`

  Optional configuration overrides for the new Live session. Omit this object or send an empty object to inherit the stored session's settings.

### Returns

- `SessionForkResponse: object { session, transport }`

  The created Live session identifier and WebRTC answer. Apply transport.sdp as the peer's remote answer and wait for session.started on the data channel before sending commands.

  - `session: object { id }`

    The newly created Live session. Use its ID for session controls and sideband connections.

    - `id: string`

      Opaque session identifier. Preserve the returned value unchanged, including its prefix.

  - `transport: object { sdp, type }`

    WebRTC transport with the SDP answer.

    - `sdp: string`

      Session Description Protocol message for the WebRTC connection.

    - `type: "webrtc"`

      The transport used for the Live session. Always `webrtc`.

### Example

```cli
openai live:sessions fork \
  --api-key 'My API Key' \
  --session-id session_id \
  --transport '{sdp: x, type: webrtc}'
```

#### Response

```json
{
  "session": {
    "id": "id"
  },
  "transport": {
    "sdp": "x",
    "type": "webrtc"
  }
}
```

## Hang up session

`$ openai live:sessions hangup`

**post** `/live/sessions/{session_id}/hangup`

End a SIP call identified by session_id.

### Parameters

- `--session-id: string`

  Opaque Live session identifier from the creation response or incoming-call webhook. Preserve the returned value unchanged, including its prefix.

### Example

```cli
openai live:sessions hangup \
  --api-key 'My API Key' \
  --session-id session_id
```

## Transfer call

`$ openai live:sessions refer`

**post** `/live/sessions/{session_id}/refer`

Transfer a SIP call to another destination. Supply a nonblank target_uri for the SIP Refer-To header.

### Parameters

- `--session-id: string`

  Opaque Live session identifier from the creation response or incoming-call webhook. Preserve the returned value unchanged, including its prefix.

- `--target-uri: string`

  Nonblank URI for the SIP Refer-To header, such as tel:+14155550123 or sip:agent@example.com.

### Example

```cli
openai live:sessions refer \
  --api-key 'My API Key' \
  --session-id session_id \
  --target-uri tel:+14155550123
```

## Reject call

`$ openai live:sessions reject`

**post** `/live/sessions/{session_id}/reject`

Reject an incoming SIP call. Send a required SIP rejection status_code between 300 and 699.

### Parameters

- `--session-id: string`

  Opaque Live session identifier from the creation response or incoming-call webhook. Preserve the returned value unchanged, including its prefix.

- `--status-code: number`

  SIP rejection status sent to the caller. This field is required.

### Example

```cli
openai live:sessions reject \
  --api-key 'My API Key' \
  --session-id session_id \
  --status-code 486
```
