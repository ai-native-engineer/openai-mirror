<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/certificates/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Certificates

##### [List organization certificates](/api/reference/resources/admin/subresources/organization/subresources/certificates/methods/list)

GET/organization/certificates

##### [Upload certificate](/api/reference/resources/admin/subresources/organization/subresources/certificates/methods/create)

POST/organization/certificates

##### [Get certificate](/api/reference/resources/admin/subresources/organization/subresources/certificates/methods/retrieve)

GET/organization/certificates/{certificate\_id}

##### [Modify certificate](/api/reference/resources/admin/subresources/organization/subresources/certificates/methods/update)

POST/organization/certificates/{certificate\_id}

##### [Delete certificate](/api/reference/resources/admin/subresources/organization/subresources/certificates/methods/delete)

DELETE/organization/certificates/{certificate\_id}

##### [Activate certificates for organization](/api/reference/resources/admin/subresources/organization/subresources/certificates/methods/activate)

POST/organization/certificates/activate

##### [Deactivate certificates for organization](/api/reference/resources/admin/subresources/organization/subresources/certificates/methods/deactivate)

POST/organization/certificates/deactivate

##### ModelsExpand Collapse

Certificate object { id, certificate\_details, created\_at, 3 more }

Represents an individual `certificate` uploaded to the organization.

id: string

The identifier, which can be referenced in API endpoints

certificate\_details: object { content, expires\_at, valid\_at }

content: optional string

The content of the certificate in PEM format.

expires\_at: optional number

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

valid\_at: optional number

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

created\_at: number

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

name: string

The name of the certificate.

object: "certificate" or "organization.certificate" or "organization.project.certificate"

The object type.

* If creating, updating, or getting a specific certificate, the object type is `certificate`.
* If listing, activating, or deactivating certificates for the organization, the object type is `organization.certificate`.
* If listing, activating, or deactivating certificates for a project, the object type is `organization.project.certificate`.

One of the following:

"certificate"

"organization.certificate"

"organization.project.certificate"

active: optional boolean

Whether the certificate is currently active at the specified scope. Not returned when getting details for a specific certificate.

CertificateListResponse object { id, active, certificate\_details, 3 more }

Represents an individual certificate configured at the organization level.

id: string

The identifier, which can be referenced in API endpoints

active: boolean

Whether the certificate is currently active at the organization level.

certificate\_details: object { expires\_at, valid\_at }

expires\_at: optional number

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

valid\_at: optional number

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

created\_at: number

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

name: string

The name of the certificate.

object: "organization.certificate"

The object type, which is always `organization.certificate`.

CertificateDeleteResponse object { id, object }

id: string

The ID of the certificate that was deleted.

object: "certificate.deleted"

The object type, must be `certificate.deleted`.

CertificateActivateResponse object { id, active, certificate\_details, 3 more }

Represents an individual certificate configured at the organization level.

id: string

The identifier, which can be referenced in API endpoints

active: boolean

Whether the certificate is currently active at the organization level.

certificate\_details: object { expires\_at, valid\_at }

expires\_at: optional number

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

valid\_at: optional number

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

created\_at: number

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

name: string

The name of the certificate.

object: "organization.certificate"

The object type, which is always `organization.certificate`.

CertificateDeactivateResponse object { id, active, certificate\_details, 3 more }

Represents an individual certificate configured at the organization level.

id: string

The identifier, which can be referenced in API endpoints

active: boolean

Whether the certificate is currently active at the organization level.

certificate\_details: object { expires\_at, valid\_at }

expires\_at: optional number

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

valid\_at: optional number

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

created\_at: number

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

name: string

The name of the certificate.

object: "organization.certificate"

The object type, which is always `organization.certificate`.
