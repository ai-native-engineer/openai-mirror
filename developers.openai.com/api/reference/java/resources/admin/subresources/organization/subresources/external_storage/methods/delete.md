<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/external_storage/methods/delete/ -->

## Delete an external storage configuration

`ExternalStorageDeleted admin().organization().externalStorage().delete(ExternalStorageDeleteParamsparams = ExternalStorageDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/organization/external_storage/{external_storage_id}`

Disconnect a customer-managed external storage configuration. Removing the project's last configuration restores organization-default retention if customer-managed retention was active. Repeating a deletion also completes any interrupted retention update. Cloud storage is unchanged.

- `ExternalStorageDeleteParams params`

  - `Optional<String> externalStorageId`

- `class ExternalStorageDeleted:`

  - `String id`

  - `boolean deleted`

  - `JsonValue; object_ "organization.external_storage.deleted"constant`

    - `ORGANIZATION_EXTERNAL_STORAGE_DELETED("organization.external_storage.deleted")`

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

  "deleted": true,
  "object": "organization.external_storage.deleted"
