<!-- source: https://developers.openai.com/api/reference/go/resources/live/subresources/sessions/methods/hangup/ -->

## Hang up session

`client.Live.Sessions.Hangup(ctx, sessionID) error`

**post** `/live/sessions/{session_id}/hangup`

End a SIP call identified by session_id.

- `sessionID string`

```go
package main

import (
  "context"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  err := client.Live.Sessions.Hangup(context.TODO(), "session_id")
  if err != nil {
    panic(err.Error())
