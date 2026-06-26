<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/create/ -->

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

# Add group user

[UserCreateResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20UserCreateResponse%20%3E%20(schema)) admin().organization().groups().users().create(UserCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/groups/{group\_id}/users

Adds a user to a group.

##### ParametersExpand Collapse

UserCreateParams params

Optional<String> groupId

String userId

Identifier of the user to add to the group.

##### ReturnsExpand Collapse

class UserCreateResponse:

Confirmation payload returned after adding a user to a group.

String groupId

Identifier of the group the user was added to.

JsonValue; object\_ "group.user"constant"group.user"constant

Always `group.user`.

String userId

Identifier of the user that was added.

### Add group user

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
import com.openai.models.admin.organization.groups.users.UserCreateParams;
import com.openai.models.admin.organization.groups.users.UserCreateResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        UserCreateParams params = UserCreateParams.builder()
            .groupId("group_id")
            .userId("user_id")
            .build();
        UserCreateResponse user = client.admin().organization().groups().users().create(params);

    "object": "group.user",
    "user_id": "user_abc123",
    "group_id": "group_01J1F8ABCDXYZ"

##### Returns Examples

    "object": "group.user",
    "user_id": "user_abc123",
    "group_id": "group_01J1F8ABCDXYZ"
