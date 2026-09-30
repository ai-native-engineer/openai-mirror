<!-- source: https://developers.openai.com/api/reference/go/resources/live/subresources/sessions/methods/reject/ -->

## Reject call

`client.Live.Sessions.Reject(ctx, sessionID, body) error`

**post** `/live/sessions/{session_id}/reject`

Reject an incoming SIP call. Send a required SIP rejection status_code between 300 and 699.

- `sessionID string`

- `body SessionRejectParams`

  - `StatusCode param.Field[int64]`

    SIP rejection status sent to the caller. This field is required.

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
  err := client.Live.Sessions.Reject(
    context.TODO(),
    "session_id",
    live.SessionRejectParams{
      StatusCode: 486,
  if err != nil {
    panic(err.Error())
