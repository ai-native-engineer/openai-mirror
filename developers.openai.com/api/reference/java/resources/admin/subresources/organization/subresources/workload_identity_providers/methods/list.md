<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/workload_identity_providers/methods/list/ -->

## List Platform workload identity providers

`WorkloadIdentityProviderListPage admin().organization().workloadIdentityProviders().list(WorkloadIdentityProviderListParamsparams = WorkloadIdentityProviderListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/organization/workload_identity_providers`

List OIDC providers in the authenticated Admin API key's organization.

- `WorkloadIdentityProviderListParams params`

  - `Optional<String> after`

    `minLength: 1`

  - `Optional<Long> limit`

    `minimum: 1`, `maximum: 100`

  - `Optional<Order> order`

    - `ASC("asc")`

    - `DESC("desc")`

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
import com.openai.models.admin.organization.workloadidentityproviders.WorkloadIdentityProviderListPage;
import com.openai.models.admin.organization.workloadidentityproviders.WorkloadIdentityProviderListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        WorkloadIdentityProviderListPage page = client.admin().organization().workloadIdentityProviders().list();

  "data": [
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
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
