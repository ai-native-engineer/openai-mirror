<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Projects](/api/reference/cli/resources/admin/subresources/organization/subresources/projects)

[Groups](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/groups)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Roles

##### [List project group role assignments](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/list)

$ openai admin:organization:projects:groups:roles list

GET/projects/{project\_id}/groups/{group\_id}/roles

##### [Assign project role to group](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/create)

$ openai admin:organization:projects:groups:roles create

POST/projects/{project\_id}/groups/{group\_id}/roles

##### [Retrieve project group role](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/retrieve)

$ openai admin:organization:projects:groups:roles retrieve

GET/projects/{project\_id}/groups/{group\_id}/roles/{role\_id}

##### [Unassign project role from group](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/groups/subresources/roles/methods/delete)

$ openai admin:organization:projects:groups:roles delete

DELETE/projects/{project\_id}/groups/{group\_id}/roles/{role\_id}
