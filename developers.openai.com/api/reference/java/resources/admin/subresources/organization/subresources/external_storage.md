<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/external_storage/ -->

# External Storage

## Create an external storage configuration

`ExternalStorageConfiguration admin().organization().externalStorage().create(ExternalStorageCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/organization/external_storage`

Register one customer-managed external storage configuration.

### Parameters

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

### Returns

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

### Example

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
    }
}
```

#### Response

```json
{
  "id": "id",
  "created_at": 0,
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
  },
  "status": "pending"
}
```

## Delete an external storage configuration

`ExternalStorageDeleted admin().organization().externalStorage().delete(ExternalStorageDeleteParamsparams = ExternalStorageDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/organization/external_storage/{external_storage_id}`

Disconnect a customer-managed external storage configuration. Removing the project's last configuration restores organization-default retention if customer-managed retention was active. Repeating a deletion also completes any interrupted retention update. Cloud storage is unchanged.

### Parameters

- `ExternalStorageDeleteParams params`

  - `Optional<String> externalStorageId`

### Returns

- `class ExternalStorageDeleted:`

  - `String id`

  - `boolean deleted`

  - `JsonValue; object_ "organization.external_storage.deleted"constant`

    - `ORGANIZATION_EXTERNAL_STORAGE_DELETED("organization.external_storage.deleted")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.admin.organization.externalstorage.ExternalStorageDeleteParams;
import com.openai.models.admin.organization.externalstorage.ExternalStorageDeleted;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ExternalStorageDeleted externalStorageDeleted = client.admin().organization().externalStorage().delete("extstorage_123");
    }
}
```

#### Response

```json
{
  "id": "id",
  "deleted": true,
  "object": "organization.external_storage.deleted"
}
```

## List external storage configurations

`ExternalStorageListPage admin().organization().externalStorage().list(ExternalStorageListParamsparams = ExternalStorageListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/organization/external_storage`

List the organization's customer-managed external storage configurations.

### Parameters

- `ExternalStorageListParams params`

  - `Optional<String> after`

    Return external storage configurations after this ID.

  - `Optional<Long> limit`

  - `Optional<Order> order`

    - `ASC("asc")`

    - `DESC("desc")`

  - `Optional<String> projectId`

### Returns

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

### Example

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
    }
}
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "created_at": 0,
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
      },
      "status": "pending"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Get an external storage configuration

`ExternalStorageConfiguration admin().organization().externalStorage().retrieve(ExternalStorageRetrieveParamsparams = ExternalStorageRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/organization/external_storage/{external_storage_id}`

Get one customer-managed external storage configuration.

### Parameters

- `ExternalStorageRetrieveParams params`

  - `Optional<String> externalStorageId`

### Returns

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

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.admin.organization.externalstorage.ExternalStorageConfiguration;
import com.openai.models.admin.organization.externalstorage.ExternalStorageRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ExternalStorageConfiguration externalStorageConfiguration = client.admin().organization().externalStorage().retrieve("extstorage_123");
    }
}
```

#### Response

```json
{
  "id": "id",
  "created_at": 0,
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
  },
  "status": "pending"
}
```

## Validate an external storage configuration

`ExternalStorageConfiguration admin().organization().externalStorage().validate(ExternalStorageValidateParamsparams = ExternalStorageValidateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/organization/external_storage/{external_storage_id}/validate`

Validate one customer-managed external storage configuration.

### Parameters

- `ExternalStorageValidateParams params`

  - `Optional<String> externalStorageId`

### Returns

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

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.admin.organization.externalstorage.ExternalStorageConfiguration;
import com.openai.models.admin.organization.externalstorage.ExternalStorageValidateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ExternalStorageConfiguration externalStorageConfiguration = client.admin().organization().externalStorage().validate("extstorage_123");
    }
}
```

#### Response

```json
{
  "id": "id",
  "created_at": 0,
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
  },
  "status": "pending"
}
```

## Domain Types

### Aws External Storage Provider

- `class AwsExternalStorageProvider:`

  - `String accountId`

  - `String bucket`

  - `String externalId`

  - `String region`

  - `String roleArn`

  - `JsonValue; type "aws"constant`

    - `AWS("aws")`

### Azure External Storage Provider

- `class AzureExternalStorageProvider:`

  - `String accountName`

  - `String container`

  - `String region`

  - `String resourceGroup`

  - `String subscriptionId`

  - `String tenantId`

  - `JsonValue; type "azure"constant`

    - `AZURE("azure")`

### External Storage Configuration

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

### External Storage Deleted

- `class ExternalStorageDeleted:`

  - `String id`

  - `boolean deleted`

  - `JsonValue; object_ "organization.external_storage.deleted"constant`

    - `ORGANIZATION_EXTERNAL_STORAGE_DELETED("organization.external_storage.deleted")`
