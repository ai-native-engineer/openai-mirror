<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/agents/subresources/sessions/subresources/artifacts/methods/content/ -->

[Sessions](/api/reference/resources/beta/subresources/agents/subresources/sessions)

[Artifacts](/api/reference/resources/beta/subresources/agents/subresources/sessions/subresources/artifacts)

# Retrieve agent session artifact content

GET/agents/sessions/{session\_id}/artifacts/{artifact\_id}/content

Downloads immutable session artifact bytes after the execution environment expires. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

session\_id: string

artifact\_id: string

### Retrieve agent session artifact content

curl https://api.openai.com/v1/agents/sessions/$SESSION_ID/artifacts/$ARTIFACT_ID/content \
