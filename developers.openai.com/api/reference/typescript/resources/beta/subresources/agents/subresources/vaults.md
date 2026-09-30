<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/agents/subresources/vaults/ -->

# Vaults

## Create a vault

`client.beta.agents.vaults.create(VaultCreateParamsbody?, RequestOptionsoptions?): Vault`

**post** `/vaults`

Creates a vault for the current project. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `body: VaultCreateParams`

  - `metadata?: Record<string, string> | null`

    Key-value pairs to associate with the vault, such as an application or team identifier.

  - `name?: string`

    The name is trimmed before storage. It must contain 1 to 256 UTF-8 bytes after trimming.

### Returns

- `Vault`

  A collection of credentials for MCP servers and OpenAI-hosted environments.

  - `id: string`

    The ID of the vault.

  - `created_at: number`

    The Unix timestamp, in seconds, when the vault was created.

  - `metadata: Record<string, string>`

    Key-value pairs associated with the vault, such as an application or team identifier.

  - `name: string | null`

    The human-readable name of the vault, if set.

  - `object: "vault"`

    The object type. Always `vault`.

    - `"vault"`

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const vault = await client.beta.agents.vaults.create();

console.log(vault.id);
```

#### Response

```json
{
  "id": "id",
  "created_at": 0,
  "metadata": {
    "foo": "string"
  },
  "name": "name",
  "object": "vault"
}
```

## Delete a vault

`client.beta.agents.vaults.delete(stringvaultID, RequestOptionsoptions?): VaultDeleted`

**delete** `/vaults/{vault_id}`

Deletes a vault and all its credentials. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vaultID: string`

### Returns

- `VaultDeleted`

  Confirmation that a vault was deleted.

  - `id: string`

    The ID of the deleted vault.

  - `deleted: boolean`

    Whether the resource was deleted. Always `true`.

  - `object: "vault.deleted"`

    The object type. Always `vault.deleted`.

    - `"vault.deleted"`

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const vaultDeleted = await client.beta.agents.vaults.delete('vault_id');

console.log(vaultDeleted.id);
```

#### Response

```json
{
  "id": "id",
  "deleted": true,
  "object": "vault.deleted"
}
```

## List vaults

`client.beta.agents.vaults.list(VaultListParamsquery?, RequestOptionsoptions?): CursorPage<Vault>`

**get** `/vaults`

Lists vaults using ID-based pagination. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `query: VaultListParams`

  - `after?: string`

    Return resources after this resource ID in the selected order.

  - `limit?: number | null`

    The maximum number of resources to return. Defaults to 20. Values are clamped between 1 and 100.

  - `order?: "asc" | "desc"`

    Sort order by the `created_at` timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `desc`.

    - `"asc"`

      Returns resources in ascending order.

    - `"desc"`

      Returns resources in descending order.

  - `status?: VaultStatusFilter`

    Filter by one status or a list, such as `status=active` or `status[]=active&status[]=archived`. Both statuses are included by default.

    - `VaultStatus = "active" | "archived"`

      Whether a vault or credential is active or archived.

      - `"active"`

      - `"archived"`

    - `Array<VaultStatus>`

      - `"active"`

      - `"archived"`

### Returns

- `Vault`

  A collection of credentials for MCP servers and OpenAI-hosted environments.

  - `id: string`

    The ID of the vault.

  - `created_at: number`

    The Unix timestamp, in seconds, when the vault was created.

  - `metadata: Record<string, string>`

    Key-value pairs associated with the vault, such as an application or team identifier.

  - `name: string | null`

    The human-readable name of the vault, if set.

  - `object: "vault"`

    The object type. Always `vault`.

    - `"vault"`

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const vault of client.beta.agents.vaults.list()) {
  console.log(vault.id);
}
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "created_at": 0,
      "metadata": {
        "foo": "string"
      },
      "name": "name",
      "object": "vault"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve a vault

`client.beta.agents.vaults.retrieve(stringvaultID, RequestOptionsoptions?): Vault`

**get** `/vaults/{vault_id}`

Retrieves a vault by its ID. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vaultID: string`

### Returns

- `Vault`

  A collection of credentials for MCP servers and OpenAI-hosted environments.

  - `id: string`

    The ID of the vault.

  - `created_at: number`

    The Unix timestamp, in seconds, when the vault was created.

  - `metadata: Record<string, string>`

    Key-value pairs associated with the vault, such as an application or team identifier.

  - `name: string | null`

    The human-readable name of the vault, if set.

  - `object: "vault"`

    The object type. Always `vault`.

    - `"vault"`

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const vault = await client.beta.agents.vaults.retrieve('vault_id');

console.log(vault.id);
```

#### Response

```json
{
  "id": "id",
  "created_at": 0,
  "metadata": {
    "foo": "string"
  },
  "name": "name",
  "object": "vault"
}
```

## Domain Types

### Vault

- `Vault`

  A collection of credentials for MCP servers and OpenAI-hosted environments.

  - `id: string`

    The ID of the vault.

  - `created_at: number`

    The Unix timestamp, in seconds, when the vault was created.

  - `metadata: Record<string, string>`

    Key-value pairs associated with the vault, such as an application or team identifier.

  - `name: string | null`

    The human-readable name of the vault, if set.

  - `object: "vault"`

    The object type. Always `vault`.

    - `"vault"`

### Vault Deleted

- `VaultDeleted`

  Confirmation that a vault was deleted.

  - `id: string`

    The ID of the deleted vault.

  - `deleted: boolean`

    Whether the resource was deleted. Always `true`.

  - `object: "vault.deleted"`

    The object type. Always `vault.deleted`.

    - `"vault.deleted"`

### Vault Status

- `VaultStatus = "active" | "archived"`

  Whether a vault or credential is active or archived.

  - `"active"`

  - `"archived"`

### Vault Status Filter

- `VaultStatusFilter = VaultStatus | Array<VaultStatus>`

  One or more lifecycle statuses to include when listing vaults or credentials.

  - `VaultStatus = "active" | "archived"`

    Whether a vault or credential is active or archived.

    - `"active"`

    - `"archived"`

  - `Array<VaultStatus>`

    - `"active"`

    - `"archived"`

# Credentials

## Create a vault credential

`client.beta.agents.vaults.credentials.create(stringvaultID, CredentialCreateParamsbody, RequestOptionsoptions?): Credential`

**post** `/vaults/{vault_id}/credentials`

Creates a vault credential. Secret values are write-only and are never returned. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vaultID: string`

