<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/update/ -->

## Update project API key

`$ openai admin:organization:projects:api-keys update`

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

- `--project-id: string`

  The ID of the project.

- `--api-key-id: string`

  The ID of the API key.

- `--expires-in-seconds: optional number`

  Number of seconds from this request until the API key expires. Must comply with the organization and project expiry policies. Expired keys cannot be updated. Retrying resets the expiry relative to the new request. Omit to keep the current expiration.

  `minimum: 1`, `maximum: 31536000`

- `--scope: optional array of string`

  Replace the API key scope restrictions. Omit to leave scopes unchanged. An empty array removes key restrictions (All permissions), subject to the owner's effective permissions. Use ["api.all.read"] for read-only access. Scopes do not change the owner's roles or grant administrative permissions.

- `project_api_key: object { id, created_at, last_used_at, 6 more }`

  Represents an individual API key in a project.

  - `id: string`

    The identifier, which can be referenced in API endpoints

  - `created_at: number`

    The Unix timestamp (in seconds) of when the API key was created

    `format: unixtime`

  - `last_used_at: number`

    The Unix timestamp (in seconds) of when the API key was last used.

    `format: unixtime`

  - `name: string`

    The name of the API key

  - `object: "organization.project.api_key"`

    The object type, which is always `organization.project.api_key`

  - `owner: object { service_account, type, user }`

    - `service_account: optional object { id, created_at, name, role }`

      The service account that owns a project API key.

      - `id: string`

        The identifier, which can be referenced in API endpoints

      - `created_at: number`

        The Unix timestamp (in seconds) of when the service account was created.

        `format: unixtime`

      - `name: string`

        The name of the service account.

      - `role: string`

        The service account's project role.

    - `type: optional "user" or "service_account"`

      `user` or `service_account`

      - `"user"`

      - `"service_account"`

    - `user: optional object { id, created_at, email, 2 more }`

      The user that owns a project API key.

      - `id: string`

        The identifier, which can be referenced in API endpoints

      - `created_at: number`

        The Unix timestamp (in seconds) of when the user was created.

        `format: unixtime`

      - `email: string`

        The email address of the user.

      - `name: string`

        The name of the user.

      - `role: string`

        The user's project role.

  - `owner_project_access: "active" or "inactive"`

    Whether the API key's owner currently has effective access to the project.

    - `"active"`

    - `"inactive"`

  - `redacted_value: string`

    The redacted value of the API key

  - `expires_at: optional number`

    The Unix timestamp (in seconds) when the API key expires, or null if it does not expire.

    `format: unixtime`

```cli
openai admin:organization:projects:api-keys update \
  --admin-api-key 'My Admin API Key' \
  --project-id project_id \
  --api-key-id api_key_id \
  --scope api.all.read

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
