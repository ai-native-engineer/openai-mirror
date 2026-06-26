<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/deactivate/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Projects](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects)

[Certificates](/api/reference/ruby/resources/admin/subresources/organization/subresources/projects/subresources/certificates)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Deactivate certificates for project

admin.organization.projects.certificates.deactivate(project\_id, \*\*kwargs) -> Page<[CertificateDeactivateResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_deactivate_response%20%3E%20(schema)) { id, active, certificate\_details, 3 more } >

POST/organization/projects/{project\_id}/certificates/deactivate

Deactivate certificates at the project level. You can atomically and
idempotently deactivate up to 10 certificates at a time.

##### ParametersExpand Collapse

project\_id: String

certificate\_ids: Array[String]

##### ReturnsExpand Collapse

class CertificateDeactivateResponse { id, active, certificate\_details, 3 more }

Represents an individual certificate configured at the project level.

id: String

The identifier, which can be referenced in API endpoints

active: bool

Whether the certificate is currently active at the project level.

certificate\_details: CertificateDetails{ expires\_at, valid\_at}

expires\_at: Integer

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

valid\_at: Integer

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

created\_at: Integer

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

name: String

The name of the certificate.

object: :"organization.project.certificate"

The object type, which is always `organization.project.certificate`.

### Deactivate certificates for project

Ruby

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

require "openai"

openai = OpenAI::Client.new(admin_api_key: "My Admin API Key")

page = openai.admin.organization.projects.certificates.deactivate("project_id", certificate_ids: ["cert_abc"])

puts(page)

  "object": "organization.project.certificate.deactivation",
  "data": [
      "object": "organization.project.certificate",
      "id": "cert_abc",
      "name": "My Example Certificate",
      "active": false,
      "created_at": 1234567,
      "certificate_details": {
        "valid_at": 12345667,
        "expires_at": 12345678
      "object": "organization.project.certificate",
      "id": "cert_def",
      "name": "My Example Certificate 2",
      "active": false,
      "created_at": 1234567,
      "certificate_details": {
        "valid_at": 12345667,
        "expires_at": 12345678
  ],

##### Returns Examples

  "object": "organization.project.certificate.deactivation",
  "data": [
      "object": "organization.project.certificate",
      "id": "cert_abc",
      "name": "My Example Certificate",
      "active": false,
      "created_at": 1234567,
      "certificate_details": {
        "valid_at": 12345667,
        "expires_at": 12345678
      "object": "organization.project.certificate",
      "id": "cert_def",
      "name": "My Example Certificate 2",
      "active": false,
      "created_at": 1234567,
      "certificate_details": {
        "valid_at": 12345667,
        "expires_at": 12345678
  ],
