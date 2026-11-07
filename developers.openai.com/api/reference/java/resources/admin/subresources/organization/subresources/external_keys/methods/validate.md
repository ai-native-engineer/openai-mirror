<!-- source: https://developers.openai.com/api/reference/java/resources/admin/subresources/organization/subresources/external_keys/methods/validate/ -->

## Validate an external key config for the user's organization

`ExternalKeyValidateResponse admin().organization().externalKeys().validate(ExternalKeyValidateParamsparams = ExternalKeyValidateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/organization/external_keys/{external_key_id}/validate`

Validate an external key config for the user's organization

- `ExternalKeyValidateParams params`

  - `Optional<String> externalKeyId`

- `class ExternalKeyValidateResponse:`

  - `String status`

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.admin.organization.externalkeys.ExternalKeyValidateParams;
import com.openai.models.admin.organization.externalkeys.ExternalKeyValidateResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ExternalKeyValidateResponse response = client.admin().organization().externalKeys().validate("external_key_id");

  "status": "status"
