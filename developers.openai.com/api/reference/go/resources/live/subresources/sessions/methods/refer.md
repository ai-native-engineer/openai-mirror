<!-- source: https://developers.openai.com/api/reference/go/resources/live/subresources/sessions/methods/refer/ -->

## Transfer call

`client.Live.Sessions.Refer(ctx, sessionID, body) error`

**post** `/live/sessions/{session_id}/refer`

Transfer a SIP call to another destination. Supply a nonblank target_uri for the SIP Refer-To header.

- `sessionID string`

- `body SessionReferParams`

  - `TargetUri param.Field[string]`

    Nonblank URI for the SIP Refer-To header, such as tel:+14155550123 or sip:agent@example.com.

```go
package main

import (
  "context"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/live"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  err := client.Live.Sessions.Refer(
    context.TODO(),
    "session_id",
    live.SessionReferParams{
      TargetUri: "tel:+14155550123",
  if err != nil {
    panic(err.Error())
