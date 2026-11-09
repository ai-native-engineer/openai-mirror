<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/workload_identity_providers/subresources/federation_rules/methods/list/ -->

## List Platform workload identity federation rules

`FederationRuleListPage admin().organization().workloadIdentityProviders().federationRules().list(FederationRuleListParamsparams = FederationRuleListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/organization/workload_identity_providers/{workload_identity_provider_id}/federation_rules`

List the provider's federation rules to project service accounts.

- `FederationRuleListParams params`

  - `Optional<String> workloadIdentityProviderId`

    `minLength: 1`

  - `Optional<String> after`

    `minLength: 1`

  - `Optional<Long> limit`

    `minimum: 1`, `maximum: 100`

  - `Optional<Order> order`

    - `ASC("asc")`

    - `DESC("desc")`

  - `Optional<String> serviceAccountId`

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
import com.openai.models.admin.organization.workloadidentityproviders.federationrules.FederationRuleListPage;
import com.openai.models.admin.organization.workloadidentityproviders.federationrules.FederationRuleListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FederationRuleListPage page = client.admin().organization().workloadIdentityProviders().federationRules().list("x");

  "data": [
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
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
