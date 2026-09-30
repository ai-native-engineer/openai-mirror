<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/agents/subresources/vaults/ -->

# Vaults

## Create a vault

`beta.agents.vaults.create(VaultCreateParams**kwargs)  -> Vault`

**post** `/vaults`

Creates a vault for the current project. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `metadata: Optional[Dict[str, str]]`

  Key-value pairs to associate with the vault, such as an application or team identifier.

- `name: Optional[str]`

  The name is trimmed before storage. It must contain 1 to 256 UTF-8 bytes after trimming.

### Returns

- `class Vault: …`

  A collection of credentials for MCP servers and OpenAI-hosted environments.

  - `id: str`

    The ID of the vault.

  - `created_at: int`

    The Unix timestamp, in seconds, when the vault was created.

  - `metadata: Dict[str, str]`

    Key-value pairs associated with the vault, such as an application or team identifier.

  - `name: Optional[str]`

    The human-readable name of the vault, if set.

  - `object: Literal["vault"]`

    The object type. Always `vault`.

    - `"vault"`

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
vault = client.beta.agents.vaults.create()
print(vault.id)
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

`beta.agents.vaults.delete(strvault_id)  -> VaultDeleted`

**delete** `/vaults/{vault_id}`

Deletes a vault and all its credentials. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vault_id: str`

### Returns

- `class VaultDeleted: …`

  Confirmation that a vault was deleted.

  - `id: str`

    The ID of the deleted vault.

  - `deleted: bool`

    Whether the resource was deleted. Always `true`.

  - `object: Literal["vault.deleted"]`

    The object type. Always `vault.deleted`.

    - `"vault.deleted"`

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
vault_deleted = client.beta.agents.vaults.delete(
    "vault_id",
)
print(vault_deleted.id)
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

`beta.agents.vaults.list(VaultListParams**kwargs)  -> SyncCursorPage[Vault]`

**get** `/vaults`

Lists vaults using ID-based pagination. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `after: Optional[str]`

  Return resources after this resource ID in the selected order.

- `limit: Optional[int]`

  The maximum number of resources to return. Defaults to 20. Values are clamped between 1 and 100.

- `order: Optional[Literal["asc", "desc"]]`

  Sort order by the `created_at` timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `desc`.

  - `"asc"`

    Returns resources in ascending order.

  - `"desc"`

    Returns resources in descending order.

- `status: Optional[VaultStatusFilterParam]`

  Filter by one status or a list, such as `status=active` or `status[]=active&status[]=archived`. Both statuses are included by default.

  - `Literal["active", "archived"]`

    - `"active"`

    - `"archived"`

  - `List[VaultStatus]`

    - `"active"`

    - `"archived"`

### Returns

- `class Vault: …`

  A collection of credentials for MCP servers and OpenAI-hosted environments.

  - `id: str`

    The ID of the vault.

  - `created_at: int`

    The Unix timestamp, in seconds, when the vault was created.

  - `metadata: Dict[str, str]`

    Key-value pairs associated with the vault, such as an application or team identifier.

  - `name: Optional[str]`

    The human-readable name of the vault, if set.

  - `object: Literal["vault"]`

    The object type. Always `vault`.

    - `"vault"`

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.agents.vaults.list()
page = page.data[0]
print(page.id)
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

`beta.agents.vaults.retrieve(strvault_id)  -> Vault`

**get** `/vaults/{vault_id}`

Retrieves a vault by its ID. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vault_id: str`

### Returns

- `class Vault: …`

  A collection of credentials for MCP servers and OpenAI-hosted environments.

  - `id: str`

    The ID of the vault.

  - `created_at: int`

    The Unix timestamp, in seconds, when the vault was created.

  - `metadata: Dict[str, str]`

    Key-value pairs associated with the vault, such as an application or team identifier.

  - `name: Optional[str]`

    The human-readable name of the vault, if set.

  - `object: Literal["vault"]`

    The object type. Always `vault`.

    - `"vault"`

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
vault = client.beta.agents.vaults.retrieve(
    "vault_id",
)
print(vault.id)
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

- `class Vault: …`

  A collection of credentials for MCP servers and OpenAI-hosted environments.

  - `id: str`

    The ID of the vault.

  - `created_at: int`

    The Unix timestamp, in seconds, when the vault was created.

  - `metadata: Dict[str, str]`

    Key-value pairs associated with the vault, such as an application or team identifier.

  - `name: Optional[str]`

    The human-readable name of the vault, if set.

  - `object: Literal["vault"]`

    The object type. Always `vault`.

    - `"vault"`

### Vault Deleted

- `class VaultDeleted: …`

  Confirmation that a vault was deleted.

  - `id: str`

    The ID of the deleted vault.

  - `deleted: bool`

    Whether the resource was deleted. Always `true`.

  - `object: Literal["vault.deleted"]`

    The object type. Always `vault.deleted`.

    - `"vault.deleted"`

### Vault Status

- `Literal["active", "archived"]`

  Whether a vault or credential is active or archived.

  - `"active"`

  - `"archived"`

### Vault Status Filter

- `Union[VaultStatus, List[VaultStatus]]`

  One or more lifecycle statuses to include when listing vaults or credentials.

  - `Literal["active", "archived"]`

    - `"active"`

    - `"archived"`

  - `List[VaultStatus]`

    - `"active"`

    - `"archived"`

# Credentials

## Create a vault credential

`beta.agents.vaults.credentials.create(strvault_id, CredentialCreateParams**kwargs)  -> Credential`

**post** `/vaults/{vault_id}/credentials`

