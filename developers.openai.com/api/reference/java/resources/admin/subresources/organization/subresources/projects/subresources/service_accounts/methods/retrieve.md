<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/retrieve/ -->

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

# Retrieve project service account

[ProjectServiceAccount](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)) admin().organization().projects().serviceAccounts().retrieve(ServiceAccountRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

Retrieves a service account in the project.

##### ParametersExpand Collapse

ServiceAccountRetrieveParams params

String projectId

Optional<String> serviceAccountId

##### ReturnsExpand Collapse

class ProjectServiceAccount:

Represents an individual service account in a project.

String id

The identifier, which can be referenced in API endpoints

long createdAt

The Unix timestamp (in seconds) of when the service account was created

formatunixtime

String name

The name of the service account

JsonValue; object\_ "organization.project.service\_account"constant"organization.project.service\_account"constant

The object type, which is always `organization.project.service_account`

Role role

`owner` or `member`

One of the following:

OWNER("owner")

MEMBER("member")

### Retrieve project service account

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
import com.openai.models.admin.organization.projects.serviceaccounts.ProjectServiceAccount;
import com.openai.models.admin.organization.projects.serviceaccounts.ServiceAccountRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ServiceAccountRetrieveParams params = ServiceAccountRetrieveParams.builder()
            .projectId("project_id")
            .serviceAccountId("service_account_id")
            .build();
        ProjectServiceAccount projectServiceAccount = client.admin().organization().projects().serviceAccounts().retrieve(params);

    "object": "organization.project.service_account",
    "id": "svc_acct_abc",
    "name": "Service Account",
    "role": "owner",
    "created_at": 1711471533

##### Returns Examples

    "object": "organization.project.service_account",
    "id": "svc_acct_abc",
    "name": "Service Account",
    "role": "owner",
    "created_at": 1711471533
