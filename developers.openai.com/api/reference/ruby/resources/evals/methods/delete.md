<!-- source: https://developers.openai.com/api/reference/ruby/resources/evals/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Evals](/api/reference/ruby/resources/evals)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete an eval

evals.delete(eval\_id) -> [EvalDeleteResponse](/api/reference/ruby/resources/evals#(resource)%20evals%20%3E%20(model)%20eval_delete_response%20%3E%20(schema)) { deleted, eval\_id, object }

DELETE/evals/{eval\_id}

Delete an evaluation.

##### ParametersExpand Collapse

eval\_id: String

##### ReturnsExpand Collapse

class EvalDeleteResponse { deleted, eval\_id, object }

deleted: bool

eval\_id: String

object: String

### Delete an eval

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

eval_ = openai.evals.delete("eval_id")

puts(eval_)

  "object": "eval.deleted",
  "deleted": true,
  "eval_id": "eval_abc123"

##### Returns Examples

  "object": "eval.deleted",
  "deleted": true,
  "eval_id": "eval_abc123"
