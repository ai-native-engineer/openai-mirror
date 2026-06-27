---
title: "Sam, Jakub, and Wojciech on the future of OpenAI with audience Q&A"
channel: openai
url: https://www.youtube.com/watch?v=ngDCxlZcecw
youtube_id: ngDCxlZcecw
published: 2025-10-29
duration: "1:02:09"
captions: en-orig
---

# Sam, Jakub, and Wojciech on the future of OpenAI with audience Q&A

[![Sam, Jakub, and Wojciech on the future of OpenAI with audience Q&A](https://img.youtube.com/vi/ngDCxlZcecw/hqdefault.jpg)](https://www.youtube.com/watch?v=ngDCxlZcecw)

<details>
<summary>자막: Sam, Jakub, and Wojciech on the future of OpenAI with audience Q&A (1:02:09)</summary>

[00:00]
Hello, I'm Sam. This is our chief
scientist, Yakob. And we have a bunch of
updates to share today about OpenAI. Um,
obviously the news of today is our new
structure. We're going to get to that
near the end, but there's a lot of other
important context we would like to share
first. Given the importance of a lot of
this, we're going to go into uh an
unusual level of transparency about some
of our specific research goals and
infrastructure plans and product, but we
think it's uh you know sort of very much
in the public interest at this point to
cover all of this. So our mission at
OpenAI in both the nonprofit and our new
PBC is to ensure that artificial general
intelligence benefits all of humanity.
As we get closer to building this, we
have new insights into what that is
going to mean.
There was a time earlier on in OpenAI
where we thought that AI would or AGI
would be sort of this oracular thing in
the sky and it would make all these
wonderful things for us and we now have
a sharper view of that which is we want
to create tools and then we want people
to use them to create the future. We

[00:01]
want to empower people with AI as much
as possible and then trust that the
process that has been working for human
history of people building um better and
better things with newer and better
tools will continue to go on. We we can
now see a vision where we help build a
personal AGI that people can use
anywhere with all of these different
tools, access to all these different
services and systems to help with work
and personal life and their personal
life. And as AI gets better and better,
as AI can even do things like discover
or help discover new science, what
people will be able to create with that
um to make all of society better and
their own lives more fulfilled, we think
should be quite incredible.
There are three core pillars we think
about for OpenAI. Research, product, and
infrastructure. We have to succeed at
the research required to build AGI. We
have to build a platform that makes it
easy and powerful to use. And we have to
build enough infrastructure such that
people can use at a low cost all of this
amazing AI that they'd like. Here's a
little like cartoon of how we think
about our world. So, at the bottom layer

[00:02]
here, we have chips, racks, and the
systems around them, the data centers
that these go into, and the energy. Uh
we'll talk more about the first three
today in energy another time. Then we
train models on top of these. Then we
have an open AI account on top of that.
We have a browser now uh called Atlas
and we have devices coming um in the
next few years that you'll be able to
take AI with you everywhere. And we have
a few first party apps like Chachi Pine
and Sor and we'll have more over time.
But mostly what we're excited about is
this big puzzle piece in the upper
right. We're finally getting to a world
where we can see that people are going
to be able to build incredible services
uh with AI starting with our API with
apps and chatbt new enterprise platform
that we'll have over time uh an open
account and way way more and people will
be able to fit all of the kind of like
current things in the world and many
more into this new AI world and we want
to enable that and we we believe the
world will build just a huge amount of
value for um for all of us. So that's
kind of what we see the economic picture

[00:03]
looking like. But one of the things that
we've thought about for a long time and
we really see happening now or starting
to happen now, glimmers of it, green
shoots, whatever you want to call it, is
the uh impact that AI will have on
science. And um although the economic
impact from that previous slide will be
huge for the long-term quality of life
uh and improvement that and change in
society, AI that can autonomously
discover new science or help people
discover new science uh faster will be I
think one of the most important things
and something that we're really trying
to wrap our heads around. So I'm going
to hand this over to Yakob to talk about
research and as I mentioned uh we're
going to share a lot about our internal
goals and our picture of where thing
where things are.
Thanks Sam. Um at the core we are a
research laboratory focused on
understanding a technology called deep
learning. And so a particular focus of
ours is um understanding uh what happens
as you scale up training deep learning
systems.
Um and one consequence we discuss a lot

[00:04]
there uh is AGI artificial general
intelligence. But we find that um in
some way even this maybe understates a
bit um the magnitude of um the possible
progress and change here. Um and so in
particular we believe uh that it is
possible that deep learning systems are
less than a decade away from super
intelligence. So systems that are
smarter uh than all of us on
uh a large number of of of of critical
axis
and
um this is of course a a serious thing
right there's uh a lot of implications
of this to grapple with and one uh
particular focusing impact of this
technology um and the technologies
leading up to it and something that we

[00:05]
organize our entire research program
around is the potential uh to accelerate
scientific discovery um to accelerate
the development of new technology.
Um
we believe that this will be uh perhaps
the most significant uh long-term impact
of AI development. um and it will
fundamentally change the pace of
progress on on on developing new
technologies.
Um and so thinking about how far along
we are uh uh towards these goals, uh one
good way to think about progress is to
look at the time horizon that it would
take people to accomplish the task that
the models can perform. And so this is
something that has been extending
rapidly over the past few years. Um so
where the current generation of models
is at right now is about five hours. So
um if you you can see this by looking at

[00:06]
the models matching the best people in
competition such as the international
Olympics or informatics
and we believe that this horizon will
continue to extend rapidly and this is
in part as a result of algorithmic
innovation and a part uh just scaling
deep learning further and in particular
scaling um along this um new axis um in
context compute also called test time
compute uh where we really see orders
and orders of magnitude to go. Um so
this is roughly how much time the model
spends thinking right and if you look at
how much time the model's currently
spent thinking about problems and if you
think about how much compute how much
time you would like to spend on problems
that really matter such as scientific
breakthroughs you should be okay using
entire data centers. Uh and so there is
there is really quite a way to go there.
Um and anticipating this progress uh we
of course make plans around it
internally and we want to provide some

[00:07]
transparency around our thinking there
and so we want to take this maybe
somewhat unusual step of sharing our
internal goals and goal timelines uh
towards these very powerful systems and
you know these particular dates we
absolutely may be quite wrong about them
uh but this is how we currently think
this is currently how how how we plan
and organize and So as a research
organization that is working on
automating research, naturally we are
thinking about how does this impact our
own work and uh how will AI systems that
accelerate development of future AI
systems look like? How can they empower
um research like alignment? And so uh we
are making plans around getting to quite
capable AI research interns that can
meaningfully accelerate our researchers
by expanding
a a significant amount of compute um by
September of next year. So we believe
that is actually quite close. Um and
then we uh look towards getting a system

[00:08]
capable of autonomously delivering on
larger research projects and a
meaningful uh fully automated AI
researcher uh by March of 2028.
Um and so of course as we look towards
these very capable systems uh we think a
lot about safety and alignment right and
in fact a lot of our work uh both on
deployments and safety uh but also just
on on on understanding deep learning and
development capability side we can think
of preparation for these very capable
models. Um safety is a multiaceted
problem and so the way we generally
structure our thinking uh are these five
layers ranging from uh factors that are
most internal to the model to ones that
are most external. And so at the core
right and what we believe is the most
important uh long-term safety question
for super intelligence is value
alignment.

[00:09]
So to put this um
this
value alignment uh you can think of as
what is what is really the thing that
the AI fundamentally cares about uh can
it adhere to some high level principles
u what will it do if it's given unclear
and conflicting objectives u does it
laugh humanity
um and the reason we believe that kind
of this this high level uh um
um
objectives or or or or principles
driving the AI are so important is that
as we get to the systems that are
thinking for very long, uh as they
become very smart, as they tackle
problems that are uh um at the edge or
perhaps beyond human ability, uh really
getting to like complete specifications
becomes quite difficult. Uh and so we
have to rely on this on this deeper

[00:10]
alignment.
Um then there's goal alignment. Um, does
the agent uh interact with people? How
does it interact with people? How does
it um do it following instructions? Um,
then reliability. Um, can the AI
correctly calibrate its predictions? Uh,
can it be reliable on easy tasks,
express uncertainty on hard ones, can it
deal with environments that are a little
bit unfamili unfamiliar?
Um then we have adversarial robustness
which is very related to reliability but
it's about adversarial settings. So can
can the AI withstand target attacks from
human or AI adversaries.
And then the outer layer is systemic
safety which are guarantees about the
behavior of the overall system that do
not rely on the AI's intelligence or
alignment. Um so for example this can be
security or what data does the AI have
access to? um or um um uh um what

[00:11]
devices it can use. And so we invest in
multiple research directions across
these domains. And we have seen uh quite
a lot of progress also come from just
the general uh development and improving
understanding of deep learning uh as a
whole. And uh I want to I I want to take
a slightly deeper technical dive here.
Um and talk about a particular
direction. Uh value alignment is a hard
problem, right? It's definitely not
solved yet. Um however, there is a new
promising tool that aids our study of
it. [snorts] Uh and that is chain of fun
faithfulness. Uh it's something we
invest in very heavily. Um, starting
from our first reasoning models, we've
been pursuing this new direction in
interpretability. And the idea is to
keep parts of the model's internal
reasoning free from supervision. So
don't look at it during training and
thus let it remain representative of the

[00:12]
model's internal process. Um,
so we refrain from from from from kind
of guiding the model to think good
thoughts and and and and and so let it
let let it remain a bit more faithful to
to to what it actually thinks, right?
And this is not guaranteed to work, of
course, right? We cannot make uh
mathematical proofs about deep learning.
And so this is something we study. Uh
but there are two reasons to be
optimistic. One reason is that we have
seen very promising empirical results.
Uh this is a technology we employed a
lot internally. Uh we use this to
understand um how our models u um train
h how their propensities evolve over
training. Uh also we have had successful
external collaborations on investigating
the models propensity scheme for
example.
Um and secondly uh it is scalable and in

[00:13]
the sense that explicitly we make the
scalable objective not adversarial to
our ability to monitor the model. Um
and of course an objective not being
adversarial to the ability to monitor
the model is only half the battle. Um
and you know ideally you want it to to
to get it to help with monitoring the
model. And so this is something we're
we're researching quite heavily.
Um but one important thing to underscore
about train of thought faithfulness is
it's somewhat fragile. Um it really
requires drawing this clean boundary uh
and having this clear abstraction uh and
having restraint in in what ways you can
access the chain of thought [snorts] and
this is something that is present uh at
OpenAI from algorithm design to the way
we design our products right so so if
you look at the chain of thought
summaries in chat GPT uh if we didn't
have the chain of summarizer if we just
make the chain of f fully visible at all
times right that would make it kind part

[00:14]
of the overall experience over time it
will be very difficult to not subjected
to any supervision.
Um and so longterm we believe that by
preserving some amount of this
controlled privacy for the models uh we
can retain the ability to understand
their inner process and we believe this
can be a very impactful technique uh as
we move towards these very capable
longunning systems. Um and I'll hand
back to Tom.
>> Okay, that's very hard to follow uh with
the rest of this and obviously that's
the most important part of what we have
to say. But um you know just to to
reiterate uh we may be totally wrong. We
have set goals and missed them miserably
before. But with the picture we see we
think it is plausible that by September
of next year we have sort of a intern
level AI research assistant and that by
March of 2028 which I believe is almost
5 years to the month after the launch of
GPT4. um we have like a a legitimate AI
researcher and this is the core thrust
of our research program. There are two
other areas we want to talk about uh
product and then infrastructure. On the

[00:15]
product side,
as we make this incredible progress with
deep learning, we want to make it useful
to people to sort of invent the future
as we mentioned. And um what that's
looked like traditionally for us as an
AI super assistant inside of Chacht, but
we're now really going to evolve to a
platform uh that other people will build
on top of and all of the pieces that
need to fit in uh of the world um you
know will be built by others. Before we
go talk about that, wanted to just show
a quick video of how people are using
GPT5. Some of the ways people are using
GPT5 in Chacht today.
>> I'm a quantum physicist.
>> I'm a nail [music] technician, human
iminologist.
>> I'm a steel worker,
>> a designer and developer, a professor of
economics.
>> I [music] basically go fishing for a
living.
>> GPT5 is able to predict the outcomes of
experiments that [music] we haven't even
done. Can you create a part numbering
system that's easy for my guys in the
shop?
>> I want to catch dungeonous [music] crab
in the Bay Area. Here I would ask a

[00:16]
question about the application of a
certain [music] quantum operator. This
one gives me a very detailed
mathematics.
>> I ask for basically a camera app where I
[music] can draw real time in the air.
>> We have a theme. We have a direction to
go. Let's go from a million or infinite
amount of ideas to like give me 10 or
20.
>> You just start testing it. You know, you
tell it jokes. You ask it questions like
[music] what should economists do?
>> Different baits I can use, different
water depths, all this information that
it would take years to figure out on
your own. A lot of trial [music] and
error. It's tremendous for
brainstorming. It's back and forth.
>> I can kind of easily follow the
reasoning. I don't need to trust the
result. I can just look what did you do?
>> GBD5 just like did this um in [music]
one shot.
>> A 101 part numbers. It would have taken
weeks for me to number this and it would
have made me go crosseyed.

[00:17]
>> Uh Yakob will join me back for Q&A in a
little bit, but we're going to have one
special guest on before before the end.
Um we love that. We want much more of
that. We want that everywhere. So we
want open AI to be a platform that
people and companies can build on top
of. We can sort of see our way now to an
AI cloud where this is not just in chat
GPD. This is not just services that we
create, but we want to expose our
technology for as many people to build
the things that people will depend on
and use and create with as possible. I
think this this quote or at least this
like idea is originally from Bill Gates.
um at least that's where I first heard
it that you know you've built a platform
when there's more value created by
people building on the platform than by
the platform builder builder and that's
our goal um and that's our goal like
next year we we really think we can now
take this technology and this user base
and this sort of framework we've built
and get the whole world to build amazing
new companies and services and
applications on top of it
to do that uh there will be many things
that we have to evolve towards but

[00:18]
there's two foundational principles as
we as we move towards being in this
platform that I wanted to touch on. Um,
one is about user freedom. If this is
going to be a platform that all sorts of
people are building, uh, on using, um,
creating with, people around the world
have very different needs and desires
and there will of course be some very
broad bounds, but we want users to have
a lot of u control and customization of
how they of how they use it. Now, I
made, you know, one of my many stupid
mistakes when I tried to talk about this
recently. Uh, I wish I had used an
example other than erotica. thought
there was an understandable difference
between erotica and pornbots. But in any
case, we were trying to show the point
we're trying to get across is that
people need a lot of flexibility and
people want to use these things in
different ways and we want to treat our
adult users like adults. In our own
first party services, we may have, you
know, tighter guidelines, but AI is
going to become such an important part
of people's lives. The freedom of human
expression is going to need to be there.
Along with that, we think that world
will need to think about privacy in a

[00:19]
different way than they have for
previous kinds of technology. Privacy is
important for all sorts of technology,
of course, but privacy for AI will be
especially important. People are using
this technology in a different way than
they've used the technologies of the
past. They're talking to it like they
would to their doctor, their lawyer,
their spouse. Um, they're sharing the
most intimate details of their lives.
And of course, we need strong technical
protections on that privacy of that
privacy. But we also think we need
strong um policy protections of that
privacy. We've talked about concepts
like AI privilege. Um but really strong
protections if AI is going to be this
fundamental platform in people's lives
seem super important to us.
Okay. And then I want to go on to
infrastructure. So I know there's been a
lot of confusion about sort of where we
are in our infrastructure buildout and
we figured we would just be super
transparent about that. So where we are
today, um all of our commitments total a
little bit over 30 gawatts of uh of
infrastructure buildout. Um and that's
about a $1.4 trillion total uh financial

[00:20]
obligation for us over the next many
years. Um this is what we've committed
to so far. We of course hope to do much
more, but given the picture we see
today, given what we think we can see
for revenue growth, our ability to raise
capital, this is what we're currently
comfortable with. This requires a ton of
partnerships. We've talked about uh many
of our great chip partners. Uh there are
people building the data centers for us,
land, energy. Uh there will be chip fab
facilities. This is already getting to
require quite a lot of supply chain
innovation. And we're thrilled to get to
work with uh AMD, Broadcom, Google,
Microsoft, Nvidia, Oracle, SoftBank,
many others to really make this happen.
But this is still early. if the if the
work that Yakob talks about comes to
fruition, which we think it will, and if
the economic value of these things um
happen and people want to use all these
services, we're going to need much more
than this. So, I want to be clear, we're
not committing to this yet, but we are
having conversations about it. Our
aspiration is that we can build an
infrastructure factory where we can
create 1 gawatt a week of uh compute and

[00:21]
we aspirationally would like to get that
cost down significantly um to like $20
billion a gigawatt over the 5year life
cycle of uh you know that equipment. To
do this will require a ton of
innovation, a ton of partnerships,
obviously a lot of revenue growth. Um
we'll have to repurpose our thoughts
about robotics to help us build data
centers instead of doing all the other
things. Um, but this is where we'd like
to go and over the coming months we are
going to do a lot of work to see if we
can get here. Um, it will be some time
before we're in a financial position
where we could actually pull the trigger
and get going on this. 1 gawatt is like
a big number, but I figured we would
show a little video to put this into
perspective. Um, this is a data center
that we're building in Abene, Texas.
This is the first Stargate site. We're
doing several of these now around the
country, but this one is the furthest
[music] along. There's like many
thousands of people that work here every
day just doing the construction at the
site. There's probably hundreds of
thousands or [music] millions of people
that work in the supply chain to make
all this happen to design these chips,

[00:22]
to fab these chips, to put them
together. [music] Um there, you know,
there's all of the work that goes into
this for energy. There's an enormous
amount of stuff [music] that has to
happen um for each one gigawatt. And we
want to figure out how we can make this
way more efficient and way cheaper and
way more scalable so that we can deliver
on the infrastructure that the research
roadmap requires and that all of the
ways that people will want to use this
need um to enable that uh we have a new
structure. So um maybe you saw before
this like crazy convoluted uh diagram of
all of the open entities. Now it's much
simpler. We have a nonprofit called the
open air foundation that is in control
of uh where the board sits uh or where
uh let's come back to the board uh where
the board also sits and uh owns a slice
of our PBC public benefit corporation
called OpenAI group. So uh nonprofit and
control public benefit corporation sits
under it. Um we hope for the OpenAI
Foundation to be the biggest nonprofit

[00:23]
ever. As I mentioned now uh a few times,
science is one of the ways that we think
the world most improves along with the
institutions that broadly distribute the
benefits of that. So the science will
not be the only thing that the nonprofit
funds, but it will be an important first
major area of the things that we do. The
nonprofit will govern the PBC. It will
initially own about 26% of the PBC
equity, but that can increase over time
with warrants if if we perform really
well. and it will use these resources to
uh pursue what we think are the best
benefits of AI uh given where the
technology is and what society needs.
The PBC uh will operate more like a
normal company. It will have the same
mission. Um it will be bound to that
mission. Um and you know in matters of
safety will only be bound to that
mission but it will be able to attract
the resources that we need for that
gigantic infrastructure buildout to
serve the research and product goals
that we have. So, the initial focus of
the the foundation, we'll do more things

[00:24]
over time, but we want to knock
something out of the out of the park,
uh, hopefully first, is a $25 billion
commitment to use AI to help cure
disease. There are a lot of ways this
can happen. Um, generating data, um, you
know, using a lot of compute grants to
grants to scientists and also for AI
resilience. Um AI resilience is a new
and I think very important area and I'd
like to invite uh our co-founder of
Voyche up to talk about what this will
what this will look like.
>> Hello
glad to be here.
>> Thanks for being here.
>> So um term AI resilience is um little
bit broader than what we historically
thought about AI safety. So in case of
the uh resilience we think that advanced
AI comes with risks and disruptions and
we would like to have an ecosystem of
organizations that uh can help to um
solve a number of these problems. Um so
let me give you an example to better
illustrate it. Um we all believe that AI

[00:25]
uh will advance in biology and as it
advances in biology there is a there is
a risk that some bad actor could use AI
to create manmade pandemics. So the on
the safety level the mitigation would be
to make sure that the models uh block
the queries that have to do with a
viology. Um however um if you consider
the entire entire um AI uh industry it's
very likely that even if open AI blocks
it someone could use uh different models
out there and still uh produce pathogens
and um the in case of resilience we
don't want just to block it but also
have a uh rapid response if the problem
would occur. So when I think about the
uh risks uh and disruptions there are
just many the the mental health is one
of them bio is another one another one

[00:26]
uh job displacement might be another one
and we think that we need the ecosystem
and maybe a good analogy that I like is
cyber security so at the beginning of
internet
uh it was actually it was a place that
people didn't feel comfortable putting
their credit card numbers because it was
so easy to get hacked and uh when there
was a virus people were giving each
other a call to disconnect the computer
from internet and we got a long way at
the moment there's entire infrastructure
of cyber security companies they are
protecting uh um the critical
infrastructure governments corporations
and individual users to such extent that
people are willing to put the most
personal data uh online to have life
savings um be online. Um yeah, so the
the cyber security got really far and we
think that something analogous will be

[00:27]
present for AI that there will be AI
resilience layer and uh I'm really
excited that the uh nonprofit uh will
help out uh to stimulate it to create
such an ecosystem.
>> So am I. I think this is an important
time to be doing this and I'm very
excited to that you're going to like
figure out how how we how we go off and
make it happen. So again, these are not
the only things that the nonprofit will
fund, but we're excited about these as
the first two using AI to develop cures
and uh treatments for diseases and this
new AI resilience effort as we figure
out what the deployment of AGI into
society is going to look like.
So we mentioned that those are our three
pillars, but you know what what if this
all works? We we think it is plausible
that in 2026 we start to see the models
of that year begin to make small
discoveries. By 2028 medium or maybe
even larger discoveries and you know who
knows what 2030 and 2032 are going to

[00:28]
look like. If AI can keep advancing
science as has happened in the past um
we think the future can be very bright.
Of course, we think it's very important
that humans can self-determine our way
through this future. But the open space
that new scientific advances give us is
quite impressive. So, we asked Sora to
help us imagine a radically better
future by looking at the past. And we
are particularly interested in how the
history of science builds on itself
discovery after discovery. This is what
we hope will happen with AI. You know,
this is going to be 200 years of
science. But if you can do these 200
years of compounding discoveries of the
scaffolding [music] building up on each
other not in 200 years but in 20 years
or in two years and if you look at how
much this this is accelerated [music]
think about what could be possible
before you can imagine a world uh where
a radically better future becomes quite
possible. You have a data [music] center
here that is discovering a cure for
cancer. A data center there that's
making the best entertainment ever. A
data center here that's helping you find

[00:29]
your future husband or wife. This one is
building rockets and helping you
colonize space. This one is helping to
solve the climate [music] crisis. So, we
did all this stuff the oldfashioned way.
Um, and now with the help of AI, we'll
be able to shape what comes next, uh,
with maybe much more power. So, we
talked a little about AI medicine. We're
very excited [music] about robots. Um,
we really think energy is very, very
important to the world. We want to
figure out what personalized education
can mean, design novel [music]
materials, and probably a ton of other
things that we can't even think of yet.
So as we head into this next phase of
open AI and more importantly than that
this continual progress in deep learning
um we thank you for joining us today and
we're going to try something new now
which is we're going to just answer
questions. If this works it's something
we are we'll try more in the future.
Yakob is going to rejoin for this Q&A.
Thank you very much.
>> Um but uh this is a new format for us.
So bear with us as we try it this first
time again. If if um if this is useful
it's something we'll do uh again a lot
more. and we're going to try to just

[00:30]
answer questions in the order they are
most upvoted. Um,
are we good to go? All right, let's see
how this works. So, uh, you can put
questions in the Vimeo link and we will
just start answering them. So, from
Caleb, we've warned that the tech is
becoming addictive and eroding the tech
is becoming addictive and eroding trust
yet Sora mimics Tik Tok and Chach may
add ads. Why repeat the same patterns
you criticized and how will you build
build rebuild trust through actions and
not just words? We're definitely worried
about this. Uh I worry about it not just
for things like Sora and Tik Tok and ads
and chatbt which are maybe known
problems that we can design carefully
but you know we have certainly seen
people develop relationships with chat
bots that we didn't expect and there can
clearly be addictive behavior there
given the dynamics and competition in
the in the world. I suspect some
companies will offer very addictive new
kinds of products. Um and I think you'll
have to just judge us on our actions.
We'll have to you know we'll make some
mistakes. We'll try to roll back models
that are problematic. If we ship Sora

[00:31]
and it becomes super addictive and not
about creation, we'll, you know, cancel
the product and you'll you'll have to
just judge us on that. My hope and
belief is that we will not make the same
mistakes that companies before us have
made. Uh I don't think they meant to
make them either. It's uh you know,
we're all kind of discovering this
together. We probably will make new ones
though and we'll just have to evolve
quickly and have a tight feedback loop.
We we can imagine all sorts of ways this
technology does incredible good in the
world. also obvious bad ones and um you
know we're guided by a mission where
we'll just continuously evolve evolve
the product. Um one thing that we are
quite hopeful about for in terms of um
what we optim optimize for in in uh
products like chat GPT or or Sora is
thinking about um optimizing for the
very long term which is naturally very
aligned with uh how we think in general
about extending uh the horizon on which
the models can work productively. Um
and so we believe that quite a lot of

[00:32]
development is possible there and we can
eventually get the models that really
optimize for um long-term uh
satisfaction and and and well-being
instead of just short-term signals.
Um okay, next question. Will we have an
option to keep the for model uh
permanently after adult mode is
installed? We don't need a safer models
responsible adults. Um,
we have no plans to sunset 40. Uh, we
are not going to promise to keep it
around till the heat death of the
universe either, but we we understand
that it's a product that some of our
users really love. We also hope other
people understand why um it was not a
model that we thought was healthy for
miners to be using. Um, we hope that we
build better models over time that
people like more. You know, the people
you have a relationship with in your
life, they evolve and get smarter and
change a little bit over time. And we
think that we hope that the same thing
will happen. But yeah, no, no plans to
uh no plans to sunset 40 currently.

[00:33]
Uh wow, we have a lot of for questions.
All right, we're not going to in the
interest of time, we will not go through
uh all of these, but but yeah, we don't,
you know, we want people to have models
that they want to use. We don't want
people to feel like we're routing them
around models. Um, and you know, we we
want adults to make choices as adults
as long as we think we're not, you know,
selling heroin or whatever, which also
you you shouldn't you shouldn't do. Um,
so people that want to have emotional
speech, uh, as we've said, we want to
allow more of that and we plan to. Okay,
here's a good anonymous question for
Yakob. When will AGI happen?
Um
so
I think I think
in in some number of years we'll look
back at these years and we'll say you
know this was kind of the transition
period when AGI happened. Um I think you
know what one way we thought about
um I think as as some said like early on
adopting we thought about AGI kind of

[00:34]
emotionally as this like thing that is
like the kind of ultimate solution of
all the problems and and and um it's
it's this like single point um for which
there is before and after and um I think
um we found that it's a bit more
continuous than that. Um
and and so in particular for like
various kind of benchmarks that you know
seemed at uh um
seem like kind of the obvious like
milestones towards AGI. I think I think
we now think of them as kind of like
indicating like you know roughly how far
away we are in years. And so uh you know
if you look at a succession of of of of
milestones such as computers beating
humans at chess and then at go and then
uh you know computers being able to
speak in natural language and computers
being able to solve math problems right
I think well they clearly kind of get uh

[00:35]
closer together. Um
yeah, I I would say I think it's the AGI
term has become hugely overloaded and as
Jakob said, it'll be this process over a
number of years that we're in the middle
of. Uh but one of the reasons we wanted
to present what we did today is I think
it's much more useful to say our
intention our goal is by March of 2028
to have a true automated AI researcher
um and define what that means uh than it
is to sort of try to you know satisfy
everyone with a definition of AGI
>> and and maybe one other thing to mention
right like I think like one kind of
counterintuitive thing here is that
obviously we're working with like a
pretty complicated technology we're
trying to understand all these
algorithms and maybe initially we kind
imagined that like AGI is the moment
once you where you kind of have figured
out all the answers and and and and it's
kind of the the final thing and I think
now we increasingly realize that you
know there is kind of a some some curve
of intelligence maybe a
multi-dimensional one and you know

[00:36]
humans are somewhere on it and as you
scale deep learning as you develop these
new algorithms like eventually well you
kind of inch closer to that point and
eventually and eventually will surpass
it and you know already have surpassed
on multiple axis um and and and so and
that doesn't actually mean you have
solved all the problems around it which
is something we we need to seriously
think about.
>> Can you give us an idea of how far ahead
internal models are compared to deployed
ones?
>> Um
I think
um
we we have quite strong expectations for
our for for for our next models. Um so I
think I think we we expect quite rapid
progress over the next uh uh couple
months and a year. Um
yeah I think um but we
we haven't been like withholding
something something uh extremely crazy.

[00:37]
>> Yeah. One of the ways this uh kind of
often works in practice is there's like
a lot of pieces that we develop and that
you know they're all kind of hard one
victories and then we know that when we
put them together um we will have
something quite impressive and we're
able to predict that fairly well. Uh
part of our goal today is to say that um
we have a lot of those pieces. It's not
like we're kind of currently sitting on
this giant, you know, thing that we're
not showing to the world, but that we
expect by a year from now, certainly
with this September of 2026 goal
that we have a a like I mean not likely,
we have a realistic shot at a like
tremendously
important step forward in capability.
Um, what is OpenAI? Ronin asks, "What is
OpenAI's stance on partnering with labs
like Anthropic, Gemini, or XAI for joint
research, compute sharing, and safety
efforts?" Uh, we think this is going to
be increasingly important on the safety
front. Uh, labs will need to share
safety techniques, safety standards. Um,

[00:38]
you can imagine a time when the whole
world would say, uh, okay, before we hit
a recursive self-improvement phase, we
really need to all carefully study this
together. Um, we welcome that
collaboration. I think it'll be quite
important. Um one thing to mention on
the on the on chain of thought
faithfulness that I talked about earlier
um we actually have um started talking
about establishing industry arms and and
we started some some joint
investigations with researchers from
Google and entropic uh and and and some
other labs and uh yeah that's something
I'm very excited about and I think that
is an example of something where we can
really benefit from collaborating across
multiple labs.
Anonymous asks, "Will you ever open
source some of your old models like the
original GPT4?" Um, we might do those as
museum artifacts someday, but they're
not like GPT4
is not a particularly useful open source
model. It's big. It's not that good. Uh,
you know, we could probably make
something that is beyond the power of
GPT4 at a very tiny scale. Uh, that
actually would be useful to people. So,
for useful things, I expect more things

[00:39]
like that. For uh for fun museum
artifacts, yeah, someday, who who knows?
Like I think there could be a lot of
cool things like that. Another anonymous
or maybe the same one asks, "Will you
admit that your new model is inferior to
the previous one and that you're ruining
your company with your arrogance and
greed while ignoring users needs?" Um,
I believe that it is inferior to you for
your use case and we would like to build
models that are better for your use
case. on the whole uh we think for most
users it's a it's a better and more
capable model but we definitely have
learned things about the 40 to5 upgrade
and we will try to do much better in the
future both about better continuity and
about making sure that our model gets
better for most users not just sort of
people that are using AI for science or
coding or for whatever
uh Y asks will there ever be a version
of chatbt meant for personal connection
and reflection not only business or
education yeah for sure this is this
We think this is a wonderful use of AI.
Um, we're very touched by how much this
has meant to people's lives. We get all
of us get a ton of emails and outreach

[00:40]
from users about how Chacht has helped
people in difficult personal situations
or to live a better life. And like this
is what we're here for. I mean, this is
like as important as anything that we
do. Like we we love to hear about
scientific progress. We love to hear
about people that, you know, got
diagnosed with the disease and got
cured.
The personal stories are incredibly
important to us and we're thrilled about
that and we absolutely want to offer uh
such a service.
Your safety oh
uh okay two parts of this two questions
that are about tide uh from G and
anonymous. Your safety routing breaks
user trust and workflows by overriding
our choices. Will you commit to revoking
this paternalistic policy for all
consenting adult users and stop treating
us like children? Uh when do users get
control over routing? Where's the
transparency on safety and censorship?
Why can't adults pick their own models?
Yeah, I I don't think the way we handled
uh the model routing was our best thing
ever. There there are some real problems
with forro. Um and we have seen a

[00:41]
problem where people are forming people
that are in fragile psychiatric
situations using a model like 40 can get
into a worse one. um most adult users
can use those fine, but we do, as we've
mentioned, we have an obligation to
protect minor users. And we also um have
an obligation to protect adult users who
are not in a frame of mind where, you
know, we're reasonably likely that
they're choosing what they really want
and we're not causing them harm. as we
build age verification um in and as we
are able to differentiate users that are
having like a true um mental health
crisis from users who are not uh we of
course want to give people more user
freedom as we mentioned that's one of
our our platform principles um so yes
expect improvement there and I don't
think this was our best work and how we
communicated the previous roll out
how we strike the right balance between
protecting people and allowing adults to
speak about difficult things without
feeling policed
you want to say anything there?

[00:42]
Yeah. So, so,
so the definitely there is a problem
where um we we we
aim to lay out the kind of high high
level um
policies and and guidelines for the
model in in in the spec uh that we um
that we develop for for CH GBT. But um
the the the the
space of of of of of situations you can
find yourself in is is is is enormous
and and and um and at some point kind of
like establishing the the right
boundaries really becomes a a tough
intelligence problem. Um and so we are
seeing uh
improved results on this matrix from
reasoning models and from expanding uh
more more reasoning on on thinking about
this uh uh software uh software

[00:43]
questions and and and trade-offs. Um,
of course, this is like a bit more
difficult to train for also than uh math
problems, for example. And and so this
is something that we're uh researching
quite heavily.
Uh Kate says, "When in December will
adult mode come? Will it have more than
just NSFW? when writing even slight
conflict when writing triggers filters
on for uh I don't know exactly when in
December it will ship but yes the goal
is um when you are writing when you are
using open AAI to help chat to help you
with creative writing um you it should
be much more permissive in in many
categories than the previous uh models
are again we want this and we know users
want this too um if this is going to be
your personal tool it should help you
with what you're doing and every time
you hit a content filter for something
that
uh you know feels like it shouldn't. We
we understand how annoying that is. So
uh we are uh we're going to try to fix

[00:44]
that with adult mode. There may be new
problems that we face, but we want to
give people uh more flexibility.
Uh anonymous says, "Why does your idea
of safety require lying to users about
what model they're actually using?" Uh
again, I think we mis rolled this one
out, but the goal here was to let people
continue to use Forro, but in the
situations where Foro has behavior that
we think is actually really harmful
before we have all of the age gain in
that we'd like to kick it uh to to put
the user into a model where they are not
going to have some of the mental health
problems that we faced with for um FORO
was an interesting challenge. It's a
model that uh some users really love and
it was a model that was causing some
users harm that they really didn't want
and I don't think this is the last time
we'll face challenges like this with a
model. Um but we are trying to figure
out the right the right way to balance
that.
Um will we legacy models back for adults
without rewriting rewriting? Yes. Uh, y,
will the December update officially
clarify OpenAI's position on human AI

[00:45]
emotional bonds? Uh, or will
restrictions continue implicitly
defining such connections as harmful
worldwide?
I I don't know what it means to have an
official position like we build this
tool, you can use it the way you want.
If if you want to have like a small R
relationship and you're getting
something like empathy or friendship
that matters to you and your life out of
a model, like it's very important to us
that the model faithfully communicate
what it is and what it isn't. But if you
as the user are finding value in that
support, again, we think that's awesome.
Like we we are very touched by the
stories of people who find
value, utility, a better life in the
emotional support or other kinds of
support they get from these models.
Kylo says, "How is OpenAI increasingly
allowing so many features for the free
version users?" I can answer this from a
product and business perspective, but
Jakob, I think it might be useful for
you to just talk about the incredible
rate at which models are getting more
capable for lower prices and less
amounts of compute. Um yeah, we we are

[00:46]
seeing quite a lot of uh
um
ability as we get to like the new
frontiers of intelligence to to to
reduce the cost for that quite quite
quickly. Um
and so yeah, especially especially with
reasoning models, we've seen uh that
actually quite uh quite cheap models
when allowed some some additional test
time compute can become much more
capable. Um
yeah, and so this is uh this is
something that I expect will continue.
And so um yeah, as we talk kind of about
about um you know, getting to these um
new frontiers and automating research
and so forth, I I I expect that the cost
of of of a lot of that will will keep
falling quite a lot too. So yeah, our
our
we talk a lot about the increase in
model capability and for you know

[00:47]
pushing forward science that's that's
hugely important. One of the most
amazing things that I've observed about
AI is over the last few years, the sort
of price of a particular unit of
intelligence has fallen about 40x per
year for the last few years. Um, so when
we first,
you know, when we first had like GPT3,
we thought it was very cool and it was
at this cost that was kind of hard and
like GP3 scale models now basically run
for free like on a phone or something.
um the cost of a model that's as smart
as GPT4 at the time we launch it
relative now has fallen hugely and we
expect this trend to keep going. Now we
still think we need a ton of
infrastructure because what we continue
to find is the cheaper we can make it
the more people want to use it and I
expect that only to increase but our
goal is to drive the you know cost of
intelligence down and down and down and
have people use it for more and more
things that will allow us to continue to
offer lots of features for free. Um, but

[00:48]
that will also mean, I think, that
people who really want to spend a lot on
pushing AI to the limit to cure a
disease or figure out how to build a
better rocket or whatever will spend a
huge amount. Um, we are committed to
continuing to put the best technology we
can uh as long as we can make the
business model even sort of work into
the free tier and you should expect a
lot more from us there over time.
Uh, okay. Anonymous asks, "Will an age
will an age verification start that
allows users to opt out of the safety
route or a waiver that could be signed
releasing open air from any liability?"
Um, we're not going to like do again,
we're not going to do the equivalent of
selling heroin or whatever, uh, even if
you sign a liability. But yes, on the on
the principle of treat adult users like
adults, if you're age verified, you will
get quite a lot of of flexibility. We
think that's important and clearly it
resonates with the people asking these
questions. Um, anonymous also asks, "Is
chatbt the ask jeieves of AI?" We sure

[00:49]
hope not. We don't think it will be. Uh,
okay. Since we only have 10 minutes
left, we're going to um, and some of
these touch other things that we've uh,
we've already touched on. We're going to
skip down through some of the same
questions and try to get to more. Uh, in
future qu sessions, we can um, do more
of these if we don't get to everything
here. Um,
just as the Macintosh, no asks, just how
the Macintosh was the precursor to the
iPhone, do you see Chacht as the OpenAI
product or do you see it as a precursor
to something much greater that truly
reshapes the world?
Um,
so I would say like as a research lab,
um,
well, we haven't set out to build a a
chatbot originally, although I think
we've since come to appreciate how
aligned this this product is with with
our overall mission. Um, and we of
course expect Chad GPT to continue to
become better and and and and be this

[00:50]
way um for people to interact with
increasingly advanced AI. Um but we do
anticipate that uh eventually AI systems
will be capable of um
creating valuable artifacts of actually
pushing scientific progress forward as
we were discussing and um I believe that
will be the the real lasting legacy of
AI. I I think the chat interface is a
great interface. It won't be the only
interface, but the way that people use
these systems um will
change hugely over time. If you think
about what Yakob shared earlier of the
5-second, 5 minute, 5 hour tasks, um if
you think about a 5year or five century
task that would take something that
would take humans, it's hard to even
think about what that means. But
probably you want a different kind of of
product experience. I also think you
probably will want this to feel more
like a sort of ambient always present

[00:51]
companion. Like right now you can ask
Chacht something. It can do something
for you. But it'd be really nice to have
a service that was sort of just
observing your life and proactively
helping you when you needed it and you
know helping you come up with better
ideas and just I I think we can probably
push very hard in in that direction.
Um Neil asks, "I love GPT 4.5. It's by
far the best on the market for writing
and it's the main reason I pay for Pro.
Could we get some clarity on its future,
please?
Um, we think we're going to have models
that are much better than 4.5 very soon
uh and for writing much much better. We
plan to keep it around until we have a
model that is a huge step forward in uh
writing. But, you know, we'd like to we
don't think 4.5 is that good anymore.
We'd like to offer something much much
better.
>> But yeah, we are definitely not done
with that direction of research. Uh and
yeah, we we expect combining combining
that with with uh other things we're
working on, we'll get wheels are
dramatically better than 4.5 on all
axis. Do you have uh any sense of timing

[00:52]
to share about when you think we have a
model that is dramatically better than
4.5 on on this kind of task like writing
and also anything about like how far
that's going to go?
>> Um next year I think is definitely
what I expect.
Um, when is Chach Atlas for Windows
coming? asks Lars. Uh, I don't know an
exact time frame. Some number of months,
I would guess. Uh, it's it's definitely
something we want to do. And more
generally, this idea that we can build
experiences like browsers and new
devices that let you take AI with you
that get towards this sort of ambient
always helpful uh assistant rather than
something you just query in response. uh
this will be a very this will be a very
important direction for us to to push
more on.
Will you disclose the documents with the
opinions of the 170 experts so that
we'll have some transparency regarding
the new justifications for model
behavior? Um I will ask Fiji Simo uh how
she'd like to handle that, but I think

[00:53]
we could I don't know exactly what we'll
be able to share, but I think we should
do something there. And I I think more
um more transparency there is a good
thing. Anonymous says, "I've been a
prouser since month two. As a researcher
and fiction writer, I feel GPT helps me
think clearer. I lost the question." Um,
sorry, that was a really good question.
Let me try to find it again.
Uh, clearer but not freer. Has
imagination become an optimization
casualty?
What do you think?
Um
it is
I think it is definitely possible for
current systems that uh you know like I
think if you compare a model like 4.5 to
a model like 03 I would expect that like
there will be trade-offs there. I I
think there are definitely like
transitory as we like figure out our way
around these technologies and so again
like I expect this will this will get
better. Yeah, I

[00:54]
I I think there are going to be
population scale like one one of the
sort of strange things I've noticed is
people in real life talking in like
CHBTE
uh where they sort of use some of the
quirks of of things ChachiBT says and I
I think there will be other things like
this where there's like this
co-evolution of people and the
technology in ways we can't totally
predict but my expectation is over time
people are much more capable, much more
creative, think much more expansively
and much more broadly than they do
today. Um, and we start
we certainly see examples of this uh
where people are just like I never would
have been able to keep this in my head.
I never would have been able to have
this idea. And then we hear other
examples where people say, you know,
I've outsourced my thinking and I just
do what this thing tells me. And
obviously we're much more excited about
the former than the latter.
Um, can you help us understand why you
build emotionally intelligent models and
then criticize people for using using it

[00:55]
for accessibility reasons when it comes
to processing emotions and mental
health? Uh, again, we think that's a
good thing. We want that. Uh, we're
happy about that. There the same model
that can do that can also be used to
encourage delusions and mentally fragile
users. And what we want is people who
are using these models intentionally.
The model is not deceiving the user
about what it is and what it isn't. the
model's being helpful, the model's
helping a user accomplish their goals.
We want more of that and less of
anything that would feel like the model
tricking a user, for lack of a more
scientific word. Um, I totally get we
totally get the the frustration here
like to, you know, whenever you're
trying to stop something that is causing
harm, you stop some perfectly good use
as well. Um, but please understand the
place we're coming from here is trying
to
provide a service to adults that are
aware of it and that are getting real
value from it and not cause unintended
harm to people who who don't want that
along along the way. Um, all right.
Given that we have just a couple of
minutes left, let's see if there's any

[00:56]
questions in very other directions that
we should try to get to.
Okay. Uh, when do you think massive jobs
loss will happen due to AI from Razi?
So I think I think
already we are at a point where I think
a lot of the um
um the gap that stops that stops present
models from like being able to perform a
lot of um intellectual jobs. uh it's
more about um integrations and
interfaces
uh than maybe raw intellectual
capability. Um and so I think we
definitely have to

[00:57]
uh
think about that um uh think about
automation of of of a lot of jobs is
something that um will be happening over
the next years. And I think this is a
big uh
thing for for for for us to to
collectively think about like what are
uh
what are the jobs that will will replace
those and uh and what are the kind of
new pursuits that we'll that that we'll
all engage on.
>> This is a question from me not from uh
not from the live stream. What what do
you think meaning will look like? Uh
what do you think the jobs of the future
will look like? How do you think when AI
automates a lot of the current things
like how do you think we'll derive our
fulfillment and spend our time?
>> Um
I I expect um

[00:58]
yeah well I I think this is a this is a
quite um
philosophical question. I think I I
think can go in many directions but some
things I expect I think the high level
goal setting right like picking what
pursuits uh um
we're we're chasing that is something
will remain human and and
uh and I think that that is something
that a lot of people will derive meaning
from. Um, I think also just the ability
to
understand so much more about the world,
the wide the incredible variety of of of
new knowledge and new also
entertainment, but al also
uh
um just intelligence that that that that
that
will be in the world. I think I think

[00:59]
will uh will provide quite a lot of
meaning and fulfillment for people.
>> Okay, rapid fire, two minutes. Uh Shindi
says when GBT6
um
I think I think I think uh in some ways
maybe that's more of a question for you
uh in that like um I think I think with
with with GPD with GPD 5 uh we have uh
with previous models right like uh like
GPD4 GPD3 like we've kind of like kept
very tight uh connection of like how h
how we're training new models like what
are the products that we ship
And as I was just saying like I think
right now there's a lot to do on the
kind of integration side and on on the
uh so for example with GPT5 is the kind
of the the first time we really bring
reasoning models as kind of our our
flagship our main flagship model. Um and
so uh we're we're not coupling like
these releases and these products as
tightly to our research program anymore.

[01:00]
>> Yeah. Um I don't know either exactly
when we'll call it that but I think a
clear message from us is say 6 months
from now probably sooner we expect to
have huge steps forward in model
capability. Felix asks is an IPO still
planned and how would the structure then
look like? Are there rules in place for
increasing capital? Um we don't have
like specific plans or this is exactly
when it's going to happen but I think it
it's fair to say it is the most likely
path for us given the capital needs that
we'll have in sort of the size of the
company. Um, but you know that's not
like a top of- mind thing for us right
now. Alec asks, "You mentioned being
comfortable with the 1.4 trillion of
investment. What level of revenues would
you need to support this over time? What
will be the largest revenue driver? It
can't just be a per user subscription."
Um, you know, eventually we need to get
to hundreds of billions of a year in
revenue and and we're on a pretty steep
curve towards that. I expect enterprise
to be a huge revenue driver for us, but
I think consumer really will be too. And
it won't just be the subscript
subscription, but we'll have new
products, devices, tons of other things
there as well. Uh, and this says nothing

[01:01]
about like what it would really mean to
have AI discovery and science and all of
the revenue uh um possibilities that
that would unlock. And as we see more of
that, we will uh we will increase spend
on infrastructure. Okay. Um, we are out
of time. Thank you all very much for
joining us and the questions. and we
will try to learn from this format and
iterate on it and keep doing uh these
sorts of Q&A. Thank you very much.

</details>
