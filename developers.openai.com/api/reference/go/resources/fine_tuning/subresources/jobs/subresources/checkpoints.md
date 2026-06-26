<!-- source: https://developers.openai.com/api/reference/go/resources/fine_tuning/subresources/jobs/subresources/checkpoints/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Fine Tuning](/api/reference/go/resources/fine_tuning)

[Jobs](/api/reference/go/resources/fine_tuning/subresources/jobs)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Checkpoints

Manage fine-tuning jobs to tailor a model to your specific training data.

##### [List fine-tuning checkpoints](/api/reference/go/resources/fine_tuning/subresources/jobs/subresources/checkpoints/methods/list)

client.FineTuning.Jobs.Checkpoints.List(ctx, fineTuningJobID, query) (\*CursorPage[[FineTuningJobCheckpoint](/api/reference/go/resources/fine_tuning#(resource)%20fine_tuning.jobs.checkpoints%20%3E%20(model)%20fine_tuning_job_checkpoint%20%3E%20(schema))], error)

GET/fine\_tuning/jobs/{fine\_tuning\_job\_id}/checkpoints

##### ModelsExpand Collapse

type FineTuningJobCheckpoint struct{…}

The `fine_tuning.job.checkpoint` object represents a model checkpoint for a fine-tuning job that is ready to use.

ID string

The checkpoint identifier, which can be referenced in the API endpoints.

CreatedAt int64

The Unix timestamp (in seconds) for when the checkpoint was created.

formatunixtime

FineTunedModelCheckpoint string

The name of the fine-tuned checkpoint model that is created.

FineTuningJobID string

The name of the fine-tuning job that this checkpoint was created from.

Metrics FineTuningJobCheckpointMetrics

Metrics at the step number during the fine-tuning job.

FullValidLoss float64Optional

FullValidMeanTokenAccuracy float64Optional

Step float64Optional

TrainLoss float64Optional

TrainMeanTokenAccuracy float64Optional

ValidLoss float64Optional

ValidMeanTokenAccuracy float64Optional

Object FineTuningJobCheckpoint

The object type, which is always “fine\_tuning.job.checkpoint”.

StepNumber int64

The step number that the checkpoint was created at.