Creates a vault credential. Secret values are write-only and are never returned. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vault_id: str`

- `auth: CredentialAuthCreateParam`

  The authentication method and write-only secret values to store.

  - `class CreateVaultCredentialAuthParamMcpOauth: …`

    An OAuth credential for an HTTPS MCP destination.

    - `access_token: str`

      A write-only OAuth access token; never returned by credential resources.

    - `mcp_server_url: str`

      The HTTPS MCP server URL authorized by this credential.

    - `type: Literal["mcp_oauth"]`

      The type of the object. Always `mcp_oauth`.

      - `"mcp_oauth"`

    - `expires_at: Optional[str]`

      When the OAuth access token expires, as an RFC 3339 timestamp, if known.

    - `refresh: Optional[CreateVaultCredentialAuthParamMcpOauthRefresh]`

      Optional refresh configuration for an HTTPS OAuth token endpoint.

      - `client_id: str`

        The OAuth client ID used when requesting a new access token.

      - `refresh_token: str`

        The refresh token to store. This secret is never returned in credential resources.

      - `token_endpoint: str`

        The HTTPS OAuth token endpoint used to exchange the refresh token for a new access token.

      - `token_endpoint_auth: McpOauthTokenEndpointAuthCreateParam`

        How the OAuth client authenticates to the token endpoint.

        - `class CreateMcpOauthTokenEndpointAuthParamNone: …`

          Sends the client ID without a client secret.

          - `type: Literal["none"]`

            The type of the object. Always `none`.

            - `"none"`

        - `class CreateMcpOauthTokenEndpointAuthParamClientSecretBasic: …`

          Sends the client ID and secret using HTTP Basic authentication.

          - `client_secret: str`

            The OAuth client secret to store. Never returned in credential resources.

          - `type: Literal["client_secret_basic"]`

            The type of the object. Always `client_secret_basic`.

            - `"client_secret_basic"`

        - `class CreateMcpOauthTokenEndpointAuthParamClientSecretPost: …`

          Sends the client ID and secret in the token request body.

          - `client_secret: str`

            The OAuth client secret to store. Never returned in credential resources.

          - `type: Literal["client_secret_post"]`

            The type of the object. Always `client_secret_post`.

            - `"client_secret_post"`

      - `resource: Optional[str]`

        The resource URI to send to the OAuth token endpoint during refresh, if required.

      - `scope: Optional[str]`

        Space-separated OAuth scopes to request during refresh, if required.

  - `class CreateVaultCredentialAuthParamStaticBearer: …`

    A bearer token for an MCP server, without automatic OAuth refresh.

    - `token: str`

      The bearer token to store. This secret is never returned in credential resources.

    - `mcp_server_url: str`

      The HTTPS MCP server URL authorized by this credential.

    - `type: Literal["static_bearer"]`

      The type of the object. Always `static_bearer`.

      - `"static_bearer"`

  - `class CreateVaultCredentialAuthParamEnvironmentVariable: …`

    An HTTP credential for OpenAI-hosted environments only. The sandbox receives an environment variable containing a placeholder, not the secret. Use the placeholder unchanged in outgoing requests. The egress proxy replaces the placeholder with the secret for allowed HTTPS destinations on ports 443 and 8443. Sandbox code cannot read the real secret or use it for local computation, such as signing a request.

    - `networking: CredentialNetworkingParam`

      The destinations where the proxy can substitute this secret. The environment network policy must also allow them.

      - `class VaultCredentialNetworkingParamUnrestricted: …`

        Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

        - `type: Literal["unrestricted"]`

          The type of the object. Always `unrestricted`.

          - `"unrestricted"`

      - `class VaultCredentialNetworkingParamLimited: …`

        Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

        - `allowed_hosts: List[str]`

          The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

        - `type: Literal["limited"]`

          The type of the object. Always `limited`.

          - `"limited"`

    - `secret_name: str`

      The environment variable name that receives the placeholder, such as `SERVICE_API_KEY`. Use ASCII letters, digits, and underscores, starting with a letter or underscore. Names starting with `CODEX_` and managed proxy or certificate variable names are reserved.

    - `secret_value: str`

      The write-only secret to store. Never returned in credential resources or supplied directly to sandbox code. Must be nonempty and must not contain carriage returns, newlines, or NUL bytes.

    - `type: Literal["environment_variable"]`

      The type of the object. Always `environment_variable`.

      - `"environment_variable"`

- `name: str`

  The name is trimmed before storage. It must contain 1 to 256 UTF-8 bytes after trimming.

- `metadata: Optional[Dict[str, str]]`

  Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters. Defaults to an empty map.

### Returns

- `class Credential: …`

  Metadata for a stored credential. Secret values are never returned.

  - `id: str`

    The ID of the credential.

  - `auth: CredentialAuth`

    The authentication method and non-secret configuration of the credential.

    - `class VaultCredentialAuthResourceMcpOauth: …`

      Public metadata for an OAuth credential; tokens and client secrets are never returned.

      - `expires_at: Optional[str]`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `mcp_server_url: str`

        The HTTPS MCP server URL authorized by this credential.

      - `refresh: Optional[VaultCredentialAuthResourceMcpOauthRefresh]`

        Public refresh metadata without refresh tokens or OAuth client secrets.

        - `client_id: str`

          The OAuth client ID used when requesting a new access token.

        - `resource: Optional[str]`

          The resource URI sent to the OAuth token endpoint during refresh, if configured.

        - `scope: Optional[str]`

          Space-separated OAuth scopes requested during refresh, if configured.

        - `token_endpoint: str`

          The HTTPS OAuth token endpoint used for refresh.

        - `token_endpoint_auth: McpOauthTokenEndpointAuth`

          How the OAuth client authenticates to the token endpoint, excluding its client secret.

          - `class McpOauthTokenEndpointAuthResourceNone: …`

            Sends the client ID without a client secret.

            - `type: Literal["none"]`

              The type of the object. Always `none`.

              - `"none"`

          - `class McpOauthTokenEndpointAuthResourceClientSecretBasic: …`

            Sends the client ID and secret using HTTP Basic authentication.

            - `type: Literal["client_secret_basic"]`

              The type of the object. Always `client_secret_basic`.

              - `"client_secret_basic"`

          - `class McpOauthTokenEndpointAuthResourceClientSecretPost: …`

            Sends the client ID and secret in the token request body.

            - `type: Literal["client_secret_post"]`

              The type of the object. Always `client_secret_post`.

              - `"client_secret_post"`

      - `type: Literal["mcp_oauth"]`

        The type of the object. Always `mcp_oauth`.

        - `"mcp_oauth"`

    - `class VaultCredentialAuthResourceStaticBearer: …`

      Metadata for a bearer-token credential, without automatic OAuth refresh.

      - `mcp_server_url: str`

        The HTTPS MCP server URL authorized by this credential.

      - `type: Literal["static_bearer"]`

        The type of the object. Always `static_bearer`.

        - `"static_bearer"`

    - `class VaultCredentialAuthResourceEnvironmentVariable: …`

      Metadata for an HTTP credential used only in OpenAI-hosted environments. Sandbox code receives a placeholder. The proxy substitutes the secret for allowed HTTPS destinations on ports 443 and 8443. The real secret is not available to sandbox code for local computation and is never returned in this resource.

      - `networking: CredentialNetworking`

        The destinations where the proxy can substitute the secret, subject to the environment network policy.

        - `class VaultCredentialNetworkingResourceUnrestricted: …`

          Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

          - `type: Literal["unrestricted"]`

            The type of the object. Always `unrestricted`.

            - `"unrestricted"`

        - `class VaultCredentialNetworkingResourceLimited: …`

          Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

          - `allowed_hosts: List[str]`

            The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

          - `type: Literal["limited"]`

            The type of the object. Always `limited`.

            - `"limited"`

      - `secret_name: str`

        The environment variable name that receives the placeholder in the sandbox.

      - `type: Literal["environment_variable"]`

        The type of the object. Always `environment_variable`.

        - `"environment_variable"`

  - `created_at: int`

    The Unix timestamp, in seconds, when the credential was created.

  - `metadata: Dict[str, str]`

    Application-defined key-value pairs associated with this credential.

  - `name: str`

    The human-readable name of the credential.

  - `object: Literal["vault.credential"]`

    The object type. Always `vault.credential`.

    - `"vault.credential"`

  - `updated_at: int`

    The Unix timestamp, in seconds, when the credential was last updated.

  - `vault_id: str`

    The ID of the vault containing this credential.

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
credential = client.beta.agents.vaults.credentials.create(
    vault_id="vault_id",
    auth={
        "access_token": "access_token",
        "mcp_server_url": "mcp_server_url",
        "type": "mcp_oauth",
    },
    name="x",
)
print(credential.id)
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

`beta.agents.vaults.credentials.delete(strcredential_id, CredentialDeleteParams**kwargs)  -> CredentialDeleted`

**delete** `/vaults/{vault_id}/credentials/{credential_id}`

Deletes a vault credential. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vault_id: str`

