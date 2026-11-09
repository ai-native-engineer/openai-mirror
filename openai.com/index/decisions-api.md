<!-- source: https://openai.com/index/decisions-api/ -->

October 22, 2026

[Product](/news/product-releases/)

# Build more responsive apps with the Decisions API

Fast, focused, low-cost decisions for any application.

Applications and agents make many small decisions throughout a workflow: how to classify an input, where to route a request, or which action to take next. Individually, they are simple. At scale, their latency and cost add up.

Today, we’re making the Decisions API generally available. Built with [GPT‑6 Luna](/index/introducing-gpt-6-sol-and-luna/), the Decisions API focuses Luna’s intelligence on questions with bounded answers, helping applications and agents make near real-time decisions from text, images, and structured inputs up to 10x faster than GPT‑6 Luna through the Responses API.

Since public beta, we’ve added a native GPT‑Live integration, prompt caching for reused context, and inference residency in the US and EU. Developers can also pass native JSON inputs, include images in question instructions, and ask up to 400 questions per request, twice the previous limit. We’ve also continued to improve latency, including additional capacity in several regions in Asia.

## How teams are using the Decisions API

Early adoption of Decisions has shown its applicability across a variety of use cases.

Across OpenAI, teams are applying the Decisions API across product and business workflows. The dots team is using it to reduce response times and improve interactivity. Our Personal Finance team is using it to categorize transaction descriptions, while our Communications team is using Decisions to classify coverage by the themes and scores whether it reinforces or challenges key narratives—helping identify what warrants closer review.

These early examples show how fast, structured decision-making can turn incoming information into useful action across a wide range of use cases. Customers are applying the Decisions API just as broadly, from accurately attributing AI costs to making language-learning experiences more interactive.

1 of 5

> “*With Box Extract and* *the* *Decisions API, we classify business documents and route them to the right next step. In our evaluation,* *the* *Decisions API delivered ~5x faster route selection on 30 certificate of insurance cases, with the same accuracy as* *the* *Responses API—automating routine work and sending lower-confidence cases to reviewers.*”

*—Biswaroop Palit, VP, Product Management Platform and Integrations, Box*

