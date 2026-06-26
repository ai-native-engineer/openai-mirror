<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Projects](/api/reference/java/resources/admin/subresources/organization/subresources/projects)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Data Retention

##### [Retrieve project data retention](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/retrieve)

[ProjectDataRetention](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.data_retention%20%3E%20(model)%20project_data_retention%20%3E%20(schema)) admin().organization().projects().dataRetention().retrieve(DataRetentionRetrieveParamsparams = DataRetentionRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}/data\_retention

##### [Update project data retention](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/update)

[ProjectDataRetention](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.data_retention%20%3E%20(model)%20project_data_retention%20%3E%20(schema)) admin().organization().projects().dataRetention().update(DataRetentionUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/data\_retention

##### ModelsExpand Collapse

class ProjectDataRetention:

Represents a project’s data retention control setting.

JsonValue; object\_ "project.data\_retention"constant"project.data\_retention"constant

The object type, which is always `project.data_retention`.

Type type

The configured project data retention type.

One of the following:

ORGANIZATION\_DEFAULT("organization\_default")

NONE("none")

ZERO\_DATA\_RETENTION("zero\_data\_retention")

MODIFIED\_ABUSE\_MONITORING("modified\_abuse\_monitoring")

ENHANCED\_ZERO\_DATA\_RETENTION("enhanced\_zero\_data\_retention")

ENHANCED\_MODIFIED\_ABUSE\_MONITORING("enhanced\_modified\_abuse\_monitoring")
