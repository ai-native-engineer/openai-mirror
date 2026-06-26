<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/create/ -->

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

# Create project user

[ProjectUser](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema)) admin().organization().projects().users().create(UserCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/users

Adds a user to the project. Users must already be members of the organization to be added to a project.

##### ParametersExpand Collapse

UserCreateParams params

Optional<String> projectId

String role

`owner` or `member`

Optional<String> email

Email of the user to add.

Optional<String> userId

The ID of the user.

##### ReturnsExpand Collapse

class ProjectUser:

Represents an individual user in a project.

String id

The identifier, which can be referenced in API endpoints

long addedAt

The Unix timestamp (in seconds) of when the project was added.

formatunixtime

JsonValue; object\_ "organization.project.user"constant"organization.project.user"constant

The object type, which is always `organization.project.user`

String role

`owner` or `member`

Optional<String> email

The email address of the user

Optional<String> name

The name of the user

### Create project user

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
import com.openai.models.admin.organization.projects.users.ProjectUser;
import com.openai.models.admin.organization.projects.users.UserCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        UserCreateParams params = UserCreateParams.builder()
            .projectId("project_id")
            .role("role")
            .build();
        ProjectUser projectUser = client.admin().organization().projects().users().create(params);

    "object": "organization.project.user",
    "id": "user_abc",
    "email": "user@example.com",
    "role": "owner",
    "added_at": 1711471533

##### Returns Examples

    "object": "organization.project.user",
    "id": "user_abc",
    "email": "user@example.com",
    "role": "owner",
    "added_at": 1711471533
