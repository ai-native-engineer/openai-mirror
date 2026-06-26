<!-- source: https://developers.openai.com/api/reference/go/resources/webhooks/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Webhooks

##### [Unwrap](/api/reference/go/resources/webhooks/methods/unwrap)

client.Webhooks.Unwrap(ctx) error

Function

##### ModelsExpand Collapse

type BatchCancelledWebhookEvent struct{…}

Sent when a batch API request has been cancelled.

ID string

The unique ID of the event.

CreatedAt int64

The Unix timestamp (in seconds) of when the batch API request was cancelled.

formatunixtime

Data BatchCancelledWebhookEventData

Event data payload.

ID string

The unique ID of the batch API request.

Type BatchCancelled

The type of the event. Always `batch.cancelled`.

Object BatchCancelledWebhookEventObjectOptional

The object of the event. Always `event`.

type BatchCompletedWebhookEvent struct{…}

Sent when a batch API request has been completed.

ID string

The unique ID of the event.

CreatedAt int64

The Unix timestamp (in seconds) of when the batch API request was completed.

formatunixtime

Data BatchCompletedWebhookEventData

Event data payload.

ID string

The unique ID of the batch API request.

Type BatchCompleted

The type of the event. Always `batch.completed`.

Object BatchCompletedWebhookEventObjectOptional

The object of the event. Always `event`.

type BatchExpiredWebhookEvent struct{…}

Sent when a batch API request has expired.

ID string

The unique ID of the event.

CreatedAt int64

The Unix timestamp (in seconds) of when the batch API request expired.

formatunixtime

Data BatchExpiredWebhookEventData

Event data payload.

ID string

The unique ID of the batch API request.

Type BatchExpired

The type of the event. Always `batch.expired`.

Object BatchExpiredWebhookEventObjectOptional

The object of the event. Always `event`.

type BatchFailedWebhookEvent struct{…}

Sent when a batch API request has failed.

ID string

The unique ID of the event.

CreatedAt int64

The Unix timestamp (in seconds) of when the batch API request failed.

formatunixtime

Data BatchFailedWebhookEventData

Event data payload.

ID string

The unique ID of the batch API request.

Type BatchFailed

The type of the event. Always `batch.failed`.

Object BatchFailedWebhookEventObjectOptional

The object of the event. Always `event`.

type EvalRunCanceledWebhookEvent struct{…}

Sent when an eval run has been canceled.

ID string

The unique ID of the event.

CreatedAt int64

The Unix timestamp (in seconds) of when the eval run was canceled.

formatunixtime

Data EvalRunCanceledWebhookEventData

Event data payload.

ID string

The unique ID of the eval run.

Type EvalRunCanceled

The type of the event. Always `eval.run.canceled`.

Object EvalRunCanceledWebhookEventObjectOptional

The object of the event. Always `event`.

type EvalRunFailedWebhookEvent struct{…}

Sent when an eval run has failed.

ID string

The unique ID of the event.

CreatedAt int64

The Unix timestamp (in seconds) of when the eval run failed.

formatunixtime

Data EvalRunFailedWebhookEventData

Event data payload.

ID string

The unique ID of the eval run.

Type EvalRunFailed

The type of the event. Always `eval.run.failed`.

Object EvalRunFailedWebhookEventObjectOptional

The object of the event. Always `event`.

type EvalRunSucceededWebhookEvent struct{…}

Sent when an eval run has succeeded.

ID string

The unique ID of the event.

CreatedAt int64

The Unix timestamp (in seconds) of when the eval run succeeded.

formatunixtime

Data EvalRunSucceededWebhookEventData

Event data payload.

ID string

The unique ID of the eval run.

Type EvalRunSucceeded

The type of the event. Always `eval.run.succeeded`.

Object EvalRunSucceededWebhookEventObjectOptional

The object of the event. Always `event`.

type FineTuningJobCancelledWebhookEvent struct{…}

Sent when a fine-tuning job has been cancelled.

ID string

The unique ID of the event.

CreatedAt int64

The Unix timestamp (in seconds) of when the fine-tuning job was cancelled.

formatunixtime

