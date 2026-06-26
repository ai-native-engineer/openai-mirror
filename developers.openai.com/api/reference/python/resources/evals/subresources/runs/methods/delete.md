<!-- source: https://developers.openai.com/api/reference/python/resources/evals/subresources/runs/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Evals](/api/reference/python/resources/evals)

[Runs](/api/reference/python/resources/evals/subresources/runs)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete eval run

evals.runs.delete(strrun\_id, RunDeleteParams\*\*kwargs)  -> [RunDeleteResponse](/api/reference/python/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20run_delete_response%20%3E%20(schema))

DELETE/evals/{eval\_id}/runs/{run\_id}

Delete an eval run.

##### ParametersExpand Collapse

eval\_id: str

run\_id: str

##### ReturnsExpand Collapse

class RunDeleteResponse: …

deleted: Optional[bool]

object: Optional[str]

run\_id: Optional[str]

### Delete eval run

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

deleted = client.evals.runs.delete(
  "eval_123abc",
  "evalrun_abc456"
print(deleted)

  "object": "eval.run.deleted",
  "deleted": true,
  "run_id": "evalrun_abc456"

##### Returns Examples

  "object": "eval.run.deleted",
  "deleted": true,
  "run_id": "evalrun_abc456"
