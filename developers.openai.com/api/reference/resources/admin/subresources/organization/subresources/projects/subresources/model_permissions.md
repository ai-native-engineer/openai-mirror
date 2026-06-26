<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Model Permissions

##### [Retrieve project model permissions](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/retrieve)

GET/organization/projects/{project\_id}/model\_permissions

##### [Modify project model permissions](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/update)

POST/organization/projects/{project\_id}/model\_permissions

##### [Delete project model permissions](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/delete)

DELETE/organization/projects/{project\_id}/model\_permissions

##### ModelsExpand Collapse

ProjectModelPermissions object { mode, model\_ids, object }

Represents the model allowlist or denylist policy for a project.

mode: "allow\_list" or "deny\_list"

Whether the project uses an allowlist or a denylist.

One of the following:

"allow\_list"

"deny\_list"

model\_ids: array of string

The model IDs included in the model permissions policy.

object: "project.model\_permissions"

The object type, which is always `project.model_permissions`.

ProjectModelPermissionsDeleted object { deleted, object }

Confirmation payload returned after deleting project model permissions.

deleted: boolean

Whether the project model permissions were deleted.

object: "project.model\_permissions.deleted"

The object type, which is always `project.model_permissions.deleted`.
