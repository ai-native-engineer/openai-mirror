<!-- source: https://developers.openai.com/api/reference/java/resources/fine_tuning/subresources/jobs/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Fine Tuning](/api/reference/java/resources/fine_tuning)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Jobs

Manage fine-tuning jobs to tailor a model to your specific training data.

##### [Create fine-tuning job](/api/reference/java/resources/fine_tuning/subresources/jobs/methods/create)

[FineTuningJob](/api/reference/java/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)) fineTuning().jobs().create(JobCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/fine\_tuning/jobs

##### [List fine-tuning jobs](/api/reference/java/resources/fine_tuning/subresources/jobs/methods/list)

JobListPage fineTuning().jobs().list(JobListParamsparams = JobListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/fine\_tuning/jobs

##### [Retrieve fine-tuning job](/api/reference/java/resources/fine_tuning/subresources/jobs/methods/retrieve)

[FineTuningJob](/api/reference/java/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)) fineTuning().jobs().retrieve(JobRetrieveParamsparams = JobRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/fine\_tuning/jobs/{fine\_tuning\_job\_id}

##### [List fine-tuning events](/api/reference/java/resources/fine_tuning/subresources/jobs/methods/list_events)

JobListEventsPage fineTuning().jobs().listEvents(JobListEventsParamsparams = JobListEventsParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/fine\_tuning/jobs/{fine\_tuning\_job\_id}/events

##### [Cancel fine-tuning](/api/reference/java/resources/fine_tuning/subresources/jobs/methods/cancel)

[FineTuningJob](/api/reference/java/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)) fineTuning().jobs().cancel(JobCancelParamsparams = JobCancelParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/fine\_tuning/jobs/{fine\_tuning\_job\_id}/cancel

##### [Pause fine-tuning](/api/reference/java/resources/fine_tuning/subresources/jobs/methods/pause)

[FineTuningJob](/api/reference/java/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)) fineTuning().jobs().pause(JobPauseParamsparams = JobPauseParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/fine\_tuning/jobs/{fine\_tuning\_job\_id}/pause

##### [Resume fine-tuning](/api/reference/java/resources/fine_tuning/subresources/jobs/methods/resume)

[FineTuningJob](/api/reference/java/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job%20%3E%20(schema)) fineTuning().jobs().resume(JobResumeParamsparams = JobResumeParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/fine\_tuning/jobs/{fine\_tuning\_job\_id}/resume

##### ModelsExpand Collapse

class FineTuningJob:

The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.

String id

The object identifier, which can be referenced in the API endpoints.

long createdAt

The Unix timestamp (in seconds) for when the fine-tuning job was created.

formatunixtime

Optional<Error> error

For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.

String code

A machine-readable error code.

String message

A human-readable error message.

Optional<String> param

The parameter that was invalid, usually `training_file` or `validation_file`. This field will be null if the failure was not parameter-specific.

Optional<String> fineTunedModel

The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.

Optional<Long> finishedAt

The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.

formatunixtime

Hyperparameters hyperparameters

The hyperparameters used for the fine-tuning job. This value will only be returned when running `supervised` jobs.

Optional<BatchSize> batchSize

Number of examples in each batch. A larger batch size means that model parameters
are updated less frequently, but with lower variance.

One of the following:

JsonValue;

long

Optional<LearningRateMultiplier> learningRateMultiplier

Scaling factor for the learning rate. A smaller learning rate may be useful to avoid
overfitting.

One of the following:

JsonValue;

double

Optional<NEpochs> nEpochs

The number of epochs to train the model for. An epoch refers to one full cycle
through the training dataset.

One of the following:

JsonValue;

long

String model

The base model that is being fine-tuned.

JsonValue; object\_ "fine\_tuning.job"constant"fine\_tuning.job"constant

The object type, which is always “fine\_tuning.job”.

String organizationId

The organization that owns the fine-tuning job.

List<String> resultFiles

The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

long seed

The seed used for the fine-tuning job.

Status status

The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.

One of the following:

VALIDATING\_FILES("validating\_files")

QUEUED("queued")

RUNNING("running")

SUCCEEDED("succeeded")

FAILED("failed")

CANCELLED("cancelled")

Optional<Long> trainedTokens

The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.

String trainingFile

The file ID used for training. You can retrieve the training data with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

Optional<String> validationFile

The file ID used for validation. You can retrieve the validation results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

Optional<Long> estimatedFinish

The Unix timestamp (in seconds) for when the fine-tuning job is estimated to finish. The value will be null if the fine-tuning job is not running.

formatunixtime

Optional<List<[FineTuningJobWandbIntegrationObject](/api/reference/java/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration_object%20%3E%20(schema))>> integrations

A list of integrations to enable for this fine-tuning job.

JsonValue; type "wandb"constant"wandb"constant

The type of the integration being enabled for the fine-tuning job

[FineTuningJobWandbIntegration](/api/reference/java/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration%20%3E%20(schema)) wandb

The settings for your integration with Weights and Biases. This payload specifies the project that
metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
to your run, and set a default entity (team, username, etc) to be associated with your run.

Optional<Metadata> metadata

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

Optional<Method> method

The method used for fine-tuning.

Type type

The type of method. Is either `supervised`, `dpo`, or `reinforcement`.

One of the following:

SUPERVISED("supervised")

DPO("dpo")

REINFORCEMENT("reinforcement")

Optional<[DpoMethod](/api/reference/java/resources/fine_tuning#(resource)%20fine_tuning.methods%20%3E%20(model)%20dpo_method%20%3E%20(schema))> dpo

Configuration for the DPO fine-tuning method.

Optional<[ReinforcementMethod](/api/reference/java/resources/fine_tuning#(resource)%20fine_tuning.methods%20%3E%20(model)%20reinforcement_method%20%3E%20(schema))> reinforcement

Configuration for the reinforcement fine-tuning method.

Optional<[SupervisedMethod](/api/reference/java/resources/fine_tuning#(resource)%20fine_tuning.methods%20%3E%20(model)%20supervised_method%20%3E%20(schema))> supervised

Configuration for the supervised fine-tuning method.

class FineTuningJobEvent:

Fine-tuning job event object

String id

The object identifier.

long createdAt

The Unix timestamp (in seconds) for when the fine-tuning job was created.

formatunixtime

Level level

The log level of the event.

One of the following:

INFO("info")

WARN("warn")

ERROR("error")

String message

The message of the event.

JsonValue; object\_ "fine\_tuning.job.event"constant"fine\_tuning.job.event"constant

The object type, which is always “fine\_tuning.job.event”.

Optional<JsonValue> data

The data associated with the event.

Optional<Type> type

The type of event.

One of the following:

MESSAGE("message")

METRICS("metrics")

class FineTuningJobWandbIntegration:

The settings for your integration with Weights and Biases. This payload specifies the project that
metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
to your run, and set a default entity (team, username, etc) to be associated with your run.

String project

The name of the project that the new run will be created under.

Optional<String> entity

The entity to use for the run. This allows you to set the team or username of the WandB user that you would
like associated with the run. If not set, the default entity for the registered WandB API key is used.

Optional<String> name

A display name to set for the run. If not set, we will use the Job ID as the name.

Optional<List<String>> tags

A list of tags to be attached to the newly created run. These tags are passed through directly to WandB. Some
default tags are generated by OpenAI: “openai/finetune”, “openai/{base-model}”, “openai/{ftjob-abcdef}”.

class FineTuningJobWandbIntegrationObject:

JsonValue; type "wandb"constant"wandb"constant

The type of the integration being enabled for the fine-tuning job

[FineTuningJobWandbIntegration](/api/reference/java/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_wandb_integration%20%3E%20(schema)) wandb

The settings for your integration with Weights and Biases. This payload specifies the project that
metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags
to your run, and set a default entity (team, username, etc) to be associated with your run.

#### JobsCheckpoints

Manage fine-tuning jobs to tailor a model to your specific training data.

##### [List fine-tuning checkpoints](/api/reference/java/resources/fine_tuning/subresources/jobs/subresources/checkpoints/methods/list)

CheckpointListPage fineTuning().jobs().checkpoints().list(CheckpointListParamsparams = CheckpointListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/fine\_tuning/jobs/{fine\_tuning\_job\_id}/checkpoints

##### ModelsExpand Collapse

class FineTuningJobCheckpoint:

The `fine_tuning.job.checkpoint` object represents a model checkpoint for a fine-tuning job that is ready to use.

String id

The checkpoint identifier, which can be referenced in the API endpoints.

long createdAt

The Unix timestamp (in seconds) for when the checkpoint was created.

formatunixtime

String fineTunedModelCheckpoint

The name of the fine-tuned checkpoint model that is created.

String fineTuningJobId

The name of the fine-tuning job that this checkpoint was created from.

Metrics metrics

Metrics at the step number during the fine-tuning job.

Optional<Double> fullValidLoss

Optional<Double> fullValidMeanTokenAccuracy

Optional<Double> step

Optional<Double> trainLoss

Optional<Double> trainMeanTokenAccuracy

Optional<Double> validLoss

Optional<Double> validMeanTokenAccuracy

JsonValue; object\_ "fine\_tuning.job.checkpoint"constant"fine\_tuning.job.checkpoint"constant

The object type, which is always “fine\_tuning.job.checkpoint”.

long stepNumber

The step number that the checkpoint was created at.
