<!-- source: https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/deactivate/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Admin](/api/reference/resources/admin)

[Organization](/api/reference/resources/admin/subresources/organization)

[Projects](/api/reference/resources/admin/subresources/organization/subresources/projects)

[Certificates](/api/reference/resources/admin/subresources/organization/subresources/projects/subresources/certificates)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Deactivate certificates for project

POST/organization/projects/{project\_id}/certificates/deactivate

Deactivate certificates at the project level. You can atomically and
idempotently deactivate up to 10 certificates at a time.

##### Path ParametersExpand Collapse

project\_id: string

##### Body ParametersJSONExpand Collapse

certificate\_ids: array of string

##### ReturnsExpand Collapse

data: array of object { id, active, certificate\_details, 3 more }

id: string

The identifier, which can be referenced in API endpoints

active: boolean

Whether the certificate is currently active at the project level.

certificate\_details: object { expires\_at, valid\_at }

expires\_at: optional number

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

valid\_at: optional number

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

created\_at: number

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

name: string

The name of the certificate.

object: "organization.project.certificate"

The object type, which is always `organization.project.certificate`.

object: "organization.project.certificate.deactivation"

The project certificate deactivation result type.

### Deactivate certificates for project

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/organization/projects/proj_abc/certificates/deactivate \
-H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
-H "Content-Type: application/json" \
-d '{
  "certificate_ids": ["cert_abc", "cert_def"]
}'

  "object": "organization.project.certificate.deactivation",
  "data": [
      "object": "organization.project.certificate",
      "id": "cert_abc",
      "name": "My Example Certificate",
      "active": false,
      "created_at": 1234567,
      "certificate_details": {
        "valid_at": 12345667,
        "expires_at": 12345678
      "object": "organization.project.certificate",
      "id": "cert_def",
      "name": "My Example Certificate 2",
      "active": false,
      "created_at": 1234567,
      "certificate_details": {
        "valid_at": 12345667,
        "expires_at": 12345678
  ],

##### Returns Examples

  "object": "organization.project.certificate.deactivation",
  "data": [
      "object": "organization.project.certificate",
      "id": "cert_abc",
      "name": "My Example Certificate",
      "active": false,
      "created_at": 1234567,
      "certificate_details": {
        "valid_at": 12345667,
        "expires_at": 12345678
      "object": "organization.project.certificate",
      "id": "cert_def",
      "name": "My Example Certificate 2",
      "active": false,
      "created_at": 1234567,
      "certificate_details": {
        "valid_at": 12345667,
        "expires_at": 12345678
  ],
