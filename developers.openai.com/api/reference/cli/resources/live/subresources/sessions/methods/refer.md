<!-- source: https://developers.openai.com/api/reference/cli/resources/live/subresources/sessions/methods/refer/ -->

## Transfer call

`$ openai live:sessions refer`

**post** `/live/sessions/{session_id}/refer`

Transfer a SIP call to another destination. Supply a nonblank target_uri for the SIP Refer-To header.

- `--session-id: string`

  Opaque Live session identifier from the creation response or incoming-call webhook. Preserve the returned value unchanged, including its prefix.

- `--target-uri: string`

  Nonblank URI for the SIP Refer-To header, such as tel:+14155550123 or sip:agent@example.com.

```cli
openai live:sessions refer \
  --api-key 'My API Key' \
  --session-id session_id \
  --target-uri tel:+14155550123
