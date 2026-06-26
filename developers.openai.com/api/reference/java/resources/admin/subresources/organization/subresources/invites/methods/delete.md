<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/invites/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Invites](/api/reference/java/resources/admin/subresources/organization/subresources/invites)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete invite

[InviteDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20InviteDeleteResponse%20%3E%20(schema)) admin().organization().invites().delete(InviteDeleteParamsparams = InviteDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/invites/{invite\_id}

Delete an invite. If the invite has already been accepted, it cannot be deleted.

##### ParametersExpand Collapse

InviteDeleteParams params

Optional<String> inviteId

##### ReturnsExpand Collapse

class InviteDeleteResponse:

String id

boolean deleted

JsonValue; object\_ "organization.invite.deleted"constant"organization.invite.deleted"constant

The object type, which is always `organization.invite.deleted`

### Delete invite

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
import com.openai.models.admin.organization.invites.InviteDeleteParams;
import com.openai.models.admin.organization.invites.InviteDeleteResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        InviteDeleteResponse invite = client.admin().organization().invites().delete("invite_id");

    "object": "organization.invite.deleted",
    "id": "invite-abc",
    "deleted": true

##### Returns Examples

    "object": "organization.invite.deleted",
    "id": "invite-abc",
    "deleted": true
