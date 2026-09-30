<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/agents/subresources/vaults/subresources/credentials/methods/list/ -->

## List vault credentials

`beta.agents.vaults.credentials.list(vault_id, **kwargs) -> CursorPage<Credential>`

**get** `/vaults/{vault_id}/credentials`

Lists a vault's credentials using ID-based pagination without returning secret values. See [vaults](/api/docs/guides/agents-api/tools/vaults).

- `vault_id: String`

- `after: String`

  Return resources after this resource ID in the selected order.

- `limit: Integer`

  The maximum number of resources to return. Defaults to 20. Values are clamped between 1 and 100.

- `order: :asc | :desc`

  Sort order by the `created_at` timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `desc`.

  - `:asc`

    Returns resources in ascending order.

  - `:desc`

    Returns resources in descending order.

- `status: VaultStatusFilter`

  Filter by one status or a list, such as `status=active` or `status[]=active&status[]=archived`. Both statuses are included by default.

  - `VaultStatus = :active | :archived`

    Whether a vault or credential is active or archived.

    - `:active`

    - `:archived`

  - `UnionMember1 = Array[VaultStatus]`

    - `:active`

    - `:archived`

- `class Credential`

  Metadata for a stored credential. Secret values are never returned.

  - `id: String`

    The ID of the credential.

  - `auth: CredentialAuth`

    The authentication method and non-secret configuration of the credential.

    - `class McpOauth`

      Public metadata for an OAuth credential; tokens and client secrets are never returned.

      - `expires_at: String`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `mcp_server_url: String`

        The HTTPS MCP server URL authorized by this credential.

      - `refresh: Refresh{ client_id, resource, scope, 2 more}`

        Public refresh metadata without refresh tokens or OAuth client secrets.

        - `client_id: String`

          The OAuth client ID used when requesting a new access token.

        - `resource: String`

          The resource URI sent to the OAuth token endpoint during refresh, if configured.

        - `scope: String`

          Space-separated OAuth scopes requested during refresh, if configured.

        - `token_endpoint: String`

          The HTTPS OAuth token endpoint used for refresh.

        - `token_endpoint_auth: McpOauthTokenEndpointAuth`

          How the OAuth client authenticates to the token endpoint, excluding its client secret.

          - `class None`

            Sends the client ID without a client secret.

            - `type: :none`

              The type of the object. Always `none`.

              - `:none`

          - `class ClientSecretBasic`

            Sends the client ID and secret using HTTP Basic authentication.

            - `type: :client_secret_basic`

              The type of the object. Always `client_secret_basic`.

              - `:client_secret_basic`

          - `class ClientSecretPost`

            Sends the client ID and secret in the token request body.

            - `type: :client_secret_post`

              The type of the object. Always `client_secret_post`.

              - `:client_secret_post`

      - `type: :mcp_oauth`

        The type of the object. Always `mcp_oauth`.

        - `:mcp_oauth`

    - `class StaticBearer`

      Metadata for a bearer-token credential, without automatic OAuth refresh.

      - `mcp_server_url: String`

        The HTTPS MCP server URL authorized by this credential.

      - `type: :static_bearer`

        The type of the object. Always `static_bearer`.

        - `:static_bearer`

    - `class EnvironmentVariable`

      Metadata for an HTTP credential used only in OpenAI-hosted environments. Sandbox code receives a placeholder. The proxy substitutes the secret for allowed HTTPS destinations on ports 443 and 8443. The real secret is not available to sandbox code for local computation and is never returned in this resource.

      - `networking: CredentialNetworking`

        The destinations where the proxy can substitute the secret, subject to the environment network policy.

        - `class Unrestricted`

          Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

          - `type: :unrestricted`

            The type of the object. Always `unrestricted`.

            - `:unrestricted`

        - `class Limited`

          Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

          - `allowed_hosts: Array[String]`

            The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

          - `type: :limited`

            The type of the object. Always `limited`.

            - `:limited`

      - `secret_name: String`

        The environment variable name that receives the placeholder in the sandbox.

      - `type: :environment_variable`

        The type of the object. Always `environment_variable`.

        - `:environment_variable`

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the credential was created.

  - `metadata: Hash[Symbol, String]`

    Application-defined key-value pairs associated with this credential.

  - `name: String`

    The human-readable name of the credential.

  - `object: :"vault.credential"`

    The object type. Always `vault.credential`.

    - `:"vault.credential"`

  - `updated_at: Integer`

    The Unix timestamp, in seconds, when the credential was last updated.

  - `vault_id: String`

    The ID of the vault containing this credential.

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.beta.agents.vaults.credentials.list("vault_id")

puts(page)

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
