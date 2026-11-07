<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/update/ -->

## Update project API key

`client.Admin.Organization.Projects.APIKeys.Update(ctx, projectID, apiKeyID, body) (*ProjectAPIKey, error)`

**post** `/organization/projects/{project_id}/api_keys/{api_key_id}`

Updates the scopes and/or expiration of an existing API key in the project, including a
service-account-owned key. Requires permission to write project API keys.

Provide at least one of `scopes` or `expires_in_seconds`. Omitted fields stay
unchanged; neither field accepts `null`. Both changes are saved together.

`scopes` replaces the key's scope restrictions using the same scope identifiers
as the dashboard. An empty array means All permissions, subject to the owner's
effective access; it does not mean no access. Use `["api.all.read"]` for read-only
access or specific scopes such as `["api.files.read"]` for restricted access.
This does not change user or service-account roles or grant admin permissions.
Scope changes follow the same authentication-cache propagation as dashboard edits.

Provide `expires_in_seconds` to set the expiration relative to this request.
The value must satisfy the organization's and project's expiry policies.
Expired keys cannot be updated. Retrying resets the expiration relative to
the new request. The response contains only the redacted key, not its secret.

- `projectID string`

- `apiKeyID string`

- `body AdminOrganizationProjectAPIKeyUpdateParams`

  - `ExpiresInSeconds param.Field[int64]`

    Number of seconds from this request until the API key expires. Must comply with the organization and project expiry policies. Expired keys cannot be updated. Retrying resets the expiry relative to the new request. Omit to keep the current expiration.

    `minimum: 1`, `maximum: 31536000`

  - `Scopes param.Field[[]string]`

    Replace the API key scope restrictions. Omit to leave scopes unchanged. An empty array removes key restrictions (All permissions), subject to the owner's effective permissions. Use ["api.all.read"] for read-only access. Scopes do not change the owner's roles or grant administrative permissions.

- `type ProjectAPIKey struct{…}`

  Represents an individual API key in a project.

  - `ID string`

    The identifier, which can be referenced in API endpoints

  - `CreatedAt int64`

    The Unix timestamp (in seconds) of when the API key was created

    `format: unixtime`

  - `LastUsedAt int64`

    The Unix timestamp (in seconds) of when the API key was last used.

    `format: unixtime`

  - `Name string`

    The name of the API key

  - `Object OrganizationProjectAPIKey`

    The object type, which is always `organization.project.api_key`

    - `const OrganizationProjectAPIKeyOrganizationProjectAPIKey OrganizationProjectAPIKey = "organization.project.api_key"`

  - `Owner ProjectAPIKeyOwner`

    - `ServiceAccount ProjectAPIKeyOwnerServiceAccount`

      The service account that owns a project API key.

      - `ID string`

        The identifier, which can be referenced in API endpoints

      - `CreatedAt int64`

        The Unix timestamp (in seconds) of when the service account was created.

        `format: unixtime`

      - `Name string`

        The name of the service account.

      - `Role string`

        The service account's project role.

    - `Type string`

      `user` or `service_account`

      - `const ProjectAPIKeyOwnerTypeUser ProjectAPIKeyOwnerType = "user"`

      - `const ProjectAPIKeyOwnerTypeServiceAccount ProjectAPIKeyOwnerType = "service_account"`

    - `User ProjectAPIKeyOwnerUser`

      The user that owns a project API key.

      - `ID string`

        The identifier, which can be referenced in API endpoints

      - `CreatedAt int64`

        The Unix timestamp (in seconds) of when the user was created.

        `format: unixtime`

      - `Email string`

        The email address of the user.

      - `Name string`

        The name of the user.

      - `Role string`

        The user's project role.

  - `OwnerProjectAccess ProjectAPIKeyOwnerProjectAccess`

    Whether the API key's owner currently has effective access to the project.

    - `const ProjectAPIKeyOwnerProjectAccessActive ProjectAPIKeyOwnerProjectAccess = "active"`

    - `const ProjectAPIKeyOwnerProjectAccessInactive ProjectAPIKeyOwnerProjectAccess = "inactive"`

  - `RedactedValue string`

    The redacted value of the API key

  - `ExpiresAt int64`

    The Unix timestamp (in seconds) when the API key expires, or null if it does not expire.

    `format: unixtime`

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAdminAPIKey("My Admin API Key"),
  projectAPIKey, err := client.Admin.Organization.Projects.APIKeys.Update(
    context.TODO(),
    "project_id",
    "api_key_id",
    openai.AdminOrganizationProjectAPIKeyUpdateParams{
      Scopes: []string{"api.all.read"},
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", projectAPIKey.ID)

  "last_used_at": 0,
  "object": "organization.project.api_key",
  "owner": {
    "service_account": {
      "role": "role"
    "type": "user",
    "user": {
      "email": "email",
      "role": "role"
  "owner_project_access": "active",
  "redacted_value": "redacted_value",
  "expires_at": 0
