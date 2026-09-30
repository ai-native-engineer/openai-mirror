<!-- source: https://developers.openai.com/api/reference/python/resources/live/subresources/sessions/methods/hangup/ -->

## Hang up session

`live.sessions.hangup(strsession_id)`

**post** `/live/sessions/{session_id}/hangup`

End a SIP call identified by session_id.

- `session_id: str`

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
client.live.sessions.hangup(
    "session_id",
