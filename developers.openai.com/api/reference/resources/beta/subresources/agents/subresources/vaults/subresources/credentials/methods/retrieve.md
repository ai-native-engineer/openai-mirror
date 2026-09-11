<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/agents/subresources/vaults/subresources/credentials/methods/retrieve/ -->

[Vaults](/api/reference/resources/beta/subresources/agents/subresources/vaults)

[Credentials](/api/reference/resources/beta/subresources/agents/subresources/vaults/subresources/credentials)

# Retrieve a vault credential

GET/vaults/{vault\_id}/credentials/{credential\_id}

Retrieves vault credential metadata without returning secret values. See [vaults](/api/docs/guides/agents-api/tools/vaults).

vault\_id: string

credential\_id: string

Credential object { id, auth, created\_at, 4 more }

Metadata for a stored MCP server credential. Secret values are never returned.

The ID of the credential.

auth: [CredentialAuth](/api/reference/resources/beta#(resource)%20beta.agents.vaults.credentials%20%3E%20(model)%20credential_auth%20%3E%20(schema))

The authentication method and non-secret configuration for the MCP server.

McpOauth object { expires\_at, mcp\_server\_url, refresh, type }

Public metadata for an OAuth credential; tokens and client secrets are never returned.

expires\_at: string or null

When the OAuth access token expires, as an RFC 3339 timestamp, if known.

mcp\_server\_url: string

The HTTPS MCP server URL authorized by this credential.

refresh: object { client\_id, resource, scope, 2 more }  or null

Configuration used to refresh an MCP OAuth access token, excluding secret values.

client\_id: string

The OAuth client ID used when requesting a new access token.

resource: string or null

The resource URI sent to the OAuth token endpoint during refresh, if configured.

scope: string or null

Space-separated OAuth scopes requested during refresh, if configured.

token\_endpoint: string

The HTTPS OAuth token endpoint used for refresh.

token\_endpoint\_auth: [McpOauthTokenEndpointAuth](/api/reference/resources/beta#(resource)%20beta.agents.vaults.credentials%20%3E%20(model)%20mcp_oauth_token_endpoint_auth%20%3E%20(schema))

How the OAuth client authenticates to the token endpoint, excluding its client secret.

None object { type }

Sends the client ID without a client secret.

type: "none"

The type of the object. Always `none`.

ClientSecretBasic object { type }

Sends the client ID and secret using HTTP Basic authentication.

type: "client\_secret\_basic"

The type of the object. Always `client_secret_basic`.

ClientSecretPost object { type }

Sends the client ID and secret in the token request body.

type: "client\_secret\_post"

The type of the object. Always `client_secret_post`.

type: "mcp\_oauth"

The type of the object. Always `mcp_oauth`.

StaticBearer object { mcp\_server\_url, type }

Metadata for a bearer-token credential, without automatic OAuth refresh.

mcp\_server\_url: string

The HTTPS MCP server URL authorized by this credential.

type: "static\_bearer"

The type of the object. Always `static_bearer`.

The Unix timestamp, in seconds, when the credential was created.

The human-readable name of the credential.

object: "vault.credential"

The object type. Always `vault.credential`.

updated\_at: number

The Unix timestamp, in seconds, when the credential was last updated.

vault\_id: string

The ID of the vault containing this credential.

### Retrieve a vault credential

curl https://api.openai.com/v1/vaults/$VAULT_ID/credentials/$CREDENTIAL_ID \

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
    },
    "type": "mcp_oauth"
  },
  "created_at": 0,
  "name": "name",
  "object": "vault.credential",
  "updated_at": 0,
  "vault_id": "vault_id"

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
    },
    "type": "mcp_oauth"
  },
  "created_at": 0,
  "name": "name",
  "object": "vault.credential",
  "updated_at": 0,
  "vault_id": "vault_id"
