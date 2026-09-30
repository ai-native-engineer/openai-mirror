<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/agents/subresources/environments/subresources/files/methods/create/ -->

## Create an agent environment file

`client.beta.agents.environments.files.create(stringenvironmentID, FileCreateParamsbody, RequestOptionsoptions?): EnvironmentFile`

**post** `/agents/environments/{environment_id}/files`

Copies inline bytes or a Files API file into a connected execution environment. See [environment files](/api/docs/guides/agents-api/environments/files).

- `environmentID: string`

- `FileCreateParams = HostedEnvironmentFileParamFileID | HostedEnvironmentFileParamInline`

  - `FileCreateParamsBase`

    - `file_id?: string`

      The ID of the uploaded file.

    - `path_?: string`

      The absolute destination path inside `/workspace`.

    - `type?: "file_id"`

      The type of the object. Always `file_id`.

      - `"file_id"`

  - `HostedEnvironmentFileParamFileID extends FileCreateParamsBase`

  - `HostedEnvironmentFileParamInline extends FileCreateParamsBase`

- `EnvironmentFile`

  A live file in an execution environment.

  - `environment_id: string`

    The ID of the environment containing this file.

  - `object: "agent.environment.file"`

    The object type. Always `agent.environment.file`.

    - `"agent.environment.file"`

  - `path: string`

    The absolute file path inside the environment's workspace.

  - `size_bytes: number`

    The file size in bytes.

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const environmentFile = await client.beta.agents.environments.files.create('environment_id');

console.log(environmentFile.environment_id);

  "environment_id": "environment_id",
  "object": "agent.environment.file",
  "path": "path",
  "size_bytes": 0
