<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/retrieve/ -->

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

# Retrieve project model permissions

[ProjectModelPermissions](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions%20%3E%20(schema)) admin().organization().projects().modelPermissions().retrieve(ModelPermissionRetrieveParamsparams = ModelPermissionRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}/model\_permissions

Returns model permissions for a project.

##### ParametersExpand Collapse

ModelPermissionRetrieveParams params

Optional<String> projectId

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

### Retrieve project model permissions

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
import com.openai.models.admin.organization.projects.modelpermissions.ModelPermissionRetrieveParams;
import com.openai.models.admin.organization.projects.modelpermissions.ProjectModelPermissions;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ProjectModelPermissions projectModelPermissions = client.admin().organization().projects().modelPermissions().retrieve("project_id");

    "object": "project.model_permissions",
    "mode": "allow_list",
    "model_ids": [
        "gpt-4.1",
        "o3"
    ]

##### Returns Examples

    "object": "project.model_permissions",
    "mode": "allow_list",
    "model_ids": [
        "gpt-4.1",
        "o3"
    ]
