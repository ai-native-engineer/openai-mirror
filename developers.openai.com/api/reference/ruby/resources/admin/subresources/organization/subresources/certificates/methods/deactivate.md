<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/certificates/methods/deactivate/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Admin](/api/reference/ruby/resources/admin)

[Organization](/api/reference/ruby/resources/admin/subresources/organization)

[Certificates](/api/reference/ruby/resources/admin/subresources/organization/subresources/certificates)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Deactivate certificates for organization

admin.organization.certificates.deactivate(\*\*kwargs) -> Page<[CertificateDeactivateResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate_deactivate_response%20%3E%20(schema)) { id, active, certificate\_details, 3 more } >

POST/organization/certificates/deactivate

Deactivate certificates at the organization level.

You can atomically and idempotently deactivate up to 10 certificates at a time.

##### ParametersExpand Collapse

certificate\_ids: Array[String]

##### ReturnsExpand Collapse

class CertificateDeactivateResponse { id, active, certificate\_details, 3 more }

Represents an individual certificate configured at the organization level.

id: String

The identifier, which can be referenced in API endpoints

active: bool

Whether the certificate is currently active at the organization level.

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

object: :"organization.certificate"

The object type, which is always `organization.certificate`.

### Deactivate certificates for organization

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

page = openai.admin.organization.certificates.deactivate(certificate_ids: ["cert_abc"])

puts(page)

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
