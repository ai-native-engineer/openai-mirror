<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/subresources/environments/ -->

# Environments

## Retrieve an agent environment

`EnvironmentInfo beta().agents().environments().retrieve(EnvironmentRetrieveParamsparams = EnvironmentRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/environments/{environment_id}`

Retrieves an execution environment's connection status and safe installed metadata. See [environment lifecycle](/api/docs/guides/agents-api/environments/lifecycle).

### Parameters

- `EnvironmentRetrieveParams params`

  - `Optional<String> environmentId`

### Returns

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

### Example

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
    }
}
```

#### Response

```json
{
  "id": "id",
  "files": [
    {
      "id": "id",
      "file_id": "file_id",
      "path": "path",
      "size_bytes": 0,
      "type": "file_id"
    }
  ],
  "object": "agent.environment",
  "plugins": [
    {
      "description": "description",
      "name": "name",
      "type": "inline"
    }
  ],
  "skills": [
    {
      "description": "description",
      "name": "name",
      "skill_id": "skill_id",
      "type": "skill_reference",
      "version": "version"
    }
  ],
  "status": "pending",
  "type": "openai_hosted"
}
```

## Domain Types

### Environment Info

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

# Files

## Create an agent environment file

`EnvironmentFile beta().agents().environments().files().create(FileCreateParamsparams = FileCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/agents/environments/{environment_id}/files`

Copies inline bytes or a Files API file into a connected execution environment. See [environment files](/api/docs/guides/agents-api/environments/files).

### Parameters

- `FileCreateParams params`

  - `Optional<String> environmentId`

  - `Optional<HostedEnvironmentFileParam> hostedEnvironmentFileParam`

    A file materialized in an OpenAI-hosted execution environment.

### Returns

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

### Example

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
    }
}
```

#### Response

```json
{
  "environment_id": "environment_id",
  "object": "agent.environment.file",
  "path": "path",
  "size_bytes": 0
}
```

## List agent environment files

`FileListPage beta().agents().environments().files().list(FileListParamsparams = FileListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/environments/{environment_id}/files`

Lists live files on a connected execution environment with optional directory filtering and opaque cursor pagination. See [environment files](/api/docs/guides/agents-api/environments/files).

### Parameters

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

### Returns

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

### Example

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
    }
}
```

#### Response

```json
{
  "data": [
    {
      "environment_id": "environment_id",
      "object": "agent.environment.file",
      "path": "path",
      "size_bytes": 0
    }
  ],
  "has_more": true,
  "next": "next",
  "object": "page"
}
```

## Domain Types

### Environment File

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

# Templates

## Create an agent environment template

`EnvironmentTemplate beta().agents().environments().templates().create(TemplateCreateParamsparams = TemplateCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/agents/environments/templates`

Creates reusable environment configuration without returning confidential setup commands or environment values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `TemplateCreateParams params`

  - `Optional<List<String>> capabilityDirectories`

    Directories that contain capabilities exposed to the agent. Defaults to an empty list.

  - `Optional<Desktop> desktop`

    Desktop provisioning. Omission or null inherits the template setting, or defaults to disabled.

    - `boolean enabled`

      Whether to provision the desktop and its browser proxy.

  - `Optional<Env> env`

    Environment variables made available to the agent.

  - `Optional<List<HostedEnvironmentFileParam>> files`

    Files available before the agent starts. Defaults to an empty list.

    - `FileId`

      - `String fileId`

        The ID of the uploaded file.

      - `String path`

        The absolute destination path inside `/workspace`.

      - `JsonValue; type "file_id"constant`

        The type of the object. Always `file_id`.

        - `FILE_ID("file_id")`

    - `Inline`

      - `String data`

        The standard-base64-encoded file contents.

      - `String path`

        The absolute destination path inside `/workspace`.

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

  - `Optional<String> name`

    An optional human-readable display name for the template.

  - `Optional<Network> network`

    Network access policy for the environment. Defaults to disabled for GA requests and enabled for beta requests.

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

    - `Optional<List<String>> blockedDomains`

      Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

  - `Optional<Packages> packages`

    Packages to install in the environment. Defaults to empty package lists.

    - `Optional<List<String>> npm`

      npm packages to install globally. Defaults to an empty list.

    - `Optional<List<String>> python`

      Python packages to install. Defaults to an empty list.

    - `Optional<List<String>> system`

      System packages to install. Defaults to an empty list.

  - `Optional<List<HostedPluginParam>> plugins`

    Plugins provided as inline ZIP archives. Defaults to an empty list.

    - `String description`

      The plugin description declared in `.codex-plugin/plugin.json`.

    - `String name`

      The plugin name declared in `.codex-plugin/plugin.json`.

    - `InlineCapabilitySourceParam source`

      Provides ZIP bytes encoded with standard base64.

      - `String data`

        Standard-base64 encoded ZIP archive bytes.

      - `JsonValue; mediaType "application/zip"constant`

        The archive media type, always `application/zip`.

        - `APPLICATION_ZIP("application/zip")`

          A ZIP archive.

      - `JsonValue; type "base64"constant`

        The type of the object. Always `base64`.

        - `BASE64("base64")`

    - `JsonValue; type "inline"constant`

      The type of the object. Always `inline`.

      - `INLINE("inline")`

  - `Optional<List<SetupCommandParam>> setupCommands`

    Ordered, confidential setup commands. Command bodies are never returned.

    - `String command`

      The shell command to execute.

    - `Optional<String> cwd`

      The absolute working directory. Defaults to `/workspace`.

  - `Optional<List<HostedSkillParam>> skills`

    Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

    - `SkillReference`

      - `String skillId`

        The ID of the skill created through `/v1/skills`.

      - `JsonValue; type "skill_reference"constant`

        The type of the object. Always `skill_reference`.

        - `SKILL_REFERENCE("skill_reference")`

      - `Optional<String> version`

        The skill version, a positive integer or `latest`; omission selects the default.

    - `Inline`

      - `String description`

        The skill description declared in `SKILL.md`.

      - `String name`

        The skill name declared in `SKILL.md`.

      - `InlineCapabilitySourceParam source`

        Provides ZIP bytes encoded with standard base64.

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

### Returns

- `class EnvironmentTemplate:`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `String id`

    The ID of the reusable environment template.

  - `List<String> capabilityDirectories`

    Directories that expose capabilities to the agent.

  - `long createdAt`

    The Unix timestamp, in seconds, when the template was created.

  - `Desktop desktop`

    Desktop configuration for each OpenAI-hosted environment.

    - `boolean enabled`

      Whether the environment provisions a desktop and browser proxy.

  - `List<File> files`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `class FileId:`

      A project-scoped Files API reference resolved separately for each session.

      - `String fileId`

        The ID of the uploaded file.

      - `String path`

        The file's absolute path inside the environment.

      - `JsonValue; type "file_id"constant`

        The type of the object. Always `file_id`.

        - `FILE_ID("file_id")`

    - `class Inline:`

      Metadata for confidential inline file contents.

      - `String path`

        The file's absolute path inside the environment.

      - `long sizeBytes`

        The decoded size of the inline file in bytes.

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

  - `Optional<String> name`

    An optional human-readable display name for the template.

  - `Network network`

    Runtime network access for each OpenAI-hosted environment.

    - `Access access`

      The environment's network access mode.

      - `ENABLED("enabled")`

        Allows unrestricted network access.

      - `DISABLED("disabled")`

        Disables network access.

      - `RESTRICTED("restricted")`

        Applies the configured domain restrictions.

    - `List<String> allowedDomains`

      Domains the environment may access when network access is restricted.

  - `JsonValue; object_ "agent.environment.template"constant`

    The object type. Always `agent.environment.template`.

    - `AGENT_ENVIRONMENT_TEMPLATE("agent.environment.template")`

  - `Packages packages`

    Packages installed in each fresh OpenAI-hosted environment.

    - `List<String> npm`

      npm packages installed globally in the environment.

    - `List<String> python`

      Python packages installed in the environment.

    - `List<String> system`

      System packages installed in the environment.

  - `List<HostedPlugin> plugins`

    Safe plugin metadata, excluding inline archive contents.

    - `String description`

      The installed plugin description.

    - `String name`

      The installed plugin name.

    - `JsonValue; type "inline"constant`

      The type of the object. Always `inline`.

      - `INLINE("inline")`

  - `List<Skill> skills`

    Safe skill metadata, preserving unresolved version selectors.

    - `class SkillReference:`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `String skillId`

        The referenced skill ID.

      - `JsonValue; type "skill_reference"constant`

        The type of the object. Always `skill_reference`.

        - `SKILL_REFERENCE("skill_reference")`

      - `Optional<String> version`

        The requested version selector, including `latest`.

    - `class Inline:`

      Safe metadata for an inline skill archive.

      - `String description`

        The skill description declared in `SKILL.md`.

      - `String name`

        The skill name declared in `SKILL.md`.

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

  - `long updatedAt`

    The Unix timestamp, in seconds, when the template was last updated.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.environments.templates.EnvironmentTemplate;
import com.openai.models.beta.agents.environments.templates.TemplateCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        EnvironmentTemplate environmentTemplate = client.beta().agents().environments().templates().create();
    }
}
```

#### Response

```json
{
  "id": "id",
  "capability_directories": [
    "string"
  ],
  "created_at": 0,
  "desktop": {
    "enabled": true
  },
  "files": [
    {
      "file_id": "file_id",
      "path": "path",
      "type": "file_id"
    }
  ],
  "name": "name",
  "network": {
    "access": "enabled",
    "allowed_domains": [
      "string"
    ]
  },
  "object": "agent.environment.template",
  "packages": {
    "npm": [
      "string"
    ],
    "python": [
      "string"
    ],
    "system": [
      "string"
    ]
  },
  "plugins": [
    {
      "description": "description",
      "name": "name",
      "type": "inline"
    }
  ],
  "skills": [
    {
      "skill_id": "skill_id",
      "type": "skill_reference",
      "version": "version"
    }
  ],
  "updated_at": 0
}
```

## Delete an agent environment template

`EnvironmentTemplateDeleted beta().agents().environments().templates().delete(TemplateDeleteParamsparams = TemplateDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/agents/environments/templates/{environment_template_id}`

Deletes reusable environment configuration and all confidential template inputs. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `TemplateDeleteParams params`

  - `Optional<String> environmentTemplateId`

### Returns

- `class EnvironmentTemplateDeleted:`

  A deleted reusable environment template.

  - `String id`

    The ID of the deleted environment template.

  - `boolean deleted`

    Whether the environment template was deleted. Always `true`.

  - `JsonValue; object_ "agent.environment.template.deleted"constant`

    The object type. Always `agent.environment.template.deleted`.

    - `AGENT_ENVIRONMENT_TEMPLATE_DELETED("agent.environment.template.deleted")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.environments.templates.EnvironmentTemplateDeleted;
import com.openai.models.beta.agents.environments.templates.TemplateDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        EnvironmentTemplateDeleted environmentTemplateDeleted = client.beta().agents().environments().templates().delete("environment_template_id");
    }
}
```

#### Response

```json
{
  "id": "id",
  "deleted": true,
  "object": "agent.environment.template.deleted"
}
```

## List agent environment templates

`TemplateListPage beta().agents().environments().templates().list(TemplateListParamsparams = TemplateListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/environments/templates`

Lists reusable environment templates without returning confidential values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `TemplateListParams params`

  - `Optional<String> after`

    Return resources after this resource ID in the selected order.

  - `Optional<Long> limit`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

  - `Optional<Order> order`

    The order in which resources are returned. Defaults to `desc`.

    - `ASC("asc")`

      Returns resources in ascending order.

    - `DESC("desc")`

      Returns resources in descending order.

### Returns

- `class EnvironmentTemplate:`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `String id`

    The ID of the reusable environment template.

  - `List<String> capabilityDirectories`

    Directories that expose capabilities to the agent.

  - `long createdAt`

    The Unix timestamp, in seconds, when the template was created.

  - `Desktop desktop`

    Desktop configuration for each OpenAI-hosted environment.

    - `boolean enabled`

      Whether the environment provisions a desktop and browser proxy.

  - `List<File> files`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `class FileId:`

      A project-scoped Files API reference resolved separately for each session.

      - `String fileId`

        The ID of the uploaded file.

      - `String path`

        The file's absolute path inside the environment.

      - `JsonValue; type "file_id"constant`

        The type of the object. Always `file_id`.

        - `FILE_ID("file_id")`

    - `class Inline:`

      Metadata for confidential inline file contents.

      - `String path`

        The file's absolute path inside the environment.

      - `long sizeBytes`

        The decoded size of the inline file in bytes.

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

  - `Optional<String> name`

    An optional human-readable display name for the template.

  - `Network network`

    Runtime network access for each OpenAI-hosted environment.

    - `Access access`

      The environment's network access mode.

      - `ENABLED("enabled")`

        Allows unrestricted network access.

      - `DISABLED("disabled")`

        Disables network access.

      - `RESTRICTED("restricted")`

        Applies the configured domain restrictions.

    - `List<String> allowedDomains`

      Domains the environment may access when network access is restricted.

  - `JsonValue; object_ "agent.environment.template"constant`

    The object type. Always `agent.environment.template`.

    - `AGENT_ENVIRONMENT_TEMPLATE("agent.environment.template")`

  - `Packages packages`

    Packages installed in each fresh OpenAI-hosted environment.

    - `List<String> npm`

      npm packages installed globally in the environment.

    - `List<String> python`

      Python packages installed in the environment.

    - `List<String> system`

      System packages installed in the environment.

  - `List<HostedPlugin> plugins`

    Safe plugin metadata, excluding inline archive contents.

    - `String description`

      The installed plugin description.

    - `String name`

      The installed plugin name.

    - `JsonValue; type "inline"constant`

      The type of the object. Always `inline`.

      - `INLINE("inline")`

  - `List<Skill> skills`

    Safe skill metadata, preserving unresolved version selectors.

    - `class SkillReference:`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `String skillId`

        The referenced skill ID.

      - `JsonValue; type "skill_reference"constant`

        The type of the object. Always `skill_reference`.

        - `SKILL_REFERENCE("skill_reference")`

      - `Optional<String> version`

        The requested version selector, including `latest`.

    - `class Inline:`

      Safe metadata for an inline skill archive.

      - `String description`

        The skill description declared in `SKILL.md`.

      - `String name`

        The skill name declared in `SKILL.md`.

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

  - `long updatedAt`

    The Unix timestamp, in seconds, when the template was last updated.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.environments.templates.TemplateListPage;
import com.openai.models.beta.agents.environments.templates.TemplateListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        TemplateListPage page = client.beta().agents().environments().templates().list();
    }
}
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "capability_directories": [
        "string"
      ],
      "created_at": 0,
      "desktop": {
        "enabled": true
      },
      "files": [
        {
          "file_id": "file_id",
          "path": "path",
          "type": "file_id"
        }
      ],
      "name": "name",
      "network": {
        "access": "enabled",
        "allowed_domains": [
          "string"
        ]
      },
      "object": "agent.environment.template",
      "packages": {
        "npm": [
          "string"
        ],
        "python": [
          "string"
        ],
        "system": [
          "string"
        ]
      },
      "plugins": [
        {
          "description": "description",
          "name": "name",
          "type": "inline"
        }
      ],
      "skills": [
        {
          "skill_id": "skill_id",
          "type": "skill_reference",
          "version": "version"
        }
      ],
      "updated_at": 0
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve an agent environment template

