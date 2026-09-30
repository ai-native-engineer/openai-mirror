<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/agents/subresources/sessions/subresources/artifacts/methods/delete/ -->

## Delete an agent session artifact

`beta.agents.sessions.artifacts.delete(strartifact_id, ArtifactDeleteParams**kwargs)  -> SessionArtifactDeleted`

**delete** `/agents/sessions/{session_id}/artifacts/{artifact_id}`

Deletes an immutable session artifact without deleting its live environment file or original Files API object. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

- `session_id: str`

- `artifact_id: str`

- `class SessionArtifactDeleted: …`

  Confirmation that an immutable session artifact was deleted.

  - `id: str`

    The ID of the deleted session artifact.

  - `deleted: bool`

    Whether the session artifact was deleted. Always `true`.

  - `object: Literal["agent.session.artifact.deleted"]`

    The object type. Always `agent.session.artifact.deleted`.

    - `"agent.session.artifact.deleted"`

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
session_artifact_deleted = client.beta.agents.sessions.artifacts.delete(
    artifact_id="artifact_id",
    session_id="session_id",
print(session_artifact_deleted.id)

  "deleted": true,
  "object": "agent.session.artifact.deleted"
