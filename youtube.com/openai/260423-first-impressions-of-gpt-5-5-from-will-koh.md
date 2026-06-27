---
title: "First impressions of GPT-5.5 from Will Koh"
channel: openai
url: https://www.youtube.com/watch?v=Aq0Q_G-rtfA
youtube_id: Aq0Q_G-rtfA
published: 2026-04-23
duration: "3:26"
captions: en
---

# First impressions of GPT-5.5 from Will Koh

[![First impressions of GPT-5.5 from Will Koh](https://img.youtube.com/vi/Aq0Q_G-rtfA/hqdefault.jpg)](https://www.youtube.com/watch?v=Aq0Q_G-rtfA)

<details>
<summary>자막: First impressions of GPT-5.5 from Will Koh (3:26)</summary>

[00:00]
Hi everyone, Romain from OpenAI here.
Very excited to be here today with Will,
who is an AI engineer.
And Will, you've been using AI models for coding
for a long time now.
How has it felt?
How has it been?
It's been a wild journey.
I feel like even two years ago, we started off
with tab completions,
and now we're all the way to the point
where AI is actively doing ambiguous tasks
that we assign it and partitions it and just gets it done.
And it's just been kind of amazing being there
at the forefront of it all.
Obviously, I'm lucky enough to have access, you know, early access to some of the newest models.
But yeah, it's been honestly a crazy time.
Speaking of newest model, I'm very excited that you've tried GPT-5.5.
What has been your first impression?
My first impression of GPT-5.5 is that it is different in the sense that it actually understands what I'm trying to tell it to do.
I see before previously, a lot of my prompts have to be very detailed or very instruction-y,

[00:01]
kind of, where I'm trying to tell it like, "hey, look in this part of the code base, do this."
Whereas with GPT-5.5, sometimes I become lazy and I kind of give it a very ambiguous task,
but then it will figure it out.
It actually directs its research and exploration to the right areas of the code base,
comes up with potentially multiple options of how we could do it,
and then gets it done for me.
So it's been impressive.
That's amazing.
And I think in your work at Ramp, you were also building your own harness, right?
I'd love to hear more how you've been using and testing GPT-5.5 in this harness of yours.
Yeah, so at Ramp, we do have our own harness called Inspect.
And it was honestly just kind of a plug and play.
So we opened the API, opened it to GPT-5.5, and it worked like any other model.
But the impressive part was that it was discovering ways to use the tools that we had given it,
such as access to our databases, access to our telemetry tools,
and figure out novel ways to solve problems using them.
So it's been interesting to see how it comes up with newer ways to solve problems.

[00:02]
Was that a magical thing that you did not see the others model do before?
Yeah, the other models, I would have to direct it to use tools,
or it would sometimes use the wrong tools.
And it got the job done in the end, I think, one way or the other,
and a lot of intervention.
But with GPT-5.5, it's been discovering ways to solve the problem on its own.
I'm curious, in your testing so far for the past week or so,
has there been anything that really surprised you that the model got right?
Yeah, I think, so with some of the tasks that I'm giving it, with the bigger tasks,
it's more likely to run out of its context window.
But during those compaction periods, I actually noticed it much less as if it's running on the same context.
It's able to pass on the right details, the right findings, and the right goal
from one compaction to the other and is able to carry on its task as if compaction never happened.
I think that's amazing.
Can you tell us more about the evals you've run so far?
Yeah, so we have within Ramp some benchmarks that we have for our use cases such as

[00:03]
extracting information out of large customer financial documents and how often can we get it from
a zero touch we got everything correct and we call that perfect extraction rate.
And we've seen that GPT-5.5 is actually performing at the highest rate of that,
which is amazing for our customers.
You know, it's like a magical experience for them.
And we're really excited to get that into their hands.

</details>
