<!-- source: https://developers.openai.com/api/reference/cli/resources/live/subresources/sessions/methods/fork/ -->

## Fork session

`$ openai live:sessions fork`

**post** `/live/sessions/{session_id}/fork`

Fork a stored Live session onto a new WebRTC connection.

- `--session-id: string`

  The ID of the stored Live session to fork.

- `--transport: object { sdp, type }`

  WebRTC transport with an SDP offer for the new connection to the forked session.

- `--session: optional object { client, delegation, store }`

  Optional configuration overrides for the new Live session. Omit this object or send an empty object to inherit the stored session's settings.

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

```cli
openai live:sessions fork \
  --api-key 'My API Key' \
  --session-id session_id \
  --transport '{sdp: x, type: webrtc}'

  "session": {
    "id": "id"
  "transport": {
    "sdp": "x",
    "type": "webrtc"
