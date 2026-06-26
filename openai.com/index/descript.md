<!-- source: https://openai.com/index/descript/ -->

March 6, 2026

Startup

# How Descript engineers multilingual video dubbing at scale

Using OpenAI reasoning models, Descript unlocked automatic localization of large content libraries without losing timing or meaning.

[Start Building](/startups/)

![Descript logo and wordmark over a pink and purple abstract waveform background.](https://images.ctfassets.net/kftzwdyauwt9/7wL94yXvqYUEQRfOpp68V8/4f6d4a21db6e98ddb2352cbc52ac3b77/oai_descript_1x1.png?w=3840&q=90&fm=webp)

Company size: Startup

Region: North America

Industry: Technology

Products: API

Results

43

Percentage point improvement in duration adherence with OpenAI

Results

15%

Increase in dubbed exports post-rollout

[Descript⁠(opens in a new window)](http://descript.com) is an AI-native video editor built around a simple idea: if you can edit text, you should be able to edit video. Since Descript’s early days, AI has powered every aspect of the product: transcription, editing, audio cleanup, and increasingly complex creative workflows. They’ve built on OpenAI for years, using Whisper for transcription and GPT series models inside their co-editor Underlord.

Translation quickly emerged as a high-impact use case. Traditionally, translating video has been slow and expensive, requiring language experts to manage projects, produce rote translations, handle quality control, and generate corresponding audio. LLMs dramatically compress that workflow, making high-quality translation at scale possible.

Captions and dubbing both require semantic fidelity: the translation must preserve the original meaning. But duration adherence plays a different role in each. For captions, it's a nice-to-have. For dubbing, it's critical, because if translated speech runs too long or too short, it will sound unnatural even if the meaning is correct.

To address this, Descript redesigned its translation pipeline using OpenAI reasoning models to optimize for semantic fidelity and duration adherence during generation, not after. In the first 30 days after rollout, exports of translated videos with dubbing increased 15%, and duration adherence improved by 13 to 43 percentage points, depending on the language.

“Dubbing is an increasingly popular use case for Descript, so we’re building ways to do it in batch for companies that want to translate and lip-sync entire libraries,” said Laura Burkhauser, CEO.

## Where dubbing started to break down

Translation was one of Descript’s earliest and most requested features. They started with captions-only translation, which worked well—but many users wanted to go further and have spoken audio (dubbing) in the target language.

However, one issue kept surfacing: dubbed audio didn’t always sound right. “Probably the number one complaint we heard was that the pace of the speech was unnatural in the translated language,” said Aleks Mistratov, Head of AI Product at Descript.

The problem came down to the fact that different languages take different amounts of time to express the same idea. Descript observed, for instance, that on average German is a “longer” language than English. To fit into fixed video segments, translated speech often had to be artificially sped up or slowed down. “You’d end up with something that sounded like chipmunks, or a sleepy giant,” Mistratov explained.

|  |  |
| --- | --- |
| **English:** | **German:** |
| “Please review the safety guidelines before operating the machine.”  **Syllables: 18** | “Bitte überprüfen Sie die Sicherheitsrichtlinien, bevor Sie die Maschine bedienen.”  **Syllables: 24** (40% increase) |

*In this case, the German audio would either have to be sped up unnaturally, or the translation would need to be rewritten to fit the time budget.*

Users were left with two options: manually retime the audio segment by segment, or rewrite the translation itself to make it fit. Both approaches required deep timeline edits and, often, near-native fluency in the target language. It was tedious for creators, and became a blocker to scaling the feature to large enterprise localization projects.

## Optimizing translations for timing, not just meaning

The team had a clear theory of what it would take to make dubbing work. The system would need to not only optimize for semantic meaning, but also be aware of timing constraints. When translating from English into German, for example, the model would need to understand how to use fewer words or simplify the concept, so the dubbed audio would remain natural.

Earlier approaches optimized semantic fidelity first and attempted to correct timing afterward. The translations were often semantically correct, but they routinely missed the duration constraints, and the overall quality still wasn’t good enough.

“We ran incremental tests, not even generating anything, just asking the model to output the number of syllables in a chunk of text,” Mistratov said. “Earlier models simply weren’t good at that.”

Reliable syllable counting turned out to be critical. If the model could not consistently calculate syllables, it could not reliably target a specific duration window.

GPT‑5 series models brought a level of reasoning consistency that earlier models lacked, especially on tasks like syllable counting and constraint tracking. With that improvement, Descript redesigned its translation and dubbing pipeline.

First, Descript’s system breaks the transcript into chunks, guided by sentence boundaries, natural pauses, and speaking patterns in the original recording. Each chunk maintains semantic continuity, but is small enough to reason about as a timing unit.

From there, the model calculates the number of syllables in the chunk. Using language-specific speaking-rate assumptions, the system estimates how many syllables the translated chunk should target to preserve natural pacing (“duration adherence”). The prompt asks the model to optimize for both duration adherence and meaning preservation. Surrounding chunks are passed in as context so that the model maintains semantic coherence across segments.

The team evaluated multiple configurations to balance duration adherence, semantic fidelity, latency, and cost. The selected setup delivered strong constraint-following at production speed, enabling high-volume translation without manual retiming. The result is a translation pipeline where pacing is treated as a first-class variable instead of something corrected after the fact.

## Defining and measuring natural pacing

To develop the acceptance criteria for evals, the team ran listening tests: they generated translated audio samples and adjusted the playback speed in small increments, asking users to rate when speech became unnatural.

“Anything that was slowed down by 10%, or sped up by 20%, generally still sounded natural,” Mistratov said. Beyond this range, speech became too distorted.

Earlier systems performed poorly by that measure. Depending on the language, only 40% to 60% of segments fell within the acceptable pacing window. With the redesigned pipeline, that number increased from 40%–60% to between 73% and 83%, depending on language.

The team also evaluated semantic fidelity using a separate model-as-judge rating on a scale ranging from 1 (“completely different”) to 5 (“semantically equivalent”).  For dubbing, they decided to accept a lower semantic threshold than for caption-only translation, where duration constraints are irrelevant. Even with that tradeoff, 85.5% of segments were rated a four or five out of five for semantic adherence.

The result was a system that could balance two competing constraints—timing and meaning—with measurable confidence. And because both metrics were automated, Descript is able to continuously evaluate new model releases and prompt variations against the same benchmarks.

## Unlocking large-scale video localization

As translation moves from single videos to large content libraries, Descript is building more control into how translations are tuned, including the ability to prioritize stricter semantic fidelity when needed.

Translation inside Descript is only one layer of a broader multimodal system. Translated text feeds into speech generation, which then drives lip sync and final video rendering.

Improvements at the text layer make natural pacing possible, but the overall experience also depends on how well the audio model preserves tone, cadence, and nonverbal characteristics of speech. That’s where the team sees the next frontier.

“A lot of what's going to improve translation output is making the pipeline more multimodal: incorporating audio, video, and text together when deciding how to translate,” said Mistratov. “That should better maintain the nonverbal characteristics of speech, like tone and emphasis, and preserve even more of the original delivery.”

For Descript, stronger reasoning models made the complexity of dubbing tractable. By crossing the threshold where models could reliably balance tradeoffs between pacing and meaning, translation became something the team could systematically improve, and deploy at scale.

## OpenAI <3 startups

[Join the community](/leads/startup/)[Start building(opens in a new window)](/startups)

## Keep reading

![Warp customer story 1x1 hero art card](https://images.ctfassets.net/kftzwdyauwt9/3DK9g0hpubvAEz7lDs0nUf/713989b24b9d377312714303868b9126/oai_Warp_1x1.png?w=3840&q=90&fm=webp)

[Warp’s big bet on building open source with GPT-5.5

StartupMay 27, 2026](/index/warp/)

![Parloa > Card](https://images.ctfassets.net/kftzwdyauwt9/79CIP6zYxNAKgc3cJfSimj/cd0b9187ba78aeca8088ba6c11ce8b7e/oai_Parloa_1x1.png?w=3840&q=90&fm=webp)

[Parloa builds service agents customers want to talk to

StartupMay 7, 2026](/index/parloa/)

![oai GradientLabs 1x1](https://images.ctfassets.net/kftzwdyauwt9/5KZQBYyY2LBtllikqf9aul/6143158d9c259eed5aafb47cdac9bcdd/oai_GradientLabs_1x1.png?w=3840&q=90&fm=webp)

[Gradient Labs gives every bank customer an AI account manager

StartupApr 1, 2026](/index/gradient-labs/)