- `body: CredentialCreateParams`

  - `auth: CredentialAuthCreateParam`

    The authentication method and write-only secret values to store.

    - `CreateVaultCredentialAuthParamMcpOauth`

      An OAuth credential for an HTTPS MCP destination.

      - `access_token: string`

        A write-only OAuth access token; never returned by credential resources.

      - `mcp_server_url: string`

        The HTTPS MCP server URL authorized by this credential.

      - `type: "mcp_oauth"`

        The type of the object. Always `mcp_oauth`.

        - `"mcp_oauth"`

      - `expires_at?: string | null`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `refresh?: Refresh | null`

        Optional refresh configuration for an HTTPS OAuth token endpoint.

        - `client_id: string`

          The OAuth client ID used when requesting a new access token.

        - `refresh_token: string`

          The refresh token to store. This secret is never returned in credential resources.

        - `token_endpoint: string`

          The HTTPS OAuth token endpoint used to exchange the refresh token for a new access token.

        - `token_endpoint_auth: McpOauthTokenEndpointAuthCreateParam`

          How the OAuth client authenticates to the token endpoint.

          - `CreateMcpOauthTokenEndpointAuthParamNone`

            Sends the client ID without a client secret.

            - `type: "none"`

              The type of the object. Always `none`.

              - `"none"`

          - `CreateMcpOauthTokenEndpointAuthParamClientSecretBasic`

            Sends the client ID and secret using HTTP Basic authentication.

            - `client_secret: string`

              The OAuth client secret to store. Never returned in credential resources.

            - `type: "client_secret_basic"`

              The type of the object. Always `client_secret_basic`.

              - `"client_secret_basic"`

          - `CreateMcpOauthTokenEndpointAuthParamClientSecretPost`

            Sends the client ID and secret in the token request body.

            - `client_secret: string`

              The OAuth client secret to store. Never returned in credential resources.

            - `type: "client_secret_post"`

              The type of the object. Always `client_secret_post`.

              - `"client_secret_post"`

        - `resource?: string | null`

          The resource URI to send to the OAuth token endpoint during refresh, if required.

        - `scope?: string | null`

          Space-separated OAuth scopes to request during refresh, if required.

    - `CreateVaultCredentialAuthParamStaticBearer`

      A bearer token for an MCP server, without automatic OAuth refresh.

      - `token: string`

        The bearer token to store. This secret is never returned in credential resources.

      - `mcp_server_url: string`

        The HTTPS MCP server URL authorized by this credential.

      - `type: "static_bearer"`

        The type of the object. Always `static_bearer`.

        - `"static_bearer"`

    - `CreateVaultCredentialAuthParamEnvironmentVariable`

      An HTTP credential for OpenAI-hosted environments only. The sandbox receives an environment variable containing a placeholder, not the secret. Use the placeholder unchanged in outgoing requests. The egress proxy replaces the placeholder with the secret for allowed HTTPS destinations on ports 443 and 8443. Sandbox code cannot read the real secret or use it for local computation, such as signing a request.

      - `networking: CredentialNetworkingParam`

        The destinations where the proxy can substitute this secret. The environment network policy must also allow them.

        - `VaultCredentialNetworkingParamUnrestricted`

          Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

          - `type: "unrestricted"`

            The type of the object. Always `unrestricted`.

            - `"unrestricted"`

        - `VaultCredentialNetworkingParamLimited`

          Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

          - `allowed_hosts: Array<string>`

            The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

          - `type: "limited"`

            The type of the object. Always `limited`.

            - `"limited"`

      - `secret_name: string`

        The environment variable name that receives the placeholder, such as `SERVICE_API_KEY`. Use ASCII letters, digits, and underscores, starting with a letter or underscore. Names starting with `CODEX_` and managed proxy or certificate variable names are reserved.

      - `secret_value: string`

        The write-only secret to store. Never returned in credential resources or supplied directly to sandbox code. Must be nonempty and must not contain carriage returns, newlines, or NUL bytes.

      - `type: "environment_variable"`

        The type of the object. Always `environment_variable`.

        - `"environment_variable"`

  - `name: string`

    The name is trimmed before storage. It must contain 1 to 256 UTF-8 bytes after trimming.

  - `metadata?: Record<string, string>`

    Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters. Defaults to an empty map.

### Returns

- `Credential`

  Metadata for a stored credential. Secret values are never returned.

  - `id: string`

    The ID of the credential.

  - `auth: CredentialAuth`

    The authentication method and non-secret configuration of the credential.

    - `VaultCredentialAuthResourceMcpOauth`

      Public metadata for an OAuth credential; tokens and client secrets are never returned.

      - `expires_at: string | null`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `mcp_server_url: string`

        The HTTPS MCP server URL authorized by this credential.

      - `refresh: Refresh | null`

        Public refresh metadata without refresh tokens or OAuth client secrets.

        - `client_id: string`

          The OAuth client ID used when requesting a new access token.

        - `resource: string | null`

          The resource URI sent to the OAuth token endpoint during refresh, if configured.

        - `scope: string | null`

          Space-separated OAuth scopes requested during refresh, if configured.

        - `token_endpoint: string`

          The HTTPS OAuth token endpoint used for refresh.

        - `token_endpoint_auth: McpOauthTokenEndpointAuth`

          How the OAuth client authenticates to the token endpoint, excluding its client secret.

          - `McpOauthTokenEndpointAuthResourceNone`

            Sends the client ID without a client secret.

            - `type: "none"`

              The type of the object. Always `none`.

              - `"none"`

          - `McpOauthTokenEndpointAuthResourceClientSecretBasic`

            Sends the client ID and secret using HTTP Basic authentication.

            - `type: "client_secret_basic"`

              The type of the object. Always `client_secret_basic`.

              - `"client_secret_basic"`

          - `McpOauthTokenEndpointAuthResourceClientSecretPost`

            Sends the client ID and secret in the token request body.

            - `type: "client_secret_post"`

              The type of the object. Always `client_secret_post`.

              - `"client_secret_post"`

      - `type: "mcp_oauth"`

        The type of the object. Always `mcp_oauth`.

        - `"mcp_oauth"`

    - `VaultCredentialAuthResourceStaticBearer`

      Metadata for a bearer-token credential, without automatic OAuth refresh.

      - `mcp_server_url: string`

        The HTTPS MCP server URL authorized by this credential.

      - `type: "static_bearer"`

        The type of the object. Always `static_bearer`.

        - `"static_bearer"`

    - `VaultCredentialAuthResourceEnvironmentVariable`

      Metadata for an HTTP credential used only in OpenAI-hosted environments. Sandbox code receives a placeholder. The proxy substitutes the secret for allowed HTTPS destinations on ports 443 and 8443. The real secret is not available to sandbox code for local computation and is never returned in this resource.

      - `networking: CredentialNetworking`

        The destinations where the proxy can substitute the secret, subject to the environment network policy.

        - `VaultCredentialNetworkingResourceUnrestricted`

          Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

          - `type: "unrestricted"`

            The type of the object. Always `unrestricted`.

            - `"unrestricted"`

        - `VaultCredentialNetworkingResourceLimited`

          Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

          - `allowed_hosts: Array<string>`

            The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

          - `type: "limited"`

            The type of the object. Always `limited`.

            - `"limited"`

      - `secret_name: string`

        The environment variable name that receives the placeholder in the sandbox.

      - `type: "environment_variable"`

        The type of the object. Always `environment_variable`.

        - `"environment_variable"`

  - `created_at: number`

    The Unix timestamp, in seconds, when the credential was created.

  - `metadata: Record<string, string>`

    Application-defined key-value pairs associated with this credential.

  - `name: string`

    The human-readable name of the credential.

  - `object: "vault.credential"`

    The object type. Always `vault.credential`.

    - `"vault.credential"`

  - `updated_at: number`

    The Unix timestamp, in seconds, when the credential was last updated.

  - `vault_id: string`

    The ID of the vault containing this credential.

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const credential = await client.beta.agents.vaults.credentials.create('vault_id', {
  auth: {
    access_token: 'access_token',
    mcp_server_url: 'mcp_server_url',
    type: 'mcp_oauth',
  },
  name: 'x',
});

