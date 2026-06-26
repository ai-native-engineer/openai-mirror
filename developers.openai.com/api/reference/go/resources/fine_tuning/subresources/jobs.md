<!-- source: https://developers.openai.com/api/reference/go/resources/fine_tuning/subresources/jobs/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Fine Tuning](/api/reference/go/resources/fine_tuning)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Jobs

Manage fine-tuning jobs to tailor a model to your specific training data.

##### [Create fine-tuning job](/api/reference/go/resources/fine_tuning/subresources/jobs/methods/create)

client.FineTuning.Jobs.New(ctx, body) (\*[FineTuningJob](/api/reference/go/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)), error)

POST/fine\_tuning/jobs

##### [List fine-tuning jobs](/api/reference/go/resources/fine_tuning/subresources/jobs/methods/list)

client.FineTuning.Jobs.List(ctx, query) (\*CursorPage[[FineTuningJob](/api/reference/go/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema))], error)

GET/fine\_tuning/jobs

##### [Retrieve fine-tuning job](/api/reference/go/resources/fine_tuning/subresources/jobs/methods/retrieve)

client.FineTuning.Jobs.Get(ctx, fineTuningJobID) (\*[FineTuningJob](/api/reference/go/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)), error)

GET/fine\_tuning/jobs/{fine\_tuning\_job\_id}

##### [List fine-tuning events](/api/reference/go/resources/fine_tuning/subresources/jobs/methods/list_events)

client.FineTuning.Jobs.ListEvents(ctx, fineTuningJobID, query) (\*CursorPage[[FineTuningJobEvent](/api/reference/go/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_event%20%3E%20(schema))], error)

GET/fine\_tuning/jobs/{fine\_tuning\_job\_id}/events

##### [Cancel fine-tuning](/api/reference/go/resources/fine_tuning/subresources/jobs/methods/cancel)

client.FineTuning.Jobs.Cancel(ctx, fineTuningJobID) (\*[FineTuningJob](/api/reference/go/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)), error)

POST/fine\_tuning/jobs/{fine\_tuning\_job\_id}/cancel

##### [Pause fine-tuning](/api/reference/go/resources/fine_tuning/subresources/jobs/methods/pause)

client.FineTuning.Jobs.Pause(ctx, fineTuningJobID) (\*[FineTuningJob](/api/reference/go/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)), error)

POST/fine\_tuning/jobs/{fine\_tuning\_job\_id}/pause

##### [Resume fine-tuning](/api/reference/go/resources/fine_tuning/subresources/jobs/methods/resume)

client.FineTuning.Jobs.Resume(ctx, fineTuningJobID) (\*[FineTuningJob](/api/reference/go/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)), error)

POST/fine\_tuning/jobs/{fine\_tuning\_job\_id}/resume

##### ModelsExpand Collapse

type FineTuningJob struct{…}

The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.

ID string

The object identifier, which can be referenced in the API endpoints.

CreatedAt int64

The Unix timestamp (in seconds) for when the fine-tuning job was created.

formatunixtime

Error FineTuningJobError

For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.

Code string

A machine-readable error code.

Message string

A human-readable error message.

Param string

The parameter that was invalid, usually `training_file` or `validation_file`. This field will be null if the failure was not parameter-specific.

FineTunedModel string

The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.

FinishedAt int64

The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.

formatunixtime

Hyperparameters FineTuningJobHyperparameters

The hyperparameters used for the fine-tuning job. This value will only be returned when running `supervised` jobs.

BatchSize FineTuningJobHyperparametersBatchSizeUnionOptional

Number of examples in each batch. A larger batch size means that model parameters
are updated less frequently, but with lower variance.

One of the following:

type Auto string

int64

LearningRateMultiplier FineTuningJobHyperparametersLearningRateMultiplierUnionOptional

Scaling factor for the learning rate. A smaller learning rate may be useful to avoid
overfitting.

One of the following:

type Auto string

float64

NEpochs FineTuningJobHyperparametersNEpochsUnionOptional

The number of epochs to train the model for. An epoch refers to one full cycle
through the training dataset.

One of the following:

type Auto string

int64

Model string

The base model that is being fine-tuned.

Object FineTuningJob

The object type, which is always “fine\_tuning.job”.

OrganizationID string

The organization that owns the fine-tuning job.

ResultFiles []string

The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

Seed int64

The seed used for the fine-tuning job.

Status FineTuningJobStatus

