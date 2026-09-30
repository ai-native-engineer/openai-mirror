<!-- source: https://developers.openai.com/api/reference/go/resources/live/subresources/sessions/methods/download_recording/ -->

## Download recording

`client.Live.Sessions.DownloadRecording(ctx, sessionID) (*Response, error)`

**get** `/live/sessions/{session_id}/content`

Get Live session content

- `sessionID string`

  The ID of the stored Live session to download. Use the session ID returned when the session started with storage enabled.

- `type SessionDownloadRecordingResponse interface{…}`

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
  response, err := client.Live.Sessions.DownloadRecording(context.TODO(), "live_SQ")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", response)
