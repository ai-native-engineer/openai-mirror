<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Projects](/api/reference/cli/resources/admin/subresources/organization/subresources/projects)

[Users](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/users)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Roles

##### [List project user role assignments](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/list)

$ openai admin:organization:projects:users:roles list

GET/projects/{project\_id}/users/{user\_id}/roles

##### [Assign project role to user](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/create)

$ openai admin:organization:projects:users:roles create

POST/projects/{project\_id}/users/{user\_id}/roles

##### [Retrieve project user role](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/retrieve)

$ openai admin:organization:projects:users:roles retrieve

GET/projects/{project\_id}/users/{user\_id}/roles/{role\_id}

##### [Unassign project role from user](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/users/subresources/roles/methods/delete)

$ openai admin:organization:projects:users:roles delete

DELETE/projects/{project\_id}/users/{user\_id}/roles/{role\_id}
