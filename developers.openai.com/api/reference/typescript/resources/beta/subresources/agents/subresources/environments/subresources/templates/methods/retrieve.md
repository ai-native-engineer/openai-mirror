<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/agents/subresources/environments/subresources/templates/methods/retrieve/ -->

## Retrieve an agent environment template

`client.beta.agents.environments.templates.retrieve(stringenvironmentTemplateID, RequestOptionsoptions?): EnvironmentTemplate`

**get** `/agents/environments/templates/{environment_template_id}`

Retrieves reusable environment configuration without returning confidential values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

- `environmentTemplateID: string`

- `EnvironmentTemplate`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `id: string`

    The ID of the reusable environment template.

  - `capability_directories: Array<string>`

    Directories that expose capabilities to the agent.

  - `created_at: number`

    The Unix timestamp, in seconds, when the template was created.

  - `desktop: Desktop`

    Desktop configuration for each OpenAI-hosted environment.

    - `enabled: boolean`

      Whether the environment provisions a desktop and browser proxy.

  - `files: Array<HostedTemplateFileResourceFileID | HostedTemplateFileResourceInline>`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `HostedTemplateFileResourceFileID`

      A project-scoped Files API reference resolved separately for each session.

      - `file_id: string`

        The ID of the uploaded file.

      - `path: string`

        The file's absolute path inside the environment.

      - `type: "file_id"`

        The type of the object. Always `file_id`.

        - `"file_id"`

    - `HostedTemplateFileResourceInline`

      Metadata for confidential inline file contents.

      - `path: string`

        The file's absolute path inside the environment.

      - `size_bytes: number`

        The decoded size of the inline file in bytes.

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

  - `name: string | null`

    An optional human-readable display name for the template.

  - `network: Network`

    Runtime network access for each OpenAI-hosted environment.

    - `access: "enabled" | "disabled" | "restricted"`

      The environment's network access mode.

      - `"enabled"`

        Allows unrestricted network access.

      - `"disabled"`

        Disables network access.

      - `"restricted"`

        Applies the configured domain restrictions.

    - `allowed_domains: Array<string>`

      Domains the environment may access when network access is restricted.

  - `object: "agent.environment.template"`

    The object type. Always `agent.environment.template`.

    - `"agent.environment.template"`

  - `packages: Packages`

    Packages installed in each fresh OpenAI-hosted environment.

    - `npm: Array<string>`

      npm packages installed globally in the environment.

    - `python: Array<string>`

      Python packages installed in the environment.

    - `system: Array<string>`

      System packages installed in the environment.

  - `plugins: Array<HostedPlugin>`

    Safe plugin metadata, excluding inline archive contents.

    - `description: string`

      The installed plugin description.

    - `name: string`

      The installed plugin name.

    - `type: "inline"`

      The type of the object. Always `inline`.

      - `"inline"`

  - `skills: Array<HostedTemplateSkillResourceSkillReference | HostedTemplateSkillResourceInline>`

    Safe skill metadata, preserving unresolved version selectors.

    - `HostedTemplateSkillResourceSkillReference`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `skill_id: string`

        The referenced skill ID.

      - `type: "skill_reference"`

        The type of the object. Always `skill_reference`.

        - `"skill_reference"`

      - `version: string | null`

        The requested version selector, including `latest`.

    - `HostedTemplateSkillResourceInline`

      Safe metadata for an inline skill archive.

      - `description: string`

        The skill description declared in `SKILL.md`.

      - `name: string`

        The skill name declared in `SKILL.md`.

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

  - `updated_at: number`

    The Unix timestamp, in seconds, when the template was last updated.

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const environmentTemplate = await client.beta.agents.environments.templates.retrieve(
  'environment_template_id',
);

console.log(environmentTemplate.id);

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