Data FineTuningJobCancelledWebhookEventData

Event data payload.

ID string

The unique ID of the fine-tuning job.

Type FineTuningJobCancelled

The type of the event. Always `fine_tuning.job.cancelled`.

Object FineTuningJobCancelledWebhookEventObjectOptional

The object of the event. Always `event`.

type FineTuningJobFailedWebhookEvent struct{…}

Sent when a fine-tuning job has failed.

ID string

The unique ID of the event.

CreatedAt int64

The Unix timestamp (in seconds) of when the fine-tuning job failed.

formatunixtime

Data FineTuningJobFailedWebhookEventData

Event data payload.

ID string

The unique ID of the fine-tuning job.

Type FineTuningJobFailed

The type of the event. Always `fine_tuning.job.failed`.

Object FineTuningJobFailedWebhookEventObjectOptional

The object of the event. Always `event`.

type FineTuningJobSucceededWebhookEvent struct{…}

Sent when a fine-tuning job has succeeded.

ID string

The unique ID of the event.

CreatedAt int64

The Unix timestamp (in seconds) of when the fine-tuning job succeeded.

formatunixtime

Data FineTuningJobSucceededWebhookEventData

Event data payload.

ID string

The unique ID of the fine-tuning job.

Type FineTuningJobSucceeded

The type of the event. Always `fine_tuning.job.succeeded`.

Object FineTuningJobSucceededWebhookEventObjectOptional

The object of the event. Always `event`.

type RealtimeCallIncomingWebhookEvent struct{…}

Sent when Realtime API Receives a incoming SIP call.

ID string

The unique ID of the event.

CreatedAt int64

The Unix timestamp (in seconds) of when the model response was completed.

formatunixtime

Data RealtimeCallIncomingWebhookEventData

Event data payload.

CallID string

The unique ID of this call.

SipHeaders []RealtimeCallIncomingWebhookEventDataSipHeader

Headers from the SIP Invite.

Name string

Name of the SIP Header.

Value string

Value of the SIP Header.

Type RealtimeCallIncoming

The type of the event. Always `realtime.call.incoming`.

Object RealtimeCallIncomingWebhookEventObjectOptional

The object of the event. Always `event`.

type ResponseCancelledWebhookEvent struct{…}

Sent when a background response has been cancelled.

ID string

The unique ID of the event.

CreatedAt int64

The Unix timestamp (in seconds) of when the model response was cancelled.

formatunixtime

Data ResponseCancelledWebhookEventData

Event data payload.

ID string

The unique ID of the model response.

Type ResponseCancelled

The type of the event. Always `response.cancelled`.

Object ResponseCancelledWebhookEventObjectOptional

The object of the event. Always `event`.

type ResponseCompletedWebhookEvent struct{…}

Sent when a background response has been completed.

ID string

The unique ID of the event.

CreatedAt int64

The Unix timestamp (in seconds) of when the model response was completed.

formatunixtime

Data ResponseCompletedWebhookEventData

Event data payload.

ID string

The unique ID of the model response.

Type ResponseCompleted

The type of the event. Always `response.completed`.

Object ResponseCompletedWebhookEventObjectOptional

The object of the event. Always `event`.

type ResponseFailedWebhookEvent struct{…}

Sent when a background response has failed.

ID string

The unique ID of the event.

CreatedAt int64

The Unix timestamp (in seconds) of when the model response failed.

formatunixtime

Data ResponseFailedWebhookEventData

Event data payload.

ID string

The unique ID of the model response.

Type ResponseFailed

The type of the event. Always `response.failed`.

Object ResponseFailedWebhookEventObjectOptional

The object of the event. Always `event`.

type ResponseIncompleteWebhookEvent struct{…}

Sent when a background response has been interrupted.

ID string

The unique ID of the event.

CreatedAt int64

The Unix timestamp (in seconds) of when the model response was interrupted.

formatunixtime

Data ResponseIncompleteWebhookEventData

Event data payload.

ID string

The unique ID of the model response.

Type ResponseIncomplete

The type of the event. Always `response.incomplete`.

Object ResponseIncompleteWebhookEventObjectOptional

The object of the event. Always `event`.
