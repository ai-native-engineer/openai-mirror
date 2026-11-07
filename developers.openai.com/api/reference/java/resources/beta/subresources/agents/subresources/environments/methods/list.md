<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/subresources/environments/methods/list/ -->

## List agent environments

`EnvironmentListPage beta().agents().environments().list(EnvironmentListParamsparams = EnvironmentListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/environments`

Lists OpenAI-hosted environments owned by the authenticated principal. Requires access to the prewarming beta.

- `EnvironmentListParams params`

  - `Optional<String> after`

    Return resources after this resource ID in the selected order.

    `minLength: 0`, `maxLength: 1048576`

  - `Optional<Long> limit`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

    `format: int64`, `minimum: 1`, `maximum: 100`

  - `Optional<Order> order`

    The order in which resources are returned. Defaults to `desc`.

    - `ASC("asc")`

      Returns resources in ascending order.

    - `DESC("desc")`

      Returns resources in descending order.

  - `Optional<Type> type`

    The hosting type to list. Defaults to `openai_hosted`.

    - `OPENAI_HOSTED("openai_hosted")`

- `class EnvironmentInfo:`

  Safe metadata for a first-class execution environment.

  - `String id`

    The ID of the environment.

    `minLength: 0`

  - `List<HostedEnvironmentFile> files`

    Files installed in the environment, without their contents.

    `minItems: 0`, `maxItems: 2000`

    - `class HostedEnvironmentFileId:`

      A file copied from the OpenAI Files API.

      - `String id`

        The session-scoped ID of the file in the execution environment.

        `minLength: 0`

      - `String fileId`

        The ID of the uploaded file.

        `minLength: 0`

      - `String path`

        The file's absolute path inside the environment.

        `minLength: 0`

      - `long sizeBytes`

        The decoded file size in bytes.

        `format: int64`, `minimum: 0`

      - `JsonValue; type "file_id"constant`

        The type of the object. Always `file_id`.

        - `FILE_ID("file_id")`

    - `Inline`

      - `String id`

        The session-scoped ID of the file in the execution environment.

        `minLength: 0`

      - `String path`

        The file's absolute path inside the environment.

        `minLength: 0`

      - `long sizeBytes`

        The decoded file size in bytes.

        `format: int64`, `minimum: 0`

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

  - `JsonValue; object_ "agent.environment"constant`

    The object type. Always `agent.environment`.

    - `AGENT_ENVIRONMENT("agent.environment")`

  - `List<HostedPlugin> plugins`

    Plugins installed in the environment, without their archive contents.

    `minItems: 0`, `maxItems: 2000`

    - `String description`

      The installed plugin description.

      `minLength: 0`

    - `String name`

      The installed plugin name.

      `minLength: 0`

    - `JsonValue; type "inline"constant`

      The type of the object. Always `inline`.

      - `INLINE("inline")`

  - `List<HostedSkill> skills`

    Skills installed in the environment, without their archive contents.

    `minItems: 0`, `maxItems: 2000`

    - `class HostedSkillReference:`

      A skill installed from the Skills API.

      - `String description`

        The installed skill description.

        `minLength: 0`

      - `String name`

        The installed skill name.

        `minLength: 0`

      - `String skillId`

        The referenced skill ID.

        `minLength: 0`

      - `JsonValue; type "skill_reference"constant`

        The type of the object. Always `skill_reference`.

        - `SKILL_REFERENCE("skill_reference")`

      - `String version`

        The concrete skill version installed for this session.

        `minLength: 0`

    - `Inline`

      - `String description`

        The installed skill description.

        `minLength: 0`

      - `String name`

        The installed skill name.

        `minLength: 0`

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

  - `Status status`

    The current environment connection status.

    - `PENDING("pending")`

    - `READY("ready")`

      Provisioning succeeded and the environment is available for attachment or use.

    - `CONNECTED("connected")`

    - `DISCONNECTED("disconnected")`

    - `SUSPENDED("suspended")`

      The sandbox is stopped and can be resumed from its private checkpoint.

    - `EXPIRED("expired")`

    - `FAILED("failed")`

  - `Type type`

    Whether the environment is hosted by OpenAI or by the application.

    - `OPENAI_HOSTED("openai_hosted")`

    - `SELF_HOSTED("self_hosted")`

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.environments.EnvironmentListPage;
import com.openai.models.beta.agents.environments.EnvironmentListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        EnvironmentListPage page = client.beta().agents().environments().list();

  "data": [
      "files": [
          "file_id": "file_id",
          "path": "path",
          "size_bytes": 0,
          "type": "file_id"
      "object": "agent.environment",
      "plugins": [
          "type": "inline"
      "skills": [
          "skill_id": "skill_id",
          "type": "skill_reference",
          "version": "version"
      "status": "pending",
      "type": "openai_hosted"
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
