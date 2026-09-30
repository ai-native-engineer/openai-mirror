<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/subresources/environments/methods/retrieve/ -->

## Retrieve an agent environment

`EnvironmentInfo beta().agents().environments().retrieve(EnvironmentRetrieveParamsparams = EnvironmentRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/environments/{environment_id}`

Retrieves an execution environment's connection status and safe installed metadata. See [environment lifecycle](/api/docs/guides/agents-api/environments/lifecycle).

- `EnvironmentRetrieveParams params`

  - `Optional<String> environmentId`

- `class EnvironmentInfo:`

  Safe metadata for a first-class execution environment.

  - `String id`

    The ID of the environment.

  - `List<HostedEnvironmentFile> files`

    Files installed in the environment, without their contents.

    - `class HostedEnvironmentFileId:`

      A file copied from the OpenAI Files API.

      - `String id`

        The session-scoped ID of the file in the execution environment.

      - `String fileId`

        The ID of the uploaded file.

      - `String path`

        The file's absolute path inside the environment.

      - `long sizeBytes`

        The decoded file size in bytes.

      - `JsonValue; type "file_id"constant`

        The type of the object. Always `file_id`.

        - `FILE_ID("file_id")`

    - `Inline`

      - `String id`

        The session-scoped ID of the file in the execution environment.

      - `String path`

        The file's absolute path inside the environment.

      - `long sizeBytes`

        The decoded file size in bytes.

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

  - `JsonValue; object_ "agent.environment"constant`

    The object type. Always `agent.environment`.

    - `AGENT_ENVIRONMENT("agent.environment")`

  - `List<HostedPlugin> plugins`

    Plugins installed in the environment, without their archive contents.

    - `String description`

      The installed plugin description.

    - `String name`

      The installed plugin name.

    - `JsonValue; type "inline"constant`

      The type of the object. Always `inline`.

      - `INLINE("inline")`

  - `List<HostedSkill> skills`

    Skills installed in the environment, without their archive contents.

    - `class HostedSkillReference:`

      A skill installed from the Skills API.

      - `String description`

        The installed skill description.

      - `String name`

        The installed skill name.

      - `String skillId`

        The referenced skill ID.

      - `JsonValue; type "skill_reference"constant`

        The type of the object. Always `skill_reference`.

        - `SKILL_REFERENCE("skill_reference")`

      - `String version`

        The concrete skill version installed for this session.

    - `Inline`

      - `String description`

        The installed skill description.

      - `String name`

        The installed skill name.

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

  - `Status status`

    The current environment connection status.

    - `PENDING("pending")`

    - `CONNECTED("connected")`

    - `DISCONNECTED("disconnected")`

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
import com.openai.models.beta.agents.environments.EnvironmentInfo;
import com.openai.models.beta.agents.environments.EnvironmentRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        EnvironmentInfo environmentInfo = client.beta().agents().environments().retrieve("environment_id");

  "files": [
      "file_id": "file_id",
      "path": "path",
      "size_bytes": 0,
      "type": "file_id"
  "object": "agent.environment",
  "plugins": [
      "description": "description",
      "type": "inline"
  "skills": [
      "description": "description",
      "skill_id": "skill_id",
      "type": "skill_reference",
      "version": "version"
  "status": "pending",
  "type": "openai_hosted"
