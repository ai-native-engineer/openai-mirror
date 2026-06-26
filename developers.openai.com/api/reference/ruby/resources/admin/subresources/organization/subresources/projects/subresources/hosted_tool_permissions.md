<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/ -->

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

# Hosted Tool Permissions

##### [Retrieve project hosted tool permissions](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/retrieve)

admin.organization.projects.hosted\_tool\_permissions.retrieve(project\_id) -> [ProjectHostedToolPermissions](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(model)%20project_hosted_tool_permissions%20%3E%20(schema)) { code\_interpreter, file\_search, image\_generation, 2 more }

GET/organization/projects/{project\_id}/hosted\_tool\_permissions

##### [Modify project hosted tool permissions](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/hosted_tool_permissions/methods/update)

admin.organization.projects.hosted\_tool\_permissions.update(project\_id, \*\*kwargs) -> [ProjectHostedToolPermissions](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.hosted_tool_permissions%20%3E%20(model)%20project_hosted_tool_permissions%20%3E%20(schema)) { code\_interpreter, file\_search, image\_generation, 2 more }

POST/organization/projects/{project\_id}/hosted\_tool\_permissions

##### ModelsExpand Collapse

class ProjectHostedToolPermissions { code\_interpreter, file\_search, image\_generation, 2 more }

Represents hosted tool permissions for a project.

code\_interpreter: CodeInterpreter{ enabled}

Permission state for a single hosted tool on a project.

enabled: bool

Whether the hosted tool is enabled for the project.

file\_search: FileSearch{ enabled}

Permission state for a single hosted tool on a project.

enabled: bool

Whether the hosted tool is enabled for the project.

image\_generation: ImageGeneration{ enabled}

Permission state for a single hosted tool on a project.

enabled: bool

Whether the hosted tool is enabled for the project.

mcp: Mcp{ enabled}

Permission state for a single hosted tool on a project.

enabled: bool

Whether the hosted tool is enabled for the project.

web\_search: WebSearch{ enabled}

Permission state for a single hosted tool on a project.

enabled: bool

Whether the hosted tool is enabled for the project.
