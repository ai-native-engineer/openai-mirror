<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

[Service Accounts](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete project service account

DELETE/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

Deletes a service account from the project.

Returns confirmation of service account deletion, or an error if the project
is archived (archived projects have no service accounts).

##### Path ParametersExpand Collapse

project\_id: string

service\_account\_id: string

##### ReturnsExpand Collapse

id: string

deleted: boolean

object: "organization.project.service\_account.deleted"

### Delete project service account

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl -X DELETE https://api.openai.com/v1/organization/projects/proj_abc/service_accounts/svc_acct_abc \
  -H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
  -H "Content-Type: application/json"

    "object": "organization.project.service_account.deleted",
    "id": "svc_acct_abc",
    "deleted": true

##### Returns Examples

    "object": "organization.project.service_account.deleted",
    "id": "svc_acct_abc",
    "deleted": true
