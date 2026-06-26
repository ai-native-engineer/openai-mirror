<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/methods/update/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Groups](/api/reference/typescript/resources/admin/subresources/organization/subresources/groups)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Update group

client.admin.organization.groups.update(stringgroupID, GroupUpdateParams { name } body, RequestOptionsoptions?): [GroupUpdateResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group_update_response%20%3E%20(schema)) { id, created\_at, is\_scim\_managed, name }

POST/organization/groups/{group\_id}

Updates a group’s information.

##### ParametersExpand Collapse

groupID: string

body: GroupUpdateParams { name }

name: string

New display name for the group.

minLength1

maxLength255

##### ReturnsExpand Collapse

GroupUpdateResponse { id, created\_at, is\_scim\_managed, name }

Response returned after updating a group.

id: string

Identifier for the group.

created\_at: number

Unix timestamp (in seconds) when the group was created.

formatunixtime

is\_scim\_managed: boolean

Whether the group is managed through SCIM and controlled by your identity provider.

name: string

Updated display name for the group.

### Update group

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

const group = await client.admin.organization.groups.update('group_id', { name: 'x' });

console.log(group.id);

    "id": "group_01J1F8ABCDXYZ",
    "name": "Escalations",
    "created_at": 1711471533,
    "is_scim_managed": false

##### Returns Examples

    "id": "group_01J1F8ABCDXYZ",
    "name": "Escalations",
    "created_at": 1711471533,
    "is_scim_managed": false
