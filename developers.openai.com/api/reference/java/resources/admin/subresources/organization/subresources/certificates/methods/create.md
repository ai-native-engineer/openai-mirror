<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/certificates/methods/create/ -->

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

# Upload certificate

[Certificate](/api/reference/java/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20certificate%20%3E%20(schema)) admin().organization().certificates().create(CertificateCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/organization/certificates

Upload a certificate to the organization. This does **not** automatically activate the certificate.

Organizations can upload up to 50 certificates.

##### ParametersExpand Collapse

CertificateCreateParams params

String certificate

The certificate content in PEM format

Optional<String> name

An optional name for the certificate

##### ReturnsExpand Collapse

class Certificate:

Represents an individual `certificate` uploaded to the organization.

String id

The identifier, which can be referenced in API endpoints

CertificateDetails certificateDetails

Optional<String> content

The content of the certificate in PEM format.

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

Object object\_

The object type.

* If creating, updating, or getting a specific certificate, the object type is `certificate`.
* If listing, activating, or deactivating certificates for the organization, the object type is `organization.certificate`.
* If listing, activating, or deactivating certificates for a project, the object type is `organization.project.certificate`.

One of the following:

CERTIFICATE("certificate")

ORGANIZATION\_CERTIFICATE("organization.certificate")

ORGANIZATION\_PROJECT\_CERTIFICATE("organization.project.certificate")

Optional<Boolean> active

Whether the certificate is currently active at the specified scope. Not returned when getting details for a specific certificate.

### Upload certificate

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
import com.openai.models.admin.organization.certificates.Certificate;
import com.openai.models.admin.organization.certificates.CertificateCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        CertificateCreateParams params = CertificateCreateParams.builder()
            .certificate("certificate")
            .build();
        Certificate certificate = client.admin().organization().certificates().create(params);

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
