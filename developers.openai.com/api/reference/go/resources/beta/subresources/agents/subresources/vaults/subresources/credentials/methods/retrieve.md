<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/subresources/vaults/subresources/credentials/methods/retrieve/ -->

## Retrieve a vault credential

`client.Beta.Agents.Vaults.Credentials.Get(ctx, vaultID, credentialID) (*Credential, error)`

**get** `/vaults/{vault_id}/credentials/{credential_id}`

Retrieves vault credential metadata without returning secret values. See [vaults](/api/docs/guides/agents-api/tools/vaults).

- `vaultID string`

- `credentialID string`

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
  credential, err := client.Beta.Agents.Vaults.Credentials.Get(
    context.TODO(),
    "vault_id",
    "credential_id",
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", credential.ID)

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
