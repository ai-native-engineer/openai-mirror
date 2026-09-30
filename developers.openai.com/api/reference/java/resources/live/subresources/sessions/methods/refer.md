<!-- source: https://developers.openai.com/api/reference/java/resources/live/subresources/sessions/methods/refer/ -->

## Transfer call

`live().sessions().refer(SessionReferParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/live/sessions/{session_id}/refer`

Transfer a SIP call to another destination. Supply a nonblank target_uri for the SIP Refer-To header.

- `SessionReferParams params`

  - `Optional<String> sessionId`

  - `String targetUri`

    Nonblank URI for the SIP Refer-To header, such as tel:+14155550123 or sip:agent@example.com.

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.live.sessions.SessionReferParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        SessionReferParams params = SessionReferParams.builder()
            .sessionId("session_id")
            .targetUri("tel:+14155550123")
            .build();
        client.live().sessions().refer(params);
