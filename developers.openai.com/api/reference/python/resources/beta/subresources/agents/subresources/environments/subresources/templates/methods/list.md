<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/agents/subresources/environments/subresources/templates/methods/list/ -->

## List agent environment templates

`beta.agents.environments.templates.list(TemplateListParams**kwargs)  -> SyncCursorPage[EnvironmentTemplate]`

**get** `/agents/environments/templates`

Lists reusable environment templates without returning confidential values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

- `after: Optional[str]`

  Return resources after this resource ID in the selected order.

- `limit: Optional[int]`

  The maximum number of resources to return, between 1 and 100. Defaults to 20.

- `order: Optional[Literal["asc", "desc"]]`

  The order in which resources are returned. Defaults to `desc`.

  - `"asc"`

    Returns resources in ascending order.

  - `"desc"`

    Returns resources in descending order.

- `class EnvironmentTemplate: …`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `id: str`

    The ID of the reusable environment template.

  - `capability_directories: List[str]`

    Directories that expose capabilities to the agent.

  - `created_at: int`

    The Unix timestamp, in seconds, when the template was created.

  - `desktop: Desktop`

    Desktop configuration for each OpenAI-hosted environment.

    - `enabled: bool`

      Whether the environment provisions a desktop and browser proxy.

  - `files: List[File]`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `class FileHostedTemplateFileResourceFileID: …`

      A project-scoped Files API reference resolved separately for each session.

      - `file_id: str`

        The ID of the uploaded file.

      - `path: str`

        The file's absolute path inside the environment.

      - `type: Literal["file_id"]`

        The type of the object. Always `file_id`.

        - `"file_id"`

    - `class FileHostedTemplateFileResourceInline: …`

      Metadata for confidential inline file contents.

      - `path: str`

        The file's absolute path inside the environment.

      - `size_bytes: int`

        The decoded size of the inline file in bytes.

      - `type: Literal["inline"]`

        The type of the object. Always `inline`.

        - `"inline"`

  - `name: Optional[str]`

    An optional human-readable display name for the template.

  - `network: Network`

    Runtime network access for each OpenAI-hosted environment.

    - `access: Literal["enabled", "disabled", "restricted"]`

      The environment's network access mode.

      - `"enabled"`

        Allows unrestricted network access.

      - `"disabled"`

        Disables network access.

      - `"restricted"`

        Applies the configured domain restrictions.

    - `allowed_domains: List[str]`

      Domains the environment may access when network access is restricted.

  - `object: Literal["agent.environment.template"]`

    The object type. Always `agent.environment.template`.

    - `"agent.environment.template"`

  - `packages: Packages`

    Packages installed in each fresh OpenAI-hosted environment.

    - `npm: List[str]`

      npm packages installed globally in the environment.

    - `python: List[str]`

      Python packages installed in the environment.

    - `system: List[str]`

      System packages installed in the environment.

  - `plugins: List[HostedPlugin]`

    Safe plugin metadata, excluding inline archive contents.

    - `description: str`

      The installed plugin description.

    - `name: str`

      The installed plugin name.

    - `type: Literal["inline"]`

      The type of the object. Always `inline`.

      - `"inline"`

  - `skills: List[Skill]`

    Safe skill metadata, preserving unresolved version selectors.

    - `class SkillHostedTemplateSkillResourceSkillReference: …`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `skill_id: str`

        The referenced skill ID.

      - `type: Literal["skill_reference"]`

        The type of the object. Always `skill_reference`.

        - `"skill_reference"`

      - `version: Optional[str]`

        The requested version selector, including `latest`.

    - `class SkillHostedTemplateSkillResourceInline: …`

      Safe metadata for an inline skill archive.

      - `description: str`

        The skill description declared in `SKILL.md`.

      - `name: str`

        The skill name declared in `SKILL.md`.

      - `type: Literal["inline"]`

        The type of the object. Always `inline`.

        - `"inline"`

  - `updated_at: int`

    The Unix timestamp, in seconds, when the template was last updated.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
page = client.beta.agents.environments.templates.list()
page = page.data[0]
print(page.id)

  "data": [
      "capability_directories": [
        "string"
      "desktop": {
        "enabled": true
      "files": [
          "file_id": "file_id",
          "path": "path",
          "type": "file_id"
      "network": {
        "access": "enabled",
        "allowed_domains": [
          "string"
        ]
      "object": "agent.environment.template",
      "packages": {
        "npm": [
          "string"
        "python": [
          "string"
        "system": [
          "string"
        ]
      "plugins": [
          "description": "description",
          "type": "inline"
      "skills": [
          "skill_id": "skill_id",
          "type": "skill_reference",
          "version": "version"
      "updated_at": 0
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
