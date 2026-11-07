<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/workload_identity_providers/methods/update/ -->

## Update Platform workload identity provider

`WorkloadIdentityProvider admin().organization().workloadIdentityProviders().update(WorkloadIdentityProviderUpdateParamsparams = WorkloadIdentityProviderUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/organization/workload_identity_providers/{workload_identity_provider_id}`

Update supplied provider fields, preserving omitted fields.

- `WorkloadIdentityProviderUpdateParams params`

  - `Optional<String> workloadIdentityProviderId`

    `minLength: 1`

  - `Optional<List<AttributeTransformation>> attributeTransformations`

    `maxItems: 20`

    - `String attribute`

      `minLength: 1`, `maxLength: 256`

    - `String expression`

      `minLength: 1`, `maxLength: 4096`

  - `Optional<String> audience`

    `minLength: 1`

  - `Optional<String> description`

  - `Optional<Boolean> enabled`

  - `Optional<String> issuer`

    `minLength: 1`

  - `Optional<String> name`

    `minLength: 1`

  - `Optional<Verification> verification`

    - `class DiscoveryVerificationParam:`

      - `Optional<String> discoveryUrl`

      - `JsonValue; type "discovery"constant`

        - `DISCOVERY("discovery")`

    - `class UploadedJwksVerificationParam:`

      - `Jwks jwks`

      - `JsonValue; type "uploaded_jwks"constant`

        - `UPLOADED_JWKS("uploaded_jwks")`

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
import com.openai.models.admin.organization.workloadidentityproviders.WorkloadIdentityProviderUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        WorkloadIdentityProvider workloadIdentityProvider = client.admin().organization().workloadIdentityProviders().update("x");

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
