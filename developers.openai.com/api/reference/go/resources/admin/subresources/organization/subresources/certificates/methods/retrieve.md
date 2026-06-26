<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/certificates/methods/retrieve/ -->

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

# Get certificate

client.Admin.Organization.Certificates.Get(ctx, certificateID, query) (\*[Certificate](/api/reference/go/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema)), error)

GET/organization/certificates/{certificate\_id}

Get a certificate that has been uploaded to the organization.

You can get a certificate regardless of whether it is active or not.

##### ParametersExpand Collapse

certificateID string

query AdminOrganizationCertificateGetParams

Include param.Field[[]string]Optional

A list of additional fields to include in the response. Currently the only supported value is `content` to fetch the PEM content of the certificate.

const AdminOrganizationCertificateGetParamsIncludeContent AdminOrganizationCertificateGetParamsInclude = "content"

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

### Get certificate

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
  certificate, err := client.Admin.Organization.Certificates.Get(
    context.TODO(),
    "certificate_id",
    openai.AdminOrganizationCertificateGetParams{

  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", certificate.ID)

  "object": "certificate",
  "id": "cert_abc",
  "name": "My Example Certificate",
  "created_at": 1234567,
  "certificate_details": {
    "valid_at": 1234567,
    "expires_at": 12345678,
    "content": "-----BEGIN CERTIFICATE-----MIIDeT...-----END CERTIFICATE-----"

##### Returns Examples

  "object": "certificate",
  "id": "cert_abc",
  "name": "My Example Certificate",
  "created_at": 1234567,
  "certificate_details": {
    "valid_at": 1234567,
    "expires_at": 12345678,
    "content": "-----BEGIN CERTIFICATE-----MIIDeT...-----END CERTIFICATE-----"
