<!-- source: https://developers.openai.com/api/reference/resources/evals/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Evals](/api/reference/resources/evals)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete an eval

DELETE/evals/{eval\_id}

Delete an evaluation.

##### Path ParametersExpand Collapse

eval\_id: string

##### ReturnsExpand Collapse

deleted: boolean

eval\_id: string

object: string

### Delete an eval

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/evals/eval_abc123 \
  -X DELETE \
  -H "Authorization: Bearer $OPENAI_API_KEY"

  "object": "eval.deleted",
  "deleted": true,
  "eval_id": "eval_abc123"

##### Returns Examples

  "object": "eval.deleted",
  "deleted": true,
  "eval_id": "eval_abc123"
