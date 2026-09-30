<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/subresources/environments/subresources/templates/methods/retrieve/ -->

## Retrieve an agent environment template

`client.Beta.Agents.Environments.Templates.Get(ctx, environmentTemplateID) (*EnvironmentTemplate, error)`

**get** `/agents/environments/templates/{environment_template_id}`

Retrieves reusable environment configuration without returning confidential values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

- `environmentTemplateID string`

- `type EnvironmentTemplate struct{…}`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `ID string`

    The ID of the reusable environment template.

  - `CapabilityDirectories []string`

    Directories that expose capabilities to the agent.

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the template was created.

  - `Desktop EnvironmentTemplateDesktop`

    Desktop configuration for each OpenAI-hosted environment.

    - `Enabled bool`

      Whether the environment provisions a desktop and browser proxy.

  - `Files []EnvironmentTemplateFileUnion`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `type EnvironmentTemplateFileFileID struct{…}`

      A project-scoped Files API reference resolved separately for each session.

      - `FileID string`

        The ID of the uploaded file.

      - `Path string`

        The file's absolute path inside the environment.

      - `Type FileID`

        The type of the object. Always `file_id`.

        - `const FileIDFileID FileID = "file_id"`

    - `type EnvironmentTemplateFileInline struct{…}`

      Metadata for confidential inline file contents.

      - `Path string`

        The file's absolute path inside the environment.

      - `SizeBytes int64`

        The decoded size of the inline file in bytes.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `Name string`

    An optional human-readable display name for the template.

  - `Network EnvironmentTemplateNetwork`

    Runtime network access for each OpenAI-hosted environment.

    - `Access string`

      The environment's network access mode.

      - `const EnvironmentTemplateNetworkAccessEnabled EnvironmentTemplateNetworkAccess = "enabled"`

        Allows unrestricted network access.

      - `const EnvironmentTemplateNetworkAccessDisabled EnvironmentTemplateNetworkAccess = "disabled"`

        Disables network access.

      - `const EnvironmentTemplateNetworkAccessRestricted EnvironmentTemplateNetworkAccess = "restricted"`

        Applies the configured domain restrictions.

    - `AllowedDomains []string`

      Domains the environment may access when network access is restricted.

  - `Object AgentEnvironmentTemplate`

    The object type. Always `agent.environment.template`.

    - `const AgentEnvironmentTemplateAgentEnvironmentTemplate AgentEnvironmentTemplate = "agent.environment.template"`

  - `Packages EnvironmentTemplatePackages`

    Packages installed in each fresh OpenAI-hosted environment.

    - `Npm []string`

      npm packages installed globally in the environment.

    - `Python []string`

      Python packages installed in the environment.

    - `System []string`

      System packages installed in the environment.

  - `Plugins []HostedPlugin`

    Safe plugin metadata, excluding inline archive contents.

    - `Description string`

      The installed plugin description.

    - `Name string`

      The installed plugin name.

    - `Type Inline`

      The type of the object. Always `inline`.

      - `const InlineInline Inline = "inline"`

  - `Skills []EnvironmentTemplateSkillUnion`

    Safe skill metadata, preserving unresolved version selectors.

    - `type EnvironmentTemplateSkillSkillReference struct{…}`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `SkillID string`

        The referenced skill ID.

      - `Type SkillReference`

        The type of the object. Always `skill_reference`.

        - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

      - `Version string`

        The requested version selector, including `latest`.

    - `type EnvironmentTemplateSkillInline struct{…}`

      Safe metadata for an inline skill archive.

      - `Description string`

        The skill description declared in `SKILL.md`.

      - `Name string`

        The skill name declared in `SKILL.md`.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `UpdatedAt int64`

    The Unix timestamp, in seconds, when the template was last updated.

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  environmentTemplate, err := client.Beta.Agents.Environments.Templates.Get(context.TODO(), "environment_template_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", environmentTemplate.ID)

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