console.log(credential.id);
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

`client.beta.agents.vaults.credentials.delete(stringcredentialID, CredentialDeleteParamsparams, RequestOptionsoptions?): CredentialDeleted`

**delete** `/vaults/{vault_id}/credentials/{credential_id}`

Deletes a vault credential. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `credentialID: string`

- `params: CredentialDeleteParams`

  - `vault_id: string`

    The ID of the vault.

### Returns

- `CredentialDeleted`

  Confirmation that a vault credential was deleted.

  - `id: string`

    The ID of the deleted credential.

  - `deleted: boolean`

    Whether the resource was deleted. Always `true`.

  - `object: "vault.credential.deleted"`

    The object type. Always `vault.credential.deleted`.

    - `"vault.credential.deleted"`

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const credentialDeleted = await client.beta.agents.vaults.credentials.delete('credential_id', {
  vault_id: 'vault_id',
});

console.log(credentialDeleted.id);
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

`client.beta.agents.vaults.credentials.list(stringvaultID, CredentialListParamsquery?, RequestOptionsoptions?): CursorPage<Credential>`

**get** `/vaults/{vault_id}/credentials`

Lists a vault's credentials using ID-based pagination without returning secret values. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vaultID: string`

- `query: CredentialListParams`

  - `after?: string`

    Return resources after this resource ID in the selected order.

  - `limit?: number | null`

    The maximum number of resources to return. Defaults to 20. Values are clamped between 1 and 100.

  - `order?: "asc" | "desc"`

    Sort order by the `created_at` timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `desc`.

    - `"asc"`

      Returns resources in ascending order.

    - `"desc"`

      Returns resources in descending order.

  - `status?: VaultStatusFilter`

    Filter by one status or a list, such as `status=active` or `status[]=active&status[]=archived`. Both statuses are included by default.

    - `VaultStatus = "active" | "archived"`

      Whether a vault or credential is active or archived.

      - `"active"`

      - `"archived"`

    - `Array<VaultStatus>`

      - `"active"`

      - `"archived"`

### Returns

