<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/certificates/methods/deactivate/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Admin](/api/reference/java/resources/admin)

[Organization](/api/reference/java/resources/admin/subresources/organization)

[Projects](/api/reference/java/resources/admin/subresources/organization/subresources/projects)

[Certificates](/api/reference/java/resources/admin/subresources/organization/subresources/projects/subresources/certificates)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Deactivate certificates for project

CertificateDeactivatePage admin().organization().projects().certificates().deactivate(CertificateDeactivateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/projects/{project\_id}/certificates/deactivate

Deactivate certificates at the project level. You can atomically and
idempotently deactivate up to 10 certificates at a time.

##### ParametersExpand Collapse

CertificateDeactivateParams params

Optional<String> projectId

List<String> certificateIds

##### ReturnsExpand Collapse

class CertificateDeactivateResponse:

Represents an individual certificate configured at the project level.

String id

The identifier, which can be referenced in API endpoints

boolean active

Whether the certificate is currently active at the project level.

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

JsonValue; object\_ "organization.project.certificate"constant"organization.project.certificate"constant

The object type, which is always `organization.project.certificate`.

### Deactivate certificates for project

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
import com.openai.models.admin.organization.projects.certificates.CertificateDeactivatePage;
import com.openai.models.admin.organization.projects.certificates.CertificateDeactivateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        CertificateDeactivateParams params = CertificateDeactivateParams.builder()
            .projectId("project_id")
            .addCertificateId("cert_abc")
            .build();
        CertificateDeactivatePage page = client.admin().organization().projects().certificates().deactivate(params);

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
