<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/roles/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Roles](/api/reference/java/resources/admin/subresources/organization/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete organization role

[RoleDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20RoleDeleteResponse%20%3E%20(schema)) admin().organization().roles().delete(RoleDeleteParamsparams = RoleDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/roles/{role\_id}

Deletes a custom role from the organization.

##### ParametersExpand Collapse

RoleDeleteParams params

Optional<String> roleId

##### ReturnsExpand Collapse

class RoleDeleteResponse:

Confirmation payload returned after deleting a role.

String id

Identifier of the deleted role.

boolean deleted

Whether the role was deleted.

JsonValue; object\_ "role.deleted"constant"role.deleted"constant

Always `role.deleted`.

### Delete organization role

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
import com.openai.models.admin.organization.roles.RoleDeleteParams;
import com.openai.models.admin.organization.roles.RoleDeleteResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        RoleDeleteResponse role = client.admin().organization().roles().delete("role_id");

    "object": "role.deleted",
    "id": "role_01J1F8ROLE01",
    "deleted": true

##### Returns Examples

    "object": "role.deleted",
    "id": "role_01J1F8ROLE01",
    "deleted": true
