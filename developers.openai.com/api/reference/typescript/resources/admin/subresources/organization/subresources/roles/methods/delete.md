<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/roles/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Roles](/api/reference/typescript/resources/admin/subresources/organization/subresources/roles)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete organization role

client.admin.organization.roles.delete(stringroleID, RequestOptionsoptions?): [RoleDeleteResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.roles%20%3E%20(model)%20role_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/roles/{role\_id}

Deletes a custom role from the organization.

##### ParametersExpand Collapse

roleID: string

##### ReturnsExpand Collapse

RoleDeleteResponse { id, deleted, object }

Confirmation payload returned after deleting a role.

id: string

Identifier of the deleted role.

deleted: boolean

Whether the role was deleted.

object: "role.deleted"

Always `role.deleted`.

### Delete organization role

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

const role = await client.admin.organization.roles.delete('role_id');

console.log(role.id);

    "object": "role.deleted",
    "id": "role_01J1F8ROLE01",
    "deleted": true

##### Returns Examples

    "object": "role.deleted",
    "id": "role_01J1F8ROLE01",
    "deleted": true
