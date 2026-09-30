<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/agents/subresources/vaults/subresources/credentials/methods/list/ -->

## List vault credentials

`client.beta.agents.vaults.credentials.list(stringvaultID, CredentialListParamsquery?, RequestOptionsoptions?): CursorPage<Credential>`

**get** `/vaults/{vault_id}/credentials`

Lists a vault's credentials using ID-based pagination without returning secret values. See [vaults](/api/docs/guides/agents-api/tools/vaults).

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

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const credential of client.beta.agents.vaults.credentials.list('vault_id')) {
  console.log(credential.id);

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
        "type": "mcp_oauth"
      "metadata": {
        "foo": "string"
      "object": "vault.credential",
      "updated_at": 0,
      "vault_id": "vault_id"
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
