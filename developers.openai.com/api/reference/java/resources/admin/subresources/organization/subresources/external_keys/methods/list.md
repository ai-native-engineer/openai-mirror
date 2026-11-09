<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/external_keys/methods/list/ -->

## List the external key configs registered on the user's organization

`ExternalKeyListPage admin().organization().externalKeys().list(ExternalKeyListParamsparams = ExternalKeyListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/organization/external_keys`

List the external key configs registered on the user's organization

- `ExternalKeyListParams params`

  - `Optional<String> after`

  - `Optional<Long> limit`

    `minimum: 0`, `maximum: 100`

  - `Optional<Order> order`

    - `ASC("asc")`

    - `DESC("desc")`

  - `Optional<Purpose> purpose`

    Filter by key purpose. When omitted, returns keys of all purposes.

    - `EKM("ekm")`

    - `PSP_DECRYPTION("psp_decryption")`

- `class ExternalKey:`

  - `String id`

  - `List<String> apiProjectIds`

  - `long createdAt`

  - `String name`

  - `String object_`

  - `String type`

  - `String workspaceId`

  - `Optional<String> audience`

  - `Optional<String> externalId`

  - `Optional<String> keyName`

  - `Optional<String> keyVersion`

  - `Optional<String> kmsArn`

  - `Optional<String> kmsKeyLocation`

  - `Optional<String> kmsKeyName`

  - `Optional<String> kmsKeyRingName`

  - `Optional<String> kmsKeyVersion`

  - `Optional<String> kmsProjectId`

  - `Optional<Purpose> purpose`

    - `EKM("ekm")`

    - `PSP_DECRYPTION("psp_decryption")`

  - `Optional<String> roleArn`

  - `Optional<String> tenantId`

  - `Optional<String> vaultUri`

  - `Optional<String> workloadIdentityPoolId`

  - `Optional<String> workloadIdentityProjectNumber`

  - `Optional<String> workloadIdentityProviderId`

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.admin.organization.externalkeys.ExternalKeyListPage;
import com.openai.models.admin.organization.externalkeys.ExternalKeyListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ExternalKeyListPage page = client.admin().organization().externalKeys().list();

  "data": [
      "api_project_ids": [
        "string"
      "object": "object",
      "type": "type",
      "workspace_id": "workspace_id",
      "audience": "audience",
      "external_id": "external_id",
      "key_name": "key_name",
      "key_version": "key_version",
      "kms_arn": "kms_arn",
      "kms_key_location": "kms_key_location",
      "kms_key_name": "kms_key_name",
      "kms_key_ring_name": "kms_key_ring_name",
      "kms_key_version": "kms_key_version",
      "kms_project_id": "kms_project_id",
      "purpose": "ekm",
      "role_arn": "role_arn",
      "tenant_id": "tenant_id",
      "vault_uri": "vault_uri",
      "workload_identity_pool_id": "workload_identity_pool_id",
      "workload_identity_project_number": "workload_identity_project_number",
      "workload_identity_provider_id": "workload_identity_provider_id"
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
