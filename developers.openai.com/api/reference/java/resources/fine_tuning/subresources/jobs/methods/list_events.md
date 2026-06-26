<!-- source: https://developers.openai.com/api/reference/java/resources/fine_tuning/subresources/jobs/methods/list_events/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Fine Tuning](/api/reference/java/resources/fine_tuning)

[Jobs](/api/reference/java/resources/fine_tuning/subresources/jobs)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List fine-tuning events

JobListEventsPage fineTuning().jobs().listEvents(JobListEventsParamsparams = JobListEventsParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/fine\_tuning/jobs/{fine\_tuning\_job\_id}/events

Get status updates for a fine-tuning job.

##### ParametersExpand Collapse

JobListEventsParams params

Optional<String> fineTuningJobId

Optional<String> after

Identifier for the last event from the previous pagination request.

Optional<Long> limit

Number of events to retrieve.

##### ReturnsExpand Collapse

class FineTuningJobEvent:

Fine-tuning job event object

String id

The object identifier.

long createdAt

The Unix timestamp (in seconds) for when the fine-tuning job was created.

formatunixtime

Level level

The log level of the event.

One of the following:

INFO("info")

WARN("warn")

ERROR("error")

String message

The message of the event.

JsonValue; object\_ "fine\_tuning.job.event"constant"fine\_tuning.job.event"constant

The object type, which is always “fine\_tuning.job.event”.

Optional<JsonValue> data

The data associated with the event.

Optional<Type> type

The type of event.

One of the following:

MESSAGE("message")

METRICS("metrics")

### List fine-tuning events

Java

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.finetuning.jobs.JobListEventsPage;
import com.openai.models.finetuning.jobs.JobListEventsParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        JobListEventsPage page = client.fineTuning().jobs().listEvents("ft-AF1WoRqd3aJAHsqc9NY7iL8F");

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
