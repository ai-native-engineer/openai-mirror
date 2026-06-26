<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Projects](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects)

[Users](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/users)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create project user

admin.organization.projects.users.create(project\_id, \*\*kwargs) -> [ProjectUser](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.users%20%3E%20(model)%20project_user%20%3E%20(schema)) { id, added\_at, object, 3 more }

POST/organization/projects/{project\_id}/users

Adds a user to the project. Users must already be members of the organization to be added to a project.

##### ParametersExpand Collapse

project\_id: String

role: String

`owner` or `member`

email: String

Email of the user to add.

user\_id: String

The ID of the user.

##### ReturnsExpand Collapse

class ProjectUser { id, added\_at, object, 3 more }

Represents an individual user in a project.

id: String

The identifier, which can be referenced in API endpoints

added\_at: Integer

The Unix timestamp (in seconds) of when the project was added.

formatunixtime

object: :"organization.project.user"

The object type, which is always `organization.project.user`

role: String

`owner` or `member`

email: String

The email address of the user

name: String

The name of the user

### Create project user

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

project_user = openai.admin.organization.projects.users.create("project_id", role: "role")

puts(project_user)

    "object": "organization.project.user",
    "id": "user_abc",
    "email": "user@example.com",
    "role": "owner",
    "added_at": 1711471533

##### Returns Examples

    "object": "organization.project.user",
    "id": "user_abc",
    "email": "user@example.com",
    "role": "owner",
    "added_at": 1711471533
