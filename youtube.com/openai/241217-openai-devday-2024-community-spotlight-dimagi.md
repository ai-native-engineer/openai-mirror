---
title: "OpenAI DevDay 2024 | Community Spotlight | Dimagi"
channel: openai
url: https://www.youtube.com/watch?v=Cj4MU_CJhwU
youtube_id: Cj4MU_CJhwU
published: 2024-12-17
duration: "10:41"
captions: en
---

# OpenAI DevDay 2024 | Community Spotlight | Dimagi

[![OpenAI DevDay 2024 | Community Spotlight | Dimagi](https://img.youtube.com/vi/Cj4MU_CJhwU/hqdefault.jpg)](https://www.youtube.com/watch?v=Cj4MU_CJhwU)

<details>
<summary>자막: OpenAI DevDay 2024 | Community Spotlight | Dimagi (10:41)</summary>

[00:00]
-Hey, everybody.
My name is Anna Dixon.
I'm an applied research
scientist at Dimagi.
That means that I get to do
like a really cool job,
which to take
all the advancements
in AI and machine learning
and I get to make
them work in our space.
And so,
Dimagi is a social enterprise
that's been around
for a couple decades.
And what we do is
we build digital health tools
for use in low
to middle income countries.
And most of those tools go into
the hands of front-line workers,
but we also have some
direct-to-user cases as well.
And so,
our goal at Dimagi is to see
that LLM technologies
are spread equitably
by making them work in
native low resource languages.
And so this project was all
about fine-tuning GPT-4o mini
and GPT-4o
for health education chat bots
in those low resource
Kenyan and Malayan languages.

[00:01]
Alright, so I'm going to
introduce our use case.
This was a project funded by
the Bill and
Melinda Gates Foundation,
where we were going
to use LLMs
for family planning
in Kenya and Senegal.
Our project goal was
to evaluate the efficacy
of a conversational agent
to support behavior change
in family planning
via changing knowledge,
attitudes and self-efficacy
of young people.
This is an architecture
of our chat bot.
The user message comes in
and it hits the router LLM,
each one of these brain graph
looking icons
is a different instance of
GPT-4.
And the latter sends the message
to one of three support bots.
We have
a general conversationalist,
a quiz bot
and a roleplaying bot.
And then finally the response
is sent back to the user.
Now, one of
the major project requirements
was that it had to work
in Sheng.
So Sheng is
a Swahili-English slang,
it's match up
between Swahili and English.
Some other languages
mixed in there,
as well as some slang words.

[00:02]
And we do this
so that we can be more relatable
to the Kenyan youth.
But this is really hard. Right?
Because the LLMs are pretrained
on data that's
available to them,
and these languages are
just less available.
So. We started the project
like most people do.
We did zero-shot
and few-shot prompting.
But we found that it just
didn't produce very good Sheng.
And my native speaking teammates
say that the Swahili-English
substitutions were
really awkward.
And flow was just not
what they expected So we tried
something else
where we injected
more than 800 Sheng sentences
from some partner source
material.
Into the prompt
as a style guide.
And what we found was that,
it achieved good Sheng,
so we were pretty excited.
But that's a lot of tokens
to inject into your prompt.
And so it was really slow
and it was really costly.
And we also found out
that the Sheng quality wasn't
really robust
to the conversation history
and the prompt changes.
So, we shook it up
and did something new.

[00:03]
And this is
the updated architecture.
And everything on the left
is the same,
except for now we're telling
all the instances of GPT-4,
only respond in English.
And at the very end
we funnel it through
a new machine translation layer.
That translates from English
into our target language.
So, this adds some modularity
to the system
and there are a few benefits
that come with it.
The first is, the obvious one
where get to now isolate
our development efforts.
So now we can optimize for
our health education chat bots.
As well as for that
machine translation layer
and then look at
different languages as well.
The second advantage was
that we can now isolate
our language quality evaluation.
And that was really difficult
before,
and I'll talk a little bit more
about that in a couple slides,
because I think it's
really interesting.
And then, finally, when
you do an section fine-tuning,
one of the risks
is that the LLM become
less good at other things.
And so by keeping
our scope very narrow,
to just machine
translation layer,
for the fine-tuning we feel

[00:04]
like we don't have to worry
about that quite so much.
Machine translation layer
is really easily implemented,
just using the LLM
chat completion endpoint.
So, you're going to send
your input messages,
this is the system prompts
that I used.
You are a machine
translation bot.
Whenever the user enters text,
translate the text from English
to the target language.
Only respond to the translation.
If you can't translate the text,
just say none.
Return only the translation,
do not return
additional explanation.
So those of you who have
iterated on your prompts
are laughing.
I am as well.
One of the models
was a bit verbose
and I always wanted to explain
its translation to us.
So, then the user message
will be the text to translate.
And finally, we'll send it to
the GPT-4 chat completion point
and the assistant reply
should be the translated text.
But, now that we have a way
to implement it,
we need to know if it worked.
So that's when we get to
the evaluation part.

[00:05]
And to start you'll build
your evaluation data set,
which for us is just
a CSV file of sentence pairs.
So one columns are input,
your English sentence
and the other column
is just going to be
your ground truth translation.
And for each one
of those sentence pairs,
they're going to send
your input into your system
and generate
the candidate translation.
And now for each one
of those candidate translations
we need a way to measure
how well it's doing.
So, that enters
into the BLEU metric.
Which is a very commonly used
machine translation metric.
And I really had to resist
the urge actually
to put a math equation up here.
But I really,
but I didn't have 10 minutes
to just talk through that.
So instead I want to tell you
that,
approximately speaking,
it's a measure of
how well the tokens match
between the candidate
translation
and the ground truth
translation.
The things
that you might want to know are
that it is on the scale
from zero to 100,
with a higher score meaning
that it's a better translation.

[00:06]
And a score of about 40
is typically considered
a pretty good.
Some other tidbits
if you were tackling
this issue yourself is that,
at a sentence level,
BLEU is not very good.
It's more good
on a large data set.
BLEU is also dependent
on multiple parameters
and a tokenizer selection.
So if you're comparing
your metric between papers,
for example, you may not
be comparing the same things.
And so to get over that
to keep a standard
metric working within our team,
we adopted using
the SacreBLEU package,
it's really great,
I highly recommend it.
And it has just
some standard BLEU metrics
there ready for you to use.
So we used the FLORES-200
spBLEU metric.
Which is developed
by the Facebook AI Research Team
for the no-language
left behind initiative.
And it's sort of developed
with this purpose in mind.
So, we said that was a really
good one to get with here.
Okay. Cool.
Now we finally get to go through
some fine-tuning,
now that we've set up
our problem really well.

[00:07]
So we're going to use
instruction fine-tuning.
And instruction fine-tuning,
if you don't know, is the idea
that you're giving a model
the same instruction over
and over and over again.
And you're just trying to fit
the model to that instruction
so that it can do a good job.
And so, we're going to make
a fine-tuning data set.
We wrote some Python scripts.
And the Python scripts
simply constructs a JSONL file.
Where each line represents
the model completing
a machine translation task
for one
of those ground truth
translations.
So, I'm going to walk through it
and you're going to pretend
like each one of these columns
is a line in the JSONL file,
it's fully hard
to get all this up on a slide.
But, you'll start with these
messages that you'll send in.
So these are the messages
that you send to the system
and this is the responses
you would expect to see.
The first message is
the system prompt.
You are a machine translation
bot, dot, dot, dot.
That's going to be the same
prompt that you saw previously,
I recommend using
the same prompt
during training as an inference.

[00:08]
And then will have
the user text,
which is, you know, the
English sentence that goes in.
And finally,
the assistant reply.
Which is one of those
ground truth translations.
Cool.
So, you upload the JSONL file
and it's literally one line
of code,
if you're using the
OpenAI API Python package.
To start a fine-tuning job.
And then
if you're anything like me,
you open up the playground,
you sort of watch
your error curve go down,
because it's
extremely gratifying.
And what we found was that
fine-tuning actually improved
the Sheng translation quality
quite a bit.
So we had 1,300 domain specific
sentences translated
by the native-speaking speakers
on our team.
And we did an 85/15% split,
so left 15% of our data out
as a hold out.
And GPT-4o mini achieved
a 22.21 spBLEU score.
And then when we fine-tuned
GPT-4o mini,

[00:09]
we increased
that score to 65.23,
so it was pretty significant.
And we have just kicked
off another project funded
by the Bill and Melinda
Gates Foundation as well.
To explore this idea
in several other languages.
And so these results are
extremely preliminary,
but we've been looking
at Chihchewa,
which is a language spoken by
approximately 10 million people.
Predominantly in Malawi
and we generated 554 simple
sentences from another LLM.
From a suggestive list of topics
and had it translated
by professional translators.
So, GPT-4o mini started with
an 18.45 spBLEU score.
Fine-tuned GPT-4o mini
doubled that to 39.46.
GPT-4o, the base model,
gives 44.62,
so a little bit better.
And then, more recently,
GPT-4o become available
for fine-tuning.
So we put that one in as well
and got 47.40,
and it's doing
a little bit better.
And honestly,
at first I was a little bummed.

[00:10]
Because I'm looking at it
and I'm like, oh,
before we did
the fine-tuned GPT-4o.
GPT-4o was doing better
than the fine-tuned GPT-4o mini.
But if you think about it,
they're kind of
pretty comparable,
which is really exciting.
Because it's a 10th
of the cost inference.
On the right you see a box plot
we're also working
with translators to make sure
that the BLEU scores line
with the accuracy ratings,
so doing a little bit
of human validation.
And we've also been having
quite a bit of luck
looking into
open source data sets
and leveraging those
for both our evaluation
and for training.
And so you can check those out
there if you would like.
Thank you very much,
both you and my team.
[ Applause ]

</details>
