<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/certificates/methods/deactivate/ -->

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

# Deactivate certificates for organization

client.Admin.Organization.Certificates.Deactivate(ctx, body) (\*Page[[AdminOrganizationCertificateDeactivateResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20AdminOrganizationCertificateDeactivateResponse%20%3E%20(schema))], error)

POST/organization/certificates/deactivate

Deactivate certificates at the organization level.

You can atomically and idempotently deactivate up to 10 certificates at a time.

##### ParametersExpand Collapse

body AdminOrganizationCertificateDeactivateParams

CertificateIDs param.Field[[]string]

##### ReturnsExpand Collapse

type AdminOrganizationCertificateDeactivateResponse struct{…}

Represents an individual certificate configured at the organization level.

ID string

The identifier, which can be referenced in API endpoints

Active bool

Whether the certificate is currently active at the organization level.

CertificateDetails AdminOrganizationCertificateDeactivateResponseCertificateDetails

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

Object OrganizationCertificate

The object type, which is always `organization.certificate`.

### Deactivate certificates for organization

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
  page, err := client.Admin.Organization.Certificates.Deactivate(context.TODO(), openai.AdminOrganizationCertificateDeactivateParams{
    CertificateIDs: []string{"cert_abc"},
  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

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
