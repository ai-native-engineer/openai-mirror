<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/subresources/environments/methods/create/ -->

## Create an agent environment

`EnvironmentInfo beta().agents().environments().create(EnvironmentCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/agents/environments`

Creates an OpenAI-hosted environment before creating a session. Requires access to the prewarming beta.

- `EnvironmentCreateParams params`

  - `Optional<String> idempotencyKey`

    `minLength: 1`, `maxLength: 256`

  - `Environment environment`

    The required hosting type and its configuration.

    - `JsonValue; type "openai_hosted"constant`

      The type of the object. Always `openai_hosted`.

      - `OPENAI_HOSTED("openai_hosted")`

    - `Optional<List<String>> capabilityDirectories`

      Directories that contain capabilities exposed to the agent. Defaults to an empty list.

      `minItems: 0`, `maxItems: 16384`

    - `Optional<Desktop> desktop`

      Desktop provisioning. Omission or null inherits the template setting, or defaults to disabled.

      - `boolean enabled`

        Whether to provision the desktop and its browser proxy.

    - `Optional<Env> env`

      Environment variables made available to the agent.

    - `Optional<String> environmentTemplateId`

      A reusable hosted template applied before inline configuration. Omitted fields inherit the template; network overrides cannot broaden its policy.

      `minLength: 0`, `maxLength: 64`

    - `Optional<List<HostedEnvironmentFileParam>> files`

      Files available before the agent starts. Defaults to an empty list.

      `minItems: 0`, `maxItems: 50`

      - `FileId`

        - `String fileId`

          The ID of the uploaded file.

          `minLength: 1`, `maxLength: 256`

        - `String path`

          The absolute destination path inside `/workspace`.

          `minLength: 1`, `maxLength: 4096`

        - `JsonValue; type "file_id"constant`

          The type of the object. Always `file_id`.

          - `FILE_ID("file_id")`

      - `Inline`

        - `String data`

          The standard-base64-encoded file contents.

          `minLength: 0`, `maxLength: 6990508`

        - `String path`

          The absolute destination path inside `/workspace`.

          `minLength: 1`, `maxLength: 4096`

        - `JsonValue; type "inline"constant`

          The type of the object. Always `inline`.

          - `INLINE("inline")`

    - `Optional<Network> network`

      Network access policy for the environment. If omitted, the API version determines whether network access is enabled or disabled.

      - `Access access`

        The environment's network access mode.

        - `ENABLED("enabled")`

          Allows unrestricted network access.

        - `DISABLED("disabled")`

          Disables network access.

        - `RESTRICTED("restricted")`

          Applies the configured domain restrictions.

      - `Optional<List<String>> allowedDomains`

        Domains the environment may access when network access is restricted.

        `minItems: 0`, `maxItems: 16384`

      - `Optional<List<String>> blockedDomains`

        Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

        `minItems: 0`, `maxItems: 100`

    - `Optional<Packages> packages`

      Packages to install in the environment. Defaults to empty package lists.

      - `Optional<List<String>> npm`

        npm packages to install globally. Defaults to an empty list.

        `minItems: 0`, `maxItems: 16384`

      - `Optional<List<String>> python`

        Python packages to install. Defaults to an empty list.

        `minItems: 0`, `maxItems: 16384`

      - `Optional<List<String>> system`

        System packages to install. Defaults to an empty list.

        `minItems: 0`, `maxItems: 16384`

    - `Optional<List<HostedPluginParam>> plugins`

      Plugins provided as inline ZIP archives. Defaults to an empty list.

      `minItems: 0`, `maxItems: 32`

      - `String description`

        The plugin description declared in `.codex-plugin/plugin.json`.

        `minLength: 0`, `maxLength: 1048576`

      - `String name`

        The plugin name declared in `.codex-plugin/plugin.json`.

        `minLength: 1`, `maxLength: 64`

      - `InlineCapabilitySourceParam source`

        Provides ZIP bytes encoded with standard base64.

        - `String data`

          Standard-base64 encoded ZIP archive bytes.

          `minLength: 1`, `maxLength: 70254592`

        - `JsonValue; mediaType "application/zip"constant`

          The archive media type, always `application/zip`.

          - `APPLICATION_ZIP("application/zip")`

        - `JsonValue; type "base64"constant`

          The type of the object. Always `base64`.

          - `BASE64("base64")`

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

    - `Optional<List<SetupCommandParam>> setupCommands`

      Ordered, confidential setup commands. Command bodies are never returned.

      `minItems: 0`, `maxItems: 16`

      - `String command`

        The shell command to execute.

        `minLength: 0`, `maxLength: 65536`

      - `Optional<String> cwd`

        The absolute working directory. Defaults to `/workspace`.

        `minLength: 0`, `maxLength: 4096`

    - `Optional<List<HostedSkillParam>> skills`

      Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

      `minItems: 0`, `maxItems: 200`

      - `SkillReference`

        - `String skillId`

          The ID of the skill created through `/v1/skills`.

          `minLength: 1`, `maxLength: 64`

        - `JsonValue; type "skill_reference"constant`

          The type of the object. Always `skill_reference`.

          - `SKILL_REFERENCE("skill_reference")`

        - `Optional<String> version`

          The skill version, a positive integer or `latest`; omission selects the default.

          `minLength: 0`, `maxLength: 1048576`

      - `Inline`

        - `String description`

          The skill description declared in `SKILL.md`.

          `minLength: 0`, `maxLength: 1048576`

        - `String name`

          The skill name declared in `SKILL.md`.

          `minLength: 1`, `maxLength: 64`

        - `InlineCapabilitySourceParam source`

          Provides ZIP bytes encoded with standard base64.

        - `JsonValue; type "inline"constant`

          The type of the object. Always `inline`.

          - `INLINE("inline")`

  - `Optional<List<String>> vaultIds`

    The IDs of up to 10 vaults made available to an OpenAI-hosted environment.

    `minItems: 0`, `maxItems: 10`

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
import com.openai.models.beta.agents.environments.EnvironmentCreateParams;
import com.openai.models.beta.agents.environments.EnvironmentInfo;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        EnvironmentCreateParams params = EnvironmentCreateParams.builder()
            .environment(EnvironmentCreateParams.Environment.builder().build())
            .build();
        EnvironmentInfo environmentInfo = client.beta().agents().environments().create(params);

#### 201 — Example

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
