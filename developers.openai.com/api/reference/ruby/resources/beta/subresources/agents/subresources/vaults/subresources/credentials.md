<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/agents/subresources/vaults/subresources/credentials/ -->

# Credentials

## Create a vault credential

`beta.agents.vaults.credentials.create(vault_id, **kwargs) -> Credential`

**post** `/vaults/{vault_id}/credentials`

Creates a vault credential. Secret values are write-only and are never returned. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vault_id: String`

- `auth: CredentialAuthCreateParam`

  The authentication method and write-only secret values to store.

  - `class McpOauth`

    An OAuth credential for an HTTPS MCP destination.

    - `access_token: String`

      A write-only OAuth access token; never returned by credential resources.

    - `mcp_server_url: String`

      The HTTPS MCP server URL authorized by this credential.

    - `type: :mcp_oauth`

      The type of the object. Always `mcp_oauth`.

      - `:mcp_oauth`

    - `expires_at: String`

      When the OAuth access token expires, as an RFC 3339 timestamp, if known.

    - `refresh: Refresh{ client_id, refresh_token, token_endpoint, 3 more}`

      Optional refresh configuration for an HTTPS OAuth token endpoint.

      - `client_id: String`

        The OAuth client ID used when requesting a new access token.

      - `refresh_token: String`

        The refresh token to store. This secret is never returned in credential resources.

      - `token_endpoint: String`

        The HTTPS OAuth token endpoint used to exchange the refresh token for a new access token.

      - `token_endpoint_auth: McpOauthTokenEndpointAuthCreateParam`

        How the OAuth client authenticates to the token endpoint.

        - `class None`

          Sends the client ID without a client secret.

          - `type: :none`

            The type of the object. Always `none`.

            - `:none`

        - `class ClientSecretBasic`

          Sends the client ID and secret using HTTP Basic authentication.

          - `client_secret: String`

            The OAuth client secret to store. Never returned in credential resources.

          - `type: :client_secret_basic`

            The type of the object. Always `client_secret_basic`.

            - `:client_secret_basic`

        - `class ClientSecretPost`

          Sends the client ID and secret in the token request body.

          - `client_secret: String`

            The OAuth client secret to store. Never returned in credential resources.

          - `type: :client_secret_post`

            The type of the object. Always `client_secret_post`.

            - `:client_secret_post`

      - `resource: String`

        The resource URI to send to the OAuth token endpoint during refresh, if required.

      - `scope: String`

        Space-separated OAuth scopes to request during refresh, if required.

  - `class StaticBearer`

    A bearer token for an MCP server, without automatic OAuth refresh.

    - `token: String`

      The bearer token to store. This secret is never returned in credential resources.

    - `mcp_server_url: String`

      The HTTPS MCP server URL authorized by this credential.

    - `type: :static_bearer`

      The type of the object. Always `static_bearer`.

      - `:static_bearer`

  - `class EnvironmentVariable`

    An HTTP credential for OpenAI-hosted environments only. The sandbox receives an environment variable containing a placeholder, not the secret. Use the placeholder unchanged in outgoing requests. The egress proxy replaces the placeholder with the secret for allowed HTTPS destinations on ports 443 and 8443. Sandbox code cannot read the real secret or use it for local computation, such as signing a request.

    - `networking: CredentialNetworkingParam`

      The destinations where the proxy can substitute this secret. The environment network policy must also allow them.

      - `class Unrestricted`

        Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

        - `type: :unrestricted`

          The type of the object. Always `unrestricted`.

          - `:unrestricted`

      - `class Limited`

        Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

        - `allowed_hosts: Array[String]`

          The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

        - `type: :limited`

          The type of the object. Always `limited`.

          - `:limited`

    - `secret_name: String`

      The environment variable name that receives the placeholder, such as `SERVICE_API_KEY`. Use ASCII letters, digits, and underscores, starting with a letter or underscore. Names starting with `CODEX_` and managed proxy or certificate variable names are reserved.

    - `secret_value: String`

      The write-only secret to store. Never returned in credential resources or supplied directly to sandbox code. Must be nonempty and must not contain carriage returns, newlines, or NUL bytes.

    - `type: :environment_variable`

      The type of the object. Always `environment_variable`.

      - `:environment_variable`

- `name: String`

  The name is trimmed before storage. It must contain 1 to 256 UTF-8 bytes after trimming.

- `metadata: Hash[Symbol, String]`

  Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters. Defaults to an empty map.

### Returns

- `class Credential`

  Metadata for a stored credential. Secret values are never returned.

  - `id: String`

    The ID of the credential.

  - `auth: CredentialAuth`

    The authentication method and non-secret configuration of the credential.

    - `class McpOauth`

      Public metadata for an OAuth credential; tokens and client secrets are never returned.

      - `expires_at: String`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `mcp_server_url: String`

        The HTTPS MCP server URL authorized by this credential.

      - `refresh: Refresh{ client_id, resource, scope, 2 more}`

        Public refresh metadata without refresh tokens or OAuth client secrets.

        - `client_id: String`

          The OAuth client ID used when requesting a new access token.

        - `resource: String`

          The resource URI sent to the OAuth token endpoint during refresh, if configured.

        - `scope: String`

          Space-separated OAuth scopes requested during refresh, if configured.

        - `token_endpoint: String`

          The HTTPS OAuth token endpoint used for refresh.

        - `token_endpoint_auth: McpOauthTokenEndpointAuth`

          How the OAuth client authenticates to the token endpoint, excluding its client secret.

          - `class None`

            Sends the client ID without a client secret.

            - `type: :none`

              The type of the object. Always `none`.

              - `:none`

          - `class ClientSecretBasic`

            Sends the client ID and secret using HTTP Basic authentication.

            - `type: :client_secret_basic`

              The type of the object. Always `client_secret_basic`.

              - `:client_secret_basic`

          - `class ClientSecretPost`

            Sends the client ID and secret in the token request body.

            - `type: :client_secret_post`

              The type of the object. Always `client_secret_post`.

              - `:client_secret_post`

      - `type: :mcp_oauth`

        The type of the object. Always `mcp_oauth`.

        - `:mcp_oauth`

    - `class StaticBearer`

      Metadata for a bearer-token credential, without automatic OAuth refresh.

      - `mcp_server_url: String`

        The HTTPS MCP server URL authorized by this credential.

      - `type: :static_bearer`

        The type of the object. Always `static_bearer`.

        - `:static_bearer`

    - `class EnvironmentVariable`

      Metadata for an HTTP credential used only in OpenAI-hosted environments. Sandbox code receives a placeholder. The proxy substitutes the secret for allowed HTTPS destinations on ports 443 and 8443. The real secret is not available to sandbox code for local computation and is never returned in this resource.

      - `networking: CredentialNetworking`

        The destinations where the proxy can substitute the secret, subject to the environment network policy.

        - `class Unrestricted`

          Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

          - `type: :unrestricted`

            The type of the object. Always `unrestricted`.

            - `:unrestricted`

        - `class Limited`

          Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

          - `allowed_hosts: Array[String]`

            The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

          - `type: :limited`

            The type of the object. Always `limited`.

            - `:limited`

      - `secret_name: String`

        The environment variable name that receives the placeholder in the sandbox.

      - `type: :environment_variable`

        The type of the object. Always `environment_variable`.

        - `:environment_variable`

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the credential was created.

  - `metadata: Hash[Symbol, String]`

    Application-defined key-value pairs associated with this credential.

  - `name: String`

    The human-readable name of the credential.

  - `object: :"vault.credential"`

    The object type. Always `vault.credential`.

    - `:"vault.credential"`

  - `updated_at: Integer`

    The Unix timestamp, in seconds, when the credential was last updated.

  - `vault_id: String`

    The ID of the vault containing this credential.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

credential = openai.beta.agents.vaults.credentials.create(
  "vault_id",
  auth: {access_token: "access_token", mcp_server_url: "mcp_server_url", type: :mcp_oauth},
  name: "x"
)

puts(credential)
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

## Delete a vault credential

`beta.agents.vaults.credentials.delete(credential_id, **kwargs) -> CredentialDeleted`

**delete** `/vaults/{vault_id}/credentials/{credential_id}`

Deletes a vault credential. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vault_id: String`

