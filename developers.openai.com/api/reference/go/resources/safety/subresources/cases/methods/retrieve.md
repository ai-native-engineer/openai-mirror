<!-- source: https://developers.openai.com/api/reference/go/resources/safety/subresources/cases/methods/retrieve/ -->

## Get safety case

`client.Safety.Cases.Get(ctx, id) (*SafetyCase, error)`

**get** `/safety/cases/{id}`

Get a safety case by ID.

- `id string`

  Safety case ID

- `type SafetyCase struct{…}`

  - `ID string`

  - `CreatedAt int64`

  - `EntityIdentifier string`

  - `Notice SafetyCaseNotice`

    - `Type string`

      - `const SafetyCaseNoticeTypeWarning SafetyCaseNoticeType = "warning"`

      - `const SafetyCaseNoticeTypeDeactivation SafetyCaseNoticeType = "deactivation"`

  - `Object SafetyCase`

    - `const SafetyCaseSafetyCase SafetyCase = "safety.case"`

  - `Reason string`

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  safetyCase, err := client.Safety.Cases.Get(context.TODO(), "id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", safetyCase.ID)

  "entity_identifier": "entity_identifier",
  "notice": {
    "type": "warning"
  "object": "safety.case",
  "reason": "reason"
