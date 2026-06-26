<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/users/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Users](/api/reference/java/resources/admin/subresources/organization/subresources/users)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete user

[UserDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.users%20%3E%20(model)%20UserDeleteResponse%20%3E%20(schema)) admin().organization().users().delete(UserDeleteParamsparams = UserDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/users/{user\_id}

Deletes a user from the organization.

##### ParametersExpand Collapse

UserDeleteParams params

Optional<String> userId

##### ReturnsExpand Collapse

class UserDeleteResponse:

String id

boolean deleted

JsonValue; object\_ "organization.user.deleted"constant"organization.user.deleted"constant

### Delete user

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
import com.openai.models.admin.organization.users.UserDeleteParams;
import com.openai.models.admin.organization.users.UserDeleteResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        UserDeleteResponse user = client.admin().organization().users().delete("user_id");

    "object": "organization.user.deleted",
    "id": "user_abc",
    "deleted": true

##### Returns Examples

    "object": "organization.user.deleted",
    "id": "user_abc",
    "deleted": true
