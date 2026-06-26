<!-- source: https://developers.openai.com/api/reference/resources/evals/subresources/runs/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Evals](/api/reference/resources/evals)

[Runs](/api/reference/resources/evals/subresources/runs)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete eval run

DELETE/evals/{eval\_id}/runs/{run\_id}

Delete an eval run.

##### Path ParametersExpand Collapse

eval\_id: string

run\_id: string

##### ReturnsExpand Collapse

deleted: optional boolean

object: optional string

run\_id: optional string

### Delete eval run

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/evals/eval_123abc/runs/evalrun_abc456 \
  -X DELETE \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json"

  "object": "eval.run.deleted",
  "deleted": true,
  "run_id": "evalrun_abc456"

##### Returns Examples

  "object": "eval.run.deleted",
  "deleted": true,
  "run_id": "evalrun_abc456"
