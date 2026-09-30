<!-- source: https://developers.openai.com/api/reference/typescript/resources/live/subresources/sessions/methods/reject/ -->

## Reject call

`client.live.sessions.reject(stringsessionID, SessionRejectParamsbody, RequestOptionsoptions?): void`

**post** `/live/sessions/{session_id}/reject`

Reject an incoming SIP call. Send a required SIP rejection status_code between 300 and 699.

- `sessionID: string`

- `body: SessionRejectParams`

  - `status_code: number`

    SIP rejection status sent to the caller. This field is required.

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

await client.live.sessions.reject('session_id', { status_code: 486 });
