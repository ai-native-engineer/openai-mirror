<!-- source: https://developers.openai.com/api/reference/python/resources/fine_tuning/subresources/jobs/subresources/checkpoints/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Fine Tuning](/api/reference/python/resources/fine_tuning)

[Jobs](/api/reference/python/resources/fine_tuning/subresources/jobs)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Checkpoints

Manage fine-tuning jobs to tailor a model to your specific training data.

##### [List fine-tuning checkpoints](/api/reference/python/resources/fine_tuning/subresources/jobs/subresources/checkpoints/methods/list)

fine\_tuning.jobs.checkpoints.list(strfine\_tuning\_job\_id, CheckpointListParams\*\*kwargs)  -> SyncCursorPage[[FineTuningJobCheckpoint](/api/reference/python/resources/fine_tuning#(resource)%20fine_tuning.jobs.checkpoints%20%3E%20(model)%20fine_tuning_job_checkpoint%20%3E%20(schema))]

GET/fine\_tuning/jobs/{fine\_tuning\_job\_id}/checkpoints

##### ModelsExpand Collapse

class FineTuningJobCheckpoint: …

The `fine_tuning.job.checkpoint` object represents a model checkpoint for a fine-tuning job that is ready to use.

id: str

The checkpoint identifier, which can be referenced in the API endpoints.

created\_at: int

The Unix timestamp (in seconds) for when the checkpoint was created.

formatunixtime

fine\_tuned\_model\_checkpoint: str

The name of the fine-tuned checkpoint model that is created.

fine\_tuning\_job\_id: str

The name of the fine-tuning job that this checkpoint was created from.

metrics: Metrics

Metrics at the step number during the fine-tuning job.

full\_valid\_loss: Optional[float]

full\_valid\_mean\_token\_accuracy: Optional[float]

step: Optional[float]

train\_loss: Optional[float]

train\_mean\_token\_accuracy: Optional[float]

valid\_loss: Optional[float]

valid\_mean\_token\_accuracy: Optional[float]

object: Literal["fine\_tuning.job.checkpoint"]

The object type, which is always “fine\_tuning.job.checkpoint”.

step\_number: int

The step number that the checkpoint was created at.
