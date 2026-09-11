<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/agents/subresources/vaults/ -->

# Vaults

##### [Create a vault](/api/reference/resources/beta/subresources/agents/subresources/vaults/methods/create)

POST/vaults

##### [Delete a vault](/api/reference/resources/beta/subresources/agents/subresources/vaults/methods/delete)

DELETE/vaults/{vault\_id}

##### [List vaults](/api/reference/resources/beta/subresources/agents/subresources/vaults/methods/list)

GET/vaults

##### [Retrieve a vault](/api/reference/resources/beta/subresources/agents/subresources/vaults/methods/retrieve)

GET/vaults/{vault\_id}

##### ModelsExpand Collapse

Vault object { id, created\_at, metadata, 2 more }

A collection of credentials that agent tools can use to authenticate to MCP servers.

The ID of the vault.

The Unix timestamp, in seconds, when the vault was created.

metadata: map[string]

Key-value pairs associated with the vault, such as an application or team identifier.

name: string or null

The human-readable name of the vault, if set.

object: "vault"

The object type. Always `vault`.

VaultDeleted object { id, deleted, object }

Confirmation that a vault was deleted.

The ID of the deleted vault.

deleted: boolean

Whether the resource was deleted. Always `true`.

object: "vault.deleted"

The object type. Always `vault.deleted`.

VaultStatus = "active" or "archived"

Whether a vault or credential is active or archived.

"active"

"archived"

