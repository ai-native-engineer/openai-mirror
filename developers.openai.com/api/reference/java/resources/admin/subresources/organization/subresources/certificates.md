<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/certificates/ -->

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

# Certificates

##### [List organization certificates](/api/reference/java/resources/admin/subresources/organization/subresources/certificates/methods/list)

CertificateListPage admin().organization().certificates().list(CertificateListParamsparams = CertificateListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/certificates

##### [Upload certificate](/api/reference/java/resources/admin/subresources/organization/subresources/certificates/methods/create)

[Certificate](/api/reference/java/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema)) admin().organization().certificates().create(CertificateCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/certificates

##### [Get certificate](/api/reference/java/resources/admin/subresources/organization/subresources/certificates/methods/retrieve)

[Certificate](/api/reference/java/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema)) admin().organization().certificates().retrieve(CertificateRetrieveParamsparams = CertificateRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/certificates/{certificate\_id}

##### [Modify certificate](/api/reference/java/resources/admin/subresources/organization/subresources/certificates/methods/update)

[Certificate](/api/reference/java/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema)) admin().organization().certificates().update(CertificateUpdateParamsparams = CertificateUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/certificates/{certificate\_id}

##### [Delete certificate](/api/reference/java/resources/admin/subresources/organization/subresources/certificates/methods/delete)

[CertificateDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20CertificateDeleteResponse%20%3E%20(schema)) admin().organization().certificates().delete(CertificateDeleteParamsparams = CertificateDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/certificates/{certificate\_id}

##### [Activate certificates for organization](/api/reference/java/resources/admin/subresources/organization/subresources/certificates/methods/activate)

CertificateActivatePage admin().organization().certificates().activate(CertificateActivateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/certificates/activate

##### [Deactivate certificates for organization](/api/reference/java/resources/admin/subresources/organization/subresources/certificates/methods/deactivate)

CertificateDeactivatePage admin().organization().certificates().deactivate(CertificateDeactivateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/certificates/deactivate

##### ModelsExpand Collapse

class Certificate:

Represents an individual `certificate` uploaded to the organization.

String id

The identifier, which can be referenced in API endpoints

CertificateDetails certificateDetails

Optional<String> content

The content of the certificate in PEM format.

Optional<Long> expiresAt

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

Optional<Long> validAt

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

long createdAt

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

Optional<String> name

The name of the certificate.

Object object\_

The object type.

* If creating, updating, or getting a specific certificate, the object type is `certificate`.
* If listing, activating, or deactivating certificates for the organization, the object type is `organization.certificate`.
* If listing, activating, or deactivating certificates for a project, the object type is `organization.project.certificate`.

One of the following:

CERTIFICATE("certificate")

ORGANIZATION\_CERTIFICATE("organization.certificate")

ORGANIZATION\_PROJECT\_CERTIFICATE("organization.project.certificate")

Optional<Boolean> active

Whether the certificate is currently active at the specified scope. Not returned when getting details for a specific certificate.
