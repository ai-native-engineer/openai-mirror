<!-- source: https://developers.openai.com/api/reference/ruby/resources/fine_tuning/subresources/jobs/subresources/checkpoints/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Fine Tuning](/api/reference/ruby/resources/fine_tuning)

[Jobs](/api/reference/ruby/resources/fine_tuning/subresources/jobs)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Checkpoints

Manage fine-tuning jobs to tailor a model to your specific training data.

##### [List fine-tuning checkpoints](/api/reference/ruby/resources/fine_tuning/subresources/jobs/subresources/checkpoints/methods/list)

fine\_tuning.jobs.checkpoints.list(fine\_tuning\_job\_id, \*\*kwargs) -> CursorPage<[FineTuningJobCheckpoint](/api/reference/ruby/resources/fine_tuning#(resource)%20fine_tuning.jobs.checkpoints%20%3E%20(model)%20fine_tuning_job_checkpoint%20%3E%20(schema)) { id, created\_at, fine\_tuned\_model\_checkpoint, 4 more } >

GET/fine\_tuning/jobs/{fine\_tuning\_job\_id}/checkpoints

##### ModelsExpand Collapse

class FineTuningJobCheckpoint { id, created\_at, fine\_tuned\_model\_checkpoint, 4 more }

The `fine_tuning.job.checkpoint` object represents a model checkpoint for a fine-tuning job that is ready to use.

id: String

The checkpoint identifier, which can be referenced in the API endpoints.

created\_at: Integer

The Unix timestamp (in seconds) for when the checkpoint was created.

formatunixtime

fine\_tuned\_model\_checkpoint: String

The name of the fine-tuned checkpoint model that is created.

fine\_tuning\_job\_id: String

The name of the fine-tuning job that this checkpoint was created from.

metrics: Metrics{ full\_valid\_loss, full\_valid\_mean\_token\_accuracy, step, 4 more}

Metrics at the step number during the fine-tuning job.

full\_valid\_loss: Float

full\_valid\_mean\_token\_accuracy: Float

step: Float

train\_loss: Float

train\_mean\_token\_accuracy: Float

valid\_loss: Float

valid\_mean\_token\_accuracy: Float

object: :"fine\_tuning.job.checkpoint"

The object type, which is always “fine\_tuning.job.checkpoint”.

step\_number: Integer

The step number that the checkpoint was created at.
