<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/update/ -->

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

# Modify project model permissions

[ProjectModelPermissions](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions%20%3E%20(schema)) admin().organization().projects().modelPermissions().update(ModelPermissionUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/model\_permissions

Updates model permissions for a project.

##### ParametersExpand Collapse

ModelPermissionUpdateParams params

Optional<String> projectId

Mode mode

The model permissions mode to apply.

ALLOW\_LIST("allow\_list")

DENY\_LIST("deny\_list")

List<String> modelIds

The model IDs included in this permissions policy.

##### ReturnsExpand Collapse

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

### Modify project model permissions

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
import com.openai.models.admin.organization.projects.modelpermissions.ModelPermissionUpdateParams;
import com.openai.models.admin.organization.projects.modelpermissions.ProjectModelPermissions;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ModelPermissionUpdateParams params = ModelPermissionUpdateParams.builder()
            .projectId("project_id")
            .mode(ModelPermissionUpdateParams.Mode.ALLOW_LIST)
            .addModelId("string")
            .build();
        ProjectModelPermissions projectModelPermissions = client.admin().organization().projects().modelPermissions().update(params);

    "object": "project.model_permissions",
    "mode": "deny_list",
    "model_ids": [
        "o3"
    ]

##### Returns Examples

    "object": "project.model_permissions",
    "mode": "deny_list",
    "model_ids": [
        "o3"
    ]
