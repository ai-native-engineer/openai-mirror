<!-- source: https://developers.openai.com/api/reference/typescript/resources/live/subresources/sessions/methods/download_recording/ -->

## Download recording

`client.live.sessions.downloadRecording(stringsessionID, RequestOptionsoptions?): Response`

**get** `/live/sessions/{session_id}/content`

Get Live session content

- `sessionID: string`

  The ID of the stored Live session to download. Use the session ID returned when the session started with storage enabled.

- `unnamed_schema_3 = Response`

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const response = await client.live.sessions.downloadRecording('live_SQ');

console.log(response);

const content = await response.blob();
console.log(content);
