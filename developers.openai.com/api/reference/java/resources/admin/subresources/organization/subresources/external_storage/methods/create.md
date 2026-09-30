<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/external_storage/methods/create/ -->

## Create an external storage configuration

`ExternalStorageConfiguration admin().organization().externalStorage().create(ExternalStorageCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/organization/external_storage`

Register one customer-managed external storage configuration.

- `ExternalStorageCreateParams params`

  - `String projectId`

  - `Provider provider`

    - `class Aws:`

      - `String bucket`

      - `String roleArn`

      - `JsonValue; type "aws"constant`

        - `AWS("aws")`

    - `class Azure:`

      - `String accountName`

      - `String container`

      - `String resourceGroup`

      - `String subscriptionId`

      - `String tenantId`

      - `JsonValue; type "azure"constant`

        - `AZURE("azure")`

- `class ExternalStorageConfiguration:`

  - `String id`

  - `long createdAt`

  - `String geography`

  - `JsonValue; object_ "organization.external_storage"constant`

    - `ORGANIZATION_EXTERNAL_STORAGE("organization.external_storage")`

  - `String projectId`

  - `Provider provider`

    - `class AwsExternalStorageProvider:`

      - `String accountId`

      - `String bucket`

      - `String externalId`

      - `String region`

      - `String roleArn`

      - `JsonValue; type "aws"constant`

        - `AWS("aws")`

    - `class AzureExternalStorageProvider:`

      - `String accountName`

      - `String container`

      - `String region`

      - `String resourceGroup`

      - `String subscriptionId`

      - `String tenantId`

      - `JsonValue; type "azure"constant`

        - `AZURE("azure")`

  - `Status status`

    - `PENDING("pending")`

    - `VALIDATED("validated")`

    - `UNHEALTHY("unhealthy")`

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.admin.organization.externalstorage.ExternalStorageConfiguration;
import com.openai.models.admin.organization.externalstorage.ExternalStorageCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ExternalStorageCreateParams params = ExternalStorageCreateParams.builder()
            .projectId("proj_123")
            .provider(ExternalStorageCreateParams.Provider.Aws.builder()
                .bucket("bucket")
                .roleArn("role_arn")
                .build())
            .build();
        ExternalStorageConfiguration externalStorageConfiguration = client.admin().organization().externalStorage().create(params);

  "geography": "geography",
  "object": "organization.external_storage",
  "project_id": "project_id",
  "provider": {
    "account_id": "account_id",
    "bucket": "bucket",
    "external_id": "external_id",
    "region": "region",
    "role_arn": "role_arn",
    "type": "aws"
  "status": "pending"
