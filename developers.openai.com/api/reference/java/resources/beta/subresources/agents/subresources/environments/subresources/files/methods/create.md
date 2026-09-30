<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/subresources/environments/subresources/files/methods/create/ -->

## Create an agent environment file

`EnvironmentFile beta().agents().environments().files().create(FileCreateParamsparams = FileCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/agents/environments/{environment_id}/files`

Copies inline bytes or a Files API file into a connected execution environment. See [environment files](/api/docs/guides/agents-api/environments/files).

- `FileCreateParams params`

  - `Optional<String> environmentId`

  - `Optional<HostedEnvironmentFileParam> hostedEnvironmentFileParam`

    A file materialized in an OpenAI-hosted execution environment.

- `class EnvironmentFile:`

  A live file in an execution environment.

  - `String environmentId`

    The ID of the environment containing this file.

  - `JsonValue; object_ "agent.environment.file"constant`

    The object type. Always `agent.environment.file`.

    - `AGENT_ENVIRONMENT_FILE("agent.environment.file")`

  - `String path`

    The absolute file path inside the environment's workspace.

  - `long sizeBytes`

    The file size in bytes.

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.environments.files.EnvironmentFile;
import com.openai.models.beta.agents.environments.files.FileCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        EnvironmentFile environmentFile = client.beta().agents().environments().files().create("environment_id");

  "environment_id": "environment_id",
  "object": "agent.environment.file",
  "path": "path",
  "size_bytes": 0
