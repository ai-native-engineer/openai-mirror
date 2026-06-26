<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/update/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Projects](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects)

[Service Accounts](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Update project service account

admin.organization.projects.service\_accounts.update(service\_account\_id, \*\*kwargs) -> [ProjectServiceAccount](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20project_service_account%20%3E%20(schema)) { id, created\_at, name, 2 more }

POST/organization/projects/{project\_id}/service\_accounts/{service\_account\_id}

Updates a service account in the project.

##### ParametersExpand Collapse

project\_id: String

service\_account\_id: String

name: String

The updated service account name.

role: :member | :owner

The updated service account role.

One of the following:

:member

:owner

##### ReturnsExpand Collapse

class ProjectServiceAccount { id, created\_at, name, 2 more }

Represents an individual service account in a project.

id: String

The identifier, which can be referenced in API endpoints

created\_at: Integer

The Unix timestamp (in seconds) of when the service account was created

formatunixtime

name: String

The name of the service account

object: :"organization.project.service\_account"

The object type, which is always `organization.project.service_account`

role: :owner | :member

`owner` or `member`

One of the following:

:owner

:member

### Update project service account

Ruby

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

project_service_account = openai.admin.organization.projects.service_accounts.update("service_account_id", project_id: "project_id")

puts(project_service_account)

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
