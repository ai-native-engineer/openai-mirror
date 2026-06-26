<!-- source: https://developers.openai.com/api/reference/cli/resources/fine_tuning/subresources/jobs/subresources/checkpoints/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Fine Tuning](/api/reference/cli/resources/fine_tuning)

[Jobs](/api/reference/cli/resources/fine_tuning/subresources/jobs)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Checkpoints

Manage fine-tuning jobs to tailor a model to your specific training data.

##### [List fine-tuning checkpoints](/api/reference/cli/resources/fine_tuning/subresources/jobs/subresources/checkpoints/methods/list)

$ openai fine-tuning:jobs:checkpoints list

GET/fine\_tuning/jobs/{fine\_tuning\_job\_id}/checkpoints

##### ModelsExpand Collapse

fine\_tuning\_job\_checkpoint: object { id, created\_at, fine\_tuned\_model\_checkpoint, 4 more }

The `fine_tuning.job.checkpoint` object represents a model checkpoint for a fine-tuning job that is ready to use.

id: string

The checkpoint identifier, which can be referenced in the API endpoints.

created\_at: number

The Unix timestamp (in seconds) for when the checkpoint was created.

fine\_tuned\_model\_checkpoint: string

The name of the fine-tuned checkpoint model that is created.

fine\_tuning\_job\_id: string

The name of the fine-tuning job that this checkpoint was created from.

metrics: object { full\_valid\_loss, full\_valid\_mean\_token\_accuracy, step, 4 more }

Metrics at the step number during the fine-tuning job.

full\_valid\_loss: optional number

full\_valid\_mean\_token\_accuracy: optional number

step: optional number

train\_loss: optional number

train\_mean\_token\_accuracy: optional number

valid\_loss: optional number

valid\_mean\_token\_accuracy: optional number

object: "fine\_tuning.job.checkpoint"

The object type, which is always “fine\_tuning.job.checkpoint”.

step\_number: number

The step number that the checkpoint was created at.
