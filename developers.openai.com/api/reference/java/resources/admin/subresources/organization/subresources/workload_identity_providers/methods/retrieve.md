<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/workload_identity_providers/methods/retrieve/ -->

## Retrieve Platform workload identity provider

`WorkloadIdentityProvider admin().organization().workloadIdentityProviders().retrieve(WorkloadIdentityProviderRetrieveParamsparams = WorkloadIdentityProviderRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/organization/workload_identity_providers/{workload_identity_provider_id}`

Retrieve an OIDC provider in the authenticated organization.

- `WorkloadIdentityProviderRetrieveParams params`

  - `Optional<String> workloadIdentityProviderId`

    `minLength: 1`

- `class WorkloadIdentityProvider:`

  - `String id`

  - `List<AttributeTransformation> attributeTransformations`

    - `String attribute`

    - `String expression`

  - `String audience`

  - `long createdAt`

  - `Optional<String> description`

  - `boolean enabled`

  - `String issuer`

  - `String name`

  - `JsonValue; object_ "organization.workload_identity_provider"constant`

    - `ORGANIZATION_WORKLOAD_IDENTITY_PROVIDER("organization.workload_identity_provider")`

  - `JsonValue; type "oidc"constant`

    - `OIDC("oidc")`

  - `long updatedAt`

  - `Verification verification`

    - `class Discovery:`

      - `Optional<String> discoveryUrl`

      - `JsonValue; type "discovery"constant`

        - `DISCOVERY("discovery")`

    - `class UploadedJwks:`

      - `Jwks jwks`

      - `JsonValue; type "uploaded_jwks"constant`

        - `UPLOADED_JWKS("uploaded_jwks")`

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.admin.organization.workloadidentityproviders.WorkloadIdentityProvider;
import com.openai.models.admin.organization.workloadidentityproviders.WorkloadIdentityProviderRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        WorkloadIdentityProvider workloadIdentityProvider = client.admin().organization().workloadIdentityProviders().retrieve("x");

  "attribute_transformations": [
      "attribute": "attribute",
      "expression": "expression"
  "audience": "audience",
  "enabled": true,
  "issuer": "issuer",
  "object": "organization.workload_identity_provider",
  "type": "oidc",
  "updated_at": 0,
  "verification": {
    "discovery_url": "discovery_url",
    "type": "discovery"
