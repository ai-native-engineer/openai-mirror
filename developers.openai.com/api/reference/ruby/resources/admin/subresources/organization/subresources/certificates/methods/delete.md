<!-- source: https://developers.openai.com/api/reference/ruby/resources/admin/subresources/organization/subresources/certificates/methods/delete/ -->

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

# Delete certificate

admin.organization.certificates.delete(certificate\_id) -> [CertificateDeleteResponse](/api/reference/ruby/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate_delete_response%20%3E%20(schema)) { id, object }

DELETE/organization/certificates/{certificate\_id}

Delete a certificate from the organization.

The certificate must be inactive for the organization and all projects.

##### ParametersExpand Collapse

certificate\_id: String

##### ReturnsExpand Collapse

class CertificateDeleteResponse { id, object }

id: String

The ID of the certificate that was deleted.

object: :"certificate.deleted"

The object type, must be `certificate.deleted`.

### Delete certificate

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

certificate = openai.admin.organization.certificates.delete("certificate_id")

puts(certificate)

  "object": "certificate.deleted",
  "id": "cert_abc"

##### Returns Examples

  "object": "certificate.deleted",
  "id": "cert_abc"