- `credential_id: String`

### Returns

- `class CredentialDeleted`

  Confirmation that a vault credential was deleted.

  - `id: String`

    The ID of the deleted credential.

  - `deleted: bool`

    Whether the resource was deleted. Always `true`.

  - `object: :"vault.credential.deleted"`

    The object type. Always `vault.credential.deleted`.

    - `:"vault.credential.deleted"`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

credential_deleted = openai.beta.agents.vaults.credentials.delete("credential_id", vault_id: "vault_id")

puts(credential_deleted)
```

#### Response

```json
{
  "id": "id",
  "deleted": true,
  "object": "vault.credential.deleted"
}
```

## List vault credentials

`beta.agents.vaults.credentials.list(vault_id, **kwargs) -> CursorPage<Credential>`

**get** `/vaults/{vault_id}/credentials`

Lists a vault's credentials using ID-based pagination without returning secret values. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vault_id: String`

- `after: String`

  Return resources after this resource ID in the selected order.

- `limit: Integer`

  The maximum number of resources to return. Defaults to 20. Values are clamped between 1 and 100.

- `order: :asc | :desc`

  Sort order by the `created_at` timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `desc`.

  - `:asc`

    Returns resources in ascending order.

  - `:desc`

    Returns resources in descending order.

- `status: VaultStatusFilter`

  Filter by one status or a list, such as `status=active` or `status[]=active&status[]=archived`. Both statuses are included by default.

  - `VaultStatus = :active | :archived`

    Whether a vault or credential is active or archived.

    - `:active`

    - `:archived`

  - `UnionMember1 = Array[VaultStatus]`

    - `:active`

    - `:archived`

### Returns