VaultStatusFilter = [VaultStatus](/api/reference/resources/beta#(resource)%20beta.agents.vaults%20%3E%20(model)%20vault_status%20%3E%20(schema)) or array of [VaultStatus](/api/reference/resources/beta#(resource)%20beta.agents.vaults%20%3E%20(model)%20vault_status%20%3E%20(schema))

One or more lifecycle statuses to include when listing vaults or credentials.

VaultStatus = "active" or "archived"

Whether a vault or credential is active or archived.

"active"

"archived"

array of [VaultStatus](/api/reference/resources/beta#(resource)%20beta.agents.vaults%20%3E%20(model)%20vault_status%20%3E%20(schema))

"active"

"archived"

#### VaultsCredentials

##### [Create a vault credential](/api/reference/resources/beta/subresources/agents/subresources/vaults/subresources/credentials/methods/create)

POST/vaults/{vault\_id}/credentials

##### [Delete a vault credential](/api/reference/resources/beta/subresources/agents/subresources/vaults/subresources/credentials/methods/delete)

DELETE/vaults/{vault\_id}/credentials/{credential\_id}

##### [List vault credentials](/api/reference/resources/beta/subresources/agents/subresources/vaults/subresources/credentials/methods/list)

GET/vaults/{vault\_id}/credentials

##### [Retrieve a vault credential](/api/reference/resources/beta/subresources/agents/subresources/vaults/subresources/credentials/methods/retrieve)

GET/vaults/{vault\_id}/credentials/{credential\_id}

##### [Rotate a vault credential](/api/reference/resources/beta/subresources/agents/subresources/vaults/subresources/credentials/methods/update)

POST/vaults/{vault\_id}/credentials/{credential\_id}

##### ModelsExpand Collapse

Credential object { id, auth, created\_at, 4 more }

Metadata for a stored MCP server credential. Secret values are never returned.

The ID of the credential.

auth: [CredentialAuth](/api/reference/resources/beta#(resource)%20beta.agents.vaults.credentials%20%3E%20(model)%20credential_auth%20%3E%20(schema))

The authentication method and non-secret configuration for the MCP server.

The Unix timestamp, in seconds, when the credential was created.

The human-readable name of the credential.

object: "vault.credential"

The object type. Always `vault.credential`.

updated\_at: number

The Unix timestamp, in seconds, when the credential was last updated.

vault\_id: string

The ID of the vault containing this credential.

CredentialAuth = object { expires\_at, mcp\_server\_url, refresh, type }  or object { mcp\_server\_url, type }

The MCP server and authentication configuration of a vault credential, excluding secrets.

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

type: "mcp\_oauth"

The type of the object. Always `mcp_oauth`.

StaticBearer object { mcp\_server\_url, type }

Metadata for a bearer-token credential, without automatic OAuth refresh.

mcp\_server\_url: string

The HTTPS MCP server URL authorized by this credential.

type: "static\_bearer"

The type of the object. Always `static_bearer`.

CredentialAuthCreateParam = object { access\_token, mcp\_server\_url, type, 2 more }  or object { token, mcp\_server\_url, type }

Authentication credentials for an MCP server used by agent tools.

McpOauth object { access\_token, mcp\_server\_url, type, 2 more }

An OAuth credential for an HTTPS MCP destination.

access\_token: string

A write-only OAuth access token; never returned by credential resources.

mcp\_server\_url: string

The HTTPS MCP server URL authorized by this credential.

type: "mcp\_oauth"

The type of the object. Always `mcp_oauth`.

expires\_at: optional string or null

When the OAuth access token expires, as an RFC 3339 timestamp, if known.

refresh: optional object { client\_id, refresh\_token, token\_endpoint, 3 more }  or null

Configuration for refreshing the access token of an MCP OAuth credential.

client\_id: string

The OAuth client ID used when requesting a new access token.

refresh\_token: string

The refresh token to store. This secret is never returned in credential resources.

token\_endpoint: string

The HTTPS OAuth token endpoint used to exchange the refresh token for a new access token.

token\_endpoint\_auth: [McpOauthTokenEndpointAuthCreateParam](/api/reference/resources/beta#(resource)%20beta.agents.vaults.credentials%20%3E%20(model)%20mcp_oauth_token_endpoint_auth_create_param%20%3E%20(schema))

How the OAuth client authenticates to the token endpoint.

resource: optional string or null

The resource URI to send to the OAuth token endpoint during refresh, if required.

scope: optional string or null

Space-separated OAuth scopes to request during refresh, if required.

StaticBearer object { token, mcp\_server\_url, type }

A bearer token for an MCP server, without automatic OAuth refresh.

token: string

The bearer token to store. This secret is never returned in credential resources.

mcp\_server\_url: string

The HTTPS MCP server URL authorized by this credential.

type: "static\_bearer"

The type of the object. Always `static_bearer`.

CredentialAuthRotateParam = object { type, access\_token, expires\_at, refresh }  or object { token, type }

Updates to a vault credential without changing its authentication method or MCP server.

McpOauth object { type, access\_token, expires\_at, refresh }

Rotate an OAuth credential for an HTTPS MCP destination.

type: "mcp\_oauth"

The type of the object. Always `mcp_oauth`.

access\_token: optional string or null

A write-only replacement OAuth access token.

expires\_at: optional string or null

The replacement expiry as an RFC 3339 timestamp, or `null` to clear it. Omitting this field preserves the expiry unless a new access token is supplied, in which case the expiry is cleared.

refresh: optional object { refresh\_token, scope, token\_endpoint\_auth }  or null

Updates to an MCP credential’s existing OAuth refresh configuration.

refresh\_token: optional string or null

The replacement refresh token. Omit or pass `null` to keep the stored token. This secret is never returned in resources.

scope: optional string or null

Replacement space-separated OAuth scopes for refresh requests. Omit to keep the scopes, or pass `null` to stop sending a scope parameter.

token\_endpoint\_auth: optional [McpOauthTokenEndpointAuthRotateParam](/api/reference/resources/beta#(resource)%20beta.agents.vaults.credentials%20%3E%20(model)%20mcp_oauth_token_endpoint_auth_rotate_param%20%3E%20(schema)) or null

Client-secret updates that preserve the credential’s OAuth authentication method.

StaticBearer object { token, type }

Replace the bearer token for the credential’s MCP server.

token: string

The replacement bearer token. This secret is never returned in credential resources.

type: "static\_bearer"

The type of the object. Always `static_bearer`.

CredentialDeleted object { id, deleted, object }

Confirmation that a vault credential was deleted.

The ID of the deleted credential.

deleted: boolean

Whether the resource was deleted. Always `true`.

object: "vault.credential.deleted"

The object type. Always `vault.credential.deleted`.

McpOauthTokenEndpointAuth = object { type }  or object { type }  or object { type }

The client authentication method used for OAuth token refresh.

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

McpOauthTokenEndpointAuthCreateParam = object { type }  or object { client\_secret, type }  or object { client\_secret, type }

Client authentication credentials for OAuth token refresh.

None object { type }

Sends the client ID without a client secret.

type: "none"

The type of the object. Always `none`.

ClientSecretBasic object { client\_secret, type }

Sends the client ID and secret using HTTP Basic authentication.

client\_secret: string

The OAuth client secret to store. Never returned in credential resources.

type: "client\_secret\_basic"

The type of the object. Always `client_secret_basic`.

ClientSecretPost object { client\_secret, type }

Sends the client ID and secret in the token request body.

client\_secret: string

The OAuth client secret to store. Never returned in credential resources.

type: "client\_secret\_post"

The type of the object. Always `client_secret_post`.

McpOauthTokenEndpointAuthRotateParam = object { type, client\_secret }  or object { type, client\_secret }

Client-secret updates that preserve the credential’s OAuth authentication method.

ClientSecretBasic object { type, client\_secret }

Updates credentials sent using HTTP Basic authentication.

type: "client\_secret\_basic"

The type of the object. Always `client_secret_basic`.

client\_secret: optional string or null

The replacement OAuth client secret. Omit or pass `null` to keep the stored secret. This secret is never returned in resources.

ClientSecretPost object { type, client\_secret }

Updates credentials sent in the token request body.

type: "client\_secret\_post"

The type of the object. Always `client_secret_post`.

client\_secret: optional string or null

The replacement OAuth client secret. Omit or pass `null` to keep the stored secret. This secret is never returned in resources.
