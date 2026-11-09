<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/external_keys/methods/create/ -->

## Add an external key config for an organization

`ExternalKey admin().organization().externalKeys().create(ExternalKeyCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/organization/external_keys`

Add an external key config for an organization

- `ExternalKeyCreateParams params`

  - `Body body`

    - `class Aws:`

      - `String externalId`

        The ExternalID that OpenAI will pass in the AssumeRole call for the customer's AWS account. This must be the OpenAI organization ID or an API project ID that belongs to the organization.

      - `String kmsArn`

        The Key Management System ARN for the master key you manage

      - `String name`

        A friendly name to identify this config

      - `String roleArn`

        The Role ARN that OpenAI will assume to call your KMS

      - `JsonValue; type "aws"constant`

        - `AWS("aws")`

      - `Optional<Purpose> purpose`

        - `EKM("ekm")`

        - `PSP_DECRYPTION("psp_decryption")`

    - `class Gcp:`

      - `String audience`

        The aud field in the identity token OpenAI will pass in the call to the customer's GCP STS. This must be the OpenAI organization ID or an API project ID that belongs to the organization.

      - `String kmsKeyLocation`

        The region where your Key Management System master key is located

      - `String kmsKeyName`

        The name of the Key Management System master key you manage

      - `String kmsKeyRingName`

        The Key Management System key ring for the master key you manage

      - `String kmsProjectId`

        The string GCP project name where your KMS resides

      - `String name`

        A friendly name to identify this config

      - `JsonValue; type "gcp"constant`

        - `GCP("gcp")`

      - `String workloadIdentityPoolId`

        The pool containing the Workload Identity provider that you registered for OpenAI

      - `String workloadIdentityProjectNumber`

        The numeric GCP project number where you registered OpenAI's workload identity

      - `String workloadIdentityProviderId`

        The Workload Identity provider that you registered for OpenAI

      - `Optional<String> kmsKeyVersion`

        An exact CryptoKeyVersion number. Required for PSP decryption; not accepted for EKM.

      - `Optional<Purpose> purpose`

        - `EKM("ekm")`

        - `PSP_DECRYPTION("psp_decryption")`

    - `class Azure:`

      - `String keyName`

        The name of the Azure Key Vault master key that you manage

        `maxLength: 127`

      - `String name`

        A friendly name to identify this config

      - `String tenantId`

        Your Azure tenant UUID

      - `JsonValue; type "azure"constant`

        - `AZURE("azure")`

      - `String vaultUri`

        The URI of the Azure vault containing the master key you manage

      - `Optional<String> keyVersion`

        An exact Azure Key Vault key version. Required for PSP decryption; not accepted for EKM.

      - `Optional<Purpose> purpose`

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
import com.openai.models.admin.organization.externalkeys.ExternalKey;
import com.openai.models.admin.organization.externalkeys.ExternalKeyCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ExternalKeyCreateParams params = ExternalKeyCreateParams.builder()
            .body(ExternalKeyCreateParams.Body.Aws.builder()
                .externalId("external_id")
                .kmsArn("kms_arn")
                .name("name")
                .roleArn("arn:aws:iam::123456789012:role/example-role")
                .build())
            .build();
        ExternalKey externalKey = client.admin().organization().externalKeys().create(params);

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
