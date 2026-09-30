<!-- source: https://developers.openai.com/api/reference/cli/resources/live/subresources/sessions/methods/reject/ -->

## Reject call

`$ openai live:sessions reject`

**post** `/live/sessions/{session_id}/reject`

Reject an incoming SIP call. Send a required SIP rejection status_code between 300 and 699.

- `--session-id: string`

  Opaque Live session identifier from the creation response or incoming-call webhook. Preserve the returned value unchanged, including its prefix.

- `--status-code: number`

  SIP rejection status sent to the caller. This field is required.

```cli
openai live:sessions reject \
  --api-key 'My API Key' \
  --session-id session_id \
  --status-code 486
