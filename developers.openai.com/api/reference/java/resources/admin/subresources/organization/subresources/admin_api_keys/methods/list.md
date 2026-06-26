<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/admin_api_keys/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Admin API Keys](/api/reference/java/resources/admin/subresources/organization/subresources/admin_api_keys)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List all organization and project API keys.

AdminApiKeyListPage admin().organization().adminApiKeys().list(AdminApiKeyListParamsparams = AdminApiKeyListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/admin\_api\_keys

List organization API keys

##### ParametersExpand Collapse

AdminApiKeyListParams params

Optional<String> after

Return keys with IDs that come after this ID in the pagination order.

Optional<Long> limit

Maximum number of keys to return.

Optional<[Order](/api/reference/java/resources/admin/subresources/organization/subresources/admin_api_keys/methods/list#(resource)%20admin.organization.admin_api_keys%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))> order

Order results by creation time, ascending or descending.

ASC("asc")

DESC("desc")

##### ReturnsExpand Collapse

class AdminApiKey:

Represents an individual Admin API key in an org.

String id

The identifier, which can be referenced in API endpoints

long createdAt

The Unix timestamp (in seconds) of when the API key was created

formatunixtime

Optional<Long> expiresAt

The Unix timestamp (in seconds) of when the API key expires

formatunixtime

JsonValue; object\_ "organization.admin\_api\_key"constant"organization.admin\_api\_key"constant

The object type, which is always `organization.admin_api_key`

Owner owner

Optional<String> id

The identifier, which can be referenced in API endpoints

Optional<Long> createdAt

The Unix timestamp (in seconds) of when the user was created

formatunixtime

Optional<String> name

The name of the user

Optional<String> object\_

The object type, which is always organization.user

Optional<String> role

Always `owner`

Optional<String> type

Always `user`

String redactedValue

The redacted value of the API key

Optional<Long> lastUsedAt

The Unix timestamp (in seconds) of when the API key was last used

formatunixtime

Optional<String> name

The name of the API key

### List all organization and project API keys.

Java

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.admin.organization.adminapikeys.AdminApiKeyListPage;
import com.openai.models.admin.organization.adminapikeys.AdminApiKeyListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        AdminApiKeyListPage page = client.admin().organization().adminApiKeys().list();

  "object": "list",
  "data": [
      "object": "organization.admin_api_key",
      "id": "key_abc",
      "name": "Main Admin Key",
      "redacted_value": "sk-admin...def",
      "created_at": 1711471533,
      "expires_at": 1714063533,
      "last_used_at": 1711471534,
      "owner": {
        "type": "service_account",
        "object": "organization.service_account",
        "id": "sa_456",
        "name": "My Service Account",
        "created_at": 1711471533,
        "role": "member"
  ],
  "first_id": "key_abc",
  "last_id": "key_abc",
  "has_more": false

##### Returns Examples

  "object": "list",
  "data": [
      "object": "organization.admin_api_key",
      "id": "key_abc",
      "name": "Main Admin Key",
      "redacted_value": "sk-admin...def",
      "created_at": 1711471533,
      "expires_at": 1714063533,
      "last_used_at": 1711471534,
      "owner": {
        "type": "service_account",
        "object": "organization.service_account",
        "id": "sa_456",
        "name": "My Service Account",
        "created_at": 1711471533,
        "role": "member"
  ],
  "first_id": "key_abc",
  "last_id": "key_abc",
  "has_more": false
