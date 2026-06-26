<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/users/subresources/roles/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Users](/api/reference/java/resources/admin/subresources/organization/subresources/users)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Roles

##### [List user organization role assignments](/api/reference/java/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/list)

RoleListPage admin().organization().users().roles().list(RoleListParamsparams = RoleListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/users/{user\_id}/roles

##### [Assign organization role to user](/api/reference/java/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/create)

[RoleCreateResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20RoleCreateResponse%20%3E%20(schema)) admin().organization().users().roles().create(RoleCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/users/{user\_id}/roles

##### [Retrieve user organization role](/api/reference/java/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/retrieve)

[RoleRetrieveResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20RoleRetrieveResponse%20%3E%20(schema)) admin().organization().users().roles().retrieve(RoleRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/users/{user\_id}/roles/{role\_id}

##### [Unassign organization role from user](/api/reference/java/resources/admin/subresources/organization/subresources/users/subresources/roles/methods/delete)

[RoleDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.users.roles%20%3E%20(model)%20RoleDeleteResponse%20%3E%20(schema)) admin().organization().users().roles().delete(RoleDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/users/{user\_id}/roles/{role\_id}
