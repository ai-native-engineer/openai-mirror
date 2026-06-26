<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/admin_api_keys/methods/delete/ -->

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

# Delete admin API key

[AdminApiKeyDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20AdminApiKeyDeleteResponse%20%3E%20(schema)) admin().organization().adminApiKeys().delete(AdminApiKeyDeleteParamsparams = AdminApiKeyDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/admin\_api\_keys/{key\_id}

Delete an organization admin API key

##### ParametersExpand Collapse

AdminApiKeyDeleteParams params

Optional<String> keyId

The ID of the API key to be deleted.

##### ReturnsExpand Collapse

class AdminApiKeyDeleteResponse:

String id

boolean deleted

JsonValue; object\_ "organization.admin\_api\_key.deleted"constant"organization.admin\_api\_key.deleted"constant

### Delete admin API key

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
import com.openai.models.admin.organization.adminapikeys.AdminApiKeyDeleteParams;
import com.openai.models.admin.organization.adminapikeys.AdminApiKeyDeleteResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        AdminApiKeyDeleteResponse adminApiKey = client.admin().organization().adminApiKeys().delete("key_id");

  "id": "key_abc",
  "object": "organization.admin_api_key.deleted",
  "deleted": true

##### Returns Examples

  "id": "key_abc",
  "object": "organization.admin_api_key.deleted",
  "deleted": true
