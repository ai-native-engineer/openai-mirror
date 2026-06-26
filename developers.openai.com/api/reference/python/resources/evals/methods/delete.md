<!-- source: https://developers.openai.com/api/reference/python/resources/evals/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Evals](/api/reference/python/resources/evals)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete an eval

evals.delete(streval\_id)  -> [EvalDeleteResponse](/api/reference/python/resources/evals#(resource)%20evals%20%3E%20(model)%20eval_delete_response%20%3E%20(schema))

DELETE/evals/{eval\_id}

Delete an evaluation.

##### ParametersExpand Collapse

eval\_id: str

##### ReturnsExpand Collapse

class EvalDeleteResponse: …

deleted: bool

eval\_id: str

object: str

### Delete an eval

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

deleted = client.evals.delete("eval_abc123")
print(deleted)

  "object": "eval.deleted",
  "deleted": true,
  "eval_id": "eval_abc123"

##### Returns Examples

  "object": "eval.deleted",
  "deleted": true,
  "eval_id": "eval_abc123"
