<!-- source: https://developers.openai.com/api/reference/go/resources/audio/subresources/speech/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Audio](/api/reference/go/resources/audio)

[Speech](/api/reference/go/resources/audio/subresources/speech)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create speech

client.Audio.Speech.New(ctx, body) (\*Response, error)

POST/audio/speech

Generates audio from the input text.

Returns the audio file content, or a stream of audio events.

##### ParametersExpand Collapse

body AudioSpeechNewParams

Input param.Field[string]

The text to generate audio for. The maximum length is 4096 characters.

maxLength4096

Model param.Field[[SpeechModel](/api/reference/go/resources/audio#(resource)%20audio.speech%20%3E%20(model)%20speech_model%20%3E%20(schema))]

One of the available [TTS models](https://platform.openai.com/docs/models#tts): `tts-1`, `tts-1-hd`, `gpt-4o-mini-tts`, or `gpt-4o-mini-tts-2025-12-15`.

string

type SpeechModel string

One of the following:

const SpeechModelTTS1 [SpeechModel](/api/reference/go/resources/audio#(resource)%20audio.speech%20%3E%20(model)%20speech_model%20%3E%20(schema)) = "tts-1"

const SpeechModelTTS1HD [SpeechModel](/api/reference/go/resources/audio#(resource)%20audio.speech%20%3E%20(model)%20speech_model%20%3E%20(schema)) = "tts-1-hd"

const SpeechModelGPT4oMiniTTS [SpeechModel](/api/reference/go/resources/audio#(resource)%20audio.speech%20%3E%20(model)%20speech_model%20%3E%20(schema)) = "gpt-4o-mini-tts"

const SpeechModelGPT4oMiniTTS2025\_12\_15 [SpeechModel](/api/reference/go/resources/audio#(resource)%20audio.speech%20%3E%20(model)%20speech_model%20%3E%20(schema)) = "gpt-4o-mini-tts-2025-12-15"

Voice param.Field[[AudioSpeechNewParamsVoiceUnion](/api/reference/go/resources/audio/subresources/speech/methods/create#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20voice%20%3E%20(schema))]

The voice to use when generating the audio. Supported built-in voices are `alloy`, `ash`, `ballad`, `coral`, `echo`, `fable`, `onyx`, `nova`, `sage`, `shimmer`, `verse`, `marin`, and `cedar`. You may also provide a custom voice object with an `id`, for example `{ "id": "voice_1234" }`. Previews of the voices are available in the [Text to speech guide](https://platform.openai.com/docs/guides/text-to-speech#voice-options).

string

type AudioSpeechNewParamsVoiceString2 string

One of the following:

const AudioSpeechNewParamsVoiceString2Alloy AudioSpeechNewParamsVoiceString2 = "alloy"

const AudioSpeechNewParamsVoiceString2Ash AudioSpeechNewParamsVoiceString2 = "ash"

const AudioSpeechNewParamsVoiceString2Ballad AudioSpeechNewParamsVoiceString2 = "ballad"

const AudioSpeechNewParamsVoiceString2Coral AudioSpeechNewParamsVoiceString2 = "coral"

const AudioSpeechNewParamsVoiceString2Echo AudioSpeechNewParamsVoiceString2 = "echo"

const AudioSpeechNewParamsVoiceString2Sage AudioSpeechNewParamsVoiceString2 = "sage"

const AudioSpeechNewParamsVoiceString2Shimmer AudioSpeechNewParamsVoiceString2 = "shimmer"

const AudioSpeechNewParamsVoiceString2Verse AudioSpeechNewParamsVoiceString2 = "verse"

const AudioSpeechNewParamsVoiceString2Marin AudioSpeechNewParamsVoiceString2 = "marin"

const AudioSpeechNewParamsVoiceString2Cedar AudioSpeechNewParamsVoiceString2 = "cedar"

type AudioSpeechNewParamsVoiceID struct{…}

Custom voice reference.

ID string

The custom voice ID, e.g. `voice_1234`.

Instructions param.Field[string]Optional

Control the voice of your generated audio with additional instructions. Does not work with `tts-1` or `tts-1-hd`.

maxLength4096

ResponseFormat param.Field[[AudioSpeechNewParamsResponseFormat](/api/reference/go/resources/audio/subresources/speech/methods/create#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20response_format%20%3E%20(schema))]Optional

The format to audio in. Supported formats are `mp3`, `opus`, `aac`, `flac`, `wav`, and `pcm`.

const AudioSpeechNewParamsResponseFormatMP3 [AudioSpeechNewParamsResponseFormat](/api/reference/go/resources/audio/subresources/speech/methods/create#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20response_format%20%3E%20(schema)) = "mp3"

const AudioSpeechNewParamsResponseFormatOpus [AudioSpeechNewParamsResponseFormat](/api/reference/go/resources/audio/subresources/speech/methods/create#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20response_format%20%3E%20(schema)) = "opus"

const AudioSpeechNewParamsResponseFormatAAC [AudioSpeechNewParamsResponseFormat](/api/reference/go/resources/audio/subresources/speech/methods/create#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20response_format%20%3E%20(schema)) = "aac"

const AudioSpeechNewParamsResponseFormatFLAC [AudioSpeechNewParamsResponseFormat](/api/reference/go/resources/audio/subresources/speech/methods/create#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20response_format%20%3E%20(schema)) = "flac"

const AudioSpeechNewParamsResponseFormatWAV [AudioSpeechNewParamsResponseFormat](/api/reference/go/resources/audio/subresources/speech/methods/create#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20response_format%20%3E%20(schema)) = "wav"

const AudioSpeechNewParamsResponseFormatPCM [AudioSpeechNewParamsResponseFormat](/api/reference/go/resources/audio/subresources/speech/methods/create#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20response_format%20%3E%20(schema)) = "pcm"

Speed param.Field[float64]Optional

The speed of the generated audio. Select a value from `0.25` to `4.0`. `1.0` is the default.

minimum0.25

maximum4

StreamFormat param.Field[[AudioSpeechNewParamsStreamFormat](/api/reference/go/resources/audio/subresources/speech/methods/create#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20stream_format%20%3E%20(schema))]Optional

The format to stream the audio in. Supported formats are `sse` and `audio`. `sse` is not supported for `tts-1` or `tts-1-hd`.

const AudioSpeechNewParamsStreamFormatSSE [AudioSpeechNewParamsStreamFormat](/api/reference/go/resources/audio/subresources/speech/methods/create#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20stream_format%20%3E%20(schema)) = "sse"

const AudioSpeechNewParamsStreamFormatAudio [AudioSpeechNewParamsStreamFormat](/api/reference/go/resources/audio/subresources/speech/methods/create#(resource)%20audio.speech%20%3E%20(method)%20create%20%3E%20(params)%20default%20%3E%20(param)%20stream_format%20%3E%20(schema)) = "audio"

##### ReturnsExpand Collapse

type AudioSpeechNewResponse interface{…}

### Create speech

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
  speech, err := client.Audio.Speech.New(context.TODO(), openai.AudioSpeechNewParams{
    Input: "input",
    Model: openai.SpeechModelTTS1,
    Voice: openai.AudioSpeechNewParamsVoiceUnion{
      OfAudioSpeechNewsVoiceString2: openai.String("alloy"),
  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", speech)

##### Returns Examples
