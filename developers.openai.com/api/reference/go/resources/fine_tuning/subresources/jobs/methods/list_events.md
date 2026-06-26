<!-- source: https://developers.openai.com/api/reference/go/resources/fine_tuning/subresources/jobs/methods/list_events/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Fine Tuning](/api/reference/go/resources/fine_tuning)

[Jobs](/api/reference/go/resources/fine_tuning/subresources/jobs)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List fine-tuning events

client.FineTuning.Jobs.ListEvents(ctx, fineTuningJobID, query) (\*CursorPage[[FineTuningJobEvent](/api/reference/go/resources/fine_tuning#(resource)%20fine_tuning.jobs%20%3E%20(model)%20fine_tuning_job_event%20%3E%20(schema))], error)

GET/fine\_tuning/jobs/{fine\_tuning\_job\_id}/events

Get status updates for a fine-tuning job.

##### ParametersExpand Collapse

fineTuningJobID string

query FineTuningJobListEventsParams

After param.Field[string]Optional

Identifier for the last event from the previous pagination request.

Limit param.Field[int64]Optional

Number of events to retrieve.

##### ReturnsExpand Collapse

type FineTuningJobEvent struct{…}

Fine-tuning job event object

ID string

The object identifier.

CreatedAt int64

The Unix timestamp (in seconds) for when the fine-tuning job was created.

formatunixtime

Level FineTuningJobEventLevel

The log level of the event.

One of the following:

const FineTuningJobEventLevelInfo FineTuningJobEventLevel = "info"

const FineTuningJobEventLevelWarn FineTuningJobEventLevel = "warn"

const FineTuningJobEventLevelError FineTuningJobEventLevel = "error"

Message string

The message of the event.

Object FineTuningJobEvent

The object type, which is always “fine\_tuning.job.event”.

Data anyOptional

The data associated with the event.

Type FineTuningJobEventTypeOptional

The type of event.

One of the following:

const FineTuningJobEventTypeMessage FineTuningJobEventType = "message"

const FineTuningJobEventTypeMetrics FineTuningJobEventType = "metrics"

### List fine-tuning events

Go

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  page, err := client.FineTuning.Jobs.ListEvents(
    context.TODO(),
    "ft-AF1WoRqd3aJAHsqc9NY7iL8F",
    openai.FineTuningJobListEventsParams{

  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

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
