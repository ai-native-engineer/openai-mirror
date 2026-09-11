<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/agents/subresources/vaults/subresources/credentials/methods/list/ -->

[Vaults](/api/reference/resources/beta/subresources/agents/subresources/vaults)

[Credentials](/api/reference/resources/beta/subresources/agents/subresources/vaults/subresources/credentials)

# List vault credentials

GET/vaults/{vault\_id}/credentials

Lists a vault’s credentials using ID-based pagination without returning secret values. See [vaults](/api/docs/guides/agents-api/tools/vaults).

vault\_id: string

##### Query ParametersExpand Collapse

after: optional string

Return resources after this resource ID in the selected order.

limit: optional number or null

The maximum number of resources to return. Defaults to 20. Values are clamped between 1 and 100.

minimum0

order: optional "asc" or "desc"

Sort order by the `created_at` timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `desc`.

"asc"

Returns resources in ascending order.

"desc"

Returns resources in descending order.

status: optional [VaultStatusFilter](/api/reference/resources/beta#(resource)%20beta.agents.vaults%20%3E%20(model)%20vault_status_filter%20%3E%20(schema))

Filter by one status or a list, such as `status=active` or `status[]=active&status[]=archived`. Both statuses are included by default.

VaultStatus = "active" or "archived"

Whether a vault or credential is active or archived.

"active"

"archived"

array of [VaultStatus](/api/reference/resources/beta#(resource)%20beta.agents.vaults%20%3E%20(model)%20vault_status%20%3E%20(schema))

"active"

"archived"

data: array of [Credential](/api/reference/resources/beta#(resource)%20beta.agents.vaults.credentials%20%3E%20(model)%20credential%20%3E%20(schema)) { id, auth, created\_at, 4 more }

The resources returned in this page, in the requested sort order.

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

first\_id: string or null

The ID of the first resource in `data`, or `null` if the page is empty.

has\_more: boolean

Whether there are more resources to retrieve after this page.

last\_id: string or null

The ID of the last resource in `data`, or `null` if the page is empty. Pass this as `after` with the same order and filters.

object: "list"

The object type, which is always `list`.

### List vault credentials

curl https://api.openai.com/v1/vaults/$VAULT_ID/credentials \

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
        },
        "type": "mcp_oauth"
      },
      "created_at": 0,
      "name": "name",
      "object": "vault.credential",
      "updated_at": 0,
      "vault_id": "vault_id"
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"

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
        },
        "type": "mcp_oauth"
      },
      "created_at": 0,
      "name": "name",
      "object": "vault.credential",
      "updated_at": 0,
      "vault_id": "vault_id"
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