- `credential_id: str`

### Returns

- `class CredentialDeleted: …`

  Confirmation that a vault credential was deleted.

  - `id: str`

    The ID of the deleted credential.

  - `deleted: bool`

    Whether the resource was deleted. Always `true`.

  - `object: Literal["vault.credential.deleted"]`

    The object type. Always `vault.credential.deleted`.

    - `"vault.credential.deleted"`

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
credential_deleted = client.beta.agents.vaults.credentials.delete(
    credential_id="credential_id",
    vault_id="vault_id",
)
print(credential_deleted.id)
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

`beta.agents.vaults.credentials.list(strvault_id, CredentialListParams**kwargs)  -> SyncCursorPage[Credential]`

**get** `/vaults/{vault_id}/credentials`

Lists a vault's credentials using ID-based pagination without returning secret values. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vault_id: str`

- `after: Optional[str]`

  Return resources after this resource ID in the selected order.

- `limit: Optional[int]`

  The maximum number of resources to return. Defaults to 20. Values are clamped between 1 and 100.

- `order: Optional[Literal["asc", "desc"]]`

  Sort order by the `created_at` timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `desc`.

  - `"asc"`

    Returns resources in ascending order.

  - `"desc"`

    Returns resources in descending order.

- `status: Optional[VaultStatusFilterParam]`

  Filter by one status or a list, such as `status=active` or `status[]=active&status[]=archived`. Both statuses are included by default.

  - `Literal["active", "archived"]`

    - `"active"`

    - `"archived"`

  - `List[VaultStatus]`

    - `"active"`

    - `"archived"`

### Returns

- `class Credential: …`

  Metadata for a stored credential. Secret values are never returned.

  - `id: str`

    The ID of the credential.

  - `auth: CredentialAuth`

    The authentication method and non-secret configuration of the credential.

    - `class VaultCredentialAuthResourceMcpOauth: …`

      Public metadata for an OAuth credential; tokens and client secrets are never returned.

      - `expires_at: Optional[str]`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `mcp_server_url: str`

        The HTTPS MCP server URL authorized by this credential.

      - `refresh: Optional[VaultCredentialAuthResourceMcpOauthRefresh]`

        Public refresh metadata without refresh tokens or OAuth client secrets.

        - `client_id: str`

          The OAuth client ID used when requesting a new access token.

        - `resource: Optional[str]`

          The resource URI sent to the OAuth token endpoint during refresh, if configured.

        - `scope: Optional[str]`

          Space-separated OAuth scopes requested during refresh, if configured.

        - `token_endpoint: str`

          The HTTPS OAuth token endpoint used for refresh.

        - `token_endpoint_auth: McpOauthTokenEndpointAuth`

          How the OAuth client authenticates to the token endpoint, excluding its client secret.

          - `class McpOauthTokenEndpointAuthResourceNone: …`

            Sends the client ID without a client secret.

            - `type: Literal["none"]`

              The type of the object. Always `none`.

              - `"none"`

          - `class McpOauthTokenEndpointAuthResourceClientSecretBasic: …`

            Sends the client ID and secret using HTTP Basic authentication.

            - `type: Literal["client_secret_basic"]`

              The type of the object. Always `client_secret_basic`.

              - `"client_secret_basic"`

          - `class McpOauthTokenEndpointAuthResourceClientSecretPost: …`

            Sends the client ID and secret in the token request body.

            - `type: Literal["client_secret_post"]`

              The type of the object. Always `client_secret_post`.

              - `"client_secret_post"`

      - `type: Literal["mcp_oauth"]`

        The type of the object. Always `mcp_oauth`.

        - `"mcp_oauth"`

    - `class VaultCredentialAuthResourceStaticBearer: …`

      Metadata for a bearer-token credential, without automatic OAuth refresh.

      - `mcp_server_url: str`

        The HTTPS MCP server URL authorized by this credential.

      - `type: Literal["static_bearer"]`

        The type of the object. Always `static_bearer`.

        - `"static_bearer"`

    - `class VaultCredentialAuthResourceEnvironmentVariable: …`

      Metadata for an HTTP credential used only in OpenAI-hosted environments. Sandbox code receives a placeholder. The proxy substitutes the secret for allowed HTTPS destinations on ports 443 and 8443. The real secret is not available to sandbox code for local computation and is never returned in this resource.

      - `networking: CredentialNetworking`

        The destinations where the proxy can substitute the secret, subject to the environment network policy.

        - `class VaultCredentialNetworkingResourceUnrestricted: …`

          Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

          - `type: Literal["unrestricted"]`

            The type of the object. Always `unrestricted`.

            - `"unrestricted"`

        - `class VaultCredentialNetworkingResourceLimited: …`

          Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

          - `allowed_hosts: List[str]`

            The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

          - `type: Literal["limited"]`

            The type of the object. Always `limited`.

            - `"limited"`

      - `secret_name: str`

        The environment variable name that receives the placeholder in the sandbox.

      - `type: Literal["environment_variable"]`

        The type of the object. Always `environment_variable`.

        - `"environment_variable"`

  - `created_at: int`

    The Unix timestamp, in seconds, when the credential was created.

  - `metadata: Dict[str, str]`

    Application-defined key-value pairs associated with this credential.

  - `name: str`

    The human-readable name of the credential.

  - `object: Literal["vault.credential"]`

    The object type. Always `vault.credential`.

    - `"vault.credential"`

  - `updated_at: int`

    The Unix timestamp, in seconds, when the credential was last updated.

  - `vault_id: str`

    The ID of the vault containing this credential.

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.agents.vaults.credentials.list(
    vault_id="vault_id",
)
page = page.data[0]
print(page.id)
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

