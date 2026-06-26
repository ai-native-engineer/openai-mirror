<!-- source: https://developers.openai.com/api/reference/ruby/resources/webhooks/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Webhooks

##### [Unwrap](/api/reference/ruby/resources/webhooks/methods/unwrap)

webhooks.unwrap() -> void

Function

##### ModelsExpand Collapse

class BatchCancelledWebhookEvent { id, created\_at, data, 2 more }

Sent when a batch API request has been cancelled.

id: String

The unique ID of the event.

created\_at: Integer

The Unix timestamp (in seconds) of when the batch API request was cancelled.

formatunixtime

data: Data{ id}

Event data payload.

id: String

The unique ID of the batch API request.

type: :"batch.cancelled"

The type of the event. Always `batch.cancelled`.

object: :event

The object of the event. Always `event`.

class BatchCompletedWebhookEvent { id, created\_at, data, 2 more }

Sent when a batch API request has been completed.

id: String

The unique ID of the event.

created\_at: Integer

The Unix timestamp (in seconds) of when the batch API request was completed.

formatunixtime

data: Data{ id}

Event data payload.

id: String

The unique ID of the batch API request.

type: :"batch.completed"

The type of the event. Always `batch.completed`.

object: :event

The object of the event. Always `event`.

class BatchExpiredWebhookEvent { id, created\_at, data, 2 more }

Sent when a batch API request has expired.

id: String

The unique ID of the event.

created\_at: Integer

The Unix timestamp (in seconds) of when the batch API request expired.

formatunixtime

data: Data{ id}

Event data payload.

id: String

The unique ID of the batch API request.

type: :"batch.expired"

The type of the event. Always `batch.expired`.

object: :event

The object of the event. Always `event`.

class BatchFailedWebhookEvent { id, created\_at, data, 2 more }

Sent when a batch API request has failed.

id: String

The unique ID of the event.

created\_at: Integer

The Unix timestamp (in seconds) of when the batch API request failed.

formatunixtime

data: Data{ id}

Event data payload.

id: String

The unique ID of the batch API request.

type: :"batch.failed"

The type of the event. Always `batch.failed`.

object: :event

The object of the event. Always `event`.

class EvalRunCanceledWebhookEvent { id, created\_at, data, 2 more }

Sent when an eval run has been canceled.

id: String

The unique ID of the event.

created\_at: Integer

The Unix timestamp (in seconds) of when the eval run was canceled.

formatunixtime

data: Data{ id}

Event data payload.

id: String

The unique ID of the eval run.

type: :"eval.run.canceled"

The type of the event. Always `eval.run.canceled`.

object: :event

The object of the event. Always `event`.

class EvalRunFailedWebhookEvent { id, created\_at, data, 2 more }

Sent when an eval run has failed.

id: String

The unique ID of the event.

created\_at: Integer

The Unix timestamp (in seconds) of when the eval run failed.

formatunixtime

data: Data{ id}

Event data payload.

id: String

The unique ID of the eval run.

type: :"eval.run.failed"

The type of the event. Always `eval.run.failed`.

object: :event

The object of the event. Always `event`.

class EvalRunSucceededWebhookEvent { id, created\_at, data, 2 more }

Sent when an eval run has succeeded.

id: String

The unique ID of the event.

created\_at: Integer

The Unix timestamp (in seconds) of when the eval run succeeded.

formatunixtime

data: Data{ id}

Event data payload.

id: String

The unique ID of the eval run.

type: :"eval.run.succeeded"

The type of the event. Always `eval.run.succeeded`.

object: :event

The object of the event. Always `event`.

class FineTuningJobCancelledWebhookEvent { id, created\_at, data, 2 more }

Sent when a fine-tuning job has been cancelled.

id: String

The unique ID of the event.

created\_at: Integer

The Unix timestamp (in seconds) of when the fine-tuning job was cancelled.

formatunixtime

data: Data{ id}

Event data payload.

id: String

The unique ID of the fine-tuning job.

type: :"fine\_tuning.job.cancelled"

The type of the event. Always `fine_tuning.job.cancelled`.

object: :event

The object of the event. Always `event`.

class FineTuningJobFailedWebhookEvent { id, created\_at, data, 2 more }

Sent when a fine-tuning job has failed.

id: String

The unique ID of the event.

created\_at: Integer

The Unix timestamp (in seconds) of when the fine-tuning job failed.

formatunixtime

data: Data{ id}

Event data payload.

id: String

The unique ID of the fine-tuning job.

type: :"fine\_tuning.job.failed"

The type of the event. Always `fine_tuning.job.failed`.

object: :event

The object of the event. Always `event`.

class FineTuningJobSucceededWebhookEvent { id, created\_at, data, 2 more }

Sent when a fine-tuning job has succeeded.

id: String

The unique ID of the event.

created\_at: Integer

The Unix timestamp (in seconds) of when the fine-tuning job succeeded.

formatunixtime

data: Data{ id}

Event data payload.

id: String

The unique ID of the fine-tuning job.

type: :"fine\_tuning.job.succeeded"

The type of the event. Always `fine_tuning.job.succeeded`.

object: :event

The object of the event. Always `event`.

class RealtimeCallIncomingWebhookEvent { id, created\_at, data, 2 more }

Sent when Realtime API Receives a incoming SIP call.

id: String

The unique ID of the event.

created\_at: Integer

The Unix timestamp (in seconds) of when the model response was completed.

formatunixtime

data: Data{ call\_id, sip\_headers}

Event data payload.

call\_id: String

The unique ID of this call.

sip\_headers: Array[SipHeader{ name, value}]

Headers from the SIP Invite.

name: String

Name of the SIP Header.

value: String

Value of the SIP Header.

type: :"realtime.call.incoming"

The type of the event. Always `realtime.call.incoming`.

object: :event

The object of the event. Always `event`.

class ResponseCancelledWebhookEvent { id, created\_at, data, 2 more }

Sent when a background response has been cancelled.

id: String

The unique ID of the event.

created\_at: Integer

The Unix timestamp (in seconds) of when the model response was cancelled.

formatunixtime

data: Data{ id}

Event data payload.

id: String

The unique ID of the model response.

type: :"response.cancelled"

The type of the event. Always `response.cancelled`.

object: :event

The object of the event. Always `event`.

class ResponseCompletedWebhookEvent { id, created\_at, data, 2 more }

Sent when a background response has been completed.

id: String

The unique ID of the event.

created\_at: Integer

The Unix timestamp (in seconds) of when the model response was completed.

formatunixtime

data: Data{ id}

Event data payload.

id: String

The unique ID of the model response.

type: :"response.completed"

The type of the event. Always `response.completed`.

object: :event

The object of the event. Always `event`.

class ResponseFailedWebhookEvent { id, created\_at, data, 2 more }

Sent when a background response has failed.

id: String

The unique ID of the event.

created\_at: Integer

The Unix timestamp (in seconds) of when the model response failed.

formatunixtime

data: Data{ id}

Event data payload.

id: String

The unique ID of the model response.

type: :"response.failed"

The type of the event. Always `response.failed`.

object: :event

The object of the event. Always `event`.

class ResponseIncompleteWebhookEvent { id, created\_at, data, 2 more }

Sent when a background response has been interrupted.

id: String

The unique ID of the event.

created\_at: Integer

The Unix timestamp (in seconds) of when the model response was interrupted.

formatunixtime

data: Data{ id}

Event data payload.

id: String

The unique ID of the model response.

type: :"response.incomplete"

The type of the event. Always `response.incomplete`.

object: :event

The object of the event. Always `event`.
