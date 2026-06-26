<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Projects](/api/reference/cli/resources/admin/subresources/organization/subresources/projects)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Data Retention

##### [Retrieve project data retention](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/retrieve)

$ openai admin:organization:projects:data-retention retrieve

GET/organization/projects/{project\_id}/data\_retention

##### [Update project data retention](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/update)

$ openai admin:organization:projects:data-retention update

POST/organization/projects/{project\_id}/data\_retention

##### ModelsExpand Collapse

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
