<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/agents/subresources/environments/subresources/files/methods/create/ -->

## Create an agent environment file

`beta.agents.environments.files.create(strenvironment_id, FileCreateParams**kwargs)  -> EnvironmentFile`

**post** `/agents/environments/{environment_id}/files`

Copies inline bytes or a Files API file into a connected execution environment. See [environment files](/api/docs/guides/agents-api/environments/files).

- `environment_id: str`

- `file_id: Optional[str]`

  The ID of the uploaded file.

- `path: Optional[str]`

  The absolute destination path inside `/workspace`.

- `type: Optional[Literal["file_id"]]`

  The type of the object. Always `file_id`.

  - `"file_id"`

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

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
environment_file = client.beta.agents.environments.files.create(
    environment_id="environment_id",
print(environment_file.environment_id)

  "environment_id": "environment_id",
  "object": "agent.environment.file",
  "path": "path",
  "size_bytes": 0
