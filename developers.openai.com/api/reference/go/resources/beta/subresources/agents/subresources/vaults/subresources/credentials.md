<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/subresources/vaults/subresources/credentials/ -->

# Credentials

## Create a vault credential

`client.Beta.Agents.Vaults.Credentials.New(ctx, vaultID, body) (*Credential, error)`

**post** `/vaults/{vault_id}/credentials`

Creates a vault credential. Secret values are write-only and are never returned. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vaultID string`

- `body BetaAgentVaultCredentialNewParams`

  - `Auth param.Field[CredentialAuthCreateParamUnionResp]`

    The authentication method and write-only secret values to store.

  - `Name param.Field[string]`

    The name is trimmed before storage. It must contain 1 to 256 UTF-8 bytes after trimming.

  - `Metadata param.Field[map[string, string]]`

    Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters. Defaults to an empty map.

### Returns

- `type Credential struct{…}`

  Metadata for a stored credential. Secret values are never returned.

  - `ID string`

    The ID of the credential.

  - `Auth CredentialAuthUnion`

    The authentication method and non-secret configuration of the credential.

    - `type CredentialAuthMcpOAuth struct{…}`

      Public metadata for an OAuth credential; tokens and client secrets are never returned.

      - `ExpiresAt string`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `McpServerURL string`

        The HTTPS MCP server URL authorized by this credential.

      - `Refresh CredentialAuthMcpOAuthRefresh`

        Public refresh metadata without refresh tokens or OAuth client secrets.

        - `ClientID string`

          The OAuth client ID used when requesting a new access token.

        - `Resource string`

          The resource URI sent to the OAuth token endpoint during refresh, if configured.

        - `Scope string`

          Space-separated OAuth scopes requested during refresh, if configured.

        - `TokenEndpoint string`

          The HTTPS OAuth token endpoint used for refresh.

        - `TokenEndpointAuth McpOAuthTokenEndpointAuthUnion`

          How the OAuth client authenticates to the token endpoint, excluding its client secret.

          - `type McpOAuthTokenEndpointAuthNone struct{…}`

            Sends the client ID without a client secret.

            - `Type None`

              The type of the object. Always `none`.

              - `const NoneNone None = "none"`

          - `type McpOAuthTokenEndpointAuthClientSecretBasic struct{…}`

            Sends the client ID and secret using HTTP Basic authentication.

            - `Type ClientSecretBasic`

              The type of the object. Always `client_secret_basic`.

              - `const ClientSecretBasicClientSecretBasic ClientSecretBasic = "client_secret_basic"`

          - `type McpOAuthTokenEndpointAuthClientSecretPost struct{…}`

            Sends the client ID and secret in the token request body.

            - `Type ClientSecretPost`

              The type of the object. Always `client_secret_post`.

              - `const ClientSecretPostClientSecretPost ClientSecretPost = "client_secret_post"`

      - `Type McpOAuth`

        The type of the object. Always `mcp_oauth`.

        - `const McpOAuthMcpOAuth McpOAuth = "mcp_oauth"`

    - `type CredentialAuthStaticBearer struct{…}`

      Metadata for a bearer-token credential, without automatic OAuth refresh.

      - `McpServerURL string`

        The HTTPS MCP server URL authorized by this credential.

      - `Type StaticBearer`

        The type of the object. Always `static_bearer`.

        - `const StaticBearerStaticBearer StaticBearer = "static_bearer"`

    - `type CredentialAuthEnvironmentVariable struct{…}`

      Metadata for an HTTP credential used only in OpenAI-hosted environments. Sandbox code receives a placeholder. The proxy substitutes the secret for allowed HTTPS destinations on ports 443 and 8443. The real secret is not available to sandbox code for local computation and is never returned in this resource.

      - `Networking CredentialNetworkingUnion`

        The destinations where the proxy can substitute the secret, subject to the environment network policy.

        - `type CredentialNetworkingUnrestricted struct{…}`

          Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

          - `Type Unrestricted`

            The type of the object. Always `unrestricted`.

            - `const UnrestrictedUnrestricted Unrestricted = "unrestricted"`

        - `type CredentialNetworkingLimited struct{…}`

          Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

          - `AllowedHosts []string`

            The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

          - `Type Limited`

            The type of the object. Always `limited`.

            - `const LimitedLimited Limited = "limited"`

      - `SecretName string`

        The environment variable name that receives the placeholder in the sandbox.

      - `Type EnvironmentVariable`

        The type of the object. Always `environment_variable`.

        - `const EnvironmentVariableEnvironmentVariable EnvironmentVariable = "environment_variable"`

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the credential was created.

  - `Metadata map[string, string]`

    Application-defined key-value pairs associated with this credential.

  - `Name string`

    The human-readable name of the credential.

  - `Object VaultCredential`

    The object type. Always `vault.credential`.

    - `const VaultCredentialVaultCredential VaultCredential = "vault.credential"`

  - `UpdatedAt int64`

    The Unix timestamp, in seconds, when the credential was last updated.

  - `VaultID string`

    The ID of the vault containing this credential.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  credential, err := client.Beta.Agents.Vaults.Credentials.New(
    context.TODO(),
    "vault_id",
    openai.BetaAgentVaultCredentialNewParams{
      Auth: openai.CredentialAuthCreateParamUnion{
        OfMcpOauth: &openai.CredentialAuthCreateParamMcpOAuth{
          AccessToken: "access_token",
          McpServerURL: "mcp_server_url",
        },
      },
      Name: "x",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", credential.ID)
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

## Delete a vault credential

`client.Beta.Agents.Vaults.Credentials.Delete(ctx, vaultID, credentialID) (*CredentialDeleted, error)`

**delete** `/vaults/{vault_id}/credentials/{credential_id}`

Deletes a vault credential. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vaultID string`

