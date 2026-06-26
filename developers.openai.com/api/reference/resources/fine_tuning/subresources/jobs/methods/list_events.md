<!-- source: https://developers.openai.com/api/reference/resources/fine_tuning/subresources/jobs/methods/list_events/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Fine Tuning](/api/reference/resources/fine_tuning)

[Jobs](/api/reference/resources/fine_tuning/subresources/jobs)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List fine-tuning events

GET/fine\_tuning/jobs/{fine\_tuning\_job\_id}/events

Get status updates for a fine-tuning job.

##### Path ParametersExpand Collapse

fine\_tuning\_job\_id: string

##### Query ParametersExpand Collapse

after: optional string

Identifier for the last event from the previous pagination request.

limit: optional number

Number of events to retrieve.

##### ReturnsExpand Collapse

data: array of [FineTuningJobEvent](/api/reference/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_event%20%3E%20(schema)) { id, created\_at, level, 4 more }

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

has\_more: boolean

object: "list"

### List fine-tuning events

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/fine_tuning/jobs/ftjob-abc123/events \
  -H "Authorization: Bearer $OPENAI_API_KEY"

  "object": "list",
  "data": [
      "object": "fine_tuning.job.event",
      "id": "ft-event-ddTJfwuMVpfLXseO0Am0Gqjm",
      "created_at": 1721764800,
      "level": "info",
      "message": "Fine tuning job successfully completed",
      "data": null,
      "type": "message"
      "object": "fine_tuning.job.event",
      "id": "ft-event-tyiGuB72evQncpH87xe505Sv",
      "created_at": 1721764800,
      "level": "info",
      "message": "New fine-tuned model created: ft:gpt-4o-mini:openai::7p4lURel",
      "data": null,
      "type": "message"
  ],
  "has_more": true

##### Returns Examples

  "object": "list",
  "data": [
      "object": "fine_tuning.job.event",
      "id": "ft-event-ddTJfwuMVpfLXseO0Am0Gqjm",
      "created_at": 1721764800,
      "level": "info",
      "message": "Fine tuning job successfully completed",
      "data": null,
      "type": "message"
      "object": "fine_tuning.job.event",
      "id": "ft-event-tyiGuB72evQncpH87xe505Sv",
      "created_at": 1721764800,
      "level": "info",
      "message": "New fine-tuned model created: ft:gpt-4o-mini:openai::7p4lURel",
      "data": null,
      "type": "message"
  ],
  "has_more": true
