<!-- source: https://developers.openai.com/api/reference/python/resources/live/subresources/sessions/methods/download_recording/ -->

## Download recording

`live.sessions.download_recording(strsession_id)  -> BinaryResponseContent`

**get** `/live/sessions/{session_id}/content`

Get Live session content

- `session_id: str`

  The ID of the stored Live session to download. Use the session ID returned when the session started with storage enabled.

- `BinaryResponseContent`

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
response = client.live.sessions.download_recording(
    "live_SQ",
print(response)
content = response.read()
print(content)
