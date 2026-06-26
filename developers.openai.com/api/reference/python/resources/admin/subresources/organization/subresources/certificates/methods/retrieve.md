<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/certificates/methods/retrieve/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Certificates](/api/reference/python/resources/admin/subresources/organization/subresources/certificates)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Get certificate

admin.organization.certificates.retrieve(strcertificate\_id, CertificateRetrieveParams\*\*kwargs)  -> [Certificate](/api/reference/python/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema))

GET/organization/certificates/{certificate\_id}

Get a certificate that has been uploaded to the organization.

You can get a certificate regardless of whether it is active or not.

##### ParametersExpand Collapse

certificate\_id: str

include: Optional[List[Literal["content"]]]

A list of additional fields to include in the response. Currently the only supported value is `content` to fetch the PEM content of the certificate.

##### ReturnsExpand Collapse

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

### Get certificate

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
certificate = client.admin.organization.certificates.retrieve(
    certificate_id="certificate_id",
print(certificate.id)

  "object": "certificate",
  "id": "cert_abc",
  "name": "My Example Certificate",
  "created_at": 1234567,
  "certificate_details": {
    "valid_at": 1234567,
    "expires_at": 12345678,
    "content": "-----BEGIN CERTIFICATE-----MIIDeT...-----END CERTIFICATE-----"

##### Returns Examples

  "object": "certificate",
  "id": "cert_abc",
  "name": "My Example Certificate",
  "created_at": 1234567,
  "certificate_details": {
    "valid_at": 1234567,
    "expires_at": 12345678,
    "content": "-----BEGIN CERTIFICATE-----MIIDeT...-----END CERTIFICATE-----"
