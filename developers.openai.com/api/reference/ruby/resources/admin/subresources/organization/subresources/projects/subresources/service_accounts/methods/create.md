<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/methods/create/ -->

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

# Create project service account

admin.organization.projects.service\_accounts.create(project\_id, \*\*kwargs) -> [ServiceAccountCreateResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.service_accounts%20%3E%20(model)%20service_account_create_response%20%3E%20(schema)) { id, api\_key, created\_at, 3 more }

POST/organization/projects/{project\_id}/service\_accounts

Creates a new service account in the project. This also returns an unredacted API key for the service account.

##### ParametersExpand Collapse

project\_id: String

name: String

The name of the service account being created.

##### ReturnsExpand Collapse

class ServiceAccountCreateResponse { id, api\_key, created\_at, 3 more }

id: String

api\_key: APIKey{ id, created\_at, name, 2 more}

id: String

created\_at: Integer

formatunixtime

name: String

object: :"organization.project.service\_account.api\_key"

The object type, which is always `organization.project.service_account.api_key`

value: String

created\_at: Integer

formatunixtime

name: String

object: :"organization.project.service\_account"

role: :member

Service accounts can only have one role of type `member`

### Create project service account

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

service_account = openai.admin.organization.projects.service_accounts.create("project_id", name: "name")

puts(service_account)

    "object": "organization.project.service_account",
    "id": "svc_acct_abc",
    "name": "Production App",
    "role": "member",
    "created_at": 1711471533,
    "api_key": {
        "object": "organization.project.service_account.api_key",
        "value": "sk-abcdefghijklmnop123",
        "name": "Secret Key",
        "created_at": 1711471533,
        "id": "key_abc"

##### Returns Examples

    "object": "organization.project.service_account",
    "id": "svc_acct_abc",
    "name": "Production App",
    "role": "member",
    "created_at": 1711471533,
    "api_key": {
        "object": "organization.project.service_account.api_key",
        "value": "sk-abcdefghijklmnop123",
        "name": "Secret Key",
        "created_at": 1711471533,
        "id": "key_abc"
