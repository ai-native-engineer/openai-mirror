<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/subresources/vaults/subresources/credentials/methods/list/ -->

## List vault credentials

`CredentialListPage beta().agents().vaults().credentials().list(CredentialListParamsparams = CredentialListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/vaults/{vault_id}/credentials`

Lists a vault's credentials using ID-based pagination without returning secret values. See [vaults](/api/docs/guides/agents-api/tools/vaults).

- `CredentialListParams params`

  - `Optional<String> vaultId`

  - `Optional<String> after`

    Return resources after this resource ID in the selected order.

  - `Optional<Long> limit`

    The maximum number of resources to return. Defaults to 20. Values are clamped between 1 and 100.

  - `Optional<Order> order`

    Sort order by the `created_at` timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `desc`.

    - `ASC("asc")`

      Returns resources in ascending order.

    - `DESC("desc")`

      Returns resources in descending order.

  - `Optional<VaultStatusFilter> status`

    Filter by one status or a list, such as `status=active` or `status[]=active&status[]=archived`. Both statuses are included by default.

    - `enum VaultStatus:`

      Whether a vault or credential is active or archived.

      - `ACTIVE("active")`

      - `ARCHIVED("archived")`

    - `List<VaultStatus>`

      - `ACTIVE("active")`

      - `ARCHIVED("archived")`

- `class Credential:`

  Metadata for a stored credential. Secret values are never returned.

  - `String id`

    The ID of the credential.

  - `CredentialAuth auth`

    The authentication method and non-secret configuration of the credential.

    - `McpOAuth`

      - `Optional<String> expiresAt`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `String mcpServerUrl`

        The HTTPS MCP server URL authorized by this credential.

      - `Optional<Refresh> refresh`

        Public refresh metadata without refresh tokens or OAuth client secrets.

        - `String clientId`

          The OAuth client ID used when requesting a new access token.

        - `Optional<String> resource`

          The resource URI sent to the OAuth token endpoint during refresh, if configured.

        - `Optional<String> scope`

          Space-separated OAuth scopes requested during refresh, if configured.

        - `String tokenEndpoint`

          The HTTPS OAuth token endpoint used for refresh.

        - `McpOAuthTokenEndpointAuth tokenEndpointAuth`

          How the OAuth client authenticates to the token endpoint, excluding its client secret.

          - `JsonValue;`

            - `JsonValue; type "none"constant`

              The type of the object. Always `none`.

              - `NONE("none")`

          - `JsonValue;`

            - `JsonValue; type "client_secret_basic"constant`

              The type of the object. Always `client_secret_basic`.

              - `CLIENT_SECRET_BASIC("client_secret_basic")`

          - `JsonValue;`

            - `JsonValue; type "client_secret_post"constant`

              The type of the object. Always `client_secret_post`.

              - `CLIENT_SECRET_POST("client_secret_post")`

      - `JsonValue; type "mcp_oauth"constant`

        The type of the object. Always `mcp_oauth`.

        - `MCP_OAUTH("mcp_oauth")`

    - `StaticBearer`

      - `String mcpServerUrl`

        The HTTPS MCP server URL authorized by this credential.

      - `JsonValue; type "static_bearer"constant`

        The type of the object. Always `static_bearer`.

        - `STATIC_BEARER("static_bearer")`

    - `EnvironmentVariable`

      - `CredentialNetworking networking`

        The destinations where the proxy can substitute the secret, subject to the environment network policy.

        - `JsonValue;`

          - `JsonValue; type "unrestricted"constant`

            The type of the object. Always `unrestricted`.

            - `UNRESTRICTED("unrestricted")`

        - `Limited`

          - `List<String> allowedHosts`

            The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

          - `JsonValue; type "limited"constant`

            The type of the object. Always `limited`.

            - `LIMITED("limited")`

      - `String secretName`

        The environment variable name that receives the placeholder in the sandbox.

      - `JsonValue; type "environment_variable"constant`

        The type of the object. Always `environment_variable`.

        - `ENVIRONMENT_VARIABLE("environment_variable")`

  - `long createdAt`

    The Unix timestamp, in seconds, when the credential was created.

  - `Metadata metadata`

    Application-defined key-value pairs associated with this credential.

  - `String name`

    The human-readable name of the credential.

  - `JsonValue; object_ "vault.credential"constant`

    The object type. Always `vault.credential`.

    - `VAULT_CREDENTIAL("vault.credential")`

  - `long updatedAt`

    The Unix timestamp, in seconds, when the credential was last updated.

  - `String vaultId`

    The ID of the vault containing this credential.

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.vaults.credentials.CredentialListPage;
import com.openai.models.beta.agents.vaults.credentials.CredentialListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        CredentialListPage page = client.beta().agents().vaults().credentials().list("vault_id");

  "data": [
      "auth": {
        "expires_at": "expires_at",
        "mcp_server_url": "mcp_server_url",
        "refresh": {
          "client_id": "client_id",
          "resource": "resource",
          "scope": "scope",
          "token_endpoint": "token_endpoint",
          "token_endpoint_auth": {
            "type": "none"
        "type": "mcp_oauth"
      "metadata": {
        "foo": "string"
      "object": "vault.credential",
      "updated_at": 0,
      "vault_id": "vault_id"
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
