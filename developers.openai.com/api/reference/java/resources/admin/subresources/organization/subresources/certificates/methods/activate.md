<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/certificates/methods/activate/ -->

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

# Activate certificates for organization

CertificateActivatePage admin().organization().certificates().activate(CertificateActivateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/certificates/activate

Activate certificates at the organization level.

You can atomically and idempotently activate up to 10 certificates at a time.

##### ParametersExpand Collapse

CertificateActivateParams params

List<String> certificateIds

##### ReturnsExpand Collapse

class CertificateActivateResponse:

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

### Activate certificates for organization

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
import com.openai.models.admin.organization.certificates.CertificateActivatePage;
import com.openai.models.admin.organization.certificates.CertificateActivateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        CertificateActivateParams params = CertificateActivateParams.builder()
            .addCertificateId("cert_abc")
            .build();
        CertificateActivatePage page = client.admin().organization().certificates().activate(params);

  "object": "organization.certificate.activation",
  "data": [
      "object": "organization.certificate",
      "id": "cert_abc",
      "name": "My Example Certificate",
      "active": true,
      "created_at": 1234567,
      "certificate_details": {
        "valid_at": 12345667,
        "expires_at": 12345678
      "object": "organization.certificate",
      "id": "cert_def",
      "name": "My Example Certificate 2",
      "active": true,
      "created_at": 1234567,
      "certificate_details": {
        "valid_at": 12345667,
        "expires_at": 12345678
  ],

##### Returns Examples

  "object": "organization.certificate.activation",
  "data": [
      "object": "organization.certificate",
      "id": "cert_abc",
      "name": "My Example Certificate",
      "active": true,
      "created_at": 1234567,
      "certificate_details": {
        "valid_at": 12345667,
        "expires_at": 12345678
      "object": "organization.certificate",
      "id": "cert_def",
      "name": "My Example Certificate 2",
      "active": true,
      "created_at": 1234567,
      "certificate_details": {
        "valid_at": 12345667,
        "expires_at": 12345678
  ],
