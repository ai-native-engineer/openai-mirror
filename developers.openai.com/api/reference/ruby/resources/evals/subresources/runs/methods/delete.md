<!-- source: https://developers.openai.com/api/reference/ruby/resources/evals/subresources/runs/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Evals](/api/reference/ruby/resources/evals)

[Runs](/api/reference/ruby/resources/evals/subresources/runs)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete eval run

evals.runs.delete(run\_id, \*\*kwargs) -> [RunDeleteResponse](/api/reference/ruby/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20run_delete_response%20%3E%20(schema)) { deleted, object, run\_id }

DELETE/evals/{eval\_id}/runs/{run\_id}

Delete an eval run.

##### ParametersExpand Collapse

eval\_id: String

run\_id: String

##### ReturnsExpand Collapse

class RunDeleteResponse { deleted, object, run\_id }

deleted: bool

object: String

run\_id: String

### Delete eval run

Ruby

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

run = openai.evals.runs.delete("run_id", eval_id: "eval_id")

puts(run)

  "object": "eval.run.deleted",
  "deleted": true,
  "run_id": "evalrun_abc456"

##### Returns Examples

  "object": "eval.run.deleted",
  "deleted": true,
  "run_id": "evalrun_abc456"
