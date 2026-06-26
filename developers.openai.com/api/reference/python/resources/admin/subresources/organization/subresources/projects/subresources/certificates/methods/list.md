<!-- source: https://developers.openai.com/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Admin](/api/reference/python/resources/admin)

[Organization](/api/reference/python/resources/admin/subresources/organization)

[Projects](/api/reference/python/resources/admin/subresources/organization/subresources/projects)

[Certificates](/api/reference/python/resources/admin/subresources/organization/subresources/projects/subresources/certificates)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List project certificates

admin.organization.projects.certificates.list(strproject\_id, CertificateListParams\*\*kwargs)  -> SyncConversationCursorPage[[CertificateListResponse](/api/reference/python/resources/admin#(resource)%20admin.organization.projects.certificates%20%3E%20(model)%20certificate_list_response%20%3E%20(schema))]

GET/organization/projects/{project\_id}/certificates

List certificates for this project.

##### ParametersExpand Collapse

project\_id: str

after: Optional[str]

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

limit: Optional[int]

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

order: Optional[Literal["asc", "desc"]]

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

One of the following:

"asc"

"desc"

##### ReturnsExpand Collapse

class CertificateListResponse: …

Represents an individual certificate configured at the project level.

id: str

The identifier, which can be referenced in API endpoints

active: bool

Whether the certificate is currently active at the project level.

certificate\_details: CertificateDetails

expires\_at: Optional[int]

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

valid\_at: Optional[int]

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

created\_at: int

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

name: Optional[str]

The name of the certificate.

object: Literal["organization.project.certificate"]

The object type, which is always `organization.project.certificate`.

### List project certificates

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import os
from openai import OpenAI

client = OpenAI(
    admin_api_key=os.environ.get("OPENAI_ADMIN_KEY"),  # This is the default and can be omitted
page = client.admin.organization.projects.certificates.list(
    project_id="project_id",
page = page.data[0]
print(page.id)

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
