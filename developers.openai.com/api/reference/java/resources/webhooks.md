<!-- source: https://developers.openai.com/api/reference/java/resources/webhooks/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Webhooks

##### ModelsExpand Collapse

class BatchCancelledWebhookEvent:

Sent when a batch API request has been cancelled.

String id

The unique ID of the event.

long createdAt

The Unix timestamp (in seconds) of when the batch API request was cancelled.

formatunixtime

Data data

Event data payload.

String id

The unique ID of the batch API request.

JsonValue; type "batch.cancelled"constant"batch.cancelled"constant

The type of the event. Always `batch.cancelled`.

Optional<Object> object\_

The object of the event. Always `event`.

class BatchCompletedWebhookEvent:

Sent when a batch API request has been completed.

String id

The unique ID of the event.

long createdAt

The Unix timestamp (in seconds) of when the batch API request was completed.

formatunixtime

Data data

Event data payload.

String id

The unique ID of the batch API request.

JsonValue; type "batch.completed"constant"batch.completed"constant

The type of the event. Always `batch.completed`.

Optional<Object> object\_

The object of the event. Always `event`.

class BatchExpiredWebhookEvent:

Sent when a batch API request has expired.

String id

The unique ID of the event.

long createdAt

The Unix timestamp (in seconds) of when the batch API request expired.

formatunixtime

Data data

Event data payload.

String id

The unique ID of the batch API request.

JsonValue; type "batch.expired"constant"batch.expired"constant

The type of the event. Always `batch.expired`.

Optional<Object> object\_

The object of the event. Always `event`.

class BatchFailedWebhookEvent:

Sent when a batch API request has failed.

String id

The unique ID of the event.

long createdAt

The Unix timestamp (in seconds) of when the batch API request failed.

formatunixtime

Data data

Event data payload.

String id

The unique ID of the batch API request.

JsonValue; type "batch.failed"constant"batch.failed"constant

The type of the event. Always `batch.failed`.

Optional<Object> object\_

The object of the event. Always `event`.

class EvalRunCanceledWebhookEvent:

Sent when an eval run has been canceled.

String id

The unique ID of the event.

long createdAt

The Unix timestamp (in seconds) of when the eval run was canceled.

formatunixtime

Data data

Event data payload.

String id

The unique ID of the eval run.

JsonValue; type "eval.run.canceled"constant"eval.run.canceled"constant

The type of the event. Always `eval.run.canceled`.

Optional<Object> object\_

The object of the event. Always `event`.

class EvalRunFailedWebhookEvent:

Sent when an eval run has failed.

String id

The unique ID of the event.

long createdAt

The Unix timestamp (in seconds) of when the eval run failed.

formatunixtime

Data data

Event data payload.

String id

The unique ID of the eval run.

JsonValue; type "eval.run.failed"constant"eval.run.failed"constant

The type of the event. Always `eval.run.failed`.

Optional<Object> object\_

The object of the event. Always `event`.

class EvalRunSucceededWebhookEvent:

Sent when an eval run has succeeded.

String id

The unique ID of the event.

long createdAt

The Unix timestamp (in seconds) of when the eval run succeeded.

formatunixtime

Data data

Event data payload.

String id

The unique ID of the eval run.

JsonValue; type "eval.run.succeeded"constant"eval.run.succeeded"constant

The type of the event. Always `eval.run.succeeded`.

Optional<Object> object\_

The object of the event. Always `event`.

class FineTuningJobCancelledWebhookEvent:

Sent when a fine-tuning job has been cancelled.

String id

The unique ID of the event.

long createdAt

The Unix timestamp (in seconds) of when the fine-tuning job was cancelled.

formatunixtime

Data data

Event data payload.

String id

The unique ID of the fine-tuning job.

JsonValue; type "fine\_tuning.job.cancelled"constant"fine\_tuning.job.cancelled"constant

The type of the event. Always `fine_tuning.job.cancelled`.

Optional<Object> object\_

The object of the event. Always `event`.

class FineTuningJobFailedWebhookEvent:

Sent when a fine-tuning job has failed.

String id

The unique ID of the event.

long createdAt

The Unix timestamp (in seconds) of when the fine-tuning job failed.

formatunixtime

Data data

Event data payload.

String id

The unique ID of the fine-tuning job.

JsonValue; type "fine\_tuning.job.failed"constant"fine\_tuning.job.failed"constant

The type of the event. Always `fine_tuning.job.failed`.

Optional<Object> object\_

The object of the event. Always `event`.

class FineTuningJobSucceededWebhookEvent:

Sent when a fine-tuning job has succeeded.

String id

The unique ID of the event.

long createdAt

The Unix timestamp (in seconds) of when the fine-tuning job succeeded.

formatunixtime

Data data

Event data payload.

String id

The unique ID of the fine-tuning job.

JsonValue; type "fine\_tuning.job.succeeded"constant"fine\_tuning.job.succeeded"constant

The type of the event. Always `fine_tuning.job.succeeded`.

Optional<Object> object\_

The object of the event. Always `event`.

class RealtimeCallIncomingWebhookEvent:

Sent when Realtime API Receives a incoming SIP call.

String id

The unique ID of the event.

long createdAt

The Unix timestamp (in seconds) of when the model response was completed.

formatunixtime

Data data

Event data payload.

String callId

The unique ID of this call.

List<SipHeader> sipHeaders

Headers from the SIP Invite.

String name

Name of the SIP Header.

String value

Value of the SIP Header.

JsonValue; type "realtime.call.incoming"constant"realtime.call.incoming"constant

The type of the event. Always `realtime.call.incoming`.

Optional<Object> object\_

The object of the event. Always `event`.

class ResponseCancelledWebhookEvent:

Sent when a background response has been cancelled.

String id

The unique ID of the event.

long createdAt

The Unix timestamp (in seconds) of when the model response was cancelled.

formatunixtime

Data data

Event data payload.

String id

The unique ID of the model response.

JsonValue; type "response.cancelled"constant"response.cancelled"constant

The type of the event. Always `response.cancelled`.

Optional<Object> object\_

The object of the event. Always `event`.

class ResponseCompletedWebhookEvent:

Sent when a background response has been completed.

String id

The unique ID of the event.

long createdAt

The Unix timestamp (in seconds) of when the model response was completed.

formatunixtime

Data data

Event data payload.

String id

The unique ID of the model response.

JsonValue; type "response.completed"constant"response.completed"constant

The type of the event. Always `response.completed`.

Optional<Object> object\_

The object of the event. Always `event`.

class ResponseFailedWebhookEvent:

Sent when a background response has failed.

String id

The unique ID of the event.

long createdAt

The Unix timestamp (in seconds) of when the model response failed.

formatunixtime

Data data

Event data payload.

String id

The unique ID of the model response.

JsonValue; type "response.failed"constant"response.failed"constant

The type of the event. Always `response.failed`.

Optional<Object> object\_

The object of the event. Always `event`.

class ResponseIncompleteWebhookEvent:

Sent when a background response has been interrupted.

String id

The unique ID of the event.

long createdAt

The Unix timestamp (in seconds) of when the model response was interrupted.

formatunixtime

Data data

Event data payload.

String id

The unique ID of the model response.

JsonValue; type "response.incomplete"constant"response.incomplete"constant

The type of the event. Always `response.incomplete`.

Optional<Object> object\_

The object of the event. Always `event`.
