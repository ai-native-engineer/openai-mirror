<!-- source: https://developers.openai.com/api/reference/typescript/resources/webhooks/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Webhooks

##### [Unwrap](/api/reference/typescript/resources/webhooks/methods/unwrap)

client.webhooks.unwrap(RequestOptionsoptions?): void

Function

##### ModelsExpand Collapse

BatchCancelledWebhookEvent { id, created\_at, data, 2 more }

Sent when a batch API request has been cancelled.

id: string

The unique ID of the event.

created\_at: number

The Unix timestamp (in seconds) of when the batch API request was cancelled.

formatunixtime

data: Data { id }

Event data payload.

id: string

The unique ID of the batch API request.

type: "batch.cancelled"

The type of the event. Always `batch.cancelled`.

object?: "event"

The object of the event. Always `event`.

BatchCompletedWebhookEvent { id, created\_at, data, 2 more }

Sent when a batch API request has been completed.

id: string

The unique ID of the event.

created\_at: number

The Unix timestamp (in seconds) of when the batch API request was completed.

formatunixtime

data: Data { id }

Event data payload.

id: string

The unique ID of the batch API request.

type: "batch.completed"

The type of the event. Always `batch.completed`.

object?: "event"

The object of the event. Always `event`.

BatchExpiredWebhookEvent { id, created\_at, data, 2 more }

Sent when a batch API request has expired.

id: string

The unique ID of the event.

created\_at: number

The Unix timestamp (in seconds) of when the batch API request expired.

formatunixtime

data: Data { id }

Event data payload.

id: string

The unique ID of the batch API request.

type: "batch.expired"

The type of the event. Always `batch.expired`.

object?: "event"

The object of the event. Always `event`.

BatchFailedWebhookEvent { id, created\_at, data, 2 more }

Sent when a batch API request has failed.

id: string

The unique ID of the event.

created\_at: number

The Unix timestamp (in seconds) of when the batch API request failed.

formatunixtime

data: Data { id }

Event data payload.

id: string

The unique ID of the batch API request.

type: "batch.failed"

The type of the event. Always `batch.failed`.

object?: "event"

The object of the event. Always `event`.

EvalRunCanceledWebhookEvent { id, created\_at, data, 2 more }

Sent when an eval run has been canceled.

id: string

The unique ID of the event.

created\_at: number

The Unix timestamp (in seconds) of when the eval run was canceled.

formatunixtime

data: Data { id }

Event data payload.

id: string

The unique ID of the eval run.

type: "eval.run.canceled"

The type of the event. Always `eval.run.canceled`.

object?: "event"

The object of the event. Always `event`.

EvalRunFailedWebhookEvent { id, created\_at, data, 2 more }

Sent when an eval run has failed.

id: string

The unique ID of the event.

created\_at: number

The Unix timestamp (in seconds) of when the eval run failed.

formatunixtime

data: Data { id }

Event data payload.

id: string

The unique ID of the eval run.

type: "eval.run.failed"

The type of the event. Always `eval.run.failed`.

object?: "event"

The object of the event. Always `event`.

EvalRunSucceededWebhookEvent { id, created\_at, data, 2 more }

Sent when an eval run has succeeded.

id: string

The unique ID of the event.

created\_at: number

The Unix timestamp (in seconds) of when the eval run succeeded.

formatunixtime

data: Data { id }

Event data payload.

id: string

The unique ID of the eval run.

type: "eval.run.succeeded"

The type of the event. Always `eval.run.succeeded`.

object?: "event"

The object of the event. Always `event`.

FineTuningJobCancelledWebhookEvent { id, created\_at, data, 2 more }

Sent when a fine-tuning job has been cancelled.

id: string

The unique ID of the event.

created\_at: number

The Unix timestamp (in seconds) of when the fine-tuning job was cancelled.

formatunixtime

data: Data { id }

Event data payload.

id: string

The unique ID of the fine-tuning job.

type: "fine\_tuning.job.cancelled"

The type of the event. Always `fine_tuning.job.cancelled`.

object?: "event"

The object of the event. Always `event`.

FineTuningJobFailedWebhookEvent { id, created\_at, data, 2 more }

Sent when a fine-tuning job has failed.

id: string

The unique ID of the event.

created\_at: number

The Unix timestamp (in seconds) of when the fine-tuning job failed.

formatunixtime

data: Data { id }

Event data payload.

id: string

The unique ID of the fine-tuning job.

type: "fine\_tuning.job.failed"

The type of the event. Always `fine_tuning.job.failed`.

object?: "event"

The object of the event. Always `event`.

FineTuningJobSucceededWebhookEvent { id, created\_at, data, 2 more }

Sent when a fine-tuning job has succeeded.

id: string

The unique ID of the event.

created\_at: number

The Unix timestamp (in seconds) of when the fine-tuning job succeeded.

formatunixtime

data: Data { id }

Event data payload.

id: string

The unique ID of the fine-tuning job.

type: "fine\_tuning.job.succeeded"

The type of the event. Always `fine_tuning.job.succeeded`.

object?: "event"

The object of the event. Always `event`.

RealtimeCallIncomingWebhookEvent { id, created\_at, data, 2 more }

Sent when Realtime API Receives a incoming SIP call.

id: string

The unique ID of the event.

created\_at: number

The Unix timestamp (in seconds) of when the model response was completed.

formatunixtime

data: Data { call\_id, sip\_headers }

Event data payload.

call\_id: string

The unique ID of this call.

sip\_headers: Array<SipHeader>

Headers from the SIP Invite.

name: string

Name of the SIP Header.

value: string

Value of the SIP Header.

type: "realtime.call.incoming"

The type of the event. Always `realtime.call.incoming`.

object?: "event"

The object of the event. Always `event`.

ResponseCancelledWebhookEvent { id, created\_at, data, 2 more }

Sent when a background response has been cancelled.

id: string

The unique ID of the event.

created\_at: number

The Unix timestamp (in seconds) of when the model response was cancelled.

formatunixtime

data: Data { id }

Event data payload.

id: string

The unique ID of the model response.

type: "response.cancelled"

The type of the event. Always `response.cancelled`.

object?: "event"

The object of the event. Always `event`.

ResponseCompletedWebhookEvent { id, created\_at, data, 2 more }

Sent when a background response has been completed.

id: string

The unique ID of the event.

created\_at: number

The Unix timestamp (in seconds) of when the model response was completed.

formatunixtime

data: Data { id }

Event data payload.

id: string

The unique ID of the model response.

type: "response.completed"

The type of the event. Always `response.completed`.

object?: "event"

The object of the event. Always `event`.

ResponseFailedWebhookEvent { id, created\_at, data, 2 more }

Sent when a background response has failed.

id: string

The unique ID of the event.

created\_at: number

The Unix timestamp (in seconds) of when the model response failed.

formatunixtime

data: Data { id }

Event data payload.

id: string

The unique ID of the model response.

type: "response.failed"

The type of the event. Always `response.failed`.

object?: "event"

The object of the event. Always `event`.

ResponseIncompleteWebhookEvent { id, created\_at, data, 2 more }

Sent when a background response has been interrupted.

id: string

The unique ID of the event.

created\_at: number

The Unix timestamp (in seconds) of when the model response was interrupted.

formatunixtime

data: Data { id }

Event data payload.

id: string

The unique ID of the model response.

type: "response.incomplete"

The type of the event. Always `response.incomplete`.

object?: "event"

The object of the event. Always `event`.
