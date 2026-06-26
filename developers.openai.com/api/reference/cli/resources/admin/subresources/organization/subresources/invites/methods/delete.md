<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/invites/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Invites](/api/reference/cli/resources/admin/subresources/organization/subresources/invites)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete invite

$ openai admin:organization:invites delete

DELETE/organization/invites/{invite\_id}

Delete an invite. If the invite has already been accepted, it cannot be deleted.

##### ParametersExpand Collapse

--invite-id: string

The ID of the invite to delete.

##### ReturnsExpand Collapse

AdminOrganizationInviteDeleteResponse: object { id, deleted, object }

id: string

deleted: boolean

object: "organization.invite.deleted"

The object type, which is always `organization.invite.deleted`

### Delete invite

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:invites delete \
  --admin-api-key 'My Admin API Key' \
  --invite-id invite_id

    "object": "organization.invite.deleted",
    "id": "invite-abc",
    "deleted": true

##### Returns Examples

    "object": "organization.invite.deleted",
    "id": "invite-abc",
    "deleted": true
