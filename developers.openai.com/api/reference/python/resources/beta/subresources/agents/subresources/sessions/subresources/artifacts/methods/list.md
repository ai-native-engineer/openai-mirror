<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/agents/subresources/sessions/subresources/artifacts/methods/list/ -->

## List agent session artifacts

`beta.agents.sessions.artifacts.list(strsession_id, ArtifactListParams**kwargs)  -> SyncCursorPage[SessionArtifact]`

**get** `/agents/sessions/{session_id}/artifacts`

Lists immutable artifacts published by completed hosted session turns. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

- `session_id: str`

- `after: Optional[str]`

  Return artifacts after this immutable artifact ID.

- `environment_id: Optional[str]`

  Restrict the listing to artifacts produced by this environment.

- `limit: Optional[int]`

  The maximum number of artifacts to return, between 1 and 100.

- `order: Optional[Literal["asc", "desc"]]`

  Sort by creation time and ID. Defaults to descending.

  - `"asc"`

    Returns resources in ascending order.

  - `"desc"`

    Returns resources in descending order.

- `class SessionArtifact: …`

  An immutable file published by a completed hosted session turn.

  - `id: str`

    The immutable artifact ID.

  - `created_at: int`

    The Unix timestamp, in seconds, when the artifact was published.

  - `environment_id: str`

    The ID of the environment that produced the artifact.

  - `object: Literal["agent.session.artifact"]`

    The object type. Always `agent.session.artifact`.

    - `"agent.session.artifact"`

  - `path: str`

    The original absolute file path in the execution environment.

  - `session_id: str`

    The ID of the session that owns the artifact.

  - `size_bytes: int`

    The immutable artifact size in bytes.

  - `turn_id: str`

    The ID of the completed turn that published the artifact.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
page = client.beta.agents.sessions.artifacts.list(
    session_id="session_id",
page = page.data[0]
print(page.id)

  "data": [
      "environment_id": "environment_id",
      "object": "agent.session.artifact",
      "path": "path",
      "session_id": "session_id",
      "size_bytes": 0,
      "turn_id": "turn_id"
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
