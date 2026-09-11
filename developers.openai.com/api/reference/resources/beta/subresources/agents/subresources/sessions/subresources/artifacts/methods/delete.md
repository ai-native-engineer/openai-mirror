<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/agents/subresources/sessions/subresources/artifacts/methods/delete/ -->

[Sessions](/api/reference/resources/beta/subresources/agents/subresources/sessions)

[Artifacts](/api/reference/resources/beta/subresources/agents/subresources/sessions/subresources/artifacts)

# Delete an agent session artifact

DELETE/agents/sessions/{session\_id}/artifacts/{artifact\_id}

Deletes an immutable session artifact without deleting its live environment file or original Files API object. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

session\_id: string

artifact\_id: string

SessionArtifactDeleted object { id, deleted, object }

Confirmation that an immutable session artifact was deleted.

The ID of the deleted session artifact.

deleted: boolean

Whether the session artifact was deleted. Always `true`.

object: "agent.session.artifact.deleted"

The object type. Always `agent.session.artifact.deleted`.

### Delete an agent session artifact

curl https://api.openai.com/v1/agents/sessions/$SESSION_ID/artifacts/$ARTIFACT_ID \
    -X DELETE \

  "deleted": true,
  "object": "agent.session.artifact.deleted"

  "deleted": true,
  "object": "agent.session.artifact.deleted"
