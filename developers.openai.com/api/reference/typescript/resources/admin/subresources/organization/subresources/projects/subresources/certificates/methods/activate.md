<!-- source: https://developers.openai.com/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/activate/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Admin](/api/reference/typescript/resources/admin)

[Organization](/api/reference/typescript/resources/admin/subresources/organization)

[Projects](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects)

[Certificates](/api/reference/typescript/resources/admin/subresources/organization/subresources/projects/subresources/certificates)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Activate certificates for project

client.admin.organization.projects.certificates.activate(stringprojectID, CertificateActivateParams { certificate\_ids } body, RequestOptionsoptions?): Page<[CertificateActivateResponse](/api/reference/typescript/resources/admin#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_activate_response%20%3E%20(schema)) { id, active, certificate\_details, 3 more } >

POST/organization/projects/{project\_id}/certificates/activate

Activate certificates at the project level.

You can atomically and idempotently activate up to 10 certificates at a time.

##### ParametersExpand Collapse

projectID: string

body: CertificateActivateParams { certificate\_ids }

certificate\_ids: Array<string>

##### ReturnsExpand Collapse

CertificateActivateResponse { id, active, certificate\_details, 3 more }

Represents an individual certificate configured at the project level.

id: string

The identifier, which can be referenced in API endpoints

active: boolean

Whether the certificate is currently active at the project level.

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

object: "organization.project.certificate"

The object type, which is always `organization.project.certificate`.

### Activate certificates for project

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
for await (const certificateActivateResponse of client.admin.organization.projects.certificates.activate(
  'project_id',
  { certificate_ids: ['cert_abc'] },
)) {
  console.log(certificateActivateResponse.id);

  "object": "organization.project.certificate.activation",
  "data": [
      "object": "organization.project.certificate",
      "id": "cert_abc",
      "name": "My Example Certificate",
      "active": true,
      "created_at": 1234567,
      "certificate_details": {
        "valid_at": 12345667,
        "expires_at": 12345678
      "object": "organization.project.certificate",
      "id": "cert_def",
      "name": "My Example Certificate 2",
      "active": true,
      "created_at": 1234567,
      "certificate_details": {
        "valid_at": 12345667,
        "expires_at": 12345678
  ],

##### Returns Examples

  "object": "organization.project.certificate.activation",
  "data": [
      "object": "organization.project.certificate",
      "id": "cert_abc",
      "name": "My Example Certificate",
      "active": true,
      "created_at": 1234567,
      "certificate_details": {
        "valid_at": 12345667,
        "expires_at": 12345678
      "object": "organization.project.certificate",
      "id": "cert_def",
      "name": "My Example Certificate 2",
      "active": true,
      "created_at": 1234567,
      "certificate_details": {
        "valid_at": 12345667,
        "expires_at": 12345678
  ],
