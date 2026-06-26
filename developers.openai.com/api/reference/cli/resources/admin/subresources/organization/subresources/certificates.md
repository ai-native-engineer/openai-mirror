<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/certificates/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Certificates

##### [List organization certificates](/api/reference/cli/resources/admin/subresources/organization/subresources/certificates/methods/list)

$ openai admin:organization:certificates list

GET/organization/certificates

##### [Upload certificate](/api/reference/cli/resources/admin/subresources/organization/subresources/certificates/methods/create)

$ openai admin:organization:certificates create

POST/organization/certificates

##### [Get certificate](/api/reference/cli/resources/admin/subresources/organization/subresources/certificates/methods/retrieve)

$ openai admin:organization:certificates retrieve

GET/organization/certificates/{certificate\_id}

##### [Modify certificate](/api/reference/cli/resources/admin/subresources/organization/subresources/certificates/methods/update)

$ openai admin:organization:certificates update

POST/organization/certificates/{certificate\_id}

##### [Delete certificate](/api/reference/cli/resources/admin/subresources/organization/subresources/certificates/methods/delete)

$ openai admin:organization:certificates delete

DELETE/organization/certificates/{certificate\_id}

##### [Activate certificates for organization](/api/reference/cli/resources/admin/subresources/organization/subresources/certificates/methods/activate)

$ openai admin:organization:certificates activate

POST/organization/certificates/activate

##### [Deactivate certificates for organization](/api/reference/cli/resources/admin/subresources/organization/subresources/certificates/methods/deactivate)

$ openai admin:organization:certificates deactivate

POST/organization/certificates/deactivate

##### ModelsExpand Collapse

certificate: object { id, certificate\_details, created\_at, 3 more }

Represents an individual `certificate` uploaded to the organization.

id: string

The identifier, which can be referenced in API endpoints

certificate\_details: object { content, expires\_at, valid\_at }

content: optional string

The content of the certificate in PEM format.

expires\_at: optional number

The Unix timestamp (in seconds) of when the certificate expires.

valid\_at: optional number

The Unix timestamp (in seconds) of when the certificate becomes valid.

created\_at: number

The Unix timestamp (in seconds) of when the certificate was uploaded.

name: string

The name of the certificate.

object: "certificate" or "organization.certificate" or "organization.project.certificate"

The object type.

* If creating, updating, or getting a specific certificate, the object type is `certificate`.
* If listing, activating, or deactivating certificates for the organization, the object type is `organization.certificate`.
* If listing, activating, or deactivating certificates for a project, the object type is `organization.project.certificate`.

"certificate"

"organization.certificate"

"organization.project.certificate"

active: optional boolean

Whether the certificate is currently active at the specified scope. Not returned when getting details for a specific certificate.
