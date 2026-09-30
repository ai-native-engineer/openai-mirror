<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/agents/subresources/environments/methods/retrieve/ -->

## Retrieve an agent environment

`client.beta.agents.environments.retrieve(stringenvironmentID, RequestOptionsoptions?): EnvironmentInfo`

**get** `/agents/environments/{environment_id}`

Retrieves an execution environment's connection status and safe installed metadata. See [environment lifecycle](/api/docs/guides/agents-api/environments/lifecycle).

- `environmentID: string`

- `EnvironmentInfo`

  Safe metadata for a first-class execution environment.

  - `id: string`

    The ID of the environment.

  - `files: Array<HostedEnvironmentFile>`

    Files installed in the environment, without their contents.

    - `HostedEnvironmentFileID`

      A file copied from the OpenAI Files API.

      - `id: string`

        The session-scoped ID of the file in the execution environment.

      - `file_id: string`

        The ID of the uploaded file.

      - `path: string`

        The file's absolute path inside the environment.

      - `size_bytes: number`

        The decoded file size in bytes.

      - `type: "file_id"`

        The type of the object. Always `file_id`.

        - `"file_id"`

    - `HostedEnvironmentFileResourceInline`

      A file supplied inline when the session was created.

      - `id: string`

        The session-scoped ID of the file in the execution environment.

      - `path: string`

        The file's absolute path inside the environment.

      - `size_bytes: number`

        The decoded file size in bytes.

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

  - `object: "agent.environment"`

    The object type. Always `agent.environment`.

    - `"agent.environment"`

  - `plugins: Array<HostedPlugin>`

    Plugins installed in the environment, without their archive contents.

    - `description: string`

      The installed plugin description.

    - `name: string`

      The installed plugin name.

    - `type: "inline"`

      The type of the object. Always `inline`.

      - `"inline"`

  - `skills: Array<HostedSkill>`

    Skills installed in the environment, without their archive contents.

    - `HostedSkillReference`

      A skill installed from the Skills API.

      - `description: string`

        The installed skill description.

      - `name: string`

        The installed skill name.

      - `skill_id: string`

        The referenced skill ID.

      - `type: "skill_reference"`

        The type of the object. Always `skill_reference`.

        - `"skill_reference"`

      - `version: string`

        The concrete skill version installed for this session.

    - `HostedSkillResourceInline`

      A skill installed from an inline ZIP archive.

      - `description: string`

        The installed skill description.

      - `name: string`

        The installed skill name.

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

  - `status: "pending" | "connected" | "disconnected" | 2 more`

    The current environment connection status.

    - `"pending"`

    - `"connected"`

    - `"disconnected"`

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

const environmentInfo = await client.beta.agents.environments.retrieve('environment_id');

console.log(environmentInfo.id);

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
