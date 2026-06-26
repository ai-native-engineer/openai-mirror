<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/ -->

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

# Hosted Tool Permissions

##### [Retrieve project hosted tool permissions](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/retrieve)

client.Admin.Organization.Projects.HostedToolPermissions.Get(ctx, projectID) (\*[ProjectHostedToolPermissions](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(model)%20project_hosted_tool_permissions%20%3E%20(schema)), error)

GET/organization/projects/{project\_id}/hosted\_tool\_permissions

##### [Modify project hosted tool permissions](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/update)

client.Admin.Organization.Projects.HostedToolPermissions.Update(ctx, projectID, body) (\*[ProjectHostedToolPermissions](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(model)%20project_hosted_tool_permissions%20%3E%20(schema)), error)

POST/organization/projects/{project\_id}/hosted\_tool\_permissions

##### ModelsExpand Collapse

type ProjectHostedToolPermissions struct{…}

Represents hosted tool permissions for a project.

CodeInterpreter ProjectHostedToolPermissionsCodeInterpreter

Permission state for a single hosted tool on a project.

Enabled bool

Whether the hosted tool is enabled for the project.

FileSearch ProjectHostedToolPermissionsFileSearch

Permission state for a single hosted tool on a project.

Enabled bool

Whether the hosted tool is enabled for the project.

ImageGeneration ProjectHostedToolPermissionsImageGeneration

Permission state for a single hosted tool on a project.

Enabled bool

Whether the hosted tool is enabled for the project.

Mcp ProjectHostedToolPermissionsMcp

Permission state for a single hosted tool on a project.

Enabled bool

Whether the hosted tool is enabled for the project.

WebSearch ProjectHostedToolPermissionsWebSearch

Permission state for a single hosted tool on a project.

Enabled bool

Whether the hosted tool is enabled for the project.
