<!-- source: https://developers.openai.com/api/reference/typescript/resources/live/subresources/sessions/methods/hangup/ -->

## Hang up session

`client.live.sessions.hangup(stringsessionID, RequestOptionsoptions?): void`

**post** `/live/sessions/{session_id}/hangup`

End a SIP call identified by session_id.

- `sessionID: string`

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

await client.live.sessions.hangup('session_id');
