<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/certificates/methods/retrieve/ -->

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

# Get certificate

client.admin.organization.certificates.retrieve(stringcertificateID, CertificateRetrieveParams { include } query?, RequestOptionsoptions?): [Certificate](/api/reference/typescript/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema)) { id, certificate\_details, created\_at, 3 more }

GET/organization/certificates/{certificate\_id}

Get a certificate that has been uploaded to the organization.

You can get a certificate regardless of whether it is active or not.

##### ParametersExpand Collapse

certificateID: string

query: CertificateRetrieveParams { include }

include?: Array<"content">

A list of additional fields to include in the response. Currently the only supported value is `content` to fetch the PEM content of the certificate.

##### ReturnsExpand Collapse

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

### Get certificate

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

const certificate = await client.admin.organization.certificates.retrieve('certificate_id');

console.log(certificate.id);

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
