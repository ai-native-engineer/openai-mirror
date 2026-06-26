<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/certificates/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Certificates](/api/reference/typescript/resources/admin/subresources/organization/subresources/certificates)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete certificate

client.admin.organization.certificates.delete(stringcertificateID, RequestOptionsoptions?): [CertificateDeleteResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate_delete_response%20%3E%20(schema)) { id, object }

DELETE/organization/certificates/{certificate\_id}

Delete a certificate from the organization.

The certificate must be inactive for the organization and all projects.

##### ParametersExpand Collapse

certificateID: string

##### ReturnsExpand Collapse

CertificateDeleteResponse { id, object }

id: string

The ID of the certificate that was deleted.

object: "certificate.deleted"

The object type, must be `certificate.deleted`.

### Delete certificate

TypeScript

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import OpenAI from 'openai';

const client = new OpenAI({
  adminAPIKey: process.env['OPENAI_ADMIN_KEY'], // This is the default and can be omitted

const certificate = await client.admin.organization.certificates.delete('certificate_id');

console.log(certificate.id);

  "object": "certificate.deleted",
  "id": "cert_abc"

##### Returns Examples

  "object": "certificate.deleted",
  "id": "cert_abc"
