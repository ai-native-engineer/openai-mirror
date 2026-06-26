<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Groups](/api/reference/java/resources/admin/subresources/organization/subresources/groups)

[Users](/api/reference/java/resources/admin/subresources/organization/subresources/groups/subresources/users)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List group users

UserListPage admin().organization().groups().users().list(UserListParamsparams = UserListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/groups/{group\_id}/users

Lists the users assigned to a group.

##### ParametersExpand Collapse

UserListParams params

Optional<String> groupId

Optional<String> after

A cursor for use in pagination. Provide the ID of the last user from the previous list response to retrieve the next page.

Optional<Long> limit

A limit on the number of users to be returned. Limit can range between 0 and 1000, and the default is 100.

minimum0

maximum1000

Optional<[Order](/api/reference/java/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/list#(resource)%20admin.organization.groups.users%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))> order

Specifies the sort order of users in the list.

ASC("asc")

DESC("desc")

##### ReturnsExpand Collapse

class OrganizationGroupUser:

Represents an individual user returned when inspecting group membership.

String id

The identifier, which can be referenced in API endpoints

Optional<String> email

The email address of the user.

String name

The name of the user.

### List group users

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
import com.openai.models.admin.organization.groups.users.UserListPage;
import com.openai.models.admin.organization.groups.users.UserListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        UserListPage page = client.admin().organization().groups().users().list("group_id");

    "object": "list",
    "data": [
            "id": "user_abc123",
            "name": "Ada Lovelace",
            "email": "ada@example.com"
    ],
    "has_more": false,
    "next": null

##### Returns Examples

    "object": "list",
    "data": [
            "id": "user_abc123",
            "name": "Ada Lovelace",
            "email": "ada@example.com"
    ],
    "has_more": false,
    "next": null