`beta.agents.vaults.credentials.retrieve(strcredential_id, CredentialRetrieveParams**kwargs)  -> Credential`

**get** `/vaults/{vault_id}/credentials/{credential_id}`

Retrieves vault credential metadata without returning secret values. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vault_id: str`

- `credential_id: str`

### Returns

- `class Credential: …`

  Metadata for a stored credential. Secret values are never returned.

  - `id: str`

    The ID of the credential.

  - `auth: CredentialAuth`

    The authentication method and non-secret configuration of the credential.

    - `class VaultCredentialAuthResourceMcpOauth: …`

      Public metadata for an OAuth credential; tokens and client secrets are never returned.

      - `expires_at: Optional[str]`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `mcp_server_url: str`

        The HTTPS MCP server URL authorized by this credential.

      - `refresh: Optional[VaultCredentialAuthResourceMcpOauthRefresh]`

        Public refresh metadata without refresh tokens or OAuth client secrets.

        - `client_id: str`

          The OAuth client ID used when requesting a new access token.

        - `resource: Optional[str]`

          The resource URI sent to the OAuth token endpoint during refresh, if configured.

        - `scope: Optional[str]`

          Space-separated OAuth scopes requested during refresh, if configured.

        - `token_endpoint: str`

          The HTTPS OAuth token endpoint used for refresh.

        - `token_endpoint_auth: McpOauthTokenEndpointAuth`

          How the OAuth client authenticates to the token endpoint, excluding its client secret.

          - `class McpOauthTokenEndpointAuthResourceNone: …`

            Sends the client ID without a client secret.

            - `type: Literal["none"]`

              The type of the object. Always `none`.

              - `"none"`

          - `class McpOauthTokenEndpointAuthResourceClientSecretBasic: …`

            Sends the client ID and secret using HTTP Basic authentication.

            - `type: Literal["client_secret_basic"]`

              The type of the object. Always `client_secret_basic`.

              - `"client_secret_basic"`

          - `class McpOauthTokenEndpointAuthResourceClientSecretPost: …`

            Sends the client ID and secret in the token request body.

            - `type: Literal["client_secret_post"]`

              The type of the object. Always `client_secret_post`.

              - `"client_secret_post"`

      - `type: Literal["mcp_oauth"]`

        The type of the object. Always `mcp_oauth`.

        - `"mcp_oauth"`

    - `class VaultCredentialAuthResourceStaticBearer: …`

      Metadata for a bearer-token credential, without automatic OAuth refresh.

      - `mcp_server_url: str`

        The HTTPS MCP server URL authorized by this credential.

      - `type: Literal["static_bearer"]`

        The type of the object. Always `static_bearer`.

        - `"static_bearer"`

    - `class VaultCredentialAuthResourceEnvironmentVariable: …`

      Metadata for an HTTP credential used only in OpenAI-hosted environments. Sandbox code receives a placeholder. The proxy substitutes the secret for allowed HTTPS destinations on ports 443 and 8443. The real secret is not available to sandbox code for local computation and is never returned in this resource.

      - `networking: CredentialNetworking`

        The destinations where the proxy can substitute the secret, subject to the environment network policy.

        - `class VaultCredentialNetworkingResourceUnrestricted: …`

          Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

          - `type: Literal["unrestricted"]`

            The type of the object. Always `unrestricted`.

            - `"unrestricted"`

        - `class VaultCredentialNetworkingResourceLimited: …`

          Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

          - `allowed_hosts: List[str]`

            The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

          - `type: Literal["limited"]`

            The type of the object. Always `limited`.

            - `"limited"`

      - `secret_name: str`

        The environment variable name that receives the placeholder in the sandbox.

      - `type: Literal["environment_variable"]`

        The type of the object. Always `environment_variable`.

        - `"environment_variable"`

  - `created_at: int`

    The Unix timestamp, in seconds, when the credential was created.

  - `metadata: Dict[str, str]`

    Application-defined key-value pairs associated with this credential.

  - `name: str`

    The human-readable name of the credential.

  - `object: Literal["vault.credential"]`

    The object type. Always `vault.credential`.

    - `"vault.credential"`

  - `updated_at: int`

    The Unix timestamp, in seconds, when the credential was last updated.

  - `vault_id: str`

    The ID of the vault containing this credential.

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
credential = client.beta.agents.vaults.credentials.retrieve(
    credential_id="credential_id",
    vault_id="vault_id",
)
print(credential.id)
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

`beta.agents.vaults.credentials.update(strcredential_id, CredentialUpdateParams**kwargs)  -> Credential`

**post** `/vaults/{vault_id}/credentials/{credential_id}`

Updates credential metadata or rotates its write-only secret. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vault_id: str`

- `credential_id: str`

