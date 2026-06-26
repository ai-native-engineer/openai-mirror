<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/ -->

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

# Model Permissions

##### [Retrieve project model permissions](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/retrieve)

[ProjectModelPermissions](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions%20%3E%20(schema)) admin().organization().projects().modelPermissions().retrieve(ModelPermissionRetrieveParamsparams = ModelPermissionRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}/model\_permissions

##### [Modify project model permissions](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/update)

[ProjectModelPermissions](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions%20%3E%20(schema)) admin().organization().projects().modelPermissions().update(ModelPermissionUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/model\_permissions

##### [Delete project model permissions](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/delete)

[ProjectModelPermissionsDeleted](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions_deleted%20%3E%20(schema)) admin().organization().projects().modelPermissions().delete(ModelPermissionDeleteParamsparams = ModelPermissionDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/projects/{project\_id}/model\_permissions

##### ModelsExpand Collapse

class ProjectModelPermissions:

Represents the model allowlist or denylist policy for a project.

Mode mode

Whether the project uses an allowlist or a denylist.

One of the following:

ALLOW\_LIST("allow\_list")

DENY\_LIST("deny\_list")

List<String> modelIds

The model IDs included in the model permissions policy.

JsonValue; object\_ "project.model\_permissions"constant"project.model\_permissions"constant

The object type, which is always `project.model_permissions`.

class ProjectModelPermissionsDeleted:

Confirmation payload returned after deleting project model permissions.

boolean deleted

Whether the project model permissions were deleted.

JsonValue; object\_ "project.model\_permissions.deleted"constant"project.model\_permissions.deleted"constant

The object type, which is always `project.model_permissions.deleted`.