- `credentialID string`

### Returns

- `type CredentialDeleted struct{…}`

  Confirmation that a vault credential was deleted.

  - `ID string`

    The ID of the deleted credential.

  - `Deleted bool`

    Whether the resource was deleted. Always `true`.

  - `Object VaultCredentialDeleted`

    The object type. Always `vault.credential.deleted`.

    - `const VaultCredentialDeletedVaultCredentialDeleted VaultCredentialDeleted = "vault.credential.deleted"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  credentialDeleted, err := client.Beta.Agents.Vaults.Credentials.Delete(
    context.TODO(),
    "vault_id",
    "credential_id",
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", credentialDeleted.ID)
}
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

`client.Beta.Agents.Vaults.Credentials.List(ctx, vaultID, query) (*CursorPage[Credential], error)`

**get** `/vaults/{vault_id}/credentials`

Lists a vault's credentials using ID-based pagination without returning secret values. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vaultID string`

- `query BetaAgentVaultCredentialListParams`

  - `After param.Field[string]`

    Return resources after this resource ID in the selected order.

  - `Limit param.Field[int64]`

    The maximum number of resources to return. Defaults to 20. Values are clamped between 1 and 100.

  - `Order param.Field[BetaAgentVaultCredentialListParamsOrder]`

    Sort order by the `created_at` timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `desc`.

    - `const BetaAgentVaultCredentialListParamsOrderAsc BetaAgentVaultCredentialListParamsOrder = "asc"`

      Returns resources in ascending order.

    - `const BetaAgentVaultCredentialListParamsOrderDesc BetaAgentVaultCredentialListParamsOrder = "desc"`

      Returns resources in descending order.

  - `Status param.Field[VaultStatusFilterUnion]`

    Filter by one status or a list, such as `status=active` or `status[]=active&status[]=archived`. Both statuses are included by default.

### Returns

