<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/data_retention/ -->

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

# Data Retention

##### [Retrieve organization data retention](/api/reference/java/resources/admin/subresources/organization/subresources/data_retention/methods/retrieve)

[OrganizationDataRetention](/api/reference/java/resources/admin#(resource)%20admin.organization.data_retention%20%3E%20(model)%20organization_data_retention%20%3E%20(schema)) admin().organization().dataRetention().retrieve(DataRetentionRetrieveParamsparams = DataRetentionRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/data\_retention

##### [Update organization data retention](/api/reference/java/resources/admin/subresources/organization/subresources/data_retention/methods/update)

[OrganizationDataRetention](/api/reference/java/resources/admin#(resource)%20admin.organization.data_retention%20%3E%20(model)%20organization_data_retention%20%3E%20(schema)) admin().organization().dataRetention().update(DataRetentionUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/data\_retention

##### ModelsExpand Collapse

class OrganizationDataRetention:

Represents the organization’s data retention control setting.

JsonValue; object\_ "organization.data\_retention"constant"organization.data\_retention"constant

The object type, which is always `organization.data_retention`.

Type type

The configured organization data retention type.

One of the following:

ZERO\_DATA\_RETENTION("zero\_data\_retention")

MODIFIED\_ABUSE\_MONITORING("modified\_abuse\_monitoring")

ENHANCED\_ZERO\_DATA\_RETENTION("enhanced\_zero\_data\_retention")

ENHANCED\_MODIFIED\_ABUSE\_MONITORING("enhanced\_modified\_abuse\_monitoring")
