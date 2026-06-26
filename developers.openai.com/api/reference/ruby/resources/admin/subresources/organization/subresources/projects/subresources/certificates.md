<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/certificates/ -->

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

# Certificates

##### [List project certificates](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/list)

admin.organization.projects.certificates.list(project\_id, \*\*kwargs) -> ConversationCursorPage<[CertificateListResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_list_response%20%3E%20(schema)) { id, active, certificate\_details, 3 more } >

GET/organization/projects/{project\_id}/certificates

##### [Activate certificates for project](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/activate)

admin.organization.projects.certificates.activate(project\_id, \*\*kwargs) -> Page<[CertificateActivateResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_activate_response%20%3E%20(schema)) { id, active, certificate\_details, 3 more } >

POST/organization/projects/{project\_id}/certificates/activate

##### [Deactivate certificates for project](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/deactivate)

admin.organization.projects.certificates.deactivate(project\_id, \*\*kwargs) -> Page<[CertificateDeactivateResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_deactivate_response%20%3E%20(schema)) { id, active, certificate\_details, 3 more } >

POST/organization/projects/{project\_id}/certificates/deactivate

##### ModelsExpand Collapse

class CertificateListResponse { id, active, certificate\_details, 3 more }

Represents an individual certificate configured at the project level.

id: String

The identifier, which can be referenced in API endpoints

active: bool

Whether the certificate is currently active at the project level.

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

object: :"organization.project.certificate"

The object type, which is always `organization.project.certificate`.

class CertificateActivateResponse { id, active, certificate\_details, 3 more }

Represents an individual certificate configured at the project level.

id: String

The identifier, which can be referenced in API endpoints

active: bool

Whether the certificate is currently active at the project level.

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

object: :"organization.project.certificate"

The object type, which is always `organization.project.certificate`.

class CertificateDeactivateResponse { id, active, certificate\_details, 3 more }

Represents an individual certificate configured at the project level.

id: String

The identifier, which can be referenced in API endpoints

active: bool

Whether the certificate is currently active at the project level.

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

object: :"organization.project.certificate"

The object type, which is always `organization.project.certificate`.
