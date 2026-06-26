<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/ -->

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

# Hosted Tool Permissions

##### [Retrieve project hosted tool permissions](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/retrieve)

[ProjectHostedToolPermissions](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(model)%20project_hosted_tool_permissions%20%3E%20(schema)) admin().organization().projects().hostedToolPermissions().retrieve(HostedToolPermissionRetrieveParamsparams = HostedToolPermissionRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}/hosted\_tool\_permissions

##### [Modify project hosted tool permissions](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/update)

[ProjectHostedToolPermissions](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(model)%20project_hosted_tool_permissions%20%3E%20(schema)) admin().organization().projects().hostedToolPermissions().update(HostedToolPermissionUpdateParamsparams = HostedToolPermissionUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/hosted\_tool\_permissions

##### ModelsExpand Collapse

class ProjectHostedToolPermissions:

Represents hosted tool permissions for a project.

CodeInterpreter codeInterpreter

Permission state for a single hosted tool on a project.

boolean enabled

Whether the hosted tool is enabled for the project.

FileSearch fileSearch

Permission state for a single hosted tool on a project.

boolean enabled

Whether the hosted tool is enabled for the project.

ImageGeneration imageGeneration

Permission state for a single hosted tool on a project.

boolean enabled

Whether the hosted tool is enabled for the project.

Mcp mcp

Permission state for a single hosted tool on a project.

boolean enabled

Whether the hosted tool is enabled for the project.

WebSearch webSearch

Permission state for a single hosted tool on a project.

boolean enabled

Whether the hosted tool is enabled for the project.