> “*The* *Decisions API is helping us score the risk of agent-generated [*[*rshell commands*⁠(opens in a new window)](https://github.com/datadog/rshell)*] before executing them to autonomously remediate issues. Compared with available frontier models, it delivered 40x faster p95 with comparable accuracy—making it possible to place Decisions* *in the hot path of a remediation action.*”

*—AJ Stuyvenberg, Staff Engineer, Datadog*

> “*The Decisions API has made it 4x faster and 30% cheaper to attribute our AI costs to the actual work when compared to GPT‑6 Luna, without sacrificing accuracy.*”

*—René Sultan, Research Engineer, Ramp*

> “*At Sierra, we use* *the* *Decisions API to choose the right next action during parts of our orchestration in live customer conversations. It runs at under 280 ms p95, about 3× faster and 90% lower cost per call than our previous approach, with no drop in customer outcomes.*”

*—Ajeet Grewal, Engineer, Sierra*

> “For language learners, timing matters. In our testing, the Decisions API integration in GPT‑Live was able to reduce the time to next action by over 90%, from 1.4s to 0.13s, creating a much more interactive learning experience.”

—Andrew Hsu, CTO, Speak

* Box
* Datadog
* Ramp
* Sierra
* Speak

* Box
* Datadog
* Ramp
* Sierra
* Speak

## Select the type of decision your application needs

Using the Decisions API is simple: developers define a question and its allowed answers, then provide context as text, images, or native JSON. The API returns one of three supported answer types—a probability, choice, or score—that applications can use to determine what happens next. The variety of answer types allows Decisions to be applicable across a wide variety of use cases.

Decisions API supports three answer types:

| Type | Use it to | Main result |
| --- | --- | --- |
| predicate | Estimate the probability that a condition is true, such as whether a product has visible damage. | probability: an estimate from 0 to 1 that the condition is true. |
| choice | Select one of your predefined options, such as whether an agent should continue, retry, or ask for clarification. | choice: one of your supplied values. The response also includes probabilities and confidence. |
| score | Rate an input against ordered levels in a rubric, such as the severity of damage. | score: the probability-weighted average of the level indices. |

## Build real-time voice experiences with the Decisions API and GPT‑Live

With [GPT‑Live](/index/introducing-gpt-live-1-in-the-api/), you can bring natural, expressive conversation to your voice applications, with smooth interruption handling that keeps conversations flowing. Decisions API now [integrates natively with GPT‑Live⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/decisions-voice), helping applications make fast, focused decisions during live conversations. A customer support agent can decide whether to ask a clarifying question, route a request, or escalate an issue. An avatar can adjust its facial expressions as a user speaks to it, and based on the user’s words, respond with a wink or a smile to create a more interactive experience.

The example below uses transcript updates to select an avatar’s expression. Add this configuration to `session.triggers` in an existing GPT‑Live session.

#### JSON

```` ```
1

{

2

"type": "decisions",

3

"event_type": "session.input_transcript.delta",

4

"decisions": {

5

"questions": [{

6

"type": "choice",

7

"name": "reaction",

8

"instructions": "Choose an appropriate reaction for the avatar based on the user's latest message.",

9

"choices": [

10

{ "value": "neutral" },

11

{ "value": "happy" },

12

{ "value": "sad" },

13

{ "value": "concerned" }

14

]

15

}]

16

}

17

}
``` ````

Live emits a `decision.event`; the application reads the selected `reaction` and animates the character accordingly. [Learn more about connecting voice to Decisions API. ⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/decisions-voice)

## Try Decisions with GPT‑Live for yourself

Mic off

![](/_next/static/immutable/media/neutral.0e2e43zp24lhc.webp)

![](/_next/static/immutable/media/thinking-bulb.1z1_50iiwd5ra.webp)

Start session

Microphone off until you start

Connecting

Session ends in 0:00

Session ended. Start again if you'd like to keep talking.

Microphone off until you start

## Expression palette

Tap a face to preview it.

![](/_next/static/immutable/media/curious.1z8d03c0o-3de.webp?w=96&q=90&fm=webp)Curious![](/_next/static/immutable/media/delighted.3o_81fgq98onp.webp?w=96&q=90&fm=webp)Delighted![](/_next/static/immutable/media/surprised.3rw2p6nwkx66y.webp?w=96&q=90&fm=webp)Surprised![](/_next/static/immutable/media/thinking-palette.1z5po-ddh-20f.webp?w=96&q=90&fm=webp)Pensive![](/_next/static/immutable/media/empathetic.0mexjnh3muccz.webp?w=96&q=90&fm=webp)Tender![](/_next/static/immutable/media/mischievous.0piy4jm2de8n-.webp?w=96&q=90&fm=webp)Cheeky![](/_next/static/immutable/media/neutral.0e2e43zp24lhc.webp?w=96&q=90&fm=webp)At ease

## Live decisions

Watch as the Decisions API chooses a facial expression based on what each of you says.

### Your words

Watch the reaction as you speak.

### Assistant’s words

Watch the face as the assistant replies.

Try saying

I rehearsed my audition for my cat. She walked out halfway through.

I have a secret. Lean in a little closer.

Actually, my sister got the part. It’s her first show!

I’m nervous about tomorrow. Can you sit with me?

I just got the part! Can you celebrate with me?

Look surprised, then tell me what you saw.

Could you search the web for the next meteor shower?

I rehearsed my audition for my cat. She walked out halfway through.

This demo is time-limited. By using it, you agree to OpenAI's [Terms⁠](/policies/terms-of-use/) and acknowledge our [Privacy Policy⁠](/policies/privacy-policy/).

## Build and evaluate your first decision

Decisions API is generally available today with GPT‑6 Luna through the dedicated Decisions endpoint. See the [pricing and availability guide⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/decisions#pricing-and-availability) for current rates and caching details.

Start with one recurring decision your application makes often. Define the question, the possible answers, and the context needed to distinguish them. Test it on examples that reflect real usage, in the [Decisions Playground⁠(opens in a new window)](https://platform.openai.com/decisions) with your own text or images, or follow the [developer guide⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/decisions) to make your first request.

Decisions API costs $0.10 per million input tokens. Cached input costs $0.01 per million tokens. For 30-minute and 12-hour cached writes, [read our pricing guide.⁠(opens in a new window)](https://developers.openai.com/api/docs/pricing?utm_source=chatgpt.com) You only pay for input tokens: there are no output-token charges. Regional processing is available in the US and EU, and [Zero Data Retention⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/your-data) is available to eligible customers. See [pricing and caching⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/decisions#pricing-and-availability) and [data controls ⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/your-data)for details.

* [API](/news/?tags=api)
* [2026](/news/?tags=2026)

## Author

[View all](/news/)

![Introducing GPT-6 Sol and Luna — Art card](https://images.ctfassets.net/kftzwdyauwt9/4HANTuYDvaT04gpR91bEQ9/885481304c5675cb7525bcccbe8c5580/gpt-6-sol-luna-art.png?w=3840&q=90&fm=webp)

[Introducing GPT-6 Sol and Luna

ProductSep 22, 2026](/index/introducing-gpt-6-sol-and-luna/)

![Introducing the Agents API — cover image](https://images.ctfassets.net/kftzwdyauwt9/6iP1bamSOXsPLwzFAepmx2/8b8fec31ba235a13ee695a607d7fe641/cover-image.png?w=3840&q=90&fm=webp)

[Introducing the Agents API

ProductSep 10, 2026](/index/introducing-the-agents-api/)

![Better prompt caching for GPT-6 — Card image](https://images.ctfassets.net/kftzwdyauwt9/72ZKzMh8JgRDfdg4EYRtwY/ee5e406a08b69f00b0beb4ac00270364/7kneoqlc2qh37z1utkmtfk-cover-v1.png?w=3840&q=90&fm=webp)

[Better prompt caching for GPT-6

ProductSep 22, 2026](/index/better-prompt-caching-for-gpt-6/)
