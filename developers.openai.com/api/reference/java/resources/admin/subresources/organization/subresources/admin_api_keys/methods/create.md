<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/admin_api_keys/methods/create/ -->

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

# Create admin API key

[AdminApiKeyCreateResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20AdminApiKeyCreateResponse%20%3E%20(schema)) admin().organization().adminApiKeys().create(AdminApiKeyCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/admin\_api\_keys

Create an organization admin API key

##### ParametersExpand Collapse

AdminApiKeyCreateParams params

String name

Optional<Long> expiresInSeconds

The number of seconds until the API key expires. Omit this field for a key that does not expire.

minimum1

maximum31536000

##### ReturnsExpand Collapse

class AdminApiKeyCreateResponse:

Represents an individual Admin API key in an org.

String value

The value of the API key. Only shown on create.

### Create admin API key

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
import com.openai.models.admin.organization.adminapikeys.AdminApiKeyCreateParams;
import com.openai.models.admin.organization.adminapikeys.AdminApiKeyCreateResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        AdminApiKeyCreateParams params = AdminApiKeyCreateParams.builder()
            .name("New Admin Key")
            .build();
        AdminApiKeyCreateResponse adminApiKey = client.admin().organization().adminApiKeys().create(params);

  "object": "organization.admin_api_key",
  "id": "key_xyz",
  "name": "New Admin Key",
  "redacted_value": "sk-admin...xyz",
  "created_at": 1711471533,
  "expires_at": 1714063533,
  "last_used_at": 1711471534,
  "owner": {
    "type": "user",
    "object": "organization.user",
    "id": "user_123",
    "name": "John Doe",
    "created_at": 1711471533,
    "role": "owner"
  "value": "sk-admin-1234abcd"

##### Returns Examples

  "object": "organization.admin_api_key",
  "id": "key_xyz",
  "name": "New Admin Key",
  "redacted_value": "sk-admin...xyz",
  "created_at": 1711471533,
  "expires_at": 1714063533,
  "last_used_at": 1711471534,
  "owner": {
    "type": "user",
    "object": "organization.user",
    "id": "user_123",
    "name": "John Doe",
    "created_at": 1711471533,
    "role": "owner"
  "value": "sk-admin-1234abcd"
