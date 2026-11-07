<!-- source: https://developers.openai.com/api/reference/typescript/resources/realtime/subresources/translations/methods/connect/ -->

## Connect

Open a Realtime translation session. The WebSocket URL requires a `model` query parameter.

**WebSocket** `wss://api.openai.com/v1/realtime/translations`

```typescript
import { readFile } from "node:fs/promises";
import OpenAI from "openai";
import { OpenAIRealtimeTranslationWS } from "openai/realtime/translations/ws";

// input.pcm: a short recording of raw 24 kHz mono signed PCM16 little-endian audio.
const pcm = await readFile("input.pcm");
const client = new OpenAI();
const connection = await OpenAIRealtimeTranslationWS.create(client, {
  model: "gpt-realtime-translate",
  options: { handshakeTimeout: 60_000 },
});
connection.on("error", (error) => {
  console.error(error);
  process.exitCode = 1;
  connection.close();
});
connection.on("session.output_transcript.delta", (event) => {
  process.stdout.write(event.delta);
});
try {
  // The helper creates the socket asynchronously; send only after it opens.
  if (connection.socket.readyState === 0) {
    await new Promise((resolve, reject) => {
      connection.socket.once("open", resolve);
      connection.socket.once("error", reject);
      connection.socket.once("close", () =>
        reject(new Error("Connection closed before opening.")),
      );
    });
  if (connection.socket.readyState !== 1)
    throw new Error("WebSocket did not open.");
  // Wait for the new language before sending audio; never wait indefinitely.
  let updateTimeout;
  try {
    await new Promise((resolve, reject) => {
      updateTimeout = setTimeout(
        () => reject(new Error("Timed out waiting for session.updated")),
        60_000,
      );
      connection.once("session.updated", resolve);
      connection.socket.once("close", () =>
        reject(new Error("Connection closed before session.updated")),
      );
      connection.once("error", reject);
      connection.send({
        type: "session.update",
        session: { audio: { output: { language: "es" } } },
      });
    });
  } finally {
    clearTimeout(updateTimeout);
  for (let offset = 0; offset < pcm.length; offset += 9600) {
    connection.send({
      type: "session.input_audio_buffer.append",
      audio: pcm.subarray(offset, offset + 9600).toString("base64"),
    });
  // Send session.close and wait for trailing translation output and session.closed.
  await connection.finish({ timeoutMs: 60_000 });
} finally {
  connection.close();
