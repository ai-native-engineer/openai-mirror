<!-- source: https://developers.openai.com/api/reference/python/resources/realtime/subresources/translations/methods/connect/ -->

## Connect

Open a Realtime translation session. The WebSocket URL requires a `model` query parameter.

**WebSocket** `wss://api.openai.com/v1/realtime/translations`

```python
import asyncio
import base64

from openai import AsyncOpenAI

async def main() -> None:
    # input.pcm: a short recording, raw 24 kHz mono PCM16 little-endian.
    async with AsyncOpenAI() as client:
        with open("input.pcm", "rb") as audio:
            async with client.realtime.translations.connect(
                model="gpt-realtime-translate"
            ) as connection:
                await connection.session.update(
                    session={"audio": {"output": {"language": "es"}}}
                # Wait for the new language before sending any audio.
                async for event in connection:
                    if event.type == "error":
                        raise RuntimeError(event.error.model_dump_json())
                    if event.type == "session.updated":
                        break
                    if event.type == "session.closed":
                        raise RuntimeError("Translation closed before session.updated")
                else:
                    raise RuntimeError("WebSocket closed before session.updated")
                # 200 ms per 9600-byte chunk. EOF ends this prerecorded input.
                while chunk := audio.read(9600):
                    await connection.session.input_audio_buffer.append(
                        audio=base64.b64encode(chunk).decode("ascii")
                # Closing flushes remaining audio. Drain the final translated text.
                await connection.session.close()
                async for event in connection:
                    if event.type == "session.output_transcript.delta":
                        print(event.delta, end="", flush=True)
                    elif event.type == "error":
                        raise RuntimeError(event.error.model_dump_json())
                    elif event.type == "session.closed":
                        print()
                        return
                raise RuntimeError("WebSocket closed before session.closed")

async def run() -> None:
    await asyncio.wait_for(main(), timeout=60)

asyncio.run(run())
