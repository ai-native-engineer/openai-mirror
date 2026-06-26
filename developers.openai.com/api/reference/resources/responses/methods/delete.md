<!-- source: https://developers.openai.com/api/reference/resources/responses/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Responses](/api/reference/resources/responses)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete a model response

DELETE/responses/{response\_id}

Deletes a model response with the given ID.

##### Path ParametersExpand Collapse

response\_id: string

### Delete a model response

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl -X DELETE https://api.openai.com/v1/responses/resp_123 \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $OPENAI_API_KEY"

  "id": "resp_6786a1bec27481909a17d673315b29f6",
  "object": "response",
  "deleted": true

##### Returns Examples

  "id": "resp_6786a1bec27481909a17d673315b29f6",
  "object": "response",
  "deleted": true
