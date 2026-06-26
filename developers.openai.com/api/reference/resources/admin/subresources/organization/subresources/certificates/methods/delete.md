<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/certificates/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Certificates](/api/reference/resources/admin/subresources/organization/subresources/certificates)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete certificate

DELETE/organization/certificates/{certificate\_id}

Delete a certificate from the organization.

The certificate must be inactive for the organization and all projects.

##### Path ParametersExpand Collapse

certificate\_id: string

##### ReturnsExpand Collapse

id: string

The ID of the certificate that was deleted.

object: "certificate.deleted"

The object type, must be `certificate.deleted`.

### Delete certificate

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl -X DELETE https://api.openai.com/v1/organization/certificates/cert_abc \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY"

  "object": "certificate.deleted",
  "id": "cert_abc"

##### Returns Examples

  "object": "certificate.deleted",
  "id": "cert_abc"
