<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/groups/subresources/users/methods/retrieve/ -->

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

# Retrieve group user

[UserRetrieveResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.groups.users%20%3E%20(model)%20UserRetrieveResponse%20%3E%20(schema)) admin().organization().groups().users().retrieve(UserRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/groups/{group\_id}/users/{user\_id}

Retrieves a user in a group.

##### ParametersExpand Collapse

UserRetrieveParams params

String groupId

Optional<String> userId

##### ReturnsExpand Collapse

class UserRetrieveResponse:

Details about a user returned from an organization group membership lookup.

String id

Identifier for the user.

Optional<String> email

Email address of the user, or `null` for users without an email.

Optional<Boolean> isServiceAccount

Whether the user is a service account.

String name

Display name of the user.

Optional<String> picture

URL of the user’s profile picture, if available.

UserType userType

The type of user.

One of the following:

USER("user")

TENANT\_USER("tenant\_user")

### Retrieve group user

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
import com.openai.models.admin.organization.groups.users.UserRetrieveParams;
import com.openai.models.admin.organization.groups.users.UserRetrieveResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        UserRetrieveParams params = UserRetrieveParams.builder()
            .groupId("group_id")
            .userId("user_id")
            .build();
        UserRetrieveResponse user = client.admin().organization().groups().users().retrieve(params);

    "id": "user_abc123",
    "name": "Ada Lovelace",
    "email": "ada@example.com",
    "picture": null,
    "is_service_account": false,
    "user_type": "user"

##### Returns Examples

    "id": "user_abc123",
    "name": "Ada Lovelace",
    "email": "ada@example.com",
    "picture": null,
    "is_service_account": false,
    "user_type": "user"
