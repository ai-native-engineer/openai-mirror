<!-- source: https://developers.openai.com/api/reference/typescript/resources/evals/subresources/runs/methods/delete/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Evals](/api/reference/typescript/resources/evals)

[Runs](/api/reference/typescript/resources/evals/subresources/runs)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Delete eval run

client.evals.runs.delete(stringrunID, RunDeleteParams { eval\_id } params, RequestOptionsoptions?): [RunDeleteResponse](/api/reference/typescript/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20run_delete_response%20%3E%20(schema)) { deleted, object, run\_id }

DELETE/evals/{eval\_id}/runs/{run\_id}

Delete an eval run.

##### ParametersExpand Collapse

runID: string

params: RunDeleteParams { eval\_id }

eval\_id: string

The ID of the evaluation to delete the run from.

##### ReturnsExpand Collapse

RunDeleteResponse { deleted, object, run\_id }

deleted?: boolean

object?: string

run\_id?: string

### Delete eval run

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

const deleted = await openai.evals.runs.delete(
  "eval_123abc",
  "evalrun_abc456"
);
console.log(deleted);

  "object": "eval.run.deleted",
  "deleted": true,
  "run_id": "evalrun_abc456"

##### Returns Examples

  "object": "eval.run.deleted",
  "deleted": true,
  "run_id": "evalrun_abc456"