The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.

One of the following:

const FineTuningJobStatusValidatingFiles FineTuningJobStatus = "validating\_files"

const FineTuningJobStatusQueued FineTuningJobStatus = "queued"

const FineTuningJobStatusRunning FineTuningJobStatus = "running"

const FineTuningJobStatusSucceeded FineTuningJobStatus = "succeeded"

const FineTuningJobStatusFailed FineTuningJobStatus = "failed"

const FineTuningJobStatusCancelled FineTuningJobStatus = "cancelled"

TrainedTokens int64

The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.

TrainingFile string

The file ID used for training. You can retrieve the training data with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

ValidationFile string

The file ID used for validation. You can retrieve the validation results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

EstimatedFinish int64Optional

The Unix timestamp (in seconds) for when the fine-tuning job is estimated to finish. The value will be null if the fine-tuning job is not running.

formatunixtime

Integrations [][FineTuningJobWandbIntegrationObject](/api/reference/go/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration_object%20%3E%20(schema))Optional

A list of integrations to enable for this fine-tuning job.

Type Wandb

The type of the integration being enabled for the fine-tuning job

Wandb [FineTuningJobWandbIntegration](/api/reference/go/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration%20%3E%20(schema))

The settings for your integration with Weights and Biases. This payload specifies the project that
metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
to your run, and set a default entity (team, username, etc) to be associated with your run.

Metadata [Metadata](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))Optional

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

Method FineTuningJobMethodOptional

The method used for fine-tuning.

Type string

The type of method. Is either `supervised`, `dpo`, or `reinforcement`.

One of the following:

const FineTuningJobMethodTypeSupervised FineTuningJobMethodType = "supervised"

const FineTuningJobMethodTypeDpo FineTuningJobMethodType = "dpo"

const FineTuningJobMethodTypeReinforcement FineTuningJobMethodType = "reinforcement"

Dpo [DpoMethod](/api/reference/go/resources/fine_tuning#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_method%20%3E%20(schema))Optional

Configuration for the DPO fine-tuning method.

Reinforcement [ReinforcementMethod](/api/reference/go/resources/fine_tuning#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_method%20%3E%20(schema))Optional

Configuration for the reinforcement fine-tuning method.

Supervised [SupervisedMethod](/api/reference/go/resources/fine_tuning#(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_method%20%3E%20(schema))Optional

Configuration for the supervised fine-tuning method.

type FineTuningJobEvent struct{…}

Fine-tuning job event object

ID string

The object identifier.

CreatedAt int64

The Unix timestamp (in seconds) for when the fine-tuning job was created.

formatunixtime

Level FineTuningJobEventLevel

The log level of the event.

One of the following:

const FineTuningJobEventLevelInfo FineTuningJobEventLevel = "info"

const FineTuningJobEventLevelWarn FineTuningJobEventLevel = "warn"

const FineTuningJobEventLevelError FineTuningJobEventLevel = "error"

Message string

The message of the event.

Object FineTuningJobEvent

The object type, which is always “fine\_tuning.job.event”.

Data anyOptional

The data associated with the event.

Type FineTuningJobEventTypeOptional

The type of event.

One of the following:

const FineTuningJobEventTypeMessage FineTuningJobEventType = "message"

const FineTuningJobEventTypeMetrics FineTuningJobEventType = "metrics"

type FineTuningJobWandbIntegration struct{…}

The settings for your integration with Weights and Biases. This payload specifies the project that
metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
to your run, and set a default entity (team, username, etc) to be associated with your run.

Project string

The name of the project that the new run will be created under.

Entity stringOptional

The entity to use for the run. This allows you to set the team or username of the WandB user that you would
like associated with the run. If not set, the default entity for the registered WandB API key is used.

Name stringOptional

A display name to set for the run. If not set, we will use the Job ID as the name.

Tags []stringOptional

A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
default tags are generated by OpenAI: “openai/finetune”, “openai/{base-model}”, “openai/{ftjob-abcdef}”.

type FineTuningJobWandbIntegrationObject struct{…}

Type Wandb

The type of the integration being enabled for the fine-tuning job

Wandb [FineTuningJobWandbIntegration](/api/reference/go/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration%20%3E%20(schema))

The settings for your integration with Weights and Biases. This payload specifies the project that
metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
to your run, and set a default entity (team, username, etc) to be associated with your run.

#### JobsCheckpoints

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
