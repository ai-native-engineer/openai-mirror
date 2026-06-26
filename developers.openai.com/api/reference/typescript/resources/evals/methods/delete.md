<!-- source: https://developers.openai.com/api/reference/typescript/resources/evals/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Evals](/api/reference/typescript/resources/evals)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete an eval

client.evals.delete(stringevalID, RequestOptionsoptions?): [EvalDeleteResponse](/api/reference/typescript/resources/evals#(resource)%20evals%20%3E%20(model)%20eval_delete_response%20%3E%20(schema)) { deleted, eval\_id, object }

DELETE/evals/{eval\_id}

Delete an evaluation.

##### ParametersExpand Collapse

evalID: string

##### ReturnsExpand Collapse

EvalDeleteResponse { deleted, eval\_id, object }

deleted: boolean

eval\_id: string

object: string

### Delete an eval

TypeScript

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

import OpenAI from "openai";

const openai = new OpenAI();

const deleted = await openai.evals.delete("eval_abc123");
console.log(deleted);

  "object": "eval.deleted",
  "deleted": true,
  "eval_id": "eval_abc123"

##### Returns Examples

  "object": "eval.deleted",
  "deleted": true,
  "eval_id": "eval_abc123"
