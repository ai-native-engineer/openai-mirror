<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/certificates/methods/create/ -->

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

# Upload certificate

admin.organization.certificates.create(\*\*kwargs) -> [Certificate](/api/reference/ruby/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema)) { id, certificate\_details, created\_at, 3 more }

POST/organization/certificates

Upload a certificate to the organization. This does **not** automatically activate the certificate.

Organizations can upload up to 50 certificates.

##### ParametersExpand Collapse

certificate: String

The certificate content in PEM format

name: String

An optional name for the certificate

##### ReturnsExpand Collapse

class Certificate { id, certificate\_details, created\_at, 3 more }

Represents an individual `certificate` uploaded to the organization.

id: String

The identifier, which can be referenced in API endpoints

certificate\_details: CertificateDetails{ content, expires\_at, valid\_at}

content: String

The content of the certificate in PEM format.

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

object: :certificate | :"organization.certificate" | :"organization.project.certificate"

The object type.

* If creating, updating, or getting a specific certificate, the object type is `certificate`.
* If listing, activating, or deactivating certificates for the organization, the object type is `organization.certificate`.
* If listing, activating, or deactivating certificates for a project, the object type is `organization.project.certificate`.

One of the following:

:certificate

:"organization.certificate"

:"organization.project.certificate"

active: bool

Whether the certificate is currently active at the specified scope. Not returned when getting details for a specific certificate.

### Upload certificate

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

certificate = openai.admin.organization.certificates.create(certificate: "certificate")

puts(certificate)

  "object": "certificate",
  "id": "cert_abc",
  "name": "My Example Certificate",
  "created_at": 1234567,
  "certificate_details": {
    "valid_at": 12345667,
    "expires_at": 12345678

##### Returns Examples

  "object": "certificate",
  "id": "cert_abc",
  "name": "My Example Certificate",
  "created_at": 1234567,
  "certificate_details": {
    "valid_at": 12345667,
    "expires_at": 12345678
