<!-- source: https://developers.openai.com/api/reference/go/resources/safety/subresources/alerts/ -->

# Alerts

## Get project safety alert

`client.Safety.Alerts.Get(ctx, id) (*SafetyAlert, error)`

**get** `/safety/alerts/{id}`

Get a safety alert belonging to the authenticated API project.

### Parameters

- `id string`

  Project safety alert ID

### Returns

- `type SafetyAlert struct{…}`

  - `ID string`

  - `CreatedAt int64`

  - `ErrorType SafetyAlertErrorType`

    - `const SafetyAlertErrorTypePotentiallyUnintendedDataTransfer SafetyAlertErrorType = "potentially_unintended_data_transfer"`

    - `const SafetyAlertErrorTypePotentiallyUnintendedDataAccess SafetyAlertErrorType = "potentially_unintended_data_access"`

    - `const SafetyAlertErrorTypePotentiallyUnintendedDestructiveActivity SafetyAlertErrorType = "potentially_unintended_destructive_activity"`

    - `const SafetyAlertErrorTypeOther SafetyAlertErrorType = "other"`

  - `Model string`

  - `Object SafetyAlert`

    - `const SafetyAlertSafetyAlert SafetyAlert = "safety.alert"`

  - `Reason string`

    A customer-safe description derived from error_type, or null for zero data retention requests.

  - `RequestID string`

  - `RequestPaused bool`

    Whether block registration succeeded for this request. This does not confirm that response execution stopped.

  - `ResponseID string`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  safetyAlert, err := client.Safety.Alerts.Get(context.TODO(), "id")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", safetyAlert.ID)
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

- `type SafetyAlert struct{…}`

  - `ID string`

  - `CreatedAt int64`

  - `ErrorType SafetyAlertErrorType`

    - `const SafetyAlertErrorTypePotentiallyUnintendedDataTransfer SafetyAlertErrorType = "potentially_unintended_data_transfer"`

    - `const SafetyAlertErrorTypePotentiallyUnintendedDataAccess SafetyAlertErrorType = "potentially_unintended_data_access"`

    - `const SafetyAlertErrorTypePotentiallyUnintendedDestructiveActivity SafetyAlertErrorType = "potentially_unintended_destructive_activity"`

    - `const SafetyAlertErrorTypeOther SafetyAlertErrorType = "other"`

  - `Model string`

  - `Object SafetyAlert`

    - `const SafetyAlertSafetyAlert SafetyAlert = "safety.alert"`

  - `Reason string`

    A customer-safe description derived from error_type, or null for zero data retention requests.

  - `RequestID string`

  - `RequestPaused bool`

    Whether block registration succeeded for this request. This does not confirm that response execution stopped.

  - `ResponseID string`
