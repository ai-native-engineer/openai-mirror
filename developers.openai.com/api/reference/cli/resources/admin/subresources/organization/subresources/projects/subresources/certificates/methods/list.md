<!-- source: https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Admin](/api/reference/cli/resources/admin)

[Organization](/api/reference/cli/resources/admin/subresources/organization)

[Projects](/api/reference/cli/resources/admin/subresources/organization/subresources/projects)

[Certificates](/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/certificates)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List project certificates

$ openai admin:organization:projects:certificates list

GET/organization/projects/{project\_id}/certificates

List certificates for this project.

##### ParametersExpand Collapse

--project-id: string

The ID of the project.

--after: optional string

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

--limit: optional number

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

--order: optional "asc" or "desc"

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

##### ReturnsExpand Collapse

ListProjectCertificatesResponse: object { data, first\_id, has\_more, 2 more }

data: array of object { id, active, certificate\_details, 3 more }

id: string

The identifier, which can be referenced in API endpoints

active: boolean

Whether the certificate is currently active at the project level.

certificate\_details: object { expires\_at, valid\_at }

expires\_at: optional number

The Unix timestamp (in seconds) of when the certificate expires.

valid\_at: optional number

The Unix timestamp (in seconds) of when the certificate becomes valid.

created\_at: number

The Unix timestamp (in seconds) of when the certificate was uploaded.

name: string

The name of the certificate.

object: "organization.project.certificate"

The object type, which is always `organization.project.certificate`.

first\_id: string

has\_more: boolean

last\_id: string

object: "list"

### List project certificates

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai admin:organization:projects:certificates list \
  --admin-api-key 'My Admin API Key' \
  --project-id project_id

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
