<!-- source: https://developers.openai.com/api/reference/cli/resources/live/subresources/sessions/methods/download_recording/ -->

## Download recording

`$ openai live:sessions download-recording`

**get** `/live/sessions/{session_id}/content`

Get Live session content

- `--session-id: string`

  The ID of the stored Live session to download. Use the session ID returned when the session started with storage enabled.

- `unnamed_schema_2: file path`

```cli
openai live:sessions download-recording \
  --api-key 'My API Key' \
  --session-id live_SQ
