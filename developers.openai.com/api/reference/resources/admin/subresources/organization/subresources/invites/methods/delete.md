<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/invites/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Invites](/api/reference/resources/admin/subresources/organization/subresources/invites)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete invite

DELETE/organization/invites/{invite\_id}

Delete an invite. If the invite has already been accepted, it cannot be deleted.

##### Path ParametersExpand Collapse

invite\_id: string

##### ReturnsExpand Collapse

id: string

deleted: boolean

object: "organization.invite.deleted"

The object type, which is always `organization.invite.deleted`

### Delete invite

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl -X DELETE https://api.openai.com/v1/organization/invites/invite-abc \
  -H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
  -H "Content-Type: application/json"

    "object": "organization.invite.deleted",
    "id": "invite-abc",
    "deleted": true

##### Returns Examples

    "object": "organization.invite.deleted",
    "id": "invite-abc",
    "deleted": true
