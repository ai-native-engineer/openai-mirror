<!-- source: https://developers.openai.com/api/reference/python/resources/live/subresources/sessions/methods/reject/ -->

## Reject call

`live.sessions.reject(strsession_id, SessionRejectParams**kwargs)`

**post** `/live/sessions/{session_id}/reject`

Reject an incoming SIP call. Send a required SIP rejection status_code between 300 and 699.

- `session_id: str`

- `status_code: int`

  SIP rejection status sent to the caller. This field is required.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
client.live.sessions.reject(
    session_id="session_id",
    status_code=486,
