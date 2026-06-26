<!-- source: https://developers.openai.com/api/reference/go/resources/audio/subresources/translations/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Audio](/api/reference/go/resources/audio)

[Translations](/api/reference/go/resources/audio/subresources/translations)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create translation

client.Audio.Translations.New(ctx, body) (\*[Translation](/api/reference/go/resources/audio#(resource)%20audio.translations%20%3E%20(model)%20translation%20%3E%20(schema)), error)

POST/audio/translations

Translates audio into English.

##### ParametersExpand Collapse

body AudioTranslationNewParams

File param.Field[[Reader](/api/reference/go/resources/audio/subresources/translations/methods/create#(resource)%20audio.translations%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20file%20%3E%20(schema))]

The audio file object (not file name) translate, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.

Model param.Field[[AudioModel](/api/reference/go/resources/audio#(resource)%20audio%20%3E%20(model)%20audio_model%20%3E%20(schema))]

ID of the model to use. Only `whisper-1` (which is powered by our open source Whisper V2 model) is currently available.

string

type AudioModel string

One of the following:

const AudioModelWhisper1 [AudioModel](/api/reference/go/resources/audio#(resource)%20audio%20%3E%20(model)%20audio_model%20%3E%20(schema)) = "whisper-1"

const AudioModelGPT4oTranscribe [AudioModel](/api/reference/go/resources/audio#(resource)%20audio%20%3E%20(model)%20audio_model%20%3E%20(schema)) = "gpt-4o-transcribe"

const AudioModelGPT4oMiniTranscribe [AudioModel](/api/reference/go/resources/audio#(resource)%20audio%20%3E%20(model)%20audio_model%20%3E%20(schema)) = "gpt-4o-mini-transcribe"

const AudioModelGPT4oMiniTranscribe2025\_12\_15 [AudioModel](/api/reference/go/resources/audio#(resource)%20audio%20%3E%20(model)%20audio_model%20%3E%20(schema)) = "gpt-4o-mini-transcribe-2025-12-15"

const AudioModelGPT4oTranscribeDiarize [AudioModel](/api/reference/go/resources/audio#(resource)%20audio%20%3E%20(model)%20audio_model%20%3E%20(schema)) = "gpt-4o-transcribe-diarize"

Prompt param.Field[string]Optional

An optional text to guide the model’s style or continue a previous audio segment. The [prompt](https://platform.openai.com/docs/guides/speech-to-text#prompting) should be in English.

ResponseFormat param.Field[[AudioTranslationNewParamsResponseFormat](/api/reference/go/resources/audio/subresources/translations/methods/create#(resource)%20audio.translations%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20response_format%20%3E%20(schema))]Optional

The format of the output, in one of these options: `json`, `text`, `srt`, `verbose_json`, or `vtt`.

const AudioTranslationNewParamsResponseFormatJSON [AudioTranslationNewParamsResponseFormat](/api/reference/go/resources/audio/subresources/translations/methods/create#(resource)%20audio.translations%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20response_format%20%3E%20(schema)) = "json"

const AudioTranslationNewParamsResponseFormatText [AudioTranslationNewParamsResponseFormat](/api/reference/go/resources/audio/subresources/translations/methods/create#(resource)%20audio.translations%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20response_format%20%3E%20(schema)) = "text"

const AudioTranslationNewParamsResponseFormatSRT [AudioTranslationNewParamsResponseFormat](/api/reference/go/resources/audio/subresources/translations/methods/create#(resource)%20audio.translations%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20response_format%20%3E%20(schema)) = "srt"

const AudioTranslationNewParamsResponseFormatVerboseJSON [AudioTranslationNewParamsResponseFormat](/api/reference/go/resources/audio/subresources/translations/methods/create#(resource)%20audio.translations%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20response_format%20%3E%20(schema)) = "verbose\_json"

const AudioTranslationNewParamsResponseFormatVTT [AudioTranslationNewParamsResponseFormat](/api/reference/go/resources/audio/subresources/translations/methods/create#(resource)%20audio.translations%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20response_format%20%3E%20(schema)) = "vtt"

Temperature param.Field[float64]Optional

The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.

##### ReturnsExpand Collapse

type AudioTranslationNewResponse interface{…}

One of the following:

type Translation struct{…}

Text string

### Create translation

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
  "bytes"
  "context"
  "fmt"
  "io"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  translation, err := client.Audio.Translations.New(context.TODO(), openai.AudioTranslationNewParams{
    File: io.Reader(bytes.NewBuffer([]byte("Example data"))),
    Model: openai.AudioModelWhisper1,
  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", translation)

  "text": "Hello, my name is Wolfgang and I come from Germany. Where are you heading today?"

##### Returns Examples

  "text": "Hello, my name is Wolfgang and I come from Germany. Where are you heading today?"