- `auth: Optional[CredentialAuthRotateParam]`

  Replacement values for the credential's existing authentication method.

  - `class RotateVaultCredentialAuthParamMcpOauth: …`

    Rotate an OAuth credential for an HTTPS MCP destination.

    - `type: Literal["mcp_oauth"]`

      The type of the object. Always `mcp_oauth`.

      - `"mcp_oauth"`

    - `access_token: Optional[str]`

      A write-only replacement OAuth access token.

    - `expires_at: Optional[str]`

      The replacement expiry as an RFC 3339 timestamp, or `null` to clear it. Omitting this field preserves the expiry unless a new access token is supplied, in which case the expiry is cleared.

    - `refresh: Optional[RotateVaultCredentialAuthParamMcpOauthRefresh]`

      Optional write-only refresh-token and client-secret updates.

      - `refresh_token: Optional[str]`

        The replacement refresh token. Omit or pass `null` to keep the stored token. This secret is never returned in resources.

      - `scope: Optional[str]`

        Replacement space-separated OAuth scopes for refresh requests. Omit to keep the scopes, or pass `null` to stop sending a scope parameter.

      - `token_endpoint_auth: Optional[McpOauthTokenEndpointAuthRotateParam]`

        Client-secret updates for the existing token endpoint authentication method.

        - `class RotateMcpOauthTokenEndpointAuthParamClientSecretBasic: …`

          Updates credentials sent using HTTP Basic authentication.

          - `type: Literal["client_secret_basic"]`

            The type of the object. Always `client_secret_basic`.

            - `"client_secret_basic"`

          - `client_secret: Optional[str]`

            The replacement OAuth client secret. Omit or pass `null` to keep the stored secret. This secret is never returned in resources.

        - `class RotateMcpOauthTokenEndpointAuthParamClientSecretPost: …`

          Updates credentials sent in the token request body.

          - `type: Literal["client_secret_post"]`

            The type of the object. Always `client_secret_post`.

            - `"client_secret_post"`

          - `client_secret: Optional[str]`

            The replacement OAuth client secret. Omit or pass `null` to keep the stored secret. This secret is never returned in resources.

  - `class RotateVaultCredentialAuthParamStaticBearer: …`

    Replace the bearer token for the credential's MCP server.

    - `token: str`

      The replacement bearer token. This secret is never returned in credential resources.

    - `type: Literal["static_bearer"]`

      The type of the object. Always `static_bearer`.

      - `"static_bearer"`

  - `class RotateVaultCredentialAuthParamEnvironmentVariable: …`

    Replace the secret for an OpenAI-hosted environment credential. The environment variable name and networking configuration remain unchanged.

    - `secret_value: str`

      The write-only replacement secret. Never returned in credential resources or supplied directly to sandbox code. Must be nonempty and must not contain carriage returns, newlines, or NUL bytes.

    - `type: Literal["environment_variable"]`

      The type of the object. Always `environment_variable`.

      - `"environment_variable"`

- `metadata: Optional[Dict[str, str]]`

  Replaces all metadata. Omit to preserve it, or pass {} to clear it. Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters.

### Returns

- `class Credential: …`

  Metadata for a stored credential. Secret values are never returned.

  - `id: str`

    The ID of the credential.

  - `auth: CredentialAuth`

    The authentication method and non-secret configuration of the credential.

    - `class VaultCredentialAuthResourceMcpOauth: …`

      Public metadata for an OAuth credential; tokens and client secrets are never returned.

      - `expires_at: Optional[str]`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `mcp_server_url: str`

        The HTTPS MCP server URL authorized by this credential.

      - `refresh: Optional[VaultCredentialAuthResourceMcpOauthRefresh]`

        Public refresh metadata without refresh tokens or OAuth client secrets.

        - `client_id: str`

          The OAuth client ID used when requesting a new access token.

        - `resource: Optional[str]`

          The resource URI sent to the OAuth token endpoint during refresh, if configured.

        - `scope: Optional[str]`

          Space-separated OAuth scopes requested during refresh, if configured.

        - `token_endpoint: str`

          The HTTPS OAuth token endpoint used for refresh.

        - `token_endpoint_auth: McpOauthTokenEndpointAuth`

          How the OAuth client authenticates to the token endpoint, excluding its client secret.

          - `class McpOauthTokenEndpointAuthResourceNone: …`

            Sends the client ID without a client secret.

            - `type: Literal["none"]`

              The type of the object. Always `none`.

              - `"none"`

          - `class McpOauthTokenEndpointAuthResourceClientSecretBasic: …`

            Sends the client ID and secret using HTTP Basic authentication.

            - `type: Literal["client_secret_basic"]`

              The type of the object. Always `client_secret_basic`.

              - `"client_secret_basic"`

          - `class McpOauthTokenEndpointAuthResourceClientSecretPost: …`

            Sends the client ID and secret in the token request body.

            - `type: Literal["client_secret_post"]`

              The type of the object. Always `client_secret_post`.

              - `"client_secret_post"`

      - `type: Literal["mcp_oauth"]`

        The type of the object. Always `mcp_oauth`.

        - `"mcp_oauth"`

    - `class VaultCredentialAuthResourceStaticBearer: …`

      Metadata for a bearer-token credential, without automatic OAuth refresh.

      - `mcp_server_url: str`

        The HTTPS MCP server URL authorized by this credential.

      - `type: Literal["static_bearer"]`

        The type of the object. Always `static_bearer`.

        - `"static_bearer"`

    - `class VaultCredentialAuthResourceEnvironmentVariable: …`

      Metadata for an HTTP credential used only in OpenAI-hosted environments. Sandbox code receives a placeholder. The proxy substitutes the secret for allowed HTTPS destinations on ports 443 and 8443. The real secret is not available to sandbox code for local computation and is never returned in this resource.

      - `networking: CredentialNetworking`

        The destinations where the proxy can substitute the secret, subject to the environment network policy.

        - `class VaultCredentialNetworkingResourceUnrestricted: …`

          Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

          - `type: Literal["unrestricted"]`

            The type of the object. Always `unrestricted`.

            - `"unrestricted"`

        - `class VaultCredentialNetworkingResourceLimited: …`

          Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

          - `allowed_hosts: List[str]`

            The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

          - `type: Literal["limited"]`

            The type of the object. Always `limited`.

            - `"limited"`

      - `secret_name: str`

        The environment variable name that receives the placeholder in the sandbox.

      - `type: Literal["environment_variable"]`

        The type of the object. Always `environment_variable`.

        - `"environment_variable"`

  - `created_at: int`

    The Unix timestamp, in seconds, when the credential was created.

  - `metadata: Dict[str, str]`

    Application-defined key-value pairs associated with this credential.

  - `name: str`

    The human-readable name of the credential.

  - `object: Literal["vault.credential"]`

    The object type. Always `vault.credential`.

    - `"vault.credential"`

  - `updated_at: int`

    The Unix timestamp, in seconds, when the credential was last updated.

  - `vault_id: str`

    The ID of the vault containing this credential.

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
credential = client.beta.agents.vaults.credentials.update(
    credential_id="credential_id",
    vault_id="vault_id",
    metadata={},
)
print(credential.id)
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

