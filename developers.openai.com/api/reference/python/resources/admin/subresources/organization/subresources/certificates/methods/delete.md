<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/certificates/methods/delete/ -->

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

# Delete certificate

admin.organization.certificates.delete(strcertificate\_id)  -> [CertificateDeleteResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate_delete_response%20%3E%20(schema))

DELETE/organization/certificates/{certificate\_id}

Delete a certificate from the organization.

The certificate must be inactive for the organization and all projects.

##### ParametersExpand Collapse

certificate\_id: str

##### ReturnsExpand Collapse

class CertificateDeleteResponse: …

id: str

The ID of the certificate that was deleted.

object: Literal["certificate.deleted"]

The object type, must be `certificate.deleted`.

### Delete certificate

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
certificate = client.admin.organization.certificates.delete(
    "certificate_id",
print(certificate.id)

  "object": "certificate.deleted",
  "id": "cert_abc"

##### Returns Examples

  "object": "certificate.deleted",
  "id": "cert_abc"
