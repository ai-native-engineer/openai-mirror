<!-- source: https://developers.openai.com/api/reference/resources/fine_tuning/subresources/jobs/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Fine Tuning](/api/reference/resources/fine_tuning)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Jobs

Manage fine-tuning jobs to tailor a model to your specific training data.

##### [Create fine-tuning job](/api/reference/resources/fine_tuning/subresources/jobs/methods/create)

POST/fine\_tuning/jobs

##### [List fine-tuning jobs](/api/reference/resources/fine_tuning/subresources/jobs/methods/list)

GET/fine\_tuning/jobs

##### [Retrieve fine-tuning job](/api/reference/resources/fine_tuning/subresources/jobs/methods/retrieve)

GET/fine\_tuning/jobs/{fine\_tuning\_job\_id}

##### [List fine-tuning events](/api/reference/resources/fine_tuning/subresources/jobs/methods/list_events)

GET/fine\_tuning/jobs/{fine\_tuning\_job\_id}/events

##### [Cancel fine-tuning](/api/reference/resources/fine_tuning/subresources/jobs/methods/cancel)

POST/fine\_tuning/jobs/{fine\_tuning\_job\_id}/cancel

##### [Pause fine-tuning](/api/reference/resources/fine_tuning/subresources/jobs/methods/pause)

POST/fine\_tuning/jobs/{fine\_tuning\_job\_id}/pause

##### [Resume fine-tuning](/api/reference/resources/fine_tuning/subresources/jobs/methods/resume)

POST/fine\_tuning/jobs/{fine\_tuning\_job\_id}/resume

##### ModelsExpand Collapse

FineTuningJob object { id, created\_at, error, 16 more }

The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.

id: string

The object identifier, which can be referenced in the API endpoints.

created\_at: number

The Unix timestamp (in seconds) for when the fine-tuning job was created.

formatunixtime

error: object { code, message, param }

For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.

code: string

A machine-readable error code.

message: string

A human-readable error message.

param: string

The parameter that was invalid, usually `training_file` or `validation_file`. This field will be null if the failure was not parameter-specific.

fine\_tuned\_model: string

The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.

finished\_at: number

The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.

formatunixtime

hyperparameters: object { batch\_size, learning\_rate\_multiplier, n\_epochs }

The hyperparameters used for the fine-tuning job. This value will only be returned when running `supervised` jobs.

batch\_size: optional "auto" or number

Number of examples in each batch. A larger batch size means that model parameters
are updated less frequently, but with lower variance.

One of the following:

"auto"

number

learning\_rate\_multiplier: optional "auto" or number

Scaling factor for the learning rate. A smaller learning rate may be useful to avoid
overfitting.

One of the following:

"auto"

number

n\_epochs: optional "auto" or number

The number of epochs to train the model for. An epoch refers to one full cycle
through the training dataset.

One of the following:

"auto"

number

model: string

The base model that is being fine-tuned.

object: "fine\_tuning.job"

The object type, which is always “fine\_tuning.job”.

organization\_id: string

The organization that owns the fine-tuning job.

result\_files: array of string

The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](/docs/api-reference/files/retrieve-contents).

seed: number

The seed used for the fine-tuning job.

status: "validating\_files" or "queued" or "running" or 3 more

The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.

One of the following:

"validating\_files"

"queued"

"running"

"succeeded"

"failed"

"cancelled"

trained\_tokens: number

The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.

training\_file: string

The file ID used for training. You can retrieve the training data with the [Files API](/docs/api-reference/files/retrieve-contents).

validation\_file: string

The file ID used for validation. You can retrieve the validation results with the [Files API](/docs/api-reference/files/retrieve-contents).

estimated\_finish: optional number

The Unix timestamp (in seconds) for when the fine-tuning job is estimated to finish. The value will be null if the fine-tuning job is not running.

formatunixtime

integrations: optional array of [FineTuningJobWandbIntegrationObject](/api/reference/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration_object%20%3E%20(schema)) { type, wandb }

A list of integrations to enable for this fine-tuning job.

type: "wandb"

The type of the integration being enabled for the fine-tuning job

wandb: [FineTuningJobWandbIntegration](/api/reference/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration%20%3E%20(schema)) { project, entity, name, tags }

The settings for your integration with Weights and Biases. This payload specifies the project that
metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
to your run, and set a default entity (team, username, etc) to be associated with your run.

metadata: optional [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

method: optional object { type, dpo, reinforcement, supervised }

The method used for fine-tuning.

type: "supervised" or "dpo" or "reinforcement"

The type of method. Is either `supervised`, `dpo`, or `reinforcement`.

One of the following:

"supervised"

"dpo"

"reinforcement"

dpo: optional [DpoMethod](/api/reference/resources/fine_tuning#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_method%20%3E%20(schema)) { hyperparameters }

Configuration for the DPO fine-tuning method.

reinforcement: optional [ReinforcementMethod](/api/reference/resources/fine_tuning#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_method%20%3E%20(schema)) { grader, hyperparameters }

Configuration for the reinforcement fine-tuning method.

supervised: optional [SupervisedMethod](/api/reference/resources/fine_tuning#(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_method%20%3E%20(schema)) { hyperparameters }

Configuration for the supervised fine-tuning method.

FineTuningJobEvent object { id, created\_at, level, 4 more }

Fine-tuning job event object

id: string

The object identifier.

created\_at: number

The Unix timestamp (in seconds) for when the fine-tuning job was created.

formatunixtime

level: "info" or "warn" or "error"

The log level of the event.

One of the following:

"info"

"warn"

"error"

message: string

The message of the event.

object: "fine\_tuning.job.event"

The object type, which is always “fine\_tuning.job.event”.

data: optional unknown

The data associated with the event.

type: optional "message" or "metrics"

The type of event.

One of the following:

"message"

"metrics"

FineTuningJobWandbIntegration object { project, entity, name, tags }

The settings for your integration with Weights and Biases. This payload specifies the project that
metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
to your run, and set a default entity (team, username, etc) to be associated with your run.

project: string

The name of the project that the new run will be created under.

entity: optional string

The entity to use for the run. This allows you to set the team or username of the WandB user that you would
like associated with the run. If not set, the default entity for the registered WandB API key is used.

name: optional string

A display name to set for the run. If not set, we will use the Job ID as the name.

tags: optional array of string

A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
default tags are generated by OpenAI: “openai/finetune”, “openai/{base-model}”, “openai/{ftjob-abcdef}”.

FineTuningJobWandbIntegrationObject object { type, wandb }

type: "wandb"

The type of the integration being enabled for the fine-tuning job

wandb: [FineTuningJobWandbIntegration](/api/reference/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration%20%3E%20(schema)) { project, entity, name, tags }

The settings for your integration with Weights and Biases. This payload specifies the project that
metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
to your run, and set a default entity (team, username, etc) to be associated with your run.

#### JobsCheckpoints

Manage fine-tuning jobs to tailor a model to your specific training data.

##### [List fine-tuning checkpoints](/api/reference/resources/fine_tuning/subresources/jobs/subresources/checkpoints/methods/list)

GET/fine\_tuning/jobs/{fine\_tuning\_job\_id}/checkpoints

##### ModelsExpand Collapse

FineTuningJobCheckpoint object { id, created\_at, fine\_tuned\_model\_checkpoint, 4 more }

The `fine_tuning.job.checkpoint` object represents a model checkpoint for a fine-tuning job that is ready to use.

id: string

The checkpoint identifier, which can be referenced in the API endpoints.

created\_at: number

The Unix timestamp (in seconds) for when the checkpoint was created.

formatunixtime

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
