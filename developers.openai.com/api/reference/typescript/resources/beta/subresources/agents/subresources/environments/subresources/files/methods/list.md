<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/agents/subresources/environments/subresources/files/methods/list/ -->

## List agent environment files

`client.beta.agents.environments.files.list(stringenvironmentID, FileListParamsquery?, RequestOptionsoptions?): TokenPage<EnvironmentFile>`

**get** `/agents/environments/{environment_id}/files`

Lists live files on a connected execution environment with optional directory filtering and opaque cursor pagination. See [environment files](/api/docs/guides/agents-api/environments/files).

- `environmentID: string`

- `query: FileListParams`

  - `limit?: number | null`

    The maximum number of files to return, between 1 and 100.

  - `order?: "asc" | "desc"`

    Sort by case-sensitive path components. Defaults to descending.

    - `"asc"`

      Returns resources in ascending order.

    - `"desc"`

      Returns resources in descending order.

  - `page?: string`

    The opaque token from the previous page. Keep the same path, order, and limit.

  - `path_?: string | null`

    Restrict the listing to this absolute workspace directory.

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

// Automatically fetches more pages as needed.
for await (const environmentFile of client.beta.agents.environments.files.list('environment_id')) {
  console.log(environmentFile.environment_id);

  "data": [
      "environment_id": "environment_id",
      "object": "agent.environment.file",
      "path": "path",
      "size_bytes": 0
  "has_more": true,
  "next": "next",
  "object": "page"
