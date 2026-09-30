<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/agents/subresources/vaults/subresources/credentials/methods/create/ -->

## Create a vault credential

`beta.agents.vaults.credentials.create(strvault_id, CredentialCreateParams**kwargs)  -> Credential`

**post** `/vaults/{vault_id}/credentials`

Creates a vault credential. Secret values are write-only and are never returned. See [vaults](/api/docs/guides/agents-api/tools/vaults).

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

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
credential = client.beta.agents.vaults.credentials.create(
    vault_id="vault_id",
    auth={
        "access_token": "access_token",
        "mcp_server_url": "mcp_server_url",
        "type": "mcp_oauth",
    name="x",
print(credential.id)

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
