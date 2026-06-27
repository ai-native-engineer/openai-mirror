---
title: "OpenAI DevDay 2024 | Community Spotlight | Cosine"
channel: openai
url: https://www.youtube.com/watch?v=NWoSLK1Z530
youtube_id: NWoSLK1Z530
published: 2024-12-17
duration: "15:12"
captions: en-orig
---

# OpenAI DevDay 2024 | Community Spotlight | Cosine

[![OpenAI DevDay 2024 | Community Spotlight | Cosine](https://img.youtube.com/vi/NWoSLK1Z530/hqdefault.jpg)](https://www.youtube.com/watch?v=NWoSLK1Z530)

<details>
<summary>자막: OpenAI DevDay 2024 | Community Spotlight | Cosine (15:12)</summary>

[00:00]
okay hi everyone um I'm Ally I'm
co-founder and CEO of cosign and at
cosign um we've built a product called
Genie um Genie is a fully autonomous um
AI engineer and the way that we built it
is that we fine-tuned gbt 40 with some
synthetically um augmented real world
data showing how developers complete
tasks the thesis behind this was
essentially
pre-training corpuses don't integrate
examples of software Engineers doing
tasks you tend to only see the finished
artifact of the task having been done
whether it be a PO request whether it be
a code file and so on so after all the
work that we've done to build this um we
found some useful techniques to share
when building a system around
fine-tuning and that's what I'm going to
share with you guys
today so fine-tuning um broadly I feel
like it's a very underutilized tool um
in the llm tool box but I feel like at
the moment it's essential for where your

[00:01]
product um Quality is truly Mission
critical um essentially for us we found
that we couldn't get the performance we
wanted to out of um base llms so we
decided to go to fine tuning to sort of
really specialize the model in one
versicle um it requires relatively few
examples generally speaking um but
detailed uh data handling is super
crucial so there's a massive time
tradeoff with fine tuning relative to
prompting you can get very far with a
prompted product in like a day but
fundamentally for that last 20% we found
that fine-tuning is what got us that
performance but in order to show the
model how to be a software engineer in
the same way as a human required a huge
amount of data cleaning and curation to
essentially synthesize data that just
doesn't exist in the real world right
the last thing we really learned on this
front was you have to be V driven um to
start with I think like a lot of people
we started just by Vibe checking on a
bunch of uh things that we that we
thought were important and then we very
quickly realized that what we thought
was important wasn't a tool

[00:02]
representative of what people widely um
were going to use the product for the
next thing um that I wanted to talk
about was reasoning so reasoning has
been one of the cornerstones within like
the llm um tool space for for a long
time this has been you know obviously
exemplified very recently with the
release of 01 and 01 mini um whil
building Genie essentially we we
leverage customized reasoning traces to
really make the model think more like a
human when it came to software
engineering specifically um we weren't
interested in generalized reasoning
across the board we just wanted it to be
able to think like I did or or we do
when we're solving a problem
specifically so for complex tasks um you
know software engineering being one of
them it it can make sense to change the
way the model thinks before giving an
answer um as I mentioned things like
Chain of Thought have been around for a
long time and can definitely mitigate um
some of the shortcomings and the
underlying model um and then what we
realized especially with the release of
um you know dedicated reasoning models

[00:03]
like 01 during the synthesis process you
can use those models to generate custom
reasoning traces um that you can then
distill into a into a smaller or more
primitive model um it's an ideal thing
to do when you have a desired output but
the model tends to not get there by
itself so say um for example in our
cases you often have a patch that you'd
ideally like the model to write if the
base model doesn't tend to write that
consistently using custom reasoning
traces can help be the glue that really
sticks what you want and what you um and
what you input to um together so an
example of this say for example you
wanted to fine-tune um a model to be
better at doing code review for example
so say for example you had a PR and you
left a review comment on the pr now a
really simple sort of way to start fine
tuning this might be to just take the pr
itself as an input and for the assistant
message um to be the review comment that

[00:04]
was left on the PR but the performance
that you'd get from that could be
boosted even further so imagine you take
the pr and the review comment and you
feed it into 01 for example here you can
ask 01 to speculate as to why was this
comment left for example so here we've
given it the pr we've given it the
comment and then 01 will go ahead and
figure out okay given everything that's
available to me here this is why the
user who left the comment left the
comment and that's extremely important
because otherwise um it's very easy for
for Bas models to just start pointing
out sort of irrelevant stuff and stuff
that isn't really what the human would
have thought in that moment and this
reasoning is that glue to try to get us
to converge to the output that a human
would give so once you've got that
output what your training sample would
be like in a fine-tuning situation would
be you'd have your PR as the input and
then you'd have the thought process that
01 gave you um produced first by the
model and then at the very end you'd
have the actual comment that was left by

[00:05]
the developer and this approach broadly
is um we use this heavily uh inside of
inside of Genie and this approach really
helped us converge to like the
preferable answer set that we really
wanted to um above the base model so the
next technique um I wanted to speak
about after reasoning was selfplay
selfplay is a really great technique to
generate as I mentioned earlier these
training examples which are hard to
obtain if if not are impossible to
obtain in the real world so for example
um if you wanted to um like build a
personal assistant that excelled at
browser based tasks it would be super
beneficial to use self players and
approach to generate these traces which
don't really exist in the real world the
call for us is whilst building gen as I
mentioned there are no examples of
software Engineers stepbystep retrieving
code figuring out what if they've
retrieved is relevant or not and then
starting to write a solution normally
you just see the end artifact so
selfplay allows us to synthesize these

[00:06]
traces um that you can then train the
model to replicate we um we utilized it
mainly around the um exploration and
retrieval of a code base um it's very
powerful even on very large code bases
talking about like 5 to 10 million line
code bases it's still very Adept at
figuring out um what it needs to find
and one of the latest things that we've
done in this bace is we've actually
started fine-tuning models that live in
our selfplay pipeline to be even better
at this um one of the one of the main
caveats for self play is it is a huge
Vector for um dirty data to make its way
into your final data set so cleaning is
extremely important on this front um and
it can be expensive however with things
like um you know 01 mini and so on that
model um is extremely good at selfplay
and is actually pretty cheap to run so
as a as a workr example this is kind of
what our selfplay pipeline looks like
you have a player model and a supervisor
model I'll come on to those and how they
work in a second but fundamentally you

[00:07]
have the original prompt that you'd like
the model to be able to figure out and
um the player model is just given the
prompt and then the supervisor model is
supposed to act as a sort of teacher in
this Loop um and it is given the prompt
and also the desired outcome so
depending on your use case this might be
the files that have to be retrieved in a
code base or the website that you'd like
your personal assistant to visit or
whatever right and the player model has
a set of tools that it can interact with
in our situation it's you know can you
read files can you search for perplexity
and so on um and the loop is very simple
The Prompt is given to the player the
request go the player will then think
okay I need to make a request to some
tools it will get the response and at
that point that entire context window is
sent over to the supervisor that then
judges that decision and gives some non
revelatory advice back to the player
model as to what it should do next so
let's just work through an example here
so say for example we wanted to do this
task to a codebase so make a change so
that the server fingerprint is returned
as a header on every HTTP response and
say that we know these are the three

[00:08]
files that we need to edit in order to
do this thing right the way this would
work is that that original prompt would
be delivered to the player the player
would think okay I'm just going to look
at what's in the in the code base I'm
going to start doing um I'm going to do
a search for I want to read this file
the tools will return that back to the
player and then the player is going to
say okay I'm going to send this context
window over to the supervisor and the
supervisor will look at the context
window as a whole and it will decide
okay the player has done well so far so
I'm going to say great start maybe next
you should look at how um the headers
are um are set right and in this
instance it's really crucial to tune the
supervisor to not reveal the answer to
the player we don't want to make any
logical leaps here we want to make sure
that the player is learning um as it's
going along how to converge to the
solution we don't want to just jump
directly to the solution so in this
instance the player would continue would
say okay as a result I might look at
headers dop I'm going to get that
response back and then that this whole
Loop continues until you reach the point

[00:09]
where all of the files that you were
looking for whatever your termination
condition is in this instance right so
in this instance the supervisor has
replied and then the model will do its
last um bit of retrieval and then we
found everything we need and we can stop
there um as I mentioned earlier this is
a great approach you can get even more
out of this by fine-tuning so one of the
things that we've done at cosign is we'
fine-tuned both the player and the
supervisor model and by doing that you
can get even more human reasoning out of
these models and you get convergence
much more quickly and the reasoning
looks much more similar to what you
would want and to get these models to
work well you don't need you know
thousands of annotations at most
probably a couple of hundred if you can
be bothered but at the end of the day
fine-tuning those models gets you a huge
amount of additional performance above
this already working system so what you
get at the end of doing this is you get
um what this is what your training
sample would look like this is what your
context window would look like so you
can see the player model has made these

[00:10]
requests it's got the responses back
from the tools um and then all you need
to do to make this a trainable sample is
you just remove the tips and at that
point you stop revealing the answer to
the model and this is a trace of how the
model should ideally go about finding
these um files in a code base and why it
should do the next thing as a function
of everything that it's done so far so
this has been an incredibly powerful
approach for us so far so to recap um
the custom reasoning traces are
extremely effective at increasing you
know model performance across difficult
tasks as I mentioned being that glue
that sticks like where you are starting
to where you want to be is like very
powerful um there is more performance to
be extracted from these even current
generation Frontier models by just
improving data set quality than trying
to iterate on a prompt iterating on a
prompt once you've already got it to
like 85 90% of it what it what you can
actually squeeze out of it is very hard
but increasing um data set quality is

[00:11]
easier if it's fully vow driven um
selfplay as I mentioned is extremely
effective for agentic based workflows
like if I was building any sort of agent
based thing I would be using it to
synthesize data to be able to train a
vertical specific agent for that thing
and the last Point as I mentioned it's
all in the data the model always learns
whatever you put in front of it
everything must be vow driven there is
like a 0 point something per chance that
the problem you're encountering is down
to the models architecture something
down like to the base model it's more
likely going to be an attribute that you
either have noticed or haven't noticed
in your training data so finally I will
show you a quick demo of Genie In Action
and I will hopefully have set this up
correctly perfect so over here you can
see this is the cosine web platform over
here let see if I can make this full
screen um this is the cosine web
platform over here and um to get started
uh by using Genie is very simple so
essentially you on board into the
platform um you you can either use a

[00:12]
personal account or create a team with
your colleagues and the first thing that
you just have to do is go in and connect
your GitHub um and once you've connected
your GitHub um organization is a GitHub
app to cosign so it's a couple of clicks
once you've done that you're then able
to select any repo in that GitHub orb
import it um into cosign as you'll see
here and once it's
imported what we'll start doing is we'll
start indexing your repo and what
indexing a repo actually means within
the context of cosign is we will fully
semantically embed your entire codebase
um we will generate a Keyword Index for
that codebase we'll run all the language
servers on that codebase and we have all
of this information available for Genie
to be able to pull from and do retrieval
so as I showed you the example earlier
Genie does retrieval in this sort of
looplike way it uses all these tools
under the hood in order to facilitate
that so once um we've made our initial
index that index is then kept up to date
with your main branch um and you can
also select other branches if you're
working on them as well so whenever you
make changes Genie knows about them now

[00:13]
actually getting Genie to do a task so
what I'm going to put in here this task
here is a a raw Sentry output it's like
completely like unedited um and this is
a prod error that came through for us a
couple of days ago and what we're going
to do is we're just going to give it to
Genie and ask it to uh to fix it
essentially so I'm getting this error in
Century just copied it straight off the
website and then we'll kick it off in
just a second um clearly thought this
would take more time than it did there
we go so we'll kick it off and then once
we've started that Genie will start
using those retrieval tools um to figure
out what it wants to do so here it's
come up with a plan it's said okay the
error points at this file I'm going to
go ahead and retrieve this file so it's
gone ahead and done that and once Genie
has like is comfortable that it's
written everything it needs it's read
everything it needs to read to do the
task it will write a patch in order to
do the task another benefit of
fine-tuning is that we can train the
model to Output in ways that it wouldn't

[00:14]
in a in a prompted instance so here we
wrote we trained Genie to write a
proprietary patch format that llms
actually like if you've ever gone down
that rabbit hole you know that's quite a
hard thing to pull off so once Genie has
written some code we'll then run your
GitHub CI automatically to see whether
your code has actually you know runs and
passes uh and this is the way that we
can go through that agentic Loop of
getting the response um the result of
your code execution and if it didn't
pass we can then continue erasing from
there the last point is that everything
that cosign and Genie does is
automatically mirrored in GitHub you can
go ahead and hop on branches that Genie
has made you can get Genie to hop on
branches that you've started um and as
you've seen here as soon as it was done
it opened a PR the files are exactly the
same it's written a description for the
pr here um and in fact in this instance
um it was good enough uh to actually
solve the problem so I'm just going to
go ahead and merge it straight away so
this is an example of you know Sentry
has come with a problem within two
minutes I've gone ahead and merged a fix
and G need did all the heavy LIF ing for
me this is a huge use case that we can

[00:15]
see going forward with Genie but Genie
is a um is a general model and this is
only one of the ways that we can see it
being used uh in the future thank you so
much for the time thank you for
listening

</details>
