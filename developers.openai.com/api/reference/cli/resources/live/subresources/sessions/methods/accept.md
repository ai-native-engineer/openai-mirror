<!-- source: https://developers.openai.com/api/reference/cli/resources/live/subresources/sessions/methods/accept/ -->

## Accept call

`$ openai live:sessions accept`

**post** `/live/sessions/{session_id}/accept`

Accept an incoming SIP call. Supply session with type live, the model, and startup configuration. Before accepting calls, follow the [Live prompting guide](/api/docs/guides/live-prompting) to write frontend conversation instructions and a separate backend prompt. SIP media format is negotiated; omit audio.format.

- `--session-id: string`

  Opaque Live session identifier from the creation response or incoming-call webhook. Preserve the returned value unchanged, including its prefix.

- `--session: object { model, type, audio, 4 more }`

  Model and startup configuration for the Live session that answers the incoming SIP call.

```cli
openai live:sessions accept \
  --api-key 'My API Key' \
  --session-id session_id \
  --session '{model: gpt-live-1, type: live}'
