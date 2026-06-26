<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/update/ -->

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

# Update project service account

POST/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

Updates a service account in the project.

##### Path ParametersExpand Collapse

project\_id: string

service\_account\_id: string

##### Body ParametersJSONExpand Collapse

name: optional string

The updated service account name.

role: optional "member" or "owner"

The updated service account role.

One of the following:

"member"

"owner"

##### ReturnsExpand Collapse

ProjectServiceAccount object { id, created\_at, name, 2 more }

Represents an individual service account in a project.

id: string

The identifier, which can be referenced in API endpoints

created\_at: number

The Unix timestamp (in seconds) of when the service account was created

formatunixtime

name: string

The name of the service account

object: "organization.project.service\_account"

The object type, which is always `organization.project.service_account`

role: "owner" or "member"

`owner` or `member`

One of the following:

"owner"

"member"

### Update project service account

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl -X POST https://api.openai.com/v1/organization/projects/proj_abc/service_accounts/svc_acct_abc \
  -H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "name": "Updated service account",
      "role": "member"
  }'

    "object": "organization.project.service_account",
    "id": "svc_acct_abc",
    "name": "Updated service account",
    "role": "member",
    "created_at": 1711471533

##### Returns Examples

    "object": "organization.project.service_account",
    "id": "svc_acct_abc",
    "name": "Updated service account",
    "role": "member",
    "created_at": 1711471533
