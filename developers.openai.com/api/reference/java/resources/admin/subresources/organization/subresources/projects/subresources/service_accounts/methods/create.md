<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Projects](/api/reference/java/resources/admin/subresources/organization/subresources/projects)

[Service Accounts](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create project service account

[ServiceAccountCreateResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20ServiceAccountCreateResponse%20%3E%20(schema)) admin().organization().projects().serviceAccounts().create(ServiceAccountCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/service\_accounts

Creates a new service account in the project. This also returns an unredacted API key for the service account.

##### ParametersExpand Collapse

ServiceAccountCreateParams params

Optional<String> projectId

String name

The name of the service account being created.

##### ReturnsExpand Collapse

class ServiceAccountCreateResponse:

String id

Optional<ApiKey> apiKey

String id

long createdAt

formatunixtime

String name

JsonValue; object\_ "organization.project.service\_account.api\_key"constant"organization.project.service\_account.api\_key"constant

The object type, which is always `organization.project.service_account.api_key`

String value

long createdAt

formatunixtime

String name

JsonValue; object\_ "organization.project.service\_account"constant"organization.project.service\_account"constant

JsonValue; role "member"constant"member"constant

Service accounts can only have one role of type `member`

### Create project service account

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
import com.openai.models.admin.organization.projects.serviceaccounts.ServiceAccountCreateParams;
import com.openai.models.admin.organization.projects.serviceaccounts.ServiceAccountCreateResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ServiceAccountCreateParams params = ServiceAccountCreateParams.builder()
            .projectId("project_id")
            .name("name")
            .build();
        ServiceAccountCreateResponse serviceAccount = client.admin().organization().projects().serviceAccounts().create(params);

    "object": "organization.project.service_account",
    "id": "svc_acct_abc",
    "name": "Production App",
    "role": "member",
    "created_at": 1711471533,
    "api_key": {
        "object": "organization.project.service_account.api_key",
        "value": "sk-abcdefghijklmnop123",
        "name": "Secret Key",
        "created_at": 1711471533,
        "id": "key_abc"

##### Returns Examples

    "object": "organization.project.service_account",
    "id": "svc_acct_abc",
    "name": "Production App",
    "role": "member",
    "created_at": 1711471533,
    "api_key": {
        "object": "organization.project.service_account.api_key",
        "value": "sk-abcdefghijklmnop123",
        "name": "Secret Key",
        "created_at": 1711471533,
        "id": "key_abc"
