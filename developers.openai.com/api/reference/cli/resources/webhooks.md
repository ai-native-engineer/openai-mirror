<!-- source: https://developers.openai.com/api/reference/cli/resources/webhooks/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Webhooks

##### ModelsExpand Collapse

batch\_cancelled\_webhook\_event: object { id, created\_at, data, 2 more }

Sent when a batch API request has been cancelled.

id: string

The unique ID of the event.

created\_at: number

The Unix timestamp (in seconds) of when the batch API request was cancelled.

data: object { id }

Event data payload.

id: string

The unique ID of the batch API request.

type: "batch.cancelled"

The type of the event. Always `batch.cancelled`.

object: optional "event"

The object of the event. Always `event`.

"event"

batch\_completed\_webhook\_event: object { id, created\_at, data, 2 more }

Sent when a batch API request has been completed.

id: string

The unique ID of the event.

created\_at: number

The Unix timestamp (in seconds) of when the batch API request was completed.

data: object { id }

Event data payload.

id: string

The unique ID of the batch API request.

type: "batch.completed"

The type of the event. Always `batch.completed`.

object: optional "event"

The object of the event. Always `event`.

"event"

batch\_expired\_webhook\_event: object { id, created\_at, data, 2 more }

Sent when a batch API request has expired.

id: string

The unique ID of the event.

created\_at: number

The Unix timestamp (in seconds) of when the batch API request expired.

data: object { id }

Event data payload.

id: string

The unique ID of the batch API request.

type: "batch.expired"

The type of the event. Always `batch.expired`.

object: optional "event"

The object of the event. Always `event`.

"event"

batch\_failed\_webhook\_event: object { id, created\_at, data, 2 more }

Sent when a batch API request has failed.

id: string

The unique ID of the event.

created\_at: number

The Unix timestamp (in seconds) of when the batch API request failed.

data: object { id }

Event data payload.

id: string

The unique ID of the batch API request.

type: "batch.failed"

The type of the event. Always `batch.failed`.

object: optional "event"

The object of the event. Always `event`.

"event"

eval\_run\_canceled\_webhook\_event: object { id, created\_at, data, 2 more }

Sent when an eval run has been canceled.

id: string

The unique ID of the event.

created\_at: number

The Unix timestamp (in seconds) of when the eval run was canceled.

data: object { id }

Event data payload.

id: string

The unique ID of the eval run.

type: "eval.run.canceled"

The type of the event. Always `eval.run.canceled`.

object: optional "event"

The object of the event. Always `event`.

"event"

eval\_run\_failed\_webhook\_event: object { id, created\_at, data, 2 more }

Sent when an eval run has failed.

id: string

The unique ID of the event.

created\_at: number

The Unix timestamp (in seconds) of when the eval run failed.

data: object { id }

Event data payload.

id: string

The unique ID of the eval run.

type: "eval.run.failed"

The type of the event. Always `eval.run.failed`.

object: optional "event"

The object of the event. Always `event`.

"event"

eval\_run\_succeeded\_webhook\_event: object { id, created\_at, data, 2 more }

Sent when an eval run has succeeded.

id: string

The unique ID of the event.

created\_at: number

The Unix timestamp (in seconds) of when the eval run succeeded.

data: object { id }

Event data payload.

id: string

The unique ID of the eval run.

type: "eval.run.succeeded"

The type of the event. Always `eval.run.succeeded`.

object: optional "event"

The object of the event. Always `event`.

"event"

fine\_tuning\_job\_cancelled\_webhook\_event: object { id, created\_at, data, 2 more }

Sent when a fine-tuning job has been cancelled.

id: string

The unique ID of the event.

created\_at: number

The Unix timestamp (in seconds) of when the fine-tuning job was cancelled.

data: object { id }

Event data payload.

id: string

The unique ID of the fine-tuning job.

type: "fine\_tuning.job.cancelled"

The type of the event. Always `fine_tuning.job.cancelled`.

object: optional "event"

The object of the event. Always `event`.

"event"

fine\_tuning\_job\_failed\_webhook\_event: object { id, created\_at, data, 2 more }

Sent when a fine-tuning job has failed.

id: string

The unique ID of the event.

created\_at: number

The Unix timestamp (in seconds) of when the fine-tuning job failed.

data: object { id }

Event data payload.

id: string

The unique ID of the fine-tuning job.

type: "fine\_tuning.job.failed"

The type of the event. Always `fine_tuning.job.failed`.

object: optional "event"

The object of the event. Always `event`.

"event"

fine\_tuning\_job\_succeeded\_webhook\_event: object { id, created\_at, data, 2 more }

Sent when a fine-tuning job has succeeded.

id: string

The unique ID of the event.

created\_at: number

The Unix timestamp (in seconds) of when the fine-tuning job succeeded.

data: object { id }

Event data payload.

id: string

The unique ID of the fine-tuning job.

type: "fine\_tuning.job.succeeded"

The type of the event. Always `fine_tuning.job.succeeded`.

object: optional "event"

The object of the event. Always `event`.

"event"

realtime\_call\_incoming\_webhook\_event: object { id, created\_at, data, 2 more }

Sent when Realtime API Receives a incoming SIP call.

id: string

The unique ID of the event.

created\_at: number

The Unix timestamp (in seconds) of when the model response was completed.

data: object { call\_id, sip\_headers }

Event data payload.

call\_id: string

The unique ID of this call.

sip\_headers: array of object { name, value }

Headers from the SIP Invite.

name: string

Name of the SIP Header.

value: string

Value of the SIP Header.

type: "realtime.call.incoming"

The type of the event. Always `realtime.call.incoming`.

object: optional "event"

The object of the event. Always `event`.

"event"

response\_cancelled\_webhook\_event: object { id, created\_at, data, 2 more }

Sent when a background response has been cancelled.

id: string

The unique ID of the event.

created\_at: number

The Unix timestamp (in seconds) of when the model response was cancelled.

data: object { id }

Event data payload.

id: string

The unique ID of the model response.

type: "response.cancelled"

The type of the event. Always `response.cancelled`.

object: optional "event"

The object of the event. Always `event`.

"event"

response\_completed\_webhook\_event: object { id, created\_at, data, 2 more }

Sent when a background response has been completed.

id: string

The unique ID of the event.

created\_at: number

The Unix timestamp (in seconds) of when the model response was completed.

data: object { id }

Event data payload.

id: string

The unique ID of the model response.

type: "response.completed"

The type of the event. Always `response.completed`.

object: optional "event"

The object of the event. Always `event`.

"event"

response\_failed\_webhook\_event: object { id, created\_at, data, 2 more }

Sent when a background response has failed.

id: string

The unique ID of the event.

created\_at: number

The Unix timestamp (in seconds) of when the model response failed.

data: object { id }

Event data payload.

id: string

The unique ID of the model response.

type: "response.failed"

The type of the event. Always `response.failed`.

object: optional "event"

The object of the event. Always `event`.

"event"

response\_incomplete\_webhook\_event: object { id, created\_at, data, 2 more }

Sent when a background response has been interrupted.

id: string

The unique ID of the event.

created\_at: number

The Unix timestamp (in seconds) of when the model response was interrupted.

data: object { id }

Event data payload.

id: string

The unique ID of the model response.

type: "response.incomplete"

The type of the event. Always `response.incomplete`.

object: optional "event"

The object of the event. Always `event`.

"event"
