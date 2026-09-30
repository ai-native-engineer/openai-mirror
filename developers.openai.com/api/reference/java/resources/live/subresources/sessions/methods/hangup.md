<!-- source: https://developers.openai.com/api/reference/java/resources/live/subresources/sessions/methods/hangup/ -->

## Hang up session

`live().sessions().hangup(SessionHangupParamsparams = SessionHangupParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/live/sessions/{session_id}/hangup`

End a SIP call identified by session_id.

- `SessionHangupParams params`

  - `Optional<String> sessionId`

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.live.sessions.SessionHangupParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        client.live().sessions().hangup("session_id");
