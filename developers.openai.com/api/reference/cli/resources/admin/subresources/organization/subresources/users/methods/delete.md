<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/users/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Users](/api/reference/cli/resources/admin/subresources/organization/subresources/users)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete user

$ openai admin:organization:users delete

DELETE/organization/users/{user\_id}

Deletes a user from the organization.

##### ParametersExpand Collapse

--user-id: string

The ID of the user.

##### ReturnsExpand Collapse

AdminOrganizationUserDeleteResponse: object { id, deleted, object }

id: string

deleted: boolean

object: "organization.user.deleted"

### Delete user

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:users delete \
  --admin-api-key 'My Admin API Key' \
  --user-id user_id

    "object": "organization.user.deleted",
    "id": "user_abc",
    "deleted": true

##### Returns Examples

    "object": "organization.user.deleted",
    "id": "user_abc",
    "deleted": true
