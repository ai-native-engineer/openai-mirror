<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/certificates/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Certificates

##### [List organization certificates](/api/reference/python/resources/admin/subresources/organization/subresources/certificates/methods/list)

admin.organization.certificates.list(CertificateListParams\*\*kwargs)  -> SyncConversationCursorPage[[CertificateListResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate_list_response%20%3E%20(schema))]

GET/organization/certificates

##### [Upload certificate](/api/reference/python/resources/admin/subresources/organization/subresources/certificates/methods/create)

admin.organization.certificates.create(CertificateCreateParams\*\*kwargs)  -> [Certificate](/api/reference/python/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema))

POST/organization/certificates

##### [Get certificate](/api/reference/python/resources/admin/subresources/organization/subresources/certificates/methods/retrieve)

admin.organization.certificates.retrieve(strcertificate\_id, CertificateRetrieveParams\*\*kwargs)  -> [Certificate](/api/reference/python/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema))

GET/organization/certificates/{certificate\_id}

##### [Modify certificate](/api/reference/python/resources/admin/subresources/organization/subresources/certificates/methods/update)

admin.organization.certificates.update(strcertificate\_id, CertificateUpdateParams\*\*kwargs)  -> [Certificate](/api/reference/python/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema))

POST/organization/certificates/{certificate\_id}

##### [Delete certificate](/api/reference/python/resources/admin/subresources/organization/subresources/certificates/methods/delete)

admin.organization.certificates.delete(strcertificate\_id)  -> [CertificateDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate_delete_response%20%3E%20(schema))

DELETE/organization/certificates/{certificate\_id}

##### [Activate certificates for organization](/api/reference/python/resources/admin/subresources/organization/subresources/certificates/methods/activate)

admin.organization.certificates.activate(CertificateActivateParams\*\*kwargs)  -> SyncPage[[CertificateActivateResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate_activate_response%20%3E%20(schema))]

POST/organization/certificates/activate

##### [Deactivate certificates for organization](/api/reference/python/resources/admin/subresources/organization/subresources/certificates/methods/deactivate)

admin.organization.certificates.deactivate(CertificateDeactivateParams\*\*kwargs)  -> SyncPage[[CertificateDeactivateResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate_deactivate_response%20%3E%20(schema))]

POST/organization/certificates/deactivate

##### ModelsExpand Collapse

class Certificate: …

Represents an individual `certificate` uploaded to the organization.

id: str

The identifier, which can be referenced in API endpoints

certificate\_details: CertificateDetails

content: Optional[str]

The content of the certificate in PEM format.

expires\_at: Optional[int]

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

valid\_at: Optional[int]

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

created\_at: int

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

name: Optional[str]

The name of the certificate.

object: Literal["certificate", "organization.certificate", "organization.project.certificate"]

The object type.

* If creating, updating, or getting a specific certificate, the object type is `certificate`.
* If listing, activating, or deactivating certificates for the organization, the object type is `organization.certificate`.
* If listing, activating, or deactivating certificates for a project, the object type is `organization.project.certificate`.

One of the following:

"certificate"

"organization.certificate"

"organization.project.certificate"

active: Optional[bool]

Whether the certificate is currently active at the specified scope. Not returned when getting details for a specific certificate.

class CertificateListResponse: …

Represents an individual certificate configured at the organization level.

id: str

The identifier, which can be referenced in API endpoints

active: bool

Whether the certificate is currently active at the organization level.

certificate\_details: CertificateDetails

expires\_at: Optional[int]

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

valid\_at: Optional[int]

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

created\_at: int

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

name: Optional[str]

The name of the certificate.

object: Literal["organization.certificate"]

The object type, which is always `organization.certificate`.

class CertificateDeleteResponse: …

id: str

The ID of the certificate that was deleted.

object: Literal["certificate.deleted"]

The object type, must be `certificate.deleted`.

class CertificateActivateResponse: …

Represents an individual certificate configured at the organization level.

id: str

The identifier, which can be referenced in API endpoints

active: bool

Whether the certificate is currently active at the organization level.

certificate\_details: CertificateDetails

expires\_at: Optional[int]

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

valid\_at: Optional[int]

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

created\_at: int

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

name: Optional[str]

The name of the certificate.

object: Literal["organization.certificate"]

The object type, which is always `organization.certificate`.

class CertificateDeactivateResponse: …

Represents an individual certificate configured at the organization level.

id: str

The identifier, which can be referenced in API endpoints

active: bool

Whether the certificate is currently active at the organization level.

certificate\_details: CertificateDetails

expires\_at: Optional[int]

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

valid\_at: Optional[int]

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

created\_at: int

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

name: Optional[str]

The name of the certificate.

object: Literal["organization.certificate"]

The object type, which is always `organization.certificate`.