`EnvironmentTemplate beta().agents().environments().templates().retrieve(TemplateRetrieveParamsparams = TemplateRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/environments/templates/{environment_template_id}`

Retrieves reusable environment configuration without returning confidential values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `TemplateRetrieveParams params`

  - `Optional<String> environmentTemplateId`

### Returns

- `class EnvironmentTemplate:`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `String id`

    The ID of the reusable environment template.

  - `List<String> capabilityDirectories`

    Directories that expose capabilities to the agent.

  - `long createdAt`

    The Unix timestamp, in seconds, when the template was created.

  - `Desktop desktop`

    Desktop configuration for each OpenAI-hosted environment.

    - `boolean enabled`

      Whether the environment provisions a desktop and browser proxy.

  - `List<File> files`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `class FileId:`

      A project-scoped Files API reference resolved separately for each session.

      - `String fileId`

        The ID of the uploaded file.

      - `String path`

        The file's absolute path inside the environment.

      - `JsonValue; type "file_id"constant`

        The type of the object. Always `file_id`.

        - `FILE_ID("file_id")`

    - `class Inline:`

      Metadata for confidential inline file contents.

      - `String path`

        The file's absolute path inside the environment.

      - `long sizeBytes`

        The decoded size of the inline file in bytes.

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

  - `Optional<String> name`

    An optional human-readable display name for the template.

  - `Network network`

    Runtime network access for each OpenAI-hosted environment.

    - `Access access`

      The environment's network access mode.

      - `ENABLED("enabled")`

        Allows unrestricted network access.

      - `DISABLED("disabled")`

        Disables network access.

      - `RESTRICTED("restricted")`

        Applies the configured domain restrictions.

    - `List<String> allowedDomains`

      Domains the environment may access when network access is restricted.

  - `JsonValue; object_ "agent.environment.template"constant`

    The object type. Always `agent.environment.template`.

    - `AGENT_ENVIRONMENT_TEMPLATE("agent.environment.template")`

  - `Packages packages`

    Packages installed in each fresh OpenAI-hosted environment.

    - `List<String> npm`

      npm packages installed globally in the environment.

    - `List<String> python`

      Python packages installed in the environment.

    - `List<String> system`

      System packages installed in the environment.

  - `List<HostedPlugin> plugins`

    Safe plugin metadata, excluding inline archive contents.

    - `String description`

      The installed plugin description.

    - `String name`

      The installed plugin name.

    - `JsonValue; type "inline"constant`

      The type of the object. Always `inline`.

      - `INLINE("inline")`

  - `List<Skill> skills`

    Safe skill metadata, preserving unresolved version selectors.

    - `class SkillReference:`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `String skillId`

        The referenced skill ID.

      - `JsonValue; type "skill_reference"constant`

        The type of the object. Always `skill_reference`.

        - `SKILL_REFERENCE("skill_reference")`

      - `Optional<String> version`

        The requested version selector, including `latest`.

    - `class Inline:`

      Safe metadata for an inline skill archive.

      - `String description`

        The skill description declared in `SKILL.md`.

      - `String name`

        The skill name declared in `SKILL.md`.

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

  - `long updatedAt`

    The Unix timestamp, in seconds, when the template was last updated.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.environments.templates.EnvironmentTemplate;
