<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/agents/subresources/sessions/subresources/artifacts/methods/retrieve/ -->

## Retrieve an agent session artifact

`beta.agents.sessions.artifacts.retrieve(strartifact_id, ArtifactRetrieveParams**kwargs)  -> SessionArtifact`

**get** `/agents/sessions/{session_id}/artifacts/{artifact_id}`

Retrieves immutable metadata for one durable session artifact. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

- `session_id: str`

- `artifact_id: str`

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
session_artifact = client.beta.agents.sessions.artifacts.retrieve(
    artifact_id="artifact_id",
    session_id="session_id",
print(session_artifact.id)

  "environment_id": "environment_id",
  "object": "agent.session.artifact",
  "path": "path",
  "session_id": "session_id",
  "size_bytes": 0,
  "turn_id": "turn_id"
