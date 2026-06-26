<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/admin_api_keys/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Admin API Keys

##### [List all organization and project API keys.](/api/reference/go/resources/admin/subresources/organization/subresources/admin_api_keys/methods/list)

client.Admin.Organization.AdminAPIKeys.List(ctx, query) (\*CursorPage[[AdminAPIKey](/api/reference/go/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema))], error)

GET/organization/admin\_api\_keys

##### [Create admin API key](/api/reference/go/resources/admin/subresources/organization/subresources/admin_api_keys/methods/create)

client.Admin.Organization.AdminAPIKeys.New(ctx, body) (\*[AdminOrganizationAdminAPIKeyNewResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20AdminOrganizationAdminAPIKeyNewResponse%20%3E%20(schema)), error)

POST/organization/admin\_api\_keys

##### [Retrieve admin API key](/api/reference/go/resources/admin/subresources/organization/subresources/admin_api_keys/methods/retrieve)

client.Admin.Organization.AdminAPIKeys.Get(ctx, keyID) (\*[AdminAPIKey](/api/reference/go/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)), error)

GET/organization/admin\_api\_keys/{key\_id}

##### [Delete admin API key](/api/reference/go/resources/admin/subresources/organization/subresources/admin_api_keys/methods/delete)

client.Admin.Organization.AdminAPIKeys.Delete(ctx, keyID) (\*[AdminOrganizationAdminAPIKeyDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20AdminOrganizationAdminAPIKeyDeleteResponse%20%3E%20(schema)), error)

DELETE/organization/admin\_api\_keys/{key\_id}

##### ModelsExpand Collapse

type AdminAPIKey struct{…}

Represents an individual Admin API key in an org.

ID string

The identifier, which can be referenced in API endpoints

CreatedAt int64

The Unix timestamp (in seconds) of when the API key was created

formatunixtime

ExpiresAt int64

The Unix timestamp (in seconds) of when the API key expires

formatunixtime

Object OrganizationAdminAPIKey

The object type, which is always `organization.admin_api_key`

Owner AdminAPIKeyOwner

ID stringOptional

The identifier, which can be referenced in API endpoints

CreatedAt int64Optional

The Unix timestamp (in seconds) of when the user was created

formatunixtime

Name stringOptional

The name of the user

Object stringOptional

The object type, which is always organization.user

Role stringOptional

Always `owner`

Type stringOptional

Always `user`

RedactedValue string

The redacted value of the API key

LastUsedAt int64Optional

The Unix timestamp (in seconds) of when the API key was last used

formatunixtime

Name stringOptional

The name of the API key
