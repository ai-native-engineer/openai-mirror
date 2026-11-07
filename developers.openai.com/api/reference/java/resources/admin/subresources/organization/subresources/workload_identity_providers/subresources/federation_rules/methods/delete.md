<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/workload_identity_providers/subresources/federation_rules/methods/delete/ -->

## Delete Platform workload identity federation rule

`FederationRuleDeleted admin().organization().workloadIdentityProviders().federationRules().delete(FederationRuleDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules/{workload_identity_federation_rule_id}`

Delete a federation rule to a project service account.

- `FederationRuleDeleteParams params`

  - `String workloadIdentityProviderId`

    `minLength: 1`

  - `Optional<String> workloadIdentityFederationRuleId`

    `minLength: 1`

- `class FederationRuleDeleted:`

  - `String id`

  - `boolean deleted`

  - `JsonValue; object_ "organization.workload_identity_federation_rule.deleted"constant`

    - `ORGANIZATION_WORKLOAD_IDENTITY_FEDERATION_RULE_DELETED("organization.workload_identity_federation_rule.deleted")`

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.admin.organization.workloadidentityproviders.federationrules.FederationRuleDeleteParams;
import com.openai.models.admin.organization.workloadidentityproviders.federationrules.FederationRuleDeleted;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FederationRuleDeleteParams params = FederationRuleDeleteParams.builder()
            .workloadIdentityProviderId("x")
            .workloadIdentityFederationRuleId("x")
            .build();
        FederationRuleDeleted federationRuleDeleted = client.admin().organization().workloadIdentityProviders().federationRules().delete(params);

  "deleted": true,
  "object": "organization.workload_identity_federation_rule.deleted"
