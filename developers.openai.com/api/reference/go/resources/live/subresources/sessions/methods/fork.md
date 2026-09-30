<!-- source: https://developers.openai.com/api/reference/go/resources/live/subresources/sessions/methods/fork/ -->

## Fork session

`client.Live.Sessions.Fork(ctx, sessionID, body) (*SessionForkResponse, error)`

**post** `/live/sessions/{session_id}/fork`

Fork a stored Live session onto a new WebRTC connection.

- `sessionID string`

- `body SessionForkParams`

  - `Transport param.Field[SessionForkParamsTransport]`

    WebRTC transport with an SDP offer for the new connection to the forked session.

    - `Sdp string`

      Session Description Protocol message for the WebRTC connection.

    - `Type Webrtc`

      The transport used for the Live session. Always `webrtc`.

      - `const WebrtcWebrtc Webrtc = "webrtc"`

  - `Session param.Field[MediaSessionForkConfig]`

    Optional configuration overrides for the new Live session. Omit this object or send an empty object to inherit the stored session's settings.

- `type SessionForkResponse struct{…}`

  The created Live session identifier and WebRTC answer. Apply transport.sdp as the peer's remote answer and wait for session.started on the data channel before sending commands.

  - `Session SessionForkResponseSession`

    The newly created Live session. Use its ID for session controls and sideband connections.

    - `ID string`

      Opaque session identifier. Preserve the returned value unchanged, including its prefix.

  - `Transport SessionForkResponseTransport`

    WebRTC transport with the SDP answer.

    - `Sdp string`

      Session Description Protocol message for the WebRTC connection.

    - `Type Webrtc`

      The transport used for the Live session. Always `webrtc`.

      - `const WebrtcWebrtc Webrtc = "webrtc"`

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/live"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  response, err := client.Live.Sessions.Fork(
    context.TODO(),
    "session_id",
    live.SessionForkParams{
      Transport: live.SessionForkParamsTransport{
        Sdp: "x",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", response.Session)

  "session": {
    "id": "id"
  "transport": {
    "sdp": "x",
    "type": "webrtc"
