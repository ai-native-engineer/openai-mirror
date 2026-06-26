<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/certificates/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Certificates

##### [List organization certificates](/api/reference/ruby/resources/admin/subresources/organization/subresources/certificates/methods/list)

admin.organization.certificates.list(\*\*kwargs) -> ConversationCursorPage<[CertificateListResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate_list_response%20%3E%20(schema)) { id, active, certificate\_details, 3 more } >

GET/organization/certificates

##### [Upload certificate](/api/reference/ruby/resources/admin/subresources/organization/subresources/certificates/methods/create)

admin.organization.certificates.create(\*\*kwargs) -> [Certificate](/api/reference/ruby/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema)) { id, certificate\_details, created\_at, 3 more }

POST/organization/certificates

##### [Get certificate](/api/reference/ruby/resources/admin/subresources/organization/subresources/certificates/methods/retrieve)

admin.organization.certificates.retrieve(certificate\_id, \*\*kwargs) -> [Certificate](/api/reference/ruby/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema)) { id, certificate\_details, created\_at, 3 more }

GET/organization/certificates/{certificate\_id}

##### [Modify certificate](/api/reference/ruby/resources/admin/subresources/organization/subresources/certificates/methods/update)

admin.organization.certificates.update(certificate\_id, \*\*kwargs) -> [Certificate](/api/reference/ruby/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema)) { id, certificate\_details, created\_at, 3 more }

POST/organization/certificates/{certificate\_id}

##### [Delete certificate](/api/reference/ruby/resources/admin/subresources/organization/subresources/certificates/methods/delete)

admin.organization.certificates.delete(certificate\_id) -> [CertificateDeleteResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate_delete_response%20%3E%20(schema)) { id, object }

DELETE/organization/certificates/{certificate\_id}

##### [Activate certificates for organization](/api/reference/ruby/resources/admin/subresources/organization/subresources/certificates/methods/activate)

admin.organization.certificates.activate(\*\*kwargs) -> Page<[CertificateActivateResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate_activate_response%20%3E%20(schema)) { id, active, certificate\_details, 3 more } >

POST/organization/certificates/activate

##### [Deactivate certificates for organization](/api/reference/ruby/resources/admin/subresources/organization/subresources/certificates/methods/deactivate)

admin.organization.certificates.deactivate(\*\*kwargs) -> Page<[CertificateDeactivateResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate_deactivate_response%20%3E%20(schema)) { id, active, certificate\_details, 3 more } >

POST/organization/certificates/deactivate

##### ModelsExpand Collapse

class Certificate { id, certificate\_details, created\_at, 3 more }

Represents an individual `certificate` uploaded to the organization.

id: String

The identifier, which can be referenced in API endpoints

certificate\_details: CertificateDetails{ content, expires\_at, valid\_at}

content: String

The content of the certificate in PEM format.

expires\_at: Integer

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

valid\_at: Integer

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

created\_at: Integer

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

name: String

The name of the certificate.

object: :certificate | :"organization.certificate" | :"organization.project.certificate"

The object type.

* If creating, updating, or getting a specific certificate, the object type is `certificate`.
* If listing, activating, or deactivating certificates for the organization, the object type is `organization.certificate`.
* If listing, activating, or deactivating certificates for a project, the object type is `organization.project.certificate`.

One of the following:

:certificate

:"organization.certificate"

:"organization.project.certificate"

active: bool

Whether the certificate is currently active at the specified scope. Not returned when getting details for a specific certificate.

class CertificateListResponse { id, active, certificate\_details, 3 more }

Represents an individual certificate configured at the organization level.

id: String

The identifier, which can be referenced in API endpoints

active: bool

Whether the certificate is currently active at the organization level.

certificate\_details: CertificateDetails{ expires\_at, valid\_at}

expires\_at: Integer

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

valid\_at: Integer

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

created\_at: Integer

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

name: String

The name of the certificate.

object: :"organization.certificate"

The object type, which is always `organization.certificate`.

class CertificateDeleteResponse { id, object }

id: String

The ID of the certificate that was deleted.

object: :"certificate.deleted"

The object type, must be `certificate.deleted`.

class CertificateActivateResponse { id, active, certificate\_details, 3 more }

Represents an individual certificate configured at the organization level.

id: String

The identifier, which can be referenced in API endpoints

active: bool

Whether the certificate is currently active at the organization level.

certificate\_details: CertificateDetails{ expires\_at, valid\_at}

expires\_at: Integer

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

valid\_at: Integer

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

created\_at: Integer

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

name: String

The name of the certificate.

object: :"organization.certificate"

The object type, which is always `organization.certificate`.

class CertificateDeactivateResponse { id, active, certificate\_details, 3 more }

Represents an individual certificate configured at the organization level.

id: String

The identifier, which can be referenced in API endpoints

active: bool

Whether the certificate is currently active at the organization level.

certificate\_details: CertificateDetails{ expires\_at, valid\_at}

expires\_at: Integer

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

valid\_at: Integer

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

created\_at: Integer

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

name: String

The name of the certificate.

object: :"organization.certificate"

The object type, which is always `organization.certificate`.
