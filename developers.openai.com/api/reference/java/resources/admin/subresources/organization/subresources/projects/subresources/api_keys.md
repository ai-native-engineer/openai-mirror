<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/ -->

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

# API Keys

##### [List project API keys](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/list)

ApiKeyListPage admin().organization().projects().apiKeys().list(ApiKeyListParamsparams = ApiKeyListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}/api\_keys

##### [Retrieve project API key](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/retrieve)

[ProjectApiKey](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)) admin().organization().projects().apiKeys().retrieve(ApiKeyRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/projects/{project\_id}/api\_keys/{api\_key\_id}

##### [Delete project API key](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/delete)

[ApiKeyDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20ApiKeyDeleteResponse%20%3E%20(schema)) admin().organization().projects().apiKeys().delete(ApiKeyDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/projects/{project\_id}/api\_keys/{api\_key\_id}

##### ModelsExpand Collapse

class ProjectApiKey:

Represents an individual API key in a project.

String id

The identifier, which can be referenced in API endpoints

long createdAt

The Unix timestamp (in seconds) of when the API key was created

formatunixtime

Optional<Long> lastUsedAt

The Unix timestamp (in seconds) of when the API key was last used.

formatunixtime

String name

The name of the API key

JsonValue; object\_ "organization.project.api\_key"constant"organization.project.api\_key"constant

The object type, which is always `organization.project.api_key`

Owner owner

Optional<ServiceAccount> serviceAccount

The service account that owns a project API key.

String id

The identifier, which can be referenced in API endpoints

long createdAt

The Unix timestamp (in seconds) of when the service account was created.

formatunixtime

String name

The name of the service account.

String role

The service account’s project role.

Optional<Type> type

`user` or `service_account`

One of the following:

USER("user")

SERVICE\_ACCOUNT("service\_account")

Optional<User> user

The user that owns a project API key.

String id

The identifier, which can be referenced in API endpoints

long createdAt

The Unix timestamp (in seconds) of when the user was created.

formatunixtime

String email

The email address of the user.

String name

The name of the user.

String role

The user’s project role.

String redactedValue

The redacted value of the API key
