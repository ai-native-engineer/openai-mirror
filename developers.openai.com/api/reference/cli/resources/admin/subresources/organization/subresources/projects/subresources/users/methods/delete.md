<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/users/methods/delete/ -->

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

# Delete project user

$ openai admin:organization:projects:users delete

DELETE/organization/projects/{project\_id}/users/{user\_id}

Deletes a user from the project.

Returns confirmation of project user deletion, or an error if the project is
archived (archived projects have no users).

##### ParametersExpand Collapse

--project-id: string

The ID of the project.

--user-id: string

The ID of the user.

##### ReturnsExpand Collapse

AdminOrganizationProjectUserDeleteResponse: object { id, deleted, object }

id: string

deleted: boolean

object: "organization.project.user.deleted"

### Delete project user

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:projects:users delete \
  --admin-api-key 'My Admin API Key' \
  --project-id project_id \
  --user-id user_id

    "object": "organization.project.user.deleted",
    "id": "user_abc",
    "deleted": true

##### Returns Examples

    "object": "organization.project.user.deleted",
    "id": "user_abc",
    "deleted": true
