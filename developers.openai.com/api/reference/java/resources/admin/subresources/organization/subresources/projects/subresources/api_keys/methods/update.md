<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/update/ -->

## Update project API key

`ProjectApiKey admin().organization().projects().apiKeys().update(ApiKeyUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

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

- `ApiKeyUpdateParams params`

  - `String projectId`

  - `Optional<String> apiKeyId`

  - `Optional<Long> expiresInSeconds`

    Number of seconds from this request until the API key expires. Must comply with the organization and project expiry policies. Expired keys cannot be updated. Retrying resets the expiry relative to the new request. Omit to keep the current expiration.

    `minimum: 1`, `maximum: 31536000`

  - `Optional<List<String>> scopes`

    Replace the API key scope restrictions. Omit to leave scopes unchanged. An empty array removes key restrictions (All permissions), subject to the owner's effective permissions. Use ["api.all.read"] for read-only access. Scopes do not change the owner's roles or grant administrative permissions.

- `class ProjectApiKey:`

  Represents an individual API key in a project.

  - `String id`

    The identifier, which can be referenced in API endpoints

  - `long createdAt`

    The Unix timestamp (in seconds) of when the API key was created

    `format: unixtime`

  - `Optional<Long> lastUsedAt`

    The Unix timestamp (in seconds) of when the API key was last used.

    `format: unixtime`

  - `String name`

    The name of the API key

  - `JsonValue; object_ "organization.project.api_key"constant`

    The object type, which is always `organization.project.api_key`

    - `ORGANIZATION_PROJECT_API_KEY("organization.project.api_key")`

  - `Owner owner`

    - `Optional<ServiceAccount> serviceAccount`

      The service account that owns a project API key.

      - `String id`

        The identifier, which can be referenced in API endpoints

      - `long createdAt`

        The Unix timestamp (in seconds) of when the service account was created.

        `format: unixtime`

      - `String name`

        The name of the service account.

      - `String role`

        The service account's project role.

    - `Optional<Type> type`

      `user` or `service_account`

      - `USER("user")`

      - `SERVICE_ACCOUNT("service_account")`

    - `Optional<User> user`

      The user that owns a project API key.

      - `String id`

        The identifier, which can be referenced in API endpoints

      - `long createdAt`

        The Unix timestamp (in seconds) of when the user was created.

        `format: unixtime`

      - `String email`

        The email address of the user.

      - `String name`

        The name of the user.

      - `String role`

        The user's project role.

  - `OwnerProjectAccess ownerProjectAccess`

    Whether the API key's owner currently has effective access to the project.

    - `ACTIVE("active")`

    - `INACTIVE("inactive")`

  - `String redactedValue`

    The redacted value of the API key

  - `Optional<Long> expiresAt`

    The Unix timestamp (in seconds) when the API key expires, or null if it does not expire.

    `format: unixtime`

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.admin.organization.projects.apikeys.ApiKeyUpdateParams;
import com.openai.models.admin.organization.projects.apikeys.ProjectApiKey;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ApiKeyUpdateParams params = ApiKeyUpdateParams.builder()
            .projectId("project_id")
            .apiKeyId("api_key_id")
            .addScope("api.all.read")
            .build();
        ProjectApiKey projectApiKey = client.admin().organization().projects().apiKeys().update(params);

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
