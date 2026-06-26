<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Projects](/api/reference/cli/resources/admin/subresources/organization/subresources/projects)

[Data Retention](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/data_retention)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Retrieve project data retention

$ openai admin:organization:projects:data-retention retrieve

GET/organization/projects/{project\_id}/data\_retention

Retrieves project data retention controls.

##### ParametersExpand Collapse

--project-id: string

The ID of the project to inspect.

##### ReturnsExpand Collapse

project\_data\_retention: object { object, type }

Represents a project’s data retention control setting.

object: "project.data\_retention"

The object type, which is always `project.data_retention`.

type: "organization\_default" or "none" or "zero\_data\_retention" or 3 more

The configured project data retention type.

"organization\_default"

"none"

"zero\_data\_retention"

"modified\_abuse\_monitoring"

"enhanced\_zero\_data\_retention"

"enhanced\_modified\_abuse\_monitoring"

### Retrieve project data retention

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:projects:data-retention retrieve \
  --admin-api-key 'My Admin API Key' \
  --project-id project_id

    "object": "project.data_retention",
    "type": "organization_default"

##### Returns Examples

    "object": "project.data_retention",
    "type": "organization_default"