- `class Credential: …`

  Metadata for a stored credential. Secret values are never returned.

  - `id: str`

    The ID of the credential.

  - `auth: CredentialAuth`

    The authentication method and non-secret configuration of the credential.

    - `class VaultCredentialAuthResourceMcpOauth: …`

      Public metadata for an OAuth credential; tokens and client secrets are never returned.

      - `expires_at: Optional[str]`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `mcp_server_url: str`

        The HTTPS MCP server URL authorized by this credential.

      - `refresh: Optional[VaultCredentialAuthResourceMcpOauthRefresh]`

        Public refresh metadata without refresh tokens or OAuth client secrets.

        - `client_id: str`

          The OAuth client ID used when requesting a new access token.

        - `resource: Optional[str]`

          The resource URI sent to the OAuth token endpoint during refresh, if configured.

        - `scope: Optional[str]`

          Space-separated OAuth scopes requested during refresh, if configured.

        - `token_endpoint: str`

          The HTTPS OAuth token endpoint used for refresh.

        - `token_endpoint_auth: McpOauthTokenEndpointAuth`

          How the OAuth client authenticates to the token endpoint, excluding its client secret.

          - `class McpOauthTokenEndpointAuthResourceNone: …`

            Sends the client ID without a client secret.

            - `type: Literal["none"]`

              The type of the object. Always `none`.

              - `"none"`

          - `class McpOauthTokenEndpointAuthResourceClientSecretBasic: …`

            Sends the client ID and secret using HTTP Basic authentication.

            - `type: Literal["client_secret_basic"]`

              The type of the object. Always `client_secret_basic`.

              - `"client_secret_basic"`

          - `class McpOauthTokenEndpointAuthResourceClientSecretPost: …`

            Sends the client ID and secret in the token request body.

            - `type: Literal["client_secret_post"]`

              The type of the object. Always `client_secret_post`.

              - `"client_secret_post"`

      - `type: Literal["mcp_oauth"]`

        The type of the object. Always `mcp_oauth`.

        - `"mcp_oauth"`

    - `class VaultCredentialAuthResourceStaticBearer: …`

      Metadata for a bearer-token credential, without automatic OAuth refresh.

      - `mcp_server_url: str`

        The HTTPS MCP server URL authorized by this credential.

      - `type: Literal["static_bearer"]`

        The type of the object. Always `static_bearer`.

        - `"static_bearer"`

    - `class VaultCredentialAuthResourceEnvironmentVariable: …`

      Metadata for an HTTP credential used only in OpenAI-hosted environments. Sandbox code receives a placeholder. The proxy substitutes the secret for allowed HTTPS destinations on ports 443 and 8443. The real secret is not available to sandbox code for local computation and is never returned in this resource.

      - `networking: CredentialNetworking`

        The destinations where the proxy can substitute the secret, subject to the environment network policy.

        - `class VaultCredentialNetworkingResourceUnrestricted: …`

          Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

          - `type: Literal["unrestricted"]`

            The type of the object. Always `unrestricted`.

            - `"unrestricted"`

        - `class VaultCredentialNetworkingResourceLimited: …`

          Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

          - `allowed_hosts: List[str]`

            The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

          - `type: Literal["limited"]`

            The type of the object. Always `limited`.

            - `"limited"`

      - `secret_name: str`

        The environment variable name that receives the placeholder in the sandbox.

      - `type: Literal["environment_variable"]`

        The type of the object. Always `environment_variable`.

        - `"environment_variable"`

  - `created_at: int`

    The Unix timestamp, in seconds, when the credential was created.

  - `metadata: Dict[str, str]`

    Application-defined key-value pairs associated with this credential.

  - `name: str`

    The human-readable name of the credential.

  - `object: Literal["vault.credential"]`

    The object type. Always `vault.credential`.

    - `"vault.credential"`

  - `updated_at: int`

    The Unix timestamp, in seconds, when the credential was last updated.

  - `vault_id: str`

    The ID of the vault containing this credential.

### Credential Auth

- `CredentialAuth`

  The authentication configuration of a vault credential, excluding secrets.

  - `class VaultCredentialAuthResourceMcpOauth: …`

    Public metadata for an OAuth credential; tokens and client secrets are never returned.

    - `expires_at: Optional[str]`

      When the OAuth access token expires, as an RFC 3339 timestamp, if known.

    - `mcp_server_url: str`

      The HTTPS MCP server URL authorized by this credential.

    - `refresh: Optional[VaultCredentialAuthResourceMcpOauthRefresh]`

      Public refresh metadata without refresh tokens or OAuth client secrets.

      - `client_id: str`

        The OAuth client ID used when requesting a new access token.

      - `resource: Optional[str]`

        The resource URI sent to the OAuth token endpoint during refresh, if configured.

      - `scope: Optional[str]`

        Space-separated OAuth scopes requested during refresh, if configured.

      - `token_endpoint: str`

        The HTTPS OAuth token endpoint used for refresh.

      - `token_endpoint_auth: McpOauthTokenEndpointAuth`

        How the OAuth client authenticates to the token endpoint, excluding its client secret.

        - `class McpOauthTokenEndpointAuthResourceNone: …`

          Sends the client ID without a client secret.

          - `type: Literal["none"]`

            The type of the object. Always `none`.

            - `"none"`

        - `class McpOauthTokenEndpointAuthResourceClientSecretBasic: …`

          Sends the client ID and secret using HTTP Basic authentication.

          - `type: Literal["client_secret_basic"]`

            The type of the object. Always `client_secret_basic`.

            - `"client_secret_basic"`

        - `class McpOauthTokenEndpointAuthResourceClientSecretPost: …`

          Sends the client ID and secret in the token request body.

          - `type: Literal["client_secret_post"]`

            The type of the object. Always `client_secret_post`.

            - `"client_secret_post"`

    - `type: Literal["mcp_oauth"]`

      The type of the object. Always `mcp_oauth`.

      - `"mcp_oauth"`

  - `class VaultCredentialAuthResourceStaticBearer: …`

    Metadata for a bearer-token credential, without automatic OAuth refresh.

    - `mcp_server_url: str`

      The HTTPS MCP server URL authorized by this credential.

    - `type: Literal["static_bearer"]`

      The type of the object. Always `static_bearer`.

      - `"static_bearer"`

  - `class VaultCredentialAuthResourceEnvironmentVariable: …`

    Metadata for an HTTP credential used only in OpenAI-hosted environments. Sandbox code receives a placeholder. The proxy substitutes the secret for allowed HTTPS destinations on ports 443 and 8443. The real secret is not available to sandbox code for local computation and is never returned in this resource.

    - `networking: CredentialNetworking`

      The destinations where the proxy can substitute the secret, subject to the environment network policy.

      - `class VaultCredentialNetworkingResourceUnrestricted: …`

        Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

        - `type: Literal["unrestricted"]`

          The type of the object. Always `unrestricted`.

          - `"unrestricted"`

      - `class VaultCredentialNetworkingResourceLimited: …`

        Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

        - `allowed_hosts: List[str]`

          The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

        - `type: Literal["limited"]`

          The type of the object. Always `limited`.

          - `"limited"`

    - `secret_name: str`

      The environment variable name that receives the placeholder in the sandbox.

    - `type: Literal["environment_variable"]`

      The type of the object. Always `environment_variable`.

      - `"environment_variable"`

