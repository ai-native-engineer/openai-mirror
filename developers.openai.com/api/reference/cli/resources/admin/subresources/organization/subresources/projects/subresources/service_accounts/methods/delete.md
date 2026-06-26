<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Projects](/api/reference/cli/resources/admin/subresources/organization/subresources/projects)

[Service Accounts](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete project service account

$ openai admin:organization:projects:service-accounts delete

DELETE/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

Deletes a service account from the project.

Returns confirmation of service account deletion, or an error if the project
is archived (archived projects have no service accounts).

##### ParametersExpand Collapse

--project-id: string

The ID of the project.

--service-account-id: string

The ID of the service account.

##### ReturnsExpand Collapse

AdminOrganizationProjectServiceAccountDeleteResponse: object { id, deleted, object }

id: string

deleted: boolean

object: "organization.project.service\_account.deleted"

### Delete project service account

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:projects:service-accounts delete \
  --admin-api-key 'My Admin API Key' \
  --project-id project_id \
  --service-account-id service_account_id

    "object": "organization.project.service_account.deleted",
    "id": "svc_acct_abc",
    "deleted": true

##### Returns Examples

    "object": "organization.project.service_account.deleted",
    "id": "svc_acct_abc",
    "deleted": true
