---
title: "OpenAI DevDay 2024 | Community Spotlight | Swyx"
channel: openai
url: https://www.youtube.com/watch?v=wnsZ7DuqYp0
youtube_id: wnsZ7DuqYp0
published: 2024-12-17
duration: "9:40"
captions: en-orig
---

# OpenAI DevDay 2024 | Community Spotlight | Swyx

[![OpenAI DevDay 2024 | Community Spotlight | Swyx](https://img.youtube.com/vi/wnsZ7DuqYp0/hqdefault.jpg)](https://www.youtube.com/watch?v=wnsZ7DuqYp0)

<details>
<summary>자막: OpenAI DevDay 2024 | Community Spotlight | Swyx (9:40)</summary>

[00:00]
hi everyone okay so I'm supposed to
bring up this as though as a cooking
show and it was already pre prepared um
I'm s or Sean I'm natively from
Singapore but I've been working and
living in the states for the past 15
years um and uh I have a secret I have a
couple secret agendas first of all um I
was given I was I thought I had 25
minutes then I was given 15 minutes and
now 10 and then today I was told it was
9 minutes so I'm going to give you a ton
of homework and don't worry you can take
photos all these but uh everything's
already on my website uh 6i engineering
agents um and so I'll just give you a
title homelet because my my you know I'm
just I'm not going to like uh dump
things down just uh for you the second
thing second agenda I really have is on
the 30-year Horizon I want to turn
Singapore into an AI engineering Nation
uh I want every single one of you to
understand how much power you have uh
with the foundation models that are
available to us today um and to respect
that um you know there's so much

[00:01]
knowledge is being shared publicly by
all the other engineering organizations
so I'll go Dive Right into this the
reason this talk is awkwardly named is
because I wanted to kind of squeeze some
form of AI engineering into the talk
title um I'm very well known for this
essay on the rise of the AI engineer
speing out this sort of specialist role
for software Engineers building with AI
um and particularly uh my the podcast
that I've been running with alesio
alesio where where you at hey um uh we
we both basically focus on AI
engineering covering all the builders
and researchers in the space and
including one episode with Minister
Josephine too on turning Singapore into
an AI engineering Nation so highly
recommend checking that out if you are
interested um personally I've also been
building small AI agents um so I I have
a news um newsletter that reports on the
top AI discords reddits and twitters
every single day it's the biggest AI
newspaper with no journalists and you
can also build this yourself so
basically I'm here to just condense
everything that we've learned on
building AI Agents from talking to

[00:02]
people from building it ourselves and
and all that um and um I think the main
starting point I recommend to people is
from lilan Wang uh she is a very
well-known uh writer but also formerly
head of uh Safety Systems at open a and
she says agents are llm plus memory plus
planning plus two use um I personally
tend to modify that a little bit um and
we'll go into that in a little bit of
detail but each of each of my slides has
homework at the bottom and you can
obviously um see the sort of slides
presentation that the at the end of this
talk
um so a lot of my thinking about
developer tools comes in impossible
triangles like this vend diagram of like
you start here and you know eventually
you start adding the features of
competitor tools and where should you
really pick pick um and I think having a
clear map of what jobs to be done uh for
building sort of your LM infrastructure
is really important so I tend to
recommend having some kind of Gateway
some kind of Ops tool some kind of rag
framework uh the top ones are all the
open source tools that I use um I also
want to especially shout out Eugene Shia
where are you um who who runs feedist AI

[00:03]
um uh and so like there's a lot of
prominent singaporeans who are actually
working on uh this this AI so I I I I
highly recommend you checking out Eugene
work and fist AI as well the second part
of the stack that is really emerging for
agents is memory and knowledge uh not
enough people still appreciate chat gbt
including memory in February of this
year it feels like an eternity ago but
uh it's still a very good Agent uh
memory implementation and I highly
recommend reading the M GPT paper if
you're interested in that on the
knowledge site uh Vector DB is are very
well known but increasingly U of of a
lot of interest is knowledge graphs I
would say the most surprising popular
talk at the conference that I run AI
engineer conference uh was the graph rag
talk again I leave your homework to
check it out as well the third part of
the stack is kind of the most the most
of vague um area of active research this
is planning and multi-agent um here I
would recommend people read a couple
things from openi one it's the let's
verify step-by-step paper which shows
the potential process War models um and
then secondly the SW F uh project which

[00:04]
is a project that's not a framework
worked on by Elan and shamal I think who
are here in the audience as well um and
so highly recommend multi-agent as as
the single simplest Improvement in um
performance grab was also talking about
that's their what they aspire to next
and at the end of this talk I'm going to
show you a demo of how multi-agent
actually improves the experience by
quite a
bit um together and and I think the last
part of St is sort of tools and
orchestration I kind of jam them
together in in the same place it's no
coincidence that when Lang chain
launched the first three things that
first three features that they launch
with were these three things that
eventually every single agent eventually
needs to have so the first is a code
interpreter like a Sandbox environment
like e2b that executes code and and runs
all the deterministic things that llms
cannot run second thing is browser
control by being able to surf the
Internet to search for results um and to
sort of read from using the computer
then lastly is the self ask or react
Loop where you sort of uh do this sort
of cycle of observing and reacting to
the external environment um and

[00:05]
um these these tend to be the building
blocks of all agent systems whether it's
magentic from Microsoft which I highly
recommend checking out or cognition
which um I think um you know opening eye
works really closely with and also spoke
into into their architecture at the uh
their specific talk in my conference so
highly recommend uh checking out all
these talks if you're interested and
lastly this is my brain down Talk Brain
down slide where I'm like basically
making the meta point that everything I
just told you was like parts of the
stack that is well known that you're
going to need to build agents I think
the meta lesson for AI Engineers is to
have some kind of mental map of
capabilities because every single time
there's an advance in model capabilities
there's actually an opportunity for you
to build a state of-the-art agent by
utilizing those features so that's
something I want to really try to show
you uh in My Demo today um I'm very
inspired by this sort of scene in Iron
Man where basically he's kind of talking
to his computer and just kind of
manipulating directly the the the thing
that he's working on and I think that
the lot of coding should actually move
closer towards direct manipulation so I

[00:06]
really am interested in showing that off
um and I hacked on this a little bit uh
in my free time so um I'm going to show
an uh a fork of bolt. new which is an
open source sort of text prompt to app
creator uh and we're going to make a
Space Invaders game this is all standard
bolt. newu stuff uh it's basically just
going to like based on a very small
prompt of make a fastpac space evors
game by the way we're using uh today's
GPT 40 version be nice if we have like
daily uh cuts of GPT 40 right
um and uh yeah I mean it it like creates
a pretty decent app but it doesn't
really look like Space Invaders so the
second thing I did is I'm going to add a
second agent to talk to this first agent
and I'm going to use voice because I I'm
very obsessed withal voice hey um so uh
we have this space Anders um game but uh
the aliens are not really sort of coming
in waves I want come them I want them to
come in waves and to fall down in
discreet steps can you do
that okay I've asked the code Jenny I
think the way that I want to code is

[00:07]
just to QA I should play the game call
out like what I don't like about they
too fast and it should just be working
on it in the background so here it is
it's been fixed um it's just pretty cool
all right but like it's not still not
engaging enough I need all my like sort
of dopamine hits uh so like every time
an alien dies can you drop a special
bonus some kind of PowerUp feature um
and also like let's maybe add um some
sparkling stars in the background to
make it feel more like space and then
also lastly maybe let us do uh make the
aliens look more aliens use alien emojis
and make the spaceship look more like a
spaceship can you do
that great so I just gave a triple
prompt it's all squeezed in one there
and if you use an agent that has a
planning stage you can actually split
that out and manage each of those things
step by step this is exactly what we're
doing inside of here um again I don't
have the BWI to give you the source code
or anything like that for for this uh
but it's just kind of building back
consider it a visual upgrade a little
make

[00:08]
uh so yeah it's kind I like the I like
the powerups it's very cool um and I I
think like this sort of human AI
collaboration I think is really powerful
by the way um any any audience
suggestions like I can take audience
participation this a real life
demo make them shoot back can you make
the aliens shoot back at me so I can
potentially
lose oh I just love that I can speak
features into existence all I'm doing is
kind of QA the game get ready to dodge
and it's it makes for such a much better
flow it's like it's kind of like we're
living in the age of iron is just an
opportunity to practice your dramatic
defeat scene ready for the laser oh oh I
lost okay well yeah that's uh that's
about it
um really really
fun so what is my thank you uh by the
way that demo is open uh we also have
I've also will be publishing on the
Laten space newsletter all the learnings
that we've had building the real time
API we call it sort of um the uh Missing

[00:09]
manual to the opening eye real time API
that was the BB I was working on guys um
so what's the overall lesson is that you
can build so much with this core
understanding of the agent stack um I
think you as software Engineers don't
have to be PhD level researcher to do it
um I I I feel I think it's so
understated how much potential there is
in Singapore in all of you building with
uh with these Foundation models and it's
so underrated how opening eye values you
like flying all there San Francisco us
team here to talk to you so I hope you
take advantage of this opportunity and I
hope that we all collectively turn
Singapore into an AI engineering Nation
thank you very much

</details>
