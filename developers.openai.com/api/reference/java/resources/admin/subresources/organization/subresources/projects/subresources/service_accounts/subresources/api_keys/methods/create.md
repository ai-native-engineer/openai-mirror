<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/subresources/api_keys/methods/create/ -->

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Projects](/api/reference/java/resources/admin/subresources/organization/subresources/projects)

[Service Accounts](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts)

[API Keys](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/subresources/api_keys)

# Create project service account API key

[ApiKeyCreateResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.service_accounts.api_keys%20%3E%20(model)%20ApiKeyCreateResponse%20%3E%20(schema)) admin().organization().projects().serviceAccounts().apiKeys().create(ApiKeyCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}/api\_keys

Creates an API key for a service account in the project.

##### ParametersExpand Collapse

ApiKeyCreateParams params

String projectId

Optional<String> serviceAccountId

Optional<String> name

API key name.

Optional<List<String>> scopes

API key scopes.

##### ReturnsExpand Collapse

class ApiKeyCreateResponse:

String id

long createdAt

formatunixtime

String name

JsonValue; object\_ "organization.project.service\_account.api\_key"constant"organization.project.service\_account.api\_key"constant

The object type, which is always `organization.project.service_account.api_key`

String value

### Create project service account API key

Java

package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.admin.organization.projects.serviceaccounts.apikeys.ApiKeyCreateParams;
import com.openai.models.admin.organization.projects.serviceaccounts.apikeys.ApiKeyCreateResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ApiKeyCreateParams params = ApiKeyCreateParams.builder()
            .projectId("project_id")
            .serviceAccountId("service_account_id")
            .build();
        ApiKeyCreateResponse apiKey = client.admin().organization().projects().serviceAccounts().apiKeys().create(params);

    "object": "organization.project.service_account.api_key",
    "value": "sk-abcdefghijklmnop123",
    "name": "Production App",
    "created_at": 1711471533,
    "id": "key_abc"

    "object": "organization.project.service_account.api_key",
    "value": "sk-abcdefghijklmnop123",
    "name": "Production App",
    "created_at": 1711471533,
    "id": "key_abc"
