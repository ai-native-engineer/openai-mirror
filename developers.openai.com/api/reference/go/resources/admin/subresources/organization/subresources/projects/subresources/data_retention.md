<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Projects](/api/reference/go/resources/admin/subresources/organization/subresources/projects)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Data Retention

##### [Retrieve project data retention](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/retrieve)

client.Admin.Organization.Projects.DataRetention.Get(ctx, projectID) (\*[ProjectDataRetention](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.data_retention%20%3E%20(model)%20project_data_retention%20%3E%20(schema)), error)

GET/organization/projects/{project\_id}/data\_retention

##### [Update project data retention](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/data_retention/methods/update)

client.Admin.Organization.Projects.DataRetention.Update(ctx, projectID, body) (\*[ProjectDataRetention](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.data_retention%20%3E%20(model)%20project_data_retention%20%3E%20(schema)), error)

POST/organization/projects/{project\_id}/data\_retention

##### ModelsExpand Collapse

type ProjectDataRetention struct{…}

Represents a project’s data retention control setting.

Object ProjectDataRetention

The object type, which is always `project.data_retention`.

Type ProjectDataRetentionType

The configured project data retention type.

One of the following:

const ProjectDataRetentionTypeOrganizationDefault ProjectDataRetentionType = "organization\_default"

const ProjectDataRetentionTypeNone ProjectDataRetentionType = "none"

const ProjectDataRetentionTypeZeroDataRetention ProjectDataRetentionType = "zero\_data\_retention"

const ProjectDataRetentionTypeModifiedAbuseMonitoring ProjectDataRetentionType = "modified\_abuse\_monitoring"

const ProjectDataRetentionTypeEnhancedZeroDataRetention ProjectDataRetentionType = "enhanced\_zero\_data\_retention"

const ProjectDataRetentionTypeEnhancedModifiedAbuseMonitoring ProjectDataRetentionType = "enhanced\_modified\_abuse\_monitoring"
