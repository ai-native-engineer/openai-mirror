<!-- source: https://openai.com/index/introducing-gpt-live-1-in-the-api/ -->

[Product](/news/product-releases/)[Release](/research/index/release/)

# Build more natural voice experiences with GPT‑Live‑1 in the API

GPT‑Live‑1 brings ChatGPT’s natural, full-duplex conversations to the API, with more control over how voice agents speak and act.

Loading…

Share

We’re launching GPT‑Live‑1 in the API, giving developers a powerful, natural voice model for building voice-enabled apps and business workflows. [First introduced in ChatGPT](/index/introducing-gpt-live/), GPT‑Live‑1 is capable of listening and speaking at the same time, and, as [seen with Codex and ChatGPT Work⁠(opens in a new window)](https://www.youtube.com/watch?v=E0ZMOschrTU), can delegate deeper reasoning and actions to the models and tools it is paired with.

<!-- yt-inline:E0ZMOschrTU -->
[![Building with ChatGPT Voice | OpenAI](https://img.youtube.com/vi/E0ZMOschrTU/hqdefault.jpg)](https://www.youtube.com/watch?v=E0ZMOschrTU)

<details>
<summary>자막: Building with ChatGPT Voice | OpenAI (1:09)</summary>

[00:00]
Hey Chat, put yourself on the projector.
Play my daylist.
One moment.
So we got to prepare some
launch materials for the voice
launch next week. Could you help us
draft some blog posts?
Absolutely. A simple first pass.
Meet Voice in the desktop app.
Voice makes it easier to move
work forward naturally.
What do you think about that?
Use your computer without breaking flow.
Let's ship it.
I got this feature idea for, like, some
last-minute polish we can do.
I'm going to ramble a little bit and
then I want you to ask me some
questions and push back on me.
It looks like we can get pretty far
just inside the shader since it already
has the audio and phase inputs.
Codex, could you go check
the feature flags and make sure
they're all configured properly?
Wait, there's also a new bug report
in the feedback channel.
Can you spin up a new thread,
make a pull request,
find the root cause?
Let me take a look.
Found it. It was that feature flag.
Totally misconfigured.
Happens.
We've got everything set
for launch, right?
Yeah, I think we're ready to go.
You get the idea, just set a goal
and then tag the team for review later.

[00:01]
I'll check in with you from my phone.
Got it.
I'll create a follow-up goal for that.
And then just, you know,
make no mistakes.

</details>


For the API release of GPT‑Live‑1, we’ve focused on new capabilities that let developers steer and customize voice experiences around their users, workflows, and goals. A core GPT‑Live‑1 strength, smooth interruption handling, is already delivering business impact: in early evaluations, Speak found that GPT‑Live‑1 gave learners more time to think before the language tutor responded, cutting interruptions by almost 80% versus previous turn-based systems.

Key strengths of GPT‑Live‑1 in the API:

* **Interruption handling:** Improves interruption handling via a single model that reasons over incoming and outgoing audio together, avoiding the latency and brittle handoffs of chained STT–LLM–TTS architectures.
* **Reasoning & tool calling delegation:** GPT‑Live‑1 can delegate reasoning and tool calls to a backend text model like GPT‑6 Astra or a third-party model.
* **Tone, pace, and style:** Lets developers shape an agent’s tone, pace, and conversational style through the system prompt.
* **Silent context management & background noise:** Better handles background noise and silence without interrupting the conversation or narrating every step out loud.
* **Long-session reliability:** Improves context retention and conversational quality across extended interactions.
* **Telephony support:** Enables deployment of full-duplex voice agents for phone calls, from restaurant reservations to customer support.

# Try GPT-Live-1

Start a session and speak naturally. Interrupt, laugh, change your mind - try it at home or in a loud space like a coffee shop or city street.

Start sessionSee what it can do

* **Talk over it—naturally.** Ask for help, then interrupt mid-response to change the question or add detail.
* **Take it with you.** Try a conversation while walking outside or with everyday background noise, and see how it stays with you.
* **Make it playful.** Laugh, hesitate, use short acknowledgments, or briefly talk to someone nearby—then continue the conversation.

This demo is time-limited. By using it, you agree to OpenAI's [Terms](/policies/terms-of-use/) and acknowledge our [Privacy Policy](/policies/privacy-policy/).

## Simplify your voice-agent architecture and reduce voice latency

Traditional voice agents stitch together speech-to-text, a reasoning model, and text-to-speech. Each handoff adds latency and creates more opportunities to lose timing, context, or the natural rhythm of a conversation. Developers are often the ones left coordinating those stages, including what happens when someone interrupts, pauses, or changes direction.

GPT‑Live‑1 handles listening and speaking in a single model, simplifying the voice layer. It can respond to interruptions and acknowledgements as they happen, while delegating deeper reasoning to the back end. This lets the conversation continue while work happens in the background.

> “Compared to our cascaded build, GPT‑Live‑1 simplified our code base by 80% and removed 23K lines of code. This enabled natural, real-time patient conversations & freed our team to improve the experience from booking an appointment to navigating care.”

—Tony Stoyanov, Co-Founder & CTO

Developers choose the models, tools, and agent harness behind the conversation. For example, they might pair GPT‑Live‑1 with a model like Luna for high-volume tasks like scheduling or order updates, and use a model like Astra for complex customer issues that require reasoning. That flexibility lets developers match reasoning depth, speed, and cost to each task.

GPT‑Live‑1 natively provides ASR transcripts and response text. It also offers strong alphanumeric understanding and supports keyword biasing. Although GPT‑Live‑1 is not a turn-based model, it natively supports turn detection, so developers can continue to build around explicit turn boundaries.

## Measuring the full-duplex advantage

Across our evaluations, GPT‑Live‑1 improves Full Duplex Bench performance by 30 percentage points over GPT‑Realtime‑2.1, with large gains in turn-taking latency and interactive behavior. Paired with GPT‑6 Astra at medium reasoning effort, it also ranks #1 on Tau3, which measures frontier voice-agent intelligence on end-to-end tasks.

Evaluates spoken customer-service tasks in airline, retail, and telecom domains. Pass@1 measures task success; the headline gives each domain equal weight.

\* GPT Live backend: Astra (medium).

Evaluates spoken banking support with knowledge retrieval and account tools. Pass@1 is the fraction of 97 banking\_knowledge tasks completed successfully.

\* GPT Live backend: Astra (medium).

Evaluates pause handling, conversational turn taking, interruptions, and backchannels.

Tests reactions to background speech, speech to another person, listener backchannels, and interruptions.

Measures how quickly the agent starts its reply after the user finishes a turn.

Tests tool use from spoken requests containing natural pauses, hesitations, and self-corrections. Pass@1 scores the tool-call sequence.

\* GPT Live backend: Terra (low).

Evaluates the spoken answer to tool-using requests containing pauses, hesitations, and self-corrections. Scores how well the answer matches the reference intent.

\* GPT Live backend: Terra (low).

## What customers are saying

1 of 4

> “Adding GPT‑Live‑1 into Yelp Host and Hatch improved turn-taking and accuracy over our traditional voice architecture. When Yelp Host uses GPT‑Live‑1 to answer calls, like reservations and food orders, we're seeing meaningful improvements in call handling rates. Callers are also speaking fuller, more natural sentences, which tells us the experience on the other end of the phone feels genuinely different.”

—Alex Levy, Chief Technology Officer

> “A good language tutor knows when to give learners space and when to step in, and GPT‑Live‑1 brings that naturalness to Speak’s Live Tutor Lessons—in our early evaluations, it cut interruptions during thinking pauses by almost 80% compared with previous turn-based systems.”

—Andrew Hsu, Co-founder & CTO

> “GPT‑Live-1 shows what a full-duplex model can unlock: It moves AI voice support from the stop-start rhythm toward the natural flow of a phone call. Customers can pause, interrupt, and change direction naturally; voice delivery is a clear step forward; and Fin can combine that natural conversation with its proprietary support system to do the deeper work needed to resolve the issue. For us, this is the clearest signal yet of where voice support is heading.”

—Jordan Neil, COO

> “With Devin and GPT‑Live‑1, working with an AI engineer starts to feel more like collaborating with a teammate. You can talk through an idea, pressure-test an approach, or just hand off work while you’re away from your keyboard.”

—Walden Yan, Co-Founder and CPO

* Yelp
* Speak
* Fin
* Cognition

## New voice options

Developers need voices that fit their product and sound natural to the people using it. With GPT‑Live‑1, we’re expanding from a small set of real-time voices to a broader selection across accents, dialects, and languages giving developers more choice in how their assistants sound.

Listen to the new voices

We’ll continue to expand voice options and language availability over the coming months.

## Pricing & Availability

GPT‑Live‑1 is available [in the API today⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/live) at $0.05 per minute for the front-end voice layer. Pair it with the backend model and agent harness that fit your product, then build a voice experience that can scale with the work it needs to do.

#### Connecting GPT-Live-1 to Codex

```` ```
1

import { Codex } from "@openai/codex-sdk";

2

3

const thread = new Codex().startThread({

4

workingDirectory: "./repo",

5

sandboxMode: "read-only",

6

approvalPolicy: "never",

7

});

8

9

async function answer(live, delegationId, context) {

10

const { finalResponse } = await thread.run(

11

`Answer the latest question using this repo.

12

Reply in two short spoken sentences.\n${context}`

13

);

14

15

live.send({

16

type: "session.commentary.append",

17

delegation_id: delegationId,

18

content: finalResponse,

19

});

20

}
``` ````

Connecting GPT-Live-1 to Codex. This excerpt shows how an application passes conversation context to Codex and returns its answer to GPT-Live-1. Connection setup and delegation handling are omitted.

For custom voice access, [contact sales](/contact-sales/) to learn more about eligibility and the request process.

Another way to build voice workflows on top of GPT‑Live‑1 is with [OpenAI Presence](/index/introducing-openai-presence/), which uses the model to power real-time voice interactions. Presence helps enterprises deploy trusted AI agents that can answer questions, resolve issues, use company systems, take approved actions, and escalate to people when needed. Reach out to your OpenAI account director to learn more.

* [API Platform](/news/?tags=api-platform)
* [2026](/news/?tags=2026)

## Author

## Keep reading

[View all](/news/)

![Now everyone can put data to work — card image](https://images.ctfassets.net/kftzwdyauwt9/6FhMXOSe8XadGwEUev6QjJ/916a64d20bcc59b8619fea1827fa6bd3/put-data-to-work--cover-v001.png?w=3840&q=90&fm=webp)

[Now everyone can put data to work

ProductSep 10, 2026](/index/put-data-to-work/)

![FinServ Blog - Art Card Texture Square](https://images.ctfassets.net/kftzwdyauwt9/6Bcg403pebiJhQdHUS17FK/572e478dc4579deca27c9700c662e908/finserv-art-card.png?w=3840&q=90&fm=webp)

[Introducing ChatGPT for Financial Services

ProductSep 10, 2026](/index/introducing-chatgpt-financial-services/)

![Introducing the Agents API — cover image](https://images.ctfassets.net/kftzwdyauwt9/6iP1bamSOXsPLwzFAepmx2/8b8fec31ba235a13ee695a607d7fe641/cover-image.png?w=3840&q=90&fm=webp)

[Introducing the Agents API

ProductSep 10, 2026](/index/introducing-the-agents-api/)

Yelp Host seamlessly secures a reservation with GPT‑Live‑1 handling background noise, side conversations, and interruptions.

Listen00:00

Australian English influenced
