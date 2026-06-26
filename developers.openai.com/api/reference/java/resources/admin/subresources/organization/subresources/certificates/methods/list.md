<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/certificates/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Certificates](/api/reference/java/resources/admin/subresources/organization/subresources/certificates)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List organization certificates

CertificateListPage admin().organization().certificates().list(CertificateListParamsparams = CertificateListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/organization/certificates

List uploaded certificates for this organization.

##### ParametersExpand Collapse

CertificateListParams params

Optional<String> after

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

Optional<Long> limit

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

Optional<[Order](/api/reference/java/resources/admin/subresources/organization/subresources/certificates/methods/list#(resource)%20admin.organization.certificates%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))> order

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

ASC("asc")

DESC("desc")

##### ReturnsExpand Collapse

class CertificateListResponse:

Represents an individual certificate configured at the organization level.

String id

The identifier, which can be referenced in API endpoints

boolean active

Whether the certificate is currently active at the organization level.

CertificateDetails certificateDetails

Optional<Long> expiresAt

The Unix timestamp (in seconds) of when the certificate expires.

formatunixtime

Optional<Long> validAt

The Unix timestamp (in seconds) of when the certificate becomes valid.

formatunixtime

long createdAt

The Unix timestamp (in seconds) of when the certificate was uploaded.

formatunixtime

Optional<String> name

The name of the certificate.

JsonValue; object\_ "organization.certificate"constant"organization.certificate"constant

The object type, which is always `organization.certificate`.

### List organization certificates

Java

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.admin.organization.certificates.CertificateListPage;
import com.openai.models.admin.organization.certificates.CertificateListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        CertificateListPage page = client.admin().organization().certificates().list();

  "object": "list",
  "data": [
      "object": "organization.certificate",
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
      "object": "organization.certificate",
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
