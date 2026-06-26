<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions/methods/update/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Projects](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects)

[Model Permissions](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/model_permissions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Modify project model permissions

client.admin.organization.projects.modelPermissions.update(stringprojectID, ModelPermissionUpdateParams { mode, model\_ids } body, RequestOptionsoptions?): [ProjectModelPermissions](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.model_permissions%20%3E%20(model)%20project_model_permissions%20%3E%20(schema)) { mode, model\_ids, object }

POST/organization/projects/{project\_id}/model\_permissions

Updates model permissions for a project.

##### ParametersExpand Collapse

projectID: string

body: ModelPermissionUpdateParams { mode, model\_ids }

mode: "allow\_list" | "deny\_list"

The model permissions mode to apply.

One of the following:

"allow\_list"

"deny\_list"

model\_ids: Array<string>

The model IDs included in this permissions policy.

##### ReturnsExpand Collapse

ProjectModelPermissions { mode, model\_ids, object }

Represents the model allowlist or denylist policy for a project.

mode: "allow\_list" | "deny\_list"

Whether the project uses an allowlist or a denylist.

One of the following:

"allow\_list"

"deny\_list"

model\_ids: Array<string>

The model IDs included in the model permissions policy.

object: "project.model\_permissions"

The object type, which is always `project.model_permissions`.

### Modify project model permissions

TypeScript

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import OpenAI from 'openai';

const client = new OpenAI({
  adminAPIKey: process.env['OPENAI_ADMIN_KEY'], // This is the default and can be omitted

const projectModelPermissions = await client.admin.organization.projects.modelPermissions.update(
  'project_id',
  { mode: 'allow_list', model_ids: ['string'] },
);

console.log(projectModelPermissions.model_ids);

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
