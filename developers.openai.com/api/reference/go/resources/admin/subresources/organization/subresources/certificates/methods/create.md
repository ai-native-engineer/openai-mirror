<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/certificates/methods/create/ -->

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

# Upload certificate

client.Admin.Organization.Certificates.New(ctx, body) (\*[Certificate](/api/reference/go/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema)), error)

POST/organization/certificates

Upload a certificate to the organization. This does **not** automatically activate the certificate.

Organizations can upload up to 50 certificates.

##### ParametersExpand Collapse

body AdminOrganizationCertificateNewParams

Certificate param.Field[string]

The certificate content in PEM format

Name param.Field[string]Optional

An optional name for the certificate

##### ReturnsExpand Collapse

type Certificate struct{…}

Represents an individual `certificate` uploaded to the organization.

ID string

The identifier, which can be referenced in API endpoints

CertificateDetails CertificateCertificateDetails

Content stringOptional

The content of the certificate in PEM format.

ExpiresAt int64Optional

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

ValidAt int64Optional

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

CreatedAt int64

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

Name string

The name of the certificate.

Object CertificateObject

The object type.

* If creating, updating, or getting a specific certificate, the object type is `certificate`.
* If listing, activating, or deactivating certificates for the organization, the object type is `organization.certificate`.
* If listing, activating, or deactivating certificates for a project, the object type is `organization.project.certificate`.

One of the following:

const CertificateObjectCertificate CertificateObject = "certificate"

const CertificateObjectOrganizationCertificate CertificateObject = "organization.certificate"

const CertificateObjectOrganizationProjectCertificate CertificateObject = "organization.project.certificate"

Active boolOptional

Whether the certificate is currently active at the specified scope. Not returned when getting details for a specific certificate.

### Upload certificate

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
  certificate, err := client.Admin.Organization.Certificates.New(context.TODO(), openai.AdminOrganizationCertificateNewParams{
    Certificate: "certificate",
  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", certificate.ID)

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
