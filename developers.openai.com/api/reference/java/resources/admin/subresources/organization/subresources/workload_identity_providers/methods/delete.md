<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/workload_identity_providers/methods/delete/ -->

## Delete Platform workload identity provider

`WorkloadIdentityProviderDeleted admin().organization().workloadIdentityProviders().delete(WorkloadIdentityProviderDeleteParamsparams = WorkloadIdentityProviderDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/organization/workload_identity_providers/{workload_identity_provider_id}`

Delete a provider after deleting all its federation rules.

- `WorkloadIdentityProviderDeleteParams params`

  - `Optional<String> workloadIdentityProviderId`

    `minLength: 1`

- `class WorkloadIdentityProviderDeleted:`

  - `String id`

  - `boolean deleted`

  - `JsonValue; object_ "organization.workload_identity_provider.deleted"constant`

    - `ORGANIZATION_WORKLOAD_IDENTITY_PROVIDER_DELETED("organization.workload_identity_provider.deleted")`

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.admin.organization.workloadidentityproviders.WorkloadIdentityProviderDeleteParams;
import com.openai.models.admin.organization.workloadidentityproviders.WorkloadIdentityProviderDeleted;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        WorkloadIdentityProviderDeleted workloadIdentityProviderDeleted = client.admin().organization().workloadIdentityProviders().delete("x");

  "deleted": true,
  "object": "organization.workload_identity_provider.deleted"
