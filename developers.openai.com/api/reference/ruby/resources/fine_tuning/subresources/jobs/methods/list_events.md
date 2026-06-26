<!-- source: https://developers.openai.com/api/reference/ruby/resources/fine_tuning/subresources/jobs/methods/list_events/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Fine Tuning](/api/reference/ruby/resources/fine_tuning)

[Jobs](/api/reference/ruby/resources/fine_tuning/subresources/jobs)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List fine-tuning events

fine\_tuning.jobs.list\_events(fine\_tuning\_job\_id, \*\*kwargs) -> CursorPage<[FineTuningJobEvent](/api/reference/ruby/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_event%20%3E%20(schema)) { id, created\_at, level, 4 more } >

GET/fine\_tuning/jobs/{fine\_tuning\_job\_id}/events

Get status updates for a fine-tuning job.

##### ParametersExpand Collapse

fine\_tuning\_job\_id: String

after: String

Identifier for the last event from the previous pagination request.

limit: Integer

Number of events to retrieve.

##### ReturnsExpand Collapse

class FineTuningJobEvent { id, created\_at, level, 4 more }

Fine-tuning job event object

id: String

The object identifier.

created\_at: Integer

The Unix timestamp (in seconds) for when the fine-tuning job was created.

formatunixtime

level: :info | :warn | :error

The log level of the event.

One of the following:

:info

:warn

:error

message: String

The message of the event.

object: :"fine\_tuning.job.event"

The object type, which is always “fine\_tuning.job.event”.

data: untyped

The data associated with the event.

type: :message | :metrics

The type of event.

One of the following:

:message

:metrics

### List fine-tuning events

Ruby

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.fine_tuning.jobs.list_events("ft-AF1WoRqd3aJAHsqc9NY7iL8F")

puts(page)

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
