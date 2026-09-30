<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/subresources/environments/subresources/files/methods/list/ -->

## List agent environment files

`FileListPage beta().agents().environments().files().list(FileListParamsparams = FileListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/environments/{environment_id}/files`

Lists live files on a connected execution environment with optional directory filtering and opaque cursor pagination. See [environment files](/api/docs/guides/agents-api/environments/files).

- `FileListParams params`

  - `Optional<String> environmentId`

  - `Optional<Long> limit`

    The maximum number of files to return, between 1 and 100.

  - `Optional<Order> order`

    Sort by case-sensitive path components. Defaults to descending.

    - `ASC("asc")`

      Returns resources in ascending order.

    - `DESC("desc")`

      Returns resources in descending order.

  - `Optional<String> page`

    The opaque token from the previous page. Keep the same path, order, and limit.

  - `Optional<String> path`

    Restrict the listing to this absolute workspace directory.

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
import com.openai.models.beta.agents.environments.files.FileListPage;
import com.openai.models.beta.agents.environments.files.FileListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FileListPage page = client.beta().agents().environments().files().list("environment_id");

  "data": [
      "environment_id": "environment_id",
      "object": "agent.environment.file",
      "path": "path",
      "size_bytes": 0
  "has_more": true,
  "next": "next",
  "object": "page"
