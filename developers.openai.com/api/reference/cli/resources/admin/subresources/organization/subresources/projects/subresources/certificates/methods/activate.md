<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/activate/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Projects](/api/reference/cli/resources/admin/subresources/organization/subresources/projects)

[Certificates](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/certificates)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Activate certificates for project

$ openai admin:organization:projects:certificates activate

POST/organization/projects/{project\_id}/certificates/activate

Activate certificates at the project level.

You can atomically and idempotently activate up to 10 certificates at a time.

##### ParametersExpand Collapse

--project-id: string

The ID of the project.

--certificate-id: array of string

##### ReturnsExpand Collapse

OrganizationProjectCertificateActivationResponse: object { data, object }

data: array of object { id, active, certificate\_details, 3 more }

id: string

The identifier, which can be referenced in API endpoints

active: boolean

Whether the certificate is currently active at the project level.

certificate\_details: object { expires\_at, valid\_at }

expires\_at: optional number

The Unix timestamp (in seconds) of when the certificate expires.

valid\_at: optional number

The Unix timestamp (in seconds) of when the certificate becomes valid.

created\_at: number

The Unix timestamp (in seconds) of when the certificate was uploaded.

name: string

The name of the certificate.

object: "organization.project.certificate"

The object type, which is always `organization.project.certificate`.

object: "organization.project.certificate.activation"

The project certificate activation result type.

### Activate certificates for project

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:projects:certificates activate \
  --admin-api-key 'My Admin API Key' \
  --project-id project_id \
  --certificate-id cert_abc

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
