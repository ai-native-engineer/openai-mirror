<!-- source: https://developers.openai.com/api/reference/cli/resources/fine_tuning/subresources/jobs/methods/list_events/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Fine Tuning](/api/reference/cli/resources/fine_tuning)

[Jobs](/api/reference/cli/resources/fine_tuning/subresources/jobs)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List fine-tuning events

$ openai fine-tuning:jobs list-events

GET/fine\_tuning/jobs/{fine\_tuning\_job\_id}/events

Get status updates for a fine-tuning job.

##### ParametersExpand Collapse

--fine-tuning-job-id: string

The ID of the fine-tuning job to get events for.

--after: optional string

Identifier for the last event from the previous pagination request.

--limit: optional number

Number of events to retrieve.

##### ReturnsExpand Collapse

ListFineTuningJobEventsResponse: object { data, has\_more, object }

data: array of [FineTuningJobEvent](/api/reference/cli/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_event%20%3E%20(schema)) { id, created\_at, level, 4 more }

id: string

The object identifier.

created\_at: number

The Unix timestamp (in seconds) for when the fine-tuning job was created.

level: "info" or "warn" or "error"

The log level of the event.

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

"message"

"metrics"

has\_more: boolean

object: "list"

### List fine-tuning events

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai fine-tuning:jobs list-events \
  --api-key 'My API Key' \
  --fine-tuning-job-id ft-AF1WoRqd3aJAHsqc9NY7iL8F

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