### Credential Auth Create Param

- `CredentialAuthCreateParam`

  Authentication credentials for an MCP server or an OpenAI-hosted environment.

  - `class CreateVaultCredentialAuthParamMcpOauth: …`

    An OAuth credential for an HTTPS MCP destination.

    - `access_token: str`

      A write-only OAuth access token; never returned by credential resources.

    - `mcp_server_url: str`

      The HTTPS MCP server URL authorized by this credential.

    - `type: Literal["mcp_oauth"]`

      The type of the object. Always `mcp_oauth`.

      - `"mcp_oauth"`

    - `expires_at: Optional[str]`

      When the OAuth access token expires, as an RFC 3339 timestamp, if known.

    - `refresh: Optional[CreateVaultCredentialAuthParamMcpOauthRefresh]`

      Optional refresh configuration for an HTTPS OAuth token endpoint.

      - `client_id: str`

        The OAuth client ID used when requesting a new access token.

      - `refresh_token: str`

        The refresh token to store. This secret is never returned in credential resources.

      - `token_endpoint: str`

        The HTTPS OAuth token endpoint used to exchange the refresh token for a new access token.

      - `token_endpoint_auth: McpOauthTokenEndpointAuthCreateParam`

        How the OAuth client authenticates to the token endpoint.

        - `class CreateMcpOauthTokenEndpointAuthParamNone: …`

          Sends the client ID without a client secret.

          - `type: Literal["none"]`

            The type of the object. Always `none`.

            - `"none"`

        - `class CreateMcpOauthTokenEndpointAuthParamClientSecretBasic: …`

          Sends the client ID and secret using HTTP Basic authentication.

          - `client_secret: str`

            The OAuth client secret to store. Never returned in credential resources.

          - `type: Literal["client_secret_basic"]`

            The type of the object. Always `client_secret_basic`.

            - `"client_secret_basic"`

        - `class CreateMcpOauthTokenEndpointAuthParamClientSecretPost: …`

          Sends the client ID and secret in the token request body.

          - `client_secret: str`

            The OAuth client secret to store. Never returned in credential resources.

          - `type: Literal["client_secret_post"]`

            The type of the object. Always `client_secret_post`.

            - `"client_secret_post"`

      - `resource: Optional[str]`

        The resource URI to send to the OAuth token endpoint during refresh, if required.

      - `scope: Optional[str]`

        Space-separated OAuth scopes to request during refresh, if required.

  - `class CreateVaultCredentialAuthParamStaticBearer: …`

    A bearer token for an MCP server, without automatic OAuth refresh.

    - `token: str`

      The bearer token to store. This secret is never returned in credential resources.

    - `mcp_server_url: str`

      The HTTPS MCP server URL authorized by this credential.

    - `type: Literal["static_bearer"]`

      The type of the object. Always `static_bearer`.

      - `"static_bearer"`

  - `class CreateVaultCredentialAuthParamEnvironmentVariable: …`

    An HTTP credential for OpenAI-hosted environments only. The sandbox receives an environment variable containing a placeholder, not the secret. Use the placeholder unchanged in outgoing requests. The egress proxy replaces the placeholder with the secret for allowed HTTPS destinations on ports 443 and 8443. Sandbox code cannot read the real secret or use it for local computation, such as signing a request.

    - `networking: CredentialNetworkingParam`

      The destinations where the proxy can substitute this secret. The environment network policy must also allow them.

      - `class VaultCredentialNetworkingParamUnrestricted: …`

        Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

        - `type: Literal["unrestricted"]`

          The type of the object. Always `unrestricted`.

          - `"unrestricted"`

      - `class VaultCredentialNetworkingParamLimited: …`

        Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

        - `allowed_hosts: List[str]`

          The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

        - `type: Literal["limited"]`

          The type of the object. Always `limited`.

          - `"limited"`

    - `secret_name: str`

      The environment variable name that receives the placeholder, such as `SERVICE_API_KEY`. Use ASCII letters, digits, and underscores, starting with a letter or underscore. Names starting with `CODEX_` and managed proxy or certificate variable names are reserved.

    - `secret_value: str`

      The write-only secret to store. Never returned in credential resources or supplied directly to sandbox code. Must be nonempty and must not contain carriage returns, newlines, or NUL bytes.

    - `type: Literal["environment_variable"]`

      The type of the object. Always `environment_variable`.

      - `"environment_variable"`

### Credential Auth Rotate Param

