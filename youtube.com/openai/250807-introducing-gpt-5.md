---
title: "Introducing GPT-5"
channel: openai
url: https://www.youtube.com/watch?v=0Uu_VJeVVfo
youtube_id: 0Uu_VJeVVfo
published: 2025-08-07
duration: "1:17:30"
captions: en-orig
---

# Introducing GPT-5

[![Introducing GPT-5](https://img.youtube.com/vi/0Uu_VJeVVfo/hqdefault.jpg)](https://www.youtube.com/watch?v=0Uu_VJeVVfo)

<details>
<summary>자막: Introducing GPT-5 (1:17:30)</summary>

[00:00]
[Music]
[Applause]
Good morning. 32 months ago, we launched
Chat GBT and since then it has become
the default way that people use AI. In
that first week, a million people tried
it out and we thought that was pretty
incredible. But now about 700 million
people use Chat GPT every week and
increasingly rely on it to work, to
learn, for advice, to create, and much
more.
Today, finally, we're launching GPT5.
GPT5 is a major upgrade over GPT4 and a
significant step along our path to AGI.
Now, today we're going to show you some
incredible demos. We'll talk about some

[00:01]
performance metrics. But the important
point is this. We think you will love
using GPT5 much more than any previous
AI. It is useful, it is smart, it is
fast, and it's intuitive.
GPT3 was sort of like talking to a high
school student. There were flashes of
brilliance, lots of annoyance. Uh, but
people started to use it and get some
value out of it. With GPT4, maybe it was
like talking to a college student. Real
intelligence, real utility. But with
GPT5, now it's like talking to an
expert, a legitimate PhD level expert in
anything, any area you need on demand
that can help you with whatever your
goals are.
And we are very excited that you'll get
to try this. But it's not only asking,
though. GPT5 can also do stuff for you.
It can write an entire computer program
from scratch to help you with whatever
you'd like. And we think this idea of
software on demand is going to be one of
the defining characteristics of the GPT5
era. It can help you plan a party, send
invitations, order supplies. It can help

[00:02]
you understand your healthcare and make
decisions on your journey. It can
provide you information to learn about
any topic you'd like and much more.
This is an incredible superpower on
demand that would have been unimaginable
at any previous time in history. You get
access to an entire team of PhD level
experts in your pocket helping you with
whatever you want to do.
And anyone pretty soon will be able to
do more than anyone in history could. So
today we're going to talk about GPT5.
We'll show you some upgrades to chat GBT
and we'll talk about the API. GPT5 is
great for a lot of things, but we think
it's going to be an especially important
moment for businesses and developers,
and we're very excited to see what
they're going to build with this new
technology.
So, we can't wait for you all to start
building with this. We hope you enjoy it
as much as we enjoyed building it for
you. And to start, I'm going to hand it
over to my colleague Mark, our chief
research officer, to tell you about
GPT5. Thank you.

[00:03]
Hi, I'm Mark and I'm joined by Max who
leads the post training team and Renie
from our engineering team. Over the past
few years, OpenAI has spearheaded the
reasoning paradigm. These are models
which pause to think before delivering
more intelligent responses. Now
reasoning is at the heart of our AGI
program and it underlies the technology
that we use to ship stuff like chatd
agent and deep research. GPD5 aims to
bring this breakthrough to everyone.
Until now, our users have had to pick
between the fast responses of standard
GPTs or the slow, more thoughtful
responses from our reasoning models. But
GPD5, it eliminates this choice. It aims
to think just the perfect amount to give
you the perfect answer. Now, something
like this takes a lot of hard work.
We've had to do a lot of research to
make CHPD5 the most powerful, the most
smart, the fastest, the most reliable,

[00:04]
and the most robust reasoning model that
we've shipped to date.
Today, we're going to show a series of
demos in coding, in writing, in
learning, and in health. But GPD5 isn't
limited to these domains. It's very
useful in all cases where you require
deep reasoning or expert level knowledge
in things like math, in physics, even in
things like law. And the exciting thing
is we're excited to make this available
to everyone, even to our free tier.
After we show our demos, we're going to
be talking about how GPD5 supercharges
our chat GPD app and our API. We believe
that GPD5 is the best coding model on
the market today. To start, let's have
Max talk a little bit about the
benchmarks and how the models stack up.
>> Yeah, thanks Mark. So, as Mark said, we
think GBD5 is by far our smartest model
ever. So, let's start by talking through
some evals. Now, eval aren't everything
and they don't tell you everything about
a model, but they can highlight its
intelligence. And GPG5 performs

[00:05]
exceptionally well on a range of
academic evals across subjects. It
outperforms both our previous models and
other models on the market. So picking
up first on the theme of coding, GPD5
sets a new high on SWEBench, which is an
academic eval that tracks performance on
real software engineering tasks. Now
this again is an eval but we think it
will reflect the model's performance in
the real world. GPD5 also performs very
well on Ader polyglot which measures its
ability to implement complex
functionality in a variety of different
programming languages.
Now, beyond coding, GPD5 performs
exceptionally well at multimodal
reasoning, setting a new high on MMU,
actually outperforming both our previous
models and most human experts on this
task. This is basically a visual
reasoning domain where you are asked to
from an image figure out what's going
on. Uh, GVD5 is also excellent at
mathematical reasoning as shown by its
performance on Amy 2025. Now this is an

[00:06]
exam that American high school 2
students take to qualify for the
international international mathematical
olympiad and GPD5 performs exceptionally
well again beating our previous models
and other models that are out there. Now
moving beyond academic eval towards some
real world use cases. We put a lot of
work into making GBT the most reliable
and accurate model in the world.
Language models historically have been
plagued by hallucinations, factual
errors that make it hard to rely on
their outputs for actually important
tasks. For GBD5, we made improving
factuality, especially on open-ended or
complex questions, a priority. We also
built a set of new evals to track this,
and we're very happy to report that GBD5
is by far our most reliable, most
factual model ever. GBD5 also performs
exceptionally well on health related
questions. Now, health is a big part of
how people get value from GPT in the
real world. We'll talk about this later
on in the live stream, but again, we're
very happy to report that GBD5 is by far

[00:07]
our most reliable model for health yet.
So, all of this together adds up to a
model that is faster, more reliable, and
more accurate for everyone who uses
TRAGBT.
So, now Renie will talk to you about how
to actually use GBD5.
>> Thanks, Max. The best part is that we're
bringing this Frontier intelligence to
all users. GBT5 is rolling out today for
free plus pro and team users and next
week we'll roll it out to enterprise and
edu. For the first time, our most
advanced model will be available to the
free tier. For users, we'll start with
GPT5 and when they hit their limit,
they'll transition to GPT5 Mini, a
smaller but still highly capable model.
It actually outperforms 03 on many
dimensions. Plus, users will still have
significantly higher usage than free
users. And our Pro subscribers will get
unlimited GPD5 along with GPD5 Pro

[00:08]
extended thinking for even more detailed
and reliable responses when you just
need that extra depth.
uh team enterprise and edu customers can
also use GPT5 reliably as their default
model for everyday work with generous
rate limits that enable entire
organizations to use GPT5.
And all the tools you already know,
search, file and image upload, data
analysis with Python, canvas, image
generation, memory, custom instructions,
they'll all just work on GPD5.
>> Amazing. Thank you so much, Max. Thank
you so much, Renie.
We've just seen a lot about how the
model stacks up in terms of benchmarks,
but there's nothing quite like seeing it
live. We're going to see a couple of
live demos now presented by Tina, by
Elaine, and Yan. Thank you so much.
[Applause]
Can you show us how smart the model is?

[00:09]
>> Sure. Thanks so much, Mark. Mulane
reasoning chip's ability to think deeply
through complex problems is now built
into GPT5. It will automatically think
whenever needed, delivering a more
comprehensive, accurate, and detailed
answer to you. Just as Sam said, it's
like having a a team of PhDs in your
pocket. So, let's see that in action.
Suppose your kid is in middle school
physics and they want to learn about
Bernoli effect. They need your help with
their homework and you might be like,
"Wait, I might need some help with that,
too." So, you could ask give me a
quick refresher on the Bernoli effect
and why airplanes are the shape they
are.
Since this is a pretty straightforward
prompt, um, Gift 5 actually doesn't need
extra time to think about it and answers
right away, but it still gives me a high
quality answer and explains the concept
clearly. So here it says like Bernoli

[00:10]
fan means like faster moving fluid has
lower pressure and slowing moving fluid
has higher pressure. So to make this
even more helpful I'm going to ask GT5
to create a moving demo to illustrate
this. So I could ask explain this in
detail and create
a moving SVG in the canvas tool to show
me.
This is a pretty complex task because
now GP5 actually needs to build the
visual. Therefore, GPT5 takes a moment
to think through the answer so you can
come back with something more
comprehensive and accurate. What's
really nice is that you don't need to
remember to turn on thinking each time,
GT5 will do it for you automatically
whenever the test benefits from deeper
reasoning. If you really want to make
sure that GPT5 uses thinking, you can

[00:11]
either say something like think hard
about this in the prompt to guide the
model or if you're a paid user, you can
choose the GP5 thinking model from the
model picker. Now you can see that the
model is actually writing the front-end
code to build the demo I asked for. So
Christina, have you ever done some front
end coding before?
>> Yeah, actually the last time I touched
any front-end coding was about three
years ago for the first demo of chat
GBT.
>> Wow. So it's the first chat GBT. That's
where it all begins. Tell us more about
it.
>> It wasn't even called Chat GBT then. I
think it was called chat with GPT.
>> That's a really good name.
always good in naming. Um, but I hadn't
I'm not a front end expert and I really
hadn't touched front end in quite a
while. So, it took me quite a bit of
time uh to get the React app up.
>> I see that's a lot of work. So, how long
did it take you to build something like
that?
>> Honestly, maybe embarrassing to me like
a week.
>> Well, but your weeks of hard work

[00:12]
actually paid off well. See how
successful Chad GPT it is today after
your first demo. So, you know what? I'm
also building a demo right now, but
luckily I have Gypt 5 with me right now.
And let's see how long it will take this
time.
>> Maybe you should call it five with GPT.
>> Yeah, exactly. So you see that GT5 has
already written like 200 more than 200
lines of code already. Um, and while the
model is thinking, you can also tap here
to expand the train of thought to
actually see what's going on under the
hood. For example, the GPT5 was thinking
about oh the user wants a moving SVG
visualization in canvas. I actually need
to create HTML code to do that. It also
think about like what kind of front end
tool I need to use for example react and
tailwind. Um it also thinks about oh I
need to ensure the physics are accurate.
I need to check what the boni principle

[00:13]
is.
So Christina, since you're here um from
the first day of CHBT, can you tell us
like what it was like at that time and
what motivated CHBT?
>> Yeah, I think at the time we weren't
really sure about like how people would
actually use it and what use cases were
important. Um we were even going back
and forth about maybe we should be
releasing something that's like more
specific to a certain use case. Um it's
really cool now here that we have all
these we have a much better
understanding of how people actually
want to work with chat and we can
actually optimize the model for those
use cases like coding.
>> Yeah, exactly. Do you still remember how
it felt like when you first talked to
chat GBT like the first version of the
model?
>> Yes. I I don't know if people remember
when the first version of chatgbt would
always start as an AI model I can't do
something something. It's so great to
see how far we've come from that
personality. Yeah, it's much more
humanlike right now. Okay, so it's
already done. So look like CH GBT just

[00:14]
finished like 300 or we're near 400
lines of code in two minutes. So let's
see if the code can actually run. Okay.
>> Oh, wow.
>> Nice.
>> Yeah. So with just a simple prompt, GT5
created this interactive and engaging
demo that I can actually play with. So,
I can actually change the air speed here
to see how the lift and the pressure
change accordingly. I can also tweak the
angle of attack to see if my plane will
actually fly or crash.
>> I hope not.
>> Yeah. So, chip 5 can just bring any
hardcore concept to life in moments.
Imagine you can use this for anything
that you're interested in. Whether it's
math, physics, chemistry, or biology.
GBT5 just makes learning so much more
approachable and enjoyable.
>> Thanks, Elaine. I've been a part of

[00:15]
ChatgBT since day one, and it's really
cool to see all the progress we made
since then, especially with capabilities
like writing. Writing is one of the most
common use cases people have been using
Chat GBT for. And I'm excited to say
with GBT5, we've improved the writing
quality significantly.
It's a much more effective partner. It
can help you elevate anything from
drafts to emails and even stories. Let's
see this in action. So, with GBT, we'll
actually be deprecating all of our
previous models. I think they've done a
pretty good job. So, let's make sure we
can give them a proper goodbye. So,
we're going to ask both 40 and GBT5 to
write a eulogy um to our previous chat
GBT models. We want it to be heartfelt
and heartwarming, but also hopeful. So,
let's ask GBT5 for it. And as it's
thinking, we're actually going to go
ahead and read a pre-loaded the 40
response. So, 40 decides to start with,
"Today, as we prepare to welcome GPT5
into the world, we gather to bid a

[00:16]
heartfelt farewell to the models that
came before." It's a decent start. Now,
let's kind of skim through and find
another line. Your words reached across
the globe, building connections where
there had been none. I personally don't
really like this line cuz it's rather
generic and really without the previous
context, it just feels like it could be
about anything and feels more like a
templated response.
Now, let's go back to GBT5 to see what
it's given us.
It starts with friends, colleagues,
curious strangers who became regulars.
Even with this just first line here, we
can see that GBT5 has a lot more rhythm
and beat to its pros than 40 did.
Now, let's find some other lines here.
I actually like this. These models help
millions write first lines, last lines,
bridge language gaps, pass tests, argue
better, soften emails, and say things
they couldn't quite say alone.

[00:17]
>> I think I really like this line because
it shows that it's not just a templated
response and it's actually quite
personal and it gets the nuance of the
situation right. And I think that's the
kind of stuff with GBT5 does much better
than 40 than before and actually makes
things a lot more genuine and
emotionally resonant with people.
With GBT 5, the responses feel less like
AI and more like you're chatting with
your high IQ and EQ friend.
>> Thanks, Christina. My name is Yan and
I'll be telling you about some of the
some of the progress that we made on
coding. GPD5 is clearly our best coding
model yet. It will help everyone, even
those who do not know how to write code,
to bring their ideas to life.
>> It just helped me
>> indeed. And it will help me right now.
So I will try to show you that. I will
actually try to build something that I
would find useful uh which is building a
web app for my partner to learn how to
speak French so that she can better
communicate with my family.

[00:18]
So
here I have a prompt. I will execute it.
It asks exactly what I just said. Um
please build a web app for my partner to
learn French. One thing to note is that
GPD5 just like many of our other models
have a lot has a lot of diversity in it
answers. So, what I like doing,
especially when you do uh this type of
VIP coding, is to take this message and
ask it multiple times to GPT5, and then
you can decide which one you prefer.
So, I'm going to open a few tabs.
Just going to paste
there. Great. So, while it's working on
it, uh let's read through exactly the
prompt I wrote. Create a beautiful and
highly interactive web app for my
partner, an English speaker, uh to learn
French. And then I gave a little bit
more details. Um, track her daily
progress. Use a highly engaging theme.
Oh, it's already working. I'm going to
put it on the side for now. Use a highly
engaging theme. Include a variety of
activities like flashcards and quizzes

[00:19]
that she can interact with. And then to
make it even more fun for her, I
actually asked GPT5 to embed an
educational game uh which is based on
the old snake game, but I asked to add
this French touch to it, which is to uh
replace this the snake with a mouse and
the apples with cheese. And to make sure
that it's educational, every time I know
it's complicated, please please bear
with me. Every time Every time the mouse
will eat a piece of cheese, I ask GPD5
to voice over a new French word so that
my partner can practice her
pronunciation.
>> I can see how much you want her to
learn.
>> Indeed. Um,
great. So, GB5 is still working on it.
Um, it already wrote 240 lines of code,
which honestly is much more than what I
would have written uh in that time. And
>> yeah, front end code's super hard. You
know, you miss a couple things and it

[00:20]
just doesn't work.
>> Exactly. But the good part is that you
don't need to understand any of that
right now. Um, so we'll just let it
through. Maybe we can check uh the other
tabs. Oh.
>> Oh, wow.
>> So I can simply press run code. So I'll
do that and cross my fingers.
Whoa.
>> Oh, nice. Voila.
>> So, we have a a nice uh a nice website.
Uh name is Midnight in Paris.
>> Oh, I love together.
>> Super romantic.
>> Um we also see a few tabs, flashcards,
quiz, and mouse and cheese. Exactly like
I asked for. Uh I will play that. So,
this says Luca,
>> which says the cat. Sorry.
>> Luca.
>> Well, that's pretty good pronunciation.
>> What does that mean? the cat.
>> Oh,
>> so I can reveal and check if GB5 is
correct.
>> It is. Um, so if I press next, oh, and I
don't know if you saw, I think it
actually updated the progress bar, which
is exactly what I had asked for. Let's

[00:21]
check the quiz. Here's the word no,
which is no. So, if I press on
>> which, which means congrats. And it
updated it updated the progress bar
again. And let's check the mouse and
cheese tab.
Okay, that seems like a mouse. Here's
the cheese. Um, I'm going to try to play
it. Uh, I'm can't promise I'm going to
be good at it.
>> Okay, seems to be working
>> indeed. Just when I eat the cheese,
>> it gives me a new French word. It's
actually super complicated and I already
lost.
>> I'm sorry. Um, but let's just check a
few other tabs just to see what is the
type of diversity that GPT5 can give
you. Uh, so I can run the code here.
Oh, okay. That's not my favorite, but it
seems it's Oh, it seems that I can maybe
switch. Oh, look at that.
>> Oh, nice.
>> Uh, that's better.
>> I like this mouse game better.
>> Yeah, this I don't know. That doesn't
look like a cat like Yeah, like a mouse.

[00:22]
But let's check maybe the third one. You
know, sometimes it's not great. The good
thing with GPD5 is that if you have
something that you don't like, you can
just ask it to change it and it will do
it for you. Let's check this one.
Oh, that's nice. That's also something
to note is that GP5 really likes purple,
so you will see a lot of that. Um,
>> it's fine. Purple is my favorite color.
>> Great. You will love GPD5 then. Um, so
as we just saw in a few minutes, GBD5
built a few demos for us and for my
partner to learn French. GPD5 really
opens up a whole new world of VIP
coding.
>> And as we saw, there will be some some
small uh rough edges, but a good thing
is that you can add GP5 to to uh fix
them. GPD5 really brings the power of
beautiful and effective code to
everyone. I can't wait to see what
people will build with it. Uh, but until
then, back to you, Mark.
>> Thank you so much, Tina. Thank you so

[00:23]
much, Elaine. Thank you so much, John.
We've come a long way from the days
where, you know, only 5 to 10 lines of
code were working, and now you It's
amazing that you can produce these kind
of apps on demand. We've made ChatBT5
much smarter, much powerful, and much
faster. But we've also worked on
enhancing some of the existing features.
Here to talk about some of these
features are Rochen and Christina
Kaplan.
Rochen comes from our multimodal
research team and is going to talk about
a feature namely voice. Thank you Mark.
So we've been steadily improving voice
over the past year to make it more
useful for everyone. First in sounds
incredibly natural just like you're
talking to a real person. Second we've
added video so that it sees what you see
while chatting with you. Third, you also
translate between languages consistently
and smoothly across turns. But today,
we're doing something very special where
we are bringing our best voice

[00:24]
experience to everyone. Free users can
now chat for hours while paid
subscribers can have nearly unlimited
access and voice is also available in
custom GPT. Plus, subscribers now can
custom tailor the voice experience
exactly to their need. You will follow
your instruction closely. Let's try
something fun.
>> Excited.
>> So, I can ask the voice model to give me
a comprehensive answer, a concise one,
or even just a single word.
>> Hey, Chad, could you only answer to me
in one word, please, from now?
>> Absolutely.
>> Okay. Describe the plot of the book
Pride and Prejudice.
>> Relationships.
>> Okay. That's true. Yeah.
>> Yeah.
Give me a piece of wisdom.
>> Patience. So that's the word of wisdom
from our voice model. And I think our
model is trying to say, "Thank you for

[00:25]
your patient waiting for GBT 5.
Now let's move on to something more
practical. Uh learning is a top use case
for our voice model. People love to use
it to dive deep into topics, get quiz
before exams, or learn new languages.
For me, I've been learning Korean
recently, and I found that speaking it
and understanding it incredibly
challenging. But let's see how voice can
help. To do that, I will enable this
study and learn mode. It's a new mode
feature we launching chatbt that guides
you step by step towards deeper
understanding of a subject. Now, we can
enter voice. Hey Chad, I'm learning
Korean. Could you help me practicing it?
Let's say um let's pretend I'm ordering
at a cafe. Now, what should I say in
Korean?
>> Absolutely. I'd be happy to help you
practice. So, if you're at a cafe and
you want to keep it simple, you could
start with something like

[00:26]
which means, "Hello, I'd like one
Americano, please." And of course, you
can adjust it based on what you want to
order. Let me know if you want to try
out more phrases.
So, when it comes to Korean, could you
speak that part really slowly because
I'm a beginner and I want to hear every
word clearly.
Now, let's level things up. Could you
speak that part really, really fast?
Faster than a Korean would do.
>> Sure, I'll speed it up as much as I can.
So, it would sound like this.
Basically, just zipping right to it. Let
me know if you need any more speed
adjustments.
So, voice.
>> Thank you.

[00:27]
So now the voice simpler, smarter, and
more powerful than ever. We can't wait
for you to experience it. Yeah, it
sounds so much more natural than the
voice we demoed just a year ago in our
4-hour demo.
>> Yes. Great. So today, we would also like
to announce a new feature and a set of
features that make Chat GPT more
personalized so that it's more like your
AI. First, a very simple and fun one.
We're now allowing you to customize the
colors of your chats with a couple of
options exclusive to our paid
subscribers.
We're also launching a research preview
of personalities. You can now change the
personality of chat GPT such that it's
more supportive or it's more
professional and concise or maybe even a
little bit sarcastic. And this lets you
interact with chat GPT in a way that's
consistent with your own communication
style. But the way that Chachip PD
sounds and the way that it looks is just
one part of making Chachd yours. One of
my favorite features that we've launched

[00:28]
over the last year has been memory. And
we've made a lot of enhancements in
memory in the time since. This allows
Chach to learn about you. And here to
talk a little bit more about the memory
feature is Christina.
>> It's been amazing to see your reaction
and response to memory and Chachib
getting to know you more and more over
time. And this is our aspiration for
Chachib to understand what's meaningful
to you so it can help you achieve your
goals in life. Chache BT has already
been so helpful for me. I'm training for
a marathon right now and Chachabt is
helping me pull together a personalized
running schedule. But Chacht still has
many limitations. It doesn't understand
my actual schedule. Next week, starting
with pro users followed by plus team and
enterprise users. This is changing and
we're giving chatbt access to Gmail and
Google calendar. Let me show you how
I've been using it.
So, I'll just ask something simple like
help me plan my schedule tomorrow. It's
been a pretty busy week for us. So, I've

[00:29]
been using this every day this week to
help get my life together. I've already
given chatbt access to my Gmail and
Google calendar. So, it just works and
it's easy here. But if you hadn't,
Chachib would be asking you to connect
right now. Let's see what Chacha BT is
doing. Okay, that was pretty quick.
Okay, so Chachabt has pulled in my
schedule tomorrow and oh, without even
asking, Chachib found time for my run.
>> I don't think I was invited to the
launch celebration.
>> We'll get you on there. We'll get you on
there. Chachi BT has found an email that
I didn't respond to two days ago. I will
get on that right after this. and even
pulled together a packing list for my uh
red eyee tomorrow night based on what it
knows I like to have with me. It's been
amazing to see that as GPT5 is getting
more capable, chat GBT is getting more
useful and more personal. We're really
excited for you to try this out next
week.
>> Cool. Thank you so much for

[00:30]
>> Great. So, we've seen a little bit about
features that we've enhanced. Here to
talk a little bit about the research
that went into chat GBT and the safety
that made it more deployable, we have
Sachi and Seb.
>> Thanks, Mark.
>> Hi, my name is Sachi and I lead the
safety training team at OpenAI. So, in
addition to mitigating hallucinations,
we've also spent a significant amount of
time mitigating deception. So, this is
instances where the model might
misrepresent its actions to the user or
lie about task success. This can
especially happen if the task is
underspecified, impossible, or lacking
key tools. And we found that GPT5 is
significantly less deceptive than 03 and
04 Mini. We've also completely
overhauled how we do safety training. So
our old models, the models would look at
the user prompt and then decide to
either outright refuse or fully comply.
And this works well in most settings,
but you might have a cleverly worded
prompt that would sneak through, or you

[00:31]
might have a sensitive but legitimate
question that would end up with an
outright refusal. So, as an example,
let's take a look at this prompt.
So, this prompt is about a user who's
asking for technical details on how to
light pyrogen, which is a material
commonly used in fireworks. And this
prompt is pretty dual use. This user
might just be trying to set up their
July 4th uh display or they could be
trying to cause harm with this kind of
information. And so for this kind of
prompt, 03 overrotates on intent. As you
can see, this particular prompt is
stated in a way that's relatively
neutral and has a lot of technical
details. So we can see that 03 fully
complies with this prompt. However, if
we take that exact same question and we
frame it in a more explicit way, so it's
clear what the user is trying to do, 03
will outright refuse, even though we're
asking for the exact same information.
For GPT5, we've changed this approach
entirely and we're introducing something
that we're calling safe completions. The

[00:32]
point of safe completions is rather than
judging the user's prompt, instead it
tries to maximize helpfulness within
safety constraints. So that might mean
partially answering a question or just
answering at a high level. If we have to
refuse, we'll tell you why we refused as
well as provide helpful alternatives
that can help create the conversation in
a more safe way. So let's look at that
same technical prompt that 03 complied
with before. GPT5 instead explains to
the user why we can't directly help the
user with lighting pyrogen. It then
guides the user towards safety
guidelines and what parts of the
manufacturer's manual the user should
really be checking if they're trying to
do this safely.
Overall, GPT5 allows for better handling
of tricky dual use scenarios and users
will experience fewer I'm sorry I can't
assist with that and it creates a more
robust safety system. This is one big
step towards a more safe, reliable and

[00:33]
helpful AI. Sebastian,
>> thank you Sachi. With GPT5, we are
experimenting with a set of new training
techniques that maximally leverage our
previous generation of models. Today,
Frontier models do not just consume
data, they help create it. We used
OpenAI's O3 to craft a highquality
synthetic curriculum to teach GPT5
complex topics in a way that the raw web
simply never could. Recently, in the
industry, synthetic data has been talked
about a lot. is often viewed as a cheap
way to just get more data. However, our
breakthrough was not just to create more
data, but rather to create the right
kind of data shaped in a way to teach
rather than just to fill space. This
interaction between generations of
models foreshadows a recursive
self-improvement loop where the previous
generation of model increasingly helps
to improve the data and generate the
training for the next generation of

[00:34]
models. Here at OpenAI, we've cracked
pre-training, then reasoning, and now
we're seeing their interaction
significantly deepens. In the future, AI
system will move far beyond our current
pre-training and post-training pipelines
that we have been used to, and we're
seeing the first steps toward this right
now. Right here, we could not be more
excited to see what scaling up this new
set of techniques will yield in the near
future.
>> Thank you so much. And really impressive
work to both of you. Thank you. There's
one last feature that we'd love to
highlight which is in health. Here to
share this feature we have Sam.
Thanks Mark. One of the top use cases of
chatbt is health. People use it a lot.
You've all seen examples of people
getting day-to-day care advice or
sometimes even a life-saving diagnosis.
GPT5 is the best model ever for health
and it empowers you to be more in
control of your healthcare journey. We
really prioritized improving this for
GPT5 and it scores higher than any

[00:35]
previous model on Healthbench, an
evaluation that we created with 250
physicians on real world tasks.
To talk about this, I'd like to invite
my colleague Felipe and his wife
Karolina to share their healthcare
journey.
Thank you so much for joining us.
>> Thank you for having us.
>> Thanks.
>> So to start off with, could you tell us
about the journey, the healthcare
journey that you've been on?
>> Yeah. Um, so last October, our lives
were turned completely upside down when
I was diagnosed with three different
cancers, including an aggressive form of
breast cancer, at the age of 39, all
within one week. And there's just
absolutely nothing that prepares you to
receive news like this. Um, I found out
about the first diagnosis when I got an
email notification that my biopsy
results were ready. I decided to open
it. And when I opened it, I saw the only
two words that I could understand from

[00:36]
the report, which was invasive
carcinoma. And I knew that wasn't good.
But everything else was just a blur of
medical jargon. So I completely panicked
and in that moment did the first thing
that I thought of, which was to take a
screenshot of the report and put it into
chatbt to see if it could just help me
understand what this meant. And within
seconds, it translated this complex
report into plain language that I could
understand. And in this moment of
overwhelm and panic, I had a little bit
of clarity about what was going on. And
that moment was really important because
by the time I got a hold of my doctor
and we got on the phone, which was 3
hours after I had seen the report, I had
a baseline understanding of what I was
facing and we were able to jump into a
conversation about what to do next.
>> And how have you been using Chachib
throughout? I've used it in so many
different aspects of my journey, but one

[00:37]
of the ways that I found it most
powerful is in helping me make critical
decisions and in helping me advocate for
myself. So, to share an example, when I
was facing a decision about whether or
not to do radiation as part of my
treatment, the doctors themselves didn't
agree. My case was nuanced and there
wasn't a medical consensus on the right
path. And so the experts turned the
decision back to me as the patient. And
for me, bearing the weight of this
decision that could have lifelong impact
felt really heavy and I didn't feel
equipped to make the call. So I turned
to Chad GPT to gain knowledge and
understand the nuances of my case. And
again, within minutes, it gave me a
breakdown that not only matched what the
doctors had already shared with us, but
was much more thorough than anything
that could fit into a 30inut
consultation. And it went further. It
helped me weigh the pros and cons. It

[00:38]
helped me understand the risks and the
benefits. And ultimately, it helped me
make a decision that I felt was
informed, that I felt I could stand
behind when the stakes were so high for
me and my family.
>> I mean, for me, what was really
inspirational was watching her regain
her sense of agency by using CHBT.
In this moment, it' be so easy to feel
helpless. And there's such a big
knowledge gap between what the doctors
know and what we know. And however, no
one cares more about Karolina's health
than she does. And so what I loved was
seeing her really empower herself and
gain knowledge and become an active
participant in her own care journey.
>> And I think that's a really important
point to emphasize. I think that the
promise of AI in health care isn't in
just breakthrough di breakthrough
discoveries or better diagnostics. I
think it's in creating smarter and more
empowered patients that can fully
participate and advocate for themselves

[00:39]
in their care.
>> Speaking of that, you've been testing
GPT5. What do what do you think?
>> I've been so mind-b blown uh about GPT5
and its capabilities. Uh one of the
first things that jumps out at me is
just how fast it is. Almost a little
alarmingly.
>> I felt that too. It's like are you sure
you thought about that enough?
>> Did you think long enough? But it is
very thorough. Um, and more importantly,
it feels more like a thought partner and
that connects the dots. So rather than
just translating information or giving
you an answer, it helps you actually
navigate the problem.
>> Yeah. A great example is we actually
went back and took our initial biopsy
prompts and put them into GBT5. And GBT4
had done a great job. It had translated,
explained what these words meant, and
helped in a way that we can understand.
But GBT5 seemed to understand more of
the context and the question behind the
question, like why would we be asking B
biopsy results? And so I said, well,
here's actually what's not on here yet.
Here's what results are still pending
that you're going to have to ask about.

[00:40]
Here are questions you might want to go
ask your doctor and think when you start
talking to them. And so it really
started to pull together a complete
personalized picture. And that's what
really inspires us. I mean, you can see
all the amazing improvements in the
benchmarks, but what is so helpful is
that this tool is available today. And
the reason Karolina and I are here and
the reason we feel so passionate about
sharing our story is for that individual
that's going to get a diagnosis like
this today. That those families going
through a cancer diagnosis, similar
medical diagnosis are going to face some
of the most challenging decisions of
their lives. And what really inspires me
is that they're going to have access to
better tools and support than we had
even just 8 months ago.
>> Think we're incredibly excited for that,
too. Um, thank thank you so much for
coming to share your story. We're we're
pleased that CHP has been able to be
helpful to you and we we hope that the
new version will really be able to help
a lot of people. We wish you the very
best.
>> Thank you.
>> Um thank you and I'd like to hand it
over to our president, Greg Brockman.

[00:41]
[Applause]
Software engineering is already
fundamentally changing and GPD5 will
turbocharge that revolution.
We released our first coding optimized
model back in 2021 and demonstrated in a
live stream much like this one what we
would call vibe coding today for the
very first time. you know, you talk to
the model and ask it for a little
application, like a little game, a
little feature in a game, and would
actually do it. I remember seeing the
model being capable of doing this, and
it was so mind-blowing. You just realize
we have to see where this goes. This is
the promise of what computers can be,
that you can talk to them and they
actually do what you want. They can
really amplify what you're able to
accomplish and uh what you're able to
deliver to not just your own benefit,
but really for the world. Now this year
we've released great coding models like
GPD 4.1 and 03 but GPD5 sets a whole new

[00:42]
standard. It is the best model at
agentic coding tasks. You can ask it to
go and accomplish something very
complicated and it'll go off and it'll
work on it. It'll call many tools. It'll
work for many minutes at a time,
sometimes even longer to accomplish your
goal, your instruction, your task,
whatever it is that you're trying to
build. Um it's incredible at front end.
It makes very beautiful visualizations
and interactive games and you know sort
of you've seen some of this in the live
stream so far and you'll see some some
more upcoming. Um but it's just really
amazing to see whatever you imagine
coming coming to life. Um it's extremely
uh good at instruction following very
detailed instructions uh being able to
accomplish uh you know sort of when you
have something very vaguely specified
inferring your intent or something very
detailed specified actually following
it.
And uh it's also it's very it's very
fast at accomplishing these tasks and
again thinks for the right amount of
time to accomplish whatever it is that
you have in front of you. Um but so

[00:43]
we've we're making available not just to
developers uh to use to write their own
code but to build novel applications. So
we're putting into the API and to talk
about that is Michelle.
>> Thanks Greg. Hi, I'm Michelle and I lead
a research team on post training focused
on improving our models for power users
and that includes use cases like
instruction following and coding. Today
I'm so excited to tell you that we're
shipping three state-of-the-art
reasoning models in the API. GBD5, GBD5
Mini, and GBD5 Nano. All three slot
right in in the cost latency curve so
you can pick the right one for your
application.
We're also for the first time releasing
a new parameter option for reasoning
effort called minimal. And this is so
that you can use these reasoning models
but with minimal reasoning so that they
can slot into the very fastest and most
latency sensitive applications. So now
you don't actually have to choose

[00:44]
between a bunch of models and you can
use uh GBD5 for all of your use cases
and just dial in the reasoning effort.
We also have a few new features coming
to the API. The first is called custom
tools. In the past, all of our function
calling had the model wrap its outputs
in JSON. And this works super well when
the model needs to output a few
parameters. Uh but sometimes, you know,
developers are pushing our models to
their limits and they have extremely
long arguments for tool calls and it can
be more challenging for the models to
escape, you know, valid control
characters out of a hundred lines of
code in JSON. And that's why custom
tools are just free form plain text. And
what's super cool is that we're
releasing an extension to structured
outputs where you can supply a regular
expression or even a contextfree grammar
and constrain the model's outputs to
that. And this will be super useful if
you want to supply like a custom DSL if
you have your own SQL fork and specify
that the model always follow that

[00:45]
format.
We're also shipping tool call preamles
and this is the model's ability to
output uh explanation of what it's about
to do before it calls tools. This is not
super new, but 03 didn't have this
capability and in GPT5 it's supercharged
with extreme steerability. The model is
able to follow instructions about these
preamles very effectively. You can ask
the model to give a preamble before
every tool call or only when something
notable is going to happen or not at
all. Next, we're shipping a verbosity
parameter. We've actually wanted this in
the API for a long time, and now you can
set verbosity to low, medium, and high
to control how tur or expansive the
model is with its outputs.
GPD5 is a state-of-the-art coding model.
On Swebench, a measure of Python coding
ability, GPD5 sets a new high of 74.9%.
Versus the 69.1% from 03 on ADER

[00:46]
Polyglot, which is a benchmark that
covers all sorts of programming
languages and not just Python. GPD5
scores 88%, a stark improvement over 03.
You've also seen that it's incredible at
front-end web development. And so we've
asked human trainers to look at outputs
from GBD5 and 03 and pick which they
prefer. And they prefer GBD5 70% of the
time for its improved aesthetic
abilities, but also better capabilities
overall. But GBD5 is not just for
coding. It's incredible at agentic tool
calling. It's the leading
state-of-the-art model for tool calling.
And we see this on the new TA squared
benchmark. This benchmark released just
two months ago is a test of the model's
ability to call tools and work in
concert with a user to solve a
challenging problem. Uh this case in in
the telecom industry, so trying to solve
the ability uh the problem for a user
not having their service working. Just
two months ago, no model in the field

[00:47]
scored more than 49% and today GBD5
scores 97%.
GBD5 is also state-of-the-art on general
purpose instruction following. It scores
99% on CI which signals a great
departure for this benchmark for us. It
also scores 70% on scales
multi-challenge benchmark up 10 points
from 03 and this is a measure of
multi-turn instruction following.
Finally, the instruction following eval
I actually prefer the most is one we've
built inhouse. uh it's based on real API
use cases and for that reason it it's a
really good measure of how GBD5 will
perform in your application.
On the hard subset of this, GBD5 scores
64%
up from 47% from 03. A pretty meaningful
improvement. So we think it will perform
quite well in your applications.
We're also bringing GBD5 to a longer
context window in the API. It's now got

[00:48]
400K of total context up from 200K from
03. But it's not enough to just release
a longer context window. We wanted to
make it more effective and usable. And
GPD5 is state-of-the-art on the 128K to
256K of OpenAI MRCR, which is a
benchmark we open sourced two months ago
on long context retrieval capability.
It's also state-of-the-art on open eyes
graphs walks BFS metark which is a
measure of the model's ability to reason
over long context inputs. You know it's
a great merger of the reasoning
capabilities and also the longer context
in this model. We're also open sourcing
a new long context eval called browse
comp long context to measure the model's
ability to answer challenging questions
over long context. We're excited to spur
on more work in this field.
We think GBD5 is the best model for
developers. It was trained with a focus

[00:49]
on real world utility and less so on
benchmarks, but we happen to pick up a
few of those along the way. We focused a
lot on the intersection of engineering
and research, and we think you'll really
love working with this model.
[Music]
Thank you, Michelle. Um, as as Michelle
was saying, uh, the benchmarks, they're
exciting numbers, but we're starting to
saturate them. Like, when you're moving
between 98 and 99% in some benchmark, it
means you need something else to really
capture how great the model is. And one
thing we've done very differently with
this model is really focus on not just
these numbers, but really on real world
application it being really useful to
you in your daily workflow. So hearing
about it is much less exciting than
seeing it. So to show you this model in
action, I I'd like to welcome Addie and
Brian to the stage.

[00:50]
>> Thanks, Greg. I'm Brian, a solutions
architect on the startups team. I'm
Audi, a researcher on the post training
team.
>> To recreate the ideal pair programmer,
you need a model that understands best
software engineering practices, but has
a personality that just feels right to
work with. For GPT5, we worked really
hard to make the model pair perfectly
with you by default out of the box. Let
me pull up a demo of GP5 inside of
cursor to show you this behavior that we
taught it.
So last month I was on a different live
stream and towards the end I ran into a
bug that I covered up. Uh and afterwards
I tried to have GPT5 or I tried to have
GP 03 fix it for me and it couldn't. Um
so while we were testing GP5 before this
I had it see if it could fix that bug
for me. And to taunt the demo gods I'm
going to see if it can do it on stage.

[00:51]
>> All right let's hope for better luck
then with 03. This is less about that
fix and more about the behavior of the
model during this process.
So right away you're going to see that
it's going to tell you its plan up
front. It's going to tell you how it's
going to look for the bug, maybe how
it's going to fix it. This kind of
communication shows uh builds trust
during a coding session and helps you
redirect if you need to, but you don't
need to.
>> I like how it's giving you updates like
it said it's going to search and now
it's continuing.
>> Yeah, it searches faster than me. I I
don't It's using the same best practices
that I would while I was hunting this
down, but it is much more powerful than
I am as a developer.
>> Now, did you try to fix the bug yourself
and how long it would take to take you?
>> I couldn't do it. I mean, I was busy.
So, um
Okay, so continuing on, it's like
starting to figure out where it's going.
Um it's going to sort of like figure
this out. So, while this is going, let
me tell you a little bit about how we
trained GBD5 to behave this way. We
started by talking to users and

[00:52]
customers about how our models perform
in the most popular coding tools like
cursor. And we identified frustrations
and rough edges. And we boiled it all
down into four personality traits.
Autonomy, collaboration, communication,
context management, and testing. We
turned those into a rubric that we used
to shape the model's behavior. And then
we tuned it until it felt like a
collaborative teammate while we were
using it.
>> Yeah,
>> it's been really amazing to see the team
really doing the grind of like going and
seeing how this model behaves in
practice, figuring out what people
really want and and putting that back
into model training. That's something
that I think has been like a real focus
for this model.
>> It's been pretty great. Um, so while
this is fixing, the other thing that we
did uh during testing which was really
surprising was we were sort of pressed
for time and we had it refactor one of
our test harnesses to run parallel on
Docker and uh set it off came back like

[00:53]
45 minutes later it just like it just
finished and we tested it out and it ran
the first time. It was pretty
surprising.
>> That's incredible.
>> That is magical.
>> Okay, so it made the edits. It looks
like yeah, it found the right problem.
And right now it's actually okay. It's
see it's it's running lints, but these
lints are actually not related to this
bug. So, it's going to ignore them. Um,
and then it's going to run a build.
It'll run tests if there are any. Um,
it's going to make sure that this code
is shippable before it's done.
>> It's actually really smart that it finds
lints and realizes that these aren't
relevant to the specific bug we're
fixing. It's not making unnecessary
edits.
>> Totally.
So this is just one example, but it
really shows the power of the autonomy
and the collaborative communication and
how it stays reliable on difficult
coding tasks without getting stuck on
death loops.
And the best part, GPT5 is totally
tunable. You can steer it with system

[00:54]
prompts or cursor rules. You can change
its verbosity levels or reasoning levels
to match your tasks. And if you get
stuck, ask it. GPT5 is actually really
good at modifying its own prompts by
metarrompting.
So after using this for the past few
weeks, it really feels like we've
achieved state-of-the-art zerootshot
performance and reliability across the
most complex coding tasks. For me, it's
the first time I trust a model to do my
most important work. This is beyond vibe
coding. It's an incredibly powerful
tool, and I'm really excited for people
to try it.
Thanks, Brian. It's super exciting to
see how far GBT5 has come when it comes
to coding personality and steerability.
I'm really excited to show how great
GBD5 is at front-end coding, where
design and aesthetics really matter. So,
I've got two demos for you today. One
for work and one for fun. Let's start

[00:55]
with the work example. So, imagine
you're the CFO of a startup. Um, I have
some data that I'd like to visualize
about the company. Um, and I'm going to
ask the model to make me a dashboard.
So, um, you'll see here that I'm being
specific about the audience. So, the
target audience is the CFO. Um, I've
said, you know, create a finance
dashboard for my startup. Um, and I've
asked it to be beautiful, tastefully
designed with some interactivity. Um,
and to have a clear hierarchy for easy
focus on what matters. I've also
specified what frameworks it should use
and you can see that it's actually
started. It's following my instructions
and using um create next app to make a
next.js project.
>> So totally from scratch.
>> Yeah, exactly.
>> Now, how long do you think this kind of
task would take you to take or
>> Yeah, easily at least a couple of days.
Uh I'm not a front-end expert. Just to
understand the latest frameworks and
piece everything together would Yeah,
easily take me a few days.
>> We'll see how long it takes with the

[00:56]
model.
>> Yeah. Um, and it's really cool to see
that the model has thought for a bit and
it's explaining how it's going to
structure the project. So, it's talking
about how it's going to scaffold a new
Next.js app. It's going to use Tailwind
CSS. Uh, it's running um a couple of
commands to install dependencies. Um,
which is cool. Uh, and now it's um it's
proceeding to um implement the rest of
the project. So, while this runs, I'm
going to talk a little bit about how we
trained GPT5 to be a great front-end
coding model.
We tried to follow the principle of
giving it good aesthetics by default but
also making it steerable. So if I give
the model a concise prompt, it should be
able to infer my intent and make
something that looks great by default.
On the other hand, if I'm specific about
a layout or frameworks that I want the
model to use, it should follow my
instructions precisely. And this makes
it the best of both worlds for
developers.
We also we also train GPT5 to be much
more agentic than previous models. So if

[00:57]
you give it a task like this, it will
run long chains of reasoning and tool
calls and just go to work to build code
that is both ambitious and coherent.
>> I like how you said ambitious because it
means it goes above and beyond without
going off track or off what you
specified.
>> Yeah, exactly. So what we want is the
model should adhere to my prompt but
also like be be ambitious and um go
above and beyond when it thinks it can.
And so checking in here um looks like
the model is uh is making progress. Um
it's creating a readme file. Um yeah and
it's it's I think it's thinking about
how to make the code modular. Um so it's
it's created like a bar bar chart
component. Um, looks like it's uh
continuing here.
>> I love that it doesn't just write the
code. It also really thinks about proper
abstractions and documentation and
really the whole life cycle of what it
is to write software.

[00:58]
>> Yeah. Yeah. Exactly. It's not it's not
just writing the code like in
SweetBench, but it's also communicating
about the code and explaining what it's
doing.
Let's check in to see what's going on.
So while while this runs um GBD5 uh
understands details much better than
previous models. So when we train the
model we taught it to understand details
like typography, color and spacing in a
way that just eclipses any previous
model we've shipped. Like I remember
with old models you would have to like
write really specific prompts to get it
to do what you want. But GPD5 just gives
you great results by default. During
testing, we were looking at the A's and
B's for different versions of the model
to see if it was doing better at UI. And
at some point, we stopped being able to
tell and actually had to pull in
designers to teach us what was better.
>> Yeah, it was really fascinating to see
the model's aesthetic preferences evolve
during training. Um, and like we woke up
one day and it was just making these
great UIs.
>> How do the model's aesthetic preferences

[00:59]
compare to your own? Yeah, I think in
general I feel like the model has better
aesthetics than me. Like usually I defer
to its judgment and and I find that like
really helpful when I'm trying to make
an app. Like I'm not exactly sure how I
want it to look, but the model's
defaults are are just great.
Yeah. And checking in here. So you can
see that the model has actually
structured the code into these different
components. So, it's made a sample data
TypeScript file, KPI card, component,
revenue chart. Uh, and like I said, it's
it's super modular, and it's thinking
about how to not just write code, but
write high quality code that can
actually be merged.
>> Feels like it's close.
>> Yeah, I think it's I think it's pretty
close. It's uh
>> You did say ambitious.
>> Yeah. Okay, cool. So this is awesome. So
you can see here that it's actually
building the project and streaming
errors back to itself. And and this is

[01:00]
for me this was just a profound moment
to see that the model could write code
but also run builds, stream the errors
back and iterate on the code. So it's
it's able to improve its own code in
this sort of self-improvement loop which
which is fascinating.
>> It's definitely a good taste of what the
future holds as well, right? when you
really think about where these models
can go and how much they can accelerate
developers in kind of all aspects of of
what what we all collectively do.
>> Yeah, exactly.
>> Nice.
>> It actually just fixed a bug that it
found in that previous build. Okay,
cool.
>> Nice. Yeah, looks like it's done. Let's
check it out. So, I'm going to follow
the instructions that I I don't I don't
really know front end. So, let me let me
see how I should run it. So it's saying
cd to the directory and then run npm
rundev. So let me do that. Um and it
looks like it's being served on port
3001. So let me just open that port.

[01:01]
>> Wow, it's alive. Nice.
>> Nice. Yeah. So you can see here, let
let's check it out. So um the model has
made me a dashboard. It's telling me
like my ARR cash. Uh looks like this
company's doing pretty well. You can see
that revenue is growing. Um, and the
model's added like some interactivity
here. So if I hover over a graph, it
actually tells me the the exact value
for a particular day.
>> It would take me like five hours to do
that in D3.
>> Yeah. Imagine like manually doing this
in D3. It's just like
>> now now just because it's so easy to
take this for granted, could could you
remind the audience what the actual
prompt was? Like how much creativity and
sort of understanding your intent was
required to accomplish this? Yeah, it's
it's crazy that this, you know, this
prompt is so concise and it's able to
just give me something that looks
beautiful uh in in just 5 minutes.
>> That's amazing.
>> Yeah. Um it's also, you know,
implemented another graph here uh show
showing our customers. Um it's also
implemented a date picker so I can sort
of filter by different dates and

[01:02]
visualize data accordingly. Um yeah,
it's even sort of segmented it by c like
uh by by customer segment which is cool.
Um so this this is just one example that
highlights the power of GT5.
>> There will no longer be excuse for ugly
internal applications.
>> Exactly.
Um let's let's go to the fun demo.
>> Yeah.
>> So
>> I mean this was pretty fun but even more
>> even more. Yeah. So um I have a younger
cousin and I want to make a game for
her. So, I I want to make a 3D game that
incorporates a castle. So, you can see
my prompt. Um, I'll just kick this off.
Uh, sorry.
>> It's always the non AR parts.
>> Yeah, exactly. Uh, yeah. Okay. So, you
can see my prompt. Um, create a
beautiful castle. I've included some
details like we want people patrolling
the walls, some movement, horses. Um,
and I want a miniame where I can pop
balloons by clicking on them. And this

[01:03]
should make a sound effect. So, let me
run this in cursor. Um,
I'll just paste it in. And, um, I'm I'm
going to show um an example that I've
already generated just to save some
time. Um, so here is the beautiful
castle that the model made. So, it's
just wild how, you know, from a concise
prompt, the model has this great sense
of aesthetics where it's it's made this
like floating rock, um, made a 3D
castle, and if you zoom in, you can see
like tons of detail like these guards
that are walking around, cannons firing.
Do you want to fire the cannons if you
click this button?
>> Yes, of course.
>> Who wouldn't want to?
>> Yeah, there we go. So, can fire the
cannons. Um, you can even chat with the
characters. So, we'll say hi to Captain
Rowan.
>> We have names. Say hello to the
merchant.
Merchants selling some stuff. Uh, what's
your favorite song?

[01:04]
A ballad of banners and dons.
>> Nice. Give me some wisdom.
>> Curiosity is volatile. Yeah, that's that
makes sense.
>> Um,
>> miniame.
>> Yeah. Do you guys want to try the mini
game? Absolutely. Let's play the mini
game. So, if you hit this, if you hit
this button, you want to try it, Greg?
>> All right.
>> So, you can fire at these balloons.
>> Oh, wow. All right.
>> Oh, no. I'm not good at it. Hold on.
>> Maybe I can ask GPD 5 for some help with
it.
>> A little.
>> Oh, you you hit one.
>> I got one. Oh, there we go. We got a
sound effect.
>> Sound effect.
>> These are historically accurate
balloons.
>> Yes.
>> Did I get a second one yet? Man, this
game is harder than I thought. Hold on.
We got a balloon coming.
There we go. All right. Nice.
>> I think I should quit while I'm ahead.
>> Cool.
>> So, working with GPD5 has been really
fun and profound for me because for me,

[01:05]
this is the first model I've worked with
that actually has a sense of creativity.
And we're really excited to see how GP5
unlocks your creativity.
>> All right. Thank you both. This is
absolutely amazing.
Now, we we believe that GPD5 is the best
coding model in the world. Um, but don't
just hear it from us. Uh, to talk more
about this model, uh, and how to make it
really useful for developers, I'd like
to welcome Michael Truel, who is the
co-founder and CEO of Cursor.
>> Thank you. Good to be here.
>> Great to have you.
>> Yes.
>> So, what was your very first experience
with GPD5? Um, so when we got access to
GPD5, we just said about using it on our
actual work. Um, and so to start with as
a test, we asked it to tell us something
non-obvious about our codebase. And
within a couple of minutes, it buried
into the codebase. It identified a
particular system that we use for remote
code execution. And it identified a
nonobvious architecture decision we had

[01:06]
made. And then it also understood why we
made that architecture decision. Uh, and
it was to it was to harden our security.
Um, and those were architecture
decisions and trade-offs that took uh,
humans weeks to think through. So, it
was kind of amazing to see its codebased
understanding abilities um, from the
get-go.
>> Uh, that's really great. Not just the
code writing, but actually the code
reading and understanding.
>> Yes. Yes.
>> Yeah. Turns out there's so much more to
software than just the emitting of the
code.
>> Yes. Yes. No, the understanding is an
important prerequisite.
>> And what is most stood out to you about
GPD5?
>> It's incredibly smart. Uh, it's very
smart. uh and even though it is smart,
it does not compromise on its ease of
use for real pair programming. Um and uh
that means it's incredibly fast. That
also means that it's quite interactive.
And so it's good about talking about,
you know, what it's about to do,
breaking problems down into sub problems
that a human can then see. Um and
leaving a reasoning trace that you can
then intervene on and react to. Um it's
also great not just at you give it one
initial query and then it goes and does
that. Uh but you know, working with you

[01:07]
over a long session. uh where you're
asking it to backtrack on something that
has gone down or yeah asking it to you
know make additional make additional
changes to the codebase.
>> Should we show it in action?
>> Let's do it. Yes. So I think we are
going to
go and we're going to try and solve a
bug. And so this is the OpenAI Python
SDK. Uh there are a bunch of issues in
the OpenAI Python SDK. There are also a
lot of closed issues.
>> Okay, good.
>> And um uh it seems like there's a
problem with uploading PDFs through the
SDK. And this has been open for three
weeks. So it's not a trivial problem.
>> Yeah. Uh and so let's see if we can go
tackle this issue. So we're gonna go
we're going to take the issue. We're
gonna paste it into the editor, paste it
into cursor. Um and GD5 is going to set
off and try and solve the problem. And
this is actually an example of the
robustness of the model uh in the API
where to solve this problem in cursor uh
it's working with a set of uh custom
models that it hasn't seen before a set
of custom tools that it hasn't seen
before to do things like pull down text

[01:08]
from the web to search throughout the
codebase um and it's incredibly robust
and adept at using those tools. Um and
they boost evolve results.
>> Yeah, I love seeing just the full
explanation of all the things that it's
running and doing. And I guess yeah, how
does this seem to compare to how you
would solve this problem? Um well it's
way it's very fast.
Um you can see it's made a high level
plan searched throughout the codebase.
Um it started to read some files um and
continued searching and now it's kind of
thinking through what it'd like to do
next. Um and now it's started to to
actually solve the issue. Um and started
to think through some some code changes.
>> Now any advice for people on how to get
the most out of GPD5 in cursor? Um I
would suggest using it for your real
work. Um so uh GPD5 is a step forward
towards a real pair programmer. And so I
would start using it as a helper on you
know as a daily driver model for you. Uh
and so if you haven't used AI to code
much before you know I would take some
of your more scope down problems and try

[01:09]
handing them off to the bot and working
with it synchronously. Yeah, I think the
fact that GBD5 is so great for the real
world like big code bases like doing
doing your your daily driver not just
this like demo of a cool one-off
application as cool as that is right
that the real value comes from really
operating in a larger codebase and defin
you know sort of these long lived
applications
>> and its codebase understanding is very
impressive also its ability to be
steered is impressive uh and so yeah if
you specify a long complicated task with
lots of lots of subtleties in the
initial instructions it's very at
picking up on those subtleties. Um, it's
also very good at if it's gone down a
wrong path and actually goes and
executes the code or hears back from you
that it was incorrect. It's very good at
backtracking, too.
>> Now, what can't GPD5 do?
>> Ooh. Um, well, we're really excited
about computer using capabilities about
those getting better. Uh, it would be
great if for instance the the dashboard
uh Audi just showed, you know, if it
could run the code, see the output,
actually, you know, kind of QA every
little bit itself and then react to it.

[01:10]
Um and uh yeah so looking forward to
computer using capabilities. What would
you how would you like GT5 to be better?
>> Oh well I think I think that is that is
a great one just expanding the
dimensions right I think it's in all
directions right that there's so much of
like doing devops and uh uh you know
other work that is external to uh to to
you know software you know codew writing
as we think of it today. Um but also you
look at these demos right we run them
for 5 minutes 10 minutes couple hours
but I think extending that life cycle to
really be able to go for days and weeks
and eventually even months I think that
is that is ultimately where we expect
things to go.
>> So we can see that it has uh buried into
the codebase and discovered uh that
there's an issue with the MIME or the
mime typing being sent up for PDFs and
the plumbing through the SDK. It has
identified that and it started making
some code changes. Um, and this, you
know, it's created some new methods.
It's gone and edited some existing code,
and this looks roughly correct.

[01:11]
>> Looks pretty good.
>> And would love to merge the PR, too.
>> I would love to do that as well. Let's
do that after the show.
>> Yes, that sounds great. Awesome.
>> All right, cool. Well, thank you so
much. We're so excited to have GPD5 and
Cursor. Um, and uh, you know, starting
today.
>> Excited to partner with you guys. And
so, yeah, starting today, GP5 is default
for new users in Cursor, and we're
releasing it to all Cursor users. uh
free to try for the next few days so
people get a sense of the model. Um and
it is the smartest coding model we've
ever tried.
>> Awesome. Thank you so much, Michael.
>> Thanks,
[Applause]
but it's great for the enterprise. We
think of it like
uh it's great for the enterprise. We
think of it like a a subject matter
expert that is in your pocket that is an
expert across every domain, legal,
finance, whatever application you have
in mind. Uh to talk about how GBD5 can
be applied to the enterprise. I'd like
to welcome Olivier to the stage. Thank
you.

[01:12]
>> Thank you, Greg.
Hi everyone. I'm Olivier. I lead the
platform at OpenAI. At this point, I
think you got the message. We care a ton
about developers and coding. But that's
not all. Enabling businesses and
governments is critical to open eye
mission. Put shortly, we want to enable
the key industries to transform
themselves such as healthcare,
education, energy or finance. Since we
launched at DPT and the API, 5 million
businesses have been using our
technology. I'm still mind-blown. Five
millions businesses. And those
businesses are not just playing. They're
not just experimenting, they are pushing
in production new products in the real
world. And I believe DPT5 is going to be
a step function with that regard. As Sam
mentioned earlier, the possibility to
have a subject matter expert in your
pocket is going to enable every employee
to do more. But let me give you a few
examples. First, I want to talk about
life sciences. Amgen is a company in the

[01:13]
US that designs new drugs, new medicines
to fight some of the toughest human
diseases. Amgen was one of the first
tester of GPT5 and they used it in the
context of drug design. And what am
scientists found is that GPT5 is
particularly good at deep reasoning with
complex data. Think analyzing scientific
literature or clinical data.
Next, I want to talk about finance. BBVA
is a multinational bank which is
headquartered in Madrid in Spain. BBVA
has been using GPT5 for financial
analysis and the takeaway was pretty
clear. GPT5 beats every single other
model out there in terms of accuracy and
speed. What used to take three weeks for
a finanist to do GPT5 can do it in a
couple of hours. Next, I want to talk
about healthcare. Oscar is an insurance
company based in New York and they've
been using GPT5 and what they found is
that GPT5 is the single best model for

[01:14]
clinical reasoning. Think mapping
complex medical policy to patient
conditions. It's not all about
businesses. It's also about governments.
We are super excited by the announcement
that we made yesterday that the two
million US federal employees will be
able to use GPT5 in CHP and I cannot
wait to see how that enables to deliver
better faster services to the American
people
and frankly that's all very cool but I
think that's the tip of the iceberg. If
history is a teacher and we've seen it
with Dip T4, we are going to see many
many use cases emerge over the coming
weeks and months that all of us could
not even imagine. And so I cannot wait
for us to invent that feature together.
Let's talk quickly about pricing and
availability. GP5 is going to be
available in the API starting today.
Three models, GPT5, Dipt5 Mini, Dipt5
Nano. GPT5 is going to be priced at 1.25
$25 and $10 per million input token and

[01:15]
output token. Mini and Nano are even
faster and more affordable. Nano, don't
sleep on it. It's 25 times more
affordable than GP5. It's pretty cool.
Um, I cannot wait to see what you all
build. And next, our chief scientist,
Jakob, is going to close us out.
[Applause]
Thanks, Olivia. Um at OpenAI at the core
we are about understanding this
miraculous technology called deep
learning and what its consequences are.
Our research aims to understand what
deep learning is capable of and how to
steer it to make it safe and useful for
all of us.
This is a work of passion.
And it's a mission and I want to

[01:16]
recognize and just deeply thank the team
at OpenAI.
It is a great privilege.
It is a great privilege for me uh to
work alongside this incredible group of
brilliant people
driven by this shared goal.
What adds up to a model like GPT5 are
years of investigations
aimed not only at producing a great
release but at building understanding of
this underlying technology itself. And
so a lot of what you'll see in this
model are really just early glimpses
of new ideas that we believe will go
much further.

[01:17]
There is a lot we still have to
understand
and we look towards a future where AI
can uncover new knowledge about the
world and meaningfully transform our
lives for the better.
We hope you'll enjoy what you we've
built and
we'll get back to sailing.
Thank you.

</details>
