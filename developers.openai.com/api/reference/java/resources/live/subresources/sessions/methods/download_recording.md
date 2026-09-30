<!-- source: https://developers.openai.com/api/reference/java/resources/live/subresources/sessions/methods/download_recording/ -->

## Download recording

`HttpResponse live().sessions().downloadRecording(SessionDownloadRecordingParamsparams = SessionDownloadRecordingParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/live/sessions/{session_id}/content`

Get Live session content

- `SessionDownloadRecordingParams params`

  - `Optional<String> sessionId`

    The ID of the stored Live session to download. Use the session ID returned when the session started with storage enabled.

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.core.http.HttpResponse;
import com.openai.models.live.sessions.SessionDownloadRecordingParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        HttpResponse response = client.live().sessions().downloadRecording("live_SQ");
