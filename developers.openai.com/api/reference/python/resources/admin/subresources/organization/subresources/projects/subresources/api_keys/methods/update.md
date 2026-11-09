<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/update/ -->

## Update project API key

`admin.organization.projects.api_keys.update(strapi_key_id, APIKeyUpdateParams**kwargs)  -> ProjectAPIKey`

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

- `project_id: str`

- `api_key_id: str`

- `expires_in_seconds: Optional[int]`

  Number of seconds from this request until the API key expires. Must comply with the organization and project expiry policies. Expired keys cannot be updated. Retrying resets the expiry relative to the new request. Omit to keep the current expiration.

  `minimum: 1`, `maximum: 31536000`

- `scopes: Optional[Sequence[str]]`

  Replace the API key scope restrictions. Omit to leave scopes unchanged. An empty array removes key restrictions (All permissions), subject to the owner's effective permissions. Use ["api.all.read"] for read-only access. Scopes do not change the owner's roles or grant administrative permissions.

- `class ProjectAPIKey: …`

  Represents an individual API key in a project.

  - `id: str`

    The identifier, which can be referenced in API endpoints

  - `created_at: int`

    The Unix timestamp (in seconds) of when the API key was created

    `format: unixtime`

  - `last_used_at: Optional[int]`

    The Unix timestamp (in seconds) of when the API key was last used.

    `format: unixtime`

  - `name: str`

    The name of the API key

  - `object: Literal["organization.project.api_key"]`

    The object type, which is always `organization.project.api_key`

    - `"organization.project.api_key"`

  - `owner: Owner`

    - `service_account: Optional[OwnerServiceAccount]`

      The service account that owns a project API key.

      - `id: str`

        The identifier, which can be referenced in API endpoints

      - `created_at: int`

        The Unix timestamp (in seconds) of when the service account was created.

        `format: unixtime`

      - `name: str`

        The name of the service account.

      - `role: str`

        The service account's project role.

    - `type: Optional[Literal["user", "service_account"]]`

      `user` or `service_account`

      - `"user"`

      - `"service_account"`

    - `user: Optional[OwnerUser]`

      The user that owns a project API key.

      - `id: str`

        The identifier, which can be referenced in API endpoints

      - `created_at: int`

        The Unix timestamp (in seconds) of when the user was created.

        `format: unixtime`

      - `email: str`

        The email address of the user.

      - `name: str`

        The name of the user.

      - `role: str`

        The user's project role.

  - `owner_project_access: Literal["active", "inactive"]`

    Whether the API key's owner currently has effective access to the project.

    - `"active"`

    - `"inactive"`

  - `redacted_value: str`

    The redacted value of the API key

  - `expires_at: Optional[int]`

    The Unix timestamp (in seconds) when the API key expires, or null if it does not expire.

    `format: unixtime`

```python
import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
project_api_key = client.admin.organization.projects.api_keys.update(
    api_key_id="api_key_id",
    project_id="project_id",
    scopes=["api.all.read"],
print(project_api_key.id)

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
