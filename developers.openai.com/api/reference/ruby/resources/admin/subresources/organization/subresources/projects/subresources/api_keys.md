<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/ -->

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

# API Keys

##### [List project API keys](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/list)

admin.organization.projects.api\_keys.list(project\_id, \*\*kwargs) -> ConversationCursorPage<[ProjectAPIKey](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)) { id, created\_at, last\_used\_at, 4 more } >

GET/organization/projects/{project\_id}/api\_keys

##### [Retrieve project API key](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/retrieve)

admin.organization.projects.api\_keys.retrieve(api\_key\_id, \*\*kwargs) -> [ProjectAPIKey](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)) { id, created\_at, last\_used\_at, 4 more }

GET/organization/projects/{project\_id}/api\_keys/{api\_key\_id}

##### [Delete project API key](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/delete)

admin.organization.projects.api\_keys.delete(api\_key\_id, \*\*kwargs) -> [APIKeyDeleteResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20api_key_delete_response%20%3E%20(schema)) { id, deleted, object }

DELETE/organization/projects/{project\_id}/api\_keys/{api\_key\_id}

##### ModelsExpand Collapse

class ProjectAPIKey { id, created\_at, last\_used\_at, 4 more }

Represents an individual API key in a project.

id: String

The identifier, which can be referenced in API endpoints

created\_at: Integer

The Unix timestamp (in seconds) of when the API key was created

formatunixtime

last\_used\_at: Integer

The Unix timestamp (in seconds) of when the API key was last used.

formatunixtime

name: String

The name of the API key

object: :"organization.project.api\_key"

The object type, which is always `organization.project.api_key`

owner: Owner{ service\_account, type, user}

service\_account: ServiceAccount{ id, created\_at, name, role}

The service account that owns a project API key.

id: String

The identifier, which can be referenced in API endpoints

created\_at: Integer

The Unix timestamp (in seconds) of when the service account was created.

formatunixtime

name: String

The name of the service account.

role: String

The service account’s project role.

type: :user | :service\_account

`user` or `service_account`

One of the following:

:user

:service\_account

user: User{ id, created\_at, email, 2 more}

The user that owns a project API key.

id: String

The identifier, which can be referenced in API endpoints

created\_at: Integer

The Unix timestamp (in seconds) of when the user was created.

formatunixtime

email: String

The email address of the user.

name: String

The name of the user.

role: String

The user’s project role.

redacted\_value: String

The redacted value of the API key

class APIKeyDeleteResponse { id, deleted, object }

id: String

deleted: bool

object: :"organization.project.api\_key.deleted"