- `CredentialAuthRotateParam`

  Updates to a vault credential without changing its authentication method or destination configuration.

  - `class RotateVaultCredentialAuthParamMcpOauth: …`

    Rotate an OAuth credential for an HTTPS MCP destination.

    - `type: Literal["mcp_oauth"]`

      The type of the object. Always `mcp_oauth`.

      - `"mcp_oauth"`

    - `access_token: Optional[str]`

      A write-only replacement OAuth access token.

    - `expires_at: Optional[str]`

      The replacement expiry as an RFC 3339 timestamp, or `null` to clear it. Omitting this field preserves the expiry unless a new access token is supplied, in which case the expiry is cleared.

    - `refresh: Optional[RotateVaultCredentialAuthParamMcpOauthRefresh]`

      Optional write-only refresh-token and client-secret updates.

      - `refresh_token: Optional[str]`

        The replacement refresh token. Omit or pass `null` to keep the stored token. This secret is never returned in resources.

      - `scope: Optional[str]`

        Replacement space-separated OAuth scopes for refresh requests. Omit to keep the scopes, or pass `null` to stop sending a scope parameter.

      - `token_endpoint_auth: Optional[McpOauthTokenEndpointAuthRotateParam]`

        Client-secret updates for the existing token endpoint authentication method.

        - `class RotateMcpOauthTokenEndpointAuthParamClientSecretBasic: …`

          Updates credentials sent using HTTP Basic authentication.

          - `type: Literal["client_secret_basic"]`

            The type of the object. Always `client_secret_basic`.

            - `"client_secret_basic"`

          - `client_secret: Optional[str]`

            The replacement OAuth client secret. Omit or pass `null` to keep the stored secret. This secret is never returned in resources.

        - `class RotateMcpOauthTokenEndpointAuthParamClientSecretPost: …`

          Updates credentials sent in the token request body.

          - `type: Literal["client_secret_post"]`

            The type of the object. Always `client_secret_post`.

            - `"client_secret_post"`

          - `client_secret: Optional[str]`

            The replacement OAuth client secret. Omit or pass `null` to keep the stored secret. This secret is never returned in resources.

  - `class RotateVaultCredentialAuthParamStaticBearer: …`

    Replace the bearer token for the credential's MCP server.

    - `token: str`

      The replacement bearer token. This secret is never returned in credential resources.

    - `type: Literal["static_bearer"]`

      The type of the object. Always `static_bearer`.

      - `"static_bearer"`

  - `class RotateVaultCredentialAuthParamEnvironmentVariable: …`

    Replace the secret for an OpenAI-hosted environment credential. The environment variable name and networking configuration remain unchanged.

    - `secret_value: str`

      The write-only replacement secret. Never returned in credential resources or supplied directly to sandbox code. Must be nonempty and must not contain carriage returns, newlines, or NUL bytes.

    - `type: Literal["environment_variable"]`

      The type of the object. Always `environment_variable`.

      - `"environment_variable"`

### Credential Deleted

- `class CredentialDeleted: …`

  Confirmation that a vault credential was deleted.

  - `id: str`

    The ID of the deleted credential.

  - `deleted: bool`

    Whether the resource was deleted. Always `true`.

  - `object: Literal["vault.credential.deleted"]`

    The object type. Always `vault.credential.deleted`.

    - `"vault.credential.deleted"`

### Credential Networking

- `CredentialNetworking`

  Destination permissions for an environment-variable credential. These do not grant network access to the environment.

  - `class VaultCredentialNetworkingResourceUnrestricted: …`

    Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

    - `type: Literal["unrestricted"]`

      The type of the object. Always `unrestricted`.

      - `"unrestricted"`

  - `class VaultCredentialNetworkingResourceLimited: …`

    Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

    - `allowed_hosts: List[str]`

      The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

    - `type: Literal["limited"]`

      The type of the object. Always `limited`.

      - `"limited"`

### Credential Networking Param

- `CredentialNetworkingParam`

  Destination permissions for an environment-variable credential. These do not grant network access to the environment.

  - `class VaultCredentialNetworkingParamUnrestricted: …`

    Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

    - `type: Literal["unrestricted"]`

      The type of the object. Always `unrestricted`.

      - `"unrestricted"`

  - `class VaultCredentialNetworkingParamLimited: …`

    Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

    - `allowed_hosts: List[str]`

      The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

    - `type: Literal["limited"]`

      The type of the object. Always `limited`.

      - `"limited"`

### Mcp OAuth Token Endpoint Auth

- `McpOauthTokenEndpointAuth`

  The client authentication method used for OAuth token refresh.

  - `class McpOauthTokenEndpointAuthResourceNone: …`

    Sends the client ID without a client secret.

    - `type: Literal["none"]`

      The type of the object. Always `none`.

      - `"none"`

  - `class McpOauthTokenEndpointAuthResourceClientSecretBasic: …`

    Sends the client ID and secret using HTTP Basic authentication.

    - `type: Literal["client_secret_basic"]`

      The type of the object. Always `client_secret_basic`.

      - `"client_secret_basic"`

  - `class McpOauthTokenEndpointAuthResourceClientSecretPost: …`

    Sends the client ID and secret in the token request body.

    - `type: Literal["client_secret_post"]`

      The type of the object. Always `client_secret_post`.

      - `"client_secret_post"`

### Mcp OAuth Token Endpoint Auth Create Param

- `McpOauthTokenEndpointAuthCreateParam`

  Client authentication credentials for OAuth token refresh.

  - `class CreateMcpOauthTokenEndpointAuthParamNone: …`

    Sends the client ID without a client secret.

    - `type: Literal["none"]`

      The type of the object. Always `none`.

      - `"none"`

  - `class CreateMcpOauthTokenEndpointAuthParamClientSecretBasic: …`

    Sends the client ID and secret using HTTP Basic authentication.

    - `client_secret: str`

      The OAuth client secret to store. Never returned in credential resources.

    - `type: Literal["client_secret_basic"]`

      The type of the object. Always `client_secret_basic`.

      - `"client_secret_basic"`

  - `class CreateMcpOauthTokenEndpointAuthParamClientSecretPost: …`

    Sends the client ID and secret in the token request body.

    - `client_secret: str`

      The OAuth client secret to store. Never returned in credential resources.

    - `type: Literal["client_secret_post"]`

      The type of the object. Always `client_secret_post`.

      - `"client_secret_post"`

### Mcp OAuth Token Endpoint Auth Rotate Param

- `McpOauthTokenEndpointAuthRotateParam`

  Client-secret updates that preserve the credential's OAuth authentication method.

  - `class RotateMcpOauthTokenEndpointAuthParamClientSecretBasic: …`

    Updates credentials sent using HTTP Basic authentication.

    - `type: Literal["client_secret_basic"]`

      The type of the object. Always `client_secret_basic`.

      - `"client_secret_basic"`

    - `client_secret: Optional[str]`

      The replacement OAuth client secret. Omit or pass `null` to keep the stored secret. This secret is never returned in resources.

  - `class RotateMcpOauthTokenEndpointAuthParamClientSecretPost: …`

    Updates credentials sent in the token request body.

    - `type: Literal["client_secret_post"]`

      The type of the object. Always `client_secret_post`.

      - `"client_secret_post"`

    - `client_secret: Optional[str]`

      The replacement OAuth client secret. Omit or pass `null` to keep the stored secret. This secret is never returned in resources.