- `class Credential`

  Metadata for a stored credential. Secret values are never returned.

  - `id: String`

    The ID of the credential.

  - `auth: CredentialAuth`

    The authentication method and non-secret configuration of the credential.

    - `class McpOauth`

      Public metadata for an OAuth credential; tokens and client secrets are never returned.

      - `expires_at: String`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `mcp_server_url: String`

        The HTTPS MCP server URL authorized by this credential.

      - `refresh: Refresh{ client_id, resource, scope, 2 more}`

        Public refresh metadata without refresh tokens or OAuth client secrets.

        - `client_id: String`

          The OAuth client ID used when requesting a new access token.

        - `resource: String`

          The resource URI sent to the OAuth token endpoint during refresh, if configured.

        - `scope: String`

          Space-separated OAuth scopes requested during refresh, if configured.

        - `token_endpoint: String`

          The HTTPS OAuth token endpoint used for refresh.

        - `token_endpoint_auth: McpOauthTokenEndpointAuth`

          How the OAuth client authenticates to the token endpoint, excluding its client secret.

          - `class None`

            Sends the client ID without a client secret.

            - `type: :none`

              The type of the object. Always `none`.

              - `:none`

          - `class ClientSecretBasic`

            Sends the client ID and secret using HTTP Basic authentication.

            - `type: :client_secret_basic`

              The type of the object. Always `client_secret_basic`.

              - `:client_secret_basic`

          - `class ClientSecretPost`

            Sends the client ID and secret in the token request body.

            - `type: :client_secret_post`

              The type of the object. Always `client_secret_post`.

              - `:client_secret_post`

      - `type: :mcp_oauth`

        The type of the object. Always `mcp_oauth`.

        - `:mcp_oauth`

    - `class StaticBearer`

      Metadata for a bearer-token credential, without automatic OAuth refresh.

      - `mcp_server_url: String`

        The HTTPS MCP server URL authorized by this credential.

      - `type: :static_bearer`

        The type of the object. Always `static_bearer`.

        - `:static_bearer`

    - `class EnvironmentVariable`

      Metadata for an HTTP credential used only in OpenAI-hosted environments. Sandbox code receives a placeholder. The proxy substitutes the secret for allowed HTTPS destinations on ports 443 and 8443. The real secret is not available to sandbox code for local computation and is never returned in this resource.

      - `networking: CredentialNetworking`

        The destinations where the proxy can substitute the secret, subject to the environment network policy.

        - `class Unrestricted`

          Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

          - `type: :unrestricted`

            The type of the object. Always `unrestricted`.

            - `:unrestricted`

        - `class Limited`

          Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

          - `allowed_hosts: Array[String]`

            The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

          - `type: :limited`

            The type of the object. Always `limited`.

            - `:limited`

      - `secret_name: String`

        The environment variable name that receives the placeholder in the sandbox.

      - `type: :environment_variable`

        The type of the object. Always `environment_variable`.

        - `:environment_variable`

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the credential was created.

  - `metadata: Hash[Symbol, String]`

    Application-defined key-value pairs associated with this credential.

  - `name: String`

    The human-readable name of the credential.

  - `object: :"vault.credential"`

    The object type. Always `vault.credential`.

    - `:"vault.credential"`

  - `updated_at: Integer`

    The Unix timestamp, in seconds, when the credential was last updated.

  - `vault_id: String`

    The ID of the vault containing this credential.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.beta.agents.vaults.credentials.list("vault_id")

