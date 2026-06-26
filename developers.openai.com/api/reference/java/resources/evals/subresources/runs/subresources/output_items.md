<!-- source: https://developers.openai.com/api/reference/java/resources/evals/subresources/runs/subresources/output_items/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Evals](/api/reference/java/resources/evals)

[Runs](/api/reference/java/resources/evals/subresources/runs)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Output Items

Manage and run evals in the OpenAI platform.

##### [Get eval run output items](/api/reference/java/resources/evals/subresources/runs/subresources/output_items/methods/list)

OutputItemListPage evals().runs().outputItems().list(OutputItemListParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/evals/{eval\_id}/runs/{run\_id}/output\_items

##### [Get an output item of an eval run](/api/reference/java/resources/evals/subresources/runs/subresources/output_items/methods/retrieve)

[OutputItemRetrieveResponse](/api/reference/java/resources/evals#(resource)%20evals.runs.output_items%20%3E%20(model)%20OutputItemRetrieveResponse%20%3E%20(schema)) evals().runs().outputItems().retrieve(OutputItemRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/evals/{eval\_id}/runs/{run\_id}/output\_items/{output\_item\_id}
