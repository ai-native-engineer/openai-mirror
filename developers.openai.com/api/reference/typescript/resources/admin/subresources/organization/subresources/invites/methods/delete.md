<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/invites/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Invites](/api/reference/typescript/resources/admin/subresources/organization/subresources/invites)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete invite

client.admin.organization.invites.delete(stringinviteID, RequestOptionsoptions?): [InviteDeleteResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.invites%20%3E%20(model)%20invite_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/invites/{invite\_id}

Delete an invite. If the invite has already been accepted, it cannot be deleted.

##### ParametersExpand Collapse

inviteID: string

##### ReturnsExpand Collapse

InviteDeleteResponse { id, deleted, object }

id: string

deleted: boolean

object: "organization.invite.deleted"

The object type, which is always `organization.invite.deleted`

### Delete invite

TypeScript

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import OpenAI from 'openai';

const client = new OpenAI({
  adminAPIKey: process.env['OPENAI_ADMIN_KEY'], // This is the default and can be omitted

const invite = await client.admin.organization.invites.delete('invite_id');

console.log(invite.id);

    "object": "organization.invite.deleted",
    "id": "invite-abc",
    "deleted": true

##### Returns Examples

    "object": "organization.invite.deleted",
    "id": "invite-abc",
    "deleted": true
