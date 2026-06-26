<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/ -->

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

# API Keys

##### [List project API keys](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/list)

client.Admin.Organization.Projects.APIKeys.List(ctx, projectID, query) (\*ConversationCursorPage[[ProjectAPIKey](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema))], error)

GET/organization/projects/{project\_id}/api\_keys

##### [Retrieve project API key](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/retrieve)

client.Admin.Organization.Projects.APIKeys.Get(ctx, projectID, apiKeyID) (\*[ProjectAPIKey](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20project_api_key%20%3E%20(schema)), error)

GET/organization/projects/{project\_id}/api\_keys/{api\_key\_id}

##### [Delete project API key](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/api_keys/methods/delete)

client.Admin.Organization.Projects.APIKeys.Delete(ctx, projectID, apiKeyID) (\*[AdminOrganizationProjectAPIKeyDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.api_keys%20%3E%20(model)%20AdminOrganizationProjectAPIKeyDeleteResponse%20%3E%20(schema)), error)

DELETE/organization/projects/{project\_id}/api\_keys/{api\_key\_id}

##### ModelsExpand Collapse

type ProjectAPIKey struct{…}

Represents an individual API key in a project.

ID string

The identifier, which can be referenced in API endpoints

CreatedAt int64

The Unix timestamp (in seconds) of when the API key was created

formatunixtime

LastUsedAt int64

The Unix timestamp (in seconds) of when the API key was last used.

formatunixtime

Name string

The name of the API key

Object OrganizationProjectAPIKey

The object type, which is always `organization.project.api_key`

Owner ProjectAPIKeyOwner

ServiceAccount ProjectAPIKeyOwnerServiceAccountOptional

The service account that owns a project API key.

ID string

The identifier, which can be referenced in API endpoints

CreatedAt int64

The Unix timestamp (in seconds) of when the service account was created.

formatunixtime

Name string

The name of the service account.

Role string

The service account’s project role.

Type stringOptional

`user` or `service_account`

One of the following:

const ProjectAPIKeyOwnerTypeUser ProjectAPIKeyOwnerType = "user"

const ProjectAPIKeyOwnerTypeServiceAccount ProjectAPIKeyOwnerType = "service\_account"

User ProjectAPIKeyOwnerUserOptional

The user that owns a project API key.

ID string

The identifier, which can be referenced in API endpoints

CreatedAt int64

The Unix timestamp (in seconds) of when the user was created.

formatunixtime

Email string

The email address of the user.

Name string

The name of the user.

Role string

The user’s project role.

RedactedValue string

The redacted value of the API key
