<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/agents/subresources/environments/subresources/files/ -->

# Files

## Create an agent environment file

`beta.agents.environments.files.create(strenvironment_id, FileCreateParams**kwargs)  -> EnvironmentFile`

**post** `/agents/environments/{environment_id}/files`

Copies inline bytes or a Files API file into a connected execution environment. See [environment files](/api/docs/guides/agents-api/environments/files).

### Parameters

- `environment_id: str`

- `file_id: Optional[str]`

  The ID of the uploaded file.

- `path: Optional[str]`

  The absolute destination path inside `/workspace`.

- `type: Optional[Literal["file_id"]]`

  The type of the object. Always `file_id`.

  - `"file_id"`

### Returns

- `class EnvironmentFile: …`

  A live file in an execution environment.

  - `environment_id: str`

    The ID of the environment containing this file.

  - `object: Literal["agent.environment.file"]`

    The object type. Always `agent.environment.file`.

    - `"agent.environment.file"`

  - `path: str`

    The absolute file path inside the environment's workspace.

  - `size_bytes: int`

    The file size in bytes.

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
environment_file = client.beta.agents.environments.files.create(
    environment_id="environment_id",
)
print(environment_file.environment_id)
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

`beta.agents.environments.files.list(strenvironment_id, FileListParams**kwargs)  -> SyncTokenPage[EnvironmentFile]`

**get** `/agents/environments/{environment_id}/files`

Lists live files on a connected execution environment with optional directory filtering and opaque cursor pagination. See [environment files](/api/docs/guides/agents-api/environments/files).

### Parameters

- `environment_id: str`

- `limit: Optional[int]`

  The maximum number of files to return, between 1 and 100.

- `order: Optional[Literal["asc", "desc"]]`

  Sort by case-sensitive path components. Defaults to descending.

  - `"asc"`

    Returns resources in ascending order.

  - `"desc"`

    Returns resources in descending order.

- `page: Optional[str]`

  The opaque token from the previous page. Keep the same path, order, and limit.

- `path: Optional[str]`

  Restrict the listing to this absolute workspace directory.

### Returns

- `class EnvironmentFile: …`

  A live file in an execution environment.

  - `environment_id: str`

    The ID of the environment containing this file.

  - `object: Literal["agent.environment.file"]`

    The object type. Always `agent.environment.file`.

    - `"agent.environment.file"`

  - `path: str`

    The absolute file path inside the environment's workspace.

  - `size_bytes: int`

    The file size in bytes.

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.agents.environments.files.list(
    environment_id="environment_id",
)
page = page.data[0]
print(page.environment_id)
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

- `class EnvironmentFile: …`

  A live file in an execution environment.

  - `environment_id: str`

    The ID of the environment containing this file.

  - `object: Literal["agent.environment.file"]`

    The object type. Always `agent.environment.file`.

    - `"agent.environment.file"`

  - `path: str`

    The absolute file path inside the environment's workspace.

  - `size_bytes: int`

    The file size in bytes.
