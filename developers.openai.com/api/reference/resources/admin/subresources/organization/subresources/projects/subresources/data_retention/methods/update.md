<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/update/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

[Data Retention](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/data_retention)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Update project data retention

POST/organization/projects/{project\_id}/data\_retention

Updates project data retention controls.

##### Path ParametersExpand Collapse

project\_id: string

##### Body ParametersJSONExpand Collapse

retention\_type: "organization\_default" or "none" or "zero\_data\_retention" or 3 more

The desired project data retention type.

One of the following:

"organization\_default"

"none"

"zero\_data\_retention"

"modified\_abuse\_monitoring"

"enhanced\_zero\_data\_retention"

"enhanced\_modified\_abuse\_monitoring"

##### ReturnsExpand Collapse

ProjectDataRetention object { object, type }

Represents a project’s data retention control setting.

object: "project.data\_retention"

The object type, which is always `project.data_retention`.

type: "organization\_default" or "none" or "zero\_data\_retention" or 3 more

The configured project data retention type.

One of the following:

"organization\_default"

"none"

"zero\_data\_retention"

"modified\_abuse\_monitoring"

"enhanced\_zero\_data\_retention"

"enhanced\_modified\_abuse\_monitoring"

### Update project data retention

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl -X POST https://api.openai.com/v1/organization/projects/proj_abc/data_retention \
  -H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "retention_type": "modified_abuse_monitoring"
  }'

    "object": "project.data_retention",
    "type": "modified_abuse_monitoring"

##### Returns Examples

    "object": "project.data_retention",
    "type": "modified_abuse_monitoring"
