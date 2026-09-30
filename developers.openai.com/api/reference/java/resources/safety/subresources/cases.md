<!-- source: https://developers.openai.com/api/reference/java/resources/safety/subresources/cases/ -->

# Cases

## Get safety case

`SafetyCase safety().cases().retrieve(CaseRetrieveParamsparams = CaseRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/safety/cases/{id}`

Get a safety case by ID.

### Parameters

- `CaseRetrieveParams params`

  - `Optional<String> id`

    Safety case ID

### Returns

- `class SafetyCase:`

  - `String id`

  - `long createdAt`

  - `String entityIdentifier`

  - `Notice notice`

    - `Type type`

      - `WARNING("warning")`

      - `DEACTIVATION("deactivation")`

  - `JsonValue; object_ "safety.case"constant`

    - `SAFETY_CASE("safety.case")`

  - `Optional<String> reason`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.safety.cases.CaseRetrieveParams;
import com.openai.models.safety.cases.SafetyCase;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        SafetyCase safetyCase = client.safety().cases().retrieve("id");
    }
}
```

#### Response

```json
{
  "id": "id",
  "created_at": 0,
  "entity_identifier": "entity_identifier",
  "notice": {
    "type": "warning"
  },
  "object": "safety.case",
  "reason": "reason"
}
```

## Domain Types

### Safety Case

- `class SafetyCase:`

  - `String id`

  - `long createdAt`

  - `String entityIdentifier`

  - `Notice notice`

    - `Type type`

      - `WARNING("warning")`

      - `DEACTIVATION("deactivation")`

  - `JsonValue; object_ "safety.case"constant`

    - `SAFETY_CASE("safety.case")`

  - `Optional<String> reason`
