<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/delete/ -->

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

# Delete project service account

[ServiceAccountDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20ServiceAccountDeleteResponse%20%3E%20(schema)) admin().organization().projects().serviceAccounts().delete(ServiceAccountDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

Deletes a service account from the project.

Returns confirmation of service account deletion, or an error if the project
is archived (archived projects have no service accounts).

##### ParametersExpand Collapse

ServiceAccountDeleteParams params

String projectId

Optional<String> serviceAccountId

##### ReturnsExpand Collapse

class ServiceAccountDeleteResponse:

String id

boolean deleted

JsonValue; object\_ "organization.project.service\_account.deleted"constant"organization.project.service\_account.deleted"constant

### Delete project service account

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
import com.openai.models.admin.organization.projects.serviceaccounts.ServiceAccountDeleteParams;
import com.openai.models.admin.organization.projects.serviceaccounts.ServiceAccountDeleteResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ServiceAccountDeleteParams params = ServiceAccountDeleteParams.builder()
            .projectId("project_id")
            .serviceAccountId("service_account_id")
            .build();
        ServiceAccountDeleteResponse serviceAccount = client.admin().organization().projects().serviceAccounts().delete(params);

    "object": "organization.project.service_account.deleted",
    "id": "svc_acct_abc",
    "deleted": true

##### Returns Examples

    "object": "organization.project.service_account.deleted",
    "id": "svc_acct_abc",
    "deleted": true
