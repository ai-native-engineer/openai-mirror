<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/certificates/methods/delete/ -->

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

# Delete certificate

[CertificateDeleteResponse](/api/reference/java/resources/admin#(resource)%20admin.organization.certificates%20%3E%20(model)%20CertificateDeleteResponse%20%3E%20(schema)) admin().organization().certificates().delete(CertificateDeleteParamsparams = CertificateDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/organization/certificates/{certificate\_id}

Delete a certificate from the organization.

The certificate must be inactive for the organization and all projects.

##### ParametersExpand Collapse

CertificateDeleteParams params

Optional<String> certificateId

##### ReturnsExpand Collapse

class CertificateDeleteResponse:

String id

The ID of the certificate that was deleted.

JsonValue; object\_ "certificate.deleted"constant"certificate.deleted"constant

The object type, must be `certificate.deleted`.

### Delete certificate

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
import com.openai.models.admin.organization.certificates.CertificateDeleteParams;
import com.openai.models.admin.organization.certificates.CertificateDeleteResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        CertificateDeleteResponse certificate = client.admin().organization().certificates().delete("certificate_id");

  "object": "certificate.deleted",
  "id": "cert_abc"

##### Returns Examples

  "object": "certificate.deleted",
  "id": "cert_abc"