puts(page)
```

#### Response

```json
{
  "data": [
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
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve a vault credential

`beta.agents.vaults.credentials.retrieve(credential_id, **kwargs) -> Credential`

**get** `/vaults/{vault_id}/credentials/{credential_id}`

Retrieves vault credential metadata without returning secret values. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vault_id: String`

- `credential_id: String`

### Returns

- `class Credential`

  Metadata for a stored credential. Secret values are never returned.

  - `id: String`

    The ID of the credential.

  - `auth: CredentialAuth`

    The authentication method and non-secret configuration of the credential.

    - `class McpOauth`

      Public metadata for an OAuth credential; tokens and client secrets are never returned.

      - `expires_at: String`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `mcp_server_url: String`

        The HTTPS MCP server URL authorized by this credential.

      - `refresh: Refresh{ client_id, resource, scope, 2 more}`

        Public refresh metadata without refresh tokens or OAuth client secrets.

        - `client_id: String`

          The OAuth client ID used when requesting a new access token.

        - `resource: String`

          The resource URI sent to the OAuth token endpoint during refresh, if configured.

        - `scope: String`

          Space-separated OAuth scopes requested during refresh, if configured.

        - `token_endpoint: String`

          The HTTPS OAuth token endpoint used for refresh.

        - `token_endpoint_auth: McpOauthTokenEndpointAuth`

          How the OAuth client authenticates to the token endpoint, excluding its client secret.

          - `class None`

            Sends the client ID without a client secret.

            - `type: :none`

              The type of the object. Always `none`.

              - `:none`

          - `class ClientSecretBasic`

            Sends the client ID and secret using HTTP Basic authentication.

            - `type: :client_secret_basic`

              The type of the object. Always `client_secret_basic`.

              - `:client_secret_basic`

          - `class ClientSecretPost`

            Sends the client ID and secret in the token request body.

            - `type: :client_secret_post`

              The type of the object. Always `client_secret_post`.

              - `:client_secret_post`

      - `type: :mcp_oauth`

        The type of the object. Always `mcp_oauth`.

        - `:mcp_oauth`

    - `class StaticBearer`

      Metadata for a bearer-token credential, without automatic OAuth refresh.

      - `mcp_server_url: String`

        The HTTPS MCP server URL authorized by this credential.

      - `type: :static_bearer`

        The type of the object. Always `static_bearer`.

        - `:static_bearer`

    - `class EnvironmentVariable`

      Metadata for an HTTP credential used only in OpenAI-hosted environments. Sandbox code receives a placeholder. The proxy substitutes the secret for allowed HTTPS destinations on ports 443 and 8443. The real secret is not available to sandbox code for local computation and is never returned in this resource.

      - `networking: CredentialNetworking`

        The destinations where the proxy can substitute the secret, subject to the environment network policy.

        - `class Unrestricted`

          Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

          - `type: :unrestricted`

            The type of the object. Always `unrestricted`.

            - `:unrestricted`

        - `class Limited`

          Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

          - `allowed_hosts: Array[String]`

            The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

          - `type: :limited`

            The type of the object. Always `limited`.

            - `:limited`

      - `secret_name: String`

        The environment variable name that receives the placeholder in the sandbox.

      - `type: :environment_variable`

        The type of the object. Always `environment_variable`.

        - `:environment_variable`

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the credential was created.

  - `metadata: Hash[Symbol, String]`

    Application-defined key-value pairs associated with this credential.

  - `name: String`

    The human-readable name of the credential.

  - `object: :"vault.credential"`

    The object type. Always `vault.credential`.

    - `:"vault.credential"`

  - `updated_at: Integer`

    The Unix timestamp, in seconds, when the credential was last updated.

  - `vault_id: String`

    The ID of the vault containing this credential.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

credential = openai.beta.agents.vaults.credentials.retrieve("credential_id", vault_id: "vault_id")

puts(credential)
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

`beta.agents.vaults.credentials.update(credential_id, **kwargs) -> Credential`

**post** `/vaults/{vault_id}/credentials/{credential_id}`

Updates credential metadata or rotates its write-only secret. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vault_id: String`

- `credential_id: String`

- `auth: CredentialAuthRotateParam`

  Replacement values for the credential's existing authentication method.

  - `class McpOauth`

    Rotate an OAuth credential for an HTTPS MCP destination.

    - `type: :mcp_oauth`

      The type of the object. Always `mcp_oauth`.

      - `:mcp_oauth`

    - `access_token: String`

      A write-only replacement OAuth access token.

    - `expires_at: String`

      The replacement expiry as an RFC 3339 timestamp, or `null` to clear it. Omitting this field preserves the expiry unless a new access token is supplied, in which case the expiry is cleared.

    - `refresh: Refresh{ refresh_token, scope, token_endpoint_auth}`

      Optional write-only refresh-token and client-secret updates.

      - `refresh_token: String`

        The replacement refresh token. Omit or pass `null` to keep the stored token. This secret is never returned in resources.

      - `scope: String`

        Replacement space-separated OAuth scopes for refresh requests. Omit to keep the scopes, or pass `null` to stop sending a scope parameter.

      - `token_endpoint_auth: McpOauthTokenEndpointAuthRotateParam`

        Client-secret updates for the existing token endpoint authentication method.

        - `class ClientSecretBasic`

          Updates credentials sent using HTTP Basic authentication.

          - `type: :client_secret_basic`

            The type of the object. Always `client_secret_basic`.

            - `:client_secret_basic`

          - `client_secret: String`

            The replacement OAuth client secret. Omit or pass `null` to keep the stored secret. This secret is never returned in resources.

        - `class ClientSecretPost`

          Updates credentials sent in the token request body.

          - `type: :client_secret_post`

            The type of the object. Always `client_secret_post`.

            - `:client_secret_post`

          - `client_secret: String`

            The replacement OAuth client secret. Omit or pass `null` to keep the stored secret. This secret is never returned in resources.

  - `class StaticBearer`

    Replace the bearer token for the credential's MCP server.

    - `token: String`

      The replacement bearer token. This secret is never returned in credential resources.

    - `type: :static_bearer`

      The type of the object. Always `static_bearer`.

      - `:static_bearer`

  - `class EnvironmentVariable`

    Replace the secret for an OpenAI-hosted environment credential. The environment variable name and networking configuration remain unchanged.

    - `secret_value: String`

      The write-only replacement secret. Never returned in credential resources or supplied directly to sandbox code. Must be nonempty and must not contain carriage returns, newlines, or NUL bytes.

    - `type: :environment_variable`

      The type of the object. Always `environment_variable`.

      - `:environment_variable`

- `metadata: Hash[Symbol, String]`

  Replaces all metadata. Omit to preserve it, or pass {} to clear it. Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters.

### Returns

- `class Credential`

  Metadata for a stored credential. Secret values are never returned.

  - `id: String`

    The ID of the credential.

  - `auth: CredentialAuth`

    The authentication method and non-secret configuration of the credential.

    - `class McpOauth`

      Public metadata for an OAuth credential; tokens and client secrets are never returned.

      - `expires_at: String`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `mcp_server_url: String`

        The HTTPS MCP server URL authorized by this credential.

      - `refresh: Refresh{ client_id, resource, scope, 2 more}`

        Public refresh metadata without refresh tokens or OAuth client secrets.

        - `client_id: String`

          The OAuth client ID used when requesting a new access token.

        - `resource: String`

          The resource URI sent to the OAuth token endpoint during refresh, if configured.

        - `scope: String`

          Space-separated OAuth scopes requested during refresh, if configured.

        - `token_endpoint: String`

          The HTTPS OAuth token endpoint used for refresh.

        - `token_endpoint_auth: McpOauthTokenEndpointAuth`

          How the OAuth client authenticates to the token endpoint, excluding its client secret.

          - `class None`

            Sends the client ID without a client secret.

            - `type: :none`

              The type of the object. Always `none`.

              - `:none`

          - `class ClientSecretBasic`

            Sends the client ID and secret using HTTP Basic authentication.

            - `type: :client_secret_basic`

              The type of the object. Always `client_secret_basic`.

              - `:client_secret_basic`

          - `class ClientSecretPost`

            Sends the client ID and secret in the token request body.

            - `type: :client_secret_post`

              The type of the object. Always `client_secret_post`.

              - `:client_secret_post`

      - `type: :mcp_oauth`

        The type of the object. Always `mcp_oauth`.

        - `:mcp_oauth`

    - `class StaticBearer`

      Metadata for a bearer-token credential, without automatic OAuth refresh.

      - `mcp_server_url: String`

        The HTTPS MCP server URL authorized by this credential.

      - `type: :static_bearer`

        The type of the object. Always `static_bearer`.

        - `:static_bearer`

    - `class EnvironmentVariable`

      Metadata for an HTTP credential used only in OpenAI-hosted environments. Sandbox code receives a placeholder. The proxy substitutes the secret for allowed HTTPS destinations on ports 443 and 8443. The real secret is not available to sandbox code for local computation and is never returned in this resource.

      - `networking: CredentialNetworking`

        The destinations where the proxy can substitute the secret, subject to the environment network policy.

        - `class Unrestricted`

          Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

          - `type: :unrestricted`

            The type of the object. Always `unrestricted`.

            - `:unrestricted`

        - `class Limited`

          Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

          - `allowed_hosts: Array[String]`

            The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

          - `type: :limited`

            The type of the object. Always `limited`.

            - `:limited`

      - `secret_name: String`

        The environment variable name that receives the placeholder in the sandbox.

      - `type: :environment_variable`

        The type of the object. Always `environment_variable`.

        - `:environment_variable`

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the credential was created.

  - `metadata: Hash[Symbol, String]`

    Application-defined key-value pairs associated with this credential.

  - `name: String`

    The human-readable name of the credential.

  - `object: :"vault.credential"`

    The object type. Always `vault.credential`.

    - `:"vault.credential"`

  - `updated_at: Integer`

    The Unix timestamp, in seconds, when the credential was last updated.

  - `vault_id: String`

    The ID of the vault containing this credential.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

credential = openai.beta.agents.vaults.credentials.update("credential_id", vault_id: "vault_id")

puts(credential)
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

- `class Credential`

  Metadata for a stored credential. Secret values are never returned.

  - `id: String`

    The ID of the credential.

  - `auth: CredentialAuth`

    The authentication method and non-secret configuration of the credential.

    - `class McpOauth`

      Public metadata for an OAuth credential; tokens and client secrets are never returned.

      - `expires_at: String`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `mcp_server_url: String`

        The HTTPS MCP server URL authorized by this credential.

      - `refresh: Refresh{ client_id, resource, scope, 2 more}`

        Public refresh metadata without refresh tokens or OAuth client secrets.

        - `client_id: String`

          The OAuth client ID used when requesting a new access token.

        - `resource: String`

          The resource URI sent to the OAuth token endpoint during refresh, if configured.

        - `scope: String`

          Space-separated OAuth scopes requested during refresh, if configured.

        - `token_endpoint: String`

          The HTTPS OAuth token endpoint used for refresh.

        - `token_endpoint_auth: McpOauthTokenEndpointAuth`

          How the OAuth client authenticates to the token endpoint, excluding its client secret.

          - `class None`

            Sends the client ID without a client secret.

            - `type: :none`

              The type of the object. Always `none`.

              - `:none`

          - `class ClientSecretBasic`

            Sends the client ID and secret using HTTP Basic authentication.

            - `type: :client_secret_basic`

              The type of the object. Always `client_secret_basic`.

              - `:client_secret_basic`

          - `class ClientSecretPost`

            Sends the client ID and secret in the token request body.

            - `type: :client_secret_post`

              The type of the object. Always `client_secret_post`.

              - `:client_secret_post`

      - `type: :mcp_oauth`

        The type of the object. Always `mcp_oauth`.

        - `:mcp_oauth`

    - `class StaticBearer`

      Metadata for a bearer-token credential, without automatic OAuth refresh.

      - `mcp_server_url: String`

        The HTTPS MCP server URL authorized by this credential.

      - `type: :static_bearer`

        The type of the object. Always `static_bearer`.

        - `:static_bearer`

    - `class EnvironmentVariable`

      Metadata for an HTTP credential used only in OpenAI-hosted environments. Sandbox code receives a placeholder. The proxy substitutes the secret for allowed HTTPS destinations on ports 443 and 8443. The real secret is not available to sandbox code for local computation and is never returned in this resource.

      - `networking: CredentialNetworking`

        The destinations where the proxy can substitute the secret, subject to the environment network policy.

        - `class Unrestricted`

          Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

          - `type: :unrestricted`

            The type of the object. Always `unrestricted`.

            - `:unrestricted`

        - `class Limited`

          Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

          - `allowed_hosts: Array[String]`

            The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

          - `type: :limited`

            The type of the object. Always `limited`.

            - `:limited`

      - `secret_name: String`

        The environment variable name that receives the placeholder in the sandbox.

      - `type: :environment_variable`

        The type of the object. Always `environment_variable`.

        - `:environment_variable`

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the credential was created.

  - `metadata: Hash[Symbol, String]`

    Application-defined key-value pairs associated with this credential.

  - `name: String`

    The human-readable name of the credential.

  - `object: :"vault.credential"`

    The object type. Always `vault.credential`.

    - `:"vault.credential"`

  - `updated_at: Integer`

    The Unix timestamp, in seconds, when the credential was last updated.

  - `vault_id: String`

    The ID of the vault containing this credential.

### Credential Auth

- `CredentialAuth = McpOauth{ expires_at, mcp_server_url, refresh, type} | StaticBearer{ mcp_server_url, type} | EnvironmentVariable{ networking, secret_name, type}`

  The authentication configuration of a vault credential, excluding secrets.

  - `class McpOauth`

    Public metadata for an OAuth credential; tokens and client secrets are never returned.

    - `expires_at: String`

      When the OAuth access token expires, as an RFC 3339 timestamp, if known.

    - `mcp_server_url: String`

      The HTTPS MCP server URL authorized by this credential.

    - `refresh: Refresh{ client_id, resource, scope, 2 more}`

      Public refresh metadata without refresh tokens or OAuth client secrets.

      - `client_id: String`

        The OAuth client ID used when requesting a new access token.

      - `resource: String`

        The resource URI sent to the OAuth token endpoint during refresh, if configured.

      - `scope: String`

        Space-separated OAuth scopes requested during refresh, if configured.

      - `token_endpoint: String`

        The HTTPS OAuth token endpoint used for refresh.

      - `token_endpoint_auth: McpOauthTokenEndpointAuth`

        How the OAuth client authenticates to the token endpoint, excluding its client secret.

        - `class None`

          Sends the client ID without a client secret.

          - `type: :none`

            The type of the object. Always `none`.

            - `:none`

        - `class ClientSecretBasic`

          Sends the client ID and secret using HTTP Basic authentication.

          - `type: :client_secret_basic`

            The type of the object. Always `client_secret_basic`.

            - `:client_secret_basic`

        - `class ClientSecretPost`

          Sends the client ID and secret in the token request body.

          - `type: :client_secret_post`

            The type of the object. Always `client_secret_post`.

            - `:client_secret_post`

    - `type: :mcp_oauth`

      The type of the object. Always `mcp_oauth`.

      - `:mcp_oauth`

  - `class StaticBearer`

    Metadata for a bearer-token credential, without automatic OAuth refresh.

    - `mcp_server_url: String`

      The HTTPS MCP server URL authorized by this credential.

    - `type: :static_bearer`

      The type of the object. Always `static_bearer`.

      - `:static_bearer`

  - `class EnvironmentVariable`

    Metadata for an HTTP credential used only in OpenAI-hosted environments. Sandbox code receives a placeholder. The proxy substitutes the secret for allowed HTTPS destinations on ports 443 and 8443. The real secret is not available to sandbox code for local computation and is never returned in this resource.

    - `networking: CredentialNetworking`

      The destinations where the proxy can substitute the secret, subject to the environment network policy.

      - `class Unrestricted`

        Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

        - `type: :unrestricted`

          The type of the object. Always `unrestricted`.

          - `:unrestricted`

      - `class Limited`

        Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

        - `allowed_hosts: Array[String]`

          The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

        - `type: :limited`

          The type of the object. Always `limited`.

          - `:limited`

    - `secret_name: String`

      The environment variable name that receives the placeholder in the sandbox.

    - `type: :environment_variable`

      The type of the object. Always `environment_variable`.

      - `:environment_variable`

### Credential Auth Create Param

- `CredentialAuthCreateParam = McpOauth{ access_token, mcp_server_url, type, 2 more} | StaticBearer{ token, mcp_server_url, type} | EnvironmentVariable{ networking, secret_name, secret_value, type}`

  Authentication credentials for an MCP server or an OpenAI-hosted environment.

  - `class McpOauth`

    An OAuth credential for an HTTPS MCP destination.

    - `access_token: String`

      A write-only OAuth access token; never returned by credential resources.

    - `mcp_server_url: String`

      The HTTPS MCP server URL authorized by this credential.

    - `type: :mcp_oauth`

      The type of the object. Always `mcp_oauth`.

      - `:mcp_oauth`

    - `expires_at: String`

      When the OAuth access token expires, as an RFC 3339 timestamp, if known.

    - `refresh: Refresh{ client_id, refresh_token, token_endpoint, 3 more}`

      Optional refresh configuration for an HTTPS OAuth token endpoint.

      - `client_id: String`

        The OAuth client ID used when requesting a new access token.

      - `refresh_token: String`

        The refresh token to store. This secret is never returned in credential resources.

      - `token_endpoint: String`

        The HTTPS OAuth token endpoint used to exchange the refresh token for a new access token.

      - `token_endpoint_auth: McpOauthTokenEndpointAuthCreateParam`

        How the OAuth client authenticates to the token endpoint.

        - `class None`

          Sends the client ID without a client secret.

          - `type: :none`

            The type of the object. Always `none`.

            - `:none`

        - `class ClientSecretBasic`

          Sends the client ID and secret using HTTP Basic authentication.

          - `client_secret: String`

            The OAuth client secret to store. Never returned in credential resources.

          - `type: :client_secret_basic`

            The type of the object. Always `client_secret_basic`.

            - `:client_secret_basic`

        - `class ClientSecretPost`

          Sends the client ID and secret in the token request body.

          - `client_secret: String`

            The OAuth client secret to store. Never returned in credential resources.

          - `type: :client_secret_post`

            The type of the object. Always `client_secret_post`.

            - `:client_secret_post`

      - `resource: String`

        The resource URI to send to the OAuth token endpoint during refresh, if required.

      - `scope: String`

        Space-separated OAuth scopes to request during refresh, if required.

  - `class StaticBearer`

    A bearer token for an MCP server, without automatic OAuth refresh.

    - `token: String`

      The bearer token to store. This secret is never returned in credential resources.

    - `mcp_server_url: String`

      The HTTPS MCP server URL authorized by this credential.

    - `type: :static_bearer`

      The type of the object. Always `static_bearer`.

      - `:static_bearer`

  - `class EnvironmentVariable`

    An HTTP credential for OpenAI-hosted environments only. The sandbox receives an environment variable containing a placeholder, not the secret. Use the placeholder unchanged in outgoing requests. The egress proxy replaces the placeholder with the secret for allowed HTTPS destinations on ports 443 and 8443. Sandbox code cannot read the real secret or use it for local computation, such as signing a request.

    - `networking: CredentialNetworkingParam`

      The destinations where the proxy can substitute this secret. The environment network policy must also allow them.

      - `class Unrestricted`

        Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

        - `type: :unrestricted`

          The type of the object. Always `unrestricted`.

          - `:unrestricted`

      - `class Limited`

        Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

        - `allowed_hosts: Array[String]`

          The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

        - `type: :limited`

          The type of the object. Always `limited`.

          - `:limited`

    - `secret_name: String`

      The environment variable name that receives the placeholder, such as `SERVICE_API_KEY`. Use ASCII letters, digits, and underscores, starting with a letter or underscore. Names starting with `CODEX_` and managed proxy or certificate variable names are reserved.

    - `secret_value: String`

      The write-only secret to store. Never returned in credential resources or supplied directly to sandbox code. Must be nonempty and must not contain carriage returns, newlines, or NUL bytes.

    - `type: :environment_variable`

      The type of the object. Always `environment_variable`.

      - `:environment_variable`

### Credential Auth Rotate Param

- `CredentialAuthRotateParam = McpOauth{ type, access_token, expires_at, refresh} | StaticBearer{ token, type} | EnvironmentVariable{ secret_value, type}`

  Updates to a vault credential without changing its authentication method or destination configuration.

  - `class McpOauth`

    Rotate an OAuth credential for an HTTPS MCP destination.

    - `type: :mcp_oauth`

      The type of the object. Always `mcp_oauth`.

      - `:mcp_oauth`

    - `access_token: String`

      A write-only replacement OAuth access token.

    - `expires_at: String`

      The replacement expiry as an RFC 3339 timestamp, or `null` to clear it. Omitting this field preserves the expiry unless a new access token is supplied, in which case the expiry is cleared.

    - `refresh: Refresh{ refresh_token, scope, token_endpoint_auth}`

      Optional write-only refresh-token and client-secret updates.

      - `refresh_token: String`

        The replacement refresh token. Omit or pass `null` to keep the stored token. This secret is never returned in resources.

      - `scope: String`

        Replacement space-separated OAuth scopes for refresh requests. Omit to keep the scopes, or pass `null` to stop sending a scope parameter.

      - `token_endpoint_auth: McpOauthTokenEndpointAuthRotateParam`

        Client-secret updates for the existing token endpoint authentication method.

        - `class ClientSecretBasic`

          Updates credentials sent using HTTP Basic authentication.

          - `type: :client_secret_basic`

            The type of the object. Always `client_secret_basic`.

            - `:client_secret_basic`

          - `client_secret: String`

            The replacement OAuth client secret. Omit or pass `null` to keep the stored secret. This secret is never returned in resources.

        - `class ClientSecretPost`

          Updates credentials sent in the token request body.

          - `type: :client_secret_post`

            The type of the object. Always `client_secret_post`.

            - `:client_secret_post`

          - `client_secret: String`

            The replacement OAuth client secret. Omit or pass `null` to keep the stored secret. This secret is never returned in resources.

  - `class StaticBearer`

    Replace the bearer token for the credential's MCP server.

    - `token: String`

      The replacement bearer token. This secret is never returned in credential resources.

    - `type: :static_bearer`

      The type of the object. Always `static_bearer`.

      - `:static_bearer`

  - `class EnvironmentVariable`

    Replace the secret for an OpenAI-hosted environment credential. The environment variable name and networking configuration remain unchanged.

    - `secret_value: String`

      The write-only replacement secret. Never returned in credential resources or supplied directly to sandbox code. Must be nonempty and must not contain carriage returns, newlines, or NUL bytes.

    - `type: :environment_variable`

      The type of the object. Always `environment_variable`.

      - `:environment_variable`

### Credential Deleted

- `class CredentialDeleted`

  Confirmation that a vault credential was deleted.

  - `id: String`

    The ID of the deleted credential.

  - `deleted: bool`

    Whether the resource was deleted. Always `true`.

  - `object: :"vault.credential.deleted"`

    The object type. Always `vault.credential.deleted`.

    - `:"vault.credential.deleted"`

### Credential Networking

- `CredentialNetworking = Unrestricted{ type} | Limited{ allowed_hosts, type}`

  Destination permissions for an environment-variable credential. These do not grant network access to the environment.

  - `class Unrestricted`

    Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

    - `type: :unrestricted`

      The type of the object. Always `unrestricted`.

      - `:unrestricted`

  - `class Limited`

    Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

    - `allowed_hosts: Array[String]`

      The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

    - `type: :limited`

      The type of the object. Always `limited`.

      - `:limited`

### Credential Networking Param

- `CredentialNetworkingParam = Unrestricted{ type} | Limited{ allowed_hosts, type}`

  Destination permissions for an environment-variable credential. These do not grant network access to the environment.

  - `class Unrestricted`

    Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

    - `type: :unrestricted`

      The type of the object. Always `unrestricted`.

      - `:unrestricted`

  - `class Limited`

    Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

    - `allowed_hosts: Array[String]`

      The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

    - `type: :limited`

      The type of the object. Always `limited`.

      - `:limited`

### Mcp OAuth Token Endpoint Auth

- `McpOauthTokenEndpointAuth = None{ type} | ClientSecretBasic{ type} | ClientSecretPost{ type}`

  The client authentication method used for OAuth token refresh.

  - `class None`

    Sends the client ID without a client secret.

    - `type: :none`

      The type of the object. Always `none`.

      - `:none`

  - `class ClientSecretBasic`

    Sends the client ID and secret using HTTP Basic authentication.

    - `type: :client_secret_basic`

      The type of the object. Always `client_secret_basic`.

      - `:client_secret_basic`

  - `class ClientSecretPost`

    Sends the client ID and secret in the token request body.

    - `type: :client_secret_post`

      The type of the object. Always `client_secret_post`.

      - `:client_secret_post`

### Mcp OAuth Token Endpoint Auth Create Param

- `McpOauthTokenEndpointAuthCreateParam = None{ type} | ClientSecretBasic{ client_secret, type} | ClientSecretPost{ client_secret, type}`

  Client authentication credentials for OAuth token refresh.

  - `class None`

    Sends the client ID without a client secret.

    - `type: :none`

      The type of the object. Always `none`.

      - `:none`

  - `class ClientSecretBasic`

    Sends the client ID and secret using HTTP Basic authentication.

    - `client_secret: String`

      The OAuth client secret to store. Never returned in credential resources.

    - `type: :client_secret_basic`

      The type of the object. Always `client_secret_basic`.

      - `:client_secret_basic`

  - `class ClientSecretPost`

    Sends the client ID and secret in the token request body.

    - `client_secret: String`

      The OAuth client secret to store. Never returned in credential resources.

    - `type: :client_secret_post`

      The type of the object. Always `client_secret_post`.

      - `:client_secret_post`

### Mcp OAuth Token Endpoint Auth Rotate Param

- `McpOauthTokenEndpointAuthRotateParam = ClientSecretBasic{ type, client_secret} | ClientSecretPost{ type, client_secret}`

  Client-secret updates that preserve the credential's OAuth authentication method.

  - `class ClientSecretBasic`

    Updates credentials sent using HTTP Basic authentication.

    - `type: :client_secret_basic`

      The type of the object. Always `client_secret_basic`.

      - `:client_secret_basic`

    - `client_secret: String`

      The replacement OAuth client secret. Omit or pass `null` to keep the stored secret. This secret is never returned in resources.

  - `class ClientSecretPost`

    Updates credentials sent in the token request body.

    - `type: :client_secret_post`

      The type of the object. Always `client_secret_post`.

      - `:client_secret_post`

    - `client_secret: String`

      The replacement OAuth client secret. Omit or pass `null` to keep the stored secret. This secret is never returned in resources.
