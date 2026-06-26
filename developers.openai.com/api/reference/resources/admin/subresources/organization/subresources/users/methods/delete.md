<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/users/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Users](/api/reference/resources/admin/subresources/organization/subresources/users)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete user

DELETE/organization/users/{user\_id}

Deletes a user from the organization.

##### Path ParametersExpand Collapse

user\_id: string

##### ReturnsExpand Collapse

id: string

deleted: boolean

object: "organization.user.deleted"

### Delete user

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl -X DELETE https://api.openai.com/v1/organization/users/user_abc \
  -H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
  -H "Content-Type: application/json"

    "object": "organization.user.deleted",
    "id": "user_abc",
    "deleted": true

##### Returns Examples

    "object": "organization.user.deleted",
    "id": "user_abc",
    "deleted": true
