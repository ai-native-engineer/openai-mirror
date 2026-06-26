<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/list/ -->

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

# List project users

UserListPage admin().organization().projects().users().list(UserListParamsparams = UserListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}/users

Returns a list of users in the project.

##### ParametersExpand Collapse

UserListParams params

Optional<String> projectId

Optional<String> after

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

Optional<Long> limit

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

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

### List project users

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
import com.openai.models.admin.organization.projects.users.UserListPage;
import com.openai.models.admin.organization.projects.users.UserListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        UserListPage page = client.admin().organization().projects().users().list("project_id");

    "object": "list",
    "data": [
            "object": "organization.project.user",
            "id": "user_abc",
            "name": "First Last",
            "email": "user@example.com",
            "role": "owner",
            "added_at": 1711471533
    ],
    "first_id": "user-abc",
    "last_id": "user-xyz",
    "has_more": false

##### Returns Examples

    "object": "list",
    "data": [
            "object": "organization.project.user",
            "id": "user_abc",
            "name": "First Last",
            "email": "user@example.com",
            "role": "owner",
            "added_at": 1711471533
    ],
    "first_id": "user-abc",
    "last_id": "user-xyz",
    "has_more": false
