<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Projects](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Data Retention

##### [Retrieve project data retention](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/retrieve)

admin.organization.projects.data\_retention.retrieve(project\_id) -> [ProjectDataRetention](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.data_retention%20%3E%20(model)%20project_data_retention%20%3E%20(schema)) { object, type }

GET/organization/projects/{project\_id}/data\_retention

##### [Update project data retention](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/update)

admin.organization.projects.data\_retention.update(project\_id, \*\*kwargs) -> [ProjectDataRetention](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.data_retention%20%3E%20(model)%20project_data_retention%20%3E%20(schema)) { object, type }

POST/organization/projects/{project\_id}/data\_retention

##### ModelsExpand Collapse

class ProjectDataRetention { object, type }

Represents a project’s data retention control setting.

object: :"project.data\_retention"

The object type, which is always `project.data_retention`.

type: :organization\_default | :none | :zero\_data\_retention | 3 more

The configured project data retention type.

One of the following:

:organization\_default

:none

:zero\_data\_retention

:modified\_abuse\_monitoring

:enhanced\_zero\_data\_retention

:enhanced\_modified\_abuse\_monitoring
