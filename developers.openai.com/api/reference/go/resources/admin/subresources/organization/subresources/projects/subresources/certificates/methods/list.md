<!-- source: https://developers.openai.com/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Admin](/api/reference/go/resources/admin)

[Organization](/api/reference/go/resources/admin/subresources/organization)

[Projects](/api/reference/go/resources/admin/subresources/organization/subresources/projects)

[Certificates](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/certificates)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List project certificates

client.Admin.Organization.Projects.Certificates.List(ctx, projectID, query) (\*ConversationCursorPage[[AdminOrganizationProjectCertificateListResponse](/api/reference/go/resources/admin#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20AdminOrganizationProjectCertificateListResponse%20%3E%20(schema))], error)

GET/organization/projects/{project\_id}/certificates

List certificates for this project.

##### ParametersExpand Collapse

projectID string

query AdminOrganizationProjectCertificateListParams

After param.Field[string]Optional

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

Limit param.Field[int64]Optional

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

Order param.Field[[AdminOrganizationProjectCertificateListParamsOrder](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/list#(resource)%20admin.organization.projects.certificates%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))]Optional

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

const AdminOrganizationProjectCertificateListParamsOrderAsc [AdminOrganizationProjectCertificateListParamsOrder](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/list#(resource)%20admin.organization.projects.certificates%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "asc"

const AdminOrganizationProjectCertificateListParamsOrderDesc [AdminOrganizationProjectCertificateListParamsOrder](/api/reference/go/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/list#(resource)%20admin.organization.projects.certificates%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "desc"

##### ReturnsExpand Collapse

type AdminOrganizationProjectCertificateListResponse struct{…}

Represents an individual certificate configured at the project level.

ID string

The identifier, which can be referenced in API endpoints

Active bool

Whether the certificate is currently active at the project level.

CertificateDetails AdminOrganizationProjectCertificateListResponseCertificateDetails

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

Object OrganizationProjectCertificate

The object type, which is always `organization.project.certificate`.

### List project certificates

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
  page, err := client.Admin.Organization.Projects.Certificates.List(
    context.TODO(),
    "project_id",
    openai.AdminOrganizationProjectCertificateListParams{

  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

  "object": "list",
  "data": [
      "object": "organization.project.certificate",
      "id": "cert_abc",
      "name": "My Example Certificate",
      "active": true,
      "created_at": 1234567,
      "certificate_details": {
        "valid_at": 12345667,
        "expires_at": 12345678
  ],
  "first_id": "cert_abc",
  "last_id": "cert_abc",
  "has_more": false

##### Returns Examples

  "object": "list",
  "data": [
      "object": "organization.project.certificate",
      "id": "cert_abc",
      "name": "My Example Certificate",
      "active": true,
      "created_at": 1234567,
      "certificate_details": {
        "valid_at": 12345667,
        "expires_at": 12345678
  ],
  "first_id": "cert_abc",
  "last_id": "cert_abc",
  "has_more": false
