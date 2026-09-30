<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/ -->
<!-- part of: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/ -->

<!-- chunk-start -->

`Credential beta().agents().vaults().credentials().retrieve(CredentialRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/vaults/{vault_id}/credentials/{credential_id}`

Retrieves vault credential metadata without returning secret values. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `CredentialRetrieveParams params`

  - `String vaultId`

  - `Optional<String> credentialId`

### Returns

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

### Example

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
    }
}
```

#### Response

```json
{
  "id": "id",
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
      }
    },
    "type": "mcp_oauth"
  },
  "created_at": 0,
  "metadata": {
    "foo": "string"
  },
  "name": "name",
  "object": "vault.credential",
  "updated_at": 0,
  "vault_id": "vault_id"
}
```

## Update a vault credential

`Credential beta().agents().vaults().credentials().update(CredentialUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/vaults/{vault_id}/credentials/{credential_id}`

Updates credential metadata or rotates its write-only secret. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `CredentialUpdateParams params`

  - `String vaultId`

  - `Optional<String> credentialId`

  - `Optional<CredentialAuthRotateParam> auth`

    Replacement values for the credential's existing authentication method.

  - `Optional<Metadata> metadata`

    Replaces all metadata. Omit to preserve it, or pass {} to clear it. Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters.

### Returns

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

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.vaults.credentials.Credential;
import com.openai.models.beta.agents.vaults.credentials.CredentialUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        CredentialUpdateParams params = CredentialUpdateParams.builder()
            .vaultId("vault_id")
            .credentialId("credential_id")
            .build();
        Credential credential = client.beta().agents().vaults().credentials().update(params);
    }
}
```

#### Response

```json
{
  "id": "id",
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
      }
    },
    "type": "mcp_oauth"
  },
  "created_at": 0,
  "metadata": {
    "foo": "string"
  },
  "name": "name",
  "object": "vault.credential",
  "updated_at": 0,
  "vault_id": "vault_id"
}
```

## Domain Types

### Credential

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

### Credential Auth

- `class CredentialAuth: A class that can be one of several variants.union`

  The authentication configuration of a vault credential, excluding secrets.

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

### Credential Auth Create Param

- `class CredentialAuthCreateParam: A class that can be one of several variants.union`

  Authentication credentials for an MCP server or an OpenAI-hosted environment.

  - `McpOAuth`

    - `String accessToken`

      A write-only OAuth access token; never returned by credential resources.

    - `String mcpServerUrl`

      The HTTPS MCP server URL authorized by this credential.

    - `JsonValue; type "mcp_oauth"constant`

      The type of the object. Always `mcp_oauth`.

      - `MCP_OAUTH("mcp_oauth")`

    - `Optional<String> expiresAt`

      When the OAuth access token expires, as an RFC 3339 timestamp, if known.

    - `Optional<Refresh> refresh`

      Optional refresh configuration for an HTTPS OAuth token endpoint.

      - `String clientId`

        The OAuth client ID used when requesting a new access token.

      - `String refreshToken`

        The refresh token to store. This secret is never returned in credential resources.

      - `String tokenEndpoint`

        The HTTPS OAuth token endpoint used to exchange the refresh token for a new access token.

      - `McpOAuthTokenEndpointAuthCreateParam tokenEndpointAuth`

        How the OAuth client authenticates to the token endpoint.

        - `JsonValue;`

          - `JsonValue; type "none"constant`

            The type of the object. Always `none`.

            - `NONE("none")`

        - `ClientSecretBasic`

          - `String clientSecret`

            The OAuth client secret to store. Never returned in credential resources.

          - `JsonValue; type "client_secret_basic"constant`

            The type of the object. Always `client_secret_basic`.

            - `CLIENT_SECRET_BASIC("client_secret_basic")`

        - `ClientSecretPost`

          - `String clientSecret`

            The OAuth client secret to store. Never returned in credential resources.

          - `JsonValue; type "client_secret_post"constant`

            The type of the object. Always `client_secret_post`.

            - `CLIENT_SECRET_POST("client_secret_post")`

      - `Optional<String> resource`

        The resource URI to send to the OAuth token endpoint during refresh, if required.

      - `Optional<String> scope`

        Space-separated OAuth scopes to request during refresh, if required.

  - `StaticBearer`

    - `String token`

      The bearer token to store. This secret is never returned in credential resources.

    - `String mcpServerUrl`

      The HTTPS MCP server URL authorized by this credential.

    - `JsonValue; type "static_bearer"constant`

      The type of the object. Always `static_bearer`.

      - `STATIC_BEARER("static_bearer")`

  - `EnvironmentVariable`

    - `CredentialNetworkingParam networking`

      The destinations where the proxy can substitute this secret. The environment network policy must also allow them.

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

      The environment variable name that receives the placeholder, such as `SERVICE_API_KEY`. Use ASCII letters, digits, and underscores, starting with a letter or underscore. Names starting with `CODEX_` and managed proxy or certificate variable names are reserved.

    - `String secretValue`

      The write-only secret to store. Never returned in credential resources or supplied directly to sandbox code. Must be nonempty and must not contain carriage returns, newlines, or NUL bytes.

    - `JsonValue; type "environment_variable"constant`

      The type of the object. Always `environment_variable`.

      - `ENVIRONMENT_VARIABLE("environment_variable")`

### Credential Auth Rotate Param

- `class CredentialAuthRotateParam: A class that can be one of several variants.union`

  Updates to a vault credential without changing its authentication method or destination configuration.

  - `McpOAuth`

    - `JsonValue; type "mcp_oauth"constant`

      The type of the object. Always `mcp_oauth`.

      - `MCP_OAUTH("mcp_oauth")`

    - `Optional<String> accessToken`

      A write-only replacement OAuth access token.

    - `Optional<String> expiresAt`

      The replacement expiry as an RFC 3339 timestamp, or `null` to clear it. Omitting this field preserves the expiry unless a new access token is supplied, in which case the expiry is cleared.

    - `Optional<Refresh> refresh`

      Optional write-only refresh-token and client-secret updates.

      - `Optional<String> refreshToken`

        The replacement refresh token. Omit or pass `null` to keep the stored token. This secret is never returned in resources.

      - `Optional<String> scope`

        Replacement space-separated OAuth scopes for refresh requests. Omit to keep the scopes, or pass `null` to stop sending a scope parameter.

      - `Optional<McpOAuthTokenEndpointAuthRotateParam> tokenEndpointAuth`

        Client-secret updates for the existing token endpoint authentication method.

        - `ClientSecretBasic`

          - `JsonValue; type "client_secret_basic"constant`

            The type of the object. Always `client_secret_basic`.

            - `CLIENT_SECRET_BASIC("client_secret_basic")`

          - `Optional<String> clientSecret`

            The replacement OAuth client secret. Omit or pass `null` to keep the stored secret. This secret is never returned in resources.

        - `ClientSecretPost`

          - `JsonValue; type "client_secret_post"constant`

            The type of the object. Always `client_secret_post`.

            - `CLIENT_SECRET_POST("client_secret_post")`

          - `Optional<String> clientSecret`

            The replacement OAuth client secret. Omit or pass `null` to keep the stored secret. This secret is never returned in resources.

  - `StaticBearer`

    - `String token`

      The replacement bearer token. This secret is never returned in credential resources.

    - `JsonValue; type "static_bearer"constant`

      The type of the object. Always `static_bearer`.

      - `STATIC_BEARER("static_bearer")`

  - `EnvironmentVariable`

    - `String secretValue`

      The write-only replacement secret. Never returned in credential resources or supplied directly to sandbox code. Must be nonempty and must not contain carriage returns, newlines, or NUL bytes.

    - `JsonValue; type "environment_variable"constant`

      The type of the object. Always `environment_variable`.

      - `ENVIRONMENT_VARIABLE("environment_variable")`

### Credential Deleted

- `class CredentialDeleted:`

  Confirmation that a vault credential was deleted.

  - `String id`

    The ID of the deleted credential.

  - `boolean deleted`

    Whether the resource was deleted. Always `true`.

  - `JsonValue; object_ "vault.credential.deleted"constant`

    The object type. Always `vault.credential.deleted`.

    - `VAULT_CREDENTIAL_DELETED("vault.credential.deleted")`

### Credential Networking

- `class CredentialNetworking: A class that can be one of several variants.union`

  Destination permissions for an environment-variable credential. These do not grant network access to the environment.

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

### Credential Networking Param

- `class CredentialNetworkingParam: A class that can be one of several variants.union`

  Destination permissions for an environment-variable credential. These do not grant network access to the environment.

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

### Mcp OAuth Token Endpoint Auth

- `class McpOAuthTokenEndpointAuth: A class that can be one of several variants.union`

  The client authentication method used for OAuth token refresh.

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

### Mcp OAuth Token Endpoint Auth Create Param

- `class McpOAuthTokenEndpointAuthCreateParam: A class that can be one of several variants.union`

  Client authentication credentials for OAuth token refresh.

  - `JsonValue;`

    - `JsonValue; type "none"constant`

      The type of the object. Always `none`.

      - `NONE("none")`

  - `ClientSecretBasic`

    - `String clientSecret`

      The OAuth client secret to store. Never returned in credential resources.

    - `JsonValue; type "client_secret_basic"constant`

      The type of the object. Always `client_secret_basic`.

      - `CLIENT_SECRET_BASIC("client_secret_basic")`

  - `ClientSecretPost`

    - `String clientSecret`

      The OAuth client secret to store. Never returned in credential resources.

    - `JsonValue; type "client_secret_post"constant`

      The type of the object. Always `client_secret_post`.

      - `CLIENT_SECRET_POST("client_secret_post")`

### Mcp OAuth Token Endpoint Auth Rotate Param

- `class McpOAuthTokenEndpointAuthRotateParam: A class that can be one of several variants.union`

  Client-secret updates that preserve the credential's OAuth authentication method.

  - `ClientSecretBasic`

    - `JsonValue; type "client_secret_basic"constant`

      The type of the object. Always `client_secret_basic`.

      - `CLIENT_SECRET_BASIC("client_secret_basic")`

    - `Optional<String> clientSecret`

      The replacement OAuth client secret. Omit or pass `null` to keep the stored secret. This secret is never returned in resources.

  - `ClientSecretPost`

    - `JsonValue; type "client_secret_post"constant`

      The type of the object. Always `client_secret_post`.

      - `CLIENT_SECRET_POST("client_secret_post")`

    - `Optional<String> clientSecret`

      The replacement OAuth client secret. Omit or pass `null` to keep the stored secret. This secret is never returned in resources.
