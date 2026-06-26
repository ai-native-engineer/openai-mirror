<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/update/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Projects](/api/reference/cli/resources/admin/subresources/organization/subresources/projects)

[Users](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/users)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Modify project user

$ openai admin:organization:projects:users update

POST/organization/projects/{project\_id}/users/{user\_id}

Modifies a user’s role in the project.

##### ParametersExpand Collapse

--project-id: string

The ID of the project.

--user-id: string

The ID of the user.

--role: optional string

`owner` or `member`

##### ReturnsExpand Collapse

project\_user: object { id, added\_at, object, 3 more }

Represents an individual user in a project.

id: string

The identifier, which can be referenced in API endpoints

added\_at: number

The Unix timestamp (in seconds) of when the project was added.

object: "organization.project.user"

The object type, which is always `organization.project.user`

role: string

`owner` or `member`

email: optional string

The email address of the user

name: optional string

The name of the user

### Modify project user

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:projects:users update \
  --admin-api-key 'My Admin API Key' \
  --project-id project_id \
  --user-id user_id

    "object": "organization.project.user",
    "id": "user_abc",
    "name": "First Last",
    "email": "user@example.com",
    "role": "owner",
    "added_at": 1711471533

##### Returns Examples

    "object": "organization.project.user",
    "id": "user_abc",
    "name": "First Last",
    "email": "user@example.com",
    "role": "owner",
    "added_at": 1711471533
