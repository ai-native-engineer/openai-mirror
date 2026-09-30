<!-- source: https://developers.openai.com/api/reference/java/resources/live/subresources/sessions/methods/reject/ -->

## Reject call

`live().sessions().reject(SessionRejectParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/live/sessions/{session_id}/reject`

Reject an incoming SIP call. Send a required SIP rejection status_code between 300 and 699.

- `SessionRejectParams params`

  - `Optional<String> sessionId`

  - `long statusCode`

    SIP rejection status sent to the caller. This field is required.

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.live.sessions.SessionRejectParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        SessionRejectParams params = SessionRejectParams.builder()
            .sessionId("session_id")
            .statusCode(486L)
            .build();
        client.live().sessions().reject(params);
