<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/certificates/methods/deactivate/ -->

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

# Deactivate certificates for organization

client.admin.organization.certificates.deactivate(CertificateDeactivateParams { certificate\_ids } body, RequestOptionsoptions?): Page<[CertificateDeactivateResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate_deactivate_response%20%3E%20(schema)) { id, active, certificate\_details, 3 more } >

POST/organization/certificates/deactivate

Deactivate certificates at the organization level.

You can atomically and idempotently deactivate up to 10 certificates at a time.

##### ParametersExpand Collapse

body: CertificateDeactivateParams { certificate\_ids }

certificate\_ids: Array<string>

##### ReturnsExpand Collapse

CertificateDeactivateResponse { id, active, certificate\_details, 3 more }

Represents an individual certificate configured at the organization level.

id: string

The identifier, which can be referenced in API endpoints

active: boolean

Whether the certificate is currently active at the organization level.

certificate\_details: CertificateDetails { expires\_at, valid\_at }

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

object: "organization.certificate"

The object type, which is always `organization.certificate`.

### Deactivate certificates for organization

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

// Automatically fetches more pages as needed.
for await (const certificateDeactivateResponse of client.admin.organization.certificates.deactivate(
  { certificate_ids: ['cert_abc'] },
)) {
  console.log(certificateDeactivateResponse.id);

  "object": "organization.certificate.deactivation",
  "data": [
      "object": "organization.certificate",
      "id": "cert_abc",
      "name": "My Example Certificate",
      "active": false,
      "created_at": 1234567,
      "certificate_details": {
        "valid_at": 12345667,
        "expires_at": 12345678
      "object": "organization.certificate",
      "id": "cert_def",
      "name": "My Example Certificate 2",
      "active": false,
      "created_at": 1234567,
      "certificate_details": {
        "valid_at": 12345667,
        "expires_at": 12345678
  ],

##### Returns Examples

  "object": "organization.certificate.deactivation",
  "data": [
      "object": "organization.certificate",
      "id": "cert_abc",
      "name": "My Example Certificate",
      "active": false,
      "created_at": 1234567,
      "certificate_details": {
        "valid_at": 12345667,
        "expires_at": 12345678
      "object": "organization.certificate",
      "id": "cert_def",
      "name": "My Example Certificate 2",
      "active": false,
      "created_at": 1234567,
      "certificate_details": {
        "valid_at": 12345667,
        "expires_at": 12345678
  ],
