<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/certificates/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Certificates](/api/reference/go/resources/admin/subresources/organization/subresources/certificates)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete certificate

client.Admin.Organization.Certificates.Delete(ctx, certificateID) (\*[AdminOrganizationCertificateDeleteResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20AdminOrganizationCertificateDeleteResponse%20%3E%20(schema)), error)

DELETE/organization/certificates/{certificate\_id}

Delete a certificate from the organization.

The certificate must be inactive for the organization and all projects.

##### ParametersExpand Collapse

certificateID string

##### ReturnsExpand Collapse

type AdminOrganizationCertificateDeleteResponse struct{…}

ID string

The ID of the certificate that was deleted.

Object CertificateDeleted

The object type, must be `certificate.deleted`.

### Delete certificate

Go

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAdminAPIKey("My Admin API Key"),
  certificate, err := client.Admin.Organization.Certificates.Delete(context.TODO(), "certificate_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", certificate.ID)

  "object": "certificate.deleted",
  "id": "cert_abc"

##### Returns Examples

  "object": "certificate.deleted",
  "id": "cert_abc"
