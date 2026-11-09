<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/workload_identity_providers/subresources/federation_rules/methods/retrieve/ -->

## Retrieve Platform workload identity federation rule

`FederationRule admin().organization().workloadIdentityProviders().federationRules().retrieve(FederationRuleRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules/{workload_identity_federation_rule_id}`

Retrieve a federation rule owned by the authenticated organization and provider.

- `FederationRuleRetrieveParams params`

  - `String workloadIdentityProviderId`

    `minLength: 1`

  - `Optional<String> workloadIdentityFederationRuleId`

    `minLength: 1`

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
import com.openai.models.admin.organization.workloadidentityproviders.federationrules.FederationRule;
import com.openai.models.admin.organization.workloadidentityproviders.federationrules.FederationRuleRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FederationRuleRetrieveParams params = FederationRuleRetrieveParams.builder()
            .workloadIdentityProviderId("x")
            .workloadIdentityFederationRuleId("x")
            .build();
        FederationRule federationRule = client.admin().organization().workloadIdentityProviders().federationRules().retrieve(params);

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
