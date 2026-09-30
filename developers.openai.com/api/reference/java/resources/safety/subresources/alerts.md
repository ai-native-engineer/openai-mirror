<!-- source: https://developers.openai.com/api/reference/java/resources/safety/subresources/alerts/ -->

# Alerts

## Get project safety alert

`SafetyAlert safety().alerts().retrieve(AlertRetrieveParamsparams = AlertRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/safety/alerts/{id}`

Get a safety alert belonging to the authenticated API project.

### Parameters

- `AlertRetrieveParams params`

  - `Optional<String> id`

    Project safety alert ID

### Returns

- `class SafetyAlert:`

  - `String id`

  - `long createdAt`

  - `ErrorType errorType`

    - `POTENTIALLY_UNINTENDED_DATA_TRANSFER("potentially_unintended_data_transfer")`

    - `POTENTIALLY_UNINTENDED_DATA_ACCESS("potentially_unintended_data_access")`

    - `POTENTIALLY_UNINTENDED_DESTRUCTIVE_ACTIVITY("potentially_unintended_destructive_activity")`

    - `OTHER("other")`

  - `String model`

  - `JsonValue; object_ "safety.alert"constant`

    - `SAFETY_ALERT("safety.alert")`

  - `Optional<String> reason`

    A customer-safe description derived from error_type, or null for zero data retention requests.

  - `String requestId`

  - `boolean requestPaused`

    Whether block registration succeeded for this request. This does not confirm that response execution stopped.

  - `String responseId`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.safety.alerts.AlertRetrieveParams;
import com.openai.models.safety.alerts.SafetyAlert;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        SafetyAlert safetyAlert = client.safety().alerts().retrieve("id");
    }
}
```

#### Response

```json
{
  "id": "id",
  "created_at": 0,
  "error_type": "potentially_unintended_data_transfer",
  "model": "model",
  "object": "safety.alert",
  "reason": "reason",
  "request_id": "request_id",
  "request_paused": true,
  "response_id": "response_id"
}
```

## Domain Types

### Safety Alert

- `class SafetyAlert:`

  - `String id`

  - `long createdAt`

  - `ErrorType errorType`

    - `POTENTIALLY_UNINTENDED_DATA_TRANSFER("potentially_unintended_data_transfer")`

    - `POTENTIALLY_UNINTENDED_DATA_ACCESS("potentially_unintended_data_access")`

    - `POTENTIALLY_UNINTENDED_DESTRUCTIVE_ACTIVITY("potentially_unintended_destructive_activity")`

    - `OTHER("other")`

  - `String model`

  - `JsonValue; object_ "safety.alert"constant`

    - `SAFETY_ALERT("safety.alert")`

  - `Optional<String> reason`

    A customer-safe description derived from error_type, or null for zero data retention requests.

  - `String requestId`

  - `boolean requestPaused`

    Whether block registration succeeded for this request. This does not confirm that response execution stopped.

  - `String responseId`
