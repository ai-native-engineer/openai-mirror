<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/ -->

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

# Model Permissions

##### [Retrieve project model permissions](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/retrieve)

admin.organization.projects.model\_permissions.retrieve(project\_id) -> [ProjectModelPermissions](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions%20%3E%20(schema)) { mode, model\_ids, object }

GET/organization/projects/{project\_id}/model\_permissions

##### [Modify project model permissions](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/update)

admin.organization.projects.model\_permissions.update(project\_id, \*\*kwargs) -> [ProjectModelPermissions](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions%20%3E%20(schema)) { mode, model\_ids, object }

POST/organization/projects/{project\_id}/model\_permissions

##### [Delete project model permissions](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/delete)

admin.organization.projects.model\_permissions.delete(project\_id) -> [ProjectModelPermissionsDeleted](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions_deleted%20%3E%20(schema)) { deleted, object }

DELETE/organization/projects/{project\_id}/model\_permissions

##### ModelsExpand Collapse

class ProjectModelPermissions { mode, model\_ids, object }

Represents the model allowlist or denylist policy for a project.

mode: :allow\_list | :deny\_list

Whether the project uses an allowlist or a denylist.

One of the following:

:allow\_list

:deny\_list

model\_ids: Array[String]

The model IDs included in the model permissions policy.

object: :"project.model\_permissions"

The object type, which is always `project.model_permissions`.

class ProjectModelPermissionsDeleted { deleted, object }

Confirmation payload returned after deleting project model permissions.

deleted: bool

Whether the project model permissions were deleted.

object: :"project.model\_permissions.deleted"

The object type, which is always `project.model_permissions.deleted`.
