<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/subresources/sessions/subresources/artifacts/methods/content/ -->

## Retrieve agent session artifact content

`HttpResponse beta().agents().sessions().artifacts().content(ArtifactContentParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/sessions/{session_id}/artifacts/{artifact_id}/content`

Downloads immutable session artifact bytes after the execution environment expires. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

- `ArtifactContentParams params`

  - `String sessionId`

  - `Optional<String> artifactId`

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.core.http.HttpResponse;
import com.openai.models.beta.agents.sessions.artifacts.ArtifactContentParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ArtifactContentParams params = ArtifactContentParams.builder()
            .sessionId("session_id")
            .artifactId("artifact_id")
            .build();
        HttpResponse response = client.beta().agents().sessions().artifacts().content(params);
