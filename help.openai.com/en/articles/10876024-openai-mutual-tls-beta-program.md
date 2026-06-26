<!-- source: https://help.openai.com/en/articles/10876024-openai-mutual-tls-beta-program -->

# OpenAI Mutual TLS Beta Program

Updated: 15 days ago

OpenAI Mutual TLS allows organizations to configure an additional layer of security for their OpenAI API traffic. Once configured, API requests should be made to <https://mtls.api.openai.com> (or <https://mtls-eu.api.openai.com> for EU Data Residency customers) and traffic will only be accepted if the right API key and client certificate are provided. mTLS does not apply to the <https://platform.openai.com> Dashboard. This feature is currently in **beta**.

# How do I set up the mTLS integration?

On the settings navigation bar, you’ll see a “Mutual TLS” tab.

![Mutual TLS settings page prompting the user to upload a client certificate to enable mTLS](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-637c2324f904a58c75dab42c/a66804b8aa8e0aef9a873e91f2c2bac0/AD_4nXeIPs9urqazGoflU_vx_ppV1lDszqhAncUMjQiGbnL2ZCEVx55Ln2EMnl0VMbsYyy7qg2_m3ontyNQ9tIIkalESH2qFhNDNyiFs8UtQ2hB1jYKtYzTmaJezkIfN)

**Upload Certificate**

![Upload a certificate dialog for mutual TLS with name field and PEM certificate text area](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-fa290dddf9b7447060946c82/e0b039bace78c0d65e465acb46f85351/AD_4nXe4DwESrmeiekrVQsUaM89IkSH7enzG7XjLlbalS3Th9uq6HJ__nbdkcxgMNZHBYl1yasJ0h321SoQIph4Mzunb3acAn0YtCC7eqV18Q2lfz5dKCKZmXFSzYbRw)

**Activate Certificate**  
  
After uploading your certificate, the next step is to **activate** your certificate. Once a certificate is **activated** for a project, all API requests going to that project will start to require a corresponding client certificate as well. If a project has multiple certificates activated, you can pass in any corresponding client certificate. If a certificate is activated for the organization, it will apply to **all** API requests and is “inherited” by all projects.

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-1e1ee552656332e9579018ea/48596665f4545636cbcea5d0b0486040/AD_4nXdR8yrw9xzBItk_HqNxOfwh9H0EyJHbxj3kHOSM9JmKSMH4OcyvBFnoxTHEJ-LJbmYwIXc_uYFo_Hq394uXMJf-19zxvVrgpWZdn1HNyfMpOXRL3t7qcdFUFoDI)

## CA certificate requirements

You can upload any X.509 CA certificate in PEM format that meets the following requirements:

1. directly signs your client certificates that you plan to make requests with
2. has the **Certificate Authority**, **Subject Key Identifier**, and **Authority Key Identifier** (in KeyIdentifier format) extensions
3. has the Key Usage: “**Certificate Sign, CRL Sign**” permissions
4. is not set to expire within 1 day
5. total certificate size must be less than 16kb.

## Client certificate requirements

Client certificates must be **directly signed** by the certificates that you uploaded in advance. At the moment, we currently only support single-length certificate chains. Apart from this, your client certificates must meet the following requirements:

1. has the **Subject Key Identifier** and **Authority Key Identifier** extension (in KeyIdentifier format)
2. has the Key Usage: “**Digital Signature, Key Encipherment**” permissions
3. has the Extended Key Usage: “**TLS Web Client Authentication**” permission
4. has the Subject Alternate Name extension

# FAQ

## Can I configure mTLS via API?

Yes — you can see the API Reference at <https://platform.openai.com/docs/api-reference/> for more information.

## What endpoints support mTLS?

During this beta period, mTLS is officially supported in

* `/v1/chat/completions (with all supported extensions e.g. image, audio, streaming, etc.)`
* `/v1/completions`
* `/v1/embeddings`
* `/v1/audio/transcriptions`
* `/v1/audio/speech`
* `/v1/files`
* `/v1/batches`
* `/v1/responses`
* `/v1/images`
* `/v1/moderations`
* `/v1/realtime (via server-side web sockets)`
* `/v1/fine_tuning`
* `/v1/tunnels`

## How do I send client certificates with my request?

For a cURL request, you can use the --cert and --key options (see the man page [here](https://curl.se/docs/manpage.html#--key)). In most other HTTP clients, there are ways to pass client certificates as well. Examples: [requests](https://requests.readthedocs.io/en/latest/user/advanced/#client-side-certificates) in python, [fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch#including_credentials) in js. Through our official SDKs, we support overriding the HTTP client as well — see [here](https://github.com/openai/openai-python?tab=readme-ov-file#configuring-the-http-client) for a Python example.  
  
Before enforcing mTLS for production traffic, ensure that the HTTP client you are using behaves well with client certificate requests (some, such as WebSockets in certain browsers, do not). Note that our server does not provide a certificate\_authorities [list](https://www.rfc-editor.org/rfc/rfc5246#section-7.4.4) in the client certificate request.

## Who can access and modify certificates?

Through the <https://platform.openai.com/settings/organization/mtls> Dashboard UI, organization **owners** can access and modify certificates. Anyone with an Admin API Key (<https://platform.openai.com/settings/organization/admin-keys>) can access/modify certificates as well, though beware — if you activate Mutual TLS at the **organization** level, you will be enforcing certificates on these API requests as well. All mTLS changes are visible in audit logs.

## How many certificates can I have?

Each organization can upload up to 50 certificates, which can be shared across projects but not with other organizations. You can atomically activate/deactivate a certificate for 10 projects at a time. Alternatively, you can activate/deactivate 10 certificates at a time for your organization or for 1 specific project.

## Can I update or delete certificates?

You can update the names of your certificates, but not the content. You can also delete certificates if they are not currently active at any scope.

## How does certificate revocation work?

At the moment, we do not support CRLs or OCSP stapling. The recommended alternative is to delete or rotate your API key instead. You can also swap out your CA certificates or use client certificates with shorter validity periods.

## Can I use longer length certificate chains?

At the moment, we only support single-length chains — i.e. your CA certificate should directly sign your client certificates. Please reach out to your Account Director if you have further questions.

## What’s the recommended setup?

When initially setting up this feature, we recommend starting off with a staging project that doesn’t serve official production traffic. Use this opportunity to make sure that your certificates are properly set up on your machines and that you can send API traffic successfully. Apart from this, we recommend consulting with your organization’s security team to best understand your needs.

## Extra Support

You can fully self-serve the mTLS feature via the dashboard and API. However, if you’d like to enable mTLS in a shadow mode at first, please reach out to your Account Director or open a support ticket by starting a new chat on the bottom-right corner of this page.

# Appendix: Terminology

* **CA certificate**: One of your trusted certificates that has directly signed your client certificates that you will send with requests. You are welcome to use self-signed CA certificates.
* **Upload a certificate**: adding a CA certificate to your account. It does not get enforced anywhere for mTLS yet, but you can begin to configure it.
* **Scope:** a specific project or your entire organization.
* **Activate a CA certificate at a scope**: enables mTLS for that scope specifically, and all API-key based requests will need to require a client certificate that is signed by the CA certificate.
* **Deactivate a CA certificate at a scope**: disables the usage of this certificate to verify requests at this scope. If you have no certificates left for the scope, mTLS is effectively turned off.
* **Inheriting a certificate**: If you activate a certificate for your organization, it will be activated for all projects as well.
