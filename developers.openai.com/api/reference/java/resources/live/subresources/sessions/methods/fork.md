<!-- source: https://developers.openai.com/api/reference/java/resources/live/subresources/sessions/methods/fork/ -->

## Fork session

`SessionForkResponse live().sessions().fork(SessionForkParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/live/sessions/{session_id}/fork`

Fork a stored Live session onto a new WebRTC connection.

- `SessionForkParams params`

  - `Optional<String> sessionId`

  - `Transport transport`

    WebRTC transport with an SDP offer for the new connection to the forked session.

    - `String sdp`

      Session Description Protocol message for the WebRTC connection.

    - `JsonValue; type "webrtc"constant`

      The transport used for the Live session. Always `webrtc`.

      - `WEBRTC("webrtc")`

  - `Optional<MediaSessionForkConfig> session`

    Optional configuration overrides for the new Live session. Omit this object or send an empty object to inherit the stored session's settings.

- `class SessionForkResponse:`

  The created Live session identifier and WebRTC answer. Apply transport.sdp as the peer's remote answer and wait for session.started on the data channel before sending commands.

  - `Session session`

    The newly created Live session. Use its ID for session controls and sideband connections.

    - `String id`

      Opaque session identifier. Preserve the returned value unchanged, including its prefix.

  - `Transport transport`

    WebRTC transport with the SDP answer.

    - `String sdp`

      Session Description Protocol message for the WebRTC connection.

    - `JsonValue; type "webrtc"constant`

      The transport used for the Live session. Always `webrtc`.

      - `WEBRTC("webrtc")`

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.live.sessions.SessionForkParams;
import com.openai.models.live.sessions.SessionForkResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        SessionForkParams params = SessionForkParams.builder()
            .sessionId("session_id")
            .transport(SessionForkParams.Transport.builder()
                .sdp("x")
                .build())
            .build();
        SessionForkResponse response = client.live().sessions().fork(params);

  "session": {
    "id": "id"
  "transport": {
    "sdp": "x",
    "type": "webrtc"
