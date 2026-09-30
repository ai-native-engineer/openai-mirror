<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/agents/subresources/sessions/subresources/artifacts/methods/content/ -->

## Retrieve agent session artifact content

`beta.agents.sessions.artifacts.content(strartifact_id, ArtifactContentParams**kwargs)  -> BinaryResponseContent`

**get** `/agents/sessions/{session_id}/artifacts/{artifact_id}/content`

Downloads immutable session artifact bytes after the execution environment expires. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

- `session_id: str`

- `artifact_id: str`

- `BinaryResponseContent`

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
response = client.beta.agents.sessions.artifacts.content(
    artifact_id="artifact_id",
    session_id="session_id",
print(response)
content = response.read()
print(content)
