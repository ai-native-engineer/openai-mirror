<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/groups/methods/retrieve/ -->

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

# Retrieve group

client.admin.organization.groups.retrieve(stringgroupID, RequestOptionsoptions?): [Group](/api/reference/typescript/resources/admin#(resource)%20admin.organization.groups%20%3E%20(model)%20group%20%3E%20(schema)) { id, created\_at, group\_type, 2 more }

GET/organization/groups/{group\_id}

Retrieves a group.

##### ParametersExpand Collapse

groupID: string

##### ReturnsExpand Collapse

Group { id, created\_at, group\_type, 2 more }

Details about an organization group.

id: string

Identifier for the group.

created\_at: number

Unix timestamp (in seconds) when the group was created.

formatunixtime

group\_type: "group" | "tenant\_group"

The type of the group.

One of the following:

"group"

"tenant\_group"

is\_scim\_managed: boolean

Whether the group is managed through SCIM and controlled by your identity provider.

name: string

Display name of the group.

### Retrieve group

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

const group = await client.admin.organization.groups.retrieve('group_id');

console.log(group.id);

    "id": "group_01J1F8ABCDXYZ",
    "name": "Support Team",
    "created_at": 1711471533,
    "is_scim_managed": false,
    "group_type": "group"

##### Returns Examples

    "id": "group_01J1F8ABCDXYZ",
    "name": "Support Team",
    "created_at": 1711471533,
    "is_scim_managed": false,
    "group_type": "group"
