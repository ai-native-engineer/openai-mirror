<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/agents/subresources/environments/methods/retrieve/ -->

## Retrieve an agent environment

`beta.agents.environments.retrieve(strenvironment_id)  -> EnvironmentInfo`

**get** `/agents/environments/{environment_id}`

Retrieves an execution environment's connection status and safe installed metadata. See [environment lifecycle](/api/docs/guides/agents-api/environments/lifecycle).

- `environment_id: str`

- `class EnvironmentInfo: …`

  Safe metadata for a first-class execution environment.

  - `id: str`

    The ID of the environment.

  - `files: List[HostedEnvironmentFile]`

    Files installed in the environment, without their contents.

    - `class HostedEnvironmentFileID: …`

      A file copied from the OpenAI Files API.

      - `id: str`

        The session-scoped ID of the file in the execution environment.

      - `file_id: str`

        The ID of the uploaded file.

      - `path: str`

        The file's absolute path inside the environment.

      - `size_bytes: int`

        The decoded file size in bytes.

      - `type: Literal["file_id"]`

        The type of the object. Always `file_id`.

        - `"file_id"`

    - `class HostedEnvironmentFileResourceInline: …`

      A file supplied inline when the session was created.

      - `id: str`

        The session-scoped ID of the file in the execution environment.

      - `path: str`

        The file's absolute path inside the environment.

      - `size_bytes: int`

        The decoded file size in bytes.

      - `type: Literal["inline"]`

        The type of the object. Always `inline`.

        - `"inline"`

  - `object: Literal["agent.environment"]`

    The object type. Always `agent.environment`.

    - `"agent.environment"`

  - `plugins: List[HostedPlugin]`

    Plugins installed in the environment, without their archive contents.

    - `description: str`

      The installed plugin description.

    - `name: str`

      The installed plugin name.

    - `type: Literal["inline"]`

      The type of the object. Always `inline`.

      - `"inline"`

  - `skills: List[HostedSkill]`

    Skills installed in the environment, without their archive contents.

    - `class HostedSkillReference: …`

      A skill installed from the Skills API.

      - `description: str`

        The installed skill description.

      - `name: str`

        The installed skill name.

      - `skill_id: str`

        The referenced skill ID.

      - `type: Literal["skill_reference"]`

        The type of the object. Always `skill_reference`.

        - `"skill_reference"`

      - `version: str`

        The concrete skill version installed for this session.

    - `class HostedSkillResourceInline: …`

      A skill installed from an inline ZIP archive.

      - `description: str`

        The installed skill description.

      - `name: str`

        The installed skill name.

      - `type: Literal["inline"]`

        The type of the object. Always `inline`.

        - `"inline"`

  - `status: Literal["pending", "connected", "disconnected", 2 more]`

    The current environment connection status.

    - `"pending"`

    - `"connected"`

    - `"disconnected"`

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
environment_info = client.beta.agents.environments.retrieve(
    "environment_id",
print(environment_info.id)

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
