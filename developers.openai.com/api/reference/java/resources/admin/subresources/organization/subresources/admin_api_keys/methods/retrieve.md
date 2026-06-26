<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/admin_api_keys/methods/retrieve/ -->

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

# Retrieve admin API key

[AdminApiKey](/api/reference/java/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)) admin().organization().adminApiKeys().retrieve(AdminApiKeyRetrieveParamsparams = AdminApiKeyRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/admin\_api\_keys/{key\_id}

Retrieve a single organization API key

##### ParametersExpand Collapse

AdminApiKeyRetrieveParams params

Optional<String> keyId

The ID of the API key.

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

### Retrieve admin API key

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
import com.openai.models.admin.organization.adminapikeys.AdminApiKey;
import com.openai.models.admin.organization.adminapikeys.AdminApiKeyRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        AdminApiKey adminApiKey = client.admin().organization().adminApiKeys().retrieve("key_id");

  "object": "organization.admin_api_key",
  "id": "key_abc",
  "name": "Main Admin Key",
  "redacted_value": "sk-admin...xyz",
  "created_at": 1711471533,
  "last_used_at": 1711471534,
  "owner": {
    "type": "user",
    "object": "organization.user",
    "id": "user_123",
    "name": "John Doe",
    "created_at": 1711471533,
    "role": "owner"

##### Returns Examples

  "object": "organization.admin_api_key",
  "id": "key_abc",
  "name": "Main Admin Key",
  "redacted_value": "sk-admin...xyz",
  "created_at": 1711471533,
  "last_used_at": 1711471534,
  "owner": {
    "type": "user",
    "object": "organization.user",
    "id": "user_123",
    "name": "John Doe",
    "created_at": 1711471533,
    "role": "owner"
