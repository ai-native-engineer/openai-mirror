<!-- source: https://developers.openai.com/api/docs/models/gpt-transcribe -->

OverviewModelsAgentsToolsVoice & AudioProductionAPI referenceDocs sectionModels

[Models](/api/docs/models)

![gpt-transcribe](/images/api/models/icons/gpt-transcribe.png)

GPT Transcribe

Default

High-accuracy speech-to-text model for file and Realtime input transcription

High-accuracy speech-to-text model for file and Realtime input transcription

Compare

Performance

Highest

Speed

Medium

Price

$0.0045

Price

Input

Audio, text

Output

Text

GPT Transcribe is a speech-to-text model for completed audio files, streamed file transcripts, and committed turns in Realtime sessions over WebSocket. It supports unstructured context, keyword hints, and multiple language hints to improve transcription of domain terms, multilingual audio, and code-switching.

Pricing

Pricing is based on the number of tokens used, or other metrics based on the model type. For tool-specific models, like search and computer use, there’s a fee per tool call. See details in the [pricing page](/api/docs/pricing).

Transcription audio duration

Per minute

Price

$0.0045

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

Snapshots let you lock in a specific version of the model so that performance and behavior remain consistent. Below is a list of all available snapshots and aliases for GPT Transcribe.

![gpt-transcribe](/images/api/models/icons/gpt-transcribe.png)

gpt-transcribe

gpt-transcribe

gpt-transcribe