- `type Credential struct{…}`

  Metadata for a stored credential. Secret values are never returned.

  - `ID string`

    The ID of the credential.

  - `Auth CredentialAuthUnion`

    The authentication method and non-secret configuration of the credential.

    - `type CredentialAuthMcpOAuth struct{…}`

      Public metadata for an OAuth credential; tokens and client secrets are never returned.

      - `ExpiresAt string`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `McpServerURL string`

        The HTTPS MCP server URL authorized by this credential.

      - `Refresh CredentialAuthMcpOAuthRefresh`

        Public refresh metadata without refresh tokens or OAuth client secrets.

        - `ClientID string`

          The OAuth client ID used when requesting a new access token.

        - `Resource string`

          The resource URI sent to the OAuth token endpoint during refresh, if configured.

        - `Scope string`

          Space-separated OAuth scopes requested during refresh, if configured.

        - `TokenEndpoint string`

          The HTTPS OAuth token endpoint used for refresh.

        - `TokenEndpointAuth McpOAuthTokenEndpointAuthUnion`

          How the OAuth client authenticates to the token endpoint, excluding its client secret.

          - `type McpOAuthTokenEndpointAuthNone struct{…}`

            Sends the client ID without a client secret.

            - `Type None`

              The type of the object. Always `none`.

              - `const NoneNone None = "none"`

          - `type McpOAuthTokenEndpointAuthClientSecretBasic struct{…}`

            Sends the client ID and secret using HTTP Basic authentication.

            - `Type ClientSecretBasic`

              The type of the object. Always `client_secret_basic`.

              - `const ClientSecretBasicClientSecretBasic ClientSecretBasic = "client_secret_basic"`

          - `type McpOAuthTokenEndpointAuthClientSecretPost struct{…}`

            Sends the client ID and secret in the token request body.

            - `Type ClientSecretPost`

              The type of the object. Always `client_secret_post`.

              - `const ClientSecretPostClientSecretPost ClientSecretPost = "client_secret_post"`

      - `Type McpOAuth`

        The type of the object. Always `mcp_oauth`.

        - `const McpOAuthMcpOAuth McpOAuth = "mcp_oauth"`

    - `type CredentialAuthStaticBearer struct{…}`

      Metadata for a bearer-token credential, without automatic OAuth refresh.

      - `McpServerURL string`

        The HTTPS MCP server URL authorized by this credential.

      - `Type StaticBearer`

        The type of the object. Always `static_bearer`.

        - `const StaticBearerStaticBearer StaticBearer = "static_bearer"`

    - `type CredentialAuthEnvironmentVariable struct{…}`

      Metadata for an HTTP credential used only in OpenAI-hosted environments. Sandbox code receives a placeholder. The proxy substitutes the secret for allowed HTTPS destinations on ports 443 and 8443. The real secret is not available to sandbox code for local computation and is never returned in this resource.

      - `Networking CredentialNetworkingUnion`

        The destinations where the proxy can substitute the secret, subject to the environment network policy.

        - `type CredentialNetworkingUnrestricted struct{…}`

          Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

          - `Type Unrestricted`

            The type of the object. Always `unrestricted`.

            - `const UnrestrictedUnrestricted Unrestricted = "unrestricted"`

        - `type CredentialNetworkingLimited struct{…}`

          Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

          - `AllowedHosts []string`

            The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

          - `Type Limited`

            The type of the object. Always `limited`.

            - `const LimitedLimited Limited = "limited"`

      - `SecretName string`

        The environment variable name that receives the placeholder in the sandbox.

      - `Type EnvironmentVariable`

        The type of the object. Always `environment_variable`.

        - `const EnvironmentVariableEnvironmentVariable EnvironmentVariable = "environment_variable"`

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the credential was created.

  - `Metadata map[string, string]`

    Application-defined key-value pairs associated with this credential.

  - `Name string`

    The human-readable name of the credential.

  - `Object VaultCredential`

    The object type. Always `vault.credential`.

    - `const VaultCredentialVaultCredential VaultCredential = "vault.credential"`

  - `UpdatedAt int64`

    The Unix timestamp, in seconds, when the credential was last updated.

  - `VaultID string`

    The ID of the vault containing this credential.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  page, err := client.Beta.Agents.Vaults.Credentials.List(
    context.TODO(),
    "vault_id",
    openai.BetaAgentVaultCredentialListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
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

`client.Beta.Agents.Vaults.Credentials.Get(ctx, vaultID, credentialID) (*Credential, error)`

**get** `/vaults/{vault_id}/credentials/{credential_id}`

Retrieves vault credential metadata without returning secret values. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vaultID string`

- `credentialID string`

### Returns

- `type Credential struct{…}`

  Metadata for a stored credential. Secret values are never returned.

  - `ID string`

    The ID of the credential.

  - `Auth CredentialAuthUnion`

    The authentication method and non-secret configuration of the credential.

    - `type CredentialAuthMcpOAuth struct{…}`

      Public metadata for an OAuth credential; tokens and client secrets are never returned.

      - `ExpiresAt string`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `McpServerURL string`

        The HTTPS MCP server URL authorized by this credential.

      - `Refresh CredentialAuthMcpOAuthRefresh`

        Public refresh metadata without refresh tokens or OAuth client secrets.

        - `ClientID string`

          The OAuth client ID used when requesting a new access token.

        - `Resource string`

          The resource URI sent to the OAuth token endpoint during refresh, if configured.

        - `Scope string`

          Space-separated OAuth scopes requested during refresh, if configured.

        - `TokenEndpoint string`

          The HTTPS OAuth token endpoint used for refresh.

        - `TokenEndpointAuth McpOAuthTokenEndpointAuthUnion`

          How the OAuth client authenticates to the token endpoint, excluding its client secret.

          - `type McpOAuthTokenEndpointAuthNone struct{…}`

            Sends the client ID without a client secret.

            - `Type None`

              The type of the object. Always `none`.

              - `const NoneNone None = "none"`

          - `type McpOAuthTokenEndpointAuthClientSecretBasic struct{…}`

            Sends the client ID and secret using HTTP Basic authentication.

            - `Type ClientSecretBasic`

              The type of the object. Always `client_secret_basic`.

              - `const ClientSecretBasicClientSecretBasic ClientSecretBasic = "client_secret_basic"`

          - `type McpOAuthTokenEndpointAuthClientSecretPost struct{…}`

            Sends the client ID and secret in the token request body.

            - `Type ClientSecretPost`

              The type of the object. Always `client_secret_post`.

              - `const ClientSecretPostClientSecretPost ClientSecretPost = "client_secret_post"`

      - `Type McpOAuth`

        The type of the object. Always `mcp_oauth`.

        - `const McpOAuthMcpOAuth McpOAuth = "mcp_oauth"`

    - `type CredentialAuthStaticBearer struct{…}`

      Metadata for a bearer-token credential, without automatic OAuth refresh.

      - `McpServerURL string`

        The HTTPS MCP server URL authorized by this credential.

      - `Type StaticBearer`

        The type of the object. Always `static_bearer`.

        - `const StaticBearerStaticBearer StaticBearer = "static_bearer"`

    - `type CredentialAuthEnvironmentVariable struct{…}`

      Metadata for an HTTP credential used only in OpenAI-hosted environments. Sandbox code receives a placeholder. The proxy substitutes the secret for allowed HTTPS destinations on ports 443 and 8443. The real secret is not available to sandbox code for local computation and is never returned in this resource.

      - `Networking CredentialNetworkingUnion`

        The destinations where the proxy can substitute the secret, subject to the environment network policy.

        - `type CredentialNetworkingUnrestricted struct{…}`

          Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

          - `Type Unrestricted`

            The type of the object. Always `unrestricted`.

            - `const UnrestrictedUnrestricted Unrestricted = "unrestricted"`

        - `type CredentialNetworkingLimited struct{…}`

          Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

          - `AllowedHosts []string`

            The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

          - `Type Limited`

            The type of the object. Always `limited`.

            - `const LimitedLimited Limited = "limited"`

      - `SecretName string`

        The environment variable name that receives the placeholder in the sandbox.

      - `Type EnvironmentVariable`

        The type of the object. Always `environment_variable`.

        - `const EnvironmentVariableEnvironmentVariable EnvironmentVariable = "environment_variable"`

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the credential was created.

  - `Metadata map[string, string]`

    Application-defined key-value pairs associated with this credential.

  - `Name string`

    The human-readable name of the credential.

  - `Object VaultCredential`

    The object type. Always `vault.credential`.

    - `const VaultCredentialVaultCredential VaultCredential = "vault.credential"`

  - `UpdatedAt int64`

    The Unix timestamp, in seconds, when the credential was last updated.

  - `VaultID string`

    The ID of the vault containing this credential.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  credential, err := client.Beta.Agents.Vaults.Credentials.Get(
    context.TODO(),
    "vault_id",
    "credential_id",
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", credential.ID)
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

`client.Beta.Agents.Vaults.Credentials.Update(ctx, vaultID, credentialID, body) (*Credential, error)`

**post** `/vaults/{vault_id}/credentials/{credential_id}`

Updates credential metadata or rotates its write-only secret. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vaultID string`

- `credentialID string`

- `body BetaAgentVaultCredentialUpdateParams`

  - `Auth param.Field[CredentialAuthRotateParamUnionResp]`

    Replacement values for the credential's existing authentication method.

  - `Metadata param.Field[map[string, string]]`

    Replaces all metadata. Omit to preserve it, or pass {} to clear it. Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters.

### Returns

- `type Credential struct{…}`

  Metadata for a stored credential. Secret values are never returned.

  - `ID string`

    The ID of the credential.

  - `Auth CredentialAuthUnion`

    The authentication method and non-secret configuration of the credential.

    - `type CredentialAuthMcpOAuth struct{…}`

      Public metadata for an OAuth credential; tokens and client secrets are never returned.

      - `ExpiresAt string`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `McpServerURL string`

        The HTTPS MCP server URL authorized by this credential.

      - `Refresh CredentialAuthMcpOAuthRefresh`

        Public refresh metadata without refresh tokens or OAuth client secrets.

        - `ClientID string`

          The OAuth client ID used when requesting a new access token.

        - `Resource string`

          The resource URI sent to the OAuth token endpoint during refresh, if configured.

        - `Scope string`

          Space-separated OAuth scopes requested during refresh, if configured.

        - `TokenEndpoint string`

          The HTTPS OAuth token endpoint used for refresh.

        - `TokenEndpointAuth McpOAuthTokenEndpointAuthUnion`

          How the OAuth client authenticates to the token endpoint, excluding its client secret.

          - `type McpOAuthTokenEndpointAuthNone struct{…}`

            Sends the client ID without a client secret.

            - `Type None`

              The type of the object. Always `none`.

              - `const NoneNone None = "none"`

          - `type McpOAuthTokenEndpointAuthClientSecretBasic struct{…}`

            Sends the client ID and secret using HTTP Basic authentication.

            - `Type ClientSecretBasic`

              The type of the object. Always `client_secret_basic`.

              - `const ClientSecretBasicClientSecretBasic ClientSecretBasic = "client_secret_basic"`

          - `type McpOAuthTokenEndpointAuthClientSecretPost struct{…}`

            Sends the client ID and secret in the token request body.

            - `Type ClientSecretPost`

              The type of the object. Always `client_secret_post`.

              - `const ClientSecretPostClientSecretPost ClientSecretPost = "client_secret_post"`

      - `Type McpOAuth`

        The type of the object. Always `mcp_oauth`.

        - `const McpOAuthMcpOAuth McpOAuth = "mcp_oauth"`

    - `type CredentialAuthStaticBearer struct{…}`

      Metadata for a bearer-token credential, without automatic OAuth refresh.

      - `McpServerURL string`

        The HTTPS MCP server URL authorized by this credential.

      - `Type StaticBearer`

        The type of the object. Always `static_bearer`.

        - `const StaticBearerStaticBearer StaticBearer = "static_bearer"`

    - `type CredentialAuthEnvironmentVariable struct{…}`

      Metadata for an HTTP credential used only in OpenAI-hosted environments. Sandbox code receives a placeholder. The proxy substitutes the secret for allowed HTTPS destinations on ports 443 and 8443. The real secret is not available to sandbox code for local computation and is never returned in this resource.

      - `Networking CredentialNetworkingUnion`

        The destinations where the proxy can substitute the secret, subject to the environment network policy.

        - `type CredentialNetworkingUnrestricted struct{…}`

          Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

          - `Type Unrestricted`

            The type of the object. Always `unrestricted`.

            - `const UnrestrictedUnrestricted Unrestricted = "unrestricted"`

        - `type CredentialNetworkingLimited struct{…}`

          Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

          - `AllowedHosts []string`

            The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

          - `Type Limited`

            The type of the object. Always `limited`.

            - `const LimitedLimited Limited = "limited"`

      - `SecretName string`

        The environment variable name that receives the placeholder in the sandbox.

      - `Type EnvironmentVariable`

        The type of the object. Always `environment_variable`.

        - `const EnvironmentVariableEnvironmentVariable EnvironmentVariable = "environment_variable"`

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the credential was created.

  - `Metadata map[string, string]`

    Application-defined key-value pairs associated with this credential.

  - `Name string`

    The human-readable name of the credential.

  - `Object VaultCredential`

    The object type. Always `vault.credential`.

    - `const VaultCredentialVaultCredential VaultCredential = "vault.credential"`

  - `UpdatedAt int64`

    The Unix timestamp, in seconds, when the credential was last updated.

  - `VaultID string`

    The ID of the vault containing this credential.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  credential, err := client.Beta.Agents.Vaults.Credentials.Update(
    context.TODO(),
    "vault_id",
    "credential_id",
    openai.BetaAgentVaultCredentialUpdateParams{
      Metadata: map[string]string{
      },
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", credential.ID)
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

- `type Credential struct{…}`

  Metadata for a stored credential. Secret values are never returned.

  - `ID string`

    The ID of the credential.

  - `Auth CredentialAuthUnion`

    The authentication method and non-secret configuration of the credential.

    - `type CredentialAuthMcpOAuth struct{…}`

      Public metadata for an OAuth credential; tokens and client secrets are never returned.

      - `ExpiresAt string`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `McpServerURL string`

        The HTTPS MCP server URL authorized by this credential.

      - `Refresh CredentialAuthMcpOAuthRefresh`

        Public refresh metadata without refresh tokens or OAuth client secrets.

        - `ClientID string`

          The OAuth client ID used when requesting a new access token.

        - `Resource string`

          The resource URI sent to the OAuth token endpoint during refresh, if configured.

        - `Scope string`

          Space-separated OAuth scopes requested during refresh, if configured.

        - `TokenEndpoint string`

          The HTTPS OAuth token endpoint used for refresh.

        - `TokenEndpointAuth McpOAuthTokenEndpointAuthUnion`

          How the OAuth client authenticates to the token endpoint, excluding its client secret.

          - `type McpOAuthTokenEndpointAuthNone struct{…}`

            Sends the client ID without a client secret.

            - `Type None`

              The type of the object. Always `none`.

              - `const NoneNone None = "none"`

          - `type McpOAuthTokenEndpointAuthClientSecretBasic struct{…}`

            Sends the client ID and secret using HTTP Basic authentication.

            - `Type ClientSecretBasic`

              The type of the object. Always `client_secret_basic`.

              - `const ClientSecretBasicClientSecretBasic ClientSecretBasic = "client_secret_basic"`

          - `type McpOAuthTokenEndpointAuthClientSecretPost struct{…}`

            Sends the client ID and secret in the token request body.

            - `Type ClientSecretPost`

              The type of the object. Always `client_secret_post`.

              - `const ClientSecretPostClientSecretPost ClientSecretPost = "client_secret_post"`

      - `Type McpOAuth`

        The type of the object. Always `mcp_oauth`.

        - `const McpOAuthMcpOAuth McpOAuth = "mcp_oauth"`

    - `type CredentialAuthStaticBearer struct{…}`

      Metadata for a bearer-token credential, without automatic OAuth refresh.

      - `McpServerURL string`

        The HTTPS MCP server URL authorized by this credential.

      - `Type StaticBearer`

        The type of the object. Always `static_bearer`.

        - `const StaticBearerStaticBearer StaticBearer = "static_bearer"`

    - `type CredentialAuthEnvironmentVariable struct{…}`

      Metadata for an HTTP credential used only in OpenAI-hosted environments. Sandbox code receives a placeholder. The proxy substitutes the secret for allowed HTTPS destinations on ports 443 and 8443. The real secret is not available to sandbox code for local computation and is never returned in this resource.

      - `Networking CredentialNetworkingUnion`

        The destinations where the proxy can substitute the secret, subject to the environment network policy.

        - `type CredentialNetworkingUnrestricted struct{…}`

          Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

          - `Type Unrestricted`

            The type of the object. Always `unrestricted`.

            - `const UnrestrictedUnrestricted Unrestricted = "unrestricted"`

        - `type CredentialNetworkingLimited struct{…}`

          Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

          - `AllowedHosts []string`

            The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

          - `Type Limited`

            The type of the object. Always `limited`.

            - `const LimitedLimited Limited = "limited"`

      - `SecretName string`

        The environment variable name that receives the placeholder in the sandbox.

      - `Type EnvironmentVariable`

        The type of the object. Always `environment_variable`.

        - `const EnvironmentVariableEnvironmentVariable EnvironmentVariable = "environment_variable"`

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the credential was created.

  - `Metadata map[string, string]`

    Application-defined key-value pairs associated with this credential.

  - `Name string`

    The human-readable name of the credential.

  - `Object VaultCredential`

    The object type. Always `vault.credential`.

    - `const VaultCredentialVaultCredential VaultCredential = "vault.credential"`

  - `UpdatedAt int64`

    The Unix timestamp, in seconds, when the credential was last updated.

  - `VaultID string`

    The ID of the vault containing this credential.

### Credential Auth

- `type CredentialAuthUnion interface{…}`

  The authentication configuration of a vault credential, excluding secrets.

  - `type CredentialAuthMcpOAuth struct{…}`

    Public metadata for an OAuth credential; tokens and client secrets are never returned.

    - `ExpiresAt string`

      When the OAuth access token expires, as an RFC 3339 timestamp, if known.

    - `McpServerURL string`

      The HTTPS MCP server URL authorized by this credential.

    - `Refresh CredentialAuthMcpOAuthRefresh`

      Public refresh metadata without refresh tokens or OAuth client secrets.

      - `ClientID string`

        The OAuth client ID used when requesting a new access token.

      - `Resource string`

        The resource URI sent to the OAuth token endpoint during refresh, if configured.

      - `Scope string`

        Space-separated OAuth scopes requested during refresh, if configured.

      - `TokenEndpoint string`

        The HTTPS OAuth token endpoint used for refresh.

      - `TokenEndpointAuth McpOAuthTokenEndpointAuthUnion`

        How the OAuth client authenticates to the token endpoint, excluding its client secret.

        - `type McpOAuthTokenEndpointAuthNone struct{…}`

          Sends the client ID without a client secret.

          - `Type None`

            The type of the object. Always `none`.

            - `const NoneNone None = "none"`

        - `type McpOAuthTokenEndpointAuthClientSecretBasic struct{…}`

          Sends the client ID and secret using HTTP Basic authentication.

          - `Type ClientSecretBasic`

            The type of the object. Always `client_secret_basic`.

            - `const ClientSecretBasicClientSecretBasic ClientSecretBasic = "client_secret_basic"`

        - `type McpOAuthTokenEndpointAuthClientSecretPost struct{…}`

          Sends the client ID and secret in the token request body.

          - `Type ClientSecretPost`

            The type of the object. Always `client_secret_post`.

            - `const ClientSecretPostClientSecretPost ClientSecretPost = "client_secret_post"`

    - `Type McpOAuth`

      The type of the object. Always `mcp_oauth`.

      - `const McpOAuthMcpOAuth McpOAuth = "mcp_oauth"`

  - `type CredentialAuthStaticBearer struct{…}`

    Metadata for a bearer-token credential, without automatic OAuth refresh.

    - `McpServerURL string`

      The HTTPS MCP server URL authorized by this credential.

    - `Type StaticBearer`

      The type of the object. Always `static_bearer`.

      - `const StaticBearerStaticBearer StaticBearer = "static_bearer"`

  - `type CredentialAuthEnvironmentVariable struct{…}`

    Metadata for an HTTP credential used only in OpenAI-hosted environments. Sandbox code receives a placeholder. The proxy substitutes the secret for allowed HTTPS destinations on ports 443 and 8443. The real secret is not available to sandbox code for local computation and is never returned in this resource.

    - `Networking CredentialNetworkingUnion`

      The destinations where the proxy can substitute the secret, subject to the environment network policy.

      - `type CredentialNetworkingUnrestricted struct{…}`

        Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

        - `Type Unrestricted`

          The type of the object. Always `unrestricted`.

          - `const UnrestrictedUnrestricted Unrestricted = "unrestricted"`

      - `type CredentialNetworkingLimited struct{…}`

        Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

        - `AllowedHosts []string`

          The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

        - `Type Limited`

          The type of the object. Always `limited`.

          - `const LimitedLimited Limited = "limited"`

    - `SecretName string`

      The environment variable name that receives the placeholder in the sandbox.

    - `Type EnvironmentVariable`

      The type of the object. Always `environment_variable`.

      - `const EnvironmentVariableEnvironmentVariable EnvironmentVariable = "environment_variable"`

### Credential Auth Create Param

- `type CredentialAuthCreateParamUnionResp interface{…}`

  Authentication credentials for an MCP server or an OpenAI-hosted environment.

  - `CredentialAuthCreateParamMcpOAuthResp`

    - `AccessToken string`

      A write-only OAuth access token; never returned by credential resources.

    - `McpServerURL string`

      The HTTPS MCP server URL authorized by this credential.

    - `Type McpOAuth`

      The type of the object. Always `mcp_oauth`.

      - `const McpOAuthMcpOAuth McpOAuth = "mcp_oauth"`

    - `ExpiresAt string`

      When the OAuth access token expires, as an RFC 3339 timestamp, if known.

    - `Refresh CredentialAuthCreateParamMcpOAuthRefreshResp`

      Optional refresh configuration for an HTTPS OAuth token endpoint.

      - `ClientID string`

        The OAuth client ID used when requesting a new access token.

      - `RefreshToken string`

        The refresh token to store. This secret is never returned in credential resources.

      - `TokenEndpoint string`

        The HTTPS OAuth token endpoint used to exchange the refresh token for a new access token.

      - `TokenEndpointAuth McpOAuthTokenEndpointAuthCreateParamUnionResp`

        How the OAuth client authenticates to the token endpoint.

        - `McpOAuthTokenEndpointAuthCreateParamNoneResp`

          - `Type None`

            The type of the object. Always `none`.

            - `const NoneNone None = "none"`

        - `McpOAuthTokenEndpointAuthCreateParamClientSecretBasicResp`

          - `ClientSecret string`

            The OAuth client secret to store. Never returned in credential resources.

          - `Type ClientSecretBasic`

            The type of the object. Always `client_secret_basic`.

            - `const ClientSecretBasicClientSecretBasic ClientSecretBasic = "client_secret_basic"`

        - `McpOAuthTokenEndpointAuthCreateParamClientSecretPostResp`

          - `ClientSecret string`

            The OAuth client secret to store. Never returned in credential resources.

          - `Type ClientSecretPost`

            The type of the object. Always `client_secret_post`.

            - `const ClientSecretPostClientSecretPost ClientSecretPost = "client_secret_post"`

      - `Resource string`

        The resource URI to send to the OAuth token endpoint during refresh, if required.

      - `Scope string`

        Space-separated OAuth scopes to request during refresh, if required.

  - `CredentialAuthCreateParamStaticBearerResp`

    - `Token string`

      The bearer token to store. This secret is never returned in credential resources.

    - `McpServerURL string`

      The HTTPS MCP server URL authorized by this credential.

    - `Type StaticBearer`

      The type of the object. Always `static_bearer`.

      - `const StaticBearerStaticBearer StaticBearer = "static_bearer"`

  - `CredentialAuthCreateParamEnvironmentVariableResp`

    - `Networking CredentialNetworkingParamUnionResp`

      The destinations where the proxy can substitute this secret. The environment network policy must also allow them.

      - `CredentialNetworkingParamUnrestrictedResp`

        - `Type Unrestricted`

          The type of the object. Always `unrestricted`.

          - `const UnrestrictedUnrestricted Unrestricted = "unrestricted"`

      - `CredentialNetworkingParamLimitedResp`

        - `AllowedHosts []string`

          The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

        - `Type Limited`

          The type of the object. Always `limited`.

          - `const LimitedLimited Limited = "limited"`

    - `SecretName string`

      The environment variable name that receives the placeholder, such as `SERVICE_API_KEY`. Use ASCII letters, digits, and underscores, starting with a letter or underscore. Names starting with `CODEX_` and managed proxy or certificate variable names are reserved.

    - `SecretValue string`

      The write-only secret to store. Never returned in credential resources or supplied directly to sandbox code. Must be nonempty and must not contain carriage returns, newlines, or NUL bytes.

    - `Type EnvironmentVariable`

      The type of the object. Always `environment_variable`.

      - `const EnvironmentVariableEnvironmentVariable EnvironmentVariable = "environment_variable"`

### Credential Auth Rotate Param

- `type CredentialAuthRotateParamUnionResp interface{…}`

  Updates to a vault credential without changing its authentication method or destination configuration.

  - `CredentialAuthRotateParamMcpOAuthResp`

    - `Type McpOAuth`

      The type of the object. Always `mcp_oauth`.

      - `const McpOAuthMcpOAuth McpOAuth = "mcp_oauth"`

    - `AccessToken string`

      A write-only replacement OAuth access token.

    - `ExpiresAt string`

      The replacement expiry as an RFC 3339 timestamp, or `null` to clear it. Omitting this field preserves the expiry unless a new access token is supplied, in which case the expiry is cleared.

    - `Refresh CredentialAuthRotateParamMcpOAuthRefreshResp`

      Optional write-only refresh-token and client-secret updates.

      - `RefreshToken string`

        The replacement refresh token. Omit or pass `null` to keep the stored token. This secret is never returned in resources.

      - `Scope string`

        Replacement space-separated OAuth scopes for refresh requests. Omit to keep the scopes, or pass `null` to stop sending a scope parameter.

      - `TokenEndpointAuth McpOAuthTokenEndpointAuthRotateParamUnionResp`

        Client-secret updates for the existing token endpoint authentication method.

        - `McpOAuthTokenEndpointAuthRotateParamClientSecretBasicResp`

          - `Type ClientSecretBasic`

            The type of the object. Always `client_secret_basic`.

            - `const ClientSecretBasicClientSecretBasic ClientSecretBasic = "client_secret_basic"`

          - `ClientSecret string`

            The replacement OAuth client secret. Omit or pass `null` to keep the stored secret. This secret is never returned in resources.

        - `McpOAuthTokenEndpointAuthRotateParamClientSecretPostResp`

          - `Type ClientSecretPost`

            The type of the object. Always `client_secret_post`.

            - `const ClientSecretPostClientSecretPost ClientSecretPost = "client_secret_post"`

          - `ClientSecret string`

            The replacement OAuth client secret. Omit or pass `null` to keep the stored secret. This secret is never returned in resources.

  - `CredentialAuthRotateParamStaticBearerResp`

    - `Token string`

      The replacement bearer token. This secret is never returned in credential resources.

    - `Type StaticBearer`

      The type of the object. Always `static_bearer`.

      - `const StaticBearerStaticBearer StaticBearer = "static_bearer"`

  - `CredentialAuthRotateParamEnvironmentVariableResp`

    - `SecretValue string`

      The write-only replacement secret. Never returned in credential resources or supplied directly to sandbox code. Must be nonempty and must not contain carriage returns, newlines, or NUL bytes.

    - `Type EnvironmentVariable`

      The type of the object. Always `environment_variable`.

      - `const EnvironmentVariableEnvironmentVariable EnvironmentVariable = "environment_variable"`

### Credential Deleted

- `type CredentialDeleted struct{…}`

  Confirmation that a vault credential was deleted.

  - `ID string`

    The ID of the deleted credential.

  - `Deleted bool`

    Whether the resource was deleted. Always `true`.

  - `Object VaultCredentialDeleted`

    The object type. Always `vault.credential.deleted`.

    - `const VaultCredentialDeletedVaultCredentialDeleted VaultCredentialDeleted = "vault.credential.deleted"`

### Credential Networking

- `type CredentialNetworkingUnion interface{…}`

  Destination permissions for an environment-variable credential. These do not grant network access to the environment.

  - `type CredentialNetworkingUnrestricted struct{…}`

    Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

    - `Type Unrestricted`

      The type of the object. Always `unrestricted`.

      - `const UnrestrictedUnrestricted Unrestricted = "unrestricted"`

  - `type CredentialNetworkingLimited struct{…}`

    Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

    - `AllowedHosts []string`

      The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

    - `Type Limited`

      The type of the object. Always `limited`.

      - `const LimitedLimited Limited = "limited"`

### Credential Networking Param

- `type CredentialNetworkingParamUnionResp interface{…}`

  Destination permissions for an environment-variable credential. These do not grant network access to the environment.

  - `CredentialNetworkingParamUnrestrictedResp`

    - `Type Unrestricted`

      The type of the object. Always `unrestricted`.

      - `const UnrestrictedUnrestricted Unrestricted = "unrestricted"`

  - `CredentialNetworkingParamLimitedResp`

    - `AllowedHosts []string`

      The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

    - `Type Limited`

      The type of the object. Always `limited`.

      - `const LimitedLimited Limited = "limited"`

### Mcp OAuth Token Endpoint Auth

- `type McpOAuthTokenEndpointAuthUnion interface{…}`

  The client authentication method used for OAuth token refresh.

  - `type McpOAuthTokenEndpointAuthNone struct{…}`

    Sends the client ID without a client secret.

    - `Type None`

      The type of the object. Always `none`.

      - `const NoneNone None = "none"`

  - `type McpOAuthTokenEndpointAuthClientSecretBasic struct{…}`

    Sends the client ID and secret using HTTP Basic authentication.

    - `Type ClientSecretBasic`

      The type of the object. Always `client_secret_basic`.

      - `const ClientSecretBasicClientSecretBasic ClientSecretBasic = "client_secret_basic"`

  - `type McpOAuthTokenEndpointAuthClientSecretPost struct{…}`

    Sends the client ID and secret in the token request body.

    - `Type ClientSecretPost`

      The type of the object. Always `client_secret_post`.

      - `const ClientSecretPostClientSecretPost ClientSecretPost = "client_secret_post"`

### Mcp OAuth Token Endpoint Auth Create Param

- `type McpOAuthTokenEndpointAuthCreateParamUnionResp interface{…}`

  Client authentication credentials for OAuth token refresh.

  - `McpOAuthTokenEndpointAuthCreateParamNoneResp`

    - `Type None`

      The type of the object. Always `none`.

      - `const NoneNone None = "none"`

  - `McpOAuthTokenEndpointAuthCreateParamClientSecretBasicResp`

    - `ClientSecret string`

      The OAuth client secret to store. Never returned in credential resources.

    - `Type ClientSecretBasic`

      The type of the object. Always `client_secret_basic`.

      - `const ClientSecretBasicClientSecretBasic ClientSecretBasic = "client_secret_basic"`

  - `McpOAuthTokenEndpointAuthCreateParamClientSecretPostResp`

    - `ClientSecret string`

      The OAuth client secret to store. Never returned in credential resources.

    - `Type ClientSecretPost`

      The type of the object. Always `client_secret_post`.

      - `const ClientSecretPostClientSecretPost ClientSecretPost = "client_secret_post"`

### Mcp OAuth Token Endpoint Auth Rotate Param

- `type McpOAuthTokenEndpointAuthRotateParamUnionResp interface{…}`

  Client-secret updates that preserve the credential's OAuth authentication method.

  - `McpOAuthTokenEndpointAuthRotateParamClientSecretBasicResp`

    - `Type ClientSecretBasic`

      The type of the object. Always `client_secret_basic`.

      - `const ClientSecretBasicClientSecretBasic ClientSecretBasic = "client_secret_basic"`

    - `ClientSecret string`

      The replacement OAuth client secret. Omit or pass `null` to keep the stored secret. This secret is never returned in resources.

  - `McpOAuthTokenEndpointAuthRotateParamClientSecretPostResp`

    - `Type ClientSecretPost`

      The type of the object. Always `client_secret_post`.

      - `const ClientSecretPostClientSecretPost ClientSecretPost = "client_secret_post"`

    - `ClientSecret string`

      The replacement OAuth client secret. Omit or pass `null` to keep the stored secret. This secret is never returned in resources.
