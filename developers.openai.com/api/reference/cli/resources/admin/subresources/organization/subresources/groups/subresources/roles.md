<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/groups/subresources/roles/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Groups](/api/reference/cli/resources/admin/subresources/organization/subresources/groups)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Roles

##### [List group organization role assignments](/api/reference/cli/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/list)

$ openai admin:organization:groups:roles list

GET/organization/groups/{group\_id}/roles

##### [Assign organization role to group](/api/reference/cli/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/create)

$ openai admin:organization:groups:roles create

POST/organization/groups/{group\_id}/roles

##### [Retrieve group organization role](/api/reference/cli/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/retrieve)

$ openai admin:organization:groups:roles retrieve

GET/organization/groups/{group\_id}/roles/{role\_id}

##### [Unassign organization role from group](/api/reference/cli/resources/admin/subresources/organization/subresources/groups/subresources/roles/methods/delete)

$ openai admin:organization:groups:roles delete

DELETE/organization/groups/{group\_id}/roles/{role\_id}
