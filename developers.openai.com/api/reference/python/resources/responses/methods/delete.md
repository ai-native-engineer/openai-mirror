<!-- source: https://developers.openai.com/api/reference/python/resources/responses/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Responses](/api/reference/python/resources/responses)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete a model response

responses.delete(strresponse\_id)

DELETE/responses/{response\_id}

Deletes a model response with the given ID.

##### ParametersExpand Collapse

response\_id: str

### Delete a model response

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

from openai import OpenAI
client = OpenAI()

response = client.responses.delete("resp_123")
print(response)

  "id": "resp_6786a1bec27481909a17d673315b29f6",
  "object": "response",
  "deleted": true

##### Returns Examples

  "id": "resp_6786a1bec27481909a17d673315b29f6",
  "object": "response",
  "deleted": true
