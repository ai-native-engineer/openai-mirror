<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/external_storage/methods/list/ -->

## List external storage configurations

`ExternalStorageListPage admin().organization().externalStorage().list(ExternalStorageListParamsparams = ExternalStorageListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/organization/external_storage`

List the organization's customer-managed external storage configurations.

- `ExternalStorageListParams params`

  - `Optional<String> after`

    Return external storage configurations after this ID.

  - `Optional<Long> limit`

  - `Optional<Order> order`

    - `ASC("asc")`

    - `DESC("desc")`

  - `Optional<String> projectId`

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
import com.openai.models.admin.organization.externalstorage.ExternalStorageListPage;
import com.openai.models.admin.organization.externalstorage.ExternalStorageListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ExternalStorageListPage page = client.admin().organization().externalStorage().list();

  "data": [
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
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
