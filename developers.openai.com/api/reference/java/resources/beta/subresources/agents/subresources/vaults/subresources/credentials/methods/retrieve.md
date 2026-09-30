<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/subresources/vaults/subresources/credentials/methods/retrieve/ -->

## Retrieve a vault credential

`Credential beta().agents().vaults().credentials().retrieve(CredentialRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/vaults/{vault_id}/credentials/{credential_id}`

Retrieves vault credential metadata without returning secret values. See [vaults](/api/docs/guides/agents-api/tools/vaults).

- `CredentialRetrieveParams params`

  - `String vaultId`

  - `Optional<String> credentialId`

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
import com.openai.models.beta.agents.vaults.credentials.Credential;
import com.openai.models.beta.agents.vaults.credentials.CredentialRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        CredentialRetrieveParams params = CredentialRetrieveParams.builder()
            .vaultId("vault_id")
            .credentialId("credential_id")
            .build();
        Credential credential = client.beta().agents().vaults().credentials().retrieve(params);

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
