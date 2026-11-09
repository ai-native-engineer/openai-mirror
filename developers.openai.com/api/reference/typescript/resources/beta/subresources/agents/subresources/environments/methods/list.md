<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/agents/subresources/environments/methods/list/ -->

## List agent environments

`client.beta.agents.environments.list(EnvironmentListParamsquery?, RequestOptionsoptions?): CursorPage<EnvironmentInfo>`

**get** `/agents/environments`

Lists OpenAI-hosted environments owned by the authenticated principal. Requires access to the prewarming beta.

- `query: EnvironmentListParams`

  - `after?: string`

    Return resources after this resource ID in the selected order.

    `minLength: 0`, `maxLength: 1048576`

  - `limit?: number`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

    `format: int64`, `minimum: 1`, `maximum: 100`

  - `order?: "asc" | "desc"`

    The order in which resources are returned. Defaults to `desc`.

    - `"asc"`

      Returns resources in ascending order.

    - `"desc"`

      Returns resources in descending order.

  - `type?: "openai_hosted"`

    The hosting type to list. Defaults to `openai_hosted`.

    - `"openai_hosted"`

- `EnvironmentInfo`

  Safe metadata for a first-class execution environment.

  - `id: string`

    The ID of the environment.

    `minLength: 0`

  - `files: Array<HostedEnvironmentFile>`

    Files installed in the environment, without their contents.

    `minItems: 0`, `maxItems: 2000`

    - `HostedEnvironmentFileID`

      A file copied from the OpenAI Files API.

      - `id: string`

        The session-scoped ID of the file in the execution environment.

        `minLength: 0`

      - `file_id: string`

        The ID of the uploaded file.

        `minLength: 0`

      - `path: string`

        The file's absolute path inside the environment.

        `minLength: 0`

      - `size_bytes: number`

        The decoded file size in bytes.

        `format: int64`, `minimum: 0`

      - `type: "file_id"`

        The type of the object. Always `file_id`.

        - `"file_id"`

    - `HostedEnvironmentFileResourceInline`

      A file supplied inline when the session was created.

      - `id: string`

        The session-scoped ID of the file in the execution environment.

        `minLength: 0`

      - `path: string`

        The file's absolute path inside the environment.

        `minLength: 0`

      - `size_bytes: number`

        The decoded file size in bytes.

        `format: int64`, `minimum: 0`

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

  - `object: "agent.environment"`

    The object type. Always `agent.environment`.

    - `"agent.environment"`

  - `plugins: Array<HostedPlugin>`

    Plugins installed in the environment, without their archive contents.

    `minItems: 0`, `maxItems: 2000`

    - `description: string`

      The installed plugin description.

      `minLength: 0`

    - `name: string`

      The installed plugin name.

      `minLength: 0`

    - `type: "inline"`

      The type of the object. Always `inline`.

      - `"inline"`

  - `skills: Array<HostedSkill>`

    Skills installed in the environment, without their archive contents.

    `minItems: 0`, `maxItems: 2000`

    - `HostedSkillReference`

      A skill installed from the Skills API.

      - `description: string`

        The installed skill description.

        `minLength: 0`

      - `name: string`

        The installed skill name.

        `minLength: 0`

      - `skill_id: string`

        The referenced skill ID.

        `minLength: 0`

      - `type: "skill_reference"`

        The type of the object. Always `skill_reference`.

        - `"skill_reference"`

      - `version: string`

        The concrete skill version installed for this session.

        `minLength: 0`

    - `HostedSkillResourceInline`

      A skill installed from an inline ZIP archive.

      - `description: string`

        The installed skill description.

        `minLength: 0`

      - `name: string`

        The installed skill name.

        `minLength: 0`

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

  - `status: "pending" | "ready" | "connected" | 4 more`

    The current environment connection status.

    - `"pending"`

    - `"ready"`

      Provisioning succeeded and the environment is available for attachment or use.

    - `"connected"`

    - `"disconnected"`

    - `"suspended"`

      The sandbox is stopped and can be resumed from its private checkpoint.

    - `"expired"`

    - `"failed"`

  - `type: "openai_hosted" | "self_hosted"`

    Whether the environment is hosted by OpenAI or by the application.

    - `"openai_hosted"`

    - `"self_hosted"`

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const environmentInfo of client.beta.agents.environments.list()) {
  console.log(environmentInfo.id);

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
