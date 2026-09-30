<!-- source: https://developers.openai.com/api/reference/cli/resources/live/subresources/sessions/methods/hangup/ -->

## Hang up session

`$ openai live:sessions hangup`

**post** `/live/sessions/{session_id}/hangup`

End a SIP call identified by session_id.

- `--session-id: string`

  Opaque Live session identifier from the creation response or incoming-call webhook. Preserve the returned value unchanged, including its prefix.

```cli
openai live:sessions hangup \
  --api-key 'My API Key' \
  --session-id session_id
