<!-- source: https://developers.openai.com/api/docs/models/gpt-live-transcribe -->

OverviewModelsAgentsToolsVoice & AudioProductionAPI referenceDocs sectionModels

[Models](/api/docs/models)

![gpt-live-transcribe](/images/api/models/icons/gpt-live-transcribe.png)

GPT Live Transcribe

Default

Low-latency speech-to-text model for realtime transcription

Low-latency speech-to-text model for realtime transcription

Compare

Performance

Highest

Speed

Very fast

Price

$0.017

Price

Input

Audio, text

Output

Text

GPT Live Transcribe is a streaming speech-to-text model for applications that need low-latency transcript deltas from live audio. It supports tunable latency, unstructured context, keyword hints, and multiple language hints.

Pricing

Pricing is based on the number of tokens used, or other metrics based on the model type. For tool-specific models, like search and computer use, there’s a fee per tool call. See details in the [pricing page](/api/docs/pricing).

Realtime audio duration

Per minute

Price

$0.017

Modalities

Text

Input and output

Image

Not supported

Audio

Input only

Video

Not supported

Endpoints

Chat Completions

v1/chat/completions

Responses

v1/responses

Realtime

v1/realtime

Realtime translation

v1/realtime/translations

Realtime transcription

v1/realtime/transcription\_sessions

Assistants

v1/assistants

Batch

v1/batch

Fine-tuning

v1/fine-tuning

Embeddings

v1/embeddings

Image generation

v1/images/generations

Videos

v1/videos

Image edit

v1/images/edits

Speech generation

v1/audio/speech

Transcription

v1/audio/transcriptions

Translation

v1/audio/translations

Moderation

v1/moderations

Completions (legacy)

v1/completions

Features

Streaming

Supported

Function calling

Not supported

Structured outputs

Not supported

Fine-tuning

Not supported

Predicted outputs

Not supported

Snapshots

Snapshots let you lock in a specific version of the model so that performance and behavior remain consistent. Below is a list of all available snapshots and aliases for GPT Live Transcribe.

![gpt-live-transcribe](/images/api/models/icons/gpt-live-transcribe.png)

gpt-live-transcribe

gpt-live-transcribe

gpt-live-transcribe
