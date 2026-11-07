<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/workload_identity_providers/subresources/federation_rules/methods/create/ -->

## Create Platform workload identity federation rule

`FederationRule admin().organization().workloadIdentityProviders().federationRules().create(FederationRuleCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules`

Bind verified token attributes to an existing project service account.

- `FederationRuleCreateParams params`

  - `Optional<String> workloadIdentityProviderId`

    `minLength: 1`

  - `AttributeMatchers attributeMatchers`

    - `String`

    - `boolean`

    - `class UnionMember2: A class that can be one of several variants.union`

      - `long`

      - `double`

  - `String projectId`

    `minLength: 1`

  - `String serviceAccountId`

    `minLength: 1`

  - `Optional<String> description`

  - `Optional<Boolean> enabled`

  - `Optional<String> name`

  - `Optional<Permissions> permissions`

    - `JsonValue;`

      - `JsonValue; type "service_account_default"constant`

        - `SERVICE_ACCOUNT_DEFAULT("service_account_default")`

    - `class Restricted:`

      - `List<String> scopes`

        `minItems: 1`

      - `JsonValue; type "restricted"constant`

        - `RESTRICTED("restricted")`

- `class FederationRule:`

  - `String id`

  - `AttributeMatchers attributeMatchers`

    - `String`

    - `boolean`

    - `class UnionMember2: A class that can be one of several variants.union`

      - `long`

      - `double`

  - `long createdAt`

  - `Optional<String> description`

  - `boolean enabled`

  - `Optional<String> name`

  - `JsonValue; object_ "organization.workload_identity_federation_rule"constant`

    - `ORGANIZATION_WORKLOAD_IDENTITY_FEDERATION_RULE("organization.workload_identity_federation_rule")`

  - `Permissions permissions`

    - `JsonValue;`

      - `JsonValue; type "service_account_default"constant`

        - `SERVICE_ACCOUNT_DEFAULT("service_account_default")`

    - `class Restricted:`

      - `List<String> scopes`

      - `JsonValue; type "restricted"constant`

        - `RESTRICTED("restricted")`

  - `String projectId`

  - `String serviceAccountId`

  - `long updatedAt`

  - `String workloadIdentityProviderId`

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.core.JsonValue;
import com.openai.models.admin.organization.workloadidentityproviders.federationrules.FederationRule;
import com.openai.models.admin.organization.workloadidentityproviders.federationrules.FederationRuleCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FederationRuleCreateParams params = FederationRuleCreateParams.builder()
            .workloadIdentityProviderId("x")
            .attributeMatchers(FederationRuleCreateParams.AttributeMatchers.builder()
                .putAdditionalProperty("foo", JsonValue.from("string"))
                .build())
            .projectId("x")
            .serviceAccountId("x")
            .build();
        FederationRule federationRule = client.admin().organization().workloadIdentityProviders().federationRules().create(params);

  "attribute_matchers": {
    "foo": "string"
  "enabled": true,
  "object": "organization.workload_identity_federation_rule",
  "permissions": {
    "type": "service_account_default"
  "project_id": "project_id",
  "service_account_id": "service_account_id",
  "updated_at": 0,
  "workload_identity_provider_id": "workload_identity_provider_id"
