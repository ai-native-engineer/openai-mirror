<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Projects](/api/reference/java/resources/admin/subresources/organization/subresources/projects)

[Model Permissions](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete project model permissions

[ProjectModelPermissionsDeleted](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions_deleted%20%3E%20(schema)) admin().organization().projects().modelPermissions().delete(ModelPermissionDeleteParamsparams = ModelPermissionDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/projects/{project\_id}/model\_permissions

Deletes model permissions for a project.

##### ParametersExpand Collapse

ModelPermissionDeleteParams params

Optional<String> projectId

##### ReturnsExpand Collapse

class ProjectModelPermissionsDeleted:

Confirmation payload returned after deleting project model permissions.

boolean deleted

Whether the project model permissions were deleted.

JsonValue; object\_ "project.model\_permissions.deleted"constant"project.model\_permissions.deleted"constant

The object type, which is always `project.model_permissions.deleted`.

### Delete project model permissions

Java

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.admin.organization.projects.modelpermissions.ModelPermissionDeleteParams;
import com.openai.models.admin.organization.projects.modelpermissions.ProjectModelPermissionsDeleted;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ProjectModelPermissionsDeleted projectModelPermissionsDeleted = client.admin().organization().projects().modelPermissions().delete("project_id");

    "object": "project.model_permissions.deleted",
    "deleted": true

##### Returns Examples

    "object": "project.model_permissions.deleted",
    "deleted": true
