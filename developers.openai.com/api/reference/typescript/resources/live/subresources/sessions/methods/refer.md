<!-- source: https://developers.openai.com/api/reference/typescript/resources/live/subresources/sessions/methods/refer/ -->

## Transfer call

`client.live.sessions.refer(stringsessionID, SessionReferParamsbody, RequestOptionsoptions?): void`

**post** `/live/sessions/{session_id}/refer`

Transfer a SIP call to another destination. Supply a nonblank target_uri for the SIP Refer-To header.

- `sessionID: string`

- `body: SessionReferParams`

  - `target_uri: string`

    Nonblank URI for the SIP Refer-To header, such as tel:+14155550123 or sip:agent@example.com.

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

await client.live.sessions.refer('session_id', { target_uri: 'tel:+14155550123' });
