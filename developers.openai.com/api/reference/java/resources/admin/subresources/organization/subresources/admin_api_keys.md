<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/admin_api_keys/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Admin API Keys

##### [List all organization and project API keys.](/api/reference/java/resources/admin/subresources/organization/subresources/admin_api_keys/methods/list)

AdminApiKeyListPage admin().organization().adminApiKeys().list(AdminApiKeyListParamsparams = AdminApiKeyListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/admin\_api\_keys

##### [Create admin API key](/api/reference/java/resources/admin/subresources/organization/subresources/admin_api_keys/methods/create)

[AdminApiKeyCreateResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20AdminApiKeyCreateResponse%20%3E%20(schema)) admin().organization().adminApiKeys().create(AdminApiKeyCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/admin\_api\_keys

##### [Retrieve admin API key](/api/reference/java/resources/admin/subresources/organization/subresources/admin_api_keys/methods/retrieve)

[AdminApiKey](/api/reference/java/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20admin_api_key%20%3E%20(schema)) admin().organization().adminApiKeys().retrieve(AdminApiKeyRetrieveParamsparams = AdminApiKeyRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/admin\_api\_keys/{key\_id}

##### [Delete admin API key](/api/reference/java/resources/admin/subresources/organization/subresources/admin_api_keys/methods/delete)

[AdminApiKeyDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.admin_api_keys%20%3E%20(model)%20AdminApiKeyDeleteResponse%20%3E%20(schema)) admin().organization().adminApiKeys().delete(AdminApiKeyDeleteParamsparams = AdminApiKeyDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/admin\_api\_keys/{key\_id}

##### ModelsExpand Collapse

class AdminApiKey:

Represents an individual Admin API key in an org.

String id

The identifier, which can be referenced in API endpoints

long createdAt

The Unix timestamp (in seconds) of when the API key was created

formatunixtime

Optional<Long> expiresAt

The Unix timestamp (in seconds) of when the API key expires

formatunixtime

JsonValue; object\_ "organization.admin\_api\_key"constant"organization.admin\_api\_key"constant

The object type, which is always `organization.admin_api_key`

Owner owner

Optional<String> id

The identifier, which can be referenced in API endpoints

Optional<Long> createdAt

The Unix timestamp (in seconds) of when the user was created

formatunixtime

Optional<String> name

The name of the user

Optional<String> object\_

The object type, which is always organization.user

Optional<String> role

Always `owner`

Optional<String> type

Always `user`

String redactedValue

The redacted value of the API key

Optional<Long> lastUsedAt

The Unix timestamp (in seconds) of when the API key was last used

formatunixtime

Optional<String> name

The name of the API key
