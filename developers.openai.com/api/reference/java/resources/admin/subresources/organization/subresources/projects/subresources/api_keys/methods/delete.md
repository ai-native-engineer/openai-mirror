<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Projects](/api/reference/java/resources/admin/subresources/organization/subresources/projects)

[API Keys](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/api_keys)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete project API key

[ApiKeyDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20ApiKeyDeleteResponse%20%3E%20(schema)) admin().organization().projects().apiKeys().delete(ApiKeyDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/projects/{project\_id}/api\_keys/{api\_key\_id}

Deletes an API key from the project.

Returns confirmation of the key deletion, or an error if the key belonged to
a service account.

##### ParametersExpand Collapse

ApiKeyDeleteParams params

String projectId

Optional<String> apiKeyId

##### ReturnsExpand Collapse

class ApiKeyDeleteResponse:

String id

boolean deleted

JsonValue; object\_ "organization.project.api\_key.deleted"constant"organization.project.api\_key.deleted"constant

### Delete project API key

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
import com.openai.models.admin.organization.projects.apikeys.ApiKeyDeleteParams;
import com.openai.models.admin.organization.projects.apikeys.ApiKeyDeleteResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ApiKeyDeleteParams params = ApiKeyDeleteParams.builder()
            .projectId("project_id")
            .apiKeyId("api_key_id")
            .build();
        ApiKeyDeleteResponse apiKey = client.admin().organization().projects().apiKeys().delete(params);

    "object": "organization.project.api_key.deleted",
    "id": "key_abc",
    "deleted": true

##### Returns Examples

    "object": "organization.project.api_key.deleted",
    "id": "key_abc",
    "deleted": true
