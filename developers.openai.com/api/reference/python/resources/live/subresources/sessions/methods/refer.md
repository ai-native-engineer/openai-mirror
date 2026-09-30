<!-- source: https://developers.openai.com/api/reference/python/resources/live/subresources/sessions/methods/refer/ -->

## Transfer call

`live.sessions.refer(strsession_id, SessionReferParams**kwargs)`

**post** `/live/sessions/{session_id}/refer`

Transfer a SIP call to another destination. Supply a nonblank target_uri for the SIP Refer-To header.

- `session_id: str`

- `target_uri: str`

  Nonblank URI for the SIP Refer-To header, such as tel:+14155550123 or sip:agent@example.com.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
client.live.sessions.refer(
    session_id="session_id",
    target_uri="tel:+14155550123",
