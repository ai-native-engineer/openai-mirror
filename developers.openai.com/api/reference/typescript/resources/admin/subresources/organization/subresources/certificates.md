<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/certificates/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Certificates

##### [List organization certificates](/api/reference/typescript/resources/admin/subresources/organization/subresources/certificates/methods/list)

client.admin.organization.certificates.list(CertificateListParams { after, limit, order } query?, RequestOptionsoptions?): ConversationCursorPage<[CertificateListResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate_list_response%20%3E%20(schema)) { id, active, certificate\_details, 3 more } >

GET/organization/certificates

##### [Upload certificate](/api/reference/typescript/resources/admin/subresources/organization/subresources/certificates/methods/create)

client.admin.organization.certificates.create(CertificateCreateParams { certificate, name } body, RequestOptionsoptions?): [Certificate](/api/reference/typescript/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema)) { id, certificate\_details, created\_at, 3 more }

POST/organization/certificates

##### [Get certificate](/api/reference/typescript/resources/admin/subresources/organization/subresources/certificates/methods/retrieve)

client.admin.organization.certificates.retrieve(stringcertificateID, CertificateRetrieveParams { include } query?, RequestOptionsoptions?): [Certificate](/api/reference/typescript/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema)) { id, certificate\_details, created\_at, 3 more }

GET/organization/certificates/{certificate\_id}

##### [Modify certificate](/api/reference/typescript/resources/admin/subresources/organization/subresources/certificates/methods/update)

client.admin.organization.certificates.update(stringcertificateID, CertificateUpdateParams { name } body, RequestOptionsoptions?): [Certificate](/api/reference/typescript/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema)) { id, certificate\_details, created\_at, 3 more }

POST/organization/certificates/{certificate\_id}

##### [Delete certificate](/api/reference/typescript/resources/admin/subresources/organization/subresources/certificates/methods/delete)

client.admin.organization.certificates.delete(stringcertificateID, RequestOptionsoptions?): [CertificateDeleteResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate_delete_response%20%3E%20(schema)) { id, object }

DELETE/organization/certificates/{certificate\_id}

##### [Activate certificates for organization](/api/reference/typescript/resources/admin/subresources/organization/subresources/certificates/methods/activate)

client.admin.organization.certificates.activate(CertificateActivateParams { certificate\_ids } body, RequestOptionsoptions?): Page<[CertificateActivateResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate_activate_response%20%3E%20(schema)) { id, active, certificate\_details, 3 more } >

POST/organization/certificates/activate

##### [Deactivate certificates for organization](/api/reference/typescript/resources/admin/subresources/organization/subresources/certificates/methods/deactivate)

client.admin.organization.certificates.deactivate(CertificateDeactivateParams { certificate\_ids } body, RequestOptionsoptions?): Page<[CertificateDeactivateResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate_deactivate_response%20%3E%20(schema)) { id, active, certificate\_details, 3 more } >

POST/organization/certificates/deactivate

##### ModelsExpand Collapse

Certificate { id, certificate\_details, created\_at, 3 more }

Represents an individual `certificate` uploaded to the organization.

id: string

The identifier, which can be referenced in API endpoints

certificate\_details: CertificateDetails { content, expires\_at, valid\_at }

content?: string

The content of the certificate in PEM format.

expires\_at?: number

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

valid\_at?: number

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

created\_at: number

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

name: string | null

The name of the certificate.

object: "certificate" | "organization.certificate" | "organization.project.certificate"

The object type.

* If creating, updating, or getting a specific certificate, the object type is `certificate`.
* If listing, activating, or deactivating certificates for the organization, the object type is `organization.certificate`.
* If listing, activating, or deactivating certificates for a project, the object type is `organization.project.certificate`.

One of the following:

"certificate"

"organization.certificate"

"organization.project.certificate"

active?: boolean

Whether the certificate is currently active at the specified scope. Not returned when getting details for a specific certificate.

CertificateListResponse { id, active, certificate\_details, 3 more }

Represents an individual certificate configured at the organization level.

id: string

The identifier, which can be referenced in API endpoints

active: boolean

Whether the certificate is currently active at the organization level.

certificate\_details: CertificateDetails { expires\_at, valid\_at }

expires\_at?: number

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

valid\_at?: number

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

created\_at: number

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

name: string | null

The name of the certificate.

object: "organization.certificate"

The object type, which is always `organization.certificate`.

CertificateDeleteResponse { id, object }

id: string

The ID of the certificate that was deleted.

object: "certificate.deleted"

The object type, must be `certificate.deleted`.

CertificateActivateResponse { id, active, certificate\_details, 3 more }

Represents an individual certificate configured at the organization level.

id: string

The identifier, which can be referenced in API endpoints

active: boolean

Whether the certificate is currently active at the organization level.

certificate\_details: CertificateDetails { expires\_at, valid\_at }

expires\_at?: number

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

valid\_at?: number

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

created\_at: number

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

name: string | null

The name of the certificate.

object: "organization.certificate"

The object type, which is always `organization.certificate`.

CertificateDeactivateResponse { id, active, certificate\_details, 3 more }

Represents an individual certificate configured at the organization level.

id: string

The identifier, which can be referenced in API endpoints

active: boolean

Whether the certificate is currently active at the organization level.

certificate\_details: CertificateDetails { expires\_at, valid\_at }

expires\_at?: number

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

valid\_at?: number

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

created\_at: number

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

name: string | null

The name of the certificate.

object: "organization.certificate"

The object type, which is always `organization.certificate`.
