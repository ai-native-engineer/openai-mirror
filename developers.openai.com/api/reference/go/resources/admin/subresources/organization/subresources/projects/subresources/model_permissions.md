<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/ -->

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

# Model Permissions

##### [Retrieve project model permissions](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/retrieve)

client.Admin.Organization.Projects.ModelPermissions.Get(ctx, projectID) (\*[ProjectModelPermissions](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions%20%3E%20(schema)), error)

GET/organization/projects/{project\_id}/model\_permissions

##### [Modify project model permissions](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/update)

client.Admin.Organization.Projects.ModelPermissions.Update(ctx, projectID, body) (\*[ProjectModelPermissions](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions%20%3E%20(schema)), error)

POST/organization/projects/{project\_id}/model\_permissions

##### [Delete project model permissions](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/delete)

client.Admin.Organization.Projects.ModelPermissions.Delete(ctx, projectID) (\*[ProjectModelPermissionsDeleted](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions_deleted%20%3E%20(schema)), error)

DELETE/organization/projects/{project\_id}/model\_permissions

##### ModelsExpand Collapse

type ProjectModelPermissions struct{…}

Represents the model allowlist or denylist policy for a project.

Mode ProjectModelPermissionsMode

Whether the project uses an allowlist or a denylist.

One of the following:

const ProjectModelPermissionsModeAllowList ProjectModelPermissionsMode = "allow\_list"

const ProjectModelPermissionsModeDenyList ProjectModelPermissionsMode = "deny\_list"

ModelIDs []string

The model IDs included in the model permissions policy.

Object ProjectModelPermissions

The object type, which is always `project.model_permissions`.

type ProjectModelPermissionsDeleted struct{…}

Confirmation payload returned after deleting project model permissions.

Deleted bool

Whether the project model permissions were deleted.

Object ProjectModelPermissionsDeleted

The object type, which is always `project.model_permissions.deleted`.