- `Credential`

  Metadata for a stored credential. Secret values are never returned.

  - `id: string`

    The ID of the credential.

  - `auth: CredentialAuth`

    The authentication method and non-secret configuration of the credential.

    - `VaultCredentialAuthResourceMcpOauth`

      Public metadata for an OAuth credential; tokens and client secrets are never returned.

      - `expires_at: string | null`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `mcp_server_url: string`

        The HTTPS MCP server URL authorized by this credential.

      - `refresh: Refresh | null`

        Public refresh metadata without refresh tokens or OAuth client secrets.

        - `client_id: string`

          The OAuth client ID used when requesting a new access token.

        - `resource: string | null`

          The resource URI sent to the OAuth token endpoint during refresh, if configured.

        - `scope: string | null`

          Space-separated OAuth scopes requested during refresh, if configured.

        - `token_endpoint: string`

          The HTTPS OAuth token endpoint used for refresh.

        - `token_endpoint_auth: McpOauthTokenEndpointAuth`

          How the OAuth client authenticates to the token endpoint, excluding its client secret.

          - `McpOauthTokenEndpointAuthResourceNone`

            Sends the client ID without a client secret.

            - `type: "none"`

              The type of the object. Always `none`.

              - `"none"`

          - `McpOauthTokenEndpointAuthResourceClientSecretBasic`

            Sends the client ID and secret using HTTP Basic authentication.

            - `type: "client_secret_basic"`

              The type of the object. Always `client_secret_basic`.

              - `"client_secret_basic"`

          - `McpOauthTokenEndpointAuthResourceClientSecretPost`

            Sends the client ID and secret in the token request body.

            - `type: "client_secret_post"`

              The type of the object. Always `client_secret_post`.

              - `"client_secret_post"`

      - `type: "mcp_oauth"`

        The type of the object. Always `mcp_oauth`.

        - `"mcp_oauth"`

    - `VaultCredentialAuthResourceStaticBearer`

      Metadata for a bearer-token credential, without automatic OAuth refresh.

      - `mcp_server_url: string`

        The HTTPS MCP server URL authorized by this credential.

      - `type: "static_bearer"`

        The type of the object. Always `static_bearer`.

        - `"static_bearer"`

    - `VaultCredentialAuthResourceEnvironmentVariable`

      Metadata for an HTTP credential used only in OpenAI-hosted environments. Sandbox code receives a placeholder. The proxy substitutes the secret for allowed HTTPS destinations on ports 443 and 8443. The real secret is not available to sandbox code for local computation and is never returned in this resource.

      - `networking: CredentialNetworking`

        The destinations where the proxy can substitute the secret, subject to the environment network policy.

        - `VaultCredentialNetworkingResourceUnrestricted`

          Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

          - `type: "unrestricted"`

            The type of the object. Always `unrestricted`.

            - `"unrestricted"`

        - `VaultCredentialNetworkingResourceLimited`

          Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

          - `allowed_hosts: Array<string>`

            The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

          - `type: "limited"`

            The type of the object. Always `limited`.

            - `"limited"`

      - `secret_name: string`

        The environment variable name that receives the placeholder in the sandbox.

      - `type: "environment_variable"`

        The type of the object. Always `environment_variable`.

        - `"environment_variable"`

  - `created_at: number`

    The Unix timestamp, in seconds, when the credential was created.

  - `metadata: Record<string, string>`

    Application-defined key-value pairs associated with this credential.

  - `name: string`

    The human-readable name of the credential.

  - `object: "vault.credential"`

    The object type. Always `vault.credential`.

    - `"vault.credential"`

  - `updated_at: number`

    The Unix timestamp, in seconds, when the credential was last updated.

  - `vault_id: string`

    The ID of the vault containing this credential.

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const credential of client.beta.agents.vaults.credentials.list('vault_id')) {
  console.log(credential.id);
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

`client.beta.agents.vaults.credentials.retrieve(stringcredentialID, CredentialRetrieveParamsparams, RequestOptionsoptions?): Credential`

**get** `/vaults/{vault_id}/credentials/{credential_id}`

Retrieves vault credential metadata without returning secret values. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `credentialID: string`

- `params: CredentialRetrieveParams`

  - `vault_id: string`

    The ID of the vault.

### Returns

- `Credential`

  Metadata for a stored credential. Secret values are never returned.

  - `id: string`

    The ID of the credential.

  - `auth: CredentialAuth`

    The authentication method and non-secret configuration of the credential.

    - `VaultCredentialAuthResourceMcpOauth`

      Public metadata for an OAuth credential; tokens and client secrets are never returned.

      - `expires_at: string | null`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `mcp_server_url: string`

        The HTTPS MCP server URL authorized by this credential.

      - `refresh: Refresh | null`

        Public refresh metadata without refresh tokens or OAuth client secrets.

        - `client_id: string`

          The OAuth client ID used when requesting a new access token.

        - `resource: string | null`

          The resource URI sent to the OAuth token endpoint during refresh, if configured.

        - `scope: string | null`

          Space-separated OAuth scopes requested during refresh, if configured.

        - `token_endpoint: string`

          The HTTPS OAuth token endpoint used for refresh.

        - `token_endpoint_auth: McpOauthTokenEndpointAuth`

          How the OAuth client authenticates to the token endpoint, excluding its client secret.

          - `McpOauthTokenEndpointAuthResourceNone`

            Sends the client ID without a client secret.

            - `type: "none"`

              The type of the object. Always `none`.

              - `"none"`

          - `McpOauthTokenEndpointAuthResourceClientSecretBasic`

            Sends the client ID and secret using HTTP Basic authentication.

            - `type: "client_secret_basic"`

              The type of the object. Always `client_secret_basic`.

              - `"client_secret_basic"`

          - `McpOauthTokenEndpointAuthResourceClientSecretPost`

            Sends the client ID and secret in the token request body.

            - `type: "client_secret_post"`

              The type of the object. Always `client_secret_post`.

              - `"client_secret_post"`

      - `type: "mcp_oauth"`

        The type of the object. Always `mcp_oauth`.

        - `"mcp_oauth"`

    - `VaultCredentialAuthResourceStaticBearer`

      Metadata for a bearer-token credential, without automatic OAuth refresh.

      - `mcp_server_url: string`

        The HTTPS MCP server URL authorized by this credential.

      - `type: "static_bearer"`

        The type of the object. Always `static_bearer`.

        - `"static_bearer"`

    - `VaultCredentialAuthResourceEnvironmentVariable`

      Metadata for an HTTP credential used only in OpenAI-hosted environments. Sandbox code receives a placeholder. The proxy substitutes the secret for allowed HTTPS destinations on ports 443 and 8443. The real secret is not available to sandbox code for local computation and is never returned in this resource.

      - `networking: CredentialNetworking`

        The destinations where the proxy can substitute the secret, subject to the environment network policy.

        - `VaultCredentialNetworkingResourceUnrestricted`

          Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

          - `type: "unrestricted"`

            The type of the object. Always `unrestricted`.

            - `"unrestricted"`

        - `VaultCredentialNetworkingResourceLimited`

          Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

          - `allowed_hosts: Array<string>`

            The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

          - `type: "limited"`

            The type of the object. Always `limited`.

            - `"limited"`

      - `secret_name: string`

        The environment variable name that receives the placeholder in the sandbox.

      - `type: "environment_variable"`

        The type of the object. Always `environment_variable`.

        - `"environment_variable"`

  - `created_at: number`

    The Unix timestamp, in seconds, when the credential was created.

  - `metadata: Record<string, string>`

    Application-defined key-value pairs associated with this credential.

  - `name: string`

    The human-readable name of the credential.

  - `object: "vault.credential"`

    The object type. Always `vault.credential`.

    - `"vault.credential"`

  - `updated_at: number`

    The Unix timestamp, in seconds, when the credential was last updated.

  - `vault_id: string`

    The ID of the vault containing this credential.

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const credential = await client.beta.agents.vaults.credentials.retrieve('credential_id', {
  vault_id: 'vault_id',
});

console.log(credential.id);
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

`client.beta.agents.vaults.credentials.update(stringcredentialID, CredentialUpdateParamsparams, RequestOptionsoptions?): Credential`

**post** `/vaults/{vault_id}/credentials/{credential_id}`

Updates credential metadata or rotates its write-only secret. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `credentialID: string`

- `params: CredentialUpdateParams`

  - `vault_id: string`

    Path param: The ID of the vault.

  - `auth?: CredentialAuthRotateParam`

    Body param: Replacement values for the credential's existing authentication method.

    - `RotateVaultCredentialAuthParamMcpOauth`

      Rotate an OAuth credential for an HTTPS MCP destination.

      - `type: "mcp_oauth"`

        The type of the object. Always `mcp_oauth`.

        - `"mcp_oauth"`

      - `access_token?: string | null`

        A write-only replacement OAuth access token.

      - `expires_at?: string | null`

        The replacement expiry as an RFC 3339 timestamp, or `null` to clear it. Omitting this field preserves the expiry unless a new access token is supplied, in which case the expiry is cleared.

      - `refresh?: Refresh | null`

        Optional write-only refresh-token and client-secret updates.

        - `refresh_token?: string | null`

          The replacement refresh token. Omit or pass `null` to keep the stored token. This secret is never returned in resources.

        - `scope?: string | null`

          Replacement space-separated OAuth scopes for refresh requests. Omit to keep the scopes, or pass `null` to stop sending a scope parameter.

        - `token_endpoint_auth?: McpOauthTokenEndpointAuthRotateParam | null`

          Client-secret updates for the existing token endpoint authentication method.

          - `RotateMcpOauthTokenEndpointAuthParamClientSecretBasic`

            Updates credentials sent using HTTP Basic authentication.

            - `type: "client_secret_basic"`

              The type of the object. Always `client_secret_basic`.

              - `"client_secret_basic"`

            - `client_secret?: string | null`

              The replacement OAuth client secret. Omit or pass `null` to keep the stored secret. This secret is never returned in resources.

          - `RotateMcpOauthTokenEndpointAuthParamClientSecretPost`

            Updates credentials sent in the token request body.

            - `type: "client_secret_post"`

              The type of the object. Always `client_secret_post`.

              - `"client_secret_post"`

            - `client_secret?: string | null`

              The replacement OAuth client secret. Omit or pass `null` to keep the stored secret. This secret is never returned in resources.

    - `RotateVaultCredentialAuthParamStaticBearer`

      Replace the bearer token for the credential's MCP server.

      - `token: string`

        The replacement bearer token. This secret is never returned in credential resources.

      - `type: "static_bearer"`

        The type of the object. Always `static_bearer`.

        - `"static_bearer"`

    - `RotateVaultCredentialAuthParamEnvironmentVariable`

      Replace the secret for an OpenAI-hosted environment credential. The environment variable name and networking configuration remain unchanged.

      - `secret_value: string`

        The write-only replacement secret. Never returned in credential resources or supplied directly to sandbox code. Must be nonempty and must not contain carriage returns, newlines, or NUL bytes.

      - `type: "environment_variable"`

        The type of the object. Always `environment_variable`.

        - `"environment_variable"`

  - `metadata?: Record<string, string>`

    Body param: Replaces all metadata. Omit to preserve it, or pass {} to clear it. Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters.

### Returns

- `Credential`

  Metadata for a stored credential. Secret values are never returned.

  - `id: string`

    The ID of the credential.

  - `auth: CredentialAuth`

    The authentication method and non-secret configuration of the credential.

    - `VaultCredentialAuthResourceMcpOauth`

      Public metadata for an OAuth credential; tokens and client secrets are never returned.

      - `expires_at: string | null`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `mcp_server_url: string`

        The HTTPS MCP server URL authorized by this credential.

      - `refresh: Refresh | null`

        Public refresh metadata without refresh tokens or OAuth client secrets.

        - `client_id: string`

          The OAuth client ID used when requesting a new access token.

        - `resource: string | null`

          The resource URI sent to the OAuth token endpoint during refresh, if configured.

        - `scope: string | null`

          Space-separated OAuth scopes requested during refresh, if configured.

        - `token_endpoint: string`

          The HTTPS OAuth token endpoint used for refresh.

        - `token_endpoint_auth: McpOauthTokenEndpointAuth`

          How the OAuth client authenticates to the token endpoint, excluding its client secret.

          - `McpOauthTokenEndpointAuthResourceNone`

            Sends the client ID without a client secret.

            - `type: "none"`

              The type of the object. Always `none`.

              - `"none"`

          - `McpOauthTokenEndpointAuthResourceClientSecretBasic`

            Sends the client ID and secret using HTTP Basic authentication.

            - `type: "client_secret_basic"`

              The type of the object. Always `client_secret_basic`.

              - `"client_secret_basic"`

          - `McpOauthTokenEndpointAuthResourceClientSecretPost`

            Sends the client ID and secret in the token request body.

            - `type: "client_secret_post"`

              The type of the object. Always `client_secret_post`.

              - `"client_secret_post"`

      - `type: "mcp_oauth"`

        The type of the object. Always `mcp_oauth`.

        - `"mcp_oauth"`

    - `VaultCredentialAuthResourceStaticBearer`

      Metadata for a bearer-token credential, without automatic OAuth refresh.

      - `mcp_server_url: string`

        The HTTPS MCP server URL authorized by this credential.

      - `type: "static_bearer"`

        The type of the object. Always `static_bearer`.

        - `"static_bearer"`

    - `VaultCredentialAuthResourceEnvironmentVariable`

      Metadata for an HTTP credential used only in OpenAI-hosted environments. Sandbox code receives a placeholder. The proxy substitutes the secret for allowed HTTPS destinations on ports 443 and 8443. The real secret is not available to sandbox code for local computation and is never returned in this resource.

      - `networking: CredentialNetworking`

        The destinations where the proxy can substitute the secret, subject to the environment network policy.

        - `VaultCredentialNetworkingResourceUnrestricted`

          Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

          - `type: "unrestricted"`

            The type of the object. Always `unrestricted`.

            - `"unrestricted"`

        - `VaultCredentialNetworkingResourceLimited`

          Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

          - `allowed_hosts: Array<string>`

            The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

          - `type: "limited"`

            The type of the object. Always `limited`.

            - `"limited"`

      - `secret_name: string`

        The environment variable name that receives the placeholder in the sandbox.

      - `type: "environment_variable"`

        The type of the object. Always `environment_variable`.

        - `"environment_variable"`

  - `created_at: number`

    The Unix timestamp, in seconds, when the credential was created.

  - `metadata: Record<string, string>`

    Application-defined key-value pairs associated with this credential.

  - `name: string`

    The human-readable name of the credential.

  - `object: "vault.credential"`

    The object type. Always `vault.credential`.

    - `"vault.credential"`

  - `updated_at: number`

    The Unix timestamp, in seconds, when the credential was last updated.

  - `vault_id: string`

    The ID of the vault containing this credential.

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const credential = await client.beta.agents.vaults.credentials.update('credential_id', {
  vault_id: 'vault_id',
  metadata: {},
});

console.log(credential.id);
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

- `Credential`

  Metadata for a stored credential. Secret values are never returned.

  - `id: string`

    The ID of the credential.

  - `auth: CredentialAuth`

    The authentication method and non-secret configuration of the credential.

    - `VaultCredentialAuthResourceMcpOauth`

      Public metadata for an OAuth credential; tokens and client secrets are never returned.

      - `expires_at: string | null`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `mcp_server_url: string`

        The HTTPS MCP server URL authorized by this credential.

      - `refresh: Refresh | null`

        Public refresh metadata without refresh tokens or OAuth client secrets.

        - `client_id: string`

          The OAuth client ID used when requesting a new access token.

        - `resource: string | null`

          The resource URI sent to the OAuth token endpoint during refresh, if configured.

        - `scope: string | null`

          Space-separated OAuth scopes requested during refresh, if configured.

        - `token_endpoint: string`

          The HTTPS OAuth token endpoint used for refresh.

        - `token_endpoint_auth: McpOauthTokenEndpointAuth`

          How the OAuth client authenticates to the token endpoint, excluding its client secret.

          - `McpOauthTokenEndpointAuthResourceNone`

            Sends the client ID without a client secret.

            - `type: "none"`

              The type of the object. Always `none`.

              - `"none"`

          - `McpOauthTokenEndpointAuthResourceClientSecretBasic`

            Sends the client ID and secret using HTTP Basic authentication.

            - `type: "client_secret_basic"`

              The type of the object. Always `client_secret_basic`.

              - `"client_secret_basic"`

          - `McpOauthTokenEndpointAuthResourceClientSecretPost`

            Sends the client ID and secret in the token request body.

            - `type: "client_secret_post"`

              The type of the object. Always `client_secret_post`.

              - `"client_secret_post"`

      - `type: "mcp_oauth"`

        The type of the object. Always `mcp_oauth`.

        - `"mcp_oauth"`

    - `VaultCredentialAuthResourceStaticBearer`

      Metadata for a bearer-token credential, without automatic OAuth refresh.

      - `mcp_server_url: string`

        The HTTPS MCP server URL authorized by this credential.

      - `type: "static_bearer"`

        The type of the object. Always `static_bearer`.

        - `"static_bearer"`

    - `VaultCredentialAuthResourceEnvironmentVariable`

      Metadata for an HTTP credential used only in OpenAI-hosted environments. Sandbox code receives a placeholder. The proxy substitutes the secret for allowed HTTPS destinations on ports 443 and 8443. The real secret is not available to sandbox code for local computation and is never returned in this resource.

      - `networking: CredentialNetworking`

        The destinations where the proxy can substitute the secret, subject to the environment network policy.

        - `VaultCredentialNetworkingResourceUnrestricted`

          Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

          - `type: "unrestricted"`

            The type of the object. Always `unrestricted`.

            - `"unrestricted"`

        - `VaultCredentialNetworkingResourceLimited`

          Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

          - `allowed_hosts: Array<string>`

            The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

          - `type: "limited"`

            The type of the object. Always `limited`.

            - `"limited"`

      - `secret_name: string`

        The environment variable name that receives the placeholder in the sandbox.

      - `type: "environment_variable"`

        The type of the object. Always `environment_variable`.

        - `"environment_variable"`

  - `created_at: number`

    The Unix timestamp, in seconds, when the credential was created.

  - `metadata: Record<string, string>`

    Application-defined key-value pairs associated with this credential.

  - `name: string`

    The human-readable name of the credential.

  - `object: "vault.credential"`

    The object type. Always `vault.credential`.

    - `"vault.credential"`

  - `updated_at: number`

    The Unix timestamp, in seconds, when the credential was last updated.

  - `vault_id: string`

    The ID of the vault containing this credential.

### Credential Auth

- `CredentialAuth = VaultCredentialAuthResourceMcpOauth | VaultCredentialAuthResourceStaticBearer | VaultCredentialAuthResourceEnvironmentVariable`

  The authentication configuration of a vault credential, excluding secrets.

  - `VaultCredentialAuthResourceMcpOauth`

    Public metadata for an OAuth credential; tokens and client secrets are never returned.

    - `expires_at: string | null`

      When the OAuth access token expires, as an RFC 3339 timestamp, if known.

    - `mcp_server_url: string`

      The HTTPS MCP server URL authorized by this credential.

    - `refresh: Refresh | null`

      Public refresh metadata without refresh tokens or OAuth client secrets.

      - `client_id: string`

        The OAuth client ID used when requesting a new access token.

      - `resource: string | null`

        The resource URI sent to the OAuth token endpoint during refresh, if configured.

      - `scope: string | null`

        Space-separated OAuth scopes requested during refresh, if configured.

      - `token_endpoint: string`

        The HTTPS OAuth token endpoint used for refresh.

      - `token_endpoint_auth: McpOauthTokenEndpointAuth`

        How the OAuth client authenticates to the token endpoint, excluding its client secret.

        - `McpOauthTokenEndpointAuthResourceNone`

          Sends the client ID without a client secret.

          - `type: "none"`

            The type of the object. Always `none`.

            - `"none"`

        - `McpOauthTokenEndpointAuthResourceClientSecretBasic`

          Sends the client ID and secret using HTTP Basic authentication.

          - `type: "client_secret_basic"`

            The type of the object. Always `client_secret_basic`.

            - `"client_secret_basic"`

        - `McpOauthTokenEndpointAuthResourceClientSecretPost`

          Sends the client ID and secret in the token request body.

          - `type: "client_secret_post"`

            The type of the object. Always `client_secret_post`.

            - `"client_secret_post"`

    - `type: "mcp_oauth"`

      The type of the object. Always `mcp_oauth`.

      - `"mcp_oauth"`

  - `VaultCredentialAuthResourceStaticBearer`

    Metadata for a bearer-token credential, without automatic OAuth refresh.

    - `mcp_server_url: string`

      The HTTPS MCP server URL authorized by this credential.

    - `type: "static_bearer"`

      The type of the object. Always `static_bearer`.

      - `"static_bearer"`

  - `VaultCredentialAuthResourceEnvironmentVariable`

    Metadata for an HTTP credential used only in OpenAI-hosted environments. Sandbox code receives a placeholder. The proxy substitutes the secret for allowed HTTPS destinations on ports 443 and 8443. The real secret is not available to sandbox code for local computation and is never returned in this resource.

    - `networking: CredentialNetworking`

      The destinations where the proxy can substitute the secret, subject to the environment network policy.

      - `VaultCredentialNetworkingResourceUnrestricted`

        Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

        - `type: "unrestricted"`

          The type of the object. Always `unrestricted`.

          - `"unrestricted"`

      - `VaultCredentialNetworkingResourceLimited`

        Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

        - `allowed_hosts: Array<string>`

          The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

        - `type: "limited"`

          The type of the object. Always `limited`.

          - `"limited"`

    - `secret_name: string`

      The environment variable name that receives the placeholder in the sandbox.

    - `type: "environment_variable"`

      The type of the object. Always `environment_variable`.

      - `"environment_variable"`

### Credential Auth Create Param

- `CredentialAuthCreateParam = CreateVaultCredentialAuthParamMcpOauth | CreateVaultCredentialAuthParamStaticBearer | CreateVaultCredentialAuthParamEnvironmentVariable`

  Authentication credentials for an MCP server or an OpenAI-hosted environment.

  - `CreateVaultCredentialAuthParamMcpOauth`

    An OAuth credential for an HTTPS MCP destination.

    - `access_token: string`

      A write-only OAuth access token; never returned by credential resources.

    - `mcp_server_url: string`

      The HTTPS MCP server URL authorized by this credential.

    - `type: "mcp_oauth"`

      The type of the object. Always `mcp_oauth`.

      - `"mcp_oauth"`

    - `expires_at?: string | null`

      When the OAuth access token expires, as an RFC 3339 timestamp, if known.

    - `refresh?: Refresh | null`

      Optional refresh configuration for an HTTPS OAuth token endpoint.

      - `client_id: string`

        The OAuth client ID used when requesting a new access token.

      - `refresh_token: string`

        The refresh token to store. This secret is never returned in credential resources.

      - `token_endpoint: string`

        The HTTPS OAuth token endpoint used to exchange the refresh token for a new access token.

      - `token_endpoint_auth: McpOauthTokenEndpointAuthCreateParam`

        How the OAuth client authenticates to the token endpoint.

        - `CreateMcpOauthTokenEndpointAuthParamNone`

          Sends the client ID without a client secret.

          - `type: "none"`

            The type of the object. Always `none`.

            - `"none"`

        - `CreateMcpOauthTokenEndpointAuthParamClientSecretBasic`

          Sends the client ID and secret using HTTP Basic authentication.

          - `client_secret: string`

            The OAuth client secret to store. Never returned in credential resources.

          - `type: "client_secret_basic"`

            The type of the object. Always `client_secret_basic`.

            - `"client_secret_basic"`

        - `CreateMcpOauthTokenEndpointAuthParamClientSecretPost`

          Sends the client ID and secret in the token request body.

          - `client_secret: string`

            The OAuth client secret to store. Never returned in credential resources.

          - `type: "client_secret_post"`

            The type of the object. Always `client_secret_post`.

            - `"client_secret_post"`

      - `resource?: string | null`

        The resource URI to send to the OAuth token endpoint during refresh, if required.

      - `scope?: string | null`

        Space-separated OAuth scopes to request during refresh, if required.

  - `CreateVaultCredentialAuthParamStaticBearer`

    A bearer token for an MCP server, without automatic OAuth refresh.

    - `token: string`

      The bearer token to store. This secret is never returned in credential resources.

    - `mcp_server_url: string`

      The HTTPS MCP server URL authorized by this credential.

    - `type: "static_bearer"`

      The type of the object. Always `static_bearer`.

      - `"static_bearer"`

  - `CreateVaultCredentialAuthParamEnvironmentVariable`

    An HTTP credential for OpenAI-hosted environments only. The sandbox receives an environment variable containing a placeholder, not the secret. Use the placeholder unchanged in outgoing requests. The egress proxy replaces the placeholder with the secret for allowed HTTPS destinations on ports 443 and 8443. Sandbox code cannot read the real secret or use it for local computation, such as signing a request.

    - `networking: CredentialNetworkingParam`

      The destinations where the proxy can substitute this secret. The environment network policy must also allow them.

      - `VaultCredentialNetworkingParamUnrestricted`

        Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

        - `type: "unrestricted"`

          The type of the object. Always `unrestricted`.

          - `"unrestricted"`

      - `VaultCredentialNetworkingParamLimited`

        Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

        - `allowed_hosts: Array<string>`

          The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

        - `type: "limited"`

          The type of the object. Always `limited`.

          - `"limited"`

    - `secret_name: string`

      The environment variable name that receives the placeholder, such as `SERVICE_API_KEY`. Use ASCII letters, digits, and underscores, starting with a letter or underscore. Names starting with `CODEX_` and managed proxy or certificate variable names are reserved.

    - `secret_value: string`

      The write-only secret to store. Never returned in credential resources or supplied directly to sandbox code. Must be nonempty and must not contain carriage returns, newlines, or NUL bytes.

    - `type: "environment_variable"`

      The type of the object. Always `environment_variable`.

      - `"environment_variable"`

### Credential Auth Rotate Param

- `CredentialAuthRotateParam = RotateVaultCredentialAuthParamMcpOauth | RotateVaultCredentialAuthParamStaticBearer | RotateVaultCredentialAuthParamEnvironmentVariable`

  Updates to a vault credential without changing its authentication method or destination configuration.

  - `RotateVaultCredentialAuthParamMcpOauth`

    Rotate an OAuth credential for an HTTPS MCP destination.

    - `type: "mcp_oauth"`

      The type of the object. Always `mcp_oauth`.

      - `"mcp_oauth"`

    - `access_token?: string | null`

      A write-only replacement OAuth access token.

    - `expires_at?: string | null`

      The replacement expiry as an RFC 3339 timestamp, or `null` to clear it. Omitting this field preserves the expiry unless a new access token is supplied, in which case the expiry is cleared.

    - `refresh?: Refresh | null`

      Optional write-only refresh-token and client-secret updates.

      - `refresh_token?: string | null`

        The replacement refresh token. Omit or pass `null` to keep the stored token. This secret is never returned in resources.

      - `scope?: string | null`

        Replacement space-separated OAuth scopes for refresh requests. Omit to keep the scopes, or pass `null` to stop sending a scope parameter.

      - `token_endpoint_auth?: McpOauthTokenEndpointAuthRotateParam | null`

        Client-secret updates for the existing token endpoint authentication method.

        - `RotateMcpOauthTokenEndpointAuthParamClientSecretBasic`

          Updates credentials sent using HTTP Basic authentication.

          - `type: "client_secret_basic"`

            The type of the object. Always `client_secret_basic`.

            - `"client_secret_basic"`

          - `client_secret?: string | null`

            The replacement OAuth client secret. Omit or pass `null` to keep the stored secret. This secret is never returned in resources.

        - `RotateMcpOauthTokenEndpointAuthParamClientSecretPost`

          Updates credentials sent in the token request body.

          - `type: "client_secret_post"`

            The type of the object. Always `client_secret_post`.

            - `"client_secret_post"`

          - `client_secret?: string | null`

            The replacement OAuth client secret. Omit or pass `null` to keep the stored secret. This secret is never returned in resources.

  - `RotateVaultCredentialAuthParamStaticBearer`

    Replace the bearer token for the credential's MCP server.

    - `token: string`

      The replacement bearer token. This secret is never returned in credential resources.

    - `type: "static_bearer"`

      The type of the object. Always `static_bearer`.

      - `"static_bearer"`

  - `RotateVaultCredentialAuthParamEnvironmentVariable`

    Replace the secret for an OpenAI-hosted environment credential. The environment variable name and networking configuration remain unchanged.

    - `secret_value: string`

      The write-only replacement secret. Never returned in credential resources or supplied directly to sandbox code. Must be nonempty and must not contain carriage returns, newlines, or NUL bytes.

    - `type: "environment_variable"`

      The type of the object. Always `environment_variable`.

      - `"environment_variable"`

### Credential Deleted

- `CredentialDeleted`

  Confirmation that a vault credential was deleted.

  - `id: string`

    The ID of the deleted credential.

  - `deleted: boolean`

    Whether the resource was deleted. Always `true`.

  - `object: "vault.credential.deleted"`

    The object type. Always `vault.credential.deleted`.

    - `"vault.credential.deleted"`

### Credential Networking

- `CredentialNetworking = VaultCredentialNetworkingResourceUnrestricted | VaultCredentialNetworkingResourceLimited`

  Destination permissions for an environment-variable credential. These do not grant network access to the environment.

  - `VaultCredentialNetworkingResourceUnrestricted`

    Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

    - `type: "unrestricted"`

      The type of the object. Always `unrestricted`.

      - `"unrestricted"`

  - `VaultCredentialNetworkingResourceLimited`

    Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

    - `allowed_hosts: Array<string>`

      The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

    - `type: "limited"`

      The type of the object. Always `limited`.

      - `"limited"`

### Credential Networking Param

- `CredentialNetworkingParam = VaultCredentialNetworkingParamUnrestricted | VaultCredentialNetworkingParamLimited`

  Destination permissions for an environment-variable credential. These do not grant network access to the environment.

  - `VaultCredentialNetworkingParamUnrestricted`

    Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

    - `type: "unrestricted"`

      The type of the object. Always `unrestricted`.

      - `"unrestricted"`

  - `VaultCredentialNetworkingParamLimited`

    Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

    - `allowed_hosts: Array<string>`

      The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

    - `type: "limited"`

      The type of the object. Always `limited`.

      - `"limited"`

### Mcp OAuth Token Endpoint Auth

- `McpOauthTokenEndpointAuth = McpOauthTokenEndpointAuthResourceNone | McpOauthTokenEndpointAuthResourceClientSecretBasic | McpOauthTokenEndpointAuthResourceClientSecretPost`

  The client authentication method used for OAuth token refresh.

  - `McpOauthTokenEndpointAuthResourceNone`

    Sends the client ID without a client secret.

    - `type: "none"`

      The type of the object. Always `none`.

      - `"none"`

  - `McpOauthTokenEndpointAuthResourceClientSecretBasic`

    Sends the client ID and secret using HTTP Basic authentication.

    - `type: "client_secret_basic"`

      The type of the object. Always `client_secret_basic`.

      - `"client_secret_basic"`

  - `McpOauthTokenEndpointAuthResourceClientSecretPost`

    Sends the client ID and secret in the token request body.

    - `type: "client_secret_post"`

      The type of the object. Always `client_secret_post`.

      - `"client_secret_post"`

### Mcp OAuth Token Endpoint Auth Create Param

- `McpOauthTokenEndpointAuthCreateParam = CreateMcpOauthTokenEndpointAuthParamNone | CreateMcpOauthTokenEndpointAuthParamClientSecretBasic | CreateMcpOauthTokenEndpointAuthParamClientSecretPost`

  Client authentication credentials for OAuth token refresh.

  - `CreateMcpOauthTokenEndpointAuthParamNone`

    Sends the client ID without a client secret.

    - `type: "none"`

      The type of the object. Always `none`.

      - `"none"`

  - `CreateMcpOauthTokenEndpointAuthParamClientSecretBasic`

    Sends the client ID and secret using HTTP Basic authentication.

    - `client_secret: string`

      The OAuth client secret to store. Never returned in credential resources.

    - `type: "client_secret_basic"`

      The type of the object. Always `client_secret_basic`.

      - `"client_secret_basic"`

  - `CreateMcpOauthTokenEndpointAuthParamClientSecretPost`

    Sends the client ID and secret in the token request body.

    - `client_secret: string`

      The OAuth client secret to store. Never returned in credential resources.

    - `type: "client_secret_post"`

      The type of the object. Always `client_secret_post`.

      - `"client_secret_post"`

### Mcp OAuth Token Endpoint Auth Rotate Param

- `McpOauthTokenEndpointAuthRotateParam = RotateMcpOauthTokenEndpointAuthParamClientSecretBasic | RotateMcpOauthTokenEndpointAuthParamClientSecretPost`

  Client-secret updates that preserve the credential's OAuth authentication method.

  - `RotateMcpOauthTokenEndpointAuthParamClientSecretBasic`

    Updates credentials sent using HTTP Basic authentication.

    - `type: "client_secret_basic"`

      The type of the object. Always `client_secret_basic`.

      - `"client_secret_basic"`

    - `client_secret?: string | null`

      The replacement OAuth client secret. Omit or pass `null` to keep the stored secret. This secret is never returned in resources.

  - `RotateMcpOauthTokenEndpointAuthParamClientSecretPost`

    Updates credentials sent in the token request body.

    - `type: "client_secret_post"`

      The type of the object. Always `client_secret_post`.

      - `"client_secret_post"`

    - `client_secret?: string | null`

      The replacement OAuth client secret. Omit or pass `null` to keep the stored secret. This secret is never returned in resources.
