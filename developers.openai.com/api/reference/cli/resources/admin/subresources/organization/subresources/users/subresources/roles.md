<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/users/subresources/roles/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Users](/api/reference/cli/resources/admin/subresources/organization/subresources/users)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Roles

##### [List user organization role assignments](/api/reference/cli/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/list)

$ openai admin:organization:users:roles list

GET/organization/users/{user\_id}/roles

##### [Assign organization role to user](/api/reference/cli/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/create)

$ openai admin:organization:users:roles create

POST/organization/users/{user\_id}/roles

##### [Retrieve user organization role](/api/reference/cli/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/retrieve)

$ openai admin:organization:users:roles retrieve

GET/organization/users/{user\_id}/roles/{role\_id}

##### [Unassign organization role from user](/api/reference/cli/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/delete)

$ openai admin:organization:users:roles delete

DELETE/organization/users/{user\_id}/roles/{role\_id}
