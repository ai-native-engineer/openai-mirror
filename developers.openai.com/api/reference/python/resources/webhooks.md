<!-- source: https://developers.openai.com/api/reference/python/resources/webhooks/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Webhooks

##### [Unwrap](/api/reference/python/resources/webhooks/methods/unwrap)

webhooks.unwrap()

Function

##### ModelsExpand Collapse

class BatchCancelledWebhookEvent: …

Sent when a batch API request has been cancelled.

id: str

The unique ID of the event.

created\_at: int

The Unix timestamp (in seconds) of when the batch API request was cancelled.

formatunixtime

data: Data

Event data payload.

id: str

The unique ID of the batch API request.

type: Literal["batch.cancelled"]

The type of the event. Always `batch.cancelled`.

object: Optional[Literal["event"]]

The object of the event. Always `event`.

class BatchCompletedWebhookEvent: …

Sent when a batch API request has been completed.

id: str

The unique ID of the event.

created\_at: int

The Unix timestamp (in seconds) of when the batch API request was completed.

formatunixtime

data: Data

Event data payload.

id: str

The unique ID of the batch API request.

type: Literal["batch.completed"]

The type of the event. Always `batch.completed`.

object: Optional[Literal["event"]]

The object of the event. Always `event`.

class BatchExpiredWebhookEvent: …

Sent when a batch API request has expired.

id: str

The unique ID of the event.

created\_at: int

The Unix timestamp (in seconds) of when the batch API request expired.

formatunixtime

data: Data

Event data payload.

id: str

The unique ID of the batch API request.

type: Literal["batch.expired"]

The type of the event. Always `batch.expired`.

object: Optional[Literal["event"]]

The object of the event. Always `event`.

class BatchFailedWebhookEvent: …

Sent when a batch API request has failed.

id: str

The unique ID of the event.

created\_at: int

The Unix timestamp (in seconds) of when the batch API request failed.

formatunixtime

data: Data

Event data payload.

id: str

The unique ID of the batch API request.

type: Literal["batch.failed"]

The type of the event. Always `batch.failed`.

object: Optional[Literal["event"]]

The object of the event. Always `event`.

class EvalRunCanceledWebhookEvent: …

Sent when an eval run has been canceled.

id: str

The unique ID of the event.

created\_at: int

The Unix timestamp (in seconds) of when the eval run was canceled.

formatunixtime

data: Data

Event data payload.

id: str

The unique ID of the eval run.

type: Literal["eval.run.canceled"]

The type of the event. Always `eval.run.canceled`.

object: Optional[Literal["event"]]

The object of the event. Always `event`.

class EvalRunFailedWebhookEvent: …

Sent when an eval run has failed.

id: str

The unique ID of the event.

created\_at: int

The Unix timestamp (in seconds) of when the eval run failed.

formatunixtime

data: Data

Event data payload.

id: str

The unique ID of the eval run.

type: Literal["eval.run.failed"]

The type of the event. Always `eval.run.failed`.

object: Optional[Literal["event"]]

The object of the event. Always `event`.

class EvalRunSucceededWebhookEvent: …

Sent when an eval run has succeeded.

id: str

The unique ID of the event.

created\_at: int

The Unix timestamp (in seconds) of when the eval run succeeded.

formatunixtime

data: Data

Event data payload.

id: str

The unique ID of the eval run.

type: Literal["eval.run.succeeded"]

The type of the event. Always `eval.run.succeeded`.

object: Optional[Literal["event"]]

The object of the event. Always `event`.

class FineTuningJobCancelledWebhookEvent: …

Sent when a fine-tuning job has been cancelled.

id: str

The unique ID of the event.

created\_at: int

The Unix timestamp (in seconds) of when the fine-tuning job was cancelled.

formatunixtime

data: Data

Event data payload.

id: str

The unique ID of the fine-tuning job.

type: Literal["fine\_tuning.job.cancelled"]

The type of the event. Always `fine_tuning.job.cancelled`.

object: Optional[Literal["event"]]

The object of the event. Always `event`.

class FineTuningJobFailedWebhookEvent: …

Sent when a fine-tuning job has failed.

id: str

The unique ID of the event.

created\_at: int

The Unix timestamp (in seconds) of when the fine-tuning job failed.

formatunixtime

data: Data

Event data payload.

id: str

The unique ID of the fine-tuning job.

type: Literal["fine\_tuning.job.failed"]

The type of the event. Always `fine_tuning.job.failed`.

object: Optional[Literal["event"]]

The object of the event. Always `event`.

class FineTuningJobSucceededWebhookEvent: …

Sent when a fine-tuning job has succeeded.

id: str

The unique ID of the event.

created\_at: int

The Unix timestamp (in seconds) of when the fine-tuning job succeeded.

formatunixtime

data: Data

Event data payload.

id: str

The unique ID of the fine-tuning job.

type: Literal["fine\_tuning.job.succeeded"]

The type of the event. Always `fine_tuning.job.succeeded`.

object: Optional[Literal["event"]]

The object of the event. Always `event`.

class RealtimeCallIncomingWebhookEvent: …

Sent when Realtime API Receives a incoming SIP call.

id: str

The unique ID of the event.

created\_at: int

The Unix timestamp (in seconds) of when the model response was completed.

formatunixtime

data: Data

Event data payload.

call\_id: str

The unique ID of this call.

sip\_headers: List[DataSipHeader]

Headers from the SIP Invite.

name: str

Name of the SIP Header.

value: str

Value of the SIP Header.

type: Literal["realtime.call.incoming"]

The type of the event. Always `realtime.call.incoming`.

object: Optional[Literal["event"]]

The object of the event. Always `event`.

class ResponseCancelledWebhookEvent: …

Sent when a background response has been cancelled.

id: str

The unique ID of the event.

created\_at: int

The Unix timestamp (in seconds) of when the model response was cancelled.

formatunixtime

data: Data

Event data payload.

id: str

The unique ID of the model response.

type: Literal["response.cancelled"]

The type of the event. Always `response.cancelled`.

object: Optional[Literal["event"]]

The object of the event. Always `event`.

class ResponseCompletedWebhookEvent: …

Sent when a background response has been completed.

id: str

The unique ID of the event.

created\_at: int

The Unix timestamp (in seconds) of when the model response was completed.

formatunixtime

data: Data

Event data payload.

id: str

The unique ID of the model response.

type: Literal["response.completed"]

The type of the event. Always `response.completed`.

object: Optional[Literal["event"]]

The object of the event. Always `event`.

class ResponseFailedWebhookEvent: …

Sent when a background response has failed.

id: str

The unique ID of the event.

created\_at: int

The Unix timestamp (in seconds) of when the model response failed.

formatunixtime

data: Data

Event data payload.

id: str

The unique ID of the model response.

type: Literal["response.failed"]

The type of the event. Always `response.failed`.

object: Optional[Literal["event"]]

The object of the event. Always `event`.

class ResponseIncompleteWebhookEvent: …

Sent when a background response has been interrupted.

id: str

The unique ID of the event.

created\_at: int

The Unix timestamp (in seconds) of when the model response was interrupted.

formatunixtime

data: Data

Event data payload.

id: str

The unique ID of the model response.

type: Literal["response.incomplete"]

The type of the event. Always `response.incomplete`.

object: Optional[Literal["event"]]

The object of the event. Always `event`.
