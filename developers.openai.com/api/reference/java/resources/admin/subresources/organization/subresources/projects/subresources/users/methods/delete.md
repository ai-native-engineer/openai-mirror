<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Projects](/api/reference/java/resources/admin/subresources/organization/subresources/projects)

[Users](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/users)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete project user

[UserDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20UserDeleteResponse%20%3E%20(schema)) admin().organization().projects().users().delete(UserDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/projects/{project\_id}/users/{user\_id}

Deletes a user from the project.

Returns confirmation of project user deletion, or an error if the project is
archived (archived projects have no users).

##### ParametersExpand Collapse

UserDeleteParams params

String projectId

Optional<String> userId

##### ReturnsExpand Collapse

class UserDeleteResponse:

String id

boolean deleted

JsonValue; object\_ "organization.project.user.deleted"constant"organization.project.user.deleted"constant

### Delete project user

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
import com.openai.models.admin.organization.projects.users.UserDeleteParams;
import com.openai.models.admin.organization.projects.users.UserDeleteResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        UserDeleteParams params = UserDeleteParams.builder()
            .projectId("project_id")
            .userId("user_id")
            .build();
        UserDeleteResponse user = client.admin().organization().projects().users().delete(params);

    "object": "organization.project.user.deleted",
    "id": "user_abc",
    "deleted": true

##### Returns Examples

    "object": "organization.project.user.deleted",
    "id": "user_abc",
    "deleted": true
