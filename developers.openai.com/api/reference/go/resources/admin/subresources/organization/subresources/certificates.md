<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/certificates/ -->

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

# Certificates

##### [List organization certificates](/api/reference/go/resources/admin/subresources/organization/subresources/certificates/methods/list)

client.Admin.Organization.Certificates.List(ctx, query) (\*ConversationCursorPage[[AdminOrganizationCertificateListResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20AdminOrganizationCertificateListResponse%20%3E%20(schema))], error)

GET/organization/certificates

##### [Upload certificate](/api/reference/go/resources/admin/subresources/organization/subresources/certificates/methods/create)

client.Admin.Organization.Certificates.New(ctx, body) (\*[Certificate](/api/reference/go/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema)), error)

POST/organization/certificates

##### [Get certificate](/api/reference/go/resources/admin/subresources/organization/subresources/certificates/methods/retrieve)

client.Admin.Organization.Certificates.Get(ctx, certificateID, query) (\*[Certificate](/api/reference/go/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema)), error)

GET/organization/certificates/{certificate\_id}

##### [Modify certificate](/api/reference/go/resources/admin/subresources/organization/subresources/certificates/methods/update)

client.Admin.Organization.Certificates.Update(ctx, certificateID, body) (\*[Certificate](/api/reference/go/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema)), error)

POST/organization/certificates/{certificate\_id}

##### [Delete certificate](/api/reference/go/resources/admin/subresources/organization/subresources/certificates/methods/delete)

client.Admin.Organization.Certificates.Delete(ctx, certificateID) (\*[AdminOrganizationCertificateDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20AdminOrganizationCertificateDeleteResponse%20%3E%20(schema)), error)

DELETE/organization/certificates/{certificate\_id}

##### [Activate certificates for organization](/api/reference/go/resources/admin/subresources/organization/subresources/certificates/methods/activate)

client.Admin.Organization.Certificates.Activate(ctx, body) (\*Page[[AdminOrganizationCertificateActivateResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20AdminOrganizationCertificateActivateResponse%20%3E%20(schema))], error)

POST/organization/certificates/activate

##### [Deactivate certificates for organization](/api/reference/go/resources/admin/subresources/organization/subresources/certificates/methods/deactivate)

client.Admin.Organization.Certificates.Deactivate(ctx, body) (\*Page[[AdminOrganizationCertificateDeactivateResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20AdminOrganizationCertificateDeactivateResponse%20%3E%20(schema))], error)

POST/organization/certificates/deactivate

##### ModelsExpand Collapse

type Certificate struct{…}

Represents an individual `certificate` uploaded to the organization.

ID string

The identifier, which can be referenced in API endpoints

CertificateDetails CertificateCertificateDetails

Content stringOptional

The content of the certificate in PEM format.

ExpiresAt int64Optional

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

ValidAt int64Optional

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

CreatedAt int64

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

Name string

The name of the certificate.

Object CertificateObject

The object type.

* If creating, updating, or getting a specific certificate, the object type is `certificate`.
* If listing, activating, or deactivating certificates for the organization, the object type is `organization.certificate`.
* If listing, activating, or deactivating certificates for a project, the object type is `organization.project.certificate`.

One of the following:

const CertificateObjectCertificate CertificateObject = "certificate"

const CertificateObjectOrganizationCertificate CertificateObject = "organization.certificate"

const CertificateObjectOrganizationProjectCertificate CertificateObject = "organization.project.certificate"

Active boolOptional

Whether the certificate is currently active at the specified scope. Not returned when getting details for a specific certificate.
