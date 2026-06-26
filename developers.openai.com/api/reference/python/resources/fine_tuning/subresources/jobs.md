<!-- source: https://developers.openai.com/api/reference/python/resources/fine_tuning/subresources/jobs/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Fine Tuning](/api/reference/python/resources/fine_tuning)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Jobs

Manage fine-tuning jobs to tailor a model to your specific training data.

##### [Create fine-tuning job](/api/reference/python/resources/fine_tuning/subresources/jobs/methods/create)

fine\_tuning.jobs.create(JobCreateParams\*\*kwargs)  -> [FineTuningJob](/api/reference/python/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema))

POST/fine\_tuning/jobs

##### [List fine-tuning jobs](/api/reference/python/resources/fine_tuning/subresources/jobs/methods/list)

fine\_tuning.jobs.list(JobListParams\*\*kwargs)  -> SyncCursorPage[[FineTuningJob](/api/reference/python/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema))]

GET/fine\_tuning/jobs

##### [Retrieve fine-tuning job](/api/reference/python/resources/fine_tuning/subresources/jobs/methods/retrieve)

fine\_tuning.jobs.retrieve(strfine\_tuning\_job\_id)  -> [FineTuningJob](/api/reference/python/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema))

GET/fine\_tuning/jobs/{fine\_tuning\_job\_id}

##### [List fine-tuning events](/api/reference/python/resources/fine_tuning/subresources/jobs/methods/list_events)

fine\_tuning.jobs.list\_events(strfine\_tuning\_job\_id, JobListEventsParams\*\*kwargs)  -> SyncCursorPage[[FineTuningJobEvent](/api/reference/python/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_event%20%3E%20(schema))]

GET/fine\_tuning/jobs/{fine\_tuning\_job\_id}/events

##### [Cancel fine-tuning](/api/reference/python/resources/fine_tuning/subresources/jobs/methods/cancel)

fine\_tuning.jobs.cancel(strfine\_tuning\_job\_id)  -> [FineTuningJob](/api/reference/python/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema))

POST/fine\_tuning/jobs/{fine\_tuning\_job\_id}/cancel

##### [Pause fine-tuning](/api/reference/python/resources/fine_tuning/subresources/jobs/methods/pause)

fine\_tuning.jobs.pause(strfine\_tuning\_job\_id)  -> [FineTuningJob](/api/reference/python/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema))

POST/fine\_tuning/jobs/{fine\_tuning\_job\_id}/pause

##### [Resume fine-tuning](/api/reference/python/resources/fine_tuning/subresources/jobs/methods/resume)

fine\_tuning.jobs.resume(strfine\_tuning\_job\_id)  -> [FineTuningJob](/api/reference/python/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema))

POST/fine\_tuning/jobs/{fine\_tuning\_job\_id}/resume

##### ModelsExpand Collapse

class FineTuningJob: …

The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.

id: str

The object identifier, which can be referenced in the API endpoints.

created\_at: int

The Unix timestamp (in seconds) for when the fine-tuning job was created.

formatunixtime

error: Optional[Error]

For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.

code: str

A machine-readable error code.

message: str

A human-readable error message.

param: Optional[str]

The parameter that was invalid, usually `training_file` or `validation_file`. This field will be null if the failure was not parameter-specific.

fine\_tuned\_model: Optional[str]

The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.

finished\_at: Optional[int]

The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.

formatunixtime

hyperparameters: Hyperparameters

The hyperparameters used for the fine-tuning job. This value will only be returned when running `supervised` jobs.

batch\_size: Optional[Union[Literal["auto"], int, null]]

Number of examples in each batch. A larger batch size means that model parameters
are updated less frequently, but with lower variance.

One of the following:

Literal["auto"]

int

learning\_rate\_multiplier: Optional[Union[Literal["auto"], float, null]]

Scaling factor for the learning rate. A smaller learning rate may be useful to avoid
overfitting.

One of the following:

Literal["auto"]

float

n\_epochs: Optional[Union[Literal["auto"], int, null]]

The number of epochs to train the model for. An epoch refers to one full cycle
through the training dataset.

One of the following:

Literal["auto"]

int

model: str

The base model that is being fine-tuned.

object: Literal["fine\_tuning.job"]

The object type, which is always “fine\_tuning.job”.

organization\_id: str

The organization that owns the fine-tuning job.

result\_files: List[str]

The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

seed: int

The seed used for the fine-tuning job.

status: Literal["validating\_files", "queued", "running", 3 more]

The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.

One of the following:

"validating\_files"

"queued"

"running"

"succeeded"

"failed"

"cancelled"

trained\_tokens: Optional[int]

The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.

training\_file: str

The file ID used for training. You can retrieve the training data with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

validation\_file: Optional[str]

The file ID used for validation. You can retrieve the validation results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

estimated\_finish: Optional[int]

The Unix timestamp (in seconds) for when the fine-tuning job is estimated to finish. The value will be null if the fine-tuning job is not running.

formatunixtime

integrations: Optional[List[[FineTuningJobWandbIntegrationObject](/api/reference/python/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration_object%20%3E%20(schema))]]

A list of integrations to enable for this fine-tuning job.

type: Literal["wandb"]

The type of the integration being enabled for the fine-tuning job

wandb: [FineTuningJobWandbIntegration](/api/reference/python/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration%20%3E%20(schema))

The settings for your integration with Weights and Biases. This payload specifies the project that
metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
to your run, and set a default entity (team, username, etc) to be associated with your run.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

method: Optional[Method]

The method used for fine-tuning.

type: Literal["supervised", "dpo", "reinforcement"]

The type of method. Is either `supervised`, `dpo`, or `reinforcement`.

One of the following:

"supervised"

"dpo"

"reinforcement"

dpo: Optional[DpoMethod]

Configuration for the DPO fine-tuning method.

reinforcement: Optional[ReinforcementMethod]

Configuration for the reinforcement fine-tuning method.

supervised: Optional[SupervisedMethod]

Configuration for the supervised fine-tuning method.

class FineTuningJobEvent: …

Fine-tuning job event object

id: str

The object identifier.

created\_at: int

The Unix timestamp (in seconds) for when the fine-tuning job was created.

formatunixtime

level: Literal["info", "warn", "error"]

The log level of the event.

One of the following:

"info"

"warn"

"error"

message: str

The message of the event.

object: Literal["fine\_tuning.job.event"]

The object type, which is always “fine\_tuning.job.event”.

data: Optional[object]

The data associated with the event.

type: Optional[Literal["message", "metrics"]]

The type of event.

One of the following:

"message"

"metrics"

class FineTuningJobWandbIntegration: …

The settings for your integration with Weights and Biases. This payload specifies the project that
metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
to your run, and set a default entity (team, username, etc) to be associated with your run.

project: str

The name of the project that the new run will be created under.

entity: Optional[str]

The entity to use for the run. This allows you to set the team or username of the WandB user that you would
like associated with the run. If not set, the default entity for the registered WandB API key is used.

name: Optional[str]

A display name to set for the run. If not set, we will use the Job ID as the name.

tags: Optional[List[str]]

A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
default tags are generated by OpenAI: “openai/finetune”, “openai/{base-model}”, “openai/{ftjob-abcdef}”.

class FineTuningJobWandbIntegrationObject: …

type: Literal["wandb"]

The type of the integration being enabled for the fine-tuning job

wandb: [FineTuningJobWandbIntegration](/api/reference/python/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration%20%3E%20(schema))

The settings for your integration with Weights and Biases. This payload specifies the project that
metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
to your run, and set a default entity (team, username, etc) to be associated with your run.

#### JobsCheckpoints

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
