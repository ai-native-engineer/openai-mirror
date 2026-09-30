<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/agents/subresources/vaults/subresources/credentials/methods/update/ -->

## Update a vault credential

`beta.agents.vaults.credentials.update(strcredential_id, CredentialUpdateParams**kwargs)  -> Credential`

**post** `/vaults/{vault_id}/credentials/{credential_id}`

Updates credential metadata or rotates its write-only secret. See [vaults](/api/docs/guides/agents-api/tools/vaults).

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
credential = client.beta.agents.vaults.credentials.update(
    credential_id="credential_id",
    vault_id="vault_id",
    metadata={},
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
