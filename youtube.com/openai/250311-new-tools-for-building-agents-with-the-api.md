---
title: "New tools for building agents with the API"
channel: openai
url: https://www.youtube.com/watch?v=hciNKcLwSes
youtube_id: hciNKcLwSes
published: 2025-03-11
duration: "19:45"
captions: en-orig
---

# New tools for building agents with the API

[![New tools for building agents with the API](https://img.youtube.com/vi/hciNKcLwSes/hqdefault.jpg)](https://www.youtube.com/watch?v=hciNKcLwSes)

<details>
<summary>자막: New tools for building agents with the API (19:45)</summary>

[00:00]
hey everyone I'm Kevin and I lead
product at open aai today we're here to
talk developers and agents and in
particular we're excited to launch a
bunch of new tools that make it easy for
developers to build reliable and useful
agents now when we say agent we mean A
system that can act independently to do
tasks on your behalf and we've launched
two agents this year in chat PT the
first is uh operator which can browse
the web and do things for you on the web
the second is deep research which can uh
create detailed reports for you on any
topic you want so you give it a topic
and it can go off and do what might be a
week's worth of research for you and
come back with an answer in 15 minutes
now the feedback for those has been
fantastic but we want to Now launch
those tools and more in the API to
developers so we've spent the last

[00:01]
couple months going around talking to
developers all over the world about how
we can make it easy for them to build
agents and what we've heard is that the
models are ready so with Advanced
reasoning with multimodal understanding
our models can now do the kind of
complex multi-step workflows that agents
need but on the other hand developers
feel like they're having to Cobble
together different low-level apis from
different sources it's difficult it's
slow it often feels brittle So today
we're really excited to bring that
together into a series of tools uh and
and a new API and an open source SDK to
make this a lot easier so with that let
me introduce the team yeah hi I'm Elan
I'm an engineer on the developer
experience team I'm Steve I'm an
engineer on the API team and I'm Nik I
work on the API product team so let's
dive into all the stuff that we are
launching today like Kevin mentioned we
have three new built-in tools we have a
new API and an open source SDK uh
starting off with the built-in tools the

[00:02]
first tool that we're announcing today
is called the web search tool the web
search tool allows our models to access
information from the internet so that
your responses and the output that you
get is up to-date and factual uh the web
search tool is the same tool that powers
chat gbd search and it's powered by a
fine-tuned model under the hood so this
is a fine tuned gbd 40 or 40 mini that
is really good at looking at large
amounts of data retriev from the web
finding the relevant pieces of
information and then clearly citing it
in its response um in a benchmark that
uh measures uh these type of things uh
which is called Simple QA uh you can see
that gbd 40 hits a high score of
state-of-the-art score of
90% so that's the first tool Steve do
you want to tell us about the second one
yeah the second tool is actually my
favorite tool and this is the file
Search tool now we launched the file
Search tool last year uh in the
assistance API as a way for developers
to upload chunk embed their documents

[00:03]
and then do really easily do uh rag
really easily over those documents now
we're really excited to be launching two
new features in the file Search tool
today the first is metadata filtering so
with metadata filtering you can add
attributes to your files to be able to
easily filter them down to just the ones
that are the most relevant for your
query the second is a direct search
endpoint so now you can directly search
your vector stores without your queries
being filtered through the model first
nice so you have web search for the
public data file search for the the
private data that you have and then the
third tool that we are launching is the
computer use tool the computer use tool
is operator in the API but it allows you
to control the computers that you are
operating so this could be a virtual
machine it could be a legacy application
that just has a graphical user interface
and you have no API access to it if you
want to automate those kind of tasks and
build applications on that you can use
the computer use tool which comes with
the computer use model um so this is the
same model that is used by operator in
chat gbt it has soda benchmarks on uh OS

[00:04]
World web Arena web Voyager early user
feedback on the Kua model and the tool
has been super super positive so I'm
really excited to see what all of you
built with it all right so those are the
three tools um and while we were
building these tools and thinking of
getting them out we also wanted to take
a first principles Approach at designing
the best API for these tools um we
released chat completions I think in
March 2023 alongside gbd 3.5 5 turbo and
every single API interaction at that
time was just text in and text out since
then we've we've uh introduced
multimodality so you have images you
have audio we're introducing tools today
and you also have products like 01 Pro
deep research operator that make these
multiple model turns and multiple tool
calls behind the scenes so you wanted to
build an API primitive that is flexible
enough it supports multiple terms it
supports tools um and we're calling this
new API the respon API and to show you

[00:05]
the responses API I'm going to hand it
over to Steve cool let's go ahead and
take a look at the responses API so if
you've used chat completions before this
will look really familiar to you you
select some context you pick a model and
you get a response that's pretty simple
it's pretty
simple and it's always hilarious so
maybe not I don't know um so to
demonstrate the power of the responses
API we're going to be building sort of a
personal stylist assistant so let's
start by giving it some instructions you
are a
personal stylist you're only typing in
front of like 50,000 people right now
don't worry about
it cool and we'll say uh we'll get rid
of this and we'll
say what are some of the latest
trends the jokes in the context the joke
is in the let's see what it
says okay okay cool great um but no

[00:06]
personal stylist assistant is complete
unless it understands what its users
like so in order to demonstrate this
we've created a vector store that has uh
some you know like some entries almost
some diary entries of what people on the
team have been wearing um we've kind
that's not weird at all it's not weird
at all I would just let it happen uh
we've kind of been following people
around the office and kind of like
understanding what they what they've
been up to so we we we uh we yeah
there's a whole there's a team there's a
team on it
yeah so go ahead and add the file Search
tool and uh I'll copy in my Vector store
ID and here I can actually filter down
this the files in this Vector store to
just the ones that are relevant to the
person that we want to style so uh in
this case let's start with Elon we'll go
ahead and filter down to his
username and we'll come back here and
we'll refresh and we'll say uh can you
[Music]
briefly

[00:07]
summarize what Elon likes to
wear I often ask chat GPT this question
yeah but it never knows and now it can
actually tell you what Alon lookes
to cool so Elon has a distinct in
consistent style characterized by Miami
Chic that's really
awesome um so the file Search tool is a
great way to bring information about
your users into your application but in
order to be able to create a really good
application for this personal stylist we
want to be able to bring in fresh data
from around the web um so that we have
both the newest information and also
stuff that's really relevant to your
users so in order to demonstrate that
I'll add the web search
tool cool the web search tool is really
great because you can also add loc you
can also add data about like where your
user is so let's try with somebody else
Kevin are you Happ going to be taking
any trips anytime soon let's say Tokyo
okay cool Tokyo so I'll put in Tokyo
here and we'll swap in Kevin and the

[00:08]
responses API is really cool because it
can do multiple things at once it can
call a file Search tool it can call the
web search tool and it can give you a
final answer just in one API response so
in order to tell it exactly what we want
let's give it some
instructions and it'd be good if I knew
how to code well great you say you're an
engineer here yeah well I'm in
training so uh what we want we want the
model to do is when it's asked recommend
products we wanted to use the file
Search tool to understand what Kevin
likes and then use the web search tool
to find a store near him where he can
buy something that he might be
interested in so let's go back and say
uh find me a
jacket um that I would
like
nearby and what the model will do is it
will uh issue a file Search tool call to
understand what kinds of things Kevin
likes to wear and then it will isue a
web search tool call to then go and find
uh stuff that Kevin would like based on

[00:09]
where he is so the model was able to uh
just in the scope of one API call find a
bunch of Patagonia stores in Tokyo for
you Kevin which which go it actually
corresponds to Kevin's preferences he's
been wearing a lot of Patagonia around
the office so um but no personal stylist
assistant would be complete unless they
could actually go and make purchases on
your behalf so in order to do that let's
demonstrate the computer use
tool so we'll go ahead and add this
we're using the computer use preview mod
mod and the computer use preview tool
and we will ask um help me find my
friend Kevin a new
pagonia jacket what's your favorite
color Kev uh let's go with black and
black can't have too many black patagon
jackets and what the model will do is it
will ask us for a screenshot and we have
a Docker container running locally on
this computer and we will go ahead and
send that screenshot to the model it
will look at the state of the computer
and issue another action click drag move

[00:10]
type and then we will execute that
action take another screenshot send it
back to the model and then it will
continue in this fashion until it feels
that it's completed the task and then
return a final answer so well this is
kind of going and doing its thing we'll
hand it back to nun yeah awesome so
these are some really cool tools and a
really flexible API for you to build uh
agents and and you have you have amazing
building blocks to to do that now but
for those of you who have built more
complex applications like say you're
building a customer support agent it's
not always about just having one agent
that's sort of the personal style uh
stylist you also have some uh agentic
application that's doing your refunds
you have another thing that's answering
customer support uh FAQ queries you have
something else that's dealing with
orders and billing Etc and to make these
applications easy to build we released
an SDK last year called swarm and swarm
made it easy to do agent
orchestration this was uh supposed to be
an experimental and educational thing
but so many of you took it to production

[00:11]
anyway so uh you're like forcing our
hand over here and so uh we've decided
to take swarm and make it production
ready add a bunch of new features and
we're going to be rebranding it to be
called the agents SDK Elan built uh
swarm uh and help build it so I'm going
to have hand it over to him to tell you
more about how it works yeah thanks nun
yeah so uh in my time at open AI I've
spent a lot of time working with
Enterprises and Builders to help them
build out agentic experience
and I've seen firsthand how pretty
simple ideas can actually grow in
complexity like when you actually go to
implement them and so the idea with the
agents SDK is to keep Simple ideas
simple to implement while allowing you
to build more complex and robust ideas
still in a pretty like straightforward
and simple way so um let's take a look
at what Steve had before in the demo but
implemented using the agents s it's
going to look very similar at first we
have our agent defined here we have some
instructions
um and we also have both of the tools

[00:12]
file Search tool web search tool that we
had before is this using like responses
under the hood yeah so by default this
is using the responses API but we
actually support multiple vendors
anything that really fits the chat
completions um shape can work with the
agents SDK nice so um during the
practice runs we actually we actually
accidentally ordered like many many
pagonas so I'm sorry we're have I
understand what's the problem we're
helping you here uh want to return some
of them uh and so to do that I could
usually just add in like a returns tool
and like add more to this prompt and get
it to work but the problem with that is
you start to mix all of this business
logic which makes your agents a little
bit harder to test and so this is the
power of multiple agents is you can
actually separate your concerns and
develop and test them separately so to
do so let's actually introduce a like an
agent specifically to deal with the
sorts of uh like returns so I'm going to
load mine in and great so we still have
our agent from before but you can see

[00:13]
there's also this new agent the customer
support agent here and I've defined a
couple tools for it to use the guest get
passed orders and then submit refund
request and um you might notice these
are just regular python functions as
this is actually a feature that we
people really loved in swarm that we
brought over to the agent SDK which is
we'll take your python functions and
look at the type inference or look at
the type signatures and then
automatically generate the Json schema
that the models need to use to perform
those function calls and then once they
do we actually run the code and then
return the results so you can just
Define these functions um as as they are
now I've given them um now we have our
two agents right we have the stylist
agent and we have the customer support
refunds agent so how do we interact with
both of them as a user this is where the
notion of handoffs come in and a handoff
is actually a pretty simple idea it's
pretty powerful and it's when you have
one conversation where One agent is

[00:14]
handling it and then it hands it off to
another where you keep the entire
conversation the same but behind the
scenes you just swap out the
instructions and the tools um and this
gives you a way to triage conversations
and like load in the correct context for
each part of the conversation so what
we've done here is created this triage
agent that can hand off to the stylist
agent or the customer support agent so
enough talking let's actually see this
in action so I'm going to
save and do you know um I think we may
have ordered one too many
pagonas can you help me return I don't
understand I I know I'm so sorry I can
get you one
later so what just happened here is it
started off by transferring remember
we're starting with the triage agent um
to the customer support agent and this
is just a function call that I'll show
show you in a second um and then the
customer support agent proactively
called the get past orders function
where we can see all of Kevin's pedagog
I think you'll be

[00:15]
okay um cool so to actually see what
happened behind the scenes usually you
might need to add some debugging
statements by hand but one of the things
that the agents s brings right out of
the box is monitoring and tracing so I'm
going to go over to the tracing UI that
we have on our platform um to actually
take a look what just happened so these
are some of the previous runs that we've
had I'm just refreshing the page um and
we can see the last one uh and this last
one you can actually see exactly what
happened we started with a tree agent
which um we sent a request to made a
handoff and then switched over to the
customer support agent which called the
function
now uh we can see what the original
input was and handoffs are first class
objects in this dashboard so you can see
not only which agent we actually handed
it off to but any that it like it had as
options that it did not which is
actually a really useful feature for
debugging um afterward once we're in the
customer support agent you can see they
get get past orders function call with
any input prams Here There Were None um

[00:16]
and then the output is just again just
all of Kevin's very monotonous history
um and then finally we can get to the
end where you get a response and so
these are some of the features that you
get right out of the box with the agents
SDK there's a few more you uh we also
have built-in guard rails that you can
enable we have life cycle events um and
importantly this is an open source
framework so we're going to keep
building it out um and you can install
it like very soon or right now so you
can just do pip install open AI middle
Dash agents and we'll have an one for
the JavaScript coming soon um but to
close this off let's um let's let's
actually perform the the refund so uh
you know uh you know what I'm sorry
Kevin get rid of all of them
oh what am I going to
wear Kevin's going to be cold yeah let's
see it's a lot of them there we go takes
a while to return so many P gam and so

[00:17]
what what happens under the hood how do
you how do you debug this how do you
understand more about what's going on
yeah so that we can all do back in the
in the tracing in the tracing UI so this
is a pretty nice straightforward way to
build out these experiences yeah the
awesome pass to you I'm so excited for
all of you to have access to all of
these tools uh and before we wrap up I
wanted to make two additional points
first we've introduced the responses API
but the chat completions API is not
going away we're going to continue
supporting it with new models and
capabilities there will be certain
capabilities that require built-in tool
use and there'll be certain models and
agentic products that we release in the
future that will require will require
them and those will be available in
responses API only responses API
features are a superet of what chat chat
completions support so whenever you
decide to migrate over it should be a
pretty straightforward migration to you
and we hope you love the developer
experience of responses cuz be put a lot
of thought into that the second point I

[00:18]
wanted to make was around the assistance
API we built the assistance API based on
all the great feedback that we got from
all of our beta users and uh you know we
we wouldn't be here without uh without
all the learnings that we had during the
assistance API phase we are going to be
adding more features to the responses
API so that it can support everything
that the assistance API can do and once
that happens we'll be sharing a
migration guide that makes it really
easy for all of you to migrate your
applications from assistants to
responses without any loss of
functionality or data we'll give you
ample time to move things over and once
we once we're done with that we plan to
Sunset the assistance API sometime in
2026 we'll be sharing a lot more details
about this uh offline as well but yeah
that's it for me I'll hand it over to
Kevin to wrap us up awesome well we're
super excited to announce the the
responses API and the idea that we can
bring take a single powerful API and

[00:19]
bring together a whole bunch of
different tools from Rag and file search
to web search to Kua and our uh operator
uh computer use apis now um now you can
count on us to continue building
powerful new models and bring more
intelligence to bring more powerful
tools to help you build better agents
20125 is going to be the year of the
agent it's the year that chat GPT and
our developer tools go from just
answering questions to actually doing
things for you out in the real world
we're super excited about that we're
just getting started we know you are too
and we can't wait to see what you build

</details>
