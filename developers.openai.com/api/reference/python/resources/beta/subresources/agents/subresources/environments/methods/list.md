<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/agents/subresources/environments/methods/list/ -->

## List agent environments

`beta.agents.environments.list(EnvironmentListParams**kwargs)  -> SyncCursorPage[EnvironmentInfo]`

**get** `/agents/environments`

Lists OpenAI-hosted environments owned by the authenticated principal. Requires access to the prewarming beta.

- `after: Optional[str]`

  Return resources after this resource ID in the selected order.

  `minLength: 0`, `maxLength: 1048576`

- `limit: Optional[int]`

  The maximum number of resources to return, between 1 and 100. Defaults to 20.

  `format: int64`, `minimum: 1`, `maximum: 100`

- `order: Optional[Literal["asc", "desc"]]`

  The order in which resources are returned. Defaults to `desc`.

  - `"asc"`

    Returns resources in ascending order.

  - `"desc"`

    Returns resources in descending order.

- `type: Optional[Literal["openai_hosted"]]`

  The hosting type to list. Defaults to `openai_hosted`.

  - `"openai_hosted"`

- `class EnvironmentInfo: …`

  Safe metadata for a first-class execution environment.

  - `id: str`

    The ID of the environment.

    `minLength: 0`

  - `files: List[HostedEnvironmentFile]`

    Files installed in the environment, without their contents.

    `minItems: 0`, `maxItems: 2000`

    - `class HostedEnvironmentFileID: …`

      A file copied from the OpenAI Files API.

      - `id: str`

        The session-scoped ID of the file in the execution environment.

        `minLength: 0`

      - `file_id: str`

        The ID of the uploaded file.

        `minLength: 0`

      - `path: str`

        The file's absolute path inside the environment.

        `minLength: 0`

      - `size_bytes: int`

        The decoded file size in bytes.

        `format: int64`, `minimum: 0`

      - `type: Literal["file_id"]`

        The type of the object. Always `file_id`.

        - `"file_id"`

    - `class HostedEnvironmentFileResourceInline: …`

      A file supplied inline when the session was created.

      - `id: str`

        The session-scoped ID of the file in the execution environment.

        `minLength: 0`

      - `path: str`

        The file's absolute path inside the environment.

        `minLength: 0`

      - `size_bytes: int`

        The decoded file size in bytes.

        `format: int64`, `minimum: 0`

      - `type: Literal["inline"]`

        The type of the object. Always `inline`.

        - `"inline"`

  - `object: Literal["agent.environment"]`

    The object type. Always `agent.environment`.

    - `"agent.environment"`

  - `plugins: List[HostedPlugin]`

    Plugins installed in the environment, without their archive contents.

    `minItems: 0`, `maxItems: 2000`

    - `description: str`

      The installed plugin description.

      `minLength: 0`

    - `name: str`

      The installed plugin name.

      `minLength: 0`

    - `type: Literal["inline"]`

      The type of the object. Always `inline`.

      - `"inline"`

  - `skills: List[HostedSkill]`

    Skills installed in the environment, without their archive contents.

    `minItems: 0`, `maxItems: 2000`

    - `class HostedSkillReference: …`

      A skill installed from the Skills API.

      - `description: str`

        The installed skill description.

        `minLength: 0`

      - `name: str`

        The installed skill name.

        `minLength: 0`

      - `skill_id: str`

        The referenced skill ID.

        `minLength: 0`

      - `type: Literal["skill_reference"]`

        The type of the object. Always `skill_reference`.

        - `"skill_reference"`

      - `version: str`

        The concrete skill version installed for this session.

        `minLength: 0`

    - `class HostedSkillResourceInline: …`

      A skill installed from an inline ZIP archive.

      - `description: str`

        The installed skill description.

        `minLength: 0`

      - `name: str`

        The installed skill name.

        `minLength: 0`

      - `type: Literal["inline"]`

        The type of the object. Always `inline`.

        - `"inline"`

  - `status: Literal["pending", "ready", "connected", 4 more]`

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

  - `type: Literal["openai_hosted", "self_hosted"]`

    Whether the environment is hosted by OpenAI or by the application.

    - `"openai_hosted"`

    - `"self_hosted"`

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
page = client.beta.agents.environments.list()
page = page.data[0]
print(page.id)

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