import com.openai.models.beta.agents.environments.templates.TemplateRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        EnvironmentTemplate environmentTemplate = client.beta().agents().environments().templates().retrieve("environment_template_id");
    }
}
```

#### Response

```json
{
  "id": "id",
  "capability_directories": [
    "string"
  ],
  "created_at": 0,
  "desktop": {
    "enabled": true
  },
  "files": [
    {
      "file_id": "file_id",
      "path": "path",
      "type": "file_id"
    }
  ],
  "name": "name",
  "network": {
    "access": "enabled",
    "allowed_domains": [
      "string"
    ]
  },
  "object": "agent.environment.template",
  "packages": {
    "npm": [
      "string"
    ],
    "python": [
      "string"
    ],
    "system": [
      "string"
    ]
  },
  "plugins": [
    {
      "description": "description",
      "name": "name",
      "type": "inline"
    }
  ],
  "skills": [
    {
      "skill_id": "skill_id",
      "type": "skill_reference",
      "version": "version"
    }
  ],
  "updated_at": 0
}
```

## Update an agent environment template

`EnvironmentTemplate beta().agents().environments().templates().update(TemplateUpdateParamsparams = TemplateUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/agents/environments/templates/{environment_template_id}`

Updates reusable environment configuration without returning confidential values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `TemplateUpdateParams params`

  - `Optional<String> environmentTemplateId`

  - `Optional<List<String>> capabilityDirectories`

    Directories that expose capabilities to the agent.

  - `Optional<Desktop> desktop`

    Replacement desktop configuration, or null to disable the desktop.

    - `boolean enabled`

      Whether to provision the desktop and its browser proxy.

  - `Optional<Env> env`

    Replacement confidential environment values.

  - `Optional<List<HostedEnvironmentFileParam>> files`

    Replacement file configuration materialized for each new session.

    - `FileId`

      - `String fileId`

        The ID of the uploaded file.

      - `String path`

        The absolute destination path inside `/workspace`.

      - `JsonValue; type "file_id"constant`

        The type of the object. Always `file_id`.

        - `FILE_ID("file_id")`

    - `Inline`

      - `String data`

        The standard-base64-encoded file contents.

      - `String path`

        The absolute destination path inside `/workspace`.

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

  - `Optional<String> name`

    A replacement human-readable display name, or `null` to clear the name.

  - `Optional<Network> network`

    Network access available after setup completes. Omit to preserve the current policy, or pass `null` to reset to disabled for GA requests or enabled for beta requests.

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

    - `Optional<List<String>> blockedDomains`

      Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

  - `Optional<Packages> packages`

    Packages installed before the runtime network policy applies.

    - `Optional<List<String>> npm`

      npm packages to install globally. Defaults to an empty list.

    - `Optional<List<String>> python`

      Python packages to install. Defaults to an empty list.

    - `Optional<List<String>> system`

      System packages to install. Defaults to an empty list.

  - `Optional<List<HostedPluginParam>> plugins`

    Replacement plugin configuration installed for each new session.

    - `String description`

      The plugin description declared in `.codex-plugin/plugin.json`.

    - `String name`

      The plugin name declared in `.codex-plugin/plugin.json`.

    - `InlineCapabilitySourceParam source`

      Provides ZIP bytes encoded with standard base64.

      - `String data`

        Standard-base64 encoded ZIP archive bytes.

      - `JsonValue; mediaType "application/zip"constant`

        The archive media type, always `application/zip`.

        - `APPLICATION_ZIP("application/zip")`

          A ZIP archive.

      - `JsonValue; type "base64"constant`

        The type of the object. Always `base64`.

        - `BASE64("base64")`

    - `JsonValue; type "inline"constant`

      The type of the object. Always `inline`.

      - `INLINE("inline")`

  - `Optional<List<SetupCommandParam>> setupCommands`

    Replacement confidential setup commands, never included in returned resources.

    - `String command`

      The shell command to execute.

    - `Optional<String> cwd`

      The absolute working directory. Defaults to `/workspace`.

  - `Optional<List<HostedSkillParam>> skills`

    Replacement skill configuration installed for each new session.

    - `SkillReference`

      - `String skillId`

        The ID of the skill created through `/v1/skills`.

      - `JsonValue; type "skill_reference"constant`

        The type of the object. Always `skill_reference`.

        - `SKILL_REFERENCE("skill_reference")`

      - `Optional<String> version`

        The skill version, a positive integer or `latest`; omission selects the default.

    - `Inline`

      - `String description`

        The skill description declared in `SKILL.md`.

      - `String name`

        The skill name declared in `SKILL.md`.

      - `InlineCapabilitySourceParam source`

        Provides ZIP bytes encoded with standard base64.

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

### Returns

- `class EnvironmentTemplate:`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `String id`

    The ID of the reusable environment template.

  - `List<String> capabilityDirectories`

    Directories that expose capabilities to the agent.

  - `long createdAt`

    The Unix timestamp, in seconds, when the template was created.

  - `Desktop desktop`

    Desktop configuration for each OpenAI-hosted environment.

    - `boolean enabled`

      Whether the environment provisions a desktop and browser proxy.

  - `List<File> files`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `class FileId:`

      A project-scoped Files API reference resolved separately for each session.

      - `String fileId`

        The ID of the uploaded file.

      - `String path`

        The file's absolute path inside the environment.

      - `JsonValue; type "file_id"constant`

        The type of the object. Always `file_id`.

        - `FILE_ID("file_id")`

    - `class Inline:`

      Metadata for confidential inline file contents.

      - `String path`

        The file's absolute path inside the environment.

      - `long sizeBytes`

        The decoded size of the inline file in bytes.

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

  - `Optional<String> name`

    An optional human-readable display name for the template.

  - `Network network`

    Runtime network access for each OpenAI-hosted environment.

    - `Access access`

      The environment's network access mode.

      - `ENABLED("enabled")`

        Allows unrestricted network access.

      - `DISABLED("disabled")`

        Disables network access.

      - `RESTRICTED("restricted")`

        Applies the configured domain restrictions.

    - `List<String> allowedDomains`

      Domains the environment may access when network access is restricted.

  - `JsonValue; object_ "agent.environment.template"constant`

    The object type. Always `agent.environment.template`.

    - `AGENT_ENVIRONMENT_TEMPLATE("agent.environment.template")`

  - `Packages packages`

    Packages installed in each fresh OpenAI-hosted environment.

    - `List<String> npm`

      npm packages installed globally in the environment.

    - `List<String> python`

      Python packages installed in the environment.

    - `List<String> system`

      System packages installed in the environment.

  - `List<HostedPlugin> plugins`

    Safe plugin metadata, excluding inline archive contents.

    - `String description`

      The installed plugin description.

    - `String name`

      The installed plugin name.

    - `JsonValue; type "inline"constant`

      The type of the object. Always `inline`.

      - `INLINE("inline")`

  - `List<Skill> skills`

    Safe skill metadata, preserving unresolved version selectors.

    - `class SkillReference:`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `String skillId`

        The referenced skill ID.

      - `JsonValue; type "skill_reference"constant`

        The type of the object. Always `skill_reference`.

        - `SKILL_REFERENCE("skill_reference")`

      - `Optional<String> version`

        The requested version selector, including `latest`.

    - `class Inline:`

      Safe metadata for an inline skill archive.

      - `String description`

        The skill description declared in `SKILL.md`.

      - `String name`

        The skill name declared in `SKILL.md`.

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

  - `long updatedAt`

    The Unix timestamp, in seconds, when the template was last updated.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.environments.templates.EnvironmentTemplate;
import com.openai.models.beta.agents.environments.templates.TemplateUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        EnvironmentTemplate environmentTemplate = client.beta().agents().environments().templates().update("environment_template_id");
    }
}
```

#### Response

```json
{
  "id": "id",
  "capability_directories": [
    "string"
  ],
  "created_at": 0,
  "desktop": {
    "enabled": true
  },
  "files": [
    {
      "file_id": "file_id",
      "path": "path",
      "type": "file_id"
    }
  ],
  "name": "name",
  "network": {
    "access": "enabled",
    "allowed_domains": [
      "string"
    ]
  },
  "object": "agent.environment.template",
  "packages": {
    "npm": [
      "string"
    ],
    "python": [
      "string"
    ],
    "system": [
      "string"
    ]
  },
  "plugins": [
    {
      "description": "description",
      "name": "name",
      "type": "inline"
    }
  ],
  "skills": [
    {
      "skill_id": "skill_id",
      "type": "skill_reference",
      "version": "version"
    }
  ],
  "updated_at": 0
}
```

## Domain Types

### Environment Template

- `class EnvironmentTemplate:`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `String id`

    The ID of the reusable environment template.

  - `List<String> capabilityDirectories`

    Directories that expose capabilities to the agent.

  - `long createdAt`

    The Unix timestamp, in seconds, when the template was created.

  - `Desktop desktop`

    Desktop configuration for each OpenAI-hosted environment.

    - `boolean enabled`

      Whether the environment provisions a desktop and browser proxy.

  - `List<File> files`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `class FileId:`

      A project-scoped Files API reference resolved separately for each session.

      - `String fileId`

        The ID of the uploaded file.

      - `String path`

        The file's absolute path inside the environment.

      - `JsonValue; type "file_id"constant`

        The type of the object. Always `file_id`.

        - `FILE_ID("file_id")`

    - `class Inline:`

      Metadata for confidential inline file contents.

      - `String path`

        The file's absolute path inside the environment.

      - `long sizeBytes`

        The decoded size of the inline file in bytes.

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

  - `Optional<String> name`

    An optional human-readable display name for the template.

  - `Network network`

    Runtime network access for each OpenAI-hosted environment.

    - `Access access`

      The environment's network access mode.

      - `ENABLED("enabled")`

        Allows unrestricted network access.

      - `DISABLED("disabled")`

        Disables network access.

      - `RESTRICTED("restricted")`

        Applies the configured domain restrictions.

    - `List<String> allowedDomains`

      Domains the environment may access when network access is restricted.

  - `JsonValue; object_ "agent.environment.template"constant`

    The object type. Always `agent.environment.template`.

    - `AGENT_ENVIRONMENT_TEMPLATE("agent.environment.template")`

  - `Packages packages`

    Packages installed in each fresh OpenAI-hosted environment.

    - `List<String> npm`

      npm packages installed globally in the environment.

    - `List<String> python`

      Python packages installed in the environment.

    - `List<String> system`

      System packages installed in the environment.

  - `List<HostedPlugin> plugins`

    Safe plugin metadata, excluding inline archive contents.

    - `String description`

      The installed plugin description.

    - `String name`

      The installed plugin name.

    - `JsonValue; type "inline"constant`

      The type of the object. Always `inline`.

      - `INLINE("inline")`

  - `List<Skill> skills`

    Safe skill metadata, preserving unresolved version selectors.

    - `class SkillReference:`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `String skillId`

        The referenced skill ID.

      - `JsonValue; type "skill_reference"constant`

        The type of the object. Always `skill_reference`.

        - `SKILL_REFERENCE("skill_reference")`

      - `Optional<String> version`

        The requested version selector, including `latest`.

    - `class Inline:`

      Safe metadata for an inline skill archive.

      - `String description`

        The skill description declared in `SKILL.md`.

      - `String name`

        The skill name declared in `SKILL.md`.

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

  - `long updatedAt`

    The Unix timestamp, in seconds, when the template was last updated.

### Environment Template Deleted

- `class EnvironmentTemplateDeleted:`

  A deleted reusable environment template.

  - `String id`

    The ID of the deleted environment template.

  - `boolean deleted`

    Whether the environment template was deleted. Always `true`.

  - `JsonValue; object_ "agent.environment.template.deleted"constant`

    The object type. Always `agent.environment.template.deleted`.

    - `AGENT_ENVIRONMENT_TEMPLATE_DELETED("agent.environment.template.deleted")`
