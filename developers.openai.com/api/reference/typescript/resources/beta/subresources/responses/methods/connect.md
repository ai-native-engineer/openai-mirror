<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/responses/methods/connect/ -->

[API Reference](/api/reference/typescript)

[Beta](/api/reference/typescript/resources/beta)

[Responses](/api/reference/typescript/resources/beta/subresources/responses)

# Connect

client.beta.responses.connect(RequestOptionsoptions?): void

Function

Connect to a persistent Responses API WebSocket. Send `response.create` events and receive response stream events over the socket.

### Connect

TypeScript

import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

await client.beta.responses.connect();
