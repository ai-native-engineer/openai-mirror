<!-- source: https://help.openai.com/en/articles/7031512-audio-api-faq -->

# Audio API FAQ

General questions about the Whisper, speech to text, Audio API

Updated: 10 days ago

The Audio API supports two speech to text endpoints:

* `transcriptions`
* `translations`

To get started with the Audio API, please read our [speech to text developer documentation](https://platform.openai.com/docs/guides/speech-to-text).  
  
  
**How much does the Audio API cost to use?**  
  
See our [pricing page](https://platform.openai.com/docs/pricing) for details.  
  
  
**What languages are supported?**  
  
View a list of [supported languages here](https://platform.openai.com/docs/guides/speech-to-text/supported-languages/#supported-languages).  
  
  
**How can we handle large audio files?**  
  
For legacy/whisper-1 Audio API transcription uploads, the maximum request size is 25 MiB. Newer gpt-4o transcription routes may use different validation, such as duration or token limits, so check the model-specific documentation when handling long audio inputs from users.  
  
  
**What streaming methods are available?**  
  
There are two ways you can stream your transcription depending on your use case and whether you are trying to transcribe an already completed audio recording or handle an ongoing stream of audio and use OpenAI for turn detection:

* [Streaming the transcription of a completed audio recording](https://platform.openai.com/docs/guides/speech-to-text#streaming-the-transcription-of-a-completed-audio-recording)
* [Streaming the transcription of an ongoing audio recording](https://platform.openai.com/docs/guides/speech-to-text#streaming-the-transcription-of-an-ongoing-audio-recording)

Note that streaming is not supported with the `whisper-1` model.

**What file formats are supported?**  
  
The supported file formats are included [in our API docs](https://platform.openai.com/docs/guides/speech-to-text#overview).  
  
  
**Can I send links to audio files to the Audio API?**  
  
No, you must send a file in one of the supported audio formats.
